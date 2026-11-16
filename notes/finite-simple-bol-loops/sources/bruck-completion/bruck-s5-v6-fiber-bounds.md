# Transposition-fiber bounds for the V₆ principal block

**Scoped independent review of necessary conditions recorded below.** This manuscript continues [C0010](../../claims/0010.md), allocates no new claim ID, and assumes the faithful simple exponent-two Bruck-envelope hypotheses used in [the radical analysis](bruck-s5-radical.md): V=O₂(G) is elementary abelian, G/V≅S₅, W=H∩V, and the image of K in S₅ is the identity together with the transposition class. Suppose the principal block is X=V₆ and the remaining block is Y≅Nᵃ⊕Uᵇ, with U=N⊗F₂C₂ and a,b≥0. The N-block decomposition, projectivity of U and H²(S₅,Y)=0 were independently reviewed at the recorded source revision; see [the N-block manuscript](bruck-s5-module-blocks.md). The calculation below has the scoped independent review recorded below. It gives necessary conditions only and does not assert the existence or classification of an envelope or loop.

Let P≅C₅ in F₂₀=N_{S₅}(P). The [P-fixed feasibility calculation](bruck-s5-principal-stabilizer-fixed.md), with its complete four-model subspace enumeration independently reviewed at the recorded source revision, gives W₀=W^P=X^P, of dimension 2, and Y^P=0. The P-idempotent splits W=W₀⊕W₁ with W₁=[P,W]. Since P acts semisimply in characteristic 2 and its only nontrivial irreducible F₂-module has dimension 4, dim W₁=4c for some integer c≥0. Write d=dim V, w=dim W, and r=rank(1+t|V) for a transposition t. Then


```math
d=6+4a+8b,\quad w=2+4c,\quad r=3+a+4b.
```


The ranks are 3 on V₆, 1 on the natural even-weight module N, and 4 on U. The U rank follows since a transposition acts freely on the regular sign factor, so 1+t has rank half of dim U.

## Two independent capacity inequalities

The fiber over any transposition has size κ=2^{d−w−1}, by the cited envelope fiber count; see [Baumeister–Stein, arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Lemma 4.5, and [the arbitrary-N J* argument](bruck-s5-jdual-arbitrary-n.md). It is a nonempty union of V-conjugacy orbits of involution lifts, each of size 2ʳ, since conjugation by V changes a lift by (1+t)V. Hence κ≥2ʳ, or r≤d−w−1.

If one involution lift exists, all involution lifts over t solve an affine equation with translation kernel C_V(t); therefore their total number is 2^{d−r}. The K fiber is a subset of these lifts, so κ≤2^{d−r}, or r≤w+1. Substituting the displayed values gives


```math
a+4b\le 4c\le 3a+4b,\qquad
q:=\frac{\kappa}{2^r}=2^{3a+4b-4c}\le 2^{2a}.
```


In particular Y=N (a=1,b=0) is impossible for every integer c, since 1≤4c≤3 has no solution. This does not depend on a separate classification of W₁.

## The centralizer action on orbit labels

The involution-lift V-orbits over t form an affine torsor for H¹(T,V), where T=⟨t⟩. On X, dim ker(1+t)=dim im(1+t)=3, so H¹(T,X)=0. On N the cohomology has dimension 2, and U is free on restriction to T, so H¹(T,U)=0. Thus H¹(T,V)≅H¹(T,N)ᵃ has 2^{2a} elements.

The cohomology vanishing H²(S₅,Y)=0 allows the Y-component of the group extension to be chosen split. An involution lift of t exists. Its image in the X-extension is an involution, and combining that image with zero in the split Y-component gives an involution lift with Y-coordinate zero. This provides an origin without assuming that every Y-cocycle is a coboundary. For each g∈C_{S₅}(t), choose a lift with Y-coordinate zero. Its conjugate of the chosen t-lift is another involution lift with Y-coordinate zero, hence in the same V-orbit because H¹(T,X)=0. Changing a lift by an element of V changes its action on orbit labels only by a T-coboundary. Consequently the zero label is fixed by the centralizer and its action on labels is the linear action on H¹(T,Y); it factors through C_{S₅}(t)/T≅S₃. This is an action on involution-lift orbits, not a quotient-loop assertion.

In the natural five-point model, t swaps two coordinates. For N, the quotient ker(1+t)/im(1+t) identifies with the even-sum subspace of the remaining three coordinates. S₃ permutes them and acts transitively on the three nonzero vectors. On the diagonal a-fold power, the zero tuple is the unique fixed point; any other tuple has orbit size 3 if all its nonzero entries agree and orbit size 6 otherwise. Since K is conjugation-invariant, its q selected V-orbits form a union of these S₃-orbits. Thus q≡0 or 1 modulo 3. The exponent 3a+4b−4c has the parity of a, and q is a positive power of 2; if a were odd then q≡2 modulo 3. Therefore **a is even**.

If a=0, the two inequalities force c=b and q=1. The sole label is selected, so K contains every involution lift over every transposition. These conditions remain necessary, not sufficient: neither W nor a compatible K has been constructed.

## A separate nonsplit generation requirement

In the nonsplit extension of S₅ by X=V₆, the independently reviewed [dimension-six certificate](bruck-s5-radical.md#degree-two-cohomology-calculation) at exact revision the recorded source revision constructs an index-two subgroup L with L∩X=J and checks that it contains all involution lifts above transpositions. Conditional on that certificate and its identification with the projected extension G/Y, the image of every transposition element of K lies in L. Because K generates G, its image generates G/Y. Hence, in this nonsplit case, the projection of D=K∩V to X must meet X\J. This uses generation of an image and does not claim that the projected K is a transversal or defines a quotient loop. It is a further necessary condition, not a proof that such D is impossible.

## Independent review

an independent check accepted this manuscript at exact source the recorded source revision, conditional on the pinned envelope, module-block and finite-certificate inputs. The review checked both fiber-capacity inequalities, the bound on q, the affine-origin construction even for a nonsplit X-extension, the linear S₃ action and even-a consequence, full fiber when a=0, and the necessary projection outside J for generation. It does not assert existence of a compatible radical section or a quotient loop. The same review checked that the principal-block reduction to J or V₆ in the fixed-stabilizer manuscript correctly assembles the previously reviewed exclusions.

