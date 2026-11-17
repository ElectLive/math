# G2 extension-field/vector-parabolic capacity

Continuation of [0323:C0010](../foundations/research-C0010.md), with independent exact-source mathematical review recorded below. Let Q be a finite simple proper left Bol loop with almost-simple full multiplication group M and socle S=PSL_n(q), where q=2^f, n=6b and b≥1. Let G=LMlt(Q), I=M_1 and H=G∩I. Suppose the actual pair (I,G) tightly contains (X,Y), where X is the natural projective image of G2(q^b)' and Y=q^(n−1):SL_(n−1)(q) is the nonzero-vector stabilizer. Under the cited inputs, no such Q exists. Together with the reviewed opposite orientation this excludes this entire vector-parabolic pair, not the different G2/SL5 antiflag pair or all even-dimensional linear full socles.

Use the canonical definitions in [PROBLEM](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`. In particular the original marked set Λ has |Λ|=[G:H]. The [weighted original-fiber bound](even-linear-extension-parabolic.md), independently reviewed at `d95f900af71ff43fcc5486345a0c24f7eb47f6da`, applies to every actual vector-parabolic canonical factor here and gives

    |Λ| < 12 q^[n(n−1)/2].                              (1)

This imports only its natural radical/action and upper-capacity interfaces, not its linear-extension lower bound.

## Actual model and source inputs

Li–Wang–Xia, *Factorizations of almost simple linear groups*, arXiv:2106.03109v2, Theorem1.2/Table1.1 row2, printed p.2, definition of tight containment, and Lemmas4.3–4.4, printed p.5, [exact primary version](https://arxiv.org/html/2106.03109v2), give the common natural embeddings and transitivity of G2(R)' on the nonzero vectors of its six-dimensional F_R-module, where R=q^b. Tight containment preserves equality of perfect residuals as well as actual containment; in particular I^(∞)=X, so I normalizes X. A common source automorphism is applied to the entire actual pair when necessary. No actual factor is silently replaced by its perfect residual.

For R≥4, T=G2(R) is perfect, centerless and simple, has order R^6(R^6−1)(R^2−1), and has outer automorphism group C_(fb). The latter is the characteristic-two row of Burness–Guralnick–Harper, *The spread of a finite group*, arXiv:2006.01421v2, Table2, printed p.19, [primary version](https://arxiv.org/html/2006.01421v2). The exceptional graph-field automorphism of G2 occurs in characteristic three, not characteristic two. An early scratch argument mixed these cases; it is not used here.

A. V. Vasilyev, *Minimal permutation representations of finite simple exceptional groups of types G2 and F4*, Algebra and Logic35(6)(1996), Theorem1, printed pp.377–378, [author-hosted primary PDF](https://old.math.nsc.ru/~vasand/Papers_eng/g2f4.pdf), gives minimal faithful permutation degree416 for G2(4), and (R^6−1)/(R−1) for G2(R) with R>4. The coordinator freshly inspected this theorem, the BGH table and the LWX model statements. The initial direct Vasilyev fetch timed out; the indexed primary PDF was accessible. These source results remain inputs, not consequences of the argument below.

## The restricted-scalar centralizer

Assume R≥4 and let V be the natural six-dimensional F_R-module, regarded as an n-dimensional F_q-module. Its transitivity on nonzero vectors implies irreducibility over F_q. Therefore E=End_(F_q T)(V) is a finite division ring, hence a finite field. It contains the scalar field F_R. Set k=[E:F_R]; since V is an E-vector space, k divides6.

If k=6, V has dimension one over E, forcing faithful T to embed in the abelian group E×, impossible. If k=2 or3, T acts transitively on the E-lines, of number

    d=(R^6−1)/(R^k−1).

This nontrivial action is faithful by simplicity of T. At R=4, d≤273<416. For R>4, d<(R^6−1)/(R−1). Both contradict the cited minimum-degree theorem. Thus k=1 and

    C_GL_n(q)(T)=F_R×.

Conjugation by the linear normalizer N=N_GL_n(q)(T) maps it into Aut(T), with that centralizer as kernel. The full outer-group order therefore yields the sufficient bound

    |N| ≤ fb(R−1)|T|.                                  (2)

No sharper assertion that only the b field automorphisms fixing F_q occur is needed. In particular this proof needs no entrywise realization of field automorphisms and no density theorem.

## Original intersection and uniform contradiction

Let Z be the scalar center of SL_n(q). Since T is perfect and centerless, the full inverse image of X in SL_n(q) is TZ and its derived subgroup is exactly T. Hence a projective normalizer of X lifts to a genuine linear normalizer of T. An element of Y has a unique determinant-one representative fixing the specified nonzero vector v: the source model identifies Y with SL_n(q)_v, and a scalar fixing v is identity. Consequently

    |N_S(X)∩Y| ≤ |N_v| = |N|/(q^n−1),

where the equality follows because N contains T, transitive on V minus zero. Since H∩Y≤I∩Y≤N_S(X)∩Y and Y≤G, we have

    |Λ|=[G:H] ≥ [Y:H∩Y]
        ≥ |SL_n(q)|/[fb(R−1)|T|].                      (3)

This uses the actual subgroup intersection, retaining all possible outer elements of I and G. Those outer elements cannot enlarge I∩Y beyond N_S(X)∩Y.

The elementary bounds |SL_n(q)|>q^(n²−1)/2, R−1<R and |T|<R^14 show that (3) is strictly greater than

    q^[36b²−15b−1]/(2fb).

The exponent in (1) is18b²−3b. Their difference is

    D=18b²−12b−1 ≥ 5b,

because D−5b=(b−1)(18b+1). For every positive integer f, q^D=2^(fD)≥f·2^D; and 2^(5b)>24b for b≥1 (base32>24, followed by multiplication by32 while b increases by1). Therefore q^D>24fb, making (3) strictly larger than the upper bound (1). This is a contradiction for all R≥4, with no finite residual computation.

## The small parameter and scope

If R=2, then q=2,b=1,n=6. The actual vector-parabolic canonical group is AGL5(2), as proved in the reviewed linear-extension/parabolic manuscript at `d95f900af71ff43fcc5486345a0c24f7eb47f6da`. Its completeness and the reviewed inner-inversion criterion at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8` would give a Bruck isotope with the same canonical group, contradicting its simple GL5(2) quotient and the stated Bruck-envelope theorem. This does not assert that the original loop is Bruck. It avoids any normalizer claim for the exceptional G2(2)' module and does not rerun the small Magma calculation quoted in LWX.

Thus every stated parabolic-side parameter is excluded. The opposite component orientation is independently reviewed at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, in the [marked involution/vector obstruction](marked-involution-vector-obstruction.md). The odd-characteristic linear and symplectic component sides, the antiflag pairs and the complete classification are separate obligations. No new computation is required for this minimum-degree centralizer proof or the uniform arithmetic. Independent exact-source mathematical review is recorded below; passing repository integrity does not certify these deductions.

## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted this assembly at exact source `4169b5a5219bf8872dcf8723a2dbea6e07ddb111`: contributor 1, contributor 2, and contributor 3. Each checked irreducibility, the finite-field centralizer and faithful E-line action, the full characteristic-two outer-order bound, projective normalizer lift and actual vector-stabilizer intersection, uniform exponent inequality, and the retained R=2 affine exception. Their acceptance is conditional on the cited natural model, minimum-degree theorem, automorphism data and pinned canonical/fiber/affine/Bruck inputs.

The paired-simple reviewer freshly inspected Vasilyev Theorem1 pp.377–378, BGH v2 Table2 and LWX v2 Lemma4.4. The presentations reviewer freshly inspected the LWX and BGH statements; its direct Vasilyev request timed out, and it used the indexed primary excerpt as corroboration while retaining the earlier full theorem inspection. The S5 reviewer retained the primary inputs without fresh PDF inspection. None reran the source's small Magma calculation or claimed new computational evidence. The exact source is locally available. Repository integrity separately passed115 tests with Python3.12.14; these research reviews are not formal GitHub approvals. The antiflag pairs and full classification remain open.
