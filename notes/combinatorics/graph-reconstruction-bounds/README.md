# Counting and stability in graph reconstruction

**Mira**

What can we say about graph reconstruction without assuming that every graph is reconstructible? There are two distinct questions: how many parents a single deck can have, and where a failure of uniqueness could lie in the space of graphs. We obtain three bounds.

- **Number of parents.** An ordinary deck with $`n\ge3`$ cards has at most $`(n!)^{2/(n-2)}`$ nonisomorphic parents. This is asymptotic to $`n^2/e^2`$ and implies that the language *Legitimate Deck* is in LWPP.
- **Distance to a reconstructible graph.** From any sufficiently large graph, changing $`O(\log n)`$ edges suffices to obtain a graph uniquely identified by its ordinary deck. Only edges touching two chosen vertices need to change.
- **A random graph's distance from any counterexample.** For independent edges with probabilities in $`[\beta,1-\beta]`$ and $`\beta n/\log n\to\infty`$, with probability at least $`1-\exp(-c\beta n^2)`$ every graph within $`\lfloor c\beta n^2\rfloor`$ edits of the sample is reconstructible. The adversary may choose the edits *after* seeing the sample.

[Read the standalone paper (PDF)](paper/counting-and-stability.pdf) · [LaTeX source and build instructions](paper/README.md)

The first theorem counts labeled representatives and uses the fact that every edge appears in exactly $`n-2`$ labeled deletions. The other two depend on a structural constraint: any hypothetical nonreconstructible graph has linearly many disjoint pairs of vertices with only logarithmically many differences between their neighborhoods. One such pair can be marked cheaply enough for the deck to identify its clone. Many such pairs are simultaneously unlikely in a large random edit ball. Neither argument proves the Reconstruction Conjecture or provides a counterexample.

## Counting the parents of one deck

All graphs here are finite, simple and undirected. Fix a realizable deck $`D`$ with $`n\ge3`$ cards, each of order $`n-1`$. Let $`p(D)`$ be the number of isomorphism classes of graphs with deck $`D`$. For each such class $`G`$, its labeled orbit $`O_G`$ is the set of all graphs on the fixed vertex set $`[n]`$ isomorphic to $`G`$. It has $`n!/|\operatorname{Aut}(G)|`$ elements. Let $`L`$ be the smallest of these orbit sizes.

**Theorem.** The number of parent classes satisfies

```math
p(D)\;\le\; L^{2/(n-2)}\;\le\;(n!)^{2/(n-2)}.
```

The key is to count whole labeled graphs in two ways. Each parent class contributes at least $`L`$ different graphs. Yet for any fixed deleted label, **every** card that can appear is already visible among the labelings of just one parent class, the one with orbit size $`L`$.

**Proof.** Let $`U`$ be the disjoint union of all the labeled parent orbits, so $`|U|\ge p(D)L`$. For a label $`i`$, let $`\pi_i`$ delete the vertex with that label, keeping the other labels unchanged. Choose one parent class $`G_0`$ with $`|O_{G_0}|=L`$. Then

```math
\pi_i(U)=\pi_i(O_{G_0}),\qquad |\pi_i(U)|\le L.
```

Indeed, take a card $`C`$ on $`[n]\setminus\{i\}`$ arising from any graph in $`U`$. Some vertex deletion in $`G_0`$ yields the same **unlabeled** card type, since both parents have deck $`D`$. Choose an isomorphism from that deletion to $`C`$, and give its omitted vertex label $`i`$. This produces a member of $`O_{G_0}`$ whose projection is exactly $`C`$, with its given labels. The reverse inclusion is immediate. No correspondence between the labels of different cards is required.

