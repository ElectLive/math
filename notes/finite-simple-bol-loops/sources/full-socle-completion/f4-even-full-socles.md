# Even-characteristic F₄ full multiplication socles

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md), independently reviewed at the exact corrected source recorded below.

**Proposed theorem.** No finite simple proper left Bol loop Q has Soc(Mlt(Q))≅F₄(q), q=2^f, f≥1, under the canonical and classification inputs below. This covers the socle-containing canonical group and both actual proper-factor orientations. The [odd-field result](exceptional-field-involution-exclusions.md) is separate. Neither conclusion classifies the surviving loop operations.

## Interfaces and exhaustive division

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion/component obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. These are scoped dependencies, not promotions of their aggregate claims. Write M=Mlt(Q), G=LMlt(Q), I=M₁, H=G₁, S=Soc(M). Thus S≤M≤Aut(S), M=GI, I is core-free, and S is transitive. The original formal extension E=G⋊⟨t⟩ has the G-invariant set Λ=tK of involutions, with t∈Λ, ⟨K⟩=G, |Λ|=[G:H]=|Q|, and H∩Λ²={1}. No quotient folder or invariance of H under inversion is assumed.

Kazarin–Martínez-Pastor–Pérez-Ramos2015 Lemma11, pp.56–57, quotes LPS1990 TheoremB and explicitly gives the **actual** proper-factor intersections, up to exchanging their roles:

    G₀=G∩S, I₀=I∩S:  Sp₈(q) versus ³D₄(q) or ³D₄(q).3,
    S=G₀I₀.

The displayed product is a specific source input, not a general property of intersections with a socle. These alternatives apply if S is not contained in G; I₀ is proper by core-freeness. Otherwise §2 applies. Standard automorphism data give Out(S)=C_(2f), Out(Sp₈(q))=C_f and Out(³D₄(q))=C_(3f). The .3 in the triality normalizer acts by a genuine outer automorphism. Exact source locators and inspections are in [REFERENCES](../foundations/references.md).

We use the complete maximal-subgroup classification for F₄(q) in Craven2023 Theorem1.1 and Tables1,8, **with the author's22April2025 errata(ii)**: the ordinary Ree entry is ²F₄(q), q an odd power of2. Novelty entries concern larger almost-simple groups and are not maximal subgroups of S itself. In characteristic2 the ordinary list consists of two parabolic types, Sp₈(q), Ω₈⁺(q).S₃, ³D₄(q).3, the two A₂×A₂ forms, subfield F₄(q₀), and that Ree entry. The characteristic-two Table1 entries are PSL₄(3).2 at q=2 and PSL₂(27) at q=8; §4.3.2 confirms the first extension order, and §4.4.6/Proposition4.14 confirms the second case. Completeness, embeddings and conjugacy counts remain classification inputs.

## Socle-containing canonical groups

The cyclic-outer reduction in [the reviewed exceptional manuscript](exceptional-field-involution-exclusions.md), source `cd5bf6a31bc63eb838b3150e51dd7aaec57be838`, applies to S≤G≤Aut(S): canonical inversion acts trivially on the cyclic quotient and inverts its generating image, so G/S has exponent at most2. If G>S, its outer image contains the unique order-two label, and any involutory restriction of canonical inversion is induced by an element of G. Faithful restriction then makes inversion inner, a contradiction. Hence G=S and τ is outer.

If f is even, put q=s². There is one S-class of involutions in the field coset, with centralizer F₄(s), by Aschbacher–Seitz1976 §19(19.1), or the connected Lang argument in the reviewed manuscript. Thus Λ is that class and |H|=|F₄(s)| is even. Burness–Thomas Remark2.2 and Proposition2.3 give the natural finite/algebraic involution-class correspondence for split F₄ in characteristic2. Apply it at **both** s and q: every algebraic class has a representative in F₄(s), and any two representatives in F₄(q) in that algebraic class are F₄(q)-conjugate. Hence the fixed subgroup meets every S-involution class. For each fixed involution u, τ and τu lie in the single outside class, so u∈Λ². Conjugacy invariance gives every S-involution in Λ², contradicting even |H|.

