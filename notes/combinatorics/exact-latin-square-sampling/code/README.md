# Exact labeled Latin-square sampler

**Scope of this code.** This is the exact finite reference implementation accompanying the earlier proposal. The revised [paper](../paper/README.md) uses a different terminal construction and multiscale correction; the command-line program here does not implement the revised $\widetilde O(n^{25})$ algorithm end to end, and its tests do not validate that runtime.

**For a sample:** use Python 3.10 or newer. No installation, network access, or dependencies are required. From this directory:

```sh
python latin_sampler.py 7
python latin_sampler.py 5 --samples 10 --one-based
python latin_sampler.py 4 --method huber
python latin_sampler.py 7 --counts
python -m unittest discover -v
```

Each sample is one JSON array of rows on one line. Rows, columns and symbols are labeled: this is not a sampler on isomorphism classes or just on reduced squares. Symbols start at 0 unless `--one-based` is passed. Independent fair bits imply mathematically exact uniformity; the program defaults to the operating system random source. Set `--seed 353` only for reproducible tests and benchmarks: a fixed seed is not a uniform draw. A null proposal is retried; no deadline, conditioning on finishing first, floating-point probabilities or uncorrected mixing cutoff is used.

## Which mode?

| Mode | Implementation | Use |
|---|---|---|
| `auto` | `reduced` at orders 1–7, `rejection` afterward | Default |
| `reduced` | Memoized completion counts and bijective integer unranking | Small orders, exact counts, repeated draws |
| `rejection` | Row-by-row matching proposal with integer permanent upper envelopes | Simple finite exact sampler, no Latin-square completion counts |
| `decorated` | All three research proposal families; exact sigmoid + safe-scale split inverse | Exercise the joint research proposal efficiently at small orders |
| `huber` | Same three families; exact sigmoid + genuine Huber reciprocal factory | End-to-end theorem-style control flow at a conservative, explicitly proved scale |

**Scope.** Every CLI sampling mode is exact under independent fair bits. None of the shipped modes has the paper's proved polynomial expected *total* bit cost. The uniform perfect-matching backend uses exponential subset DP. The reference scale is a computable upper envelope; its ratio to the Latin count is not proved polynomial. Do not use large orders without assessing available memory and time: a single order-`n` subset table has `2**n` entries, reduced completion caches can also grow extremely rapidly, and rejection may take many trials. The finite and asymptotic claims are different.

## APIs and why they are exact

```python
from exact_core import ReducedSpace, sample_latin, is_latin
from decorated import Parameters, forward_path, reverse_path, safe_huber_trial

square = sample_latin(5)                    # tuple of tuple, 0-based
assert is_latin(square)
space = ReducedSpace(7)                     # reusable completion memo
assert space.labeled_count == 61479419904000
first = space.unrank(0)
second = space.sample()
proposal = forward_path(Parameters(4))      # includes veto/null; NOT a uniform sample
nonnull_or_none = safe_huber_trial(Parameters(4))
```

