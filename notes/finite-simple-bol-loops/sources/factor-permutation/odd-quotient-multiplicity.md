# Uniform multiplicity in odd canonical quotients

**Mira Cult**

**Independently reviewed, conditional on the pinned inputs**, continuing [0323:C0010](../../claims/0010.md). Let $`(G,H,K,\tau)`$ be the faithful generated canonical folder of a finite simple nonassociative left Bol loop. Let $`1<N<G`$ be normal and $`\tau`$-stable, and put $`Q=G/N`$, $`\theta`$ for the induced involution, and $`U=HN/N`$. Assume $`|Q|`$ is odd. The original folder, all-conjugate transversality and normal-subloop interfaces are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45) and [C0007](../foundations/C0007.md) with scoped review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). All deductions below use actual $`H,K`$, not an assumed quotient folder.

Define

```math
I=\{x\in Q:\theta(x)=x^{-1}\}.
```

Every left coset of $`U`$, and of every conjugate of $`U`$, contains exactly

```math
r=\frac{|I|}{[Q:U]}=\frac{|U|}{|C_Q(\theta)|} \tag{1}
```

elements of $`I`$. Here $`r`$ is an odd integer at least 3. The same statement applies to every nontrivial quotient $`Q/M`$ by a $`\theta`$-stable normal subgroup $`M\triangleleft Q`$, using the full preimage of $`M`$ in $`G`$; the preimage must be proper in $`G`$. In particular this assertion is not applied to the trivial quotient.

Indeed the outside involutions $`x\widehat\theta`$ in the formal extension $`Q\rtimes\langle\widehat\theta\rangle`$ form one $`Q`$-class: the unique odd-order square root $`b`$ of $`x`$ satisfies $`\theta(b)=b^{-1}`$, and $`x=b\theta(b)^{-1}`$. Thus $`|I|=[Q:C_Q(\theta)]`$. The actual marked set $`\Lambda=\widehat\tau K`$ is $`G`$-conjugacy invariant and contains $`\widehat\tau`$, so its image is exactly this outside class. Conjugation by lifts of $`Q`$-elements gives bijections between all its fibers; multiplication by $`\widehat\tau`$ gives a common positive fiber size $`b`$ for $`K\to I`$.

The inverse image of any left $`U`$-coset is a disjoint union of $`[N:H\cap N]`$ left $`H`$-cosets. Original transversality therefore gives

```math
b|I\cap xU|=[N:H\cap N]\qquad(x\in Q). \tag{2}
```

This proves uniformity, integrality and (1). Both $`|I|`$ and $`[Q:U]`$ are odd. If $`U<Q`$, the original strict normal-subloop criterion gives $`|I|>[Q:U]`$. If $`U=Q`$, then $`r=|I|`$; $`r=1`$ would make the $`Q`$-image of every element of $`K`$ trivial, contradicting $`G=\langle K\rangle`$ and $`Q\ne1`$. Hence in either case $`r\ge3`$. Original all-conjugate transversality gives the same calculation for $`H^g`$, and every $`Q`$-conjugate of $`U`$ arises this way.

## Complement obstruction

Suppose a nontrivial odd quotient has $`Q=V\rtimes L`$, where $`V\ne0`$ is elementary abelian, $`L`$ acts faithfully on $`V`$, and $`\theta`$ preserves both $`V`$ and a complement $`L`$. If $`U`$ is contained in a conjugate of $`L`$, uniformity excludes the folder. After the allowed conjugation, take $`U\le L`$. Uniformity on $`U`$-cosets aggregates to uniformity on $`L`$-cosets. Since $`\theta`$ preserves both factors,

```math
|I\cap L|=|I|/[Q:L]=[L:C_L(\theta)]/|C_V(\theta)|.
```

The outside-involution class calculation inside $`L`$ also gives $`|I\cap L|=[L:C_L(\theta)]`$. Hence $`C_V(\theta)=1`$, and $`\theta`$ acts as $`-1`$ on the odd-characteristic vector space $`V`$. If $`L`$ acts faithfully on $`V`$, preservation of $`L`$ then forces $`\theta|_L=1`$. Consequently $`I\cap L=\{1\}`$. Uniformity on $`U`$-cosets inside $`L`$ forces $`U=L`$, and then (1) gives $`r=1`$, contradiction. No coprimality assumption between $`|L|`$ and the characteristic of $`V`$ is used.

