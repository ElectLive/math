# Marked charged transport and analytic reconstruction

**Mira Cult**

Can a finite Bol construction produce useful analytic observables beyond its individual spectra? This work gives a bounded positive answer: retaining specified split, inversion and boundary markings produces separated-point transport measurements that recover a central cocycle stably. A separate mixed-heat observable reconstructs full marked boundary matrices. These observables are determined by complete marked finite matrices; they are not independent information beyond all finite tensors.

## Results

The following are complete written research results, with the stated source qualifications and independent automated-model review. They do not classify finite simple Bol loops or establish an arithmetic moonshine correspondence.

### Charged transport with a finite dynamical base

The [collective transport construction](manuscripts/bol-collective-charged-transport.md), using the [finite dynamical twist](manuscripts/bol-dynamical-fusion-construction.md), retains every charge, actual multiplicity space, product-reached zero sector, integer degree, carry line and true dual. It proves a full shifted coefficient-intertwining equation, normally convergent analytic propagators and shifted coherence. Its modulus operator is a Chern connection with a marked modular law on Gamma(2p).

The tensor rule is **collective**: a group element acts on all factors simultaneously. It is not the ordinary primitive tensor connection. The dynamical base is finite; fixed-parameter geometric holonomies and finite-base difference transport are distinct. This is not a continuous-Cartan Felder fusion theorem or a heat connection.

### Stable cocycle recovery and a separated-transport gap

The [analytic recovery theorem](manuscripts/bol-shifted-analytic-fusion.md) considers finite-dimensional norm-at-most-one operators A and B and the transport

```math
\frac{dU}{dt}=\left(\frac{uA}{t}+\frac{vB}{1-t}\right)U,
\qquad U(1/4;u,v)=I.
```

The endpoint is t=3/4, away from the singularities. With the specified charged operators and boundary markings, the two ordered mixed responses recover the retained central cocycle with inverse sup norm at most 3. The theorem gives finite-amplitude error bounds, not merely a formal derivative identity. At p=3 and amplitude 0.01, measurement error at most 5×10⁻⁷ gives phase error below 0.087, or below 0.103 with the stated nonzero third-residue perturbation.

A separate proper-Bol cubic control has an ordered-transport gap greater than 9×10⁻⁶ despite equal individual spectra. Its associative and proper commuting controls have gap zero. This control is a separate ODE construction, not an unproved realization of every charged component on that group. Removing the split/reference marking has an explicit erasure control.

### Reconstruction from a separate mixed-heat observable

The [heat reconstruction theorem](manuscripts/bol-heat-sewing-repair.md) uses a marked Weyl pair, its true-dual kernel and the entire multiplicity space. Separated mixed-heat correlations recover arbitrary marked boundary operators, including the full matrix zero algebra, by a double-residue inverse. There are contour stability bounds, exponentially convergent finite-sampling estimates and an operator-level modular covariance law.

The boundary is fixed in its marked covering frame. It is not asserted to be a parallel morphism between arbitrary independent insertion fibers. This heat construction has **not** been joined to the collective difference construction by a heat-compatible fusion pentagon.

## Why the restrictions matter

The [finite dynamical rigidity](manuscripts/bol-finite-dynamical-rigidity.md), [separate-symbol obstruction](manuscripts/bol-fusion-symbol-obstruction.md), and [theta/heat analysis](manuscripts/bol-theta-fusion-connection.md) explain why several simpler architectures fail. Their hypotheses matter: they do not exclude arbitrary infinite-dimensional systems, other bases, higher-order intertwiners, fixed markings or global monodromy.

The earlier foundations are also included rather than hidden behind private references:

- [Fourier sewing](manuscripts/bol-fourier-sewing.md) and [holonomy rigidity](manuscripts/bol-holonomy-rigidity.md): a finite marked support relation lifts to a four-sector analytic identity; the analytic lift uses standard exterior factorization and modularity.
- [Charged modules and carry channels](manuscripts/bol-charged-heisenberg-obstruction.md), [Gaussian sewing](manuscripts/bol-charged-gaussian-sewing.md), and [charged exchange](manuscripts/bol-charged-exchange.md): complete channels, singular Gaussian baselines and the exact Felder compatibility boundary.
- [Ordinary tensor naturality](manuscripts/bol-fusion-naturality-obstruction.md) and [actual-product local currents](manuscripts/bol-local-current-obstruction.md): scoped obstructions, not universal impossibility theorems.
- [Cubic controls](manuscripts/bol-cubic-isotopes.md), [modular packets](manuscripts/bol-modular-packets.md), and [genus-one architecture](manuscripts/bol-genus-one-architecture.md): prior constructions and their exact marked/isotope assumptions.

The [local claim record](../claims/charged-analytic-transport.md) indexes these statements without allocating permanent numeric IDs. The [bibliography](REFERENCES.md) retains the exact external inputs.

## Open problems

1. Construct continuous-Cartan Felder charged fusion compatible with the required full zero and carry channels, rather than only the finite collective dynamical base.
2. Join the heat reconstruction family to the collective transport functor. First compute the mixed heat/difference principal symbols on the joint holonomy base; a heat-compatible fusion pentagon is not yet proved.
3. Identify a new marked response with the original Fock traces, or prove precisely what information is lost. Recovering the cocycle also recovers the prior marked norm probe, but this finite reconstruction bridge is not an equality of analytic objects.
4. Determine how much boundary/split/inversion marking can be discarded while retaining useful stable recovery. The existing erasure controls rule out simply forgetting all those markings.

No Monster action, genus-zero property, replicability, arithmetic moonshine consequence or unrestricted classification follows from the present results.

## Source, review and reproduction

This deliberate publication freezes delivery `ed6f9ed28225465f0491e5d6e39b2609c8da5d50` from research PR 438. The exact accepted latest scientific source is `625f6060200a6f165c33d98afe80b8091a1280e5`. The [review record](evidence/bol-dynamical-payoff-review.md) distinguishes one fresh noncontributing review of all seven current manuscripts and six executables from a second independent review of CT/SA only. The second reviewer contributed the heat work, so that work is excluded from its independent acceptance. Earlier checkpoints retain their own [charged-sewing](evidence/bol-charged-sewing-review.md) and [Fourier-sewing](evidence/bol-analytic-rigidity-review.md) review scopes.

Presentation adapts internal ownership labels, relative links and math delimiters. Executables and JSON certificates retain their source bytes. [MANIFEST.json](MANIFEST.json) maps original and public hashes; source-hash tables in review records refer to the original scientific bytes, not the presentation-adapted Markdown. See the [code guide](code/README.md) and [publication validation](PUBLICATION.md) for exact checks and remaining gaps. Model reviews are not human refereeing, formal verification, or novelty certification.
