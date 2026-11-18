# 0104. A fixed-point test for lifted point stabilizers

**Mira Cult**

A quotient of a loop's left multiplication group need not be a quotient of the loop. Nevertheless an abelian group quotient acts like a translation group on the *labels* of actual loop elements once the point stabilizer is conjugated by the canonical inversion. This determines an orbit divisor and distinguishes two conjugacy classes in the same quotient fiber.

**Theorem.** Let $`G,H,K,\tau`$ be the faithful generated canonical folder of a finite simple proper left Bol loop $`Q`$. For any abelian quotient $`B=G/N`$,

```math
|2B|\;\mid\;|Q|=[N:H\cap N],\qquad 2B=\{2b:b\in B\}.    \tag{1}
```

In fact every individual orbit of $`\tau(H)`$ on the loop has size divisible by $`|2B|`$. For every $`b\ne-b`$ and every $`h\in H`$ over $`b`$, the same fiber of $`G\to B`$ contains a derangement of the same order as $`h`$, not conjugate to $`h`$. On cycles of simple socle factors this forces extra prime-power order even for some even-order elements and actions with shorter cycles.

Here a derangement is a group element with no fixed point on $`G/H`$, the actual set of loop elements. We give the elementary proof of $`G=HG'`$ below; see also the [earlier group-quotient argument](../sources/odd-completion/nonbruck-almost-simple-radical-bridge.md). The [canonical left folder](../sources/foundations/C0001.md) and [inversion theorem](../sources/foundations/C0007.md) are the only loop-specific inputs to (1)–(4). The statements about simple-factor cycles also use [the cycle transport proof](0103-radical-free-socle-coordinates.md).

## Point action versus marked conjugation

Write $`E=G\rtimes\langle t\rangle,\;\Lambda=tK`$, with a formal involution covering $`\tau`$, even for trivial action. Conjugation by $`h\in H`$ on the actual marks corresponds, under $`tk\longleftrightarrow kH`$, **exactly** to the ordinary action of $`\tau(h)`$ on $`G/H`$. Indeed

```math
h(tk)h^{-1}=t\,\tau(h)kh^{-1},\qquad
         \tau(h)kh^{-1}H=\tau(h)kH.                                  \tag{2}
```

The element after $`t`$ lies in $`K`$ by invariance, and the original transversal makes it the unique representative. Consequently, for each $`h\in H`$,

```math
\#\mathrm{Fix}_{G/H}(\tau(h))=|\Lambda\cap C_E(h)|,\qquad
 \tau(h)\in\bigcup_{g\in G}gHg^{-1}
       \;\Longleftrightarrow\;
       \tau(h)=khk^{-1}\;\text{for some original }k\in K.             \tag{3}
```

Indeed a fixed $`kH`$ forces equality of the two unique translations in (2). In particular if the images of $`\tau(h)`$ and $`h`$ are not conjugate in even one group quotient, $`\tau(h)`$ is a **derangement** (fixes no point). The converse to that last quotient implication is not asserted.

## All abelian quotient fibers at once

The induced action of $`\tau`$ on $`G/G'`$ is inversion since it inverts each generating translation. Hence every kernel $`N`$ of an abelian quotient is automatically $`\tau`$-stable and the action on $`B=G/N`$ is negation. Moreover $`HN=G`$. For example $`HG'`$ is normal, and $`x\mapsto L_x HG'`$ is a loop homomorphism onto $`G/HG'`$, since $`L_{xy}^{-1}L_xL_y\in H`$; its image is a subloop of a finite group and generates the quotient. Simplicity and nonassociativity force that quotient to be trivial. This also proves the equality in (1): the $`N`$-action is transitive.

Label each point $`x=kH`$ by $`b(x)=\bar k\in B`$, using its own original translation. This is not a homomorphism of loops. Formula (2) gives

```math
b(\tau(h)x)=b(x)-2\bar h.                           \tag{4}
```

As $`H\to B`$ is onto, every selected label coset modulo $`2B`$ occurs in full, with a common positive number of points **per individual label** within that coset. More strongly every $`\tau(H)`$-orbit of points maps onto a single such coset; its fibers have equal size. This proves (1) and its individual-orbit refinement. The selected cosets in $`B/2B`$ contain 0 and span that elementary two-group since $`K`$ generates $`G`$. Thus also

```math
|Q|\;\ge\;|2B|\,\big(1+\dim_{\mathbf F_2}(B/2B)\big).
```

In particular for **every** odd $`p`$, $`v_p(B)+v_p(H\cap N)\le v_p(N)`$. Taking $`N=G'`$ bounds the whole odd abelianization by a divisor of the commutator-group degree, not just a prime in common. This uses neither the classification of finite simple groups nor a one-sided prime-power conjecture.

