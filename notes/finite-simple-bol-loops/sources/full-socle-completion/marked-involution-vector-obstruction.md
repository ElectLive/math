# Marked involutions, odd-central components and vector stabilizers

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source review recorded below. Two original-folder obstructions below exclude (i) every characteristic-two component-side orientation in the linear, symplectic and G2 extension-field/vector-parabolic pairs of Li–Wang–Xia Table1.1 rows1–2, and (ii) every symplectic extension-field/vector-parabolic canonical orientation on the parabolic side, in every characteristic. Each application has its explicit parameter/model restrictions below. They do not classify all actual factors or loop operations.

Use the canonical definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. In the actual formal extension, Λ=τK is a G-invariant set of outside involutions, contains τ, has H∩Λ²=1, and τΛ generates G. All uses of this interface concern the original group and marks.

## An involution in an automorphism-class square

Let T be nonabelian simple of even order and α a nonidentity automorphism of order two. Form the external semidirect product E=T⋊⟨α̂⟩, even when α is inner. Its odd normal core is trivial: its intersection with T is1, hence it centralizes T, whose centralizer in E has order at most2. The element α̂ is not central, since it acts nontrivially on T. Thus α̂∉Z*(E), where Z* is the preimage of the center modulo the odd normal core. If α is inner, E can have a central involution; the argument does not assert Z(E)=1.

