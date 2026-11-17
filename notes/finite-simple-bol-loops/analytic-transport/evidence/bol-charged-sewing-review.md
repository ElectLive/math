# Charged sewing: exact-source review and mathematical boundary



## Exact scientific source

- Scientific commit: `197d13d4ac2e48763ed20bf418228d7b4d16aa8c`.
- Scientific tree: `73bbb288ddcae52dcd83c3d3ab40c2936eed02b5`.
- Recoverable preliminary milestone:
  `49ef05e757e63849b1fd6ede1a052f47196025ca`.

The full scientific commit is published on the owned branch and exists as
an exact Git object locally. It contains all five complete manuscripts,
both executable certificates, their deterministic JSON and calculation
notes, and the overview/reference updates. A later delivery commit adds
this review and updates status only. It does not change the reviewed
manuscripts, executables or JSON.

The earlier [Fourier-sewing review](bol-analytic-rigidity-review.md),
[genus-one review](bol-genus-one-review.md),
[graded review](bol-graded-review.md) and
[initial review](bol-modular-review.md) retain their own exact sources
and scopes. Acceptance here is not a re-review of the inherited huge-loop
construction, simplicity, properness or strict-isomorphism interface.

## Actual independent review

These reviewers are model agents in this research session. Their verdicts
are mathematical model reviews, not human acceptance, formal certification,
or GitHub approval by a maintainer.

| Reviewer | Exact source | Independent scope | Verdict |
| --- | --- | --- | --- |
| model participant 1 | `197d13d4ac2e48763ed20bf418228d7b4d16aa8c` | Complete GS1--GS6, CH1--CH6, CE1--CE7, FN1--FN4, LC1--LC3; both complete scripts and certificates; overview and source qualifications | Accepted within the stated hypotheses and nonclaims; no unresolved defect found |
| model participant 2 | `197d13d4ac2e48763ed20bf418228d7b4d16aa8c` | Complete new CE1--CE7, FN1--FN4 and LC1--LC3 arguments; charged-script reproducibility | Accepted; no correction required in this independent scope |

Both reviewers inspected exact `git show` source bytes. The fresh reviewer
contributed no mathematical construction or proof and covered all five
new manuscripts. The literature reviewer excluded its own GS authorship;
inspection of CH interfaces and execution of the CH certificate are not
recorded as independent acceptance of all CH proofs. That reviewer also
authored the earlier proper cubic family, so its LC3 acceptance concerns
the new associative-quotient argument, not re-certification of the inherited
proper-Bol theorem.

### What the independent reviews checked

The full review checked finite Berezin signs and complementary minors,
singular-channel saturation, the bordered determinant's anomaly cancellation,
its eta factor and modular multiplier, and the conditional trace-class
limit. The continuum result requires its stated bounded source maps and
trace-class hypotheses; it is not unrestricted geometric sewing.

For the charged geometry, the review checked the actual monomial
representation, noncommuting matrix-coordinate fusion-tree change, full
dual zero algebra, automorphy and curvature signs, tensor-degree carry,
line-valued fusion maps and true-dual distinction. It checked the exact
rigid determinant/adjugate argument and the limited graph-only cocycle
erasure statement.

Both independent exchange reviews rederived the two-index and three-index
coefficients of the dynamical Yang--Baxter equation, the residual
total-weight term in the position commutator, the modular gauge's
quadratic cancellation and its composition law. They checked the
homogeneous-residue obstruction, uniform-shift spectator factorization,
separate-Cartan Fourier theorem and restricted Weyl genus bound.

The naturality reviews checked identification of natural currents with
group-algebra elements, absence of primitive elements, the degree-extension
scalar argument and the formal unipotent recursion. The local-current
reviews checked four-index Jacobi, the two-sided associator ideal, the
universal group quotient and the explicit cubic witness.

Primary Felder, Tuite--Zuevsky and Keller locators and the limited arithmetic
benchmark attributions were checked in the recorded scopes. Standard
Felder flatness, Gaussian sewing and theta identities are not claimed as
new Bol-specific mechanisms or as literature-priority results.

### Review correction resolved before the scientific pin

The fresh reviewer found that the initial GS2 phrase "quadratic
exponentials" was broader than its determinant proof. Quadratic terms
joining two unbarred or two barred variables generally require Pfaffians.
The author explicitly restricted GS2 propagators and channel identifications
to the incoming/outgoing type of GS1, retained arbitrary finite polynomial
insertions, and made GS4, GS5 and the calculation note consistent. The
fresh reviewer inspected and accepted this correction at the exact
scientific pin. No executable or JSON change was needed.

### Authorship exclusions

- model participant 2 authored GS and its script/certificate.
  Its author corrections and execution of that work are not independent review.
- model participant 4 authored CH and the charged script/certificate,
  and contributed the finite charged/zero-channel interfaces used in CE.
- model participant 3 authored CE and contributed to the CH analytic
  and degree interface. Its checks of those results are participant checks.
- model participant 5 authored FN and LC, contributed the exact CE6 Fourier-separability
  strengthening and CE7 target, and contributed the CH degree/duality and
  architecture boundary. Root's proof checks are not independent acceptance.
- model participant 1 performed the fresh read-only mathematical
  review and independent executions, with no research-construction authorship.

## Exact reproducibility

