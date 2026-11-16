#!/usr/bin/env python3
"""Exact multiplicity checks for the intrinsic matched-rank comparison.

Standard library only.  This verifies the orbit bookkeeping of AQ.27--AQ.29,
the aggregated spectral table, all its dimensions, the moment-transfer formula,
and the canonical low spectral cluster.  It does not enumerate a full loop
table, reconstruct the extension-field pencils, or prove the all-h theorem.
The separate incidence checker and written proof own those obligations.

At h=1 an independent loop over the allowed character labels reproduces the
entire spectral multiset.  At h=1,2,3,4 exact rational calculations check the
dimension, fixed-space rank, transfer measure, moments 1,2,3,4, low cutoff and
top multiplicity.  The fixed quadratic filter is checked both by its exact
spectrum and by moments 2,3,4, including its explicit residual estimate.
A bounded h=8 calculation illustrates, but does not prove, the stated
asymptotics of the normalized Hilbert--Schmidt energy ratios.
"""

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import comb


@dataclass(frozen=True)
class Parameters:
    h: int
    kind: str

    @property
    def k(self):
        return 2 * self.h + 1

    @property
    def nparams(self):
        return 3**self.k

    @property
    def wsize(self):
        return 729 ** (6 * self.h)

    @property
    def kernel(self):
        return 729 ** (2 * self.h)

    @property
    def r(self):
        return F(1, 729 ** (4 * self.h))

    @property
    def compatible(self):
        exponent = 4 * self.h if self.kind == "spread" else 6 * self.h - 1
        assert self.kind in ("spread", "aligned")
        return 729**exponent

    @property
    def dimension(self):
        return 7 * self.nparams * 49**self.k * self.wsize

    @property
    def low_dimension(self):
        return 7 * self.nparams * self.wsize * (49**self.k - 17**self.k)


def quotient7(numerator):
    assert numerator % 7 == 0
    return numerator // 7


def scalar_multiplicities(p):
    n, w, kernel, x = p.nparams, p.wsize, p.kernel, p.compatible
    a0 = quotient7(w - 1 + (n - 1) * (kernel - 1))
    b0 = quotient7((n - 1) * (w - kernel))
    a1 = quotient7(3 * (w - 1) + (n - 3) * (x - 1))
    b1 = quotient7((n - 3) * (w - x))
    assert a0 + b0 == a1 + b1 == quotient7(n * (w - 1))
    return a0, b0, a1, b1


def add_product(spectrum, left, right, scale):
    for eigenvalue, count in left:
        for factor, multiplicity in right:
            if count:
                spectrum[eigenvalue * factor] += scale * count * multiplicity


def spectrum_table(p):
    """Aggregated table; equal numerical eigenvalues are automatically merged."""
    a0, b0, a1, b1 = scalar_multiplicities(p)
    spectrum = defaultdict(int)
    for j in range(p.k + 1):
        c = comb(p.k, j) * 16**j
        nonzero_alpha = 3**j - 1
        ring_zero_w = [(F(1), 1), (F(1, 9**j), 6)]
        ring_nonzero_w = ring_zero_w + [(F(1, 49**p.k), 42)]
        add_product(
            spectrum,
            [(F(1), p.nparams), (p.r, p.nparams * nonzero_alpha)],
            ring_zero_w,
            c,
        )
        add_product(
            spectrum,
            [
                (F(1), a0),
                (F(1, 49), b0),
                (p.r, nonzero_alpha * a1),
                (p.r / 49, nonzero_alpha * b1),
            ],
            ring_nonzero_w,
            c,
        )
    return dict(spectrum)


def plane_orbits():
    """Enumerate the actual order-three dilation on F_7^2."""
    unseen = set(product(range(7), repeat=2))
    sizes = []
    while unseen:
        x, y = min(unseen)
        orbit = {((a * x) % 7, (a * y) % 7) for a in (1, 2, 4)}
        assert orbit <= unseen
        unseen -= orbit
        sizes.append(len(orbit))
    assert sorted(sizes) == [1] + [3] * 16
    assert sum(sizes) == 49
    return sizes.count(3)


