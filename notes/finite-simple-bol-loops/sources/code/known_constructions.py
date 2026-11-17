"""Reproducible constructions & censuses of finite simple proper left Bol loops.

Implements and verifies canonical constructions across five proved structural families:
  1. [N07] Exact-factorization G-loops Q_{(X, Y_0, Y_1)} (G. P. Nagy, arXiv:math/0703919v1):
     - Example II (n=4): Q_24 = Q_{(S_4, C_4, S_3)} of minimum possible order 24 (solvable LMlt).
     - Theorem 3.6: Q_60 = Q_{(A_5, C_5, A_4)} (|N_rho|=2, rank(LMlt)=8, Mlt=A_60) & Q_120 = Q_{(S_5, F_20, S_3)}.
     - Example I (n=3): Q_168 = Q_{(PSL_3(2), C_7, S_4)} of order 168.
  2. [N07E] Exponent-2 Bruck family & N_96^op isotopy class census (G. P. Nagy, arXiv:0709.4544v1):
     - Lemma 3.2 & Theorem 3.6: Simple exponent-2 left Bruck loop N_96^op of order 96.
     - Complete 4-loop isotopy class census of N_96^op (principal folder isotopes (G, H, k_0 K)):
       1 exp-2 Bruck loop (|Aut|=80), 2 non-Bruck exp-4 simple 2-loops (|Aut|=8, 16),
       and 1 rigid (|Aut|=1) max-order-6 / exp-12 simple proper left Bol loop!
     - Proposition 5.1 & Theorem 5.2 (k=1): Order-1536 exponent-2 left Bol loops in G |x U
       (|calG| = 983,040) using explicit homomorphism pi(c)=(4,5), pi(d)=(1,2,3,4) and
       F_2 pi(H)-module isomorphism psi: J_0 -> T_1 (undeformed Prop 5.1 has normal subloop
       of size 16; deformed Thm 5.2 via S^* is simple with Mlt = A_1536).
  3. Odd-order / prime-power solvable-LMlt family p^{p+1} q (extending [N07, §4 Example IV]):
     - Q_1053 on X <= AGammaL(1, 27) of odd order 1053 = 3^4 * 13 (solvable odd |LMlt| = 369,603).
  4. Affine-simple exact-factorization family Q_{(V : G_0, Y_0, G_0)}:
     - Q_960 on F_4^2 : SL_2(4) (|Q| = 960, |N_rho| = 4) and Q_1344 on F_2^3 : SL_3(2) (|Q| = 1344, |N_rho| = 4).
  5. Solvable-wreath exact-factorization construction:
     - Q_1152 on S_4 wr C_2 = SD_16 * (S_3 wr C_2) (|Q| = 1152, solvable |LMlt| = 331,776).
  6. Rank-3 simple Moufang positive control for #0323/S1 (L. J. Paige, 1956):
     - M(3) = U(Zorn(F_3)) / {+-1} on NO_8^+(3) (|M(3)| = 1080, Moufang, Mlt = POmega_8^+(3), rank 3).
"""

from __future__ import annotations

from collections import Counter, deque
import itertools
import math
import time
from typing import Any, Dict, List, Tuple

from bol_engine import (
    Loop,
    bol_folder_from_perms,
    deduplicate_loops,
    exact_factorization_bol_loop,
    sims_automorphism_group,
)
from perm_group import (
    Perm,
    PermGroup,
    compose,
    cycles_to_perm,
    identity_perm,
    invert,
    perm_sign,
)


def build_nagy_q24() -> Loop:
    """Nagy [N07, §4 Example II, n=4]: Q_{(S_4, C_4, S_3)} of minimum order 24 (solvable LMlt)."""
    y0 = PermGroup(4, [cycles_to_perm(4, [[0, 1, 2, 3]])]).enumerate_elements()
    y1 = PermGroup(
        4, [cycles_to_perm(4, [[0, 1, 2]]), cycles_to_perm(4, [[0, 1]])]
    ).enumerate_elements()
    return exact_factorization_bol_loop(4, y0, y1, name="N07_ExII_Q24_(S4,C4,S3)")


def build_nagy_q60() -> Loop:
    """Nagy [N07, Thm 3.6]: Q_{(A_5, C_5, A_4)} of order 60."""
    y0 = PermGroup(5, [cycles_to_perm(5, [[0, 1, 2, 3, 4]])]).enumerate_elements()
    y1 = PermGroup(
        5, [cycles_to_perm(5, [[0, 1, 2]]), cycles_to_perm(5, [[0, 1], [2, 3]])]
    ).enumerate_elements()
    return exact_factorization_bol_loop(5, y0, y1, name="N07_Thm3.6_Q60_(A5,C5,A4)")


def build_nagy_q120() -> Loop:
    """Nagy [N07, Thm 3.6]: Q_{(S_5, F_20, S_3)} of order 120."""
    y0 = PermGroup(
        5, [cycles_to_perm(5, [[0, 1, 2, 3, 4]]), cycles_to_perm(5, [[1, 2, 4, 3]])]
    ).enumerate_elements()
    y1 = PermGroup(
        5, [cycles_to_perm(5, [[0, 1, 2]]), cycles_to_perm(5, [[0, 1]])]
    ).enumerate_elements()
    return exact_factorization_bol_loop(5, y0, y1, name="N07_Thm3.6_Q120_(S5,F20,S3)")


