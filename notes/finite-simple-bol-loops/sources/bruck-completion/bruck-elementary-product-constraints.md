# Elementary-radical constraints for product PGL₂ quotients

**Mira Cult**

**Scoped independent reviews below, conditional on the cited inputs.** Let X be a finite simple nonassociative right Bruck loop with faithful Baer envelope (G,H,K), elementary abelian V=O₂(G), and quotient A=G/V=∏ᵢDᵢ, e≥1, where Dᵢ=PGL₂(qᵢ) and qᵢ=9 or a Fermat prime at least 5. Let Bᵢ≤Dᵢ be the point-stabilizing Borel, B=∏ᵢBᵢ, W=V∩H, and D=V∩K. These results continue [C0010](../../claims/0010.md); no new claim ID or classification is asserted.

We use Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemma 3.2(1)–(2) and Lemmas 3.4, 4.1–4.5, with the full faithful Bruck-envelope hypotheses there. Theorem 1(a), with the introductory odd-order Bruck solvability input, supplies the simple nonassociative 2-power-exponent case; Theorem 1(b) supplies the quotient structure; Lemma 4.1 gives Hbar=B and only the **coordinatewise** restriction on Kbar: each coordinate is 1 or an outer involution. It does not say that Kbar has at most one nonidentity coordinate. Lemma 4.2 gives V=WD. Lemmas 4.4–4.5 provide the joint-support conjugacy classes and fiber sizes used below. For Sylow restriction injectivity in mod-2 cohomology we use Cartan–Eilenberg, *Homological Algebra* (1956), XII §9 p. 257 and §10 Theorem 10.1 p. 259, [primary scan](https://www.math.stonybrook.edu/~mmovshev/BOOKS/homologicalalgeb033541mbp.pdf), also recorded in [REFERENCES](../foundations/references.md). Prior reviews of individual S₅ cases do not review this product argument.

## Inversion and active coordinates

The canonical inversion automorphism τ fixes H pointwise and takes k∈K to k⁻¹. It fixes W and, since V is elementary, fixes D. Thus V=WD implies τ|V=1. Every image of K in A is an involution or identity, so τ fixes that image and hence fixes A because K generates G. For a=gV define δ(a)=τ(g)g⁻¹∈V. This is a well-defined left derivation, zero on B, and k²=δ(kV) for k∈K. In particular X has exponent dividing 4. No splitting of G is assumed.

Let Ω=A/B and E=ker(F₂[Ω]→F₂). The natural bijection


```math
\{\delta\in Z^1(A,V):\delta|_B=0\}\cong\mathop{\mathrm{Hom}}\nolimits_A(E,V)
```


sends δ to the map taking aB+bB to δ(a)+δ(b); the inverse sends f to a↦f(aB+B). For i≠j and aᵢ∈Dᵢ,bⱼ∈Dⱼ, commutativity and the derivation identity give


```math
(1+b_j)\delta_i(a_i)=(1+a_i)\delta_j(b_j).
```


Thus the span of δᵢ(Dᵢ) is fixed by Bⱼ, but need not be fixed by all of Dⱼ. This interface retains possible mixed-coordinate coupling.

The zero set Z={a:δ(a)=0} is a subgroup containing B. Every subgroup between B and A is a product of choices Bᵢ or Dᵢ. Indeed each Bᵢ is maximal and self-normalizing by the doubly transitive projective-line action. If an intermediate subgroup contains x with xᵢ outside Bᵢ, self-normalization gives bᵢ∈Bᵢ with [bᵢ,xᵢ] outside Bᵢ; [bᵢ,x] is supported solely in factor i, so maximality forces Dᵢ into the subgroup. Consequently the stabilizer of 0 in the affine action a⋆v=av+δ(a) is ∏Cᵢ, with Cᵢ=Bᵢ exactly when δᵢ≠0. Lemma 3.2(2), using the formal semidirect product by τ, makes D affine A-invariant. Since 0∈D, δ(A)⊂D, and


```math
\prod_{i:\,\delta_i\ne0}(q_i+1)\le |D|=2^{\dim V-\dim W}.\tag{1}
```


D is a transversal to W in V, so the forced orbit also injects into V/W. This bounds simultaneously active coordinates only when the radical quotient dimension is independently bounded.

## Joint-support fiber constraints

For J⊆{1,…,e}, let t_J have an outer involution in exactly the factors indexed by J. Put d=dim V, w=dim W, and s_J=Σ_{j∈J} log₂((qⱼ−1)/2). Lemmas 4.4–4.5 give the same fiber size for all such elements:


```math
|K\cap\pi^{-1}(t_J)|=2^{d-w-s_J}.
```


The formula is positive; occurrence of all these classes follows from this fiber theorem, not merely from the coordinatewise containment in Lemma 4.1. V-conjugacy invariance gives orbit size 2^rank(1+t_J), while k²=δ(t_J) places the fiber in a single affine solution set of size at most 2^{d−rank(1+t_J)}. Hence


```math
\mathop{\mathrm{rank}}\nolimits(1+t_J\mid V)\le\min(d-w-s_J,\;w+s_J).\tag{2}
```


No additivity of ranks over factors is assumed.

## Central extension detector and invariant functionals

**Detector.** Let D=PGL₂(q), q=9 or a Fermat prime at least 5, with Borel B₀. A central C₂-extension of D that splits over B₀ and admits an involution lift of an outer involution splits over D.

Write q−1=2^k, k≥2, choose ζ generating F_q*, a=diag(ζ,1), j=[[0,1],[1,0]], and b=aj in PGL₂(q). Since q≡1 mod 4, j is inner and a and b are outer by determinant square class. P=<a,b> is Sylow dihedral of order 2(q−1). The outer involutions form one D-conjugacy class by Lemma 4.4, so b has an involutory lift b̃. A B₀-complement supplies a lift ã of a of order 2^k. Centrality gives b̃ãb̃⁻¹=ã⁻¹z^ε and (ãb̃)²=z^ε, where z generates the central kernel. But ab=a²j is a split involution: a representing matrix squares to ζ²I, so it has two distinct eigenlines over F_q. It is conjugate to a^{2^{k−1}}=diag(−1,1), whose lift in the B₀-complement is an involution. Lift squares of involutions are independent of the lift and invariant under conjugacy, so ε=0. The lifts satisfy the dihedral presentation, splitting the extension over P; odd-index restriction injectivity then gives splitting over D.

For A=∏Dᵢ, an extension by central C₂ splitting over B and admitting involution lifts for all singleton-coordinate outer involutions splits as well. Each factor restriction splits by the detector. Commutators of lifts of different factors factor through Dᵢ^ab×Dⱼ^ab, and each Bᵢ surjects onto Dᵢ^ab≅C₂ via determinant square class. A B-complement forces these cross-commutators to vanish, so the factor complements commute and multiply to an A-complement.

We claim, under the envelope hypotheses, that restriction


```math
\mathop{\mathrm{Hom}}\nolimits_A(V,\mathbf1)\longrightarrow\mathop{\mathrm{Hom}}\nolimits_B(W,\mathbf1)\tag{3}
```


is injective. If nonzero invariant λ vanishes on W, form the central C₂ pushout G/ker λ. The image of H complements the kernel over B. Moreover λδ:A→C₂ is a homomorphism vanishing on B, so it vanishes because B surjects onto A^ab. Every singleton outer-involution fiber occurs by Lemmas 4.4–4.5, and the square identity supplies an involution lift in the pushout. The product detector gives a split pushout. Its B-complement H-image is the graph of a character B→C₂, and every such character extends to A: the additive subgroup of each Bᵢ has odd order and the cyclic torus has exactly one nontrivial C₂-character, the determinant square class. Adjusting the central projection by that extension gives a homomorphism G→C₂ vanishing on H and nonzero on V. Since K generates G, it induces a nontrivial loop homomorphism X→C₂. But |X|≥[A:B]=∏(qᵢ+1)>2, contradicting simplicity. Thus (3) is injective. This argument does not assume K is G-conjugacy invariant.

## Uniform radical-dimension bound

Let m be the total number, counted with multiplicity, of nontrivial A-composition factors of V. The following bound is in terms of the *full* finite group A; it is not uniform in the number or orders of its factors:


```math
\dim V\le\bigl[1+2^e(3e+1)\bigr]|A|m.\tag{4}
```


Put A′=∏PSL₂(qᵢ), A₀=V^{A′}, and Q=V/A₀. Each PSL₂(qᵢ) is perfect. If Q had a nonzero A′-fixed vector, its preimage would be an extension of A′-trivial modules, and the induced map A′→Hom(1,A₀) would vanish by perfectness, contradicting maximality of A₀. Hence Q^{A′}=0 and its socle contains no trivial A-composition factor. Its socle has at most m simple summands. Since F₂[A] is symmetric, their injective hulls are projective indecomposable summands of the regular algebra and each has dimension at most |A|. Embedding the socle and extending into their injective direct sum embeds Q itself: any nonzero kernel would meet the socle. Thus dim Q≤|A|m.

The B-module W∩A₀ is A-invariant because A′ acts trivially on A₀ and B surjects onto A/A′. Corefreeness of H gives W∩A₀=0, so dim W≤dim Q. From (3) and the Hom long exact sequence for 0→A₀→V→Q→0,


```math
\dim\mathop{\mathrm{Hom}}\nolimits_A(A₀,\mathbf1)\le\dim W+\dim\mathop{\mathrm{Ext}}\nolimits^1_A(Q,\mathbf1)\le(3e+1)\dim Q.
```


For the last inequality, Ext¹ is H¹(A,Q*) and A has 3e generators: in each factor choose an upper unipotent of parameter 1, diag(ζ,1) with ζ primitive, and the swap matrix. Diagonal conjugation generates all upper-unipotent parameters as their primitive-scaled values span F_q over its prime field; the swap gives lower unipotents, and Gaussian elimination gives PGL₂(q). A derivation is determined by its values on these generators, giving dim H¹≤3e dim Q. This includes q=9 without an auxiliary computational input.

A/A′≅C₂^e, and its group algebra over F₂ is local of dimension 2^e. Nakayama's lemma bounds dim A₀ by 2^e dim Hom_A(A₀,1). Together these inequalities yield (4).

Finally m≥1. If m=0, then Q=0 and (3) and corefreeness give V=0. A singleton fiber in Lemma 4.5 would have size 2/(qᵢ−1), strictly between 0 and 1 for every permitted qᵢ, contradicting integrality. The bounds do not limit e, the qᵢ, m, or non-elementary radicals, and do not classify affine radical sections or the resulting loops.

## Independent reviews

reviewers contributor 1 and contributor 2 independently accepted this manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/b88cd1d25a469cc06277febc9f20725ed68934f4), conditional on the stated Baumeister–Stein Bruck-envelope, full-support fiber and Sylow cohomology inputs. Both checked the nonsplit derivation and product intermediate-subgroup argument, forced affine orbit and joint-support capacity bounds, the dihedral central-extension detector including q=9, cross-factor commutators and the functional injection. Their reviews checked perfectness in the fixed-space quotient, injective hulls without an absolute-irreducibility assumption, the explicit three generators per factor, the Hom/Ext estimate, Nakayama bound and m≥1 integrality argument. No loop classification, bound on e, qᵢ or m, efficient enumeration, non-elementary-radical extension, or formal/computational verification is asserted by these reviews.
