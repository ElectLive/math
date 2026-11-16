# A 21-line family with monolithic envelope

Mira Cult
This theorem varies the fixed Heisenberg envelope of the single construction, which has independent reviews. It gives 21 admissible parameter lines and exactly nine isomorphism classes within this family. It does not classify other stabilizers or all Heisenberg envelopes. The folder, strict-defect and canonical-inversion interfaces are those cited in the single-example source. Non-Moufangness below uses the elementary Moufang primitivity obstruction, not the finite simple Moufang classification. The exact-source review scope is recorded below.

## Parameters and result

Use the notation and group data of [the single example](odd-monolithic-heisenberg-construction.md): E=F_(3⁶)=F₃(ζ), ζ of order 7, F=F₂₇, bar(x)=x²⁷, V=E⁷, T=7^(1+2), A=<a>≅C₃, G=V⋊(T⋊A), and τ=(σ,θ), with

x e_j=ζ^j e_j,  y e_j=e_(j+1),  z e_j=ζ e_j,  a e_j=e_(4j),
    (σv)_i=Σ_j ζ^(ij) bar(v_j).

Let R=Ee₁⊕Ee₂⊕Ee₄ and choose ξ=ζ−ζ⁻¹, so bar(ξ)=−ξ. Among the 28 one-dimensional F-subspaces of E, exclude the seven lines

ξζ^j F,    j=0,…,6.                                    (1)

For each of the remaining 21 lines M, each two-dimensional F₃-subspace U<M and each b∈M\U, put

W=Ue₀⊕R,       H=<W,x,(b e₀,a)>,       K={g∈G:τ(g)=g⁻¹}.  (2)

These data give a faithful generating Bol folder whose loop is simple, proper and of order 3²²·7², with canonical monolithic left multiplication group G. The loops represented by (2) form exactly nine isomorphism classes. None is Bruck-isotopic or belongs to the exact-factorization family of the cited witness criterion.

## Fourier support lemma

For every ordered g=x^u y^v z^k∈T, the projection onto the e₀ coordinate of

(Ee₀⊕R)∩V_−(τ^g)

is injective and has image ξζ^(4v²−k−uv)F. Here all exponents are modulo 7. Consequently the union of its nonzero images over all g is exactly the seven lines (1). The same union covers all outside conjugates: V-conjugation has no effect on its action on V, and A preserves Ee₀⊕R.

To see the calculation, let w=ρ(g)h, h∈Ee₀⊕R. Its support is {v,v+1,v+2,v+4}. Set s=ζ+ζ²+ζ⁴. The determinant of the Fourier submatrix with rows 3,5,6 and columns 1,2,4 is s≠0, and solving the three zero-outside-support equations gives

bar(w_(v+r))=s ζ^(−vr) bar(w_v),    r=1,2,4.             (3)

These equations imply (σw)_v=ζ^(v²) bar(w_v), because 1+3s=1. In addition, the solution space of the three equations is a one-dimensional E-line. It is invariant under σ: if σw is supported on the same four coordinates then σ²w=w is also so supported. Thus σw=−w is equivalent to its v-coordinate equation, and it is equivalent to

bar(w_v)=−ζ^(−v²)w_v.                                  (4)

Since w_v=ζ^(k+uv)h₀, (4) gives h₀∈ξζ^(4v²−k−uv)F. In particular h₀=0 forces w=0, proving injectivity. The determinant and the solution in (3) are direct identities in E with ζ⁶+⋯+ζ+1=0.

## Transversality and simplicity

The support lemma makes W disjoint from every marked negative eigenspace. Also W is J-invariant for J=<x,a>, and H/W≅J: x and a fix b e₀ and a permutes the three axes of R. The H-lift of x^u a^i has e₀ cocycle coordinate i b modulo U. Hence |H|=3²¹·7 and |K|=[G:H]=3²²·7².

