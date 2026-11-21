# The least odd simple Bol loop, and what its order rules out

**Mira Cult**

The least odd order of a finite simple nonassociative left Bol loop is **1053**, or 3⁴·13. [Gábor Nagy supplied the example](https://arxiv.org/pdf/math/0703919). The result here is the proof that no smaller odd order works, **not** another construction or a uniqueness theorem at 1053.

Three arguments give the lower bound:

1. [Odd cube-free order forces classical solvability](manuscripts/odd-cubefree-normal-tower.md). There is a series of subloops normal in the *original loop*, with abelian factors of prime or prime-square order. In odd square-free order the factors have prime order. This does not force native Sylow subloops: [order 63 is a counterexample](../odd-bol-hall/README.md).
2. [Two distinct odd primes](manuscripts/two-prime-exponent-threshold.md). For a simple nonassociative loop of order $`p^a q`$, one must have $`q>p`$ and $`a\ge p+1`$. At $`a=p+1`$, existence is equivalent to $`\mathrm{ord}_q(p)=p`$. The theorem does not classify larger exponents or prove uniqueness.
3. [Exclusion of the remaining smaller orders](manuscripts/least-odd-simple-bol-order.md). A low-rank representation argument excludes the square-free-cofactor family needed for 945; a separate two-projection argument excludes 675. The known nonassociative simple quotient of Nagy's 1053-element construction cannot be smaller, by the lower bound just proved.

[The exact two-prime minimum and its census](../odd-prime-pair/README.md) strengthen item 2: the minimum for each admissible pair is $`1+\operatorname{lcm}(p,\operatorname{ord}_q(p))`$, and its immediate successor is excluded.

## All prime-cube orders

[A separate classification](manuscripts/all-bol-loops-of-prime-cube-order.md) gives all finite left Bol loops of order $`p^3`$ for $`p\ge5`$, up to **both isomorphism and isotopy**. Its four cases are groups, nonregular class-two left translation groups, class-three groups and class-four groups. A cubic polynomial with no root in the prime field controls the last case. There are 28 ordinary isomorphism types at order 125 and 41 at order 343. The smaller primes use the cited published classifications. None of these proper odd prime-power loops is simple.

The [alternating-algebra theorem](manuscripts/abelian-bruck-fibers-as-alternating-algebras.md) is useful beyond order $`p^3`$: it describes the entire native multiplication of every finite odd Bol loop whose associated Bruck loop is abelian, together with its homomorphisms, normal subloops and nuclei. It does not assert that every odd Bol loop has abelian associate.

[Independent checks, finite controls and replay](verification.md) · [Finite simple Bol classification](../README.md)
