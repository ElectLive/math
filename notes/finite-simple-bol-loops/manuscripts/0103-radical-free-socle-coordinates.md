# 0103. Recognizing radical-free Bol folders from simple coordinates

**Mira Cult**

Suppose the left multiplication group of a finite simple proper left Bol loop has trivial solvable radical. Its socle is then a product of nonabelian simple groups. Those factors give useful coordinates, but two natural shortcuts do not work: a point stabilizer need not be the product of its projections, and the canonical inversion need not preserve a normal subgroup on which one wants to test simplicity.

**Theorem.** The data and tests (1)–(8) below recognize exactly the faithful generated simple left-Bol folders with radical-free left group. They also give an ordinary loop-isomorphism criterion and an explicit non-Moufang test. The input uses a list of simple groups, arrows between them, an arbitrary outer permutation group, actual stabilizer cosets and a conjugacy-invariant choice of involution classes. A quotient cut can be evaluated without building the normal subgroup lattice of the original group. The point stabilizer is not assumed to split, and neither is the extension by the socle.

An application at the end shows that some rotations of order $`p^e`$ cannot have a lift of that order in the point stabilizer. [The complementary elementary descent](0102-canonical-elementary-descent.md) handles the case of nontrivial solvable radical. Between them the two methods test data in either branch; they do **not** give a structural list of the data that pass. We use the [faithful canonical left folder and normal-subloop criterion](../sources/foundations/C0001.md) and [canonical inversion, Theorem 1.1(1)](../sources/foundations/C0007.md).

## Simple coordinates and actual outside marks

Fix $`S=\prod_{i\in I}T_i`$ for a nonempty finite list of nonabelian finite simple groups. Identify $`S`$ with its inner automorphism group, put $`\mathcal{A}=\operatorname{Aut}(S)`$, $`\mathcal{O}=\mathcal{A}/S`$, and choose $`B\le\mathcal{O}`$. Set $`G=\pi^{-1}(B)`$ in $`\mathcal{A}`$. An element $`x`$ of $`\mathcal{A}`$ is a permutation $`\pi_x`$ of isomorphic factors, with an arrow $`x_i:T_i\to T_{\pi_x i}`$. Multiplication means composition, applying the right-hand arrow first. An outer element specifies the permutation and each arrow up to inner automorphisms.

These are precisely the nontrivial finite groups with trivial solvable radical. Indeed their socles are direct products of nonabelian simple groups; the socle centralizer is trivial, since any nontrivial normal centralizer would contain a minimal normal subgroup meeting the centerless socle. Conversely each nontrivial normal of the displayed $`G`$ meets $`S`$ nontrivially for the same centralizer reason. A subgroup normal in $`S`$ is a product of full coordinate factors: a nontrivial projection yields that factor by commutators with the supported simple group. Consequently the products over individual $`B`$-orbits are exactly the minimal normals; the socle is $`S`$ and the radical is trivial. The restriction $`\alpha`$ of an automorphism of $`G`$ to this characteristic socle determines that automorphism: $`g`$ is identified with its conjugation on $`S`$, so its image must be $`\alpha g\alpha^{-1}`$. Conversely every $`\alpha`$ normalizing $`G`$ gives an automorphism.

Choose $`\alpha\in N_\mathcal{A}(G)`$ with $`\alpha^2=1`$, allowing identity. Model the formally extended group with both signs in $`\mathcal{A}\times C_2`$: its elements are $`(G,0)`$ and $`(G\alpha,1)`$, its distinguished involution is $`t=(\alpha,1)`$. Do **not** identify the second copy with the first if $`\alpha\in G`$. We describe an outside mark by its first coordinate $`a\in G\alpha,\;a^2=1`$; this coordinate can be identity.

For an outer label $`u\in B\bar\alpha,\;u^2=1`$, write $`\rho`$ for its permutation. For each $`\rho`$-fixed $`i`$, choose one $`T_i`$-inner-conjugacy class $`\mathcal{C}_i`$ of actual $`\gamma\in\operatorname{Aut}(T_i)`$ with $`\gamma^2=1`$ and outside arrow prescribed by $`u_i`$. If none exists, there is no class with that choice. On a transposition $`i,j`$ there is just one local orbit: choose any arrow in the prescribed inner coset and its inverse on the return leg. Independent inner conjugation at the two ends ranges over all $`|T_i|`$ choices. This gives all $`S`$-conjugacy classes of marks above $`u`$, exactly once. The weight of the complete decorated label $`\lambda=(u,(\mathcal{C}_i))`$ is

