# 0038. Inversion and affine sections in elementary S₅ Bruck envelopes

*Mira Cult*

[Research programme](../README.md) · [Claim catalogue](../CLAIMS.md) · [Open problems](../OPEN_PROBLEMS.md)

## Results obtained

In the elementary-abelian-radical, S₅-quotient branch, the distinction between exponent two and exponent four has a particularly concrete form. Inversion fixes the radical pointwise, but can move a lift of a quotient element by a vector in the radical. Those displacement vectors form a relative derivation.

This article proves the resulting reduction: the derivation is represented by a homomorphism from a fixed five-dimensional module; it determines every section element's square; and it turns the radical-section problem into an **affine**, rather than necessarily linear, orbit-cover problem. The same argument gives two useful bounds on transposition ranks.

These are structural restrictions, not a classification of all Bruck loops. They explain part of the mechanism behind the broader elementary-S₅ parameterization registered under claim 0038. We separate the elementary proof here from that parameterization's additional module, extension and simplicity inputs.

## 1. Setting and imported structural facts

A right Bruck loop is a right Bol loop in which inversion is an automorphism. Its faithful Baer envelope is the triple consisting of its right multiplication group G, the stabilizer H of the identity, and the set K of right translations. Thus K generates G, contains the identity, and is a transversal to every conjugate of H. The group H is core-free.

Let X be a finite simple right Bruck loop with

```math
V=O_2(G)\text{ elementary abelian},\qquad G/V\cong S_5.
```

Write V additively as a vector space over the two-element field, and let π be the quotient map. Set W = H ∩ V and D = K ∩ V. The S₅-action on V is conjugation; it is well-defined because V is abelian.

We use the following specialized consequences of Baumeister–Stein, *The finite Bruck Loops*, Theorem 1 and Lemmas 3.2, 3.4, 4.1, 4.2 and 4.5:

1. The loop has 2-power exponent. The image F = π(H) is the order-20 Borel subgroup in the six-point action of S₅ ≅ PGL₂(5).
2. The section image consists of the identity and the transpositions, and every k in K has its square in V.
3. There is a canonical automorphism τ of G fixing H pointwise and sending k to its inverse for every k in K.
4. V = WD. The marked set τK is invariant under conjugation in the associated inversion extension.
5. If d = dim V and w = dim W, each transposition fiber of K has size 2 to the power d − w − 1.

These are the external folder-theoretic inputs; their proofs are not reproduced here. [Baumeister–Stein, arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1).

For precision in the fourth item, we always use a **formal external** involution, written τ̂, acting on G by τ. The group is G⁺ = G ⋊ ⟨τ̂⟩, even when τ is the identity automorphism. Then Λ = τ̂K is a conjugacy-invariant set of involutions. This avoids identifying an automorphism with an element of G.

## 2. Inversion is a relative derivation

**Theorem 1.** In the setting above:

- the exponent of X divides four;
- τ fixes V pointwise and induces the identity on G/V;
- there is a well-defined derivation δ from S₅ to V, vanishing on F, such that

```math
\tau(g)=\delta(\pi(g))g,
\qquad
\delta(xy)=\delta(x)+x\delta(y);
```

- every section element satisfies

```math
k^2=\delta(\pi(k)).
```

The exponent is two exactly when δ is zero.

**Proof.** Every element of D is an involution or the identity because V is elementary abelian. Inversion therefore fixes D. It fixes W because W is contained in H. Since V = WD, it fixes V pointwise.

The image of every section element in S₅ is an involution or the identity. Since τ inverts K, it fixes its image in the quotient. That image generates the quotient, so τ induces the identity there. Finally, the square of every section element lies in the elementary abelian group V, hence its fourth power is the identity. Powers in a Bol loop agree with the corresponding powers of its translations; the exponent of X therefore divides four.

Define

```math
\delta(gV)=\tau(g)g^{-1}.
```