def build_nagy_q168() -> Loop:
    """Nagy [N07, §4 Example I, n=3]: Q_{(PSL(3,2), C_7, S_4)} of order 168."""
    s_cyc = cycles_to_perm(7, [[0, 1, 2, 3, 4, 5, 6]])
    g1 = cycles_to_perm(7, [[1, 3], [2, 6]])
    g2 = cycles_to_perm(7, [[1, 2, 4], [3, 6, 5]])
    g3 = cycles_to_perm(7, [[2, 4], [5, 6]])
    y0 = PermGroup(7, [s_cyc]).enumerate_elements()
    y1 = PermGroup(7, [g1, g2, g3]).enumerate_elements()
    return exact_factorization_bol_loop(7, y0, y1, name="N07_ExI_Q168_(PSL3_2,C7,S4)")


def _nagy_exp2_base_data() -> Dict[str, Any]:
    """Construct base group G <= S_40 (|G|=3840), J, J_0, c^G, and H = N_G(P) from [N07E, Lemma 3.2].

    Note: [N07E] writes permutations in GAP right action x^(g1 * g2) = (x^g1)^g2 = compose(g2, g1)[x].
    Both <c, d>_left and <c, d>_right equal the identical subgroup G of Sym(40) (order 3840),
    J = O_2(G) (order 32), J_0 = [G, J] (order 16), and c^G (80 involutions). Here we take P = <c *_GAP d>
    so H = N_G(P) matches [N07E, Lemma 3.2] verbatim under GAP right multiplication as well.
    """
    c = cycles_to_perm(
        40,
        [
            [1, 4], [2, 9], [3, 10], [6, 11], [7, 12],
            [13, 21], [14, 22], [15, 24], [16, 23], [17, 30],
            [18, 29], [19, 31], [20, 32], [33, 35], [38, 40],
        ],
        one_based=True,
    )
    d = cycles_to_perm(
        40,
        [
            [1, 2, 4, 6, 8, 7, 5, 3],
            [9, 13, 25, 18, 10, 14, 26, 17],
            [11, 15, 27, 20, 12, 16, 28, 19],
            [21, 30, 38, 34, 23, 31, 40, 35],
            [22, 32, 39, 36, 24, 29, 37, 33],
        ],
        one_based=True,
    )
    G_elems = sorted(PermGroup(40, [c, d]).enumerate_elements())
    d2 = compose(d, d)
    u1 = compose(d2, d2)
    J_elems = set(
        PermGroup(40, [compose(invert(g), compose(u1, g)) for g in G_elems]).enumerate_elements()
    )
    comm_GJ = [
        compose(invert(g), compose(invert(j), compose(g, j)))
        for g in (c, d)
        for j in J_elems
    ]
    J0_elems = sorted(PermGroup(40, comm_GJ).enumerate_elements())
    c_class = sorted({compose(invert(g), compose(c, g)) for g in G_elems})
    # cd in GAP right action: x^(c*d) = d[c[x]] = compose(d, c)[x]
    cd_gap = compose(d, c)
    P_set = set(PermGroup(40, [cd_gap]).enumerate_elements())
    H_elems = sorted(
        g for g in G_elems if all(compose(g, compose(p, invert(g))) in P_set for p in P_set)
    )
    return {
        "c": c,
        "d": d,
        "G": G_elems,
        "J": J_elems,
        "J0": J0_elems,
        "c_class": c_class,
        "H": H_elems,
    }


def build_nagy_exp2_q96() -> Loop:
    """Nagy [N07E, Lemma 3.2 & Thm 3.6]: Simple exponent-2 left Bruck loop N_96^op of order 96.

    Note on handedness: [N07E] defines right Bol folders via right cosets Hx.
    Because k^-1 = k on K and H^-1 = H, group inversion sends the opposite loop Q_R^op
    isomorphically onto the left-coset folder loop on the identical (G, H, K)!
    """
    data = _nagy_exp2_base_data()
    id_40 = identity_perm(40)
    K_96 = [id_40] + sorted(
        k for k in (set(data["J0"]) | set(data["c_class"])) if k != id_40
    )
    res = bol_folder_from_perms(
        40,
        data["G"],
        data["H"],
        K_96,
        name="N07E_Thm3.6_N96_op_exp2_Bruck",
        verify_conjugate_transversals=False,
    )
    if not res.is_valid or res.loop is None:
        raise RuntimeError(f"Failed to construct Nagy N_96^op: {res.reason}")
    return res.loop