Glauberman, *Central Elements in Core-Free Groups*, Journal of Algebra4(1966),403–420, Corollary1 on printed p.404 (following Theorem4 on p.403), [primary publisher PDF](https://www.sciencedirect.com/science/article/pii/0021869366900305/pdfft?md5=6be99e092fb862214b7faea13789413b&pid=1-s2.0-0021869366900305-main.pdf), gives a distinct E-conjugate β̂ commuting with α̂ in a common Sylow2-subgroup. E-conjugacy of α̂ is the same as T-conjugacy, since E=T⟨α̂⟩ and α̂ centralizes itself. Their product is a nonidentity involution in T, lying in (α̂^T)².

The coordinator and the source auditor directly inspected the primary theorem/corollary statements through the cached publisher PDF; neither reverified its character-theoretic proof. An initial direct URL request returned403 before the cached reference was accessible. This is the general existence part of the earlier [single-class argument](../primitive-completion/sd3-involution-count.md), whose exact reviewed source `65c54aff108cc70208bf6f7271b1e5cf6a0a76bc` is retained. Here no hypothesis says that T has one internal involution class; we use only existence and independently review this general application.

## Original-folder obstruction with an odd-central characteristic component

Suppose L is characteristic in G, is perfect, has odd center Z, and T=L/Z is nonabelian simple of even order. Suppose also that H∩L meets every L-conjugacy class of nonidentity involutions in L. Then the original folder cannot exist.

An automorphism of perfect L inducing identity on T is identity: its central displacement is a homomorphism L→Z. If every λ∈Λ induced identity on T, all marks, including τ, would centralize L; then their products K and the group they generate would centralize L, contradicting nonabelian L≤G. Choose a mark inducing a nonidentity involution α of T.

Apply the preceding class-square lemma and lift the two projected T-conjugates to actual L-conjugates λ₁,λ₂ of that mark. Their product x lies in L and projects to a nonidentity T-involution, so x²∈Z. Put k=|Z|, odd. Then y=x^k is an actual involution in L and still projects to the same nonidentity involution. It remains in Λ², a point which cannot be inferred merely from the projected product: with x=λ₁λ₂ and r=(k−1)/2,

    x^k=λ₁ (x^(−r) λ₂ x^r).

Both factors lie in Λ because x∈L≤G. Thus an actual L-involution belongs to Λ². By the hypothesis on H∩L, an L-conjugate of y lies in H. G-invariance of Λ² contradicts H∩Λ²=1. This elementary odd-power argument does not assume the central kernel is fixed by the mark, and it does not construct a quotient loop.

A sufficient geometric condition for the hypothesis is an odd-central cover π:L̃→L with a faithful linear action in characteristic two, transitive on its nonzero vectors, such that π(L̃_v)≤H for some nonzero v. An actual involution y∈L lifts uniquely to an involution ỹ∈L̃: central adjustment uses the bijective square map of the odd kernel. Since (ỹ−1)²=0 on a nonzero characteristic-two vector space, ỹ fixes a nonzero vector. Transitivity of L̃ conjugates it into L̃_v. Its image is the required conjugate of y in H. In particular L itself need not possess a faithful natural module. No lift of τ or G to the covering group is assumed.

## Characteristic-two extension-field components on the canonical side

Let M=Mlt(Q) be almost simple with socle S=PSL_n(q), q even, n≥4. Let actual G=LMlt(Q) and I=M_1 satisfy M=GI, with G tightly containing X and I tightly containing the vector stabilizer Y in one of these Li–Wang–Xia pairs:

* Linear X=image SL_a(q^b), n=ab, a,b≥2.
* Symplectic X=image Sp_a(q^b)', n=ab, a even, in the nonsolvable range.
* G2 X=image G2(q^b)', n=6b, b≥1.

The source is Li–Wang–Xia, *Factorizations of almost simple linear groups*, arXiv:2106.03109v2, definition of tight containment, Theorem1.2/Table1.1 rows1–2, printed p.2, and Lemmas4.1–4.4, pp.4–5, [exact primary version](https://arxiv.org/html/2106.03109v2). Those lemmas use the actual common natural embeddings, not just abstract factor orders. A common source automorphism can be applied to the entire folder and the displayed subgroups. In each stated nonsolvable case X is perfect, so tightness gives L=G^(∞)=X characteristic in G. It is quasisimple with odd center: for the linear family the scalar center has odd order; in characteristic two the symplectic and G2 groups are centerless in the simple cases described below. The simple quotient T has even order.

For the linear family the cover L̃=SL_a(q^b) is perfect and transitive on nonzero vectors of the restricted-scalar module. Its projective kernel is odd and central. Lemma4.1 explicitly identifies the vector stabilizer in the common model and its image in X∩Y≤G∩I=H. The case a=2,q^b=4 is included; SL2(2) cannot arise under a,b≥2. The geometric condition therefore applies even when the projective image has no faithful natural vector module.

For symplectic groups, Lemma4.2 identifies the full nonzero-vector stabilizer of Sp_a(q^b)' and states transitivity. Except for (a,b,q)=(4,1,2), the relevant group is the usual perfect symplectic group. For that exception it is Sp4(2)'≅A6, and the source gives stabilizer2²:S3 of order24, hence index15=2⁴−1. This perfect simple group still has the faithful restricted natural characteristic-two action. The stated exceptional stabilizer calculation is source-reported Magma evidence, not a computation reproduced here. It can alternatively be omitted using the separately reviewed full-socle A8 exclusion.

For G2, Lemmas4.3–4.4 similarly give the natural six-dimensional action over F_(q^b), transitivity on all q^(6b)−1 nonzero vectors, and the full vector stabilizer. For q^b=2 the group is G2(2)'≅PSU3(3), simple and centerless; the source's stabilizer has order96, giving index63. This exceptional calculation also relies on the paper's reported Magma computation. The general group is the perfect simple G2(q^b), with faithful module and trivial center. The source auditor observed that one proof sentence of Lemma4.3 says q>4, while the statement of Lemma4.4 explicitly covers every nonexceptional parameter including q=4; we retain the stated complete lemma rather than silently changing its range.

Thus every displayed characteristic-two canonical component side satisfies the geometric obstruction and is excluded. The small simple-group identifications and natural embeddings are explicit source inputs; they are not inferred solely from their orders. In particular the argument does not require a complete outer-involution class roster or a quotient-folder hypothesis.

## Same-field symplectic component on the full-stabilizer side

Now let q be any prime power and n≥4 even. Suppose the actual canonical group G tightly contains the vector parabolic Y=U:SL_(n−1)(q), and actual I tightly contains the natural same-field X=image Sp_n(q)'. Retain the characteristic-radical and natural-action interface from exact reviewed source `472e2653976598a9666142e7f64e07a4601c61e8`, also used in the [reviewed linear extension/parabolic theorem](even-linear-extension-parabolic.md), source `d95f900af71ff43fcc5486345a0c24f7eb47f6da`. It makes U characteristic in G and makes G transitive on U minus identity.

If every mark centralized U, then τ and K=τΛ would centralize U, contradicting generation and the nontrivial natural action of SL_(n−1)(q). Thus some λ∈Λ and u∈U have λ^u≠λ. Their product λλ^u is a nonidentity element of U∩Λ². By G-invariance and transitivity, every nonidentity element of U belongs to Λ². Therefore

    H∩U=1.                                               (1)

In the common model of Li–Wang–Xia Lemma4.2 with b=1, Y fixes a nonzero vector v and U consists of x↦x+f(x)v, f(v)=0. For a nonzero scalar c, the symplectic transvection x↦x+c⟨x,v⟩v belongs to both U and Sp_n(q). The latter is perfect in the present range except Sp4(2), so its projective image belongs to X∩Y≤H and is nonidentity. This contradicts (1). The exceptional Sp4(2)' case has full socle PSL4(2)≅A8 and is excluded by the reviewed alternating full-action theorem and minimum-order24 result, as pinned in the linear extension/parabolic manuscript. This proof includes odd q, retains the actual common model, and does not assume that the transvection lies in Sp4(2)'.

## Symplectic extension-field factors on the full-stabilizer side

Continue with canonical G on the vector-parabolic Y side, now with X=image Sp_a(R)', a=2k≥4, R=q^b and b≥2. Thus R≥4 and the full symplectic group is perfect. We derive its natural-module normalizer instead of assuming an unverified bound.

For every nonzero v and c∈F_R, the symplectic transvection 1+c v(vᵀJ) lies in Sp_a(R). Hence its generated F_q-algebra contains all operators c v(vᵀJ). For any nonzero v,w choose z pairing nontrivially with both; two proper hyperplanes do not cover the space over F_R. Multiplying the three corresponding rank-one operators gives a nonzero scalar multiple of v(wᵀJ). Varying c supplies every F_R multiple. These operators span Mat_a(F_R), whose commutant in End_(F_q)(V) is F_R. Any F_q-linear normalizer therefore preserves that field; after a field automorphism of F_R/F_q it is F_R-linear. If g normalizes Sp_a(R), the alternating form with matrix gᵀJg is invariant, so J⁻¹gᵀJg commutes with Sp_a(R) and is scalar. Thus g is a symplectic similitude. We obtain the uniform bound

    |N_GL_n(q)(Sp_a(R))| ≤ b(R−1)|Sp_a(R)|.

A projective normalizer of X lifts to this genuine linear normalizer: after adjoining the scalar kernel, the derived subgroup of the full preimage is the perfect Sp_a(R). As in the reviewed linear intersection proof, an element of Y has a unique vector-fixing determinant-one representative. The linear normalizer contains Sp_a(R), which is transitive on nonzero vectors. Consequently

    |N_S(X)∩Y| ≤ b(R−1)|Sp_a(R)|/(q^n−1),
    |Λ|≥|Y|/|N_S(X)∩Y|≥|SL_n(q)|/[b(R−1)|Sp_a(R)|].

The elementary order bounds |SL_n(q)|>q^(n²−1)/2 and |Sp_(2k)(R)|<R^(2k²+k), and n=2kb, make this last lower bound strictly larger than

    q^[4k²b²−1−b(2k²+k+1)]/(2b).

The reviewed weighted original-fiber bound from `d95f900af71ff43fcc5486345a0c24f7eb47f6da` is |Λ|<12q^[2k²b²−kb]. The exponent difference is D=2k²b(b−1)−b−1≥7b−1 for k,b≥2, and q^D≥2^(7b−1)>24b. The lower and upper bounds contradict each other for every parameter; there is no finite residual. For the SL order bound, ∏_(i=2)^n(1−q^(−i))>1/2 follows directly from the finite-product bound by the sum of the omitted geometric series.

If a=2 then Sp₂(R)=SL₂(R), already covered by the reviewed linear-extension Y-side theorem. If b=1, use the preceding radical collision and the separately pinned Sp4(2)' exception. This completes every symplectic vector-parabolic Y-side case in the nonsolvable source range, for all fields. The derived-group and common-model interfaces remain those of LWX Lemma4.2; no new representation classification is invoked.

## Scope, evidence and review boundary

The characteristic-two result closes the X-side of the specified vector-parabolic pairs, including linear, symplectic and G2 extension-field components. The last two sections separately close every symplectic Y-side for all q. The linear Y-side already has the separate all-field review at `d95f900af71ff43fcc5486345a0c24f7eb47f6da`. The G2 Y-side and odd-characteristic component sides are not claimed here, nor are the different vector-and-complement factor pairs in LWX rows3–8.

The coordinator and contributor 1 freshly inspected Glauberman's Theorem4/Corollary1 statements and the exact LWX model statements; the source's small Magma calculations and the primary group-theoretic proofs were not rerun or rederived. No new computation is needed for the marked-square, odd-power, covering-vector, radical-collision or symplectic normalizer/capacity deductions. The exact central quotient distinction is essential: a projective image is not silently assigned the cover's faithful module. Independent exact-source mathematical review of this entire assembly is recorded below.


## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted the entire assembly at exact source `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`: contributor 2, contributor 3, and contributor 4. Each checked the formal semidirect product including inner automorphisms, the odd-core/noncentral Z* application, actual marked-product odd-power identity, and covering-module vector transport without lifting τ. Each also checked the actual characteristic-component/common-model applications, same-field radical collision, symplectic transvection-algebra normalizer, projective intersection and uniform exponent bound. All retain the pinned canonical, common-embedding/factorization, weighted-fiber and stated finite-group inputs.

The paired-simple reviewer freshly inspected Glauberman Corollary1 p.404 through the indexed publisher PDF and LWX v2 Lemmas4.1-4.4. The presentations reviewer freshly inspected LWX Theorem1.2/Table1.1 and those lemmas, but its direct Glauberman URL request returned403, so it retained the coordinator/source-auditor primary inspection. The S5 reviewer retained the precise primary inputs without a fresh PDF audit. None reran the source-reported exceptional Magma calculations, and none claimed a new computation for these algebraic deductions. The source commit is locally available. Repository integrity separately passed115 tests under Python3.12.14; that is not mathematical proof. These are research reviews, not formal GitHub approvals. The G2 parabolic side, odd-characteristic component sides and unrestricted classification remain open.
