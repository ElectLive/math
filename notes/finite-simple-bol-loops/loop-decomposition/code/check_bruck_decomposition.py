#!/usr/bin/env python3
"""Exact supplementary diagnostics for bruck-extension-decomposition.md.

No dependency beyond Python 3.11. The finite computations do not prove the
general extension-rigidity or decomposition theorems.
"""

from __future__ import annotations

from itertools import product
import json


def rank(rows, width, p):
    """Incremental exact row rank over the prime field."""
    pivots = {}
    for source in rows:
        row = [x % p for x in source]
        for j in range(width):
            if not row[j]:
                continue
            if j in pivots:
                scale = row[j]
                row = [(a - scale * b) % p for a, b in zip(row, pivots[j])]
            else:
                scale = pow(row[j], -1, p)
                pivots[j] = [(scale * a) % p for a in row]
                break
    return len(pivots)


def nullspace(rows, width, p):
    data = [[x % p for x in row] for row in rows]
    pivots = []
    r = 0
    for col in range(width):
        pivot = next((i for i in range(r, len(data)) if data[i][col]), None)
        if pivot is None:
            continue
        data[r], data[pivot] = data[pivot], data[r]
        inv = pow(data[r][col], -1, p)
        data[r] = [(x * inv) % p for x in data[r]]
        for i in range(len(data)):
            if i != r and data[i][col]:
                factor = data[i][col]
                data[i] = [(a - factor * b) % p for a, b in zip(data[i], data[r])]
        pivots.append(col)
        r += 1
    free = [j for j in range(width) if j not in pivots]
    basis = []
    for j in free:
        v = [0] * width
        v[j] = 1
        for i, col in enumerate(pivots):
            v[col] = -data[i][j] % p
        basis.append(v)
    return basis


def alternating(n, z, entries, p):
    b = {}
    for i, j in product(range(n), repeat=2):
        b[i, j] = [0] * z
    for i, j, output in entries:
        b[i, j] = [x % p for x in output]
        b[j, i] = [-x % p for x in output]
    return b


def suspension(b, n, z, p):
    d = {}
    for i, j, k in product(range(n + 1), repeat=3):
        out = [0] * z
        if i == 0 and j and k:
            out = [(a + v) % p for a, v in zip(out, b[j - 1, k - 1])]
        if j == 0 and i and k:
            out = [(a - v) % p for a, v in zip(out, b[i - 1, k - 1])]
        if k == 0 and i and j:
            out = [(a - 2 * v) % p for a, v in zip(out, b[i - 1, j - 1])]
        d[i, j, k] = out
    return d


def centroid(tensor, n, z, arity, p):
    """Solve the complete balanced-centroid equations, no predicted shortcut."""
    width = n * n + z * z
    rows = []
    for indices in product(range(n), repeat=arity):
        for slot in range(arity):
            for output in range(z):
                row = [0] * width
                for j in range(n):
                    args = list(indices)
                    args[slot] = j
                    row[j * n + indices[slot]] += tensor[tuple(args)][output]
                for j in range(z):
                    row[n * n + output * z + j] -= tensor[indices][j]
                rows.append(row)
    return nullspace(rows, width, p)


def idempotents(basis, n, z, p):
    result = 0
    for coefficients in product(range(p), repeat=len(basis)):
        v = [sum(c * b[i] for c, b in zip(coefficients, basis)) % p
             for i in range(n * n + z * z)]
        valid = True
        for dim, offset in [(n, 0), (z, n * n)]:
            for i, j in product(range(dim), repeat=2):
                square = sum(v[offset + i * dim + k] * v[offset + k * dim + j]
                             for k in range(dim)) % p
                if square != v[offset + i * dim + j]:
                    valid = False
        result += valid
    return result


def direct_sum(d, n, z, p):
    out = {}
    for indices in product(range(2 * n), repeat=3):
        value = [0] * (2 * z)
        if all(i < n for i in indices):
            value[:z] = d[indices]
        elif all(i >= n for i in indices):
            value[z:] = d[tuple(i - n for i in indices)]
        out[indices] = value
    return out


def centroid_diagnostics():
    records = []
    for p in (2, 3, 5):
        edge = alternating(2, 1, [(0, 1, [1])], p)
        d_edge = suspension(edge, 2, 1, p)
        matching = alternating(4, 2, [(0, 1, [1, 0]), (2, 3, [0, 1])], p)
        scalar = alternating(4, 1, [(0, 1, [1]), (2, 3, [1])], p)
        star = alternating(4, 3, [
            (0, 1, [1, 0, 0]), (0, 2, [0, 1, 0]), (0, 3, [0, 0, 1])], p)
        cases = [
            ("one_edge", edge, 2, 1, 1),
            ("two_edge_graph", matching, 4, 2, 2),
            ("shared_output_symplectic", scalar, 4, 1, 1),
            ("three_leaf_star", star, 4, 3, 1),
        ]
        for name, b, n, z, bdim in cases:
            bc = centroid(b, n, z, 2, p)
            dc = centroid(suspension(b, n, z, p), n + 1, z, 3, p)
            assert len(bc) == bdim
            assert len(dc) == 1
            assert idempotents(dc, n + 1, z, p) == 2
            records.append({"p": p, "case": name, "bilinear_centroid_dimension": len(bc),
                            "associator_centroid_dimension": len(dc)})
        dd = direct_sum(d_edge, 3, 1, p)
        dc = centroid(dd, 6, 2, 3, p)
        assert len(dc) == 2
        assert idempotents(dc, 6, 2, p) == 4
        records.append({"p": p, "case": "direct_product_of_two_edge_loops",
                        "associator_centroid_dimension": 2, "idempotents": 4})
    return records