def build_nagy_q96_isotopy_census() -> List[Dict[str, Any]]:
    """Complete 4-loop isotopy class census of N_96^op via principal folder isotopes (G, H, k_0 K).

    For any centerless exponent-2 left Bol folder (G, H, K), every loop isotopic to Q is isomorphic
    to a principal folder isotope Q_{k_0} defined on (G, H, k_0 K) (k_0 in K), and isomorphism
    classes biject with Aut(Q)-orbits on Q with |Aut(Q_{k_0})| = |Aut(Q)| / |Orb(k_0)|.

    Returns the 4 canonical isomorphism class records sorted as:
      0. k_0 = 1 (size 1):            max_ord = 2, exp = 2,  {1:1, 2:95},               |Aut| = 80, Bruck = True
      1. k_0 in J_0 \\ {1} (size 10): max_ord = 4, exp = 4,  {1:1, 2:31, 4:64},         |Aut| = 8,  Bruck = False
      2. k_0 in J_0 \\ {1} (size 5):  max_ord = 4, exp = 4,  {1:1, 2:31, 4:64},         |Aut| = 16, Bruck = False
      3. k_0 in c^G (size 80):        max_ord = 6, exp = 12, {1:1, 2:11, 3:24, 4:36, 6:24}, |Aut| = 1 (rigid!), Bruck = False
    """
    data = _nagy_exp2_base_data()
    id_40 = identity_perm(40)
    j0_set = set(data["J0"])
    K_96 = [id_40] + sorted(
        k for k in (j0_set | set(data["c_class"])) if k != id_40
    )
    H_96 = data["H"]

    # Build left-coset lookup under the same left composition used by bol_folder_from_perms
    coset_96: Dict[Perm, int] = {}
    for idx, k in enumerate(K_96):
        for h in H_96:
            coset_96[compose(k, h)] = idx

    iso_loops: List[Loop] = []
    stratum_by_name: Dict[str, str] = {}
    for c_idx, kc in enumerate(K_96):
        # Every kc in K_96 is an involution (kc^-1 == kc), so kc * kc = 1_G is the identity of k_0 K.
        order_idx = [c_idx] + [i for i in range(96) if i != c_idx]
        pos_of = {orig: new_i for new_i, orig in enumerate(order_idx)}
        tbl = [[0] * 96 for _ in range(96)]
        for ni, ia in enumerate(order_idx):
            ka = K_96[ia]
            row = tbl[ni]
            for nj, ib in enumerate(order_idx):
                kb = K_96[ib]
                # (kc * u) H = (kc * ka)(kc * kb) H  <=>  u H = (ka * kc * kb) H
                u_orig = coset_96[compose(ka, compose(kc, kb))]
                row[nj] = pos_of[u_orig]
        lname = f"N07E_N96_op_k{c_idx}"
        if kc == id_40:
            stratum = "1"
        elif kc in j0_set:
            stratum = "J_0 \\ {1}"
        else:
            stratum = "c^G"
        stratum_by_name[lname] = stratum
        iso_loops.append(Loop(tbl, name=lname))

    raw_classes = deduplicate_loops(iso_loops)
    records: List[Dict[str, Any]] = []
    for rep_lp, members in raw_classes:
        is_pa, elem_orders, exp_val = rep_lp.power_associativity_and_orders()
        assert is_pa and elem_orders is not None
        spec = dict(sorted(Counter(elem_orders).items()))
        inv_p = rep_lp.inverse_properties()
        aut_ord = rep_lp.automorphism_group_order()
        strata = {stratum_by_name[m] for m in members}
        assert len(strata) == 1
        records.append(
            {
                "loop": rep_lp,
                "orbit_size": len(members),
                "source_stratum": next(iter(strata)),
                "max_order": max(elem_orders),
                "exponent": exp_val,
                "order_spectrum": spec,
                "aut_order": aut_ord,
                "is_left_bruck": inv_p["has_AIP"],
            }
        )

    records.sort(
        key=lambda r: (
            r["exponent"],
            r["aut_order"] if r["exponent"] == 4 else -r["aut_order"],
        )
    )
    labels = [
        "N07E_N96_op_Orb0_exp2_Bruck_Aut80",
        "N07E_N96_op_Orb1_exp4_2loop_Aut8",
        "N07E_N96_op_Orb2_exp4_2loop_Aut16",
        "N07E_N96_op_Orb3_maxOrd6_exp12_Rigid_Aut1",
    ]
    for idx, rec in enumerate(records):
        if idx < len(labels):
            rec["loop"].name = labels[idx]
        assert rec["orbit_size"] * rec["aut_order"] == 80, (
            f"Orbit-Stabilizer mismatch on orbit {idx}: size={rec['orbit_size']}, |Aut|={rec['aut_order']}"
        )
    return records


