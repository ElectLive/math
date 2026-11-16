"""Wave-2 reproducible censuses & verifiers for Problem #0323 and #0323/S1.

Covers all three computational sub-targets of Wave 2:
  1. Sub-target 4.1 (Principal Folder Isotopes & Q_1536 20-Loop Isotopy Census):
     - Exact Sims bottom-up automorphism group (`sims_automorphism_group`) and complete
       20-class isotopy-orbit census of `Q_1536` (`|Aut| = 1280`, `1 + 3*5 + 6*10 + 9*20 + 1280`).
  2. Sub-target 4.2 (Rank-3 Almost-Simple UOD & Left-Bol Transversal Sweep, deg <= 415):
     - Exact BSGS tree-pruned Lemma 3.2(a) Uniform Orbital Displacement solver (`check_uod_bsgs`)
       across primitive rank-3 AS actions of degree <= 415 (including the full order-13,063,680
       `Aut(srg(126,45,12,18)) = PSU_4(3).2^2` on `NO_6^-(3)`, the 3 sporadic/exceptional Johnson
       actions `PGammaL_2(8)(36)`, `M_23(253)`, `M_24(276)`, and `Omega_7(3)/O_7(3)` on `351, 378`).
     - Exact Left-Bol UOD transversal classifier (`classify_left_bol_uod_transversals`) eliminating
       `A_9(120)`, `Sp_4(4):2(120)`, and `PSU_4(3).2^2(162)`, and confirming collapse to Paige's
       simple Moufang loop `M(2)` inside `O_8^+(2)(120)`.
     - Caveat: Universal completeness of the degree <= 415 rank-3 AS list is conditional on CFSG
       (Bannai 1972; Kantor-Liebler 1982; Liebeck-Saxl 1986). Each individual group elimination
       certified here is unconditionally exact (`CFSG`-free).
  3. Sub-target 4.3 (Primitive HA Twisted p-Element Obstruction & Minimum Order 24 Census):
     - Exhaustive `0`-solution certification of irreducible twisted p-element-quotient subsets
       in `GL_d(p)` across all 7 prime powers `p^d in {4, 8, 9, 16, 25, 27, 32}`.
     - Complete loop-level classification at order `8` (`5` groups + `6` Burn proper left Bol
       loops, all `6` with `|LMlt|=16, |RMlt|=32, |Mlt|=64`, `0` simple; `0` proper in `PGL_2(7)`).
     - Complete exact-factorization census across all `15` pairwise non-isomorphic groups of
       order `24` (proving `Q_24 = Q_{(S_4, C_4, S_3)}` is the unique simple proper exact-fact
       left Bol loop of order `<= 24`), plus first-principles C99 wreath-product imprimitive
       censuses across all composite orders `< 24` (`0` simple proper, pairing with the
       CFSG-free Primitive vs. Imprimitive dichotomy for `n < 24`) and `S_2 wr (S_3 wr S_4)`
       at element orders `d <= 4` (`24` simple proper hits, all `24` isomorphic to `Q_24`).

Run fast default unit test suite (~25s):
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave2_census.py

Run complete exhaustive Wave-2 sweep (including Q_1536 20-loop census, all <= 415 rank-3 AS
cases, and heavy n=16,18,20,21,24 C99 wreath searches via ${TMPDIR:-/tmp}; add --above415 to
also certify G_2(4)(416), NU_6(2)(672), Omega_7(3)(1080), M_24(1288), PSU_6(2)(1408)):
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave2_census.py --full
"""

from __future__ import annotations

from collections import defaultdict, deque
import itertools
import os
import random
import shutil
import subprocess
import sys
import tempfile
import time
from typing import Any, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple
import unittest

from bol_engine import (
    Loop,
    are_loops_isomorphic,
    deduplicate_loops,
    exact_factorization_bol_loop,
    sims_automorphism_group,
)
from known_constructions import (
    build_nagy_exp2_q96,
    build_nagy_q24,
    build_nagy_q60,
    build_nagy_q1536_isotopy_census,
)
from perm_group import Perm, PermGroup, compose, cycles_to_perm, identity_perm, invert
from test_s1_obstructions import (
    _build_f2_orthogonal_or_symplectic,
    _build_psp4_3_isotropic_40,
    _induced_kset_action,
    build_paige_moufang_m2,
    check_uod_on_group,
)

__all__ = [
    "TestWave2Fast",
    "check_uod_bsgs",
    "classify_left_bol_uod_transversals",
    "run_full_wave2_sweep",
]


def _popcount(x: int) -> int:
    """Python 3.9+ compatible bit population count."""
    return bin(x).count("1")


def _find_c_compiler() -> Optional[str]:
    for cand in ("clang", "cc", "gcc"):
        path = shutil.which(cand)
        if path:
            return path
    return None


# ======================================================================
# 1. Exact BSGS-Pruned UOD & Left-Bol UOD Transversal Classifier (4.2)
# ======================================================================


def check_uod_bsgs(
    name: str,
    n: int,
    gens: Sequence[Perm],
    cap_per_suborbit: Optional[int] = None,
) -> Dict[str, Any]:
    """Exact BSGS tree-pruned Uniform Orbital Displacement (UOD) solver on P = <gens> <= Sym(n)."""
    pg = PermGroup(n, gens, initial_base=[0], allow_jordan_fastpath=False)
    assert pg.is_primitive(), f"{name} (deg {n}, |P|={pg.order()}) is NOT primitive"
    sub_orbs = sorted(pg.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o), o[0]))
    r = len(sub_orbs)
    orb_id = [0] * n
    for idx, o in enumerate(sub_orbs):
        for pt in o:
            orb_id[pt] = idx

    tr_inv0 = pg.trans_inv[0]
    color = [[orb_id[tr_inv0[u][v]] for v in range(n)] for u in range(n)]

    active_levels = [lvl for lvl in range(1, len(pg.base)) if len(pg.orbits_list[lvl]) > 1]
    m_act = len(active_levels)

    already_checked = [False] * n
    already_checked[0] = True
    newly_fixed: List[List[int]] = []
    trans_by_act: List[List[Perm]] = []

    for j, lvl in enumerate(active_levels):
        trans_by_act.append(list(pg.trans[lvl].values()))
        if j + 1 < m_act:
            nxt_gens = pg.level_gens[active_levels[j + 1]]
            fixed_now = [
                y
                for y in range(n)
                if (not already_checked[y]) and all(g[y] == y for g in nxt_gens)
            ]
        else:
            fixed_now = [y for y in range(n) if not already_checked[y]]
        b_lvl = pg.base[lvl]
        fixed_now.sort(key=lambda y: (0 if y == b_lvl else 1, y))
        for y in fixed_now:
            already_checked[y] = True
        newly_fixed.append(fixed_now)

    rem_unchecked = [y for y in range(n) if not already_checked[y]]

    uod_counts: List[Tuple[int, int]] = []
    for target_orb in range(1, r):
        x = sub_orbs[target_orb][0]
        u0 = pg.trans[0][x]
        if any(color[y][u0[y]] != target_orb for y in rem_unchecked):
            uod_counts.append((len(sub_orbs[target_orb]), 0))
            continue

        if m_act == 0:
            cnt = 1 if all(color[y][u0[y]] == target_orb for y in range(n)) else 0
            uod_counts.append((len(sub_orbs[target_orb]), cnt))
            continue

        cnt = 0

        def dfs(j: int, cur_p: Perm) -> bool:
            nonlocal cnt
            check_pts = newly_fixed[j]
            is_last = j == m_act - 1
            for u_lvl in trans_by_act[j]:
                ok = True
                for y in check_pts:
                    if color[y][cur_p[u_lvl[y]]] != target_orb:
                        ok = False
                        break
                if not ok:
                    continue
                if is_last:
                    cnt += 1
                    if cap_per_suborbit is not None and cnt >= cap_per_suborbit:
                        return True
                else:
                    if dfs(j + 1, compose(cur_p, u_lvl)):
                        return True
            return False

        dfs(0, u0)
        uod_counts.append((len(sub_orbs[target_orb]), cnt))

    return {
        "name": name,
        "degree": n,
        "order": pg.order(),
        "rank": r,
        "subdegrees": tuple(len(o) for o in sub_orbs),
        "uod_by_suborbit": uod_counts,
        "passes_lemma_3_2a": all(c > 0 for _, c in uod_counts),
    }


def classify_left_bol_uod_transversals(
    name: str,
    n: int,
    gens: Sequence[Perm],
    stop_on_first_proper: bool = True,
    max_loops: Optional[int] = None,
) -> Dict[str, Any]:
    """Exact classifier of left Bol loops Q on {0..n-1} with Mlt(Q) <= P = <gens> sharing P's orbitals.

    Uses:
      1. Exact BSGS extraction of all UOD candidates in every coset x P_0;
      2. Left-Bol power closure (L_x^{-1} and all L_x^k must be UOD);
      3. Pairwise Latin + Bol arc-consistency (L_x L_y L_x in Cand[L_x(L_y(x))]);
      4. Exact Bol-closure backtracking search, checking Moufang vs proper left Bol on every hit.
    """
    id_p = identity_perm(n)
    pg = PermGroup(n, gens, initial_base=[0], allow_jordan_fastpath=False)
    sub_orbs = sorted(pg.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o), o[0]))
    orb_id = [0] * n
    for idx, o in enumerate(sub_orbs):
        for pt in o:
            orb_id[pt] = idx

    tr_inv0 = pg.trans_inv[0]
    color = [[orb_id[tr_inv0[u][v]] for v in range(n)] for u in range(n)]
    active_levels = [lvl for lvl in range(1, len(pg.base)) if len(pg.orbits_list[lvl]) > 1]
    m_act = len(active_levels)
    already = [False] * n
    already[0] = True
    newly_fixed: List[List[int]] = []
    trans_by_act: List[List[Perm]] = []
    for j, lvl in enumerate(active_levels):
        trans_by_act.append(list(pg.trans[lvl].values()))
        nxt_g = pg.level_gens[active_levels[j + 1]] if j + 1 < m_act else []
        fn = [y for y in range(n) if (not already[y]) and all(g[y] == y for g in nxt_g)]
        for y in fn:
            already[y] = True
        newly_fixed.append(fn)
    rem_un = [y for y in range(n) if not already[y]]

    def is_uod(p: Perm) -> bool:
        if p == id_p:
            return True
        t = orb_id[p[0]]
        return all(color[y][p[y]] == t for y in range(n))

    def all_uod_in_coset(x: int) -> List[Perm]:
        target = orb_id[x]
        u0 = pg.trans[0][x]
        if any(color[y][u0[y]] != target for y in rem_un):
            return []
        if m_act == 0:
            return [u0] if is_uod(u0) else []
        found: List[Perm] = []

        def dfs(j: int, cur_p: Perm) -> None:
            for u_lvl in trans_by_act[j]:
                if any(color[y][cur_p[u_lvl[y]]] != target for y in newly_fixed[j]):
                    continue
                np = compose(cur_p, u_lvl)
                if j == m_act - 1:
                    found.append(np)
                else:
                    dfs(j + 1, np)

        dfs(0, u0)
        return found

    def is_semireg(p: Perm) -> bool:
        seen = [False] * n
        ord0 = 0
        for i in range(n):
            if seen[i]:
                continue
            ln = 0
            u = i
            while not seen[u]:
                seen[u] = True
                u = p[u]
                ln += 1
            if ord0 == 0:
                ord0 = ln
            elif ord0 != ln:
                return False
        return ord0 > 1

    st0_gens = pg.level_gens[1] if len(pg.base) > 1 else []
    bol_cands: Dict[int, List[Perm]] = {}
    raw_uod_rep_counts: List[Tuple[int, int]] = []
    orb_conj_maps: List[Tuple[int, List[Tuple[int, Perm, Perm]]]] = []
    for o in sub_orbs[1:]:
        x0 = o[0]
        rc0 = all_uod_in_coset(x0)
        raw_uod_rep_counts.append((len(o), len(rc0)))
        good0: List[Perm] = []
        for p in rc0:
            if not is_semireg(p):
                continue
            ok = is_uod(invert(p))
            cur = compose(p, p)
            while ok and cur != id_p:
                if not is_uod(cur):
                    ok = False
                    break
                cur = compose(cur, p)
            if ok:
                good0.append(p)
        if not good0:
            return {
                "name": name,
                "order": pg.order(),
                "raw_uod": raw_uod_rep_counts,
                "wiped_by_arc_consistency": True,
                "moufang_loops": 0,
                "proper_left_bol_loops": 0,
                "sample_loops": [],
            }
        # Populate bol_cands[x] for all x in o via P_0 conjugation h * good0 * h^{-1}
        bol_cands[x0] = good0
        h_map: Dict[int, Tuple[Perm, Perm]] = {x0: (id_p, id_p)}
        qh = deque([x0])
        while qh:
            u = qh.popleft()
            hu, _ = h_map[u]
            for g in st0_gens:
                v = g[u]
                if v not in h_map:
                    hv = compose(g, hu)
                    hvi = invert(hv)
                    h_map[v] = (hv, hvi)
                    bol_cands[v] = [compose(hv, compose(p, hvi)) for p in good0]
                    qh.append(v)
        assert len(h_map) == len(o)
        orb_conj_maps.append((x0, [(v, h_map[v][0], h_map[v][1]) for v in o if v != x0]))

    cands_sets: Dict[int, Set[Perm]] = {x: set(bol_cands[x]) for x in range(1, n)}
    cands_sets[0] = {id_p}

    def compat(px: Perm, py: Perm) -> bool:
        if any(px[z] == py[z] for z in range(n)):
            return False
        xyx = compose(px, compose(py, px))
        if xyx not in cands_sets[xyx[0]]:
            return False
        yxy = compose(py, compose(px, py))
        if yxy not in cands_sets[yxy[0]]:
            return False
        return True

    changed = True
    while changed:
        changed = False
        for x0, v_list in orb_conj_maps:
            keep: List[Perm] = []
            for px in bol_cands[x0]:
                ix = invert(px)
                if ix not in cands_sets[ix[0]]:
                    continue
                cur = compose(px, px)
                ok_pow = True
                while cur != id_p:
                    if cur not in cands_sets[cur[0]]:
                        ok_pow = False
                        break
                    cur = compose(cur, px)
                if not ok_pow:
                    continue
                if all(any(compat(px, py) for py in bol_cands[y]) for y in range(1, n) if y != x0):
                    keep.append(px)
            if len(keep) < len(bol_cands[x0]):
                changed = True
                if not keep:
                    return {
                        "name": name,
                        "order": pg.order(),
                        "raw_uod": raw_uod_rep_counts,
                        "wiped_by_arc_consistency": True,
                        "moufang_loops": 0,
                        "proper_left_bol_loops": 0,
                        "sample_loops": [],
                    }
                bol_cands[x0] = keep
                cands_sets[x0] = set(keep)
                for v, hv, hvi in v_list:
                    kv = [compose(hv, compose(p, hvi)) for p in keep]
                    bol_cands[v] = kv
                    cands_sets[v] = set(kv)

    chosen: Dict[int, Perm] = {0: id_p}
    moufang_cnt = 0
    proper_cnt = 0
    samples: List[Loop] = []

    def bt() -> bool:
        nonlocal moufang_cnt, proper_cnt
        if len(chosen) == n:
            tbl = [list(chosen[x]) for x in range(n)]
            lp = Loop(tbl, name=f"{name}_hit_{moufang_cnt + proper_cnt}", validate_loop=True)
            is_lb, _ = lp.check_left_bol()
            if not is_lb:
                return False
            # Also verify every R_y lies in P (so Mlt(lp) <= P)
            if not all(pg.contains(lp.R[y]) for y in range(1, n)):
                return False
            is_mf, _ = lp.check_moufang()
            if is_mf:
                moufang_cnt += 1
            else:
                proper_cnt += 1
            if len(samples) < 4:
                samples.append(lp)
            if stop_on_first_proper and proper_cnt > 0:
                return True
            if max_loops is not None and (moufang_cnt + proper_cnt) >= max_loops:
                return True
            return False

        rem = [x for x in range(1, n) if x not in chosen]
        x = min(rem, key=lambda u: (len(bol_cands[u]), u))
        branch_cands = bol_cands[x]
        if len(chosen) == 1 and len(branch_cands) > 1 and st0_gens:
            # Root symmetry reduction: P_{0, x}-conjugation is a loop isomorphism preserving P and x.
            st0_pg = PermGroup(n, st0_gens, initial_base=[x], allow_jordan_fastpath=False)
            p0x_gens = st0_pg.level_gens[1] if len(st0_pg.base) > 1 else []
            if p0x_gens:
                p0x_invs = [invert(g) for g in p0x_gens]
                seen_c: Set[Perm] = set()
                reps_c: List[Perm] = []
                cand_pool = set(branch_cands)
                for c0 in branch_cands:
                    if c0 in seen_c:
                        continue
                    reps_c.append(c0)
                    seen_c.add(c0)
                    qc = deque([c0])
                    while qc:
                        cur_c = qc.popleft()
                        for g, gi in zip(p0x_gens, p0x_invs):
                            nc = compose(g, compose(cur_c, gi))
                            if nc in cand_pool and nc not in seen_c:
                                seen_c.add(nc)
                                qc.append(nc)
                branch_cands = reps_c
        for px in branch_cands:
            to_add: Dict[int, Perm] = {x: px}
            q_cl = [px]
            ok = True
            while q_cl and ok:
                a = q_cl.pop()
                ia = invert(a)
                for unary in (ia, compose(a, a)):
                    u0 = unary[0]
                    if u0 in chosen:
                        if chosen[u0] != unary:
                            ok = False
                            break
                    elif u0 in to_add:
                        if to_add[u0] != unary:
                            ok = False
                            break
                    elif unary in cands_sets[u0]:
                        to_add[u0] = unary
                        q_cl.append(unary)
                    else:
                        ok = False
                        break
                if not ok:
                    break
                cur_vals = list(chosen.values()) + list(to_add.values())
                for b in cur_vals:
                    for prod in (compose(a, compose(b, a)), compose(b, compose(a, b))):
                        z0 = prod[0]
                        if z0 in chosen:
                            if chosen[z0] != prod:
                                ok = False
                                break
                        elif z0 in to_add:
                            if to_add[z0] != prod:
                                ok = False
                                break
                        elif prod in cands_sets[z0]:
                            to_add[z0] = prod
                            q_cl.append(prod)
                        else:
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                new_items = list(to_add.items())
                for idx_i, (_, pi) in enumerate(new_items):
                    if any(pi[w] == pj[w] for pj in chosen.values() for w in range(n)):
                        ok = False
                        break
                    for _, pj in new_items[idx_i + 1 :]:
                        if any(pi[w] == pj[w] for w in range(n)):
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                chosen.update(to_add)
                if bt():
                    return True
                for uk in to_add:
                    del chosen[uk]
        return False

    bt()
    return {
        "name": name,
        "order": pg.order(),
        "raw_uod": raw_uod_rep_counts,
        "wiped_by_arc_consistency": False,
        "moufang_loops": moufang_cnt,
        "proper_left_bol_loops": proper_cnt,
        "sample_loops": samples,
    }