If f is odd, Aschbacher–Seitz §19(19.3),(19.5), pp.76–77, gives one **S-class**, not merely an Aut(S)-class, of outside involutions, with centralizer R=²F₄(q). Its proof conjugates within the Sylow subgroup of S. Therefore

    |H|=|R|=q¹²(q⁶+1)(q⁴−1)(q³+1)(q−1).

Take primitive prime divisors r₁₂ of 2^(12f)−1 and r₄ of 2^(4f)−1; Zsigmondy has no exceptions at these exponents. Both divide |H|. Among the complete ordinary maximal list, parabolics, Sp₈(q), Ω₈⁺(q).S₃ and the A₂×A₂ forms miss r₁₂. The triality normalizer misses r₄: modulo r₄, q²=−1 and q⁸+q⁴+1=3, while r₄≥5, so none of its order factors q¹²(q⁸+q⁴+1)(q⁶−1)(q²−1)·3 supplies r₄. A proper subfield F₄(q₀), q=q₀^d with d≥2, misses r₁₂ because its largest defining2-exponent is12f/d≤6f. The exceptional q=2 subgroup PSL₄(3).2 has order24,261,120<35,942,400=|R|. The other Table1 case, PSL₂(27) at q=8, has order9828<8¹²≤|R| and is too small. Thus a maximal subgroup containing H must be the unique S-class of R-subgroups. Equality of orders yields H=C_S(α) for an outside involution α conjugate to τ. Since Λ is the entire outside class, α∈Λ; choose a nonidentity involution u∈H. Then αu is another outside involution, so u=α(αu)∈H∩Λ², a contradiction. This does not incorrectly keep τ fixed while conjugating H.

## Sp₈ as the actual canonical factor

Suppose G₀=T=Sp₈(q). Then T=G^(∞) is characteristic, since G/T is solvable and T is perfect. First establish C_S(T)=1 for the **actual** embedded T. A primitive prime r of 2^(8f)−1 divides |T|. Every ordinary maximal in the complete F₄ list other than Sp₈(q) misses r: their non-2 factors have q-exponents among1,2,3,4,6,12, none divisible by8; finite multipliers2,3 do not supply r. The subfield maximum exponent is≤6f<8f. The q=2 exceptional subgroup misses17. The q=8 exceptional PSL₂(27) has order9828<8¹⁶≤|Sp₈(8)|, so it cannot contain the actual T either. Consequently any maximal containing T is an Sp₈(q) of the same order, and equals T. Thus N_S(T)=T and C_S(T)=Z(T)=1. It follows that C_G(T) injects into M/S and has order at most2f.

Let j(X) count elements whose square is1, including the identity. Fulman–Guralnick–Stanton arXiv:1602.03611v2, Theorem4.3 and equation(12), gives

    Σ_(n≥0) uⁿ q^(n²) j(Sp_(2n)(q))/|Sp_(2n)(q)|
      = (1−u)⁻¹ ∏_(i≥1)(1+u/q^(2i))/(1−u²/q^(2i)).

All coefficients on the right are nonnegative. Every coefficient is bounded by the product at u=1. Its logarithm is at most Σ2q^(−2i)/(1−q^(−2i))≤8/9<1, so that product is<3. With n=4 and |Sp₈(q)|<q³⁶ this proves j(T)<3q²⁰. If f is even, the only further outer label of a square-one automorphism is the field involution. Connected Lang descent gives one coset class of size

    |Sp₈(q)|/|Sp₈(√q)|=q¹⁸∏_(i=1)^4(1+q^(−i)) < (3/2)q¹⁸,

since q≥4 and the logarithm of the product is<1/(q−1)≤1/3<log(3/2). For odd f there is no additional label. Thus j(Aut(T))<5q²⁰.

Restriction of original marks to T has each fiber of size at most |C_G(T)|: the ratio of two outside elements with the same restriction belongs to that centralizer in G. Therefore

    |Q|=|Λ|<10f q²⁰,
    |Q|=[S:I₀]≥q¹²(q⁴−1)(q⁸−1)/3.

