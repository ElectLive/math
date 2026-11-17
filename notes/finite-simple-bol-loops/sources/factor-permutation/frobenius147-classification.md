# The fixed Frobenius-147 canonical envelope

**Mira Cult**

**Independently reviewed classification at the exact source below.** This is a bounded continuation of [0323:C0010](../../claims/0010.md). Let `F=F7`, `P=F⋊C3`, with the generator of `C3` acting by multiplication by 2, and let

    S=A5^F⋊P,       G={(s,t)∈S² : φ(s)+φ(t)=0},
    K={(s,s⁻¹):s∈S},       τ(s,t)=(t,s),

where `φ:S→C3` is the top quotient. The claim is that exactly **15** loop-isomorphism classes of finite simple nonassociative left Bol loops have this entire faithful generated canonical group, section and inversion. All are proper and arise from exact factorizations. This is a classification of this fixed envelope and full section, not of other canonical groups or of all loops of the same order.

The original folder, normal-subloop and isomorphism interfaces are C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45) and scoped C0007 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The full section, odd quotient and top-image theorem are in [the singleton-strip family](frobenius-singleton-strip-family.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/5c93bf4da693a8b863c5e87562ce420a9b2789b2). The actual selected-class-square and Sylow-two information-set argument is [paired support without surjectivity](radical-free-a5-nonsurjective-paired-support.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/82c3b17fc6f25e1a0dc6b0096219ad0efad5a41d). The graph and fixed-support calculations below use the actual H and selected classes, not a quotient folder. The F3- and F5-module decompositions are proved by the factorization of `x^7−1` over those fields.

## Top normalization and the 15 representatives

Put `N=N1×N2=A5^F×A5^F`. Its quotient is

    Q=(A×B)⋊⟨c⟩,   A=B=(F,+),   c(a,b)c⁻¹=(2a,4b),
    θ(a,b,c^k)=(b,a,c^(-k)).

The pinned top-image theorem says that, after an actual τ-compatible automorphism, `H N/N` is `U=A⋊⟨c⟩`; its action is transitive on the first row and has orbits `{0}`, `T1={1,2,4}` and `T2={3,5,6}` on the second. Every such stabilizer has

    |H0|=60^7/3,  v2(|H0|)=14,  v3(|H0|)=6,  v5(|H0|)=7,
    H0=H∩N.                                                (1)

Fix `V4◁A4≤A5`, a quotient `χ:A4→F3`, and `C5≤A5`. Write `V4^J⋊C` for the inverse image of a subspace `C≤F3^J` under the coordinatewise quotient. The normalized possibilities are:

* **Type I:** first-row `C5^F`; second-row `V4^F⋊ker λ`, where `λ` is a nonzero linear combination of the fixed coordinate and the two triple sums. Its projective coefficient `[α:β:γ]∈P²(F3)` is taken modulo interchange of β and γ.
* **Type II:** first-row augmentation subgroup `{x∈C5^F:Σx=0}`; second-row full `A5` at 0 and `V4^(F−{0})⋊ker λ` elsewhere. Here `[β:γ]∈P¹(F3)` is taken modulo interchange.
* **Type III:** first-row diagonal `C5`; second-row `V4` at 0 and six individual full `A5` factors.
* **Type IV:** first-row `V4^F⋊ker(Σ:F3^F→F3)`; second-row `C5^F`.
* **Type V:** first-row diagonal `V4`; second-row `C5` at 0 and six individual full `A5` factors.

In Types I–IV the coherent lift into the one-dimensional C3-shadow quotient is nonzero. In Type V the lift of `c` rotates the diagonal V4 nontrivially. Its two nonzero orientations, and the two nonzero C3-shadow lifts in Types I–IV, are related by a simultaneous odd `C4=N_S5(C5)∩N_S5(A4)` coordinate automorphism. The triple interchange fixes five of the 13 points of `P²(F3)` and two of the four points of `P¹(F3)`. Thus these types give

    (13+5)/2 + (4+2)/2 + 1+1+1 = 15.                      (2)