def build_nagy_exp2_q1536(deformed: bool = True) -> Loop:
    r"""Nagy [N07E, §5 Prop 5.1 & Thm 5.2, k = 1]: Exponent-2 left Bol loop of order 1536.

    Constructed explicitly in GAP right-action convention (matching [N07E, §§3-5] with
    verified explicit quotient map pi(c) = (4, 5), pi(d) = (1, 2, 3, 4)):
      - Enveloping group calG = G |x U of order 3840 * 256 = 983,040, where U = N (+) N
        is the 8-dimensional even-weight F_2 S_5-module (acting diagonally on A_5 and
        swapping summands on S_5 \ A_5), with (g_1, u_1)(g_2, u_2) = (g_1 g_2, (u_1 . pi(g_2)) + u_2).
      - Explicit F_2 pi(H)-module isomorphism psi: J_0 -> T_1 on basis e_i = u_1 u_{i+1} (i=1..4):
          psi(u_1 u_2) = (01010, 11011),  psi(u_1 u_3) = (00101, 11101),
          psi(u_1 u_4) = (00110, 01001),  psi(u_1 u_5) = (10111, 00011)   (bit 0 = leftmost).
      - `deformed=True` (Thm 5.2): calH = <(H, 0), (j, psi(j))>, calK = c^calG cup (J_0 x S^*);
        yields a SIMPLE exponent-2 proper left Bol loop of order 1536 with Mlt = A_1536.
      - `deformed=False` (Prop 5.1): calH = H |x T_1, calK = c^calG cup (J_0 x W);
        yields a non-simple exponent-2 left Bol loop of order 1536 (normal subloop of size 16).
    """
    data = _nagy_exp2_base_data()
    c, d = data["c"], data["d"]
    G = data["G"]
    J = data["J"]
    J0 = data["J0"]
    c_class = data["c_class"]
    H = data["H"]
    id_40 = identity_perm(40)
    id_5 = identity_perm(5)
    g_to_idx = {g: i for i, g in enumerate(G)}

    # Right-action group multiplication in Sym(40) and Sym(5): (g1 *_GAP g2)(x) = g2[g1[x]]
    def mul_r(g1: Perm, g2: Perm) -> Perm:
        return compose(g2, g1)

    def conj_r(x: Perm, g: Perm) -> Perm:
        return mul_r(invert(g), mul_r(x, g))

    # Explicit quotient homomorphism pi: G ->> S_5 with pi(c) = (4, 5), pi(d) = (1, 2, 3, 4)
    pi_c = cycles_to_perm(5, [[4, 5]], one_based=True)
    pi_d = cycles_to_perm(5, [[1, 2, 3, 4]], one_based=True)
    pi_map: Dict[Perm, Perm] = {id_40: id_5}
    bfs_q: deque[Perm] = deque([id_40])
    while bfs_q:
        g = bfs_q.popleft()
        pg = pi_map[g]
        for gen_g, gen_s5 in ((c, pi_c), (d, pi_d)):
            ng = mul_r(g, gen_g)
            npg = mul_r(pg, gen_s5)
            prev = pi_map.get(ng)
            if prev is None:
                pi_map[ng] = npg
                bfs_q.append(ng)
            elif prev != npg:
                raise RuntimeError("pi: G -> S_5 failed homomorphism consistency")
    assert len(pi_map) == 3840
    assert {g for g, pg in pi_map.items() if pg == id_5} == J

    # Right G-action on U = N (+) N (bit 0 = leftmost digit of 5-bit string)
    N_vecs = [v for v in range(32) if bin(v).count("1") % 2 == 0]
    wt4_vecs = [v for v in N_vecs if bin(v).count("1") == 4]
    U_elems = [(a << 5) | b for a in N_vecs for b in N_vecs]

    def bits5(bit_str: str) -> int:
        out = 0
        for idx_b, ch in enumerate(bit_str):
            if ch == "1":
                out |= 1 << idx_b
        return out

    def pair_u(sa: str, sb: str) -> int:
        return (bits5(sa) << 5) | bits5(sb)

    def act_N_r(v: int, s5: Perm) -> int:
        out = 0
        for bit in range(5):
            if (v >> bit) & 1:
                out |= 1 << s5[bit]
        return out

    def act_U_r(u: int, s5: Perm) -> int:
        a, b = u >> 5, u & 31
        sa, sb = act_N_r(a, s5), act_N_r(b, s5)
        return ((sa << 5) | sb) if perm_sign(s5) == 1 else ((sb << 5) | sa)

    W_set = sorted((v << 5) | v for v in N_vecs)
    S_star = sorted(
        {0}
        | {(v << 5) | v for v in wt4_vecs}
        | {(v << 5) for v in wt4_vecs}
        | set(wt4_vecs)
    )

    # Basis e_1 = u_1 u_2, ..., e_4 = u_1 u_5 of J_0 and explicit F_2 pi(H)-isomorphism psi: J_0 -> T_1
    cd_r = mul_r(c, d)
    cdc_r = mul_r(cd_r, c)
    cdcd_r = mul_r(cdc_r, d)
    u1 = mul_r(mul_r(d, d), mul_r(d, d))
    u2 = conj_r(u1, c)
    u3 = conj_r(u1, cd_r)
    u4 = conj_r(u1, cdc_r)
    u5 = conj_r(u1, cdcd_r)
    psi_basis = [
        (mul_r(u1, u2), pair_u("01010", "11011")),
        (mul_r(u1, u3), pair_u("00101", "11101")),
        (mul_r(u1, u4), pair_u("00110", "01001")),
        (mul_r(u1, u5), pair_u("10111", "00011")),
    ]
    psi: Dict[Perm, int] = {id_40: 0}
    for ej, tj in psi_basis:
        for k_prev, v_prev in list(psi.items()):
            psi[mul_r(k_prev, ej)] = v_prev ^ tj
    assert len(psi) == 16 and set(psi.keys()) == set(J0)
    T1 = sorted(psi.values())
    assert len(T1) == 16 and T1 != W_set

    # Verify F_2 pi(H)-equivariance of psi on all (h, j) in H x J_0
    for h in H:
        sh = pi_map[h]
        for j in J0:
            if psi[conj_r(j, h)] != act_U_r(psi[j], sh):
                raise RuntimeError("psi failed F_2 pi(H)-module equivariance")

    c_calG = [(cg, u) for cg in c_class for u in U_elems if act_U_r(u, pi_map[cg]) == u]
    assert len(c_calG) == 1280

    if deformed:
        K_1536 = (
            [(id_40, 0)]
            + [(j, s) for j in J0 for s in S_star if not (j == id_40 and s == 0)]
            + c_calG
        )
        # Since (h, 0)(j, psi(j)) = (h *_GAP j, psi(j)) and psi is pi(H)-equivariant, this is a 640-subgroup!
        H_1536 = [(mul_r(h, j), psi[j]) for h in H for j in J0]
        lp_name = "N07E_Thm5.2_Q1536_k1_exp2_leftOp"
    else:
        K_1536 = (
            [(id_40, 0)]
            + [(j, w) for j in J0 for w in W_set if not (j == id_40 and w == 0)]
            + c_calG
        )
        H_1536 = [(h, t) for h in H for t in T1]
        lp_name = "N07E_Prop5.1_Q1536_nonsimple_ext"

    # Left cosets x * calH in calG (since calK^-1 == calK, left cosets give the left Bol loop directly)
    coset_rep: Dict[int, int] = {}
    for idx_k, (kg, ku) in enumerate(K_1536):
        for hg, hu in H_1536:
            pg = g_to_idx[mul_r(kg, hg)]
            pu = act_U_r(ku, pi_map[hg]) ^ hu
            key = (pg << 10) | pu
            if key in coset_rep:
                raise RuntimeError("Left transversal collision in Q_1536 folder")
            coset_rep[key] = idx_k
    assert len(coset_rep) == 1536 * 640

    distinct_kg = list({kg for kg, _ in K_1536})
    kg_mul = {
        kg1: {kg2: g_to_idx[mul_r(kg1, kg2)] for kg2 in distinct_kg}
        for kg1 in distinct_kg
    }
    distinct_s5 = list(set(pi_map.values()))
    act_table = {s5: [act_U_r(uv, s5) for uv in range(1024)] for s5 in distinct_s5}

    tbl: List[List[int]] = [[0] * 1536 for _ in range(1536)]
    for i, (ag, au) in enumerate(K_1536):
        row_gm = kg_mul[ag]
        row_t = tbl[i]
        for j, (bg, bu) in enumerate(K_1536):
            key = (row_gm[bg] << 10) | (act_table[pi_map[bg]][au] ^ bu)
            row_t[j] = coset_rep[key]

    return Loop(tbl, name=lp_name, validate_loop=True)


