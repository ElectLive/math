# Transvection products and actual classical stabilizer intersections

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source mathematical review recorded below. We prove three scoped exclusions for actual factor pairs of an almost-simple full multiplication group with socle PSL_n(q): the odd-characteristic vector-parabolic component side for SL_a(q^b) with a≥3 and for Sp_a(q^b) with a≥4; the symplectic canonical side of the symplectic/SL_(n−1) antiflag pair for even n≥6 in every characteristic; and its opposite linear canonical side for every even n≥4 and every q, with a separate n=4,q=2 route. These statements retain the precise natural embeddings below. They do not classify arbitrary component embeddings or loop operations.

Let Q be a finite simple proper left Bol loop, M=Mlt(Q) almost simple, G=LMlt(Q), I=M_1, and H=G∩I. Use the definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. In the actual formal extension, Λ=τK is G-invariant, consists of involutions, contains τ, satisfies H∩Λ²=1 and has ⟨τΛ⟩=G. All products below use these actual marks.

## A moved transvection gives a low-rank actual product

Suppose L is a characteristic perfect subgroup of G, is an intermediate central quotient of a natural SL_a(R) or Sp_a(R), and every automorphism of L preserves the images of natural transvections. Those images generate L. Some λ∈Λ acts nontrivially on L: otherwise τ and τΛ would centralize L, forcing G to centralize its own nonabelian subgroup L. Choose a transvection image u moved by λ. With the convention u^λ=λ⁻¹uλ and λ^u=u⁻¹λu,

    x=λ^u λ=u⁻¹u^λ ∈ L∩Λ²,        x≠1.              (1)

Let π denote the natural matrix group's central quotient onto L. There are genuine transvections U,V with π(U)=u and π(V)=u^λ. The matrix g=U⁻¹V represents the actual x, and

    rank_R(g−1) ≤ 2.                                  (2)

No assertion says g or x is an involution. No quotient-folder hypothesis or lift of λ to an involution is required. Nontriviality is in the original L, by the choice of u.

For completeness, transvection generation can be seen directly from elementary generators of SL and the symplectic root generators. In type C, the long-root generators are transvections t_v(c):z↦z+cB(z,v)v. If B(v,w)=0, the identity

    t_(v+w)(c) t_v(−c) t_w(−c)
      = 1+c[v B(−,w)+w B(−,v)]

expresses each standard short-root generator as a product of transvections by taking the appropriate distinct hyperbolic basis vectors v,w. The standard root generators generate the natural symplectic group. Thus no assumption that all transvections form one rational conjugacy class is used.

## Automorphism and central-quotient interface

Robert Steinberg, *Automorphisms of finite linear groups*, Canadian J. Math.12(1960),606–615, §3 Theorem3.2, printed p.608, with the group identification in §2 p.607 and graph discussion pp.607–608, [primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16023F257E0F21D57873B1450E9F15E4/S0008414X00010245a.pdf/automorphisms-of-finite-linear-groups.pdf), supplies the inner, diagonal, field and graph decomposition. The coordinator and source auditor freshly inspected these statements. Type A uses linear conjugation, field maps and inverse transpose. All preserve natural transvections: inverse transpose sends 1+N to 1−Nᵀ for N²=0 of rank one. Type C of rank at least three, and type C2 in odd characteristic, has only symplectic similitude conjugation and field maps, also preserving transvections. The exceptional B2/C2 graph automorphism is in characteristic two and is not included in that assertion. In particular PSp4(3) is covered by the ordinary odd-characteristic description.

This simple-quotient theorem suffices for every intermediate scalar quotient L=T/Z0 of the displayed perfect natural matrix group T. An automorphism α of L induces one on T/Z(T). Choose a standard matrix-group automorphism β inducing that simple-quotient action. Its action preserves Z0 because the scalar center Z(T) is cyclic. Therefore β descends to L. The discrepancy from α induces identity modulo Z(L) and is of the form z↦z c(z), where c:L→Z(L) is a homomorphism. Perfectness makes c trivial. Hence α itself preserves the images of genuine transvections. We do not assume that T is a universal central extension, so no claim about exceptional Schur multipliers is needed.

