# Exact proposal components

All probabilities are rational and all sampling uses `rng.getrandbits(k)`.
The forward direction returns `None` on veto. **Do not resample a failed
block in place**: that conditions on survival and invalidates the odds.

* `polygon.py`: a canonical proper color word describes an alternating cycle.
  `seed_forward(n, slots, word, rng)` chooses a disjoint set of rooted labeled
  copies with fugacity one, fills partial permutations, vetoes intersecting
  physical rows and decorations outside the canonical packing. `seed_reverse`
  draws a fair subset of that packing. Write $`Z`$ for the total unrestricted
  number of decorated blocks. Each forward history has mass $`1/Z`$, each
  reverse history on its given block has mass $`2^{-\lvert P\rvert}`$, so `ratio` is
  $`Z/2^{\lvert P\rvert}`$. A dummy word has no marks. `mark_counts` gives the **integer**
  counts split by mark count; these include forward vetoes.
* `marked.py`: `forward(board,b,rng,masked=True)` and `reverse(board,rows,rng,
  masked=True)` place one auxiliary matching. The normalizer is
  $`Z_b=(n!)^2\sum_{\sum a=n}\prod_i(n-a_i)!/a_i!`$. A finite integer
  convolution samples the composition, followed by a uniform assignment of
  these color counts to domain sites. With masking, the auxiliary mark is
  sampled in the input host; each free bin avoids used edges and still-reserved
  marks. With `masked=False`, fill uniformly without masking, veto conflicts.
  For fixed rows, the reverse mark is uniform among matchings of their union.
  `odds_from_history` returns the exact ratio without counting any permanent:
  $`T=(Z_b/\mathrm{per}\,U)\times(\mathrm{per}\,A/n!)\prod_c(\mathrm{per}\,A_c/s_c!)`$ in masked mode; omit the last two
  factors in raw mode. $`U`$ is the row union and $`A_c`$ is the compact
  free-bin board of size $`s_c`$.
* `selector.py`: `Odds` represents a positive scalar times products/ratios
  of feasible matching counts. `direct_gate` computes the exact sigmoid
  $`T/(T+H)`$ or its reverse using the counting backend. `oracle_sigmoid_gate`
  has the **same law** with no permanent evaluations, using only iid exact
  uniform matching draws on a board and its minors. For each anchor step
  with conditional probability $`p`$, $`\mathrm{NB}(k,p)`$ counts trials up through success
  k. The ordinary factors use $`\mathrm{NB}(m,p)/m`$ (mean $`1/p`$); reciprocal factors
  use $`(m-1)/(\mathrm{NB}(m,p)-1)`$ (mean $`p`$). Size-bias transforms the
  two counts to $`\mathrm{NB}(m+1,p)-1`$ and $`\mathrm{NB}(m-1,p)+1`$ respectively. The product $`Y`$
  thus has mean $`T`$ and the reverse product has its size-biased law. For
  $`a=\mathbb E\min(1,Y/H)`$, $`h=\mathbb E\min(1,H/Y^*)`$, one has $`a/h=T/H`$.
  A fair-side Bernoulli race gives the claimed sigmoid. The default replicate
  count 2 plus the total matching dimension bounds $`\mathbb E[Y^2]/T^2\le e`$.
  The expected number of rounds is at most $`16e`$. This is a polynomial-oracle
  reduction, **not** a claim that the default subset-DP matching backend runs
  in polynomial time or that these block primitives alone sample Latin squares.

`python3 -m unittest -v test_marked test_polygon_selector` includes exact
unrestricted normalizer checks, exhaustive supported-history detailed
probabilities in both directions on small/punctured hosts, and the two
negative-binomial size-bias identities.