def build_nagy_q1536_isotopy_census(verify_all_isotopes: bool = True) -> List[Dict[str, Any]]:
    """Complete 20-loop isotopy class census of Q_1536 via Sims exact Aut(Q_1536) orbits.

    Because Q_1536 has exponent 2 and N_rho(Q_1536) = {1} (so Z(LMlt(Q_1536)) = {1}),
    by C0006 Theorem 1.1 every loop isotopic to Q_1536 is isomorphic to a principal
    folder isotope x o_d y = x * (d * y) (d in Q_1536), and isomorphism classes biject
    with Aut(Q_1536)-orbits on Q_1536 (`1 + 3*5 + 6*10 + 9*20 + 1280 = 1536`) with
    |Aut(Q_{1536}^{(d)})| = 1280 / |Orb(d)|:
      - d = 0 (1 class, size 1): exp 2, Bruck = True, |Aut| = 1280;
      - d in (J_0 x S*) \\ {0} (18 classes: 3 of size 5, 6 of size 10, 9 of size 20):
        exp 4, non-Bruck simple 2-loops, |Aut| in {256, 128, 64};
      - d in c^calG (1 class, size 1280): max_ord 6, exp 12, non-Bruck rigid (|Aut| = 1).
    """
    q1536 = build_nagy_exp2_q1536(deformed=True)
    assert q1536.right_nucleus() == (0,), "Expected N_rho(Q_1536) = {1}"
    aut_grp = sims_automorphism_group(q1536, prefer_idx_from=256)
    aut_ord = aut_grp.order()
    assert aut_ord == 1280, f"Expected |Aut(Q_1536)| = 1280, got {aut_ord}"

    orbs = sorted(aut_grp.orbits(), key=lambda o: (o[0] != 0, len(o), o[0]))
    assert sum(len(o) for o in orbs) == 1536

    records: List[Dict[str, Any]] = []
    for idx, orb in enumerate(orbs):
        d = orb[0]
        order_idx = [d] + [i for i in range(1536) if i != d]
        pos = {orig: ni for ni, orig in enumerate(order_idx)}
        ld = q1536.table[d]
        tbl = [[0] * 1536 for _ in range(1536)]
        for ni, ou in enumerate(order_idx):
            row_u = q1536.table[ou]
            row_out = tbl[ni]
            for nj, ov in enumerate(order_idx):
                row_out[nj] = pos[row_u[ld[ov]]]

        if d == 0:
            stratum = "1"
        elif d < 16:
            stratum = "1 x (S* \\ {0})"
        elif d < 256:
            stratum = "(J_0 \\ {1}) x S*"
        else:
            stratum = "c^calG"

        lp_d = Loop(tbl, name=f"N07E_Q1536_Orb{idx}_d{d}_sz{len(orb)}", validate_loop=True)
        is_pa, elem_orders, exp_val = lp_d.power_associativity_and_orders()
        assert is_pa and elem_orders is not None
        spec = dict(sorted(Counter(elem_orders).items()))
        inv_p = lp_d.inverse_properties()
        assert aut_ord % len(orb) == 0
        stab_aut = aut_ord // len(orb)

        if verify_all_isotopes:
            is_lb, _ = lp_d.check_left_bol()
            is_mf, _ = lp_d.check_moufang()
            is_smp, ns = lp_d.check_simplicity()
            assert is_lb and (not is_mf) and is_smp and ns == []
            assert lp_d.RMlt()._giant_kind == "A_n"
            assert lp_d.Mlt()._giant_kind == "A_n"

        records.append(
            {
                "loop": lp_d,
                "rep_index": d,
                "orbit_size": len(orb),
                "source_stratum": stratum,
                "max_order": max(elem_orders),
                "exponent": exp_val,
                "order_spectrum": spec,
                "aut_order": stab_aut,
                "is_left_bruck": inv_p["has_AIP"],
            }
        )
    return records


