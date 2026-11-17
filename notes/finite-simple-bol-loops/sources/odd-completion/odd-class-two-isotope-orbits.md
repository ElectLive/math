# Isotope orbits for odd class-two-derived folders

**Mira Cult**

**Independently reviewed deductions for [0323:C0010](../../claims/0010.md).** Let Q be a finite simple nonassociative odd left Bol loop whose canonical group G has nilpotent derived subgroup D=G′ with every Sylow factor of class at most two. The construction, exhaustion and strict isomorphism criterion in [the class-two-derived classification](odd-class-two-classification.md) have three scoped independent acceptances at [the source revision](https://github.com/Mira-Cult/math-wip/commit/226a8dc1eb503026c350ffe3b7ac93da9077a593). The [rigid-center simple proper example](odd-rigid-center-nongloop.md) is used at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/88214700dc527d238d5754029711752495c9a292), with the independent reviews recorded there. The arbitrary-principal-isotope interface has scoped independent acceptance at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ea836a5f328d6bc52913aac8fd1841a87072f5f8). The new deductions have two separate exact-source acceptances recorded below.

## Every isotope is a negative-central shift

Let a selected class-two normal-form datum have positive crossed cocycle $`f:A\to Z=Z(D)`$, center involution σ, center action T, and $`Z^-=\{z:\sigma z=-z\}`$. The reviewed exhaustion proof gives $`G=DH`$ and the product-set factorization

```math
D=C_D(\tau)\,Z^-\,S,\qquad S=H\cap D.\tag{1}
```

For every $`z\in Z^-`$, put

```math
f_z(a)=f(a)+(1-T(a))z.\tag{2}
```

Each $`f_z`$ is a crossed cocycle satisfying the same positive-fiber condition, and its folder is $`(G,zHz^{-1},K)`$. It is selected and simple: the full marked-transversal condition, core-freeness and generation are invariant under stabilizer conjugation, and for every normal subgroup N its defect depends on $`|H\cap N|`$, which is unchanged by conjugation.

Every loop isotope is isomorphic to a principal isotope, and the cited isotope interface identifies its transported canonical folder with $`(G,gHg^{-1},K)`$ for some $`g\in G`$. Write $`g=dh`$, $`d\in D,h\in H`$, so $`gHg^{-1}=dHd^{-1}`$. Decompose d as in (1). Conjugation by $`C_D(\tau)`$ preserves τ and K, while S normalizes H; hence the shifted folder is genuinely isomorphic to $`(G,zHz^{-1},K)`$ for some $`z\in Z^-`$. No G-loop assumption is made. Therefore every isotopy class has at most $`|Z^-|`$ loop-isomorphism classes.

The exact identification of these representatives is the reviewed **strict** isomorphism criterion of the class-two theorem: $`f_z\sim f_w`$ if and only if permitted Lie-ring and torus isomorphisms preserving the bracket, σ, actions and W transport $`f_z`$ exactly to $`f_w`$. In a simple odd folder the map from $`Z^-`$ to cocycle differences is injective: if $`(1-T(a))z=0`$ for all a, then z centralizes D and A, so z is central in G; the reviewed odd-center theorem says τ fixes $`Z(G)`$, while τ inverts z, forcing z=1. The cocycles are therefore distinct, though strict data automorphisms may still identify their loops.

## The rigid-center example has exactly three classes

In the cited rigid example,

```math
Z_p=\mathbb F_3[\epsilon]/(\epsilon^3),\quad T(a)=1+\epsilon,\quad
\sigma(\epsilon)=-\epsilon+\epsilon^2,\quad
Z_p^-=\mathbb F_3(\epsilon+\epsilon^2).
```

There is no q-negative center. Its three shifts are

```math
f_k(a)=f(a)-k\epsilon^2\qquad(k\in\mathbb F_3).\tag{3}
```

The general bound gives at most three classes, all in the same isotopy class.

Suppose strict data equivalence identifies $`f_i`$ with $`f_j`$, $`i\ne j`$. The 19-side action is scalar by an element of order 9 over the prime field $`\mathbb F_{19}`$; the intertwining equation forces the $`C_9`$ torus automorphism to be the identity. The p-center map then commutes with T and σ, and transports $`f_i(a)`$ to $`f_j(a)`$. The centralizer of the one-block T is $`\mathbb F_3[T]`$; commuting with σ removes its linear $`T-1`$ term. The constant coefficient of $`f_i(a)`$ forces the scalar term to be one, and the transport equation forces a nonzero shear

```math
M=1+(i-j)\epsilon^2,\tag{4}
```

up to the harmless reversal of the direction of the isomorphism. In characteristic 3, one of M and $`M^2`$ is $`1-\epsilon^2`$. The assumed equivalence is an automorphism of the underlying $`(G,\tau)`$ data preserving the bimap and torus action, so its square is also such an automorphism, regardless of its possible 19-torus/Frobenius component.

The cited rigid-bimap proof excludes the latter shear. The p-W map is semilinear over $`E=\mathbb F_{3^{18}}`$ because the 19-scalar generates E. Remove its Frobenius part using the $`\mathbb F_3`$-defined bimap matrices and trace invariance. The remaining invertible E-linear map would carry $`B_2`$ by congruence to $`B_2-B_0`$, but the cited matrices have

```math
\det(B_2-B_2^T)=1,\qquad
\det((B_2-B_0)-(B_2-B_0)^T)=0\quad\text{in }\mathbb F_3.
```

Congruence preserves skew rank over E, a contradiction. Thus all three shifts in (3) are pairwise nonisomorphic. The full isotopy class of the cited simple proper loop has **exactly three isomorphism classes**, under the pinned inputs.

## Rank-one positive center

Fix a prime p dividing $`D`$. Write $`Z_p=Z(P_p)`$, let $`A_p`$ be the p-primary part of $`A=G/D`$, and let σ and T be the induced center involution and action. If

```math
|A_p|=|Z_p^+|=p,\tag{5}
```

then $`Z_p\le Z(G)`$ and $`P_p`$ is extraspecial of exponent p. This is a consequence of the class-two normal form.

For $`t\in A_p`$, put $`Z_p^-(t)=\ker(\sigma+T(t)^{-1})`$. Since A has odd order, $`T(t)\sigma`$ is conjugate to σ by a square root of $`T(t)`$; hence $`|Z_p^-(t)|=|Z_p^-|`$. Both subgroups have index p in $`Z_p`$. Apply the reviewed quadratic transversal test with torus labels $`a=1,c=t`$ and vector variable zero. At every other prime j the cocycle value $`f_j(t)`$ is zero: the p-group $`A_p`$ acts trivially on the coprime center $`Z_j`$, and its cocycle there is a homomorphism to a group of coprime order. Thus, for each nonidentity t, the p-coordinate requires

```math
f_p(t)\notin Z_p^-+Z_p^-(t).\tag{6}
```

Distinct index-p subgroups of a finite abelian p-group sum to the whole group, so (6) forces $`Z_p^-(t)=Z_p^-`$. Its defining equation shows that $`T(t)`$ fixes $`Z_p^-`$ pointwise. The coprime torus already fixes all of $`Z_p`$, so $`Z_p^-`$ is central in G. The odd-center theorem fixes it pointwise under τ, whereas it is τ-inverted; oddness gives $`Z_p^-=1`$. Hence σ is trivial on $`Z_p`$, and $`\sigma T(t)\sigma=T(t)^{-1}`$ plus oddness makes the full A-action on $`Z_p`$ trivial. This proves centrality and $`|Z_p|=p`$.

The commutator pairing $`U_p=P_p/Z_p`$ into $`C_p`$ has zero radical, so $`pU_p=0`$. Coprime B-averaging in the reviewed normal form splits the additive BCH group of $`P_p`$ as $`Z_p\oplus U_p`$; consequently $`P_p`$ has exponent p. The class-two theorem gives $`P_p'=Z_p`$, and the zero-radical pairing makes $`P_p/Z_p`$ elementary abelian, so $`P_p`$ is extraspecial.

As a corollary, if $`G/G'`$ is squarefree, every prime p of D has $`|A_p|=p`$ because |A_p|=1 would give σ=−1 on Z_p; the relation σTσ=T⁻¹ and oddness then make T trivial, creating a forbidden nontrivial central τ-inverted subgroup. All Sylow factors of D are then extraspecial, and the [extraspecial-derived classification](odd-extraspecial-classification.md), independently accepted at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dce010e03e56d50af4fbfbb4aba69806228ec518), makes Q a G-loop. Alternatively, the [central class-two theorem](odd-central-class-two-classification.md), independently accepted at [the source revision](https://github.com/Mira-Cult/math-wip/commit/598fa119be327480c829af2a9beb709b02886bc4), supplies the G-loop conclusion after the same centrality result. This does not assert that the abelianization is always squarefree; the rigid-center counterexample has a larger p-primary factor.

No computation, formal verification or literature-novelty claim is used in the new deductions. At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/7530ae6eeeb0614d7c94ed6ab1f6761f3493ab88), reviewers contributor 1 and contributor 2 independently accepted the entire manuscript under its cited inputs. Both checked the reduction of every actual isotope to a negative-central shift, the strict orbit criterion and exact three-class result despite possible torus/Frobenius components, and the arbitrary-exponent rank-one center and extraspecial/squarefree consequences. These are separate reviews of the new deductions, not an inference from the earlier source acceptances.
