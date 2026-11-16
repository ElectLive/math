"""Exact weighted-substitution orbits of alternating forms over F_5.

This verifies the finite orbit count used by the exponent-25 regular-top
manuscript. It does not verify the mathematical reduction from Bol folders.
Only the Python standard library is used; there are no external inputs.
"""

from collections import Counter
from itertools import product


PRIME = 5
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
IDENTITY = (1, 0, 0, 0)
GENERATORS = ((2, 0, 0, 0), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1))


def multiply(left, right):
    """Polynomial multiplication modulo t^5 over F_5."""
    result = [0] * 5
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            if i + j < 5:
                result[i + j] = (result[i + j] + x * y) % PRIME
    return tuple(result)


def substitution_columns(coefficients):
    """Columns of t^j -> (a1*t+...+a4*t^4)^j, j=1,...,4."""
    polynomial = (0,) + coefficients
    power = (1, 0, 0, 0, 0)
    columns = []
    for _ in range(4):
        power = multiply(power, polynomial)
        columns.append(power[1:])
    return tuple(columns)


def compose(left, right):
    """Return left(right(t)), modulo t^5."""
    columns = substitution_columns(right)
    return tuple(
        sum(left[j] * columns[j][i] for j in range(4)) % PRIME
        for i in range(4)
    )


def weighted_exterior_matrix(coefficients):
    """Matrix for beta -> a1^-1 * S^T beta S on its six entries."""
    columns = substitution_columns(coefficients)
    scale = pow(coefficients[0], -1, PRIME)
    return tuple(
        tuple(
            scale * (columns[i][k] * columns[j][ell]
                     - columns[i][ell] * columns[j][k]) % PRIME
            for k, ell in PAIRS
        )
        for i, j in PAIRS
    )


def apply(matrix, form):
    return tuple(sum(x * y for x, y in zip(row, form)) % PRIME for row in matrix)


def pfaffian(form):
    return (form[0] * form[5] - form[1] * form[4] + form[2] * form[3]) % PRIME


def main():
    substitutions = {
        (a1,) + rest
        for a1 in range(1, PRIME)
        for rest in product(range(PRIME), repeat=3)
    }
    generated = {IDENTITY}
    queue = [IDENTITY]
    for current in queue:
        for generator in GENERATORS:
            image = compose(current, generator)
            if image not in generated:
                generated.add(image)
                queue.append(image)
    assert generated == substitutions
    assert len(substitutions) == 500

    actions = tuple(weighted_exterior_matrix(s) for s in sorted(substitutions))
    forms = {f for f in product(range(PRIME), repeat=6) if pfaffian(f)}
    assert len(forms) == 12400
    remaining = set(forms)
    representatives = []
    sizes = Counter()
    while remaining:
        representative = min(remaining)
        orbit = {apply(action, representative) for action in actions}
        # Full group orbits must partition the nondegenerate forms.
        assert representative in orbit
        assert orbit <= remaining
        assert all(pfaffian(f) for f in orbit)
        assert 500 % len(orbit) == 0
        remaining.difference_update(orbit)
        representatives.append(representative)
        sizes[len(orbit)] += 1

    expected = {1: 4, 2: 8, 20: 4, 25: 12, 100: 20, 250: 40}
    assert dict(sizes) == expected
    assert len(representatives) == 88
    assert sum(size * count for size, count in sizes.items()) == len(forms)
    print("Substitution group: 500")
    print("Nondegenerate alternating forms: 12400")
    print("Full-group orbits: 88")
    print("Orbit sizes:", dict(sorted(sizes.items())))
    print("Scope: finite form orbits; the folder-isomorphism reduction is separate.")


if __name__ == "__main__":
    main()
