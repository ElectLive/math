# Associative-subloop censuses from an unaligned deletion deck

*Mira Cult*

## Scope, dependencies, and principal result

Fix a prime $`p\ne3`$. This note concerns the ordinary-graph loops

```math
 L_p(\Gamma)=\mathbb F_p\times\mathbb F_p^{V(\Gamma)}
                  \times\mathbb F_p^{E(\Gamma)},
\qquad
 (a,u,s)(b,v,t)
   =(a+b,u+v,s+t+(a+2b)\beta_\Gamma(u,v)),                 \tag{1}
```

where one independent central coordinate is used for each edge and

```math
 \beta_\Gamma(u,v)_{ij}=u_iv_j-u_jv_i.
```

The construction, its left Bol identity, and its unmarked graph-recovery
theorem are proved in the
[all-ring manuscript](../../graph-loops/manuscripts/graph-eisenstein-loops.md). The maximal associative
subloops are classified in the
[dominating-support manuscript](../../graph-loops/manuscripts/graph-associative-subloops.md). This note
adds a count of **all** associative subloops, including those that do not
contain the associator subgroup, and proves that both this count and the
maximal-associative count are determined by the unaligned deletion deck.

The deck interface used here is the multiset

```math
 \mathcal D_p(L_p(\Gamma))
    =\bigl\{[L_p(\Gamma-v)]:v\in V(\Gamma)\bigr\},       \tag{2}
```

