# Residual dependency graphs and strict invariant cuts

Mira Cult

**Independently reviewed analytic reduction under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Work in the faithful generated canonical simple nonassociative folder with Soc(G)=A5^Ω and G=A5^Ω⋊Q, where Q is finite odd nilpotent and acts faithfully by pure factor permutations. Use the [complete pairing theorem](radical-free-a5-nilpotent-orbit-pairing.md), [paired path and endpoint reduction](radical-free-a5-paired-path-residual.md), and [strict original-folder cuts](radical-free-a5-residual-kernels-cuts.md). Their original-folder, actual class-square and subgroup inputs remain pinned there. No quotient folder or independent proper residual is assumed.

There are M A4-type proper endpoint coordinates and M opposite C5/D10-type coordinates. Their actual H0=H∩A5^Ω projections are respectively V4/A4 and 1/C5/D10. Let R be the correlated residual. Its order is 60^M/k, where k=[Q:C_Q(θ)] is odd, hence k=3^d5^e for d=v3(k), e=v5(k). Original full strips are independent of R and have size two. Fix any actual selected outside N-class. Its factor pairing and the original full strips give disjoint coordinate chains between opposite proper endpoints; use this matching to index both endpoint sets by 1,...,M.

## The actual Sylow-two quotient is a graph

Let W5=R∩C5^M, embedded with identity on the A4 side. It is the unique Sylow-5 subgroup of R: the natural quotient embeds

    X=R/W5 ≤ C2^M×A4^M,

and has no factor 5. Thus |W5|=5^{M−e}. The kernel of X→C3^M is a normal elementary abelian 2-group with order 4^M, hence the unique Sylow-2 subgroup P of X. A Sylow-2 subgroup of R maps isomorphically to P. In those involution lifts an opposite coordinate whose C2 image is zero is actually identity, since it lies in C5; a nonzero C2 image is a nonidentity reflection. Quotient support is therefore actual involution support.

The original class-square test forbids a nonidentity element with matched endpoint support: it would extend through the independent full strips along the chosen chains. On P, write e_D,e_V for the indicators that an opposite and an A4 endpoint coordinate are zero. The matched-support indicator is 1+e_D+e_V over F2. Expanding its product and summing over P gives an odd count, because only identity matches. Every term selects at most one coordinate per matched pair. Unless all V4 coordinates are selected, the target has order strictly less than 4^M and the projection kernel has even order. Consequently P→V4^M has odd kernel and is an isomorphism. This argument does not require every endpoint projection to contain 3. We obtain a linear map

    φ:(F2²)^M → F2^M,

whose graph is P, with the domain indexed by A4-type endpoints and the range by their matched opposite endpoints. This retains all correlations in the Sylow-2 quotient; the odd residual can carry additional correlations.

Let C be the image of X in C3^M. Conjugation by C fixes the C2 output coordinates and acts on each V4 coordinate through its coordinate character. Since P is normal in X, φ is invariant under that action. If the coordinate projection of C is nontrivial, its order-three operator minus identity is invertible on that V4 coordinate, so the corresponding column of φ is zero. Thus any coordinate with a nonzero outgoing column has actual H0 projection V4, not A4.

Let I be the set of these nonzero columns, with r=|I|. It is Q-invariant in the original A4 endpoint set. Indeed H normalizes R and W5, hence X and its characteristic Sylow-2 subgroup P. Its induced action on the V4 domain is a permutation of coordinates with invertible local linear maps, and on the C2 outputs is a coordinate permutation. Nonzero-column support is preserved, and H→Q is onto. In particular I is a union of whole endpoint Q-orbits. The paired-path deficiency budget gives

    r ≤ d.                                                   (1)

## Directed cycles are exactly the involution obstruction

The following elementary linear statement holds for any φ:(F2²)^M→F2^M with a fixed matching, independently of the group hypotheses. Draw a directed edge i→j exactly when its block functional φ_{ji}:F2²→F2 is nonzero. There is a nonzero x satisfying

    x_i≠0  if and only if  (φx)_i=1  for every i             (2)

if and only if the dependency graph has a directed cycle, including a self-loop.

