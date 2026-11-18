# 0105. Proper stabilizer projections on a nilpotent transitive socle

**Mira Cult**

When a simple left Bol loop has several isomorphic nonabelian simple factors in the socle of its left multiplication group, the point stabilizer could appear to project either trivially or onto a whole simple factor. A transitive nilpotent action on the factors rules out both extremes. The proof first shows that a subdirect stabilizer intersection would have to be a single diagonal, then counts the actual translations lying over that diagonal.

**Theorem.** Let $`G`$ be the faithful canonical left multiplication group of a finite simple proper left Bol loop, $`H`$ its actual point stabilizer, and suppose the **entire socle** is $`S=T^\Omega`$, with $`T`$ any finite nonabelian simple group and $`n=|\Omega|\ge2`$. Suppose the permutation image $`C`$ of $`G`$ on the simple factors is transitive and nilpotent. Then

```math
1< U_i:=\pi_i(H\cap S)<T_i
\qquad\text{for every }i\in\Omega.                  \tag{1}
```

The groups $`U_i`$ are equivalent under the actual coordinate transports of $`H`$. The action need not be regular; the full top $`B=G/S`$ need not be nilpotent; its coordinate kernel is unrestricted; $`H`$ need **not** map onto $`B`$. In particular the result concerns the genuine layer intersection before projection, not arbitrary projections of $`H`$. We give a quantitative lower bound below. The theorem eliminates the trivial- and full-projection branches, **not** every such canonical group. Proper correlated $`U_i`$, multiple coordinate orbits, nonnilpotent actions and the unrestricted structural classification remain open in general.

We first prove a separate normal-layer obstruction without nilpotence, without assuming radical-freeness, and without any condition on $`\operatorname{Out}(T)`$. The key is to test every selected involution on the actual components of a strip partition, including when coordinate stabilizers are nonnormal. The counting argument then needs only the translations in $`SH`$, not all lifts of a coordinate permutation.

## A true normal layer: strips in a nonregular transitive action

Use the [canonical left-folder, generation and simple normal-cut conditions](../sources/foundations/C0001.md) and [formal inversion](../sources/foundations/C0007.md): $`E=G\rtimes\langle t\rangle`$, $`t`$ acts on $`G`$ by the canonical involutory automorphism (possibly trivial), $`\Lambda=tK`$ is an invariant set of outside involutions containing $`t`$, $`K`$ generates $`G`$ and is a left transversal to $`H`$, and $`H\cap\Lambda^2=\{1\}`$. We keep the formal sign even if the coordinate action of $`t`$ is already in $`G`$. If $`1<N\lhd G`$ with $`H\le N<G`$, quotienting by $`N`$ makes the images of $`K`$ exactly all of $`G/N`$ with trivial point stabilizer **as a set of translations**; equivalently equality holds in the normal-cut cardinality test. Simplicity forbids this. Thus if a nilpotent quotient $`C`$ has a nontrivial kernel, $`H`$ maps onto $`C`$: otherwise its image is contained in a normal maximal subgroup of $`C`$, and the preimage is such a forbidden $`N`$.

Let $`N=\prod_{i\in\Omega}T_i\le G`$ be normal in $`E`$, the $`T_i`$ isomorphic to $`T`$ as above, $`C`$ the transitive permutation image of $`G`$. Assume $`W=H\cap N`$ is subdirect. It is then a direct product of twisted full diagonals on disjoint strips partitioning $`\Omega`$. Briefly, by induction append one coordinate $`T`$ to a product of prior full strips. Goursat either adds $`T`$ independently or identifies it with a simple quotient of that product. A surjection from a direct product of simple groups onto $`T`$ is an automorphism on one factor and trivial on the others, because the commuting normal images cannot include two copies of nonabelian $`T`$. The partition is intrinsic: a two-coordinate projection is a graph exactly when the two coordinates belong to one strip. The partition is $`H`$-invariant. Assume in this normal-layer assertion only that **$`C`$ preserves the strip partition**; this is automatic when $`H`$ induces $`C`$, hence for nilpotent $`C`$ since $`N`$ is in the permutation kernel. No assertion replaces $`H\cap N`$ by a projected copy of a larger stabilizer intersection.

