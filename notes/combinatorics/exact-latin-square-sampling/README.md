# Exact uniform sampling of Latin squares

*Mira Cult · Research writeup for mathematical review*

[Paper (PDF)](paper/exact-uniform-latin-squares.pdf) · [Paper source](paper/README.md) · [Reference code](code/README.md) · [Verification scope](VERIFICATION.md)

## Result

A Latin square of order $n$ is an $n\times n$ array on $n$ symbols, with each symbol appearing exactly once in every row and column. Rows, columns and symbols are labeled. For every positive integer $n$, the algorithm returns each labeled Latin square with exactly the same probability, terminates almost surely, and uses **$\widetilde O(n^{25})$ expected total bit work**. The tilde hides powers of $\log(2n)$. The bound charges preprocessing, randomness, exact arithmetic, and rejected trials. It does not imply a practical runtime, worst-case polynomial time, or irrevocable cell-by-cell generation.

The [paper](paper/README.md) gives the technical proof. The [reference program](code/README.md) is exact at the finite orders it runs, but does **not** implement the revised theorem-scale algorithm or establish its runtime.

## Why uniform rows are not enough

Take a bipartite graph with columns on one shore and symbols on the other. A row is a perfect matching. A full square is an ordered decomposition of the edges of the complete graph $K_{n,n}$ into $n$ such matchings. If a remaining board $A$ has $W(A)$ perfect matchings, an ordinary step picks a row with probability $1/W(A)$. The product of these probabilities can vary drastically from one square to another.

The improved proposal has two ingredients:

- **Pay for differences across targets.** Randomly order the row labels. For higher residual degrees, a signed expansion of the log permanent identifies the terms common to greedy deletion and to the union of a random subset of the rows of a fixed target. A marked colored-cycle block pays for the remaining differences. Separate early matching blocks pay for the low-degree terms. A weighted fill compensates for the holes it creates for later rows in a block. The last two grades are handled together: a capped weight on the first matching in a cubic board allows one cubic block and one pair of rows to cover the exceptional cycle-size contribution.
- **Choose a scale comparable to the number of squares.** Count paths of regular boards as they lose one matching at a time. The path comparison has lists of regular boards at the two ends, with a constant fraction of paths surviving across intermediate degrees. At fixed endpoint degree, the uniform law on boards and the law obtained by putting down disjoint matchings are mutually contiguous. This lets one retain endpoints with enough ordered decompositions at only constant cost. The resulting lower bound for the number of squares makes the proposal scale efficient. It does not assume that ordinary greedy deletion produces a uniform sparse board.

## Why the correction is exact

For a target square $S$ and auxiliary history $z$, write $p(S,z)$ for the probability of proposing them together. Write $r_S(z)$ for a normalized reverse law on histories that can be drawn from $S$ alone. The reverse law does not draw a new Latin square. Set $T=r_S(z)/p(S,z)$ on the reverse support. At scale $H$, the gate with probability $T/(H+T)$ gives a square $S$ total mass

```math
\sum_z p(S,z)\frac{T}{H+T}
  = \frac{1}{H}\mathbb E_{r_S}\frac{H}{H+T}.
```

This is not yet uniform: the last expectation depends on $S$. The algorithm uses a sequence of dyadic scales and exact Bernoulli races that combine the terms into the same final mass for every target. The races inspect a target using fresh reverse histories. Their probabilities telescope, and the expensive levels are reached sufficiently infrequently that the correction costs only logarithmic factors. No numerical approximation of a permanent is passed off as an exact acceptance probability.

## Work bound and limitations

The decorated-history gates take $\widetilde O(n^4)$ exact uniform perfect-matching calls and $\widetilde O(n^{24})$ other bit work. We use a finite-rational implementation of the perfect-matching sampler for which $\widetilde O(n^{21})$ expected bit work per call suffices. The scale is within a constant factor of the square count, and the remaining correction contributes only logarithmic factors. Together these give $\widetilde O(n^{25})$ expected total bit work.

The new bound is not an optimality result or a benchmark. The main practical question is how to replace the worst-case matching and gate machinery with something fast enough to use at interesting orders, without changing the output law.

## Sources

- Göbel, Liu, Manurangsi and Pappik, [*Perfect sampling from rapidly mixing Markov chains*](https://arxiv.org/html/2410.00882v2), Theorem 2 and Section 6, for exact bipartite perfect matching generation.
- Divoux and Wang, [*The maximum number of Hamiltonian cycles in tournaments*](https://arxiv.org/html/2610.23755v1#S3), Section 3, for the starting centered permanent identities.
- Greenhill, Hasheminezhad, Iliffe and McKay, [*Asymptotic enumeration of constrained bipartite, directed and oriented graphs by degree sequence*](https://arxiv.org/html/2601.04822v1), for sparse regular-board counts.
- Greenhill, Kim and Wormald, [*Hamiltonian decompositions of random bipartite regular graphs*](https://users.monash.edu.au/~nwormald/papers/hambip.pdf), proof of Corollary 1.1, equation (1), for fixed-degree contiguity.
- DeSalvo, [*Exact sampling algorithms for Latin squares and Sudoku matrices via probabilistic divide-and-conquer*](https://arxiv.org/abs/1502.00235v2), for earlier exact sampling. The result here concerns the polynomial bound on expected total bit cost.

*AI acknowledgment.* Six instances of OpenAI’s GPT-6.2 Astra did all the mathematical work of discovering the result and developing its proof, and wrote the entire paper. The human role was to specify the problem and guide the research. The proof has not been externally refereed.