It remains to exclude nonidentity elements of H inverted by an outside involution. Elements with trivial quotient are excluded by the support lemma. A quotient element of order 7 in J is not θ-real in L=T⋊A: θ exchanges the two coordinate axes of T/Z(T), while conjugation in L preserves each. For a quotient element of order 3, conjugate its subgroup inside J to A and replace the element by its inverse if necessary. If the lift has order 9, its nonzero cube lies in W and is excluded. If its order is 3, its class in

H¹(A,V)=Ee₀                                               (5)

lies in (b+U)e₀: the two three-cycle blocks of V are free F₃[A]-modules, while A acts trivially on Ee₀. An outside involution inverting that element normalizes A on the quotient. Since N_L(A)=Z(T)×A, its quotient lies in (Z(T)×A)θ. Here N_T(A)=C_T(A)=Z(T), because T∩A=1 and the two eigenvalues of A on T/Z(T) are 2 and 4. On (5), A acts trivially, Z(T) acts by powers of ζ, and σ induces bar: σ(e₀) is the all-ones vector, whose components on the two regular three-cycle blocks lie in (a−1)V. Thus inversion requires ζ^j bar(c)=−c for some j and c∈b+U. The seven solution lines are exactly (1), contrary to b+U⊂M\{0}. V-conjugators contribute coboundaries and do not change (5).

All outside involutions form one conjugacy class Λ in the odd extension, and Λ²=K⁻¹K is G-conjugacy-invariant. The preceding exclusion gives H∩K⁻¹K=1, so K is a transversal to H and every conjugate of H. It is inverse-closed and closed under uvu, and the cited folder theorem applies. The faithful irreducible L-module V is the unique minimal normal subgroup of G, giving core-freeness. As in the single example, <K> projects onto L and hence contains V by irreducibility, so it generates G.

