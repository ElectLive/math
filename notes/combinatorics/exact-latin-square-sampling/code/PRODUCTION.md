# What remains to realize the theorem's runtime

The executable here tests the decorated proposal and correction as an exact
finite sampler. It is not a fast implementation of the asymptotic theorem.
Two interfaces separate those goals:

1. **Perfect matching backend.** For any feasible board, accept a row of
   integer bit masks and return a uniformly random perfect matching, using
   the supplied fair-bit RNG. A replacement needs to be **exact** on
   irregular boards and on minors, not simply close in total variation.
   The bundled subset-DP implementation meets the distribution contract,
   but its cost is exponential. The proof uses Göbel, Liu, Manurangsi and
   Pappik, Theorem 2, on unweighted bipartite graphs. An implementation
   of their route requires rational cooling of the Jerrum–Sinclair–Vigoda
   chain, an exactly reproducible capped approximate sampler, and the
   rare exact probability correction. Replacing the subset DP with the
   approximate phase alone would break exactness. A feasibility query can
   be answered by augmenting paths; it need not count matchings.
2. **Theorem-scale parameters.** The default uses an elementary safe row
   envelope and a lower bound visible to the code. These work at all
   orders, but do not force polynomial acceptance. The experimental
   low-level certified-trial entry point accepts a rational threshold and
   a certified lower bound on the reverse acceptance probability. The
   proof uses a logarithmic safety margin and a fixed-order coefficient
   computation. An end-to-end polynomial implementation needs to ship
   a quantified margin and startup cutoff, and the corresponding
   parameter compiler; an empirical acceptance estimate is not a
   substitute for that certificate.

For a production backend, add exact matching-distribution and conditional
minor tests independent of the Latin-square sampler, then rerun the
decorated-history exact tests. Instrument all rejected attempts, adaptive
calibration, RNG bits, arithmetic widths, and fallback costs. Do not claim
an observed timing curve proves an asymptotic upper bound. Run large-order
benchmarks only after those finite-law checks pass.

**Optional research backend:** `glmp_prototype/glmp_pm.py` implements the rational, explicitly admitted conservative form of step 1 as an optional research callback. Its finite test-clock laws and rare correction were tested separately; its huge numeric clock is for the asymptotic proof, not practical benchmarks. See its README and `../pm-bit-clock.md`. The default CLI backend has not changed, and item 2 remains open as engineering work.
