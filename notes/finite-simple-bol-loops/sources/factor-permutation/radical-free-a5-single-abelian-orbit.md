# Exclusion of one faithful transitive odd-abelian A5 factor orbit

Mira Cult

**Independently reviewed exclusion under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be the faithful generated canonical folder of a finite simple nonassociative left Bol loop. Suppose Soc(G)=N=A5^Ω and G=N⋊Q with Q a nontrivial finite odd abelian group acting faithfully and transitively on Ω by pure factor permutation. Then no such folder exists. The case Q=1 is [the reviewed nonpermuting result](radical-free-a5-code-inversion.md). This does not cover nonabelian tops, multiple Q-orbits, or arbitrary outer lifts.

The argument uses the faithful-folder and exact normal-quotient inputs in C0001, canonical inversion and actual marked-class invariance in C0007, and the A5 subgroup and full-strip facts cited in [the reviewed A5 path source](radical-free-a5-path-classification.md).

An abelian transitive action has normal point stabilizers; faithfulness makes each point stabilizer trivial. Thus Q is regular, and n=|Ω|=|Q| is odd. Since N is perfect and Q is abelian, G′=N. K generates G and τ inverts K, so τ induces inversion on G/N=Q. Simplicity forces HN=G: otherwise HN is a nontrivial proper normal subgroup because Q is abelian, and G=HK makes K map onto G/HN, giving equality in the cited strict normal-quotient test. Put H0=H∩N.

Identify Ω with Q. Any factor permutation normalizing its left regular action and inducing inversion on Q has form u↦c u^{-1}. Squaring is bijective in odd Q, so this has exactly one fixed coordinate. Conjugating the actual outside involution τ by elements of Q shifts its outside top label by squares and reaches all labels. We choose these actual conjugates as representatives; we do not assert that a chosen lift τq is itself an involution.

For an outside involution above any top label, each of its (n−1)/2 swapped factor pairs contributes one N-orbit of size 60. At the fixed factor, an even local involution coset gives classes of sizes 1 and 15, and an odd local involution coset gives the transposition class of size 10. Local parity is preserved by Q's pure factor permutations. Λ=τK is G-conjugacy invariant and contains τ, so the same nonempty selection of local classes appears over each label. Thus

    |K|=n·60^{(n−1)/2}D,   D∈{1,15,16,10},
    |H0|=60^{(n+1)/2}/(nD).                                    (1)

Here D is the sum of the selected fixed-coordinate class sizes; no full-mark assumption is used. Integrality forces all primes dividing n to be 3 or 5. For n≥5 the 3- and 5-valuations of the quotient in (1) are both positive, since (n+1)/2>v₃(n)+1 and >(v₅(n)+1). The same is true at n=3 except D=15. Because H surjects onto Q, its conjugation permutes the coordinate projections of H0 transitively. A proper A5 subgroup has order divisible by at most one of 3 and 5, so all projections are full. In the exceptional case n=3,D=15, |H0|=80. By transitivity and 5 dividing |H0|, every proper projection contains 5 and hence lies in D10, but a subgroup of D10³ has 2-part at most 2³ while 80 has 2-part 2⁴; full projection is impossible too since 60 does not divide 80. Thus this exception is excluded.

A subdirect subgroup of A5^n is a product of full twisted diagonal strips. H preserves its strip partition and acts transitively on the factors. If strips are singletons then H0=N, contradicting corefreeness. Otherwise all blocks have the same odd size b≥3. Let m=n/b≤n/3 be their number, and set k=(n+1)/2−m≥1. Comparing |H0|=60^m with (1) gives 60^k=nD. For D=1 or15 the right side is odd; for D=10 its 2-valuation is 1; neither is possible. For D=16, the 2-valuation gives k=2, and then n=225. But m=111>225/3, contradiction. Thus no such folder exists.

This counts actual marked classes and the actual stabilizer intersection. It does not infer a quotient loop or independent residual projections. No computation is used. Independent review of this complete exact source is recorded below. The next obligation concerns nonabelian odd quotients and multiple factor orbits. This excludes the displayed entire canonical group, not occurrence of its factors in larger envelopes, and does not assert that every radical-free A5 envelope has an abelian top. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned canonical-folder, actual marked-class, strict normal-quotient and A5 subgroup/full-strip inputs. They checked faithful transitivity and quotient inversion, actual conjugate outside involutions and selected local classes at every top label, HN surjectivity, the order-80 exception, and the uniform strip-size and valuation contradiction. The exclusion applies only to the entire pure-permutation odd-abelian group in the statement. No new computation or upstream source audit was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval.
