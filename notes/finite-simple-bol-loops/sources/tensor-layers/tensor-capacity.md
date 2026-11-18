# Matched swaps: a rank-capacity obstruction over finite fields

**Mira Cult**

**Scope.** Assume a finite simple nonassociative left Bol loop has an original canonical extension

```math
1\to V=\mathrm{Mat}_d(q)^+\to G\to T^2\to1,\qquad
 T=\mathrm{SL}_d(q)=\mathrm{PSL}_d(q),\quad d\ge3,\ (d,q-1)=1,
```

with the indicated natural $`(a,b)X=aXb^{\mathsf t}`$ and inversion swapping the matched quotient factors. Such a loop is impossible for **all** these $`d,q`$ except $`(3,2)`$, proved separately in the [binary supplement](binary-three.md). Both signs, all field degrees, arbitrary original stabilizers and initially possibly nonsplit extensions are allowed. This completes the higher-rank positive-transpose gap of the [odd-field checkpoint](odd-field-foundation.md) and adds characteristic two; it does not exclude all irreducible radicals or unmatched semilinear tensor actions.

## Actual mark fibers in characteristic two

The unique-minimal-layer criterion, $`|J|=m|T|`$, $`T=BA`$, $`m>1`$ and the characteristic-free irreducibility/centralizer arguments of the preceding paper still apply. Write $`W=V\cap H,\ J=\bar H`$ with its actual endpoint projections $`A,B`$. The only possible action on $`V`$ in characteristic two is transpose: after composition with transpose an intertwiner is a scalar and its square must be one.

For $`q>2`$ in even characteristic the torus proof there still gives $`H^1(T,L)=0`$, $`L=\mathbb F_q^d`$: for $`d=3`$ choose $`a^2\ne1`$, and for $`d\ge4`$ balance entries separately. At $`q=2,d\ge4`$ there is a replacement proof with root generators. Put $`\delta(x_{ij})=v_{ij}`$ for $`x_{ij}=1+E_{ij}`$. From $`x_{ij}^2=1`$ the $`j`$th entry vanishes. For each $`\ell\notin\{i,j\}`$, choose $`k`$ outside these three indices. The commuting pair $`x_{ij},x_{k\ell}`$ gives $`(v_{k\ell})_j e_i=(v_{ij})_\ell e_k`$; both vanish. Thus $`v_{ij}=c_{ij}e_i`$. The relation $`x_{ij}x_{jk}=x_{jk}x_{ij}x_{ik}`$ gives $`c_{jk}=c_{ik}`$, i.e. the coefficient depends only on the column. This is exactly the derivation of an inner vector shift, proving vanishing. As before the degree-two tensor Künneth calculation splits $`G`$; degree one conjugates all complements by $`V`$.

One must **not** conclude at even order that the given inversion fixes a complement. Instead, in any chosen split model let $`t_0`$ denote the automorphism implementing the ordinary swap and transpose. The actual $`\tau`$ is $`\operatorname{Inn}(v)t_0`$: their difference fixes the quotient and $`V`$, hence is a degree-one derivation, all of which are inner. Its square forces $`v+t_0(v)=0`$, since $`V^{T^2}=0`$. Consequently in the marked extension there is an actual outside involution implementing $`t_0`$, obtained from the formal $`t`$ by multiplying by this $`v`$; we use the same symbol $`t_0`$ for it. It is not assumed selected.

Over the quotient swap the outside involutions are $`t_0 z`$ with $`z`$ symmetric; $`V`$-conjugacy translates the fiber by the alternating matrices $`\mathcal A=(1-t_0)V`$ (symmetric with zero diagonal in characteristic two). The diagonal complement $`\Delta T`$ centralizes $`t_0`$ and acts on $`\mathrm{Sym}/\mathcal A`$ by the entrywise-squared natural action on the diagonal vector. There are exactly two orbits, zero and nonzero: squaring the field entries is a field automorphism and $`T`$ is transitive on nonzero vectors. Thus the selected sheet size over one projected mark is $`q^{d(d-1)/2}c`$, where $`c`$ is $`1,q^d-1`$, or $`q^d`$. It divides $`[V:W]`$, a power of two, so the middle choice is impossible. In particular $`t_0^G`$ is **necessarily selected** (in both surviving choices). This conclusion comes from the arithmetic of the actual fiber, not quotient-folder transversality.

