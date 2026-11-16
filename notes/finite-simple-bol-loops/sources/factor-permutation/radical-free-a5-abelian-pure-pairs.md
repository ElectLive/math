# Abelian tops with only proper paired A5 orbits

Mira Cult

**Independently reviewed exact structural parameterization under pinned inputs.** This continues [classification frontier](../../claims/0010.md). We classify the stated canonical slice by permutation modules, bijective affine cocycles, explicit normal-cut ranks and a simultaneous normalizer action. The slice has G=A5^(2Ω)⋊Q, where Q is finite odd abelian and acts faithfully by pure factor permutations, and every coordinate projection of H0=H∩A5^(2Ω) is proper. There are no full strips. The result is not a closed list of module or cocycle orbits, and does not classify full-strip or nonabelian-top models.

The exact inputs are the faithful-folder, normal-subloop and isomorphism interface C0001, canonical inversion C0007, the [complete orbit pairing](radical-free-a5-nilpotent-orbit-pairing.md), the [opposite endpoint types](radical-free-a5-paired-path-residual.md), and [abelian graph elimination and framed affine lifts](radical-free-a5-residual-dependency-graphs.md#abelian-tops-force-a-zero-residual-graph). Properness uses the simple nonassociative Moufang primitivity input pinned in [the transitive-p-group source](radical-free-a5-transitive-pgroups.md), exact revision the recorded source revision. These dependencies remain explicit; the new collision, cut and orbit arguments are below.

## Parameters and construction

Take a nonempty finite faithful Q-set Ω, of size n, without a transitivity or regularity assumption. Put S=A5^Ω⋊Q and

    G={(x,y)∈S² : top(y)=top(x)^−1},
    τ(x,y)=(y,x),              K={(s,s^−1):s∈S}.

This is a group because Q is abelian. Choose standard subgroups C5 and A4 of A5, with A4 a point stabilizer in the natural five-point action, and orient the C5 generator. Choose Q-invariant subspaces W5≤F5[Ω] and C3≤F3[Ω]. Let

    M5=F5[Ω]/W5,    M3=F3[Ω]/C3,    V=M5⊕M3,
    H0=W5 × π^−1(C3) ≤ C5^Ω × A4^Ω,

where π is the coordinatewise quotient A4→A4/V4=C3. Fix ρ(q)δ_i=δ_(qi). The Q-action on V is

    q·(v5,v3)=(ρ(q)v5,ρ(q^−1)v3).

The inverse on the second module is part of the convention and must not be omitted. Require |V|=|Q|. Let η:Q→V be a 1-cocycle for this action, so η(qr)=η(q)+q·η(r), and require η to be bijective. In the framed subgroup with first coordinates C5^Ω, second coordinates A4^Ω and top (q,q^−1), let H be the inverse image of the cocycle graph modulo H0.

Require also the actual-local conditions. When the i-th coordinate projection of W5 is zero, the map η5 restricted to the point stabilizer Q_i, followed by the well-defined i-th coordinate, must be onto F5. When the i-th coordinate projection of C3 is zero, the corresponding map η3:Q_i→F3 must be onto. These are homomorphisms because Q_i fixes i. They ensure that the actual H-coordinate stabilizer images are C5 and A4, even where H0 supplies only 1 or V4. At a nonzero coordinate projection the corresponding prime field is already supplied by H0. In particular these conditions do not silently exclude or misidentify the zero projections.

Finally impose the normal-cut inequalities below. These data construct all and only simple loops in this canonical slice, up to the stated normalizer equivalence, conditional on the pinned interfaces. The cardinality condition implies Q is a {3,5}-group, but Q=1 and zero-dimensional modules are allowed.

## Exact collision criterion

For these framed data with |V|=|Q|,

    H∩K²={1}  iff  the affine Q-action x↦η(q)+q·x is regular
                iff  η:Q→V is bijective.

Indeed K² consists exactly of pairs (u,v) with v conjugate in S to u^−1: a product (s,s^−1)(t,t^−1) has u=st and v=s^−1u^−1s, and this formula reverses for every conjugator s. Fix h∈H with first top q. Its first wreath cycle products have orders 1 or 5, while its second cycle products have orders 1, 2 or 3. Conjugation in S preserves the cycle-product conjugacy classes, possibly permuting cycles by a Q-element. Because Q is abelian the top remains q, and the cycles of q and q^−1 agree. The only common possible product class is identity. Conversely, if all cycle products on both sides are identity, the two elements are base-conjugate to their respective pure tops q and q^−1, so form a pair in K².

For an Fp-permutation module, the kernel of the sums over all q-cycles is (1−ρ(q))Fp[Ω]. Thus H0 adjustments make all first cycle products identity precisely when η5(q)∈(1−ρ(q))M5. They make all second C3 quotient cycle products identity precisely when η3(q)∈(1−ρ(q^−1))M3. Once those quotient products vanish, the independent V4^Ω subgroup in H0 kills each remaining A4 cycle product by an adjustment at one position in that cycle. The two sides can be adjusted independently. Hence for q≠1 a collision exists exactly when the affine element q has a fixed point in V. At q=1, inverse-conjugacy between C5 and A4 coordinates forces both sides to be identity.

Avoidance is therefore equivalent to a free affine action. Since |V|=|Q|, a free action is regular and its orbit map at zero, η, is bijective. Conversely a bijective η makes that orbit regular, hence the whole action free. This uses the cardinality condition; injectivity of an orbit map alone would not imply freeness on an arbitrary larger set. No general affine criterion is asserted for models with full strips.

## All actual normal-subgroup cuts

Retain any Q-invariant sets I5,I3 of individual first and second socle coordinates. Write n5=|I5|, n3=|I3|, u=|I5∪I3| and b=|I5∩I3|, so n5+n3=u+b. Let D≤Q fix every retained coordinate pointwise, and let L be the product of the killed simple factors extended by the pure subgroup {(d,d^−1):d∈D}. Every normal subgroup of G has this form. To see this, its intersection with N is a Q-invariant product of simple factors. In the quotient by that intersection, its image intersects the retained socle trivially and therefore centralizes it. Centerlessness forces all retained base labels to be identity, and its top must fix every retained coordinate. Conversely these conditions give a normal subgroup, since Q is abelian. Thus the test includes one-sided cuts and requires no τ-stability of L.

Let U5=W5 and U3=C3. Define A_p in the retained Fp-coordinate space as the span of the projection of U_p and retained projections of lifts of η_p(D). These lifts are well-defined modulo the projected U_p. As D fixes retained coordinates, the projected cocycle restriction is a homomorphism, with the same conclusion for the inverse action on M3. Put a=dim A5 and c=dim A3. The actual projected H-image satisfies

    |Hbar∩Nbar|=5^a 4^n3 3^c,       |Hbar|=5^a 4^n3 3^c |Q/D|.

The two prime images separate because they are coprime; the V4 factors remain independent. In particular the images of η(D) are essential: top lifts can enlarge the retained stabilizer beyond the image of H0.

The direct formula for K gives |Kbar|=60^u |Q/D|. For each top label, one free A5 coordinate is visible at every position retained on either side. Q-invariance of I5,I3 makes their overlap independent of the label, and D fixes the retained positions, so merging labels introduces no extra choices. As |Gbar|=60^(n5+n3)|Q/D|, the original strict normal-subloop criterion is exactly

    5^a 4^n3 3^c |Q/D| > 60^b                         (1)

for every nontrivial proper L. There are finitely many such coordinate sets and subgroups for each datum. If no coordinate is retained, every proper D<Q satisfies (1) automatically. If every coordinate is retained, faithfulness makes D=1 and L=1, which must be excluded from the strict test. No quotient folder is assumed. Together with collision avoidance, the pinned original normal-subloop criterion makes these inequalities necessary and sufficient for simplicity.

The resulting folder is faithful. A nontrivial normal subgroup of G intersects N nontrivially, since C_G(N)=1, and a normal product of simple factors cannot lie in H0 with its proper coordinate projections. Also K generates G: writing κ(s)=(s,s^−1), the product κ(s)κ(t)κ(st)^−1 is (1,s^−1t^−1st). For s,t in the perfect base A5^Ω this generates the second base; combining it with κ(s) gives the first base. The top labels cover Q. The full marked set Λ=τK is the conjugacy class of the swap in the corresponding wreath extension: the possible top differences of a conjugator in G are twice its Q-coordinate, and multiplication by two is bijective on odd Q. Thus Λ²=K² is conjugacy invariant. Collision avoidance, |K|=[G:H] and the pinned folder theorem give the loop and its Bol identity. The constructed action is imprimitive: H is strictly contained in the proper subgroup with arbitrary first A5^Ω coordinates and second A4^Ω coordinates, with the same top Q. H is nontrivial, so the loop is not an associative group in its faithful left-regular representation. The pinned primitivity of a simple nonassociative Moufang loop's left multiplication action therefore makes this simple loop proper.

## Exhaustion and exact parameter equivalence

In any original canonical folder in this slice, orbit pairing, opposite endpoint types and abelian graph elimination give H0 of the displayed form. Generatedness makes the induced θ inversion on Q. Identify the first endpoint set with Ω and the second with its τ-partner; straightening τ's coordinate isomorphisms makes it the swap. This identifies the entire G with the displayed fiber product: the second top is the inverse of the first, and arbitrary inner coordinate corrections are already in its full socle. Thus its marked set gives precisely the displayed K.

The endpoint frames can be made simultaneously standard while preserving τ. The 12 C5 generators in one A5 five-cycle class, paired with the five A4 point stabilizers, form a regular A5-set: the stabilizer is C5∩A4=1 and 12·5=60. Choose oriented first generators transported by H, consistently on each Q-orbit, and use the unique diagonal inner gauge at each paired position to standardize both frames. The first coefficients of every H-lift then lie in C5, and the second in A4. The framed quotient is V⋊Q with the stated inverse action on the second module, so H gives an ordinary η. The local conditions follow from the actual endpoint images. The preceding collision and normal-cut proofs establish every remaining required condition.

For a fixed faithful permutation group Q≤Sym(Ω), two admissible data give isomorphic loops exactly under the following operations. Take f∈N_Sym(Ω)(Q), with induced automorphism σ of Q, and a choice d of elements of

    C4 = N_S5(C5) ∩ N_S5(A4)

constant on each Q-orbit. Let T_f transport coordinates by f. Let D_d act on F5 coordinates by the C4 multiplier and on F3 coordinates by its parity sign; these two scalar actions are linked. Then

    W5′=D_d T_f W5,     C3′=D_d T_f C3,
    η′(q)=D_d T_f η(σ^−1(q)).                              (2)

For different faithful Q-sets, first allow f that conjugates their permutation groups, rather than only a normalizer of one fixed group. Equivalently choose one representative of each faithful finite abelian permutation action, then apply (2). The same f intertwines both the ordinary and inverse actions, so (2) respects the displayed cocycle convention.

For completeness, a loop isomorphism induces an isomorphism of its generated faithful canonical folder and intertwines its canonical inversion. Since N is the socle and C_G(N)=1, it is determined by the induced wreath automorphism of N. The intrinsic actual endpoint types distinguish the two rows, and commuting with τ makes its coordinate permutation and local automorphisms the same on both rows. The permutation normalizes the actual Q-action. After this transport, the local maps preserve the intrinsic C5 and A4 frames and hence lie in C4. Comparison of first coefficients of every top lift in the two reflection-free forms gives d_i d_(q^−1 i)^−1∈C4∩C5=1; thus d is constant on each Q-orbit. The coefficient action is exactly (2). Conversely every such simultaneous permutation and orbitwise C4 choice normalizes G, commutes with τ, preserves K and transports H according to (2), so induces a loop isomorphism. No arbitrary GL(V) operations or cocycle coboundaries are added.

## Evidence and remaining scope

These are analytic proofs; independent exact-source review is recorded below. The claimed endpoint is a construction, exhaustion, finite admissibility test and exact equivalence for this proper-endpoint abelian slice, allowing any number and size of factor orbits. It leaves the orbits of the admissible module/cocycle data unevaluated. Full strips, nonabelian tops, non-surjective odd tops, other socles, outer actions and radicals remain outside this result; C0010 and the unrestricted classification remain open.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned inputs. They checked simultaneous actual endpoint framing, zero-projection local surjectivity, the inverse second-module action, cycle products and the bijective-cocycle collision equivalence, all normal subgroup forms and one-sided cuts, the actual η(D) contributions, original strict simplicity, corefreeness, generation and the properness argument. They also checked construction and exhaustion and the complete simultaneous permutation/orbitwise C4 equivalence, without arbitrary GL or extra coboundary identifications. audit_c9 explicitly inspected the pinned zero-graph/framed-lift source; none independently reproved all upstream results or freshly audited their primary literature. These are analytic model reviews, not computation, human/formal certification or GitHub approval. The result leaves admissible module/cocycle orbits unevaluated and retains precisely its proper-endpoint abelian slice.
