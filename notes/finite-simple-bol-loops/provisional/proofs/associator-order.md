# Unbounded order of one associator in finite simple Bol loops of exponent six

**Mira Cult · Provisional research.** Author proof, not independently reviewed.

The construction uses the native nonlinear-cut argument of the [fixed-exponent radical family](radical-class.md), which likewise awaits independent review. It addresses the permutation order of a single associator, not merely the size of the translation group.

**Theorem.** For every $`a\ge1`$ there is a finite simple non-Moufang left Bol loop $`Q`$ of exponent six with two **order-two** points $`h,k`$ such that $`hk`$ has order three but the single left-inner permutation

```math
L_{hk}^{-1}L_hL_k
```

has order **exactly $`3^a`$**. The product $`L_hL_k`$ also has order $`3^a`$. Thus these two genuine involutory left translations generate a dihedral subgroup of order $`2\cdot3^a`$. In particular even the order of one associator is not bounded by the loop exponent, the simple quotient $`\mathrm{PSL}_2(19)`$ of its left group, or the derived length two of its radical.

More precisely take any $`N\ge2`$ prime to three and let $`a`$ be the least integer with $`3^a>N`$. The host has order $`20\cdot3^{117+20N}`$ and left group $`P\rtimes\mathrm{PSL}_2(19)`$, where the **whole** solvable radical $`P`$ is a metabelian $`3`$-group of nilpotency class exactly $`N`$ and exponent exactly $`3^a`$. One can take $`N=2`$ for $`a=1`$ and $`N=3^{a-1}+1`$ otherwise. The initial squarefree construction instead kept the radical exponent fixed at 9 for unbounded class; neither result implies the other formally.

## Replace squarefree slots by actual principal units of growing order

Keep $`T,B,w,X_0,Y_0,f_0,d,M,K`$ and the one bottom shear $`\alpha:M\to Y_0`$ from the cited proof. Thus $`K`$ is the algebra of functions on the twenty projective sites, $`M`$ its sum-zero space, and $`K/\mathbb F_3\mathbf1\simeq M`$. Let $`I`$ be the nonunital algebra with coefficients in degrees $`1,\ldots,N`$ of the truncated ring $`K[t]/(t^{N+1})`$, restricting the degree-one coefficient to $`M`$ and taking degree $`N`$ **modulo constants**. It is an associative subquotient and has dimension $`20N-2`$. Let $`B_1=1+I`$ be its full abelian principal-unit group, acting on $`I`$ by multiplication. Its order-three behavior is no longer that of squarefree monomials.

Here is an explicit equivariant homomorphic coordinate for the bottom shear. First use the unrestricted algebra $`tK[t]/t^{N+1}`$ at every site. For each $`1\le j\le N`$ prime to three set $`a_j=\#\{d\ge0:j3^d\le N\}`$. Independently at each site $`s`$, the units $`1+e_s t^j`$ generate cyclic groups of order exactly $`3^{a_j}`$. They give a direct product of the full unit group: in the base-three expansion of the exponent of this generator, the digit in position $`d`$ supplies the independent leading coefficient at $`t^{j3^d}`$, since $`(1+e_s t^j)^{3^d}=1+e_s t^{j3^d}`$. Successively recover digits in increasing ordinary degree. This proves uniqueness, generation and equivariance under genuine site permutations. Coefficients at high ordinary degrees are **not** in general the additive digits just defined. Restricting degree one to sum zero affects only the residues modulo three of the $`j=1`$ site exponents. Quotienting by the degree-$`N`$ constant subspace affects only the top $`j=N`$ vector, since $`3\nmid N`$. In particular $`B_1`$ has a genuine $`T`$-equivariant group projection to the top summand $`M`$.

Let $`A\le B_1`$ instead use, for every $`j<N`$ with $`3\nmid j`$, the sum-zero subgroup of $`(\mathbb Z/3^{a_j})^{20}`$ on the entire exponents at that primitive degree. Use the whole top $`M`$ for $`j=N`$. Each augmented module over $`\mathbb Z/3^{a_j}`$ has zero coinvariants for $`T`$: the full permutation module splits as constants and augmentation since 20 is a unit; transitivity identifies its coinvariants with the coefficient ring, and the constant summand maps isomorphically onto them by multiplication by 20. Thus $`A_T=0`$. The quotient $`B_1/A`$ has trivial $`T`$-action: before the degree-one restriction these are precisely sum-coordinate quotients, and the actual permitted degree-one sum is simply restricted modulo three. Equivalently every difference $`b-i b`$ in additive unit coordinates belongs to $`A`$. Write $`c_*`$ for the real projection of $`A`$ on its top $`M`$ summand.

