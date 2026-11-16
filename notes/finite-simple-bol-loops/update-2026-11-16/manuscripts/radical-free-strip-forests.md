# Full strips and forests in paired simple envelopes

**Independently reviewed continuation of 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** Let $`(G,H,K,\tau)`$ be the faithful generated canonical folder of a finite simple nonassociative left Bol loop, with

```math
G=N\times N,\qquad N=T^k,\qquad \tau(x,y)=(y,x),
```

where $`T`$ is finite nonabelian simple. The full marked set and the normal-quotient criterion used below are those in [the paired-simple manuscript](radical-free-paired-simple-envelopes.md) at `4c93742a59ccdd786f23598f0374f674c6f75fff` and [the path manuscript](radical-free-path-factorizations.md) at `c1be0daa47ca5f6befeb96378bc1937544acbde1`, with the faithful-folder and normal-subloop interfaces of [C0001](../proofs/C0001.md) at `9431ade99316d6bc62efb389492fef385b510b45`. The involution-class input is Fried–Guralnick–Saxl, *Schur covers and Carlitz's conjecture*, Lemma 12.1, [authors' PDF §12 p. 26](https://www.math.uci.edu/~mfried/paplist-ff/sch-carlitz.pdf), as scoped in the paired-simple manuscript; it uses CFSG.

All outside involutions form one $`G`$-class. Consequently the actual mark is full,

```math
K=\{(x,x^{-1}):x\in N\},\qquad
\Lambda^2=K^2=\{(a,b): b\text{ is }N\text{-conjugate to }a^{-1}\}, \tag{1}
```

and $`|H|=|N|`$, $`H\cap\Lambda^2=1`$.

## Strip decomposition

Call a coordinate *full* if its projection of $`H`$ is $`T`$, and *proper* otherwise; a proper projection may be trivial. The projection of $`H`$ to its full coordinates is a direct product of full twisted diagonal $`T`$-strips with disjoint supports. For completeness, this is proved by induction on the number of full coordinates. Apply Goursat to the projection on the first $`n-1`$ coordinates, already a product of disjoint simple strips, and the last $`T`$. Their common quotient is either trivial or $`T`$; in the latter case a homomorphism from the product of simple strips onto $`T`$ is an isomorphism on exactly one strip and trivial on the others. The new coordinate either forms a singleton strip or joins that strip through an automorphism of $`T`$.

Let these strips be $`S_1,\ldots,S_m`$, and let $`R`$ be the projection of $`H`$ to the proper coordinates. Each composition factor of $`R`$ has order smaller than $`|T|`$: successively project onto each coordinate and filter by the kernels, obtaining factors that are subquotients of proper subgroups of $`T`$. Goursat applied to the full-coordinate projection $`T^m`$ and $`R`$ therefore has trivial common quotient. Thus, as subgroups on disjoint coordinate supports,

```math
H=(S_1\times\cdots\times S_m)\times R. \tag{2}
```

Faithfulness means $`H`$ contains no full simple coordinate factor, so every strip has support of size at least two. The trivial proper projections are retained as coordinates, with their trivial leaf groups.

## The paired-coordinate forest

Construct a finite multigraph with a vertex for each full strip and a degree-one vertex for each proper coordinate. Each $`\tau`$-pair supplies one edge joining the vertices carrying its two coordinates. A strip may carry both ends, so loops and parallel edges are allowed at this stage. For any union $`C`$ of components, let $`k_C`$ count its edges, $`m_C`$ its strip vertices, and $`R_C`$ the projection of $`R`$ onto its proper coordinates. Retaining exactly the complete $`\tau`$-pairs in $`C`$ in the original group quotient, the normal-subloop criterion gives, for every nonempty proper union $`C`$,

```math
|R_C|>|T|^{k_C-m_C}. \tag{3}
```

Indeed the quotient $`K`$-image has order $`|T|^{k_C}`$, while the quotient stabilizer has order $`|T|^{m_C}|R_C|`$; equality in the corresponding ratio would produce a proper nontrivial normal subloop. For the full graph, $`|H|=|T|^k`$ gives

```math
|R|=|T|^{k-m}. \tag{4}
```


Every component is a tree. For a proper component with no proper-coordinate leaves, $`R_C=1`$, while all its strip degrees are at least two, so $`k_C\ge m_C`$; this contradicts (3). Now suppose a component has $`\ell_C>0`$ leaves. Its proper coordinate projections all have order strictly less than $`|T|`$, including the possible trivial ones, and hence $`|R_C|<|T|^{\ell_C}`$. Combining this with (3), or with (4) when it is the entire graph, yields $`k_C-m_C<\ell_C`$. Its cycle rank is $`k_C-m_C-\ell_C+1`$, so it is zero.

Finally, if the entire graph is a single component without leaves, select an involution from the FGS automorphism-invariant $`T`$-class independently in each strip. Every coordinate then lies in that class, so the two entries of each $`\tau`$-pair are conjugate involutions. Their product element is nonidentity in $`H\cap\Lambda^2`$, contradicting (1). Thus this last case cannot occur. Each component consequently has at least two proper-coordinate leaves. For every proper component, (3) becomes the dense-projection condition

```math
|R_C|>|T|^{\ell_C-1}. \tag{5}
```


These conclusions do **not** assert that the forest is connected or that $`R`$ is the product of its leaf projections: $`R`$ may correlate leaves in different components. The reviewed graph-to-path theorem assumes independent vertex groups, so it cannot be applied to (2) until that residual interface is established. No classification or outside-path example is claimed.

## Independent mathematical review

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted exact source `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`, conditional on the pinned canonical-folder/normal-quotient interfaces and the CFSG-dependent FGS invariant involution class. They checked both Goursat steps, strictness for every proper union of components, and the forest boundary cases including trivial proper projections, loops, parallel edges and leafless components. No reviewer freshly audited the primary classification source or ran a computation. The reviews do not establish connectedness or independence of the proper-coordinate subgroup R.
