# The remaining finite linear factor pairs

Independently reviewed continuation of [0323:C0010](../foundations/research-C0010.md), conditional on the stated inputs. Let Q be a finite simple proper left Bol loop, M=Mlt(Q) almost simple with socle S, G=LMlt(Q), I=M_1 and H=G∩I. Suppose the actual pair (G,I), in either orientation, tightly contains a pair in Li–Wang–Xia linear Table1.1 rows12–15. Under the stated inputs, no such Q exists. The four rows have full socles PSL4(3), PSL6(3), PSL12(2), PSL12(4); this statement concerns their displayed proper-factor pairs, not every canonical group or all even-dimensional linear socles.

The primary source is Li–Wang–Xia, *Factorizations of almost simple linear groups*, [arXiv:2106.03109v2](https://arxiv.org/html/2106.03109v2), Theorem1.2/Table1.1, Lemmas5.4–5.7 and6.1. The coordinator freshly inspected the theorem, table, common models and proofs. Lemmas5.4–5.5 are source-reported Magma results, not computations rerun here. Lemma5.5 prints `5^3` in its description of Y; its definition as the six-dimensional ternary vector stabilizer, Table1.1 and Table6.1 give `3^5`, used here. Lemma5.6's proof prints PSL6 where its statement and ambient dimension specify twelve; we use the stated model. Tight containment includes actual containment and equality of solvable residuals. Apply the common source automorphism to both factors, and retain all permitted actual overgroups.

Use the canonical definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. Original outside marks Λ are G-invariant involutions, contain τ, satisfy |Λ|=[G:H]=[M:I] and H∩Λ²=1, and τΛ generates G. No quotient folder is asserted below. In particular some mark acts nontrivially on any characteristic nonabelian simple component or quotient on which G has nontrivial inner action: otherwise τ and τΛ would all centralize that section.

## Ternary vector-parabolic capacities

For S=PSL_n(3), n=4 or6, the source vector stabilizer Y=3^(n−1):SL_(n−1)(3) is also the full projective point stabilizer in S: the determinant quotient of order2 is canceled by the ambient scalar center. If G tightly contains Y, its characteristic residual is Y, and G normalizes Y. No ambient graph automorphism normalizes this point parabolic, since it exchanges point and hyperplane parabolic classes. There is no field automorphism over F3.

The [reviewed original-fiber interface](even-linear-extension-parabolic.md#original-marked-fibers-and-a-weighted-capacity-bound), source `d95f900af71ff43fcc5486345a0c24f7eb47f6da`, retains the natural-module proof at `472e2653976598a9666142e7f64e07a4601c61e8`. It gives U=O3(G)=3^(n−1), C_G(U)=U, faithful G/U≤GL_(n−1)(3), and an action of the formal inversion extension on U. Two marks with the same restriction A differ by u∈U with (1+A)u=0. Thus a restriction whose negative eigenspace has dimension r has at most3^r actual mark lifts. This is a bound on the original marks, independent of the opposing factor, without assuming an affine realization of τ.

For dimension3 the four involution classes, including identity, have sizes1,117,117,1 for r=0,1,2,3. Consequently

    |Λ|≤1+117·3+117·9+27=1432.                       (1)

For dimension5 it suffices to use the coarser bound

    |Λ|≤3^5 j(GL5(3))=3^5·1,783,784.                 (2)

Here j counts elements squaring to identity. In odd characteristic the exact count is the sum of |GL_d(3)|/(|GL_r(3)||GL_(d−r)(3)|), for r=0,...,d. The certificate below verifies both numerical evaluations.

## PSL4(3): all three pairs, both orientations

Write Y=3³:SL3(3) and let X be S5, 4×A5 or 2⁴:A5. Lemma5.4 gives X∩Y respectively C3, S3 or SL2(3). These model intersections are contained in the actual H; they are not asserted to equal H.

First suppose G tightly contains X. In the first two cases A=A5=G^(∞) is characteristic, and every element of order3 in X belongs to A. In the third case P=2⁴:A5 is perfect, P=G^(∞), and E=O2(P)=2⁴ is characteristic; P/E=A5. The action on E is nontrivial and faithful, and an order5 element is irreducible on its four-dimensional binary module, so [E,A5]=E.

At least one actual mark has a nontrivial involutory action on A or P/E. The two involution classes of Aut(A5)=S5, transpositions and double transpositions, are each single A5-orbits and each has a 3-cycle in its square. For example use (12),(23), or (12)(45),(23)(45). Hence the product of two A- or P-conjugates of that same mark lies literally in A or P, as a commutator, and has order3 in the A5 quotient. In the first two cases it is an actual order3 element of A. The single A5 order3 class meets H, contradicting H∩Λ²=1.

In the third case a suitable 2-power of the product has order exactly3. All powers of a product of two marks remain in Λ²: if d=lm, with l,m marks and conjugation a^g=g^(-1)ag, then

    d^(2r)=l l^(d^r),     d^(2r+1)=l m^(d^r).

The order3 subgroups of P are conjugate. Their images are conjugate in A5; within the inverse image E:C3 of a fixed image, Schur–Zassenhaus conjugates all complements to E. Taking powers supplies either nonidentity element. Since the actual intersection SL2(3) contains an order3 element, an actual element of Λ² is conjugate into H, again impossible.

Now suppose G tightly contains Y and I tightly contains X. Set I0=I∩S. Since S is transitive in the actual primitive M-action, |Λ|=[S:I0]. We bound I0 using a different, auxiliary action: the faithful action of S on its40 projective points. The model equality S=XY makes X transitive there.

For X=S5 or4×A5, the characteristic residual A=I^(∞)=A5 has equally sized orbits, with their number dividing [X:A]=2 or4. One orbit is impossible because40 does not divide60. Two orbits have size20 and stabilizer C3, with commuting permutation group N_A(C3)/C3=C2 on each. Their total centralizer embeds in C2 wr S2, of order8. Four orbits have size10 and stabilizer S3, self-normalizing in A5, so their centralizer embeds in S4, of order24. This explicitly includes A5's order6 subgroups. Therefore |C_S(A)|≤24 and

    |I0|≤|C_S(A)||Aut(A)|≤24·120=2880.               (3)

For X=2⁴:A5, its characteristic E=O2(I^(∞)) is normalized by I. The [intrinsic extraspecial lift and projective centralizer argument](../odd-completion/nonbruck-almost-simple-radical-bridge.md#actual-centralizer-of-u), independently reviewed at `8f22211fbd9d0e3c48347ecf65a037155ed428dd`, applies to this actual E: a nontrivial order5 action is irreducible, the inverse image in SL4(3) is extraspecial of minus type, its group algebra with central involution −1 is Mat4(F3), and C_S(E)=E. Its hypotheses concern this embedded E and its order5 normalizer, not the solvability of the earlier application. Conjugation preserves the extraspecial square form, so N_S(E)/E embeds in O4^−(2)≅S5. Thus |I0|≤16·120=1920. Combining this with (3),

    |Λ|≥6,065,280/2880=2106>1432,

contrary to (1). This excludes every row12 orientation and actual overgroup under the retained inputs.

## PSL6(3): both PSL2(13)/parabolic orientations

Let X=PSL2(13) and Y=3⁵:SL5(3). Lemma5.5 gives S=XY and X∩Y=C3, so X is transitive on the364 projective points. A projective linear transformation centralizing X acts faithfully on these points and embeds in the commuting permutation group N_X(C3)/C3, of order4. Indeed C3 is in a split torus C6 with dihedral normalizer of order12. Adding the ambient graph quotient of order2 gives

    |C_Aut(S)(X)|≤8,
    |N_Aut(S)(X)|≤8|Aut(X)|=8·2184=17472.            (4)

If G tightly contains Y, then I^(∞)=X and I normalizes X. Hence |H∩Y|≤17472 and

    |Λ|≥3⁵|SL5(3)|/17472
        =3⁵·237,783,237,120/17472
        >3⁵·1,783,784,

contrary to (2). This accounts for the entire ambient centralizer; it does not assume that the projective X lifts to a faithful six-dimensional linear X-module.

For the reverse orientation X=G^(∞) is characteristic. Aut(X)=PGL2(13) has two nontrivial involution classes, of sizes91 and78. Each is a single X-orbit: the inner class already has size91 in X, while an outer involution centralizes itself outside X, preventing an orbit split. The complete CTblLib tables and normal fusion show that each class square meets the unique order3 class of X: the two structure constants at the order3 class are both6.

If an actual mark λ has nontrivial restriction to X, choose x∈X such that the restrictions of λ and λ^x have product in that order3 class. Their actual product lies in X as a commutator. Since X is centerless, restriction X→Aut(X) is injective, so the product itself has order3. The single order3 class meets the actual H via X∩Y=C3, giving H∩Λ²≠1 after X-conjugation. Therefore every mark would centralize X, contradicting generation as explained above. No restriction-kernel hypothesis is needed in this orientation.

## Degree twelve extension-field antiflag pairs

Let q∈{2,4}, R=q², S=PSL12(q), X=G2(R) and L=1⊕SL11(q). Lemmas5.6–5.7 give the actual common extension-field model for rows14–15, including their field or graph-field extensions. The covering residual intersection is SL2(R): within the extension-field SL6(R) it is the G2(R)/SL5(R) antiflag intersection. Projective intersections can gain ambient scalar representatives, so we do not identify them with this covering intersection.

Suppose G tightly contains the G2-side, so X=G^(∞). Since I normalizes its residual L, an element of I∩X uniquely lifts to its genuine G2(R) matrix preserving L's fixed F_q-line and complementary hyperplane. Its eigenvalue on that line lies in F_q×, and the kernel is contained in the covering intersection SL2(R). Thus

    |I∩X|≤(q−1)|SL2(R)|,
    |Λ|≥R⁵(R⁶−1)/(q−1).                             (5)

The [reviewed restricted-scalar commutant](g2-vector-parabolic-capacity.md), source `4169b5a5219bf8872dcf8723a2dbea6e07ddb111`, applied over F2, is exactly F_R. Perfectness removes projective scalar commutator characters. Consequently even an F_q-semilinear centralizer must be an F_R scalar, leaving at most R×/F_q× of order q+1 projectively. The ambient graph coset at most doubles it, so |C_G(X)|≤2(q+1).

The [reviewed G2 class count](g2-antiflag-pair.md), source `dc80188927778f152b0ecdb758e9b3eb76040942`, gives

    j(Aut X)≤1+(R²+1)(R⁶−1)+R³(R³+1)(R+1).

Each original restriction fiber has size at most2(q+1). Comparing this upper bound with (5) gives

    q=2:       4,193,280 > 542,496;
    q=4:   5,864,061,665,280 > 45,970,265,600.

These strict inequalities exclude the G2-canonical side. They retain the G2 involution/field and minimum-degree inputs of the cited proofs.

For the reverse orientation L=G^(∞) is simple and centerless because gcd(11,q−1)=1. At q=2 its ambient centralizer is trivial. A projective linear centralizer consists of block scalars, which vanish over F2; no graph label centralizes L because its restriction is the nontrivial graph outer label of L. Thus restriction embeds G into Aut(L), containing L, and the [reviewed odd-dimensional canonical-overgroup exclusion](../factor-permutation/radical-free-three-dimensional-linear-unitary.md), source `114ce1b011fd47589eb762ed7cd5492a190002d8`, applies.

At q=4 the ambient centralizer is C3, not trivial: diag(a,bI11) modulo common scalars has ratio a/b∈F4× in PGL12(4). The determinant condition only removes it inside PSL12(4). Field and graph labels restrict to distinct nontrivial outer labels of L and cannot centralize it. Hence original restriction fibers have size at most3; a quotient-folder argument would not be justified.

The actual H contains a rank4 L-involution. The reviewed G2 antiflag proof identifies the covering SL2(16) intersection as the long-root subgroup by its nondegenerate fixed plane and G2-transitivity on ordered symplectic pairs. Its root involution has rank2 over F16, hence rank4 over F4. Removing the fixed antiflag line leaves the same rank on L's eleven-dimensional module. This uses the common source embedding, not merely the abstract intersection order.

Every outer involution class of Aut(L) has this rank4 class in its L-class square, by [the reviewed odd-linear descent](../primitive-completion/radical-free-odd-linear-inversion.md#one-involution-class-in-each-pure-outer-coset), exact source `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`. The scalar center and diagonal quotient of L are trivial here. Each inner involution of rank r≥2 also has a rank4 product of two conjugates. For r=2 take disjoint two-block supports. For r=3 retain one common block and place the two remaining blocks on disjoint supports, using ten dimensions. For r=4 or5 keep the support, changing four block coefficients from1 to a fixed a∈F4 minus {0,1}; the unchanged blocks cancel. These commuting involutions have the same rank r, hence are SL11(4)-conjugate: an unused one-block allows arbitrary determinant correction. Each product has rank4. Taking L-conjugates of an actual mark realizes the product literally in centerless L. It then collides with the class in H.

Thus the only permitted restrictions are identity and inner transvections, whose number is T=(4¹¹−1)(4¹⁰−1)/3, and

    |Λ|≤3(1+T).                                      (6)

On the other hand I normalizes X=G2(16). Its ambient centralizer has size at most10 by the same commutant argument, and Out(X)=C4, so |N_Aut(S)(X)/X|≤40. The eigenvalue argument used in (5) gives |X∩L|≤3|SL2(16)|=12,240. Therefore |H∩L|≤489,600. As |SL11(4)| has 2-part4⁵⁵ and489,600<4¹⁰,

    |Λ|≥|SL11(4)|/489,600>4⁴⁵>3(1+T),

contradicting (6). This closes the actual scalar-kernel case directly.

## Evidence and review boundary

The standalone [finite certificate](../code/verify_even_linear_finite_pairs.g) requires GAP4.15.1 and CTblLib1.3.11. It verifies the two GL involution evaluations and capacities, the complete L2(13)/L2(13).2 involution/order3 data, normal fusion and positive class-square coefficients, and the two G2 and reverse scalar-kernel inequalities. It makes no network request and does not execute another research source. Character-table completeness/correctness, the primary actual-factor classifications and all prior canonical inputs remain external dependencies. The coordinator read and ran this source; its finite assertions do not prove the normalizer or marked-set deductions. The independent exact-source reviews below retain these external dependencies. No new permanent claim IDs are allocated; C0010 and the complete operation classification remain open.


Three independent mathematical/code reviewers accepted exact source `eb36b8f4e3bca71b1123eb5b0b4a6820088c404a`: contributor 1, contributor 2 and contributor 3. Each checked both actual orientations of all four rows, the original ternary fibers, A5 orbit centralizers including the order6 stabilizers, genuine commutator/power transfer, the intrinsic extraspecial-minus interface, PSL2(13) class fusion/squares, and the degree-twelve rank4 witnesses with the nontrivial C3 restriction kernel. Each extracted, read and independently ran the committed GAP certificate with GAP4.15.1/CTblLib1.3.11; all assertions passed.

The paired-simple and presentations reviewers freshly inspected LWX v2 Table1.1 and/or Lemmas5.4–5.7, confirming the two recorded printing discrepancies. The S5 reviewer retained the recorded primary-source inspection. None reran the source's Magma classifications, reconstructed CTblLib tables, or reproved all upstream canonical and commutant results. Acceptance is conditional on those precisely retained inputs and concerns rows12–15 only. These are model mathematical/code reviews, not formal GitHub approvals or completion of C0010.