For one direction, an acyclic graph admits a topological ordering. At the first index in that ordering for which x_i≠0, all predecessors have zero input, so (φx)_i=0. Thus (2) cannot hold.

Conversely, choose arbitrary nonzero vectors u_i∈F2² and form the M×M binary matrix A(u) with entries A(u)_{ji}=φ_{ji}(u_i). If det(I+A(u))=0, choose a nonzero kernel vector y and set x_i=y_i u_i. Then φx=A(u)y=y and (2) follows. Suppose there is a directed cycle and take a shortest one, with vertex set S. The formal determinant polynomial det(I+A(u)) is separately affine in each two-variable block u_i and has constant term one. Its component of degree one in exactly the blocks from S is the product of the edge functionals around that shortest cycle. Indeed a chord would give a shorter directed cycle, so the induced graph on S has only that cycle cover; the self-loop case is the one-variable version. This product is a nonzero polynomial, because its nonzero linear factors use disjoint variable blocks. The determinant polynomial is therefore not the constant one.

The three nonzero vectors of F2² affinely span F2². A separately affine polynomial that equals one on every tuple of nonzero vectors must therefore equal one everywhere, by applying this observation successively to each block. Hence the nonconstant determinant has value zero at some tuple with all u_i nonzero. This gives (2), completing the equivalence.

Applied to the actual graph P, condition (2) is exactly a nonidentity matched-support residual involution. Therefore the dependency graph is acyclic for every actual selected endpoint matching. This is an exact test of that involution slice; it does not assert transversality for every original group element. Acyclicity alone does not force φ=0: for example φ_1=0 and φ_2 a nonzero functional of x_1 gives a nonzero acyclic map with no matched-support vector.

## A strict cut through the active columns

If r>0, acyclicity forces r<M, since a finite directed graph with an outgoing edge from every vertex has a directed cycle. The Q-invariant set I therefore specifies a nonempty proper union U of entire paired path components and pure proper/proper orbit pairs: include the component associated with each A4-type endpoint Q-orbit in I. This union is Q- and τ-stable and contains every full strip it meets. It does not require Q to permute individual alternating coordinate chains or to act equivariantly on one aligned dependency graph.

There are 2r proper coordinates in U. If m_U full strips are retained, the selected factor permutation has c_U=m_U+r pairs and no fixed factor, so D_U=1. Every projected 3-part is trivial, because all A4-type endpoint projections in I are V4 and opposite endpoints have no 3. Projecting P onto these endpoint pairs has order 4^r: all columns outside I vanish, so the retained output depends only on the retained V4 inputs. Write r−b for the rank of the projection of W5 to the retained opposite coordinates. Then

    |R_U|=4^r5^{r−b},       0≤b≤e.                         (3)

The upper bound on b follows from dim W5=M−e: deleting the other M−r coordinates lowers rank by at most M−r. The pinned strict original normal-quotient criterion applied to A5^{Ω−U} now gives

    4^r5^{r−b} > 60^r/k,
    k > 3^r5^b.                                             (4)

This uses an actual projected residual, not a subgroup asserted to be a quotient folder. Together with r≤d and b≤e, it forces r<d or b<e. In particular if e=0, every nonzero φ satisfies

    0<r<d.                                                   (5)

Thus d=0 forces φ=0 by (1), and k=3 forces φ=0 by (5). For mixed 3/5 index, if r=d the projected 5-deficit must be strictly smaller than the global one. This is a rank statement; it does not locate that deficit at individual coordinates.

## Evidence and remaining obligation

These are analytic proofs with no computation. Independent review of the complete exact source is recorded below. The graph normal form is obtained before the additional endpoint-saturation hypothesis in the preceding residual source. The cycle criterion and strict cut leave nonzero acyclic graphs with unsaturated deficits, and they do not classify the odd residuals even when φ=0. The next obligation is to control projected odd subgroups and top lifts on invariant source or sink sets, retaining actual quotient fibers. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Orbit triangularity and actual top lifts