For any selected $`a\in\Lambda`$, form the graph on $`\Omega`$ joining coordinates in one strip and coordinates paired by the permutation of $`a`$. **Every connected component contains an $`a`$-fixed coordinate.** Otherwise take the nonidentity involution class of $`T`$ invariant under $`\operatorname{Aut}(T)`$ furnished by Fried–Guralnick–Saxl, *Schur covers and Carlitz's conjecture*, [Lemma 12.1, §12 p. 26](https://www.math.uci.edu/~mfried/paplist-ff/sch-carlitz.pdf) (CFSG). Put one representative on each full strip of the offending component with its prescribed diagonal twists, and identity on all other strips. This gives an actual $`1\ne w\in W`$. All entries on the component belong to that same inner conjugacy class in transported coordinates; we do **not** assume $`T`$ has only one involution class. On each transposed pair the two entries are inverse-conjugate after transport through its actual $`a`$-arrow. This is precisely the paired constraint for the product of two $`N`$-conjugates of $`a`$: their first arrows may independently vary over the prescribed inner coset, their return arrows being inverses. On fixed sites outside the component the two identical fixed arrows give identity; identity is likewise allowed on the other pairs. Choices are independent across cycles for the one chosen $`N`$-class, so $`w\in(a^N)^2\subseteq\Lambda^2`$, contrary to avoidance. This is an equality of actual elements in $`N`$: products of two such conjugates are already in $`N`$, whose action on itself is faithful. See also [the marked nonabelian layer calculation](0103-radical-free-socle-coordinates.md#marked-square-membership-from-cycle-transport).

In particular $`t`$ fixes a coordinate. Choose it as origin, write $`\Omega=C/P`$ for left cosets, and let $`\theta(c)=tct^{-1}`$ on the faithful permutation image $`C`$. Then $`\theta(P)=P`$ and $`t(xP)=\theta(x)P`$. The strip block through the origin is $`M/P`$ for $`P\le M\le C`$; the other blocks are $`xM/P`$. Indeed the preimage in $`C`$ of the origin block is its setwise stabilizer by block invariance. Every selected mark fixes a coordinate and can be conjugated by $`G`$ to fix the origin. The resulting **signed coordinate label** has form $`pt`$, $`p\in P`$; different selected labels at the origin are allowed and need not be conjugate to $`t`$. Its action sends $`xP`$ to $`\eta(x)P`$, where $`\eta=\operatorname{inn}(p)\theta`$. Because $`p\in P\le M`$, the subgroup

```math
U=\langle M,\theta(M)\rangle
=\langle M,\eta(M)\rangle
```

is invariant under $`\eta`$: the signed coordinate action squares to one, whence $`p\theta(p)=1`$ in the faithful $`C`$. Strip steps are right multiplications by elements of $`M`$ on representatives; conjugating them by $`\eta`$ allows right multiplications by $`\eta(M)`$. Thus the exact component of $`xP`$ is

```math
xU/P\;\cup\;\eta(x)U/P.
```

If these were distinct, the signed mark would interchange the two sets and have no fixed coordinate there. Therefore $`x^{-1}\eta(x)\in U`$ for every $`x`$. Apply this both to $`p=1`$ (the distinguished mark) and to **each** selected $`pt`$ at the origin. From

```math
x^{-1}p\theta(x)p^{-1}\in U,\qquad x^{-1}\theta(x)\in U,\qquad p\in U
```

we deduce $`x^{-1}px\in U`$ for all $`x`$. The coordinate image of an original translation from a conjugate $`x(pt)x^{-1}`$ is

```math
t[x(pt)x^{-1}]
=\theta(xp)x^{-1}
=\bigl(\theta(xp)(xp)^{-1}\bigr)\,\bigl(xpx^{-1}\bigr)\in U .
```

The first term is in $`U`$ by applying the distinguished-mark condition to $`(xp)^{-1}`$ and inverting. All original translations are covered, since a lift of any coordinate conjugator belongs to $`G`$ and preserves selection; their images generate $`C`$. Hence

```math
C=\langle M,\theta(M)\rangle,\qquad C=M[C,C],\qquad
C=P[C,C]C^2.                                                        \tag{2}
```

Here $`C^2`$ denotes the subgroup generated by squares. To see the last two statements, $`\theta`$ inverts each original translation image, hence induces inversion on $`C_{\mathrm{ab}}`$. Thus the images of $`M,\theta(M)`$ in that quotient coincide. Modulo $`[C,C]C^2`$, $`\theta`$ is identity and every displayed translation has image that of $`p\in P`$.