```math
w(\lambda)=\prod_{\{i,j\}\text{ exchanged by }\rho}|T_i|
                       \prod_{\rho i=i}|\mathcal{C}_i|.                     \tag{1}
```

Select **any** set of such labels stable under transport by $`B`$ and $`\bar\alpha`$, containing the actual decorated class of $`\alpha`$. Lifts in $`\mathcal{A}`$ give a well-defined transport of classes because the inner group is already divided out. The resulting union $`\Lambda`$ of signed marks is exactly a conjugation-invariant outside set containing $`t`$. Fixed-coordinate class labels in a single tuple need not be independently selectable. Put $`K=t\Lambda`$.

## Stabilizers, generation and faithfulness

A stabilizer is specified by $`A\le S,\;J\le B`$ and actual lifts $`n_j`$ of $`j\in J`$, with $`n_1=1`$, normalizing $`A`$ and satisfying $`n_j n_k n_{jk}^{-1}\in A`$. Then $`H=\bigcup_{j\in J}A n_j`$ is a subgroup, $`H\cap S=A`$, $`\pi H=J`$, and $`|H|=|A||J|`$. Conversely take representatives in $`H`$. Choices differing inside these actual cosets are identical data. Equivalently one can choose sections in $`N_G(A)/A`$; a complement in $`G`$ is not assumed. If the input is to be generated recursively rather than by a subgroup list for a power, every $`A`$ is obtained by adjoining one coordinate at a time by Goursat: choose its old projection $`D`$, new projection $`F\le T_i`$, normal subgroups $`D_0,F_0`$, and an isomorphism $`D/D_0\simeq F/F_0`$, taking their fiber product. The kernels and quotient isomorphism recover from the subgroup. This reduces the enumeration of $`A`$; it does not promise efficient classification of the sections.

The core of $`H`$ is trivial precisely when $`A`$ contains no product of all factors in a $`B`$-orbit. For generation call a coordinate *active* if at least one selected mark moves that factor or restricts there to a nonidentity automorphism. This is read directly from its decorated label. Then

```math
S\cap\langle K\rangle=\prod_{i\;\mathrm{active}}T_i,\qquad
 \langle K\rangle=G\;\Longleftrightarrow\;
  \langle\,\bar\alpha u:u\text{ selected}\,\rangle=B
                 \text{ and every coordinate is active}.              \tag{2}
```

Indeed $`L=\langle K\rangle=\langle\Lambda^2\rangle`$ is normal in $`G`$, since $`K=t\Lambda\subseteq\Lambda^2=K^{-1}K`$ and the latter is conjugation-invariant. If $`a`$ acts nontrivially on $`T_i`$, choose $`s\in T_i`$ so that the product of $`a`$ with its $`s`$-conjugate has a nonidentity $`i`$-coordinate. If the factor is moved this holds for any nonidentity $`s`$; if it is fixed choose one not fixed by $`a`$. This product belongs to $`L\cap S`$, so normality gives the whole factor. An inactive factor is centralized by every mark and hence by $`L`$, so no element of $`L\cap S`$ has a nontrivial coordinate there. This proves (2) without a subgroup-lattice search.

## Marked-square membership from cycle transport

For each nonidentity **actual** $`h\in H`$ and each ordered pair of selected decorated labels $`\lambda,\mu`$ with outer labels $`u,v`$ and $`\bar h=uv`$, test whether $`h=ab`$ with $`a,b`$ in these two physical classes. Write $`\sigma=\pi_h,\;\rho=\pi_u`$. Necessarily $`\rho\sigma=\sigma^{-1}\rho`$, also forced by $`u^2=v^2=1`$. The cycles of $`\sigma`$ are therefore paired by $`\rho`$ or individually preserved. On each orbit of these cycles, choose a base point $`i`$ in a cycle of length $`m`$. Test the $`|T_i|`$ possible arrows $`A_i:T_i\to T_{\rho i}`$ in the inner coset $`u_i`$. Set along that cycle

```math
A_{\sigma^k i}=(h^{-k})_{\rho i} A_i ((h^k)_i)^{-1},\qquad
 A_i(h^m)_i A_i^{-1}=(h^{-m})_{\rho i}.                              \tag{3}
```

The second equation is the closure condition. If the reversed cycle is distinct put $`A_{\rho j}=A_j^{-1}`$ on it. In either case require $`A_{\rho j}A_j=1`$, the prescribed outer arrow $`u_j`$, and the reversing recurrence (3) at every position. For a fixed point of $`\rho`$, test $`A_j\in\mathcal{C}_j(\lambda)`$; for a fixed point of $`\rho\sigma`$, test $`A_{\sigma j}h_j\in\mathcal{C}_j(\mu)`$.

