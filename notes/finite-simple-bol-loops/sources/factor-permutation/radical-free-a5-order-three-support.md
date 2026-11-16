# Order-three support in an actual marked-class square

Mira Cult

**Independently reviewed analytic obstruction under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be the faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q, Q finite odd nilpotent acting faithfully by pure factor permutations. Put H0=H∩N=T×R, the original full-strip/proper-residual decomposition. The [actual selected-class-square and counting interface](radical-free-a5-full-strip-matching.md) is pinned; original strip separation and H→Q use [the tensor source](radical-free-a5-orbit-tensors.md). The [strip-orbit forest](radical-free-a5-strip-orbit-forest.md) is pinned. This uses actual Sylow-3 subgroups, with no assumption that a separately chosen residual Sylow subgroup is normal or that proper coordinates are independent.

Let C be an actual selected N-class with involutory factor permutation σ. At a σ-fixed factor call the local class inactive if it is identity and active if it is a double transposition or a transposition. The square of the double-transposition A5-class contains the A5 class of 3-cycles: for instance the product (12)(34)·(12)(35) is a 3-cycle. The square of the S5 transposition A5-class contains the same 3-cycle class, since (12)(23)=(123). Both squares also contain identity. On a σ-swapped pair the square contains arbitrary entries that are conjugate inverses after the fixed local twist, realized by independent N-conjugation; in A5 there is one class of 3-cycles and it is closed under inversion. Therefore C² contains every socle element of order 3 whose fixed-coordinate entries vanish at inactive marks and whose two entries at each σ-pair are simultaneously zero or nonzero. Every such matching pattern can be realized simultaneously.

Choose a Sylow-3 subgroup P3(R) of the actual proper residual and a Sylow-3 subgroup C3 on each original full strip. Their product P≤H0 is elementary abelian: every 3-subgroup of a proper A5 coordinate is cyclic of order at most 3. Each coordinate of P is a linear functional P→F3 after choosing an arbitrary generator at that coordinate, and all such generators may be chosen independently.

Let a_C be the number of active fixed coordinates, c the number of σ-pairs, and f the total fixed count. Impose equality of the two F3-valued coordinate maps on every σ-pair and vanishing of the coordinate map on every inactive fixed coordinate. These are at most c+f−a_C homogeneous equations. Any nonzero solution belongs to H0∩C² by the support statement above. Thus the kernel is zero. The exact selected-class count gives dim P=c+f−v3(kD), and therefore

    v3(kD)≥a_C.                                              (1)

For the actual stable-mark decomposition D=15^s 10^v E, with a=max selected optional subset size, taking a class attaining a yields

    v3(kE)≥v+a.                                               (2)

More precisely, for each sign vector ε∈{±1}^c impose x_i=ε_i x_j on each swapped pair, together with zero at inactive fixed coordinates. Every resulting linear map L_ε:P→F3^(c+f−a_C) must be injective: any nonzero kernel vector has the required matched support. Conversely, any matched-support element of P lies in the kernel of at least one L_ε, because its two nonzero F3 coordinates differ by a sign. Thus square avoidance on the order-3 part of P is equivalent to injectivity of all these maps. In the tight case v3(kD)=a_C they are square, so all 2^c determinants must be nonzero. This is a structural constraint on the actual P3(R), not an independent-coordinate assumption. 

## Actual supported component codes

A second, graph-specific restriction can detect collisions even when (1) is sharp. For this chosen class C form a graph with one vertex for each original full strip and one vertex for each proper coordinate whose local H0 projection is divisible by 3. Carry every full coordinate by its strip vertex and every 3-bearing proper coordinate by its own vertex. Add an edge for each σ-pair of carried coordinates; a σ-pair joining a carried coordinate to a 3-free proper coordinate flags that vertex as zero. Flag a carried vertex as zero also if it carries any inactive σ-fixed coordinate. Multiple edges and loops are allowed.

Take an unflagged graph component and let I be its set of 3-bearing proper-coordinate vertices. Let K_I be the actual subspace of P3(R) supported only on I, viewed in F3^I; its coordinate projection is injective because it is defined to be trivial at every proper coordinate outside I. If I is empty, any nonidentity 3-element on each strip of the component gives a collision. If I is nonempty and K_I contains a word nonzero at every coordinate of I, choosing that word and nonidentity 3-elements on the component's full strips gives an element of H0∩C², a contradiction. Thus every unflagged component with nonempty I requires K_I to have no full-support word.

Two checkable sufficient conditions for a full-support word are:

* all coordinate functionals on K_I are nonzero and their projective classes number at most three; three proper hyperplanes cannot cover an F3-vector space;
* |I|≥2, every coordinate functional on K_I is nonzero, and codim_{F3^I} K_I≤1. In the proper hyperplane case, a defining equation has at least two nonzero coefficients; choose each nonzero coordinate ±1 so their weighted sum is zero. A sum of r≥2 signs in F3 can be zero (use pairs of opposite signs and, when r is odd, a triple of equal signs). Coordinates absent from the equation can be arbitrary nonzero values.

For |I|=1, nonzero K_I immediately gives full support. These criteria concern actual supported kernels and actual correlated Sylow-3 data, not projections treated independently. If a coordinate is identically zero on K_I, the component remains an obstruction to this particular construction rather than an automatic contradiction.

