# Every ternary local-algebra two-sheet loop is a native subloop of a finite simple Bol loop

**Mira Cult · Provisional research.** The author proofs below have not been independently reviewed.

The new coefficient construction works for arbitrary socle dimension, nonhomogeneous involutions and multiple local generators. Its finite matrix input is the independently audited [explicit projective example](../../manuscripts/0112-elementary-radical-example.md), [augmentation argument](../../manuscripts/0113-infinite-augmentation-chain.md) and [one-passive-pair lemma and review](../../projective-radicals/verification.md). We give the general sharpness and normal-cut arguments below rather than assuming an unaudited classification of thickened projective kernels.

**Theorem.** Let $`V`$ be any finite-dimensional commutative associative nilpotent algebra over $`F=\mathbb F_3`$, with any involutive algebra automorphism $`\sigma`$ (the identity is allowed). In its unitalization put $`a(u)=(1+u)/(1+\sigma u)`$. On $`\{0,1\}\times V`$ take the genuine loop multiplication

```math
(0,u)(e,v)=(e,u+v),\qquad (1,u)(e,v)=(1+e,u+a(u)\sigma v).
 \tag{1}
```

The sheet coordinate uses addition modulo two. The **entire** loop embeds in a finite simple non-Moufang left Bol loop of exponent six. All involutions on one $`V`$ can use the same host. For $`d=\dim V\ge1`$ the host has order

```math
20\cdot 3^{138+40d-h},\qquad
 h=\dim(V/V^2)+\dim\mathrm{Ann}_{F\oplus V}(V).
 \tag{2}
```

