# Candidate effective parameterization for V₆⊕Uᵇ

**Mira Cult**

This manuscript continues [C0010](../../claims/0010.md) and allocates no new claim ID.

**Scoped independent mathematical review recorded below; conditional dependencies.** Work in the faithful simple exponent-two Bruck-envelope setting with elementary abelian radical V and quotient S₅. Assume V≅X⊕Uᵇ, X=V₆, and the [V₆ fiber bounds](bruck-s5-v6-fiber-bounds.md) giving W^P=X^P, dim W=2+4b and the full transposition-involution fibers. Assume the reviewed module separation and projective N-block inputs, the exact normal-subloop and folder equivalences, and the [b=1 V₆⊕U certificate](bruck-s5-v6-u-classification.md). At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097), contributor 1 accepted the b=1 mathematics and contributor 2 accepted its 485-count computation under their stated scopes. At the same source contributor 3 accepted the [uniform projective-only reduction](bruck-s5-projective-only.md). These reviews do not cover the new all-b argument below. The proposed procedure below is effective for each fixed b, not a numerical classification of all b or of other principal blocks. Each constructed loop has order 96·16ᵇ.

## Group extension and stabilizers

H²(S₅,X)≅F₂ and H²(S₅,U)=0, so G is either the split extension or the unique nonzero X-extension extended by the split Uᵇ-block. In the split case, normalize a P-lift inside H to the pure P by V-conjugation. P is normal in F=N_{S₅}(P); Schur–Zassenhaus inside the preimage of P in H makes N_H(P)→F onto. Since C_V(P)=X^P has dimension 2, N_H(P)=N_G(P)=X^P⋊F, so H contains pure F. The full transposition fibers contain pure disjoint transpositions t,u with tu∈F, contradicting transversality. In the nonsplit case the same argument gives H=W N_G(P), unique after conjugating the P-lift.

Over F=F₂₀ let S be the four-dimensional projective irreducible with End_F(S)=F₂. As in the reviewed J-family argument, use U=N⊗R for R=F₂[ε]/ε² and U|F=S⊗(A⊕T), where A is the socle and T a complement. Put L=X^P, dim L=2, and X|F=L⊕S_X. The latter splitting is by the P-idempotent. Thus [P,V]≅S⊗(F₂⊕A₀⊕T₀), with A₀,T₀ each F₂ᵇ, and W=L⊕S⊗B for a b-dimensional B. The units of End(Uᵇ)=Mat_b(R) act on multiplicity coordinates by (x,y,q)↦(x,Ay+Cq,Aq), with A∈GL_b(F₂), C arbitrary.

If B contains (x,y,0)≠0, there are three possibilities. For x=0, W contains an S₅-invariant copy of N, violating core-freeness. For x=1,y=0, W contains L⊕S_X=X, violating core-freeness. If x=1,y≠0, consider the graph S_X→N_y. Choose one U-coordinate carrying N_y by a GL_b(F₂) change of basis. The accepted uniform projective-only reduction supplies a shared explicit witness: for the unique F-isomorphism φ:S_X→N, there exist v∈S_X and l∈L such that v+l∈(1+t)X and φ(v)∈(1+t)U via the socle embedding. Thus the graph vector (v+l,φ(v)) lies nontrivially in W∩(1+t)V, contradicting transversality of the full transposition fiber. The witness is checked in the linked source; one must not assume (1+t)X⊆S_X, since t need not normalize P. Hence B→T₀ is injective and therefore an isomorphism. Write B={(λ(q),Dq,q)}. A shear removes D, and GL_b(F₂) makes λ either zero or q↦q₁. For b≥1 the two representatives are B₀={(0,0,q)} and B₁={(q₁,0,q)}; b=0 has W=L only. Block separation, X's fixed-free module lattice, and the injective T₀ projection show these normal-form W contain no nonzero S₅-submodule.

## Outer fibers and exact covers

