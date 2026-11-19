# Arbitrary finite 3-groups in the solvable radicals of simple exponent-six left Bol loops

**Mira Cult · Provisional research.** The author proofs below have not been independently reviewed.

Every loop here is left Bol and the left multiplication group is on the same hand. This is not a statement that an arbitrary $`3`$-group embeds under the native loop operation. The group universality is in the **faithful left-group radical**; there is a separate genuine subloop theorem for the two-sheet algebras below.

**Theorems.** For every finite $`3`$-group $`H_0`$ there is a finite simple non-Moufang left Bol loop of exponent six whose faithful left multiplication group has solvable radical containing $`H_0`$, and whose quotient by that whole radical is $`\mathrm{PSL}_2(19)`$. In particular this radical has **unbounded derived length** even with those three other properties fixed. The theorem does not fix the exponent of the radical. It is stronger than prescribing arbitrary class-two exponent-three groups or obtaining unbounded nilpotency class inside a metabelian radical.

More generally, let $`V`$ be a finite-dimensional nilpotent **associative, not necessarily commutative** algebra over $`F=\mathbb F_3`$ and let $`\sigma`$ be an involutive algebra automorphism. Each whole native table

```math
(0,u)(e,v)=(e,u+v),\qquad (1,u)(e,v)=(1+e,u+a(u)\sigma(v)),
 \qquad a(u)=(1+u)(1+\sigma u)^{-1}
 \tag{1}
```

embeds in a finite simple proper exponent-six left Bol loop. Unit multiplication in this formula is *in the order shown*. Write $`d=\dim V\ge1`$ and $`C=F\oplus V`$. One host has order

```math
20\cdot3^{138+40d-h},\qquad
 h=\dim V/V^2+\dim\{c\in C:cV=Vc=0\}.
 \tag{2}
```

The host itself is independent of $`\sigma`$. The zero-algebra case $`d=0`$ is the two-element subgroup already present in the base.

