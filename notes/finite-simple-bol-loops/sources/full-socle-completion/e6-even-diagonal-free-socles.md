# Diagonal-free even E6 full multiplication socles

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source mathematical review recorded below.

**Proposed theorem.** Under the canonical and classification inputs below, no finite simple proper left Bol loop Q has full multiplication socle E6(2^f) with f odd, or twisted 2E6(2^f) with f even. These are the respective characteristic-two fields with trivial diagonal outer subgroup. The complementary fields, odd characteristic and the unrestricted classification remain open.

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. These are scoped dependencies, not promotions of aggregate claims. The original marked extension has the G-invariant outside involutions Lambda=jK with the formal outside involution j in Lambda, K generating G, |Lambda|=[G:H] and H intersect Lambda^2={1}. Once G=S and inversion is outer, restriction faithfully identifies this formal extension with the corresponding subgroup of Aut(S). No quotient folder or invariance of H under inversion is assumed.

## Reduction and small graph-class selection

C0008 gives faithful primitive almost-simple M=Mlt(Q), M=GI with I=M_1 and H=G∩I. If S is not contained in G then S is not contained in I, since S normal in M and contained in I would lie in the action kernel. This would be a proper factorization, excluded for E6 by Kazarin–Martínez-Pastor–Pérez-Ramos (2015), Lemma 11 pp.56–57, citing Liebeck–Praeger–Saxl 1990 Theorem B; their full exceptional list is G2(3^c), G2(4), F4(2^c). Thus S≤G≤Aut(S). Burness–Guralnick–Harper arXiv:2006.01421v2 §3.2 Table 2 p.19 gives cyclic Out(S) of order 2f in precisely these d=1 ranges. Its unique order-two label is the graph automorphism. Restriction embeds Aut(G) in Aut(S); its action on G/S is trivial because Out(S) is abelian. Canonical inversion inverts G/S, making it exponent 2. If G>S its quotient contains the unique outer order-two label, making every involutory automorphism of G inner, excluded by reviewed source `84eba0ffd4dfab4b6d64853a3131010ad2b945b8` because O2(G)=1. Hence G=S and τ has graph label.

Aschbacher–Seitz, *Involutions in Chevalley groups over fields of even order*, §19 (19.8)–(19.9) pp.80–81, gives two Aut(S)-classes in the graph coset, represented by the pinned graph σ and σt for t=U_r(1) in the highest-root group; their centralizers are F4(q) and the centralizer of a 2-central involution in F4(q). Since no diagonal outer automorphism is present and the generating field automorphism fixes both σ and t, both representative centralizers surject onto Out(S). Thus both Aut(S)-classes are already S-classes. The smaller class is σ^S and its centralizer is F4(q). The actual marked set is one of these two whole S-classes or their union. In this first case assume it is the smaller class, so |H|=|F4(q)|.

The following maximal-subgroup audit shows that H is an S-conjugate of the natural F4(q). By Guralnick–Robinson arXiv:2012.08693v1 §3.3 pp.4–5, that F4(q) meets every internal involution class of S. It therefore suffices to exhibit one nonidentity internal involution in Λ². For untwisted S choose orthogonal simple roots α,β interchanged by σ and let x=x_α(1); then σσ^x=x_β(1)x_α(1) is such an involution. For twisted S, use F=σF_q and choose u∈F_(q²) with u+u^q≠0. Then x=x_α(u)x_β(u^q) lies in S, and σσ^x=x_α(u+u^q)x_β(u+u^q), again a nonidentity involution. Λ² is S-invariant, so some conjugate of that element lies in H, contradicting H∩Λ²={1}. The formula uses actual marks, not a projected folder.

### Row-by-row proposed proof of the order-uniqueness lemma

Take q=2^f in one of the two scoped field ranges, and let S=E6(q) when f is odd, or S=²E6(q) when f is even. Let H≤S have |H|=|F4(q)|. Then |H|_2=q^24. By Zsigmondy's theorem choose a prime ℓ such that q has multiplicative order12 modulo ℓ; it divides q^12−1, hence |H|, and no q^j−1 for 1≤j<12. The only Zsigmondy exponent exception (2,6) does not apply. In particular ℓ is odd and ℓ≡1 mod12, so ℓ≥13.

Let H≤K<S be maximal. Apply Craven arXiv:2103.04869v4, Thm 1.1 and Tables 2,9 for E6 or Tables 3,10 for ²E6. Use only ordinary S-maximals; the rows below the novelty line are not maximals of S. In the untwisted range q≡2 mod3, e=(3,q−1)=1 and f is odd. In the twisted range q≡1 mod3, e'=(3,q+1)=1 and f is even, so q≥4. Since q is even, the table's parameter d=(2,q−1) is 1. The unused opposite-sign e or e′ multiplier may be3, but is odd and does not affect the 2-part screen. Thus the displayed central torus denominators and e/e' factors add no 2-part.

Untwisted Table 9:

* The four parabolics have Levi components Spin10+(q), SL6(q), SL2(q)×SL5(q), and SL3(q)×SL3(q)×SL2(q). Their odd factors divide products of q^j−1 with j≤10, together with q−1; in particular ℓ does not divide their orders. Their unipotent radicals are powers of 2 and do not change this.
* Among the nonparabolic subsystem rows, the 2-parts are bounded respectively by q^16 for PSL2×PSL6; 2q^9 for PSL3(q)^3.Sym3; 2q^9 for PSL3(q²)×PSU3(q); q^9 for PSL3(q³).3; 2q^12 for PΩ8+(q).Sym3; q^12 for ³D4(q).3; 2^7 for W(E6)-torus normalizers; 2^3 for the indicated (q²+q+1)^3.(3^{1+2}.SL2(3)) row; q^9 for PSL3(q)×G2(q); and q^6 for G2(q). All bounds are strictly less than q^24 for q≥2. The PSp8(q).2 row is explicitly restricted to odd p.
* The subfield row E6(q0).gcd(e,r) has q=q0^r, r an odd prime because f is odd; its 2-part is q0^36=q^(36/r)≤q^12. The additional ²E6(q0), q=q0² row cannot occur because f is odd. The 3-local row is explicitly restricted to p≥5.
* All ordinary Table 2 entries with p=2, including J3 and PSL2(11), occur at q=4; other p=2 entries at q=4 are likewise outside the odd-f range. Thus no finite Table 2 row survives in this range; novelty status is not needed for this exclusion.

Twisted Table 10:

* The four parabolic Levi components are PSU6(q), Spin8−(q), PSL3(q²)×SL2(q), and SL3(q)×SL2(q²). Their odd factors divide products of q^j−1 with j≤10: for the unitary factors use q^i−(−1)^i, and for Spin8− use q^4+1, which divides q^8−1. Thus none has ℓ.
* The nonparabolic subsystem bounds are q^20 for PΩ10−(q)×(q+1); q^16 for PSL2×PSU6; 2q^9 for PSU3(q)^3.Sym3; 2q^9 for PSL3(q²)×PSL3(q); q^9 for PSU3(q³).3; 2q^12 for PΩ8+(q).Sym3; q^12 for ³D4(q).3; 2^7 for W(E6)-torus normalizers; 2^3 for the (q²−q+1)^3.(3^{1+2}.SL2(3)) row; q^9 for PSU3(q)×G2(q); and q^6 for G2(q). Each is strictly below q^24 for q≥4. Again PSp8(q).2 is only listed for odd p, and the 3-local row only for p≥5.
* The only subfield row is ²E6(q0).gcd(e',r) with q=q0^r and r an odd prime; its 2-part is at most q^12. Table 3's only ordinary p=2 almost-simple exceptional possibility is Fi22 at q=2, excluded since q≥4; the Ω7(3) row is explicitly novelty. Thus no finite Table 3 row survives in scope.

Every maximal K other than F4(q) is therefore impossible by ℓ-divisibility or 2-part. The F4(q) row has the relevant e=1 or e'=1 and one S-class; because |H|=|F4(q)|, H=K is conjugate to that natural F4(q). This gives the small-graph-class collision above and completes that case, subject to independent verification of the source table transcription, 2-parts, root conventions, and prior external inputs. The proposed conclusion is source-dependent and is not a claim that Craven's classification was rederived.


## Large graph-class square

Use the E6 simple-root labeling of Aschbacher–Seitz §15 p.53: edges 1–3–4–5–6 and 2–4. The graph automorphism swaps α1,α6 and α3,α5 and fixes α2,α4. The highest root is θ=α1+2α2+2α3+3α4+2α5+α6. Put δ=θ−α2. The Cartan calculation verifies that δ is a root, θ−2α2 is not, θ is graph-fixed with <θ,α2∨>=1, and α1,α6,δ are pairwise strongly orthogonal. Set h=x_{−α2}(1). It is graph-fixed and commutes with the α1 and α6 root groups. The Chevalley root-string relation, in characteristic2, gives

 t^h=t x_δ(1).                                             (1)

All signs in these simply-laced root-group formulas disappear in characteristic2. Write λ=σt. For any x∈S, λ^x is an actual S-conjugate in the *same* outside class; thus λλ^x lies in that class square. The following choices produce three involutions:

1. With x=h, equation (1) gives λλ^h=x_δ(1), a root involution.
2. In split E6(q), choose x=x_{α1}(a) with a≠0. In twisted ²E6(q), choose x=x_{α1}(a)x_{α6}(a^q), a∈F_(q²), with s=a+a^q≠0. Then λλ^x=x_{α1}(s)x_{α6}(s), where s=a in the split case. These factors commute and give the two-root involution class.
3. In either case multiply the corresponding x from 2 by h. Since h commutes with both paired root groups, (1) gives

 λλ^x=x_δ(1)x_{α1}(s)x_{α6}(s).                         (2)

This works even at q=2: the trace map F_(q²)→F_q is onto, so the twisted choice exists, and no nontrivial torus scalar is required. The twisted choices are rational for F=σF_q, and h is rational because σ fixes α2 and its parameter 1.

The [standard-library root certificate](../code/verify_e6_three_roots.py) constructs the 72 E6 roots from that Cartan matrix, checks all the root relations just stated, and verifies that the Weyl word

 (4,3,1,5,4,3,6,5,4)

maps the unordered triple {δ,α1,α6} to {α2,α3,α5}. Aschbacher–Seitz §15 (15.1) and the explicit Weyl calculation on p.56 identify that latter triple with the third involution class. That page introduces its torus argument under q>2; the displayed Weyl-root identity itself is characteristic-independent, and AS (15.1)/(15.4) gives the class representatives and separation also at q=2. Their §15 p.55 similarly identifies the paired α1,α6 representative with the second. Over the algebraic closure, the commuting root coroot tori scale the three nonzero parameters independently, so (2) lies in that third geometric class. Burness–Thomas, *On the involution fixity of exceptional groups of Lie type*, Remark 2.2 and Proposition 2.3, printed p.8 and Table 5 p.10, https://seis.bristol.ac.uk/~tb13602/docs/BTh_revised_2.pdf, state the natural one-to-one correspondence between algebraic involution classes and finite T-classes. With this correspondence applied separately to E6(q) and ²E6(q), the three constructed rational involutions lie in the three distinct finite classes. In particular, no assertion is needed that the displayed Weyl word is fixed by the twisted Frobenius.

Consequently the S-invariance of the square of (σt)^S puts every S-involution into that square. In the canonical large-class branch here, if the actual Λ is (σt)^S, this forces H to have odd order, while the actual marked cardinality gives |H|=|C_{F4(q)}(t)|, which is even. This contradiction closes that branch under its separately retained actual outer-class, centralizer, source and canonical inputs. The root computation does not reprove AS class separation, Burness–Thomas correspondence or the full-socle classification; these remain explicit external inputs requiring separate review of this deduction.


## Selecting both graph classes

Let A be the smaller class and B the larger. Aschbacher-Seitz (19.7), with the covering condition verified in the proof of (19.9), gives the exact equality C_S(sigma*t)=C_S(sigma) intersect C_S(t)=C_F4(q)(t). The highest E6 root is graph-fixed and gives a long root of the fixed F4 root system: fixed roots retain squared length2, whereas the folded pairs give the short roots. Burness-Thomas Table5 gives

    c_A=|F4(q)|=q^24(q^12-1)(q^8-1)(q^6-1)(q^2-1),
    c_B=|C_F4(q)(t)|=q^15|Sp6(q)|=q^24(q^6-1)(q^4-1)(q^2-1).

The graph-fixed embedding, standard root folding, exact centralizer statements and group orders are retained inputs. Thus |B|/|A|=c_A/c_B=L=(q^12-1)(q^4+1). If Lambda=A union B, its actual size forces

    |H|=c_A/(1+L)
       =q^20(q^12-1)(q^8-1)(q^6-1)(q^2-1)/(q^12+q^8-1).

Set D=q^12+q^8-1>1. It is coprime to q. Modulo q^12-1, q^8-1, q^6-1 and q^2-1 its residues are respectively q^8,q^4,q^2,1, so it is coprime to every numerator factor. The displayed order cannot be an integer. This is an exact all-field divisibility proof, not an experiment.

All three possible selected sets have now been excluded. Together with the source-qualified canonical reduction this proves the proposed full-socle theorem in precisely the stated diagonal-free even-field ranges.

## Evidence and limitations

The coordinator freshly inspected the relevant primary statements, the complete corrected Craven tables and the original Aschbacher-Seitz page images for the root labeling and third-class representative. The source target on p.56 is {alpha2,alpha3,alpha5}; an exploratory transcription as alpha6 was corrected before this source was frozen. The coordinator independently checked the root arithmetic and read and ran the certificate with Python3.12.14. The finite Cartan calculation does not prove the external class classification, rational-form correspondence, Chevalley-group construction or canonical-loop inputs.

The proof does not use the abandoned assertion that the small graph-class square covers all involution classes, nor infer a uniform conclusion from the twisted E6(2) character-table control. No disputed transcription of a twisted unipotent-centralizer order is used. Independent exact-source mathematical review is recorded below. Repository integrity is separate. The remaining E6 fields and other families and loop-operation classification remain open.

## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted the full scoped deduction at exact source `79273df37632fe7b6143710d0566566d561d6dd8`: contributor 1, contributor 2, and contributor 3. Each checked the actual outer-class reduction, all three marked-set selections, the maximal-order filter and the root-product argument, conditional on the stated canonical and exceptional-group inputs. Each extracted, read and independently ran the committed root certificate with Python3.12.14; all passed.

The paired-simple reviewer freshly inspected Craven Tables2,3,9,10, Guralnick-Robinson section3.3, Aschbacher-Seitz (19.8)-(19.9), and the supplied original page images53/56. The S5 reviewer freshly inspected those root-label images; the rank-three reviewer freshly inspected Craven Tables2-3 and page56. Other classification, centralizer, root-folding and rational-correspondence interfaces were retained as cited inputs, not independently rederived. The exact reviewed commit is locally available. Repository integrity separately passed115 tests under Python3.12.14; that does not prove the mathematics. These are research reviews, not formal GitHub approvals. C0010 and the classification endpoint remain open.