The rest of the proof justifies exhaustion, existence and exactly this orbit relation.

## Exhausting the original projections

The first-row `H0` projections are H-conjugate. Suppose they are full. Full-coordinate Goursat splitting gives independent twisted A5 strips and a correlated proper residual. Seven is prime, so either seven strips meet the first row once each, or one strip contains the whole first row. In the former case, singleton strips would put a whole Q-orbit product in H; if the strips continue to the second row, their supports give a U-equivariant bijection from the transitive first row to the intransitive `1+3+3` second row, impossible.

In the latter case let b be the number of second-row coordinates in the large strip, a the number of singleton strips, m the total number of full strips, and `e=Σ_S(|S|−2)` over them. Their residual has 5- and 3-valuations `7−m` and `6−m`. A proper A5 projection contributes at most one to either valuation and never to both. Since there are `14−2m−e` proper coordinates, `e≤1`. The large strip contributes `5+b`, so `a≥4+b`; also `a≤7−b`, hence `b≤1`. If b=1, U-invariance forces a=6, but then the large strip and these singletons already contribute seven factors of 3, contrary to (1). If b=0, U-invariance and the same 3-bound force a=4: the singleton set is the fixed coordinate and one triple. The remaining triple is either proper or a single full three-strip. The latter gives `H0=A5^6`, not order `60^7/3`; in the former case its residual has order `1200`, with 5-valuation 2 and 3-valuation 1. Its three conjugate proper projections must all contain 5 and hence none contains 3, a contradiction. Thus the first row is proper throughout.

The information-set theorem applies to each actual selected class. Its Sylow-two subgroup has dimension 14 and an injective selection takes one full V4 image per factor pair. If the first-row proper type is `1,C2,C3` or `S3`, every selected coordinate lies in the second row, so every second-row projection contains V4. Since the first row is 5-free and (1) has 5-valuation 7, every second-row projection contains 5 too and is A5. Injectivity makes all its full strips singleton, whose Q-orbit product lies in H, a contradiction.

If the first-row projection is A4, all seven 5-parts lie in the second row. A Sylow-5 projection into its seven coordinates is an isomorphism, so no full strip meets two second-row coordinates. All second-row full strips are singleton. If a is their number, the first-row C3-shadow has dimension `6−a`. Actual H-lifts normalize each local A4 and act trivially on its C3 quotient, so this shadow is invariant under the pure first-row translation. Since `ord_7(3)=6`, the F3 permutation module of A decomposes into a trivial line and an irreducible six-space, so its invariant dimensions are 0,1,6,7. The U-invariant singleton numbers are `0,1,3,4,6`; hence a=0 or 6, and a=6 contradicts A4 projection. With a=0 the shadow is the augmentation hyperplane, the actual Sylow-two graph vanishes because every first-row C3 coordinate is nonzero, and the second-row projections are C5. Its full second-row C5 subgroup leaves no 5-quotient. The remaining second-row reflection signs form a U-cocycle over F2, killed by odd-order averaging using common τ-paired involutions; these normalize the first-row A4 frames and preserve its augmentation shadow. Its only remaining lift quotient is the one-dimensional first-row C3 quotient. This is Type IV.

If the first-row projection is V4, all seven 5-parts again lie in the second row. Six singleton second-row factors are forced by the 3-valuation, and they are the two triples. The remaining residual R has order 20, projects onto V4 at every first coordinate, and its fixed-output projection contains C5. Its Sylow-5 subgroup is normal, since the number of Sylow-5 subgroups divides 4 and is 1 modulo 5. A Sylow-two subgroup has order 4 and projects injectively to the first row: otherwise its first image has order at most 2, contrary to every local V4 projection.