For b≥1 project the first nonsplit X⊕U block and remaining U factors to the b=1 normal-form calculation. Under the accepted b=1 certificate, both outer-fiber types are transversal. If two full outer-fiber elements lie in one H-coset, their base projections coincide; their difference lies in the remaining U-block, belongs to the appropriate complement T^{b−1}, and is fixed by the common transposition. Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.3(i) gives T∩C_U(t)=0, so the difference is zero. Mixed radical/outer cosets do not collide because F contains no transpositions. Thus outer transversality for all b≥1 is conditional on the b=1 certificate and this projection. For b=0 the independently reviewed [dimension-six exclusion](bruck-s5-radical.md#degree-two-cohomology-calculation) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/20ba07f5536f13153a074d7dc70ec54b8dd3f6dd) applies; in particular, the only forced full-fiber radical section cannot generate G.

For either normal form, enumerate the S₅-orbits O on V and W-cosets v+W. Binary variables x_O satisfying

  x_{\{0\}}=1,    Σ_O |O∩(v+W)| x_O=1 for every v+W

define exactly all invariant radical sections D containing 0 and transversal to W. With the forced full outer class C, K=D∪C is conjugacy-invariant, consists of involutions, and is a transversal to H and its conjugates. The reviewed nonsplit dimension-six certificate gives an index-two subgroup of the X-extension containing every transposition involution lift and intersecting X in J. The subgroup generated by C projects onto S₅ and contains [S₅,V]=J⊕Uᵇ; it is therefore exactly the index-two preimage L_G with radical J⊕Uᵇ. Consequently K generates G if and only if D meets V\(J⊕Uᵇ). This is an image/generation argument, not a quotient-loop assertion. The exact-cover test plus that condition is a finite construction for each b.

## Simplicity criterion

For R◁G with nontrivial image in S₅, its image contains A₅ and [V,R] contains [V,A₅]=M⊕Uᵇ. Since X=M⊕L as F₂-vector spaces and F A₅=S₅, V⊆HR and HR=G. Thus proper normal-subloop kernels can only arise from S₅-submodules S≤V. Block separation gives exactly

  S=S_X⊕(N⊗B),   S_X∈{0,M,J,X},

where B ranges over the ε-stable F₂-subspaces of Rᵇ. For each nonzero S, with C_t=C_V(t), compare

  |KS/S| = |(D+S)/S|+10·2^(dim C_t−dim(C_t∩S)),
  [G:HS] = 6·2^(dim V−dim(W+S)).

The full fibers ensure the first equality; distinct images over the ten transpositions stay distinct modulo S≤V. By [C0001's exact normal-subloop criterion](../foundations/C0001.md), equality gives a proper nontrivial quotient (π(HS)=F and core-freeness excludes S≤H). Thus a constructed folder is simple precisely when all these comparisons are unequal. Include S=V: the two values are 11 and 6. This is a finite linear-algebra/orbit calculation for each b.

## Isomorphism interface

All automorphisms of S₅ are inner and N_{S₅}(F)=F, so after conjugation by the target stabilizer any folder isomorphism induces identity on S₅. Block separation, End(X)=F₂, and End(Uᵇ)=Mat_b(R) force its radical action to be identity on X and an element of GL_b(R) on Uᵇ. Conversely such a unit lifts by acting on the split Uᵇ-block, preserves the full outer class, and sends W,D to the transported data. Normalized H's are V-conjugate: after matching W, their P-lifts are V-conjugate and both contain N_G(P), as above. Thus data are isomorphic exactly under GL_b(R). The normalized B₀ and B₁ are distinct orbits, and their stabilizers are respectively GL_b(F₂) and {A∈GL_b(F₂):λA=λ}; in both cases the ε-shear must vanish to preserve the zero-socle graph. Quotient the finite exact-cover solutions satisfying the generation and simplicity tests by these groups.

At b=1 the separately reviewed count is 362+123=485, including the identity-containing exact-cover checks, at [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097). At b=0 there are no admissible simple envelopes by the dimension-six result. None of this proves existence for every b, nor treats principal blocks outside V₆.

## One-M assembly

**Scoped independent assembly and all-b review recorded below.** Combine the [projective-only reduction](bruck-s5-projective-only.md), accepted at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b4d22c1c373a162117c0726b2faa2237fc51097), with the [J⊕Uᵇ parameterization](bruck-s5-j-projective-family.md), accepted at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c314e6ed0153240a4712b08d59288501f560f977), and the proposed V₆⊕Uᵇ parameterization above. Conditional on these arguments and their cited inputs, every faithful Baer envelope of a finite simple exponent-two Bruck loop with elementary abelian radical, quotient S₅ and exactly one M composition factor is covered by one of those two effective parameterizations. Its order is 96·16ᵇ. The b=0 J branch gives the unique Nagy loop of order 96, while the V₆ branch has no b=0 envelope. At b=1, the separately reviewed J⊕U and V₆⊕U counts give 53+485=**538** classes.

The two branches cannot identify the same loop: their canonical faithful Baer envelopes have radical dimensions 5+8b and 6+8b, respectively, and hence group orders differing by a factor of 2. The canonical folder equivalence identifies a loop isomorphism with an isomorphism of its faithful canonical envelope, so those group orders are loop invariants. The loop order determines b. This assembly makes no claim about other order-1536 loops or envelopes with more than one M composition factor; its arbitrary-b V₆ component and this corollary have the exact-source review below.

## Independent review

contributor 1 accepted the V₆⊕Uᵇ parameterization and one-M assembly at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b091f64620504d07eadfe4186f265eb5afc18e2), conditional on the listed prior V₆/J, cocycle, module, shared-witness, b=1, projective-only and C0001 inputs. The review checked extension and H normalization, zero-top exclusion and graph normal forms, the all-b outer projection, generation, exact-cover necessity and sufficiency, every invariant-submodule quotient test, and both directions of the GL_b(R) equivalence. It also checked the explicit normalized stabilizers and the assembly: orders 96·16ᵇ, b=0 unique Nagy loop, b=1 538 classes, with the two branches distinguished by canonical envelope orders. This is an effective structural procedure under elementary radical, S₅ quotient and exactly one M; it does not claim existence for every b or unrestricted classification.