This one pair of labels contains $`h`$ in its product **if and only if every cycle component succeeds**, not if just one succeeds. In fact $`a h=h^{-1}a`$ and $`a^2=1`$ are exactly (3) and the inverse conditions. They force $`b=ah`$ to be an involution with outer label $`u\bar h=v`$. The tests at fixed coordinates impose exactly its class decoration; transposed pairs carry no further conditions by (1). Conversely the independently chosen successful arrows on disjoint components assemble an actual $`a`$; the entire tuples $`\lambda,\mu`$ were fixed before making the choices. On a pair of distinct cycles there are no fixed-coordinate tests. On a self-reversed cycle write $`\rho(\sigma^j i)=\sigma^{s-j}i`$: the two decorations concern $`2j=s`$ and $`2j=s-1`$ modulo $`m`$, respectively. There are only two such conditions in total, even for $`m=1`$ when both concern the same point. This is a local map search, not an assertion that separate stabilizer projections can be tested independently for every $`h`$.

Require that no nonidentity $`h`$ succeeds for any pair of selected labels. Together with

```math
\sum_{\lambda\;\mathrm{selected}} w(\lambda)
                                = |G|/(|A||J|),                         \tag{4}
```

this is exactly sharp transversality at $`H`$ and all its conjugates. Namely $`K^{-1}K=\Lambda^2`$ is invariant. Also $`K`$ contains 1, is inverse-closed under conjugation by $`t`$, and is sandwich-closed since conjugating the mark $`t l`$ by $`t k`$ gives $`t(k l^{-1}k)`$. This constructs the left Bol folder on $`G/H`$.

## All true normal cuts, including non-inversion-stable ones

Let $`D\subseteq I`$ be any union of $`B`$-orbits, $`C=I\setminus D`$, and $`S_D=\prod_{i\in D}T_i`$. Put

```math
B_D=\{b\in B:b\text{ fixes every coordinate in }C
                 \text{ with identity outer arrow there}\}.
```

For every $`B'\lhd B`$ with $`B'\le B_D`$, set

```math
N(D,B')=\{g\in G:\bar g\in B',\quad g|_{S_C}=1\}.
                                                                        \tag{5}
```

These are **all** normal subgroups of $`G`$, each exactly once. Indeed for any such $`N`$, write $`N\cap S=S_D`$. The commutator $`[N,S_C]`$ lies in this intersection and in $`S_C`$; it is trivial. Thus $`B'=\pi N`$ lies in $`B_D`$, and $`N`$ lies in (5). Conversely (5) is normal, two kernels being intersected. Every $`b\in B'`$ has a representative acting by an inner automorphism on $`S_C`$; multiply by the inverse inner action from this very factor to get a representative centralizing $`S_C`$. The kernel is $`S_D`$. Hence $`|N(D,B')|=|S_D||B'|`$, giving equality for the original $`N`$ as well. There is no requirement that $`\alpha D=D`$ or that $`B'`$ be normal in the group generated by $`B,\bar\alpha`$.

For this cut, let $`A_C`$ denote the restriction of $`A`$ to $`S_C`$ as inner automorphisms. Then

```math
|H\cap N|=|A\cap S_D|\,
 \big|\{j\in J\cap B': n_j|_{S_C}\in A_C\}\big| .                    \tag{6}
```

For such $`j`$, either the coset $`An_j`$ has no representative acting trivially on $`S_C`$, or the set of them has exactly the kernel size $`|A\cap S_D|`$. This argument keeps the actual stabilizer cosets, not just $`J`$.

Give each selected label $`\lambda=(u,(\mathcal{C}_i))`$ the following **cut signature**:

```math
\left((\bar\alpha u) B',\;
                  (\mathcal{C}_i:\;i\in C,\;\pi_u i=i)\right).
```

If first entries coincide, the outer arrows and permutations of $`u`$ agree on $`C`$, since $`B'`$ acts outer-trivially there. A signature has weight

```math
w_C(\lambda)=\prod_{\substack{\{i,j\}\;{\rm exchanged\;by}\;\pi_u\\;
                                  \{i,j\}\cap C\ne\varnothing}}|T_i|\;
                   \prod_{\substack{i\in C\\\pi_u i=i}}|\mathcal{C}_i| .
```

