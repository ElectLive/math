# 0072. Odd and affine structural reductions

Mira Cult

## What is classified, and what remains open

This guide assembles the odd-order and affine proof families. The results replace several unrestricted searches with intrinsic algebraic data, exact admissibility tests and isomorphism relations. They do **not** classify every finite simple non-Moufang Bol loop. In particular, the general odd-envelope recursion is a candidate scheme, not an accepted structural exhaustion theorem. Exact-factorization constructions and sufficient splitting criteria must not be mistaken for necessity.

The principal additional classification recorded as [claim 0072](../claims/0072.md) is the coprime-metabelian-derived branch. The source family below also makes available the proofs behind class-two and Lazard branches, unbounded-complexity constructions, monolithic obstructions and affine regular-subgroup reductions. Each source states its own hypotheses; no union of these families is asserted to exhaust the unrestricted problem.

## 1. Coprime metabelian derived groups

Let a finite simple nonassociative odd left Bol loop have canonical envelope G with

```math
G'=M\rtimes T,\qquad M,T\ne1\text{ finite abelian},\qquad (|M|,|T|)=1,\qquad [T,M]=M.
```

The [complete theorem and proof](../sources/odd-completion/odd-coprime-metabelian-derived-classification.md) give construction, exhaustion, finite admissibility and simplicity tests, and complete loop-isomorphism data for this class. The abelian quotient A=G/G′ may share primes with M or T. The extension over the derived group need not split. Neither hypothesis is silently strengthened to the familiar split coprime-top situation.

### Structural reduction and proof mechanism

Coprime averaging gives M^T=0 and identifies M=G″ intrinsically. An actual inversion-stable Hall complement T can be selected; its normalizer L gives G=M⋊L with L′=T and L/T=A. This does not claim that L splits over T.

The stabilizer is encoded by W=H∩M, its projected subgroup J≤L and a crossed cocycle η:J→M/W. It is essential to retain both a displacement term and the residual cohomology class: conjugating H alone need not preserve the loop. The complete presentation uses a normalized extension cocycle for L, an involution θ on L, an L-action on M and its compatible involution σ, plus the actual graph data for H.

For each θ-inverted element l of L, put Q_l=ker(1+ρ(l)σ). The inverted set consists of the pairs (m,l) with m∈Q_l. An exact cardinality identity and the source's pairwise coset-intersection tests characterize transversality; they are not heuristic dimension counts. Generation follows from the odd solvable-envelope argument. Normal subgroups are explicitly parameterized by an invariant subgroup I≤M, a normal subgroup R of L acting trivially on M/I, and an equivariant homomorphism R→M/I. This gives finite corefreeness tests and the inversion-stable strict-defect test for simplicity.

Finally, the isomorphism relation includes compatible maps of M and L **and** a complement-displacement cocycle. Omitting that cocycle would incorrectly treat the chosen complement L as characteristic. These steps prove both directions: admissible data construct the intended loops, and every loop satisfying the stated derived-group hypotheses occurs.

### Precise limits

This is not the whole metabelian-derived case, a numerical census, a complexity bound or an unrestricted odd-loop classification. The theorem concerns nonassociative loops. Restricting to the non-Moufang subclass requires the stated finite identity test; nonassociative is not a synonym for non-Moufang. The proof retains the canonical-folder, full-inverted-set and strict-defect interfaces cited in the source.

## 2. Other complete scoped reductions

The class-two-derived theorem allows arbitrary odd exponent, while the central-center and coprime-center theorems identify narrower but more explicit branches. The Lazard and extraspecial results likewise retain their stated restrictions. Their coordinate descriptions must not be read as a short list of parameter orbits.

Elementary-layer and arbitrary-multiplicity results give exact recognition tests, full-shadow compression and monolithic reinsertion. They do not assert that every relevant layer is a quotient loop. The odd-envelope parameterization supplies a recursive search framework, not a proof that this framework is a satisfactory structural classification.

The affine results classify regular subgroups in specified families: the natural SL₂ root-graph family, its single-root and prime-transvection specializations, the stated SL₃ cocycle model, and solvable complements with cyclic prime quotient. They do not exhaust all affine or all even non-Bruck loops. The almost-simple radical bridge is conditional on the separately identified multiplication-group input, whose aggregate review status cannot be upgraded by this deduction.

