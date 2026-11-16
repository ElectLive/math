r"""Targeted `#0323/S1` structural & geometric obstruction experiments.

Implements four exact computational tests supporting the O'Nan-Scott / rank >= 3 elimination:
  1. **Positive Rank-3 Moufang Control (`M(2)`)**: Constructs Paige's simple Moufang loop `M(2)`
     of order 120 (unit Zorn vector-matrices over F_2), verifying that `bol_engine.py` certifies
     `is_moufang=True`, `is_simple=True`, `|Mlt(M(2))| = 174,182,400 = |Omega_8^+(2)|`, and
     `rank(Mlt(M(2))) = 3` with subdegrees `(1, 56, 63)` (confirming Moufang exclusion in #0323/S1
     is essential and that our engine detects rank > 2 whenever present).
  2. **O'Nan-Scott `SD_2` Single-x Class Filter on `T = A_6` (`n = 360`, `|Aut(A_6)| = 1440`)**:
     Tests all `(beta, eps) in Aut(A_6) x {+1, -1}` (`2,880` maps) on every `x in A_6 \ {1}`
     against `x * beta(y^eps) * y^{-1} in x^{Aut(A_6)} cup (x^{-1})^{Aut(A_6)}` for all `y in A_6`.
  3. **Lemma 3.2(a) Uniform Orbital Displacement (UOD) Census Across Rank >= 3 Primitive `AS` Groups**:
     Tests existence of coset elements `g in P` (`g(0) = x`) satisfying `(y, g(y)) in Gamma_P(0, x)`
     for all `y in Omega` across Johnson, Grassmannian, dihedral-coset, and classical rank-3 polar
     / orthogonal geometries (`O_6^+(2)`, `O_6^-(2)`, `PSp_4(3)`, `Sp_6(2)`, and `Omega_8^+(2)`).
  4. **S_8 on unordered 4+4 partitions**: checks all 21 nonidentity cycle types against
     every one of the 35 partitions, certifying nonuniform orbital displacement.
"""

from __future__ import annotations

import itertools
import time
from typing import Dict, List, Sequence, Set, Tuple

from bol_engine import Loop
from perm_group import Perm, PermGroup, compose, compute_orbits, cycles_to_perm, invert


# ======================================================================
# 1. Paige's Simple Moufang Loop M(2) of Order 120 (Rank-3 Positive Control)
# ======================================================================


def build_paige_moufang_m2() -> Loop:
    """Construct Paige's smallest finite simple nonassociative Moufang loop M(2) of order 120.

    Elements are 8-tuples (a, d, u0, u1, u2, v0, v1, v2) in F_2^8 with hyperbolic determinant
        a*d + u0*v0 + u1*v1 + u2*v2 == 1 (mod 2).
    Over F_2, -1 == 1 so {+I, -I} = {I} has size 1, giving 120 elements directly with
    identity I = (1, 1, 0, 0, 0, 0, 0, 0).
    """
    id_vec = (1, 1, 0, 0, 0, 0, 0, 0)
    elems: List[Tuple[int, ...]] = [id_vec]
    for vec in itertools.product((0, 1), repeat=8):
        if vec == id_vec:
            continue
        a, d, u0, u1, u2, v0, v1, v2 = vec
        det = (a * d + u0 * v0 + u1 * v1 + u2 * v2) & 1
        if det == 1:
            elems.append(vec)
    assert len(elems) == 120
    to_idx = {v: i for i, v in enumerate(elems)}

    def cross_f2(x0: int, x1: int, x2: int, y0: int, y1: int, y2: int) -> Tuple[int, int, int]:
        return (
            (x1 * y2 ^ x2 * y1) & 1,
            (x2 * y0 ^ x0 * y2) & 1,
            (x0 * y1 ^ x1 * y0) & 1,
        )

    tbl: List[List[int]] = [[0] * 120 for _ in range(120)]
    for i, (a1, d1, u10, u11, u12, v10, v11, v12) in enumerate(elems):
        row = tbl[i]
        for j, (a2, d2, u20, u21, u22, v20, v21, v22) in enumerate(elems):
            uv = (u10 * v20 ^ u11 * v21 ^ u12 * v22) & 1
            vu = (v10 * u20 ^ v11 * u21 ^ v12 * u22) & 1
            a_new = (a1 * a2 ^ uv) & 1
            d_new = (d1 * d2 ^ vu) & 1
            vv0, vv1, vv2 = cross_f2(v10, v11, v12, v20, v21, v22)
            uu0, uu1, uu2 = cross_f2(u10, u11, u12, u20, u21, u22)
            u_new = (
                (a1 * u20 ^ d2 * u10 ^ vv0) & 1,
                (a1 * u21 ^ d2 * u11 ^ vv1) & 1,
                (a1 * u22 ^ d2 * u12 ^ vv2) & 1,
            )
            v_new = (
                (d1 * v20 ^ a2 * v10 ^ uu0) & 1,
                (d1 * v21 ^ a2 * v11 ^ uu1) & 1,
                (d1 * v22 ^ a2 * v12 ^ uu2) & 1,
            )
            row[j] = to_idx[(a_new, d_new, *u_new, *v_new)]
    return Loop(tbl, name="Paige_Moufang_M(2)_ord120")