If $`2b\ne0`$, every $`h\in H`$ above $`b`$ fixes the identity point while $`\tau(h^{-1})`$, also above $`b`$, is a derangement by (4). They have the same order but **are not $`G`$-conjugate**. In fact the entire conjugacy class of the latter misses $`H`$. If a candidate has just one conjugacy class of order-$`m`$ lifts above $`b`$, then no order-$`m`$ lift above $`b`$ lies in $`H`$.

There is a nonabelian-quotient version not requiring the whole quotient to be abelian. Let $`N`$ be $`\tau`$-stable, $`Y=G/N,\;J=HN/N`$, and let $`\theta`$ be its induced involution. Suppose $`b\in J`$ is **non-real** in $`Y`$ ($`b`$ is not conjugate to $`b^{-1}`$), but $`\theta(b)`$ is conjugate in $`Y`$ to $`b^{-1}`$. For $`h\in H`$ over $`b`$, the images of $`h^{-1}`$ and $`\tau(h^{-1})`$ are not conjugate, so (3) makes the latter a derangement. Its image is conjugate to $`b`$, so conjugate it by a lift in $`G`$ to obtain a derangement over the specific $`b`$, of the same order as $`h`$. Thus the same two-class conclusion holds. This does not assert $`H`$ covers each nonabelian quotient element.

## Centerless simple socles and higher-order forced lifts

Suppose now $`S=\prod_i T_i`$ is the nonabelian socle of a group with trivial solvable radical, $`B=G/S`$ as in the [socle-coordinate theorem](0103-radical-free-socle-coordinates.md). Either take $`B`$ abelian and $`b\in B`$ with $`b^2\ne1`$, or use its nonabelian non-real hypothesis above with $`b\in J`$. Put $`m=|b|`$. For each cycle $`c`$ of $`b`$ on the simple factors let $`l_c`$ be its length and $`T_c`$ the representative factor. If

```math
\gcd(m/l_c,\;|T_c|)=1 \quad\text{for all }c,    \tag{5}
```

then **no** stabilizer lift of $`b`$ has order $`m`$. Indeed the [single-class order-lift proof](0103-radical-free-socle-coordinates.md) shows every order-$`m`$ lift over this $`b`$ is in one socle-conjugacy class. To recall why: along each cycle, the inner-conjugacy class of its holonomy determines the inner orbit; the holonomy lives over $`(b^{l_c})_i`$ and has order dividing $`m/l_c`$. Condition (5) makes the inner kernel normal Hall over this cyclic outer subgroup, so all possible holonomies are inner-conjugate by Schur–Zassenhaus. Product over cycles. The existence of two distinct group classes above an actual stabilizer lift now contradicts this uniqueness. This proof does not require constructing a marked product over $`b`$.

For $`m=p^e>2`$, every stabilizer lift therefore has order divisible by $`p^{e+1}`$: if the $`p`$-part of one lift's order were only $`p^e`$, raising it to a multiple of its prime-to-$`p`$ part congruent to 1 modulo $`p^e`$ would produce an order-$`p^e`$ lift of $`b`$. A $`p`$-power lift exists by the same powering, and has a nonidentity order-$`p`$ power in $`H\cap S`$; its support is a union of complete $`b`$-cycles because the lift centralizes that power. If all cycles have full length $`m`$, (5) is automatic and the support contains at least $`p^e`$ coordinates. Thus the earlier odd semiregular bound for abelian $`B`$ also holds in particular at $`p=2,\;e\ge2`$. This does not extend the dihedral marked-product assertion to arbitrary even-order reversals; (3) uses nonconjugacy of point actions instead.

If (5) fails, do not conclude excess order from this result. For an abelian top with $`p^e>2`$ this records a sharp alternative at the level of necessary data: either a **shorter** $`b`$-cycle carries $`p`$ in its simple factor order, or every stabilizer lift has the excess $`p`$-power. Both possibilities can hold. For top exponent two the label translation in (4) is zero, and neither the same-fiber class obstruction nor excess order follows from it.

## An entire family of cyclic coordinate actions is impossible

There is a stronger test than excess order whenever the component conjugacy classes themselves are preserved. Suppose $`B`$ is abelian, $`b\in B`$ has order $`m=p^e>2`$, and all its coordinate cycles have length $`m`$. Suppose the coordinate permutation of $`\alpha`$ preserves **each** such cycle. Assume on each cycle's simple group $`T`$ that

