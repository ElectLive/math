# Exclusion of the four-orbit pattern for a common transitive Q-set

Mira Cult

**Independently reviewed exclusion under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=A5^Ω and G=A5^Ω⋊Q for a nontrivial finite odd nilpotent group Q acting by pure factor permutations. Suppose Ω is the disjoint union of four isomorphic faithful transitive Q-sets, each of degree N: τ-stable full/proper projection orbits A,B and τ-exchanged full/proper projection orbits C,D. Suppose the original H0=H∩A5^Ω has exactly N full strips, each on two coordinates, joining A to C. Then no such folder exists. No regularity of the Q-action is assumed; other orbit or strip patterns remain outside the statement.

The faithful-folder, strict normal-quotient and actual marked-class inputs are C0001 and C0007. Original full-strip separation uses [the orbit-tensor source](radical-free-a5-orbit-tensors.md). The actual local stabilizer and double-mark statement is [the local source](radical-free-a5-stable-orbit-local.md); the correlated fixed-mark 2-adic bound is [the matching source](radical-free-a5-full-strip-matching.md). The actual residual projection-saturation theorem and the previous regular special case are [the companion regular-orbit sources](radical-free-a5-residual-saturation.md). Their precise reviewed scopes are assumed; the nonregular extension is proved here.

## Fixed counts and the original residual order

Nilpotence and the normal-maximal strict-quotient argument give H→Q onto. Let θ be the automorphism induced by τ on Q; it inverts Q_ab because the canonical section generates G and is inverted by τ. Put k=[Q:C_Q(θ)].

The τ-fixed counts on A and B agree. To see this without assuming a τ-equivariant identification, identify the two rows by any Q-equivariant bijection. The two resulting involutions σ_A,σ_B on the common Q-set induce the same θ and differ by an element of the centralizer C of Q in its permutation group. For a point stabilizer L, C has order |N_Q(L)/L|, which is odd. The involutions σ_A and σ_B belong to C⋊<σ_A>; their order-two subgroups are Sylow 2-subgroups and are conjugate by C. Hence their fixed counts are equal. Denote the common positive count by f; the orbit degree is odd, so f≥1. The two exchanged rows have no fixed factors.

The local theorem gives actual point-stabilizer image A4 on B, its H0 projection V4 or A4, and double-transposition marks at every fixed B-factor of every selected outside involution. On A local outer parity is constant, because τ normalizes the pure permutation action and G has only inner local maps. If that parity were odd, all f fixed A-marks would be transpositions and the actual fixed-class weight would be 15^f10^f. Its 2-adic valuation is f, while the reviewed active-support bound requires at least 4f. Thus the parity on A is even.

Let E be the actual sum of weights 15^{|S|} over the nonempty selected family of subsets of the f fixed A-factors marked by doubles. No independence is assumed. The total fixed-class weight is 15^f E, with E≤16^f. If a is the largest selected subset size, the active-support bound says v2(E)≥2f+2a. The choice a=0 would give E=1 and violate that bound, so a≥1 and

    E≤16^f,   v2(E)≥2f+2.                                      (1)

There are k original outside top labels, all Q-conjugate. Their factor permutations have 2f fixed coordinates and 2N−f pairs, so the original marked count and H→Q give |H0|=60^{2N}4^f/(kE). After separating the N full strips, the actual correlated proper residual R satisfies

    |R|=60^N4^f/(kE),   v2(|R|)=2N+2f−v2(E)<2N.               (2)

## Sylow bounds and the residual shadow

Each nontrivial Sylow Q_p is preserved by θ, which inverts its nontrivial abelianization. Thus p divides [Q_p:C_{Q_p}(θ)] and divides k. Integrality of (2) forces all primes in Q to be 3 or 5. Write Q=Q3×Q5, allowing a trivial factor. The faithful transitive common Q-set is the product of faithful transitive Sylow sets, with degrees N3,N5 and fixed counts f3,f5, so N=N3N5 and f=f3f5. This follows by writing a point stabilizer as L3×L5; faithfulness makes each Sylow quotient action faithful. For a nontrivial Q_p, the fixed-coset formula gives f_p=[C_{Q_p}(θ):C_{L_p}(θ)]. It is a p-power dividing N_p. Equality would make the induced permutation involution trivial on the whole faithful Sylow set and hence θ trivial on Q_p, impossible. Consequently N_p≥p f_p. Also

    v3(k)≤(N3−1)/2,   v5(k)≤(N5−1)/4.                         (3)

These are the orders of Sylow subgroups in the respective symmetric groups. In the pure 3 case f≤N/3; in the pure 5 case f≤N/5; with both primes f≤N/15. The elementary inequalities

    sqrt(3)·16^{1/3}<5,
    5^{1/4}·16^{1/5}<5,
    sqrt(3)·5^{1/4}·16^{1/15}<5