**Independently reviewed continuation under pinned inputs.** Retain the odd-nilpotent hypotheses and the graph theorem above at. Form a directed graph on the Q-orbits of A4-type input coordinates, identifying each opposite output Q-orbit with its input partner by the selected alternating strip/pair paths. Draw an orbit edge if a nonzero block of φ joins coordinates in those orbits. This orbit graph is acyclic. Every edge ends at a D10 residual-projection orbit whose degree is divisible by 3. In particular φ=0 whenever all endpoint Q-orbit degrees are coprime to 3.

For the first assertion, H acts on input blocks by coordinate permutations and invertible local maps and on output blocks by coordinate permutations. The two permutations need not agree under the selected path alignment, but both preserve the respective Q-orbits. If any input in an orbit has an edge to an output orbit, transitivity makes this true of every input in that orbit. A directed cycle in the orbit graph can therefore be lifted indefinitely to edges in the coordinate graph: the output coordinate reached determines the next matched input. Finiteness then gives a directed coordinate cycle, contradicting the reviewed cycle criterion. This proves orbit acyclicity, including absence of within-orbit blocks. A topological ordering of the whole orbits makes φ strictly triangular in orbit blocks; initial and final orbit unions define Q- and τ-invariant whole-component unions. No coordinate-level Q-equivariant matching is inferred.

For the second assertion, take a nonzero block φ_ji. The input has H0 projection V4 and actual point-stabilizer image A4. Its Q-point-stabilizer Q_i consequently acts on V4_i through a nontrivial C3 character; changing an H-lift by H0 changes local conjugation by V4, which acts trivially on itself. The actual output coordinate stabilizer Q_j acts trivially on its C2 quotient. For every u∈Q_i∩Q_j, equivariance therefore gives φ_ji ρ_i(u)=φ_ji. A nonidentity order-three rotation has no fixed nonzero F2-linear functional on F2². Thus Q_i∩Q_j is contained in the kernel of that C3 character, and 3 divides [Q_i:Q_i∩Q_j]. If the output Q-orbit degree were coprime to 3, Q_j would contain the unique Sylow-3 subgroup of nilpotent Q, and Q_i∩Q_j would contain a Sylow-3 subgroup of Q_i, a contradiction. This is where nilpotence is used; a general suborbit length need not divide the whole orbit size. Nonzero output sign also forces the residual projection at j to be D10, rather than 1 or C5.

The full column at i is an equivariant map from the irreducible two-dimensional C3-module V4_i to a permutation module on output coordinates. Its nonzero kernel is impossible, so its rank is two. A suitable 3-element of Q_i acts nontrivially on its image, hence moves output coordinates in an orbit of length divisible by 3. These columns need not be mutually independent. In particular if d=v3(k)=1 and φ≠0, its sole active input is Q-fixed, it points to a 3-divisible D10 orbit, and the earlier strict cut forces e=v5(k)>0 and zero projected 5-deficit on the singleton active cut. These are necessary conditions only.

## A strengthened cut using the actual hidden three-part

Let U be a nonempty proper Q- and τ-invariant union of whole paired components, with s retained endpoint pairs and m_U full strips. Assume no discarded input has a nonzero block to a retained output. This holds for a predecessor-closed union in the orbit DAG, and makes the actual projected Sylow-2 residual a graph of order 4^s. Let r be the number of retained inputs that retain at least one nonzero output block. Write

    |R_U|=4^s3^a5^(s−b).

Set A=O3(ker(Q→Sym(U))) and M0=N_(Ω−U)⋊A. These form actual subgroups in the given pure semidirect product. M0 is nontrivial, proper and normal in G; it is τ-stable. To justify the last assertion even if τ does not preserve the chosen complement Q, an element of A acts trivially on U, so its τ-conjugate also acts identically on the retained simple factors. Its induced top is in A, and its possible inner correction has trivial U-components because those simple factors are centerless. Thus the correction lies in N_(Ω−U). Put

    kbar=[Q/A:C_(Q/A)(θ)] = k/[A:C_A(θ)].