def run_part1_paige_control() -> Loop:
    print("\n" + "=" * 78)
    print("PART 1: PAIGE SIMPLE MOUFANG LOOP M(2) RANK-3 POSITIVE CONTROL (n = 120)")
    print("=" * 78)
    t0 = time.time()
    m2 = build_paige_moufang_m2()
    rep = m2.analyze(check_op_iso=False)
    print(f"  Name: {rep['name']} (time={time.time()-t0:.2f}s)")
    print(
        f"  left_bol={rep['is_left_bol']} right_bol={rep['is_right_bol']} "
        f"moufang={rep['is_moufang']} proper_left_bol={rep['is_proper_left_bol']} "
        f"assoc={rep['is_associative']} simple={rep['is_simple']}"
    )
    print(
        f"  |LMlt|={rep['LMlt_order']} rank(LMlt)={rep['LMlt_rank']} subdeg={rep['LMlt_subdegrees']}"
    )
    print(
        f"  |RMlt|={rep['RMlt_order']} rank(RMlt)={rep['RMlt_rank']} subdeg={rep['RMlt_subdegrees']}"
    )
    print(
        f"  |Mlt| ={rep['Mlt_order']} (= |Omega_8^+(2)|!) RANK(Mlt)={rep['Mlt_rank']} subdeg={rep['Mlt_subdegrees']}"
    )
    assert rep["is_moufang"] is True
    assert rep["is_proper_left_bol"] is False
    assert rep["is_simple"] is True
    assert rep["Mlt_order"] == 174182400
    assert rep["Mlt_rank"] == 3
    assert rep["Mlt_subdegrees"] == (1, 56, 63)
    return m2


# ======================================================================
# 2. Exact SD_2 Single-x Class Filter on T = A_6 (n = 360, |Aut(A_6)| = 1440)
# ======================================================================