## 3. Constructions and obstructions that constrain the goal

The families of unbounded derived nilpotency class, derived length and Fitting height rule out classification strategies that presuppose uniform bounds on those invariants. Noncentral Jordan-center examples and the rigid-center nongloop example show why central-center and universal G-loop assumptions cannot be imposed without proof. Isotope-orbit results belong to their specified canonical data, not to all odd loops.

Monolithic Heisenberg constructions, line and prime families, and higher-defect isomorphism criteria provide exact examples and conditional parameter mechanisms. The conditional prime-family Fourier-minor hypothesis is not proved for infinitely many primes; these results do not establish unbounded defect. Semilinear, prime-square, valuation-support and paired-diagonal exclusions eliminate specified models, not every monolithic possibility.

The stabilizer-splitting and paired-layer factorization arguments are sufficient criteria. Decorated-folder and factorization-presentation orbit correspondences describe presentations with witnesses; they do not prove that all simple loops possess such a witness. The inner-inversion reduction retains its radical-free hypothesis and the precise criterion on which it depends.

## 4. Complete mathematical source index

The linked files preserve the proof arguments, formulas, examples, negative scope boundaries and computational qualifications. This is a thematic dependency library, not 49 newly independent classification claims. Previously published claims remain in force with their original scopes.

- [Solvable p-prime affine complements with cyclic p quotient](../sources/odd-completion/affine-cyclic-prime-quotient-classification.md)
- [Selected marked involutions over an elementary two-layer](../sources/odd-completion/elementary-two-marked-lifts.md)
- [Witness orbits and exact-factorization presentations](../sources/odd-completion/factorization-presentations.md)
- [Natural SL₃ affine regular subgroups: cohomological data and center counterexample](../sources/odd-completion/nonbruck-affine-cocycle-data.md)
- [Candidate almost-simple / non-Bruck radical bridge](../sources/odd-completion/nonbruck-almost-simple-radical-bridge.md)
- [Prime-transvection orbit classification in natural affine modules](../sources/odd-completion/nonbruck-prime-transvection-orbits.md)
- [Root-graph parameters for an even affine family](../sources/odd-completion/nonbruck-root-graph-parameters.md)
- [Full single-root projection: center forcing and isomorphism data](../sources/odd-completion/nonbruck-single-root-classification.md)
- [Simple odd Bol loops from alternating-form tuples](../sources/odd-completion/odd-alternating-form-family.md)
- [Odd Bol loops with central class-two derived Sylow factors](../sources/odd-completion/odd-central-class-two-classification.md)
- [All odd simple Bol folders with class-two derived group](../sources/odd-completion/odd-class-two-classification.md)
- [Coprime center action on every class-two derived Sylow factor](../sources/odd-completion/odd-class-two-coprime-center-reduction.md)
- [Isotope orbits for odd class-two-derived folders](../sources/odd-completion/odd-class-two-isotope-orbits.md)
- [Composite-cyclic exact-factorization candidate](../sources/odd-completion/odd-composite-factors.md)
- [Odd simple Bol loops with coprime metabelian derived group](../sources/odd-completion/odd-coprime-metabelian-derived-classification.md)
- [A cross-coupled extraspecial candidate outside the exact-factorization route](../sources/odd-completion/odd-cross-extraspecial.md)
- [Directed-graph cross-extraspecial Bol loops](../sources/odd-completion/odd-cross-graph-family.md)
- [Exact elementary-layer lifting at arbitrary defect](../sources/odd-completion/odd-elementary-layer-all-defects.md)
- [Elementary normal layers in odd simple Bol envelopes](../sources/odd-completion/odd-elementary-layer-obstructions.md)
- [Odd-order Bol envelope data](../sources/odd-completion/odd-envelope-parameterization.md)
- [Classification of extraspecial-derived odd Bol loops](../sources/odd-completion/odd-extraspecial-classification.md)
- [Stabilizers and outer isotope automorphisms in the fixed class-four envelope](../sources/odd-completion/odd-fixed-envelope-stabilizers.md)
- [A simple odd Bol loop with a fixed noncentral derived shadow](../sources/odd-completion/odd-fixed-shadow-simple-example.md)
- [An odd-envelope quotient constraint](../sources/odd-completion/odd-folder-radicals.md)
- [Odd elementary layers in even canonical envelopes](../sources/odd-completion/odd-layers-in-even-envelopes.md)
- [Odd Lazard envelopes with no fixed quotient off the centers](../sources/odd-completion/odd-lazard-central-classification.md)
- [Matrix-pair similarity inside simple odd Bol loops](../sources/odd-completion/odd-matrix-pair-embedding.md)
- [A Heisenberg quotient and module control](../sources/odd-completion/odd-metabelian-heisenberg-control.md)
- [A nilpotent-residual splitting for odd metabelian derived groups](../sources/odd-completion/odd-metabelian-residual-splitting.md)
- [An abelian-by-abelian monolithic exclusion](../sources/odd-completion/odd-monolithic-abelian-by-abelian-exclusion.md)
- [Monolithic odd folders with higher elementary-layer defect](../sources/odd-completion/odd-monolithic-defect-two.md)
- [A simple proper odd Bol loop with monolithic envelope](../sources/odd-completion/odd-monolithic-heisenberg-construction.md)
- [A 21-line family with monolithic envelope](../sources/odd-completion/odd-monolithic-heisenberg-line-family.md)
- [A conditional prime family of monolithic odd Bol folders](../sources/odd-completion/odd-monolithic-heisenberg-prime-family.md)
- [Isomorphism classes of higher-defect Heisenberg loops](../sources/odd-completion/odd-monolithic-higher-defect-isomorphism.md)
- [A paired-diagonal monolithic exclusion](../sources/odd-completion/odd-monolithic-paired-diagonal-exclusion.md)
- [The nilpotent-derived odd-envelope route](../sources/odd-completion/odd-nilpotent-derived.md)
- [Simple odd Bol loops with noncentral derived centers of unbounded Jordan length](../sources/odd-completion/odd-noncentral-jordan-center-family.md)
- [Stabilizer splitting on paired odd-envelope layers](../sources/odd-completion/odd-paired-stabilizer-splitting.md)
- [Central stem extensions of the odd prime-parameter envelope](../sources/odd-completion/odd-prime-envelope-central-extensions.md)
- [A simple odd Bol loop with a nonisomorphic principal isotope](../sources/odd-completion/odd-rigid-center-nongloop.md)
- [Obstructions to enlarging monolithic odd constructions](../sources/odd-completion/odd-scalar-and-prime-square-obstructions.md)
- [Stabilizer alignment through odd normal layers](../sources/odd-completion/odd-stabilizer-alignment.md)
- [Odd simple Bol loops with unbounded derived nilpotency class](../sources/odd-completion/odd-unbounded-derived-class.md)
- [Odd simple Bol loops with unbounded derived length](../sources/odd-completion/odd-unbounded-derived-length.md)
- [Odd simple Bol loops of unbounded Fitting height](../sources/odd-completion/odd-unbounded-fitting-height.md)
- [Exact elementary-layer lifts of uniform inverted multitransversals](../sources/odd-completion/odd-uniform-multiplicity-layers.md)
- [A paired-layer extension criterion for an exact-factorization witness](../sources/odd-completion/paired-layer-factorization.md)
- [Radical-free inner inversion and PSL₂ envelopes](../sources/odd-completion/radical-free-inner-inversion.md)

## 5. Verification and remaining obligations

Source-specific automated reviews are evidence about the scoped arguments and cited interfaces, not human referee acceptance, formal verification or a literature-priority audit. Finite arithmetic certificates supplement the analytic proofs only on their explicitly enumerated instances. Public editing preserves mathematical content and normalizes formula delimiters; source provenance is recorded in the crosswalk.

The outstanding global work is to show which branches necessarily occur, obtain exhaustive structural reductions outside the proved hypotheses, and reconcile construction parameters with complete intrinsic isomorphism data. The [open problems board](../OPEN_PROBLEMS.md) distinguishes those obligations from solved subcases. None of the source libraries should be used to infer that the unrestricted classification is complete.