The equality follows from coprime fixed-point lifting. Explicitly, if θ(x)=xa for a∈A represents a fixed quotient element, then θ(a)=a^−1. Its odd-order square root b satisfies θ(b)=b^−1 and θ(xb)=xb, giving C_Q(θ)→C_(Q/A)(θ) onto.

Let B be the kernel of the actual image of H in G/M0 under its projection to Q/A. It contains H_(U,0), the image of H0; B/H_(U,0) is a 3-group of order h. This is the actual hidden H-image, not the full normalizer of H_(U,0). Every B-element arises from an H-element whose top is in A and fixes U pointwise, so its actual endpoint images lie in A4 and C5/D10, even where an opposite H0 projection is trivial. The full normalizer of such a trivial projection would be A5; using it would give an invalid bound here.

The independent projected full strips are self-normalizing in their coordinate products, so multiplication by those H_(U,0) factors removes the full-coordinate part of B. On the remaining endpoints, the homomorphism induced by A4→C3 has kernel contained in V4^s×D10^s and thus has order divisible only by 2 and 5. Its image preserves the 3-part of subgroup orders. The image of R_U has dimension a. Conjugation by B preserves R_U and its characteristic Sylow-2 quotient graph while fixing all output C2 signs. At each of the r retained active inputs, invariance of a retained nonzero functional prohibits a nontrivial local C3 rotation. Hence B has rotation image of dimension at most s−r, and

    h ≤ 3^(s−r−a),       |R_U|h ≤ 4^s3^(s−r)5^(s−b).

The original marked-set projection has size kbar·60^(m_U+s): all retained factors are paired, there is one N_U-class per projected outside top label, and merging labels through A introduces no additional fixed-mark choices. The actual H-image has order 60^m_U |R_U|h |Q/A|. The original normal-subloop criterion forces strict inequality between the section-image cardinality and the corresponding group index. If H M0=G, the index is one and the inequality is still strict, since the section image contains identity and generates the nontrivial quotient. Therefore

    |R_U|h > 60^s/kbar,
    kbar > 3^r5^b.

No quotient folder is asserted. Subtracting a in the hidden-image estimate is necessary: its rotations are already counted in R_U. An active-input cut can discard all targets of an active input, so its original r need not be this retained r; the two must not be identified. Taking directed closures can introduce inactive inputs where hidden rotations survive. These inequalities and orbit triangularity do not yet eliminate every nonzero acyclic graph. The earlier review record does not cover these added sections; their separate exact-source review is recorded below.


## Abelian tops force a zero residual graph

**Independently reviewed theorem under pinned inputs.** Under the paired A5 hypotheses of this manuscript, if Q is abelian then φ=0, with arbitrary orbit degrees, original path lengths and residual correlations. This is a structural elimination of the nonzero graph branch, not a classification of the remaining odd residuals.

Canonical generatedness makes θ inversion on abelian Q: top images of K are θ-inverted and generate Q. Suppose φ≠0. Its orbit DAG has a source orbit X with an outgoing edge. All its n input coordinates have H0 projection V4. Let J≤Q be the point stabilizer on X. It is the action kernel on X because Q is abelian, and θ(J)=J. Along the corresponding whole paired path component, each Q-set is obtained from X by Q-equivariant strip bijections and θ-semilinear pair transport. Thus J fixes every coordinate of that component U, including the opposite endpoint and all full strips. U is Q- and τ-invariant and is proper, since the outgoing edge reaches a different input orbit.

Use the actual normal subgroup M0=N_(Ω−U)⋊J. It is nontrivial and proper; normality and τ-stability follow exactly as in the preceding hidden-kernel cut, since J fixes U pointwise and its possible τ-conjugation corrections vanish on the retained centerless factors. The top quotient Q/J has order n and θ acts by inversion, so kbar=n.

Let B be the kernel of the projected H-image's map to Q/J, after removing its independent projected full strips. Its original residual subgroup has 2-part 4^n: the source has no incoming orbit edges or within-orbit blocks, so the projected Sylow graph is zero. Its 3-part is trivial, since all retained inputs project to V4 and opposite endpoints have no 3. The quotient of B by this original residual is an image of the odd group J, so adds no 2-part. Every B-element is an actual H-lift with top fixing U pointwise, hence its local images lie in A4 on the input side and C5/D10 on the opposite side. In particular its 5-part is at most 5^n, whether or not the original 5-projection was deficient.