def run_part2_sd2_a6_filter() -> None:
    print("\n" + "=" * 78)
    print("PART 2: EXACT O'NAN-SCOTT SD_2 SINGLE-x FILTER ON T = A_6 (|Aut| = 1440)")
    print("=" * 78)
    t0 = time.time()

    # Construct PSL(2, 9) ~= A_6 (360) normal inside PGammaL(2, 9) ~= Aut(A_6) (1440) on P^1(F_9) (deg 10)
    pts = [(c0, c1) for c1 in range(3) for c0 in range(3)]
    to_i = {v: i for i, v in enumerate(pts)}

    def add9(i: int, j: int) -> int:
        return to_i[((pts[i][0] + pts[j][0]) % 3, (pts[i][1] + pts[j][1]) % 3)]

    def mul9(i: int, j: int) -> int:
        a0, a1 = pts[i]
        b0, b1 = pts[j]
        return to_i[((a0 * b0 + a1 * b1) % 3, (a0 * b1 + a1 * b0 + a1 * b1) % 3)]

    def neg9(i: int) -> int:
        return to_i[((-pts[i][0]) % 3, (-pts[i][1]) % 3)]

    def frob9(i: int) -> int:
        return mul9(i, mul9(i, i))

    deg = 10
    inf = 9
    alpha = to_i[(0, 1)]
    alpha2 = mul9(alpha, alpha)
    t1 = tuple(add9(x, to_i[(1, 0)]) if x < 9 else inf for x in range(deg))
    ta = tuple(add9(x, alpha) if x < 9 else inf for x in range(deg))
    ma2 = tuple(mul9(alpha2, x) if x < 9 else inf for x in range(deg))
    inv_l = [0] * deg
    inv_l[0], inv_l[inf] = inf, 0
    for x in range(1, 9):
        for y in range(1, 9):
            if mul9(x, y) == to_i[(1, 0)]:
                inv_l[x] = neg9(y)
                break
    s_inv = tuple(inv_l)
    ma = tuple(mul9(alpha, x) if x < 9 else inf for x in range(deg))
    fr = tuple(frob9(x) if x < 9 else inf for x in range(deg))

    id_p = tuple(range(deg))
    T_raw = PermGroup(deg, [t1, ta, ma2, s_inv], allow_jordan_fastpath=False).enumerate_elements()
    Aut_raw = PermGroup(
        deg, [t1, ta, ma2, s_inv, ma, fr], allow_jordan_fastpath=False
    ).enumerate_elements()
    assert len(T_raw) == 360 and len(Aut_raw) == 1440

    T_elems = [id_p] + [g for g in T_raw if g != id_p]
    t_idx = {g: i for i, g in enumerate(T_elems)}
    m = 360

    mul_T = [[t_idx[compose(T_elems[i], T_elems[j])] for j in range(m)] for i in range(m)]
    inv_T = [t_idx[invert(T_elems[i])] for i in range(m)]

    # Action of every alpha in Aut_raw by conjugation on T_elems (gives all 1440 automorphisms of A_6!)
    aut_maps: List[Tuple[int, ...]] = []
    for g in Aut_raw:
        gi = invert(g)
        aut_maps.append(
            tuple(t_idx[compose(g, compose(T_elems[x], gi))] for x in range(m))
        )
    assert len(set(aut_maps)) == 1440

    # Partition T \ {0} into Aut(A_6)-orbits (note in A_6 every element is Aut-conjugate to its inverse,
    # still we union orb(x) | orb(x^-1) explicitly!)
    aut_orbit_mask = [0] * m
    rep_per_orbit: List[int] = []
    visited = [False] * m
    visited[0] = True
    for x in range(1, m):
        if not visited[x]:
            rep_per_orbit.append(x)
            orb_set = {am[x] for am in aut_maps}
            orb_inv_set = {am[inv_T[x]] for am in aut_maps}
            union_mask = 0
            for u in orb_set | orb_inv_set:
                union_mask |= 1 << u
            for u in orb_set:
                visited[u] = True
                aut_orbit_mask[u] = union_mask

    id_aut = tuple(range(m))
    extra_solutions = 0
    for x in range(1, m):
        allowed_mask = aut_orbit_mask[x]
        ix = inv_T[x]
        # Associative solution 1: (id_aut, +1) -> L_x(y) = x * y
        # Associative solution 2: (conj_{x^-1}, +1) -> L_x(y) = x * (x^-1 * y * x) = y * x
        conj_ix = tuple(mul_T[mul_T[ix][y]][x] for y in range(m))
        row_x = mul_T[x]

        for beta in aut_maps:
            # Test eps = +1: x * beta[y] * y^-1 in allowed_mask for all y
            ok_pos = True
            for y in range(1, m):
                val = mul_T[row_x[beta[y]]][inv_T[y]]
                if not ((allowed_mask >> val) & 1):
                    ok_pos = False
                    break
            if ok_pos and beta != id_aut and beta != conj_ix:
                extra_solutions += 1

            # Test eps = -1: x * beta[y^-1] * y^-1 in allowed_mask for all y
            ok_neg = True
            for y in range(1, m):
                val = mul_T[row_x[beta[inv_T[y]]]][inv_T[y]]
                if not ((allowed_mask >> val) & 1):
                    ok_neg = False
                    break
            if ok_neg:
                extra_solutions += 1

    print(
        f"  Tested all 359 nonzero x in A_6 x 2,880 (beta, eps) pairs in Aut(A_6) x {{+1,-1}} ({time.time()-t0:.2f}s):"
    )
    print(
        f"  Non-associative surviving (x, beta, eps) triples = {extra_solutions} (ONLY id and conj_{{x^-1}} with eps=+1 survive!)"
    )
    assert extra_solutions == 0