A $`\theta`$-stable complement exists when $`L`$ is solvable and acts faithfully and irreducibly on $`V`$. In that case $`V`$ is the unique minimal normal subgroup: any normal subgroup disjoint from it centralizes it and hence lies in $`C_Q(V)=V`$, while irreducibility makes any nonzero normal subgroup inside $`V`$ equal $`V`$. Thus $`V`$ is characteristic and is preserved by $`\theta`$. If $`L=1`$, this is immediate. Otherwise $`O_p(L)=1`$: a normal $`p`$-subgroup has a nonzero fixed vector, its fixed space is $`L`$-invariant, and faithfulness and irreducibility make it trivial. The nontrivial Fitting subgroup $`F(L)`$ is thus a $`p'`$-group, and $`V^{F(L)}=0`$. For any 1-cocycle $`c:L\to V`$, averaging over $`F(L)`$ makes its restriction a coboundary. Subtracting it makes $`c`$ vanish on $`F(L)`$; normality and the cocycle identity then put every $`c(\ell)`$ in $`V^{F(L)}=0`$. Thus $`H^1(L,V)=0`$, so all complements are $`V`$-conjugate. Their number is an odd power of $`p`$, and the involution $`\theta`$ fixes one. This proves the complement obstruction for all solvable faithful irreducible affine complements.

Every finite odd-order group is solvable by Feit–Thompson, *Solvability of groups of odd order*, Pacific J. Math. 13 (1963), Chapter I §1, theorem statement on printed p. 775, [publisher PDF](https://msp.org/pjm/1963/13-3/pjm-v13-n3-p01-s.pdf). That statement was inspected; the full proof was not audited here. Therefore the obstruction applies to every faithful primitive affine odd quotient when the image of $`U`$ lies in a complement.

## Maximal overgroups have unstable cores

If $`U<Q`$, every maximal subgroup $`A\ge U`$ has $`\theta`$-unstable core $`M=\mathop{\mathrm{Core}}\nolimits_Q(A)`$. Otherwise $`Q/M`$ is a faithful primitive odd permutation group. Feit–Thompson makes it solvable. A minimal normal subgroup of a finite solvable group is elementary abelian; its orbits are blocks, so faithfulness and primitivity make it transitive. An abelian faithful transitive group is regular. Its point stabilizer is therefore a complement, acts faithfully (the centralizer of the regular abelian group is that group itself), and acts irreducibly since invariant subspaces would give blocks. This gives the affine decomposition with complement $`A/M`$. The full preimage of $`M`$ in $`G`$ is nontrivial, proper and $`\tau`$-stable. The complement obstruction applied to that original quotient gives a contradiction. This asserts no conclusion about an arbitrary non-invariant core beyond its instability.

## A top-only survivor

The unstable-core case is real. Let $`P=C_7\rtimes C_3`$ with faithful action and $`P'=C_7`$, and set

```math
Q=\{(x,y)\in P\times P:xP'=(yP')^{-1}\},\quad
 \theta(x,y)=(y,x),\quad U=Q\cap(C_3\times P).
```

Then $`|Q|=147`$, $`|U|=21`$, and

```math
I=\{(x,x^{-1}):x\in P\},\qquad |I|=21.
```

Projection to the first $`P`$ maps $`I`$ bijectively onto $`P`$ and $`U`$ onto $`C_3`$, with second $`C_7`$-axis as kernel. Every $`U`$-coset therefore contains exactly three elements of $`I`$, and the same holds for every conjugate. The set $`I`$ generates $`Q`$: choose $`a,c`$ of orders 7,3 with $`cac^{-1}=a^2`$. It contains $`(a,a^{-1})`$ and $`(c,c^{-1})`$. Conjugating the former by the latter gives exponent vectors $`(1,-1)`$ and $`(2,-4)`$ in the two $`C_7`$ axes. Their determinant is $`-2\ne0`$ modulo 7, so they generate $`P'\times P'`$; the second element surjects onto the anti-diagonal $`C_3`$ quotient. Also $`U`$ normally generates $`Q`$, because its $`C_3`$ element acts fixed-point-freely on the two $`C_7`$ axes.

The maximal subgroup $`U`$ has core the second $`C_7`$-axis, which $`\theta`$ swaps with the first. Normal subgroups inside $`C_7^2`$ are 1, the two eigenspaces and $`C_7^2`$; a normal subgroup with nontrivial $`C_3`$-image contains $`C_7^2`$, since its commutator with that group is all of it. Thus the only proper nontrivial $`\theta`$-stable normal subgroup is $`C_7^2`$. In the corresponding $`C_3`$ quotient, the image of $`U`$ is all of $`C_3`$, $`\theta`$ acts by inversion, and $`r=3`$. Hence this example satisfies the uniformity, generation and invariant-normal-cut conditions above. It is top-only group data, not a Bol-loop construction or evidence of a compatible socle and stabilizer.

## Independent mathematical review

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/508ed66f7323592d4ac8b74efc943b1e3072211a). Their acceptance is conditional on the pinned canonical-folder and original normal-subloop interfaces and the explicitly cited Feit–Thompson theorem. They checked actual marked-fiber uniformity, every conjugate stabilizer coset, the U=Q generation case, the affine complement obstruction including modular actions, the Fitting/H¹ complement argument, the primitive maximal-core consequence and the order-147 top-only control. They did not independently audit the full odd-order theorem or reprove all upstream inputs; no new computation is claimed. These are model mathematical reviews, not human/formal certification or GitHub approval.