def build_nagy_odd_q1053() -> Loop:
    """Nagy [N07, §4 Example IV]: Odd-order 1053 = 3^4 * 13 simple proper left Bol loop.

    Constructs F_27 = F_3[t] / (t^3 - t + 1) (t^3 = t + 2 mod 3), Sigma = (F_27^*)^2 (|Sigma|=13),
    X = {z -> a * z^(3^k) + b : a in Sigma, b in F_27, k in 0..2} (|X|=1053),
    Y_1 = X_0 (|Y_1|=39), and Y_0 = <ker(Tr_{F_27/F_3}), z -> z^3 + v_0> where Tr(v_0) = 1
    (|Y_0|=27, regular on F_27, Y_0 != V). Solvable odd-order |LMlt| = 369,603 = 3^7 * 13^2.
    """
    elems: List[Tuple[int, int, int]] = [
        (c0, c1, c2) for c2 in range(3) for c1 in range(3) for c0 in range(3)
    ]
    to_idx: Dict[Tuple[int, int, int], int] = {v: i for i, v in enumerate(elems)}

    def f_add(i: int, j: int) -> int:
        a0, a1, a2 = elems[i]
        b0, b1, b2 = elems[j]
        return to_idx[((a0 + b0) % 3, (a1 + b1) % 3, (a2 + b2) % 3)]

    def f_mul(i: int, j: int) -> int:
        a = elems[i]
        b = elems[j]
        p = [0, 0, 0, 0, 0]
        for u in range(3):
            for v in range(3):
                p[u + v] += a[u] * b[v]
        p[2] += p[4]
        p[1] += 2 * p[4]
        p[1] += p[3]
        p[0] += 2 * p[3]
        return to_idx[(p[0] % 3, p[1] % 3, p[2] % 3)]

    frob1 = [f_mul(i, f_mul(i, i)) for i in range(27)]
    frob2 = [frob1[frob1[i]] for i in range(27)]
    frobs = [list(range(27)), frob1, frob2]

    sigma = sorted({f_mul(i, i) for i in range(1, 27)})
    assert len(sigma) == 13

    def make_perm(a: int, b: int, k: int) -> Perm:
        fr = frobs[k]
        return tuple(f_add(f_mul(a, fr[z]), b) for z in range(27))

    def trace_f27(i: int) -> int:
        return f_add(i, f_add(frob1[i], frob2[i]))

    one_idx = to_idx[(1, 0, 0)]
    Y1 = [make_perm(a, 0, k) for a in sigma for k in range(3)]
    W_gens = [make_perm(one_idx, b, 0) for b in range(1, 27) if trace_f27(b) == 0]
    v0 = next(b for b in range(1, 27) if trace_f27(b) == one_idx)
    g_star = make_perm(one_idx, v0, 1)
    Y0 = PermGroup(27, W_gens + [g_star]).enumerate_elements()
    assert len(Y0) == 27
    return exact_factorization_bol_loop(27, Y0, Y1, name="N07_ExIV_Q1053_odd_(3^4x13)")


def build_affine_simple_q960() -> Loop:
    """Affine-simple exact-factorization loop Q_960 on X = F_4^2 : SL(2, 4) (|Q| = 960).

    Uses Cauchy-hyperplane regular subgroup Y_0 = <V_0, (v_0, u)> != V of order 16, where
    u(x, y) = (x ^ y, y) in SL(2, 4), V_0 = {(x, y) in F_4^2 : y in {0, 2}}, v_0 = (0, 1).
    """
    mul4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    pts = [(x, y) for x in range(4) for y in range(4)]
    to_i = {pt: i for i, pt in enumerate(pts)}

    mats = [((1, 1), (0, 1)), ((1, 2), (0, 1)), ((0, 1), (1, 0)), ((2, 0), (0, 3))]
    y1_gens = [
        tuple(
            to_i[
                (
                    mul4[m[0][0]][pts[z][0]] ^ mul4[m[0][1]][pts[z][1]],
                    mul4[m[1][0]][pts[z][0]] ^ mul4[m[1][1]][pts[z][1]],
                )
            ]
            for z in range(16)
        )
        for m in mats
    ]
    Y1 = PermGroup(16, y1_gens, allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y1) == 60

    v0_gens = [
        tuple(to_i[(pts[z][0] ^ vx, pts[z][1] ^ vy)] for z in range(16))
        for vx, vy in pts
        if vy in (0, 2) and (vx, vy) != (0, 0)
    ]
    g_star = tuple(to_i[(pts[z][0] ^ pts[z][1], pts[z][1] ^ 1)] for z in range(16))
    Y0 = PermGroup(16, v0_gens + [g_star], allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y0) == 16
    return exact_factorization_bol_loop(16, Y0, Y1, name="AffineSimple_Q960_(F4^2:SL2_4)")