The small groups in the applications below have nonabelian simple central quotient: SL_a(R), a≥3 and odd R≥9 in the extension-field case; Sp_a(R), a≥4 and odd R≥3; and Sp_n(q), n≥6 for any q. All these natural groups are perfect. The separate odd-dimensional SL_d(q), d≥3, used in the last section is also perfect with simple central quotient, including SL3(2) and SL3(3).

## Odd-characteristic vector-parabolic component sides

Use Li–Wang–Xia, *Factorizations of almost simple linear groups*, arXiv:2106.03109v2, definition of tight containment, Theorem1.2/Table1.1 row1, printed p.2, and Lemmas4.1–4.2, pp.4–5, [primary version](https://arxiv.org/html/2106.03109v2). Suppose actual (G,I) tightly contains (X,Y), with Y the nonzero-vector stabilizer in PSL_n(q), q odd, and either:

* X=image SL_a(R), R=q^b, n=ab even, a≥3,b≥2; or
* X=image Sp_a(R), R=q^b, n=ab, even a≥4,b≥1.

Tight containment includes equality of perfect residuals. Since X is perfect here, L=G^(∞)=X is characteristic in G, and X∩Y≤H. The source lemmas give the actual common restricted-scalar embedding, transitivity on all nonzero R-vectors, and the full vector-stabilizer intersection. Apply (1)–(2) and the preceding automorphism interface. Since a≥3, g fixes a nonzero R-vector. Transitivity of the covering natural group conjugates it into the stabilizer of the specific vector defining Y. After projection this gives a nonidentity element of H∩Λ², contradiction. The determinant-one vector-fixing representative is actual; a projective scalar quotient is not assigned a faithful natural module.

Together with the reviewed characteristic-two component result at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, this treats every symplectic vector-parabolic component side and every linear one with a≥3. The opposite parabolic orientations are independently reviewed at that source and at `d95f900af71ff43fcc5486345a0c24f7eb47f6da`. The odd-characteristic a=2 linear component side is not covered by (2), since a rank-two displacement may have no fixed vector.

## Symplectic canonical side of the antiflag pair, n≥6

Now let n≥6 be even and q arbitrary. Use LWX v2 Theorem1.2/Table1.1 row3 and Lemma4.5, printed p.6. In its common natural model X=image Sp_n(q), and Y=image SL_(n−1)(q) fixes an actual nonzero vector and a complementary hyperplane. Suppose actual (G,I) tightly contains (X,Y). Then L=G^(∞)=X=PSp_n(q), and H contains the projective image of Sp_(n−2)(q) fixing a specified nondegenerate symplectic plane pointwise. The source proof identifies this embedded intersection, not merely its order.

The standard automorphism interface applies in symplectic rank at least three for every q. Use (1)–(2) in the natural n-dimensional symplectic module. Let W=ker(g−1). Then dim W≥n−2 and dim rad(W)≤dim W^⊥≤2, so dim(W/rad(W))≥n−4≥2. Therefore W contains a nondegenerate symplectic plane. A symplectic conjugation carries this plane to the source model's specified plane; g fixes it pointwise and preserves its orthogonal complement. Its projective image is then in H∩Λ² and remains nonidentity. This contradiction excludes every stated actual overgroup.

For odd q the scalar kernel {±1} is explicitly removed in X, but the matrix product g is taken before projection. We do not lift an arbitrary projective involution through that even kernel. For n=4 the fixed-space estimate does not guarantee a nondegenerate plane, so this proof leaves the symplectic canonical orientation open there, except q=2 below.

## Linear canonical side of the antiflag pair, all even n

Reverse the actual orientation: G tightly contains Y and I tightly contains X. Exclude (n,q)=(4,2) for the moment. Put d=n−1, odd. In the common model Y is the genuine SL_d(q) embedded as 1⊕SL_d(q); it has no projective scalar kernel, since its representative fixes an actual nonzero vector. Thus L=G^(∞)=Y is perfect, with odd center of order gcd(d,q−1) and simple central quotient PSL_d(q). The actual H contains C=Sp_(d−1)(q), acting on a (d−1)-dimensional complement and fixing a remaining line in L's d-dimensional natural module.

Every nonidentity L-involution class meets C. In characteristic two its Jordan form is 2^r1^(d−2r), 1≤r≤(d−1)/2. A product of r symplectic transvections on distinct orthogonal hyperbolic planes in the C-module realizes that rank. There is at least one Jordan1-block since d is odd; scaling on that block shows the GL_d centralizer has surjective determinant, so a GL_d conjugator can be adjusted to lie in SL_d. In odd characteristic an SL_d involution has negative eigenspace of even dimension 2r≤d−1. Act as −1 on a nondegenerate symplectic 2r-space inside C and as +1 elsewhere. The eigenspace centralizer again has surjective determinant, so this realizes the actual SL_d class. These are statements about genuine L-involutions, not projected class labels.

The general odd-central characteristic-component obstruction in [the marked involution/vector manuscript](marked-involution-vector-obstruction.md), independently reviewed at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, now applies: every L-involution class meets H, contradicting the actual marked-square collision. Its proof supplies the actual involution by an odd power of a marked product and does not require a quotient loop. This excludes the linear canonical orientation for every remaining q,n.

For (n,q)=(4,2), the full socle is A8. The reviewed all-alternating full-action reduction at `b782384e807bb07f6197b2a06fd732fe8c6e5c8a` forces the natural degree8 action, excluded by the independently reviewed minimum proper-loop order24 input of C0011 at `932ead5db5f39045e2085caa6b062f6b981b2813`. This closes both orientations at this endpoint.

There is a source-formula boundary worth recording: Lemma4.5 displays Sp_(n−2)(q) as the intersection while also using Sp4(2)'=A6 in its exceptional case. At (4,2), the asserted factorization and orders give 360·168/20160=3, not |Sp2(2)|=6. Our intersection argument explicitly omits that endpoint and uses the separate reviewed A8 exclusion. We neither silently use the full Sp4(2) in place of its derived subgroup nor infer the displayed exceptional intersection from its notation.

## Evidence and remaining scope

The coordinator freshly inspected the cited Steinberg and LWX statements, and two proof-development agents supplied independent derivations of the rank and involution-coverage steps. Those contributions are not independent acceptance of this assembled source. No new computation is required; the order3 endpoint check is elementary arithmetic. Independent exact-source mathematical review is recorded below. The remaining boundaries include the odd-characteristic SL2 vector-parabolic component side, the Sp4 antiflag canonical side for q≥3, the other LWX actual factor pairs, and classification of loop operations. C0010 remains open.

## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted all three stated scopes at exact source `bc837277fd94e4a4184c2843319fbff86331aa4a`: contributor 1, contributor 2, and contributor 3. Each checked the actual moved-transvection identity, rank bound, transvection generation, intermediate central-quotient automorphism transfer, fixed-vector and fixed-plane applications, and both-characteristic coverage of all genuine involution classes of odd-dimensional SL. They checked the actual tight-containment/characteristic-component interfaces and the separate A8 route for the inconsistent (4,2) displayed intersection. Acceptance retains the canonical collision, Steinberg automorphism classification, stated LWX common embeddings away from the bypassed endpoint, and pinned odd-central/A8 inputs.

The paired-simple reviewer freshly inspected Steinberg Theorem3.2 and graph exceptions, and LWX v2 Lemmas4.1,4.2,4.5 including the antiflag model. The presentations reviewer had freshly inspected those LWX lemmas in the immediately preceding audit and retained Steinberg; the S5 reviewer retained both primary sources without a fresh audit. None ran a new computation or rederived the external classifications. The exact source is locally available, and repository integrity separately passed115 tests with Python3.12.14. These are research reviews, not formal GitHub approvals. The odd-characteristic SL2 vector case and Sp4(q), q≥3, symplectic antiflag orientation remain outside this proof, along with the other factor pairs and complete classification.