For a projective involution $`i`$, the odd abelian group $`B_1`$ splits into plus and minus parts. Its minus subgroup is already in $`A`$, and $`|C_{B_1}(i)|=|C_I(i)|`$ under $`1+v\leftrightarrow v`$ because $`i`$ acts by algebra automorphisms. Consequently

```math
|A_i^-|=|(B_1)_i^-|=|I_i^-|.                      \tag{1}
```

This exact equality, not a vector-space dimension for $`A`$, keeps every reflected sheet cardinality unchanged relative to the abelian base. For future use, $`A`$ contains the actual degree-one units $`(1+e_s t)/(1+e_b t)`$ for $`s\ne b`$. Their leading differences are $`e_s-e_b`$. Multiplying any nonzero coefficient in degree $`d<N`$ by $`N-d`$ such differences supported at its chosen nonzero site and one other gives a nonzero top vector modulo constants. The intervening higher terms cannot affect that top coefficient. Also $`[A,I]=I_{\ge2}`$: the leading differences at degree two span $`K`$ since $`(e_s-e_b)(e_s-e_c)=e_s`$ for distinct $`s,b,c`$; at further degrees the same argument spans every requisite coefficient. This proves equality by descending induction on the finite degree filtration, including when $`N=2`$ and the top is already projected. It proves as well that the annihilator of $`I`$ is its top and that nonzero $`A`$-invariant subspaces with a lower degree term meet the top nontrivially.

## Why the original signed folder and all normal cuts still work

Take $`X=X_0\oplus A`$, $`Y=Y_0\oplus I`$, $`P=Y\rtimes X`$ by the actions above, sign $`z`$ acting as $`+1,-1`$. Keep the cocycle $`D(x_0,s)=(f_0(x_0)+\alpha(c_*(s)),s-1)`$ and its abelian graph $`W`$, making $`H`$ by adjoining the true $`B`$-lifts with cocycle $`d`$. The same identity $`ss'-1=(s-1)+s(s'-1)`$ makes $`W`$ an actual subgroup; the base-coordinate shear is additive even when $`s`$ has large order. Symmetric coordinates $`s(x/2)\iota(y)s(x/2)`$ are meaningful in **any odd abelian** $`X`$. Their inverses are $`[-x,-y]`$, giving exactly $`Y`$ and $`[X_i^-,Y_i^+]i`$ as the actual section sheets, of the required sizes by (1).

For vertical avoidance a nonzero leading term of $`s-1`$ and the identical leading term of $`D`$ are acted on by $`(i,-i)`$ modulo the next ordinary degree. Every inner conjugation by $`P`$ vanishes on that grade. So inversion by a genuine conjugate sign is impossible. If $`s=1`$ the old vertical avoidance applies. For nonvertical avoidance project away ring $`Y`$ and **also the direct factors of $`A`$ other than its actual top coordinate**. This is an ordinary group homomorphism, and the image stabilizer in $`X_0\oplus M\oplus Y_0`$ is the graph $`(x,c)\mapsto f_0(x)+\alpha(c)`$ with the original derivation. Thus the nonzero $`r^3,zw`$ compression from the preceding proof works literally in an elementary abelian group at this step. This is not an attempt to apply an $`\mathbb F_3`$-linear test to all of $`A`$. The cardinality and conjugacy of signs then give a sharp Bol section on $`G/H`$.