The total rotation image of B in (A4/V4)^X has rank at most one. For j∈J, any H-lift gives a well-defined local character J→C3 at i∈X, independent of the lift because the local H0 projection is V4. If a lift of q∈Q carries i to another coordinate, conjugating the lift of j still has top j because Q is abelian. Its difference from the original lift lies in H0 and has trivial local C3 image. Thus all local characters agree after transport around X. The transport is coherent: the coordinate stabilizer has image A4, whose inner action on A4/V4 is trivial. The rotation vectors therefore lie on one diagonal line. The kernel of this rotation map has only 2- and 5-parts in its actual endpoint coordinates, so

    |B| ≤ 4^n · 3 · 5^n.

If m_U full strips are retained, the actual selected-set image has size n·60^(m_U+n), and the actual H-image has size n·60^m_U |B|. The original strict normal-quotient criterion, including the whole-stabilizer case as in the preceding section, gives |B|>60^n/n. Together these imply 3n>3^n, impossible for positive odd n (equality at n=1, and the reverse strict inequality for n≥3). Therefore φ=0.

### Generated Sylow support and nonabelian source rotations

For the general nilpotent model, Q has no Sylow factor at a prime absent from k. Indeed θ preserves every Sylow subgroup Q_p. If v_p(k)=0, it fixes Q_p pointwise; every θ-inverted top element then has trivial p-component because p is odd. Such elements generate Q, so Q_p=1. Since k=3^d5^e, Q is consequently a {3,5}-group; if k is a 3-power, Q is a 3-group.

In that pure-3 case, let U be a source active component of degree n and A the pointwise Q-kernel on U. All its rows are isomorphic either to the source Q-set or to its θ-twist, so Q/A embeds in Sym(n)×Sym(n). Here n is a power of 3 and v3(kbar)≤2v3(n!)=n−1. The original projected residual has order 20^n: the global 5-core has full rank and the source has no incoming graph block. Write h=3^t for the actual hidden enlargement after quotienting by N_(Ω−U)⋊A. Its 3-rank t is exactly the rank of the actual local source rotations; the endpoint rotation kernel has only 2- and 5-parts and the full strips have been removed. Strictness gives kbar·3^t>3^n, hence t≥2. In particular, Q cannot act trivially on A/Φ(A): otherwise its conjugation fixes every local character A→C3, and transitivity makes all those characters equal, giving t≤1 as in the abelian proof. This is a necessary restriction on a nonabelian survivor, not its elimination.

## Zero-graph splitting and a framed affine lift

**Independently reviewed reduction under pinned inputs.** When φ=0, without assuming that every input H0 projection is A4, the residual splits as

    R=W5 × π^−1(C3) ≤ C5^X5 × A4^X3,
    π:A4^X3→F3[X3],

where |X5|=|X3|=M, W5≤F5[X5] and C3≤F3[X3]. Indeed every actual Sylow-2 element has trivial opposite projection, so no opposite projection can be D10. Its involution lifts from the quotient graph have identity on all C5 coordinates, and its full V4^M image therefore gives the literal independent V4^M subgroup in R. Quotient by that subgroup and use Goursat on the remaining 5- and 3-group images; their common quotient is trivial. This proves the split while retaining correlations within each prime. The exact order gives codim(W5)=v5(k), codim(C3)=v3(k).

There is a useful nonenumerative description of the actual H-lifts after fixing their endpoint frames. The actual opposite local image is now C5: D10 would have an even quotient over either possible H0 projection 1 or C5. At each such coordinate choose an oriented generator of this actual C5. It transports consistently along H because its point stabilizer is C5 and acts trivially by conjugation. On each input orbit transport an A4 frame and its C3 quotient orientation; actual point stabilizers A4 act trivially on that quotient. Choose inner coordinate maps g_i from the corresponding standard frames to these actual frames. In these coordinates W5 and C3 are Q-invariant, since H normalizes H0 and acts on each quotient by the indicated permutations. Set

    M5=F5[X5]/W5,    M3=F3[X3]/C3,    V=M5⊕M3.

