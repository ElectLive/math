# All inversions for the odd-field affine square

**Independently reviewed extension of [0323:C0010](../foundations/research-C0010.md).** For every odd prime power q≥5, every finite simple proper left Bol loop whose canonical left multiplication group is abstractly ASL₂(q)² belongs to the [root-graph classification](../odd-completion/nonbruck-root-graph-parameters.md). No inversion or stabilizer type is prescribed. The converse and isomorphism criterion are those of the [paired affine theorem](paired-affine-swap-exhaustion.md), independently reviewed at `e8644c4779fe3ad9cc03c69f97d2ac8071a95a05`, conditional on its pinned canonical-folder, construction and isomorphism inputs. The field has odd characteristic, although the loops in the theorem have even order.

Put k=F_q, p=char k, V=k², A=SL₂(q) and X=V⋊A. If q is a square, σ denotes the field involution and k₀ its fixed field. The new obligation is to rule out factor-preserving canonical inversion.

## Structure of Aut(X)

The A-module V is irreducible even over F_p: if 0≠(x,y) lies in an invariant additive subgroup W, applying u(t)−1 and l(t)−1, where u(t)=I+tE₁₂ and l(t)=I+tE₂₁, yields a nonzero coordinate vector and then all scalar multiples of both coordinate vectors. Hence V is a minimal normal subgroup of X. If N is a nontrivial normal subgroup of X disjoint from V then [N,V]=1; however C_X(V)=V because A acts faithfully, a contradiction. Every nontrivial normal subgroup contains V, so V is the unique minimal normal subgroup and is characteristic. Also Z(X)=1, and X is directly indecomposable.

An explicit centralizer computation gives End_A(V)=k. An F_p-linear map T commuting with all u(t), l(t) has block form T(x,y)=(a(x)+b(y),c(x)+d(y)) with F_p-linear a,b,c,d:k→k. Commutation with u(1), l(1) yields b=c=0 and a=d; commutation with u(t) yields a(ty)=t a(y) for all t,y, so a is multiplication by a scalar. Thus the algebra centralizer is exactly the scalar copy of k. Any F_p-linear normalizer of A normalizes this algebra, and conjugation induces a field automorphism of k; after removing that field automorphism, the normalizer is k-linear. Conversely GL₂(k) and the field automorphisms normalize SL₂(k). Hence N_{GL(V as F_p-space)}(A)=ΓL₂(k).

Let α∈Aut(X). Its restriction T to V is F_p-linear. If α sends a∈A to a translation times φ(a)∈A, then T a T⁻¹=φ(a), so T∈ΓL₂(k). The latter induces a standard automorphism of X. After removing it, α fixes V pointwise and induces the identity on A, hence has form α(a)=d(a)a for a 1-cocycle d:A→V, d(ab)=d(a)+a d(b). With z=−I central in A, d(z)+z d(a)=d(a)+a d(z), giving 2d(a)=(I−a)d(z). Thus d(a)=(I−a)v for v=d(z)/2 and α is conjugation by translation v. Therefore

Aut(X) = V ⋊ ΓL₂(k),

with the natural semilinear action; this identification is faithful. The embedded inner automorphism group X is V⋊SL₂(k).

## Involutions

Let an automorphism be (v,T), T∈ΓL₂(k). It squares to 1 iff T²=1 and v+Tv=0. Since p is odd, v=(I−T)(v/2); conjugating by a translation removes v. If T is k-linear, its minimal polynomial divides (t−1)(t+1), and it is GL₂(k)-conjugate to I, −I, or diag(1,−1). Here I represents the identity, while the latter two represent the nontrivial linear involutions.

If T has nontrivial field part, its field part must be σ, so f is even and T=gσ, g∈GL₂(k), with gσ(g)=I. Choose η∈k× with σ(η)=−η. Over k₀ the involution T has plus and minus eigenspaces, and multiplication by η interchanges them. A k₀-basis of the plus space is therefore a k-basis of V, in which T is σ. In particular g=hσ(h)⁻¹ for a change of basis h∈GL₂(k). Thus, under Aut(X)-conjugacy, the full list of elements of order dividing two is identity, −I, diag(1,−1), and, when f is even, σ. The four representatives are distinct: identity and field part are immediate invariants, and the two linear involutions have different dimensions of their (−1)-eigenspaces. This statement is about Aut(X)-conjugacy; it must not be confused with X-conjugacy of arbitrary semilinear involutions.

For the narrower coset Xσ, all involutions form one X-conjugacy class. Indeed, if x=(v,g)∈X and (xσ)²=1, then gσ(g)=I and v+gσ(v)=0. The preceding basis construction gives g=hσ(h)⁻¹ for some h∈GL₂(k). Taking determinants and using det g=1 gives det h∈k₀×. Multiplying h on the right by diag((det h)⁻¹,1)∈GL₂(k₀) makes h lie in SL₂(k) without changing hσ(h)⁻¹. Now B=gσ is an involution on V and v+ Bv=0; conjugating gσ by the translation v/2 adds v. Therefore xσ is X-conjugate to σ. This determinant adjustment is the required SL₂ descent, rather than an assumption that arbitrary GL₂ conjugators already have determinant one.

The centralizer C_X(σ) consists precisely of σ-fixed translations and σ-fixed matrices in SL₂(k); thus C_X(σ)=k₀²⋊SL₂(k₀)=ASL₂(k₀), of order |C_X(σ)|=s³(s²−1) for s=sqrt(q). Consequently the number of involutions in Xσ is |X|/|C_X(σ)|. This count applies to Xσ, not all field-type involutions in Aut(X).