In a putatively flat normal cut $`R\lhd G`$ inside $`P`$ use $`U=R\cap Y`$, $`J=\pi_X R`$. As in the predecessor's §5 the saturated base coset gives $`R=U(R\cap W)`$. The residual graph $`R/U`$ in $`P/U`$ is central, so its map $`\bar D:J\to Y/U`$ is additive, $`T`$-equivariant and fixed by the $`X`$-action. With $`J_1=\ker\bar D`$, the true fiber size in an $`i`$-sheet is still $`|(J_1)_i^-|\,|U_i^+|`$ by addition of a central graph element in midpoint coordinates; no $`z`$-stability of $`R`$ is assumed. Thus flatness requires $`|(J_1)_w^-|=|U_w^-|`$. Filter by the leading *ordinary* degree of $`s-1`$ on $`A`$ and by that of $`y`$ on $`I`$, with the old base kept with the very last degree. Each graded quotient is elementary and the map $`D`$ on any leading grade below $`N`$ is just inclusion of its actual coefficient in the corresponding $`I`$ grade. The filtration on $`A`$ is a subgroup filtration by truncated units, preserved by $`T`$. Even though $`J_1`$ need not be elementary, taking the negative subgroup for $`w`$ preserves short exact sequences of these abelian odd groups: apply the projection $`(1-w)/2`$. The logarithm of its size therefore adds along the grades. The bottom degree on $`A`$ is exactly the single copy of $`M`$ (the top unit factor); there $`D`$ is $`f_b`$. Equality forces zero bottom intersections by the single passive input, and then $`U=0`$ by the actual degree-one difference test. The normal graph would lie in $`W`$, centralize $`Y`$, and hence have its ring-unit part supported only in top degree. The bottom no-zero-defect condition again excludes any nonzero $`T`$-linear restriction in $`W`$. This checks the potentially non-elementary and tilted kernel cases, not just the associated graded loop.

A normal surjecting on $`T`$ kills pure perfect $`T`$ in its remaining 3-group quotient, hence all of $`X`$ by $`X_T=0`$, then $`I_{\ge2}`$ by $`[A,I]`$ and the last degree-one $`M`$ by $`T`$. The unique possible old base coinvariant is hit by both $`H`$ and the section, so no nontrivial proper quotient cut is flat. As before these arguments give faithful action and the exact normal-subloop criterion proves simplicity. The physical involution sheets generate: in any abelian odd module $`X`$, the subgroup generated by all $`(1-i)X=X_i^-`$ contains the differences for the projective group generated by its involutions, so equals $`X`$ here. The pure projective group and all of $`Y`$ occur too. The old proper loop embeds at zero new coordinates. For a reflected mark $`[x,y]i`$ its square belongs to elementary $`Y`$ by $`ix=-x,iy=y`$, so the native exponent remains exactly six.

## Actual group orders and two specially chosen native involutions

Every $`s\in1+I`$ has $`s^{3^a}=1`$, and $`(s-1)^{3^a-1}y=0`$ for $`y\in I`$, since $`3^a>N`$. Summing the geometric series in characteristic three gives

```math
(\iota(y)s)^{3^a}=\iota\big((s-1)^{3^a-1}y\big)=1.
```

(The separately central base $`Y_0,X_0`$ has exponent three.) A signed ratio unit $`s=(1+e_0t)/(1+e_\infty t)`$ has order exactly $`3^a`$, as seen on the first nonzero coefficient of $`s^{3^{a-1}}-1`$. Thus the true metabelian radical exponent is $`3^a`$. It has class $`N`$: $`N-1`$ successive differences by degree-one ratio units on a degree-one vector have nonzero top by the support calculation, while $`N`$ differences vanish. No group of higher derived length is hidden in this action.

Finally $`w`$ exchanges sites $`0,\infty`$, so $`ws=s^{-1}`$ as units. Let $`x\in X`$ be the corresponding pure unit with zero old component, and denote its pure group element by $`S(x)`$. The two actual native left translations $`S(x)w`$ and $`w`$ are distinct involutions in the reflected $`w`$-sheet (their midpoint $`Y`$ coordinate is zero). Call their points $`h,k`$, in that order. Their product as permutations is $`S(x)`$ of order $`3^a`$. Evaluation at the identity gives $`hk=S(x)H=\iota(-D(x))H`$ because $`\iota(D(x))S(x)\in W`$. Thus the native left translation of $`hk`$ is **exactly** $`\iota(-D(x))`$ in the vertical sheet, of order three since the ring entry $`s-1`$ is nonzero. The true associator is consequently the single actual stabilizer element

```math
L_{hk}^{-1}L_hL_k=\iota(D(x))S(x)\in W .
```

Projection of this graph is an isomorphism $`W\to X`$. Faithfulness of the native action was proved first. Hence its permutation order equals exactly $`3^a`$; the same is true of $`L_hL_k`$, and the dihedral assertion follows. This distinguishes native-element order, subgroup exponent and inner-permutation order without relying on a word in an abstract nonfaithful presentation.

[Provisional results and replay](../README.md)
