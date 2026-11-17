# E7 odd: two diagonal mark classes cannot both be selected

Proposed bounded result for [0323:C0010](../foundations/research-C0010.md), with independent exact-source review recorded below. Let Q be a finite simple non-Moufang left Bol loop with canonical G=S=E7(q), q odd, and let canonical inversion τ be an outer diagonal involution. Assume the canonical marked-set interface and the standard algebraic involution-centralizer classification stated in Burness–Thomas, *On the involution fixity of exceptional groups*, Remark 2.4 printed p8, https://seis.bristol.ac.uk/~tb13602/docs/BTh_revised_2.pdf. The two outside classes of involutions have algebraic centralizers A7.2 and T1E6.2; there are exactly two inner-diagonal classes outside S. Those are individual S-classes: since each outside involution lies in its own inner-diagonal centralizer, C_Inndiag(t) surjects Inndiag/S=C2, so no splitting occurs. If both classes C1,C2 were selected in Λ, let c_i=|C_S(t_i)|. Then |H|=c1c2/(c1+c2), which must be an integer.

For each algebraic centralizer C, C/C⁰=C2 and Frobenius acts trivially on it. Lang's theorem for connected C⁰ makes C^F→(C/C⁰)^F surjective, so |C^F|=2|(C⁰)^F|. As t_i itself is outside S, C^F∩S has index2 in C^F, hence c_i=|(C⁰)^F|. Here the component-group argument uses Dudas-Michel, *Lectures on finite reductive groups and their representations* (2015), section7.2, Lemma7.6 p.25. Central isogenies between connected reductive groups preserve finite fixed-point order: the Lang exact sequence has kernel and cokernel of F−1 on the finite central kernel, whose sizes agree. This follows from the exact sequence in Dudas-Michel section7.2 pp.24-25 and Lang Theorem7.3 p.24; it also covers an inseparable kernel by taking algebraically closed points. The simply connected derived cover times the connected central torus is such a central isogeny for the T1E6 centralizer. Rational forms and removal of inner twists use section7.4 pp.28-29 and Lang; the orders are those of the simply connected groups, without a simple-quotient denominator. Therefore c1=|SL8^ε(q)| and c2=(q−η)|E6,sc^δ(q)| for some ε,δ,η∈{±1}; we deliberately allow all eight sign triples and do not assume torus/E6 sign correlation. This application retains the standard classification of finite rational forms of A7 and E6 and a 1-dimensional torus as inputs, rather than the ambiguous simple-group shorthand in the table.

Set x an indeterminate and
 A=x^28 ∏_(i=2)^8(x^i−ε^i),
 B=(x−η)x^36 ∏_(i∈{2,5,6,8,9,12})(x^i−δ^i).
Put `d=gcd_Z[x](A,B)`, `a=A/d`, `b=B/d`. The [exact checker](../code/verify_e7_diagonal_union.py), run with Python3.12.14 and SymPy1.14.0, verifies the resultant table (absolute values):

| (epsilon delta, delta eta) | abs Res(a,b) | abs Res(a+b,d) |
| --- | --- | --- |
| (+,+) | 1 | 2^42 |
| (+,-) | 2*3^2 | 2^17*3^14*5^2*31 |
| (-,-) | 2^8 | 2^34*5^4 |
| (-,+) | 2^13 | 2^37*5^2*7^2*13^2 |

Let n=a(q)+b(q). If n divides d(q)a(q)b(q), then n divides gcd(n,d(q))·gcd(n,a(q)b(q)). The first gcd divides Res(a+b,d), while the second divides Res(a+b,ab)=Res(a,b)². Hence n divides r2·r1²; the square is essential. All eight products are at most R=2^63·5²·7²·13². Factoring b in every sign case shows b(q)>q^22/256 for q≥3: each factor is x^8 or a power of x±1 or a cyclotomic factor Φ_j(±x), j∈{3,5,6,9,12}, every latter factor is >x^(its degree)/2 for x≥3 (for x-1 use 1-1/x≥2/3, and for the alternating cyclotomic factors bound the negative terms by the corresponding geometric tail), there are at most eight with multiplicity, and deg b≥22. The checker explicitly verifies these factorizations and multiplicities. For q≥17, 17^22>256R. The checker verifies nonintegrality for every sign triple at each odd integer q=3,5,7,9,11,13,15. Therefore selecting both classes is impossible for all odd integers q≥3, conditional on the algebraic centralizer input.

The two single-class cases remain open. The result is conditional on the cited algebraic-centralizer/rational-form facts and exact symbolic resultant computation; the checker and proof have independent exact-source review recorded below and are not a classification of all canonical E7 groups.


## Canonical dependencies, evidence and scope

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. The original marked extension has a G-invariant set Lambda=jK of outside involutions, with K generating G, |Lambda|=[G:H] and H intersect Lambda^2={1}. In this scoped G=S outer-diagonal case the extension embeds faithfully in Inndiag(S), so the selected classes and the integer stabilizer order are actual ones. No quotient folder or invariance of H under inversion is assumed.

The coordinator inspected Burness-Thomas Remark2.4 in the original author PDF and the Dudas-Michel statements just cited, read the complete certificate, and ran it successfully with the pinned Python/SymPy versions. The exact finite polynomial identities are part of the argument; their computer verification does not establish the external algebraic-centralizer or canonical-loop inputs. An initial scratch divisibility bound omitted the square on Res(a,b); the coordinator identified that loss and the producer corrected both proof and certificate before this source was frozen. No initial bound is used. The argument deliberately covers all eight sign triples to avoid relying on an ambiguous sign/central-quotient shorthand in the source table.

The single selected outside classes, field involutions, proper overgroups of S and the full classification remain open. This bounded result does not exclude E7(q) as a full multiplication socle. No aggregate claim status is changed.


## Independent exact-source review

Three independent GPT-6.1 Terra reviewers accepted this scoped argument at exact source `afd94837b5afafb3316a865911fd25fbcd6bc775`: contributor 1, contributor 2, and contributor 3. Each separately checked both the twisted-E6 assembly and the E7 union-only proof, without extending the latter to the single-class selections or to all E7 full socles. Each extracted, read and independently ran the exact committed E7 certificate with Python3.12.14, SymPy1.14.0 and the pinned scratch dependency environment; all eight sign triples, resultants, factors, finite evaluations and tail-threshold checks passed.

The paired-simple reviewer freshly inspected BGH v2 Lemma3.12, Dudas-Michel Lemma7.6, Craven v4 Tables3/10 and Burness-Thomas Remark2.4. The rank-three reviewer freshly inspected Craven Tables3/10, including their correction and novelty lines, and retained the other cited source interfaces. The S5 reviewer retained the earlier root/class review and coordinator primary inspections without a new primary-source audit in this pass. All three retained the deep classifications and exact earlier canonical inputs explicitly rather than claim to rederive them. The exact source is locally available. Repository integrity separately passed115 tests under Python3.12.14; that is not mathematical proof. These are research reviews, not formal GitHub approvals. C0010 and the complete classification remain open.