If $`[M:P]=2`$, then $`P`$ must normally generate $`C`$. Its normal closure $`R`$ is $`\theta`$-stable. The first equality in (2) exhibits $`C/R`$ as generated by two elements of order dividing two. If nontrivial such a finite group has a quotient of order two: it is cyclic of order two or a quotient with the usual dihedral presentation, and a nontrivial group genuinely generated by two involutions cannot be a nontrivial odd cyclic rotation quotient. More explicitly, if neither generator lies outside their cyclic product subgroup then it is cyclic with at most one involution; otherwise that product subgroup is normal of index two. A quotient of order two killing $`P`$ contradicts the third equality in (2). This does **not** assert the impossibility of two-coordinate strips for every nonregular $`C`$.

For **nilpotent** $`C`$, the second equality forces $`M=C`$, since any proper $`M`$ lies in a normal maximal subgroup containing $`[C,C]`$. So the only possible subdirect $`W`$ is one full diagonal. Furthermore, $`n=[C:P]`$ is odd: if $`n`$ is even the Sylow 2-factor of $`P`$ is proper in that of $`C`$; place it in a maximal subgroup of the latter and extend by the other Sylow factors. This gives an index-two normal subgroup containing $`P`$, contradicting (2). In even degree subdirectness is therefore impossible on this general normal layer, not just on a whole socle.

## Counting the actual stabilizer fiber, not the entire outer group

Now take $`N=S=\operatorname{Soc}(G)=T^\Omega`$, nilpotent transitive $`C`$, $`n\ge2`$. Such $`G`$ has trivial radical: a nontrivial solvable normal would contain an abelian minimal normal in the socle. Its conjugation action on the centerless socle is faithful, because any nontrivial normal centralizer would contain a minimal normal of $`G`$ in the center of $`S`$. We can thus use the [reviewed radical-free coordinates and true mark fibers](0103-radical-free-socle-coordinates.md). Let $`L=|T|`$, $`B=G/S`$, $`A=H\cap S`$, $`J=HS/S`$, and

```math
I=\big|\{\gamma\in\operatorname{Aut}(T):\gamma^2=1\}\big|
```

**including the identity**. The surjection $`H\to C`$ makes all $`\pi_i(A)`$ equivalent under actual coordinate transports. If any is full then all are. The layer result forces $`n`$ odd and $`A`$ a single full strip, which we rectify to $`\Delta(T)`$ by changing coordinate frames. An element normalizing $`\Delta(T)`$ has identical actual local automorphisms at every site, irrespective of its permutation. In particular $`J`$ is contained in the constant outer group times $`C`$. **Nothing implies this for $`B`$.**

By original transversality, exactly $`[SH:H]=[S:A]=L^{n-1}`$ translations lie in $`SH`$. The associated marks $`t(K\cap SH)`$ lie over $`\bar\alpha J`$, where $`\alpha`$ is conjugation by $`t`$ on $`S`$. This restricted set need not be conjugation-invariant. Its permitted coordinate permutations lie in the coordinate coset $`tC`$; all actual ones have $`s\ge1`$ fixed points by the earlier graph argument. Given one such permutation, there are at most

```math
L^{(n-s)/2}\,I^s                          \tag{3}
```

restricted marks. Indeed two outer labels in $`\bar\alpha J`$ over this permutation differ on the right by an element of $`\ker(J\to C)`$, a constant outer automorphism. Therefore fixing an actual arrow at even one fixed position fixes that outer label: multiplying by a constant outer arrow acts freely on the right on any one prescribed outer arrow. There are at most $`I^s`$ choices for the full vector of fixed arrows; after these choices each exchanged pair has $`L`$ choices for one actual arrow in its now fixed outer coset, the other being its inverse. No product assumption on selected classes, no splitting, and no surjectivity of $`H\to B`$ enter (3).

A finite transitive faithful nilpotent permutation group of odd degree has odd order: its normal Sylow 2-subgroup has orbits of equal power-of-two size dividing that degree, so fixes every point. Choose a maximal subgroup $`C_0`$ containing $`P`$. It is normal of prime index $`p\ge3`$; it is $`\theta`$-stable because $`\theta`$ is inversion on $`C_{\mathrm{ab}}`$. The $`p`$ blocks $`C/C_0`$ each have size $`n/p`$. Every element of the signed coset $`tC`$ acts there by an affine inversion, which fixes exactly one of these odd-prime-many blocks, so $`s\le n/p\le n/3`$.