If $`c=q^d`$, all symmetric differences occur over this projected mark. Their $`T^2`$-conjugates cover every matrix (the same determinant argument as over odd fields). Thus $`W=0`$ and $`m=|T|_2`$; both projections contain a full Sylow 2-subgroup and the Bruhat/Grassmannian lemma of the previous paper forces a full endpoint. In any case with a full endpoint, the derivation argument there kills $`H/W`$'s cocycle and produces an original collision, using $`t_0^G`$ inside the selected set and the split complement defining $`t_0`$. Here the needed $`H^1(T,L)=0`$ was proved above. Hence only the small sheet with both endpoints proper remains.

## Rank parity, including even fields and even dimension

In the small binary sheet or in the odd-field positive-transpose case, differences over one mark include all skew/alternating matrices. The $`T^2`$-orbit union contains **every even-rank matrix**. At nonfull rank one can adjust determinant on the unused domain and range; at full even rank in characteristic two choose a block-diagonal alternating nonsingular form of any required determinant, possible because every element of $`\mathbb F_q^\times`$ is a square. For odd characteristic the hypothesis $`(d,q-1)=1`$ makes $`d`$ odd, so no full even rank has to be covered. Every nonzero member of the additive $`W`$ therefore has odd rank, and

```math
m|W|=q^{d(d+1)/2}.                            \tag{1}
```

The odd-field negative sign was already excluded in every indicated rank.

Let $`\ell`$ be any prime dividing $`q+1`$, **not necessarily two**. The number of projective points on a $`j`$-space is congruent modulo $`\ell`$ to zero for even $`j`$ and to one for odd $`j`$. For $`X\in W`$ take the vector over $`\mathbb F_\ell`$ of projective point incidences on its graph in $`L\oplus L`$. Omit all vertical projective points since no graph uses them; the remaining coordinate count is $`C=q^d(q^d-1)/(q-1)`$. Two graphs meet in dimension $`d-\operatorname{rank}(X-Y)`$. If $`d`$ is odd their Gram matrix is the identity; if $`d`$ is even it is the all-ones matrix minus the identity and has nullity at most one over every field. Hence

```math
|W|\le C\ (d\ \mathrm{odd}),\qquad |W|\le C+1\ (d\ \mathrm{even}).
                                                                         \tag{2}
```

No linearity over the ambient field is assumed. In particular $`|W|<q^{2d}`$ also at $`q=2`$; discarding the vertical points is useful for this strict endpoint.

