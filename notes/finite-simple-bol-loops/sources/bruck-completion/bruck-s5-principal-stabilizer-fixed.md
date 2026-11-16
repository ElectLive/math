# P-fixed stabilizer feasibility for one-M principal blocks

This manuscript continues [C0010](../../claims/0010.md), allocates no new claim ID, and records a necessary-condition computation with scoped independent review below; the appended `--models` calculation has a separate scoped review below. It assumes the envelope hypotheses and invariant-functional obstruction in [the principal-envelope bound](bruck-s5-principal-envelope-bound.md), the one-M cover and the [17-isotype classification](bruck-s5-principal-isotypes.md). The latter was accepted by an independent check at source the recorded source revision under its recorded scope. The computation does not construct a stabilizer, group extension, section, folder, or loop, and gives no dimension bound on the N-block.

## Reduction to a finite graph problem

Write the radical module as V=X⊕Y, with X=X₀⊕A its principal block, A=1ᵘ⊕Rᵛ, and Y having only N composition factors, as in the cited reductions. Let P≅C₅ and F=N_{S₅}(P)≅F₂₀; write W=H∩V and W₀=W^P. The natural four-dimensional module N has no P-fixed vector: on the five-point permutation module a 5-cycle fixes only the constant vector, while N is its even-weight complement. Restriction to P is semisimple in characteristic 2, so the P-fixed functor is exact; a composition series of Y gives Y^P=0. Thus W₀≤C_X(P).

Core-freeness gives W₀∩A=0. Indeed W∩A is F-invariant, and F acts on A through the same sign quotient as S₅, so W∩A is S₅-invariant and lies in the normal core. Likewise W₀∩V^{S₅}=0. Here Y^{S₅}=0 since Y has no trivial composition factor, so this last condition is W₀∩X^{S₅}=0. Every invariant functional on V vanishes on Y (Y has no trivial quotient), and hence invariant functionals are dual to X/[S₅,X]. The cited obstruction says restriction to W is injective. Since P acts trivially on the target and |P| is odd, each such functional has the same image on W as on W₀: averaging over P projects W onto W₀. By finite-dimensional duality, the map W₀→X/[S₅,X] must therefore be surjective.

Put K=C_{X₀}(P). Since W₀∩A=0, projection onto K identifies W₀ with the graph of a unique linear f:U→A for some subspace U≤K. Choose Q whose image generates F/P. P acts trivially on K and A; the graph is F-invariant exactly when U is Q-invariant and fQ=Qf. Conversely every such graph has trivial intersection with A. Thus exhaustive enumeration of Q-invariant U and Q-equivariant f, followed by the fixed-vector intersection and coinvariant-surjectivity tests, is exactly the stated necessary feasibility problem. The condition dim U≥dim X/[S₅,X] permits a safe early cutoff.

## Certificate and results

[verify_bruck_s5_principal_stabilizer_fixed.py](../code/verify_bruck_s5_principal_stabilizer_fixed.py) imports the classifier at the stated source and its reviewed enumerator dependency at the recorded source revision. Their SHA-256 file digests at these pins are respectively `4f4673e6909175c5ccea9f85703e884a372d2d7edd9040950c98b37f6e14406d` and `75f773394e5f59f85bf506764482618bc2b6ee5d4e021b383200495c4c05bf33`. In their six-point convention it constructs all 120 elements and verifies that P=(1,3,2,5,0,4), word CD, has order 5, and Q=(3,4,2,1,0,5), word DCDCDDC, has order 4. It checks Q normalizes P, the normalizer has order 20, and the 20 products PⁱQʲ are distinct. C and D are odd in the six-point action; Q is odd, so its action on A is the sign involution.

The program checks dim K=d−4≤4 for each isotype. It enumerates all subspaces by repeatedly adjoining vectors; for ambient dimensions 0 through 4 it asserts counts 1, 2, 5, 16 and 67. For each Q-invariant U it solves the intertwiner equations over F₂ and enumerates every linear combination of a basis. Two rank tests enforce the intersection and surjectivity conditions. The underlying classifier's identity, swap, zero and identity-plus-swap R-unit controls run on import; the present program asserts two rejected controls as well as the complete survivor list.

For the 79 labelled-isotype triples satisfying h₀+u+v≤d−4, the program tests 2403 graph maps after the dimension cutoff and reports six feasible triples, all with u=v=0. Class labels refer to the table in [the isotype manuscript](bruck-s5-principal-isotypes.md):

| Class | X₀ label (quotient,a,b,index) | dim X₀ | h₀ |
|---:|:---|---:|---:|
| 0 | (M,0,0,0) | 4 | 0 |
| 1 | (M,0,1,1) | 6 | 0 |
| 3 | (M,1,0,1) | 5 | 0 |
| 4 | (J,0,0,0) | 5 | 1 |
| 7 | (J,1,0,1) | 6 | 1 |
| 13 | (V₆,0,0,0) | 6 | 1 |

