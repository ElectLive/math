# All alternating paired folders: a quotient bound and normal form

**Mira Cult**

**The structural theorem and appended small-degree evaluation are independently
reviewed at their respective exact sources below**, continuing
[0323:C0010](../../claims/0010.md). Let T=A_n, n≥5. Consider finite simple
nonassociative left Bol loops whose entire faithful canonical left multiplication
group is T×T and whose canonical inversion exchanges the two factors. Conditional
on the pinned paired-folder interfaces and the group-classification inputs below,
every such folder has common Goursat quotient C=1 or C2. Every such loop is
isomorphic to all of its isotopes. There is an exhaustive normal form consisting
of exact factorizations and the index-two lifts specified below, with the existing
simultaneous-automorphism/swap isomorphism test.

This treats every alternating degree, without ambivalence. It bounds the
coupling quotient and gives a construction-and-isomorphism reduction; it does not
evaluate the parameter orbits in every degree, or classify other canonical
groups. The previously evaluated [ambivalent table](paired-ambivalent-alternating-classification.md)
retains its separate source/review pins.

The canonical paired interface is [the paired source](../factor-permutation/radical-free-paired-simple-envelopes.md)
at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff); its intersection-bijection,
principal-isotope and regular-subgroup orbit continuations were reviewed at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/e898d8a00b1fc97431ad8092b4e51b9217650187). These retain C0001 at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), the scoped C0007 input at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), and their stated CFSG/FGS and
folder dependencies. In particular, the canonical section is the full
anti-diagonal K={(t,t⁻¹):t∈T}, and the projections A,B of H are nontrivial proper
subgroups of T.

## The quotient bound

Write α:A→C and β:B→C for the epimorphisms defining

    H={(a,b)∈A×B: α(a)=β(b)},    A0=ker α,    B0=ker β.

The paired interface gives T=AB, |H|=|T| and |C|=|A∩B|. Both kernels are
nontrivial: if A0=1, then |H|=|B|<|T|, and symmetrically for B0.
Whenever C≠1 both kernels are also proper. We prove |C|≤2.

At n=5 the elementary paired A5 proof at the first pin gives C=1. At n=6
there are no such folders by the [paired PSL2(9) exclusion](../factor-permutation/radical-free-involution-support.md#paired-psl9-exclusion)
at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563). At n=7,8,9 the finite certificate
below excludes every common quotient of order greater than two using only
necessary subgroup and quotient orders.

For n≥10 use the actual-factor version of Liebeck–Praeger–Saxl Theorem D,
as stated in Chen et al., arXiv:2111.06579v2, Theorem 2.6. This concerns the
actual factors A,B, not merely maximal overgroups. Apart from one degree-ten
exception, after interchange there is a k with 1≤k≤5 such that, for m=n−k,

    A_m ◁ A ≤ (S_m×S_k)∩A_n,     B is k-homogeneous.

The degree-ten exception has A=PSL2(8) or PSL2(8).3 and
A5×A5◁B≤(S5 wr S2)∩A10. If A is simple it has no nontrivial proper kernel.
Otherwise any nontrivial proper quotient of A is C3: a normal subgroup
disjoint from its simple socle centralizes that socle and is trivial in this
almost simple group. But a map B→C3 kills the perfect subgroup A5×A5,
whereas B/(A5×A5) is a 2-group. Thus this exception cannot have C≠1.

Now assume the displayed intransitive-factor case and |C|>2.

For k=1, A=A_(n−1) is simple, impossible. For k=2, A is A_m or S_m;
their nontrivial proper quotients have order at most two.

For k=5, Kantor's homogeneous-group theorem makes B 5-transitive. The
CFSG-dependent multiply-transitive list makes the proper possibilities M12
and M24 in their natural actions, both simple. This is again impossible.
For k=4 the 4-transitive possibilities are the simple groups M11,M12,M23,M24.
Kantor's non-4-transitive list leaves only B=PΓL2(32) at n≥10 (the other
listed actions have degree nine). Its only nontrivial proper quotient is C5.
However A contains perfect A29 and A/A29 embeds in S4, so A has no quotient
C5. This excludes k=4. The source list does not require, and we do not assert,
that PΓL2(32) is sharply 3-transitive.

