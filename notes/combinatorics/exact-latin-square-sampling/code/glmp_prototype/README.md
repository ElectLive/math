# GLMP matching-backend prototype

This standalone Python module implements the finite, rational version of the matching construction in [Göbel–Liu–Manurangsi–Pappik, §6](https://arxiv.org/html/2410.00882v2#S6). Unlike a matching-count placeholder, it runs the adaptive sequence of Markov chains, computes the distribution of its finite procedure on the correction branch, and corrects it. It is a research prototype; **its tiny test clocks are not scalable mixing/admission constants**.

```sh
cd glmp_prototype
python -m unittest -v test_glmp_pm
python - <<'PY'
from fractions import Fraction
from glmp_pm import Clock, checked_sampler

# 3 columns; the last disallows symbol 0. There are four feasible permutations.
board = (0b111, 0b111, 0b110)
c = Clock(phase_samples=10, phase_steps=5, final_steps=8,
          attempts=2, bits=4, correction=Fraction(5,6))
draw = checked_sampler(board,c)
print(draw())
PY
```

* `attempt` includes null when one or more calibration bins are empty, a near-perfect state is drawn, or a forbidden final edge is used. *No* calibration run is secretly conditioned on successful observations.
* `approximate` caps independent attempts and returns an ordinary deterministically computed augmenting-path matching on failure. It has full probability mass, but is **not a uniform sampler**.
* `attempt_law` pushes exact dyadic distributions through the phase-weight/hole-histogram recursion, combining collisions and charging the other histograms to null. `approximate_law` uses the geometric sum for capped retries/fallback. Both compute probability laws on finite data, without enumerating every random bit trajectory.
* `correction_table` computes `h(x)=[1/#PM-(1-δ)Q(x)]/δ` from the actual finite returned distribution Q and from enumerating *real* perfect matchings. It checks nonnegativity rather than clipping. `checked_sampler` first checks this on the input board and caches the rare law before returning a callable.
* `sample_admitted(board,clock,rng)` does **not** compute the table on its cheap branch. Its documented precondition is a proved clock satisfying the pointwise upper bound. If such a certificate has not been supplied, use the finite checked version, not empirical tuning. The unconditional conservative choice `δ>=1-1/n!` (and positive δ) makes any otherwise valid clock safe by counting, but does not provide polynomial expected total time. To use it as a backend for `certified_trial`, supply a wrapper choosing clocks for the actual current board and all possible minors, including empty boards.

The kernel uses 4n proposal tokens: 2n hold, and 2n symmetric move tokens with multiplicity two for paths between a full and a near-full matching. Each step allocates b fair bits for the token and b separately for the rounded Metropolis acceptance, including on a self-loop. Calibration samples reset to a deterministic *real* perfect matching. A cooling phase changes forbidden edges at a single left vertex by a factor of 3/4, clipped at 1/n!; full matching-edge weights stay one. Each calibration counts all n² near-hole classes and the perfect class, then multiplies each old hole weight by perfect/hole hits. This is rational and time-bounded on every cheap attempt; the exact correction removes finite-rounding and finite-mixing errors rather than discarding them.

Tests directly enumerate the fair-bit transition laws and capped outcomes, verify detailed balance of the unrounded kernel, exercise positive and null annealing outcomes on a board with four target matchings, and verify the corrected probability of each is exactly 1/4. A bad small clock is rejected by the exhaustive precheck. These tests validate the executable finite laws, not asymptotic mixing constants.

## Conservative-clock prototype

`research_clock(board)` encodes the explicit integer proposal for the clocks in the accompanying `pm-bit-clock.md`. Treat numerical admission as its own proof obligation, not as something the small tests verify. In particular, `Clock(10,5,8,2,4,5/6)` above is only a small exact-law demonstration, not such a production clock. The conservative clock has a compressed `correction_exponent`; do not inspect its `correction` property on ordinary hardware since the exact denominator would be enormous. Sampling a rare-branch decision inspects at most two fair bits in expectation, without constructing that denominator.

On the ordinary path, highly precise rounded moves are implemented lazily. The token uses successive random-prefix bins until the entire possible interval gives the same move (or the precision is reached). For the accept coin, compare independent random bits to successive digits of a ratio of the two hole factors and only the changed edges; ties at the precision cutoff reject. The exact law is that of the finite padded kernel, and is checked by enumerating every short fair-bit string. Computing the law on the correction branch may allocate extremely large integers. The clock counts are intentionally far too expensive for practical runs; this is distinct from correctness or an asymptotic bit bound.

`matching_backend(board,rng=None)` is the callback with the shape needed by the decorated Latin trial. It uses finite enumeration through order seven (also for the empty board), and the conservative `research_clock` plus lazy GLMP/rare correction beyond that. The clock formulas and their numerical mixing/admission argument in `../../pm-bit-clock.md` were checked against this code internally. The large-order branch is deliberately impractical and has not been run at its astronomical clock, nor externally verified. Its internal bit bound is for *one perfect matching*, not for choosing the missing Latin-scale parameters. It is not the default of the fast example CLI.
