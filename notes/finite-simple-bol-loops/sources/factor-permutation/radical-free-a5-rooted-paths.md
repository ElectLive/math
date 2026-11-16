# Rooted strip paths over a common transitive Q-set

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Retain the faithful generated simple nonassociative canonical folder (G,H,K,τ), Soc(G)=N=A5^Ω and G=N⋊Q, with Q finite odd nilpotent acting faithfully by pure factor permutations. Use the [original strip-orbit forest](radical-free-a5-strip-orbit-forest.md) and [positive orbit-tensor theorem](radical-free-a5-orbit-tensors.md). No assumption τ(H)=H is made.

## Incidence propagation

Root a strip-orbit forest component at a τ-stable full-coordinate Q-orbit. On the root, the reviewed single-orbit tensor consequence says that each strip meets this orbit once. For any path from the root to another strip-orbit vertex, let U be the root stable orbit plus both full-coordinate Q-orbits corresponding to every τ-edge on the path. It is τ-stable. Every strip in an internal vertex orbit meets U at least twice; if the terminal incoming coordinate orbit met each terminal strip at least twice, every strip meeting U would do so, contradicting the reviewed tensor theorem. Thus the terminal incoming intersection multiplicity is exactly one. This argument does not assume regularity or a strip permutation by τ.

For an oriented edge, its outgoing coordinate Q-orbit maps Q-equivariantly onto the parent strip orbit. The τ-partner is identified with it through the automorphism θ of Q and, by the preceding paragraph, is bijective onto the child strip orbit. Hence strip-orbit degrees are nondecreasing away from the root, and the child stabilizer is contained in an appropriate conjugate/θ-transport of the parent stabilizer. This statement is an incidence map, not an identification of actual residual subgroups.

If all coordinate Q-sets are isomorphic of common degree N, the root strip orbit has N members and every incoming orbit has degree N. Induction therefore forces every strip orbit in the rooted component to have N members and every coordinate-orbit incidence multiplicity to be one. If it has exactly one full/proper boundary half-edge, it is a path and every strip has exactly two coordinates. Indeed, if there are L strip-orbit vertices, the L−1 internal edges and the two half-edges contribute total graph degree 2L. Every vertex has degree at least two because its strips have at least two coordinates and all incidences have multiplicity one. Thus every degree is two. The underlying tree is a path, with its marked and boundary half-edges at its ends; this includes L=1.

## One path and one stable proper orbit

Assume now that Q is nontrivial and Ω consists exactly of such a rooted path with L≥1 strip-orbit vertices, its one proper boundary orbit D, and one additional τ-stable proper orbit B, all isomorphic to the same faithful transitive Q-set of odd degree N. The path contributes 2L full Q-orbits, of which one, A, is τ-stable. The L−1 internal τ-pairs and the boundary pair contribute L exchanged pairs of Q-orbits. Thus Ω has 2L+2 Q-orbits and H0 has LN full strips.

The τ-fixed counts on A and B are equal, say f, by the odd-centralizer conjugacy argument in [the four-transitive-orbit proof](radical-free-a5-four-transitive-orbits.md). A selected outside factor permutation has 2f fixed factors and LN+N−f transposed factor pairs. B's f fixed marks are actual double transpositions by the reviewed local theorem. As in the four-orbit proof, the local outer-parity alternative on A is ruled out by the original support inequality. Let E be the actual selected weighted sum 15^{|S|} on the f fixed A factors. It obeys E≤16^f and v2(E)≥2f+2. Let k=[Q:C_Q(θ)] be the number of selected outside top labels. Then the original H0 order is

  |H0|=60^{(L+1)N}4^f/(kE).

After splitting off its LN original full strips, the actual correlated proper residual on B∪D has order

  |R|=60^N4^f/(kE).                                      (1)

The unique proper boundary D is 5-free by the companion [component boundary argument](radical-free-a5-forest-prime-budget.md), which does not require regularity: use the tensor theorem on all full orbits in the path together with D. Each full strip lies wholly inside this τ-stable union. If D were 5-bearing, every proper projection in the union would contain 5, a contradiction. The stable proper orbit B is also 5-free by its V4/A4 alternatives. Hence the actual R on B∪D is a 5′-group.

On the other hand kE<5^N by the first, 5-adic part of the pinned four-transitive-orbit proof. More explicitly, integrality of (1) and inversion on the top abelianization force every nontrivial Sylow prime of Q to be 3 or 5. The common faithful transitive Q-set has Sylow degrees N3,N5 with N=N3N5, and v3(k)≤(N3−1)/2, v5(k)≤(N5−1)/4. Its fixed counts satisfy f≤N/3 in the pure-3 case, f≤N/5 in the pure-5 case, and f≤N/15 in the mixed case. Together with E≤16^f, the elementary inequalities sqrt(3)·16^(1/3)<5, 5^(1/4)·16^(1/5)<5 and sqrt(3)·5^(1/4)·16^(1/15)<5 give kE<5^N, exactly as in that source. Formula (1) would then require v5(kE)=N to make R a 5′-group, impossible. This proves the exclusion for every L≥1.

The argument uses neither the later 3-shadow saturation estimate nor the one-third-fixed 3-group lemma from the four-orbit proof; those remain historical results at their original source pin. The present exclusion does NOT apply to a path component when additional proper Q-orbits are present: then R has their coordinates too, and the 5-free conclusion cannot be inferred for the whole residual.

## Evidence and remaining obligation

The topology applies to arbitrary factor-orbit sizes, with monotone degrees on rooted paths. The exclusion requires the entire displayed path and exactly its two proper-coordinate orbits; extra proper coordinates cannot be discarded. The next obligation is to control their correlations using the actual residual-kernel and invariant-cut constraints. The unrestricted classification remains open.
