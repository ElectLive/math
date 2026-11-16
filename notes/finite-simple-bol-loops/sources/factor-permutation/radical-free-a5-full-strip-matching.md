# Full-strip matching in the remaining stable-orbit branch

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q for a finite odd nilpotent group Q acting faithfully by pure factor permutations. Assume τ preserves at least one Q-orbit. We give necessary full/proper orbit, matching and marked-weight conditions for the remaining stable full-projection branch. These do not prove that it is empty or construct a surviving folder.

The faithful-folder, strict normal-quotient and marked-class interfaces are C0001 and C0007. In particular H maps onto Q by the nilpotent normal-maximal argument, H0=H∩N, and Λ=τK is the actual selected outside set with H∩Λ²=1. The [orbit tensor theorem](radical-free-a5-orbit-tensors.md) supplies the original full-strip/Goursat splitting and positive tensor obstruction. The [local direct-sum theorem](radical-free-a5-stable-orbit-local.md) supplies the actual stabilizer and pointwise double marks on stable proper orbits. The [mixed proper-orbit parity theorem](radical-free-a5-stable-proper-parity.md) forces at least one stable full-projection orbit. All these complete sources were independently reviewed at the stated revisions.

## A full/proper orbit pair is necessary

Let F={i∈Ω:pr_i(H0)=A5}. It is Q-invariant, because H normalizes H0 and maps onto Q. The factor permutation of τ normalizes Q, so τF is Q-invariant too. Set U=F∩τF. This is a τ-stable union of Q-orbits. The mixed proper-orbit parity theorem ensures that U contains a stable full-projection orbit and is therefore nonempty.

If every original full diagonal H0 strip met U in zero or at least two coordinates, the positive tensor theorem would give a contradiction. Hence some full strip S meets U exactly once. A full singleton strip is impossible: H conjugates its individual A5 factor through its whole Q-orbit, placing a nontrivial G-normal orbit product inside H. Thus |S|≥2. Another coordinate j∈S−U belongs to F but τj does not. The Q-orbit of j consequently has full H0 projections, while the distinct Q-orbit of τj has proper projections. These two orbits are exchanged by τ. This is a necessary coupling, not an exact-factorization or quotient-folder assertion.

## An exact parity certificate for each selected class

The original full-coordinate part of H0 splits as a product of m independent twisted diagonal A5 strips and the correlated proper-coordinate residual R. Choose a Sylow-2 subgroup P=V4^m×P_R. It is an F2-vector space, because every Sylow-2 subgroup of A5 is V4. The coordinate maps on a full strip are isomorphisms on its V4 factor; the maps on proper coordinates are those of the actual subgroup P_R, without any independence assumption.

Choose any actual selected N-conjugacy class C⊆Λ, and let σ be the involution it induces on the factors. The matching statements below use σ, which need not equal the original factor permutation of τ. At each σ-fixed coordinate the local class is identity, double transpositions, or transpositions in S5. Call a coordinate active if the square of its local class contains the A5 involution class. Both nonidentity types are active: a double transposition is the product of two other nonidentity elements of a V4, and is also the product of two disjoint transpositions. The identity type is inactive. Both active local squares also contain identity.

Let I be any set of σ-fixed coordinates containing all inactive coordinates; one may also put active coordinates in I. The square C² contains every N-involution with identity on I, arbitrary involution or identity on the other fixed coordinates, and matched identity/nonidentity support on each σ-swapped pair. On a swapped pair the local entries are conjugate inverses after the fixed twist; all nonidentity A5 involutions are conjugate, so any two such entries are allowed. All these realizations occur simultaneously within the square of this one original N-class by independent N-conjugation.

Since H0∩C²=1, the identity is the only element of P with that support pattern. Write e_i for the F2-valued indicator that coordinate i is zero. The matched-support indicator on a pair (i,j) is 1+e_i+e_j. Therefore the matching count, modulo two, is the sum over P of

    (product over i∈I of e_i) · product over σ-pairs (i,j) of (1+e_i+e_j).       (1)

An expansion term chooses at most one zero endpoint per σ-pair, together with all coordinates in I. Its count is the size of the kernel of the selected zero-coordinate projection of P. It is odd exactly when that projection is injective. The complete matching count is exactly one. Hence an odd number of expansion terms are injective, and in particular at least one is.

An injective term must hit every full strip, or its untouched V4 factor remains in the kernel. It must also project P_R injectively onto the chosen proper coordinates. Conversely these two conditions make the projection injective, by the original direct-product splitting. Thus (1) is an exact parity certificate on endpoint choices and the actual residual subgroup. It does not replace the residual by independently projected leaves.