Each Mp is generated by the point vectors from its actual endpoint Q-orbits, with a chosen point vector fixed by its Q-point-stabilizer. Multiple orbits do not imply a single cyclic generator, and X3 and X5 are related by the existing path-dependent θ-semilinear maps, not necessarily by an ordinary Q-isomorphism.

Define the framed normalizer F to consist of elements of N_G(H0) that carry the chosen A4 frames and oriented C5 frames according to their factor permutations. It contains H. Its intersection with N consists of the original full strips, A4^X3 and C5^X5; after dividing by H0 its kernel is exactly V. Its map to Q is onto. We now construct a section, rather than assuming its extension splits.

For q∈Q, the endpoint corrections g_i g_(q^−1 i)^−1 form an exact coboundary and transport the standard frames. On each full strip, an actual H-lift of q shows that the transported strip graph and the target graph have the same outer twist class. Thus an inner coordinate correction sends one to the other. Such a correction is unique modulo the target full strip, because a graph A5 is self-normalizing in A5×A5. Combine these disjoint strip and endpoint corrections into s(q)∈F with top q. The product defect s(q)s(r)s(qr)^−1 has trivial endpoint coordinates by the coboundary identity. It is supported on full strips and normalizes each of them, hence lies in their direct product, contained in H0. Therefore q↦s(q)H0 is a homomorphism and

    F/H0 ≅ V⋊Q.

The actual H/H0 is a complement to V in this quotient, so is the graph of an ordinary 1-cocycle η:Q→V. This conclusion includes the original strip twists; no arbitrary split-extension assumption was made. Changing actual frames or their identifications can change the coordinate expression. Only transformations induced by actual folder isomorphisms may identify parameters; arbitrary GL(V) changes are not justified.

This supplies necessary module and cocycle data and a split framed normalizer, not the missing complete collision, simplicity and isomorphism classification. In particular an affine transitivity test alone has not been proved equivalent to the original marked-set avoidance, and no stabilizer conjugacy to C_Q(θ) is asserted. The earlier review records do not cover these sections; their separate exact-source review follows.



## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned inputs. Each read the complete preceding source the recorded source revision and verified the sole subsequent scope correction: the graph retains all correlations in the Sylow-2 quotient, while the odd residual can carry others. The last reviewer requested that correction; all four accepted the corrected revision. Their analytic reviews checked the actual W5 quotient and involution lifts, normal Sylow-2 graph, intrinsic Q-invariant columns, both directions of the determinant cycle criterion, the whole-component invariant cut without individual-chain equivariance, and exact projected 2/3/5 orders and strict inequalities. No fresh computation, full independent re-review of upstream proofs, formal verification or GitHub approval is claimed. Nonzero acyclic cases and odd residual/top data remain unresolved.

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted the complete orbit-triangularity and hidden-three-part sections at exact revision the recorded source revision, conditional on the pinned inputs. They checked orbit-cycle lifting without pointwise matching equivariance, nilpotent point-stabilizer divisibility, the actual hidden H-image rather than its full normalizer, removal of independent strips, subtraction of existing residual rotation rank, fixed-label deduplication and original strict quotient criterion including H M0=G. No new computation or full upstream reproof was performed. These are model mathematical reviews, not human/formal certification or GitHub approval; deficient acyclic cases remain open.

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted every section from the abelian-top theorem through the framed affine lift at exact revision the recorded source revision, conditional on the pinned inputs. They checked the proper source-component cut, full point-stabilizer kernel and diagonal rotation rank one, generated Sylow support and nonabelian source bound, literal V4 containment and coprime residual splitting, coherent actual endpoint frames, inner strip corrections and multiplication defect in H0, and the resulting normalizer quotient and cocycle graph. The proof leaves actual marked collisions, all simplicity cuts and the parameter isomorphism relation unresolved. No new computation or fresh upstream-source audit was performed. These are model mathematical reviews, not human/formal certification or GitHub approval.