It remains to take k=3 and m≥7. Quotienting the displayed overgroup by A_m
gives S3. Thus, up to conjugacy, A is one of

    A_m,    A_m×C3,    S_m,    (S_m×S3)∩A_n.

The first and third have no quotient in question. For either of the others,
a normal subgroup disjoint from A_m centralizes A_m, hence lies in its
centralizer C3. A normal subgroup containing A_m is the inverse image of a
normal subgroup of the indicated quotient C3 or S3. Consequently the only
remaining possibilities with nontrivial proper kernel and |C|>2 are:

* kernel C3, with quotient A_m or S_m;
* kernel A_m, with quotient C3 or S3, respectively.

In the first case |H|=|A0||B| forces [T:B]=3. The coset action would embed
the simple group A_n into S3, an impossibility. In the second case the same
order equation gives

    |B|=n(n−1)(n−2).

If B is 3-transitive, it is sharply 3-transitive. Zassenhaus's classification
(in the precise restatement cited below) gives a normal simple PSL2 over the
relevant field of index at most two; n≥10 excludes the nonsimple small fields.
Its image in either C3 or S3 must be trivial, so neither quotient is possible.

If B is not 3-transitive, apply Kantor Theorem 1(ii),(iii), rather than inferring
sharp transitivity from the order. The projective possibility contains normal
PSL2(q), with n=q+1 and q≡3 mod4. Its order is half the displayed order of B,
so the index is two and the same quotient obstruction applies. The affine
possibilities of degree eight are outside this case. The remaining AΓL1(32)
has order 32·31·5, not 32·31·30, and is excluded by order. This exhausts k=3
and proves |C|≤2 under the stated classification inputs.

## Regularity without ambivalence

For any paired data with C of exponent at most two, the Bol collision and
left–right fixed-point tests coincide. Explicitly, a forbidden anti-diagonal
collision is a nonidentity x∈A∩gBg⁻¹ with

    α(x)=β(g⁻¹x⁻¹g),

whereas a nonidentity element of H fixing a point in the left–right action
(a,b):t↦atb⁻¹ gives the same equation with x in place of x⁻¹ on the right.
The two equations agree because every element of C is its own inverse.
Therefore every folder in the theorem is left–right regular, since |H|=|T|.

The regular-subgroup orbit lemma at the second pin now applies without any
ambivalence assumption on T. In particular T²=ΔT H, so conjugating H by any
element of T² has the same effect as conjugating by an element of ΔT. The
additional coordinate-inner actions that normalize principal isotopes introduce
no new orbits beyond simultaneous Aut(T) and swap. Thus every isotope is
isomorphic to the original loop. The corresponding Rota–Baxter graph construction
at that pin is available as well. No classification of arbitrary Rota–Baxter
maps is used to prove the quotient bound.

## Exhaustive exact-factorization and index-two-lift data

For C=1 the stabilizer is exactly a product A×B with T=AB an exact
factorization into nontrivial proper factors. Conversely every such product is
admissible by the paired intersection-bijection criterion.

For C=C2 put R=A∩B=⟨r⟩. The same criterion reduces to bijectivity of
d↦α(d)β(d) on R. Therefore exactly one of α(r),β(r) is nonidentity.
Orient the factors so that α(r)=1 and β(r)≠1, and set V=ker β. Then

    T=AV is exact,     V◁B<T,     [B:V]=2,
    α:A→C2 is onto,    α(A∩B)=1.

Indeed A∩V=1 and |A||V|=|T|. This gives the promised normal form. Conversely
choose nontrivial proper A,V<T with T=AV exact, a proper subgroup B<T with
V◁B and [B:V]=2, and an epimorphism α:A→C2 trivial on A∩B. Let β be the
quotient map B→B/V=C2 and form the fiber product H above. Exactness gives
T=AB, |A∩B|=2 and (A∩B)∩V=1. Thus β is nontrivial on R, and the same
bijection criterion proves admissibility. All the canonicality, simplicity,
properness and non-Bruck conclusions of the paired construction apply.