def build_solvable_wreath_q1152() -> Loop:
    """Solvable-wreath simple proper left Bol G-loop Q_1152 on X = S_4 wr C_2 <= S_8.

    Y_1 = S_3 wr C_2 = Stab_X({3, 7}) (|Y_1| = 72) and Y_0 = <r, s> ~= SD_16 (|Y_0| = 16)
    with r = (0, 4, 1, 5, 2, 6, 3, 7) and s = (1, 3)(4, 5)(6, 7), satisfying Y_0 cap Y_1 = 1
    and X' Y_0 = X' Y_1 = X (giving solvable |LMlt(Q_1152)| = 331,776 = 2^12 * 3^4).
    """
    y1_gens = [
        cycles_to_perm(8, [[0, 1, 2]]),
        cycles_to_perm(8, [[0, 1]]),
        cycles_to_perm(8, [[0, 4], [1, 5], [2, 6], [3, 7]]),
    ]
    Y1 = PermGroup(8, y1_gens, allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y1) == 72

    r_gen = cycles_to_perm(8, [[0, 4, 1, 5, 2, 6, 3, 7]])
    s_gen = cycles_to_perm(8, [[1, 3], [4, 5], [6, 7]])
    Y0 = PermGroup(8, [r_gen, s_gen], allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y0) == 16
    return exact_factorization_bol_loop(8, Y0, Y1, name="SolvableWreath_Q1152_(S4wrC2,SD16,S3wrC2)")


def build_affine_simple_q1344() -> Loop:
    """Affine-simple exact-factorization loop Q_1344 on X = F_2^3 : SL(3, 2) (|Q| = 1344, |N_rho| = 4).

    Uses elementary abelian regular subgroup Y_0 = W : <(e_2, U_1)> ~= C_2^3 != V of order 8,
    where W = {(x0, x1, x2) : x2 = 0} and g_*(x0, x1, x2) = (x0 ^ x1, x1, x2 ^ 1).
    """
    g1 = tuple((((z & 1) ^ ((z >> 1) & 1)) | (z & 0b110)) for z in range(8))
    g2 = tuple((((z >> 1) & 0b011) | ((z & 1) << 2)) for z in range(8))
    Y1 = PermGroup(8, [g1, g2], allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y1) == 168

    w_gens = [tuple(z ^ u for z in range(8)) for u in (1, 2)]
    g_star = tuple(
        (((z & 1) ^ ((z >> 1) & 1)) | (z & 0b010) | ((z ^ 0b100) & 0b100))
        for z in range(8)
    )
    Y0 = PermGroup(8, w_gens + [g_star], allow_jordan_fastpath=False).enumerate_elements()
    assert len(Y0) == 8
    return exact_factorization_bol_loop(8, Y0, Y1, name="AffineSimple_Q1344_(F2^3:SL3_2)")


def _paige_m3_points() -> Tuple[List[Tuple[int, ...]], List[Tuple[int, ...]]]:
    """Return canonical projective point lists `(pts_plus_1080, pts_minus_1080)` over F_3^8
    for the Zorn quadratic form Q(v) = v_0 v_1 - v_2 v_5 - v_3 v_6 - v_4 v_7 (mod 3),
    normalized so the first nonzero coordinate is 1, with `pts_plus_1080[0] = (1, 1, 0, 0, 0, 0, 0, 0)`.
    """
    pts_plus: List[Tuple[int, ...]] = []
    pts_minus: List[Tuple[int, ...]] = []
    for v in itertools.product(range(3), repeat=8):
        if v == (0,) * 8 or next(c for c in v if c != 0) != 1:
            continue
        qv = (v[0] * v[1] - v[2] * v[5] - v[3] * v[6] - v[4] * v[7]) % 3
        if qv == 1:
            pts_plus.append(v)
        elif qv == 2:
            pts_minus.append(v)
    id_vec = (1, 1, 0, 0, 0, 0, 0, 0)
    pts_plus.remove(id_vec)
    pts_plus.insert(0, id_vec)
    assert len(pts_plus) == 1080 and len(pts_minus) == 1080
    return pts_plus, pts_minus


