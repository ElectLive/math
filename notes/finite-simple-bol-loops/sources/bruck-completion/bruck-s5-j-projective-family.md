# Candidate linear-algebra reduction for J ⊕ U^b

**Mira Cult**

**Scoped independent mathematical review recorded below.** Assume the exact envelope hypotheses and reviewed inputs of [bruck-s5-j-branch.md](bruck-s5-j-branch.md), reviewed by contributor 1 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/527aa14d458a5b7d43cef2be7faef4c90033b975): V=J⊕U^b, b≥0; G is Nagy's nonsplit E over J extended by the split U^b block; L=J^P≤W=H∩V; W=L⊕S⊗B, dim B=b; and every involution above every transposition belongs to K. Here F=N_{S5}(P)≅F20 and S is its projective irreducible 4-dimensional module. The source for the module U and its F-complement T is Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemmas 4.1–4.3. Below is a proposed uniform stabilizer reduction and a finite exact-cover interface for the remaining radical section. It does not claim every exact cover is simple. The proposed isomorphism criterion distinguishes the two W types, with the scoped review recorded below. This is an effective parameterization, not an explicit enumeration for all b or a classification of all Bol loops. Every resulting loop has order 96·16^b, so its order determines b.

## Stabilizer multiplicity spaces

Write U=N⊗R for R=F₂[ε]/(ε²), with socle εU=N; restrict to F and choose an F-isomorphism U|F≅S⊗(A⊕T), where A is the socle and T a complement. There is also J|F=L⊕S_J. Thus [P,V]≅S⊗(F₂⊕A₀⊕T₀), with A₀=T₀=F₂^b, and every F-stable W with dim W=1+4b and W^P=L has the form W=L⊕(S⊗B), for a b-dimensional subspace B≤F₂⊕A₀⊕T₀. This uses End_F(S)=F₂ and semisimplicity of the unique projective simple block.

The endomorphisms of U^b form Mat_b(R), and its invertible module maps are GL_b(R). Relative to these coordinates they act as

(x,y,q) ↦ (x,A y+C q,A q),  A∈GL_b(F₂), C arbitrary b×b.

This uses End_{A5}(N)=F₂ and the sign action on the multiplicity modules. These automorphisms lift to the fixed group extension because they are identity on J and the U-block extension splits.

Suppose B has a nonzero vector (x,y,0). If x=0, then S⊗⟨y⟩ is an S₅-invariant copy of N contained in W, contradicting core-freeness. If x=1 and y=0, then W contains J, again impossible. If x=1 and y≠0, W contains the graph of an F-isomorphism S_J→N_y⊂U^b. As in the b=1 calculation [bruck-s5-j-one-projective-block.md](bruck-s5-j-one-projective-block.md), reviewed by contributor 2 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/527aa14d458a5b7d43cef2be7faef4c90033b975), C_{N_y}(t) has dimension 3, while (1+t)J has dimension 2 in S_J. Their graph preimages therefore meet nontrivially; because C_{N_y}(t) lies inside (1+t)U^b, one gets W∩(1+t)V≠0. This contradicts transversality of the mandatory involution fiber. Hence B→T₀ is injective and, because both have dimension b, an isomorphism.

Write B={(λ(q),Dq,q):q∈T₀} for a linear functional λ and matrix D. A shear C removes D; a change A∈GL_b(F₂) puts λ in one of exactly two orbits: zero, or q↦q₁. Thus there are precisely two potential stabilizer types for b≥1, represented by

B₀={(0,0,q)},   B₁={(q₁,0,q)}.

For b=0 there is one type W=L. Both displayed W are core-free: J and U blocks have no cross S₅-homomorphisms, no nonzero S₅-submodule of J lies in L, and B→T₀ injective ensures W meets the U^b socle trivially; every nonzero submodule of U^b meets its socle. The isomorphism argument below shows that larger envelope automorphisms induce no additional identifications.

## Outer-fiber transversality

For b=0 Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Theorem 3.6 supplies a folder. For b=1 the two displayed cases are the undeformed folder of Proposition 5.1 and the deformed folder of Theorem 5.2. The following projection proves full mandatory outer–outer transversality for all b. Project G to the first J⊕U factor (or to J for B₀), with W projected to the corresponding base stabilizer and the rest equal to T^{b−1} (or T^b). If two outer involution lifts have quotient in H, their projections have quotient in the base H; base folder transversality forces their projections to coincide. Their quotient is then in the remaining U-block and in W, and belongs to C_{Urest}(t) for their common transposition t. Nagy Lemma 4.3(i) gives T∩C_U(t)=0, so the quotient is trivial. Because F is transitive on transpositions, the same holds for any t. The radical–outer products cannot lie in a conjugate of H since F contains no transpositions. Thus outer transversality is independent of the radical-section choice, with the projection argument and source matching reviewed below.

## Radical exact cover and equivalence interface

For fixed b and either normal-form W, enumerate the S₅-orbits O on V, including {0}. Form the integer matrix A with one row per W-coset v+W and one column per O, entry A_(v+W,O)=|O∩(v+W)|. The binary variables x_O define D=⋃_{x_O=1}O, and the equations A x=1 with x_{0}=1 are exactly the condition that D is S₅-invariant, contains 0, and is a transversal to W in V. These are explicit finite orbit computations and integer exact-cover equations; they do not require enumerating loop multiplication tables. Because D is S₅-invariant and W conjugates equivariantly, the resulting full K=D∪K_outer is a transversal to H and all its conjugates once the outer transversality claim above is accepted. It then defines an exponent-2 Bruck folder.