## Paired affine sections and finite descent

**Independently reviewed, conditional on the pinned inputs.** The following extends only the necessary odd-quotient restrictions above and relies on their exact reviewed source [the source revision](https://github.com/Mira-Cult/math-wip/commit/508ed66f7323592d4ac8b74efc943b1e3072211a). It asserts neither a folder construction nor a classification of the possible intervening kernels.

Let `(Q,θ,U)` be any nontrivial θ-stable quotient of the original data, with `U<Q`. Choose a maximal subgroup `A≥U`, write `M=core_Q(A)` and `M*=θ(M)`, and put

`P=Q/(M∩M*)`, `L1=Q/M`, `L2=Q/M*`.

The reviewed maximal-core theorem gives `M≠M*`. Both `L_i` are odd primitive solvable groups, and each has a unique minimal normal subgroup `V_i`, elementary abelian and regular in its primitive action. The involution exchanges the two quotients, so `|V1|=|V2|=v=p^d`.

The natural map `P→L1×L2` is injective and subdirect. The kernel of its **first** projection is `M/(M∩M*)`, whose image in `L2` is a nontrivial normal subgroup and therefore contains `V2`. Similarly, the second projection kernel contains `V1` in the first coordinate. Consequently `P` contains a normal θ-stable subgroup `W=V1×V2` with independent coordinate supports, and θ exchanges its two factors. Write `B=P/W`. It embeds subdirectly in `(L1/V1)×(L2/V2)`. It need not be a common quotient of the two affine point stabilizers, nor is `B` necessarily `Q/(MM*)`.

Let `U_P` and `U_B` denote the images of `U` in `P` and `B`. Since `U≤A`, its first primitive projection fixes the chosen point, and hence `U_P∩W≤V2`. Write `|U_P∩W|=v/p^e`, with `e≥0`. Denoting by `I_X` the inverted set of the induced involution on an odd quotient `X`, one has

`|I_P|=v|I_B|`, and `[P:U_P]=v p^e[B:U_B]`.  (3)

For the first equality, each outside involution of `B` lifts to an outside involution of the odd-kernel extension, and its action exchanges `V1,V2`. Its negative eigenspace on `W` has order `v`, giving exactly `v` involutory lifts. The second equality follows from the displayed intersection. The reviewed original-folder uniformity theorem applies separately to `P` and, when nontrivial, to `B`, via their full preimages in `G`. It follows that

`p^e[B:U_B]` divides `|I_B|`, and `|I_B|/(p^e[B:U_B])≥3`.  (4)

Here `B` is necessarily nontrivial: if `B=1`, (3) would give `|I_P|/[P:U_P]=1/p^e`, contradicting the reviewed multiplicity lower bound for `P`. In particular, `p∤|I_B|` forces `e=0`, so `U_P` contains all of `V2`. These statements retain the actual stabilizer image; no assumption `U=Q` is made.

If `U_B<B`, repeat the construction on `(B,θ,U_B)`. Otherwise stop. The procedure is finite: at each paired section the quotient order strictly decreases, since `W` is nontrivial. Each intermediate quotient is nontrivial and inherits the original uniform-multiplicity statement by taking its full preimage in `G`. At a section, the exact multiplicity relation is `r_P=r_B/p^e`. The initial quotient `Q→P` can have a nontrivial θ-stable kernel `M∩M*`; no equality between `r_Q` and `r_P` follows. Thus this is a finite necessary descent through paired affine **sections**, interspersed with possible nontrivial quotient kernels, not a filtration in which every factor has the displayed form. The terminal stabilizer image is the whole terminal quotient, whose multiplicity remains at least three. No converse, direct global bound, or compatible Bol folder is asserted.

### Review of the paired-section continuation

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete paired-affine-section and finite-descent addition at [the source revision](https://github.com/Mira-Cult/math-wip/commit/5a5f6193f758463d419fe5bddb00920985487f20), conditional on the reviewed odd-quotient and odd-solvability inputs. They checked the projection kernels, independent affine factors, subdirect residual quotient, nonsplit involution-lift count, stabilizer intersection, multiplicity relation, nontrivial residual and finite descent with possible intervening kernels. No construction, classification, fresh primary-source audit, upstream reproof or computation is certified by this review; it is model mathematical review, not formal GitHub approval.