Choose an order-7 H-lift of the first-row translation by Sylow's theorem; 7 does not divide |H0|. Paired coordinate gauges put the first-row V4 projections in standard position. The lift's local components normalize V4 and lie in A4. Gauges along its seven-cycle remove them, with the closing identity supplied by its seventh power. Set the gauge at the coordinate τ-paired to output 0 equal to 1; the paired gauges then leave that output unchanged, while the other six outputs are full A5 factors. The order-7 lift now acts by pure shift on the first-row V4 coordinates. The order-7 lift acts on the Sylow-two subgroups of R. Their number divides five, so all its orbits have size one and it fixes such a subgroup. Its four-group image is invariant under this shift, but `Aut(V4)` has no element of order 7, so the image is the diagonal V4. Modulo the normal C5 its possible output sign is a linear map `ΔV4→C2`. If this map is nonzero, choose an element with sign 1 and fill the six independent singleton factors with involutions to match the remaining pairs of any actual selected class. Its class square contains the resulting nonidentity tuple, a contradiction. The sign is zero; the order-20 residual is therefore `ΔV4×C5`, giving Type V.

## Five-bearing first row: graphs, modules and lifts

The remaining proper first-row types are C5 and D10. The information-set theorem makes projection of a Sylow-two subgroup onto the entire second row an isomorphism. Consequently every full strip on that row is a singleton. Let A be its U-invariant singleton set, `a=|A|`. Corefreeness gives `a<7`.

Before using a permutation module, eliminate all possible signs. The singleton factors contribute `3^a`; on the `7−a` proper inputs the actual residual C3-shadow has dimension `6−a`. At most one coordinate can be V4 instead of A4, and U-invariance places any such deficient coordinate at 0. A nonzero C3-coordinate kills its column in the actual Sylow-two graph. Varying the first translation component among the 21 selected outside top labels matches the only possible deficient input to every first-row output. Any remaining nonzero block would become a self-loop in one actual matching and give a matched involution. Hence the graph is zero: the first-row `H0` projections are C5.

Here is the graph argument with all selected matchings retained. Remove the independent full singleton factors and call the proper residual R. Its normal 5-subgroup is `W=R∩C5^F`; the quotient embeds in `C2^F×A4^(F−A)`. The kernel of its C3-shadow map is its normal Sylow-two subgroup. The information set makes its projection to the proper second-row `V4^(F−A)` an isomorphism, so it is exactly the graph of a linear map `φ:V4^(F−A)→C2^F`. Conjugation by R is trivial on the C2 output and rotates a V4 input whenever that coordinate has nonzero C3 shadow. Such a rotation has no fixed nonzero functional to F2; hence that entire input column of φ is zero. This proves the preceding column assertion without assuming that the original Sylow-two subgroup was normalized by all H.

If a column remains, its input is the fixed coordinate j=0. Choose a nonzero output block `φ_i` and a nonzero input v with `φ_i(v)=1`. The selected top labels with k=0 match j to each possible first-row coordinate, so choose the matching j↔i. Put v at input j. At every other proper input put zero or a nonzero V4 vector according as its matched output bit of φ(v) is zero or one. Those columns are zero, so this changes no output bit. At each full singleton second-row factor independently choose identity or an involution with the same matched bit. This produces an H0 involution whose two coordinates in each matched pair are either both identity or both nonidentity. All nonidentity A5 involutions are conjugate; for an actual paired outside N-class its square contains exactly these involution support patterns, by the pinned selected-class interface. Thus this nonidentity element lies in that actual class square. The contradiction eliminates the last column, independently of twists in the matching. In the Type IV argument every input column is already active under its C3 shadow, so the same reasoning eliminates all columns directly.

The first-row signs of actual H-lifts are now a 1-cocycle `U→F2^F`. Since |U| is odd, averaging kills it. Realize the correcting vector by a common involution on each τ-pair: at proper partners use `A4∩N_A5(C5)`, and at singleton partners use an involution of the full A5 factor. This whole-folder gauge preserves τ and carries the actual 5-subspace with it. Only now are the lift signs zero and the first-row 5-subgroup `W` invariant under the pure U permutation action.