## Direct squares

Every automorphism of X×X permutes the two factors. For an elementary proof, let an automorphism send the factors to commuting normal subgroups Y,Z with YZ=X×X and Y∩Z=1. For i=1,2, the projections P_i=π_i(Y), Q_i=π_i(Z) are commuting normal subgroups with P_iQ_i=X. Their intersection is central in X and hence trivial, so X=P_i×Q_i. Its direct indecomposability forces one projection to be X and the other 1. Since Y and Z are both nontrivial, each must project nontrivially on some coordinate. Thus the choices differ at i=1 and i=2. Hence Y and Z are the original factors, possibly exchanged, and Aut(X²)=Aut(X) wr S₂.

## Generating the affine factors and forcing the outside class

Suppose the canonical inversion preserves the two factors, acting by α₁,α₂ on them. Conjugating each action by a separate automorphism of X preserves the folder problem. A coordinate action cannot be inner. If α_i is induced by s then s²=1 since X is centerless. For any projection x of a translation in K, xs squares to 1 since α_i(x)=x⁻¹. In SL₂(q) each element of square one is ±I, by determinant and diagonalization in odd characteristic. The linear parts of s and xs and hence also x belong to {±I}. This prevents the projected K from generating X. This excludes the identity as well.

The remaining actions are the reflection diag(1,−1) and, for square q, the field involution σ. For reflection action identify the outside coset with the affine maps of determinant −1. Every involution there has linear part with distinct eigenvalues 1 and −1. There is one SL₂(q)-class of such matrices, since a choice of eigenvectors can be scaled to give determinant one. Its translation part is anti-fixed and is removed by a translation, since 2 is invertible. Thus there is exactly one X-class of involutions in this coset. Its representative has centralizer in X of order q(q−1), with a q-element fixed line and a determinant-one diagonal torus. For field action the determinant-adjusted descent above proves the analogous single-class assertion in Xσ.

In the simultaneous extension E=G⋊⟨t⟩, an outside element is a pair in Xα₁ × Xα₂ with both parities odd. It is an involution exactly when both coordinates are involutions. Conjugation by X×X acts independently. There is therefore exactly one outside class, with no hypothesis on class selection. The [canonical marked set](../odd-completion/elementary-two-marked-lifts.md) Λ=tK contains t and hence is the entire class. Counting |K|=[G:H] now gives

    |H| = |C_X(α₁)| |C_X(α₂)|.

Write W=H∩(V×V). In each coordinate α_i has a nonzero minus space on V, since it is a nonidentity F_p-linear involution in odd characteristic. K contains the product of these two minus spaces, by conjugating t by translations and multiplying by t (on each minus space 1−α_i is multiplication by 2). Independent SL₂(q) actions are transitive on nonzero vectors in each coordinate. Every w∈W is thus conjugate to an element of K, including when one coordinate vanishes. Transversality to every conjugate of H forces W=1. So H embeds in A² and |H|_p≤q². The reflection centralizer has p-part q, and the field centralizer has p-part q^{3/2}. Either coordinate of field type would give |H|_p>q², a contradiction.

## Product of two affine reflections

It remains to exclude two reflection actions. Write S for all affine involutions of determinant −1. We claim S²=X.

Represent affine elements as `(v,a)` with `(v,a)(w,b)=(v+aw,ab)`. To show `S²=X`, it suffices for every `g=(v,a)∈X` to find `b=(w,r)∈S` with `bgb=g⁻¹`; then `bg` is another involution of determinant −1 and `g=b(bg)`.

* If `a−I` is invertible, translate the origin to remove v. If a is nonscalar, choose a cyclic vector e, and define r by `r(e)=e`, `r(ae)=a⁻¹e`. Cayley–Hamilton gives `a⁻¹e=tr(a)e−ae`, so r is a determinant −1 involution and `rar=a⁻¹`. If a=−I, take any linear reflection. Conjugating the resulting reverser back by the translation handles v.
* If a=I, choose a reflection r with rv=−v (arbitrary when v=0), and take w=0.
* Otherwise a is nontrivial unipotent. In an F_q basis write `a=[[1,t],[0,1]]` with t≠0 and `v=(s,u)`. Take `r=diag(1,−1)` and `w=(0,u−2s/t)`. Then `(I+r)w=0`, `rar=a⁻¹`, and `(I+ra)w+rv=(−s+tu,−u)=−a⁻¹v`, so b²=1 and bgb=g⁻¹.

Since Λ is the entire product of the two classes, K⁻¹K=Λ²=S²×S²=G. Collision-freeness gives H=1, impossible by the positive centralizer orders above. This excludes both reflection actions. The factor-permutation result leaves only exchange, so the reviewed affine-swap exhaustion gives the claimed classification.

## Independent mathematical review

GPT-6.1 Terra reviewers contributor 1 and contributor 2 independently accepted the new deductions at source `bb5a92abe1c4963c1218fbea4508987a9e88c118`. Both checked the automorphism calculation for non-prime fields, the field descent and determinant adjustment, the coordinate and class arguments, the p-part obstruction and the affine reversal calculation, including its unipotent case. The reviews are conditional on the linked original-folder and paired affine inputs. Neither reviewer repeated the upstream construction and isomorphism proofs or used a finite census. The characteristic-two factor-preserving branch remains open.