Enlarge the two proper endpoints to maximal subgroups of simple $`T`$. They still factor $`T`$, and $`|J|`$ divides the product of their orders; in particular $`m`$ divides the $`p`$-part of **each** endpoint order since $`m|T|=|J|`$ and both endpoint orders divide $`|T|`$. The maximal-factorization input is Liebeck–Praeger–Saxl, explicitly restated without a solvable-factor requirement in Li–Xia, [arXiv:1408.0350v3, Theorem 2.15, Appendix Table A.1 pp.18,95, and Table A.2 p.96](https://arxiv.org/pdf/1408.0350v3). It excludes abstract $`A_5,A_6,A_8`$ from the table's hypothesis; only $`T=\mathrm{SL}_4(2)\cong A_8`$ needs separate treatment here. The rows used concern maximal overgroups and give upper bounds, not an assertion that the actual stabilizer splits or equals their product.

For odd $`d\ge5`$ the only asymptotic row is A.1 row 1: one factor is within an extension-field $`\mathrm{GL}_a(q^b).b`$, $`d=ab`$, $`b`$ prime; its $`p`$-part is at most $`b_p q^{d(a-1)/2}`$. Rows 2–4 require even dimension, 5–8 dimension two, 9 dimension three; row 10 at $`(5,2)`$ has odd endpoint $`31.5`$, incompatible with the even $`m>1`$. Scalar determinant restrictions do not enlarge the stated $`p`$-part. With (1),(2) this forces

```math
q^{d(d-a-2)/2}\,(q-1)< b_p .
```

But $`b\ge3,\ d-a-2\ge2,\ b_p\le d`$, contradiction. For $`d=3`$ the same row gives $`m\le3_p`$; q=4 in row 9 is excluded by the natural centerless hypothesis. Even fields with $`d=3,q>2`$ have $`3_p=1`$, immediately impossible. Odd fields of rank three were already exhausted in the preceding paper, including the delicate additive cap at $`q=3`$; this provides an alternate subgroup-route proof of $`m\le3_p`$.

For even $`d\ge6`$, only even characteristic is under consideration. A.1 rows 1–4 bound one endpoint's 2-part by $`q^{d^2/4}`$: for the symplectic rows this is the full symplectic 2-part (their scalar multiplier is one in even characteristic), for the extension-field rows use $`2q^{d(d/2-1)/2}\le q^{d^2/4}`$, and the other rows do not apply. Thus (1) gives $`|W|\ge q^{d^2/4+d/2}\ge q^{2d}`$, contradicting (2). This covers all these ranks without enumerating individual factorizations.

## Rank four in characteristic two

First $`q\ge4`$. Formula (2) gives

```math
m> q^2(q-1).
```

Indeed $`C+1=(q^8-q^4)/(q-1)+1<q^8/(q-1)`$. Extension-field endpoints have 2-part at most $`2q^2`$, too small. Thus in A.1 a maximal factor is symplectic $`\mathrm{Sp}_4(q)`$; the opposite is contained in a natural point/hyperplane stabilizer (an ordered line and complementary hyperplane also suffice). The actual endpoint $`A`$ inside the symplectic group must be transitive on the corresponding points or hyperplanes by $`T=AB`$. Symplectic polarity identifies the latter action with the former. If $`A<\mathrm{Sp}_4(q)`$, enlarge it to a maximal and factor the simple symplectic group by that maximal and its point parabolic. Table A.2 at $`m_{\rm rank}=2,q`$ even yields opposing 2-part at most $`2q^2`$: the appropriate extension-field group $`\mathrm{Sp}_2(q^2).2`$, or the minus orthogonal group $`O^-_4(q)`$ of that same order, allowing the graph-swapped parabolic types. The even-field Suzuki line has an orthogonal, not point-parabolic, partner; rows with larger rank or odd $`q`$ do not give additional parabolic pairs. The two even parabolics have the same order but are distinct; keeping either possibility only enlarges the order bound. This would again contradict $`m>q^2(q-1)`$. Hence the **actual** endpoint equals simple $`\mathrm{Sp}_4(q)`$.

A simple endpoint $`A`$ in any such Goursat subgroup with $`|J|>|T|`$ must occur purely: were the coupling quotient $`A`$, then $`|J|=|B|\le|T|`$. The additive $`W`$ is consequently invariant under the pure natural symplectic action. Its algebra on $`L`$ is the full matrix algebra over $`\mathbb F_q`$: differences of symplectic transvections give $`v\langle\,\cdot\,,v\rangle`$ with arbitrary field multipliers, and their products give all $`v\langle\,\cdot\,,w\rangle`$. If two target vectors pair to zero, choose an intermediate vector pairing nontrivially with both (two proper hyperplanes do not cover $`L`$). Thus $`W`$ is a full-row or full-column compression space as in the preceding paper. It can use at most one independent row direction because it avoids rank two, so $`|W|\le q^4`$ and $`m\ge q^6>|\mathrm{Sp}_4(q)|_2=q^4`$, a contradiction.

For $`q=2,d=4`$, (1),(2) give $`|W|\le241`$, hence $`|W|\le128,\ m\ge8`$. Consult the actual [$`A_8`$ maximal roster](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A8.html) (orders 2520,1344 twice,720,576,360) and [$`A_7`$ roster](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A7.html). The two groups of order 1344 are the natural line/hyperplane stabilizers in $`\mathrm{GL}_4(2)`$: both have that order, both are maximal (the dual point actions are doubly transitive), and they are nonconjugate since their invariant subspaces have different dimensions. If an endpoint contains both 5 and 7 in its order it must be $`A_7`$ by the two rosters. A pure $`A_7`$ gives $`|W|\le16`$: its order-five element is irreducible in four binary dimensions, and its commuting field must be $`\mathbb F_2`$ because $`|\mathrm{GL}_2(4)|=180<|A_7|`$. Thus its generated algebra is full (the finite-dimensional density theorem for an irreducible module with scalar commuting algebra), forcing the same compression bound. But then $`m\ge64>|A_7|_2`$.

Otherwise label the 5-bearing endpoint $`A`$ and the 7-bearing endpoint $`B`$. They both exist since $`|J|`$ is a multiple of 20160. The maximal orders bound $`|A|_2\le16`$. From $`|A|_2|B|_2\ge 8\cdot64`$, $`|B|_2\ge32`$, so its 7-bearing maximal cannot be $`A_7`$. Thus $`B`$ lies in one of the 1344 parabolics, and $`A`$ is transitive on the 15 points of the natural module or its dual. By Hering's 1-space theorem in [Liebeck–Praeger–Saxl, *Regular subgroups of primitive permutation groups*, Lemma 3.1](https://www.ma.imperial.ac.uk/~mwl/REGFINAL.PDF), $`A`$ contains natural $`\mathrm{SL}_2(4)`$ on restriction of scalars, contains $`\mathrm{Sp}_4(2)`$, equals $`A_6`$ or $`A_7`$, or is in $`\Gamma L_1(16)`$; the full $`\mathrm{SL}_4(2)`$ was already excluded. The semilinear last group has 2-part four. Any simple $`A_6`$ here is in the pure endpoint because the common quotient divides $`|B|`$, which is 5-free. Order five again forces irreducibility, and $`360>180`$ forces the full matrix algebra. The same applies when $`A`$ contains $`\mathrm{Sp}_4(2)\cong S_6`$ by its $`A_6`$. In either case $`m\ge64>|A|_2`$.

It remains that $`A`$ contains $`\mathrm{SL}_2(4)\cong A_5`$, also pure, and may be assumed to have no $`A_6`$. Necessarily $`|A|_2=8`$. For if $`|A|_2=16`$, the maximal roster forces containment in $`S_6`$. Its index there divides nine (its order is divisible by 80). Index three is impossible since the simple $`A_6`$ cannot act nontrivially on three points. Index nine would yield a subgroup of order 80, meeting $`A_6`$ in order 40; the latter normalizes its Sylow 5 by Sylow counting, whereas the normalizer of a 5-cycle's subgroup in $`S_6`$ has order 20. Index one includes $`A_6`$. Thus $`8\le m\le|A|_2=8`$ and $`|W|=128`$. But invariance under the pure restriction-of-scalars $`\mathrm{SL}_2(4)`$ makes $`W`$ stable under $`\mathbb F_4`$ scalars on that side: elementary root operators and products generate $`\mathrm{Mat}_2(4)`$, including those scalars. So $`|W|`$ must be a power of four, not 128. Duality gives the same argument with the dual scalar structure. This closes the binary rank-four exception to the general maximal-factor table.

The [finite checker](../code/verify_tensor_parity_capacity.py) computes actual symmetric/alternating transvection orbit unions in binary ranks three and four, their nonzero diagonal-coset orbits, incidence Gram controls, and 414 rank/field arithmetic instances. The $`(3,2)`$ computation checks geometry, not the outstanding nonsplit and lift possibilities there. The original odd-field proof and its independent-certificate status are retained separately. The all-field capacity deduction received one independent AI mathematical acceptance; the [theorem overview](../../manuscripts/0100-matched-tensor-radicals.md) records its scope and the separate binary rank-three audit. The original classification inputs are not formally verified.