Thus its order is polynomial in the order of (1). A finite list of different algebras can share one host, by taking their direct sum with products between distinct summands zero. We do not claim that every exponent-six loop, or even every loop with an abelian index-two kernel, has form (1). When $`d=0`$ the two-element group already occurs in the base example. Formula (1) defines a Bol loop on its own by [the explicit four sandwiches and both divisions](two-associators.md#1-three-involutions-in-an-associative-algebra-two-sheet-loop); the embedding below also verifies its whole multiplication independently of those sandwiches.

## 1. From an arbitrary algebra to a visible one-dimensional socle

Set $`C=F\oplus V`$ and write $`C^\vee=\mathrm{Hom}_F(C,F)`$, acted on by $`(b\ell)(a)=\ell(ba)`$. The trivial extension $`E=C\oplus C^\vee`$ has product

```math
(b,\ell)(c,k)=(bc,bk+c\ell).
```

It is local with radical $`N=V\oplus C^\vee`$, nilpotent and of dimension $`2d+1`$. Its socle (annihilator of $`N`$) is the single line $`S=\{(0,\ell):\ell(V)=0\}`$. Indeed annihilating all dual vectors first forces the $`C`$ component to be zero; annihilating $`V`$ then gives the displayed dual condition. Every nonzero ideal meets $`S`$ by multiplying it as often as possible by $`N`$. Thus, if $`L`$ is maximal with $`N^L\ne0`$, then $`N^L=S`$. For $`V\ne0`$, $`L\ge2`$: some product of a nonzero $`v`$ and a dual vector is nonzero. Since $`N^2=V^2\oplus V C^\vee`$, annihilator duality gives $`\dim N/N^2=h`$ of (2).

The ordinary group of units $`U_0=1+N`$ need not have exponent three. Its subgroup $`1+C^\vee`$ is elementary and splits off:

```math
(b,\ell)=(b,0)(1,b^{-1}\ell),\qquad b\in1+V .
```

Units commute, so $`c(b,\ell)=(b^{-1}\ell)(1)`$ is an actual additive group homomorphism $`U_0\to F`$. On $`1+S`$ it is evaluation at $`1`$, an isomorphism. On every pure $`C`$ unit it is zero. Merely evaluating the *unnormalized* dual coordinate is not a group character.

## 2. The twenty-site algebra and its actual units

Let $`T=\mathrm{PSL}_2(19)`$ act on its twenty projective sites. Write $`M`$ for the sum-zero subspace of $`F^{20}`$, and identify $`S\simeq F`$ by evaluation at $`1`$. Diagonal $`S`$ is an annihilating ideal. Define the $`T`$-algebra and an abelian unit group by

```math
I=\{(v_j)\in N^{20}:\textstyle\sum_j v_j\in N^2\}/\mathrm{diag}(S),\qquad
 A=\{(u_j)\in U_0^{20}:\textstyle\prod_j u_j=1\}.
 \tag{3}
```

$`A`$ acts on $`I`$ by multiplication and embeds in $`1+I`$: the first-grade condition follows by linearizing the product, and a diagonal socle unit with twentieth power one is trivial. The induced map on $`1+I`$ given by site product modulo $`1+S`$ has kernel $`A`$. Indeed a product in $`1+S`$ is corrected to $`1`$ by a unique diagonal socle unit since $`20`$ is invertible. In particular $`(1+I)/A`$ is $`T`$-trivial. Also $`A_T=0`$: the permutation unit group is the direct product of $`A`$ and the diagonal by the twentieth-power automorphism of the odd $`3`$-group $`U_0`$; its coinvariants are $`U_0`$ by product and the diagonal already maps isomorphically. Thus for a projective involution $`i`$,

```math
|A_i^-|=|(1+I)_i^-|=|I_i^-|.
 \tag{4}
```

For the first equality every negative unit dies in the $`T`$-trivial quotient; for the second, fixed units are in bijection with fixed algebra elements by subtracting one and the positive and negative parts split in an odd abelian group. Write $`c_*(a)=(c(a_j))_j\in M`$, a $`T`$-map. The bottom units with $`a-1`$ in $`S^{20}/\mathrm{diag}(S)`$ identify with $`M`$; precisely the unique sum-zero representatives occur in $`A`$. The homomorphism $`c_*`$ is identity under this identification.

Three facts about the genuine action will be used. Put $`I_{\ge2}=(N^2)^{20}/\mathrm{diag}(S)`$.

1. $`[A,I]=I_{\ge2}`$. Inclusion is multiplication by a radical element. For distinct sites $`i,b,c`$, take the unit with $`1+v`$ at $`i`$, its inverse at $`b`$, one elsewhere; apply its difference from $`1`$ to the vector with entries $`t,-t`$ at $`i,c`$. The exact result is $`e_i vt`$, with no higher contamination. These span all of $`I_{\ge2}`$. Thus $`I/I_{\ge2}`$ is a direct sum of $`h`$ copies of $`M`$.
2. A nonzero stable additive subgroup having any element outside the socle-site layer can be driven to a nonzero element of that layer by *actual unit differences*. Given a representative $`y=(y_j)`$ with a non-socle component, take maximal $`k\ge1`$ for which $`y_i v_1\cdots v_k\ne0`$ at some site $`i`$ with $`v_j\in N`$. Every component times every $`k`$ factors now belongs to $`S`$, since all further products vanish. Use $`k`$ unit differences as in the previous paragraph, all with selected site $`i`$ and the same spare site $`b`$. The result is supported at $`i,b`$, lies in $`S`$ there (the inverse at $`b`$ differs from $`-v_j`$ by $`N^2`$), and is nonzero at $`i`$. It cannot vanish modulo the twenty-site diagonal. Changing the original representative by diagonal $`S`$ changes none of these calculations.
3. A unit $`a\in A`$ acting trivially on $`I`$ has $`a_i-1\in S`$ for every $`i`$. If not, some $`(a_i-1)v\ne0`$; apply $`a-1`$ to the vector with $`v,-v`$ at $`i,b`$. A nonzero output of support at most two is never diagonal. This is a kernel-of-action statement, not faithfulness of all $`A`$.

## 3. Sharp projective host and every normal cut

Here are the finite inputs, with their role identified. Write $`B=19{:}9`$ for the infinity stabilizer, $`r:x\mapsto4x`$, $`w:x\mapsto-1/x`$, and $`e=(1-w)/2`$. The [matrix and one-passive-pair source, §1](../../projective-radicals/proofs/multiplicity.md#1-the-base-matrix-input-and-an-obstruction-insensitive-to-all-the-new-central-slots) gives $`T`$-modules $`X_0,Y_0`$ of dimensions $`117,119`$, a $`B`$-map $`f_0:X_0\to Y_0`$, a derivation $`d_0:B\to Y_0`$, and a $`B`$-map $`\alpha:M\to Y_0`$. For the abelian bottom map

```math
f_b(x,m)=(f_0(x)+\alpha(m),m): X_0\oplus M\to Y_0\oplus M
```

the map $`e f_b`$ on the negative subspace is injective, and for any $`T`$-submodules $`J_b,U_b`$ with $`f_b(J_b)\subseteq U_b`$, equality of the negative dimensions occurs only when both are zero. Also $`(X_0)_T=0`$; $`(Y_0)_T`$ is a single line hit by $`f_0`$ and $`d_0`$ together. In the compressed signed group on $`X_0\oplus M\oplus Y_0`$ with graph map $`f(x,m)=f_0(x)+\alpha(m)`$ and derivation $`d_0`$, a genuine sign cannot invert a stabilizer element of nontrivial projective projection: the Borel moves a simultaneous nontrivial pair to projections $`zw,r^j`$, then power to $`r^3`$; the row killing $`(f+wfw)(X_0\oplus M)+(r^3-1)Y_0`$ has nonzero value on $`(1-w)d_0(r^3)`$. This is an obstruction to *all* kernel lifts. It is the same finite row, not a new use of a semisimple or associated-graded criterion. $`M_T=0`$.

Put $`X=X_0\oplus A`$, $`Y=Y_0\oplus I`$, $`P=Y\rtimes X`$, $`G=P\rtimes T`$. The only nontrivial $`X`$-action is multiplication of $`A`$ on $`I`$. Adjoin the commuting-with-$`T`$ involution $`z`$ with signs $`+,-`$ on $`X,Y`$. Let $`S(x)`$ and $`T_y`$ be the pure kernel lifts. The map

```math
D(x,a)=(f_0(x)+\alpha(c_*(a)),a-1)
```

is a $`B`$-equivariant cocycle because $`ab-1=(a-1)+a(b-1)`$. Its abelian graph $`W`$ together with lifts $`T_{d_0(g)}g`$ for $`g\in B`$ is an actual subgroup $`H`$, of order $`|X||B|`$. Take $`K=z\Lambda`$ for the full set $`\Lambda`$ of involutions outside $`G`$ in $`G\rtimes\langle z\rangle`$. In midpoint coordinates $`[x,y]=S(x/2)T_yS(x/2)`$ (multiplicative halving of the unit coordinate), inversion negates both coordinates. Consequently $`K`$ has identity sheet $`Y`$ and sheets $`[X_i^-,Y_i^+]i`$ on the $`171`$ nonidentity projective involutions. The [original negative rank difference](../../manuscripts/0112-elementary-radical-example.md) is two; (4) preserves it. Hence $`|K|=|Y|(1+171/9)=20|Y|=[G:H]`$.

Sharpness requires $`H\cap\Lambda^2=1`$, equivalently no nonidentity $`h\in H`$ is inverted by an outside involution. With nonidentity projective projection, quotient out the whole $`I`$ and apply $`a\mapsto c_*(a)`$ on $`A`$. This is a true group homomorphism to the preceding finite compression, with the genuine graph and derivation as image, so the separating row rules this out. For $`h\in W`$ with nontrivial unit coordinate, work on the first nonzero grade of $`a-1`$ in $`I`$, filtering by the images of $`(N^j)^{20}`$ (and the first-grade restriction at $`j=1`$). The pair of leading unit and translation coordinates of $`h`$ is $`(v,v)`$. Inner conjugations by $`P`$ do not change this pair, since commutators multiply by a radical factor, and the old coordinates commute with $`P`$. Thus a lift of $`zi`$ on this pair acts by $`(i,-i)`$, which cannot invert both identical nonzero entries. The same applies to $`i=1`$. If $`a=1`$ the original vertical avoidance applies. Conjugacy of $`\Lambda`$ gives the transversal condition at every conjugate of $`H`$; the signed sandwiches give a left Bol loop.

For completeness consider any $`1<R\lhd G`$ inside $`P`$, **not** necessarily $`z`$-stable. Write $`U=R\cap Y`$, $`J=\pi_X R`$. A flat cut would mean that the images of $`K`$ in $`G/R`$ have cardinality $`[G:HR]`$ and hence are sharp on the identity orbit of that quotient. Only the identity projective sheet $`Y`$ lies over the Borel coset since $`|B|`$ is odd. Its image there has size $`|Y|/|U|`$; the quotient block has size $`|Y|/[R:R\cap W]`$. Equality gives $`R=U(R\cap W)`$. Modulo $`U`$ its graph over $`J`$ is central in $`P/U`$ since all its commutators with $`P`$ lie in $`R\cap Y`$. Thus its displacement $`\bar D:J\to Y/U`$ is a $`T`$-equivariant additive homomorphism, with $`X`$-fixed values; $`J`$ acts trivially on $`Y/U`$. Set $`J_1=\ker\bar D`$.

In an $`i`$-sheet two midpoint coordinates can agree modulo $`R`$ only when their $`X`$ difference is $`j\in J_i^-`$ and the positive $`Y`$-coordinate difference modulo $`U`$ equals $`\pm\bar D(j)`$. Multiplying by this central graph in midpoint coordinates adds exactly those differences: $`j/2`$ acts trivially on $`Y/U`$ and $`\bar D(j)`$ is $`X`$-fixed. But $`\bar D(j)`$ is $`i`$-negative. Thus the precise common fiber cardinality is $`|(J_1)_i^-|\,|U_i^+|`$, with every such choice working. Each nonbase projective coset originally has nine disjoint equally sized involution sheets (the original projective geometry), still distinct in $`G/R`$; their fiber counts coincide by $`B`$-conjugacy. Flatness forces $`|(J_1)_w^-|=|U_w^-|`$.

Filter $`J_1`$ and $`U`$ by leading $`N`$-power, with the old $`X_0,Y_0`$ kept at the bottom together with $`S^{20}/\mathrm{diag}(S)`$. The plus slots use the unit-subgroup flag defined by $`a-1`$ in that additive flag. For every grade above the bottom, $`D(J_1)\subseteq U`$ and its leading map is the identity inclusion of the actual coefficient. This gives an injection of each entire graded $`J_1`$ into the corresponding graded $`U`$, irrespective of correlations between coordinates. At the bottom, $`D`$ is *exactly* $`f_b`$, by the normalization of (3). The negative-subgroup log size adds over the flag, since the negative projector is exact on finite odd abelian groups. The injectivity of $`e f_b`$ gives the bottom inequality too. Equality thus forces equality at the bottom, and hence zero bottom intersections by the finite input. Fact 2 then forces $`U=0`$: differences kill $`Y_0`$ and detect any lower coordinate. Now $`R\le W`$, and it commutes with $`Y`$ since $`R\cap Y=0`$. Fact 3 puts its graph entirely at the bottom. Normality gives a $`T`$-equivariant restriction of $`f_b`$ on $`J`$; its image has precisely the same negative dimension by injectivity there. The bottom no-equality condition forces $`R=1`$, a contradiction.

If a proper normal $`R`$ has nontrivial projective image it surjects onto simple $`T`$, leaving a $`3`$-group quotient. The pure perfect $`T`$ dies, then $`X`$ dies by zero coinvariants, then $`[A,I]=I_{\ge2}`$ dies, and $`I/I_{\ge2}`$ dies by $`M_T=0`$. In the sole remaining possible nontrivial quotient, the old $`Y_0`$ coinvariant, $`H`$ and $`K`$ both surject: the section strictly exceeds quotient index one. This verifies all cuts in the [exact simplicity criterion](../../sources/foundations/C0001.md). The action is faithful: a normal subgroup contained in $`H`$ lies in $`P`$, and its cut would be flat (or its graph kernel is excluded directly as above). The marks generate $`G`$: $`Y`$ and pure projective involutions belong to them, and all pure $`S(X_i^-)`$ are obtained from the reflected marks. These subgroups span $`X`$ since $`T`$ is generated by its involutions and $`X_T=0`$. The actual left group is therefore $`G`$, with whole radical $`P`$. The old non-Moufang example embeds at zero new coordinates. Reflected marks square into elementary $`Y`$ in midpoint coordinates, so the native exponent is exactly six. Finally $`\dim I=20(2d+1)-h-1`$, giving (2).

## 4. Three literal Weyl pairs, not an embedding of left groups alone

The physical $`w`$ has ten two-cycles on the twenty sites ($`-1`$ is not a square modulo $`19`$). Select three different cycles and orient them. Embed an element $`y\in V`$ by giving its pure $`C`$ value at the three chosen first sites, the pure $`C`$ value $`\sigma y`$ at the three opposite sites, and zero elsewhere. Write $`\jmath y`$ for the result. It is a multiplicative additive injection into $`I`$: the first-grade condition holds since **three** copies sum to zero; no nonzero supported tuple is diagonal. Also $`w\jmath y=\jmath\sigma y`$. This argument does not require $`\sigma`$ to extend to $`E`$. A single pair need not meet the first-grade condition.

Let $`A'`$ be the local norm-one units in $`1+V`$, embedded as $`1+\jmath(a-1)`$. Each lies in $`A`$: the two units on each pair are inverse. All have $`c_*=0`$ since their dual coordinates are zero. Thus in the subgroup generated by $`T_{\jmath V},S(A'),w`$, the full $`H`$ intersection is exactly $`E'=\{T_{a-1}S(a):a\in A'\}`$, suppressing $`\jmath`$ on the local coordinates. Indeed $`w\notin B`$; above identity the full graph fixes the exact $`T`$ coordinate, and its old shear vanishes. $`w`$ normalizes $`E'`$. The smaller cosets $`T_y w^e E'`$ therefore embed in the actual host cosets. On these cosets $`T_y`$ translates, $`w`$ switches the sheets and applies $`\sigma`$, and $`S(a)`$ sends $`v`$ to $`av+1-a`$ on either sheet.

For an odd point $`y`$, set $`a=(1+y)/(1+\sigma y)`$ and $`b=a^{-1/2}(y-1+a)`$. Then $`\sigma b=b`$: in characteristic three the equation $`y-1+a=a(\sigma y-1+a^{-1})`$ is precisely $`1+y=a(1+\sigma y)`$. The genuine midpoint mark $`S(a^{1/2})T_bS(a^{1/2})w`$ reaches the odd point and acts with intercept $`y`$ and slope $`a\sigma`$. Even marks are the true $`T_y`$. Thus the restriction of **each native multiplication cell** is (1), and finite sharpness gives both divisions, as claimed. This includes simultaneous embeddings associated with different $`\sigma`$; disjoint images are not asserted.

[Overview and reproducible checks](README.md)