For f≥2 the second exceeds the first: (q⁴−1)(1−q⁻⁸)>q⁴/2=2^(4f−1)>30f. The last inequality starts with128>60 at f=2 and persists as its left side multiplies by16. For f=1, Aut(Sp₈(2))=Sp₈(2), and the pinned [finite certificate](../code/verify_f4_sp8_q2.g) gives j(T)=1,371,136 and2j(T)=2,742,272<5,222,400, the required degree lower bound. This excludes this orientation without a quotient-folder assumption.

## Triality as the actual canonical factor

Suppose G₀=T or T.3, T=³D₄(q), and I₀=Sp₈(q). Again T=G^(∞) is characteristic. Conjugation by τ on the image of G in Out(T) is trivial because Out(T) is abelian. Since τ inverts the generating section K, that image has exponent at most2. The actual T.3 alternative has a genuine outer element of order3 and is impossible. We have G₀=T. With P=H∩T=T∩I₀, the **source-provided** product S=TI₀ yields

    [T:P]=q⁸(q⁸+q⁴+1),     |P|=q⁴(q⁶−1)(q²−1).                 (1)

For q=2, [T:P]=69888 and |P|=3024. The pinned [finite certificate](../code/verify_f4_triality_q2.g) checks all nine stored T-maximal classes, of orders258048,86016,12096,3024,2352,1296,1176,216,52. Only U₃(3).2 and S₃×L₂(8) have order divisible by3024. The first would give index4; intersecting its normal simple U₃(3) gives index at most4, impossible since its complete maximal list has largest order216. Thus P is conjugate to the listed S₃×L₂(8). Its S₃ involution maps to T-class2A. The two T-involution classes have sizes819,68796, and their square coefficients into2A are18,2268, checked also by the exact irreducible-character formula. Since Out(T)=C₃, every nonidentity involutory restriction of a mark is inner, and either such square captures2A. The original-mark argument at the end of this section therefore gives a contradiction.

For q>2, use Kleidman's complete maximal classification as explicitly restated with T-conjugacy in Liu–Dai–Gong2006 Lemma2.2/Table1, pp.1770–1771. Let B be a maximal of T containing P. Its parabolic possibilities have |B|/|P|=q⁸/(q+1) or q⁸/(q³+1), nonintegers. The A₂ torus normalizers have exact orders2q³(q³∓1)²(q±1); here

    |P|/|B|=q(q³±1)/(2(q²±q+1))>1  (q≥2),

so they are too small. The separate PGL₃/PGU₃ entries are also smaller: the corresponding ratios |P|/|B| are q(q³+1), q(q³−1). Remaining torus normalizers have order at most24(q²+q+1)²<|P| for q≥2.

A subfield ³D₄(q₀), q=q₀^r for an odd prime r, misses a primitive divisor of2^(6f)−1 in |P|, since its defining exponents are at most12f/r≤4f. The exponent6 exception occurs only at q=2, already treated. If r=2, a primitive divisor of2^(2f)−1 lies in q+1 and |P|. It misses the subfield order: q₀ has order4 modulo that prime, so q₀⁸+q₀⁴+1=3 and q₀⁶−1=−2, with q₀²−1=−2; the prime is at least5. Here f is even, so exponent2f is never the exceptional6. The omission of a nonmaximal r=3 subfield in the source list causes no issue. If B=G₂(q), then [B:P]=q² is a power of2, excluded by Guralnick1983 Theorem1, which lists all simple groups with a subgroup of prime-power index; G₂(q), q≥4, is absent. Therefore P equals a conjugate of the listed standard A₁(q³)×A₁(q) maximal subgroup of its exact order.

The embedding matters. Wilson §4.8.2 and §4.8.4, pp.136–139, constructs this representative from the long-root and short-root subgroups and exhibits its A₁(q) factor as long-root. Equivalently, in algebraic D₄ take the three mutually orthogonal outer simple roots cyclically permuted by triality γ and the orthogonal highest root θ, fixed by γ. Their commuting A₁ factors, with trivial centers in characteristic2, have fixed group A₁(q³)×A₁(q) under γF_q; x_θ(1) is in the second factor. Identification with the listed conjugacy representative is a retained embedding input, supported by Wilson's construction, not an inference from order alone. Hence P contains a T-long-root involution.