The mandatory outer class alone generates G: it projects onto the Nagy group E, generated by its involution class, and products of lifts over a fixed t generate C_{U^b}(t). The S₅-span of C_U(t) is U: C_U(t) has dimension 4 and its intersection with socle N has dimension 3, so it is not contained in N, the unique nonzero proper S₅-submodule of U. Each U copy is obtained independently. Therefore every exact-cover solution gives an envelope, subject to the outer-transversality proof.

## Simplicity via module subspaces

Use the reviewed exact normal-subloop criterion in [C0001 proof](../foundations/C0001.md#4-exact-simplicity-and-normal-subloop-criterion-in--g-h-k) Theorem 2.2, transported to right folders. Every normal subgroup R◁G with nontrivial image in S₅ has image containing A₅. Commutators give [V,R]=[V,A₅]=M⊕U^b≤R. Since L≤H and J=M⊕L as F₂-spaces, V≤HR. Also π(HR)=F·A₅=S₅, so HR=G. Such R cannot yield a proper quotient. The containment V≤HR is essential: π(HR)=S₅ alone would not suffice.

Consequently only nonzero S₅-submodules S≤V can give proper nontrivial kernels. The reviewed block separation and the submodule lattice of J imply

S=S_J⊕(N⊗B),  S_J∈{0,M,J},

where B ranges over the R-submodules of R^b. The latter can be enumerated as the ε-stable F₂-subspaces of F₂^{2b}, giving finite linear algebra data. Put C=C_V(t), d=dim V and w=dim W. For every such nonzero S, the section image has size

|KS/S| = |(D+S)/S| + 10·2^{dim C−dim(C∩S)},

because K has the radical part D and the full involution fiber over each of the ten transpositions. The index is

[G:HS]=6·2^{d−w−dim S+dim(W∩S)}.

The reviewed normal-subloop criterion says equality holds exactly when the image is a transversal and yields a loop quotient. Core-freeness makes S not contained in W, so this quotient has nontrivial kernel; π(HS)=F makes it proper. Therefore the constructed loop is simple exactly when the two displayed integers differ for every nonzero S on the finite list. This tests only invariant subspaces and orbit counts, with no assumption that quotienting by Y produces a loop.

## Isomorphism criterion

For two such data (B,D), a loop isomorphism induces a Baer-envelope isomorphism. All automorphisms of S₅ are inner, and since both stabilizers project to F, the quotient automorphism is conjugation by an element of N_{S₅}(F)=F. Compose with conjugation by a lift in the target H to make it identity; this preserves target H and K. Block separation and Aut_{S₅}(J)=1 force its radical restriction to be identity on J and A∈GL_b(R) on U^b. Here Aut(J)=1 follows from the nonsplit 0→M→J→1→0, End(M)=F₂ and Hom(1,M)=0. Therefore A carries B to B' and D to D'.

Conversely every A∈GL_b(R) carrying B,D to B',D' lifts to the group automorphism that is identity on the Nagy group E and A on the split U-block. It preserves the full outer involution class. The image of H has the right W'; it is conjugate by V to the selected H' because H¹(F,V/W')=0. This conjugation leaves D' and the outer class fixed. Hence the loops are isomorphic exactly when their data lie in the same GL_b(R)-orbit. Equivalently, after selecting B₀ or B₁ as normal form, quotient exact-cover solutions by that B's stabilizer in GL_b(R). The two B types cannot mix under this action. For the normalized graphs $`B_i=\{(\lambda_i(q),0,q):q\in\mathbb F_2^b\}`$, a unit $`A+\varepsilon C\in GL_b(R)`$ sends a graph vector to $`(\lambda_i(q),Cq,Aq)`$. Preserving the graph forces $`C=0`$ and $`\lambda_i A^{-1}=\lambda_i`$, equivalently $`\lambda_i A=\lambda_i`$. Thus the stabilizer acting on radical exact covers is explicitly $`GL_b(\mathbb F_2)`$ for $`B_0`$, and $`\{A\in GL_b(\mathbb F_2):\lambda A=\lambda\}`$ for $`B_1`$, where $`\lambda(q)=q_1`$. No nonzero ε-shear preserves either normalized graph. At b=1 both stabilizers are trivial, consistent with the separately proposed 53-class computation, whose separate scoped mathematical and computational reviews are recorded there.

These arguments and the exact-cover/outer-fiber construction above have the scoped review below; they concern only this J⊕U^b branch, not all Bol loops.

The stabilizer classification, outer-projection argument, exact-cover equations, simplicity test and isomorphism criterion have their separate review below. The cited b=1 review covers its source revision only and does not certify this arbitrary-b argument. No permanent claim ID is allocated.

## Independent review

contributor 3 accepted the effective construction, simplicity and isomorphism criteria at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c314e6ed0153240a4712b08d59288501f560f977), conditional on the cited reviewed branch, Nagy base folders, block separation and exact normal-subloop criterion. The review checked the multiplicity-space and endomorphism descriptions, zero-top collision, two normal forms and core-freeness, outer projection argument, generation, invariant-submodule list, both quotient formulas, lifting and normalization of isomorphisms, and explicit normal-form stabilizers. This is a finite orbit/exact-cover procedure for each b, not a numerical enumeration for all b or a classification of other modules. No computation is needed for the new all-b deduction; the b=1 count has its separate reviews.