# ======================================================================
# 2. Rank-3 AS Group Builders (deg <= 415, including #49 §2 upgrades)
# ======================================================================


def build_sp_quadric_actions(dim: int) -> Tuple[Tuple[int, List[Perm]], Tuple[int, List[Perm]]]:
    """Sp_dim(2) on elliptic O^- and hyperbolic O^+ quadratic forms polarizing to B."""

    def b_form(x: int, y: int) -> int:
        acc = 0
        for i in range(0, dim, 2):
            acc ^= (((x >> i) & 1) & ((y >> (i + 1)) & 1)) ^ (((x >> (i + 1)) & 1) & ((y >> i) & 1))
        return acc

    def q0_plus(x: int) -> int:
        acc = 0
        for i in range(dim // 2):
            acc ^= ((x >> (2 * i)) & 1) & ((x >> (2 * i + 1)) & 1)
        return acc

    plus_vs = [v for v in range(1 << dim) if q0_plus(v) == 0]
    minus_vs = [v for v in range(1 << dim) if q0_plus(v) == 1]
    p_idx = {v: i for i, v in enumerate(plus_vs)}
    m_idx = {v: i for i, v in enumerate(minus_vs)}

    gen_as = [1 << i for i in range(dim)] + [
        (1 << i) ^ (1 << j) for i in range(dim) for j in range(i + 1, dim)
    ]
    plus_gens: List[Perm] = []
    minus_gens: List[Perm] = []
    for a in gen_as:
        shift = a if q0_plus(a) == 0 else 0
        plus_gens.append(tuple(p_idx[(v ^ (a if b_form(v, a) else 0)) ^ shift] for v in plus_vs))
        minus_gens.append(tuple(m_idx[(v ^ (a if b_form(v, a) else 0)) ^ shift] for v in minus_vs))
    return (len(minus_vs), minus_gens), (len(plus_vs), plus_gens)


def build_pgammal2_8_and_a9() -> Tuple[List[Perm], List[Perm]]:
    """Return (PGammaL_2(8) on C(9,2) deg 36, A_9 on cosets of PGammaL_2(8) deg 120)."""
    f8_pow = [1]
    for _ in range(7):
        v = f8_pow[-1] << 1
        if v & 8:
            v ^= 0b1011
        f8_pow.append(v)
    f8_log = {f8_pow[i]: i for i in range(7)}

    def f8_mul(a: int, b: int) -> int:
        return 0 if (a == 0 or b == 0) else f8_pow[(f8_log[a] + f8_log[b]) % 7]

    t8 = tuple((z ^ 1) if z < 8 else 8 for z in range(9))
    m8 = tuple(f8_mul(2, z) if z < 8 else 8 for z in range(9))
    inv8 = tuple((8 if z == 0 else (0 if z == 8 else f8_pow[(7 - f8_log[z]) % 7])) for z in range(9))
    frob8 = tuple(f8_mul(z, z) if z < 8 else 8 for z in range(9))
    h_gens = [t8, m8, inv8, frob8]
    _, g_pgl28_36 = _induced_kset_action(9, 2, h_gens)

    a9_gens = [cycles_to_perm(9, [[0, 1, 2]]), cycles_to_perm(9, [[0, 1, 2, 3, 4, 5, 6, 7, 8]])]
    h_el = sorted(PermGroup(9, h_gens, allow_jordan_fastpath=False).enumerate_elements())
    assert len(h_el) == 1512

    def canon_coset(g: Perm) -> Perm:
        return min(compose(g, h) for h in h_el)

    c0 = canon_coset(identity_perm(9))
    coset_reps = [c0]
    c_to_i = {c0: 0}
    q = deque([c0])
    while q:
        r = q.popleft()
        for gen in a9_gens:
            cr = canon_coset(compose(gen, r))
            if cr not in c_to_i:
                c_to_i[cr] = len(coset_reps)
                coset_reps.append(cr)
                q.append(cr)
    assert len(coset_reps) == 120
    gens_120 = [tuple(c_to_i[canon_coset(compose(gen, r))] for r in coset_reps) for gen in a9_gens]
    return g_pgl28_36, gens_120


def build_a10_s10_deg126() -> Tuple[List[Perm], List[Perm]]:
    """A_10 and S_10 on unordered {5, 5}-bipartitions of {0..9} -> deg 126."""
    parts = [s for s in itertools.combinations(range(10), 5) if 0 in s]
    to_i = {s: i for i, s in enumerate(parts)}
    full = set(range(10))

    def induce(g: Perm) -> Perm:
        out = []
        for s in parts:
            img = {g[x] for x in s}
            if 0 not in img:
                img = full - img
            out.append(to_i[tuple(sorted(img))])  # type: ignore[index]
        return tuple(out)

    a10_base = [cycles_to_perm(10, [[0, 1, 2]]), cycles_to_perm(10, [[1, 2, 3, 4, 5, 6, 7, 8, 9]])]
    s10_base = [cycles_to_perm(10, [[0, 1]]), cycles_to_perm(10, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])]
    return [induce(g) for g in a10_base], [induce(g) for g in s10_base]


def build_mathieu_2set_actions() -> List[Tuple[str, int, List[Perm]]]:
    """M_11(55), M_12(66), M_23(253), and M_24(276) on 2-sets (#49 §2.2)."""
    a11 = tuple((x + 1) % 11 for x in range(11))
    b11 = tuple((4 * pow(x, 2, 11) - 3 * pow(x, 7, 11)) % 11 for x in range(11))
    assert PermGroup(11, [a11, b11], allow_jordan_fastpath=False).order() == 7920
    _, g_m11_55 = _induced_kset_action(11, 2, [a11, b11])

    a12 = tuple(((x + 1) % 11) if x < 11 else 11 for x in range(12))
    b12 = tuple(((4 * pow(x, 2, 11) - 3 * pow(x, 7, 11)) % 11) if x < 11 else 11 for x in range(12))
    c12 = cycles_to_perm(12, [[0, 11], [1, 10], [2, 5], [3, 7], [4, 8], [6, 9]])
    assert PermGroup(12, [a12, b12, c12], allow_jordan_fastpath=False).order() == 95040
    _, g_m12_66 = _induced_kset_action(12, 2, [a12, b12, c12])

    c23 = tuple((i + 1) % 23 for i in range(23))
    b23_1idx = [[3, 17, 10, 7, 9], [4, 13, 14, 19, 5], [8, 18, 11, 12, 23], [15, 20, 22, 21, 16]]
    b23 = cycles_to_perm(23, [[x - 1 for x in cyc] for cyc in b23_1idx])
    assert PermGroup(23, [c23, b23], allow_jordan_fastpath=False).order() == 10_200_960
    _, g_m23_253 = _induced_kset_action(23, 2, [c23, b23])

    c24 = tuple(((i + 1) % 23) if i < 23 else 23 for i in range(24))
    b24 = cycles_to_perm(24, [[x - 1 for x in cyc] for cyc in b23_1idx])
    d24 = tuple(23 if z == 0 else (0 if z == 23 else (5 * pow(z, 21, 23)) % 23) for z in range(24))
    assert PermGroup(24, [c24, b24, d24], allow_jordan_fastpath=False).order() == 244_823_040
    _, g_m24_276 = _induced_kset_action(24, 2, [c24, b24, d24])

    return [
        ("M_11 on 2-sets (deg 55)", 55, g_m11_55),
        ("M_12 on 2-sets (deg 66)", 66, g_m12_66),
        ("M_23 on 2-sets (deg 253)", 253, g_m23_253),
        ("M_24 on 2-sets (deg 276)", 276, g_m24_276),
    ]


def build_psu3_5_deg50() -> List[Tuple[str, int, List[Perm]]]:
    """PSU_3(5) (126,000) & PSU_3(5):2 (252,000) on Hoffman-Singleton srg(50, 7, 0, 1)."""
    adj = [0] * 50

    def add_e(u: int, v: int) -> None:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for i in range(5):
        for j in range(5):
            add_e(5 * i + j, 5 * i + ((j + 1) % 5))
            add_e(25 + 5 * i + j, 25 + 5 * i + ((j + 2) % 5))
            for k in range(5):
                add_e(5 * i + j, 25 + 5 * k + ((i * k + j) % 5))

    def find_aut_mapping(img0: int, img_n0_first2: Tuple[int, int]) -> Optional[Perm]:
        n0 = [v for v in range(50) if (adj[0] >> v) & 1]
        ni0 = [v for v in range(50) if (adj[img0] >> v) & 1]
        for perm_n0 in itertools.permutations(ni0):
            if perm_n0[0] != img_n0_first2[0] or perm_n0[1] != img_n0_first2[1]:
                continue
            u_a, v_a = n0[0], perm_n0[0]
            nu_a = [x for x in range(50) if x != 0 and ((adj[u_a] >> x) & 1)]
            nv_a = [x for x in range(50) if x != img0 and ((adj[v_a] >> x) & 1)]
            for perm_na in itertools.permutations(nv_a):
                mp = {0: img0}
                for x, y in zip(n0, perm_n0):
                    mp[x] = y
                for x, y in zip(nu_a, perm_na):
                    mp[x] = y
                ok = True
                for j_idx in range(1, 7):
                    uj, vj = n0[j_idx], perm_n0[j_idx]
                    for z in (x for x in range(50) if x != 0 and ((adj[uj] >> x) & 1)):
                        nb_in_nua = [w for w in nu_a if (adj[z] >> w) & 1]
                        if len(nb_in_nua) != 1:
                            ok = False
                            break
                        common = adj[vj] & adj[mp[nb_in_nua[0]]]
                        if _popcount(common) != 1:
                            ok = False
                            break
                        mp[z] = common.bit_length() - 1
                    if not ok:
                        break
                if ok and len(set(mp.values())) == 50:
                    cand = tuple(mp[i] for i in range(50))
                    if all(
                        ((adj[u] >> v) & 1) == ((adj[cand[u]] >> cand[v]) & 1)
                        for u in range(50)
                        for v in range(u + 1, 50)
                    ):
                        return cand
        return None

    n0 = [v for v in range(50) if (adj[0] >> v) & 1]
    gens_50: List[Perm] = []
    ni1 = [v for v in range(50) if (adj[n0[0]] >> v) & 1]
    for a, b in itertools.permutations(ni1, 2):
        g = find_aut_mapping(n0[0], (a, b))
        if g is not None:
            gens_50.append(g)
            break
    g_tr = find_aut_mapping(0, (n0[1], n0[0]))
    g_cy = find_aut_mapping(0, (n0[1], n0[2]))
    assert g_tr is not None and g_cy is not None
    gens_50.extend([g_tr, g_cy])
    for a, b in itertools.permutations(n0, 2):
        if (a, b) not in ((n0[0], n0[1]), (n0[1], n0[0]), (n0[1], n0[2])):
            g_ex = find_aut_mapping(0, (a, b))
            if g_ex is not None:
                gens_50.append(g_ex)
                if PermGroup(50, gens_50, allow_jordan_fastpath=False).order() == 252_000:
                    break
    aut_hs50 = PermGroup(50, gens_50, allow_jordan_fastpath=False)
    assert aut_hs50.order() == 252_000
    psu35 = aut_hs50.derived_subgroup()
    assert psu35.order() == 126_000
    return [
        ("PSU_3(5) on Hoff-Sing (deg 50)", 50, list(psu35.generators)),
        ("PSU_3(5):2 on Hoff-Sing (deg 50)", 50, list(aut_hs50.generators)),
    ]


def build_psl3_4_deg56_and_psu4_3_deg162(
    include_deg162: bool = True,
) -> List[Tuple[str, int, List[Perm]]]:
    """PSL_3(4) through PSL_3(4).2^2 on Gewirtz (deg 56) & PSU_4(3).2^2 on srg(162, 56, 10, 24)."""
    mul4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    inv4 = [0, 1, 3, 2]
    frob4 = [0, 1, 3, 2]

    pts21 = [
        v
        for v in itertools.product(range(4), repeat=3)
        if v != (0, 0, 0) and next(c for c in v if c != 0) == 1
    ]
    p_idx = {v: i for i, v in enumerate(pts21)}

    def norm3(v: Tuple[int, int, int]) -> int:
        ic = inv4[next(c for c in v if c != 0)]
        return p_idx[(mul4[v[0]][ic], mul4[v[1]][ic], mul4[v[2]][ic])]

    def mat_perm(m: Tuple[Tuple[int, int, int], ...]) -> Perm:
        return tuple(
            norm3(
                tuple(  # type: ignore[arg-type]
                    mul4[m[r][0]][x0] ^ mul4[m[r][1]][x1] ^ mul4[m[r][2]][x2] for r in range(3)
                )
            )
            for x0, x1, x2 in pts21
        )

    psl_21 = [
        mat_perm(((1, 1, 0), (0, 1, 0), (0, 0, 1))),
        mat_perm(((1, 2, 0), (0, 1, 0), (0, 0, 1))),
        mat_perm(((0, 1, 0), (0, 0, 1), (1, 0, 0))),
        mat_perm(((2, 0, 0), (0, 3, 0), (0, 0, 1))),
    ]
    frob_21 = tuple(norm3((frob4[x0], frob4[x1], frob4[x2])) for x0, x1, x2 in pts21)

    o0: FrozenSet[int] = frozenset(
        i
        for i, (x0, x1, x2) in enumerate(pts21)
        if (mul4[x0][x0] ^ mul4[x1][x2]) == 0 or (x0, x1, x2) == (1, 0, 0)
    )
    orb_56_set: Set[FrozenSet[int]] = {o0}
    q_o = deque([o0])
    while q_o:
        cur = q_o.popleft()
        for g in psl_21:
            nxt = frozenset(g[x] for x in cur)
            if nxt not in orb_56_set:
                orb_56_set.add(nxt)
                q_o.append(nxt)
    orb_56 = sorted(orb_56_set, key=lambda s: sorted(s))
    o_to_i = {b: i for i, b in enumerate(orb_56)}

    g_psl_56 = [tuple(o_to_i[frozenset(g[x] for x in b)] for b in orb_56) for g in psl_21]
    g_frob_56 = tuple(o_to_i[frozenset(frob_21[x] for x in b)] for b in orb_56)

    lines_21 = [
        frozenset(
            i
            for i, (x0, x1, x2) in enumerate(pts21)
            if (mul4[a][x0] ^ mul4[b][x1] ^ mul4[c][x2]) == 0
        )
        for a, b, c in pts21
    ]
    dual_cand = [frozenset(di for di, ln in enumerate(lines_21) if ln.isdisjoint(b)) for b in orb_56]
    if all(d in o_to_i for d in dual_cand):
        g_dual_56: Optional[Perm] = tuple(o_to_i[d] for d in dual_cand)
    else:
        g_dual_56 = None
        for sc in (2, 3):
            sc_p = tuple(norm3((mul4[sc][x0], x1, x2)) for x0, x1, x2 in pts21)
            shifted = [frozenset(sc_p[x] for x in d) for d in dual_cand]
            if all(s in o_to_i for s in shifted):
                g_dual_56 = tuple(o_to_i[s] for s in shifted)
                break
    assert g_dual_56 is not None
    out: List[Tuple[str, int, List[Perm]]] = [
        ("PSL_3(4) on Gewirtz (deg 56)", 56, g_psl_56),
        ("PSigmaL_3(4) on Gewirtz (deg 56)", 56, g_psl_56 + [g_frob_56]),
        ("PSL_3(4).2^2 on Gewirtz (deg 56)", 56, g_psl_56 + [g_frob_56, g_dual_56]),
    ]
    if not include_deg162:
        return out

    l_idx = {ln: i for i, ln in enumerate(lines_21)}
    flags105 = [(pi, li) for pi in range(21) for li in range(21) if pi in lines_21[li]]
    f_idx = {fl: i for i, fl in enumerate(flags105)}
    psl_fg = [
        tuple(f_idx[(g[p], l_idx[frozenset(g[x] for x in lines_21[li])])] for p, li in flags105)
        for g in psl_21 + [frob_21]
    ]
    pg105 = PermGroup(105, psl_fg, initial_base=[0], allow_jordan_fastpath=False)
    orbs_f0 = [o for o in pg105.stabilizer_orbits(0) if len(o) == 16]
    all_105_el = pg105.enumerate_elements()
    eds_f = {(g[0], g[c[0]]) for c in orbs_f0 for g in all_105_el}
    adj = [0] * 162
    for i in range(56):
        adj[0] |= 1 << (1 + i)
        adj[1 + i] |= 1
        for j in range(i + 1, 56):
            if orb_56[i].isdisjoint(orb_56[j]):
                adj[1 + i] |= 1 << (1 + j)
                adj[1 + j] |= 1 << (1 + i)
        for fi, (p, li) in enumerate(flags105):
            if p not in orb_56[i] and len(lines_21[li] & orb_56[i]) == 2:
                adj[1 + i] |= 1 << (57 + fi)
                adj[57 + fi] |= 1 << (1 + i)
    for u, v in eds_f:
        adj[57 + u] |= 1 << (57 + v)
        adj[57 + v] |= 1 << (57 + u)

    g_base_162 = [
        tuple(
            [0]
            + [1 + o_to_i[frozenset(g[x] for x in b)] for b in orb_56]
            + [57 + gf[fi] for fi in range(105)]
        )
        for g, gf in zip(psl_21 + [frob_21], psl_fg)
    ]

    def refine162(cur: List[int]) -> List[int]:
        while True:
            sigs = []
            for v in range(162):
                nbc: Dict[int, int] = defaultdict(int)
                m = adj[v]
                while m:
                    lb = m & -m
                    nbc[cur[lb.bit_length() - 1]] += 1
                    m ^= lb
                sigs.append((cur[v], tuple(sorted(nbc.items()))))
            uq = sorted(set(sigs))
            mp = {s: idx for idx, s in enumerate(uq)}
            nxt = [mp[s] for s in sigs]
            if len(uq) == len(set(cur)):
                return nxt
            cur = nxt

    def match_wl162(c1: List[int], c2: List[int]) -> Optional[Perm]:
        r1, r2 = refine162(c1), refine162(c2)
        cnt1: Dict[int, List[int]] = defaultdict(list)
        cnt2: Dict[int, List[int]] = defaultdict(list)
        for i in range(162):
            cnt1[r1[i]].append(i)
            cnt2[r2[i]].append(i)
        if sorted(cnt1) != sorted(cnt2) or any(len(cnt1[k]) != len(cnt2[k]) for k in cnt1):
            return None
        if len(cnt1) == 162:
            cand = tuple(cnt2[r1[i]][0] for i in range(162))
            return (
                cand
                if all(
                    ((adj[u] >> v) & 1) == ((adj[cand[u]] >> cand[v]) & 1)
                    for u in range(162)
                    for v in range(u + 1, 162)
                )
                else None
            )
        sc = min((k for k, vs in cnt1.items() if len(vs) > 1), key=lambda k: len(cnt1[k]))
        nid = max(cnt1) + 1
        nc1 = list(r1)
        nc1[cnt1[sc][0]] = nid
        for vs in cnt2[sc]:
            nc2 = list(r2)
            nc2[vs] = nid
            res = match_wl162(nc1, nc2)
            if res is not None:
                return res
        return None

    sw162 = match_wl162(
        [0 if i == 0 else (1 if i == 1 else 2) for i in range(162)],
        [1 if i == 0 else (0 if i == 1 else 2) for i in range(162)],
    )
    assert sw162 is not None
    pg162 = PermGroup(162, g_base_162 + [sw162], allow_jordan_fastpath=False)
    assert pg162.order() == 13_063_680
    out.append(("PSU_4(3).2^2 on srg(162,56,10,24) (deg 162)", 162, list(pg162.generators)))
    return out