Its dimension is `7−a`. Since `ord_7(5)=6`, the F5[A] permutation module is the direct sum of the constant line and an irreducible six-space. Thus its invariant dimensions are 0,1,6,7. Combining these with the U-invariant values `a∈{0,1,3,4,6}` leaves precisely `(a,W)=(0,F5^F),(1,augmentation),(6,constants)`, with A respectively `∅,{0},F−{0}`. The complementary C3-shadow is a U-invariant hyperplane on the proper inputs. Every one-dimensional F3 quotient of odd U is trivial, so its defining functional is constant on each U-orbit. This gives 13, 4 and 1 projective lines respectively. For a=0 the line supported only at 0 is precisely the case with V4 projection there; the other lines have A4 projection there.

After the signs vanish, the proper residual lies in `C5^F×A4^(F−A)`. The two factors have coprime orders, so Goursat gives a direct product of its projections. Its second projection contains the full `V4^(F−A)` by the Sylow-two information set, hence is exactly the inverse image of its shadow hyperplane. This proves the displayed H0 forms without a choice of extension. The sign-free actual normalizer quotient is `M5×M3`, with `M3=F3^(F−A)/ker λ≅F3` trivial under U; an H with fixed H0 is a graph of a U-cocycle in that quotient. Let `M5=F5^F/W`. As `5∤|U|`, `H¹(U,M5)=0`. In each of the three cases `F5^F=W⊕F5^A`; the averaging correction can therefore be placed at the first-row coordinates paired with the full second-row singleton factors, preserving τ and all proper endpoint frames. The remaining lift is a homomorphism `η3:U→F3` for the trivial one-dimensional shadow quotient.

The actual inverted top labels are

    I={(x,−4^k x,k):x∈F,k∈Z/3},
    I²∩U={1}∪(U−A).                                       (3)

If η3=0, the normalized graph is zero in both quotient modules, so H contains the pure top c. Equation (3), with identity socle labels, puts c in `Λ²`, contradicting transversality. If η3≠0, at least one proper second-row q-cycle has nonzero C3 cycle sum and order-three holonomy, while every matched first-row cycle has order 1 or 5. At top identity the first-row 5-support would have to lie in the matching image of A; the augmentation code has no word supported at one point, the constant line has no word supported at six, and A is empty in the full-code case. These statements hold for every actual selected matching. Thus Types I–III require exactly nonzero η3. The same cycle test makes the Type IV lift nonzero.

## Dual V4 lift normalization

For Type V the actual base normalizer modulo H0 is `(V4^F/ΔV4)⋊C3` on the first row and C2 on the exceptional output; the other six A5 factors are already in H0. The output C2 image of the odd group U is zero. The diagonal rotation defines `ψ:U→C3`; its remaining `V4^F/ΔV4` lift defect is a 1-cocycle for the combined permutation and ψ-rotation action. Averaging over odd U kills it. Choose a representative of the correcting class that is identity at the first-row coordinate τ-paired to output 0 by multiplying it by a diagonal V4 element. Pair its coordinates through τ: the output-0 coordinate stays identity and the other output coordinates lie in the six full factors. This τ-fixed gauge normalizes H0 and removes the actual defect.

If ψ=0 the normalized H contains pure c, which belongs to `Λ²` by (3). If ψ≠0, its two choices are fused by the simultaneous odd C4 automorphism. At top identity a nontrivial diagonal V4 support meets the matched C5 output and cannot occur in a class square. At any q in `U−A`, each row has one fixed factor; their holonomies have orders 3 and 1 or 5 respectively, so an actual outside involution cannot match them. Thus Type V has exactly the claimed nonzero lift.

## Existence and all normal cuts

Write `χ:A4→C3` and `φ:P→C3`. For Types I–III choose A and W as above and a nonzero U-invariant λ on the proper A4 coordinates. In `S=A5^F⋊P` put

    Y0=W⋊P,
    Y1={(v,c)∈(A5^A×A4^(F−A))⋊C3 : λ(χ(v))=c}.