with multiplicities and with each card supplied only as an abstract loop
isomorphism class. The
[intrinsic admissible-frame construction](loop-deletion-decks.md#intrinsic-frame-deck)
is a separate theorem: this note uses its conclusion (2), not an
identification of vertices, embedded subloops, or central coordinates
between cards. The
[exact reconstruction equivalence](loop-deletion-decks.md#exact-reconstruction-equivalence)
is not used as a claim that the common reconstruction problem is solved.

**Principal theorem.** Let $`\Gamma`$ be any finite simple graph on $`n\ge3`$
vertices, and let $`p\ne3`$ be prime. Its deck (2) determines:

1. the number of associative subloops of $`L_p(\Gamma)`$ of each order;
2. the multiset of their abstract group isomorphism types;
3. the number of maximal associative subloops of each order, and the entire
   dominating-component polynomial defined in Section 5.

The first two conclusions already follow from the subgraph component
polynomials of the recovered graph cards. They hold whether or not
$`\Gamma`$ itself is reconstructible. The proof computes proper induced
subgraph statistics by double counting; it never chooses an alignment of
different cards or reconstructs an unknown parent graph as an intermediate
step. Section 6 gives two nonisomorphic graph loops having the same entire
associative-subloop census at every prime $`p\ne3`$, but different maximal
associative-subloop censuses. Thus the enumerative conclusion does not
reconstruct the inclusion pattern of these groups or the loop extension.

All statements in this note have explicit proofs below. Independent review
and its exact source revision belong to the continuation's review record;
the finite checks in Section 8 are separate evidence.

## 1. Induced component counts and full-support subspaces

For $`S\subseteq V(\Gamma)`$, put $`c(S)=|\pi_0(\Gamma[S])|`$, with
$`c(\varnothing)=0`$. Use the established subgraph component polynomial

```math
 Q_\Gamma(x,y)=\sum_{S\subseteq V}x^{|S|}y^{c(S)}
              =\sum_{s,c}q_{s,c}(\Gamma)x^sy^c.            \tag{3}
```

This is the polynomial of Tittmann, Averbouch and Makowsky [TAM09, Section
2.1]; its vertex reconstructibility is an existing result [TAM09, Theorem
27]. A self-contained proof covering mixed isolated and nonisolated
components is given in Section 4, so no component-count convention from
another proof is needed.

Write $`{N\brack d}_q`$ for the Gaussian binomial coefficient, interpreted as
zero unless $`0\le d\le N`$. For a prime power $`q`$, define

```math
 F_q(c,d)=\sum_{j=0}^{c}(-1)^j{c\choose j}{c-j\brack d}_q. \tag{4}
```

This counts $`d`$-dimensional subspaces of $`\mathbb F_q^c`$ whose support is
all $`c`$ coordinates: exclude, by inclusion-exclusion, the coordinate
hyperplanes containing a subspace. In particular,
$`F_q(0,0)=1`$, $`F_q(c,0)=0`$ for $`c>0`$, and $`F_q(c,d)=0`$ for $`d>c`$.

**Lemma 1 (support formula).** The number $`I_d(\Gamma;q)`$ of
$`d`$-dimensional totally isotropic spaces for the graphical alternating map
$`\beta_\Gamma`$ is

```math
 I_d(\Gamma;q)
   =\sum_{S\subseteq V}(q-1)^{|S|-c(S)}F_q(c(S),d)
   =\sum_{s,c}q_{s,c}(\Gamma)(q-1)^{s-c}F_q(c,d).          \tag{5}
```

*Proof.* Let $`H\le\mathbb F_q^V`$ have support $`S`$, and let
$`\ell_i:H\to\mathbb F_q`$ be its coordinate functionals. Isotropy says
$`\ell_i\wedge\ell_j=0`$ for every edge $`ij`$. Each $`\ell_i`$, $`i\in S`$,
is nonzero. Along a connected component $`C`$ of $`\Gamma[S]`$, these
functionals are therefore nonzero scalar multiples of one another. It
follows that the image of $`H`$ in $`\mathbb F_q^C`$ is a full-support line
$`\mathbb F_q a_C`$.

There are $`(q-1)^{|C|-1}`$ possible lines on $`C`$. After choosing one line
on each component, the space $`H`$ is exactly a $`d`$-dimensional subspace of
$`\bigoplus_C\mathbb F_q a_C\cong\mathbb F_q^{c(S)}`$ with nonzero
projection to every summand. There are $`F_q(c(S),d)`$ such subspaces.
The component lines are recovered as the images of $`H`$, so no space is
counted twice. Multiplying and summing proves (5). $`\square`$

This is a convenient support-based form of the isotropic counting mechanism
in Qiao [Q26, Theorem 1.2 and Section 2, especially Lemma 2.3]. Neither
isotropic counting polynomials nor their interpretation through abelian
subgroups of class-two graph groups are claimed as new here. The next
section uses the specific Bol associator to determine which additional
projected spaces are associative.

## 2. All associative projected spaces

Put $`W=\mathbb F_p^V`$, $`Z=\mathbb F_p^E`$, and
$`A=\mathbb F_pm\oplus W=L_p(\Gamma)/Z`$, where $`m=(1,0)`$. Write
$`n=|V|`$ and $`e=|E|`$. The associator difference, central in $`Z`$, is

```math
 D((a,u),(b,v),(c,w))
   =a\beta(v,w)-b\beta(u,w)-2c\beta(u,v).                 \tag{6}
```

The sign of the associator convention is immaterial to its vanishing;
(6) is the difference of the central coordinates of $`(xy)z`$ and
$`x(yz)`$. This formula follows by expanding (1), as established in the
all-ring manuscript.

Let $`a_r(\Gamma;p)`$ be the number of $`r`$-dimensional subspaces $`U\le A`$
for which $`D|_{U^3}=0`$. These are precisely the quotient images of
associative subloops that contain $`Z`$.

**Lemma 2 (crossing the vertex hyperplane).** A subspace $`U\le A`$ not
contained in $`W`$ can be written uniquely as

```math
 U=\mathbb F_p(m+x)\oplus H,
\qquad H=U\cap W,
```

where $`x\in W`$ is determined modulo $`H`$. Such a space is associative if
and only if

```math
 \beta(H,H)=0,\qquad \beta(x,H)=0.                      \tag{7}
```

Moreover, the restriction of multiplication (1) to $`\pi^{-1}(U)=U\times Z`$
is ordinary vector addition whenever $`D|_{U^3}=0`$.

*Proof.* For $`h,k\in H`$, (6) gives

```math
 D(m+x,h,k)=\beta(h,k),\qquad
 D(h,m+x,m+x)=-3\beta(h,x).
```

Since $`p\ne3`$, associativity implies (7). Conversely (7) makes
$`\beta(ax+h,bx+k)=0`$ for every $`a,b\in\mathbb F_p`$ and $`h,k\in H`$.
Consequently the correction in (1) vanishes on $`U\times U`$, proving both
associativity and the final assertion. For $`U\le W`$, the correction
already vanishes because both marker coordinates are zero.
$`\square`$

Extend $`\beta`$ to $`A`$ by making $`m`$ radical. This is the graphical
alternating map of $`\Gamma\sqcup K_1`$. Lemma 2 says that the associative
spaces crossing $`W`$ are exactly its isotropic spaces crossing $`W`$.
All spaces contained in $`W`$ are associative, including its nonisotropic
spaces. Therefore

```math
\begin{split}
 a_r(\Gamma;p)
  &={n\brack r}_p+I_r(\Gamma\sqcup K_1;p)-I_r(\Gamma;p)\\
  &={n\brack r}_p+
    \sum_{s,c}q_{s,c}(\Gamma)(p-1)^{s-c}F_p(c+1,r).
                                                               \tag{8}
\end{split}
```

The second line applies Lemma 1 to supports containing the new isolated
marker. It also covers $`r=0`$, when the summation is zero and $`a_0=1`$.

For comparison with the maximal-isotropic theorem, the same crossing count
has the neighborhood expression

```math
 a_{d+1}-{n\brack d+1}_p
 =\sum_{S\subseteq V}(p-1)^{|S|-c(S)}F_p(c(S),d)
      p^{n-|N[S]|+c(S)-d}.                              \tag{9}
```

Terms with $`c(S)<d`$ are interpreted as zero. Indeed, an isotropic space
$`H`$ of support $`S`$ has

```math
 \dim H^\perp=c(S)+n-|N[S]|.
```

On each supported component, orthogonality forces a vector to lie in its
component line; a vertex outside $`S`$ adjacent to $`S`$ must have zero
coordinate; vertices outside $`N[S]`$ are free. For each such $`H`$, the
number of allowed affine choices $`x+H`$ in Lemma 2 is
$`p^{\dim H^\perp-d}`$, proving (9). Formula (8) shows that the resulting
sum depends only on component counts, despite the neighborhoods in (9).

## 3. Every associative subloop, including noncentral intersections

**Theorem 3 (full census).** Let $`g_k(\Gamma;p)`$ be the number of
associative subloops of $`L_p(\Gamma)`$ of order $`p^k`$. Then

```math
 \boxed{\quad
 g_k(\Gamma;p)=
   \sum_{\substack{0\le r\le n+1\\0\le k-r\le e}}
    a_r(\Gamma;p){e\brack k-r}_p
                p^{r(e-k+r)}.
 \quad}                                                   \tag{10}
```

Every group counted here is elementary abelian. In particular the full
multiset of abstract associative-subloop types is determined by
$`n,e,Q_\Gamma`$.

*Proof.* If $`K`$ is an associative subloop, its image $`U=\pi(K)\le A`$
is an $`\mathbb F_p`$-subspace. Since associators depend only on images,
$`D|_{U^3}=0`$. Lemma 2 makes the entire inverse image
$`\pi^{-1}(U)=U\times Z`$ an elementary abelian group, so $`K`$ is a vector
subspace of this group.

Fix $`U`$ of dimension $`r`$, and $`J=K\cap Z`$ of dimension $`j`$.
There are $`{e\brack j}_p`$ choices of $`J`$. After passing to the quotient
by $`J`$, the space $`K/J`$ must project isomorphically onto $`U`$. It is
the graph of one linear map $`U\to Z/J`$, giving $`p^{r(e-j)}`$ choices.
All have order $`p^{r+j}`$. Summing with $`j=k-r`$ proves (10).
$`\square`$

The prime-field assumption is essential to this form of the statement.
Subgroups of an additive $`\mathbb F_{p^f}`$-space need only be
$`\mathbb F_p`$-linear. Formula (5) is valid for every prime power, but (10)
does not count all subloops over a nonprime field merely by replacing $`p`$
with $`p^f`$.

For an edgeless graph, $`L_p(\Gamma)=C_p^{n+1}`$. Equation (8) becomes
$`a_r={n+1\brack r}_p`$, and (10) is the usual vector-subspace count.
For $`\Gamma=K_2`$ and $`p=2`$, the loop has order 16; its associative
subloops have orders $`1,2,4,8`$ with respective multiplicities
$`1,15,23,4`$. There are no associative subloops of order 16.

## 4. Reconstruction of the component polynomial without graph reconstruction

Suppose $`n\ge3`$. A card loop in (2) determines its graph isomorphism class
by the unmarked recovery theorem, including edgeless cards. Thus quantities
such as $`Q_{\Gamma-v}`$ can be evaluated separately on the cards. No
identification of a vertex in one card with a vertex in another is made.

For $`s<n`$, every $`s`$-vertex subset survives precisely $`n-s`$ deletions.
Consequently

```math
 q_{s,c}(\Gamma)
   =\frac{1}{n-s}\sum_{v\in V}q_{s,c}(\Gamma-v).          \tag{11}
```

This is the induced-subgraph form of Kelly's double-counting lemma
[K57, Lemma 1]. Only the top term $`x^ny^{c(V)}`$ remains.

The edge count and the degree of the deleted vertex are also determined:

```math
 e=\frac{1}{n-2}\sum_v e(\Gamma-v),
\qquad d(v)=e-e(\Gamma-v).                               \tag{12}
```

Put $`\varepsilon=1`$ if at least one value in the degree multiset is zero,
and $`\varepsilon=0`$ otherwise. Then

```math
 c(V)=\min_v c(\Gamma-v)+\varepsilon.                    \tag{13}
```

To prove (13), if there is an isolated vertex, deleting it decreases the
component count by one, while deletion of any nonisolated vertex cannot
decrease it. If there are no isolated vertices, deletion cannot decrease
the component count. A nontrivial connected component has a vertex whose
deletion leaves that component connected: take a leaf of a spanning tree.
Deleting this vertex attains equality. The same formula handles an
edgeless graph, for which the minimum is $`n-1`$.

Equations (11)--(13) reconstruct all of $`Q_\Gamma`$. In fact the multiset
of card polynomials alone suffices: their $`x^2y`$ coefficients give card
edge counts, and their top terms give card component counts. Substitution
in (8) and (10) proves the first two conclusions of the principal theorem.
This is an explicit transfer of a familiar graph-polynomial reconstruction
mechanism to the full associative-subloop census of these Bol loops.

## 5. The maximal-associative census is also reconstructible

The previously proved dominating-support classification gives

```math
 \mathcal A_\Gamma(q,z)
   =\sum_{S:\ N[S]=V}(q-1)^{|S|-c(S)}z^{c(S)}.            \tag{14}
```

For a prime $`p\ne3`$, the coefficient of $`z^d`$ in
$`\mathcal A_\Gamma(p,z)`$ counts maximal associative subloops crossing
$`W`$ of order $`p^{e+1+d}`$. If $`e>0`$, the remaining maximal group is
$`W\times Z`$, of order $`p^{n+e}`$. If $`e=0`$, the loop itself is the
unique maximal group, and the extra $`W\times Z`$ term is omitted.

**Lemma 4 (weighted component expansion).** For every finite simple graph,

```math
 \mathcal A_\Gamma(q,z)
  =\sum_{U\subseteq V}
     \prod_{C\in\pi_0(\Gamma[U])}
       \left((q-1)^{|C|-1}z+(-1)^{|C|}\right).            \tag{15}
```

*Proof.* For any $`S\subseteq V`$, inclusion-exclusion gives

```math
 \mathbf1_{N[S]=V}=\sum_{T\subseteq V\setminus N[S]}(-1)^{|T|}.
```

Insert this into (14). With $`U=S\sqcup T`$, there are no edges between
$`S`$ and $`T`$; equivalently, $`S`$ is a union of whole components of
$`\Gamma[U]`$. A component assigned to $`S`$ contributes
$`(q-1)^{|C|-1}z`$; one assigned to $`T`$ contributes $`(-1)^{|C|}`$.
Their independent choices yield (15). $`\square`$

This is a weighted version of the component-size subset expansion for the
ordinary domination polynomial in Kotek, Preen and Tittmann [KPT12,
Section 3, Corollary 11 and equation (5)]. The use of inclusion-exclusion
for domination is an existing mechanism; the weights here are fixed by
the graph-loop maximal-subgroup theorem.

To recover the contribution of proper $`U`$ in (15), define for each card
$`H=\Gamma-v`$ and $`0\le s<n`$

```math
 B_s(H)=\sum_{\substack{U\subseteq V(H)\\|U|=s}}
     \prod_{C\in\pi_0(H[U])}
       \left((q-1)^{|C|-1}z+(-1)^{|C|}\right).
```

Then the contribution of all $`s`$-vertex subsets of $`\Gamma`$ is
$`(n-s)^{-1}\sum_v B_s(\Gamma-v)`$. Thus only the component orders of
$`\Gamma`$ itself are needed for the full-$`U`$ term.

If $`c(V)=1`$, that term is simply $`(q-1)^{n-1}z+(-1)^n`$.
If $`\Gamma`$ is disconnected, all its components are proper induced
subgraphs. Their isomorphism types, hence orders, can be recovered by the
following standard descending procedure. Kelly's count gives the number
$`s(H,\Gamma)`$ of induced copies of every connected graph $`H`$ on fewer
than $`n`$ vertices. Starting at the largest such orders, recover the number
$`m(H)`$ of components isomorphic to $`H`$ using

```math
 m(H)=s(H,\Gamma)-
       \sum_{\substack{C\text{ already recovered}\\|C|>|H|}}
          m(C)s(H,C).                                    \tag{16}
```

A connected induced copy lies within one component, and a component of
the same order contributes exactly one copy only when it is isomorphic
to $`H`$. These facts prove the descending recurrence. Formula (16) is
the familiar disconnected-graph reconstruction argument, used here only
to supply the top component-order term. Equations (15)--(16) prove the
third conclusion of the principal theorem.

A direct sum of the card polynomials $`\mathcal A`$ would not have given
the same proof. The exact identity is

```math
 \sum_v\mathcal A_{\Gamma-v}(q,z)
  =\sum_{S:\ N[S]=V}(n-|S|)(q-1)^{|S|-c(S)}z^{c(S)}
   +\sum_{S:\ |V\setminus N[S]|=1}
            (q-1)^{|S|-c(S)}z^{c(S)}.                    \tag{17}
```

A set failing to dominate exactly one vertex becomes dominating in the
card deleting that vertex. This additional term is why a naive Kelly
factor applied directly to maximal groups fails. Expansion (15) repairs
the failure by using induced component data instead.

## 6. A full associative census still loses inclusion structure

Here is a concrete limitation that persists simultaneously at every
prime $`p\ne3`$. On vertices $`0,1,2,3,4`$, take

```math
\begin{split}
 E(\Gamma)&=\{01,02,04,12,13,23\},\\
 E(\Delta)&=\{01,02,03,04,14,23\}.
\end{split}                                             \tag{18}
```

The graph $`\Gamma`$ is a diamond with a leaf attached to one of its
degree-two vertices. The graph $`\Delta`$ consists of two triangles sharing
one vertex. Their degree multisets are respectively
$`\{1,2,3,3,3\}`$ and $`\{2,2,2,2,4\}`$, so they are nonisomorphic.

They nevertheless have the same component polynomial:

```math
 Q=1+5xy+x^2(6y+4y^2)+x^3(6y+4y^2)
                         +x^4(4y+y^2)+x^5y.             \tag{19}
```

For a direct check, both graphs have six edges and no independent triple.
The four disconnected triples of $`\Gamma`$ are
$`034,124,134,234`$; those of $`\Delta`$ are the four triples avoiding
vertex $`0`$. In each graph, exactly one four-vertex subset is disconnected,
namely the one avoiding $`0`$. These counts establish every coefficient
in (19), independently of a general graph-isomorphism calculation.

Equations (8)--(10) imply that $`L_p(\Gamma)`$ and $`L_p(\Delta)`$ have
identical multisets of abstract isomorphism types of **all** associative
subloops, for every prime $`p\ne3`$. Each of these subloops is an
elementary abelian group, so its order specifies its type. The loops
themselves are nonisomorphic by the existing unmarked graph-recovery
theorem.

Their maximal-associative polynomials differ:

```math
\begin{split}
 \mathcal A_\Gamma(q,z)&=(q^4-q^2)z+(q+1)^2z^2,\\
 \mathcal A_\Delta(q,z)&=q^4z+(q+1)^2z^2.                 \tag{20}
\end{split}
```

For $`\Delta`$, a connected dominating support is exactly a set containing
$`0`$, contributing $`q^4z`$. A dominating support avoiding $`0`$ meets
each of the two peripheral edges, contributing $`(q+1)^2z^2`$.
For $`\Gamma`$, a connected dominating support contains $`0`$ and meets
$`\{1,2\}`$, while vertices $`3,4`$ can be chosen freely; its contribution
is $`q^2(q^2-1)z`$. The disconnected dominating supports consist of four
pairs, four triples, and one four-set, contributing
$`(4+4(q-1)+(q-1)^2)z^2=(q+1)^2z^2`$.

Since $`e=6`$, the number of maximal associative subloops of order
$`p^8`$ differs by $`p^2`$. Thus even the complete unaligned collection of
all associative subloop types does not determine which ones are maximal,
their inclusion pattern, or the ambient loop. This is not a counterexample
to the deletion reconstruction conjecture: the degree sequences show that
the two graph deletion decks, and hence the two intrinsic loop deletion
decks, are different. It is a precise obstruction to replacing those decks
by a census of abstract associative pieces.

No novelty claim is made for graph-polynomial collisions as a phenomenon
or for this pair as a graph example. Its role is an explicitly checked
loop-theoretic loss certificate for (10).

## 7. Known reconstruction controls and scope of the payoff

Regular graphs, trees, and disconnected graphs are established
reconstruction classes. Their transfer through the faithful graph-loop
construction does not create a new reconstruction class.

For regular graphs, the elementary argument is direct. Formula (12)
recovers the common degree $`r`$. In any card, the neighbors of its deleted
vertex are exactly the vertices of degree $`r-1`$; restoring a vertex
adjacent to that set reconstructs the graph. Tree reconstruction is
Kelly's theorem [K57, main theorem, pages 964--968]. The disconnected case
is the descending component argument (16). These controls illustrate the
existing graph-to-loop equivalence; the principal theorem instead
reconstructs the full censuses for **every** graph, including graphs outside
any class assumed reconstructible.

The result remains enumerative. It does not align central edge spaces of
different cards, reconstruct a factor set from unaligned restrictions,
produce a direct-product decomposition, or classify arbitrary Bol loops.
The census is a transform of known graph component data; its new role is
to count all associative subloops of the specific nonassociative law (1),
including their possible intersections with $`Z`$. The sharp loss example
(18)--(20) shows why this structural enumeration does not by itself solve
the harder gluing problem.

The deletion-deck manuscript gives a separate and stronger obstruction when
nongraphical alternating-map loops are admitted as competitors: a central
relation can identify two edge coordinates without changing any one of the
four coordinate-deletion cards of the two-disjoint-edge example. That
argument concerns actual card loops, whereas (18)--(20) concerns the
weaker census of associative pieces. Neither obstruction is a
counterexample inside the faithful ordinary-graph deletion problem.

For the Moufang suspensions treated in the preceding manuscript, one also
gets the count of associative subloops **containing $`Z`$**. Over $`p=2`$
for the binary cubic law, or $`p=3`$ for the all-ring law, their projected
counts are

```math
 a^{\mathrm M}_r={n\brack r}_p+p^{n-r+1}I_{r-1}(\Gamma;p)
 \quad(1\le r\le n+1),\qquad a^{\mathrm M}_0=1.          \tag{21}
```

Indeed, a transverse space is $`\mathbb F_p(m+x)\oplus H`$ with $`H`$
isotropic, and $`x+H`$ is arbitrary. In characteristic three, every
associative inverse image is an abelian group of exponent three, so the
central-intersection count (10), with $`a^{\mathrm M}`$, also gives the
full census. For the binary cubic law these groups need not be elementary
abelian, and (10) is not asserted. Formula (21) is an extension of the
enumerative calculation when the graph-derived card multiset is supplied;
this note does not independently construct an intrinsic admissible-frame
deck for those Moufang cases.

## 8. Exact computation and review boundaries

Run the standalone checker

```sh
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_deck_census.py
```

It uses no graph-loop implementation or third-party package. Its direct
linear side enumerates subspaces by reduced row echelon bases and
evaluates the alternating map on basis pairs or the associator, computed
from the factor set, on ordered basis triples including repetitions.
The proved bilinearity and trilinearity make these the required linear
tests. Its comparison side uses subset component counts and formulas
(4)--(10). It checks:

- all labeled graphs through four vertices over $`\mathbb F_2,\mathbb F_3`$
  for (5): 152 graph/field cases and 18,236 subspaces;
- all labeled graphs through four vertices over $`\mathbb F_2`$, and through
  three vertices over $`\mathbb F_5`$, for (8)--(9): 88 graph/field cases and
  33,609 projected subspaces;
- all 1,100 labeled graphs through five vertices for (15) and (17), and
  the 1,096 of those with $`n\ge3`$ for (11)--(13);
- every subloop, generated directly from the multiplication table, in
  five actual $`\mathbb F_2`$ loops of orders $`2,4,8,16,32`$, verifying
  (10) against associativity on every ordered triple in each subloop;
- the exact five-vertex collision (18)--(20), including direct examination
  of all 2,825 binary quotient subspaces for each of its two loops.

The final direct loop checks include the one-edge graph with one isolated
vertex: its order-32 loop has associative-subloop multiplicities
$`1,31,107,55,4`$ at orders $`1,2,4,8,16`$. The table search finds all 222
subloops, of which 198 are associative. This independently checks the
central-intersection count beyond preimages containing $`Z`$.

These finite cases do not prove the unrestricted statements. The exact
general arguments are Sections 1--6. The extension to nonprime coefficient
fields, recovery of inclusion data from censuses, and an extension-gluing
theorem from unaligned deletion cards remain outside the assertions.

## References and exact source scope

- **[Q26]** Youming Qiao, *A q-analogue of graph independence polynomials
  with a group-theoretic interpretation*,
  [arXiv:2408.09963v2](https://arxiv.org/abs/2408.09963v2), 11 June 2026.
  Theorem 1.2 and Section 2 establish isotropic counting polynomials;
  Lemma 2.3 is the edgewise linear-dependence criterion. Section 1.3
  interprets isotropic counts using abelian subgroups of graphical groups.
  The present note supplies a support formula and the additional Bol
  associativity and central-intersection calculation.
- **[TAM09]** P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration
  of Vertex Induced Subgraphs with respect to the Number of Components*,
  [arXiv:0812.4147v2](https://arxiv.org/abs/0812.4147v2), 3 February 2009;
  later published in *European Journal of Combinatorics* 32 (2011),
  954--974, [DOI:10.1016/j.ejc.2011.03.017](https://doi.org/10.1016/j.ejc.2011.03.017).
  Section 2.1 defines $`Q`$; Theorem 27 states vertex reconstructibility.
  Section 4 above gives the complete component-count argument used here.
- **[KPT12]** Tomer Kotek, James Preen and Peter Tittmann, *Subset-Sum
  Representations of Domination Polynomials*,
  [arXiv:1207.2430v1](https://arxiv.org/abs/1207.2430v1), 10 July 2012;
  *Graphs and Combinatorics* 30 (2014), 647--660,
  [DOI:10.1007/s00373-013-1286-z](https://doi.org/10.1007/s00373-013-1286-z).
  Section 3, Corollary 11 and equation (5) give the ordinary domination
  component-size expansion to which (15) is a weighted analogue.
- **[K57]** Paul J. Kelly, *A congruence theorem for trees*, *Pacific
  Journal of Mathematics* 7 (1957), 961--968,
  [primary PDF](https://msp.org/pjm/1957/7-1/pjm-v7-n1-p14-s.pdf).
  Lemma 1 gives the proper-subgraph double count; the main theorem proves
  tree reconstruction. The induced-count instance (11) is proved directly.

The existing graph-loop faithfulness used to turn abstract cards into graph
cards has its exact He--Qiao dependency recorded in the
[all-ring manuscript](../../graph-loops/manuscripts/graph-eisenstein-loops.md#unmarked-recovery-over-prime-fields).
No graph reconstruction conjecture or unproved alignment assertion is a
dependency of the census theorem.