# ======================================================================
# 3. Lemma 3.2(a) Uniform Orbital Displacement (UOD) Across Rank >= 3 AS Groups
# ======================================================================


def check_uod_on_group(name: str, n: int, gens: Sequence[Perm]) -> Dict[str, object]:
    """Compute rank, subdegrees, and exact UOD count in one representative coset of EVERY
    nontrivial suborbit Delta_i (i = 1..r-1) for primitive group P = <gens> on {0..n-1}.
    """
    pg = PermGroup(n, gens, initial_base=[0], allow_jordan_fastpath=False)
    assert pg.is_primitive(), f"{name} is not primitive!"
    sub_orbs = sorted(pg.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o), o[0]))
    r = len(sub_orbs)
    orb_id = [0] * n
    for idx, o in enumerate(sub_orbs):
        for pt in o:
            orb_id[pt] = idx

    # Transversal u_inv[u] mapping u -> 0 in P
    tr_inv = pg.trans_inv[0]
    color = [[orb_id[tr_inv[u][v]] for v in range(n)] for u in range(n)]

    # Enumerate stabilizer P_0
    p0_pg = pg.stabilizer(0)
    p0_elems = p0_pg.enumerate_elements(limit=100000)

    uod_counts: List[Tuple[int, int]] = []
    for idx in range(1, r):
        x = sub_orbs[idx][0]
        g0 = pg.trans[0][x]  # maps 0 -> x
        cnt = 0
        for h in p0_elems:
            # g = g0 o h maps 0 -> g0(h(0)) = g0(0) = x
            ok = True
            for y in range(n):
                if color[y][g0[h[y]]] != idx:
                    ok = False
                    break
            if ok:
                cnt += 1
        uod_counts.append((len(sub_orbs[idx]), cnt))

    all_nonzero = all(c > 0 for _, c in uod_counts)
    return {
        "name": name,
        "degree": n,
        "order": pg.order(),
        "rank": r,
        "uod_by_suborbit": uod_counts,
        "passes_lemma_3_2a": all_nonzero,
    }


def _induced_kset_action(m: int, k: int, base_gens: Sequence[Perm]) -> Tuple[int, List[Perm]]:
    ksets = list(itertools.combinations(range(m), k))
    to_i = {s: i for i, s in enumerate(ksets)}
    gens_out = [
        tuple(to_i[tuple(sorted(g[x] for x in s))] for s in ksets) for g in base_gens
    ]
    return len(ksets), gens_out


def _induced_coset_action(
    deg: int, G_gens: Sequence[Perm], H_gens: Sequence[Perm]
) -> Tuple[int, List[Perm]]:
    """Left-coset action of G = <G_gens> on G / H (H = <H_gens>)."""
    G_el = PermGroup(deg, G_gens, allow_jordan_fastpath=False).enumerate_elements()
    H_el = set(PermGroup(deg, H_gens, allow_jordan_fastpath=False).enumerate_elements())
    id_p = tuple(range(deg))
    cosets: List[frozenset[Perm]] = [frozenset(H_el)]
    seen = set(H_el)
    for g in G_el:
        if g not in seen:
            cs = frozenset(compose(g, h) for h in H_el)
            cosets.append(cs)
            seen.update(cs)
    elem_to_coset: Dict[Perm, int] = {}
    for idx, cs in enumerate(cosets):
        for x in cs:
            elem_to_coset[x] = idx
    reps = [id_p] + [next(iter(cs)) for cs in cosets[1:]]
    gens_out = [tuple(elem_to_coset[compose(g, r)] for r in reps) for g in G_gens]
    return len(cosets), gens_out