The detailed scopes are in the
[charged calculation record](bol-charged-sewing-certificate.md) and
[Gaussian calculation record](bol-gaussian-sewing-certificate.md), with
their linked complete JSON. From the repository root, with assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_charged_sewing.py --certificate /tmp/bol-charged-recheck.json
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_gaussian_sewing.py
python check.py
```

All recorded runs used Python 3.12.14. Both scripts use only the standard
library and exact arithmetic. The author and root ran each script
successfully. The fresh reviewer independently extracted and ran both
scripts at the scientific commit: each exited zero, with empty stderr,
PASS, and complete output byte-identical to its pinned JSON. The literature
reviewer independently extracted and reran the charged script with the
same result. Root also obtained byte-identical JSON for both.

| Scientific artifact | SHA-256 |
| --- | --- |
| `bol-charged-gaussian-sewing.md` | `257139d98b639af00c8b827d3ac2b467c3a631d7b43208e760c162f9873d790f` |
| `bol-charged-heisenberg-obstruction.md` | `b66260fc437f86b850ebee56823416e0ea087a3d3f4b4e7840e67013fc21c2eb` |
| `bol-charged-exchange.md` | `eaa3627de23b6364c059e80a8364cf207048c1cb08566ab97ff3b0c21715994b` |
| `bol-fusion-naturality-obstruction.md` | `9834bacddf7b2bf79ca4bee4f0f7cd9e3d7a982b3d256349f044ea08ae601b3a` |
| `bol-local-current-obstruction.md` | `903fa89740065947657f8521feb24b7a94bfee5b3cd4ff3f3ba7efbf3aa07ef8` |
| `verify_bol_charged_sewing.py` | `a5c3f12f0d348b83c7fd27b56d4b2807bfc3b2f8e401536afa1427cde1010630` |
| `verify_bol_gaussian_sewing.py` | `363bc9ccc60635259f44c516b14d8c3208e2cf8b81e5006c0f1f4bb01ef9935d` |
| `bol-charged-sewing-certificate.json` | `0a0d049efe26fde4f298d0386a5ce7e5ab992f193267a0f13e1a2b9c2d2dfe5d` |
| `bol-gaussian-sewing-certificate.json` | `c0ca712dbe522e0b05e66eebd7d893204cc5607bd287f3fc4c1c5525cb640d7d` |

The charged certificate checks 6,561 monomial representation equations,
34,992 fusion equations across 72 regular-sum charge pairs, and 1,344
fusion-tree/inverse equations across 336 triples. It checks all 729 carry
pairs and 19,683 carry triples in its 27-charge model, 24 automorphy sign
equations, the polynomial rigid determinant and all sixteen adjugate
entries, 729 graph gauge phases and 2,187 charge-junction phases. For each
cubic parameter k=0,1 it generates the associative congruence from all
19,683 triples, checks 4,374 left/right contexts, and obtains precisely
nine central fibers.

The Gaussian certificate checks four invertible source formulas, four
diagonal singular cases and one nondiagonal singular case, three orders
of contraction including a singular intermediate block, an exact Schur
complement, seventeen bordered-determinant identities and the independent
quartic diagnostic. It does not numerically certify the continuum limit.

These are finite validation instances. The universal statements are proved
in the manuscripts, and the huge loop, its induced set and the field
extension are not enumerated. Temporary numerical theta checks by an
independent reviewer served only as sign diagnostics; no floating-point
calculation is the basis of the theorem or the exact certificates.

## Integrity, remote status and delivery

Root's integrity run passed all 115 tests at the scientific-source working
tree. A local navigation check verified 81 relative file links in the
affected sources and calculation notes. These are metadata/navigation
checks, not mathematical proofs.

The delivery working tree also passed all 115 integrity tests and a
90-target relative-file-link check. All five reviewed manuscripts, both
scripts and both JSON certificates were compared directly with the
scientific commit and are byte-identical.

GitHub reported one workflow at the scientific source:
[run 43789540224](https://github.com/Mira-Cult/math-wip/actions/runs/43789540224),
completed with conclusion **skipped**. Its combined commit status was
pending with zero individual statuses. No remote CI pass or satisfaction
of a maintainer's integration gate is claimed.

## Mathematical endpoint and next obligation

The positive construction supplies actual charged finite intertwiners and
a coherent holomorphic degree/carry repair, including all true dual and
zero-charge channels. The Gaussian baseline handles zero modes at separated
points and singular finite sewings. A standard dynamical elliptic system
has a direct position-flatness proof and an explicit modular gauge law on
each chosen matrix zero block.

The missing step is substantial: the constant charged intertwiners do not
transport separate dynamical Cartan parameter spaces, and full ordinary
tensor naturality permits only scalar degree exchange. The graph-only
construction also erases the coboundary shifts relating the rigid examples.
Those are precise obstructions to the stated architectures, not a general
no-go theorem for Bol moonshine.

The next obligation is to construct parameter-dependent charged
intertwiners compatible with a specified dynamical connection, obeying
coherence through the full zero and carry channels and retaining fixed
positive-cocycle markings. A successful theorem must then extract a
noncoincident relation not already supplied by the finite tensors,
Gaussian identities or the standard Felder system. No such new
Bol-specific analytic relation, new simplicity restriction, modular
isotope separator from this exchange system, tau-direction heat equation,
interacting graded vertex object or arithmetic moonshine consequence has
been established here.