Their intersection is trivial: a common base has C5 entries in A4 at every proper coordinate, and W has no nonzero word supported on A; the defining equation then kills the top. Their orders multiply to `|S|=21·60^7`. The standard exact-factorization construction therefore gives the stated H0 and nonzero lift.

For Type IV take

    Y0={(v,p)∈A4^F⋊P : Σχ(v)=φ(p)},
    Y1=C5^F⋊C3.

For Type V take

    Y0={(diag b,p): b∈A4, p∈P, χ(b)=φ(p)},
    Y1=(C5 at 0 × A5^(F−{0}))⋊C3.

In each case the intersection is trivial by `A4∩C5=1`, and the two orders multiply to `21·60^7`. These exact factorizations establish actual transversality, including the lift-collision tests above.

For completeness the original normal cuts are strict. Every nontrivial normal subgroup meets N, and its intersection with N is N1, N2 or N. Those meeting one row only are `N1`, `N1⋊A`, `N2`, `N2⋊B`: after quotienting the row, the rest centralizes the other row and lies in its action-kernel axis. The normal subgroups above N correspond to `1,A,B,A×B,Q` in Q: c has distinct eigenvalues 2 and 4, and a normal subgroup with nontrivial C3 image contains both commutator axes. The top-only proper cuts have selected-image sizes `21,21,21,3` and indices `7,7,1,1`.

For Types I–III the four row-retaining stabilizer indices, in the order `N1,N1⋊A,N2,N2⋊B`, are

    21·5^(7−a), 21·5^(7−a), 7·60^7/5^(7−a), 60^7/5^(7−a).

For Type IV they are `7·12^7,7·12^7,21·5^7,3·5^7`; for Type V they are `84,84,7·60^7/4,60^7/4`. Each selected image has size `21·60^7`, strictly larger. Thus the original normal-subloop criterion gives simplicity. The socle action is faithful, neither socle row lies in H0, and every nontrivial normal subgroup meets N, giving corefreeness. The full section generates G; H is nontrivial; and `H<N⋊U<G` makes the canonical action imprimitive. The pinned simple-Moufang primitivity theorem gives properness.

## Exact isomorphism orbits

A canonical-folder isomorphism preserves the set of two minimal socle rows, τ and the full simple factors of H0. Since `C_G(N)=1`, it is determined by its action on N: two extensions agreeing there differ by an element centralizing N at every group element. Thus the subsequent coordinate analysis accounts for top-lift corrections as well; they cannot be chosen independently of the socle action. Its induced automorphism of Q commutes with θ. Once the pinned top-image normalization returns its image to U by a θ-fixed inner automorphism, it cannot interchange the rows: `U∩Q′` is the first eigenline A, whereas a row swap sends it to B, and inner Q-conjugation preserves both eigenlines.

An automorphism of Q preserving A acts on `Q′=F7²` by `(x,y)↦(ux,vy)` and sends c to `(r,s,c)`. Commutation with θ gives `u=v` and `s=−4r`; preservation of U forces `s=r=0`. Hence the remaining top automorphisms are common nonzero scalings. Their corresponding row permutations, constrained by τ and the fixed c action, are `x↦ux`. They fix 0 and either preserve the two triples or interchange them; both possibilities occur.

At each τ-pair a folder isomorphism has the same local S5 automorphism on both factors. Its parity is constant on the Q-orbit. At proper C5/A4 pairs the common frame normalizer is C4; its action on A4/V4 is the parity sign. At a full singleton partner the additional C5-normalizer freedom can change a 5-lift by a coboundary but cannot independently change any proper C3 coordinate. Preservation of the augmentation or constant W forces its local F5 multipliers to be common; for full W they are invisible in the quotient. In the dual diagonal-V4 case, preserving that diagonal forces the same GL2(2) action on each V4 factor, and the exceptional C5 coordinate restricts the common action as above. Thus no local gauge changes the projective shadow line beyond common F3* scaling, and a common odd C4 element identifies the two nonzero lifts. Conversely the common scalings and this C4 element are actual τ-compatible folder automorphisms. The only remaining action on the shadow coordinates is the triple interchange, proving the orbit count (2) and distinguishing all five structural types by their intrinsic projections and singleton counts.