The isomorphism relation on these constructed H is exactly simultaneous
Aut(T) and optional coordinate swap, as in the pinned paired theorem. In the
nonproduct case the orientation above is unique: the unique intersection
involution lies in exactly one kernel. Hence A,B,V and α are recoverable
from the oriented H, and quotient C2 has no nonidentity automorphism to add
a further choice. Product and nonproduct cases cannot be isomorphic. This is
an exhaustive normal form with a checkable isomorphism relation; enumeration
of these data in every degree remains a separate obligation.

## Sources, finite evidence and review boundary

Exact versions, locators and inspection limits for the four classification inputs
are recorded in [REFERENCES](../foundations/references.md#paired-alternating-sign-sources).
The project inspected Chen et al. Theorem 2.6, Kantor Theorem 1, Jones's
published multiply-transitive list and the versioned Zassenhaus restatement.
The original LPS and Zassenhaus proofs and the CFSG-dependent classification
have not been reproved. This argument incorporates the degree-ten exceptional
factorization and separates the non-3-transitive case; it is not an unqualified
transfer of the Rota–Baxter argument in GG24 §7.

The project read and ran [verify_an789_goursat_orders.g](../code/verify_an789_goursat_orders.g)
under GAP4.15.1. It enumerates all subgroup conjugacy classes of A7,A8,A9,
then every normal subgroup of each proper representative, retaining quotient
orders c with 2<c<|A|. For all pairs of retained subgroup/quotient orders it
tests |A||B|=|T|c. The subgroup-class counts are 40,137,223 and each candidate
count is zero. Quotient isomorphism, relative embeddings and collision tests
cannot create a candidate when even this necessary order test has none.
Conjugacy representatives suffice because the orders and normal-quotient orders
are conjugacy invariant. The script is warning-free, uses no external data,
network or file output, and depends on GAP's complete subgroup and normal-subgroup
enumeration algorithms. The pinned release and command are in code/README.md.
This finite evidence supplies only degrees seven through nine, not the uniform
proof. Independent exact-source review is recorded below.


## Independent exact-source review

reviewers contributor 1 and
contributor 2 independently accepted the full manuscript and
certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0).
contributor 3 independently accepted the analytic argument at the same
source; that agent authored the scratch certificate, so its rerun is
reproducibility evidence rather than independent code review. All three read
and extracted the committed GAP source and reran it under GAP4.15.1, obtaining
the stated class counts and zero candidates.

Their analytic reviews cover the exceptional degree-ten factors, every k case,
the index-three contradiction, the separate non-3-transitive alternatives, the
regularity and isotope conclusion, and necessity, sufficiency and equivalence
of the oriented index-two normal form. The paired-simple reviewer independently
inspected all four cited classification statements at the precise versions
above. The C9 reviewer inspected Chen, Kantor and the Zassenhaus restatement,
but did not freshly inspect Jones. The folder-criterion reviewer did not perform
a fresh full primary-source audit. None reproved the underlying classifications,
GAP algorithms or the pinned folder inputs. These are scoped model mathematical
reviews, not human/formal certification, formal GitHub approval, evaluation of
every parameter orbit, or an unrestricted Bol-loop classification.

## Evaluated degrees seven, eight and nine

**Independently reviewed computational classification at the exact source below.**
Combining the structural theorem at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0)
with complete subgroup and double-coset enumeration in GAP4.15.1 gives the
following isomorphism counts in precisely the paired canonical branch:

| T | Product stabilizers | Correlated C2 stabilizers | Total |
|---|---:|---:|---:|
| A7 | 2 | 0 | 2 |
| A8 | 9 | 0 | 9 |
| A9 | 6 | 1 | 7 |