def spectrum_from_labels(p):
    """Direct AQ.27--29 character labels, without using the j-aggregated table.

    One nonzero W orbit has size seven.  The exact incidence counts supply its
    compatible and incompatible orbit totals.  The V orbit supports and all
    allowed alpha, nu, rho, sigma labels are then enumerated explicitly.
    """
    assert p.h == 1  # Deliberately bounded independent bookkeeping control.
    plane_count = plane_orbits()
    zero = (0,) * p.k
    parameters = list(product(range(3), repeat=p.k))
    result = defaultdict(int)
    for mask in range(1 << p.k):
        active = tuple(bool(mask & (1 << i)) for i in range(p.k))
        j = sum(active)
        vorbits = plane_count**j
        for alpha in parameters:
            if any(alpha[i] and not active[i] for i in range(p.k)):
                continue
            rank_factor = F(1) if alpha == zero else p.r
            proportional = {
                tuple((a * x) % 3 for x in alpha) for a in range(3)
            }
            for nu in parameters:
                if nu == zero:
                    count = p.wsize
                elif alpha == zero:
                    count = p.kernel
                elif nu in proportional:
                    count = p.wsize
                else:
                    count = p.compatible
                good = quotient7(count - 1)
                bad = quotient7(p.wsize - count)
                for rho in range(7):
                    # For w=0, only sigma=0 is an allowed orbit character.
                    factor_zero = F(1) if rho == 0 else F(1, 9**j)
                    result[rank_factor * factor_zero] += vorbits
                    # For w!=0, all seven sigma labels are allowed.
                    for sigma in range(7):
                        factor = F(1, 49**p.k) if sigma else factor_zero
                        if good:
                            result[rank_factor * factor] += vorbits * good
                        if bad:
                            result[rank_factor * factor / 49] += vorbits * bad
    return dict(result)


def moment(spectrum, exponent):
    return sum((value**exponent * count for value, count in spectrum.items()), F(0))


def d_k(k, exponent):
    return (
        (1 + 42 * F(1, 49 ** (k * exponent))) * (49**k - 17**k)
        + 6
        * (
            (1 + 48 * F(1, 9**exponent)) ** k
            - (1 + 16 * F(1, 9**exponent)) ** k
        )
    )


def difference_formula(h, exponent):
    spread = Parameters(h, "spread")
    aligned = Parameters(h, "aligned")
    return (
        F(spread.nparams - 3, 7)
        * (aligned.compatible - spread.compatible)
        * spread.r**exponent
        * (1 - F(1, 49**exponent))
        * d_k(spread.k, exponent)
    )


def transfer_measure(h):
    p = Parameters(h, "spread")
    aligned = Parameters(h, "aligned")
    transfers = defaultdict(int)
    size = quotient7((p.nparams - 3) * (aligned.compatible - p.compatible))
    for j in range(p.k + 1):
        copies = comb(p.k, j) * 16**j * (3**j - 1) * size
        for factor, count in [(F(1), 1), (F(1, 9**j), 6), (F(1, 49**p.k), 42)]:
            transfers[p.r * factor] += copies * count
            transfers[p.r * factor / 49] -= copies * count
    return {value: count for value, count in transfers.items() if count}


def top_density(p):
    n, w = p.nparams, p.wsize
    return F(3 * w + (n - 3) * p.compatible + 6 * n, 49 * n * w)


def quadratic_filter(x):
    return (49 * x**2 - x) / 48


def quadratic_residual_bound(p, sharpen=False):
    j_moment = (
        (1 + F(48, 81)) ** p.k - (1 + F(16, 81)) ** p.k
    ) / (49**p.k - 17**p.k)
    rho_term = F(6, 49) * (1 + F(6, p.wsize)) * j_moment
    sigma_term = F(6, 7) * (1 - F(1, p.wsize)) * F(1, 49 ** (2 * p.k))
    if sharpen:
        # |q(x)| <= (5/54)x for x<=1/9; <=x/48 for x<=1/49.
        rho_term *= F(25, 2916)
        sigma_term /= 2304
    return rho_term + sigma_term


def quadratic_energy(p, spectrum):
    low = {x / p.r: count for x, count in spectrum.items() if x <= p.r}
    energy = sum(
        (quadratic_filter(x) ** 2 * count for x, count in low.items()), F(0)
    ) / p.low_dimension
    from_moments = (
        2401 * moment(low, 4) - 98 * moment(low, 3) + moment(low, 2)
    ) / (2304 * p.low_dimension)
    assert energy == from_moments
    a = top_density(p)
    assert a <= energy <= a + quadratic_residual_bound(p, sharpen=True)
    assert energy <= a + quadratic_residual_bound(p)
    assert max(abs(quadratic_filter(x)) for x in low) == 1
    assert max(abs(quadratic_filter(x)) for x in low if x < 1) == F(5, 486)
    return energy


