# Candidate parameters for elementary-radical Bruck envelopes with product quotient

**Mira Cult**

**Effective structural parameterization with scoped independent reviews below, conditional on the cited inputs.** Fix a finite product

 A=∏_{i=1}^e PGL₂(q_i),  e≥1,

where each q_i is 9 or a Fermat prime ≥5, and put B=∏ B_i for chosen Borel subgroups. This note proposes effective structural data for faithful Baer envelopes of finite simple nonassociative right Bruck loops with elementary abelian radical V=O₂(G) and G/V≅A. It does not assume exponent 2, a split extension, a finite bound on e or the q_i, or existence of a solution for any choice. It continues [C0010](../../claims/0010.md), allocates no new claim ID, and uses [bruck-elementary-product-constraints.md](bruck-elementary-product-constraints.md) at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/b88cd1d25a469cc06277febc9f20725ed68934f4), independently accepted by contributor 1 and contributor 2 under its stated inputs. The special S₅ parameterization remains separate and is not overwritten. Associativity is automatically excluded by this quotient: an associative Bruck loop is an abelian group, whose Baer group is abelian.

The cited product input provides: canonical inversion fixes V, inducing δ∈Z¹(A,V) with δ|B=0 and an isomorphism between these relative derivations and Hom_A(ker(F₂[A/B]→1),V); exponent at most 4; H image B; the marked section involutions project to support classes described below; the full-support fiber counts; the invariant-functional restriction; and dim V≤[1+2^e(3e+1)]|A|m, where m is the total number of nontrivial composition factors. Those reviews apply only to the pinned product input, not to the new parameterization below.

## Module, extension, and stabilizer data

At fixed A and m≥1, choose a finite F₂A-module V within that bound. The cited product input establishes m≥1 by its integral-fiber argument. The module may be given by matrices satisfying a fixed finite presentation of A, with exactly m nontrivial composition factors. Finite-field linear algebra gives these composition factors and module isomorphisms; this is group-representation data rather than a loop multiplication table. Choose a B-invariant W≤V containing no nonzero A-submodule, and impose W+[V,A′]=V. Core-freeness follows because core_A(B)=1. To derive the displayed condition from the product invariant-functional obstruction, injectivity of Hom_A(V,1)→Hom_B(W,1) gives W+[V,A]=V: otherwise a nonzero functional on V/(W+[V,A]) would contradict injectivity. Put Q=V/[V,A′], and let U be the image of W in Q. The group P=A/A′≅C₂^e acts on Q, and B surjects onto P, so U is P-stable. The previous equality becomes U+I Q=Q for the augmentation ideal I⊂F₂P. Since I is nilpotent (the group algebra of a finite 2-group is local), Nakayama's lemma, or iteration of Q/U=I(Q/U), gives Q/U=0. Thus W+[V,A′]=V. This deduction uses the exact product functional-obstruction hypothesis, not an assumption that W+S captures every HR∩V.

Choose an extension class [c]∈H²(A,V) and a normalized representative c, forming G=V×_c A. Since A has no nontrivial normal 2-subgroup, V=O₂(G). Choose H over B with H∩V=W: the image of c|_B in H²(B,V/W) must vanish, and a solution of its coboundary equation specifies a complement H/W. Different solutions modulo V-conjugacy form an H¹(B,V/W) torsor; retain them rather than assuming a unique stabilizer.

Choose an A-map f:ker(F₂[A/B]→1)→V, or equivalently a relative derivation δ with δ|B=0. It defines τ(g)=δ(πg)g, an involutory automorphism fixing V and H, independently of whether G splits. Work in the formal external semidirect product G⁺=G⋊⟨hatτ⟩. The marked set Λ=hatτ K is a conjugacy-invariant involution set containing hatτ; K=hatτΛ, not Λ itself, is the prospective section.

## Support classes and affine radical exact cover

For each I⊆{1,…,e}, let C_I⊂A consist of tuples whose i-th coordinate is an involution in PGL₂(q_i)\PSL₂(q_i) when i∈I, and 1 otherwise. The product constraints and Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), §4, especially Lemmas 4.1, 4.4–4.5, give one A-conjugacy class C_I and

 |C_I|=∏_{i∈I} q_i(q_i−1)/2.

For each nonempty I choose a union Λ_I of G⁺-conjugacy classes of involutions in hatτ G projecting to C_I. Put K_I=hatτΛ_I. If n₀=2^{dim V−dim W}, require for every x∈C_I

 |K_I∩π⁻¹(x)| = n_I = n₀·2^{|I|}/∏_{i∈I}(q_i−1).           (1)

The value must be a positive integer. These are exact source fiber counts for the assumed Bruck setting, not inferred by enumeration. Choosing classes in G⁺, not merely G, ensures compatibility with inversion. Require pairwise collision-freeness for the combined outer set ⋃K_I against H; distinct supports need not be tested independently.

Choose D⊂V as a union of orbits for the affine action x⋅v=xv+δ(x), containing 0 and transversal to W. Explicitly, for its affine A-orbits O choose bits z_O, set the variable of the orbit of 0 to 1, and impose

 ∑_O |O∩(v+W)| z_O=1  for all v+W.                            (2)

Set Λ=hatτD∪⋃Λ_I and K=hatτΛ=D∪⋃K_I. Because τ fixes V, (2) makes hatτD invariant under conjugation, while the selected outer sets are invariant by construction. Thus Λ is G⁺-invariant, contains hatτ and consists of involutions. It follows that K is inverse-closed, τ inverts K, K is closed under k₁k₂k₁, and H normalizes K. In particular K K⁻¹ is G-conjugacy-invariant even though K need not be G-conjugacy-invariant.