def _build_f2_orthogonal_or_symplectic(
    dim: int, mode: str, point_kind: str
) -> Tuple[int, List[Perm]]:
    """Construct orthogonal / symplectic group over F_2 on nonsingular or nonzero isotropic points!
    `mode`:
      - 'O+'  : Q(x) = x0*x1 + x2*x3 + ...
      - 'O-'  : Q(x) = x0*x1 + ... + (x_{d-2}^2 + x_{d-2}*x_{d-1} + x_{d-1}^2)
      - 'Sp'  : symplectic form B(x,y) = sum (x_{2i}*y_{2i+1} + x_{2i+1}*y_{2i}), all nonzero vectors
    `point_kind`: 'nonsingular' (Q=1), 'singular' (Q=0, x!=0), or 'nonzero' (for Sp).
    Generated by all symplectic transvections / orthogonal reflections v -> v + B(v, a)*a!
    """
    vecs = [v for v in range(1, 1 << dim)]

    def b_form(x: int, y: int) -> int:
        acc = 0
        for i in range(0, dim, 2):
            x0, x1 = (x >> i) & 1, (x >> (i + 1)) & 1
            y0, y1 = (y >> i) & 1, (y >> (i + 1)) & 1
            acc ^= (x0 & y1) ^ (x1 & y0)
        return acc

    def q_form(x: int) -> int:
        acc = 0
        pairs = (dim // 2) if mode == "O+" else (dim // 2 - 1)
        for i in range(pairs):
            acc ^= ((x >> (2 * i)) & 1) & ((x >> (2 * i + 1)) & 1)
        if mode == "O-":
            u = (x >> (dim - 2)) & 1
            v = (x >> (dim - 1)) & 1
            acc ^= u ^ (u & v) ^ v
        return acc

    if point_kind == "nonsingular":
        pts = [v for v in vecs if q_form(v) == 1]
    elif point_kind == "singular":
        pts = [v for v in vecs if q_form(v) == 0]
    else:
        pts = vecs

    to_i = {v: idx for idx, v in enumerate(pts)}

    # Reflections / transvections:
    # For Sp: t_a(x) = x ^ (B(x, a) * a) for a in vecs (generates Sp(dim, 2))
    # For O+/O-: r_a(x) = x ^ (B(x, a) * a) for nonsingular a (Q(a) == 1) preserves Q!
    # Verify: Q(x ^ a) = Q(x) ^ Q(a) ^ B(x, a); if B(x,a)==1 and Q(a)==1, Q(x^a) = Q(x) ^ 1 ^ 1 = Q(x)!
    refl_centers = [a for a in vecs if (mode == "Sp" or q_form(a) == 1)]
    # Keep a small generating set of reflections
    full_perms: List[Perm] = []
    for a in refl_centers:
        p = tuple(to_i[x ^ a] if b_form(x, a) == 1 else to_i[x] for x in pts)
        full_perms.append(p)

    # Also build simple commutator subgroup Omega_dim^{+/-}(2) = < r_a o r_b > if needed
    return len(pts), full_perms


def _build_psp4_3_isotropic_40() -> Tuple[int, List[Perm]]:
    """Construct PSp_4(3) (order 25,920) on the 40 projective points of PG(3, 3) (rank 3: 1, 12, 27)!
    Note: in PG(3, 3), EVERY 1-dimensional subspace is isotropic for the symplectic form,
    so PSp_4(3) acts primitively of rank 3 on all (3^4 - 1)/2 = 40 points of PG(3, 3)!
    """
    # Normalize projective points in F_3^4 \ {0} by first nonzero coordinate == 1
    pts: List[Tuple[int, int, int, int]] = []
    for v in itertools.product(range(3), repeat=4):
        if v == (0, 0, 0, 0):
            continue
        for c in v:
            if c != 0:
                if c == 1:
                    pts.append(v)
                break
    assert len(pts) == 40
    to_i = {v: idx for idx, v in enumerate(pts)}

    def norm_v(v: Tuple[int, int, int, int]) -> int:
        for c in v:
            if c != 0:
                inv_c = 1 if c == 1 else 2
                nv = tuple((x * inv_c) % 3 for x in v)
                return to_i[nv]
        raise ValueError("zero vector")

    # Symplectic form B(x, y) = x0*y1 - x1*y0 + x2*y3 - x3*y2 (mod 3)
    # Symplectic transvections: x -> x + B(x, a) * a for nonzero a in pts!
    def b_f3(x: Tuple[int, int, int, int], a: Tuple[int, int, int, int]) -> int:
        return (x[0] * a[1] - x[1] * a[0] + x[2] * a[3] - x[3] * a[2]) % 3

    gens: List[Perm] = []
    for a in pts:
        p = tuple(
            norm_v(tuple((x[k] + b_f3(x, a) * a[k]) % 3 for k in range(4)))
            for x in pts
        )
        gens.append(p)
    return 40, gens


def run_part3_rank3_as_census(m2_loop: Loop) -> None:
    print("\n" + "=" * 78)
    print("PART 3: LEMMA 3.2(a) UNIFORM ORBITAL DISPLACEMENT CENSUS ON RANK >= 3 AS GROUPS")
    print("=" * 78)

    cases: List[Tuple[str, int, List[Perm]]] = []

    # 1. Johnson actions A_8, S_8 on 2-sets (deg 28), A_9, S_9 on 2-sets (deg 36), A_7, S_7 on 3-sets (deg 35)
    a8_8 = [cycles_to_perm(8, [[0, 1, 2]]), cycles_to_perm(8, [[1, 2, 3, 4, 5, 6, 7]])]
    s8_8 = [cycles_to_perm(8, [[0, 1]]), cycles_to_perm(8, [[0, 1, 2, 3, 4, 5, 6, 7]])]
    cases.append(("A_8 on 2-sets (deg 28)", *_induced_kset_action(8, 2, a8_8)))
    cases.append(("S_8 on 2-sets (deg 28)", *_induced_kset_action(8, 2, s8_8)))

    a9_9 = [cycles_to_perm(9, [[0, 1, 2]]), cycles_to_perm(9, [[0, 1, 2, 3, 4, 5, 6, 7, 8]])]
    s9_9 = [cycles_to_perm(9, [[0, 1]]), cycles_to_perm(9, [[0, 1, 2, 3, 4, 5, 6, 7, 8]])]
    cases.append(("A_9 on 2-sets (deg 36)", *_induced_kset_action(9, 2, a9_9)))
    cases.append(("S_9 on 2-sets (deg 36)", *_induced_kset_action(9, 2, s9_9)))

    a7_7 = [cycles_to_perm(7, [[0, 1, 2]]), cycles_to_perm(7, [[0, 1, 2, 3, 4, 5, 6]])]
    s7_7 = [cycles_to_perm(7, [[0, 1]]), cycles_to_perm(7, [[0, 1, 2, 3, 4, 5, 6]])]
    cases.append(("A_7 on 3-sets (deg 35)", *_induced_kset_action(7, 3, a7_7)))
    cases.append(("S_7 on 3-sets (deg 35)", *_induced_kset_action(7, 3, s7_7)))

    # 1b. Maximal dihedral coset actions: PGL(2,7)/D_12 (deg 28) & PSL(2,11)/D_12 (deg 55)
    pgl2_7_g = [
        cycles_to_perm(8, [[0, 1, 2, 3, 4, 5, 6]]),
        (0, 3, 6, 2, 5, 1, 4, 7),
        (7, 6, 3, 2, 5, 4, 1, 0),
    ]
    d12_pgl27 = [(0, 3, 6, 2, 5, 1, 4, 7), (7, 6, 3, 2, 5, 4, 1, 0)]
    cases.append(("PGL(2,7) on D_12 cosets (deg 28)", *_induced_coset_action(8, pgl2_7_g, d12_pgl27)))

    psl2_11_g = [
        cycles_to_perm(12, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]),
        cycles_to_perm(12, [[1, 4, 5, 9, 3], [2, 8, 10, 7, 6]]),
        cycles_to_perm(12, [[0, 11], [1, 10], [2, 5], [3, 7], [4, 8], [6, 9]]),
    ]

    def _mob11(a: int, b: int, c: int, d: int) -> Perm:
        out: List[int] = []
        for z in range(12):
            if z == 11:
                num, den = a % 11, c % 11
            else:
                num, den = (a * z + b) % 11, (c * z + d) % 11
            out.append(11 if den == 0 else (num * pow(den, 9, 11)) % 11)
        return tuple(out)

    # D_12 < PSL(2,11): A = [[8, 5], [6, 8]] (ord 6 in PSL(2,11)), B = [[3, 1], [1, 8]] (ord 2, B A B = A^-1)
    d12_psl211 = [_mob11(8, 5, 6, 8), _mob11(3, 1, 1, 8)]
    cases.append(("PSL(2,11) on D_12 cosets (deg 55)", *_induced_coset_action(12, psl2_11_g, d12_psl211)))

    # 2. Classical 6-dim orthogonal & symplectic polar actions over F_2 (and simple Omega_6 subgroups!)
    n_o6p_ns, g_o6p_ns = _build_f2_orthogonal_or_symplectic(6, "O+", "nonsingular")
    g_om6p_ns = [compose(g_o6p_ns[0], g) for g in g_o6p_ns[1:]]
    cases.append(("Omega_6^+(2) nonsing (deg 28)", n_o6p_ns, g_om6p_ns))
    cases.append(("O_6^+(2) nonsing (deg 28)", n_o6p_ns, g_o6p_ns))

    n_o6p_sg, g_o6p_sg = _build_f2_orthogonal_or_symplectic(6, "O+", "singular")
    g_om6p_sg = [compose(g_o6p_sg[0], g) for g in g_o6p_sg[1:]]
    cases.append(("Omega_6^+(2)~=PSL(4,2) PGlines (deg 35)", n_o6p_sg, g_om6p_sg))
    cases.append(("O_6^+(2) singular (deg 35)", n_o6p_sg, g_o6p_sg))

    n_o6m_sg, g_o6m_sg = _build_f2_orthogonal_or_symplectic(6, "O-", "singular")
    g_om6m_sg = [compose(g_o6m_sg[0], g) for g in g_o6m_sg[1:]]
    cases.append(("Omega_6^-(2)~=PSU(4,2) isotrop (deg 27)", n_o6m_sg, g_om6m_sg))
    cases.append(("O_6^-(2) isotrop (deg 27)", n_o6m_sg, g_o6m_sg))

    n_o6m_ns, g_o6m_ns = _build_f2_orthogonal_or_symplectic(6, "O-", "nonsingular")
    g_om6m_ns = [compose(g_o6m_ns[0], g) for g in g_o6m_ns[1:]]
    cases.append(("Omega_6^-(2)~=PSU(4,2) nonsing (deg 36)", n_o6m_ns, g_om6m_ns))
    cases.append(("O_6^-(2) nonsing (deg 36)", n_o6m_ns, g_o6m_ns))

    # 3. Symplectic PSp_4(3) on 40 points of PG(3,3) (rank 3: 1, 12, 27) & Sp_6(2) on 63 points (rank 3: 1, 30, 32)
    _, all_psp43 = _build_psp4_3_isotropic_40()
    cases.append(("PSp_4(3) on PG(3,3) (deg 40)", 40, all_psp43))
    n_sp6, g_sp6 = _build_f2_orthogonal_or_symplectic(6, "Sp", "nonzero")
    cases.append(("Sp_6(2) on F_2^6\\{0} (deg 63)", n_sp6, g_sp6))

    header = f"{'Primitive AS Action':<40} | {'deg':>3} | {'|P|':>9} | {'rk':>2} | {'UOD per suborbit (size: count)':<30} | {'Pass?'}"
    print(header)
    print("-" * len(header))

    for label, deg, gens in cases:
        t0 = time.time()
        res = check_uod_on_group(label, deg, gens)
        uod_str = ", ".join(f"{sz}:{cnt}" for sz, cnt in res["uod_by_suborbit"])  # type: ignore[attr-defined]
        print(
            f"{label:<40} | {deg:>3} | {res['order']:>9} | {res['rank']:>2} | {uod_str:<30} | {res['passes_lemma_3_2a']} ({time.time()-t0:.2f}s)"
        )

    # Finally verify directly on Paige M(2) inside Mlt(M(2)) = Omega_8^+(2) (deg 120, rank 3: 1, 56, 63)
    # that every L_x and R_x of M(2) IS a genuine UOD element on its suborbit!
    mlt_m2 = m2_loop.Mlt()
    sub_orbs = sorted(mlt_m2.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o)))
    orb_id = [0] * 120
    for idx, o in enumerate(sub_orbs):
        for pt in o:
            orb_id[pt] = idx
    tr_inv = mlt_m2.trans_inv[0]
    color = [[orb_id[tr_inv[u][v]] for v in range(120)] for u in range(120)]
    ok_l = all(
        color[y][m2_loop.L[x][y]] == orb_id[x] for x in range(1, 120) for y in range(120)
    )
    ok_r = all(
        color[y][m2_loop.R[x][y]] == orb_id[x] for x in range(1, 120) for y in range(120)
    )
    print(
        f"\n  [Positive check] Omega_8^+(2) on M(2) (deg 120, |P|=174,182,400, rk=3, suborbits 56 & 63): "
        f"all 119 L_x UOD = {ok_l}, all 119 R_x UOD = {ok_r}!"
    )
    assert ok_l and ok_r


