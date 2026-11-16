# Diagonal alternating strip grids and column groups

This theorem with scoped independent reviews concerns C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`]. Let n≥5, m=n+1, c≥5, d≥2, b=cd, T=A_n. Let R=diag(A_c)×S_d act on c×d original blocks, with the alternating factor acting identically on rows of every column and S_d permuting columns. Let A_m^b≤K≤S_m^b be R-invariant, P=K⋊R, N=T^(mb), and let G=N⋊P be a primitive induced twisted-wreath group with local image containing Inn(T). Under [the parity-code manuscript](tw-parity-code-subwreath.md)'s reviewed arbitrary-transitive-R local-map/normalizer, all-coset capacity and C0007 folder interfaces, no marked transversal exists for any outside involution β normalizing G. The arbitrary-transitive-R local-map and normalizer interfaces were independently reviewed at `cdfe466523a3358d1636f517f51664f3c7c51e22`; the prior symmetric-top all-marks theorem was reviewed at `123933cc594b601dd317d62b333a949d20431d35`. The full-column proof has the separate exact-source reviews below. This is one full-column diagonal strip family, not arbitrary diagonal strips or all TW. The two-column case d=2 is included.

## Characteristic strip and factor labels

The subgroup diag(A_c) is characteristic in R. When d≤4, it is the eventual derived subgroup: S_d is solvable and A_c is perfect. When d≥5, soc(R)=A_c×A_d. If c≠d the two simple factors have different orders and cannot be interchanged; if c=d their centralizers in R have different orders d! and c!/2, so they still cannot be interchanged. Thus the diag(A_c) factor is characteristic in all cases. Its orbits are the d columns.

If a permutation σ̄ normalizes R, it preserves that column partition. Composing with a column permutation, write it as (u_1,...,u_d)∈S_c^d. Normalization of diag(A_c) forces all u_i to induce the same conjugation automorphism of A_c; their ratios centralize A_c in its natural symmetric action and are 1. Therefore

    N_{S_(cd)}(R)=diag(S_c)×S_d.                              (1)

This remains valid when c=d and at c=6: it only uses the actual permutation centralizer, not an identification of abstract automorphism groups.

As in the parity-code theorem, any outside normalizing involution β has factor permutation σ normalizing P. The characteristic socle A_m^b of P forces σ to preserve the original blocks, and its induced permutation normalizes R. A compatible full-wreath lift pσ normalizes the actual induced G. The factorwise residual βpσ⁻¹ has constant outer class c₀∈Out(T), by transitivity of P and abelianity of Out(T). It may be trivial. Its square in Out(T) is trivial, so choosing γ in c₀ and putting z=(γ,...,γ) gives βG=z pσG and z²∈N; γ need not be an involution.

For λ∈βG, its factor-permutation label h∈σP has h²=1. By (1), its original-block action is (s,t)∈diag(S_c)×S_d, with s²=t²=1. Each block arrow has a lower S_m permutation; paired arrows are inverse and have the same parity. Pure diag(A_c) row permutations and pure S_d column permutations lie in P and have identity local arrows in compatible induced coordinates. Independent A_m^b≤K and N gauges are available as in the parity-code proof.

## Row collision

Let r be the number of transpositions of s. Orient them positive→negative. Each row transposition carries d lower block edges, one from each positive column j to negative column t(j); record their parity signs as a d-bit signature. If r≥2^d+3, among these signatures there are two disjoint pairs of equal signatures: at most 2^d+2 entries can avoid this (one signature can occur three times, all others at most once).

Within each selected pair-pair, independently gauge corresponding lower S_m arrows to r_j=1 or a fixed transposition according to their common sign. Coherent induced coordinates give the same local outer-arrow class on corresponding edges. Independently N-conjugate λ on the selected rows so that these forward arrows are Γ_(j,x) and their reverses Γ_(j,x)⁻¹, using separate choices for the two pair-pairs; let μ∈Λ result. A pure row permutation ρ∈diag(A_c), the product of the two transpositions swapping positive rows within the two pair-pairs, has identity local arrows, fixes all unselected rows and changes both matchings. For ν=ρμρ⁻¹∈Λ, the product μν is identity on unselected rows. Each selected arrow crosses the row bipartition twice and the column map t twice, so both the column and point-label maps cancel; its local arrows Γ and Γ⁻¹ cancel. More explicitly, an arrow from positive row a and column j to its matched negative row and column t(j) carries Γ_(j,x); the return arrow based at column t(j) is Γ_(j,x)⁻¹. The rematching keeps j fixed at the positive end, and t²=1, so the composed arrows are Γ_(j,x)⁻¹Γ_(j,x) or the reverse. The remaining nontrivial row permutation lies in diag(A_c)≤P, contradicting P∩Λ²={1}. Therefore r≤2^d+2.

## Column collision

Let v be the number of transpositions of t. Orient them positive→negative. Each column transposition carries c lower block edges indexed by the row i, with row map s, so its parities define a c-bit signature. If v≥2^c+1, two column transpositions have the same signature. Gauge their corresponding internal arrows to identical r_i values and N-conjugate their arrows to common Γ_(i,x) forward and inverse backward. A pure S_d transposition swapping the two positive columns preserves row positions and changes the matching. Its conjugation fixes all unselected columns; multiplying the two resulting Λ-elements cancels the row map s², the internal involutions r_i² and the Γ arrows, leaving a nontrivial pure S_d column permutation in P. Explicitly, a forward arrow from row i is Γ_(i,x), and its return from row s(i) is Γ_(i,x)⁻¹. The rematching fixes row labels and s²=1, so their product is identity in either direction. Hence v≤2^c. This argument does not assume the row permutation s is identity.

## Capacity

For an integer B≥0, let f_B(q) be the number of involutions of S_q with at most B transpositions. A matching with j≤B pairs embeds into a (B+1)-ary string by canonically assigning labels 1,...,j to its pairs, so

    f_B(q) ≤ (B+1)^q.                                          (2)

Let i_q be the total number of involutions including identity in S_q. The number of possible (s,t) is at most

    min(i_c,(2^d+3)^c) · min(i_d,(2^c+1)^d).                 (3)

This is ≤3^(cd). If c≥d≥4, bound the first factor by (2^d+3)^c and the second by d!, and use 3^d≥d(2^d+3): it holds at d=4 and propagates since 3d(2^d+3)≥(d+1)(2^(d+1)+3). Since d!≤d^d≤d^c, this gives (3)≤3^(cd). If c≥d=2 or 3, use c≥5 and the exact inequalities (9/7)^5>2 and (27/11)^5>6. If d≥c≥5, instead use i_c≤c! and 3^c≥c(2^c+1), which holds from c=5 by the same induction, and c!≤c^c≤c^d. For the induction with +3, the base is 3^4=81≥4(2^4+3)=76; if 3^d≥d(2^d+3), then 3d(2^d+3)−(d+1)(2^(d+1)+3)=(d−2)2^d+6d−3>0. For the +1 bound, the base is 3^5=243≥5(2^5+1)=165, and 3c(2^c+1)−(c+1)(2^(c+1)+1)=(c−2)2^c+2c−1>0. In the d=2,3 cases, c≥5 makes the displayed fifth-power comparisons sufficient. These cases cover all c≥5,d≥2. All comparisons are integer inequalities; no floating-point inference is required.

For each block label (s,t) at most (m!)^b factor-permutation labels lie in σP, and each has at most M^(mb) involutions, with the reviewed all-coset bound M and 3m!M^m<|T|^m from [the parity-code manuscript](tw-parity-code-subwreath.md). Hence

    |Λ|≤(m!)^b·3^b·M^(mb)<|T|^(mb),

contradicting the required transversal size. This establishes the full-column theorem conditional on its cited interfaces, with the exact-source reviews below; no general TW classification follows.

## Independent review of the full-column theorem

At exact source `5325d80926fe96073e800134e60fe9902f15bcce`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the full-column theorem for all n at least five, c at least five and d at least two, conditional on the pinned induced-coordinate/local-map, normalizer, all-coset capacity and C0007 interfaces. All checked the characteristic factor and permutation normalizer, including c=d and c=6; both signature-rematching arguments with arbitrary row and column involutions and order-four local representatives; and every arithmetic range in the uniform label bound. No new computation or primary-source audit was required. Their scope is the full-column diagonal-strip family and all stated marks; it does not include the later column-subgroup extensions below or unrestricted TW groups.

## Arbitrary transitive column groups with at least as many rows

**Extension with scoped independent reviews below.** Keep the alternating parity-base induced TW and marked-folder hypotheses of the preceding theorem. Let c≥5, 2≤d≤c, and let D≤S_d be any transitive group. Replace the full column group by R=diag(A_c)×D on b=cd original blocks, with R normalizing K. Then the same all-marks exclusion holds. The [full-grid theorem](tw-diagonal-block-tops.md) was independently reviewed at exact source `5325d80926fe96073e800134e60fe9902f15bcce`; the general transitive-R order-threshold and normalizer interfaces in [the parity-code manuscript](tw-parity-code-subwreath.md) have scoped reviews at `cdfe466523a3358d1636f517f51664f3c7c51e22`. The extension has its separate exact-source reviews below. In particular D may be imprimitive; the argument does not claim all transitive block tops are covered.

For d<c, |D|≤d!≤(c−1)!<|A_c|. Every homomorphism A_c→D is trivial by simplicity and order. Hence diag(A_c) is characteristic in R: its image under any automorphism projects trivially to D and has the same order. Its orbits are the d columns. A permutation normalizing R must permute these columns, and its row permutations in different columns induce the same conjugation on A_c; their ratios centralize A_c in S_c and are trivial. Consequently

    N_{S_(cd)}(R)=diag(S_c)×N_{S_d}(D).                       (1)

This includes c=6 and uses the actual permutation centralizer, not a claim that Aut(A₆)=S₆. Under the cited parity-code interface, any outside normalizing involution β has a compatible full-wreath lift reduction to the constant-outer coset described above. Every involution λ∈βG has an involutory block-permutation label (s,t)∈diag(S_c)×τD for a fixed τ∈N_{S_d}(D); in particular s²=t²=1. There are at most |D|≤d! possibilities for t, even when τ∉D.

The row-rematching proof in the reviewed full-grid theorem uses only pure diag(A_c) elements, not a column permutation in S_d. It applies unchanged with t∈τD: orient the transpositions of s and assign each the d-bit vector of parities of its lower block arrows, indexed by positive column j and matched negative column t(j). If there are at least 2^d+3 transpositions, two disjoint pair-pairs have equal signatures within each pair. Even A_m^b gauges and N gauges put the corresponding forward arrows into matching Γ_(j,x) form and reverse arrows into Γ_(j,x)⁻¹. The product of the two positive-row transpositions is in diag(A_c)≤P; conjugating by it rematches both pairs while fixing unselected rows. In the product of the two Λ-elements, the column map t is applied twice, the corresponding Γ arrows cancel, and the remaining nonidentity even row permutation lies in P, contradicting P∩Λ²={1}. Thus s has at most 2^d+2 transpositions.

A matching of at most B transpositions among c rows is encoded injectively by a (B+1)-ary string with its pairs canonically numbered. Hence there are at most (2^d+3)^c usable s, and the number of possible block labels is at most (2^d+3)^c d!≤3^(cd). For d≥4 this follows from 3^d≥d(2^d+3), proved by induction in the full-grid theorem, and d!≤d^c. For d=2 or 3 use c≥5 and the exact inequalities (9/7)^5>2 and (27/11)^5>6. At most (m!)^b factor-permutation labels lie over each block label; each fibre has at most M^(mb) involutions. The preceding all-coset estimate 3m!M^m<|T|^m gives |Λ|<|T|^(mb), contradicting transversal cardinality.

For the square case d=c, **every** D≤S_c is handled without any characteristic-strip or coordinate-normalizer claim: |R|=|A_c||D|≤(c!)²<3^(c²)=3^b. Indeed c!≤c^c and c²<3^c for c≥5, by the base 25<243 and the induction 3c²>(c+1)². The reviewed transitive-R order-threshold theorem therefore excludes all such marks regardless of whether a normalizer exchanges the grid axes. Together the two arguments cover every transitive D whenever c≥d≥2, subject to the cited inputs. The row-dominant collision deduction and this synthesis have the reviews below; no conclusion is drawn here for arbitrary D with d>c. ∎

## Alternating and small column groups when columns dominate

**Further deductions with scoped independent reviews below.** Continue under the same parity-base, primitive induced-TW and all-marks hypotheses, but let d≥c≥5 and D≤S_d be transitive. These deductions give two additional uniform classes. They do not cover arbitrary D with d>c.

First suppose |D|≤3^d. Then the already reviewed transitive-R order-threshold interface applies directly:

    |R|=|A_c||D|≤(c!/2)3^d<3^(cd).

Indeed c!≤c^c≤3^[c(c−1)]≤3^[d(c−1)], since c≤3^(c−1) for c≥2. This includes every primitive D not containing A_d by Maróti's Corollary 1.2, and every transitive D with no composition factor A_j for j>4 by his Corollary 1.5. The exact primary source, author-version limitations and CFSG qualification are recorded in [the parity-code manuscript](tw-parity-code-subwreath.md). Combining this order argument with the preceding row-dominant result covers **every primitive D**: for d<c the row result applies without a bound on |D|, and for d≥c either D does not contain A_d and satisfies Maróti's bound, or A_d≤D≤S_d as treated next.

Now suppose A_d≤D≤S_d and d>c. The d=c case is already covered by the square-grid raw-order argument above. Here soc(R)=A_c×A_d with nonisomorphic simple factors of different orders, so diag(A_c) is characteristic. Its orbits are the columns and the same centralizer argument gives N_{S_(cd)}(R)=diag(S_c)×S_d. For an outside normalizing involution mark, the reviewed parity-code interface therefore gives involutory block labels (s,t) in an appropriate normalizer coset, with s²=t²=1.

Orient the transpositions of t positive→negative. Each has c lower block edges indexed by the positive row i, with row map s, and therefore a c-bit parity signature. If there are at least 2^c+3 column transpositions, there are two disjoint pair-pairs with matching signatures within each pair. Even A_m^b gauges make corresponding internal arrows equal to r_i, where r_i is 1 or a fixed transposition, and N gauges put their local arrows in Γ_(i,x), Γ_(i,x)⁻¹ form. The product of the two transpositions swapping the positive columns within the pair-pairs lies in A_d≤D and has identity local arrows. Conjugating the Λ-element by it rematches both pairs and fixes all other columns. Their product has identity arrows and point labels because the row involution s, each r_i and each Γ/Γ⁻¹ pair cancel; its remaining nontrivial even column permutation is in D≤P. This violates P∩Λ²={1}. Thus usable t have at most 2^c+2 transpositions.

There are at most (2^c+3)^d such column matchings by the canonical matching encoding, and at most c! row permutations s. Their product is at most 3^(cd): 3^c≥c(2^c+3) for c≥5, by the base 243≥175 and induction difference (c−2)2^c+6c−3>0, while c!≤c^d since d≥c. Multiplying by at most (m!)^(cd) factor labels and M^(mcd) involutions per fibre contradicts the required |T|^(mcd), using 3m!M^m<|T|^m. Therefore the all-marks exclusion also holds for every A_d≤D≤S_d, without any constraint on the relative sizes of c and d.

Both deductions in this section have the exact-source reviews below. They inherit the stated folder, normalizer, local-count and CFSG source qualifications. Transitive D with d>c, |D|>3^d and D⊉A_d remain open here; no unrestricted TW conclusion follows. ∎

## Independent review of the column extensions

At exact source `c4154e4d8cfbe1485491f6ec0b57567f8a18e396`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted both appended column-group extensions, conditional on the pinned transitive-top induced/normalizer, folder, capacity and Maroti inputs and their source qualifications. All checked the characteristic strip for d<c, the normalizer coset and row-only collision, the raw square-grid estimate without excluding axis interchange, the small-order synthesis, and the simultaneous even column rematching for alternating overgroups. All checked the elementary inequalities and the primitive-column application of the cited order bound. No new computation or primary-source audit was performed. The scope is every transitive D with c at least d, every primitive D, and the stated small-order and alternating-overgroup classes; it does not cover all transitive D with d greater than c.


## Independent alternating column units

**Theorem with scoped independent reviews below.** Let n≥5, m=n+1, c≥5, f≥2 and e≥2^c+3, and put d=ef, b=cd, T=A_n. Let D≤S_d be transitive with A_e^f≤D≤S_e wr S_f in its natural action on f units of e columns; D need not split over its unit image. Put R=diag(A_c)×D. Assume A_m^b≤K≤S_m^b is R-invariant and G=T^(mb)⋊(K⋊R) is a primitive induced twisted-wreath group with local image containing Inn(T). Under the C0007, local-map, actual normalizer-lift and all-coset fibre inputs used above, no marked transversal exists for any outside normalizing involution β.

The prior column-subgroup extension was independently reviewed at `c4154e4d8cfbe1485491f6ec0b57567f8a18e396`; the independent-higher-base result at `123a301135a04a53738f904fce3fcc76b6394111`; and the arbitrary-transitive-R interfaces at `cdfe466523a3358d1636f517f51664f3c7c51e22`. The new argument has its separate exact-source reviews below. Its scope is this uniform independent-unit subclass, not diagonal strips inside D, smaller units, or all TW groups.

### Characteristic factors and unit system

The subgroup A_e^f is the unique minimal normal subgroup of D. It is minimal because transitivity of D makes the induced action on its f units transitive. A distinct minimal normal subgroup would centralize A_e^f, but C_{S_d}(A_e^f)=1: on each unit a permutation centralizing the natural A_e has trivial restriction, and commuting with the independent factors prevents unit movement. Hence soc(D)=A_e^f. In R, the two minimal normal subgroups are diag(A_c) and A_e^f. They cannot be interchanged by an automorphism of R because the first is simple and the second has f≥2 simple direct factors, even if c=e. Consequently diag(A_c) is characteristic and D=C_R(diag(A_c)) is characteristic as well.

The orbits of diag(A_c) are the d columns. Any permutation normalizing R therefore preserves the columns, and the row permutations in all columns are equal because they must induce the same conjugation on A_c and C_{S_c}(A_c)=1. Its column permutation normalizes D and hence preserves the units, the orbits of characteristic soc(D). No normalizer is claimed to preserve labels within units or to lie in D.

The reviewed transitive-R parity-code interface reduces any primitive local map to natural pointed-block conjugation up to a global automorphism of T and gives a compatible full-wreath lift for any outside normalizing involution mark β. Thus βG=z pσG with z=(γ,...,γ), γ² inner, and γ possibly 1 or of order 4. An involution λ∈βG has factor-permutation label h∈σP, h²=1. Its original-block action has a common row permutation s and a column permutation t that preserves the units; both are involutions. Pure elements of A_e^f≤D≤R≤P have identity local arrows in the compatible coordinates. Independent A_m^b≤K and N gauges are available.

### Collision for exchanged or internally moved units

Orient any transposed pair of e-column units positive→negative. The unit arrow π is an arbitrary bijection of their e column labels; we do not assume π∈A_e and do not gauge it away. Each positive column j gives c lower block edges, taking row i to row s(i) and the positive column j to its matched negative column π(j). Record the parity signs of the c internal S_m arrows as a c-bit signature. Since e≥2^c+3, among the e signatures there are two disjoint pair-pairs with equal signatures within each pair: otherwise at most one signature occurs three times and all others at most once, giving at most 2^c+2 entries.

Use independent even A_m^b gauges to make corresponding internal arrows of each selected pair-pair equal to r_i=1 or a fixed transposition according to the signature, and use N gauges to make their forward local arrows Γ_(i,x) and reverse arrows Γ_(i,x)⁻¹. Different pair-pairs may use different representatives. A pure permutation ρ∈A_e in the positive unit, namely the product of the two transpositions of positive columns, changes both matchings, fixes all other columns and has identity local arrows. For the normalized μ∈Λ and ν=ρμρ⁻¹∈Λ, the product μν is identity away from the selected columns; on them the row map s², internal maps r_i² and the Γ/Γ⁻¹ arrows cancel. Its remaining nontrivial column permutation is ρ in the positive unit and its π-transport in the negative unit, both even. Thus μν∈A_e^f≤D≤P, contradicting P∩Λ²={1}. No unit exchange is usable.

If a fixed unit's column involution has at least 2^c+3 transpositions, assign its transpositions the same c-bit signatures. The same two simultaneous rematchings via an element of that unit's A_e show that it is unusable. Thus each fixed unit has at most B=2^c+2 column transpositions. This remains valid if the normalizer coset σP is outside P: only conjugating elements are required to lie in P, and the product of the two Λ-elements is the displayed element of A_e^f.

### Capacity

A matching with at most B transpositions among e columns injects into (B+1)^e strings by canonically numbering its pairs. Because no unit exchange survives, at most (2^c+3)^(ef) column permutations are usable. There are at most c! row permutations. Since e≥2^c+3 implies d=ef≥c, the arithmetic from tw-diagonal-block-tops.md gives

    c!(2^c+3)^d ≤ 3^(cd):
    3^c ≥ c(2^c+3),  c!≤c^d.

The first inequality has base c=5 and follows by induction, as recorded in the grid manuscript. At most (m!)^b factor labels lie over each row/column label, and each fibre has at most M^(mb) involutions, with 3m!M^m<|T|^m from the parity-code theorem. Therefore |Λ|<|T|^(mb), contrary to the transversal cardinality. ∎

The strip characteristicity, arbitrary odd unit-arrow handling, simultaneous rematching and all-marks conclusion have the scoped independent reviews below. No claim is made for diagonal alternating strips inside D, for smaller unit degree, or for all TW groups.

## Independent review of column units

At exact source `6fe18de73836f5babe8bff5be255ff80fc864fb7`, GPT-6.1 Terra reviewers [model reviewer] and [model reviewer] independently accepted the independent alternating column-unit extension, conditional on its pinned C0007, transitive-top local-map/normalizer-lift and all-coset capacity inputs. Both checked the unique minimal normal subgroup of D, the characteristic factors and units in R, arbitrary normalizer cosets and odd unit arrows without a splitting of D, simultaneous even rematching with actual inverse-arrow cancellation, and the matching/count inequalities. No computation or fresh primary-source audit was performed. Their scope is the stated independent-unit class with e at least 2^c+3, not smaller units, diagonal strips inside D or unrestricted TW.


## A variable-degree composition-factor reduction

**Deduction with the scoped independent reviews below.** Keep the alternating parity-base induced TW and all-mark hypotheses in the preceding sections. Let c≥5, d>c, b=cd and R=diag(A_c)×D for a transitive D≤S_d. If D has no composition factor isomorphic to A_j for j>floor(3^(c+1)/c), then no marked transversal exists. Thus a remaining top must contain an alternating composition factor above this threshold. This uses the transitive-top order threshold reviewed at `cdfe466523a3358d1636f517f51664f3c7c51e22`, not independence of any alternating base; it says nothing about the arrangement of a remaining alternating section. The variable-degree application has the scoped reviews below.

### Composition-factor reduction

Attila Maróti, *On the orders of primitive groups*, J. Algebra 258 (2002), 631–640, DOI 10.1016/S0021-8693(02)00646-4, Corollary 1.5, printed p.4 of the 21 February 2002 author version, https://www.renyi.hu/~maroti/primitive.pdf, states that for an arbitrary permutation group D of degree d with no composition factor A_j for j>k, k≥4,

    |D| ≤ (k!)^((d−1)/(k−1)).                                (1)

The original paper uses CFSG; the cited author PDF and application at k=4 were checked in the parity-code manuscript's scoped review at cdfe466523a3358d1636f517f51664f3c7c51e22. No fresh primary-source audit is claimed here; the present variable-k application has separate reviews below.

Put k=k(c)=floor(3^(c+1)/c). For c≥5, k≥4 and k!≤k^(k−1), since the product over the k−1 factors 2,...,k is at most k^(k−1). Thus (1) yields |D|≤k^(d−1)≤(3^(c+1)/c)^(d−1). Since |A_c|=c!/2≤c^c/2 and d≥c+1,

    |R|=|A_c||D|
        ≤ (c^c/2)(3^(c+1)/c)^(d−1)
        = (3^(cd)/2)(3/c)^(d−c−1)
        ≤ 3^(cd)/2 < 3^(cd)=3^b.                              (2)

The independently reviewed transitive-block-top order-threshold theorem in [the parity-code manuscript](tw-parity-code-subwreath.md) applies to (2): the actual factor-permutation labels of a normalizing involution mark lie in a fixed coset σP of size |P|≤(m!)^b|R|; the all-coset fibre bound and 3m!M^m<|A_n|^m give strictly fewer than |A_n|^(mb) involutions. That theorem handles arbitrary local maps permitted by primitivity, arbitrary normalizing involution marks and possibly nontrivial quotient action. The bound does not rely on a characteristic row-strip or on unit normalizers, so no diagonal-coupling issue is silently discarded. ∎

Combining this numerical reduction with the prior reviewed d≤c row/diagonal result and full-S_d grid remains conditional on their exact stated inputs. It does not remove tops with arbitrarily large alternating composition factors, and it does not characterize how such a factor is represented. A next attack must use actual alternating-factor actions, their block/strip coupling, or collision constraints; the inequality alone does not supply such an exclusion.

## Coupled large diagonal alternating strip

**Separate theorem with the scoped independent reviews below.** The following structural result handles an unbounded diagonal alternating strip without assuming independent unit actions. Let c≥5, j≥2c², f≥2, let D≤S_f be **any transitive group of order less than |A_c|**, and put

    R=diag(A_c)×diag(A_j)×D

in its product action on b=cjf original blocks indexed by (row, middle position, unit). The two alternating factors act identically across every other coordinate, so this is genuinely coupled rather than a direct power of independent factors. Let R normalize an alternating parity base K as in the cited parity-code TW interface. The independent-column-unit argument was reviewed at `6fe18de73836f5babe8bff5be255ff80fc864fb7`; that pin does not cover this diagonal-strip argument. Under the same primitive induced-group, all-normalizing-involution mark, C0007 folder and all-coset fibre hypotheses, no marked transversal exists. This is not a conclusion for arbitrary large D, other diagonal couplings or all TW groups.

The two alternating factors are characteristic in R. An automorphism sends each to a normal subgroup. Projecting the image of A_c to A_j gives a normal subgroup of A_j, hence 1 since j>c; its projection to D is 1 because |D|<|A_c| and A_c is simple. Thus A_c is preserved. Similarly an image of A_j has trivial projection to A_c and D by simplicity and order, so A_j is preserved. The centralizer of their product is D, which is consequently characteristic as well.

A normalizer of R in the symmetric group on the b blocks preserves both alternating factors. Their orbits and intersections recover the product grid. On different units its row permutations induce the same automorphism of diagonal A_c; their ratios centralize A_c in S_c and are 1. Likewise the middle-position permutations agree, since C_{S_j}(A_j)=1. The unit permutation normalizes D. Hence

    N_{S_b}(R)=diag(S_c)×diag(S_j)×N_{S_f}(D).               (3)

This is an actual permutation statement, even if c=6; no claim is made about all abstract automorphisms of A_c. By the previously reviewed arbitrary-transitive-R parity-code interface, any outside normalizing involution β has a compatible full-wreath lift and outside coset z pσG, with constant outer class of order dividing 2. A label of an involution λ∈βG acts on the three grid coordinates as (s,t,u) in the normalizer, with s²=t²=u²=1. For fixed β, u lies in one coset of D and therefore has at most |D| possibilities; s has at most c! possibilities.

Orient the transpositions of t positive→negative. Each transposition carries cf lower block edges, indexed by positive row/unit (i,v), mapping the other coordinates by the involutions s and u. Record their S_m-arrow signs as a cf-bit signature. If t has at least 2^(cf)+3 transpositions, two disjoint pair-pairs have matching signatures within each pair. Even A_m^b gauges and independent N gauges put each collection's corresponding internal arrows into r_(i,v),r_(i,v) and Γ_(i,v,x),Γ_(i,v,x)⁻¹ form, exactly as in the reviewed grid row-rematching argument. The product of two transpositions of positive middle positions is a pure element of diagonal A_j≤R≤P; it has identity local arrows and changes both matchings. Conjugating μ∈Λ by it gives ν∈Λ with μν nontrivial in P: s²=u²=1 cancel the other coordinate maps, the r maps and Γ arrows cancel, and the remaining even middle permutation is nonidentity. Explicitly, a forward arrow based at (i,v,x) carries Γ_(i,v,x), and the return arrow based at (s(i),u(v),r_(i,v)x) carries its inverse. The rematching preserves the positive labels (i,v,x); s²=u²=1 and each r_(i,v)²=1 make the composed arrows Γ_(i,v,x) followed by its inverse, or the reverse. Thus any usable t has at most 2^(cf)+2 transpositions.

A matching of at most B pairs among j positions injects into (B+1)^j strings by canonically numbering its pairs. Hence usable middle labels are at most (2^(cf)+3)^j. Since cf≥10,

    2(2^(cf)+3) ≤ 3^(cf).

Moreover c!≤c^c<2^(c²) and |D|<|A_c|<c!, while j≥2c². Therefore

    c! |D| (2^(cf)+3)^j
      < 2^(2c²) · 3^(cfj)/2^j ≤ 3^(cfj)=3^b.              (4)

The first inequality 2(2^L+3)≤3^L follows at L=3 and by induction. Every top label has at most (m!)^b factor-permutation lifts and every fibre has at most M^(mb) involutions, with 3m!M^m<|T|^m in the reviewed parity-code theorem. Equation (4) therefore contradicts the marked-transversal size |T|^(mb).

The characteristic-strip argument, diagonal simultaneous rematching and counting comparison have the independent reviews below. The strict bound |D|<|A_c| is a real hypothesis used both for characteristicity and order; no assertion is made that an arbitrary transitive D satisfies it. No general TW exclusion follows. ∎

## Independent review of composition factors and coupled strips

GPT-6.1 Terra reviewers [model reviewer] and [model reviewer] independently accepted both appended deductions at exact source `1d4b306b5e94e1b2c0fb0a85809e374bca0f4327`, conditional on the pinned all-mark local-map, normalizer-lift, fiber-capacity and C0007 interfaces and the CFSG-dependent Maróti corollary. They checked the variable-k arithmetic, characteristic factors, actual grid normalizer including c=6, cf-bit simultaneous even rematching with inverse-arrow cancellation, and the strict counting bounds. Root directly rechecked Corollary 1.5 in the cited author PDF; the reviewers claimed no fresh primary-source audit or computation. The coupled result retains j≥2c² and |D|<|A_c| and does not cover arbitrary D or all TW groups.


## Three-axis diagonal grid with full symmetric unit top

**Theorem with scoped independent reviews below.** Let c,j≥5 and f≥2, and let R=diag(A_c)×diag(A_j)×S_f act on b=cjf original blocks. Keep T=A_n, n≥5, m=n+1, the R-invariant alternating parity base A_m^b≤K≤S_m^b, and the primitive induced twisted-wreath, local-image, C0007 and all-normalizing-involution mark hypotheses used above. Under those inputs, the argument below proposes exclusion of every marked transversal in this three-axis family. The transitive-R local-map and compatible full-wreath-lift interfaces and order-threshold theorem were independently reviewed at `cdfe466523a3358d1636f517f51664f3c7c51e22`; the alternating parity-base all-marks argument was reviewed at `123933cc594b601dd317d62b333a949d20431d35`. Neither review covers the new three-axis argument. It treats a full symmetric unit top, not arbitrary transitive unit groups or all TW.

### Normalizer and possible axis exchange

The normalizer of R preserves the unit fibres and may exchange the two alternating axes only when c=j. For f≤4, the last perfect derived subgroup of R is A_c×A_j; its two simple factors are characteristic as a set. For f≥5, soc(R)=A_c×A_j×A_f. An automorphism can permute isomorphic simple factors, but the A_f factor is distinguished from an isomorphic alternating coordinate factor by its centralizer in R: the latter contains S_f, twice the order of the corresponding alternating factor. Thus the A_f factor is characteristic. The A_c and A_j factors are individually characteristic if c≠j, and may be interchanged if c=j. Their orbits and intersections recover the grid and its unit fibres. Equal-size A6 factors cause no extra permutation axis: this argument uses only orders, characteristic factors and the trivial natural centralizers C_{S_r}(A_r), not Aut(A6)=S6.

Any normalizer permutation therefore acts coordinatewise, possibly composed with the exchange of the two equal alternating coordinates. In the nonexchange case, an involutory factor-permutation label h acts by (s,t,u)∈S_c×S_j×S_f, with s²=t²=u²=1. In the exchange case c=j, h acts by an involution w on the c×c row/middle grid, interchanging the axes, together with an involution u∈S_f. The normalizer's image on any fixed axis contains at most its full symmetric group. The compatible full-wreath complement and constant-outer coset reduction for an arbitrary β are those of the reviewed parity-code interface; the local representative may have order 4. No chosen representative is assumed in Λ.

### Rematching along an axis

Consider an axis of length L whose coordinate permutation is involutory and whose associated alternating or symmetric factor is present as a pure subgroup of R. Let a,b denote the other two axis lengths and q=ab. Each transposition of the L-axis moves q original-block edges and gives a q-bit signature of their internal S_m-arrow parities. With ≥2^q+3 transpositions, select two disjoint pair-pairs matching in signature. Even A_m^b gauges normalize their lower arrows; independent N gauges make the local arrows on each pair-pair Γ_(v,x) forward and Γ_(v,x)⁻¹ backward, where v records the other two coordinates. A pure even permutation of the L-axis, swapping the positive endpoints in each pair-pair, rematches them. It belongs to R even when that axis is alternating and has identity local arrows.

The product of the normalized Λ-element with its conjugate is identity outside the selected L-axis points. On them the other-coordinate permutation is applied twice and cancels, as do the internal r maps and Γ/Γ⁻¹ arrows. Explicitly, a forward arrow based at an other-coordinate v and point x carries Γ_(v,x), and the inverse return arrow is based at its image; rematching preserves v at the positive end, so the two arrows compose to identity even when the other-coordinate involution transposes the equal alternating axes; the remaining nonidentity even L-axis permutation lies in P. This contradicts P∩Λ²={1}. Therefore the L-axis label has at most 2^q+2 transpositions and at most (2^q+3)^L possibilities by canonical matching encoding. It also has at most L! possibilities. This works for the unit S_f axis in the exchange case: the other-coordinate map may transpose the equal alternating axes, but is still an involution and the pure unit rematching fixes those coordinates.

### Uniform arithmetic

For a,b≥2 with at least one ≥5, put q=ab and let L≥a,b. Then

    a! b! · min(L!, (2^q+3)^L) < 3^(qL).                   (4)

If L≥a²+b², use a!b!<2^(a²+b²)≤2^L and 2(2^q+3)≤3^q (valid for q≥10). If L<a²+b², use

    a²+b² < 3^(ab/3).                                         (5)

To prove (5), by symmetry start at a=5,b=2, where 29³<3^10. Increasing either coordinate multiplies the right side by at least 3^(2/3)>2 while the left side grows by a factor less than 2. Thus L<3^(ab/3). Since a+b≤2L,

    a!b!L!≤L^(a+b+L)<3^[ab(a+b+L)/3]≤3^(abL).

This proves (4) without asymptotics or a finite top census.

Since R itself acts coordinatewise, the fixed normalizer coset σR is wholly axis-preserving or wholly alternating-axis-exchanging; the following case bounds are therefore not summed. If the normalizer label h does not exchange alternating axes, choose L=max(c,j,f) and apply the axis collision above. The other two axes have lengths a,b as required; their labels contribute at most a!b!. If h exchanges the equal c=j axes and f≥c, choose L=f and use the unit collision with the possibly transposed c×c map as the other-coordinate involution. If it exchanges those axes and f<c, a raw top-coset count suffices: the number of block labels is at most |R|≤(c!)² f!≤c^(3c)<3^(c²f), since f<c, c≥5 and c³<3^(2c) (base c=5 and induction).

Thus in all cases the number of usable block-permutation labels is strictly below 3^b. The exact σP coset has at most (m!)^b factor-permutation labels over each block label, and the reviewed all-coset fibre bound is M^(mb), with 3m!M^m<|A_n|^m. It follows that |Λ|<|A_n|^(mb), contrary to transversal cardinality. ∎

The axis-characteristic, all-mark exchange treatment, simultaneous collision and arithmetic arguments have the independent reviews below. They rely on the exact cited TW/local-map, C0007 and fibre inputs, and give no exclusion for a general transitive unit group D.


## Arbitrarily many alternating axes with a symmetric unit top

**Extension with scoped independent reviews below.** Let r≥2, a₁,…,a_r≥5 and f≥2, and put R=(∏_{i=1}^r diag(A_{a_i}))×S_f in its product action on b=f∏a_i original blocks. Keep the alternating parity-base, primitive induced-TW, local-image, C0007 and all-normalizing-involution mark hypotheses of the preceding sections. Under those inputs, this candidate excludes a marked transversal for every outside normalizing involution. The arbitrary-transitive-R local-map/normalizer-lift and all-coset capacity interfaces were independently reviewed at `cdfe466523a3358d1636f517f51664f3c7c51e22`; the symmetric-top all-marks interface at `123933cc594b601dd317d62b333a949d20431d35`. Neither pin reviews the new multi-axis proof. The unit top here is the full symmetric group; no claim is made for arbitrary transitive unit groups or all TW.

### Normalizer and fixed axis

A normalizer of R can permute only equal-sized alternating axes; it preserves the S_f axis. For f≤4, the last perfect derived subgroup is the product of the alternating factors, so its minimal normal factors are preserved as a set; their common orbits recover unit fibres. For f≥5, soc(R)=∏ A_{a_i}×A_f. An automorphism permutes its simple minimal normal factors. When an A_{a_i} is isomorphic to A_f, the factors are still distinguished by the order of their centralizers in R: the centralizer of A_{a_i} contains S_f, while that of A_f contains A_{a_i}, giving a factor of 2 difference. Other simple factors have distinct orders unless their degrees are equal. Their orbit/intersection patterns recover the grid. Natural centralizers C_{S_q}(A_q)=1 rule out additional coordinatewise coupling. Thus an involutory normalizer's induced permutation on alternating axes is a product of swaps of equal-size axes; it may also apply coordinate permutations. For f≤4, the centralizer of the product of alternating factors in the grid action is the diagonal S_f on unit fibres, so the same conclusion holds. The case a_i=6 invokes no false assertion Aut(A6)=S6.

The prior parity-base interface gives βG=z pσG for every outside normalizing involution β, with compatible full-wreath lift, z constant in one outer class with z²∈N, and no need for z to be involutory or lie in Λ. Since R acts without permuting axes, the fixed coset σR has one fixed axis-permutation type. Any involutory label h∈σP has an involutory induced grid map. If that map fixes an axis of maximum length L, let its coordinate permutation there be t∈S_L and put q=b/L.

### Axis rematching

Each transposition of t carries q lower block edges, indexed by a positive value of the L-coordinate and all other coordinates. Give it the q-bit signature of signs of its lower S_m arrows. If t has at least 2^q+3 transpositions, two disjoint pair-pairs have equal signatures within each pair. Use independent even A_m^b gauges to normalize corresponding internal arrows, and N gauges to make their local arrows Γ_(v,x) and Γ_(v,x)⁻¹, with v recording all other coordinates. The product ρ of the two positive-axis swaps lies in the pure A_L factor, or in S_f if the fixed maximum axis is the unit axis. It has identity local arrows and changes both matchings. For μ∈Λ the normalized element and ν=ρμρ⁻¹∈Λ, their product fixes the complement and is identity on all local arrows and point labels, because the other-coordinate grid map is an involution and the Γ-arrows and their inverses cancel. Its remaining nontrivial even axis permutation lies in R≤P, violating P∩Λ²={1}. Thus t has at most 2^q+2 transpositions and at most (2^q+3)^L possibilities by canonical matching encoding; of course it has at most L! possibilities.

### Uniform factorial inequality

Let a₁',...,a_r' be the lengths of the other r axes, all at most L, with q=∏a_i' and S=Σ(a_i')². Their product includes all but one of the r alternating axes and possibly the unit axis, so at least r−1 entries are ≥5 and all entries are ≥2. We claim

    (∏ a_i'!) · min(L!, (2^q+3)^L) < 3^(qL).               (1)

If L≥S, use ∏a_i'!<2^S≤2^L and 2(2^q+3)≤3^q; q≥2·5^(r−1)≥10. If L<S, use

    S < 3^(q/(r+1)).                                          (2)

For r=2 at the minimal tuple (5,2), (2) is 29³<3^10. Adding one alternating axis of size 5 multiplies q by 5 while increasing S by 25; if (2) holds, the new exponent 5q/(r+2) is at least twice the old exponent q/(r+1), and S²>S+25. This proves the minimal tuple (5,...,5,2) for every r≥2. Increasing any coordinate multiplies the right side of (2) by at least 3^(2·5^(r−2)/(r+1))≥3^(2/3)>2, while S increases by a factor less than 2. Hence (2) holds for all allowed tuples.

Since every other axis length is ≤L, Σa_i'≤rL. With L<S<3^(q/(r+1)),

    (∏a_i'!)L! ≤ L^[Σa_i'+L] < 3^[q(Σa_i'+L)/(r+1)] ≤3^(qL),

proving (1). All inequalities are elementary; no finite top census is assumed.

### When maximum axes are exchanged

If h's axis permutation moves a maximum axis L, it swaps two alternating axes of size L. There are at least two such axes, so b≥2L²5^(r−2). The number of block labels in the fixed coset σR is at most

    |R|≤(L!)^(r+1)≤L^[L(r+1)]
       <3^[(2/3)L²(r+1)]≤3^[2L²5^(r−2)]≤3^b.

Here L³<3^(2L) gives the strict inequality; it holds for L≥5 by the base 5³<3^10 and induction, since the right side gains a factor 9 while the left gains at most (6/5)³. The next comparison uses r+1≤3·5^(r−2), valid for every r≥2. No axis rematching is needed in this case, even if there is another fixed maximum axis. Since R does not permute axes, the entire coset σR has the same axis-permutation type, so this and the fixed-axis bound are not summed.

In either case there are fewer than 3^b usable block labels. Over each lie at most (m!)^b factor-permutation labels, and each fibre has at most M^(mb) involutions, with 3m!M^m<|T|^m from the reviewed parity-base theorem. Hence |Λ|<|T|^(mb), contradicting transversal cardinality. ∎

The normalizer axis-permutation statement, multi-axis signature rematching and inequality (1) have the independent reviews below. They retain the precise prior induced-embedding, all-mark, local-coset and folder assumptions. No statement about arbitrary transitive unit groups or all twisted-wreath actions is asserted.

## Independent review of the full symmetric unit grids

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted both the three-axis and arbitrary-axis extensions at exact source `1818e2c44bee176638f1212fd8b36c6a8a92e5ba`, conditional on the pinned induced-group, local-map, normalizer-lift, all-mark, folder and fiber-capacity inputs. They checked the characteristic symmetric axis, equal-axis permutations including A6, fixed-coset case separation, actual inverse-arrow cancellation, and both uniform factorial bounds. No new computation or primary-source audit was performed. The full symmetric unit hypothesis remains essential to this conclusion; arbitrary transitive unit groups remain open.