def build_paige_m3() -> Loop:
    """Paige (1956) simple nonassociative Moufang loop M(3) = U(Zorn(F_3)) / {+-1} of order 1080.

    Serves as the rank-3 Moufang positive control on NO_8^+(3) for #0323/S1:
    LMlt(M(3)) = RMlt(M(3)) = Mlt(M(3)) ~= POmega_8^+(3) of order 4,952,179,814,400 and rank 3
    with subdegrees (1, 351, 728). Note: M(3) is Moufang (NOT a proper left Bol loop).
    """
    pts1080, _ = _paige_m3_points()
    p1080_i = {v: i for i, v in enumerate(pts1080)}

    def norm1080(v: Tuple[int, ...]) -> int:
        ic = 1 if next(c for c in v if c != 0) == 1 else 2
        return p1080_i[tuple((c * ic) % 3 for c in v)]

    def zorn_mul(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        a1, b1, u10, u11, u12, v10, v11, v12 = x
        a2, b2, u20, u21, u22, v20, v21, v22 = y
        u1v2 = u10 * v20 + u11 * v21 + u12 * v22
        v1u2 = v10 * u20 + v11 * u21 + v12 * u22
        vx0, vx1, vx2 = v11 * v22 - v12 * v21, v12 * v20 - v10 * v22, v10 * v21 - v11 * v20
        ux0, ux1, ux2 = u11 * u22 - u12 * u21, u12 * u20 - u10 * u22, u10 * u21 - u11 * u20
        return norm1080(
            (
                (a1 * a2 + u1v2) % 3,
                (v1u2 + b1 * b2) % 3,
                (a1 * u20 + b2 * u10 - vx0) % 3,
                (a1 * u21 + b2 * u11 - vx1) % 3,
                (a1 * u22 + b2 * u12 - vx2) % 3,
                (a2 * v10 + b1 * v20 + ux0) % 3,
                (a2 * v11 + b1 * v21 + ux1) % 3,
                (a2 * v12 + b1 * v22 + ux2) % 3,
            )
        )

    tbl = [[zorn_mul(x, y) for y in pts1080] for x in pts1080]
    return Loop(tbl, name="Paige_M3_(POmega8+3_deg1080)", validate_loop=True)


def describe_symmetric_match(n: int, order: int) -> str:
    fact = math.factorial(n)
    if order == fact:
        return f"= S_{n}!"
    if order * 2 == fact:
        return f"= A_{n}!"
    return ""


def main() -> None:
    import sys

    fast_only = "--fast" in sys.argv
    t0 = time.time()
    baselines = [
        build_nagy_q24(),
        build_nagy_q60(),
        build_nagy_exp2_q96(),
        build_nagy_q120(),
        build_nagy_q168(),
    ]
    if not fast_only:
        baselines.extend(
            [
                build_affine_simple_q960(),
                build_nagy_odd_q1053(),
                build_solvable_wreath_q1152(),
                build_affine_simple_q1344(),
                build_nagy_exp2_q1536(deformed=True),
            ]
        )

    for lp in baselines:
        t_lp = time.time()
        rep = lp.analyze(check_op_iso=(lp.n <= 168), compute_aut=(lp.n <= 96))
        n = rep["order"]
        exp_v = rep["exponent"]
        name = rep["name"]
        mlt_tag = describe_symmetric_match(n, rep["Mlt_order"])
        rmlt_tag = describe_symmetric_match(n, rep["RMlt_order"])
        mlt_ord_str = mlt_tag if mlt_tag else str(rep["Mlt_order"])
        rmlt_ord_str = rmlt_tag if rmlt_tag else str(rep["RMlt_order"])
        subdeg_l = (
            rep["LMlt_subdegrees"]
            if len(rep["LMlt_subdegrees"]) <= 16
            else f"({len(rep['LMlt_subdegrees'])} orbits, max={max(rep['LMlt_subdegrees'])})"
        )
        aut_str = f" |Aut|={rep['Aut_order']}" if "Aut_order" in rep else ""
        print(f"\n=== {name} (order={n}, exp={exp_v}, time={time.time()-t_lp:.2f}s) ===")
        print(
            "  left_bol={} proper={} mouf_witness={} simple={}{}".format(
                rep["is_left_bol"],
                rep["is_proper_left_bol"],
                rep["non_moufang_witness"],
                rep["is_simple"],
                aut_str,
            )
        )
        print(
            "  LMlt: |LMlt|={} |LInn|={} rank={} subdeg={} prim={} solvable={}".format(
                rep["LMlt_order"],
                rep["LInn_order"],
                rep["LMlt_rank"],
                subdeg_l,
                rep["is_LMlt_primitive"],
                rep["is_LMlt_solvable"],
            )
        )
        print(
            "  RMlt: |RMlt|={} rank={} subdeg={} prim={}".format(
                rmlt_ord_str,
                rep["RMlt_rank"],
                rep["RMlt_subdegrees"],
                rep["is_RMlt_primitive"],
            )
        )
        print(
            "  Mlt : |Mlt| ={} RANK(Mlt)={} subdeg={} prim={}".format(
                mlt_ord_str,
                rep["Mlt_rank"],
                rep["Mlt_subdegrees"],
                rep["is_Mlt_primitive"],
            )
        )
        print(
            "  Nuclei=(Nl={}, Nm={}, Nr={}) C={} Z={} LIP={} RIP={} Bruck={} LAuto={} Auto={} iso_op={}".format(
                rep["N_lambda_size"],
                rep["N_mu_size"],
                rep["N_rho_size"],
                rep["commutant_size"],
                rep["center_size"],
                rep["has_LIP"],
                rep["has_RIP"],
                rep["is_left_bruck"],
                rep["is_left_automorphic"],
                rep["is_automorphic"],
                rep["is_isomorphic_to_opposite"],
            )
        )

    # Complete 4-loop isotopy class census of N_96^op
    t_iso = time.time()
    census_96 = build_nagy_q96_isotopy_census()
    print(
        f"\n=== Complete N_96^op Isotopy Class Census ({len(census_96)} pairwise non-isomorphic loops, {time.time()-t_iso:.2f}s) ==="
    )
    for idx, rec in enumerate(census_96):
        lp_c: Loop = rec["loop"]
        rep_c = lp_c.analyze(check_op_iso=False)
        print(
            f"  Orbit {idx}: {lp_c.name} | k_0 in {rec['source_stratum']:<9} | "
            f"orb={rec['orbit_size']:>2} | max_ord={rec['max_order']} | exp={rec['exponent']:>2} | "
            f"|Aut|={rec['aut_order']:>2} | Bruck={str(rec['is_left_bruck']):<5} | simple={rep_c['is_simple']} | "
            f"Mlt=A_96:{rep_c['Mlt_order']*2 == math.factorial(96)} | orders={rec['order_spectrum']}"
        )

    if not fast_only:
        t_ext = time.time()
        ext_1536 = build_nagy_exp2_q1536(deformed=False)
        is_lb_ext, _ = ext_1536.check_left_bol()
        is_m_ext, wit_ext = ext_1536.check_moufang()
        is_simp_ext, ns_ext = ext_1536.check_simplicity()
        print(
            f"\n[Negative control] {ext_1536.name} (time={time.time()-t_ext:.2f}s): "
            f"left_bol={is_lb_ext} proper={not is_m_ext} witness={wit_ext} "
            f"simple={is_simp_ext} normal_subloop_sizes={ns_ext}"
        )

    print(f"\nTotal baseline suite runtime: {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