def build_no6_f3_actions() -> List[Tuple[str, int, List[Perm]]]:
    """NO_6^+(3) (deg 117) & NO_6^-(3) (deg 126, certifying full order 13,063,680 PSU_4(3).2^2!)."""
    out_cases: List[Tuple[str, int, List[Perm]]] = []
    for eps in ("+", "-"):

        def q_f3(v: Tuple[int, ...]) -> int:
            base = (v[0] * v[1] + v[2] * v[3]) % 3
            if eps == "+":
                return (base + v[4] * v[5]) % 3
            return (base + v[4] * v[4] + v[5] * v[5]) % 3

        def b_f3(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
            base = (x[0] * y[1] + x[1] * y[0] + x[2] * y[3] + x[3] * y[2]) % 3
            if eps == "+":
                return (base + x[4] * y[5] + x[5] * y[4]) % 3
            return (base + 2 * x[4] * y[4] + 2 * x[5] * y[5]) % 3

        pts: List[Tuple[int, ...]] = []
        refl_plus: List[Tuple[int, ...]] = []
        refl_minus: List[Tuple[int, ...]] = []
        for v in itertools.product(range(3), repeat=6):
            if v == (0, 0, 0, 0, 0, 0) or next(c for c in v if c != 0) != 1:
                continue
            qv = q_f3(v)
            if qv == 1:
                pts.append(v)
                refl_plus.append(v)
            elif qv == 2:
                refl_minus.append(v)

        deg = len(pts)
        assert deg == (117 if eps == "+" else 126)
        to_i = {v: i for i, v in enumerate(pts)}

        def norm6(v: Tuple[int, ...]) -> int:
            inv_c = 1 if next(c for c in v if c != 0) == 1 else 2
            return to_i[tuple((x * inv_c) % 3 for x in v)]

        def refl_perm(a: Tuple[int, ...]) -> Perm:
            qa_inv = 1 if q_f3(a) == 1 else 2
            return tuple(
                norm6(tuple((x[k] - ((b_f3(x, a) * qa_inv) % 3) * a[k]) % 3 for k in range(6)))
                for x in pts
            )

        rng = random.Random(323)
        rp = [refl_perm(a) for a in rng.sample(refl_plus, 14)]
        rm = [refl_perm(a) for a in rng.sample(refl_minus, 14)]
        po_pg = PermGroup(deg, rp + rm, allow_jordan_fastpath=False)
        pom_pg = po_pg.derived_subgroup()
        if eps == "+":
            assert pom_pg.order() == 6_065_280 and po_pg.order() == 12_130_560
            out_cases.append(("POmega_6^+(3) on NO_6^+(3) (deg 117)", 117, list(pom_pg.generators)))
            out_cases.append(("PO_6^+(3) on NO_6^+(3) (deg 117)", 117, list(po_pg.generators)))
        else:
            # Explicit certification for #49 §2.1: full Aut(srg(126, 45, 12, 18)) = PSU_4(3).2^2 (13,063,680)
            assert pom_pg.order() == 3_265_920
            assert po_pg.order() == 13_063_680
            out_cases.append(("POmega_6^-(3) on NO_6^-(3) (deg 126)", 126, list(pom_pg.generators)))
            out_cases.append(
                ("PSU_4(3).2^2 = Aut(srg(126)) on NO_6^-(3) (deg 126)", 126, list(po_pg.generators))
            )
    return out_cases


def build_sp4_4_quadric_actions() -> List[Tuple[str, int, List[Perm]]]:
    """Sp_4(4) (979,200) & Sp_4(4):2 (1,958,400) on O_4^-(4) (deg 120) & O_4^+(4) (deg 136)."""
    mul4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    sq4 = [0, 1, 3, 2]
    vecs = list(itertools.product(range(4), repeat=4))

    def b4(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        return mul4[x[0]][y[1]] ^ mul4[x[1]][y[0]] ^ mul4[x[2]][y[3]] ^ mul4[x[3]][y[2]]

    def q0(x: Tuple[int, ...]) -> int:
        return mul4[x[0]][x[1]] ^ mul4[x[2]][x[3]]

    plus_vs: List[Tuple[int, ...]] = []
    minus_vs: List[Tuple[int, ...]] = []
    for v in vecs:
        zeros = sum(1 for x in vecs if (q0(x) ^ sq4[b4(x, v)]) == 0)
        if zeros == 76:
            plus_vs.append(v)
        else:
            assert zeros == 52
            minus_vs.append(v)
    p_to_i = {v: i for i, v in enumerate(plus_vs)}
    m_to_i = {v: i for i, v in enumerate(minus_vs)}
    basis = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

    def induce_transv(
        a: Tuple[int, ...],
        c: int,
        pool: List[Tuple[int, ...]],
        mp: Dict[Tuple[int, ...], int],
    ) -> Perm:
        t_basis = []
        for e in basis:
            cb = mul4[c][b4(e, a)]
            t_basis.append(tuple(e[k] ^ mul4[cb][a[k]] for k in range(4)))
        out = []
        for v in pool:
            vals = [sq4[q0(te) ^ sq4[b4(te, v)]] for te in t_basis]
            out.append(mp[(vals[1], vals[0], vals[3], vals[2])])
        return tuple(out)

    rng = random.Random(323)
    nz_vecs = [v for v in vecs if v != (0, 0, 0, 0)]
    sample_as = basis + rng.sample(nz_vecs, 12)
    sp_120 = [induce_transv(a, c, minus_vs, m_to_i) for a in sample_as for c in (1, 2)]
    sp_136 = [induce_transv(a, c, plus_vs, p_to_i) for a in sample_as for c in (1, 2)]
    frob_120 = tuple(m_to_i[tuple(sq4[c] for c in v)] for v in minus_vs)
    frob_136 = tuple(p_to_i[tuple(sq4[c] for c in v)] for v in plus_vs)
    return [
        ("Sp_4(4) on O_4^-(4) (deg 120)", 120, sp_120),
        ("Sp_4(4):2 on O_4^-(4) (deg 120)", 120, sp_120 + [frob_120]),
        ("Sp_4(4) on O_4^+(4) (deg 136)", 136, sp_136),
        ("Sp_4(4):2 on O_4^+(4) (deg 136)", 136, sp_136 + [frob_136]),
    ]


def build_nu5_2_deg176() -> List[Tuple[str, int, List[Perm]]]:
    """PSU_5(2) (13,685,760) & PGammaU_5(2) (27,371,520) on NU_5(2) (deg 176)."""
    mul4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    inv4 = [0, 1, 3, 2]
    conj4 = [0, 1, 3, 2]

    def h5(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        acc = 0
        for k in range(5):
            acc ^= mul4[x[k]][conj4[y[k]]]
        return acc

    pts = [
        v
        for v in itertools.product(range(4), repeat=5)
        if v != (0, 0, 0, 0, 0) and next(c for c in v if c != 0) == 1 and h5(v, v) == 1
    ]
    assert len(pts) == 176
    to_i = {v: i for i, v in enumerate(pts)}

    def norm5(v: Tuple[int, ...]) -> int:
        ic = inv4[next(c for c in v if c != 0)]
        return to_i[tuple(mul4[x][ic] for x in v)]

    rng = random.Random(323)
    centers = pts[:5] + rng.sample(pts, 14)
    psu_gens = [
        tuple(
            norm5(tuple(x[k] ^ mul4[mul4[2][h5(x, a)]][a[k]] for k in range(5))) for x in pts
        )
        for a in centers
    ]
    frob_176 = tuple(norm5(tuple(conj4[c] for c in x)) for x in pts)
    return [
        ("PSU_5(2) on NU_5(2) (deg 176)", 176, psu_gens),
        ("PGammaU_5(2) on NU_5(2) (deg 176)", 176, psu_gens + [frob_176]),
    ]


def build_no7_f3_actions() -> List[Tuple[str, int, List[Perm]]]:
    """Omega_7(3) & O_7(3) on NO_7^-(3) (deg 351) and NO_7^+(3) (deg 378, covering G_2(3)(351,378))."""
    pts1: List[Tuple[int, ...]] = []
    pts2: List[Tuple[int, ...]] = []
    for v in itertools.product(range(3), repeat=7):
        if v == (0,) * 7 or next(c for c in v if c != 0) != 1:
            continue
        qv = (v[0] * v[1] + v[2] * v[3] + v[4] * v[5] + v[6] * v[6]) % 3
        if qv == 1:
            pts1.append(v)
        elif qv == 2:
            pts2.append(v)
    assert len(pts1) == 378 and len(pts2) == 351

    def b7(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        return (
            x[0] * y[1] + x[1] * y[0] + x[2] * y[3] + x[3] * y[2]
            + x[4] * y[5] + x[5] * y[4] + 2 * x[6] * y[6]
        ) % 3

    out: List[Tuple[str, int, List[Perm]]] = []
    for pts, eps in ((pts2, "-"), (pts1, "+")):
        deg = len(pts)
        to_i = {v: i for i, v in enumerate(pts)}

        def norm7(v: Tuple[int, ...]) -> int:
            ic = 1 if next(c for c in v if c != 0) == 1 else 2
            return to_i[tuple((x * ic) % 3 for x in v)]

        def refl7(a: Tuple[int, ...], qa_inv: int) -> Perm:
            return tuple(
                norm7(tuple((x[k] - ((b7(x, a) * qa_inv) % 3) * a[k]) % 3 for k in range(7)))
                for x in pts
            )

        rng = random.Random(323)
        g1 = [refl7(a, 1) for a in rng.sample(pts1, 14)]
        g2 = [refl7(a, 2) for a in rng.sample(pts2, 14)]
        po7 = PermGroup(deg, g1 + g2, allow_jordan_fastpath=False)
        om7 = po7.derived_subgroup()
        assert om7.order() == 4_585_351_680 and po7.order() == 9_170_703_360
        out.append((f"Omega_7(3) on NO_7^{eps}(3) (deg {deg})", deg, list(om7.generators)))
        out.append((f"O_7(3) on NO_7^{eps}(3) (deg {deg})", deg, list(po7.generators)))
    return out


def build_m22_176_m23_253_and_mcl_275() -> List[Tuple[str, int, List[Perm]]]:
    """M_22 on A_7 cosets (176), M_23 on S(4,7,23) heptads (253), and McL / McL:2 on srg(275)."""
    c23 = tuple((i + 1) % 23 for i in range(23))
    b23_1idx = [[3, 17, 10, 7, 9], [4, 13, 14, 19, 5], [8, 18, 11, 12, 23], [15, 20, 22, 21, 16]]
    b23 = cycles_to_perm(23, [[x - 1 for x in cyc] for cyc in b23_1idx])
    m23 = PermGroup(23, [c23, b23], initial_base=[0, 1, 2, 3], allow_jordan_fastpath=False)
    assert m23.order() == 10_200_960
    orb3 = next(
        o for o in PermGroup(23, m23.level_gens[4], allow_jordan_fastpath=False).orbits() if len(o) == 3
    )
    h0: FrozenSet[int] = frozenset([0, 1, 2, 3] + list(orb3))
    hepts_s: Set[FrozenSet[int]] = {h0}
    q = deque([h0])
    while q:
        cur = q.popleft()
        for g in (c23, b23):
            nxt = frozenset(g[x] for x in cur)
            if nxt not in hepts_s:
                hepts_s.add(nxt)
                q.append(nxt)
    hepts = sorted(hepts_s, key=lambda s: sorted(s))
    assert len(hepts) == 253
    hp_to_i = {h: i for i, h in enumerate(hepts)}
    g_m23_hepts = [tuple(hp_to_i[frozenset(g[x] for x in h)] for h in hepts) for g in (c23, b23)]

    h77 = sorted((h - {22} for h in hepts_s if 22 in h), key=lambda s: sorted(s))
    b176 = sorted((h for h in hepts_s if 22 not in h), key=lambda s: sorted(s))
    h_to_i = {h: i for i, h in enumerate(h77)}
    b_to_i = {b: i for i, b in enumerate(b176)}

    m22_23 = PermGroup(23, m23.generators, initial_base=[22], allow_jordan_fastpath=False)
    g_m22_176 = [
        tuple(b_to_i[frozenset(g[x] for x in b)] for b in b176) for g in m22_23.level_gens[1]
    ]

    adj = [0] * 275

    def add_e(u: int, v: int) -> None:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    for p in range(22):
        for hi, h in enumerate(h77):
            if p not in h:
                add_e(p, 22 + hi)
        for bi, b in enumerate(b176):
            if p in b:
                add_e(p, 99 + bi)
    for hi, h in enumerate(h77):
        for hj in range(hi + 1, 77):
            if h.isdisjoint(h77[hj]):
                add_e(22 + hi, 22 + hj)
        for bi, b in enumerate(b176):
            if len(h & b) == 3:
                add_e(22 + hi, 99 + bi)
    for bi, b in enumerate(b176):
        for bj in range(bi + 1, 176):
            if len(b & b176[bj]) == 1:
                add_e(99 + bi, 99 + bj)

    g_m22_275 = [
        tuple(
            [g[p] for p in range(22)]
            + [22 + h_to_i[frozenset(g[x] for x in h)] for h in h77]
            + [99 + b_to_i[frozenset(g[x] for x in b)] for b in b176]
        )
        for g in m22_23.level_gens[1]
    ]

    def refine275(cur: List[int]) -> List[int]:
        while True:
            sigs = []
            for v in range(275):
                nbc: Dict[int, int] = defaultdict(int)
                m = adj[v]
                while m:
                    lb = m & -m
                    nbc[cur[lb.bit_length() - 1]] += 1
                    m ^= lb
                sigs.append((cur[v], tuple(sorted(nbc.items()))))
            uq = sorted(set(sigs))
            mp = {s: idx for idx, s in enumerate(uq)}
            nxt = [mp[s] for s in sigs]
            if len(uq) == len(set(cur)):
                return nxt
            cur = nxt

    def match_wl275(c1: List[int], c2: List[int]) -> Optional[Perm]:
        r1, r2 = refine275(c1), refine275(c2)
        cnt1: Dict[int, List[int]] = defaultdict(list)
        cnt2: Dict[int, List[int]] = defaultdict(list)
        for i in range(275):
            cnt1[r1[i]].append(i)
            cnt2[r2[i]].append(i)
        if sorted(cnt1) != sorted(cnt2) or any(len(cnt1[k]) != len(cnt2[k]) for k in cnt1):
            return None
        if len(cnt1) == 275:
            cand = tuple(cnt2[r1[i]][0] for i in range(275))
            return (
                cand
                if all(
                    ((adj[u] >> v) & 1) == ((adj[cand[u]] >> cand[v]) & 1)
                    for u in range(275)
                    for v in range(u + 1, 275)
                )
                else None
            )
        sc = min((k for k, vs in cnt1.items() if len(vs) > 1), key=lambda k: len(cnt1[k]))
        nid = max(cnt1) + 1
        nc1 = list(r1)
        nc1[cnt1[sc][0]] = nid
        for vs in cnt2[sc]:
            nc2 = list(r2)
            nc2[vs] = nid
            res = match_wl275(nc1, nc2)
            if res is not None:
                return res
        return None

    sw = match_wl275(
        [0 if i == 0 else (1 if i == 22 else 2) for i in range(275)],
        [1 if i == 0 else (0 if i == 22 else 2) for i in range(275)],
    )
    assert sw is not None
    pg_first = PermGroup(275, g_m22_275 + [sw], initial_base=[0, 1, 22], allow_jordan_fastpath=False)
    if pg_first.order() == 1_796_256_000:
        pg_aut_mcl: Optional[PermGroup] = pg_first
        pg_mcl = pg_aut_mcl.derived_subgroup()
    else:
        pg_mcl = pg_first
        st2 = PermGroup(275, pg_mcl.level_gens[1], initial_base=[22], allow_jordan_fastpath=False)
        st0_22 = PermGroup(275, st2.level_gens[1], allow_jordan_fastpath=False)
        o_small = next(o for o in st0_22.orbits() if len(o) > 1)
        pg_aut_mcl = None
        for v_cand in range(1, 275):
            if (
                v_cand not in o_small
                and ((adj[0] >> v_cand) & 1) == ((adj[0] >> o_small[0]) & 1)
                and ((adj[22] >> v_cand) & 1) == ((adj[22] >> o_small[0]) & 1)
            ):
                c1 = [0] * 275
                c2 = [0] * 275
                c1[0] = c2[0] = 1
                c1[22] = c2[22] = 2
                c1[o_small[0]] = 3
                c2[v_cand] = 3
                ext = match_wl275(c1, c2)
                if ext is not None:
                    pg_aut_mcl = PermGroup(
                        275, list(pg_mcl.generators) + [ext], initial_base=[0, 1, 22], allow_jordan_fastpath=False
                    )
                    break
    assert pg_mcl.order() == 898_128_000
    assert pg_aut_mcl is not None and pg_aut_mcl.order() == 1_796_256_000
    return [
        ("M_22 on A_7 cosets (deg 176)", 176, g_m22_176),
        ("M_23 on S(4,7,23) heptads (deg 253)", 253, g_m23_hepts),
        ("McL on McLaughlin srg(275) (deg 275)", 275, list(pg_mcl.generators)),
        ("Aut(McL) = McL:2 on srg(275) (deg 275)", 275, list(pg_aut_mcl.generators)),
    ]


def build_above_415_rank3_actions() -> Tuple[List[Tuple[str, int, List[Perm]]], Tuple[str, int, List[Perm]]]:
    """Construct 10 rank-3 AS overgroup actions above deg 415 (#45 §3.3 / #54):
      - G_2(4) & G_2(4):2 on srg(416, 100, 36, 20) (deg 416),
      - PSU_6(2), PSU_6(2):2, PGU_6(2), PGU_6(2):2 on NU_6(2) (deg 672),
      - M_24 on complementary Golay dodecad pairs (deg 1288),
      - PSU_6(2) & PSU_6(2):2 on Mitchell U_4(3).2 cosets (deg 1408),
    plus (returned separately) Omega_7(3) on G_2(3) octonion cosets (deg 1080), which passes
    single-element UOD with [(351, 64), (728, 441)] and is eliminated by left-Bol arc-consistency.
    """
    rng = random.Random(323)
    uod_zero_cases: List[Tuple[str, int, List[Perm]]] = []

    # 1. G_2(4) & G_2(4):2 on deg 416 via Hermitian orthogonal bases of PG(2, 16)
    gf16_mul = [[0] * 16 for _ in range(16)]
    for a in range(16):
        for b in range(16):
            p, aa, bb = 0, a, b
            for _ in range(4):
                if bb & 1:
                    p ^= aa
                carry = aa & 8
                aa = (aa << 1) & 15
                if carry:
                    aa ^= 3
                bb >>= 1
            gf16_mul[a][b] = p
    gf16_inv = [0] * 16
    for a in range(1, 16):
        for b in range(1, 16):
            if gf16_mul[a][b] == 1:
                gf16_inv[a] = b
    gf16_p4 = [gf16_mul[gf16_mul[a][a]][gf16_mul[a][a]] for a in range(16)]
    gf16_p2 = [gf16_mul[a][a] for a in range(16)]

    def h16(u: Tuple[int, int, int], v: Tuple[int, int, int]) -> int:
        return (
            gf16_mul[u[0]][gf16_p4[v[0]]]
            ^ gf16_mul[u[1]][gf16_p4[v[1]]]
            ^ gf16_mul[u[2]][gf16_p4[v[2]]]
        )

    noniso16: List[Tuple[int, int, int]] = []
    iso16: List[Tuple[int, int, int]] = []
    for x0 in range(16):
        for x1 in range(16):
            for x2 in range(16):
                if (x0, x1, x2) == (0, 0, 0):
                    continue
                first = x0 if x0 else (x1 if x1 else x2)
                if first != 1:
                    continue
                v16 = (x0, x1, x2)
                (iso16 if h16(v16, v16) == 0 else noniso16).append(v16)
    ni16_idx = {v: i for i, v in enumerate(noniso16)}
    perp_ni = [set() for _ in range(208)]
    for i in range(208):
        for j in range(i + 1, 208):
            if h16(noniso16[i], noniso16[j]) == 0:
                perp_ni[i].add(j)
                perp_ni[j].add(i)
    bases416 = [
        (i, j, k)
        for i in range(208)
        for j in sorted(perp_ni[i])
        if j > i
        for k in sorted(perp_ni[i] & perp_ni[j])
        if k > j
    ]
    assert len(bases416) == 416
    b416_i = {b: idx for idx, b in enumerate(bases416)}

    def norm16(v: Tuple[int, int, int]) -> Tuple[int, int, int]:
        first = v[0] if v[0] else (v[1] if v[1] else v[2])
        invf = gf16_inv[first]
        return (gf16_mul[v[0]][invf], gf16_mul[v[1]][invf], gf16_mul[v[2]][invf])

    f4_c = next(a for a in range(1, 16) if gf16_p4[a] == a)
    u_gens_416: List[Perm] = []
    for a16 in rng.sample(iso16, 10):
        mp_ni = [
            ni16_idx[
                norm16(
                    (
                        v[0] ^ gf16_mul[f4_c][gf16_mul[h16(v, a16)][a16[0]]],
                        v[1] ^ gf16_mul[f4_c][gf16_mul[h16(v, a16)][a16[1]]],
                        v[2] ^ gf16_mul[f4_c][gf16_mul[h16(v, a16)][a16[2]]],
                    )
                )
            ]
            for v in noniso16
        ]
        u_gens_416.append(tuple(b416_i[tuple(sorted((mp_ni[b[0]], mp_ni[b[1]], mp_ni[b[2]])))] for b in bases416))  # type: ignore[index]
    frob_ni16 = [ni16_idx[norm16((gf16_p2[v[0]], gf16_p2[v[1]], gf16_p2[v[2]]))] for v in noniso16]
    u_gens_416.append(tuple(b416_i[tuple(sorted((frob_ni16[b[0]], frob_ni16[b[1]], frob_ni16[b[2]])))] for b in bases416))  # type: ignore[index]
    pg_u34 = PermGroup(416, u_gens_416, initial_base=[0], allow_jordan_fastpath=False)
    st0_416 = PermGroup(416, pg_u34.level_gens[1], allow_jordan_fastpath=False)
    orb100 = next(o for o in st0_416.orbits() if len(o) == 100)
    adj416 = [0] * 416
    qe416 = deque([(0, orb100[0])])
    seen416 = {(0, orb100[0]), (orb100[0], 0)}
    while qe416:
        u, v = qe416.popleft()
        adj416[u] |= 1 << v
        adj416[v] |= 1 << u
        for g in u_gens_416:
            gu, gv = g[u], g[v]
            if (gu, gv) not in seen416:
                seen416.add((gu, gv))
                seen416.add((gv, gu))
                qe416.append((gu, gv))

    def refine416(cur: List[int]) -> List[int]:
        while True:
            sigs = []
            for v in range(416):
                nbc: Dict[int, int] = defaultdict(int)
                m = adj416[v]
                while m:
                    lb = m & -m
                    nbc[cur[lb.bit_length() - 1]] += 1
                    m ^= lb
                sigs.append((cur[v], tuple(sorted(nbc.items()))))
            uq = sorted(set(sigs))
            mp = {s: idx for idx, s in enumerate(uq)}
            nxt = [mp[s] for s in sigs]
            if len(uq) == len(set(cur)):
                return nxt
            cur = nxt

    def match_wl416(c1: List[int], c2: List[int]) -> Optional[Perm]:
        r1, r2 = refine416(c1), refine416(c2)
        cnt1: Dict[int, List[int]] = defaultdict(list)
        cnt2: Dict[int, List[int]] = defaultdict(list)
        for i in range(416):
            cnt1[r1[i]].append(i)
            cnt2[r2[i]].append(i)
        if sorted(cnt1) != sorted(cnt2) or any(len(cnt1[k]) != len(cnt2[k]) for k in cnt1):
            return None
        if len(cnt1) == 416:
            cand = tuple(cnt2[r1[i]][0] for i in range(416))
            return (
                cand
                if all(
                    ((adj416[u] >> v) & 1) == ((adj416[cand[u]] >> cand[v]) & 1)
                    for u in range(416)
                    for v in range(u + 1, 416)
                )
                else None
            )
        sc = min((k for k, vs in cnt1.items() if len(vs) > 1), key=lambda k: len(cnt1[k]))
        nid = max(cnt1) + 1
        nc1 = list(r1)
        nc1[cnt1[sc][0]] = nid
        for vs in cnt2[sc]:
            nc2 = list(r2)
            nc2[vs] = nid
            res = match_wl416(nc1, nc2)
            if res is not None:
                return res
        return None

    orb15 = next(o for o in st0_416.orbits() if len(o) == 15)
    orb150 = next(o for o in st0_416.orbits() if len(o) == 150)
    c1_416 = [0] * 416
    c2_416 = [0] * 416
    c1_416[0] = c2_416[0] = 1
    c1_416[orb15[0]] = 2
    c2_416[orb150[0]] = 2
    fus416 = match_wl416(c1_416, c2_416)
    assert fus416 is not None
    pg_g24_2 = PermGroup(416, u_gens_416 + [fus416], initial_base=[0], allow_jordan_fastpath=False)
    assert pg_g24_2.order() == 503_193_600
    pg_g24 = pg_g24_2.derived_subgroup()
    assert pg_g24.order() == 251_596_800
    uod_zero_cases.append(("G_2(4) on srg(416,100,36,20) (deg 416)", 416, list(pg_g24.generators)))
    uod_zero_cases.append(("G_2(4):2 on srg(416,100,36,20) (deg 416)", 416, list(pg_g24_2.generators)))

    # 2. NU_6(2) (deg 672) and PSU_6(2) / :2 on Mitchell U_4(3).2 cosets (deg 1408)
    mul4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
    conj4 = [0, 1, 3, 2]

    def h4_6(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        s = 0
        for k in range(6):
            s ^= mul4[x[k]][conj4[y[k]]]
        return s

    iso6: List[Tuple[int, ...]] = []
    noniso6: List[Tuple[int, ...]] = []
    for v in itertools.product(range(4), repeat=6):
        if v == (0, 0, 0, 0, 0, 0) or next(c for c in v if c != 0) != 1:
            continue
        (iso6 if h4_6(v, v) == 0 else noniso6).append(v)
    assert len(iso6) == 693 and len(noniso6) == 672
    ni6_idx = {v: i for i, v in enumerate(noniso6)}
    iso6_idx = {v: i for i, v in enumerate(iso6)}

    def norm4_6(v: Tuple[int, ...]) -> Tuple[int, ...]:
        ic = conj4[next(c for c in v if c != 0)]
        return tuple(mul4[c][ic] for c in v)

    sample_iso6 = rng.sample(iso6, 14)
    psu62_672 = [
        tuple(ni6_idx[norm4_6(tuple(v[k] ^ mul4[h4_6(v, a)][a[k]] for k in range(6)))] for v in noniso6)
        for a in sample_iso6
    ]
    psu62_iso = [
        tuple(iso6_idx[norm4_6(tuple(v[k] ^ mul4[h4_6(v, a)][a[k]] for k in range(6)))] for v in iso6)
        for a in sample_iso6
    ]
    diag_672 = tuple(ni6_idx[norm4_6((mul4[2][v[0]], v[1], v[2], v[3], v[4], v[5]))] for v in noniso6)
    frob_672 = tuple(ni6_idx[norm4_6(tuple(conj4[c] for c in v))] for v in noniso6)
    frob_iso = tuple(iso6_idx[norm4_6(tuple(conj4[c] for c in v))] for v in iso6)
    uod_zero_cases.extend(
        [
            ("PSU_6(2) on NU_6(2) (deg 672)", 672, psu62_672),
            ("PSU_6(2):2 on NU_6(2) (deg 672)", 672, psu62_672 + [frob_672]),
            ("PGU_6(2) on NU_6(2) (deg 672)", 672, psu62_672 + [diag_672]),
            ("PGU_6(2):2 on NU_6(2) (deg 672)", 672, psu62_672 + [diag_672, frob_672]),
        ]
    )

    # 3. M_24 on complementary Golay dodecad pairs (deg 1288)
    b23_1idx = [[3, 17, 10, 7, 9], [4, 13, 14, 19, 5], [8, 18, 11, 12, 23], [15, 20, 22, 21, 16]]
    c24 = tuple(((i + 1) % 23) if i < 23 else 23 for i in range(24))
    b24 = cycles_to_perm(24, [[x - 1 for x in cyc] for cyc in b23_1idx])
    d24 = tuple(23 if z == 0 else (0 if z == 23 else (5 * pow(z, 21, 23)) % 23) for z in range(24))
    m24_gens = [c24, b24, d24]
    m23_tmp = PermGroup(
        23,
        [tuple((i + 1) % 23 for i in range(23)), cycles_to_perm(23, [[x - 1 for x in cyc] for cyc in b23_1idx])],
        initial_base=[0, 1, 2, 3],
        allow_jordan_fastpath=False,
    )
    orb3_m23 = next(o for o in PermGroup(23, m23_tmp.level_gens[4], allow_jordan_fastpath=False).orbits() if len(o) == 3)
    oct0 = sum(1 << x for x in ([0, 1, 2, 3] + list(orb3_m23) + [23]))
    octs = {oct0}
    qo = deque([oct0])
    while qo:
        cur_o = qo.popleft()
        for g in m24_gens:
            img_o = 0
            mm = cur_o
            while mm:
                lb = mm & -mm
                img_o |= 1 << g[lb.bit_length() - 1]
                mm ^= lb
            if img_o not in octs:
                octs.add(img_o)
                qo.append(img_o)
    c24_set = {0}
    for oc in octs:
        if oc not in c24_set:
            c24_set |= {x ^ oc for x in list(c24_set)}
        if len(c24_set) == 4096:
            break
    all_ones24 = (1 << 24) - 1
    dod_pairs = sorted({min(cw, cw ^ all_ones24) for cw in c24_set if _popcount(cw) == 12})
    assert len(dod_pairs) == 1288
    dp_idx = {d: i for i, d in enumerate(dod_pairs)}
    m24_1288: List[Perm] = []
    for g in m24_gens:
        p1288 = []
        for d in dod_pairs:
            img_d = 0
            mm = d
            while mm:
                lb = mm & -mm
                img_d |= 1 << g[lb.bit_length() - 1]
                mm ^= lb
            p1288.append(dp_idx[min(img_d, img_d ^ all_ones24)])
        m24_1288.append(tuple(p1288))
    uod_zero_cases.append(("M_24 on dodecad pairs (deg 1288)", 1288, m24_1288))

    # 4. PSU_6(2) & PSU_6(2):2 on Mitchell U_4(3).2 cosets (deg 1408)
    exp_of = {1: 0, 2: 1, 3: 2}
    mask0_126 = 0
    for idx_i, v in enumerate(iso6):
        nz = [c for c in v if c != 0]
        if len(nz) == 2 or (len(nz) == 6 and sum(exp_of[c] for c in nz) % 3 == 0):
            mask0_126 |= 1 << idx_i
    orb1408 = [mask0_126]
    m_to_1408 = {mask0_126: 0}
    q1408 = deque([mask0_126])
    while q1408:
        cur_m = q1408.popleft()
        bs = []
        mm = cur_m
        while mm:
            lb = mm & -mm
            bs.append(lb.bit_length() - 1)
            mm ^= lb
        for g in psu62_iso + [frob_iso]:
            nm_m = 0
            for b in bs:
                nm_m |= 1 << g[b]
            if nm_m not in m_to_1408:
                m_to_1408[nm_m] = len(orb1408)
                orb1408.append(nm_m)
                q1408.append(nm_m)
    assert len(orb1408) == 1408
    bits1408 = []
    for m in orb1408:
        bs = []
        mm = m
        while mm:
            lb = mm & -mm
            bs.append(lb.bit_length() - 1)
            mm ^= lb
        bits1408.append(bs)
    psu62_1408 = [tuple(m_to_1408[sum(1 << g[b] for b in bs)] for bs in bits1408) for g in psu62_iso]
    frob_1408 = tuple(m_to_1408[sum(1 << frob_iso[b] for b in bs)] for bs in bits1408)
    uod_zero_cases.append(("PSU_6(2) on U_4(3).2 cosets (deg 1408)", 1408, psu62_1408))
    uod_zero_cases.append(("PSU_6(2):2 on U_4(3).2^2 cosets (deg 1408)", 1408, psu62_1408 + [frob_1408]))

    # 5. Omega_7(3) on G_2(3) octonion cosets (deg 1080)
    cross0 = [[(0,) * 7 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        ca, cb, cc = i, (i + 1) % 7, (i + 3) % 7
        for cu, cv, cw in ((ca, cb, cc), (cb, cc, ca), (cc, ca, cb)):
            lv1 = [0] * 7
            lv1[cw] = 1
            cross0[cu][cv] = tuple(lv1)
            lv2 = [0] * 7
            lv2[cw] = 2
            cross0[cv][cu] = tuple(lv2)

    def pack_vec7(v7: Sequence[int]) -> int:
        s = 0
        for c in v7:
            s = s * 3 + c
        return s

    vecs7_q1 = [
        v
        for v in itertools.product(range(3), repeat=7)
        if v != (0,) * 7 and next(c for c in v if c != 0) == 1 and sum(c * c for c in v) % 3 == 1
    ]

    def refl7_mat(a7: Tuple[int, ...]) -> Tuple[Tuple[int, ...], ...]:
        return tuple(tuple(((1 if i == j else 0) + a7[i] * a7[j]) % 3 for j in range(7)) for i in range(7))

    def mm7(m_a: Tuple[Tuple[int, ...], ...], m_b: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
        return tuple(tuple(sum(m_a[i][k] * m_b[k][j] for k in range(7)) % 3 for j in range(7)) for i in range(7))

    r0_7 = refl7_mat(vecs7_q1[0])
    om7_mats = [mm7(r0_7, refl7_mat(a7)) for a7 in rng.sample(vecs7_q1[1:], 10)]
    om7_invs = [tuple(tuple(m_a[j][i] for j in range(7)) for i in range(7)) for m_a in om7_mats]

    def apply_mat_tbl(
        m_a: Tuple[Tuple[int, ...], ...], m_inv: Tuple[Tuple[int, ...], ...], enc: Tuple[int, ...]
    ) -> Tuple[int, ...]:
        tbl = [[[0] * 7 for _ in range(7)] for _ in range(7)]
        idx_e = 0
        for i in range(7):
            for j in range(i + 1, 7):
                val = enc[idx_e]
                idx_e += 1
                for k in range(6, -1, -1):
                    c = val % 3
                    val //= 3
                    tbl[i][j][k] = c
                    tbl[j][i][k] = (3 - c) % 3
        out_e = []
        for a in range(7):
            ua = [m_inv[i][a] for i in range(7)]
            for b in range(a + 1, 7):
                ub = [m_inv[j][b] for j in range(7)]
                res_t = [0] * 7
                for i in range(7):
                    if ua[i]:
                        for j in range(7):
                            if ub[j] and i != j:
                                coef = (ua[i] * ub[j]) % 3
                                tij = tbl[i][j]
                                for k in range(7):
                                    if tij[k]:
                                        res_t[k] = (res_t[k] + coef * tij[k]) % 3
                out_e.append(pack_vec7([sum(m_a[r][k] * res_t[k] for k in range(7)) % 3 for r in range(7)]))
        return tuple(out_e)

    enc0 = tuple(pack_vec7(cross0[i][j]) for i in range(7) for j in range(i + 1, 7))
    orb1080 = [enc0]
    t_to_1080 = {enc0: 0}
    q1080 = deque([enc0])
    while q1080:
        cur_t = q1080.popleft()
        for m_a, m_inv in zip(om7_mats, om7_invs):
            nxt_t = apply_mat_tbl(m_a, m_inv, cur_t)
            if nxt_t not in t_to_1080:
                t_to_1080[nxt_t] = len(orb1080)
                orb1080.append(nxt_t)
                q1080.append(nxt_t)
    assert len(orb1080) == 1080
    om7_1080 = [tuple(t_to_1080[apply_mat_tbl(m_a, m_inv, c)] for c in orb1080) for m_a, m_inv in zip(om7_mats, om7_invs)]
    return uod_zero_cases, ("Omega_7(3) on G_2(3) cosets (deg 1080)", 1080, om7_1080)


# ======================================================================
# 3. Sub-target 4.3A: Affine HA Twisted p-Element Quotient Verifier
# ======================================================================

_HA_F2_C_SRC = r"""
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static inline uint32_t mv_f2(uint32_t A, uint32_t v, int d) {
    uint32_t r = 0;
    for (int j = 0; j < d; j++) if ((v >> j) & 1u) r ^= (A >> (5 * j)) & 31u;
    return r;
}
static inline uint32_t mm_f2(uint32_t A, uint32_t B, int d) {
    uint32_t C = 0;
    for (int j = 0; j < d; j++) C |= (mv_f2(A, (B >> (5 * j)) & 31u, d) << (5 * j));
    return C;
}
static inline uint32_t id_f2(int d) {
    uint32_t I = 0;
    for (int j = 0; j < d; j++) I |= ((1u << j) << (5 * j));
    return I;
}
static inline int ord_2_f2(uint32_t A, int d, uint32_t I) {
    if (A == I) return 1;
    uint32_t A2 = mm_f2(A, A, d); if (A2 == I) return 2;
    uint32_t A4 = mm_f2(A2, A2, d); if (A4 == I) return 4;
    uint32_t A8 = mm_f2(A4, A4, d); if (A8 == I) return 8;
    return 0;
}
static inline uint32_t inv_2_elem_f2(uint32_t A, int d) {
    uint32_t A2 = mm_f2(A, A, d), A4 = mm_f2(A2, A2, d);
    return mm_f2(A4, mm_f2(A2, A, d), d);
}
static inline uint32_t inv_gen_f2(uint32_t A, int d) {
    uint32_t rows_L[5], rows_R[5];
    for (int i = 0; i < d; i++) {
        uint32_t rl = 0;
        for (int j = 0; j < d; j++) rl |= (((A >> (5 * j + i)) & 1u) << j);
        rows_L[i] = rl; rows_R[i] = (1u << i);
    }
    for (int col = 0; col < d; col++) {
        int piv = col;
        while (!((rows_L[piv] >> col) & 1u)) piv++;
        uint32_t tl = rows_L[col]; rows_L[col] = rows_L[piv]; rows_L[piv] = tl;
        uint32_t tr = rows_R[col]; rows_R[col] = rows_R[piv]; rows_R[piv] = tr;
        for (int r = 0; r < d; r++) if (r != col && ((rows_L[r] >> col) & 1u)) {
            rows_L[r] ^= rows_L[col]; rows_R[r] ^= rows_R[col];
        }
    }
    uint32_t invA = 0;
    for (int i = 0; i < d; i++)
        for (int j = 0; j < d; j++)
            if ((rows_R[i] >> j) & 1u) invA |= (1u << (5 * j + i));
    return invA;
}

static uint32_t *all_gl = NULL, *all_2_els = NULL;
static int *all_2_ords = NULL, num_gl = 0, num_2_els = 0, found_irred = 0;

static void gen_gl_f2(int d, int col_idx, uint32_t cur_A, uint32_t basis[5], uint32_t I) {
    if (col_idx == d) {
        all_gl[num_gl++] = cur_A;
        if (cur_A != I) {
            int o = ord_2_f2(cur_A, d, I);
            if (o > 0) { all_2_els[num_2_els] = cur_A; all_2_ords[num_2_els++] = o; }
        }
        return;
    }
    for (uint32_t v = 1; v < (1u << d); v++) {
        uint32_t w = v;
        for (int b = 0; b < col_idx; b++) if ((w ^ basis[b]) < w) w ^= basis[b];
        if (w != 0) {
            uint32_t nb[5]; memcpy(nb, basis, sizeof(nb)); nb[col_idx] = w;
            for (int i = col_idx; i > 0 && nb[i] > nb[i-1]; i--) { uint32_t t = nb[i]; nb[i] = nb[i-1]; nb[i-1] = t; }
            gen_gl_f2(d, col_idx + 1, cur_A | (v << (5 * col_idx)), nb, I);
        }
    }
}

static uint32_t find_min_subspace_f2(const uint32_t *M, int m_len, int d) {
    uint32_t full_mask = (d == 5) ? 0xFFFFFFFFu : ((1u << (1 << d)) - 1u), best_mask = 0;
    int best_pop = 999;
    for (uint32_t v0 = 1; v0 < (1u << d); v0++) {
        uint32_t span_mask = 1u | (1u << v0), q[32];
        int pop = 2, qh = 0, qt = 0; q[qt++] = v0;
        while (qh < qt) {
            uint32_t u = q[qh++];
            for (int i = 0; i < m_len; i++) {
                uint32_t w = mv_f2(M[i], u, d);
                if (!((span_mask >> w) & 1u)) {
                    uint32_t old = span_mask;
                    for (uint32_t z = 0; z < (1u << d); z++) if ((old >> z) & 1u) {
                        uint32_t zw = z ^ w;
                        if (!((span_mask >> zw) & 1u)) { span_mask |= (1u << zw); pop++; q[qt++] = zw; }
                    }
                }
            }
        }
        if (span_mask != full_mask && pop < best_pop) {
            best_pop = pop; best_mask = span_mask;
            if (pop == 2) return best_mask;
        }
    }
    return best_mask;
}

static int close_twisted_f2(uint32_t *M, int *m_len, int max_sz, int max_ord, int d, uint32_t I) {
    int idx = 0;
    while (idx < *m_len) {
        uint32_t a = M[idx++], ia = inv_2_elem_f2(a, d);
        int cur_len = *m_len;
        for (int pass = -1; pass < 2 * cur_len; pass++) {
            uint32_t cand = (pass == -1) ? ia : (pass < cur_len)
                ? mm_f2(a, mm_f2(M[pass], a, d), d)
                : mm_f2(M[pass - cur_len], mm_f2(a, M[pass - cur_len], d), d);
            int present = 0;
            for (int k = 0; k < *m_len; k++) if (M[k] == cand) { present = 1; break; }
            if (!present) {
                if (*m_len >= max_sz) return 0;
                int oc = ord_2_f2(cand, d, I);
                if (oc == 0 || oc > max_ord) return 0;
                uint32_t icand = inv_2_elem_f2(cand, d);
                for (int k = 0; k < *m_len; k++) {
                    if (ord_2_f2(mm_f2(inv_2_elem_f2(M[k], d), cand, d), d, I) == 0) return 0;
                    if (ord_2_f2(mm_f2(icand, M[k], d), d, I) == 0) return 0;
                }
                M[(*m_len)++] = cand;
            }
        }
    }
    return 1;
}

static void dfs_irred_f2(const uint32_t *M, int m_len, const uint32_t *pool, int pool_len, int max_ord, int d, uint32_t I) {
    uint32_t sub_mask = find_min_subspace_f2(M, m_len, d);
    if (sub_mask == 0) { found_irred++; return; }
    int max_sz = 1 << d;
    if (m_len >= max_sz || pool_len == 0) return;
    uint8_t *mv_arr = malloc((size_t)pool_len);
    for (int i = 0; i < pool_len; i++) {
        uint32_t X = pool[i]; int moves_out = 0;
        for (uint32_t u = 1; u < (1u << d); u++)
            if (((sub_mask >> u) & 1u) && !((sub_mask >> mv_f2(X, u, d)) & 1u)) { moves_out = 1; break; }
        mv_arr[i] = (uint8_t)moves_out;
    }
    for (int i = 0; i < pool_len; i++) {
        if (!mv_arr[i]) continue;
        uint32_t X = pool[i];
        uint32_t Mn[64]; memcpy(Mn, M, m_len * sizeof(uint32_t));
        int mn_len = m_len; Mn[mn_len++] = X;
        if (close_twisted_f2(Mn, &mn_len, max_sz, max_ord, d, I)) {
            int n_new = mn_len - m_len; uint32_t new_inv[64];
            for (int k = 0; k < n_new; k++) new_inv[k] = inv_2_elem_f2(Mn[m_len + k], d);
            uint32_t *next_pool = malloc((size_t)pool_len * sizeof(uint32_t));
            int np_len = 0;
            for (int j = 0; j < pool_len; j++) {
                if (j <= i && mv_arr[j]) continue;
                uint32_t Y = pool[j]; int in_Mn = 0;
                for (int k = m_len; k < mn_len; k++) if (Mn[k] == Y) { in_Mn = 1; break; }
                if (in_Mn) continue;
                uint32_t iY = inv_2_elem_f2(Y, d); int ok = 1;
                for (int k = 0; k < n_new; k++)
                    if (ord_2_f2(mm_f2(new_inv[k], Y, d), d, I) == 0 || ord_2_f2(mm_f2(iY, Mn[m_len + k], d), d, I) == 0) { ok = 0; break; }
                if (ok) next_pool[np_len++] = Y;
            }
            dfs_irred_f2(Mn, mn_len, next_pool, np_len, max_ord, d, I);
            free(next_pool);
            if (found_irred) { free(mv_arr); return; }
        }
    }
    free(mv_arr);
}

static uint32_t jordan_block_f2(const int *part, int p_len) {
    uint32_t A = 0; int pos = 0;
    for (int b = 0; b < p_len; b++) {
        for (int k = 0; k < part[b]; k++) {
            uint32_t col = 1u << (pos + k);
            if (k > 0) col |= 1u << (pos + k - 1);
            A |= (col << (5 * (pos + k)));
        }
        pos += part[b];
    }
    return A;
}

int main(int argc, char **argv) {
    int max_d = (argc >= 2) ? atoi(argv[1]) : 5;
    all_gl = malloc(10500000 * sizeof(uint32_t));
    all_2_els = malloc(1100000 * sizeof(uint32_t));
    all_2_ords = malloc(1100000 * sizeof(int));
    const int p2[1][1] = {{2}};
    const int p3[2][2] = {{2,1}, {3,0}};
    const int p4[4][3] = {{2,1,1}, {2,2,0}, {3,1,0}, {4,0,0}};
    const int p5[6][4] = {{2,1,1,1}, {2,2,1,0}, {3,1,1,0}, {3,2,0,0}, {4,1,0,0}, {5,0,0,0}};
    for (int d = 2; d <= max_d; d++) {
        num_gl = num_2_els = found_irred = 0;
        uint32_t I = id_f2(d), basis[5] = {0};
        gen_gl_f2(d, 0, 0, basis, I);
        int n_parts = (d==2)?1 : (d==3)?2 : (d==4)?4 : 6;
        for (int r = 0; r < n_parts; r++) {
            int part[4] = {0}, plen = 0;
            for (int k = 0; k < 4; k++) {
                int v = (d==2)?(k<1?p2[r][k]:0) : (d==3)?(k<2?p3[r][k]:0) : (d==4)?(k<3?p4[r][k]:0) : p5[r][k];
                if (v > 0) part[plen++] = v;
            }
            uint32_t A0 = jordan_block_f2(part, plen);
            int max_ord = ord_2_f2(A0, d, I), m0_len = 2;
            uint32_t M0[64] = {I, A0};
            if (!close_twisted_f2(M0, &m0_len, 1 << d, max_ord, d, I)) continue;
            uint32_t invM0[64];
            for (int k = 0; k < m0_len; k++) invM0[k] = inv_2_elem_f2(M0[k], d);
            uint32_t *pool0 = malloc((size_t)(num_2_els + 1) * sizeof(uint32_t));
            int p0_len = 0;
            for (int i = 0; i < num_2_els; i++) {
                if (all_2_ords[i] > max_ord) continue;
                uint32_t Y = all_2_els[i]; int in_M0 = 0;
                for (int k = 0; k < m0_len; k++) if (M0[k] == Y) { in_M0 = 1; break; }
                if (in_M0) continue;
                uint32_t iY = inv_2_elem_f2(Y, d); int ok = 1;
                for (int k = 0; k < m0_len; k++)
                    if (ord_2_f2(mm_f2(invM0[k], Y, d), d, I) == 0 || ord_2_f2(mm_f2(iY, M0[k], d), d, I) == 0) { ok = 0; break; }
                if (ok) pool0[p0_len++] = Y;
            }
            uint32_t *cent = malloc(65536 * sizeof(uint32_t)), *cent_inv = malloc(65536 * sizeof(uint32_t));
            int cent_len = 0;
            for (int g = 0; g < num_gl; g++) {
                uint32_t P = all_gl[g];
                if (mm_f2(P, A0, d) == mm_f2(A0, P, d)) { cent[cent_len] = P; cent_inv[cent_len++] = inv_gen_f2(P, d); }
            }
            uint32_t ker_mask = 1u;
            for (uint32_t u = 1; u < (1u << d); u++) if (mv_f2(A0, u, d) == u) ker_mask |= (1u << u);
            uint8_t *dead = calloc(1u << 25, 1);
            for (int idx1 = 0; idx1 < p0_len; idx1++) {
                uint32_t X1 = pool0[idx1];
                if (dead[X1]) continue;
                int mv_out = 0;
                for (uint32_t u = 1; u < (1u << d); u++)
                    if (((ker_mask >> u) & 1u) && !((ker_mask >> mv_f2(X1, u, d)) & 1u)) { mv_out = 1; break; }
                if (!mv_out) continue;
                uint32_t M1[64]; memcpy(M1, M0, m0_len * sizeof(uint32_t));
                int m1_len = m0_len; M1[m1_len++] = X1;
                if (close_twisted_f2(M1, &m1_len, 1 << d, max_ord, d, I)) {
                    int n_new = m1_len - m0_len; uint32_t n_inv[64];
                    for (int k = 0; k < n_new; k++) n_inv[k] = inv_2_elem_f2(M1[m0_len + k], d);
                    uint32_t *npool = malloc((size_t)(p0_len + 1) * sizeof(uint32_t));
                    int nplen = 0;
                    for (int j = 0; j < p0_len; j++) {
                        uint32_t Y = pool0[j]; int in_M1 = 0;
                        for (int k = m0_len; k < m1_len; k++) if (M1[k] == Y) { in_M1 = 1; break; }
                        if (in_M1) continue;
                        uint32_t iY = inv_2_elem_f2(Y, d); int ok = 1;
                        for (int k = 0; k < n_new; k++)
                            if (ord_2_f2(mm_f2(n_inv[k], Y, d), d, I) == 0 || ord_2_f2(mm_f2(iY, M1[m0_len + k], d), d, I) == 0) { ok = 0; break; }
                        if (ok) npool[nplen++] = Y;
                    }
                    dfs_irred_f2(M1, m1_len, npool, nplen, max_ord, d, I);
                    free(npool);
                }
                for (int c = 0; c < cent_len; c++) dead[mm_f2(cent[c], mm_f2(X1, cent_inv[c], d), d)] = 1;
            }
            free(dead); free(cent); free(cent_inv); free(pool0);
        }
        printf("d=%d found_irred=%d\n", d, found_irred);
        if (found_irred != 0) return 2;
    }
    free(all_gl); free(all_2_els); free(all_2_ords);
    return 0;
}
"""


def verify_ha_odd_or_small_python(p: int, d: int) -> int:
    """Pure-Python verifier of irreducible twisted p-element-quotient subsets in GL_d(p)
    for small prime powers (e.g. p^d in {4, 8, 9, 25, 27}). Returns number of irreducible hits (0).
    """
    vecs = [v for v in itertools.product(range(p), repeat=d)]
    nz_vecs = [v for v in vecs if any(c != 0 for c in v)]
    id_m = tuple(tuple(1 if i == j else 0 for j in range(d)) for i in range(d))

    def mv(m: Tuple[Tuple[int, ...], ...], v: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(sum(m[i][j] * v[j] for j in range(d)) % p for i in range(d))

    def mm(a: Tuple[Tuple[int, ...], ...], b: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
        return tuple(
            tuple(sum(a[i][k] * b[k][j] for k in range(d)) % p for j in range(d)) for i in range(d)
        )

    def p_ord(a: Tuple[Tuple[int, ...], ...]) -> int:
        if a == id_m:
            return 1
        cur = a
        pw = 1
        for _ in range(d):
            cur = mm(cur, cur) if p == 2 else (mm(cur, mm(cur, cur)) if p == 3 else mm(cur, mm(cur, mm(cur, mm(cur, cur)))))
            pw *= p
            if cur == id_m:
                return pw
        return 0

    def p_inv(a: Tuple[Tuple[int, ...], ...], oa: int) -> Tuple[Tuple[int, ...], ...]:
        res = id_m
        base = a
        e = oa - 1
        while e > 0:
            if e & 1:
                res = mm(res, base)
            base = mm(base, base)
            e >>= 1
        return res

    # Enumerate all nontrivial p-elements in GL_d(p)
    p_els: List[Tuple[Tuple[Tuple[int, ...], ...], int]] = []

    def gen_cols(col_i: int, cols: List[Tuple[int, ...]], span_set: Set[Tuple[int, ...]]) -> None:
        if col_i == d:
            mat = tuple(tuple(cols[j][i] for j in range(d)) for i in range(d))
            if mat != id_m:
                o = p_ord(mat)
                if o > 0:
                    p_els.append((mat, o))
            return
        for v in nz_vecs:
            if v in span_set:
                continue
            ns = set(span_set)
            for sv in list(span_set):
                for c in range(1, p):
                    ns.add(tuple((sv[k] + c * v[k]) % p for k in range(d)))
            gen_cols(col_i + 1, cols + [v], ns)

    gen_cols(0, [], {(0,) * d})
    inv_map = {m: p_inv(m, o) for m, o in p_els}
    inv_map[id_m] = id_m
    max_sz = p**d

    # Up to GL_d(p)-conjugacy, every nontrivial unipotent A_0 in GL_d(p) has a Jordan partition of d!
    parts: List[Tuple[int, ...]] = []

    def gen_parts(rem: int, mx: int, cur: Tuple[int, ...]) -> None:
        if rem == 0:
            if cur[0] >= 2:
                parts.append(cur)
            return
        for k in range(min(rem, mx), 0, -1):
            gen_parts(rem - k, k, cur + (k,))

    gen_parts(d, d, ())
    found_irred = 0

    def min_subspace(mats: Sequence[Tuple[Tuple[int, ...], ...]]) -> Optional[Set[Tuple[int, ...]]]:
        best: Optional[Set[Tuple[int, ...]]] = None
        for v0 in nz_vecs:
            sp = {(0,) * d}
            q = deque([v0])
            while q:
                u = q.popleft()
                if u in sp:
                    continue
                old = list(sp)
                for c in range(1, p):
                    for z in old:
                        sp.add(tuple((z[k] + c * u[k]) % p for k in range(d)))
                for m in mats:
                    w = mv(m, u)
                    if w not in sp:
                        q.append(w)
            if len(sp) < max_sz:
                if best is None or len(sp) < len(best):
                    best = sp
                    if len(best) == p:
                        return best
        return best

    def close_tw(
        m_list: List[Tuple[Tuple[int, ...], ...]], max_o: int
    ) -> Optional[List[Tuple[Tuple[int, ...], ...]]]:
        res = list(m_list)
        m_set = set(res)
        idx = 0
        while idx < len(res):
            a = res[idx]
            idx += 1
            cands = [inv_map[a]]
            cur_len = len(res)
            for b in res[:cur_len]:
                cands.append(mm(a, mm(b, a)))
                cands.append(mm(b, mm(a, b)))
            for c in cands:
                if c not in m_set:
                    if len(res) >= max_sz:
                        return None
                    oc = p_ord(c)
                    if oc == 0 or oc > max_o:
                        return None
                    ic = inv_map.get(c)
                    if ic is None:
                        ic = p_inv(c, oc)
                        inv_map[c] = ic
                    for x in res:
                        if p_ord(mm(inv_map[x], c)) == 0 or p_ord(mm(ic, x)) == 0:
                            return None
                    res.append(c)
                    m_set.add(c)
        return res

    for pt in parts:
        cols_j: List[List[int]] = [[0] * d for _ in range(d)]
        pos = 0
        for sz in pt:
            for k in range(sz):
                cols_j[pos + k][pos + k] = 1
                if k > 0:
                    cols_j[pos + k][pos + k - 1] = 1
            pos += sz
        a0 = tuple(tuple(cols_j[j][i] for j in range(d)) for i in range(d))
        max_o = p_ord(a0)
        m0 = close_tw([id_m, a0], max_o)
        if m0 is None:
            continue
        m0_set = set(m0)
        pool0 = [
            m
            for m, o in p_els
            if o <= max_o
            and m not in m0_set
            and all(p_ord(mm(inv_map[x], m)) > 0 and p_ord(mm(inv_map[m], x)) > 0 for x in m0)
        ]

        def dfs(cur_m: List[Tuple[Tuple[int, ...], ...]], pool: List[Tuple[Tuple[int, ...], ...]]) -> None:
            nonlocal found_irred
            sub = min_subspace(cur_m)
            if sub is None:
                found_irred += 1
                return
            if len(cur_m) >= max_sz or not pool:
                return
            sub_nz = [u for u in sub if u != (0,) * d]
            mv_arr = [any(mv(x_mat, u) not in sub for u in sub_nz) for x_mat in pool]
            for idx_p, x_mat in enumerate(pool):
                if not mv_arr[idx_p]:
                    continue
                mn = close_tw(cur_m + [x_mat], max_o)
                if mn is not None:
                    new_els = mn[len(cur_m) :]
                    mn_s = set(mn)
                    npool = [
                        y
                        for j_p, y in enumerate(pool)
                        if not (j_p <= idx_p and mv_arr[j_p])
                        and y not in mn_s
                        and all(
                            p_ord(mm(inv_map[nx], y)) > 0 and p_ord(mm(inv_map[y], nx)) > 0
                            for nx in new_els
                        )
                    ]
                    dfs(mn, npool)
                    if found_irred:
                        return

        dfs(m0, pool0)
    return found_irred


def verify_ha_f2_upto_d5_c(max_d: int = 5) -> bool:
    """Compile and run `_HA_F2_C_SRC` in `${TMPDIR:-/tmp}` (with automatic cleanup)."""
    cc = _find_c_compiler()
    if cc is None:
        return False
    with tempfile.TemporaryDirectory(prefix="bol0323_ha_") as tdir:
        c_file = os.path.join(tdir, "ha_f2.c")
        bin_file = os.path.join(tdir, "ha_f2")
        with open(c_file, "w", encoding="utf-8") as fh:
            fh.write(_HA_F2_C_SRC)
        subprocess.run([cc, "-O3", "-std=c99", c_file, "-o", bin_file], check=True)
        proc = subprocess.run([bin_file, str(max_d)], capture_output=True, text=True, check=True)
        for d in range(2, max_d + 1):
            assert f"d={d} found_irred=0" in proc.stdout
    return True


# ======================================================================
# 4. Sub-target 4.3B: Order-8 Census, Order-24 Exact-Fact & Wreath C99
# ======================================================================


def classify_all_order8_left_bol_loops() -> Dict[str, Any]:
    """Exhaustive loop-level classification of ALL left Bol loops of order 8 (zero group assumptions).

    Fixes 0 = identity. Every nontrivial L_x (x in 1..7) is semiregular of order d in {2, 4, 8}.
    If any |x| == 8, Q ~= C_8 (associative). For d in {2, 4}, searches all left-Bol-closed
    Latin transversals in S_8 up to Stab_{S_8}(0)-conjugacy of a max-order L_1!
    """
    n = 8
    id8 = identity_perm(8)
    s8_gens = [cycles_to_perm(8, [list(range(8))]), cycles_to_perm(8, [[0, 1]])]
    all_s8 = PermGroup(8, s8_gens, allow_jordan_fastpath=False).enumerate_elements()

    cands_d2: Dict[int, Set[Perm]] = defaultdict(set)
    cands_d4: Dict[int, Set[Perm]] = defaultdict(set)
    for p in all_s8:
        if p == id8 or any(p[i] == i for i in range(8)):
            continue
        p2 = compose(p, p)
        if p2 == id8:
            cands_d2[p[0]].add(p)
        elif all(p2[i] != i for i in range(8)) and compose(p2, p2) == id8:
            cands_d4[p[0]].add(p)

    # Canonical L_1 representatives under S_7 = Stab_{S_8}(0):
    # - max_d == 2: unique fpf involution (0,1)(2,3)(4,5)(6,7)
    # - max_d == 4: unique semiregular 4+4 cycle (0,1,2,3)(4,5,6,7)
    r_d2 = cycles_to_perm(8, [[0, 1], [2, 3], [4, 5], [6, 7]])
    r_d4 = cycles_to_perm(8, [[0, 1, 2, 3], [4, 5, 6, 7]])

    found_loops: List[Loop] = [Loop([[(i + j) % 8 for j in range(8)] for i in range(8)], name="C_8")]

    for root_p, allow_d4 in ((r_d2, False), (r_d4, True)):
        pool_sets = {
            x: (cands_d2[x] | cands_d4[x]) if allow_d4 else set(cands_d2[x]) for x in range(1, 8)
        }
        pool_lists = {x: sorted(pool_sets[x]) for x in range(1, 8)}
        chosen: Dict[int, Perm] = {0: id8}

        def try_add(x0: int, px: Perm) -> Optional[List[int]]:
            added = [x0]
            chosen[x0] = px
            q = [px]
            while q:
                a = q.pop()
                for u_cand in (invert(a), compose(a, a)):
                    z = u_cand[0]
                    if z in chosen:
                        if chosen[z] != u_cand:
                            for w in added:
                                del chosen[w]
                            return None
                    else:
                        if u_cand not in pool_sets[z] or any(
                            u_cand[k] == pv[k] for pv in chosen.values() for k in range(8)
                        ):
                            for w in added:
                                del chosen[w]
                            return None
                        chosen[z] = u_cand
                        added.append(z)
                        q.append(u_cand)
                for b in list(chosen.values()):
                    for prod in (compose(a, compose(b, a)), compose(b, compose(a, b))):
                        z = prod[0]
                        if z in chosen:
                            if chosen[z] != prod:
                                for w in added:
                                    del chosen[w]
                                return None
                        else:
                            if prod not in pool_sets[z] or any(
                                prod[k] == pv[k] for pv in chosen.values() for k in range(8)
                            ):
                                for w in added:
                                    del chosen[w]
                                return None
                            chosen[z] = prod
                            added.append(z)
                            q.append(prod)
            return added

        def bt8() -> None:
            if len(chosen) == 8:
                lp = Loop([list(chosen[i]) for i in range(8)], name=f"ord8_{len(found_loops)}")
                if lp.check_left_bol()[0]:
                    found_loops.append(lp)
                return
            nx = min(x for x in range(1, 8) if x not in chosen)
            for cand in pool_lists[nx]:
                if any(cand[k] == pv[k] for pv in chosen.values() for k in range(8)):
                    continue
                ad = try_add(nx, cand)
                if ad is not None:
                    bt8()
                    for w in ad:
                        del chosen[w]

        ad0 = try_add(1, root_p)
        if ad0 is not None:
            bt8()
            for w in ad0:
                del chosen[w]

    classes = deduplicate_loops(found_loops)
    assoc_classes = [lp for lp, _ in classes if lp.check_associative()[0]]
    proper_classes = [lp for lp, _ in classes if not lp.check_moufang()[0]]
    return {
        "total_classes": len(classes),
        "associative_classes": len(assoc_classes),
        "proper_bol_classes": len(proper_classes),
        "proper_invariants": [
            (
                lp.LMlt().order(),
                lp.RMlt().order(),
                lp.Mlt().order(),
                lp.check_simplicity()[0],
            )
            for lp in proper_classes
        ],
    }


def classify_order24_exact_factorizations() -> Dict[str, Any]:
    """Construct all 15 pairwise non-isomorphic groups of order 24 and classify all exact-fact loops."""
    specs: List[Tuple[str, int, List[Perm]]] = [
        ("C_24", 24, [cycles_to_perm(24, [list(range(24))])]),
        ("C_12xC_2", 14, [cycles_to_perm(14, [list(range(12))]), cycles_to_perm(14, [[12, 13]])]),
        (
            "C_6xC_2^2",
            10,
            [cycles_to_perm(10, [list(range(6))]), cycles_to_perm(10, [[6, 7]]), cycles_to_perm(10, [[8, 9]])],
        ),
        ("S_4", 4, [cycles_to_perm(4, [[0, 1, 2, 3]]), cycles_to_perm(4, [[0, 1]])]),
        (
            "A_4xC_2",
            6,
            [cycles_to_perm(6, [[0, 1, 2]]), cycles_to_perm(6, [[0, 1], [2, 3]]), cycles_to_perm(6, [[4, 5]])],
        ),
        ("D_24", 12, [cycles_to_perm(12, [list(range(12))]), tuple((-x) % 12 for x in range(12))]),
        (
            "D_8xC_3",
            7,
            [cycles_to_perm(7, [[0, 1, 2, 3]]), cycles_to_perm(7, [[0, 2]]), cycles_to_perm(7, [[4, 5, 6]])],
        ),
        (
            "S_3xV_4",
            7,
            [
                cycles_to_perm(7, [[0, 1, 2]]),
                cycles_to_perm(7, [[0, 1]]),
                cycles_to_perm(7, [[3, 4]]),
                cycles_to_perm(7, [[5, 6]]),
            ],
        ),
        (
            "S_3xC_4",
            7,
            [cycles_to_perm(7, [[0, 1, 2]]), cycles_to_perm(7, [[0, 1]]), cycles_to_perm(7, [[3, 4, 5, 6]])],
        ),
        (
            "Q_8xC_3",
            11,
            [
                cycles_to_perm(11, [[0, 2, 1, 3], [4, 6, 5, 7]]),
                cycles_to_perm(11, [[0, 4, 1, 5], [2, 7, 3, 6]]),
                cycles_to_perm(11, [[8, 9, 10]]),
            ],
        ),
    ]
    f3_nz = [(x, y) for x in range(3) for y in range(3) if (x, y) != (0, 0)]
    f3_i = {v: i for i, v in enumerate(f3_nz)}
    specs.append(
        (
            "SL_2(3)",
            8,
            [
                tuple(f3_i[((x + y) % 3, y)] for x, y in f3_nz),
                tuple(f3_i[((2 * y) % 3, x)] for x, y in f3_nz),
            ],
        )
    )
    pts24 = [(a, u) for a in range(3) for u in range(8)]
    i24 = {p: i for i, p in enumerate(pts24)}
    specs.append(
        (
            "C_3:C_8",
            24,
            [
                tuple(i24[((a + 1) % 3, u)] for a, u in pts24),
                tuple(i24[(((-a) % 3), (u + 1) % 8)] for a, u in pts24),
            ],
        )
    )
    dic24_pts = [(k, e) for k in range(12) for e in range(2)]
    id24 = {p: i for i, p in enumerate(dic24_pts)}
    specs.append(
        (
            "Dic_24",
            24,
            [
                tuple(id24[((k + 1) % 12, e)] for k, e in dic24_pts),
                tuple(id24[(((-k + 6 * e) % 12), 1 ^ e)] for k, e in dic24_pts),
            ],
        )
    )
    dic12_pts = [(k, e) for k in range(6) for e in range(2)]
    id12 = {p: i for i, p in enumerate(dic12_pts)}
    specs.append(
        (
            "Dic_12xC_2",
            14,
            [
                tuple([id12[((k + 1) % 6, e)] for k, e in dic12_pts] + [12, 13]),
                tuple([id12[(((-k + 3 * e) % 6), 1 ^ e)] for k, e in dic12_pts] + [12, 13]),
                cycles_to_perm(14, [[12, 13]]),
            ],
        )
    )
    d8_pts = [(a, u, e) for a in range(3) for u in range(4) for e in range(2)]
    id8 = {p: i for i, p in enumerate(d8_pts)}
    specs.append(
        (
            "C_3:D_8_(ker=V4)",
            24,
            [
                tuple(id8[((a + 1) % 3, u, e)] for a, u, e in d8_pts),
                tuple(id8[(((-a) % 3), (u + 1) % 4, e)] for a, u, e in d8_pts),
                tuple(id8[(a, (-u) % 4, 1 ^ e)] for a, u, e in d8_pts),
            ],
        )
    )

    group_loops: List[Loop] = []
    proper_hits: List[Loop] = []
    simple_proper_hits: List[Loop] = []

    for gname, deg, gs in specs:
        els = PermGroup(deg, gs, allow_jordan_fastpath=False).enumerate_elements()
        assert len(els) == 24
        id_p = identity_perm(deg)
        els = [id_p] + [x for x in els if x != id_p]
        mp = {x: i for i, x in enumerate(els)}
        mul = [[mp[compose(x, y)] for y in els] for x in els]
        group_loops.append(Loop(mul, name=gname))

        # Enumerate all subgroups of order 2..12 by closure
        subgroups: Set[FrozenSet[int]] = set()
        cyc_subs = []
        for x in range(1, 24):
            s = {0}
            cur = x
            while cur not in s:
                s.add(cur)
                cur = mul[cur][x]
            fs = frozenset(s)
            if len(fs) < 24 and fs not in subgroups:
                subgroups.add(fs)
                cyc_subs.append(fs)
        q_sub = deque(subgroups)
        while q_sub:
            cur_s = q_sub.popleft()
            for cs in cyc_subs:
                if cs <= cur_s:
                    continue
                cl = set(cur_s | cs)
                dq = deque(cl)
                while dq and len(cl) < 24:
                    a = dq.popleft()
                    for b in list(cl):
                        for p_ab in (mul[a][b], mul[b][a]):
                            if p_ab not in cl:
                                cl.add(p_ab)
                                dq.append(p_ab)
                if len(cl) < 24:
                    fcl = frozenset(cl)
                    if fcl not in subgroups:
                        subgroups.add(fcl)
                        q_sub.append(fcl)

        by_sz: Dict[int, List[FrozenSet[int]]] = defaultdict(list)
        for sb in subgroups:
            by_sz[len(sb)].append(sb)
        for s0 in (2, 3, 4, 6, 8, 12):
            s1 = 24 // s0
            if s0 > s1:
                continue
            for y0 in by_sz[s0]:
                for y1 in by_sz[s1]:
                    if len(y0 & y1) != 1:
                        continue
                    lp = exact_factorization_bol_loop(
                        deg,
                        [els[i] for i in y0],
                        [els[j] for j in y1],
                        name=f"EF_{gname}_{s0}x{s1}",
                    )
                    if not lp.check_moufang()[0]:
                        proper_hits.append(lp)
                        if lp.check_simplicity()[0]:
                            simple_proper_hits.append(lp)

    assert len(deduplicate_loops(group_loops)) == 15
    proper_classes = deduplicate_loops(proper_hits)
    simple_classes = deduplicate_loops(simple_proper_hits)
    return {
        "distinct_groups_order_24": 15,
        "proper_classes": [lp for lp, _ in proper_classes],
        "simple_proper_classes": [lp for lp, _ in simple_classes],
    }


_WREATH_BOL_C_SRC = r"""
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MAXN 24
typedef struct { uint8_t p[MAXN]; int ord; } Cand;

static int G_n, G_m, G_b, G_rx, G_max_d;
static uint32_t G_rx_mask = 0;
static const char *G_out = NULL;
static uint8_t bperms[720][8];
static int num_bperms = 0;
static uint8_t (*top_perms)[16] = NULL;
static int num_tperms = 0;

static inline void p_comp(const uint8_t *a, const uint8_t *b, uint8_t *out, int n) {
    for (int i = 0; i < n; i++) out[i] = a[b[i]];
}
static inline void p_inv(const uint8_t *a, uint8_t *out, int n) {
    for (int i = 0; i < n; i++) out[a[i]] = (uint8_t)i;
}
static inline int semireg_order(const uint8_t *a, int n) {
    uint8_t seen[MAXN] = {0};
    int ord = 0;
    for (int i = 0; i < n; i++) {
        if (seen[i]) continue;
        int len = 0, u = i;
        while (!seen[u]) { seen[u] = 1; u = a[u]; len++; }
        if (ord == 0) ord = len; else if (ord != len) return 0;
    }
    return ord;
}

static Cand *cands_by_x[MAXN];
static int num_cands[MAXN], cap_cands[MAXN];

static void push_cand(int x, const uint8_t *a, int ord) {
    if (num_cands[x] >= cap_cands[x]) {
        cap_cands[x] = cap_cands[x] ? cap_cands[x] * 2 : 1024;
        cands_by_x[x] = realloc(cands_by_x[x], (size_t)cap_cands[x] * sizeof(Cand));
    }
    memset(cands_by_x[x][num_cands[x]].p, 0, MAXN);
    memcpy(cands_by_x[x][num_cands[x]].p, a, G_n);
    cands_by_x[x][num_cands[x]].ord = ord;
    num_cands[x]++;
}
static int cmp_cand(const void *pa, const void *pb) {
    return memcmp(((const Cand *)pa)->p, ((const Cand *)pb)->p, G_n);
}
static int has_cand(int x, const uint8_t *a, int max_cross_d) {
    if (x == 0) { for (int i = 0; i < G_n; i++) if (a[i] != i) return 0; return 1; }
    int lo = 0, hi = num_cands[x] - 1;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        int cmp = memcmp(cands_by_x[x][mid].p, a, G_n);
        if (cmp == 0) return !(((G_rx_mask >> x) & 1u) && cands_by_x[x][mid].ord > max_cross_d);
        if (cmp < 0) lo = mid + 1; else hi = mid - 1;
    }
    return 0;
}
static int find_cand_idx(int x, const uint8_t *a) {
    int lo = 0, hi = num_cands[x] - 1;
    while (lo <= hi) {
        int mid = (lo + hi) >> 1;
        int cmp = memcmp(cands_by_x[x][mid].p, a, G_n);
        if (cmp == 0) return mid;
        if (cmp < 0) lo = mid + 1; else hi = mid - 1;
    }
    return -1;
}

static int cur_ncyc, cyc_lens[16], cyc_blks[16][16], num_bp_ord[16];
static uint8_t bperms_by_ord[16][720][8];
static void gen_for_top_cyc(int d, int c_idx, uint8_t cur[MAXN]);

static void fill_cyc_maps(int d, int c_idx, int m_idx, const uint8_t comp[8], uint8_t cur[MAXN]) {
    int c = cyc_lens[c_idx], s = d / c;
    if (m_idx == c - 1) {
        int b_last = cyc_blks[c_idx][c - 1], b_first = cyc_blks[c_idx][0];
        for (int gi = 0; gi < num_bp_ord[s]; gi++) {
            const uint8_t *gt = bperms_by_ord[s][gi];
            uint8_t nxt[MAXN]; memcpy(nxt, cur, G_n);
            for (int u = 0; u < G_b; u++) nxt[b_last * G_b + comp[u]] = (uint8_t)(b_first * G_b + gt[u]);
            gen_for_top_cyc(d, c_idx + 1, nxt);
        }
        return;
    }
    int src_b = cyc_blks[c_idx][m_idx], dst_b = cyc_blks[c_idx][m_idx + 1];
    for (int fi = 0; fi < num_bperms; fi++) {
        const uint8_t *fp = bperms[fi];
        uint8_t ncomp[8], nxt[MAXN]; memcpy(nxt, cur, G_n);
        for (int u = 0; u < G_b; u++) { nxt[src_b * G_b + u] = (uint8_t)(dst_b * G_b + fp[u]); ncomp[u] = fp[comp[u]]; }
        fill_cyc_maps(d, c_idx, m_idx + 1, ncomp, nxt);
    }
}
static void gen_for_top_cyc(int d, int c_idx, uint8_t cur[MAXN]) {
    if (c_idx == cur_ncyc) { if (cur[0] > 0) push_cand(cur[0], cur, d); return; }
    uint8_t id_c[8]; for (int u = 0; u < G_b; u++) id_c[u] = (uint8_t)u;
    fill_cyc_maps(d, c_idx, 0, id_c, cur);
}

static int check_bol_and_proper_and_simple(uint8_t tbl[MAXN][MAXN], int n, int *is_proper, int *is_simple) {
    for (int x = 0; x < n; x++) for (int y = 0; y < n; y++) {
        int xyx = tbl[x][tbl[y][x]];
        for (int z = 0; z < n; z++) if (tbl[x][tbl[y][tbl[x][z]]] != tbl[xyx][z]) return 0;
    }
    int mouf = 1;
    for (int x = 0; x < n && mouf; x++) for (int y = 0; y < n && mouf; y++) {
        int xy = tbl[x][y];
        for (int z = 0; z < n; z++) if (tbl[xy][tbl[z][x]] != tbl[tbl[x][tbl[y][z]]][x]) { mouf = 0; break; }
    }
    *is_proper = !mouf;
    int simp = 1;
    for (int a = 1; a < n; a++) {
        int par[MAXN], q[MAXN * MAXN][2], qh = 0, qt = 0, merged = 1;
        for (int i = 0; i < n; i++) par[i] = i;
        par[a] = 0; q[qt][0] = 0; q[qt][1] = a; qt++;
        while (qh < qt && merged < n - 1) {
            int u = q[qh][0], v = q[qh][1]; qh++;
            for (int x = 0; x < n && merged < n - 1; x++) {
                int pairs[2][2] = {{tbl[x][u], tbl[x][v]}, {tbl[u][x], tbl[v][x]}};
                for (int t = 0; t < 2; t++) {
                    int ru = pairs[t][0], rv = pairs[t][1];
                    while (par[ru] != ru) ru = par[ru];
                    while (par[rv] != rv) rv = par[rv];
                    if (ru != rv) {
                        if (ru > rv) { int tmp = ru; ru = rv; rv = tmp; }
                        par[rv] = ru; merged++; q[qt][0] = ru; q[qt][1] = rv; qt++;
                    }
                }
            }
        }
        if (merged < n - 1) { simp = 0; break; }
    }
    *is_simple = simp;
    return 1;
}

static uint8_t chosen[MAXN][MAXN], is_set[MAXN];
static int cur_set_cnt = 0, cur_max_cross_d = 0;
static long proper_found = 0, simple_proper_found = 0;

static int try_add_closure(int sx, const uint8_t *sp, int added_xs[MAXN], int *n_added) {
    *n_added = 0; memcpy(chosen[sx], sp, G_n); is_set[sx] = 1; added_xs[(*n_added)++] = sx;
    int q_idx = 0;
    while (q_idx < *n_added) {
        const uint8_t *pa = chosen[added_xs[q_idx++]];
        uint8_t cloc[2][MAXN]; p_inv(pa, cloc[0], G_n); p_comp(pa, pa, cloc[1], G_n);
        for (int t = 0; t < 2; t++) {
            int z0 = cloc[t][0];
            if (is_set[z0]) { if (memcmp(chosen[z0], cloc[t], G_n) != 0) return 0; }
            else {
                if (!has_cand(z0, cloc[t], cur_max_cross_d)) return 0;
                for (int w = 0; w < G_n; w++) if (is_set[w])
                    for (int k = 0; k < G_n; k++) if (chosen[w][k] == cloc[t][k]) return 0;
                memcpy(chosen[z0], cloc[t], G_n); is_set[z0] = 1; added_xs[(*n_added)++] = z0;
            }
        }
        for (int bx = 1; bx < G_n; bx++) if (is_set[bx]) {
            const uint8_t *pb = chosen[bx];
            uint8_t tmp[MAXN], prods[2][MAXN];
            p_comp(pb, pa, tmp, G_n); p_comp(pa, tmp, prods[0], G_n);
            p_comp(pa, pb, tmp, G_n); p_comp(pb, tmp, prods[1], G_n);
            for (int t = 0; t < 2; t++) {
                int z0 = prods[t][0];
                if (is_set[z0]) { if (memcmp(chosen[z0], prods[t], G_n) != 0) return 0; }
                else {
                    if (!has_cand(z0, prods[t], cur_max_cross_d)) return 0;
                    for (int w = 0; w < G_n; w++) if (is_set[w])
                        for (int k = 0; k < G_n; k++) if (chosen[w][k] == prods[t][k]) return 0;
                    memcpy(chosen[z0], prods[t], G_n); is_set[z0] = 1; added_xs[(*n_added)++] = z0;
                }
            }
        }
    }
    return 1;
}

static void bt_search(void) {
    if (cur_set_cnt == G_n) {
        int prop = 0, simp = 0;
        if (check_bol_and_proper_and_simple(chosen, G_n, &prop, &simp)) {
            if (prop) proper_found++;
            if (prop && simp) {
                simple_proper_found++;
                if (G_out) {
                    FILE *outf = fopen(G_out, "a");
                    if (outf) {
                        fprintf(outf, "%d\n", G_n);
                        for (int r = 0; r < G_n; r++) {
                            for (int c = 0; c < G_n; c++) fprintf(outf, "%d ", chosen[r][c]);
                            fprintf(outf, "\n");
                        }
                        fclose(outf);
                    }
                }
            }
        }
        return;
    }
    int best_u = -1, best_cnt = 1000000000;
    uint32_t forb[MAXN] = {0};
    for (int w = 0; w < G_n; w++) if (is_set[w])
        for (int k = 0; k < G_n; k++) forb[k] |= (1u << chosen[w][k]);
    for (int u = 1; u < G_n; u++) if (!is_set[u]) {
        int cnt = 0, nc = num_cands[u];
        const Cand *cu = cands_by_x[u];
        for (int i = 0; i < nc; i++) {
            if (((G_rx_mask >> u) & 1u) && cu[i].ord > cur_max_cross_d) continue;
            int ok = 1;
            for (int k = 0; k < G_n; k++) if ((forb[k] >> cu[i].p[k]) & 1u) { ok = 0; break; }
            if (ok && is_set[G_rx]) {
                uint8_t t1[MAXN], t2[MAXN];
                p_comp(chosen[G_rx], cu[i].p, t1, G_n); p_comp(cu[i].p, t1, t2, G_n);
                int z0 = t2[0];
                if (is_set[z0]) { if (memcmp(chosen[z0], t2, G_n) != 0) ok = 0; }
                else if (!has_cand(z0, t2, cur_max_cross_d)) ok = 0;
            }
            if (ok && ++cnt >= best_cnt) break;
        }
        if (cnt == 0) return;
        if (cnt < best_cnt) { best_cnt = cnt; best_u = u; if (cnt == 1) break; }
    }
    for (int i = 0; i < num_cands[best_u]; i++) {
        if (((G_rx_mask >> best_u) & 1u) && cands_by_x[best_u][i].ord > cur_max_cross_d) continue;
        const uint8_t *pu = cands_by_x[best_u][i].p;
        int ok = 1;
        for (int k = 0; k < G_n; k++) if ((forb[k] >> pu[k]) & 1u) { ok = 0; break; }
        if (!ok) continue;
        int added[MAXN], n_add = 0;
        if (try_add_closure(best_u, pu, added, &n_add)) {
            cur_set_cnt += n_add; bt_search(); cur_set_cnt -= n_add;
        }
        for (int j = 0; j < n_add; j++) is_set[added[j]] = 0;
    }
}

int main(int argc, char **argv) {
    if (argc < 2) return 1;
    if (argc >= 3) G_out = argv[2];
    FILE *f = fopen(argv[1], "r");
    if (!f) return 1;
    char label[128];
    int n_stab_gens = 0;
    unsigned int rx_mask_in = 0;
    while (fscanf(f, "%127s %d %d %d %d %u %d %d %d %d",
                  label, &G_n, &G_m, &G_b, &G_rx, &rx_mask_in, &G_max_d, &num_bperms, &num_tperms, &n_stab_gens) == 10) {
        G_rx_mask = (uint32_t)rx_mask_in;
        memset(num_bp_ord, 0, sizeof(num_bp_ord));
        for (int i = 0; i < num_bperms; i++) {
            int is_id = 1;
            for (int j = 0; j < G_b; j++) {
                int v; if (fscanf(f, "%d", &v) != 1) return 1;
                bperms[i][j] = (uint8_t)v;
                if (v != j) is_id = 0;
            }
            int s = is_id ? 1 : semireg_order(bperms[i], G_b);
            if (s > 0 && s < 16) memcpy(bperms_by_ord[s][num_bp_ord[s]++], bperms[i], G_b);
        }
        top_perms = malloc((size_t)num_tperms * sizeof(*top_perms));
        for (int i = 0; i < num_tperms; i++)
            for (int j = 0; j < G_m; j++) { int v; if (fscanf(f, "%d", &v) != 1) return 1; top_perms[i][j] = (uint8_t)v; }
        uint8_t stab_gens[64][MAXN], stab_inv[64][MAXN];
        for (int i = 0; i < n_stab_gens; i++) {
            for (int j = 0; j < G_n; j++) { int v; if (fscanf(f, "%d", &v) != 1) return 1; stab_gens[i][j] = (uint8_t)v; }
            p_inv(stab_gens[i], stab_inv[i], G_n);
        }
        for (int x = 0; x < G_n; x++) num_cands[x] = 0;
        for (int d = 2; d <= G_max_d && d < G_n; d++) {
            if (G_n % d != 0 || 2 * d == G_n) continue;
            for (int ti = 0; ti < num_tperms; ti++) {
                const uint8_t *tp = top_perms[ti];
                uint8_t seen[16] = {0}; cur_ncyc = 0; int ok = 1;
                for (int b0 = 0; b0 < G_m; b0++) {
                    if (seen[b0]) continue;
                    int c = 0, u = b0;
                    while (!seen[u]) { seen[u] = 1; cyc_blks[cur_ncyc][c++] = u; u = tp[u]; }
                    if (d % c != 0 || (d / c) >= 16 || num_bp_ord[d / c] == 0) { ok = 0; break; }
                    cyc_lens[cur_ncyc++] = c;
                }
                if (!ok) continue;
                uint8_t init_p[MAXN] = {0}; gen_for_top_cyc(d, 0, init_p);
            }
        }
        for (int x = 1; x < G_n; x++)
            if (num_cands[x] > 1) qsort(cands_by_x[x], (size_t)num_cands[x], sizeof(Cand), cmp_cand);

        int ncb = num_cands[G_rx];
        uint8_t *vis = calloc((size_t)(ncb > 0 ? ncb : 1), 1);
        int *q_bfs = malloc((size_t)(ncb > 0 ? ncb : 1) * sizeof(int));
        int *roots = malloc((size_t)(ncb > 0 ? ncb : 1) * sizeof(int));
        int n_roots = 0;
        for (int i = 0; i < ncb; i++) {
            if (vis[i]) continue;
            vis[i] = 1; roots[n_roots++] = i;
            int qh = 0, qt = 0; q_bfs[qt++] = i;
            while (qh < qt) {
                const uint8_t *cp = cands_by_x[G_rx][q_bfs[qh++]].p;
                for (int gi = 0; gi < n_stab_gens; gi++) {
                    uint8_t tmp[MAXN], conj[MAXN];
                    p_comp(cp, stab_inv[gi], tmp, G_n); p_comp(stab_gens[gi], tmp, conj, G_n);
                    int idx = find_cand_idx(G_rx, conj);
                    if (idx >= 0 && !vis[idx]) { vis[idx] = 1; q_bfs[qt++] = idx; }
                }
            }
        }
        proper_found = simple_proper_found = 0;
        memset(is_set, 0, sizeof(is_set));
        for (int i = 0; i < G_n; i++) chosen[0][i] = (uint8_t)i;
        is_set[0] = 1;
        for (int ri = 0; ri < n_roots; ri++) {
            int idx = roots[ri]; cur_max_cross_d = cands_by_x[G_rx][idx].ord;
            int added[MAXN], n_add = 0; cur_set_cnt = 1;
            if (try_add_closure(G_rx, cands_by_x[G_rx][idx].p, added, &n_add)) {
                cur_set_cnt += n_add; bt_search(); cur_set_cnt -= n_add;
            }
            for (int j = 0; j < n_add; j++) is_set[added[j]] = 0;
        }
        printf("%s %ld %ld\n", label, proper_found, simple_proper_found);
        free(vis); free(q_bfs); free(roots); free(top_perms);
    }
    fclose(f);
    return 0;
}
"""


def _sym_pg(k: int) -> Tuple[PermGroup, List[Perm]]:
    if k == 1:
        pg = PermGroup(1, [(0,)], allow_jordan_fastpath=False)
        return pg, [(0,)]
    gens = [cycles_to_perm(k, [list(range(k))])]
    if k >= 2:
        gens.append(cycles_to_perm(k, [[0, 1]]))
    pg = PermGroup(k, gens, allow_jordan_fastpath=False)
    return pg, list(itertools.permutations(range(k)))


def _wreath_stab_0_rx_gens(m: int, b: int, rx: int, b_pg: PermGroup, p_pg: PermGroup) -> Tuple[List[Perm], int]:
    n = m * b
    w_gens: List[Perm] = []
    for g in b_pg.generators:
        p = list(range(n))
        for u in range(b):
            p[u] = g[u]
        w_gens.append(tuple(p))
    for g in p_pg.generators:
        p = [0] * n
        for blk in range(m):
            dst = g[blk]
            for u in range(b):
                p[blk * b + u] = dst * b + u
        w_gens.append(tuple(p))
    w_pg = PermGroup(n, w_gens, allow_jordan_fastpath=False)
    s0 = PermGroup(n, w_pg.stabilizer_generators(0), allow_jordan_fastpath=False)
    rx_orb_mask = sum(1 << u for o in s0.orbits() if rx in o for u in o)
    return list(s0.stabilizer_generators(rx)), rx_orb_mask


def _s11_order_le_2() -> Tuple[PermGroup, List[Perm]]:
    """Return S_11 PermGroup and all 35,696 elements of S_11 of order <= 2 (for n=22, d=2)."""
    s11 = PermGroup(11, [cycles_to_perm(11, [list(range(11))]), cycles_to_perm(11, [[0, 1]])], allow_jordan_fastpath=False)
    els: List[Perm] = [identity_perm(11)]

    def gen_invs(rem: Tuple[int, ...], pairs: List[Tuple[int, int]]) -> None:
        if pairs:
            arr = list(range(11))
            for u, v in pairs:
                arr[u], arr[v] = v, u
            els.append(tuple(arr))
        if len(rem) < 2:
            return
        # either skip rem[0] (only once before choosing larger first-elements) or pair rem[0]
        gen_invs(rem[1:], pairs)
        u0 = rem[0]
        for idx in range(1, len(rem)):
            v0 = rem[idx]
            nxt_rem = rem[1:idx] + rem[idx + 1 :]
            # enforce increasing u0 so each involution is generated ONCE
            if not pairs or u0 > pairs[-1][0]:
                gen_invs(nxt_rem, pairs + [(u0, v0)])

    # Cleaner canonical generator: choose 2k subset, partition into k unordered pairs!
    els = [identity_perm(11)]

    def part_pairs(avail: List[int], cur: List[int]) -> None:
        if not avail:
            els.append(tuple(cur))
            return
        u = avail[0]
        for i in range(1, len(avail)):
            v = avail[i]
            cur[u], cur[v] = v, u
            part_pairs(avail[1:i] + avail[i + 1 :], cur)

    for k in range(1, 6):
        for sub in itertools.combinations(range(11), 2 * k):
            base_arr = list(range(11))
            part_pairs(list(sub), base_arr)
    assert len(els) == 35_696
    return s11, els


def run_wreath_imprimitive_cases(full_heavy: bool = False) -> Tuple[Dict[str, Tuple[int, int]], List[Loop]]:
    """Run C99 wreath-product left-Bol census in `${TMPDIR:-/tmp}` (auto-cleaned).

    Returns (dict[label -> (proper_count, simple_proper_count)], list_of_order24_simple_loops).
    """
    cc = _find_c_compiler()
    if cc is None:
        return {}, []

    s2_pg, s2_els = _sym_pg(2)
    s3_pg, s3_els = _sym_pg(3)
    s4_pg, s4_els = _sym_pg(4)
    s5_pg, s5_els = _sym_pg(5)
    s6_pg, s6_els = _sym_pg(6)
    s7_pg, s7_els = _sym_pg(7)

    f42_pg = PermGroup(
        7, [cycles_to_perm(7, [list(range(7))]), tuple((3 * x) % 7 for x in range(7))], allow_jordan_fastpath=False
    )
    f42_els = f42_pg.enumerate_elements()
    psl3_2_pg = PermGroup(
        7,
        [
            cycles_to_perm(7, [list(range(7))]),
            cycles_to_perm(7, [[1, 3], [2, 6]]),
            cycles_to_perm(7, [[1, 2, 4], [3, 6, 5]]),
        ],
        allow_jordan_fastpath=False,
    )
    psl3_2_els = psl3_2_pg.enumerate_elements()

    def f9_add(x: int, y: int) -> int:
        return ((x % 3 + y % 3) % 3) + 3 * (((x // 3) + (y // 3)) % 3)

    def f9_mul(x: int, y: int) -> int:
        a, b = x % 3, x // 3
        c, d = y % 3, y // 3
        return ((a * c - b * d) % 3) + 3 * ((a * d + b * c) % 3)

    f9_inv = {x: next(y for y in range(1, 9) if f9_mul(x, y) == 1) for x in range(1, 9)}
    pgal2_9_pg = PermGroup(
        10,
        [
            tuple(f9_add(x, 1) if x < 9 else 9 for x in range(10)),
            tuple(f9_add(x, 3) if x < 9 else 9 for x in range(10)),
            tuple(f9_mul(x, 4) if x < 9 else 9 for x in range(10)),
            tuple(9 if x == 0 else (0 if x == 9 else f9_mul(2, f9_inv[x])) for x in range(10)),
            tuple((x % 3) + 3 * ((2 * (x // 3)) % 3) if x < 9 else 9 for x in range(10)),
        ],
        allow_jordan_fastpath=False,
    )
    pgal2_9_els = pgal2_9_pg.enumerate_elements()
    pgl2_5_pg = PermGroup(
        6,
        [
            tuple((x + 1) % 5 if x < 5 else 5 for x in range(6)),
            tuple((2 * x) % 5 if x < 5 else 5 for x in range(6)),
            tuple(5 if x == 0 else (0 if x == 5 else pow(x, 3, 5)) for x in range(6)),
        ],
        allow_jordan_fastpath=False,
    )
    pgl2_5_els = pgl2_5_pg.enumerate_elements()
    _, s5_10_gens = _induced_kset_action(5, 2, s5_pg.generators)
    s5_10_pg = PermGroup(10, s5_10_gens, allow_jordan_fastpath=False)
    s5_10_els = s5_10_pg.enumerate_elements()
    s11_pg, s11_invs = _s11_order_le_2()

    # Fast suite (< 1.5s total in C99): covers 6, 8, 9, 10, 12, 14, 15, 18(3,6 PGL2(5)), 20(10,2), 21, 22!
    # Note on remaining analytic wreath reductions:
    #   - n=21, (3,7) S_7 wr S_3: any element of order d in {3,7} projects to C_3 (d=3) or {1} (d=7),
    #     so pi(G) = C_3 and H <= ker(pi) <| G of index 3 (non-simple).
    #   - n=20, (10,2) top A_10/S_10: N = G cap C_2^10 = O_2(G) is tau-characteristic and min |C_k(S_10)| = 45 > 20;
    #     imprimitive top groups on 10 blocks refine to (5,4) S_4 wr S_5 or m = 2.
    cases: List[Tuple[str, int, int, int, int, int, PermGroup, List[Perm], PermGroup, List[Perm]]] = [
        ("n=6_(3,2)_S2wrS3", 6, 3, 2, 2, 5, s2_pg, s2_els, s3_pg, s3_els),
        ("n=8_(4,2)_S2wrS4", 8, 4, 2, 2, 7, s2_pg, s2_els, s4_pg, s4_els),
        ("n=9_(3,3)_S3wrS3", 9, 3, 3, 3, 8, s3_pg, s3_els, s3_pg, s3_els),
        ("n=10_(5,2)_S2wrS5", 10, 5, 2, 2, 9, s2_pg, s2_els, s5_pg, s5_els),
        ("n=12_(3,4)_S4wrS3", 12, 3, 4, 4, 11, s4_pg, s4_els, s3_pg, s3_els),
        ("n=12_(4,3)_S3wrS4", 12, 4, 3, 3, 11, s3_pg, s3_els, s4_pg, s4_els),
        ("n=12_(6,2)_S2wrS6", 12, 6, 2, 2, 11, s2_pg, s2_els, s6_pg, s6_els),
        ("n=14_(7,2)_S2wrS7", 14, 7, 2, 2, 13, s2_pg, s2_els, s7_pg, s7_els),
        ("n=15_(5,3)_S3wrS5", 15, 5, 3, 3, 14, s3_pg, s3_els, s5_pg, s5_els),
        ("n=15_(3,5)_S5wrS3", 15, 3, 5, 5, 14, s5_pg, s5_els, s3_pg, s3_els),
        ("n=18_(3,6)_PGL2_5wrS3_d6", 18, 3, 6, 6, 6, pgl2_5_pg, pgl2_5_els, s3_pg, s3_els),
        ("n=20_(10,2)_S2wrPGaL2_9", 20, 10, 2, 2, 19, s2_pg, s2_els, pgal2_9_pg, pgal2_9_els),
        ("n=20_(10,2)_S2wrS5_10", 20, 10, 2, 2, 19, s2_pg, s2_els, s5_10_pg, s5_10_els),
        ("n=21_(3,7)_F42wrS3", 21, 3, 7, 7, 20, f42_pg, f42_els, s3_pg, s3_els),
        ("n=21_(7,3)_S3wrF42", 21, 7, 3, 3, 20, s3_pg, s3_els, f42_pg, f42_els),
        ("n=21_(7,3)_S3wrPSL3_2", 21, 7, 3, 3, 20, s3_pg, s3_els, psl3_2_pg, psl3_2_els),
        ("n=22_(11,2)_S2wrS11", 22, 11, 2, 2, 2, s2_pg, s2_els, s11_pg, s11_invs),
    ]

    if full_heavy:
        s8_pg, s8_els = _sym_pg(8)
        s9_pg, s9_els = _sym_pg(9)
        # Build S_3 wr S_4 on 12 blocks for order-24 S_2 wr (S_3 wr S_4)
        s3wrs4_gens: List[Perm] = []
        for g in s3_pg.generators:
            p = list(range(12))
            for u in range(3):
                p[u] = g[u]
            s3wrs4_gens.append(tuple(p))
        for g in s4_pg.generators:
            p = [0] * 12
            for blk in range(4):
                for u in range(3):
                    p[blk * 3 + u] = g[blk] * 3 + u
            s3wrs4_gens.append(tuple(p))
        s3wrs4_pg = PermGroup(12, s3wrs4_gens, allow_jordan_fastpath=False)
        s3wrs4_els = s3wrs4_pg.enumerate_elements()
        assert len(s3wrs4_els) == 31_104

        cases.extend(
            [
                ("n=16_(4,4)_S4wrS4", 16, 4, 4, 4, 15, s4_pg, s4_els, s4_pg, s4_els),
                ("n=16_(8,2)_S2wrS8", 16, 8, 2, 2, 15, s2_pg, s2_els, s8_pg, s8_els),
                ("n=18_(3,6)_S6wrS3_d6", 18, 3, 6, 6, 6, s6_pg, s6_els, s3_pg, s3_els),
                ("n=18_(6,3)_S3wrS6", 18, 6, 3, 3, 17, s3_pg, s3_els, s6_pg, s6_els),
                ("n=18_(9,2)_S2wrS9", 18, 9, 2, 2, 17, s2_pg, s2_els, s9_pg, s9_els),
                ("n=20_(4,5)_S5wrS4", 20, 4, 5, 5, 19, s5_pg, s5_els, s4_pg, s4_els),
                ("n=20_(5,4)_S4wrS5", 20, 5, 4, 4, 19, s4_pg, s4_els, s5_pg, s5_els),
                ("n=21_(7,3)_S3wrS7", 21, 7, 3, 3, 20, s3_pg, s3_els, s7_pg, s7_els),
                ("n=24_(12,2)_S2wr(S3wrS4)_d4", 24, 12, 2, 6, 4, s2_pg, s2_els, s3wrs4_pg, s3wrs4_els),
            ]
        )

    results: Dict[str, Tuple[int, int]] = {}
    simple_24_loops: List[Loop] = []
    with tempfile.TemporaryDirectory(prefix="bol0323_wr_") as tdir:
        c_file = os.path.join(tdir, "wreath_bol.c")
        bin_file = os.path.join(tdir, "wreath_bol")
        in_file = os.path.join(tdir, "cases.txt")
        hits_file = os.path.join(tdir, "hits.txt")
        with open(c_file, "w", encoding="utf-8") as fh:
            fh.write(_WREATH_BOL_C_SRC)
        subprocess.run([cc, "-O3", "-std=c99", c_file, "-o", bin_file], check=True)

        with open(in_file, "w", encoding="utf-8") as fh:
            for lbl, n, m, b, rx, max_d, b_pg, b_els, p_pg, p_els in cases:
                stab_gens, rx_orb_mask = _wreath_stab_0_rx_gens(m, b, rx, b_pg, p_pg)
                fh.write(
                    f"{lbl} {n} {m} {b} {rx} {rx_orb_mask} {max_d} {len(b_els)} {len(p_els)} {len(stab_gens)}\n"
                )
                for bp in b_els:
                    fh.write(" ".join(map(str, bp)) + "\n")
                for tp in p_els:
                    fh.write(" ".join(map(str, tp)) + "\n")
                for sg in stab_gens:
                    fh.write(" ".join(map(str, sg)) + "\n")

        proc = subprocess.run([bin_file, in_file, hits_file], capture_output=True, text=True, check=True)
        for line in proc.stdout.strip().splitlines():
            lbl, pr_s, sm_s = line.split()
            results[lbl] = (int(pr_s), int(sm_s))

        if os.path.exists(hits_file):
            with open(hits_file, "r", encoding="utf-8") as hfh:
                lines = [ln.strip() for ln in hfh if ln.strip()]
            ptr = 0
            while ptr < len(lines):
                ord_n = int(lines[ptr])
                ptr += 1
                tbl = [[int(v) for v in lines[ptr + r].split()] for r in range(ord_n)]
                ptr += ord_n
                simple_24_loops.append(Loop(tbl, name=f"wreath24_hit_{len(simple_24_loops)}"))

    return results, simple_24_loops


# ======================================================================
# 5. Fast Automated Unit Tests (Imported into test_bol_engine.py)
# ======================================================================


class TestWave2Fast(unittest.TestCase):
    def test_subtarget_4_1_sims_aut_and_gloop_isotopes(self) -> None:
        q24 = build_nagy_q24()
        self.assertEqual(sims_automorphism_group(q24).order(), 2)
        q60 = build_nagy_q60()
        self.assertEqual(sims_automorphism_group(q60).order(), 4)

        q96 = build_nagy_exp2_q96()
        ag96 = sims_automorphism_group(q96, prefer_idx_from=16)
        self.assertEqual(ag96.order(), 80)
        self.assertEqual(sorted(len(o) for o in ag96.orbits()), [1, 5, 10, 80])

    def test_subtarget_4_2_bsgs_uod_and_bol_transversal_fast(self) -> None:
        # 1. Bit-for-bit verification of BSGS UOD solver against brute-force enumeration
        a8_8 = [cycles_to_perm(8, [[0, 1, 2]]), cycles_to_perm(8, [[1, 2, 3, 4, 5, 6, 7]])]
        _, g_a8_28 = _induced_kset_action(8, 2, a8_8)
        _, g_o6p_28 = _build_f2_orthogonal_or_symplectic(6, "O+", "nonsingular")
        _, g_psp_40 = _build_psp4_3_isotropic_40()
        for lbl, deg, gs in (
            ("A_8(28)", 28, g_a8_28),
            ("O_6^+(2)(28)", 28, g_o6p_28),
            ("PSp_4(3)(40)", 40, g_psp_40),
        ):
            self.assertEqual(
                check_uod_on_group(lbl, deg, gs)["uod_by_suborbit"],
                check_uod_bsgs(lbl, deg, gs)["uod_by_suborbit"],
            )

        # 2. Full order-13,063,680 Aut(srg(126,45,12,18)) = PSU_4(3).2^2 on NO_6^-(3) (#49 §2.1)
        no6_cases = build_no6_f3_actions()
        res_126 = check_uod_bsgs(*no6_cases[3], cap_per_suborbit=5000)
        self.assertEqual(res_126["order"], 13_063_680)
        self.assertEqual(res_126["uod_by_suborbit"], [(45, 12), (80, 0)])
        self.assertFalse(res_126["passes_lemma_3_2a"])

        # 3. Sporadic / exceptional Johnson 2-set actions (#49 §2.2)
        g_pgl28_36, g_a9_120 = build_pgammal2_8_and_a9()
        self.assertFalse(check_uod_bsgs("PGammaL_2(8)(36)", 36, g_pgl28_36)["passes_lemma_3_2a"])
        for lbl, deg, gs in build_mathieu_2set_actions():
            self.assertFalse(check_uod_bsgs(lbl, deg, gs, cap_per_suborbit=50)["passes_lemma_3_2a"])

        # 4. Left-Bol UOD transversal wipeout on A_9(120) (where single-element UOD is 56:3, 63:6 > 0!)
        bol_a9 = classify_left_bol_uod_transversals("A_9(120)", 120, g_a9_120)
        self.assertEqual(bol_a9["raw_uod"], [(56, 3), (63, 6)])
        self.assertTrue(bol_a9["wiped_by_arc_consistency"])
        self.assertEqual(bol_a9["proper_left_bol_loops"], 0)

    def test_subtarget_4_3a_ha_no_irred_twisted_p_subsets(self) -> None:
        # Odd prime powers 9, 25, 27 + small F_2^2 (4) in pure Python
        for p, d in ((2, 2), (3, 2), (5, 2), (3, 3)):
            self.assertEqual(verify_ha_odd_or_small_python(p, d), 0, f"Unexpected HA hit at {p}^{d}")
        # Even prime powers 4, 8, 16, 32 via C99 helper in ${TMPDIR:-/tmp} (with pure-Python d=3 fallback)
        if not verify_ha_f2_upto_d5_c(max_d=5):
            self.assertEqual(verify_ha_odd_or_small_python(2, 3), 0)

    def test_subtarget_4_3b_order8_order24_and_fast_imprimitive_census(self) -> None:
        # 1. Exhaustive order-8 left Bol loop census (5 groups + 6 Burn proper 2-loops, 0 simple)
        res8 = classify_all_order8_left_bol_loops()
        self.assertEqual(res8["total_classes"], 11)
        self.assertEqual(res8["associative_classes"], 5)
        self.assertEqual(res8["proper_bol_classes"], 6)
        for lmlt_o, rmlt_o, mlt_o, is_s in res8["proper_invariants"]:
            self.assertEqual((lmlt_o, rmlt_o, mlt_o, is_s), (16, 32, 64, False))

        # 2. Exhaustive exact factorizations across all 15 groups of order 24 -> unique Q_24!
        ef24 = classify_order24_exact_factorizations()
        self.assertEqual(ef24["distinct_groups_order_24"], 15)
        self.assertEqual(len(ef24["proper_classes"]), 3)
        self.assertEqual(len(ef24["simple_proper_classes"]), 1)
        self.assertTrue(are_loops_isomorphic(ef24["simple_proper_classes"][0], build_nagy_q24()))

        # 3. Fast C99 wreath-product imprimitive sweep for n in {6,8,9,10,12,14,15,20(10,2),21,22}
        wr_res, _ = run_wreath_imprimitive_cases(full_heavy=False)
        if wr_res:
            self.assertEqual(len(wr_res), 17)
            for lbl, (_, simp_cnt) in wr_res.items():
                self.assertEqual(simp_cnt, 0, f"Unexpected simple proper hit in {lbl}")


# ======================================================================
# 6. Full Exhaustive Wave-2 CLI Sweep (`--full`)
# ======================================================================


def run_full_wave2_sweep(verify_all_1536: bool = False, include_above_415: bool = False) -> None:
    t_start = time.time()
    print("=== [1/3] Sub-target 4.1: Complete 20-Loop Q_1536 Isotopy Class Census ===")
    t0 = time.time()
    census_1536 = build_nagy_q1536_isotopy_census(verify_all_isotopes=verify_all_1536)
    assert len(census_1536) == 20
    assert sum(r["orbit_size"] for r in census_1536) == 1536
    print(f"  Verified 20 pairwise non-isomorphic simple proper left Bol loops in {time.time()-t0:.2f}s:")
    for idx, rec in enumerate(census_1536):
        print(
            f"    Orb {idx:>2}: {rec['source_stratum']:<16} | orb={rec['orbit_size']:>4} | "
            f"|Aut|={rec['aut_order']:>4} | exp={rec['exponent']:>2} | Bruck={str(rec['is_left_bruck']):<5} | "
            f"orders={rec['order_spectrum']}"
        )

    print("\n=== [2/3] Sub-target 4.2: Complete <= 415 Rank-3 AS UOD & Left-Bol Transversal Sweep ===")
    g_pgl28_36, g_a9_120 = build_pgammal2_8_and_a9()
    g_a10_126, g_s10_126 = build_a10_s10_deg126()
    psl56_and_162 = build_psl3_4_deg56_and_psu4_3_deg162(include_deg162=True)
    sp44_cases = build_sp4_4_quadric_actions()

    uod_suite: List[Tuple[str, int, List[Perm]]] = (
        [("PGammaL_2(8) on 2-sets (deg 36)", 36, g_pgl28_36)]
        + build_psu3_5_deg50()
        + psl56_and_162[:3]
        + build_mathieu_2set_actions()
        + build_no6_f3_actions()
        + [("A_10 on {5,5}-parts (deg 126)", 126, g_a10_126), ("S_10 on {5,5}-parts (deg 126)", 126, g_s10_126)]
        + sp44_cases[2:]
        + build_nu5_2_deg176()
        + build_m22_176_m23_253_and_mcl_275()
        + build_no7_f3_actions()
    )
    for lbl, deg, gs in uod_suite:
        r = check_uod_bsgs(lbl, deg, gs)
        assert not r["passes_lemma_3_2a"], f"Expected UOD=0 on {lbl}"
        print(f"  [UOD=0] {lbl:<48} | |P|={r['order']:>11} | UOD={r['uod_by_suborbit']}")

    # The 4 surviving single-element UOD geometries (deg <= 415):
    for lbl, deg, gs in (
        ("A_9 on PGammaL_2(8) (deg 120)", 120, g_a9_120),
        sp44_cases[0],
        sp44_cases[1],
        psl56_and_162[3],
    ):
        rb = classify_left_bol_uod_transversals(lbl, deg, gs)
        assert rb["proper_left_bol_loops"] == 0 and rb["moufang_loops"] == 0
        print(f"  [Bol=0] {lbl:<48} | |P|={rb['order']:>11} | raw_UOD={rb['raw_uod']}")

    # Positive control: O_8^+(2) on 120 nonsingular points collapses uniquely to Moufang M(2)
    rng = random.Random(323)
    _, g_o8p_120 = _build_f2_orthogonal_or_symplectic(8, "O+", "nonsingular")
    s_o8p_120 = [g_o8p_120[i] for i in sorted(rng.sample(range(len(g_o8p_120)), 24))]
    rb_o8 = classify_left_bol_uod_transversals(
        "O_8^+(2) nonsing (deg 120)", 120, s_o8p_120, stop_on_first_proper=False
    )
    m2_loop = build_paige_moufang_m2()
    assert rb_o8["proper_left_bol_loops"] == 0 and rb_o8["moufang_loops"] >= 1
    assert all(are_loops_isomorphic(lp, m2_loop) for lp in rb_o8["sample_loops"])
    print(
        f"  [M(2) ] O_8^+(2) nonsing (deg 120)                       | moufang_orbits={rb_o8['moufang_loops']} (all ~= M(2)), proper=0"
    )

    if include_above_415:
        print("\n=== [2b/3] Above-415 Rank-3 AS UOD & Left-Bol Transversal Sweep (416..1408) ===")
        uod_gt415, om7_1080_case = build_above_415_rank3_actions()
        for lbl, deg, gs in uod_gt415:
            r = check_uod_bsgs(lbl, deg, gs)
            assert not r["passes_lemma_3_2a"], f"Expected UOD=0 on {lbl}"
            print(f"  [UOD=0] {lbl:<48} | |P|={r['order']:>12} | UOD={r['uod_by_suborbit']}")
        rb_1080 = classify_left_bol_uod_transversals(*om7_1080_case)
        assert rb_1080["proper_left_bol_loops"] == 0 and rb_1080["moufang_loops"] == 0
        print(f"  [Bol=0] {om7_1080_case[0]:<48} | |P|={rb_1080['order']:>12} | raw_UOD={rb_1080['raw_uod']}")

    print("\n=== [3/3] Sub-target 4.3: Complete Small-Order (< 24) & Order-24 Wreath Sweep ===")
    wr_all, loops_24 = run_wreath_imprimitive_cases(full_heavy=True)
    q24 = build_nagy_q24()
    for lbl, (pr_c, sm_c) in wr_all.items():
        print(f"  {lbl:<34} | proper={pr_c:>6} | simple_proper={sm_c}")
        if not lbl.startswith("n=24_"):
            assert sm_c == 0
        else:
            assert sm_c == 24
    assert len(loops_24) == 24 and all(are_loops_isomorphic(lp, q24) for lp in loops_24)
    print("  Verified all 24 simple proper hits in S_2 wr (S_3 wr S_4) are isomorphic to Q_24!")
    print(f"\nTotal full Wave-2 sweep runtime: {time.time()-t_start:.2f}s")


if __name__ == "__main__":
    verify_1536_all = "--verify-all-1536" in sys.argv
    run_gt415 = "--above415" in sys.argv
    if "--full" in sys.argv or run_gt415:
        sys.argv = [a for a in sys.argv if a not in ("--full", "--above415", "--verify-all-1536")]
        run_full_wave2_sweep(verify_all_1536=verify_1536_all, include_above_415=run_gt415)
    unittest.main(verbosity=2)