### Why no further coefficient action is hidden in the gauges

Identify `Aut(N)` with local S5 automorphisms followed by a factor permutation. After the previously established common factor permutation, write the local maps as d_x on row one. Commutation with τ gives the same d_x on its paired row-two factor. For every pure top element q, conjugating its factor-permutation action by these maps has local correction `d_x d_(q⁻¹x)⁻¹`. Such a correction belongs to G only when it is inner at every coordinate. Thus the parities of d_x and d_(q⁻¹x) agree. Since the full Q action is transitive on each row, all these parities are one common value, even though U is intransitive on row two. This uses the automorphism of the full canonical G, not just a normalizer of H.

For a proper pair the C5 frame is a regular five-cycle and the A4 frame is a point stabilizer; the V4-deficient case has the same S5 normalizer as that A4. The normalizer F20 of the five-cycle acts transitively on the five points, and its point stabilizer is C4. Hence their common normalizer is exactly this C4. Its odd elements invert the C3 quotient and its even elements act trivially. All proper C3 coordinates therefore acquire the same scalar ±1. At a singleton partner there is no proper C3 coordinate at all; the extra F20 freedom cannot act on coefficients at another coordinate. The factor permutation already found fixes 0 and can only interchange the two triples. These facts prove necessity of precisely the displayed action on the projective functional.

This necessity argument does not have to assert that every allowed local d_x independently preserves the top lifts: allowing extra local maps would only enlarge a containing action, and that containing action is already the claimed common scalar and triple interchange. Sufficiency is explicit: a common coordinate C4 map commutes with all pure top permutations, preserves the 5-code and the shadow hyperplane, and interchanges the two nonzero lift values. A common field-coordinate scaling realizes the triple interchange. Once the lift normalizations above are imposed, no other lift parameter remains. The base normalizer quotients are the stated `M5×M3` or the dual `(V4^F/ΔV4)⋊C3`, so any lift correction has already been removed or recorded there. Since restriction to N determines the whole group automorphism, there is no additional automorphism acting trivially on N that could fuse the functional orbits. This proves both directions of the isomorphism criterion without assuming that all local normalizers act independently.

## Evidence and limits

This is an analytic classification under the pinned inputs, not a computational census. The construction and top-image inputs retain their exact review pins. At source [the source revision](https://github.com/Mira-Cult/math-wip/commit/45c50ef70aaab14d396178a5381160f8f95b8de7), independent reviewer contributor 1 accepted the complete mathematical argument conditional on the pinned interfaces. Two other independent reviewers, contributor 2 and contributor 3, checked portions of the arithmetic, projection bounds, constructions and top cuts but explicitly left the selected-matching graph and full gauge orbit calculation unverified; their reviews were incomplete, not acceptances or demonstrated rejections. The expanded arguments above respond to those exact review limits. At expanded exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/430f8e6ec8bb92e17b6fd61a916812f1d3b29668), contributor 1 independently accepted the complete proof and explicitly checked both additions. contributor 2 accepted the mathematical derivation conditional on its inputs, checking the two previously unresolved steps in addition to the earlier module, orbit, construction and cut calculations. contributor 3 accepted only the expanded graph-elimination and coefficient-gauge interfaces, explicitly not the full manuscript. These distinct review scopes are retained; the last review is not counted as a third full-source acceptance. No computation or new external-source audit was claimed by those reviewers. The reviewers did not independently reprove every upstream interface or audit all external provenance. These are model mathematical reviews, not formal GitHub approvals or human/formal certification. No permanent claim ID is allocated and C0010 remains partial.
