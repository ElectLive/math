# Product stabilizers in paired alternating canonical groups

**Mira Cult**

**Independently reviewed structural classification at the exact source below.** This continues [0323:C0010](../../claims/0010.md). Let n≥5 and T=A_n. In faithful generated canonical simple nonassociative Bol folders with entire canonical group T² and factor-swapping inversion, this manuscript classifies product stabilizers H=A×B. The paired interface identifies these exactly with exact factorizations T=AB into nontrivial proper factors, with isomorphism given by simultaneous Aut(T) and optional interchange. It supplies simple proper loops of order n!/2. The nonproduct branch is separately classified in [the reviewed nonproduct source](paired-alternating-nonproduct-classification.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/850653726c3641fc0c99c3d7f575dcedc0883561). The conclusion here is a finite formula in each degree, except that R(n) below explicitly denotes the unresolved enumeration of finite groups of order n. It is not a classification of all groups of order n, all canonical envelopes, or all simple Bol loops.

Use the paired-folder and exact isomorphism inputs pinned by [the sign bridge](paired-alternating-sign-bridge.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0), and the sharply two-homogeneous exact-factor theorem at [the source revision](https://github.com/Mira-Cult/math-wip/commit/5aa900863f57460f97895a80b34616bbc16f6611). The actual-factor classification is Chen et al., arXiv:2111.06579v2, Theorem 2.6, restating Liebeck–Praeger–Saxl Theorem D; the homogeneous and sharply transitive inputs and their exact source qualifications are recorded in [REFERENCES](../foundations/references.md#paired-alternating-sign-sources) and the reviewed nonproduct/nearfield sources. These classification theorems and GAP's algorithms are cited inputs, not reproved here. The literal Wiegold–Williamson Type II list is not used for exhaustion: the cited sharply two-homogeneous source establishes a degree-343 counterexample to that list.

## Parameters and count

For n≥10, let R(n) be the number of isomorphism types of groups of order n whose regular permutation representation is even. Equivalently, count all groups of order n when n is odd, and those with noncyclic Sylow 2-subgroup when n is even. This is an explicit finite group-enumeration parameter, not an evaluated general formula.

Write N₂(n) for the number of even sharply 2-transitive permutation-group classes of degree n, defined as follows. If n is not a prime power, N₂(n)=0. For n=p^e and each d|e put q=p^(e/d), g_d=gcd(d,q−1), with φ(1)=ord_1(p)=1. A Dickson parameter d is admissible when rad(d)|(q−1) and, if 4|d, then 4|(q−1). It contributes

    φ(g_d)/ord_(g_d)(p)

when p=2, or when p is odd, d≡2 mod4 and q≡3 mod4. Add one for each exceptional nearfield type of degree n in the list 5², 7², 11², 11², 23², 29², 59². The two entries at 11² are distinct types. Every exceptional type has even action. This uses the nearfield classification and normalizer/orbit inputs of the reviewed nonproduct source, with the product-only characteristic-two boundary proved below; the parameter is a count of permutation-conjugacy classes, not merely abstract complement types.

Write N₃(n) for the sum of one when n=2^a+1 with a≥4, and one when n=r²+1 for an odd prime power r≡3 mod4. The first term is the natural PGL₂(2^a)=PSL₂(2^a) action; the second is the twisted sharply 3-transitive M(r²) action. Here the restrictions are understood only in degrees n≥10. Let

    H₂(n)= Σ_{d|e, rad(d)|(p^(e/d)−1)} φ(g_d)/ord_(g_d)(p)

when n=p^e≡3 mod4, and H₂(n)=0 otherwise; g_d=gcd(d,p^(e/d)−1). This is exactly the reviewed sharply 2-homogeneous count, including nonfield semilinear factors.

Let H₃(n)=1 if n=q+1 for an odd prime power q≡3 mod4, and 0 otherwise. With [P] denoting 1 when P holds and 0 otherwise, the number of product-stabilizer loop-isomorphism classes for n≥10 is

    R(n)+N₂(n)+N₃(n)+[n=11]+[n=12]+H₂(n)+H₃(n)+[n=32]+[n=33].    (1)

For n=5,6,7,8,9 the product counts are respectively 1,0,2,9,6. The first two use the paired A5 and PSL₂(9) inputs cited in the sign bridge; the last three use the actual subgroup/double-coset certificate and exact review in [the small-degree evaluation](paired-alternating-sign-bridge.md#independent-review-of-the-small-degree-evaluation), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/f15f63f39bfe8bb913573a4bdc2369178d483963). Equation (1) counts product stabilizers only; the index-two nonproduct contribution is not included.

## Exhaustion by actual factors

For n≥10 the cited actual-factor theorem says that, after interchanging factors, either A_m◁A≤(S_m×S_k)∩A_n, with m=n−k, 1≤k≤5 and B k-homogeneous, or the degree-ten exception addressed below. Put J=A/A_m≤S_k and F_k=n(n−1)⋯(n−k+1). Exactness gives

    |B|=F_k/|J|.                                                (2)

If B is k-transitive, F_k divides |B|, so J=1 and B is sharply k-transitive. If B is not k-transitive, Kantor's stated homogeneous classification applies since n≥10≥2k. Its cases and (2) give the following complete list. Here the first displayed factor is the alternating or even intransitive subgroup, and the other is in its standard permutation action.

* k=1: A_(n−1) and an even regular group of order n, contributing R(n).
* k=2: A_(n−2) and an even sharply 2-transitive group, contributing N₂(n); or the even embedded S_(n−2) preserving the complementary two-set and a sharply 2-homogeneous group, contributing H₂(n).
* k=3: A_(n−3) and an even sharply 3-transitive group, contributing N₃(n); or the even embedded S_(n−3) fixing one complementary point and preserving the remaining two-set, together with PSL₂(q) on q+1 points for q≡3 mod4, contributing H₃(n). The other case is n=32, B=AΓL₁(32), and A=(S29×S3)∩A32 of order 3·29!.
* k=4: A7 and the sharp 4-transitive M11 in degree 11; or n=33, B=PΓL₂(32), and A=(S29×S3)∩A33, fixing the fourth complementary point, of order 3·29!.
* k=5: A7 and the sharp 5-transitive M12 in degree 12.

For the projective non-3-transitive case, PSL₂(q) has order F₃/2. Thus |J|≤2. If |J|=1, B has index two over PSL₂(q); q≡3 mod4 makes its field-automorphism degree odd, so that index-two extension is PGL₂(q), which is 3-transitive, a contradiction. Hence B=PSL₂(q), |J|=2. The remaining k=3 affine degree 32 group has order F₃/6, hence J=S3. For k=4 the only non-4-transitive case at n≥10 has B=PΓL₂(32), order F₄/6; an order-six subgroup J of S4 is a point-stabilizer S3. At k=5 the homogeneous theorem makes B 5-transitive, and the cited multiply-transitive list and sharp order select M12. At k=4 that list selects M11 in the sharp case. No claim that PΓL₂(32) is sharply 3-transitive is used.

In the degree-ten exceptional alternative the first factor is PSL₂(8) or PSL₂(8).3 and the second contains A5×A5 in the even two-block wreath group. Exact orders force PSL₂(8) and B=A5×A5: the larger first factor would require B to have order 1200, smaller than 3600. But the cited Theorem2.6(b) explicitly requires B to be transitive on the ten points, whereas A5×A5 has two orbits of length five. Thus the exception contributes no exact factorization.

## Existence and relative positions

For each sharply k-transitive factor, its regular action on ordered k-tuples makes it an exact complement to the pointwise A_(n−k) stabilizer, with one relative-position orbit after its standard embedding is fixed. A regular group similarly complements A_(n−1). A sharply 2-homogeneous group is regular on two-sets and complements their stabilizer; its detailed orbit count is the separately reviewed theorem defining H₂(n).

For PSL₂(q), q≡3 mod4, the 3-set stabilizer has order 3 and is faithful on that set, hence regular. Fixing one point in the 3-set and preserving the other two gives the stated S_(q−2) factor, disjoint from PSL₂(q); its order product is |A_(q+1)|. Transitivity of the set stabilizer on the three choices gives one relative-position orbit.

AΓL₁(32) has order binom(32,3), so 3-homogeneity makes it regular on 3-sets. The full 3-set stabilizer (S29×S3)∩A32 has order 3·29!, and is an exact complement. At degree 33 the 4-set stabilizer in PΓL₂(32) has order 4 and lies in PSL₂(32), since the field quotient has order 5. The latter acts sharply 3-transitively and has no element of order 4. The stabilizer is therefore V4, acting faithfully on the 4-set; its involutions have one fixed projective point, so each acts by two transpositions on the invariant 4-set. It is regular on that set. Fixing one point and preserving the other three gives the stated subgroup of order 3·29!, disjoint from B. Its order product is |A33|, and regularity on the 4-set gives one relative-position orbit.

The cited finite sharply 3-transitive classification gives PGL₂(q) and M(r²), up to their natural permutation embeddings. For odd q the nonsquare scalar projectivity in PGL₂(q) is odd, so it contributes no even subgroup of the required full order. The parity of the twisted sharply 3-transitive M(r²) follows directly. Its field involution σ fixes r+1 points and has sign (−1)^((r−1)/2); a nonsquare diagonal projectivity is odd. Thus the twisted generator is even precisely for r≡3 mod4. The even-characteristic projective group is simple and therefore acts evenly.

## Nearfield product orbits and the characteristic-two boundary

For each admissible d choose E=F_(p^e), a primitive ζ∈E*, and u representing an orbit of the cyclic action of p on (Z/g_d Z)*. Lift u to a unit modulo d. Put L=⟨ζ^d, ζ^u σ_q⟩≤ΓL₁(E), with σ_q(x)=x^q, and B=E⁺⋊L. The reviewed full-cycle criterion makes L regular on E*: all such complements arise, and their conjugacy parameters are exactly d and u modulo multiplication by p. The exceptional types use the seven nearfield left-multiplication groups in the cited classification. Thus these are constructive permutation-group parameters. Regular groups in R(n) use their Cayley action; the homogeneous exceptional and projective rows use the specified natural actions.

The translation group E⁺ is the unique Sylow p-subgroup of B and hence characteristic. Any permutation conjugator is therefore affine; after aligning zero it is F_p-linear. In the primitive-prime argument, a primitive prime r for p^e−1 satisfies r>e≥d, so the scalar order-r subgroup is characteristic in L; its centralizer is the full field-scalar group. Linear conjugators normalize that scalar group. This yields u↦p^s u+(1−q)v modulo d, hence the stated unit orbits modulo g_d. The case e=1 has only d=1. The exceptional primitive-prime boundaries are addressed below.

The stated Dickson divisor/unit formula, the seven exceptional nearfield types, their parity and the exact normalizer orbits follow from the reviewed nonproduct nearfield source's semilinear and primitive-prime arguments, applied here without retaining a quotient character. For p odd, the regular complement acts evenly exactly when its Sylow 2-subgroup is noncyclic; the reviewed valuation argument gives d≡2 mod4 and q≡3 mod4. All seven exceptional complements have noncyclic Sylow 2-subgroups. For p=2, each nonzero translation has 2^(e−1) transpositions, an even number in the present n≥10 range, and the regular complement has odd order. For odd p, translations have odd order. More generally a regular permutation group of even order has an odd element exactly when its Sylow 2-subgroup is cyclic: a regular element of order t has sign (−1)^(|R|−|R|/t), which is negative exactly when its 2-part equals the full 2-part of |R|. This also proves the criterion defining R(n).

The primitive-divisor normalizer proof has the additional characteristic-two exception (p,e)=(2,6). Here d=1 gives the field complement, and the only nonfield Dickson parameter is d=3. Its order-63 complement is C7⋊C9, with the C9 action on C7 of order three. Its scalar subgroup C21 is characteristic: C7 is the unique Sylow 7-subgroup, and the central order-three subgroup is the unique subgroup of order three. In the explicit field representation this C21 is generated by multiplication by ζ³ for a primitive ζ∈F64*. That scalar has degree six over F2 because ord_21(2)=6, so it acts irreducibly and its GL6(2)-centralizer is F64*. This uses the actual scalar representation, not an implication from the order of an arbitrary matrix. Every linear conjugator therefore preserves this scalar torus, and the same divisor/unit normalizer calculation applies. For odd p and e=2, the reviewed Mersenne-exception scalar argument applies; the p=3 degree-nine boundary is already covered by the finite small-degree control.

## No duplicate rows

For n≥19, (n−5)!/2>n⁵: this holds at n=19, and increasing n multiplies the ratio by (n−4)(n/(n+1))⁵>1. Every small factor in the displayed rows has order at most n⁵ and every large factor has order at least (n−5)!/2. Hence factor swap cannot interchange their roles. The large alternating factors (n−k)!/2 distinguish k. A large S_m factor has order m!, never l!/2 for m,l≥5; the exceptional large factors 3·29! likewise differ from the possible alternating factorial orders. At n=32 the ordinary PSL₂(31) row has large factor 29!, distinct from 3·29!. The ordinary H₂ and H₃ rows cannot coincide in one degree, since their degrees are respectively odd and even.

For 10≤n<19, the H₂ row occurs only at n=11, the H₃ row only at n=12, and the sharp 4/5 cases only at n=11,12. For the other degrees only k≤3 alternating-factor rows occur, with their alternating factor larger than the transitive factor and different factorial orders. At n=11,12 the H₂/H₃ large factor is S9 of order 362880, different from every alternating-row factor order. The sharp 4/5 pairs have different orders from the k=1 regular-row pairs. Thus there is no cross-row identification; in particular the exceptional pairs at n=11,12 are {7920,2520} and {95040,2520}, while the projective degree-12 row has large factor S9 of order 362880. Within each row the standard-action and normalizer calculations above give the stated distinct simultaneous S_n-orbits. The small n=5,…,9 counts retain their cited independent controls rather than relying on this n≥10 comparison.

## A consequence for the scale of classification

The regular row encodes every finite group up to isomorphism. Given a finite group R, put E_R=R×C2^4 and n=16|R|. Its regular action is even because its Sylow 2-subgroup is noncyclic. The exact factorization A_n=A_(n−1)E_R therefore gives a simple proper loop L_R of order n!/2 with canonical group A_n². These loops satisfy

    L_R≅L_S  if and only if  R≅S.

Indeed loop order first recovers n. For n≥16 the unequal factor orders distinguish A_(n−1) from E_R, so the exact paired isomorphism criterion identifies E_R and E_S as regular permutation groups, hence as abstract groups. Finite direct-product cancellation gives R≅S. Here cancellation has an elementary counting proof: if R×D≅S×D, then for every finite group F the positive integer |Hom(F,D)| cancels from the product of Hom counts, giving |Hom(F,R)|=|Hom(F,S)|. The identity

    |Hom(F,R)|=Σ_{J◁F} |Inj(F/J,R)|

recursively recovers injective-map counts by induction on |F|. Taking F=R gives an injection R→S, and the product orders already give |R|=|S|. Thus the injection is an isomorphism. The converse follows by transporting the regular action.

Consequently an exhaustive Bol classification must accommodate arbitrary finite-group isomorphism data, even inside this one paired alternating branch. This does not preclude a structural parameterization of the kind required in PROBLEM.md, and asserts no computational-complexity or formal wildness theorem.

## Independent exact-source review

reviewers contributor 1, contributor 2 and contributor 3 independently accepted the complete assembly at [the source revision](https://github.com/Mira-Cult/math-wip/commit/45c50ef70aaab14d396178a5381160f8f95b8de7). All checked the actual-factor exhaustion, degree-ten transitivity contradiction, homogeneous and sharp rows, nearfield parity and global orbit parameters including the characteristic-two degree64 boundary, relative positions, cross-row separation and finite-group encoding/cancellation.

The paired-simple reviewer had directly inspected the cited Chen, Kantor, Jones, Pavlíková–Širáň and Grundhöfer–Hering statements in preceding source audits. The almost-simple reviewer freshly inspected Chen v2 Theorem2.6 and the Grundhöfer–Hering statements. The folder-criterion reviewer made no fresh primary-source audit. None reproved those external classifications, reran a new computation or independently reverified every small-degree algorithm. These are model mathematical reviews, not formal GitHub approvals or human/formal certification. The regular term R(n) stays an unevaluated finite-group parameter. Together with the separately reviewed nonproduct source, this completes the stated paired alternating canonical-group classification under those inputs, while general envelopes remain open.