Then the exact number of images of genuine translations in $`G/N`$ is

```math
|KN/N|=\sum_{\text{distinct signatures}} w_C .
                                                                        \tag{7}
```

To see this, the map $`g\mapsto(\bar g B',g|_{S_C})`$ has kernel (5). For $`g=t a`$, the second coordinate is determined bijectively by the restriction $`a:S_C\to S_{\alpha C}`$, even when $`\alpha C\ne C`$. A transposition with **either one or two** endpoints in $`C`$ contributes precisely $`|T_i|`$ distinct restricted maps; it contributes no factor when both are outside. Fixed retained coordinates contribute exactly their chosen inner class sizes. The retained maps are attained independently within each physical $`S`$-orbit: inverse arrows are the only coupling on a transposition. Labels giving the same signature therefore have literally identical images, not just the same count. Different signatures have disjoint images by their top or a disjoint fixed-coordinate class. This proves (7), including $`C=\varnothing`$, $`B'\ne1`$ and cuts which split marked transpositions.

For every $`1<|S_D||B'|<|G|`$ impose the strict test

```math
\sum_{\text{distinct signatures}}w_C
       > { |G|\,|H\cap N| \over |A||J|\, |S_D||B'|}.                  \tag{8}
```

The right-hand side is $`[G:HN]`$. In a faithful generated folder this is exactly the [strict normal-cut criterion](0102-canonical-elementary-descent.md), which does not presume $`G/N`$ is a loop: equality gives a genuine quotient loop by transversality of the projected translations, and a proper loop congruence supplies an equality cut via the kernel of its induced action. If $`HN=H`$ core-freeness rules out nontrivial $`N`$; if $`HN=G`$ equality would put $`K`$ in $`N`$, contrary to generation.