## Matching and rank consequences

Mark every full strip hit by a fixed coordinate in I. Form a bipartite incidence graph between the remaining strips and the σ-pairs, joining a strip to a pair when it contains one of that pair's endpoints. Every injective expansion term supplies a matching covering all remaining strips: assign to each such strip one selected zero endpoint; a pair cannot supply endpoints to two strips. Hall failure therefore forces a genuine H0∩C² collision.

For a rank bound, let d_i≤2 be the dimension of the image of P_R at a proper coordinate i. Define B to be the sum of d_i over proper fixed coordinates in I, plus d_j for each full/proper pair whose proper endpoint is j, plus max(d_i,d_j) for each proper/proper pair. Give a strip-to-pair edge cost zero for a full/full pair and cost d_j for a full/proper pair. If c_min is the least cost of a matching covering all unmarked strips, then necessarily

    dim_F2 P_R ≤ B−c_min.                                          (2)

Indeed an injective term yields such a matching. Every pair used at a full endpoint forfeits its proper-endpoint projection capacity. The total rank of the selected proper-coordinate projection is at most B minus that matching cost; its injectivity gives (2). Correlations in R can only reduce this rank, so the inequality assumes no independent coordinates.

Let O be a τ-stable full-projection Q-orbit. The reviewed tensor theorem says each full strip meeting O meets it exactly once. The same O is preserved by σ: a selected outside element differs from τ by an element of G, whose factor permutation lies in Q. Thus the n_O coordinates of O occupy n_O different strips. Let f_O be the number of σ-fixed coordinates in O. For the selected class and set I, let t be the number of those strips already hit by any fixed coordinate in I, and b the number of distinct σ-pairs not wholly in O that are incident to those strips. There are only (n_O−f_O)/2 internal pairs. A matching covering the n_O−t unmarked strips therefore forces

    b+t ≥ (n_O+f_O)/2.                                            (3)

This quantifies the required connections to other orbits. It is not by itself a contradiction.

## The actual fixed-mark 2-adic restriction

For a selected class, let f be the number of σ-fixed coordinates, c=(|Ω|−f)/2, and a_C its number of active fixed coordinates. Let D be the common total selected fixed-class weight above each outside top label, so |H0|=60^{c+f}/(kD), where k=[Q:C_Q(θ)] is odd and θ is the induced automorphism on Q. The original marked-class count follows as in the pinned single-orbit and parity sources; Q-conjugacy of quotient outside involutions gives the same type and total weight above every label. Thus

    dim P = 2c+2f−v2(D).

Use (1) with I precisely the inactive fixed coordinates. Every term imposes at most 2(c+f−a_C) binary conditions, since each coordinate image has dimension at most two. If dim P were greater than this number, every term would have even size, contrary to (1). Consequently

    v2(D) ≥ 2a_C                                                 (4)

for every actual selected class, including those with outer fixed local automorphisms.

Partition the σ-fixed coordinates as follows: s are in stable proper-projection Q-orbits, u are even-parity coordinates in stable full-projection orbits, and v are odd-parity coordinates in stable full-projection orbits. The direct-sum theorem forces the first s to be doubles. The last v are transpositions and are active for (4). Only the u even full coordinates have an identity/double choice. Let 𝒮 be the nonempty actual selected family of subsets of these u coordinates, retaining all correlations. Above any fixed top label,

    D=15^s·10^v·E,   E=sum over S∈𝒮 of 15^{|S|},   1≤E≤16^u.

Write a=max_{S∈𝒮}|S|. Applying (4) to a class attaining a gives

    v2(E)≥2s+v+2a,   and hence   2s+v+2a≤4u.                    (5)

There must be a σ-fixed factor because a stable Q-orbit has odd size. Thus u=0 would make a=0, E=1 and (5) force s=v=0, a contradiction. Every survivor therefore has an even-parity fixed factor in a stable full-projection orbit. If s+v>0, then a≥1; otherwise E=1 again contradicts (5). As a small exact consequence, if u=1 and s≥1, the only numerical possibility is s=1, v=0, a=1, E=16, with both optional classes selected. This is only a necessary numerical pattern, not a folder construction.

## Evidence and remaining obligation

The arguments are analytic; no computation is used.  The matching, rank and marked-weight conditions retain actual stabilizer and marked-class correlations. They identify a full/proper paired orbit, an even-parity stable full fixed factor, and strict incidence requirements in every possible remaining mixed example. They do not establish whether those requirements can be realized. The next obligation is to combine them with the original normal-quotient and transversality conditions to eliminate the remaining branch or construct a genuine countermodel. The unrestricted classification remains open.