## A supported kernel on a 3-power boundary

Let I be a proper-coordinate Q-orbit of size 3^r>1. Because Q is nilpotent and transitive on I, its Sylow 3-subgroup Q3 is transitive there: the normal odd-prime-to-3 Hall subgroup has orbit sizes dividing both its order and |I|, hence fixes I pointwise. Choose P∈Syl₃(H); its image in Q is Q3. The normality of R in H makes P_R=P∩R a P-normal Sylow-3 subgroup of R.

Let E be the subgroup of P_R supported on I and trivial at every other proper coordinate. It is P-invariant. The local nontrivial projections of P_R are groups of order 3, and P acts on these coordinates by signed monomial maps. A 3-group point stabilizer has no nontrivial homomorphism to Aut(C3)=C2, so these signs can be straightened by choosing coordinate generators along the transitive P-action. If E is nontrivial, transitivity makes every local projection nontrivial. Thus the image of E on I is an F3-submodule of the ordinary transitive Q3 permutation module F3^I. If E≠1, that module contains a nonzero invariant: every nonzero module for a finite p-group in characteristic p has a nonzero fixed vector. The ambient invariant space consists of the constant vectors, so E contains an actual order-three element nonidentity at every I-coordinate.

If b is the number of OTHER proper coordinates on which R has a 3-bearing projection, then

    v3(|R|)>b  ⇒  E≠1.                                         (1)

Indeed P_R is elementary abelian and its projection to those b coordinates has dimension at most b; all remaining proper coordinates have trivial 3-projection. Thus the projection kernel is nonzero and supported on I. No residual-coordinate independence or normality of a separately chosen Sylow-3 subgroup of R is assumed: P∩R is normalized by P.

For a collision application, suppose I is the UNIQUE proper boundary orbit of a connected component of the reviewed strip-orbit forest, and some actual selected outside-involution N-class is active at every fixed full factor in that component (local double transposition or outer transposition). Fill every full strip in that component with an arbitrary nontrivial order-three element, use the full-support element of E on I, and use identity on every other residual orbit and strip. Every internal τ-pair and boundary τ-pair then has matching nonidentity support; each fixed full coordinate is active; every other coordinate is identity. Full strips are independent of R and one another, so this is an actual H0 element. Since A5 has one 3-cycle class, its precise values and the strip twists do not matter: independent N-conjugation realizes arbitrary matching 3-elements in the square of the selected class. The element is nonidentity in H0∩Λ², contradiction.

Thus (1), together with a 3-power unique boundary and one fully-active selected class on its component, excludes a folder. For multiple boundary orbits, a supported element on just one forces the other boundary supports to vanish while strip support propagates, so the conclusion does not follow without additional simultaneous-code information. If some fixed full factor is inactive in every selected class, filling all strips also fails. These are actual remaining gaps. The argument is independent of a quotient-loop assumption.

## A failed hidden-kernel control

For a concrete subgroup/mark illustration, let Q=C25×C3 act on three degree-3 rows A,C,D through C3 and two degree-25 rows E,F through C25. Let θ invert Q, let τ preserve A and exchange C,D and E,F, and give the fixed A-factor the optional identity/double family of total weight 16. Take three full strips joining A to C coordinatewise and proper residual

    R=diag(C3 on D) × A4^25 on E × C5^25 on F.

The top permutes these factors, so these are actual subgroup and marked-class data with k=75. They give v2(|R|)=50, v3(|R|)=26 and v5(|R|)=25, exactly the global order required by 59 coordinates, 29 transposed pairs, one fixed coordinate and three full strips. They do not give a folder. In the class whose fixed A-mark is a double, the diagonal C3 on D is an actual supported full-support kernel. Filling the A–C strips with nonidentity 3-elements yields a nontrivial element of H0∩C². The normal-cut test also fails, as the companion [5-kernel cut](radical-free-a5-stable-five-kernel-cut.md) computes. This example illustrates a failed order-only construction, not evidence of a surviving loop.

## Evidence and remaining obligation

These are analytic proofs and exact integer counts, with no computational certificate. Independent review of the complete exact source is recorded below. The all-sign criterion concerns the actual elementary abelian Sylow-3 slice of H0; it does not test all elements of H0. The supported-boundary exclusion requires its explicit rank, unique-boundary and active-mark hypotheses. Multiple boundary orbits, correlated supported kernels of smaller rank, and inactive fixed factors remain open. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, an automated checker, and an automated checker independently accepted both complete companion sources at exact revision the recorded source revision, conditional on their pinned original-folder, class-square, strip, local-mark and weighted-kernel inputs. They checked simultaneous order-three support and all-sign injectivity, actual supported-code criteria, the P∩R invariant-kernel argument and scoped boundary collision; normality and τ-stability of the quotient subgroup, the hidden projected stabilizer via its normalizer quotient, fixed-point lifting, merged-label mark deduplication and strictness including HM=G. The failed control's exact valuations and the two false inequalities 3>75 and 3>3 were checked. No computational rerun or fresh independent audit of the pinned inputs was performed. These are model mathematical reviews, not human or formal certification or GitHub approval. The remaining multi-boundary, mark and projected-fiber conditions retain their stated scope.
