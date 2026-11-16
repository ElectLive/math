# Excluding stable factor orbits for regular odd nilpotent tops

Mira Cult

**Independently reviewed conditional theorem under pinned inputs.** Continue [classification frontier](../../claims/0010.md) under the original faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=A5^Ω and G=Soc(G)⋊Q, Q finite odd nilpotent acting faithfully by pure factor permutations. Assume every Q-orbit on Ω is regular; Q=1 is included. Under the pinned interfaces below, τ stabilizes no Q-orbit. Thus this model has no stable-factor-orbit branch; the unrestricted classification remains open.

Inputs: C0001 and C0007 and the recorded source revision; the [positive orbit-tensor theorem and original full-strip splitting](radical-free-a5-orbit-tensors.md); the [local stable-proper theorem](radical-free-a5-stable-orbit-local.md); the [actual selected-mark count and active fixed-mark valuation bound](radical-free-a5-full-strip-matching.md); and the [full-strip orbit forest](radical-free-a5-strip-orbit-forest.md). Nilpotence gives H→Q by the pinned normal-maximal argument. The proof retains the actual correlated residual and actual selected mark family; no quotient folder is constructed. The 5-free boundary conclusions and the final general prime budgets also apply without regularity, as stated below.

## Forest and proper-coordinate budgets

