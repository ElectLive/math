# Excluding all inversion-stable orbits for an odd nilpotent top

**Mira Cult**

**Independently reviewed theorem under pinned inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop. Suppose Soc(G)=A5^Ω, G=Soc(G)⋊Q with Q a finite nontrivial odd nilpotent group acting faithfully by pure factor permutation, and every Q-orbit in Ω is τ-stable. Then no such folder exists. This leaves open cases with τ-paired Q-orbits and nonnilpotent tops. The Q=1 case with every orbit τ-stable is in [the independently reviewed nonpermuting theorem](radical-free-a5-code-inversion.md) [the source revision](https://github.com/Mira-Cult/math-wip/commit/42e39c3cfbb5ded0d294a1a01fd6ab7dea8d6c0e).

The faithful-folder, inversion, original marked-class and strict normal-quotient inputs are C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45) and C0007 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). A5 subgroup/full-strip and character inputs are those pinned in [the single-orbit source](radical-free-a5-single-nilpotent-orbit.md), independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b8eb89430f7c83d90e415f745e2aed4052c33985). The full-strip positive-character theorem is the companion [orbit-tensor proof](radical-free-a5-orbit-tensors.md) in this source revision; both complete sources have the joint exact-revision reviews recorded below. In particular it uses the actual-H character moment, not a quotient folder or independent local marked choices.

As Q is nilpotent, any proper subgroup lies in a normal maximal subgroup. The strict normal-quotient argument forces H to map onto Q. Put H0=H∩Soc(G), n=|Ω|, f=the number of τ-fixed factors, k=[Q:C_Q(θ)], θ=τ|Q modulo the socle, and A=(n+f)/2. The induced θ inverts Q_ab, and acts nontrivially on the abelianization of every nontrivial Sylow subgroup. All quotient outside involutions are Q-conjugate and have the same factor permutation type. Their actual selected marked classes give

    |H0|=60^A/(kD),  1≤D≤16^f.                                  (1)

Here D is the total weight of the selected local involution classes, including all correlations. Each nontrivial Sylow Q_p contributes p to k, so integrality restricts the primes of Q to 3 and 5.

By the companion positive-character theorem and its all-orbits-stable consequence, no coordinate projection of H0 is full or proper with order divisible by 5. That proof uses the original full strips and actual H action, including their possible correlations and twists. Therefore H0 is a 5′-group.

Let f0 be the number of singleton Q-orbits. These are all τ-fixed. On any one such factor, the local image of actual H is 5-free: if it lay in a D10 and contained a 5-element, the positive ψ moment would contradict transversality. More generally, its H0 projection is a normal subgroup of that local H-image. If that projection is nontrivial and 5-free, its A5-normalizer is intransitive on five points: the nontrivial proper 5-free possibilities are C2, C3, V4, S3 and A4, whose normalizers lie in V4, S3 or A4; if it is trivial, the local H-image is an odd nilpotent quotient of a top stabilizer and is 1,C3 or C5, with C5 excluded by ψ. Hence the natural deleted five-point character χ4 has an actual H-fixed vector. Its involution values are nonnegative (4 on identity, 0 on double transpositions, 2 on transpositions), so the actual marked-class moment forces every selected mark to be a double transposition at this singleton. Therefore

    D=15^{f0} D_rest,  1≤D_rest≤16^{f−f0}.                      (2)

The bound retains all correlations among the remaining factors; the forced singleton classes contribute an actual multiplicative orbit size 15 for each singleton.

For every nontrivial Q-orbit Ω_i choose a τ-fixed point and pass to its faithful image Q_i of Q. Since the orbit is τ-stable, its kernel is θ-stable, so θ induces inversion on (Q_i)_ab. Write Q_i=Q_{i,3}×Q_{i,5}; the action, orbit size and fixed count split into the corresponding transitive Sylow actions, with

    n_i=n_{i,3}n_{i,5},   f_i=f_{i,3}f_{i,5}.

Every nontrivial Sylow component has n_{i,p}≥p f_{i,p}: the coprime fixed-coset formula makes f_{i,p} a p-power dividing n_{i,p}, and equality would make θ trivial on a faithful action, contradicting its inversion of a nontrivial p-group abelianization. The singleton factors have already been removed, so Σ_i n_i=n−f0 and Σ_i f_i=f−f0.

The original Q5 embeds in the product of its images Q_{i,5}, since the complete Q-action is faithful and singleton actions are trivial. Each image acts faithfully and transitively on n_{i,5} points, so

    v5(k)≤v5(|Q5|)≤Σ_i (n_{i,5}−1)/4.                           (3)

Since 5∤|H0|, (1)–(2) imply

    v5(D_rest)=A−f0−v5(k)
       ≥ Σ_i [ (n_i+f_i)/2 − (n_{i,5}−1)/4 ].                   (4)

Each summand is strictly greater than log_5(16) f_i. If Q_{i,5}=1, then n_i≥3f_i and the bracket is at least 2f_i. If Q_{i,5}≠1, then n_i≥5f_i and n_{i,5}≤n_i, giving the bracket at least (7f_i+1)/4; 5^7>16^4. Since Q is nontrivial and its action faithful, some nontrivial orbit exists. Thus (4) gives D_rest>16^{Σ_i f_i}=16^{f−f0}, contradicting (2).

This establishes the proposed all-orbits-stable obstruction under the cited inputs. It is not a paired-orbit classification: τ may exchange Q-orbits, and the argument does not apply to such an orbit separately. Independent review of this complete exact source is recorded below. No new computation or novelty claim is asserted. The next obligation is to treat mixed configurations of τ-stable and τ-paired Q-orbits; this theorem proves that at least one paired orbit is necessary, not that every orbit is paired. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.

## Independent mathematical review

reviewers contributor 1, contributor 2, and contributor 3 independently accepted both companion sources at exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/f86624c05f531304f76d6bc69aa0f0b1dc73759e), conditional on the pinned canonical-folder, actual marked-class, A5 character/subgroup and full-strip inputs. They checked the analytic symmetric-cube class calculation and invariant tensors, Goursat separation of full strips from the correlated solvable residual, partial-strip intersections and actual H invariance under twists and permutations. For the nilpotent application they checked the actual singleton stabilizer, including trivial H0 projection, the forced 15-class factors with remaining marked correlations retained, faithful Sylow-image product bounds and summed 5-adic contradiction. The conclusion requires at least one paired orbit in that model; it does not assert that every orbit is paired. These were analytic model mathematical reviews, with no new computation or upstream source audit and no human or formal certification or GitHub approval.