This gives a full **simple-left-Bol** recognition condition. To restrict to **proper** loops, discard $`H=1`$, which makes the transitive action regular and the loop a group. If $`G`$ is not simple the remaining simple loops are automatically non-Moufang: the Moufang identity makes the left group normal in the full multiplication group, and a nonassociative finite simple Moufang loop has simple full multiplication group by [Nagy and Vojtěchovský, Corollaries 4.7 and 6.8](https://arxiv.org/pdf/math/0701707). If $`G`$ is simple, do not use that argument to discard it: in this case one can test the Moufang identity $`(xy)(zx)=x((yz)x)`$ directly on $`G/H`$, using the unique $`k\in K`$ for a coset to multiply on its left. Equivalently, remove the genuine canonical folders of the known Paige loops using the same isomorphism criterion. No new almost-simple operation classification is being inferred.

Two admitted data give isomorphic loops exactly when a single isomorphism of their socles, permuting isomorphic factors and intertwining their arrows, conjugates the outer subgroup $`B`$ to $`B'`$ (of the other data), $`\alpha`$ to $`\alpha'`$, all actual stabilizer cosets collectively onto $`H'`$, and the full selected decorated classes onto those of the other datum. In one direction the group isomorphism and coset bijection intertwine the actual left translations. Conversely a loop isomorphism fixes the identity point, conjugates the generated left groups, carries the original translations and stabilizer, and conjugates the unique inversion automorphism. Restrict to the characteristic socle. Faithfulness of $`G\hookrightarrow\mathcal{A}`$ and the automorphism argument above force exactly this single coordinate transport. This is ordinary loop isomorphism, not an independent relabeling of projection factors, a marked-socle isomorphism, or isotopy.

## A structural obstruction: the point stabilizer cannot lift certain top elements at their own order

Let $`j\in B`$ have order $`m`$, and consider **order-$`m`$** lifts of $`j`$. For each cycle $`c`$ of its permutation of coordinates, write $`l=|c|`$, choose $`i\in c`$, and put $`o_c=(j^l)_i\in\operatorname{Out}(T_i)`$. The $`S`$-conjugacy classes of order-$`m`$ lifts are in bijection with the product, over these cycles, of the $`T_i`$-classes of actual automorphisms

```math
\xi\;\text{over }o_c,\qquad \xi^{m/l}=1 .               \tag{9}
```

An empty choice on even one cycle means there is no such lift. Indeed the holonomy $`(h^l)_i`$ of the ordered arrows along a cycle is conjugated by the inner coordinate conjugator at its base point. Conversely two lists of prescribed-outer arrows whose holonomies are inner-conjugate are conjugate by an element of $`S_c`$: start with the given base inner conjugator and propagate it along each arrow; the neighboring conjugator is again inner because the two arrows have the same outer coset, and closure is exactly the holonomy equality. Arbitrary intermediate arrows may be chosen and the last adjusted within its inner coset to realize any allowed $`\xi`$. The order condition (9) is sufficient since $`h^m=1`$ and its projection already has order $`m`$. A tuple has exactly $`\prod_c |T_i|^{l-1}[T_i:C_{T_i}(\xi)]`$ elements, by the same free intermediate arrows. This is a classification of the indicated group lifts, not of all Bol loops.

In particular if

```math
\gcd(m/l,\;|T_i|)=1\quad\text{for every }c,       \tag{10}
```

there is exactly **one** $`S`$-class of order-$`m`$ lifts. In the inverse image of $`\langle o_c\rangle`$ in $`\operatorname{Aut}(T_i)`$ the inner group is normal Hall, since $`|o_c|\mid m/l`$. Schur–Zassenhaus gives a complement and conjugacy of complements by the inner group (the quotient is cyclic, hence soluble). Any lift satisfying (9) lies in such a complement: its order divides $`m/l`$, so its cyclic group meets the inner kernel trivially, and projects onto $`\langle o_c\rangle`$. With the projection $`o_c`$ fixed, conjugacy of complements gives conjugacy of the individual lifts. The case $`l=m`$ needs no coprimality with $`|T_i|`$: its holonomy is forced to be identity.

Now suppose $`1\ne j\in J`$, (10) holds, and the product of **two actual selected marks** over $`j`$ has order exactly $`m`$. The stabilizer can contain **no** order-$`m`$ lift of $`j`$, because its unique $`S`$-class lies in the conjugation-invariant marked square. Thus $`\gcd(m,|A|)>1`$: otherwise Schur–Zassenhaus in the inverse image of $`\langle j\rangle`$ in $`H`$ would give such a lift. If $`m=p^e`$ is a prime power, every lift of $`j`$ in $`H`$ has order divisible by $`p^{e+1}`$. Otherwise kill its prime-to-$`p`$ order part and raise by an inverse exponent modulo $`p^e`$ to obtain an order-$`p^e`$ element over $`j`$. In particular when $`j`$ acts semiregularly with all cycles of length $`m`$, any pair of plain selected permutation marks whose actual product is $`j`$ forces this excess torsion, even if $`p`$ divides the simple factor orders. This is not an assertion that arbitrary projected marked collisions are genuine, or that every word of order $`m`$ in the outer quotient lifts at that order inside the point stabilizer.


### An unconditional semiregular lift for odd order

Suppose $`j`$ has **odd** order $`m>1`$, every one of its factor cycles has length $`m`$, and some actual selected mark $`a`$ has outer action $`u j u^{-1}=j^{-1}`$. There is an actual $`g\in G`$ over $`j`$, of order $`m`$, with $`a g a=g^{-1}`$. No splitting of $`G`$ over $`S`$, coprimality of $`m`$ with $`|S|`$, or prescribed field/diagonal arrows of $`j`$ are needed.

Here the arrows of $`a`$ are the actual involutive arrows, not merely outer labels. Write $`\sigma=\pi_j`$. First take one $`\sigma`$-cycle preserved by $`\pi_a`$. A reflection of an odd cycle has exactly one fixed point $`i`$. Index the points by $`i_k=\sigma^k i`$, $`k\bmod m`$. Choose $`P_0=1`$, and for each pair $`k,-k\ne0`$ choose one isomorphism $`P_k:T_i\to T_{i_k}`$ with outer arrow $`(j^k)_i`$; define

```math
P_{-k}= a_{i_k} P_k (a_i)^{-1}.
```

This definition is consistent when applied twice since $`a^2=1`$; the outer arrow is the required one since $`u j^k u^{-1}=j^{-k}`$. Define $`g_{i_k}=P_{k+1}P_k^{-1}`$, cyclically. The actual arrows telescope to identity after $`m`$ steps; they give the prescribed $`j`$, and $`a`$ conjugates them to their inverses with reversed direction. If two distinct cycles are exchanged by $`\pi_a`$, choose $`i`$ in the first, $`i'=a(i)`$ in the second, and arbitrary $`P_k`$ on the first, with $`P_0=1`$. Put $`P'_{-k}=a_{i_k}P_k(a_i)^{-1}:T_{i'}\to T_{\sigma^{-k} i'}`$ on the second and use the same successive-arrow construction on both cycles. No fixed-point class comparison is required. Assemble over the disjoint cycle orbits; the order is exactly $`m`$ from its top. For even $`m`$ a self-reversed cycle can have two different fixed-coordinate actual classes; this argument is expressly not asserted there.

Both $`a`$ and its $`g^r`$-conjugate are actual selected marks. Their product is $`g^{2r}`$ or $`g^{-2r}`$ according to conjugation convention. As $`m`$ is odd the whole cyclic group $`\langle g\rangle`$ lies in $`\Lambda^2`$. By (9), *every* order-$`m`$ lift of $`j`$ is in the same $`S`$-class. Consequently if $`j\in J`$, the preceding excess-order obstruction holds **without hypothesizing any marked product separately**.

### Every semiregular odd top prime must recur in an abelian quotient

If the top $`B=G/S`$ is abelian, then $`J=B`$. Otherwise $`J`$ is proper normal in $`B`$, $`N=\pi^{-1}J`$ is proper nontrivial normal in $`G`$, and $`H\le N`$; the strict cut (8) is impossible because $`|KN/N|\le |G/N|=[G:HN]`$. Also $`\bar\alpha`$ inverts every element of $`B`$: it inverts each projected actual translation and these generate the abelian quotient. Since $`t`$ itself is a selected mark, the preceding semiregular theorem applies to **every** odd-order element of $`B`$ with all factor cycles of full length.

In particular, if such an element $`j`$ has order $`m=p^e`$, *every* stabilizer lift of $`j`$ has order divisible by $`p^{e+1}`$. More specifically $`A=H\cap S`$ contains an element of order $`p`$ whose nonempty support is a union of complete $`j`$-cycles. To see this, choose a $`p`$-power-order lift $`h\in H`$ over $`j`$: remove the prime-to-$`p`$ part of an arbitrary lift by powering, then restore its top using an inverse exponent modulo $`m`$. The order of $`h`$ is $`p^b,\;b>e`$. Its element $`h^{p^{b-1}}`$ has order $`p`$, lies in $`A`$, and is centralized by $`h`$, so nonidentity coordinates propagate around every cycle they meet. The order-$`p`$ entries on a given active cycle are intertwined by the actual coordinate maps of $`h`$. For a semiregular abelian top action this forces the **particular** odd prime $`p`$ attached to each top rotation to recur on at least $`p^e`$ socle coordinates and in a single actual stabilizer element. It does not force those coordinates to carry independent Sylow subgroups.

The [cyclic wreath construction](../sources/factor-permutation/radical-free-factor-permutation-construction.md) gives nonvacuous instances with $`B=C_p`$, including $`T=A_5,\;p=3`$. Its stabilizer has a lift of the top with order exactly nine: use the pure rotation on the $`Y_0`$-side and a decorated rotation (or its inverse to match the prescribed signed tops) with a single order-three $`A_4`$ decoration of nonzero character on the $`Y_1`$-side. Its cube has the same nonidentity order-three contribution at all three coordinates of that cycle. Thus the additional prime exponent is genuinely needed, and larger excess is not forced in every example. This does not classify all such stabilizers.

**Boundary.** In $`A_5^3\rtimes\langle(12)\rangle`$, the plain top transposition and its product with a nonidentity involution on the fixed third factor both have order two and the same top. They are not conjugate by the base: their fixed-coordinate holonomies differ. Thus dropping the shorter-cycle condition from the one-class assertion is not safe. Oddness in the reversible-lift construction is also real: on two A₅ factors let the top swap them, and choose the actual factor-preserving involution with identity on the first and a nonidentity inner involution on the second. It reverses the order-two top in the outer quotient, but no involutory swapping lift commutes with it: each such lift intertwines the two fixed-coordinate actions, which are not isomorphic. These are group controls, not assertions of loop existence. The [exact finite controls](../sources/code/verify_socle_component_transport.py) test class sizes, reversal with fixed and paired cycles, non-inversion-stable cut signatures, actual outer arrows and the order-lift boundary. The checker compares 1,800 actual pair-product decisions, including fixed and exchanged reversal cycles; verifies every normal in the true radical-free model S₅×S₅ and its diagonal stabilizer; and exercises odd dihedral lifts with genuine outer arrows. The controls with A₄ factors are auxiliary centerless tests, not simple factors in the theorem. The separately written [cycle and cut controls](../sources/code/check_671_socle_cut_holonomy.py) include projected false positives that vanish once actual cosets are used. The [evidence record](../normal-layer-evidence.md) gives the exact source and review scope. An open structural question is which outer groups and stabilizer subgroups can survive the cut and paired-class tests simultaneously.