def test_s8_unordered_four_four_partitions() -> None:
    """Certify that no nonidentity S8 element has uniform displacement.

    Cycle type determines conjugacy in S8; conjugation permutes the 35
    unordered partitions and preserves their intersection invariant. Hence one
    representative of every integer partition of 8 covers every group element.
    """
    def integer_partitions(total: int, maximum: int):
        if total == 0:
            yield ()
            return
        for length in range(min(total, maximum), 0, -1):
            for tail in integer_partitions(total - length, length):
                yield (length,) + tail

    # Choosing the unique block containing 0 represents each unordered pair once.
    blocks = [frozenset(c) for c in itertools.combinations(range(8), 4) if 0 in c]
    types = list(integer_partitions(8, 8))
    assert len(blocks) == 35 and len(types) == 22
    checked = 0
    for cycle_type in types:
        permutation = list(range(8))
        start = 0
        for length in cycle_type:
            for i in range(length):
                permutation[start + i] = start + (i + 1) % length
            start += length
        if cycle_type == (1,) * 8:
            continue
        distances = set()
        for block in blocks:
            image = {permutation[i] for i in block}
            overlap = len(block & image)
            distances.add(min(overlap, 4 - overlap))
        assert len(distances) >= 2, (cycle_type, distances)
        checked += 1
    assert checked == 21
    print("[PASS] S8 4+4 partitions: 21 nonidentity cycle types, 35 partitions each")


def main() -> None:
    t_all = time.time()
    test_s8_unordered_four_four_partitions()
    m2 = run_part1_paige_control()
    run_part2_sd2_a6_filter()
    run_part3_rank3_as_census(m2)
    print(f"\nTotal #0323/S1 obstruction suite runtime: {time.time() - t_all:.2f}s")


if __name__ == "__main__":
    main()
