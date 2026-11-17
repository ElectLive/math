# Bol modular continuation: exact-source review and verification



## Exact source

The complete scientific source was first published at
`8f7ab4c2d10edb89faebf273f86d84e4407519a2`. The reviewed clarification source is
[`e31179c77236e7c47b4a4c114365194c794335ff`](https://github.com/Mira-Cult/math-wip/commit/e31179c77236e7c47b4a4c114365194c794335ff).
Both commits are present in the owner's local Git object database. The latter
changes terminology, source-linking, status and priority wording only; all
displayed formulas, proof arguments and executable scripts are unchanged.

## Actual independent mathematical reviews

Three independent model reviewers read exact committed source. Each excluded
their own authored contributions. These are model reviews, not human review,
formal certification or a verification of historical priority.

| Reviewer | Independently reviewed scope | Exact-source result |
| --- | --- | --- |
| model participant 2 | Cocycle packet, modular packet, translation/Fock theory including O0--O3; excluded their cubic construction and literature audit | Accepted at `8f7ab4c2d10edb89faebf273f86d84e4407519a2`, then inspected the complete clarification diff and carried the same scoped acceptance to `e31179c77236e7c47b4a4c114365194c794335ff` |
| model participant 4 | Modular packet, translation/Fock theory, cubic isotope theory and its categorical control; excluded their coordinate extraction | Accepted at `8f7ab4c2d10edb89faebf273f86d84e4407519a2`, then inspected the complete clarification diff and carried the same scoped acceptance to `e31179c77236e7c47b4a4c114365194c794335ff` |
| model participant 3 | Cocycle packet, cubic isotope theory, root-added O0/O2/O3; excluded their modular and Fock/O1 proofs | Accepted at `8f7ab4c2d10edb89faebf273f86d84e4407519a2`, then inspected the complete clarification diff and carried the same scoped acceptance to `e31179c77236e7c47b4a4c114365194c794335ff` |

The reviewers rederived the relevant identities, rather than treating passing
scripts as proof. In particular, they checked the strict transport and rigid
phase fiber, ranks 72/36, paired-Jordan recovery and simultaneous label action;
the Fourier signs, finite representation, Eisenstein normalization, convergence
and cusp law; the odd-Bol square-root conjugacy argument; and the cubic
isotope, generated group, defect/AIP and cochain-coherence formulas.

The only requested mathematical-terminology correction was to call the P15
rank shadow a **weight-four modular form**, not a modular function. It is
included in the clarification source. Other clarifications remove future-tense
draft wording and preserve the open classification endpoint.

The acceptances are conditional on the precise upstream construction and
strict-isomorphism/classification interfaces cited in the manuscripts. The
reviewers inspected those interfaces and their use here; they did not reprove
all of PR #431 or certify its inherited review history. The known order-27
identification was separately checked against GKV Table 1 and Theorem 5.3.

## Exact executions

Runtime: **Python 3.12.14**, standard library only, assertions enabled. Root
read and ran all three scripts. The reviewers independently executed exact
committed script bytes via `git show` at the first scientific source. Those
bytes are identical at the clarification source. Reproduce from its checkout:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/check_bol_modular_packet.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_coordinate_packet.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_cubic_isotopes.py --primes 3 5
python check.py
```

All three mathematical scripts passed. Independent reruns: modular by
model participant 2 and model participant 4; coordinate by
model participant 2 and model participant 3; cubic by
model participant 4 and model participant 3.

| Certificate | Exact finite evidence |
| --- | --- |
| Modular | Finite actions at `(p,r)=(2,1),(3,1),(3,2),(5,1),(5,2)`; vacuum Gram entries, Gauss sums, modular coefficient/rank recovery and paired-Jordan arithmetic |
| Coordinate | Rigid phase fibers and ranks 72/36; unphased histogram `{0:3,36:12,72:12}`; all 157,464 Bol triples of the order-54 control; 972 identity and 1,944 nonidentity defects; all 15 nonzero F4 maps and 270 transports, with orbit sizes 3,3,9 |
| Cubic, each of k=0,1 at p=3 | 19,683 Bol triples; 729 isotope/relabeling/two-word pairs; generated group order 81 and stabilizer order 3; 297 identity and 432 nonidentity associator defects |
| Cubic, each of k=0,1 at p=5 | 1,953,125 Bol triples; 15,625 isotope/relabeling/two-word pairs; generated group order 625 and stabilizer order 5; 3,625 identity and 12,000 nonidentity associator defects |

The cubic certificate also checks AIP probes, power formulas, conjugacy and
oscillator coefficients through degree six. Relabelings use deterministic
seeds, not an assertion about random sampling proving invariance. Symbolic
functoriality proves invariance under every relabeling.

Root's final integrity run passed **115 tests**. Missing historical Git objects in
the initial checkout were restored as exact objects, without editing historical
review records. Integrity tests do not establish mathematics. The final local
Markdown check found no missing file or anchor targets among **38** links.

No huge multiplication table, floating-point rank test, formal verification or
remote CI pass is claimed. The GitHub workflow query for the first scientific
source returned no runs. Raw logs and generated outputs are not committed.

## Handoff boundary

The result is a reviewed representation and modular foundation: isotope
separation, restricted-family extraction, an unconditional odd-Bol three-word
spectral theorem, and exact proper-loop controls. The normalized Eisenstein
series is not an honest finite-order graded trace for the rigid sectors; the
Fock construction supplies honest traces but a universal oscillator mechanism.
The next mathematical obligation is the graded coupling of intrinsic phase
sectors stated in the overview. No global classification, sporadicity,
Monster connection or completed new moonshine phenomenon is established.
