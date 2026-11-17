# Both G2/linear antiflag orientations

Independently reviewed continuation of [0323:C0010](../foundations/research-C0010.md), conditional on the stated canonical and external inputs. Let Q be a finite simple proper left Bol loop, M=Mlt(Q) almost simple with socle S=PSL6(q), q even, and G=LMlt(Q), I=M_1, H=G∩I. Suppose actual (G,I), in either orientation, tightly contains the G2(q)/SL5(q) antiflag pair of Li–Wang–Xia Table1.1 row8. Under the stated inputs, no such Q exists, including q=2 with the full nonperfect G2(2) factor. Other actual factor pairs and the complete classification remain open.

The actual source is Li–Wang–Xia, *Factorizations of almost simple linear groups*, [arXiv:2106.03109v2](https://arxiv.org/html/2106.03109v2), Theorem1.2/Table1.1 row8, Lemmas4.10–4.11 and their remarks, printed p.7. The coordinator freshly inspected them. In the covering natural module, B=G2(q)≤Sp6(q) and Y=SL5(q) fixes a vector v and complementary hyperplane W; B∩Y is SL2(q), equivalently B intersected with the pointwise stabilizer Sp4(q) of a nondegenerate plane. These are covering-group intersections. In PSL6(q), an intersection can gain ambient scalar representatives; no equality with the covering intersection is assumed below. Tightness gives actual containment and equality of solvable residuals, and a common source automorphism is applied to the entire pair.

Use the canonical definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. The original marks Λ are G-invariant outside involutions with |Λ|=[G:H] and H∩Λ²=1. Restrictions below are restrictions of these actual marks, not a quotient folder.

## G2 canonical component, q≥4

Here X=G2(q) is perfect, simple and centerless, and tightness makes X=G^(∞) characteristic. Since I^(∞)=Y, I normalizes Y. Lift an element of I∩X uniquely to its genuine G2(q) matrix. Normalizing the projective Y makes it normalize (Y Z)'=Y in SL6(q), where Z is the scalar center, so it preserves Y's unique fixed F_q-line and invariant complementary hyperplane. Its eigenvalue on that line lies in F_q×; the kernel fixes the actual vector and hyperplane, hence is in the covering intersection SL2(q). Therefore

    |I∩X|≤(q−1)|SL2(q)|,
    |Λ|≥D=q⁵(q⁶−1)/(q−1)>q¹⁰.                      (1)

This direct eigenvalue argument accounts for projective scalar representatives. For example the projective perfect intersection has order gcd(6,q−1)|SL2(q)| by factorization orders; it is not silently replaced by SL2(q).

The [reviewed restricted-scalar centralizer proof](g2-vector-parabolic-capacity.md), exact source `4169b5a5219bf8872dcf8723a2dbea6e07ddb111`, can be applied with base field F2 and extension field F_q. It proves that the F2-linear commutant of the natural G2(q) module is precisely F_q, using its nonzero-vector transitivity and Vasilyev's minimum permutation degrees. Perfectness removes any projective scalar character. Thus no nontrivial base-field semilinear element centralizes X, and its projective semilinear centralizer is trivial. The full PSL6(q) automorphism description has only one additional graph coset. Consequently |C_G(X)|≤2. Every original restriction fiber over Aut(X) has size at most2.

Burness–Thomas, *On the involution fixity of exceptional groups of Lie type*, [author PDF](https://seis.bristol.ac.uk/~tb13602/docs/BTh_revised_2.pdf), Proposition2.3 p.8 and Table5 p.10, gives the complete two internal involution classes in G2(q), with centralizer orders q⁵|SL2(q)| and q³|SL2(q)|. The coordinator freshly inspected that row and its completeness statement. Hence, counting identity,

    j(X)=1+(q²+1)(q⁶−1).

The characteristic-two outer group is C_f, q=2^f, by BGH arXiv:2006.01421v2 Table2 p.19, retained with the reviewed G2 source. There is no exceptional graph automorphism in characteristic two. If f is even, the sole possible outer involution label is half-field. Connected Lang–Steinberg descent, as in the [reviewed exceptional field proof](exceptional-field-involution-exclusions.md), source `cd5bf6a31bc63eb838b3150e51dd7aaec57be838`, gives one X-class with centralizer G2(√q), hence class size q³(q³+1)(q+1). If f is odd that label is absent. Overcounting it in both cases gives

    |Λ|≤2[1+(q²+1)(q⁶−1)+q³(q³+1)(q+1)]<q¹⁰.       (2)

Indeed the bracket expands to q⁸+q⁷+2q⁶+q⁴+q³−q²; after division by q⁸ its positive terms are bounded at q=4 by 1+1/4+1/8+1/256+1/1024<2. Thus twice the bracket is less than4q⁸<q¹⁰ for q≥4. Equations (1)–(2) contradict each other uniformly.

## G2 canonical factor at q=2

The actual source factor is B=G2(2), not its derived subgroup. Put A=B'=PSU3(3); tightness gives G^(∞)=A. The binary antiflag normalizer inside SL6(2) is SL5(2), since its scalar quotient has order q−1=1. Therefore H∩A has order at most |B∩SL5(2)|=6, and

    |Λ|≥6048/6=1008.                                 (3)

The reviewed same-module input at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, using LWX Lemmas4.3–4.4, makes A transitive on the63 nonzero vectors of its natural binary six-dimensional module. It is therefore irreducible. Its endomorphism ring is a finite field F_(2^k), k|6. If k=2, perfect A would embed in SL3(4), then inject into PSL3(4) by simplicity, impossible since6048 does not divide20160. If k=3, |GL2(8)|=3528<6048; if k=6 its faithful image would be abelian. Thus k=1, the linear centralizer is trivial, and the ambient graph quotient makes |C_G(A)|≤2.

The [primary ATLAS page](https://brauer.maths.qmul.ac.uk/Atlas/exc/G22/) records |A|=6048, Out(A)=2 and G2(2)=U3(3):2, so Aut(A)=G2(2). CTblLib1.3.11's complete U3(3).2 table has involution class sizes63 and252. Therefore j(Aut A)=316 and

    |Λ|≤2·316=632<1008.                              (4)

The finite certificate below verifies the exact table arithmetic. The source's natural-module transitivity, its small Magma factorization calculation and the ATLAS group identification remain external inputs.

## Linear canonical factor, q≥4

Now G tightly contains the line/hyperplane factor, so L=G^(∞)=SL5(q), embedded as 1⊕SL5(q), with odd center. The [reviewed rank-two class-square theorem](extension-antiflag-pairs.md#a-rank-two-square-in-every-odd-dimensional-linear-automorphism-class), source `c6b16d21dc2aa8b0332e0d77eced0159a33ff832`, applies for every even q. It supplies an actual rank-two L-involution in Λ² and its full L-class. We show that H contains a member of that class, using the specific source intersection.

Gill–Guillot–Liebeck, *The binary actions of simple groups of Lie type of characteristic2*, Pacific J.Math.336(2025),113–134, §4.5, the G2(q) paragraph on printed p.129, [published primary PDF](https://msp.org/pjm/2025/336-1/pjm-v336-n1-p05-s.pdf), describes the long/short A1 subsystem pair on the natural six-dimensional module as (1⊗1)⊕(0⊗1^(2)). In particular a long-root involution has Jordan form J2²J1². The coordinator freshly inspected this exact statement through the indexed published PDF; an initial direct PDF request was not usable. The paragraph assumes q≥4, so q=2 is handled separately below.

The long A1 fixes the two-dimensional summand pointwise and has two natural summands on the remaining four dimensions. Invariance of the symplectic form gives no pairing between its trivial and natural modules, so its fixed two-space is nondegenerate. LWX Lemma4.10's factorization Sp6(q)=G2(q)Sp4(q) makes G2(q) transitive on ordered symplectic pairs: Sp4(q) is their pointwise stabilizer. We may therefore conjugate this long A1 by G2(q) so that its fixed plane is the source's specified plane. It lies in the covering intersection G2(q)∩Sp4(q), and equal orders |SL2(q)| identify it with that intersection. Its root involution has rank2 on the full six-space and, after removal of the fixed antiflag line, rank2 on L's five-space. Its image belongs to H. This is the required original marked-square collision. Neither rank nor subgroup placement is inferred from the abstract intersection order alone.

## Linear canonical factor at q=2

Let B=G2(2), A=B', K=Sp4(2), and C=B∩K≅SL2(2), of order6, in LWX's common symplectic model. Lemma4.10 gives Sp6(2)=BK, while its following remark states that Sp6(2)≠AK, by a source-reported Magma computation. Since [B:A]=2, if C were not contained in A then AC=B, implying AK=BK=Sp6(2). Hence C≤A. This retains the actual full B factor and uses the stated nonfactorization rather than incorrectly replacing B by A.

The ATLAS page linked above explicitly lists all faithful irreducible characteristic-two representations of A and a unique six-dimensional representation over F2. The actual LWX six-module is faithful and irreducible by its63-vector transitivity, so it is isomorphic to that listed module. The page identifies generator a as an involution in A's unique involution class2A. Its linked [matrix file](https://brauer.maths.qmul.ac.uk/Atlas/exc/G22/gap/U33G1-f2r6B0.g1), freshly downloaded and inspected by the coordinator, has SHA256

    1bc35417e67f777488139d79bc9848939f2c40466c3060ca2983bb874277a65e.

The certificate embeds its six-by-six binary entries and verifies a²=1 and rank(a−1)=2. CTblLib independently confirms there is one inner involution class. Thus every involution of C≤A has rank2 in the actual six-module and in the SL5(2) complement. The same reviewed rank-two square theorem now gives the H∩Λ² collision at q=2. This identification explicitly retains ATLAS's representation completeness and the LWX finite factorization/nonfactorization inputs; a rank calculation alone would not identify the geometric module.

## Evidence and review boundary

The standalone [finite certificate](../code/verify_g2_antiflag_small.g) requires GAP4.15.1 and CTblLib1.3.11, with assertions enabled. It loads no AtlasRep data and makes no network request. It checks |Aut A|=12096, involution class sizes63,252, the bound632<1008, the unique inner involution class, and the pinned published matrix's involution/rank identities. The coordinator read and ran the certificate; it proves only these finite identities. Primary classification, group/module identification and the actual folder/factorization deductions remain stated inputs. Repository integrity alone does not prove the theorem. The following independent reviews concern the exact source and retain the stated external inputs.


Three independent mathematical/code reviewers accepted exact source `dc80188927778f152b0ecdb758e9b3eb76040942`:

- contributor 1 checked both actual orientations, the projective intersection and centralizer bounds, both capacity inequalities, and transport of the rank-two witness into the actual intersection. The reviewer freshly inspected Gill–Guillot–Liebeck §4.5 p.129 through the indexed published PDF, LWX Lemmas4.10–4.11 and the nonfactorization remark, and the ATLAS representation-completeness listing. They extracted, read and ran the committed certificate with GAP4.15.1/CTblLib1.3.11 successfully. They did not independently download and rehash the ATLAS matrix source.
- contributor 2 checked the same scoped deductions and successfully ran an independently extracted committed certificate. They freshly inspected the LWX lemmas/remark and ATLAS completeness listing; they retained the coordinator's long-A1 PDF and matrix-hash checks.
- contributor 3 accepted both scoped orientations and successfully ran the extracted certificate with the pinned versions. They retained the recorded primary-source and representation-completeness checks, without a fresh primary-PDF audit.

All three reviews are conditional on the cited canonical folder, factorization, group/class/module classification, minimum-degree and prior rank-two inputs. The finite runs verify the displayed class counts and committed matrix entries, not those external classifications. These are independent model reviews, not formal GitHub approvals. Other actual factor pairs and the operation-level classification remain open.