The value belongs to V. Replacing g by vg, for v in V, does not change it: τ fixes v, and the two resulting V-elements commute. Thus δ is well-defined.

For x = gV and y = hV, direct multiplication gives

```math
\tau(gh)(gh)^{-1}
=\delta(x)g\delta(y)g^{-1}
=\delta(x)+x\delta(y).
```

The map vanishes on F because every element of F lifts to H. For k in K, its value is k to the power −2, which equals its square because k has order dividing four. This proves the square formula.

If δ vanishes, τ fixes G and every element of K is an involution or the identity. Conversely, if the loop has exponent two, τ fixes the generating set K and hence all of G. ∎

An important consequence is that **all section elements above a given transposition have the same square**. Their possible order-four behavior is not an independent choice in each radical fiber.

**Converse at the group level.** Suppose an extension of S₅ by V and a subgroup H above F have already been fixed. Any derivation δ vanishing on F defines an automorphism

```math
g\longmapsto\delta(\pi(g))g.
```

The derivation identity proves multiplicativity. The map fixes V and H; applying it twice adds δ twice, so its square is the identity. This works for nonsplit group extensions as well.

This converse constructs an automorphism, **not a Bruck loop**. A compatible section still has to exist.

## 3. A fixed five-dimensional parameter module

Let P be the permutation module on the six cosets of F and E its augmentation submodule:

```math
P=\mathbb F_2[S_5/F],
\qquad
E=\ker\!\left(P\longrightarrow\mathbb F_2\right).
```

Thus E consists of the even sums of cosets and has dimension five.

**Theorem 2.** There is a natural vector-space isomorphism

```math
\{\delta\in Z^1(S_5,V):\delta|_F=0\}
\cong
\mathrm{Hom}_{S_5}(E,V).
```

Under this correspondence a module map f gives

```math
\delta_f(g)=f(gF+F).
```

**Proof.** Given δ, define a linear map L on P by L(gF) = δ(g). This is well-defined: δ(gh) = δ(g) for h in F. For a vector v in P and an element x of S₅,

```math
L(xv)=xL(v)+\varepsilon(v)\delta(x),
```

where ε is the augmentation. On E the last term vanishes, so f = L restricted to E is equivariant.

Conversely, an equivariant f gives a derivation because

```math
xyF+F=x(yF+F)+(xF+F).
```

It vanishes on F. These constructions are inverse: δ(1) = 0, and the vectors gF + F span E. ∎

This is a concrete linear-algebra replacement for searching over arbitrary inversion automorphisms. Once the module V is given by matrices, the possible f are the solutions of intertwining equations.

The theorem does not require a classification of S₅-modules or any assertion about the submodule lattice of E. In particular, it does not depend on the additional principal-block calculations used in the larger parameterization.

## 4. The radical section is an affine exact cover

**Theorem 3.** The set D is a transversal to W in V and is a union of orbits of the affine action

```math
x\ast v=xv+\delta(x)
\qquad(x\in S_5,\ v\in V).
```

It contains the orbit δ(S₅) of zero. If δ is nonzero, this orbit has six elements.

**Proof.** The derivation identity proves that the displayed formula is a group action. Transversality of K to H and the factorization V = WD show that D meets each coset of W exactly once.

Because τ fixes V, conjugation by a lift g of x sends τ̂v to

```math
g(\hat\tau v)g^{-1}
=\hat\tau\bigl(\delta(x)+xv\bigr).
```

Conjugacy invariance of Λ therefore makes D affine-invariant. It contains zero, hence the whole orbit δ(S₅).

The zero set of a derivation is a subgroup, here containing F. The subgroup F is maximal in S₅: its index is six, and a proper intermediate subgroup would have order 40 or 60; order 40 is impossible by the Sylow-5 count and the order-20 normalizer of a Sylow-5 subgroup, while the unique index-two subgroup A₅ does not contain F. Thus a nonzero δ has zero set exactly F. Orbit-stabilizer gives six points. ∎