We now apply the finite projection form of [Shearer's entropy inequality](https://doi.org/10.1016/0097-3165(86)90019-1):

```math
|U|^{n-2}\;\le\;\prod_{i=1}^n |\pi_i(U)|.
```

Here is a proof for these particular projections. Pick $`X`$ uniformly from $`U`$, represented by its edge-indicator bits, and fix an ordering of the $`\binom n2`$ possible edges. Write $`H`$ for Shannon entropy in bits. In the chain-rule expansion of $`H(\pi_i X)`$, each surviving edge bit is conditioned only on the earlier *surviving* bits. Its conditional entropy is therefore at least its conditional entropy given **all** earlier bits of $`X`$. Every edge survives exactly $`n-2`$ deletions: only deleting either endpoint removes it. Summing the chain rules gives

```math
(n-2)\log_2 |U|=(n-2)H(X)
\;\le\;\sum_{i=1}^n H(\pi_i X)
\;\le\;\sum_{i=1}^n\log_2 |\pi_i(U)|.
```

The last inequality is the elementary bound on entropy by the logarithm of the support size. Exponentiating and substituting the orbit bounds yields $`(p(D)L)^{n-2}\le L^n`$. Since $`L>0`$, the theorem follows. ∎

### A bound computable from the card types

Let $`b(D)`$ denote the number of different **labeled** cards on a fixed $`(n-1)`$-element vertex set that occur as labelings of some card type in $`D`$. Equivalently,

```math
b(D)=\sum_{J\text{ a distinct type in }D}\frac{(n-1)!}{|\operatorname{Aut}(J)|}.
```

Each type occurs only once in this sum, even if many vertices give that type. The common projection in the proof has exactly $`b(D)`$ elements, and the projection of *each* parent orbit maps onto that set. Therefore $`b(D)\le L`$ and

```math
   (p(D)b(D))^{n-2}\le |U|^{n-2}\le b(D)^n,
   \qquad p(D)\le b(D)^{2/(n-2)}.
```

In fact the proof gives $`p(D)\le b(D)^{n/(n-2)}/L`$ when $`L`$ is known. The $`b(D)`$-only version is useful because it can be evaluated from the deck without already knowing its parents; computing automorphism group sizes is not claimed to be easy here. Integrality can matter: $`b(D)^2<2^{n-2}`$ certifies that a legitimate deck has exactly one parent. For an elementary example, the deck of a single edge and 14 isolated vertices has $`n=16`$ and $`b(D)=1+\binom{15}{2}=106`$. Its labeled cards are either empty or have exactly one edge. Since $`106^2<2^{14}`$, the inequality alone certifies uniqueness. This example illustrates the criterion, not a new family of reconstructible graphs.

### Why the unknown labels do not invalidate the entropy calculation

The labels in the proof index a set of *possible complete graphs*; they are not extra information supplied with the deck. Two distinct cards need not come equipped with any consistent identification of their common vertices. In particular, it would be incorrect to multiply the number of independently chosen card labelings and call that the number of parents. The projection inequality bounds an actual set of joint objects by projections that may be highly dependent.

There is a second way to see why so little information about the parent can be concealed. Let $`T`$ be a uniformly selected **unlabeled** parent type, and given $`T`$, let $`X`$ be uniform over the labeled representatives of that type. Then $`T`$ is determined by $`X`$ and $`H(X)=H(T)+H(X\mid T)`$. For each fixed $`i`$, however, the law of $`\pi_iX`$ is independent of $`T`$: the omitted vertex is uniform in the parent, so its card type has the frequencies in the common deck; conditional on its type the surviving labeling is uniform. This uses the ordinary card **multiplicities**. For example, a particular labeled card of type $`J`$ occurring $`m_J`$ times has probability $`(m_J/n)|\operatorname{Aut}(J)|/(n-1)!`$ regardless of $`T`$.

Now $`H(\pi_iX)=H(\pi_iX\mid T)\le H(X\mid T)`$, because deletion is a deterministic map. The same edge-coverage chain rule therefore gives

```math
 (n-2)\bigl(H(T)+H(X\mid T)\bigr)
 \le \sum_i H(\pi_iX)
 \le n H(X\mid T).
```

Since $`H(T)=\log_2 p(D)`$ and $`H(X\mid T)\le\log_2(n!)`$, this again yields the advertised uniform bound. This viewpoint distinguishes equality of the projection *distributions* for randomly relabeled parents from equality of their *supports*, the simpler fact sufficient for the first proof.

## The polynomial bound and Legitimate Deck

**An explicit polynomial for every order.** For $`n\ge6`$, the first three factors of $`n!`$ have product $`6\le n`$, and the remaining $`n-3`$ factors are each at most $`n`$. Thus $`n!\le n^{n-2}`$ and $`p(D)\le n^2`$. For $`n=3,4,5`$, fix one card on a labeled set. Every parent has a representative obtained by attaching a new vertex to a subset of that card, so $`p(D)\le2^{n-1}\le n^2`$. Orders one and two have at most one and two parent classes respectively; if order zero is admitted, there is only the empty graph. Consequently $`q(n)=(n+1)^2`$ is a single polynomial valid at every order. Stirling's formula gives $`(n!)^{2/(n-2)}=(1+o(1))n^2/e^2`$. This is the asymptotic size of the **upper bound**, not a lower bound on attainable ambiguity.

**Complexity.** The decision problem *Legitimate Deck* asks whether a given list of graphs is the vertex deck of any graph, disregarding ordering and vertex names. Hemaspaandra, Hemaspaandra, Spakowski and Watanabe [defined the polynomial bounding question and proved its complexity consequence](https://doi.org/10.4230/LIPIcs.MFCS.2018.51): their Conjecture 4.5 asks for a bound $`q(n)`$ on the number of nonisomorphic preimages, and Corollary 4.9 proves that if this holds for some polynomial $`q`$, then Legitimate Deck is in LWPP. The theorem above supplies that hypothesis. Their Corollary 4.10 also applies: Legitimate Deck is not NP-Turing-hard unless NP is low for PP. Informally, in LWPP a difference of accepting and rejecting computation-path counts is zero on no-instances and hits a specified nonzero target on yes-instances, where the target depends only on input length and is polynomial-time computable. The length of the encoded input is not the number of cards; the cited complexity result already handles that distinction. Thus membership is not a claim of deterministic polynomial-time recognition, counting, or reconstruction.

**What remains open.** The bound gives neither two nonisomorphic parents of a deck nor a proof that there can only be one. A natural intermediate question is whether the number of parents is bounded by an absolute constant independent of $`n`$.

## Linearly many pairs with logarithmic neighborhood discrepancy

For two distinct vertices $`u,v`$ of a finite simple graph $`G`$, let

```math
 d_G(u,v)=\bigl|\{w\notin\{u,v\}:w\text{ is adjacent to exactly one of }u,v\}\bigr|.
```

Thus $`d_G(u,v)`$ counts the entries on which their adjacency rows disagree
after the two endpoint positions have been removed. It is not a graph
distance. Write $`H_D(G)`$ for the graph on $`V(G)`$ in which $`uv`$ is an
edge if and only if $`d_G(u,v)\le D`$; this says nothing about whether
$`uv`$ is an edge of $`G`$. The ordinary deck is the multiset of unlabelled
graphs $`G-v`$, with one occurrence for each vertex. Nonreconstructible
means that some nonisomorphic graph has the same ordinary deck.

**A linear matching of near-twins.**
Let $`G`$ be a nonreconstructible graph of order $`n\ge 2^{20}`$ and put
$`D=\lceil320\log_2 n\rceil`$. Every vertex cover of $`H_D(G)`$ has more
than $`n/160`$ vertices. In particular, every inclusion-maximal matching
of $`H_D(G)`$ has more than $`n/320`$ edges.

The conclusion concerns distinct *endpoints* in one parent. It does
not say that the sets of vertices distinguishing the matched pairs are
disjoint, or that a surviving mate can be identified on an individual
card. The proof proceeds by contraposition. A small cover leaves a large
set of mutually distinct exterior rows. Sampling exposes enough of their
differences to obtain landmarks. The difficulty is to count all placements
of those landmarks without paying for every permutation of the cover.

### A landmark criterion requiring no distinguished copy

A named graph here is a graph on a fixed set of positions. For such a
graph $`F`$, let $`c_X(F)`$ be the number of injections of its positions
into $`X`$ preserving both edges and nonedges. If $`|F|<n=|X|`$, then

```math
 c_X(F)=\frac{1}{n-|F|}\sum_{v\in V(X)}c_{X-v}(F).
 \tag{1}
```

Indeed, an injection survives precisely the deletions outside its image.
Thus comparing named pattern counts requires no names on an input card.

Fix an ordered tuple $`L`$ of $`r<n`$ distinct vertices of $`G`$. An exterior
vertex has a binary *word* giving its adjacency to $`L`$ in order.
Call $`L`$ resolving if these words are distinct among vertices outside
$`L`$. No assumption is made about other induced copies of $`G[L]`$.

**Resolving landmarks.**
Let $`L`$ be resolving, let $`F=G[L]`$ be named by the tuple, and let
$`N=n-r`$. If

```math
 \frac{c_G(F)}{|\operatorname{Aut}(G)|}<2^{N/2-1},
 \tag{2}
```

then the ordinary deck determines $`G`$ up to isomorphism.

**Proof.**
In an arbitrary host $`X`$ of order $`n`$, fix one induced injection
$`j:F\to X`$. Read the exterior words relative to $`j`$. Discard positions
with a word absent from the target $`G`$. Every remaining position has a
unique target vertex as its name, though several positions in $`X`$ may
receive the same name. Define a conflict graph $`C_j`$ on these positions:
two conflict if their names coincide, or if the names are distinct and
their adjacency in $`G`$ disagrees with the adjacency of the positions
in $`X`$. An independent set therefore gives a set $`S`$ of distinct target
names and exactly one induced injection of $`G[L\cup S]`$ extending $`j`$.
Conversely, each such injection gives one independent set in the
conflict graph of its own root placement.

Put $`I(C;z)=\sum_{A\text{ independent in }C}z^{|A|}`$ and
$`P_X(z)=\sum_j I(C_j;z)`$, summing over *all* induced placements
of $`F`$. The bijection just described gives

```math
 [z^k]P_X(z)=
 \sum_{\substack{S\subseteq V(G)\setminus L\\|S|=k}}c_X(G[L\cup S]).
 \tag{3}
```

By (1), the coefficients below degree $`N`$ agree between
hosts with the same deck. At degree $`N`$ the only possible embeddings are
isomorphisms from the full target. Thus a nonisomorphic host $`X`$ with
the same deck as $`G`$ would satisfy

```math
 P_G(z)-P_X(z)=|\operatorname{Aut}(G)|z^N.
```

Set $`b=1+\sqrt2`$, $`a=2+\sqrt2`$. For every graph $`C`$ on $`m`$ vertices,
$`|I(C;-a)|\le b^m`$. For a union of isolated vertices and isolated edges,
use multiplicativity and the factors $`1-a=-b`$ and $`1-2a=-b^2`$. Otherwise
split independent sets according to inclusion of a vertex of degree
$`d\ge2`$. Induction bounds the result by $`b^{m-1}+a b^{m-d-1}\le b^m`$,
since $`b^2+a\le b^3`$. This includes the empty graph as the base case.
Consequently $`|P_X(-a)|\le c_X(F)b^N`$ and likewise for $`G`$. Since
$`c_X(F)=c_G(F)`$, the displayed polynomial difference would force

```math
 \frac{c_G(F)}{|\operatorname{Aut}(G)|}
 \ge \frac12(a/b)^N=2^{N/2-1},
```

contrary to (2). The tuple $`L`$ was used only in the
comparison proof; its location was not provided in any card.
∎

### Keeping the cover anonymous

We use one external group-theoretic input. A permutation's support is
the set of points it moves. By [Kempe, Pyber and Shalev, Theorem A(2)](https://doi.org/10.4171/GGD/24), a permutation group on $`t\ge2`$ points
in which every nonidentity element has support of size at least
$`\log_2 t`$ has order at most $`2^{10t}`$. Transitivity is not required.

Let $`U\subseteq V(G)`$ and $`B=V(G)\setminus U`$. Partition $`U`$ by equality
of its full adjacency words on $`B`$. There is a set $`W_0\subseteq B`$ of
size at most $`|U|`$ that defines the same partition. Start with no test
coordinates. Whenever two unequal full words remain together, add a
coordinate on which they differ. Each addition increases the number of
classes. For $`U=\varnothing`$ take $`W_0=\varnothing`$.

**An anonymous-cover automorphism bound.**
Let $`T\supseteq U\cup W_0`$, $`t=|T|\ge2`$, and $`B_T=T\setminus U`$.
Assume every distinct $`b,b'\in B_T`$ have at least $`\log_2 t`$
distinguishers in $`G[T]`$. Then

```math
 \frac{|\operatorname{Aut}(G[T])|}{|\operatorname{Aut}(G)|}
 \le 3^t 2^{10t}.
 \tag{4}
```

**Proof.**
The subgroup $`A`$ preserving $`U`$ and $`W_0`$ separately as sets has index
at most $`3^t`$: count the possible images of the three-part coloring of
$`T`$. Its elements permute $`B_T`$ and permute the classes of $`U`$, since
equality of words on the setwise preserved $`W_0`$ detects the full
partition. For each class $`C`$ create $`|C|`$ formal positions
$`(C,1),\dots,(C,|C|)`$. Act on $`B_T`$ as on actual vertices and on these
new positions by $`(C,i)\mapsto(gC,i)`$. This is an action on exactly $`t`$
points. It does not assume that $`g`$ respects any numbering of the
actual vertices inside $`C`$.

Its kernel consists precisely of elements fixing $`B_T`$ pointwise: such
an element fixes $`W_0`$ pointwise and hence preserves every class. Each
kernel element extends, by the identity off $`T`$, to an automorphism of
$`G`$. In fact it fixes the $`B_T`$ side, and vertices exchanged inside a
class have equal incidences to every vertex of $`B`$, including those
outside $`T`$. These extensions are distinct. The kernel therefore has
order at most $`|\operatorname{Aut}(G)|`$.

A nonidentity element of the image moves some actual $`b\in B_T`$ to
$`b'\ne b`$. Any distinguisher in $`B_T`$ must move. If a vertex of a class
$`C`$ distinguishes $`b,b'`$, then all vertices of $`C`$ do, and $`gC\ne C`$:
otherwise invariance of the incidences to the class would give the same
bit at $`b`$ and $`b'`$. All $`|C|`$ formal positions of such a class move.
Hence the image element moves at least $`d_{G[T]}(b,b')`$ points. Apply
the quoted motion bound to the image (the trivial image also satisfies
the order bound), then multiply by the kernel and index estimates.
∎

### Sampling the landmarks and closing the count

**Proof of the matching theorem.**
Suppose $`U`$ covers $`H_D(G)`$ and $`u=|U|\le n/160`$. Put
$`\ell=\log_2 n`$. Distinct vertices of $`B=V(G)\setminus U`$ have more
than $`D`$ distinguishers in $`G`$, which may include vertices of $`U`$.
Sample a set $`Z`$ by including *every* vertex independently with
probability $`1/80`$. For each fixed pair in $`B`$, its number $`X`$ of sampled
distinguishers is binomial with mean $`\mu\ge4\ell`$. Markov's inequality,
applied to $`4^{-X}`$, gives

```math
 \Pr(X<\ell)\le 4^\ell\mathbb E[4^{-X}]
 \le \exp\bigl(\ell\ln4-3\mu/4\bigr)
 \le \exp\bigl(-(3-\ln4)\ell\bigr).
```

A union bound over fewer than $`n^2`$ pairs is at most $`n^{-0.328}<1/26`$
for $`n\ge2^{20}`$, since $`(3-\ln4)/\ln2-2>0.328`$.
Also $`\Pr(|Z|>13n/1000)\le25/26`$ by Markov's inequality. Thus there is
one sample for which both bounds hold; independence of these success
events was not used.

Use $`W_0`$ as above and take $`T=U\cup W_0\cup Z`$. Then
$`t=|T|\le2u+13n/1000\le0.0255n<0.026n`$. Every two exterior vertices
are distinguished by $`T`$, as are all distinct vertices of $`B_T`$ by at
least $`\ell`$ vertices of $`T`$. Thus the exterior words relative to $`T`$
are distinct and the anonymous-cover lemma applies, since $`\ell\ge\log_2 t`$.
The automorphism bound is immediate also for $`t=0,1`$.

Temporarily order $`T`$ and put $`F=G[T]`$ with these names. Each choice of
its image set supports either no induced injection or precisely
$`|\operatorname{Aut}(G[T])|`$ of them. By (4),

```math
 \frac{c_G(F)}{|\operatorname{Aut}(G)|}
 \le \binom nt\,3^t 2^{10t}.
```

With $`H_2(x)=-x\log_2 x-(1-x)\log_2(1-x)`$ (and the continuous endpoint
values), $`\binom nt\le2^{n H_2(t/n)}`$ by the binomial theorem. The
base-two logarithm of the right-hand side is at most

```math
 n\bigl(H_2(0.026)+0.026(10+\log_2 3)\bigr)<0.48n
 <(n-t)/2-1.
```

For the last inequality use $`(n-t)/2-1\ge0.487n-1`$ in the asserted
range. The landmark criterion (2) now holds with
$`N=n-t`$, so $`G`$ is reconstructible. This rules out every such
cover in a counterexample. The endpoints of any inclusion-maximal
matching form a vertex cover: an uncovered edge could be added to the
matching. Dividing the strict cover bound by two proves the claim.
∎
## Editing an arbitrary graph to a reconstructible one

One edit toggles one unordered pair on a fixed vertex set. Write
$`d(G,H)=|E(G)\mathbin{\triangle} E(H)|`$, and let $`\mathcal R_n`$ be the
graphs on $`[n]`$ uniquely determined, up to isomorphism, by their ordinary
vertex decks. [Asilis, Chen, Hansen and Teng, §4, p. 12:15](https://doi.org/10.4230/LIPIcs.ITCS.2026.12)
asked about $`d(G,\mathcal R_n)=\min_{H\in\mathcal R_n}d(G,H)`$. For $`n\ge3`$, isolating
one vertex gives the bound $`n-1`$: any graph with an isolated vertex is recovered by
reattaching an isolated vertex to a card of the appropriate edge count.
Their observation about three edits concerns *edge* decks, not vertex
decks.

**Covering theorem.**
Let $`n\ge 2^{20}`$, $`D=\lceil320\log_2 n\rceil`$ and $`k=\lceil2\log_2 n\rceil`$.
Every graph $`G`$ on $`[n]`$ can be changed to a member of $`\mathcal R_n`$ in
at most $`D+12k`$ edits, all incident to at most two vertices. Such an
edited graph can be constructed in polynomial time from $`G`$.

The aim is not just to create twins. We make a twin whose place in an
actual card can be recognized among *all* possible reconstructions.
Call vertices twins if they have identical neighborhoods outside the pair;
their mutual adjacency is unrestricted.

**Twin-count lemma.**
If $`n\ge3`$ and $`2\binom n2<2^{n-2}`$, the total number of unordered twin pairs of an
$`n`$-vertex graph is determined by its ordinary deck.

**Proof.** Let $`s(u,v)`$ be the number of vertices outside $`\{u,v\}`$ adjacent to exactly
one of $`u,v`$. Form the homogeneous polynomial

```math
 F_G(X,Y)=\sum_{\{u,v\}} X^{s(u,v)}Y^{n-2-s(u,v)} .
```

Deleting a vertex other than $`u,v`$ removes one distinguisher or one
nondistinguisher. Thus the sum of $`F_J`$ over the card occurrences $`J`$
is $`(\partial_X+\partial_Y)F_G`$. Any two candidate polynomials differ
by $`a(X-Y)^{n-2}`$: in coordinates $`X-Y,Y`$ the differential operator is
just differentiation in the second coordinate. Moreover $`a`$ is an integer,
as seen from the leading coefficient. If $`a\ne0`$ the coefficient
$`\ell^1`$-norm of the difference is at least $`2^{n-2}`$, whereas the sum
of the two coefficient masses is $`2\binom n2`$. So $`F_G`$, in particular
its $`Y^{n-2}`$ coefficient, is fixed. □

Here is a second ordinary-deck test on a specific card $`J`$. The total
edge count is the sum of the card edge counts divided by $`n-2`$; subtracting
$`|E(J)|`$ gives the missing degree $`r`$. This determines the entire degree
multiset by ranging over the card occurrences. Write
$`Q_G(z)=\sum_{w\in V(G)}z^{\deg_G(w)}`$. If the added vertex has
neighborhood $`S\subseteq V(J)`$, then

```math
 Q_G(z)-Q_J(z)=z^r+(z-1)\sum_{w\in S}z^{\deg_J(w)} .
```

Thus both $`|S|`$ and its neighbor counts in each degree class of $`J`$ are
prescribed, without matching any vertices across cards.

**Proof of the covering theorem.** If every pair has $`s(u,x)>D`$, the structural near-pair matching theorem above already gives
$`G\in\mathcal R_n`$. Otherwise fix a pair with $`s(u,x)\le D`$. By editing
at most $`D`$ edges at $`x`$, make $`x`$ and $`u`$ twins. Let $`X=G-\{u,x\}`$,
write $`a_w=\deg_X(w)`$, and let $`N_0`$ be their common neighborhood in
$`X`$. Retain their mutual bit $`e`$. Choosing a new common neighborhood
$`N`$ costs $`2|N\mathbin{\triangle}N_0|`$ further edits. Call the resulting
graph $`P`$ and consider $`J=P-x`$. Put $`c=|N|`$, $`b_w=\mathbf 1_{\{w\in N\}}`$.

We shall choose $`N`$ so that the only possible center of a copy of the
missing twin row on $`J`$ is $`u`$. More precisely, a clone of $`v`$ in $`J`$
joins every neighbor of $`v`$ in $`J`$ and joins $`v`$ itself according to
a bit $`f`$. For every $`v\in X`$ and $`f\in\{0,1\}`$ we will rule out
its clone by the required degree $`c+e`$ or by the degree-exposure identity.

First suppose that the number $`s`$ of distinct $`a_w`$ is less than $`2k`$.
Forbid the at most $`3s`$ values $`a_w,a_w+1,a_w+2`$. Choose $`c`$ in
$`[0,n-2]`$ within $`3s`$ of $`|N_0|`$ such that $`c+e`$ is not forbidden.
There are at least $`3s+1`$ available integer choices of $`c`$ in this
interval even at either end, since $`3s<n-1`$. Change $`N_0`$ to a set
of this size by only insertions or only deletions. This costs at most
$`6s<12k`$ edits. A clone at $`v\in X`$ has degree $`a_v+b_v+f`$, one of
the forbidden values.

Now suppose $`s\ge2k`$. Choose $`k`$ vertices $`W\subset X`$ with distinct
$`a_w`$ separated by at least two: repeatedly take the least remaining
degree and discard it and its successor. Keep $`N`$ fixed off $`W`$, allowing
its $`k`$ bits on $`W`$ to vary, at cost at most $`2k`$. For a rival center $`v`$
and bit $`f`$, the true exposure sum in the degree-exposure identity minus the
rival's exposure sum is

```math
 (e-b_v)z^c+(b_v-f)z^{a_v+b_v}
 +\sum_{w\in X\setminus\{v\}}(b_w-A_X(v,w))z^{a_w+b_w},
```

where $`A_X(v,w)`$ is the adjacency bit. Fix $`f`$, $`b_v`$, and $`c`$. Changing
$`b_w`$ from zero to one for $`w\in W\setminus\{v\}`$ increments the varying
sum by $`z^{a_w+1}`$ if $`A_X(v,w)=0`$, and by $`z^{a_w}`$ otherwise.
These monomials have distinct exponents, so their subset sums are all
different. Among patterns with the fixed triple, at most one can give
zero difference. The total $`c`$ has at most $`k+1`$ possible values;
conditioning on it is essential since it depends on the pattern.
Across all rivals, at most $`4(n-2)(k+1)<n^2\le2^k`$ patterns are ruled
out. Take any of the others.

To verify the certificate against an arbitrary parent, first observe that
$`u`$ has no twin in $`J`$. Such a twin $`v\in X`$ would be interchangeable
with $`u`$ by an automorphism of $`J`$, so its clone with $`f=e`$ would pass
both tests. Every twin pair of $`J`$ therefore lies in $`X`$. Its two
vertices see $`u`$ alike and hence also see $`x`$ alike in $`P`$. No old twin
pair was lost, and $`u,x`$ are twins. Thus $`P`$ has strictly more twin pairs
than $`J`$. By the twin-count lemma, so does every parent of the deck
of $`P`$. Present any such parent on the same labeled copy of $`J`$ by
choosing a deletion of that card type. Adding a vertex cannot turn a
surviving nontwin pair into twins, so the new vertex must itself be
a twin of some center in $`J`$. The two tests exclude every center except
$`u`$, and the prescribed missing degree fixes $`f=e`$. Every parent is
therefore isomorphic to $`P`$.

All pair distances and degree tests above are computable from the
labeled input. In the many-degree case one may try all $`2^k<2n^2`$
patterns and all their clone tests. This constructs $`P`$ in polynomial
time, without deciding whether an arbitrary input deck has a parent. □

For smaller orders $`n\ge3`$ the isolated-vertex bound suffices. Thus the
covering radius of $`\mathcal R_n`$ is $`O(\log n)`$; no positive lower
bound is asserted. If the Reconstruction Conjecture holds, this
distance is always zero.

## Reconstruction throughout a random edit ball

The preceding theorem chooses favorable edits. We now ask for a graph
that stays reconstructible under *every* edit pattern in a given
ball, even when the pattern is chosen after seeing the graph. Write
$`B_b(G)=\{H:d(G,H)\le b\}`$.

**Robustness theorem.**
Let $`n\ge2^{20}`$, $`D=\lceil320\log_2 n\rceil`$, and $`m=\lceil n/320\rceil`$.
Let the edges of $`G`$ be independent with arbitrary probabilities in
$`[\beta,1-\beta]`$, where $`0<\beta\le1/2`$. Set

```math
 q=2\beta(1-\beta),\qquad K=m(n-2m),\qquad
 A=\frac{n!}{(n-2m)!\,2^m m!}.
```

For every integer $`b\ge0`$,

```math
 \Pr\{B_b(G)\not\subseteq\mathcal R_n\}
 \le \min\{1,\ A\Pr[\operatorname{Bin}(K,q)\le b+mD]\}.
```

In particular, if $`\beta=\beta(n)`$ satisfies $`\beta n/\log n\to\infty`$,
then for all sufficiently large $`n`$, uniformly over the allowed edge
probabilities,

```math
 \Pr\{B_{\lfloor c\beta n^2\rfloor}(G)\subseteq\mathcal R_n\}
 \ge1-\exp(-c\beta n^2),\qquad c=10^{-4}.
```

**Proof.** Fix a matching $`M`$ of $`m`$ unordered vertex pairs (not necessarily graph
edges). For each $`\{u,v\}\in M`$ and each $`w`$ outside the $`2m`$ endpoints,
compare the bits $`uw`$ and $`vw`$. Let $`L_M`$ count the disagreements in
these $`K`$ comparisons. The comparisons use disjoint pairs of edge
coordinates, so are independent. If the two edge probabilities are
$`p,t`$, the mismatch probability $`p(1-t)+(1-p)t`$ is at least $`q`$,
by minimizing at the four corners of $`[\beta,1-\beta]^2`$. Thus
$`L_M(G)`$ stochastically dominates $`\operatorname{Bin}(K,q)`$.

Each edit changes $`L_M`$ by at most one. If $`H\in B_b(G)`$ fails
reconstruction, the structural near-pair matching theorem above gives it some matching
$`M`$ of $`m`$ pairs, each with at most $`D`$ distinguishing vertices.
Consequently $`L_M(H)\le mD`$ and $`L_M(G)\le b+mD`$. Union-bounding
the fixed-matching probabilities over the $`A`$ possible $`M`$ proves
the finite probability bound. In particular, $`M`$ need not have been selected
independently of the sampled graph.

For the stated orders, $`K\ge0.003n^2`$, $`q\ge\beta`$ and
$`\ln A\le2m\ln n`$. When $`\beta n/\log n\to\infty`$, eventually
$`mD\le qK/4`$ and $`\ln A\le qK/16`$. If $`b\le qK/4`$, the
multiplicative Chernoff bound at half the mean gives a failure
probability at most $`A\exp(-qK/8)\le\exp(-qK/16)`$. The specified
$`c`$ satisfies both the radius and the exponent bounds. □

For fixed $`\beta>0`$ this is a quadratic number of arbitrary edits, with
failure exponentially small in $`n^2`$. [Asilis et al., Corollaries 18–21](https://doi.org/10.4230/LIPIcs.ITCS.2026.12)
give an unrestricted edit radius of order $`n/\log n`$ in this dense
model; their robust asymmetry event has failure $`\exp(-\Omega(n))`$.
They also allow quadratically many edit locations when the support is
sampled independently of the graph, with edits then unrestricted
within that support ([Lemma 13 and Theorem 15](https://doi.org/10.4230/LIPIcs.ITCS.2026.12)). Their structural
event controls asymmetry and distinctness of induced subgraphs missing
any fixed number of vertices; their work also yields three-card
reconstruction for the sampled graph. The robustness theorem above asserts
ordinary full-deck reconstruction, not these stronger properties:
indeed at most $`n-2`$ edits can make any designated pair twins.

## References for the counting argument

For fixed minimum degree bound $`k`$, [Kratsch and Hemaspaandra, proof of Theorem 6.1](https://doi.org/10.1007/BF01578845) already use a suitable low-degree hole card to limit candidate extensions to $`O(n^k)`$. No such degree hypothesis appears in the bound above. The entropy covering inequality is classical; [Bollobás and Thomason](https://doi.org/10.1112/blms/27.5.417) use the uniform-cover method for hereditary families of hypergraphs; the application here uses the common projection supports of labeled parent orbits. A related [preprint by Jianming Wang](https://doi.org/10.5281/zenodo.21297717) bounds the number of reconstructions using one-card extensions, degrees and overlaps. Its Theorem 14.4 gives a universal central-binomial upper bound; Corollary 15.3 gives polynomial bounds under a degree-profile hypothesis, and Theorem 20.3 gives smaller bounds under additional assembly hypotheses. None of those hypotheses is used above. The complexity implication is due to Hemaspaandra and coauthors, not to the present counting argument. No claim of exhaustive historical priority is made.

## What has and has not been checked

The arguments above are mathematical proofs. They do not rely on an exhaustive search over graphs. The entropy, marker, and random-ball proofs and the structural lemma have undergone independent AI-assisted checks. The source of the only non-elementary group bound is Kempe, Pyber and Shalev, Theorem A(2); the complexity implication is imported from Hemaspaandra and coauthors. No formal verification, external referee acceptance or exhaustive priority review is claimed.
