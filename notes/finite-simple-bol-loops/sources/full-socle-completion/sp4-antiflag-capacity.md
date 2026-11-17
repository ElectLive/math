# Rank-four symplectic antiflag capacity and the complete pair

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source mathematical review recorded below. Let Q be a finite simple proper left Bol loop with almost-simple full multiplication group M of socle S=PSL4(q). Let G=LMlt(Q), I=M_1, H=G∩I. Suppose actual (G,I) tightly contains (X,Y), where X is the natural projective image of Sp4(q)' and Y is the naturally embedded SL3(q) fixing a nonzero vector and a complementary hyperplane. Under the cited inputs, this orientation is impossible for every q. Together with the reviewed higher-dimensional and reversed orientations, this excludes both orientations of the entire symplectic/linear antiflag pair in every even dimension. Other factor pairs and complete classification remain open.

The actual pair is Li–Wang–Xia, *Factorizations of almost simple linear groups*, arXiv:2106.03109v2, Theorem1.2/Table1.1 row3 p.2 and Lemma4.5 p.6, [primary version](https://arxiv.org/html/2106.03109v2). Tightness gives equality of perfect residuals, not equality of actual factors. The [reviewed transvection/intersection proof](transvection-products-classical-intersections.md), source `bc837277fd94e4a4184c2843319fbff86331aa4a`, supplies its precise common-model interface and explicitly bypasses the source's inconsistent displayed intersection at (n,q)=(4,2). That parameter is already excluded by the pinned full-A8/minimum-order24 argument there; hence assume q≥3 below.

Use the canonical definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. The actual marked set Λ consists of outside involutions, is G-invariant, and has |Λ|=[G:H] and H∩Λ²=1.

## Actual stabilizer and restriction fibers

Here X=PSp4(q) is perfect and simple, so G^(∞)=X is characteristic in G. Likewise I^(∞)=Y, so I normalizes Y. The inverse image of Y in SL4(q) is (1⊕SL3(q))Z, with Z the scalar center. Its derived subgroup is 1⊕SL3(q); therefore a projective linear normalizer preserves its unique fixed line and unique invariant complementary hyperplane. In the symplectic model the pole of that hyperplane and the fixed line span a nondegenerate plane. The subgroup of Sp4(q) preserving those two lines separately has order (q−1)|Sp2(q)|. Dividing by the scalar center of order d=gcd(2,q−1) gives

    |I∩X| ≤ (q−1)q(q²−1)/d,
    |Λ| ≥ [X:I∩X] ≥ D=q³(q⁴−1)/(q−1).              (1)

This allows the entire GL1 factor in the actual intersection. It does not replace the actual H∩X by the smaller perfect intersection Sp2(q).

Retain the ambient normalizer and centralizer proof from [the reversed PSL4 symplectic-row argument](../odd-completion/nonbruck-almost-simple-radical-bridge.md#proposed-complete-exclusion-of-the-reversed-psl4-symplectic-row), independently reviewed at `793cb34657cdb232e7bb0be600e97acc42ec5c63`: N_Aut(S)(X)=PΓSp4(q)×⟨γ0⟩ and C_Aut(S)(X)=⟨γ0⟩ of order2, where γ0 is the symplectic-polarity graph automorphism. Its linear centralizer proof uses perfectness and the natural irreducible representation, and its full automorphism input is explicitly retained. Consequently C_G(X) has order at most2. If two actual outside marks have the same restriction to X, their quotient belongs to this centralizer. Thus each restriction α∈Aut(X), α²=1, has at most two marks above it. This includes identity restrictions; faithful restriction is not assumed.

## A mandatory collision test

For an automorphism α preserving natural transvections, write its direction action as v↦Av^σ. If B(v,Av^σ)≠0 for some v, choose a nonidentity transvection U of direction v and its actual image u∈X. Its α-image is represented by a transvection V of direction Av^σ. For a mark λ inducing α, the actual product λ^uλ=u⁻¹u^λ is nonidentity, represented by U⁻¹V. It fixes the nondegenerate plane ⟨v,Av^σ⟩^⊥ pointwise. A symplectic conjugate lies in the natural Sp2(q)≤X∩Y≤H, contradicting H∩Λ²=1. The precise matrix/projective transfer is the reviewed transvection lemma; no involution lift is assumed.

In every characteristic a genuinely nontrivial field part σ makes B(v,Av^σ) nonzero for some v. Otherwise, put C=JA for a form matrix J. Evaluating on basis vectors gives C_ii=0, and evaluating at e_i+z e_j gives C_ij z^σ+C_ji z=0 for every z∈F_q. At z=1 obtain C_ji=−C_ij; a z with z^σ≠z then gives C_ij=0. Thus C=0, impossible. This eliminates all field-semilinear restrictions that preserve transvections, including their inner-diagonal twists.

The standard automorphism interfaces are Steinberg Theorem3.2 as freshly inspected and recorded at `bc837277fd94e4a4184c2843319fbff86331aa4a`, and Scott Harper, *On the uniform spread of almost simple symplectic and orthogonal groups*, [arXiv:1703.09652v2](https://arxiv.org/pdf/1703.09652v2), Table3/preceding paragraph p.5, Theorem2.2/Remark2.3 p.6 and Proposition2.6 p.8. The coordinator freshly inspected Harper's exact Shintani and graph-field statements in this continuation. The earlier exact-source normalizer and symplectic proofs retain the table and algebraic-group inputs. These are classification inputs, not inferred from the collision test.

## Odd characteristic

Every automorphism of X is a projective semilinear symplectic similitude. By the preceding test, a surviving restriction has σ=1 and B(v,Av)=0 for all v. Polarization makes A self-adjoint for B. If μ is its similitude multiplier, A* A=μI implies A²=μI. Count all such projective linear transformations, whether or not they actually occur as restrictions.

If μ is a square, rescale to A²=I. Other than projective identity, the eigenspaces are an unordered pair of orthogonal nondegenerate planes. The number is

    |Sp4(q)|/[2|Sp2(q)|²]=q²(q²+1)/2.                 (2)

If μ is nonsquare, fix a nonsquare δ and rescale to A²=δI. Set E=F_q[A]≅F_(q²). Self-adjointness makes B balanced over E. Define β(v,w)∈E by

    Tr_(E/F_q)(a β(v,w))=B(av,w)    for every a∈E.

Nondegeneracy of the trace pairing defines β uniquely. Balance makes it E-bilinear. Since B(v,v)=B(Av,v)=0, one has B(av,v)=0 for all a∈E, so β is alternating; its nondegeneracy follows from that of B. Thus β is a nondegenerate alternating E-form on a two-dimensional E-space. Any two normalized A yield E-isometric such spaces, and the isometry preserves their trace form B and intertwines A. Hence there is at most one Sp4(q)-conjugacy class of normalized A, and at most one PGSp4(q)-class of their projective images. The embedded Sp2(q²)=SL2(q²) centralizes A. Its projective image has order |SL2(q²)|/2, while |PGSp4(q)|=|Sp4(q)|. The number of these projective restrictions is therefore at most

    2|Sp4(q)|/|SL2(q²)|=2q²(q²−1).                   (3)

This is only an upper bound; an exact projective centralizer is unnecessary. Combining identity, (2), (3), and the two-mark fiber bound gives

    |Λ| ≤ 2+5q⁴−3q² < q⁶ < D                       (4)

for every odd q≥3. Indeed q⁶≥9q⁴>5q⁴−3q²+2. This contradicts (1) uniformly, including q=3.

## Characteristic two

Write q=2^f≥4. Harper's outer group is C_(2f), with generator ρ satisfying ρ²=φ, the ordinary field generator. A restriction of order at most two is inner or belongs to the single possible outer involution label ρ^f. For even f that label is the nontrivial half-field label and has already been excluded by the collision test.

An inner restriction is conjugation by a unique element u∈Sp4(q) with u²=1. Put N=u−1. If B(v,Nv) is not identically zero the collision test excludes it. Otherwise N is self-adjoint, N²=0 and its induced form is alternating. Nonzero N cannot have rank1, since a nonzero rank-one symmetric operator gives a nonzero square function v↦B(v,Nv). Thus rank N=2, and L=im N=ker N is Lagrangian. For each fixed L, write the symplectic space in dual coordinates L⊕L*, where N has upper-right matrix M. Self-adjointness gives symmetric M, the zero square function gives zero diagonal, and rank2 gives invertible M. There are exactly q−1 alternating invertible2×2 matrices M. The number of Lagrangians is (q+1)(q²+1), obtained for example by counting isotropic ordered bases. Therefore there are exactly q⁴−1 surviving nonidentity inner restrictions, and q⁴ including identity. For even f this yields

    |Λ|≤2q⁴<D.                                      (5)

For odd f≥3, overcount every graph-field involution. Harper Proposition2.6 and the connected Lang–Steinberg argument retained from exact source `793cb34657cdb232e7bb0be600e97acc42ec5c63` give one X-class with centralizer Sz(q), order q²(q²+1)(q−1). More explicitly, the Suzuki endomorphism σ0 has σ0²=F_q. For an outside involution Aσ0, Lang gives A=Bσ0(B)⁻¹, and Aσ0(A)=1 forces B=F_q(B), so the conjugator belongs to X. Hence the entire outside involution class has size

    |Sp4(q)|/|Sz(q)|=q²(q+1)(q²−1).

We do not assert that these exceptional graph automorphisms preserve transvections; they are simply counted. Thus

    |Λ|≤2[q⁴+q²(q+1)(q²−1)]<2q⁵+4q⁴<q⁶<D          (6)

for q≥8, since q²>2q+4. Equations (5)–(6) finish every even field. The q=2 endpoint is the separate reviewed A8 case, not a simple Sp4(2) argument.

## Assembly, evidence and review boundary

The [reviewed transvection/intersection theorem](transvection-products-classical-intersections.md), source `bc837277fd94e4a4184c2843319fbff86331aa4a`, already excludes the symplectic canonical antiflag orientation for even n≥6 and the reversed linear canonical orientation for every even n≥4. The present rank-four argument therefore completes both actual orientations of LWX Table1.1 row3 for all parameters, conditional on the stated inputs. It says nothing about the other antiflag/extension rows or the classification endpoint.

The coordinator read the retained normalizer proof and freshly inspected the primary Harper graph-field statement; the producer independently checked the capacity arguments and rank-four geometry. No new computation is needed. Independent exact-source review of this assembly is recorded below; repository integrity is separate from mathematical proof.

## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted this assembly at exact source `8ce9863ba93a03014deb4afa813a212b44d9e4fc`: contributor 1, contributor 2, and contributor 3. Each checked the actual GL1-inclusive stabilizer bound, two-element original restriction fibers, fixed-plane transvection collision and nontrivial-field elimination, odd-characteristic self-adjoint square and nonsquare counts including the trace form and single normalized class, characteristic-two alternating rank-two count, Suzuki graph-field overcount, every uniform inequality and the separate A8 endpoint. The stated assembly retains the reviewed higher-dimensional and opposite-orientation theorem; no other factor pair is certified.

The paired-simple reviewer freshly inspected Harper v2 Table3/Proposition2.6 and LWX v2 Lemma4.5. The other two retained the recorded primary audits without fresh Harper inspection. All retained the exact normalizer/centralizer proof at `793cb34657cdb232e7bb0be600e97acc42ec5c63`, the canonical folder and class/fixed-group inputs, and the higher-dimensional/intersection theorem at `bc837277fd94e4a4184c2843319fbff86331aa4a`. No new computation was claimed or required. The exact reviewed source is locally available, and repository integrity separately passed115 tests with Python3.12.14. These research reviews are not formal GitHub approvals. Complete classification remains open.