def check_one(p):
    spectrum = spectrum_table(p)
    assert all(count > 0 and isinstance(count, int) for count in spectrum.values())
    assert all(0 < eigenvalue <= 1 for eigenvalue in spectrum)
    assert sum(spectrum.values()) == p.dimension
    a0, _, a1, _ = scalar_multiplicities(p)
    rank_p = (p.nparams + a0) * (17**p.k + 6)
    assert spectrum[F(1)] == rank_p
    assert max(x for x in spectrum if x < 1) == F(1, 9)

    # The high and low clusters are disjoint, including every zero/radical case.
    assert p.r < F(1, 49 ** (p.k + 1))
    low = {x: count for x, count in spectrum.items() if x <= p.r}
    high = {x: count for x, count in spectrum.items() if x > p.r}
    assert min(high) >= F(1, 49 ** (p.k + 1))
    assert sum(low.values()) == p.low_dimension
    assert low[p.r] == (49**p.k - 17**p.k) * (p.nparams + a1)
    assert F(low[p.r], p.low_dimension) == top_density(p)
    assert max(x / p.r for x in low if x < p.r) == F(1, 9)

    # Energy of T^h on an isotropic unit input in the full canonical low space.
    energy = moment(low, 2 * p.h) / p.r ** (2 * p.h) / p.low_dimension
    a = top_density(p)
    assert a <= energy <= a + (1 - a) * F(1, 9 ** (2 * p.h))
    quadratic_energy(p, spectrum)
    return spectrum, rank_p, energy


def main():
    plane_orbits()
    records = []
    for h in range(1, 5):
        ps, pa = Parameters(h, "spread"), Parameters(h, "aligned")
        ss, rank_ps, energy_s = check_one(ps)
        sa, rank_pa, energy_a = check_one(pa)
        assert rank_ps == rank_pa
        if h == 1:
            assert spectrum_from_labels(ps) == ss
            assert spectrum_from_labels(pa) == sa
        observed = {
            x: sa.get(x, 0) - ss.get(x, 0)
            for x in sa.keys() | ss.keys()
            if sa.get(x, 0) != ss.get(x, 0)
        }
        assert observed == transfer_measure(h)
        assert sum(observed.values()) == 0
        for exponent in (1, 2, 3, 4):
            difference = moment(sa, exponent) - moment(ss, exponent)
            assert difference == difference_formula(h, exponent) > 0
            # Subtracting the identical intrinsic projection P preserves it.
            assert (moment(sa, exponent) - rank_pa) - (
                moment(ss, exponent) - rank_ps
            ) == difference
        assert moment(sa, 0) == moment(ss, 0) == ps.dimension
        assert energy_s < energy_a
        quadratic_s, quadratic_a = quadratic_energy(ps, ss), quadratic_energy(pa, sa)
        assert quadratic_s < quadratic_a
        records.append(
            {
                "h": h,
                "k": ps.k,
                "dimension": str(ps.dimension),
                "distinct_eigenvalues": len(ss),
                "rank_P": str(rank_ps),
                "low_dimension": str(ps.low_dimension),
                "trace_difference": str(difference_formula(h, 1)),
                "energy_ratio_squared": str(energy_s / energy_a),
                "quadratic_energy_ratio_squared": str(quadratic_s / quadratic_a),
            }
        )
        print(
            f"h={h}, k={ps.k}: dimensions, fixed space, exact transfer, "
            "moments 1/2/3/4, cutoff, power and quadratic-filter bounds PASS"
        )

    # A finite illustration of ratio^2 ~ 729 * 9^(-h), not a proof of the limit.
    ps, pa = Parameters(8, "spread"), Parameters(8, "aligned")
    ss, _, energy_s = check_one(ps)
    sa, _, energy_a = check_one(pa)
    relative = energy_s / energy_a / (729 * F(1, 9**8))
    assert abs(relative - 1) < F(1, 1000)
    ratio_quadratic = quadratic_energy(ps, ss) / quadratic_energy(pa, sa)
    relative_quadratic = ratio_quadratic / (729 * F(1, 9**8))
    assert abs(relative_quadratic - 1) < F(1, 1000)
    print("h=8 power and quadratic ratios: relative squared errors < 1/1000 PASS")
    digest = sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()
    print(f"Exact rational record digest: {digest}")
    print("No full loop table or floating-point spectral calculation was used.")


if __name__ == "__main__":
    main()