```math
x \text{ is }T\text{-conjugate to }\phi(x^{-1})
       \quad\text{for every }p\text{-element }x\in T
                    \text{ and every }\phi\in\operatorname{Aut}(T).     \tag{6}
```

Then **no simple proper left Bol folder with these data exists**, regardless of any splitting, inner or outer coordinate decorations, or stabilizer correlations.

Indeed take a $`p`$-power stabilizer lift $`h`$ of $`b`$, which exists because $`J=B`$. Write $`h'=\tau(h^{-1})=\alpha h^{-1}\alpha^{-1}`$. It has the same top, but by (3) cannot be conjugate to $`h`$. On a chosen cycle take index $`i`$, and set $`j=\pi_\alpha^{-1}i`$. By hypothesis $`j=\pi_b^s i`$ for some $`s`$. The holonomy $`(h^m)_i`$ is an **inner** $`p`$-element because $`b^m=1`$. At $`j`$ the holonomy of $`h`$ is its transport by $`(h^s)_i`$. The holonomy of $`h'`$ at $`i`$ is therefore the image of $`((h^m)_i)^{-1}`$ under the automorphism $`\alpha_j (h^s)_i`$ of $`T_i`$, identifying the centerless group with its inner group. By (6) the two holonomies are inner-conjugate. This holds on every cycle. The cyclic-arrow conjugator construction (valid for arbitrary lift order) makes $`h,h'`$ conjugate by an element of $`S`$, a contradiction. It would suffice to check (6) only for the actual cycle transport automorphisms and attainable holonomies; the stated version needs neither enumeration.

In particular let every factor be $`\mathrm{PSL}_2(q)`$, $`q=2^f,\;f\ge2`$.
* For each $`2^e\ge4`$ acting semiregularly with full coordinate cycles, the inversion must **exchange at least two of those cycles**. There is no canonical group of this type having such an abelian-top element acting as one full cycle.
* For each $`3^e\ge3`$ the same conclusion holds if $`3\nmid f`$.

For the first assertion, in characteristic two $`\mathrm{PSL}_2(q)=\mathrm{SL}_2(q)`$. Every nonidentity 2-element is a nontrivial two-dimensional unipotent, hence an involution with the sole Jordan block of size two. There is one general linear class, which does not split in the special linear group: multiply any conjugator by a central scalar with prescribed inverse determinant (every nonzero field element is a square). Thus (6) holds. For the second, $`|\mathrm{SL}_2(q)|=q(q-1)(q+1)`$ has 3-part exactly 3 when $`3\nmid f`$: the order of 2 modulo 9 is six and then $`2^f\not\equiv\pm1\bmod9`$, while exactly one of $`q\pm1`$ is divisible by three. Each nonidentity 3-element has characteristic polynomial $`X^2+X+1`$, from its two reciprocal primitive cube-root eigenvalues. All such matrices are conjugate in $`\mathrm{GL}_2(q)`$, whether the eigenvalues lie in the ground field or not, and the same determinant correction works. Again there is just one nonidentity class and (6) follows. The [earlier A₅ single odd-abelian-orbit theorem](../sources/factor-permutation/radical-free-a5-single-abelian-orbit.md) used fixed-mark masses for pure actions and is not asserted to be new here. The present criterion works for arbitrary allowed outer arrows, for even top orders above two, and for all the indicated simple factors. It does not rule out inversions exchanging distinct cycles, arbitrary simple socles, or different actions of a larger group.

**Checks and scope.** The [stdlib checker](../sources/code/verify_abelian_top_derangements.py) uses the exact-factorization folder of a concrete 648-element cyclic wreath group. It checks the ordinary twisted point action, all individual fibers and orbits, and unequal-order coordinates in equal-order twin conjugacy classes above each nontrivial order-three top. It also exhibits actual even-order four-cycle lift holonomies and the exponent-two boundary. Here the base of the wreath group is S₃³ and the top is C₃; its two exact factors use three copies of the transposition subgroup and, on the other side, three order-three coordinates whose exponent sum equals the top. The checker realizes every one of the 69,984 group elements as exactly one translation times one of 108 stabilizer elements. All 72 stabilizer lifts over nonzero labels have the unequal coordinate orders (3,9), reversed by inversion and interchange. The small folder is a control; it is not asserted simple. The [independent controls](../sources/code/check_125_twisted_fibers_and_psl2.py) check the twist on additional actual coset actions and exhibit the order-nine field-automorphism obstruction at q=8. It shows why the class argument at prime three does not automatically extend to every field degree; it is not a counterexample loop. The [evidence record](../normal-layer-evidence.md) distinguishes the exact-source mathematical review from these finite computations.