1. **Unranking.** Fix the first row and first column to the identity. A completion-DP state is the symbol availability mask at each column. A possible next row is a perfect matching with the next prescribed value at column zero. Its subtree size gives its integer interval; these disjoint intervals exhaust the parent's interval. Sorting the other column masks merges equal *count* queries only. The labeled chart multiplies each reduced square by exactly `n! (n-1)!`: arbitrarily relabel symbols, then permute the rows fixing row zero. The output's first row and column recover both label choices uniquely. One uniform rank among all labeled ranks is sufficient.
2. **Row rejection.** At degree `d`, the permanent `p` is the number of permitted rows. Pass a `p/U_d` coin and then choose one of the `p` rows uniformly. Here `U_d` is the integer floor of the Brégman bound `(d!)^(n/d)`, tightened when the permanent or a cycle bound is available. Every particular square has one-trial probability exactly `1/H`, with `H=product(U_d)`; independent complete retries give uniformity.
3. **Decorated proposal.** Choose with equal prior one of (a) a random colored polygon and ordinary residual rows, (b) the short-word four-cycle predictor, or (c) a polygon and repeated matching-first `b`-blocks with future-edge reservation. Physical row labels are uniformly shuffled. An empty small-order range is handled conservatively: `max_b=min(n,max(2,floor(n^(1/200))))`, and only whole blocks fitting after the head are used. `T` is the ratio of reverse probability on a target's decoration to the forward subprobability of that decorated target; multiplying `T/(H+T)` on each accepted path gives `g(S)/H` for a particular square S, where `g(S)=E_reverse[H/(H+T)]`. This is *not* uniform by itself.
4. **Safe inverse.** With probability exactly `1/6` the generic family is selected and its length coin first stops at one, forcing the ordinary matching path. Here pointwise `T<=H`, so the reverse sigmoid is at least `1/2`. Subtracting `1/2` only on this tagged event realizes an exact `g(S)-c` coin for `c=1/12`. A two-coin race with a constant `c` coin returns one with probability `c/g(S)`. The complete `decorated` trial emits every square with probability `1/(12H)`.
5. **Huber inverse.** `huber` also uses the certified bound `g(S)>=γ=1/12`. A two-coin race gives `q=(γ/4)/(g+γ/4)<=1/5`; Huber's constant-gap factory doubles this bias, and a geometric number of independent doubled coins realizes `(γ/4)/g`. This trial emits every square with probability `1/(48H)`. It draws a fresh branch, order and all marks for *every* reverse coin.

`certified_trial(params,H,gamma,...)` is a low-level interface with a mathematical precondition: **the supplied constants must satisfy `0<gamma<=min_S g_H(S)`**. Do not infer this from sampled paths or tune it empirically. It is not exposed on the CLI. The optional `oracle_gate=True` selects the permanent-free sigmoid race in `selector.py`; passing `matching_fn(board,rng)` allows an exact matching backend on arbitrary feasible compact bipartite boards/minors (including empty). The default exact backend is not GLMP. See `DECORATED-BLOCKS.md` for data formats, marks and local identities.

## Verification and indicative times

The tests compare every 0/1 board through order 3 against explicit permutations, compare labeled unranking exhaustively through order 4, verify reduced counts 1, 1, 1, 4, 56, 9408, 16942080 through order 7, and check exact local marked-history weights. At orders 3 and 4, an independent rational calculation sums every labeled target, row schedule and latent matching for a nontrivial `max_half=2,max_b=2` decorated profile and verifies the constant final masses above (12 and 576 labeled squares). These are finite consistency tests, not a proof of the asymptotic runtime. They avoid relying on frequency histograms.

Illustrative single-process Python wall times in the development container, seed 353, including validity checks; reduced-space construction and caching are included once per batch. Hardware and random path affect these numbers.

| Order / draws | Reduced | Rejection | Decorated | Huber |
|---|---:|---:|---:|---:|
| 3 / 10 | <0.001 s | <0.001 s | 0.027 s | 0.93 s |
| 4 / 10 | <0.001 s | <0.001 s | 0.017 s | 1.30 s |
| 6 / 10 | 0.006 s | 0.002 s | 0.21 s | not timed |
| 7 / 10 | 0.44 s | 0.025 s | 0.47 s | not timed |
| 8 / 3 | not timed | 0.17 s | 1.23 s | not timed |

**For a polynomial executable**, the missing engineering pieces are a validated exact expected-polynomial matching backend on arbitrary required minors, and an implemented, audited large-order calibration/admission routine providing `H,γ` and an effective finite-exception cutoff. The paper explains these ingredients. The CLI intentionally uses safe substitutes instead of declaring unverified constants or an oracle to be implementations.

**Optional matching backend.** The separate `glmp_prototype/` directory now contains the rational GLMP matching kernel, finite-law correction, compact admitted parameter schedule and a `matching_backend` callback for arbitrary feasible minors. It passes small-model exact tests and its conservative clock was checked internally against `../pm-bit-clock.md`; that astronomical branch is not a practical or externally verified implementation. The CLI still uses the subset-DP matching backend. With this optional callback the remaining missing component of a standalone expected-polynomial **Latin** executable is the calibrated `H,γ` and its admission/startup implementation. Example wiring (with both directories on the Python path): `certified_trial(params,H,gamma,rng,matching_fn=matching_backend,oracle_gate=True)`.