Here is the precise residual selection problem. For each affine orbit O in V introduce a binary variable z indexed by O. Require the variable of the orbit of zero to equal one and impose, for every coset v + W,

```math
\sum_O |O\cap(v+W)|z_O=1.
```

Solutions are exactly the permitted affine-invariant transversals D. This is a finite exact-cover system, not a claim of efficient solvability. An orbit meeting one W-coset twice can never be selected; in particular the forced zero orbit must itself be collision-free.

For exponent two, δ is zero and these are ordinary linear-action orbits. For exponent four, replacing them by linear orbits would discard the inversion twist and change the problem.

## 5. Capacity bounds in the outer fibers

Fix a transposition t. Let r be the rank of 1 + t on V, and retain d = dim V and w = dim W.

**Theorem 4.** One has

```math
r\le d-w-1,
\qquad
r\le w+1.
```

**Proof.** The fiber K above t is nonempty and has the size given in Section 1. The marked-set invariance and the fact that τ̂ centralizes V imply that K is invariant under conjugation by V. Each V-conjugacy orbit above t has size

```math
|V:C_V(t)|=2^r.
```

An orbit must fit inside the fiber, giving the first inequality.

Choose a lift k in that fiber. Every other lift of t is vk for some v in V, and

```math
(vk)^2=v+tv+k^2.
```

All selected lifts have the same square by Theorem 1. Consequently their v-values lie in the kernel of 1 + t, a space of dimension d − r. The fiber has at most that many elements. Comparing its size with 2 to the power d − r gives the second inequality. ∎

The point is that neither bound assumes exponent two. They remain available when the selected lifts have order four.

## 6. What this contributes to classification

The reduction replaces part of an unstructured section search by three finite objects:

1. an S₅-module V and a stabilizer intersection W;
2. a module map from the fixed five-dimensional E to V;
3. an affine orbit exact cover on V, followed by compatible outer-fiber choices.

It applies without splitting the extension of S₅ by V. It also makes explicit why solving only the exponent-two case does not settle the elementary-radical branch.

The [structural parameterization source](../update-2026-11-16/manuscripts/bruck-s5-elementary-parameterization.md) adds active-module bounds, extension cocycles, stabilizer complements, marked conjugacy classes, generation, simplicity and isomorphism tests. Those additions use further module/cohomology and normal-subloop results. This article does not reprove or certify that entire dependency chain.

In particular, no conclusion here bounds the radical dimension, proves existence for every module parameter, solves all exact covers, or establishes efficient duplicate-free enumeration. Other quotient groups and non-elementary radicals remain outside the stated scope.

## 7. Open problems within this reduction

- **Admissible inversion maps.** For a specified V and W, characterize which module maps E → V admit an affine-invariant transversal to W containing zero. The necessary forced-orbit collision test is explicit; when is it sufficient?
- **Completing the section.** Given such a radical transversal and a specified group extension and stabilizer, determine which outer fibers complete it to a generating Bruck section whose loop is simple.
- **Separating exponent-four cases.** Determine the isomorphism classes of the resulting data with nonzero δ, accounting for simultaneous transport of the extension, stabilizer and section. Counting derivations alone does not count loops.

## Sources and scope of checking

The elementary arguments above reorganize the corresponding portions of [Inversion and linear support for elementary S₅ Bruck envelopes](../update-2026-11-16/manuscripts/bruck-s5-elementary-inversion.md). That source additionally discusses invariant functionals and module-support bounds; those arguments are deliberately not incorporated without their additional inputs.

The external facts listed in Section 1 were cross-checked against the indicated statements in Baumeister–Stein. The proofs in Sections 2–5 were checked against the source and expanded to expose their group-action and counting steps. This is a research exposition, not a claim of formal verification or independent human referee acceptance. No claim of literature priority is made.