These are classes of loops, not just abstract subgroup types. The paired
theorem gives all of them order |T| and makes them simple, proper and
non-Bruck. The structural theorem above makes every isotope isomorphic.
The evaluation is conditional on GAP's complete subgroup, normal-subgroup,
conjugacy and double-coset algorithms and the stated analytic interfaces;
the program does not prove these algorithms or construct a multiplication
table for every loop.

Here is the exhaustive orbit algorithm in
[verify_paired_an789_orbits.g](../code/verify_paired_an789_orbits.g).
For n=7,8,9, Aut(A_n)=S_n, by the alternating automorphism source already
recorded in [REFERENCES](../foundations/references.md#lyons99-alternating-automorphisms).
Start with all A_n subgroup classes and fuse them under S_n, omitting the
trivial and full groups. For each subgroup H enumerate all index-two normal
subgroups K. Two decorations (H,K),(H′,K′) are equivalent exactly when some
conjugator taking H to H′ carries K into the N_(S_n)(H′)-orbit of K′.
This gives respectively 35,110,193 proper nontrivial subgroup classes and
26,155,260 decorated classes. These are S_n-orbits, not the earlier A_n
subgroup-class totals.

For fixed subgroup classes A,B, their simultaneous S_n-orbits of relative
positions are N_(S_n)(A)\S_n/N_(S_n)(B). If d is a double-coset representative,
the pair is (A,dBd⁻¹). GAP uses exponent notation B^g=g⁻¹Bg, so the code
must, and does, use B^(d⁻¹). Products are retained exactly when
|A||B|=|T| and A∩dBd⁻¹=1. The code uses unordered subgroup-class indices
and asserts that each accepted pair has unequal factor orders. Hence the
factor swap is accounted for without an unperformed equal-factor orbit test.

For decorations (A,A0),(B,B0), replace the normalizers by their intersections
with the respective kernel normalizers and enumerate all ordered pairs of
decorated classes and their double cosets. Keep exactly those with
|A||B|=2|T|, |A∩dBd⁻¹|=2, that intersection contained in A0 and disjoint
from dB0d⁻¹. These are precisely the oriented C2 data of the structural
theorem. The orientation is unique, so a further swap quotient would
incorrectly identify or remove classes. Index-two kernels determine the
quotient maps to C2 uniquely, so no quotient-map parameter is missing.

The product-order histograms provide compact reproducibility controls:

| T | Unordered factor orders and number of orbits |
|---|---|
| A7 | (7,360):1; (21,120):1 |
| A8 | (8,2520):4; (15,1344):1; (56,360):2; (120,168):2 |
| A9 | (9,20160):2; (72,2520):1; (120,1512):1; (360,504):2 |

The unique correlated A9 class has oriented projection orders (72,5040).
Different rows or decorations are not identified by abstract group names:
the actual embedding orbits are what the algorithm counts. The code can
print concrete permutation generators for A,B and, when appropriate, A0,B0
by setting `EmitRepresentatives:=true` before reading it in GAP. Those
generators and the canonical full anti-diagonal construction recover every
listed class; no unrecorded search choices or external group databases are
required beyond GAP's built-in algorithms.

The project read and ran the exact proposed script under GAP4.15.1;
all counts and assertions passed. The producer also ran its generator-output
mode, obtaining 18 representative rows in total. The script uses no network
or output files. A preliminary independent code review checked the double-
coset convention and required the now-present unequal-product-order assertion.
Independent review of the committed evaluation and script is recorded below.


### Independent review of the small-degree evaluation

reviewers contributor 1 and
contributor 2 independently accepted the evaluated section
and certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/f15f63f39bfe8bb913573a4bdc2369178d483963).
They checked completeness of the S_n fusion and decorated double-coset
enumeration, the GAP conjugation convention, the unique correlated orientation
and the asserted unequal-order product swap condition. Both read, extracted
and reran the exact committed source under GAP4.15.1; all counts and order
histograms passed. Neither reran the optional generator-output mode or
independently verified the GAP algorithms. No fresh primary-source audit of
the upstream classifications was performed. These scoped model proof/code
reviews retain the structural source and computational dependencies and do
not classify other canonical groups or certify a formal GitHub approval.
