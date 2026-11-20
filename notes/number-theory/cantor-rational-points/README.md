# Counting rational points in the middle-third Cantor set

**Mira Cult**

How many fractions in lowest terms, with denominator at most $`T`$, belong to the middle-third Cantor set? At ternary depth $`n`$ there are $`2^n`$ intervals of length $`3^{-n}`$. This suggests the exponent $`\kappa=\log 2/\log 3`$, but it does not give the upper bound: two reduced fractions with denominators up to $`T`$ can be as close as $`T^{-2}`$, and packing at that scale gives only $`O(T^{2\kappa})`$.

**Result.** Let $`C\subset[0,1]`$ consist of the numbers admitting a ternary expansion with digits 0 and 2, and put

```math
N_C(T)=\#\{a/q\in C:0\le a\le q,\ 1\le q\le T,\ \gcd(a,q)=1\}.
```

The [paper (PDF)](paper/cantor-rational-points.pdf) gives a proof of the following bound: for every $`\varepsilon>0`$ there is a constant $`C_\varepsilon`$ such that, for every $`T\ge 2`$,

```math
N_C(T)\le C_\varepsilon T^{\kappa+\varepsilon}.
```

This is the cumulative version of [Broderick, Fishman and Reich, Conjecture 3.3](https://arxiv.org/abs/1106.0526); summing over successive powers of three recovers it from their shell formulation. Each point counts once, including 0 and 1. The height is **not** the denominator displayed by a repeating word: for example, $`0.\overline{02}_3=2/(3^2-1)=1/4`$ enters this count at height 4, not 8. There is no restriction on the prime factors of the reduced denominator.

[Rahm, Solomon, Trauthwein and Weiss, Proposition 3.3](https://arxiv.org/abs/1909.01198) give the lower bound $`N_C(T)\gg T^\kappa\log T`$. Taken together the bounds say $`\lim_{T\to\infty}\log N_C(T)/\log T=\kappa`$. The exponent is sharp; the factor beyond the power is not determined. The proof draft has been internally cross-checked, not externally refereed or formally verified. See the [source and build instructions](paper/README.md) and the [verification record](VERIFICATION.md).

## Where the upper bound comes from

First suppose $`3\nmid q`$. Tripling a point modulo one rotates its purely periodic ternary address. For $`q>1`$ the period is the multiplicative order of 3 modulo $`q`$. By a consequence of [Bourgain's subgroup estimate](https://doi.org/10.1007/BF02807410) explained by [Rahm et al., §6.2](https://arxiv.org/abs/1909.01198), the period of a represented denominator $`q`$ is $`q^{o(1)}`$. That fact alone does not count the points: one must bound both the number of eligible denominators and the number of numerators each carries.

1. **Follow the actual point through divisors of its period.** At time $`h`$, observe the signed displacement $`\{3^h x\}-x`$. Dividing the time by a prime refines the observation. Given the preceding signed displacement, the possible next values for a fixed new denominator factor $`u`$ lie on a translate of the grid of spacing $`1/u`$. Small changes are handled together using the rotation symmetry *before* conditioning. The large changes are counted on their own grids. The product of the successive denominator factors and the final grid size is $`q`$.
2. **Turn many possible numerators into many differences.** Ternary prefixes give Boolean vectors. The integer sumset inequality on the cube implies $`|A-A|\ge |A|^{1/\kappa}`$ for a set of such vectors. Applying it to fractions needs a further argument: different vector differences can represent the same modular difference. Keeping the preceding *real, signed* displacement bounds this multiplicity. Taking a bounded number of sums of rotated differences gives a set whose size controls the number of possible next observations.
3. **Count the moduli supporting those differences.** Families on different grids have the same time step. A common rotation of their digit witnesses bounds the size of their mixed sumsets without assuming that their earlier displacements agree. Grouping tuples of grids by their least common multiple then limits the number of possible large projections simultaneously. Prime-power factors on which a difference set has large conditional entropy are controlled by this projection bound. For the complementary factors the cost of specifying their primes is paid for by the entropy deficit. Thus a grid with many choices of numerator leaves little freedom to choose its modulus.

The numerical balance in the last step is worth isolating. If $`u`$ is of size $`U`$ and the associated difference sumset has size $`U^\beta`$, the two costs, expressed as exponents of $`U`$, add to at most

```math
\kappa\beta+\tfrac12(1-\beta)\le\kappa,\qquad 0\le\beta\le1,
```

apart from arbitrarily small fixed losses. This uses $`\kappa>1/2`$. Applying the balance *at each new denominator factor*, including the final grid, is what makes the costs add to $`(\kappa+\varepsilon)\log T`$ rather than paying for the whole original denominator at every step. These paragraphs are a guide; the [manuscript](paper/cantor-rational-points.pdf) supplies the conditional estimates and the order in which their parameters are chosen.

## Why a logarithm appears, and how one might match it

Let $`P(X)`$ count the same points with $`3\nmid q`$, including 0 and 1. There is an exact way to put the nonperiodic prefixes back:

```math
N_C(T)=P(T)+\sum_{j=1}^{\lfloor\log_3 T\rfloor}2^{j-1}P(T/3^j).
```

To see the coefficient, take a purely periodic tail $`y=a/d=0.\overline B_3`$ in lowest terms. Use the constant tails for 0 and 1. If the last trit of the period is $`b`$, then $`a/d\equiv-b\pmod 3`$ because the displayed periodic denominator is $`3^{|B|}-1`$. Attach a length-$`j`$ prefix of integer value $`A`$. The result is $`(dA+a)/(3^jd)`$. No prime of $`d`$ cancels; the denominator retains *all* $`j`$ factors of 3 exactly when the prefix's last trit differs from $`b`$. Precisely $`2^{j-1}`$ prefixes qualify. Conversely stripping $`j`$ trits from a point of denominator $`3^jd`$ recovers such a tail. Distinct allowed addresses give distinct points; an endpoint may have another ternary expansion, but not another using only 0 and 2.

There are $`2^k`$ distinct tails obtained by repeating length-$`k`$ words, all with denominator at most $`3^k-1`$. Thus $`P(3^k)\ge 2^k`$ for $`k\ge1`$. At $`T=3^m`$, each positive prefix length in the identity contributes at least $`2^{m-1}`$ points. This explains the known logarithmic lower bound and why simply setting $`\varepsilon=0`$ in the full count would be false.

**Open problem: is $`N_C(T)\ll T^\kappa\log(2T)`$?** The stronger bound $`P(X)\ll X^\kappa`$ would suffice. In fact it suffices, and is necessary, that $`F_k=P(3^k)/2^k`$ have bounded averages: at triadic heights the identity reads

```math
2^{-m}N_C(3^m)=F_m+\tfrac12\sum_{k=0}^{m-1}F_k.
```

Positivity and monotonicity of the unnormalized count extend the equivalence to arbitrary heights. This distinguishes two research targets: control every purely periodic scale, or bound their average and allow exceptional scales. The proof presently does neither. It allows subpower costs for period and divisor choices, a positive loss in the mixed-grid estimate, and entropy and scale errors accumulated through the descent. Improving any one of these does not remove the others. In particular, choosing $`\varepsilon`$ as a function of $`T`$ in the displayed theorem is not justified by its constant.

## A consequence for intrinsic approximation

Let $`W_C(\tau)`$ be the points of $`C`$ within distance $`q^{-\tau}`$ (strict inequality) of infinitely many **distinct** reduced $`a/q\in C`$. For $`\tau\ge1`$ the count gives the upper half of

```math
\dim_H W_C(\tau)=\kappa/\tau.
```

Indeed, shell $`2^j\le q<2^{j+1}`$ contributes at most a constant times $`2^{j(\kappa+\varepsilon-\tau s)}`$ to the $`s`$-dimensional covering cost; choose $`0<\varepsilon<\tau s-\kappa`$. For the reverse inequality one already has truncations: at sparse positions $`n`$, force a trit 2 followed by $`\lceil(\tau-1)n\rceil+1`$ zeros. The truncations then have exact denominator $`3^n`$ and error less than $`3^{-\tau n}`$. With successive positions sufficiently far apart, the lower limiting proportion of free digits is $`1/\tau`$, giving dimension at least $`\kappa/\tau`$ by the uniform measure on the free digits. This concerns approximants **in** the Cantor set, not arbitrary nearby fractions. It does not imply a zero–full law for logarithmically modified errors at ordinary reduced height.

A useful distinction appears at the logarithmic scale. Repeat the first $`n`$ trits of $`x`$ to form a purely periodic center $`r_n(x)`$. For almost every $`x`$ in the fair-digit Cantor measure, and for every $`c>0`$,

```math
|x-r_n(x)| \lt c\,3^{-n}n^{-1/\kappa}
```

infinitely often. To see this, test times $`n_j=\lfloor A j\log(j+1)\rfloor`$ with $`A>3/\log 2`$. At time $`n_j`$ ask that the next $`\lceil\log_2 n_j\rceil+M`$ trits copy the initial trits, where $`3^{-M}<c`$. Eventually these test blocks are disjoint. Conditional on all digits through the test time, the success probability is comparable to $`1/n_j`$. The sum diverges, so iterated conditioning gives infinitely many successes almost surely; take countably many $`c\downarrow0`$. With $`n^{-a}`$ instead and $`a>1/\kappa`$, the event probabilities are $`O_c(n^{-a\kappa})`$ since distinct Cantor addresses differing first at trit $`k`$ are at least $`3^{-k}`$ apart. This time their sum converges. **The convergence assertion concerns word length only:** the reduced denominator of the repeating center can be much smaller than $`3^n`$. A sharp ordinary-height logarithmic law for all centers is a different open problem.

For the broader missing-digit conjecture and results for other alphabets, see [Chow, Varjú and Yu](https://doi.org/10.1016/j.aim.2026.110807). The proof here is for the classical ternary set only. For the distinction between symbolic height and reduced height in metric approximation see [Fishman and Simmons](https://doi.org/10.1112/plms/pdu002) and [Tan, Wang and Wu](https://arxiv.org/abs/2103.00544).

**Acknowledgment.** Mira Cult directed the research. OpenAI's GPT-6.2 Astra carried out the proof discovery and development reported here and wrote the manuscript.
