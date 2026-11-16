"""Wave-3 rank-3 almost-simple (#0323/S1) spectral & constructive verifiers.

Implements and certifies all three computational obligations of Wave 3:
  1. Spectral Trace Integrality Census (`verify_spectral_trace_integrality_census`):
     - Evaluates the rational SRG trace integrality obstruction
         c_{Delta_1} = (k_2 + 1 + s) / (r - s) in Z,   |c_{Delta_1}| <= f, |-1 - c_{Delta_1}| <= g,
         c_{Delta_2} = -(k_1 - s) / (r - s) in Z,      |c_{Delta_2}| <= f, |-1 - c_{Delta_2}| <= g
       across all 26 individual rank-3 almost-simple actions (both from exact [BvM22] SRG
       parameters and via independent exhaustive `(n, k_1)` parameter recovery) and across
       all 5 infinite rank-3 almost-simple families in the Liebeck-Saxl / Bannai / Kantor-Liebler
       roster (`D_{5,5}(q)`, `E_{6,1}(q)`, `NO_{2m-1}^eps(3)` & `NO_{2m}^eps(3)`, `NU_m(2)`,
       and `NO_{2r+1}^eps(q)` for `q in {4, 8}`).
     - Confirms non-conference rationality (`r, s in Z`, `f != g`) on every evaluated SRG,
       exact elimination of all 9 large sporadics (`M_24(1288)` through `Fi_24'(306936)`),
       `E_{6,1}(q)`, `D_{5,5}(q)`, `NO_{2m}^-(3)`, `NO_{4t+2}^+(3)`, `NU_m(2)` (`6 nmid m`),
       and `NO_{2r+1}^+(q)` (`q in {4, 8}`), leaving only the 3 infinite subfamilies
       `NO_{4t}^+(3)` (`t >= 2`), `NU_{6l}(2)` outer `.2` (`l >= 2`; `l = 1` deg `672` killed
       in Wave 2), and `NO_{4s+1}^-(q)` (`q in {4, 8}, s >= 1`; `(4, 1)` deg `120` killed in Wave 2).
  2. Complete Elimination of `Sp_4(8)` & `Sp_4(8).3` at Degrees `2016` and `2080`:
     - Certifies `Sp_4(8).3` on `NO_5^+(8)` (`deg 2080`): `UOD = [(567, 0), (1512, 0)]`.
     - Certifies `Sp_4(8)` on `NO_5^-(8)` (`deg 2016`, rank `5`): `0` UOD on all three `520`-suborbits.
     - Certifies `Sp_4(8).3` on `NO_5^-(8)` (`deg 2016`, rank `3`: `1 + 455 + 1560`): passes single-element
       and power-UOD with `[(455, 9), (1560, 576)]` where `100%` (`9/9` of order `2` and `576/576` of
       order `7`) lie inside `Sp_4(8)` (`0` outer `.3` semilinear UOD elements), and `0` left Bol loops
       survive pairwise `455 x 1560` `L_x L_y L_x` arc-consistency (`wiped_by_arc_consistency = True`).
  3. Paige's `M(3)` (`deg 1080`) & Exhaustive Collapse of Full `PO_8^+(3)` on `NO_8^+(3)`:
     - Certifies Paige's simple Moufang loop `M(3)` (`|M(3)| = 1080`, `Mlt(M(3)) = POmega_8^+(3)` of
       order `4,952,179,814,400`, rank `3`, subdegrees `(1, 351, 728)`).
     - Certifies `PO_8^+(3)` (`|PO_8^+(3)| = 19,808,719,257,600`, full `AS` stabilizer of `NO_8^+(3)`)
       has identical UOD counts `[(351, 1080), (728, 30240)]` (`0` UOD elements in `PO_8^+(3) \\ POmega_8^+(3)`),
       and via lossless multi-depth Schreier centralizer symmetry breaking classifies ALL left Bol loops
       on `NO_8^+(3)` with `Mlt(Q) <= PO_8^+(3)` sharing the rank-3 orbitals: uniquely `M(3)` (`1` Moufang
       up to `PO_8^+(3)`-conjugacy, `0` proper left Bol loops).

Scope caveat: Completeness of the global rank-3 almost-simple roster relies on CFSG
(Bannai 1972; Kantor-Liebler 1982; Liebeck-Saxl 1986). Every SRG arithmetic verification and
every permutation-group UOD / left-Bol classification here is unconditionally exact (`CFSG`-free).

Run fast default unit test suite (~15s):
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave3_rank3.py

Run complete Wave-3 constructive & exhaustive suite (~4 min, including `Sp_4(8).3` deg 2016/2080
and exhaustive `PO_8^+(3)` deg 1080 left-Bol classification):
    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/test_wave3_rank3.py --full
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
import itertools
import math
import random
import sys
import time
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple
import unittest

from bol_engine import Loop
from known_constructions import _paige_m3_points, build_paige_m3
from perm_group import Perm, PermGroup, compose, identity_perm, invert
from test_wave2_census import check_uod_bsgs, classify_left_bol_uod_transversals

__all__ = [
    "TestWave3Fast",
    "build_no8_plus_3_actions",
    "build_sp4_8_quadric_actions",
    "classify_no8_plus_3_left_bol_exhaustive",
    "evaluate_srg_parameters",
    "solve_srg_from_nk",
    "verify_spectral_trace_integrality_census",
]


# ======================================================================
# 1. Exact SRG & Spectral Trace Integrality Verifier
# ======================================================================


def evaluate_srg_parameters(n: int, k1: int, lam: int, mu: int) -> Dict[str, Any]:
    """Verify all 8 exact SRG identities, non-conference rationality, Krein bounds,
    and exact `Fraction` UOD spectral traces `(c_Delta1, c_Delta2)` for `srg(n, k1, lam, mu)`.
    """
    k2 = n - 1 - k1
    assert k1 > 0 and k2 > 0 and 1 + k1 + k2 == n, f"Invalid (n, k1)=({n}, {k1})"
    assert 0 <= lam < k1 and 1 <= mu <= k1, f"Out-of-range (lam, mu)=({lam}, {mu}) for n={n}, k1={k1}"
    assert k1 * (k1 - 1 - lam) == mu * k2, (
        f"SRG degree identity failed for ({n}, {k1}, {lam}, {mu}): "
        f"{k1 * (k1 - 1 - lam)} != {mu * k2}"
    )

    disc = (lam - mu) ** 2 + 4 * (k1 - mu)
    assert disc > 0
    d = math.isqrt(disc)
    assert d * d == disc, f"Irrational conference SRG encountered at ({n}, {k1}, {lam}, {mu})"
    assert ((lam - mu) + d) % 2 == 0
    r = ((lam - mu) + d) // 2
    s = ((lam - mu) - d) // 2
    assert r > s
    assert r + s == lam - mu and r * s == mu - k1

    f_num = -k1 - (n - 1) * s
    assert f_num % (r - s) == 0, f"Non-integer multiplicity f for ({n}, {k1}, {lam}, {mu})"
    f = f_num // (r - s)
    g = (n - 1) - f
    assert f > 0 and g > 0 and 1 + f + g == n
    # Every rational-eigenvalue SRG has rational orthogonal idempotents (even if f == g,
    # though here we also record non_conference_rational = True since d^2 == disc).
    assert k1 + f * r + g * s == 0
    assert k1 * k1 + f * r * r + g * s * s == n * k1

    kr1 = (r + 1) * (k1 + r + 2 * r * s) <= (k1 + r) * ((s + 1) ** 2)
    kr2 = (s + 1) * (k1 + s + 2 * r * s) <= (k1 + s) * ((r + 1) ** 2)
    assert kr1 and kr2, f"Krein bound failed for ({n}, {k1}, {lam}, {mu})"

    c1 = Fraction(k2 + 1 + s, r - s)
    c1_comp = -1 - c1
    c2 = Fraction(-(k1 - s), r - s)
    c2_comp = -1 - c2

    ok_1 = (c1.denominator == 1) and (abs(c1.numerator) <= f) and (abs(c1_comp.numerator) <= g)
    ok_2 = (c2.denominator == 1) and (abs(c2.numerator) <= f) and (abs(c2_comp.numerator) <= g)

    return {
        "n": n,
        "k1": k1,
        "k2": k2,
        "lam": lam,
        "mu": mu,
        "r": r,
        "s": s,
        "f": f,
        "g": g,
        "c_delta1": c1,
        "c_delta2": c2,
        "ok_delta1": ok_1,
        "ok_delta2": ok_2,
        "passes_spectral_integrality": ok_1 and ok_2,
    }


def solve_srg_from_nk(n: int, k1: int) -> List[Dict[str, Any]]:
    """Independently recover all feasible rational SRG parameter sets from `(n, k1)` alone."""
    k2 = n - 1 - k1
    sols: List[Dict[str, Any]] = []
    for lam in range(0, k1):
        num = k1 * (k1 - 1 - lam)
        if num <= 0 or num % k2 != 0:
            continue
        mu = num // k2
        if mu <= 0 or mu > k1:
            continue
        disc = (lam - mu) ** 2 + 4 * (k1 - mu)
        if disc <= 0:
            continue
        d = math.isqrt(disc)
        if d * d != disc or ((lam - mu) + d) % 2 != 0:
            continue
        r = ((lam - mu) + d) // 2
        s = ((lam - mu) - d) // 2
        if r == s:
            continue
        f_num = -k1 - (n - 1) * s
        if f_num % (r - s) != 0:
            continue
        f = f_num // (r - s)
        g = (n - 1) - f
        if f <= 0 or g <= 0:
            continue
        kr1 = (r + 1) * (k1 + r + 2 * r * s) <= (k1 + r) * ((s + 1) ** 2)
        kr2 = (s + 1) * (k1 + s + 2 * r * s) <= (k1 + s) * ((r + 1) ** 2)
        if not (kr1 and kr2):
            continue
        sols.append(evaluate_srg_parameters(n, k1, lam, mu))
    return sols


# All 26 individual rank-3 almost-simple actions from the Liebeck-Saxl / Bannai / Kantor-Liebler
# census: (label, category, n, k1, lam, mu, expects_spectral_pass).
INDIVIDUAL_26_SPECS: Tuple[Tuple[str, str, int, int, int, int, bool], ...] = (
    # Classical individual actions (7)
    ("PSU_3(3) on PSL_3(2)", "classical", 36, 14, 4, 6, True),
    ("PSU_3(5) on A_7", "classical", 50, 7, 0, 1, True),
    ("PSL_3(4) on A_6", "classical", 56, 10, 0, 2, False),
    ("PSL_4(3) on PSp_4(3) [->NO_6^+(3)]", "classical", 117, 36, 15, 9, False),
    ("PSU_4(3) on PSL_3(4)", "classical", 162, 56, 10, 24, True),
    ("Omega_7(3) on G_2(3) [->NO_8^+(3)]", "classical", 1080, 351, 126, 108, True),
    ("PSU_6(2) on PSU_4(3).2", "classical", 1408, 567, 246, 216, False),
    # Exceptional Lie-type actions (4)
    ("G_2(3) on G_2(2) [->NO_7^-(3)]", "exceptional", 351, 126, 45, 45, False),
    ("G_2(4) on J_2", "exceptional", 416, 100, 36, 20, False),
    ("G_2(4) on SU_3(4):2 [->NO_7^-(4)]", "exceptional", 2016, 975, 462, 480, True),
    ("G_2(8):3 on SU_3(8):6 [->NO_7^-(8)]", "exceptional", 130816, 32319, 7742, 8064, True),
    # Sporadic actions (15)
    ("M_22 on 2^4:A_6", "sporadic", 77, 16, 0, 4, False),
    ("J_2 on PSU_3(3)", "sporadic", 100, 36, 14, 12, True),
    ("HS on M_22", "sporadic", 100, 22, 0, 6, True),
    ("M_22 on A_7", "sporadic", 176, 70, 18, 34, False),
    ("M_23 on 2^4:A_7", "sporadic", 253, 112, 36, 60, False),
    ("McL on PSU_4(3)", "sporadic", 275, 112, 30, 56, False),
    ("M_24 on M_12:2", "sporadic", 1288, 495, 206, 180, False),
    ("Suz on G_2(4)", "sporadic", 1782, 416, 100, 96, False),
    ("Co_2 on PSU_6(2):2", "sporadic", 2300, 891, 378, 324, False),
    ("Fi_22 on 2.PSU_6(2)", "sporadic", 3510, 693, 180, 126, False),
    ("Ru on ^2F_4(2)", "sporadic", 4060, 1755, 730, 780, False),
    ("Fi_22 on Omega_7(3)", "sporadic", 14080, 3159, 918, 648, False),
    ("Fi_23 on 2.Fi_22", "sporadic", 31671, 3510, 693, 351, False),
    ("Fi_23 on POmega_8^+(3).S_3", "sporadic", 137632, 28431, 6030, 5832, False),
    ("Fi_24' on Fi_23", "sporadic", 306936, 31671, 3510, 3240, False),
)


def verify_spectral_trace_integrality_census() -> Dict[str, Any]:
    """Run exact Spectral Trace Integrality verification across all 26 individual actions
    and all 5 infinite families (`D_{5,5}(q)`, `E_{6,1}(q)`, `NO_m^eps(3)`, `NU_m(2)`, `NO_{2r+1}^eps(q)`).
    """
    indiv_results: List[Dict[str, Any]] = []
    for label, cat, n, k1, lam, mu, expected_pass in INDIVIDUAL_26_SPECS:
        ev = evaluate_srg_parameters(n, k1, lam, mu)
        sols = solve_srg_from_nk(n, k1)
        assert ev in sols, f"Exact SRG parameters missing from (n, k1) recovery on {label}"
        assert ev["passes_spectral_integrality"] == expected_pass, (
            f"Unexpected spectral outcome on {label}: {ev}"
        )
        if not expected_pass:
            assert all(not s["passes_spectral_integrality"] for s in sols), (
                f"Alternative (lam, mu) unexpectedly passed spectral integrality on {label}: {sols}"
            )
        indiv_results.append({"label": label, "category": cat, **ev})

    killed_indiv = [r["label"] for r in indiv_results if not r["passes_spectral_integrality"]]
    surviving_indiv = [r["label"] for r in indiv_results if r["passes_spectral_integrality"]]
    assert len(killed_indiv) == 18 and len(surviving_indiv) == 8

    # Infinite Family 1: D_{5,5}(q) (half-spin graph, [BvM22] Thm. 2.2.20)
    for q in (2, 3, 4, 5, 7, 8, 9):
        n = (q + 1) * (q**2 + 1) * (q**3 + 1) * (q**4 + 1)
        k1 = q * (q**5 - 1) * (q**4 - 1) // ((q**2 - 1) * (q - 1))
        r_eig = (q**3) * (q**2 + q + 1) - 1
        s_eig = -(q**2) - 1
        mu = (q**2 + 1) * (q**2 + q + 1)
        lam = mu + r_eig + s_eig
        ev = evaluate_srg_parameters(n, k1, lam, mu)
        assert ev["r"] == r_eig and ev["s"] == s_eig
        assert ev["c_delta2"] == Fraction(-(q**4 + q**2 + 1), q**2)
        assert not ev["passes_spectral_integrality"]

    # Infinite Family 2: E_{6,1}(q) ([BvM22] Prop. 4.9.1 & §4.9.2)
    for q in (2, 3, 4, 5, 7, 8, 9):
        n = (q**8 + q**4 + 1) * (q**9 - 1) // (q - 1)
        k1 = q * (q**3 + 1) * (q**8 - 1) // (q - 1)
        r_eig = (q**4) * (q**5 - 1) // (q - 1) - 1
        s_eig = -(q**3) - 1
        mu = (q**3 + 1) * (q**4 - 1) // (q - 1)
        lam = mu + r_eig + s_eig
        ev = evaluate_srg_parameters(n, k1, lam, mu)
        assert ev["r"] == r_eig and ev["s"] == s_eig
        assert ev["c_delta1"] == Fraction(q**9 + q**8 + q**5 + q**2 - 1, q + 1)
        assert ev["c_delta2"] == Fraction(-(q**6 + q**3 + 1), q**3)
        assert not ev["passes_spectral_integrality"]

    # Infinite Family 3: NO_{2m}^eps(3) and NO_{2m-1}^eps(3) ([BvM22] §§3.1.3-3.1.4)
    for m in range(3, 13):
        # Even dimension 2m, eps = -1: ALL killed via c_Delta2 = -9(3^{m-2}+1)/8 not in Z
        n_m = (3 ** (m - 1)) * (3**m + 1) // 2
        k1_m = (3 ** (m - 1)) * (3 ** (m - 1) + 1) // 2
        lam_m = (3 ** (m - 2)) * (3**m - 3) // 6
        mu_m = (3 ** (m - 2)) * (3**m + 9) // 6
        ev_m = evaluate_srg_parameters(n_m, k1_m, lam_m, mu_m)
        assert ev_m["c_delta1"] == Fraction(3**m - 3, 4)
        assert ev_m["c_delta2"] == Fraction(-9 * (3 ** (m - 2) + 1), 8)
        assert not ev_m["passes_spectral_integrality"]

        # Even dimension 2m, eps = +1: killed iff m is odd; survives iff m = 2t >= 4 (NO_{4t}^+(3))
        n_p = (3 ** (m - 1)) * (3**m - 1) // 2
        k1_p = (3 ** (m - 1)) * (3 ** (m - 1) - 1) // 2
        lam_p = (3 ** (m - 2)) * (3**m + 3) // 6
        mu_p = (3 ** (m - 2)) * (3**m - 9) // 6
        ev_p = evaluate_srg_parameters(n_p, k1_p, lam_p, mu_p)
        assert ev_p["c_delta1"] == Fraction(3**m - 1, 4)
        assert ev_p["c_delta2"] == Fraction(-(3**m - 1), 8)
        assert ev_p["passes_spectral_integrality"] == (m % 2 == 0)

        # Odd dimension 2m - 1 (already killed by Wave-2 Thm 1.2(2), verified via solve_srg_from_nk for m <= 6)
        if m <= 6:
            for eps in (1, -1):
                n_odd = (3 ** (m - 1)) * (3 ** (m - 1) + eps) // 2
                k1_odd = (3 ** (m - 2)) * (3 ** (m - 1) - eps) // 2
                sols_odd = solve_srg_from_nk(n_odd, k1_odd)
                assert len(sols_odd) == 1
                assert sols_odd[0]["passes_spectral_integrality"] == (eps == ((-1) ** m))

    # Infinite Family 4: NU_{2k}(2) ([BvM22] §3.1.6; odd m already killed by Wave-2 Thm 1.2(3))
    for k in range(2, 11):
        n_u = (2 ** (2 * k - 1)) * (4**k - 1) // 3
        k1_u = (2 ** (2 * k - 2)) * (2 ** (2 * k - 1) + 1) // 3
        lam_u = (4**k) * ((4**k) // 4 - 1) // 24
        mu_u = (4**k) * ((4**k) // 8 + 1) // 12
        ev_u = evaluate_srg_parameters(n_u, k1_u, lam_u, mu_u)
        assert ev_u["c_delta1"] == Fraction(4**k - 4, 3)
        assert ev_u["c_delta2"] == Fraction(-(4**k + 8), 9)
        assert ev_u["passes_spectral_integrality"] == (k % 3 == 0)

    # Infinite Family 5: Sp_{2r}(q) / GammaSp_{2r}(q) on O_{2r}^eps(q) (~= NO_{2r+1}^eps(q), q in {4, 8})
    for q in (4, 8):
        for r_dim in range(2, 9):
            # eps = +1: ALL killed via c_Delta2 = -(q^r + q)/(q - 1) not in Z
            n_sp_p = (q**r_dim) * (q**r_dim + 1) // 2
            k1_sp_p = (q ** (r_dim - 1) + 1) * (q**r_dim - 1)
            mu_sp_p = 2 * (q ** (r_dim - 1)) * (q ** (r_dim - 1) + 1)
            r_eig_p = (q - 2) * (q ** (r_dim - 1)) - 1
            s_eig_p = -(q ** (r_dim - 1)) - 1
            lam_sp_p = mu_sp_p + r_eig_p + s_eig_p
            ev_sp_p = evaluate_srg_parameters(n_sp_p, k1_sp_p, lam_sp_p, mu_sp_p)
            assert ev_sp_p["k2"] == (q // 2 - 1) * (q ** (r_dim - 1)) * (q**r_dim - 1)
            assert ev_sp_p["c_delta2"] == Fraction(-(q**r_dim + q), q - 1)
            assert not ev_sp_p["passes_spectral_integrality"]

            # eps = -1: passes spectral integrality (odd r_dim already killed by Wave-2 C0009 Thm 1.1(4))
            n_sp_m = (q**r_dim) * (q**r_dim - 1) // 2
            k1_sp_m = (q ** (r_dim - 1) - 1) * (q**r_dim + 1)
            mu_sp_m = 2 * (q ** (r_dim - 1)) * (q ** (r_dim - 1) - 1)
            r_eig_m = q ** (r_dim - 1) - 1
            s_eig_m = -(q - 2) * (q ** (r_dim - 1)) - 1
            lam_sp_m = mu_sp_m + r_eig_m + s_eig_m
            ev_sp_m = evaluate_srg_parameters(n_sp_m, k1_sp_m, lam_sp_m, mu_sp_m)
            assert ev_sp_m["k2"] == (q // 2 - 1) * (q ** (r_dim - 1)) * (q**r_dim + 1)
            assert ev_sp_m["c_delta1"] == Fraction(ev_sp_m["k2"] + 1 + s_eig_m, r_eig_m - s_eig_m)
            if r_dim % 2 == 0:
                assert ev_sp_m["c_delta1"] == Fraction((q - 2) * (q**r_dim - 1), 2 * (q - 1))
                assert ev_sp_m["c_delta2"] == Fraction(-(q**r_dim - 1), q - 1)
            assert ev_sp_m["passes_spectral_integrality"]

    return {
        "individual_total": len(indiv_results),
        "individual_killed_count": len(killed_indiv),
        "individual_surviving_count": len(surviving_indiv),
        "individual_killed": killed_indiv,
        "individual_survivors": surviving_indiv,
        "individual_records": indiv_results,
    }


# ======================================================================
# 2. Sp_4(8) & Sp_4(8).3 on NO_5^-(8) (deg 2016) and NO_5^+(8) (deg 2080)
# ======================================================================


def build_sp4_8_quadric_actions() -> Dict[str, Tuple[int, List[Perm], Perm]]:
    """Construct exact affine-form pullback actions of `Sp_4(8)` (`|Sp_4(8)| = 1,056,706,560`)
    and `Sp_4(8).3 = GammaSp_4(8)` (`3,170,119,680`) on the two `Sp_4(8)`-orbits of quadratic forms
    `Q_v(x) = Q_0(x) + B(v, x)^2` polarising to `B` over `F_8^4`:
      - `minus_2016` (`NO_5^-(8)`): `{v in F_8^4 : Tr_{F_8/F_2}(Q_0(v)) = 1}` (`2016` forms);
      - `plus_2080` (`NO_5^+(8)`): `{v in F_8^4 : Tr_{F_8/F_2}(Q_0(v)) = 0}` (`2080` forms).
    Returns mapping `{key: (degree, sp4_8_gens, frob_gen)}`.
    """
    gf8_mul = [[0] * 8 for _ in range(8)]
    for a in range(8):
        for b in range(8):
            p, aa, bb = 0, a, b
            for _ in range(3):
                if bb & 1:
                    p ^= aa
                carry = aa & 4
                aa = (aa << 1) & 7
                if carry:
                    aa ^= 3
                bb >>= 1
            gf8_mul[a][b] = p

    sq8 = [gf8_mul[a][a] for a in range(8)]
    sqrt8 = [sq8[sq8[a]] for a in range(8)]
    tr8 = [a ^ sq8[a] ^ sqrt8[a] for a in range(8)]

    vecs8 = list(itertools.product(range(8), repeat=4))

    def b8(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        return (
            gf8_mul[x[0]][y[1]]
            ^ gf8_mul[x[1]][y[0]]
            ^ gf8_mul[x[2]][y[3]]
            ^ gf8_mul[x[3]][y[2]]
        )

    def q0_8(x: Tuple[int, ...]) -> int:
        return gf8_mul[x[0]][x[1]] ^ gf8_mul[x[2]][x[3]]

    plus_2080 = [v for v in vecs8 if tr8[q0_8(v)] == 0]
    minus_2016 = [v for v in vecs8 if tr8[q0_8(v)] == 1]
    assert len(plus_2080) == 2080 and len(minus_2016) == 2016
    p_idx = {v: i for i, v in enumerate(plus_2080)}
    m_idx = {v: i for i, v in enumerate(minus_2016)}

    basis4 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

    def induce_transvection(
        a: Tuple[int, ...],
        c: int,
        pool: Sequence[Tuple[int, ...]],
        mp: Dict[Tuple[int, ...], int],
    ) -> Perm:
        t_basis = [
            tuple(e[k] ^ gf8_mul[gf8_mul[c][b8(e, a)]][a[k]] for k in range(4))
            for e in basis4
        ]
        q0_tb = [q0_8(te) for te in t_basis]
        return tuple(
            mp[tuple(sqrt8[q0_tb[idx] ^ sq8[b8(t_basis[idx], v)]] for idx in (1, 0, 3, 2))]
            for v in pool
        )

    rng = random.Random(323)
    nz8 = [v for v in vecs8 if v != (0, 0, 0, 0)]
    extra_vecs = rng.sample(nz8, 2)
    gen_specs = [(e, 1) for e in basis4] + [(extra_vecs[0], 1), (extra_vecs[1], 2)]

    sp48_minus = [induce_transvection(a, c, minus_2016, m_idx) for a, c in gen_specs]
    frob_minus = tuple(m_idx[tuple(sq8[c] for c in v)] for v in minus_2016)

    sp48_plus = [induce_transvection(a, c, plus_2080, p_idx) for a, c in gen_specs]
    frob_plus = tuple(p_idx[tuple(sq8[c] for c in v)] for v in plus_2080)

    return {
        "minus_2016": (2016, sp48_minus, frob_minus),
        "plus_2080": (2080, sp48_plus, frob_plus),
    }


def verify_sp4_8_uod_and_outer_exclusion() -> Dict[str, Any]:
    """Certify UOD structure on `Sp_4(8)` & `Sp_4(8).3` (`deg 2016`), including that
    `100%` of the `(9, 576)` UOD candidates in `Sp_4(8).3` lie inside `Sp_4(8)` (`0` outer `.3` UODs)
    and have semiregular orders `2` (on `455`) and `7` (on `1560`).
    """
    acts = build_sp4_8_quadric_actions()
    n, sp_gens, frob = acts["minus_2016"]

    pg_sp = PermGroup(n, sp_gens, initial_base=[0], allow_jordan_fastpath=False)
    assert pg_sp.order() == 1_056_706_560
    uod_sp = check_uod_bsgs("Sp_4(8)_deg2016", n, sp_gens)
    assert uod_sp["rank"] == 5
    assert uod_sp["uod_by_suborbit"] == [(455, 9), (520, 0), (520, 0), (520, 0)]
    assert not uod_sp["passes_lemma_3_2a"]

    full_gens = sp_gens + [frob]
    pg_full = PermGroup(n, full_gens, initial_base=[0], allow_jordan_fastpath=False)
    assert pg_full.order() == 3_170_119_680

    # Extract exact UOD elements in representative cosets of 455 and 1560 inside Sp_4(8).3
    sub_orbs = sorted(pg_full.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o), o[0]))
    assert [len(o) for o in sub_orbs] == [1, 455, 1560]
    orb_id = [0] * n
    for idx, o in enumerate(sub_orbs):
        for pt in o:
            orb_id[pt] = idx
    tr_inv0 = pg_full.trans_inv[0]
    color = [[orb_id[tr_inv0[u][v]] for v in range(n)] for u in range(n)]
    active_levels = [lvl for lvl in range(1, len(pg_full.base)) if len(pg_full.orbits_list[lvl]) > 1]
    m_act = len(active_levels)
    already = [False] * n
    already[0] = True
    newly_fixed: List[List[int]] = []
    trans_by_act: List[List[Perm]] = []
    for j, lvl in enumerate(active_levels):
        trans_by_act.append(list(pg_full.trans[lvl].values()))
        nxt_g = pg_full.level_gens[active_levels[j + 1]] if j + 1 < m_act else []
        fn = [y for y in range(n) if (not already[y]) and all(g[y] == y for g in nxt_g)]
        for y in fn:
            already[y] = True
        newly_fixed.append(fn)
    rem_un = [y for y in range(n) if not already[y]]

    def extract_coset_uod(x0: int) -> List[Perm]:
        target = orb_id[x0]
        u0 = pg_full.trans[0][x0]
        if any(color[y][u0[y]] != target for y in rem_un):
            return []
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

    def semireg_order(p: Perm) -> int:
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
                return 0
        return ord0

    cands_455 = extract_coset_uod(sub_orbs[1][0])
    cands_1560 = extract_coset_uod(sub_orbs[2][0])
    assert len(cands_455) == 9 and len(cands_1560) == 576
    in_sp_455 = sum(1 for p in cands_455 if pg_sp.contains(p))
    in_sp_1560 = sum(1 for p in cands_1560 if pg_sp.contains(p))
    orders_455 = dict(Counter(semireg_order(p) for p in cands_455))
    orders_1560 = dict(Counter(semireg_order(p) for p in cands_1560))
    assert in_sp_455 == 9 and in_sp_1560 == 576
    assert orders_455 == {2: 9} and orders_1560 == {7: 576}

    return {
        "sp4_8_order": pg_sp.order(),
        "sp4_8_uod": uod_sp["uod_by_suborbit"],
        "sp4_8_dot3_order": pg_full.order(),
        "sp4_8_dot3_uod": [(455, len(cands_455)), (1560, len(cands_1560))],
        "in_inner_sp4_8": (in_sp_455, in_sp_1560),
        "semiregular_orders": (orders_455, orders_1560),
    }


# ======================================================================
# 3. POmega_8^+(3) & PO_8^+(3) on NO_8^+(3) (deg 1080) & Exhaustive Collapse
# ======================================================================


def build_no8_plus_3_actions() -> Tuple[List[Perm], List[Perm]]:
    """Construct exact generators `(pomega8_gens, po8_gens)` on the canonical `1,080`
    projective points `_paige_m3_points()` of `NO_8^+(3)`:
      - `POmega_8^+(3)` of order `4,952,179,814,400` (generated by even products of reflections
        of the same spinor/square norm);
      - `PO_8^+(3) = O_8^+(3) / {+-I_8}` of order `19,808,719,257,600 = 4 * |POmega_8^+(3)|`
        (the full almost-simple stabilizer of `NO_8^+(3)` inside `Aut(POmega_8^+(3))`, since
        no triality automorphism fixes `NO_8^+(3)`).
    """
    pts1080, pts_minus = _paige_m3_points()
    p1080_i = {v: i for i, v in enumerate(pts1080)}

    def norm1080(v: Tuple[int, ...]) -> int:
        ic = 1 if next(c for c in v if c != 0) == 1 else 2
        return p1080_i[tuple((c * ic) % 3 for c in v)]

    def b_zorn(x: Tuple[int, ...], y: Tuple[int, ...]) -> int:
        return (
            x[0] * y[1]
            + x[1] * y[0]
            - x[2] * y[5]
            - x[5] * y[2]
            - x[3] * y[6]
            - x[6] * y[3]
            - x[4] * y[7]
            - x[7] * y[4]
        ) % 3

    def refl8(a: Tuple[int, ...], qa_inv: int) -> Perm:
        return tuple(
            norm1080(tuple((x[k] - ((b_zorn(x, a) * qa_inv) % 3) * a[k]) % 3 for k in range(8)))
            for x in pts1080
        )

    rng = random.Random(323)
    r_plus_0 = refl8(pts1080[0], 1)
    r_minus_0 = refl8(pts_minus[0], 2)
    sample_plus = rng.sample(pts1080[1:], 10)[:4]
    sample_minus = rng.sample(pts_minus[1:], 10)[:4]
    pomega8_gens = [compose(r_plus_0, refl8(a, 1)) for a in sample_plus] + [
        compose(r_minus_0, refl8(b, 2)) for b in sample_minus
    ]
    po8_gens = pomega8_gens + [r_plus_0, r_minus_0]
    return pomega8_gens, po8_gens


def classify_no8_plus_3_left_bol_exhaustive() -> Dict[str, Any]:
    """Exhaustively classify ALL left Bol loops `Q` on `{0, ..., 1079}` (`NO_8^+(3)`) with
    `Mlt(Q) <= PO_8^+(3)` sharing the rank-3 orbitals `(1, 351, 728)` of `NO_8^+(3)`.

    Combines exact BSGS UOD extraction (confirming `100%` of the `(1080, 30240)` UOD elements
    lie in `POmega_8^+(3)` and satisfy power-UOD) with lossless multi-depth Schreier centralizer
    symmetry breaking (`Stab_{PO_8^+(3)}(0)` conjugation is an exact loop-isomorphism gauge
    preserving `PO_8^+(3)` and its orbitals) and unit-singleton Bol closure propagation.
    """
    n = 1080
    id_p = identity_perm(n)
    m3_loop = build_paige_m3()
    pomega8_gens, po8_gens = build_no8_plus_3_actions()

    pg_omega = PermGroup(n, pomega8_gens, initial_base=[0], allow_jordan_fastpath=False)
    pg = PermGroup(n, po8_gens, initial_base=[0], allow_jordan_fastpath=False)
    assert pg_omega.order() == 4_952_179_814_400
    assert pg.order() == 19_808_719_257_600

    sub_orbs = sorted(pg.stabilizer_orbits(0), key=lambda o: (o[0] != 0, len(o), o[0]))
    assert [len(o) for o in sub_orbs] == [1, 351, 728]
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
        t = orb_id[p[0]]
        if t == 0:
            return p == id_p
        col = color
        for y in range(n):
            if col[y][p[y]] != t:
                return False
        return True

    def all_uod_in_coset(x0: int) -> List[Perm]:
        target = orb_id[x0]
        u0 = pg.trans[0][x0]
        if any(color[y][u0[y]] != target for y in rem_un):
            return []
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

    def semireg_order(p: Perm) -> int:
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
                return 0
        return ord0

    st0_gens = pg.level_gens[1]
    rc0_by_orb: Dict[int, List[Perm]] = {}
    h_map: Dict[int, Tuple[Perm, Perm]] = {0: (id_p, id_p)}
    for idx_o, o in enumerate(sub_orbs[1:], start=1):
        x0 = o[0]
        rc0 = all_uod_in_coset(x0)
        expected_ord = 2 if idx_o == 1 else 3
        for p in rc0:
            assert pg_omega.contains(p), "Unexpected outer UOD element outside POmega_8^+(3)"
            assert semireg_order(p) == expected_ord
            ip = invert(p)
            assert is_uod(ip)
            cur = compose(p, p)
            while cur != id_p:
                assert is_uod(cur)
                cur = compose(cur, p)
        rc0_by_orb[idx_o] = rc0
        h_map[x0] = (id_p, id_p)
        qh = deque([x0])
        while qh:
            u = qh.popleft()
            hu, _ = h_map[u]
            for g in st0_gens:
                v = g[u]
                if v not in h_map:
                    hv = compose(g, hu)
                    h_map[v] = (hv, invert(hv))
                    qh.append(v)

    assert len(rc0_by_orb[1]) == 1080 and len(rc0_by_orb[2]) == 30240

    def get_raw_cands(v: int) -> List[Perm]:
        hv, hvi = h_map[v]
        return [compose(hv, compose(p, hvi)) for p in rc0_by_orb[orb_id[v]]]

    def conj_orbits_and_stabilizer(
        gens: Sequence[Perm], cands: Sequence[Perm]
    ) -> List[Tuple[Perm, List[Perm]]]:
        if not gens or len(cands) <= 1:
            return [(c, list(gens)) for c in cands]
        g_invs = [invert(g) for g in gens]
        pool = set(cands)
        seen: Set[Perm] = set()
        out: List[Tuple[Perm, List[Perm]]] = []
        for c0 in cands:
            if c0 in seen:
                continue
            tree: Dict[Perm, Tuple[Perm, Perm]] = {c0: (id_p, id_p)}
            seen.add(c0)
            q = deque([c0])
            while q:
                cur = q.popleft()
                uc, _ = tree[cur]
                for g, gi in zip(gens, g_invs):
                    nc = compose(g, compose(cur, gi))
                    assert nc in pool
                    if nc not in tree:
                        nuc = compose(g, uc)
                        tree[nc] = (nuc, invert(nuc))
                        seen.add(nc)
                        q.append(nc)
            stab_pg = PermGroup(n, [], allow_jordan_fastpath=False)
            for cur, (uc, _) in tree.items():
                for g, gi in zip(gens, g_invs):
                    nc = compose(g, compose(cur, gi))
                    _, nuci = tree[nc]
                    sch = compose(nuci, compose(g, uc))
                    if sch != id_p and not stab_pg.contains(sch):
                        stab_pg = PermGroup(
                            n, list(stab_pg.generators) + [sch], allow_jordan_fastpath=False
                        )
            out.append((c0, list(stab_pg.generators)))
        return out

    def compat_pair(pa: Perm, pb: Perm) -> bool:
        for z in range(n):
            if pa[z] == pb[z]:
                return False
        return is_uod(compose(pa, compose(pb, pa))) and is_uod(compose(pb, compose(pa, pb)))

    def add_with_bol_closure(
        start_x: int, start_p: Perm, chosen_dict: Dict[int, Perm]
    ) -> Optional[Dict[int, Perm]]:
        if start_x in chosen_dict:
            return {} if chosen_dict[start_x] == start_p else None
        to_add: Dict[int, Perm] = {start_x: start_p}
        q_cl: List[Perm] = [start_p]
        while q_cl:
            a = q_cl.pop()
            for unary in (invert(a), compose(a, a)):
                u0 = unary[0]
                if u0 in chosen_dict:
                    if chosen_dict[u0] != unary:
                        return None
                elif u0 in to_add:
                    if to_add[u0] != unary:
                        return None
                elif is_uod(unary):
                    to_add[u0] = unary
                    q_cl.append(unary)
                else:
                    return None
            cur_vals = [v for k, v in chosen_dict.items() if k != 0] + list(to_add.values())
            for b in cur_vals:
                for prod in (compose(a, compose(b, a)), compose(b, compose(a, b))):
                    z0 = prod[0]
                    if z0 in chosen_dict:
                        if chosen_dict[z0] != prod:
                            return None
                    elif z0 in to_add:
                        if to_add[z0] != prod:
                            return None
                    elif is_uod(prod):
                        to_add[z0] = prod
                        q_cl.append(prod)
                    else:
                        return None
        new_items = list(to_add.items())
        for idx_i, (_, pi) in enumerate(new_items):
            for pj in chosen_dict.values():
                for w in range(n):
                    if pi[w] == pj[w]:
                        return None
            for _, pj in new_items[idx_i + 1 :]:
                for w in range(n):
                    if pi[w] == pj[w]:
                        return None
        return to_add

    # Depth 1: x1 = 1 in 351-orbital (place M(3)'s L_{x1} first so it is the canonical orbit rep)
    x1 = sub_orbs[1][0]
    raw_x1 = get_raw_cands(x1)
    m3_lx1 = m3_loop.L[x1]
    assert m3_lx1 in set(raw_x1)
    raw_x1_ordered = [m3_lx1] + [p for p in raw_x1 if p != m3_lx1]

    st0_pg = PermGroup(n, st0_gens, initial_base=[x1], allow_jordan_fastpath=False)
    reps1 = conj_orbits_and_stabilizer(st0_pg.level_gens[1], raw_x1_ordered)
    assert len(reps1) == 1, f"Expected 1 conjugacy orbit at x1={x1}, got {len(reps1)}"
    rep1, h1_gens = reps1[0]
    assert rep1 == m3_lx1
    for g in h1_gens:
        assert g[0] == 0 and g[x1] == x1 and compose(g, compose(rep1, invert(g))) == rep1

    chosen_root: Dict[int, Perm] = {0: id_p}
    add1 = add_with_bol_closure(x1, rep1, chosen_root)
    assert add1 is not None
    chosen_root.update(add1)

    # Materialize all 1,078 rep1-compatible pools via H_1-orbit equivariance
    h1_pg = PermGroup(n, h1_gens, allow_jordan_fastpath=False)
    assert h1_pg.order() == 48_384
    pools: Dict[int, List[Perm]] = {}
    for ho in h1_pg.orbits():
        u0 = ho[0]
        if u0 in chosen_root:
            continue
        base_pool = [p for p in get_raw_cands(u0) if compat_pair(rep1, p)]
        pools[u0] = base_pool
        t_map: Dict[int, Tuple[Perm, Perm]] = {u0: (id_p, id_p)}
        qt = deque([u0])
        while qt:
            cur_u = qt.popleft()
            tu, _ = t_map[cur_u]
            for g in h1_gens:
                nxt_u = g[cur_u]
                if nxt_u not in t_map:
                    ntu = compose(g, tu)
                    ntui = invert(ntu)
                    t_map[nxt_u] = (ntu, ntui)
                    pools[nxt_u] = [compose(ntu, compose(p, ntui)) for p in base_pool]
                    qt.append(nxt_u)

    # Depth 2: MRV variable y1 in 728-orbital (pool size 4, 1 orbit under Stab_{H_1}(y1))
    y1 = min((u for u in range(1, n) if u not in chosen_root), key=lambda u: (len(pools[u]), u))
    m3_ly1 = m3_loop.L[y1]
    assert m3_ly1 in set(pools[y1])
    pool_y1_ordered = [m3_ly1] + [p for p in pools[y1] if p != m3_ly1]

    h1_y1_pg = PermGroup(n, h1_gens, initial_base=[y1], allow_jordan_fastpath=False)
    reps2 = conj_orbits_and_stabilizer(
        h1_y1_pg.level_gens[1] if len(h1_y1_pg.base) > 1 else [], pool_y1_ordered
    )
    assert len(reps2) == 1, f"Expected 1 conjugacy orbit at y1={y1}, got {len(reps2)}"

    moufang_hits = 0
    proper_hits = 0
    found_loops: List[Loop] = []
    nodes_visited = 0

    def solve_bt(
        chosen_cur: Dict[int, Perm],
        cur_pools: Dict[int, List[Perm]],
        sym_gens: List[Perm],
    ) -> None:
        nonlocal moufang_hits, proper_hits, nodes_visited
        nodes_visited += 1

        # Lossless batch unit propagation of forced singleton pools (0 branching choices)
        while len(chosen_cur) < n:
            unit_items: List[Tuple[int, Perm]] = []
            for u in range(1, n):
                if u in chosen_cur:
                    continue
                lu = len(cur_pools[u])
                if lu == 0:
                    return
                if lu == 1:
                    unit_items.append((u, cur_pools[u][0]))
            if not unit_items:
                break
            nxt_chosen = dict(chosen_cur)
            batch_added: List[Perm] = []
            for u_f, p_f in unit_items:
                if u_f in nxt_chosen:
                    if nxt_chosen[u_f] != p_f:
                        return
                    continue
                added_u = add_with_bol_closure(u_f, p_f, nxt_chosen)
                if added_u is None:
                    return
                nxt_chosen.update(added_u)
                batch_added.extend(added_u.values())
                if len(nxt_chosen) == n:
                    break
            chosen_cur = nxt_chosen
            if len(chosen_cur) == n:
                cur_pools = {}
                break
            nxt_pools: Dict[int, List[Perm]] = {}
            for u in range(1, n):
                if u in chosen_cur:
                    continue
                pu_list = [q for q in cur_pools[u] if all(compat_pair(a, q) for a in batch_added)]
                if not pu_list:
                    return
                nxt_pools[u] = pu_list
            cur_pools = nxt_pools

        if len(chosen_cur) == n:
            tbl = [list(chosen_cur[u]) for u in range(n)]
            lp = Loop(tbl, name=f"NO8_plus_3_hit_{len(found_loops)}", validate_loop=True)
            is_lb, _ = lp.check_left_bol()
            if not is_lb:
                return
            if not all(pg.contains(lp.R[u]) for u in range(1, n)):
                return
            is_mf, _ = lp.check_moufang()
            if is_mf:
                moufang_hits += 1
            else:
                proper_hits += 1
            found_loops.append(lp)
            return

        rem_u = [u for u in range(1, n) if u not in chosen_cur]
        best_u = min(rem_u, key=lambda u: (len(cur_pools[u]), u))
        cands_u = cur_pools[best_u]
        if sym_gens and len(cands_u) > 1:
            sg_pg = PermGroup(n, sym_gens, initial_base=[best_u], allow_jordan_fastpath=False)
            sub_g = sg_pg.level_gens[1] if len(sg_pg.base) > 1 else []
            branches = conj_orbits_and_stabilizer(sub_g, cands_u)
        else:
            branches = [(c, []) for c in cands_u]

        for pu, nxt_sym in branches:
            added = add_with_bol_closure(best_u, pu, chosen_cur)
            if added is None:
                continue
            nxt_chosen = dict(chosen_cur)
            nxt_chosen.update(added)
            if len(nxt_chosen) == n:
                solve_bt(nxt_chosen, {}, nxt_sym)
                continue
            added_vals = list(added.values())
            nxt_pools = {}
            dead = False
            for u in range(1, n):
                if u in nxt_chosen:
                    continue
                pu_list = [q for q in cur_pools[u] if all(compat_pair(a, q) for a in added_vals)]
                if not pu_list:
                    dead = True
                    break
                nxt_pools[u] = pu_list
            if not dead:
                solve_bt(nxt_chosen, nxt_pools, nxt_sym)

    for rep2, h2_gens in reps2:
        for g in h2_gens:
            assert g[0] == 0 and g[x1] == x1 and g[y1] == y1
            assert compose(g, compose(rep1, invert(g))) == rep1
            assert compose(g, compose(rep2, invert(g))) == rep2
        added2 = add_with_bol_closure(y1, rep2, chosen_root)
        assert added2 is not None
        c2 = dict(chosen_root)
        c2.update(added2)
        added2_vals = list(added2.values())
        p2: Dict[int, List[Perm]] = {}
        for u in range(1, n):
            if u in c2:
                continue
            p2[u] = [q for q in pools[u] if all(compat_pair(a, q) for a in added2_vals)]
        solve_bt(c2, p2, h2_gens)

    assert moufang_hits == 1 and proper_hits == 0 and len(found_loops) == 1
    assert found_loops[0].table == m3_loop.table

    return {
        "pomega8_order": pg_omega.order(),
        "po8_order": pg.order(),
        "uod_counts": [(351, len(rc0_by_orb[1])), (728, len(rc0_by_orb[2]))],
        "depth1_orbits": len(reps1),
        "h1_order": h1_pg.order(),
        "depth2_pool_size": len(pool_y1_ordered),
        "depth2_orbits": len(reps2),
        "nodes_visited": nodes_visited,
        "moufang_hits": moufang_hits,
        "proper_left_bol_hits": proper_hits,
        "unique_hit_equals_paige_m3": found_loops[0].table == m3_loop.table,
    }


# ======================================================================
# 4. Fast Unit Tests & Full CLI Runner
# ======================================================================


class TestWave3Fast(unittest.TestCase):
    def test_wave3_1_spectral_trace_integrality_all_rank3_as(self) -> None:
        """Certify exact Spectral Trace Integrality across all 26 individual actions and
        all 5 infinite families (`D_{5,5}`, `E_{6,1}`, `NO_m^eps(3)`, `NU_m(2)`, `NO_{2r+1}^eps(q)`).
        """
        res = verify_spectral_trace_integrality_census()
        self.assertEqual(res["individual_total"], 26)
        self.assertEqual(res["individual_killed_count"], 18)
        self.assertEqual(res["individual_surviving_count"], 8)
        # All 9 large sporadics (deg >= 1288) are killed by pure arithmetic
        for spor_label in (
            "M_24 on M_12:2",
            "Suz on G_2(4)",
            "Co_2 on PSU_6(2):2",
            "Fi_22 on 2.PSU_6(2)",
            "Ru on ^2F_4(2)",
            "Fi_22 on Omega_7(3)",
            "Fi_23 on 2.Fi_22",
            "Fi_23 on POmega_8^+(3).S_3",
            "Fi_24' on Fi_23",
        ):
            self.assertIn(spor_label, res["individual_killed"])

    def test_wave3_2_paige_m3_rank3_positive_control(self) -> None:
        """Certify Paige's simple Moufang loop M(3) (`|M(3)| = 1080`) has
        `Mlt(M(3)) ~= POmega_8^+(3)` of order `4,952,179,814,400` and rank `3` `(1, 351, 728)`.
        """
        m3 = build_paige_m3()
        self.assertEqual(m3.n, 1080)
        self.assertFalse(m3.check_associative()[0])
        self.assertTrue(m3.check_left_bol()[0])
        self.assertTrue(m3.check_moufang()[0])
        is_simp, ns = m3.check_simplicity()
        self.assertTrue(is_simp)
        self.assertEqual(ns, [])
        mlt = m3.Mlt()
        self.assertIsNone(mlt._giant_kind)
        self.assertEqual(mlt.order(), 4_952_179_814_400)
        self.assertEqual(mlt.rank(0), 3)
        self.assertEqual(mlt.subdegrees(0), (1, 351, 728))

    def test_wave3_3_sp4_8_quadric_uod_and_outer_exclusion(self) -> None:
        """Certify `Sp_4(8)` (`0` UOD on `520`s) and `Sp_4(8).3` (`[(455, 9), (1560, 576)]`
        with `100%` of UOD candidates inside inner `Sp_4(8)` of semiregular orders `2` and `7`).
        """
        res = verify_sp4_8_uod_and_outer_exclusion()
        self.assertEqual(res["sp4_8_uod"], [(455, 9), (520, 0), (520, 0), (520, 0)])
        self.assertEqual(res["sp4_8_dot3_uod"], [(455, 9), (1560, 576)])
        self.assertEqual(res["in_inner_sp4_8"], (9, 576))
        self.assertEqual(res["semiregular_orders"], ({2: 9}, {7: 576}))


def run_full_wave3_sweep() -> None:
    t0 = time.time()
    print("=== [1/4] Spectral Trace Integrality Census (26 Individual + 5 Infinite Families) ===")
    spec = verify_spectral_trace_integrality_census()
    print(
        f"  Individual actions: {spec['individual_killed_count']}/26 killed by spectral integrality, "
        f"{spec['individual_surviving_count']}/26 spectral survivors."
    )
    print(f"  Survivors: {spec['individual_survivors']}")

    print("\n=== [2/4] Sp_4(8) & Sp_4(8).3 on NO_5^+(8) (deg 2080) and NO_5^-(8) (deg 2016) ===")
    t_sp = time.time()
    acts = build_sp4_8_quadric_actions()
    n_p, sp_p, frob_p = acts["plus_2080"]
    uod_2080 = check_uod_bsgs("Sp_4(8).3_NO5+_deg2080", n_p, sp_p + [frob_p])
    assert uod_2080["order"] == 3_170_119_680
    assert uod_2080["uod_by_suborbit"] == [(567, 0), (1512, 0)]
    print(f"  Sp_4(8).3 (deg 2080): uod={uod_2080['uod_by_suborbit']} ({time.time() - t_sp:.2f}s)")

    uod_2016_info = verify_sp4_8_uod_and_outer_exclusion()
    print(
        f"  Sp_4(8) (deg 2016, rank 5): uod={uod_2016_info['sp4_8_uod']}\n"
        f"  Sp_4(8).3 (deg 2016, rank 3): uod={uod_2016_info['sp4_8_dot3_uod']}, "
        f"in_Sp4_8={uod_2016_info['in_inner_sp4_8']}, orders={uod_2016_info['semiregular_orders']}"
    )
    t_bol = time.time()
    n_m, sp_m, frob_m = acts["minus_2016"]
    bol_2016 = classify_left_bol_uod_transversals(
        "Sp_4(8).3_NO5-_deg2016", n_m, sp_m + [frob_m], stop_on_first_proper=False
    )
    assert bol_2016["wiped_by_arc_consistency"]
    assert bol_2016["moufang_loops"] == 0 and bol_2016["proper_left_bol_loops"] == 0
    print(
        f"  Sp_4(8).3 (deg 2016) left-Bol transversal classification ({time.time() - t_bol:.2f}s): "
        f"wiped_by_arc_consistency={bol_2016['wiped_by_arc_consistency']}, "
        f"moufang={bol_2016['moufang_loops']}, proper={bol_2016['proper_left_bol_loops']}"
    )

    print("\n=== [3/4] Paige M(3) Positive Control & POmega_8^+(3) vs PO_8^+(3) UOD Equality ===")
    t_m3 = time.time()
    m3 = build_paige_m3()
    assert m3.check_left_bol()[0] and m3.check_moufang()[0] and not m3.check_associative()[0]
    assert m3.check_simplicity() == (True, [])
    assert m3.Mlt().order() == 4_952_179_814_400 and m3.Mlt().subdegrees(0) == (1, 351, 728)
    pomega_gens, _ = build_no8_plus_3_actions()
    uod_omega = check_uod_bsgs("POmega_8^+(3)_deg1080", 1080, pomega_gens)
    assert uod_omega["uod_by_suborbit"] == [(351, 1080), (728, 30240)]
    print(
        f"  Paige M(3) certified & POmega_8^+(3) UOD = {uod_omega['uod_by_suborbit']} ({time.time() - t_m3:.2f}s)"
    )

    print("\n=== [4/4] Exhaustive Left-Bol Classification on Full PO_8^+(3) (deg 1080) ===")
    t_no8 = time.time()
    no8_res = classify_no8_plus_3_left_bol_exhaustive()
    print(
        f"  Full PO_8^+(3) (|G|={no8_res['po8_order']}, {time.time() - t_no8:.2f}s): "
        f"uod={no8_res['uod_counts']}, depth1_orbits={no8_res['depth1_orbits']} (|H_1|={no8_res['h1_order']}), "
        f"depth2_pool={no8_res['depth2_pool_size']} -> {no8_res['depth2_orbits']} orbit, "
        f"nodes={no8_res['nodes_visited']}, moufang={no8_res['moufang_hits']} (== M(3): "
        f"{no8_res['unique_hit_equals_paige_m3']}), proper_left_bol={no8_res['proper_left_bol_hits']}"
    )
    print(f"\nALL WAVE-3 CHECKS CERTIFIED IN {time.time() - t0:.2f}s.")


if __name__ == "__main__":
    if "--full" in sys.argv:
        run_full_wave3_sweep()
    else:
        unittest.main(verbosity=2)
