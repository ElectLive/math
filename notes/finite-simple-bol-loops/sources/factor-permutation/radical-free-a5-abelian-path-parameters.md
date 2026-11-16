# Structural parameters for all pure A5 envelopes with abelian odd top

Mira Cult

**Independently reviewed exact structural parameterization under pinned inputs.** This continues [classification frontier](../../claims/0010.md). The scope is every faithful generated canonical simple nonassociative Bol folder with G=A5^Ξ⋊Q, where Q is finite odd abelian and acts faithfully by pure factor permutations. Full strips, unequal orbit degrees and arbitrarily many orbits are allowed. The theorem below gives construction, exhaustion, explicit finite admissibility tests and an exact equivalence relation. It leaves the resulting module/cocycle orbits unevaluated and does not cover nonabelian tops, arbitrary outer actions, mixed socles or radicals.

Use the [complete pairing theorem](radical-free-a5-nilpotent-orbit-pairing.md), the [opposite endpoint path theorem](radical-free-a5-paired-path-residual.md), and the [abelian zero-graph theorem and framed lift](radical-free-a5-residual-dependency-graphs.md#abelian-tops-force-a-zero-residual-graph). The canonical-folder, original normal-subloop, isomorphism and simple-Moufang inputs remain exactly those pinned in the [proper-pair parameterization](radical-free-a5-abelian-pure-pairs.md). The new obligations here are normalization of arbitrary full-strip paths, their collision criterion, partial-strip cuts and completeness of the path equivalence. No quotient folder is assumed.

## Path and affine data

Choose finitely many nonempty transitive Q-sets X_j=Q/J_j and integers L_j≥0, with intersection of the J_j equal to 1. Thus the total action is faithful; no individual orbit need be faithful. Form a path with layers r=0,...,2L_j+1, each indexed by X_j. Let Ξ be the union of all these factors. Define

    q·(j,r,x)=(j,r,q^{ε_r}x),       ε_r=(-1)^ceil(r/2).

The involution τ exchanges layers (2a,2a+1) at the same x and acts on Q by inversion. Original full strips are the diagonal A5 subgroups between layers (2a−1,2a), for 1≤a≤L_j. Layer 0 is a C5 endpoint; layer 2L_j+1 is an A4 endpoint. Q acts identically across a strip and inversely across a τ pair. Put

    n=Σ_j |X_j|,     m=Σ_j L_j|X_j|,     |Ξ|=2(m+n),
    N=A5^Ξ,         G=N⋊Q,              Λ=τ^G,    K=τΛ.

For explicit marked coordinates, take Y to be the union of the even layers and put S=A5^Y⋊Q with their displayed Q-action. Then G identifies with {(u,v)∈S²:top(v)=top(u)^−1}, τ swaps the two rows, and K={(s,s^−1):s∈S}. In particular |K|=60^(m+n)|Q| and Λ is the full outside class. This is a description of the constructed set, not a fullness assumption on a new unknown folder.

Let X be the union of the X_j. On V5=F5[X], Q acts by qx at every component. On V3=F3[X], it acts on component j by q^{(-1)^(L_j+1)}x. Choose invariant W5≤V5 and C3≤V3. Define

    M5=V5/W5,     M3=V3/C3,     V=M5⊕M3,
    H0=(product of the m original full strips) × W5 × π^−1(C3),

where the last two factors are supported on the proper endpoints and π:A4^X→F3[X] is the coordinate quotient by V4. Require |V|=|Q|, and choose a bijective 1-cocycle η:Q→V for these actual parity-dependent actions. The pure Q subgroup normalizes the standard strips and endpoint frames, so the framed normalizer quotient is V⋊Q. Let H be the inverse image of the graph of η. These choices give |H0|=60^(m+n)/|Q| and |H|=60^(m+n).

Impose the same actual-local conditions as in the proper-pair theorem. At a zero coordinate projection of W5, the coordinate of η5 restricted to J_j must be onto F5. At a zero projection of C3, the coordinate of η3 restricted to J_j must be onto F3. The coordinate maps are well-defined on the quotient in these cases, and the restrictions are homomorphisms because J_j fixes that coordinate. They ensure actual endpoint stabilizers C5 and A4 even at H0 projections 1 or V4. Nonzero coordinate projections are already supplied by H0. Multiple endpoint orbits give one point-stabilizer-fixed module generator per orbit, without a cyclic-module assumption.

Finally impose every normal-cut inequality below. These are the complete admissibility conditions. In particular |V|=|Q| forces the primes of Q to lie in {3,5}; Q=1 and zero-dimensional modules remain allowed.

## Collision criterion with arbitrary full strips

For the framed path data with |V|=|Q|, the exact original condition H∩Λ²={1} holds if and only if the affine Q-action x↦η(q)+q·x is regular, equivalently η is bijective.

Fix h∈H with top q. Every q-cycle of factors has a cycle product in A5, well-defined up to conjugacy. At a C5 endpoint its order is 1 or 5; at an A4 endpoint its order is 1, 2 or 3. Consider an original full strip S_i joining coordinates a,b via its graph automorphism α_i; this notation also covers the unnormalized source folder. The two q-cycles at its ends have equal length ℓ, since Q transports strips and an odd-order strip stabilizer cannot exchange their endpoints. The element h^ℓ fixes both coordinates and normalizes S_i. A graph A5 is self-normalizing in A5×A5, so the two cycle products belong to S_i and are related by α_i. In particular their orders agree. This argument accounts for the actual coordinate transport and does not treat forward and reverse words as independent.

Suppose h=λ1λ2 for actual λ1,λ2∈Λ. Then λ1hλ1=h^−1. Its factor permutation is tτ for t∈Q, and conjugates q to q^−1 because Q is abelian. Hence it bijects the q-cycle sets on each τ-pair of coordinate orbits, preserving cycle-product orders. Full-strip transport also bijects the cycle sets and preserves those orders. Alternating these bijections follows each finite orbit-level path from one proper endpoint to the other. Each intermediate cycle has one incoming and one outgoing match, and the layer index moves monotonically; the chains cannot close. Every chain therefore has the same order at a C5 and an A4 endpoint, forcing order 1 throughout. This covers pure pairs as L_j=0. For q=1 it covers individual coordinates, so h must be identity. For q≠1, the endpoint cycle sums vanish, giving

    η5(q)∈(1−q)M5,      η3(q)∈(1−q)M3,

with the respective displayed actions. We used the elementary permutation-module identity that the kernel of all cycle sums is (1−q) times the module.

Conversely, suppose q≠1 and η(q)∈(1−q)V. Adjust an H-lift by W5 and C3 to make every endpoint cycle sum zero, then use independent V4 endpoint factors to kill the remaining A4 cycle products. On each q-orbit of original full strips, multiply by a suitable element of one independent strip to kill the cycle product at one end. Multiplication by that strip supplies an arbitrary A5 correction to this product; the other product is then identity as well by the graph-normalizer argument. Different strip q-orbits have disjoint supports, so all choices are independent. The resulting h∈H has identity cycle product on every factor cycle and is N-conjugate to its pure top q. Since τ inverts pure Q, q=(qτ)τ lies in Λ²; both outside involutions are in its full class. Conjugacy invariance of Λ² therefore makes h a collision.

Thus avoidance means that every nonidentity affine element has no fixed point. With |V|=|Q|, this is regularity and is equivalent to bijectivity of η, as in the proper-pair theorem. The proof handles moving full strips of every length and every orbit degree.

## Explicit original normal-subgroup tests

Retain any Q-invariant subset U⊆Ξ of individual factors, not necessarily τ-stable, and take D≤Q fixing U pointwise. Every normal subgroup is

    L=N_(Ξ−U)⋊D.

The proof from the proper-pair theorem applies: intersect with N, then the remaining normal subgroup centralizes the retained centerless socle, so its retained base labels are identity and its top fixes each retained coordinate. Conversely those conditions give normality since Q is abelian. In particular cuts are not restricted to whole paths or to both sides of τ pairs.

Count m_hit, the number of individual original full strips meeting U; n3, the number of retained A4 endpoints; b, the number of τ-pairs with both coordinates retained; and u, the number of τ-pairs meeting U. Then |U|=u+b. On the retained endpoints define A5(U,D) and A3(U,D) as the spans of the projected W5 and C3 together with the retained projections of lifts of η5(D) and η3(D). The projected restrictions are homomorphisms because D fixes those endpoints. These subspaces are independent of choices of lifts modulo the original projected subspaces. Write a=dim A5(U,D), c=dim A3(U,D).

Each full strip meeting U contributes one independent A5 to the projected H0, whether one or both of its coordinates survive. For an actual H-lift over D, a fully retained strip component can be removed by this projected strip because its normalizer in A5×A5 is itself; a partially retained strip can be removed by its full A5 projection. Thus no hidden top image adds another full-coordinate contribution. The endpoint hidden image is exactly accounted for by η(D), including its separate coprime 3/5 parts. Consequently

    |Hbar∩Nbar|=60^m_hit 5^a 4^n3 3^c,
    |Hbar|=60^m_hit 5^a 4^n3 3^c |Q/D|.

The explicit two-row K description gives |Kbar|=60^u |Q/D|: each retained or partially retained τ-pair gives one independent A5 label. Q-invariance of U and pointwise fixation by D make this count valid after merging top labels, even for one-sided cuts. Since |Gbar|=60^|U| |Q/D|, the exact strict normal-subloop test is

    60^m_hit 5^a 4^n3 3^c |Q/D| > 60^b                 (1)

for every nontrivial proper L. The trivial and whole-group normal subgroups are excluded; in particular if U=Ξ, faithfulness gives D=1 and L=1. If U is empty, every proper D<Q passes automatically. This is a finite rank and subgroup test for each parameter datum, with no assertion that the projected section is a quotient folder.

The collision theorem and cardinality make K a transversal of all conjugate stabilizers by the pinned folder theorem; Λ²=K² is conjugacy invariant. Generation follows from the two-row formula and perfection of the A5 base, exactly as in the proper-pair source. Corefreeness follows because H0 contains no individual full simple factor: its full strips have size two and its endpoint projections are proper, while C_G(N)=1. Inequalities (1) are necessary and sufficient for simplicity by the original normal-subloop criterion. For properness, enlarge H to the subgroup with arbitrary A5 coordinates everywhere except the A4 endpoints, where the frames remain A4, and include Q. This is a proper subgroup strictly larger than H, since it enlarges the C5 endpoints. Thus the faithful left multiplication action is imprimitive. H contains V4 endpoint factors, excluding an associative loop, and the pinned simple nonassociative Moufang primitivity input excludes a Moufang loop. This proves the constructive direction in the stated canonical model.

## Exhaustion and path normalization

For an arbitrary original folder in scope, nilpotence gives H→Q, generatedness gives θ inversion on Q, and the cited pairing and path theorems give opposite endpoint components with size-two strips. Abelian graph elimination gives the split residual. The strip bijections are Q-equivariant, while τ edges twist the action by inversion, so choosing each X_j at its C5 endpoint produces exactly the displayed layer actions and lengths. Their point stabilizers are the same J_j, since inversion preserves every subgroup of abelian Q. Faithfulness is therefore intersection J_j=1.

Here are the automorphism and gauge details needed to normalize the original paths. Straighten τ's coordinate identifications to make each τ pair a swap. The local outer labels of τ are constant on Q-orbits: conjugating a pure Q-permutation by τ gives an element of G, whose local components are inner. Thus this straightening preserves the entire pure-permutation group, allowing inner corrections already in N. Likewise an actual H-lift transporting two full strips shows their graph automorphisms have the same outer class. These classes are constant along each strip Q-orbit. Choose automorphisms constant on entire coordinate Q-orbits, equal on each τ pair and recursively along the path, to remove all strip outer classes. There is no cycle obstruction because every component is a path. These automorphisms preserve G and τ.

The remaining strip twists are inner. Choose a τ-fixed socle element recursively along each individual coordinate path to make them all diagonal. This conjugation preserves τ and preserves G as a group because the conjugator lies in N. The original pure Q remains inside G and now permutes the standardized diagonal strips. The remaining common diagonal A5 gauge on each complete coordinate chain simultaneously standardizes its oriented C5 and A4 endpoint frames, using the regular 60-element frame set proved in the proper-pair source. It preserves both the standard τ pairs and diagonal strips. In these coordinates the endpoint subspaces are Q-invariant and H has an ordinary cocycle graph in the displayed framed quotient; no residual extension defect remains. The intrinsic actual endpoint images give the local conditions. The collision and normal-cut arguments then imply all remaining admissibility conditions, proving exhaustion.

## Exact isomorphism relation

Two admissible data are equivalent precisely as follows. Choose one group isomorphism σ:Q→Q′ and a bijection of components preserving L_j, with simultaneous maps f_j:X_j→X′_(j′) satisfying

    f_j(qx)=σ(q)f_j(x).

Transport f_j to every layer of its path. For each component choose d_j in C4=N_S5(C5)∩N_S5(A4), constant on that whole endpoint orbit. Let T_f be the resulting endpoint relabeling, and D_d the scalar operation whose F5 unit and F3 parity sign are linked by this same C4 element. The relation is

    W5′=D_d T_f W5,      C3′=D_d T_f C3,
    η′(q′)=D_d T_f η(σ^−1(q′)).                         (2)

Equivalently, for a fixed faithful Q-action use its simultaneous permutation normalizer on the endpoint set with the path lengths preserved. No independent normalizer for each component, arbitrary GL(V) identification or cocycle coboundary is added.

Every operation (2) is an actual wreath automorphism preserving G, τ and the marked class, and transports H accordingly. Conversely the pinned canonical isomorphism interface sends N, H0 and τ to their counterparts. Full coordinate projections and the original full strips are intrinsic in H0, while the actual endpoint stabilizer images distinguish C5 and A4 ends. Thus it preserves the oriented paths and their lengths and induces a single σ and the displayed Q-set maps. C_G(N)=1 makes it determined by its factor action. In standardized coordinates, commuting with τ forces equality of its local maps across τ pairs, and preserving diagonal full strips forces equality across strip edges. Each individual coordinate chain therefore has one common local automorphism. Preserving its endpoint frames puts it in C4. Comparing C5 coefficients of every top lift, as in the proper-pair proof, makes this automorphism constant along the whole endpoint Q-orbit: its quotient at two q-related coordinates lies in C4∩C5=1. Its induced action is exactly (2), including the length-dependent 3-module action. This proves completeness of the equivalence relation.

## Evidence and limits

The argument is analytic; exact-source independent review is recorded below. Its endpoint is an explicit structural construction and exhaustive parameter equivalence for the whole pure A5 abelian-odd-top model, including all full-strip paths. It is not a finite census or an evaluated list of regular-affine module orbits. All upstream review and source qualifications remain in force. The general nonabelian-top paired model, non-surjective odd tops, outer actions, other or mixed socles and radicals remain open; this does not complete the unrestricted finite simple Bol classification.


## Extension to the entire nilpotent zero-graph branch

**Independently reviewed extension under pinned inputs.** There is an exact structural parameterization of the same pure A5 model with any finite odd nilpotent top Q, provided its actual residual graph φ is zero. Nonzero graphs are not excluded by this extension. The following replacements to the preceding parameters, tests and equivalence give the complete construction and exhaustion of that branch.

Choose an automorphism θ of Q of order at most two and require

    I={q∈Q:θ(q)=q^−1},      Q=⟨I⟩,      k=|I|=[Q:C_Q(θ)].

The equality follows by odd square roots: every involution qθ is Q-conjugate to θ. Replace the action on path layer r by the original Q-set action through θ^ceil(r/2). The endpoints therefore use the ordinary action and its θ^(L_j+1)-twist. The stabilizers J_j need not be normal. Faithfulness of the full factor action is exactly

    intersection over j of (core_Q(J_j) ∩ θ(core_Q(J_j))) = 1.

Both twists occur in every component, already in its first τ pair. In the endpoint modules use these actual actions, put |V|=k, and require an ordinary cocycle η:Q→V whose restriction η|I is a bijection I→V. The zero-projection local conditions use the actual point stabilizer of each endpoint, in particular the θ^(L_j+1)-twisted stabilizer at a 3-endpoint. They still assert surjectivity onto its F5 or F3 coordinate. This keeps nonnormal stabilizers and different component kernels.

The group is G=A5^Ξ⋊Q with τ swapping each adjacent paired layer and inducing θ on Q. Equivalently, with Y the even layers and S=A5^Y⋊Q, it is the fiber product

    G={(x,y)∈S²:top(y)=θ(top(x))},
    K={(s,s^−1):s∈S, top(s)∈I},       Λ=τ^G=τK.

Every indicated element is obtained from the swap class: its top labels are the twisted differences r^−1θ(r), which range over I by the square-root argument, and its base labels are arbitrary. Thus |K|=60^(m+n)k. With the same H0 and framed cocycle construction, |H0|=60^(m+n)/k and |H|=60^(m+n)|Q|/k. The parameters may still involve only the primes 3 and 5 in Q: |V|=k and generatedness imply this by the Sylow-support argument in the reviewed residual-graph source. This is a consequence, not an additional arbitrary restriction.

### The affine section replaces regularity

The exact collision condition is now

    H∩Λ²={1} iff every q∈I²−{1} has no affine fixed point on V
              iff η|I:I→V is bijective.                    (3)

In particular the affine Q-action is transitive, but it need not be regular. Its point stabilizer has order |C_Q(θ)|; no conjugacy to that particular subgroup, or normality, is assumed.

To prove the first equivalence, a collision h=λ1λ2 has top q∈I² and satisfies λ1hλ1=h^−1. Its actual outside factor permutation therefore takes q-cycles to q^−1-cycles. This replaces the use of abelian inversion in the previous cycle-product proof. The full-strip normalizer and endpoint-order arguments are unchanged: strip bijections and the actual λ1 pair bijections follow the same finite path, so all endpoint cycle products are identity. For q=1 the element h itself is identity. Otherwise η(q)∈(1−q)V. Conversely, given q∈I²−{1} with this affine fixed-point condition, the same endpoint and independent-strip adjustments kill all cycle products, giving an H-element N-conjugate to pure q. If q=ab with a,b∈I, then q=(aτ)(b^−1τ), a product of two actual outside involutions in Λ. This proves the collision and fixed-point equivalence without assuming θ inverts all of Q.

For the second equivalence, I is inverse closed and I² is Q-conjugacy invariant: it is the image of the conjugacy-invariant set Λ². If η(i)=η(j), then the affine element j^−1i fixes zero. Conversely, if ab∈I² fixes zero, the images of b and a^−1 at zero agree. Thus injectivity on I is equivalent to no nonidentity element of I² fixing zero. The cardinality |I|=|V| makes an injective restriction surjective and gives transitivity of the affine Q-action. Conjugacy invariance of I² then transports the zero-point test to every point of V. Conversely fixed-point avoidance makes η|I injective and hence bijective. This proves (3); the elements of I act sharply transitively on V, although Q itself may have point stabilizers.

### All normal cuts, including non-θ-stable subgroups

Retain arbitrary Q-invariant U⊆Ξ and choose D◁Q fixing U pointwise. The same centralizer argument classifies every normal subgroup as L=N_(Ξ−U)⋊D; abelianness was only used earlier to make every subgroup D normal automatically. Keep m_hit, n3, b and the retained ranks a,c defined using the projected endpoint subspaces enlarged by η(D). On retained coordinates D acts trivially, so this projected cocycle restriction is a homomorphism even when D is nonabelian. Its image splits into its coprime 3- and 5-parts. Thus the actual H-image has the same base order

    |Hbar∩Nbar|=60^m_hit 5^a 4^n3 3^c.

The marked top-label count is t_D=|π_D(I)|, where π_D:Q→Q/D, not |Q/D| in general. We justify the full projected count even when D is not θ-stable and U is not τ-stable. In the two-row description let A and B be the retained first and second positions in Y. Both are invariant under the full Q-action on Y. A subgroup D fixing U fixes A through its ordinary action and fixes B through θ(D). If i,j∈I have the same coset modulo D, write d=i^−1j∈D. Then

    θ(d)=i j^−1=i d^−1 i^−1 ∈D.

Hence d also fixes B in the ordinary Y-action, because θ(d)∈D and θ²=1. It fixes A as well. The two inverse-label permutations in (s,s^−1) therefore give identical correlations on A∩B for top labels i and j; where only one side is retained, its A5 label is free. There are exactly 60^|A∪B| choices above each distinct projected top label, with no extra choices from merging labels. Consequently |Kbar|=60^u t_D, with u the number of τ-pairs meeting U.

The complete strict normal-cut condition is therefore

    60^m_hit 5^a 4^n3 3^c · t_D > 60^b                 (4)

for every nontrivial proper L. The counts of Hbar and Gbar both contain |Q/D|, which cancel in the index. The proof uses the actual section image and actual hidden top lifts, and asserts no quotient folder. If U is empty, generatedness of I ensures t_D>1 for every proper D<Q, so such cuts pass automatically. The trivial and whole-group normal subgroups remain excluded from (4).

### Construction, exhaustion and equivalence in the branch

The framed construction, collision test (3), cardinalities and normal cuts (4) give a faithful simple proper Bol folder by the same original interfaces. Base generation uses the perfect A5 factors as before; the additional assumption Q=⟨I⟩ gives top generation. The subgroup enlarging every coordinate except the A4 endpoint frames proves imprimitivity and properness exactly as in the abelian construction. Conversely, a folder in the zero-φ branch has H0 and the framed split normalizer proved. Its layer actions are θ-twists. The outer-class, τ-fixed inner and endpoint-frame normalization arguments above use the actual H→Q action, not commutativity of Q; replacing inverse twists by θ throughout gives the displayed standard paths. They yield its cocycle η, and (3) and (4) give all required admissibility conditions. There is no assertion that a nonzero graph can be discarded by these gauges.

For parameter equivalence, use one group isomorphism σ:Q→Q′ satisfying σθ=θ′σ, a length-preserving component bijection with simultaneous σ-equivariant Q-set maps, and one C4 constant per endpoint Q-orbit. The linked endpoint scalars and cocycle law are exactly (2), now with these θ-twisted modules. Nonnormal stabilizers are transported as actual Q-sets; no regular-action normalizer is substituted. The necessity proof uses the intrinsic paths and actual endpoint frames and compares all top lifts, available because H→Q; it does not need Q abelian. Conversely these operations preserve G, τ, K and H and give loop isomorphisms. Thus this is an exact structural parameterization of the entire zero-graph nilpotent branch, conditional on the pinned inputs. It leaves nonzero graphs and the evaluation of admissible affine-section orbits open. The earlier review record covers the abelian theorem only; the extension has its own exact-source review below.



## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on the pinned inputs. They checked parity-dependent layer and module actions, outer/inner path normalization preserving the actual group and τ, simultaneous endpoint gauges, cycle-product order propagation under actual marked involutions, independent strip corrections, all partial-strip normal cuts with η(D) contributions, faithful/simple/proper construction and exhaustive path/normalizer equivalence. Their acceptance covers arbitrary full-strip paths and orbit multiplicities in the stated pure A5 abelian odd-top model. They did not independently reprove all upstream inputs, conduct a fresh primary-source audit or run computations. These are model mathematical reviews, not human/formal certification or GitHub approval. Admissible module/cocycle orbits remain unevaluated; the unrestricted classification is not closed.

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted this complete nilpotent zero-graph extension at exact revision the recorded source revision, conditional on its pinned inputs. They checked the nonabelian I² collision criterion and affine fixed-point transport from η|I, actual cycle reversal and strip corrections, nonnormal stabilizers and twisted cores, all normal cuts including non-θ-stable D and one-sided U, exact merged-label counts and η(D) hidden ranks, and construction/exhaustion/θ-compatible normalizer equivalence. No new computation, fresh primary-source audit or independent reproof of every upstream result was performed. These are model mathematical reviews, not human/formal certification or GitHub approval. Nonzero residual graphs and evaluation of admissible affine-section orbits remain open.