The program prints bases for a feasible graph in each case and the 73 rejected triples. In particular, if the earlier M-alone exclusion applies, five principal-module candidates remain. Under all stated hypotheses this necessary-condition calculation yields the conditional **principal-block dimension bound 6**. It does not bound the total radical: the N-block is outside this test. Neither a feasible graph nor the dimension bound establishes an envelope or a loop.

From the repository root, using Python 3.12.14 and the exact reviewed dependencies:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_s5_principal_stabilizer_fixed.py
```

The default feasibility computation and its reduction were independently accepted by an independent check at exact source the recorded source revision. The review checked the P-fixed and coinvariant reductions, core-freeness, complete graph enumeration, the exact F₂₀ construction, cutoff and rank tests, and dependency digests. An independent Python 3.12.14 run reproduced 79 triples, 2403 graph checks, six survivors and 73 failures. After the prior M-alone exclusion this gives five necessary principal-block types of dimension at most six. It does not establish full stabilizer feasibility, bound the N-block or construct loops. The appended model identifications below are later work and are outside that review.

## Four models and their complete P-fixed feasibility sets

**Scoped independent model review recorded below.** The six-candidate feasibility result above was accepted by an independent check at exact source the recorded source revision. The separate [arbitrary-N exclusion of the dual J case](bruck-s5-jdual-arbitrary-n.md) was accepted by an independent check at the same source. Conditional on those two results and the preceding inputs, four principal candidates remain: classes 1, 4, 7 and 13. The following identifications and complete subspace enumeration have their separate source-pinned review below.

Let P₆ be the six-point permutation module with C and D acting by the explicit six-point permutations of the enumerator. Class 1 is V₆* and class 7 is P₆; classes 4 and 13 are J and V₆ by construction. The optional `--models` mode computes Hom spaces using both generator equations, exhausts their binary linear combinations and checks full rank and the two intertwining equations. Its explicit invertible column matrices, from the indicated class to its target, are

- class 1 → V₆*: `(63,31,60,58,54,46)`; the Hom space has dimension 1;
- class 7 → P₆: `(63,62,2,4,8,16)`; the Hom space has dimension 2.

Here an integer encodes one column in the target's standard bit basis, and V₆* uses inverse-transpose generator matrices. The script checks the displayed matrices directly; identification does not follow merely from matching dimensions.

For each of these four classes the program enumerates **all** subspaces of K=C_{X₀}(P), retains exactly those invariant under Q, disjoint from X₀^{S₅}, and surjecting onto X₀/[S₅,X₀]. There is no early exit in this mode. In the classifier's original bit basis its complete results are:

| Class | Model | basis of K | Q on basis of K | X₀^{S₅} basis | feasible W₀ |
|---:|:---|:---|:---|:---|:---|
| 1 | V₆* | 1, 2 | 2, 1 | 3 | 0 |
| 4 | J | 4 | 4 | empty | K |
| 7 | P₆ | 1, 8 | 1, 8 | 1 | ⟨8⟩ or ⟨9⟩ |
| 13 | V₆ | 4, 40 | 4, 44 | empty | K |

Under the displayed class-7 intertwiner, 8 maps to the fixed point of P in the six-point set and 9 to the sum of the five-point orbit; the remaining line of K is the all-ones fixed vector and is excluded by core-freeness. An S₅-module isomorphism transports K, Q-invariant subspaces, global fixed vectors and the coinvariant map, so the listed conditions and their completeness are invariant under replacing these matrix representatives by isomorphic modules. The same holds in the presence of any N-block Y, since Y^P=0 as proved above. These are necessary W₀ configurations; no actual stabilizer, extension, section, folder or loop is asserted.

Run the new calculation, in addition to the default check, with

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_s5_principal_stabilizer_fixed.py --models
```

## Independent four-model review and remaining envelope candidates

an independent check accepted the four-model appendix and optional `--models` computation at exact source the recorded source revision, conditional on the reviewed classifier, default feasibility theorem and J* exclusion. The review checked the inverse-transpose and permutation models, full-rank intertwiner equations, exhaustive Hom combinations, complete subspace enumeration without early exit, rank tests and transport of the P₆ lines. An independent Python 3.12.14 run reproduced both witnesses and all four feasible-subspace sets. Arbitrary Y remains covered through Y^P=0, not through a bound on its dimension.

Combining this reviewed four-model reduction with the separately reviewed [V₆*](bruck-s5-v6dual-arbitrary-n.md) and [P₆](bruck-s5-p6-arbitrary-n.md) exclusions at the same source leaves **X=J or X=V₆** as the principal block of an elementary-abelian S₅ Bruck envelope with exactly one M factor. In either case W^P=X^P. The N-block Y=Nᵃ⊕Uᵇ, extensions, the rest of W and the section K remain to be classified. This is a necessary module reduction, not an existence or full envelope-classification theorem.