**Dependency and new issue.** We use the finite base and one-passive-pair input listed in the [commutative construction, §3](commutative-construction.md#3-sharp-projective-host-and-every-normal-cut); the [one-pair matrix review](../../projective-radicals/verification.md) is a separate acceptance. The commutative proof alone does not handle the present problem. The plus group is nonabelian, its inverted elements need not be a subgroup, an even projection of a tilted normal graph need not be central even after killing its vertical intersection, and a literal coordinatewise product constraint need not be a group homomorphism. Below we verify each replacement. No upstream results about a universal associative native subloop are used.

## 1. Noncommutative coefficient double and the acting group

Give $`C^\vee`$ its two-sided bimodule actions $`(b f)(s)=f(sb)`$ and $`(f b)(s)=f(bs)`$. Write $`E=C\oplus C^\vee`$ with associative product $`(a,f)(b,g)=(ab,ag+fb)`$. Its radical is $`N=V\oplus C^\vee`$; nilpotence follows by expanding products, since two dual factors give zero and sufficiently many $`V`$ factors on either side annihilate. Its left and right socles separately are the **same** single line

```math
S=\{(0,f):f(V)=0\}.
```

For example, $`(b,f)N=0`$ first gives $`b=0`$ by testing all dual factors, then $`f(VC)=0`$ by testing $`V`$. The other order tests $`CV`$. Thus the last nonzero power $`N^L`$ is $`S`$ and $`L\ge2`$ for $`d\ge1`$. Further $`N^2=V^2\oplus(VC^\vee+C^\vee V)`$, and the annihilator-dual of the second summand in $`C`$ is exactly the last space in (2). Thus $`\dim N/N^2=h`$.

The nonabelian $`3`$-group $`U=1+N`$ has the actual character

```math
c(a,f)=f(a^{-1})\in F .
```

Indeed evaluating $`(ag+fb)((ab)^{-1})`$ gives $`g(b^{-1})+f(a^{-1})`$, with the inverse in the right order. The character sees the whole $`1+S`$ by evaluation at one, but vanishes on all pure $`C`$ units; in particular $`1+S`$ injects into $`U_{\mathrm{ab}}`$. Identify $`S`$ with $`F`$ by that evaluation.

Use the twenty projective sites and the augmentation $`T`$-module $`M`$ as in the preceding proof. Define

```math
I=\{y\in N^{20}:\textstyle\sum y_j\in N^2\}/\mathrm{diag}(S),
 \qquad
 A=\ker\big(U^{20}\longrightarrow U_{\mathrm{ab}},\ (a_j)\longmapsto\prod_j\bar a_j\big).
 \tag{3}
```

Here $`I`$ is an associative algebra, since diagonal $`S`$ annihilates it on both sides. $`A`$ embeds in $`1+I`$: first-grade addition factors through $`U_{\mathrm{ab}}`$, and a diagonal socle unit cannot have trivial twentieth power there unless it is one (apply $`c`$). The product on $`1+I`$ into $`U_{\mathrm{ab}}/\overline{1+S}`$ is well-defined with kernel the image of $`A`$, correcting any socle product by the unique diagonal twentieth root. Thus $`(1+I)/A`$ is $`T`$-trivial and odd. The map $`c_*(a)=(c(a_j))_j`$ takes $`A`$ to $`M`$ and is the identity on the bottom sum-zero socle units modulo diagonal $`S`$.

Killing the $`T`$ action normally kills the **entire group** $`A`$. To see this, write $`d_{ib}(g)`$ for $`g`$ at $`i`$, $`g^{-1}`$ at $`b`$, one elsewhere. These elements generate $`A`$: they realize all sum-zero tuples on abelianization, and for three distinct sites the commutator of $`d_{ib}(g)`$ and $`d_{ic}(h)`$ realizes $`[g,h]`$ at the single common site. The action of $`T=\mathrm{PSL}_2(19)`$ is doubly transitive (the Borel's translations are transitive on the nineteen finite points). Thus $`d_{ib}(g)`$ and its inverse $`d_{bi}(g)`$ become equal if $`T`$ acts trivially; the common value has odd order and dies. No incorrect diagonal splitting of a product of nonabelian groups is required.

$`A`$ acts by **left multiplication** on the additive $`I`$. Facts 1–3 of [the commutative proof, §2](commutative-construction.md#2-the-twenty-site-algebra-and-its-actual-units) hold here for the following explicit reasons.
* $`[A,I]=(N^2)^{20}/\mathrm{diag}(S)`$: the difference by $`d_{ib}(1+v)`$ on a vector $`e_i u-e_c u`$ for distinct $`i,b,c`$ equals $`e_i vu`$. These span every required product and therefore all of the target.
* Given a vector with a nonsocle component, take maximal $`k\ge1`$ with $`v_1\cdots v_k y_i\ne0`$ at some site. For *every* component all products with $`k`$ left factors are now in the left socle $`S`$. Use the corresponding $`k`$ differences $`d_{ib}(1+v_j)-1`$ in that same order. At $`i`$ the product is nonzero, at $`b`$ higher-order corrections from the inverses vanish by maximality, and no other site survives. It is not a diagonal vector. Such differences carry any $`A`$-stable additive subgroup meeting a lower layer to a nonzero socle vector.
* If $`a\in A`$ acts trivially on $`I`$, then $`(a_i-1)N=0`$ at each site: test the vectors $`e_i v-e_b v`$; an output supported there is zero modulo diagonal only if identically zero. The **right** factor is arbitrary, so the first one-sided socle calculation gives $`a_i-1\in S`$. There is just one bottom copy of $`M`$, not one for every socle dimension in the original algebra.

## 2. Involution fibers without linearizing the plus group

For any finite odd group $`L`$ and involutory automorphism $`i`$, write $`D_i(L)=\{x:i(x)=x^{-1}\}`$. Each such $`x`$ has unique square root $`s`$, also inverted; $`x=s i(s)^{-1}`$. Thus $`D_i(L)`$ is a single twisted orbit, of size $`|L|/|C_L(i)|`$. If $`K\lhd L`$ is $`i`$-stable, $`C_L(i)\to C_{L/K}(i)`$ is surjective: for fixed $`gK`$, the element $`n=g^{-1}i(g)\in K`$ is inverted by $`i`$, and $`g\sqrt n`$ is fixed. Consequently

```math
|D_i(L)|=|D_i(K)|\,|D_i(L/K)|.
 \tag{4}
```

None of these inverted sets has been assumed to be closed under multiplication. Applying (4) or the fixed-count formula and the $`T`$-trivial quotient in (3) gives

```math
|D_i(A)|=|D_i(1+I)|=|I|/|I_i^+|=|I_i^-|.
```

Indeed every inverted unit maps to a trivial element of the odd quotient. The fixed units correspond to additive fixed elements by subtracting one.

Take $`X=X_0\times A`$, $`Y=Y_0\oplus I`$, $`P=Y\rtimes X`$, $`G=P\rtimes T`$. Let $`z`$ act identically on $`X`$, negatively on $`Y`$, and commute with $`T`$. The graph $`W`$ has cocycle

```math
D(x,a)=(f_0(x)+\alpha(c_*(a)),a-1).
```

The second coordinate is a (not generally additive) left cocycle because $`ab-1=(a-1)+a(b-1)`$. The graph is now typically nonabelian. The same old Borel derivation gives the actual stabilizer $`H=W\rtimes\widetilde B`$ over $`B=19{:}9`$. Use all outside involutions $`\Lambda`$ for the signed transversal $`K=z\Lambda`$. With $`[a,y]=S(\sqrt a)T_y S(\sqrt a)`$ for $`a\in X`$ (including the elementary old coordinate), inversion gives $`[a^{-1},-y]`$ without assuming any two square roots commute. Thus the genuine sheets are $`Y`$ and $`[D_i(X),Y_i^+]i`$; the preceding count gives $`|K|=20|Y|=[G:H]`$ just as in the original finite matrix example.

The original finite nonvertical separating row still applies after quotienting out $`I`$ and mapping $`A`$ by the **homomorphism** $`c_*`$. The image is the same elementary signed group, graph $`f_0+\alpha`$ and Borel cocycle, excluding all nontrivial projected stabilizer elements inverted by physical signs. In the kernel, if $`a\ne1`$ the unit $`a-1`$ and the displacement $`D`$ have the same first nonzero $`N`$-power coefficient $`b`$. Conjugation by $`P`$ fixes this pair on that grade: both a unit conjugation and an affine-coordinate correction differ by an extra radical factor. A signed lift acts there as $`(i,-i)`$ and cannot invert $`(b,b)`$ unless $`b=0`$. For trivial unit coordinate use old vertical avoidance (the old kernel commutes with the new one). Therefore $`H\cap\Lambda^2=1`$, giving actual sharpness on all cosets and the left Bol operation.

For the essential all-normal test, suppose $`1<R\lhd G`$ lies in $`P`$ and has a flat cut. Write $`U_R=R\cap Y`$, $`J=\pi_X R`$. Counting just the projective identity coset as in the [preceding cut argument](commutative-construction.md#3-sharp-projective-host-and-every-normal-cut) gives $`[R:R\cap W]=|U_R|`$, hence $`R=U_R(R\cap W)`$. In $`P/U_R`$ the residual graph over $`J`$ need **not** be central. But $`J`$ acts trivially on $`Y/U_R`$, since $`[R,Y]\le U_R`$. Its graph displacement $`\bar D:J\to Y/U_R`$ is therefore an honest additive homomorphism *from the possibly nonabelian group*, and is $`T`$-equivariant by normality. Set $`J_1=\ker\bar D`$.

The fiber size in any one reflected sheet is constant, even when $`z`$ does not stabilize $`R`$. Indeed every signed involution above $`zi`$ is $`P`$-conjugate to $`zi`$ by the twisted-orbit fact applied to $`P`$. Multiplying by $`z`$ gives bijections $`k\mapsto (z p z)k p^{-1}`$ on that sheet; they preserve equality of images modulo $`R`$ by normality in the **unsigned** $`G`$. We may count the fiber above the *pure* $`i`$. A midpoint $`[a,y]i`$ projects there just when $`a\in J`$ and $`y\bmod U_R=\bar D(a)`$: its square root belongs to $`J`$ and acts trivially on $`Y/U_R`$. Here $`i(a)=a^{-1}`$ implies $`i\bar D(a)=-\bar D(a)`$, but $`y`$ is $`i`$-positive, so both are zero in the quotient. Thus the actual uniform fiber has size

```math
|D_i(J_1)|\,|(U_R)_i^+|.
 \tag{5}
```

This argument neither compares two arbitrary noncommuting midpoints as if additive, nor assumes the residual graph central. The nine disjoint reflected projective sheets per outside Borel coset all have the same fiber by Borel conjugacy, so flatness forces $`|D_w(J_1)|=|(U_R)_w^-|`$.

Filter $`J_1`$ by intersecting it with the power-of-$`N`$ unit flag, and $`U_R`$ by the parallel additive flag; keep the old pair $`X_0,Y_0`$ together with the final $`N^L=S`$ layer. These are series normal in the relevant groups (unit powers of a two-sided ideal); all graded quotients are elementary. $`D(J_1)\subseteq U_R`$ literally, and the leading coefficient of $`a-1`$ is unchanged on every pre-bottom quotient, giving a $`T`$-equivariant graded injection there. At the bottom $`D`$ is exactly $`(x,s)\mapsto(f_0x+\alpha(s),s)`$ and its negative injection gives the last inequality. Formula (4) adds the **logarithms of the inverted-set sizes** along the *nonabelian* flag. Thus equality of the total sizes forces equality in the one-passive-pair lemma and both bottom intersections vanish. The actual site-difference argument now forces $`U_R=0`$. So $`R\le W`$ and commutes with $`Y`$; its units act trivially and are socle units, by §1. The remaining graph is a genuine $`T`$-invariant restriction of the bottom map. Its $`T`$-linear image has the same negative dimension by the negative injection, violating that same bottom lemma unless $`R=1`$. This rules out every nontrivial vertical flat cut.

If a proper normal $`R`$ projects nontrivially to $`T`$, the residual group is a $`3`$-group, hence the pure perfect $`T`$ dies. It kills all $`X_0`$ and all $`A`$ by §1, then all $`[A,I]`$. The remaining $`I/[A,I]`$ is a sum of the nontrivial augmentation modules $`M`$, with zero coinvariants. Only the old one-dimensional quotient of $`Y_0`$ can survive, and both actual stabilizer and section surject, so its cut is strict. Core-freeness follows (a nontrivial normal inside $`H`$ would have a flat vertical cut). The marks generate $`G`$: they give $`Y`$, pure $`T`$, and $`S(D_i(X))`$ for each projective involution. In any group the differences $`x^{-1}i(x)`$ belong to $`D_i(X)`$; the subgroup generated by these differences for the generating involutions is normal in $`X`$, by the difference formula for a product, and is $`T`$-stable since the set of involutions is conjugacy invariant. Its quotient is $`T`$-trivial, hence zero here. The [exact normal-cut theorem](../../sources/foundations/C0001.md) gives a simple loop with faithful left group $`G`$, whole radical $`P`$. Pure base coordinates embed the old non-Moufang example unchanged. Every reflected mark squares into elementary $`Y`$, since its plus coordinate is inverted by its projective involution. Thus the native exponent is exactly six, irrespective of the group exponents of $`A`$ and $`P`$. The host order follows from the additive dimension of (3).

## 3. Native two sheets for noncommuting local units

Use three disjoint cycles of $`w:x\mapsto-1/x`$ to embed $`y\in V`$ as pure $`C`$ entries $`y`$ at the first sites and $`\sigma y`$ at the opposite sites, zero elsewhere. This preserves **ordered** products and addition and sends $`\sigma`$ to actual $`w`$. The three copies meet the additive first-grade condition. In the local $`U_V=1+V`$ take the subgroup

```math
A'=\{g\in U_V:\bar g\,\overline{\sigma g}=1
                              \text{ in }(U_V)_{\mathrm{ab}}\}.
```

Its embedded units belong to $`A`$, have identically zero $`c_*`$, and $`A'`$ is stable under $`\sigma`$. We do **not** assert that the subset $`\sigma g=g^{-1}`$ is a group. On the small subgroup generated by the embedded $`T_V,S(A'),w`$, the actual $`H`$ intersection is exactly $`\{T_{a-1}S(a):a\in A'\}`$, since $`w\notin B`$ and the entire old shear vanishes. It is $`w`$-normalized. On the two physical coset sheets $`T_y w^e`$ the unit action is accordingly $`s\mapsto a s+1-a`$; this is left multiplication by $`a`$ on the variable, not conjugation.

For $`y\in V`$ an odd input, $`a=(1+y)(1+\sigma y)^{-1}`$ satisfies $`\sigma a=a^{-1}`$ and belongs to $`A'`$. The vector $`b=a^{-1/2}(y-1+a)`$ is $`\sigma`$-fixed: $`y-1+a=a(\sigma y-1+a^{-1})`$ is exactly $`1+y=a(1+\sigma y)`$ in characteristic three. Thus $`S(\sqrt a)T_b S(\sqrt a)w`$ truly is a native mark and acts on the small cosets with intercept $`y`$ and linear part $`a\sigma`$. Even inputs are genuine $`T_y`$. This identifies every native cell with (1), not just the ring group. Finite bijectivity gives both divisions. Distinct subgroups of the ambient radical need not be native subloops by this argument.

## 4. Explicit universal radical consequence

For $`m\ge2`$ put $`n=2m-1`$ and let $`V`$ be all strictly upper triangular $`n\times n`$ matrices over $`F`$, under matrix multiplication. Its dimension is $`n(n-1)/2`$, its first radical grade has dimension $`n-1`$, and its two-sided annihilator in $`F1+V`$ is precisely $`F E_{1n}`$. Thus the native host has order

```math
20\cdot3^{138+20n(n-1)-n}.
```

Its faithful characteristic radical contains $`\mathrm{UT}_m(3)`$: put this group on the odd-numbered rows and columns of $`\mathrm{UT}_n(3)`$, identity on all other places. Every elementary generator then has gap at least two and is a commutator in $`\mathrm{UT}_n(3)`$, by an intermediate row. Consequently the whole odd-position copy lies in $`(1+V)'\le(1+N)'`$. Putting it on **one physical site**, with units one at the other nineteen, satisfies (3). This is an injective copy in the actual $`A`$ of the faithful group, unaltered by the diagonal socle quotient. In particular this does not mistake $`g\mapsto(g,g^{-1})`$ for a group homomorphism on a nonabelian group.

Every finite $`3`$-group $`H_0`$ embeds in some $`\mathrm{UT}_m(3)`$. Its regular permutation representation over $`F`$ is faithful and has an invariant unipotent flag: on each nonzero quotient space the number of fixed vectors is divisible by three by orbit counting, so it has a nonzero fixed vector and the flag continues. One may take $`m=|H_0|`$ (the trivial case is immediate). This proves the universal assertion, in fact with one common host for all groups representable in fixed dimension $`m`$. Finally $`\mathrm{UT}_m(3)^{(j)}`$ contains a nontrivial root with index gap $`2^j`$ if $`2^j<m`$, by iterating commutators of adjacent intervals. No uniform derived-length bound for these finite simple loops' faithful radicals is therefore possible.

[Overview and reproducible checks](README.md)
