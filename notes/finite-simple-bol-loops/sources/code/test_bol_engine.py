"""Comprehensive unit tests for `perm_group.py`, `bol_engine.py`, `known_constructions.py`,
and the Wave-2 / Wave-3 census modules (`test_lmlt_exclusions.py`, `test_wave2_census.py`,
`test_wave3_rank3.py`).

Run fast default suite with Python 3.9+ or Python 3.12+:
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_bol_engine.py

Run extended higher-order witness certifications (orders 960..1536 + negative control):
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_bol_engine.py --extended
"""

from __future__ import annotations

import math
import random
import unittest
from typing import List

import bol_engine
from bol_engine import (
    Loop,
    are_loops_isomorphic,
    bol_folder_from_perms,
    deduplicate_loops,
    exact_factorization_bol_loop,
    find_loop_isomorphism,
)
from known_constructions import (
    build_affine_simple_q960,
    build_affine_simple_q1344,
    build_nagy_exp2_q96,
    build_nagy_exp2_q1536,
    build_nagy_odd_q1053,
    build_nagy_q24,
    build_nagy_q60,
    build_nagy_q96_isotopy_census,
    build_nagy_q120,
    build_solvable_wreath_q1152,
)
from perm_group import Perm, PermGroup, cycles_to_perm, invert, perm_sign
from test_lmlt_exclusions import TestLMltExclusions
from test_wave2_census import TestWave2Fast
from test_wave3_rank3 import TestWave3Fast

__all__ = [
    "TestPermGroupEngine",
    "TestBolEngineAndSimplicity",
    "TestLMltExclusions",
    "TestWave2Fast",
    "TestWave3Fast",
]

RUN_EXTENDED_WITNESSES = False


def relabel_loop(loop: Loop, seed: int) -> Loop:
    """Relabel elements {1, ..., n-1} of `loop` by a seeded random permutation (fixing 0)."""
    rng = random.Random(seed)
    rest = list(range(1, loop.n))
    rng.shuffle(rest)
    sigma = [0] + rest
    sigma_inv = [0] * loop.n
    for i, s in enumerate(sigma):
        sigma_inv[s] = i

    new_table: List[List[int]] = [[0] * loop.n for _ in range(loop.n)]
    for i in range(loop.n):
        oi = sigma_inv[i]
        for j in range(loop.n):
            oj = sigma_inv[j]
            new_table[i][j] = sigma[loop.table[oi][oj]]
    return Loop(new_table, name=f"{loop.name}_relabeled_{seed}")


def direct_product_loop(q1: Loop, q2: Loop, name: str = "prod") -> Loop:
    """Direct product Q1 x Q2 with identity (0, 0) -> 0."""
    n1, n2 = q1.n, q2.n
    n = n1 * n2
    tbl: List[List[int]] = [[0] * n for _ in range(n)]
    for i1 in range(n1):
        for i2 in range(n2):
            u = i1 * n2 + i2
            for j1 in range(n1):
                p1 = q1.table[i1][j1]
                for j2 in range(n2):
                    p2 = q2.table[i2][j2]
                    v = j1 * n2 + j2
                    tbl[u][v] = p1 * n2 + p2
    return Loop(tbl, name=name)


