# Extension-field antiflag pairs in characteristics two and four

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source mathematical review recorded below. Let Q be a finite simple proper left Bol loop with almost-simple full multiplication group M, socle S=PSL_(2m)(q), q∈{2,4}, and actual factors G=LMlt(Q), I=M_1, H=G∩I. Suppose the actual pair, in either orientation, tightly contains one of the extension-linear or extension-symplectic antiflag pairs in Li–Wang–Xia Table1.1 rows4–7. Under the stated inputs, no such Q exists. The proof covers every permitted m and all listed outer extensions, retaining the small endpoints. It does not cover their different G2 antiflag pair, odd-characteristic vector SL2 components or all linear full socles.

The primary actual-factor source is Li–Wang–Xia, *Factorizations of almost simple linear groups*, [arXiv:2106.03109v2](https://arxiv.org/html/2106.03109v2), Theorem1.2/Table1.1 rows4–7, definition of tight containment, and Lemmas4.6–4.9, printed pp.6–7. The coordinator freshly inspected their statements and common-model proofs. Tightness is actual containment and equality of solvable residuals. Put R=q². Denote the extension component by X and the antiflag component by Y. Their perfect residuals are the projective image of SL_m(R), or Sp_m(R) for even m, and the genuine 1⊕SL_(2m−1)(q), respectively. The source's outer groups may be larger; they are not replaced by these residuals. In the covering common module, with R-basis v1,…,vm and λ∈R\F_q, the antiflag consists of v1 and

    W=⟨λv1,v2,λv2,…,vm,λvm⟩_(F_q).

The intersections of the residual groups contain the natural SL_(m−1)(R) or Sp_(m−2)(R), respectively. Projecting these actual subgroups gives subgroups of H in either orientation. A common source automorphism transports the whole pair, never only one factor.

Use the definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. The original marks Λ are G-invariant outside involutions, contain τ, satisfy H∩Λ²=1 and |Λ|=[G:H], and generate G through τΛ. The [reviewed moved-transvection lemma](transvection-products-classical-intersections.md), source `bc837277fd94e4a4184c2843319fbff86331aa4a`, and the [odd-central component obstruction](marked-involution-vector-obstruction.md), source `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, will always be applied to this original folder.

## A rank-two square in every odd-dimensional linear automorphism class

Let T=PSL_d(s), d≥5 odd, s any even prime power. For every nonidentity involutory automorphism α of T, the square of its T-class contains the T-class of a rank-two unipotent involution. Here the class is interpreted in the external semidirect product even when α is inner; products of its conjugates belong to T.

For inner α, lift its inducing involution uniquely to an SL_d(s)-involution u=1+N; the scalar center has odd order. If rank N=1, two independent commuting transvections give rank2 and are both SL-conjugate to u. If rank N≥2, choose v with Nv≠0, hence v∉im N, and a functional φ with φ(v)=φ(Nv)=0 but φN≠0. Such φ exists by taking a vector in im N outside ⟨Nv⟩ and specifying its value independently from v,Nv. Put t=1+vφ. The transvections t and t^u have independent directions v,v+Nv and independent covectors φ,φ+φN; both cross pairings vanish. Their product is an involution of rank2: relative to directions v,Nv and covectors φ,φN its nonzero part has coefficient matrix [[0,1],[1,1]]. This product also equals a product of two conjugates of u. The rank-two GL class is one SL class because d−4≥1 provides a determinant-surjective centralizer on a Jordan1-block.

For outer α, retain exactly the [odd-linear outer-class proof](../primitive-completion/radical-free-odd-linear-inversion.md#one-involution-class-in-each-pure-outer-coset), independently reviewed at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`, with the overgroup continuation at `114ce1b011fd47589eb762ed7cd5492a190002d8`. It proves one T-class of involutions in each standard graph, field or graph-field coset by symmetric forms, determinant-one Hilbert90 and Hermitian descent, including odd-central correction. If V has columns e1+e2,e3+e4, the rank-two involution u2=1+VVᵀ is defined over F2 and fixed by all these standard automorphisms. Thus α and αu2 are in the same T-class and their product is u2. The odd diagonal quotient D is handled there by ker(1+α)=im(1−α), so any involutory diagonal twist is transported into a standard coset by an actual PGL automorphism, which preserves the rank-two class. This imports the class-square deduction, not an assertion that different diagonal cosets are one T-class. The coordinator reread the exact descent proof and common representative.

Consequently, if the actual characteristic subgroup L of G is SL_d(s), its odd center permits the same actual rank-two collision. Choose a mark acting nontrivially modulo Z(L); one exists by perfectness and generation. Lift the two T-conjugates to L-conjugates of that same actual mark. Their product x∈L projects to the rank-two involution. The odd-power identity from the reviewed component lemma makes x^|Z(L)| an actual involution still in Λ². Its unique involution lift has rank2, so every genuine rank-two SL_d(s)-class lies in Λ². No quotient loop is formed.

## Linear antiflag component on the canonical side

Suppose G tightly contains the Y side. For linear extensions m≥3, or symplectic extensions with even m≥4, L=G^(∞)=SL_(2m−1)(q) is the actual embedded 1⊕SL group, with odd center. A single transvection in SL_(m−1)(R), or in Sp_(m−2)(R), has rank2 over F_q. Its actual image belongs to H∩L. The preceding rank-two square theorem gives a collision and excludes every such reverse orientation. The m=2 endpoint is treated below. The argument works with the original subgroup inclusion, not equality of H with the displayed perfect intersection.

## Extension component on the canonical side: dimensions other than four

Suppose G tightly contains the X side. Its perfect residual L is the indicated natural group modulo its odd scalar kernel and is characteristic. For SL_m(R) with m≥5, the reviewed moved-transvection lemma gives a nonidentity actual product represented by g with rank_R(g−1)≤2. Its fixed space has dimension at least m−2>2≥dim im(g−1). Choose a fixed vector v outside that image and a functional φ annihilating the image with φ(v)=1. Then φg=φ, so g fixes the nonincident vector/hyperplane pair (v,kerφ). A determinant-one conjugator carries this pair to the source's R-antiflag: adjust any GL conjugator on the complementary (m−1)-space to correct its determinant. Hence a conjugate of the actual product lies in the image of SL_(m−1)(R)≤H, contradiction.

For m=3, every actual involution of L lifts uniquely through the odd scalar kernel to an SL3(R)-involution of rank1. Every such class meets the natural SL2(R) intersection; GL-to-SL conjugacy again uses the Jordan1-block. The reviewed odd-central component lemma therefore excludes this parameter directly.

For Sp_m(R) with even m≥6, the same marked product has displacement rank at most2. Its fixed space contains a nondegenerate symplectic plane by the reviewed dimension/radical argument. Conjugating into its pointwise stabilizer puts it in the actual Sp_(m−2)(R)≤H. The automorphism-preservation input is the reviewed Steinberg interface; rank at least three has no exceptional graph automorphism. The m=2 symplectic case coincides with SL2(R). It remains to treat m=4 and m=2.

## Extension dimension four

Here S=SL8(q), since gcd(8,q−1)=1. The components SL4(R) and Sp4(R) are faithful and centerless. In the linear or semilinear ambient automorphism part, projective centralization lifts to honest centralization of these perfect groups: a scalar commutator character is trivial. Their F2-algebra generated by natural transvections is Mat4(R). For SL this follows from elementary matrix products with arbitrary R-parameters; for Sp it is the reviewed transvection-algebra calculation at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, which also works over F2 because every parameter in R occurs. Thus an F2-linear centralizer is an R-scalar. In particular a nontrivial base-field semilinear map cannot centralize the component, as it would have to commute with the F_q-scalars. The projective scalar centralizer has order at most (R−1)/(q−1)=q+1; the ambient graph quotient can add at most one coset. Therefore

    |C_G(L)|≤2(q+1),                                 (1)

and every original restriction fiber has at most that size. This permits a graph centralizer rather than assuming one absent.

Because I normalizes its perfect residual SL7(q), H∩L preserves the unique F_q-line and complementary hyperplane fixed by that residual. The unique R-hyperplane contained in W is U=⟨v2,v3,v4⟩_R (also W∩λW). Thus an R-linear element of H∩SL4(R) preserves U and acts on v1 by c∈F_q×. For each c, its action on U has prescribed determinant c⁻¹, giving

    |H∩SL4(R)|≤(q−1)|SL3(R)|,
    |Λ|≥R³(R⁴−1)/(q−1)>q¹³.                        (2)

A nonidentity inner involutory automorphism of SL4(R) has inducing matrix u=1+N, N²=0. Choose Nv≠0 and a nonzero φ annihilating im N+⟨v⟩, possible as its dimension is at most3. With t=1+vφ, a product of two conjugates of u is the nonidentity transvection 1+(Nv)φ. This fixes an antiflag and gives the actual H-collision. Nonalternating graph restrictions likewise have a transvection in their class square: for γ the inverse transpose and v=(1,1,0,0), u=1+vvᵀ is a rank-one involution, and its symmetric form remains nonalternating. The determinant-one congruence at reviewed source `1ca7a62efde571600a531c8e352151faca2ab626` makes γu conjugate to γ.

For field or graph-field restrictions, the same reviewed even-linear descent gives one class in each standard semilinear coset; here gcd(4,R−1)=1, so no diagonal label occurs. Write σ:z↦z^q. In an antidiagonal symplectic basis the graph γ fixes the root group x_(1,4)(a) parameterwise in characteristic two. Choose a+a^q=1. For α=σ or γσ and t=x_(1,4)(a), the actual product α(t)⁻¹t=x_(1,4)(1) is a transvection. Its class-square inclusion is literal, and descent transfers it to every restriction in those cosets. Thus the only possible nonidentity surviving restrictions are the alternating graph involutions. Their centralizer is Sp4(R), so their number is R²(R³−1), by the same reviewed form classification. With identity and (1),

    |Λ|≤2(q+1)[1+R²(R³−1)]<2(q+1)q¹⁰<q¹³,          (3)

since q³>2(q+1) for q≥2. This contradicts (2) and closes the linear m=4 cases.

For Sp4(R), R=4 or16 has even extension degree over F2. The [reviewed rank-four collision/count](sp4-antiflag-capacity.md), source `8ce9863ba93a03014deb4afa813a212b44d9e4fc`, excludes every nontrivial field restriction and leaves at most R⁴ inner restrictions including identity. There is no involutory exceptional graph-field label at these even degrees. Retain (1). The ordered nondegenerate line-pair stabilizer over R bounds H∩L by (R−1)|Sp2(R)|, even allowing the larger R-scalar factor. Hence

    |Λ|≥R³(R⁴−1)/(R−1),       |Λ|≤2(q+1)R⁴.

The exact comparisons are 5440>1536 for (q,R)=(2,4), and 17895424>655360 for (4,16). They are direct order arithmetic, with no finite group census. This closes both symplectic m=4 endpoints.

## Extension dimension two: the PSL4(4) endpoint

The q=2 endpoint has full socle A8 and is already excluded by the exact full-action/minimum-order inputs pinned in the [reviewed antiflag proof](transvection-products-classical-intersections.md). Suppose q=4. Put X=SL2(16)=PSL2(16), of order4080, and Y=SL3(4), of order60480. The source Lemmas4.6–4.7 give their actual common-model intersection X∩Y=1. Since S=SL4(4) has trivial scalar center, these are genuine matrix intersections.

We first record the needed normalizers. The F2-algebra generated by X is Mat2(F16), so its F4-linear centralizer is F16× and its projective linear centralizer is C5. Perfectness removes projective commutator characters, and the same algebra argument rules out any nontrivial base-field label in the projective semilinear centralizer. The remaining ambient graph quotient has order2. Thus C_Aut(S)(X) has order dividing10. Restriction to Aut(X), whose outer group is C4, yields

    |N_Aut(S)(X)/X| divides40.                        (4)

This is divisibility, not just an order upper bound: the linear centralizer is C5, its graph quotient has order at most2, and the restriction image modulo X is a subgroup of C4.

For Y in the 1⊕3 embedding, a linear centralizer is block scalar. In SL4(4), its determinant condition leaves exactly diag(1,cI3), c∈F4×, of order3. A nontrivial ambient field or graph label induces the corresponding nontrivial outer label on PSL3(4), which cannot be cancelled by an inner-diagonal transformation by the reviewed Steinberg decomposition. Hence

    C_Aut(S)(Y)=Z(Y)≅C3.                             (5)

The full ambient automorphism decomposition and actual natural models are the previously cited inputs; neither equality assumes the entire actual factor is almost simple.

First take G on the X side. Since I normalizes Y, H∩X preserves its unique fixed F4-line and complementary hyperplane. Its action on that line maps it into F4×; the kernel fixes the vector and hyperplane and lies in X∩Y=1. Thus H∩X is 1 or C3. Some mark restricts nontrivially to X by generation. In Aut(X)=X:C4, the possible nonidentity involutory restrictions are inner involutions (one X-class of size255) or the half-field class (one X-class of size68, with centralizer PSL2(4) of order60). The finite-field descent and standard automorphism inputs are retained from the reviewed PSL2 proof at `47b07688a82d3df93f537946fe0780112200383b`.

Both restriction classes have an order-three element in their square. In the fixed PSL2(4), choose u of order3 and an involution w inverting u. Then w,wu are conjugate inner involutions. If σ is the half-field automorphism, wσ,wσu are involutions in its unique X-class, with product u; σu alone would not be an involution. The witnesses lift to X-conjugates of the same actual mark. Their product lies in X, because the mark normalizes X, and the restriction to centerless X identifies it with the order-three witness. PSL2(16) has one order-three class, since its split torus elements of order3 are paired by inversion. Consequently H∩X=C3 would collide with Λ². Therefore H∩X=1, and

    |Λ|≥4080,           |Λ|≤10(1+255+68)=3240,         (6)

contradiction.

Finally take G on the Y side and I on the X side. Equation (4), I≤N_Aut(S)(X), and X∩Y=1 show that H∩Y injects into a group of order dividing40. All genuine involutions in SL3(4) form one class, with odd center3. If H∩Y had even order, it would meet that class, and the reviewed odd-central component lemma would give a collision. Thus |H∩Y| is odd and divides40, so is at most5. Consequently |Λ|≥60480/5=12096.

For an upper bound use (5). Automorphisms of perfect Y inject into Aut(Y/Z(Y))=Aut(PSL3(4)). The complete order-at-most-two count there is

    1+315+3·336+3·120+280=1964.

Here315 is the sole inner involution class; the three graph labels each have centralizer Sp2(4), order60, in PSL3(4), of order20160; the three field labels each have centralizer PSL3(2), order168; and the graph-field label has centralizer PSU3(2), order72. The odd-linear descent and diagonal-label calculation at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede` give these complete classes. In particular the graph-field centralizer is the projective fixed group, not SU3(2) before its center3 is removed. The inner class count315 follows from its rank-one Jordan centralizer. With original restriction fibers at most3,

    |Λ|≤3·1964=5892<12096.                            (7)

This excludes the reverse endpoint as well. No assertion of faithful restriction, quotient-folder transversality, or a fixed-subfield element automatically lying in a class square is used.

## Evidence and scope

The coordinator read the cited exact reviewed odd/even-linear descent proofs and the source's actual extension-antiflag models. The new deductions are the inner rank-two witness, its actual odd-central transfer, the larger scalar-centralizer control, and the endpoint assembly. A producer ran an exploratory GAP4.15.1/CTblLib control on L3(4).D12 and obtained aggregate class sizes1,315,280,360,1008; that unversioned control is corroboration only and is not used as the proof of (7), whose source-backed class calculation is given above. No new executable certificate is needed for the displayed order arithmetic. Independent exact-source mathematical review is recorded below; repository integrity alone does not establish these results.

## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted this entire assembly at exact source `c6b16d21dc2aa8b0332e0d77eced0159a33ff832`: contributor 1, contributor 2, and contributor 3. Each checked the inner rank-two class-square construction, retained outer-class deduction and actual odd-central transfer; large-component fixed antiflags/planes and the m=3 case; m=4 enlarged scalar fibers, same-class witnesses and capacity bounds; and both m=2,q=4 orientations. Their endpoint checks included the actual trivial intersection, centralizers, divisibility by40, corrected order-three field-class witnesses, oddness of the stabilizer intersection and the complete1964 automorphism count. Acceptance is conditional on the cited canonical, common-model, automorphism/descent, marked-component and A8 inputs.

The paired-simple reviewer freshly inspected LWX v2 Lemmas4.6–4.9 and their explicit natural model. The other reviewers retained the recorded source audits without a fresh primary inspection. All retained the exact earlier odd/even-linear descent and rank-four capacity proofs rather than claiming fresh proofs of the external classifications. No new computation or rerun of the exploratory GAP control was claimed. The exact source is locally available; repository integrity separately passed115 tests under Python3.12.14. These research reviews are not formal GitHub approvals. G2 antiflag pairs, other full-socle cases and complete classification remain open.
