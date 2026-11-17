# All odd-dimensional linear full multiplication socles

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md), with three independent exact-source reviews recorded below.

**Conditionally proved theorem.** For every odd n≥3 and every prime power q, no finite simple proper left Bol loop has full multiplication group with socle PSL_n(q), under the canonical and group-classification inputs below. The theorem covers every almost-simple overgroup and actual factor orientation. It does not exclude even-dimensional linear socles or classify the surviving alternating loop operations.

## Inputs and the actual residual

Use the [canonical definitions](../foundations/problem-contract.md), writing M=Mlt(Q), G=LMlt(Q), I=M₁, H=G∩I and Λ=tK in the formal inversion extension. Retain C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped C0007 inversion at `932ead5db5f39045e2085caa6b062f6b981b2813` and C0008 full-group almost-simplicity at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. In particular Λ is G-invariant, consists of outside involutions, |Λ|=[M:I], H∩Λ²={1}, t∈Λ and ⟨tΛ⟩=G.

The [odd-dimensional canonical-overgroup theorem](../factor-permutation/radical-free-three-dimensional-linear-unitary.md#almost-simple-odd-dimensional-linear-and-unitary-canonical-groups), reviewed at `114ce1b011fd47589eb762ed7cd5492a190002d8`, excludes S=Soc(M)≤G. The solvable-I result at `030ebb1d681efd8b12139efc7d0e3d4bdc9173ce` would force S≤G and is therefore also excluded. Prime n is already covered by the reviewed all-prime-dimensional full-socle theorem at `c3f045c52e5e5dea344aba9823567834eb304218`. For odd composite n≥9, the solvable-G possibility is the linear Singer/parabolic family in Li–Xia arXiv:1408.0350v3, Theorem1.1 and Tables1.1–1.2; the other table entries have different socles. That entire actual family, in both orientations, is reviewed at `472e2653976598a9666142e7f64e07a4601c61e8`. Its canonical proof is [the linear Singer-parabolic section](../odd-completion/nonbruck-almost-simple-radical-bridge.md#proposed-exclusion-of-the-linear-singer-parabolic-family-in-every-dimension). These are scoped dependencies, not aggregate claim promotions.

Thus both actual factors G,I are nonsolvable and neither contains S. **Li–Wang–Xia**, *Factorizations of almost simple linear groups*, [arXiv:2106.03109v2](https://arxiv.org/html/2106.03109v2),11October2021, Theorem1.2, definition of tight containment immediately preceding it, and Table1.1 give the actual pair. In odd composite dimension only row1 is possible, with the special-linear extension-field option; its symplectic option and rows2–8 have even dimension, and rows9–15 have dimension2,3 or even. Up to swapping the factors and applying one common automorphism of S, (G,I) tightly contains

    X=image of SL_a(q^b),   Y=q^(n−1):SL_(n−1)(q),   n=ab,

where a,b are odd and a≥3,b≥3. The alternatives a=1 and b=1 would respectively give a solvable factor or a factor containing S. The divisor b need not be prime. Tight containment means the perfect residual of each actual factor equals that of the indicated subgroup; X and Y are perfect in this range. The embeddings and their simultaneous intersection are given by Lemma4.1: before projectivization the intersection is q^(n−b):SL_(a−1)(q^b). The source authors directly inspected the definition, theorem, every table row and Lemma4.1 at this exact version. The CFSG-dependent factorization theorem is an external input.

## Canonical factor containing the extension-field component

Suppose G tightly contains X and I contains Y. Then L=X=G^(∞) is characteristic and quasisimple, with odd center Z, and L/Z≅PSL_a(q^b). Its center is an image of the odd-order scalar center of SL_a(q^b); it need not be trivial. Set r=q^b. The embedded SL_(a−1)(r) in the actual intersection X∩Y≤H contains a minimal involution: a diagonal matrix with two entries −1 in odd characteristic, or a rank-one transvection in characteristic two. These matrices lie on the coordinates complementary to the first extension-field basis vector, so they survive projectivization as actual involutions of H∩L.

Every actual selected mark λ normalizes L and induces an automorphism of order at most two on L/Z. If every mark induces the identity, each centralizes L: for perfect L, an automorphism acting trivially on L/Z differs from the identity by a homomorphism L→Z, which is trivial. Then t∈Λ and K=tΛ imply G=⟨K⟩ centralizes its own nonabelian subgroup L, impossible. Choose a mark with a nonidentity induced automorphism β.

For every outer involution β of PSL_a(r), the local class-square interfaces in the pinned odd-dimensional manuscript put every internal involution in the square of its PSL_a(r)-class. Their exact sources are `b436485f3c07c3413c19b319e51e8c7bc2c3a580`, `d5e26dd6aef4ad09f61e0569e383782dea0d468b`, `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede` and `fa462cdffd3082b37b0f100ea7e0364a97832473`, with their local scope collected at `114ce1b011fd47589eb762ed7cd5492a190002d8`. Only the linear statements are used here. Their field/graph/diagonal normalization, finite-field descent and standard automorphism descriptions remain inputs.

For inner β the required minimal class follows directly. In odd characteristic, lift its involution to SL_a(r); the lift is unique because its center is odd. It is diagonalizable with an even, nonzero number j of −1 entries, 2≤j≤a−1. Choose two such diagonal matrices sharing j−1 negative coordinates. They are conjugate in SL_a(r), commute, and have product with exactly two negative entries. In characteristic two, every involution is I+N with N²=0 of rank j≤(a−1)/2. Representatives

    A=I+Σ_(i=1)^j E_(i,j+i),   B=A+E_(1,2j+1)

are conjugate involutions, commute, and have transvection product. The GL conjugacies can be chosen in SL: the centralizer has a determinant-surjective factor on a fixed one-dimensional summand, which exists in odd dimension. Consequently the square of every nontrivial inner class contains the entire minimal projective involution class as well.

Apply these class-square statements in the FORMAL local quotient (L⋊⟨λ⟩)/Z. Even for inner β the external coordinate is retained; its map to Aut(L/Z) is faithful on L/Z, so the displayed products correspond to the same internal involutions. The [odd-normal collision lifting lemma](odd-normal-involution-collisions.md), locally with kernel Z, puts the specified actual minimal involution of H∩L in (λ^L)²⊆Λ². No assumption that λ fixes Z is needed. This contradicts H∩Λ²={1} and excludes this orientation for every q,a,b in the stated range.

## Canonical factor containing the vector parabolic

Suppose instead G tightly contains Y and I tightly contains X. Put m=n−1 and U=O_p(Y)≅F_q^m, where q=p^f. Since G^(∞)=Y, U is characteristic in G. The characteristic-module argument in the reviewed Singer/parabolic source applies before its Singer-specific lower bound: the common fixed space of U identifies the point parabolic (or its dual under the common ambient automorphism), graph automorphisms exchange the two distinct fixed-space dimensions, and the faithful projective Levi representation gives

    G=U⋊D,   SL_m(q)≤D≤ΓL_m(q),   U=O_p(G),   D^(∞)=SL_m(q).

The projective scalar kernel is exactly the one removed in PSL_n(q); the Levi action A↦det(A)A is faithful on SL_m(q). Here m≥8, so all the perfectness and endomorphism-field hypotheses of that reviewed argument hold. Canonical inversion acts on U through ΓL_m(q), because it normalizes the characteristic SL_m(q) quotient and its endomorphism field F_q. The kernel of conjugation on U inside G is U. Hence every original outside involution fiber over an image in ΓL_m(q) has at most |U|=q^m elements. The uniform semilinear count, equation(18) at exact source `472e2653976598a9666142e7f64e07a4601c61e8`, includes identity and gives

    |Λ| ≤ q^m J_m(q) < 11 q^(m²/2+m) = 11 q^((n²−1)/2).

Only the original upper-bound argument is transferred. No quotient folder, affine realization of inversion, vanishing of H¹ or hypothesis about I∩U is used.

For the lower bound, X=I^(∞) is characteristic in I, so I normalizes the actual extension-field subgroup X. View the natural space as F_(q^b)^a over F_q. The F_q-algebra generated by the elementary root transvections of SL_a(q^b) is Mat_a(F_(q^b)), whose commutant in End_(F_q)(V) is the scalar field F_(q^b). A projective F_q-linear normalizer of X preserves this generated algebra: the possible scalar discrepancies lie in the same algebra. It therefore normalizes the commutant field and is induced by an F_q-semilinear transformation of the extension-field structure. The field-automorphism quotient has order b, so the projective linear normalizer has order at most b|GL_a(q^b)|/(q−1). The full automorphism description of PSL_n(q), already pinned in the odd-linear source, adds at most f base-field labels and two graph labels. Thus

    |I| ≤ 2bf |GL_a(q^b)|/(q−1) < 2bf q^(ba²)/(q−1).

This bound is about the actual I, not a chosen maximal overgroup. Standard group orders give |S|>q^(n²−1)/(4n), and therefore

    |Λ|=[M:I] ≥ |S|/|I| > (q−1)q^(n²−1−n²/b)/(8nbf).

Let D₀=n²(1/2−1/b)−1/2. The two bounds contradict one another as soon as (q−1)q^D₀>88nbf. Indeed b≥3, n≥9, b≤n/3 and q≥2^f give

    (q−1)q^D₀ ≥ f·2^(n²/6−1/2) > f·(88/3)n² ≥ 88nbf.

For the first inequality use D₀≥n²/6−1/2≥13 and 2^(f−1)≥f. For the strict inequality, at n=9 it is 8192>2376. When n increases by one, the exponential grows by at least2^(19/6)>8, while n² grows by at most(10/9)²<2; hence the inequality persists for every n≥9. This excludes the reverse orientation in every characteristic.

## Assembly and limits

The two orientations exhaust the actual nonsolvable-factor residual in odd composite dimension. Together with the pinned prime-dimensional, socle-containing and solvable-factor exclusions, they prove the proposed full-socle theorem for every odd n≥3 under the displayed inputs. The new normalizer argument and comparison use exact algebra and inequalities; no finite census or numerical experiment is required. The new odd-normal lifting lemma is independent of CFSG, but this full-socle assembly uses the cited classifications and previously reviewed local square/count results. Independent exact-source reviews are recorded below. Even-dimensional linear socles, other remaining Lie types and the complete loop classification remain open.


## Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted both new manuscripts at exact source `59338c6eebe69e352d561b68c870ac842d6047e0`. Each checked the actual-factor exhaustion, characteristic quasisimple component and odd kernel, original selected-mark class-square lifting including center-moving inversion, the minimal inner class in both characteristics and special-linear determinant correction, and the reverse orientation's characteristic U, original outside fibers, commutant normalizer and uniform inequality at the n=9 boundary. Each directly inspected Li–Wang–Xia v2 Theorem1.2 and its tight-containment definition and Lemma4.1; reviewer A and reviewer C explicitly inspected every Table1.1 row as part of the exhaustion audit. reviewer A also reread the pinned characteristic-two local square interface. All retained the previously reviewed outer-class, semilinear-count, solvable-factor, prime-dimensional and standard automorphism inputs, without reproving their external classifications.

No new research computation was needed. The source authors separately ran Python3.12.14 repository integrity:115 tests passed. These are independent model mathematical reviews, not formal proof, human certification, remote CI results or GitHub approvals. They support the odd-dimensional linear full-socle exclusion under the displayed inputs and leave the other stated classification gaps open.