def factor_set_diagnostics(p, dim):
    """Solve all normalized scalar factor sets in small quotient dimensions."""
    vectors = list(product(range(p), repeat=dim))
    zero = (0,) * dim
    nonzero = [v for v in vectors if v != zero]
    pairs = {(u, v): i for i, (u, v) in enumerate(product(nonzero, repeat=2))}
    width = len(pairs)

    def add(u, v):
        return tuple((a + b) % p for a, b in zip(u, v))

    def mul(c, u):
        return tuple(c * a % p for a in u)

    def row(terms):
        out = [0] * width
        for coefficient, u, v in terms:
            if u != zero and v != zero:
                out[pairs[u, v]] += coefficient
        return out

    constraints = []
    for u in vectors:
        constraints.append(row([(1, u, mul(-1, u))]))
        constraints.append(row([(1, mul(j, u), u) for j in range(p)]))
    for u, v in product(vectors, repeat=2):
        constraints.append(row([(1, mul(-1, u), mul(-1, v)), (1, u, v)]))
    for x, y, z in product(vectors, repeat=3):
        constraints.append(row([
            (1, x, z), (1, y, add(x, z)), (1, x, add(add(x, y), z)),
            (-1, y, x), (-1, x, add(x, y)), (-1, add(mul(2, x), y), z)]))
    r = rank(constraints, width, p)
    associator_rows = []
    for x, y, z in product(vectors, repeat=3):
        associator_rows.append(row([
            (1, x, y), (1, add(x, y), z), (-1, y, z), (-1, x, add(y, z))]))
    rk = rank(constraints + associator_rows, width, p)
    kernel_dimension = width - rk
    expected = ((len(vectors) - 1) if p == 2 else (len(vectors) - 1) // 2) - dim
    assert kernel_dimension == expected
    return {"p": p, "quotient_dimension": dim, "factor_set_variables": width,
            "Bruck_exponent_p_solution_dimension": width - r,
            "zero_associator_kernel_dimension": kernel_dimension,
            "inverse_compatible_coboundary_dimension": expected}


def fiber_product_diagnostic(p):
    # Two independent edge coordinates; common marker. Then identify the centers.
    vectors = list(product(range(p), repeat=5))

    def mul(x, y):
        a, u1, u2, u3, u4 = x
        b, v1, v2, v3, v4 = y
        central = ((a + 2 * b) * (u1 * v2 - u2 * v1) % p,
                   (a + 2 * b) * (u3 * v4 - u4 * v3) % p)
        return tuple((s + t) % p for s, t in zip(x, y)), central

    checks = 0
    # Central shifts cancel identically, so all quotient-coordinate pairs suffice.
    for x, y in product(vectors, repeat=2):
        _, c = mul(x, y)
        a, u1, u2, u3, u4 = x
        b, v1, v2, v3, v4 = y
        c1 = (a + 2 * b) * (u1 * v2 - u2 * v1) % p
        c2 = (a + 2 * b) * (u3 * v4 - u4 * v3) % p
        assert c == (c1, c2)
        assert sum(c) % p == ((a + 2 * b)
               * (u1 * v2 - u2 * v1 + u3 * v4 - u4 * v3)) % p
        checks += 1
    return {"p": p, "all_quotient_product_pairs": checks,
            "central_quotient_kernel_order": p}


def ring_obstruction():
    p = 4
    vectors = list(product(range(4), repeat=3))

    def b(u, v):
        return 2 * (u[0] * v[1] - u[1] * v[0]) % 4

    def d(x, y, z):
        a, *u = x
        c, *v = y
        e, *w = z
        return (a * b(v, w) - c * b(u, w) - 2 * e * b(u, v)) % p

    nuclear = []
    values = set()
    for u in vectors:
        good = True
        for v, w in product(vectors, repeat=2):
            dv = (d(u, v, w), d(v, u, w), d(v, w, u))
            values.update(dv)
            if any(dv):
                good = False
        if good:
            nuclear.append(u)
    assert len(nuclear) == 8
    assert values == {0, 2}
    # Four central-coordinate choices, two of which are killed by doubling.
    assert len(nuclear) * 4 == 32
    assert len(nuclear) * 2 == 16
    return {"loop_order": 256, "center_order": 32, "associator_order": 2,
            "center_2_torsion_order": 16, "center_mod_associator_order": 16}


def main():
    print(json.dumps({
        "centroid_cases": centroid_diagnostics(),
        "extension_rigidity_small_systems": [
            factor_set_diagnostics(2, 2), factor_set_diagnostics(2, 3),
            factor_set_diagnostics(3, 2)],
        "fiber_product_cases": [fiber_product_diagnostic(2), fiber_product_diagnostic(3)],
        "Z4_obstruction": ring_obstruction(),
        "scope": "Exact bounded diagnostics, supplementary to the general proofs."
    }, sort_keys=True))


if __name__ == "__main__":
    main()