For later use write $`C=\prod C_\ell`$ as a product of Sylow groups, put $`n_\ell=[C_\ell:P\cap C_\ell]`$. Its coset action is a product, $`n=\prod n_\ell`$, because $`P`$ is a product of its Sylow intersections. Faithfulness embeds each $`C_\ell`$ in $`\operatorname{Sym}(n_\ell)`$; its order is at most $`\ell^{(n_\ell-1)/(\ell-1)}`$ by the factorial valuation of the prime power $`n_\ell`$. As $`\sum_\ell(n_\ell-1)\le n-1`$, this gives

```math
|C|\le 2^{n-1}\quad\hbox{in general},\qquad
|C|\le 3^{(n-1)/2}\quad\hbox{in odd degree}.                        \tag{4}
```

Here $`\ell^{1/(\ell-1)}`$ decreases for $`\ell\ge2`$.

## A uniform simple-type bound and a genuine rank-three endpoint

Let $`o=|\operatorname{Out}(T)|`$. Alexander Bors, [arXiv:1601.04311v3](https://arxiv.org/pdf/1601.04311), Notation 1.1.2, Theorems 2.3.1 and 2.3.4, Corollary 2.3.5 **and its proof**, gives

```math
I\le L_{-1}(\operatorname{Aut}(T))
\le (Lo)^{141/200}\le L^{E_0},\qquad
E_0=\tfrac{141}{200}(1+\log_{20160}12)<\tfrac{441}{500},\qquad
o\le L^{\log_{20160}12}.
```

The first inequality uses the identity automorphism of $`\operatorname{Aut}(T)`$: it inverts exactly the square-one elements. The strict rational upper bound follows from $`12^{235}<20160^{59}`$. We use the cited classification-dependent estimates, not a new proof of them. In particular $`I<L`$.

Sum (3) over at most $`|C|`$ permutations. For odd $`n\ge5`$, (4) and $`s\le n/3`$ would imply

```math
L^{n-1}\le3^{(n-1)/2} L^{2n/3}.
```

This fails already for $`n=5,L=60`$ since $`60^{2/3}>9`$, and the ratio of the left side to the right then grows with $`L`$ and with $`n`$, the latter by the factor $`L^{1/3}/\sqrt3>1`$. Every nonabelian finite simple group has order at least 60.

For $`n=3`$, the faithful nilpotent image is $`C_3`$, and every relevant permutation is a reflection with $`s=1`$. Equation (3) would require $`L\le3I`$. For $`L\ge12000`$ this fails since $`12000^{59}>3^{500}`$. Below this cutoff the [GAP Character Table Library's CFSG simple groups by order, order and Out columns](https://www.math.rwth-aachen.de/homes/Thomas.Breuer/ctbllib/ctbltoc/views/simplebyorder.html) give the following complete $`(L,o)`$ list, with next order 12180:

(60,2), (168,2), (360,4), (504,3), (660,2), (1092,2), (2448,2), (2520,2), (3420,2), (4080,4), (5616,2), (6048,2), (6072,2), (7800,4), (7920,1), (9828,6).

For all but the first four, $`3^{200}o^{141}<L^{59}`$, so already $`3(Lo)^{141/200}<L`$. For $`L=168,504,360`$ the groups are $`\operatorname{PSL}_2(q)`$ with $`q=7,8,9`$, respectively. Their full automorphism group is $`\operatorname{P\Gamma L}_2(q)`$. The projective subgroup contributes $`50,64,82`$ square-one elements, respectively, including identity. The field group for $`q=8`$ has odd order and adds none. At $`q=9`$ the field coset contributes 30: by the projective Lang conjugacy statement every involution in that coset is projectively conjugate to Frobenius, whose centralizer in $`\operatorname{PGL}_2(9)`$ is $`\operatorname{PGL}_2(3)`$ (normalize any projective matrix by its first nonzero entry, which makes entrywise fixedness literal). Its class has size $`720/24=30`$. See Guralnick–Zieve, [*Polynomials with PSL(2) monodromy*, Appendix A, Lemma A.3 and the discussions following Lemmas A.4 and A.5](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf). Thus $`I=50,64,112`$; each has $`3I<L`$. The accompanying finite program also exhausts the actual normalized semilinear matrices and their squares.

For $`T=A_5`$, $`I=26`$ since $`\operatorname{Aut}(A_5)=S_5`$. The crude inequality genuinely **fails** ($`60<3\cdot26`$); it cannot dispose of this endpoint. But if any actual selected mark has a nonidentity arrow at its single fixed site, the square of the $`A_5`$-class of that arrow contains the whole double-transposition class. For a transposition take two disjoint transpositions, conjugate by an even permutation; for a double transposition take two distinct nonidentity elements of the four-point Klein four, permuted by an even 3-cycle. Their product is a double transposition in each case, and its whole $`A_5`$-class follows by simultaneous conjugation. Put such a double transposition $`v`$ on the entire rectified diagonal. At the fixed site it belongs to the required class square; on the exchanged pair both entries are $`v`$, inverse-conjugate under **any** $`A_5`$-automorphism. The actual mark square therefore meets $`\Delta(A_5)`$ nontrivially, forbidden. Every selected mark has identity fixed arrow instead. In the restricted count (3) this replaces $`I`$ by 1, forcing $`60\le3`$. This endpoint uses neither conjugacy of $`H`$ with its inverted stabilizer nor full-top surjectivity. We have proved every $`U_i`$ is proper.

## The proper projection cannot be trivial

This part does not assume subdirectness, an invariant strip, or any fixed coordinate of the outside marks. Put $`F=\max(I,\sqrt{|\operatorname{Aut}(T)|})`$. For a fixed signed coordinate permutation with $`s`$ fixed sites, there are at most $`I^s|\operatorname{Aut}(T)|^{(n-s)/2}\le F^n`$ candidates even allowing **all** local outer arrows: there are $`I`$ choices at a fixed site, and one arbitrary actual automorphism and its forced inverse per exchanged pair. Consequently

```math
|A|=\frac{[B:J]L^n}{|K|}
\;\ge\;\frac{[B:J]L^n}{|C|F^n}
\;\ge\;2[B:J]\left(\frac{L}{2F}\right)^n.                     \tag{5}
```

The Bors outer bound gives $`o<L^{1/3}`$, hence $`\sqrt{Lo}<L^{2/3}<L/2`$. Also $`I<L/2`$ for $`L\ge360`$, since $`360^{59}>2^{500}`$; below 360 the two possibilities have $`I=26,50`$ at $`L=60,168`$. Thus $`L>2F`$ in all types. In particular $`|A|>2`$, and transitivity of $`H`$ on the coordinates makes every $`U_i`$ nontrivial, completing (1). More quantitatively, their common order $`u`$ satisfies

```math
u\ge |A|^{1/n}\ge (2[B:J])^{1/n}\frac{L}{2F}
>\tfrac12 L^{59/500}.
```

Here $`F<L^{441/500}`$ follows from the two uniform bounds above. We do not claim that $`A`$ is the direct product of its proper projections or that $`H`$ is the full normalizer of that product.

## Checks and remaining boundary

The [finite checks](../sources/code/verify_transitive_full_strip_obstructions.py) construct the nonnormal coset actions in $`S_3,S_4,A_4,A_5`$, compute components as physical graphs, compare the two-coset formula, and test original marked generation rather than the distinguished class alone. They include a nonnormal adverse case where $`t`$ alone passes but another selected label fails, two distinct actual $`A_8`$ involution classes preserved even by odd frame changes, the exceptional $`A_5`$ same-class products, all semilinear square-one matrices over $`\mathbb F_7,\mathbb F_8,\mathbb F_9`$, integral cutoff arithmetic, and a genuine nonregular order-81 nilpotent group acting on nine sites. They do not certify the source theorems or replace the proof. The open branch consists of genuine proper stabilizer projections with arbitrary correlations, and substantially more general groups outside the scope of (1). A [separate set of group-theoretic checks](../sources/code/check_96_heisenberg_and_true_a5_square.py) realizes 45,000 actual class-square products at the exceptional three-factor endpoint. [Sources and reproducibility](../normal-layer-evidence.md) distinguish the reviewed proof from the finite tests.