Mixed radical–outer collisions are impossible: every nonempty support has an outer involution in some coordinate, while every conjugate of a Borel contains no such involution. The exact cover (2) handles radical collisions, and the chosen outer collision test handles the rest. The support-count identity

 |A:B|=∏(q_i+1)=∑_{I⊆[e]} ∏_{i∈I}q_i

and (1) imply |K|=n₀|A:B|=[G:H]. Thus K is a transversal to all conjugates of H, and defines a Bruck folder. Require separately <K>=G. This is a finite group computation, or a linear residue-span test: choose selected section lifts of a finite generating set of A, fix words for all support elements, and span in V the radical section, all fiber-versus-word differences and all relator residues. Such generators exist within the singleton-support classes: the normal closure in each PGL₂(q_i) of an outer involution contains its simple derived subgroup and the outer involution itself, hence is the whole factor. The fiber counts select every element of these support classes, so their union generates A. The stated residues generate <K>∩V; equality with V is generation. Selected lifts can have order 4, so squared relators must not be omitted.

## Exact simplicity test: all normal quotient supports

One cannot discard normal subgroups with proper quotient support. Enumerate them structurally as follows. For each A-invariant subspace S≤V, and each normal subgroup L◁A, consider R◁G with R∩V=S and πR=L. In G/S, such an R is a complement to V/S in the preimage of L. It exists exactly when c|_L becomes a coboundary in H²(L,V/S); enumerate the solutions r:L→V/S. Require (1−l)V⊆S for l∈L, and verify the finite conjugation-equivariance equations for the graph by lifts of generators of A. These conditions are necessary and sufficient for the inverse image R to be normal in G. The case L=1 includes all radical submodules S. The finite tests are cohomology and module equations, not loop-table enumeration.

This construction enumerates every normal R by its intersection S, image L and quotient complement; omit the single case S=0, L=1 corresponding to R=1. For each nontrivial such R with HR<G, require

 |KR/R| ≠ [G:HR].                                              (3)

The reviewed [C0001 normal-subloop criterion, Theorem 2.2](../foundations/C0001.md) makes this equivalent to simplicity, because core-freeness prevents any nontrivial normal R from being contained in H. Both sides are computed from the constructed extension and section; equality is the exact quotient-transversal condition, not an assumption that quotienting by S produces a loop.

For an efficient index calculation, let C=(HR)∩V. It is generated by W+S together with the differences h_b r_b⁻¹∈V for lifts h_b∈H, r_b∈R of b∈B∩L. Then

 [G:HR]=[A:BL]·2^{dim V−dim C}.                               (4)

The mismatch terms in C are essential: in general C need not equal W+S. The size |KR/R| can be computed by actual coset hashing in the finite extension using the selected orbit/class representatives. As an optional restriction on L, if I is its set of nontrivial coordinate projections, normality forces ∏_{i∈I}PSL₂(q_i)≤L≤∏_{i∈I}PGL₂(q_i), and L/(∏ PSL₂(q_i)) is a subgroup of the 2-elementary outer quotient. This includes proper I and mixed outer sign subspaces.

## Isomorphisms and actual scope

For two admissible data, possibly with differently labelled quotient presentations A and A′, a loop isomorphism induces an isomorphism of their Baer envelopes. Retain every quotient isomorphism γ:A→A′ carrying B onto B′. Unlike the single S₅ case, do not discard outer automorphisms, field automorphisms where present, permutations of isomorphic factors, or isomorphisms between different parameter labels. Search for a vector-space isomorphism α:V→V′ intertwining the A-action through γ, and a normalized 1-cochain u:A→V′ satisfying the transported extension equation

 α c(x,y)+c′(γx,γy)=d_γu(x,y),   αδ(x)=δ′(γx),                (5)

where d_γu(x,y)=u(x)+γ(x)u(y)+u(xy).
The resulting group isomorphism must send H to H' and K to K'. Conversely any such (γ,α,u) gives an isomorphism of the loop folders. Keeping the full cochain and exact H,K conditions accounts for different extension sections and complement choices.

At each fixed A,m the dimension bound makes the module, cohomology, subspace, class, affine exact-cover, normal-subgroup and isomorphism searches finite. These conditions are proposed to be sound and exhaustive conditional on the pinned product constraints and the cited normal-subloop theorem. They are an effective structural recognition scheme, not a numerical census, an efficient algorithm, or a solution of the unrestricted Bol-loop classification. The new construction, full normal-subgroup and isomorphism reductions have the scoped independent reviews below; the earlier product reviews cover only their pinned input.

## Independent reviews

reviewers contributor 3 and contributor 4 independently accepted this parameterization at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/9009bb98c97148e7cf250344f714528b1620b0a9), conditional on the product constraints reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b88cd1d25a469cc06277febc9f20725ed68934f4), C0001’s normal-subloop criterion and the cited class/fiber results. Both checked the module and complement data, Nakayama condition, affine and marked-involution construction, all-support collision and cardinality tests, independent generation, and enumeration of all normal subgroups including proper quotient supports. They checked the lift-mismatch terms in (HR)∩V and the full quotient-isomorphism/cochain/derivation criterion. The reviews accept a structural finite construction and recognition scheme at fixed A,m, beyond loop-table enumeration. They do not establish efficient computation, nonemptiness at every parameter, a numerical census, bounds on A or m, or classification of non-elementary radicals or unrestricted Bol loops. No new computation or formal verification was supplied; the upstream proofs remain the stated inputs.