Liebeck's *On products of involutions in finite groups of Lie type*, p.7, gives the two involution classes of T in characteristic2 and a nonroot representative diagonal in the standard A₁(q)×A₁(q³). For q>2 the long-root class square contains a long-root involution by taking distinct nonzero parameters in its root group; all nonzero parameters are conjugate. The nonroot class square does too: keep its nonidentity A₁(q³) coordinate fixed and vary two distinct nonzero root parameters in the A₁(q) coordinate. Their product has only the long-root coordinate.

For even f, involutory outer restrictions add the unique field label. Put q=s² and realize T=𝔇^(γF_q) in connected algebraic D₄. The Steinberg endomorphism F₀=γ²F_s satisfies F₀²=γF_q and fixes x_θ(1). Lang–Steinberg gives one T-class of outside involutions: a cocycle xF₀(x)=1 has x=y⁻¹F₀(y), and then F₀²(y)=y, so y∈T. Thus F₀ and F₀x_θ(1) are conjugate involutions and their product is long-root. This is also the triality descent in the reviewed exceptional manuscript. For odd f there is no outer involution label.

Finally, at least one λ∈Λ has nontrivial action on T; otherwise t∈Λ and K=tΛ would centralize the nonabelian T despite generating G≥T. Its T-conjugates remain actual marks. Their pairwise products lie in T, and the centerless action of T identifies these products exactly with the corresponding class-square products in Aut(T). For q=2 they capture every2A element; for q>2 every long-root involution. In each case the identified P contains such an element, contradicting H∩Λ²={1}. No triviality of C_G(T), quotient loop, or τ-invariance of H was needed in this orientation.

## Evidence and remaining scope

The source authors read and ran both finite certificates under GAP4.15.1/CTblLib1.3.11; their classifications, subgroup fusions and character values remain explicit inputs. Uniform deductions use the exact primary statements recorded in REFERENCES; the CFSG and subgroup classification proofs are not reproved here. Independent mathematical review of the corrected exact source is recorded below. Repository integrity is separate and cannot certify the theorem. E₆/²E₆, odd E₇, remaining classical socles and operation-level classification remain open.


Source correction before final review: revision `0be7a92cf3faa34602fe6aad492138102cfa1d73` omitted the q=8 PSL2(27) Table1 case and misstated which factor contains the primitive divisor in the quadratic triality subfield argument. The source authors found the former by inspecting the full Table1/Proposition4.14; reviewer C found the latter. The current text includes both corrections. The two earlier provisional acceptances of that revision were withdrawn; fresh exact-source reviews of the corrected source are recorded below. Neither finite certificate changed.


## Independent corrected-source review

Three independent automated-model reviewers accepted exact corrected source `4d5ba4746ef45bdbeae9d570ee306fe04b8f7463`: reviewer A, reviewer B, and reviewer C. Each audited the entire division and original-mark arguments, and freshly inspected the complete characteristic-two Table1 possibilities, including PSL2(27) at q=8, and the corrected primitive-divisor factor. The rank-three reviewer requested the sign correction at the first revision; the other two explicitly withdrew their provisional first-revision acceptances after the two corrections were identified. All three then accepted the revised mathematical statement under its listed external inputs.

Each had independently read, extracted and run both GAP certificates at `0be7a92cf3faa34602fe6aad492138102cfa1d73`; the files are identical at the corrected source, and the re-reviews explicitly reuse those successful runs rather than claim new execution. The paired-simple reviewer also freshly inspected FGS Theorem4.3, Liu-Dai-Gong Lemma2.2/Table1 and Liebeck's triality class passage in the initial audit; the other primary-source interfaces retained the source authors's inspections and their explicit input status. None claims to rederive the classifications or certify an embedding from order alone. Both exact source commits are locally available. Repository integrity separately passed115 tests under Python3.12.14 after the corrections; that is not mathematical proof. These are research reviews, not formal GitHub approvals. C0010 and global classification remain open.
