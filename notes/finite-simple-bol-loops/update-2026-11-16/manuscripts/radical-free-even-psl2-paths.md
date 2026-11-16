# Paired PSL₂ over every even field

**Independently reviewed continuation of 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** Let T=PSL₂(q), q=2^f≥4. For every k≥1 there is exactly one isomorphism class of finite simple nonassociative left Bol loops with faithful canonical group G=T^k×T^k and inversion swapping the two blocks coordinatewise. It is the k-edge path with endpoints a Borel B of order q(q−1) and a nonsplit cyclic torus C of order q+1. The construction gives a proper non-Bruck loop. This classification is confined to the stated canonical group and inversion.

The dependencies are the [strip-forest theorem](radical-free-strip-forests.md), independently reviewed at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`, the [path construction and isomorphism criterion](radical-free-path-factorizations.md) at `1818e2c44bee176638f1212fd8b36c6a8a92e5ba` and `c1be0daa47ca5f6befeb96378bc1937544acbde1`, and their canonical-folder and CFSG qualifications. The q=4 case is the [reviewed A₅ classification](radical-free-a5-path-classification.md) at `ad94accf574f89bf1e8487bb046cf30fb685cd0c`. We prove the remaining q≥8 cases below, using the subgroup and primitive-divisor statements cited in [the odd-characteristic PSL₂ source](radical-free-psl2-path-classification.md). No novelty or independent reproof of those external classifications is claimed.

## Two subgroup properties

For q≥8 we will use a prime r dividing q+1 with these properties: every proper subgroup whose order is divisible by r lies in a nonsplit normalizer D=C_(q+1):2, and every proper subgroup containing a full Sylow 2-subgroup lies in a Borel. Sylow 2-subgroups of T are elementary abelian of order q, and T has one involution class. Actual torus and Borel containment, as opposed to just abstract subgroup types, follows from characteristic Sylow subgroups and their normalizers.

For f≥4, Zsigmondy's theorem supplies r with ord_r(2)=2f and r≥2f+1>5. The exception at exponent six does not occur. Dickson's list excludes r from the exceptional groups and all proper subfield groups, so every r-bearing proper subgroup lies in D. A subgroup with 2-part q cannot be an exceptional or proper subfield group, and the remaining upper-triangular type has a normal full Sylow 2-subgroup and lies in its Borel normalizer. These inputs are Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, published Appendix Theorem A.1 and Lemmas A.2–A.3, pp.1354–1355, and Avcı arXiv:2011.06136v2 §1 as pinned in the linked source.

For q=8 take r=3. Here |T|=2³·3²·7. The Borel 2³:7 and split normalizer D₁₄ are 3-free. A₅ cannot occur since 5 does not divide |T|, and S₄ cannot occur since its Sylow 2-subgroup is not elementary abelian. An A₄ would normalize its V₄, whose nontrivial unipotents fix the same unique point of the projective line; its normalizer lies in that point's 3-free Borel, a contradiction. The only proper subfield group is PSL₂(2)=S₃. Such a subgroup normalizes its C₃; this C₃ has nonsplit centralizer C₉, and its normalizer is D₁₈. Thus every proper 3-bearing group lies in D₁₈. The remaining subgroup types with full 2-part lie in a Borel. This establishes the two properties at q=8 without a primitive-divisor assumption.

## A support parity argument forces paths

Write c for the forest component count, ℓ for its proper-coordinate leaves, and R for the simultaneous leaf projection of H. The reviewed forest gives

    |R|=|T|^(ℓ−c),    ℓ≥2c.

The r-part requires at least ℓ−c r-bearing leaves. Let n≤c be the number of other leaves. A Sylow 2-subgroup Q of R is elementary abelian, of dimension f(ℓ−c). Its projection rank d_i at an r-bearing leaf is at most one, and at any other leaf is at most f. All these projections are linear maps on Q.

For a rank-d projection with independent linear coordinates L₁,…,L_d, the polynomial 1+∏_j(1+L_j) over F₂ is its nonzero indicator, of degree at most d. For rank zero it is zero. In every component choose a leaf of minimum projection rank and equate every other indicator to that leaf's indicator. The total degree is at most ∑d_i−∑d_min. If z leaves have rank zero, then

    ∑d_i≤ℓ+(f−1)n−z,    ∑d_min≥c−z,

so the total degree is at most ℓ+(f−1)n−c≤ℓ+(f−2)c. This estimate needs no r-bearing anchor in each component.

If ℓ>2c, that degree is strictly smaller than dim Q=f(ℓ−c). The number of common zeros is even: modulo two it is ∑_(x∈Q)∏_j(1+F_j(x)), and every monomial misses a variable and sums to zero. Since the zero solution exists, there is a nonzero common zero. Its leaf values are simultaneously identity or nonidentity involutions on each component. On active components set every full strip to an involution and on inactive components set it to identity. T has one involution class, so each paired coordinate is conjugate to the inverse of its mate, even after strip twists. The resulting nonidentity element of H lies in Λ², contradicting transversality. Hence ℓ=2c and every component is a path.

At ℓ=2c the same bound is strictly below fc if n<c. Thus n=c: there are c leaves of each kind. If a path has two r-bearing ends, another has two other ends. Their indicator equations have total degree at most 1+f, rather than 2f; including the remaining paths again gives a strict inequality and collision. Hence all paths are mixed. The per-path degree is at most f; if any non-r leaf has projection rank below f, the total is strictly below fc. Therefore every non-r leaf has full 2-part and lies in a Borel.

## The Hall subgroup removes correlations and reflections

After coordinate conjugations put R≤A=B^c×D^c. Since |B||D|=2|T|, the index [A:R] is 2^c. The solvable Hall theorem, applied to R and A, lets an A-conjugation put a full odd Hall subgroup of A inside R:

    F=(C_(q−1))^c×(C_(q+1))^c ≤ R.

These coordinate conjugations are compatible with the paired-folder automorphisms and only change strip twists. The normal torus Z=(C_(q+1))^c is contained in R. In

    A/Z=(P^c⋊(C_(q−1))^c)×C₂^c,    P=(F_q,+),

let W=(R/Z)∩(P^c×C₂^c). Its order is 2^(fc), since R/Z maps onto the full odd complement. It is invariant under the independent scalar rotations (C_(q−1))^c. The full projection rank of Q at every Borel leaf is preserved by coordinate conjugation and gives full P-projection of W there: an element of 2-power order maps trivially to the odd complement.

As an F₂-module for this odd complement, P^c×C₂^c is the sum of pairwise nonisomorphic irreducible P_i and a trivial reflection module. Each P_i is F_q under all nonzero scalars in its own coordinate, which is irreducible; different coordinates have different kernels of action, and f≥3 makes these modules nontrivial. Maschke's theorem and the full P_i projections force every P_i to be contained in W. Their total dimension is fc, so W=P^c and the reflection module is absent. Thus

    R=B^c×C_(q+1)^c.

For c>1 the projection on one component has leaf order |B||C_(q+1)|=|T|, contrary to the strict normal-quotient inequality of the forest theorem. Hence c=1. Pair flips and the tree coordinate gauges give the standard path. The two endpoint orders are coprime and multiply to |T|, proving exact factorization and existence by the reviewed construction. All nonsplit tori are conjugate, and each is regular on the q+1 projective points, so endpoint pairs are simultaneously conjugate and the path isomorphism criterion gives uniqueness.

The new parity, Hall/module and q=8 arguments have the independent exact-source reviews below. The solvable Hall conjugacy and Maschke theorems are standard group/representation inputs invoked here without a fresh primary-source audit. No finite loop census or quotient-loop assertion is used.


## Independent mathematical review

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted this complete even-field theorem and the appended odd small-characteristic/q=17 continuation in [the preceding source](radical-free-psl2-path-classification.md) at exact revision `184bc5f1b24d05d4dac1860060c6189afefda70c`. All checked the minimum-rank/zero-rank degree budget, actual constant-support collision, equality cases, Hall conjugation and scalar-module splitting, strict quotient, q=8 subgroup argument and endpoint uniqueness. [model reviewer] and [model reviewer] had directly inspected the pinned Guralnick–Zieve and Avcı statements in the preceding review work; none made a fresh primary-source audit of Hall or Maschke. The acceptance is conditional on the pinned external and canonical-folder inputs, not a reproof of the classification theorems, a computation, or formal certification. It concerns the stated paired canonical groups only.