class TestPermGroupEngine(unittest.TestCase):
    def test_jordan_boundary_primitive_exceptions(self) -> None:
        """Primitive groups of degree n >= 10 that are NOT A_n/S_n (e.g. M_11, PGL(2,11), AGL(1,13))
        have prime cycles p > n - 3 only and MUST NOT trigger the Jordan A_n/S_n certificate.
        """
        m11_a = cycles_to_perm(11, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]], one_based=True)
        m11_b = cycles_to_perm(11, [[3, 7, 11, 8], [4, 10, 5, 6]], one_based=True)
        pg_m11 = PermGroup(11, [m11_a, m11_b], allow_jordan_fastpath=True)
        self.assertIsNone(pg_m11._giant_kind)
        self.assertEqual(pg_m11.order(), 7920)
        self.assertTrue(pg_m11.is_primitive())
        self.assertEqual(pg_m11.rank(0), 2)

        pgl_t = cycles_to_perm(12, [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        pgl_m = cycles_to_perm(12, [[1, 2, 4, 8, 5, 10, 9, 7, 3, 6]])
        pgl_inv = cycles_to_perm(12, [[0, 11], [1, 10], [2, 5], [3, 7], [4, 8], [6, 9]])
        pg_pgl = PermGroup(12, [pgl_t, pgl_m, pgl_inv], allow_jordan_fastpath=True)
        self.assertIsNone(pg_pgl._giant_kind)
        self.assertEqual(pg_pgl.order(), 1320)
        self.assertTrue(pg_pgl.is_primitive())
        self.assertEqual(pg_pgl.rank(0), 2)

        agl_t = cycles_to_perm(13, [list(range(13))])
        agl_m = cycles_to_perm(13, [[1, 2, 4, 8, 3, 6, 12, 11, 9, 5, 10, 7]])
        pg_agl = PermGroup(13, [agl_t, agl_m], allow_jordan_fastpath=True)
        self.assertIsNone(pg_agl._giant_kind)
        self.assertEqual(pg_agl.order(), 156)
        self.assertTrue(pg_agl.is_primitive())
        self.assertEqual(pg_agl.rank(0), 2)

    def test_jordan_fastpath_matches_explicit_bsgs(self) -> None:
        """Verify exact agreement between Jordan certification and explicit BSGS on A_12 and RMlt(Q_24)."""
        c3 = cycles_to_perm(12, [[0, 1, 2]])
        shift_even = cycles_to_perm(12, [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])
        g_fast = PermGroup(12, [c3, shift_even], allow_jordan_fastpath=True)
        g_bsgs = PermGroup(12, [c3, shift_even], allow_jordan_fastpath=False)
        self.assertEqual(g_fast._giant_kind, "A_n")
        self.assertEqual(g_fast.order(), math.factorial(12) // 2)
        self.assertEqual(g_fast.order(), g_bsgs.order())
        self.assertEqual(g_fast.rank(0), g_bsgs.rank(0))
        self.assertEqual(g_fast.subdegrees(0), g_bsgs.subdegrees(0))

        odd_swap = cycles_to_perm(12, [[0, 1]])
        self.assertFalse(g_fast.contains(odd_swap))
        self.assertFalse(g_bsgs.contains(odd_swap))
        self.assertTrue(g_fast.contains(c3))

        q24 = build_nagy_q24()
        rmlt_fast = PermGroup(24, q24.R, initial_base=[0], allow_jordan_fastpath=True)
        rmlt_bsgs = PermGroup(24, q24.R, initial_base=[0], allow_jordan_fastpath=False)
        self.assertEqual(rmlt_fast.order(), math.factorial(24) // 2)
        self.assertEqual(rmlt_fast.order(), rmlt_bsgs.order())

    def test_contains_is_purely_read_only(self) -> None:
        """Ensure PermGroup.contains() never mutates base/orbits on non-member queries."""
        g = PermGroup(6, [cycles_to_perm(6, [[0, 1, 2]]), cycles_to_perm(6, [[3, 4]])])
        base_before = list(g.base)
        ord_before = g.order()
        outside = cycles_to_perm(6, [[0, 5]])
        self.assertFalse(g.contains(outside))
        self.assertEqual(g.base, base_before)
        self.assertEqual(g.order(), ord_before)

    def test_derived_series_and_solvability(self) -> None:
        """Verify exact BSGS commutator normal-closure derived series and solvability checks."""
        s4 = PermGroup(4, [cycles_to_perm(4, [[0, 1, 2, 3]]), cycles_to_perm(4, [[0, 1]])])
        self.assertEqual(s4.derived_series_orders(), (24, 12, 4, 1))
        self.assertTrue(s4.is_solvable())

        a5 = PermGroup(5, [cycles_to_perm(5, [[0, 1, 2, 3, 4]]), cycles_to_perm(5, [[0, 1, 2]])])
        self.assertEqual(a5.derived_series_orders(), (60,))
        self.assertFalse(a5.is_solvable())

        agl_1_13 = PermGroup(
            13,
            [
                cycles_to_perm(13, [list(range(13))]),
                cycles_to_perm(13, [[1, 2, 4, 8, 3, 6, 12, 11, 9, 5, 10, 7]]),
            ],
        )
        self.assertEqual(agl_1_13.derived_series_orders(), (156, 13, 1))
        self.assertTrue(agl_1_13.is_solvable())


class TestBolEngineAndSimplicity(unittest.TestCase):
    def test_identities_and_opposite_transport(self) -> None:
        q24 = build_nagy_q24()
        is_lb, lb_wit = q24.check_left_bol()
        self.assertTrue(is_lb)
        self.assertIsNone(lb_wit)

        is_rb, rb_wit = q24.check_right_bol()
        self.assertFalse(is_rb)
        self.assertIsNotNone(rb_wit)
        assert rb_wit is not None
        x, y, z = rb_wit
        lhs = q24.mul(q24.mul(q24.mul(z, x), y), x)
        rhs = q24.mul(z, q24.mul(q24.mul(x, y), x))
        self.assertNotEqual(lhs, rhs)

        is_m, m_wit = q24.check_moufang()
        self.assertFalse(is_m)
        assert m_wit is not None
        mx, my, mz = m_wit
        m_lhs = q24.mul(q24.mul(mx, my), q24.mul(mz, mx))
        m_rhs = q24.mul(q24.mul(mx, q24.mul(my, mz)), mx)
        self.assertNotEqual(m_lhs, m_rhs)

        q24_op = q24.opposite()
        self.assertTrue(q24_op.check_right_bol()[0])
        self.assertFalse(q24_op.check_left_bol()[0])
        self.assertFalse(are_loops_isomorphic(q24, q24_op))

    def test_both_simplicity_checks_on_simple_and_nonsimple_loops(self) -> None:
        c5_tbl = [[(i + j) % 5 for j in range(5)] for i in range(5)]
        c5 = Loop(c5_tbl, name="C_5")
        is_simp, sizes = c5.check_simplicity()
        self.assertTrue(is_simp)
        self.assertEqual(sizes, [])

        c4_tbl = [[(i + j) % 4 for j in range(4)] for i in range(4)]
        c4 = Loop(c4_tbl, name="C_4")
        is_simp4, sizes4 = c4.check_simplicity()
        self.assertFalse(is_simp4)
        self.assertEqual(sizes4, [2])

        y0_c3 = PermGroup(4, [cycles_to_perm(4, [[0, 1, 2]])]).enumerate_elements()
        y1_d8 = PermGroup(
            4, [cycles_to_perm(4, [[0, 1, 2, 3]]), cycles_to_perm(4, [[0, 2]])]
        ).enumerate_elements()
        q24_nonsimple = exact_factorization_bol_loop(4, y0_c3, y1_d8, name="Q24_nonsimple_(S4,C3,D8)")
        self.assertTrue(q24_nonsimple.check_left_bol()[0])
        self.assertFalse(q24_nonsimple.check_moufang()[0])
        simp_ns, ns_sizes = q24_nonsimple.check_simplicity()
        self.assertFalse(simp_ns)
        self.assertIn(4, ns_sizes)
        self.assertFalse(q24_nonsimple.Mlt().is_primitive())

        q24_simple = build_nagy_q24()
        c2 = Loop([[0, 1], [1, 0]], name="C_2")
        q48 = direct_product_loop(q24_simple, c2, name="Q24xC2")
        self.assertTrue(q48.check_left_bol()[0])
        self.assertFalse(q48.check_moufang()[0])
        simp_48, sizes_48 = q48.check_simplicity()
        self.assertFalse(simp_48)
        self.assertEqual(sizes_48, [2, 24])

        for builder in (build_nagy_q24, build_nagy_q60, build_nagy_exp2_q96):
            lp = builder()
            simp_lp, lp_sizes = lp.check_simplicity()
            self.assertTrue(simp_lp)
            self.assertEqual(lp_sizes, [])
            self.assertEqual(lp.Mlt().rank(0), 2)

    def test_q24_and_q60_structural_invariants(self) -> None:
        """Certify exact structural invariants for Q_24 (S_4 = C_4 * S_3) and Q_60 (A_5 = C_5 * A_4)."""
        q24 = build_nagy_q24()
        rep24 = q24.analyze(check_op_iso=True, compute_aut=True)
        self.assertEqual(rep24["order"], 24)
        self.assertEqual(rep24["exponent"], 12)
        self.assertTrue(rep24["is_proper_left_bol"])
        self.assertTrue(rep24["is_simple"])
        self.assertEqual(rep24["LMlt_order"], 288)
        self.assertEqual(rep24["LMlt_rank"], 6)
        self.assertTrue(rep24["is_LMlt_solvable"])
        self.assertEqual(q24.LMlt().derived_series_orders(), (288, 144, 16, 1))
        self.assertEqual(rep24["N_lambda_size"], 1)
        self.assertEqual(rep24["N_mu_size"], 1)
        self.assertEqual(rep24["N_rho_size"], 2)
        self.assertEqual(rep24["Aut_order"], 2)
        self.assertEqual(q24.automorphism_group().order(), 2)
        self.assertEqual(rep24["RMlt_order"], math.factorial(24) // 2)
        self.assertEqual(rep24["Mlt_order"], math.factorial(24) // 2)
        # Direct stabilizer-chain order plus generator parity identifies A_24,
        # independently of the optional Jordan fast path.
        right24 = PermGroup(24, q24.R, allow_jordan_fastpath=False)
        self.assertEqual(right24.order(), math.factorial(24) // 2)
        self.assertTrue(all(perm_sign(g) == 1 for g in q24.L + q24.R))
        self.assertEqual(rep24["Mlt_rank"], 2)
        self.assertFalse(rep24["is_isomorphic_to_opposite"])

        q60 = build_nagy_q60()
        rep60 = q60.analyze(check_op_iso=True, compute_aut=True)
        self.assertEqual(rep60["order"], 60)
        self.assertEqual(rep60["exponent"], 30)
        self.assertTrue(rep60["is_proper_left_bol"])
        self.assertTrue(rep60["is_simple"])
        self.assertEqual(rep60["LMlt_order"], 3600)
        self.assertEqual(rep60["LMlt_rank"], 8)
        self.assertFalse(rep60["is_LMlt_solvable"])
        self.assertEqual(q60.LMlt().derived_series_orders(), (3600,))
        self.assertEqual(rep60["N_lambda_size"], 1)
        self.assertEqual(rep60["N_mu_size"], 1)
        self.assertEqual(rep60["N_rho_size"], 2)
        self.assertEqual(rep60["Aut_order"], 4)
        self.assertEqual(q60.automorphism_group().order(), 4)
        self.assertEqual(rep60["RMlt_order"], math.factorial(60) // 2)
        self.assertEqual(rep60["Mlt_order"], math.factorial(60) // 2)
        self.assertEqual(rep60["Mlt_rank"], 2)
        self.assertFalse(rep60["is_isomorphic_to_opposite"])

    def test_nagy_q96_four_loop_isotopy_census(self) -> None:
        """Certify N_96^op and its complete 4-loop isotopy class census (exp 2, two exp-4 2-loops, rigid max-ord 6 / exp 12)."""
        q96_base = build_nagy_exp2_q96()
        census = build_nagy_q96_isotopy_census()
        self.assertEqual(len(census), 4)
        self.assertEqual(sum(r["orbit_size"] for r in census), 96)

        expected = [
            ("1", 1, 2, 2, 80, True, {1: 1, 2: 95}),
            ("J_0 \\ {1}", 10, 4, 4, 8, False, {1: 1, 2: 31, 4: 64}),
            ("J_0 \\ {1}", 5, 4, 4, 16, False, {1: 1, 2: 31, 4: 64}),
            ("c^G", 80, 6, 12, 1, False, {1: 1, 2: 11, 3: 24, 4: 36, 6: 24}),
        ]
        reps: List[Loop] = []
        for idx, (rec, exp_spec) in enumerate(zip(census, expected)):
            stratum, orb_sz, max_ord, exp_val, aut_ord, is_bruck, spec = exp_spec
            lp: Loop = rec["loop"]
            reps.append(lp)
            self.assertEqual(rec["source_stratum"], stratum)
            self.assertEqual(rec["orbit_size"], orb_sz)
            self.assertEqual(rec["max_order"], max_ord)
            self.assertEqual(rec["exponent"], exp_val)
            self.assertEqual(rec["aut_order"], aut_ord)
            self.assertEqual(rec["is_left_bruck"], is_bruck)
            self.assertEqual(rec["order_spectrum"], spec)
            self.assertEqual(orb_sz * aut_ord, 80)

            self.assertTrue(lp.check_left_bol()[0], f"Orbit {idx} failed left Bol")
            self.assertFalse(lp.check_moufang()[0], f"Orbit {idx} collapsed to Moufang")
            is_simp, ns = lp.check_simplicity()
            self.assertTrue(is_simp, f"Orbit {idx} failed simplicity")
            self.assertEqual(ns, [])
            self.assertEqual(lp.left_nucleus(), (0,))
            self.assertEqual(lp.middle_nucleus(), (0,))
            self.assertEqual(lp.right_nucleus(), (0,))
            self.assertEqual(lp.LMlt().order(), 3840)
            self.assertFalse(lp.LMlt().is_solvable())
            self.assertEqual(lp.RMlt()._giant_kind, "A_n")
            self.assertEqual(lp.Mlt()._giant_kind, "A_n")
            self.assertEqual(lp.Mlt().rank(0), 2)

        self.assertTrue(are_loops_isomorphic(q96_base, reps[0]))
        for i in range(4):
            for j in range(i + 1, 4):
                self.assertFalse(are_loops_isomorphic(reps[i], reps[j]))

    def test_folder_matches_exact_factorization_and_relabeling(self) -> None:
        q24_ef = build_nagy_q24()

        s4_elems = PermGroup(
            4, [cycles_to_perm(4, [[0, 1, 2, 3]]), cycles_to_perm(4, [[0, 1]])]
        ).enumerate_elements()
        c4_elems = PermGroup(4, [cycles_to_perm(4, [[0, 1, 2, 3]])]).enumerate_elements()
        s3_elems = PermGroup(
            4, [cycles_to_perm(4, [[0, 1, 2]]), cycles_to_perm(4, [[0, 1]])]
        ).enumerate_elements()

        def pair_perm(p1: Perm, p2: Perm) -> Perm:
            return tuple(list(p1) + [x + 4 for x in p2])

        G_s8 = [pair_perm(a, b) for a in s4_elems for b in s4_elems]
        H_s8 = [pair_perm(y0, y1) for y0 in c4_elems for y1 in s3_elems]
        K_s8 = [pair_perm(x, invert(x)) for x in s4_elems]

        res = bol_folder_from_perms(8, G_s8, H_s8, K_s8, name="Q24_folder_explicit")
        self.assertTrue(res.is_valid)
        assert res.loop is not None

        phi = find_loop_isomorphism(q24_ef, res.loop)
        self.assertIsNotNone(phi)
        assert phi is not None
        for x in range(24):
            for y in range(24):
                self.assertEqual(phi[q24_ef.mul(x, y)], res.loop.mul(phi[x], phi[y]))

        q24_r1 = relabel_loop(q24_ef, seed=101)
        q24_r2 = relabel_loop(q24_ef, seed=202)
        classes = deduplicate_loops([q24_ef, q24_r1, q24_r2, q24_ef.opposite()])
        self.assertEqual(len(classes), 2)
        self.assertEqual(len(classes[0][1]), 3)

    def test_c_accelerator_matches_pure_python_at_n120(self) -> None:
        from test_s1_obstructions import build_paige_moufang_m2

        q120 = build_nagy_q120()
        m2 = build_paige_moufang_m2()
        ok_c, wit_c = q120.check_left_bol()
        self.assertTrue(ok_c)
        self.assertIsNone(wit_c)

        mf_q120_c = q120.check_moufang()
        self.assertFalse(mf_q120_c[0])
        self.assertIsNotNone(mf_q120_c[1])
        mf_m2_c = m2.check_moufang()
        self.assertEqual(mf_m2_c, (True, None))

        bad_tbl = [list(r) for r in q120.table]
        bad_tbl[1][2], bad_tbl[1][3] = bad_tbl[1][3], bad_tbl[1][2]
        bad_loop = Loop(bad_tbl, name="corrupted_120", validate_loop=False)
        ok_bad, wit_bad = bad_loop.check_left_bol()
        self.assertFalse(ok_bad)
        self.assertIsNotNone(wit_bad)
        assert wit_bad is not None
        bx, by, bz = wit_bad
        lhs = bad_loop.mul(bx, bad_loop.mul(by, bad_loop.mul(bx, bz)))
        rhs = bad_loop.mul(bad_loop.mul(bx, bad_loop.mul(by, bx)), bz)
        self.assertNotEqual(lhs, rhs)

        # Force pure-Python fallback and assert exact bit-for-bit witness agreement
        saved_lib = bol_engine._C_ACCEL_LIB
        saved_tried = bol_engine._C_ACCEL_TRIED
        try:
            bol_engine._C_ACCEL_LIB = None
            bol_engine._C_ACCEL_TRIED = True
            self.assertEqual(q120.check_left_bol(), (ok_c, wit_c))
            self.assertEqual(bad_loop.check_left_bol(), (ok_bad, wit_bad))
            self.assertEqual(q120.check_moufang(), mf_q120_c)
            self.assertEqual(m2.check_moufang(), mf_m2_c)
        finally:
            bol_engine._C_ACCEL_LIB = saved_lib
            bol_engine._C_ACCEL_TRIED = saved_tried

    def test_paige_m2_rank3_positive_control(self) -> None:
        """Verify Paige's simple Moufang loop M(2) (|M(2)|=120) has Mlt(M(2)) ~= Omega_8^+(2) of rank 3."""
        from test_s1_obstructions import build_paige_moufang_m2

        m2 = build_paige_moufang_m2()
        self.assertTrue(m2.check_left_bol()[0])
        self.assertTrue(m2.check_right_bol()[0])
        self.assertTrue(m2.check_moufang()[0])
        self.assertFalse(m2.check_associative()[0])
        is_simp, sizes = m2.check_simplicity()
        self.assertTrue(is_simp)
        self.assertEqual(sizes, [])
        mlt = m2.Mlt()
        self.assertIsNone(mlt._giant_kind)
        self.assertEqual(mlt.order(), 174_182_400)
        self.assertEqual(mlt.rank(0), 3)
        self.assertEqual(mlt.subdegrees(0), (1, 56, 63))

    def test_higher_order_witnesses_smoke_and_extended(self) -> None:
        """Fast smoke/Mlt=A_n checks on Q_960 & Q_1344; full 960..1536 certifications under --extended."""
        for builder, expected_n, expected_nrho in (
            (build_affine_simple_q960, 960, 4),
            (build_affine_simple_q1344, 1344, 4),
        ):
            lp = builder()
            self.assertEqual(lp.n, expected_n)
            self.assertTrue(lp.is_valid_loop)
            self.assertFalse(lp.check_moufang()[0])
            self.assertEqual(len(lp.right_nucleus()), expected_nrho)
            mlt = lp.Mlt()
            self.assertEqual(mlt._giant_kind, "A_n")
            self.assertEqual(mlt.rank(0), 2)

        if RUN_EXTENDED_WITNESSES:
            # (builder, order, LMlt_order, is_LMlt_solvable, N_rho_size, is_left_bruck)
            specs = [
                (build_affine_simple_q960, 960, 921_600, False, 4, False),
                (build_nagy_odd_q1053, 1053, 369_603, True, 3, False),
                (build_solvable_wreath_q1152, 1152, 331_776, True, 2, False),
                (build_affine_simple_q1344, 1344, 1_806_336, False, 4, False),
                (lambda: build_nagy_exp2_q1536(deformed=True), 1536, 983_040, False, 1, True),
            ]
            for builder, ord_n, lmlt_ord, lmlt_solv, nrho_sz, bruck in specs:
                lp = builder()
                self.assertEqual(lp.n, ord_n)
                self.assertTrue(lp.check_left_bol()[0])
                self.assertFalse(lp.check_moufang()[0])
                is_simp, ns = lp.check_simplicity()
                self.assertTrue(is_simp)
                self.assertEqual(ns, [])
                self.assertEqual(lp.LMlt().order(), lmlt_ord)
                self.assertEqual(lp.LMlt().is_solvable(), lmlt_solv)
                self.assertEqual(len(lp.right_nucleus()), nrho_sz)
                self.assertEqual(lp.inverse_properties()["has_AIP"], bruck)
                self.assertEqual(lp.RMlt()._giant_kind, "A_n")
                self.assertEqual(lp.Mlt()._giant_kind, "A_n")
                self.assertEqual(lp.Mlt().rank(0), 2)

            # Negative control: undeformed N07E Prop 5.1 loop of order 1536 has normal subloop of size 16
            lp_ext_ns = build_nagy_exp2_q1536(deformed=False)
            self.assertEqual(lp_ext_ns.n, 1536)
            self.assertTrue(lp_ext_ns.check_left_bol()[0])
            self.assertFalse(lp_ext_ns.check_moufang()[0])
            is_simp_ns, ns_sizes = lp_ext_ns.check_simplicity()
            self.assertFalse(is_simp_ns)
            self.assertEqual(ns_sizes, [16])


if __name__ == "__main__":
    import sys

    if "--extended" in sys.argv or "--slow" in sys.argv:
        RUN_EXTENDED_WITNESSES = True
        sys.argv = [a for a in sys.argv if a not in ("--extended", "--slow")]
    unittest.main(verbosity=2)