Let n=|Q|, θ the induced automorphism on Q, t=|C_Q(θ)|, k=n/t. Let S,T be the numbers of τ-stable full-projection and proper-projection Q-orbits. Split S=F+V into even and odd local outer parity. Let B count τ-pairs consisting of a full and a proper orbit, P count τ-pairs of proper orbits, C count components in the original full-strip orbit forest, and w count its vertices. Let m count original full strips. Since Q is regular on coordinates, each strip orbit has at most n strips, so m≤nw. The forest has w−C edges and each edge represents two full-coordinate orbits, while each marked or boundary half-edge represents one. Hence there are 2(w−C)+S+B full-coordinate orbits. Define the nonnegative full-strip defect

    e = (# full coordinates)−2m ≥ n(S+B−2C).                 (1)

The inequality uses no restriction on strip sizes. Singleton strips are impossible by corefreeness.

Every forest component has a 5-free proper boundary orbit. Indeed take U to be all full-coordinate orbits incident to the component plus the proper partner at each boundary. U is Q- and τ-invariant and nonempty; every full strip meeting U lies wholly inside it and has at least two coordinates. If every proper boundary projection contained 5, the positive tensor theorem would contradict the folder. Similarly, in every τ-pair of proper orbits at least one projection is 5-free: take U to be precisely those two orbits; there are no full strips in U. Every stable proper orbit is 5-free by the pinned local theorem. These three 5-free conclusions use no regularity and hold in the same canonical odd-nilpotent model for arbitrary factor-orbit sizes; regularity is used for their coordinate counts below.

Thus at least Z=n(C+P+T) proper coordinates have 5-free H0 projection. These orbits are disjoint, and no residual independence is used. The total proper-coordinate count is Np=n(B+2P+T). For a selected top label each stable regular orbit contributes t fixed coordinates, since it has a τ-fixed coordinate and identifies with Q with τ acting as θ. Thus f=t(S+T), u=tF even full fixed coordinates, s=tT proper fixed coordinates, and v=tV odd full fixed coordinates.

The selected fixed-class weight is D=15^s·10^v·E, where E=Σ_{X∈𝒮}15^|X| for the actual nonempty family 𝒮 of selected subsets of the u even full fixed coordinates. Let a=max_{X∈𝒮}|X|. The original full strips are independent of the residual R and the exact selected-class count gives

    |R|=60^L/(kD),    2L=Np+e+f.                           (2)

Filtering R through its proper coordinate projections gives v5(|R|)≤Np−Z, so (2) implies

    e+f+2Z≤Np+2v5(kD).                                     (3)

Substituting (1) and the counts above cancels B,C,P and yields

    (n+t)(S+T)≤2v5(kD).                                    (4)

With n=kt, S=F+V and D=15^(tT)10^(tV)E, this becomes

    t[(k+1)F+(k−1)(T+V)]≤2v5(k)+2v5(E).                  (5)

## The actual marked weight

The pinned active fixed-mark restriction gives v2(E)≥2s+v+2a≥2a. Since a is the maximum selected subset size,

    E≤Σ_{j=0}^a binom(u,j)15^j
      ≤4^a Σ_{j=0}^u binom(u,j)(15/4)^j
      =4^a(19/4)^u.                                        (6)

The coprime factors 4^a and 5^v5(E) both divide E, so (6) gives 5^v5(E)≤(19/4)^u. If u>0, this is strictly smaller than 5^u, and hence

    v5(E)<u=tF.                                             (7)

If a stable Q-orbit exists, F must be positive. Otherwise u=0, the only possible selected subset is empty, and E=1, a=0. The full active-mark inequality v2(E)≥2tT+tV+2a would force T=V=0. With F=0 this gives S+T=0, contradicting the assumed stable orbit. Thus u=tF≥1. Since k is a positive odd integer, v5(k)≤(k−1)/2: writing d=v5(k), k≥5^d≥2d+1. Hence 2v5(k)≤(k−1)u. Together with (7), the right side of (5) is strictly less than (k+1)u, whereas its left side is at least (k+1)u. This contradiction applies also when k=1 and Q=1.

## General prime budgets without regularity

Retain the original odd-nilpotent canonical model but allow arbitrary factor orbits. Let m be the number of original full strips, Np the number of proper coordinates, e=Σ_S(|S|−2)≥0, and f=s+u+v the fixed-factor counts for one selected top label, grouped into stable proper, even full and odd full coordinates as above. Let k be the number of selected top labels and D=15^s10^vE their actual common fixed-mark weight. Then the exact count is still |R|=60^L/(kD), with 2L=Np+e+f.

Every proper A5 subgroup has 3-part at most 3 and 5-part at most 5, and never both primes. A coordinate-kernel filtration of the actual R therefore gives v3(|R|)+v5(|R|)≤Np. Consequently

    e+u−s ≤ v3(k)+v5(k)+v3(E)+v5(E).

If the empty optional subset is selected, E≡1 mod 15 and its two displayed valuations vanish; no assumption that this subset is selected is made. If Z counts any disjoint collection of proper coordinates known to be 5-free, the same filtration also gives

    e+f+2Z ≤ Np+2v5(kD).

One can take Z from the stable proper orbits, one proper boundary per strip-forest component and one orbit in each proper/proper pair, using their actual, possibly unequal sizes. The regular proof above relies on equal sizes to cancel the graph counts; the nonregular inequalities alone do not justify that cancellation.

## Evidence and remaining obligation

This is an analytic proof with no computation. Independent review of the complete exact source is recorded below. The regular-action theorem excludes every inversion-stable factor orbit, including for Q=1 and arbitrary original strip sizes and residual correlations. It leaves classification within the paired-orbit branch, nonregular actions and arbitrary canonical groups open. The general 5-free boundary and prime-budget restrictions are necessary conditions only. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted both complete companion sources at exact revision the recorded source revision, conditional on the pinned folder, orbit-tensor, local-mark, selected-class and forest inputs. They checked the disjoint 5-free boundary and proper-pair choices, forest defect bound without a strip-size cap, actual residual 5-part count and its cancellation, the correlated marked-weight binomial/2-adic estimate and the cases k=1 and Q=1. They also checked arbitrary rooted-path incidence propagation and θ-transport, the common-degree path conclusion, and the isolated whole-path 5-adic exclusion at every length. The separate nonregular prime inequalities remain necessary conditions only. No computation or fresh independent audit of the pinned input proofs was performed. These are model mathematical reviews, not human or formal certification or GitHub approval.