and (3) imply kE<5^N in all three cases. Thus 5 divides |R|. The B-projections have no 5, so transitivity forces every D-projection to contain 5 and hence to be C5 or D10.

By (1), 3^{v3(E)}≤E/2^{2f+2}≤4^{f−1}. Write λ=log_3(4)<3/2. The image W of R in (A4/V4)^B is defined even if some B-projection is V4. Its kernel lies in V4^B×D10^D and has order prime to 3. Thus

    d=dim_F3 W=v3(|R|)=N−v3(kE),
    v3(kE)≤(N3−1)/2+λ(f−1).                                  (4)

We will show v3(kE)<2N/3. Then d>N/3≥N/ℓ, where ℓ is the least prime divisor of N. In particular d>0, so transitivity and the local V4/A4 alternatives force every B-projection to be A4. The reviewed actual residual saturation theorem then gives a full V4^B projection of O₂(R′), hence v2(|R|)≥2N, contrary to (2). This uses only a projection and dimension bound, not independent supported factors.

If Q is a 5-group, the right side of (4) is less than 3N/10. If both primes occur, N3≤N/5 and f≤N/15 make it less than N/5. If Q is a 3-group and f≤N/9, it is less than N/2+N/6=2N/3. The only remaining case is a 3-group with f=N/3, because N/f is a nontrivial 3-power.

## An involution fixing one third of a transitive 3-set

We prove the needed group-theoretic bound separately. Let a finite 3-group Q act faithfully and transitively on a set of degree N, let a permutation involution σ normalize it, and suppose θ=conj_σ inverts Q/Q′. If σ fixes f=N/3 points, then

    [Q:C_Q(θ)]≤3^{(f+1)/2}.                                   (5)

Choose a σ-fixed point with θ-stable stabilizer L and a maximal subgroup Q0 containing L. It is normal of index 3 and θ-stable: it contains Q′, and inversion on Q/Q′ preserves it. Its three orbits are blocks of size [Q0:L]=N/3=f. On the three blocks σ fixes the base block and exchanges the others, since θ induces inversion on Q/Q0. All f fixed points lie in the base block, which has size f, so σ fixes that block pointwise.

Consider the set I={q∈Q0:θ(q)=q^{-1}}; it need not be a subgroup. Its elements act trivially on the fixed block, because on that block θ(q) has the same action as q and an odd-order permutation equal to its inverse is identity. On the two exchanged blocks the restrictions determine one another by inverse σ-conjugation. Faithfulness therefore makes restriction from I to either exchanged block injective. The image lies in the image of the 3-group Q0 on f points, whose order is at most 3^{(f−1)/2}.

The map x↦x^{-1}θ(x) on Q0 has fibers of size |C_{Q0}(θ)| and image I. For surjectivity, an inverted element a has the square-root preimage x=a^{-1/2} in its odd cyclic subgroup. Thus |I|=[Q0:C_{Q0}(θ)]. Every θ-fixed element of Q lies in Q0, because θ inverts the odd quotient Q/Q0. Therefore k=3|I|, proving (5). The containment L≤Q0 is essential to the three-block conclusion.

Apply (5) to the A-row in the remaining case. Combining it with (1) gives

    3^{v3(kE)}≤3^{(f+1)/2}4^{f−1}<3^{2f}.

The final inequality follows from 4<3^{3/2}, including f=1 directly. Since N=3f, this is v3(kE)<2N/3 as required. The contradiction to (2) finishes the exclusion.

## Evidence and remaining obligation

This is an analytic proof with no computation. Independent review of this complete exact source, including the three-block bound and its application, is recorded below. The theorem extends [the reviewed regular four-orbit exclusion](radical-free-a5-four-regular-orbits.md) to a common faithful transitive Q-set, with no separate equal-fixed-count assumption. It does not cover different Q-sets on the two stable rows or other orbit and full-strip patterns. The next obligation is to combine actual residual kernel and normal-quotient cut bounds for those general patterns. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned folder, local-mark, support-parity and residual-saturation inputs. They checked equal fixed counts via the odd centralizer of the common Q-set, the actual correlated marked and residual orders, faithful Sylow degree bounds, every pure/mixed valuation case, and the remaining three-block bound. They checked the essential choice of a maximal subgroup containing the fixed-point stabilizer, the injection of the inverted set into one block image, and the square-root/fiber argument and application. The result remains limited to the displayed four common faithful transitive Q-sets and full-strip pattern. No new computation or upstream theorem reproof was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval.
