# Quantum randomization from reciprocal Bol operations

Mira Cult

## Local labels and status

This record indexes the [complete theorem-and-proof manuscript](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md)
using its theorem labels and QR equations. These are **manuscript-local labels,
not permanent numeric claim IDs**. No number is allocated or reserved, and
the numbered claim crosswalk is unchanged.

The scientific source is `f6f415a5b05ce38b51adc9d2894c9795af500b3e`.
It contains conventional written proofs and exact finite corroborating
programs. Two noncontributing model reviewers accepted its mathematical and
resource/comparison claims at this exact revision, with no remaining blocker
within their stated remits. The reports retain the initial audits and the
separate exact-revision acceptance addenda. This is not external human review,
formal verification or a literature-wide novelty audit.
See the [reproducibility and review record](../analytic-2026-11-16/evidence/bol-randomization-reproducibility.md).

## Statements and boundaries

| Local label | Statement and public proof location | Scope or limitation |
| --- | --- | --- |
| Recovered NI theorem | [Channel, basis and measures](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#1-the-channel-basis-and-sampling-law) | The exact dense global Hilbert--Schmidt rate and coherence upper bound require a nondegenerate sector. The separate spread/aligned joint-trace comparison does not imply that mixing theorem in its degenerate scalar sectors. |
| Lemma R; Theorem QD | [Operational tasks and dense fixed-family bound](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#2-operational-tasks-and-unavoidable-costs) | State rank and Choi rank give different key lower bounds. The fixed-family dense depolarizing component gives a dimension-independent diamond upper bound with fresh samples, not an exact diamond rate. |
| Theorems D/A/C | [Native obstructions](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#3-native-normal-form-and-distribution-independent-obstructions) | Every degenerate sector has a universal stationary state. In the fixed F729 family, at most 2n native generators leave a nontrivial common fixed algebra; an explicit list of 2n+1 has scalar common commutant. No quantitative gap at the threshold is claimed. |
| Theorems W/S; Lemma B | [One-call reachability and explicit sampler](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#5-one-call-weyl-reachability-and-an-explicit-sparse-randomizer) | In the stated $`d=49\cdot3^N`$ family and for $`0<\varepsilon\leq1`$, one actual translated defect gives arbitrary-state trace error at most $`\varepsilon`$ with $`M\leq\min(d^2,3969d/\varepsilon^2)`$ keys. Fixed-qudit quantum depth is constant, gate count is linear in register size and no quantum ancilla is needed. Deterministic preprocessing/key mapping and expected fair-bit sampling costs are charged, with a bounded-time truncation option. A matching Weyl control reproduces the complete channel. |
| Theorems F/P | [Fixed-pair two-round channel](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#6-holding-the-defect-pair-fixed-exact-two-round-mixing-and-purity) | Two independent uniform center averages depolarize exactly. Sparse averages have exact two-step Hilbert--Schmidt norms and a direct purity bound through two noncommutative subalgebras. One-step coherence norm is one. The same improvement holds for the complete correlated Weyl control. |
| Section 9.1; QR.33a | [Decoupling the fused conjugate sector](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#91-decoupling-the-fused-conjugate-sector) | Independent conjugate-sector sampling is an algebraic diagnostic, generally not a trace-preserving channel. For the fixed-pair representatives its output trace on states is $`1/d`$. The exhaustive ring-factor check is separate from the two-round correlation experiment. |
| Proposition M | [Ablations and higher moments](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#9-ablations-and-higher-moments) | Every unaugmented monomial ensemble in dimension greater than one has second-moment induced Hilbert--Schmidt distance exactly one from Haar. First-moment randomization does not establish a unitary 2-design. |

The manuscript distinguishes worst-case state trace error, Hilbert--Schmidt
contraction/purity and diamond error against a reference. It states the logical
encoding, operation set, fair-bit sampling, preparation, gate count, depth,
precision and fresh-randomness requirements. Finite tests corroborate their
stated ranges; they are not proofs by enumeration of the enormous channels.
For fixed error below one, the one-call key entropy is within an additive
constant of the support lower bound for uniform-key or fixed-length-key
implementations. This is not a lower bound on every nonuniform key entropy,
and no optimal dependence on accuracy is claimed for all mixed-unitary randomizers.

## Dependencies and remaining scope

The accessible proof dependencies are the [non-scalar intertwiners manuscript](../analytic-2026-11-16/manuscripts/bol-nonscalar-intertwiners.md)
and [associator-quantization manuscript](../analytic-2026-11-16/manuscripts/bol-associator-quantization.md).
The [matched comparisons](../analytic-2026-11-16/manuscripts/bol-quantum-randomization.md#8-benchmarks-in-matched-criteria)
include exact Weyl randomization, phase randomization with classical mixing,
explicit quantum expanders and approximate quantum encryption.

No general resource advantage over the strongest applicable standard randomizers
is established. The structural contribution is the actual native obstruction
and sharp commutant threshold, reachability, the dense depolarizing component
and the fixed-pair purity estimate. The [remaining targets](../OPEN_PROBLEMS.md#quantum-randomization-with-actual-reciprocal-defects)
are sparse approximation of the original two-rate law, higher-conductor
reachability and a task with a strict benefit from loop structure. None of
these statements classifies finite simple Bol loops.