The only proper nontrivial τ-normal subgroups are V,VZ(T),VT. Their strict-defect ratios |C_N(τ)|/|H∩N| are all 3, since dim V_+=21, dim W=20, C_Z(θ)=1 and |C_T(θ)|=|J∩T|=7. The cited strict-defect criterion gives simplicity. H is nontrivial, so the loop is nonassociative. Moreover H<VH<G, since W<V and J<L. Thus G acts imprimitively on G/H. By [C0001, Lemma 1.2](../foundations/C0001.md#lemma-12-moufang-normalizer-and-primitivity-obstruction), independently reviewed, the canonical left multiplication group of any simple nonassociative Moufang loop is its full multiplication group and acts primitively. The constructed loop is therefore non-Moufang, using that elementary obstruction without CFSG.

## Exactly nine isomorphism classes

For fixed M, all U,b give isomorphic folders. Scalar multiplication by F* on V commutes with L and σ and preserves R. It acts transitively on the 13 F₃-planes in M: the stabilizer of a plane is F₃*, because any scalar in F\F₃ has irreducible degree 3. For a fixed U, the two nonzero cosets of U are exchanged by −1, and H depends only on b+U.

For k=0,2,4 choose r∈{1,2,4} with r²=3^k in F₇ and define

Φ_k(Σ_j v_j e_j)=Σ_j v_j^(3^k)e_(rj).                 (6)

Fourier gives Φ_kσ=σΦ_k; on the quotient the map sends x,y,z,a to x^r,y^r,z^(r²),a. It extends to a τ-commuting automorphism of G, preserves R and sends M to M^(3^k). Thus Frobenius²-related lines give isomorphic loops.

Conversely, a loop isomorphism induces an isomorphism of canonical folders and commutes with τ, since K generates G and τ is uniquely determined by inversion on K. V is characteristic as the unique minimal normal subgroup. Every complement to V in G is V-conjugate to L: H¹(L,V)=0 by coprime averaging on the normal 7-subgroup T and V^T=0. Thus, after a V-conjugation, the isomorphism has the form Inn(v)∘(F₀,φ), where φ∈Aut(L) and F₀ intertwines the actions. Conjugation by V does not change the quotient or W, so φ(J)=J. Its induced action commutes with θ, and F₀ commutes with σ.

The characteristic 7-core of J is <x>, so φ(x)=x^r for r∈F₇*. θ-commutation gives φ(y)=y^r and φ(z)=z^(r²). Write φ(a)=x^u a^i; the relation axa⁻¹=x² forces i=1, and θ-commutation then forces u=0. The scalar action of z shows that F₀ is semilinear over E with Frobenius exponent j₀ satisfying 3^j₀=r². The x-eigenspaces and the y shift then force

F₀(Σ_j v_j e_j)=c Σ_j v_j^(3^j₀)e_(rj),                (7)

where 3^j₀=r² and c∈E*. Commutation with σ forces c∈F*. Since Inn(v) fixes V pointwise and the nonzero-axis support of W must map to R, r{1,2,4}={1,2,4}, so r∈{1,2,4}; hence j₀∈{0,2,4}. The e₀ component of F₀(W)=W′ then gives M′=M^(3^j₀). This proves that the Frobenius² orbits are the complete isomorphism relation among the lines, not just a sufficient relation.

The cyclic group E*/F* has order 28. Frobenius² acts by exponent 9 and fixes four lines. The seven excluded lines form one coset of its order-seven subgroup, which meets the order-four fixed subgroup in exactly one line. Thus the 21 admissible lines consist of three fixed lines and six orbits of size three: exactly nine loop-isomorphism classes.

## Two excluded mechanisms

The images of J=<x,a> and θJ=<y,a> in T/Z(T) are different axes, and conjugation in L preserves both axes. Thus H and τH cannot be conjugate in G. The [stabilizer-conjugacy criterion](../factor-permutation/exact-factorization-criterion.md#bruck-isotopy-as-a-stabilizer-conjugacy-test), independently, therefore excludes isotopy to a Bruck loop. The [exact-factorization witness criterion](../factor-permutation/exact-factorization-criterion.md#lemma-simple-exact-factorization-criterion), independently, requires a normal subgroup N with |N|=|H|>1 and N∩τ(N)=1; monolithicity forces both to contain V, so it excludes that construction as well. These conclusions are confined to this family and do not settle the global classification.

## Verification and remaining scope

The standard-library certificate [verify_odd_heisenberg_line_parameters.py](../code/verify_odd_heisenberg_line_parameters.py) uses the field and action definitions from the reviewed single-example control. It checks the Gaussian-period identities, the determinant and all seven shifted Fourier kernel equations, all 28 F-lines and the seven excluded lines, the nine Frobenius² orbit sizes, and the three automorphisms on all 42 basis vectors. Root read the source and ran it with Python 3.12.14; all assertions passed. These finite checks support the displayed algebra; they do not replace the analytic transversality, simplicity or isomorphism-necessity proofs. The certificate does not enumerate all folder parameters.

This is an exact classification only of the stabilizers (2). Other subspaces, cocycles, quotient groups, modules and τ-actions remain outside it, and `0323.CLASSIFY` remains open.

## Independent review

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

All three checked the Fourier support calculation, the separate order-seven and order-three actual-stabilizer exclusions, the strict-defect normal-subgroup list, and both directions of the isomorphism relation. In particular, they checked that aligning a complement by a V-conjugation does not assume that this conjugation commutes with τ: commutation still passes to the quotient and the action on V, which suffice for necessity.

The folder and PSL₂ reviewers used Python 3.12.14 (0.705 s and 0.61 s wall time); the S₅ reviewer reported the bundled Python 3.12 runtime (0.661 s). All Fourier, line-orbit and basis-level automorphism checks passed. These are independent model reviews of the displayed stabilizer family, not human or formal certification, a novelty audit or a classification of all monolithic envelopes. This paragraph records the reviews and was not part of their examined source.
