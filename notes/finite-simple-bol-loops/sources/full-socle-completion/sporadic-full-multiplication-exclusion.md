# Excluding every sporadic full multiplication socle

Mira Cult

This is a proposed deduction under
[0323-finite-simple-non-moufang-bol-loops:C0010](../foundations/research-C0010.md).
It does not change that claim's open status. Three independent mathematical/code
reviewers accepted exact source `8cd335ea73dadc72b38b75c294e690bdbeb7c155`,
conditional on the stated inputs, as recorded below. Finite-group classifications and the pinned GAP and
CTblLib data below are explicit inputs, not theorems proved by running code.

## Endpoint and interfaces

**Conditionally proved theorem.** Let Q be any finite simple proper (non-Moufang) left Bol
loop. Then the socle of its full multiplication group M=Mlt(Q) is not one of
the 26 sporadic simple groups. The left multiplication group G=LMlt(Q) and the
full point stabilizer I=M₁ are unrestricted: in particular, they may both be
nonsolvable and G need not contain Soc(M).

Use the canonical [folder definitions](../foundations/problem-contract.md), with H=G₁,
K={L_x:x∈Q}, n=|Q|, and the formal inversion extension E=G⋊⟨t⟩.
The actual outside marked set Λ=tK consists of involutions, is invariant under
G-conjugation, has size n, and satisfies H∩Λ²={1}. We always count this set,
not a putative folder in a quotient. The following previously reviewed sources
are the exact interfaces used here; their source and review qualifications are
retained in their canonical files.

| Interface | Source revision and canonical location |
| --- | --- |
| Faithful folder and canonical inversion | C0001, `9431ade99316d6bc62efb389492fef385b510b45`; scoped C0007 inversion at `932ead5db5f39045e2085caa6b062f6b981b2813` |
| Primitive almost-simple full M | [C0008](../../claims/0008.md), `06857e28349ca4529c31a9855ce12cfbb191c1b7` |
| Inner inversion impossible when G has a component; inversion fixes Z(G) and inverts G/G′ | [Canonical inversion consequences](../odd-completion/nonbruck-almost-simple-radical-bridge.md), `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`, `e7476945cf987cf1c654a385ac8f78fe2beb320a` |
| All entire canonical PSL₂ overgroups | [Canonical PSL₂ assembly](../odd-completion/nonbruck-almost-simple-radical-bridge.md), `47b07688a82d3df93f537946fe0780112200383b` |
| All entire canonical odd-dimensional PSL/PSU overgroups | Same bridge, `114ce1b011fd47589eb762ed7cd5492a190002d8` |
| All entire canonical sporadic overgroups | [Sporadic canonical theorem](../odd-completion/nonbruck-almost-simple-radical-bridge.md#proposed-exclusion-of-all-sporadic-canonical-socles), `39991d55d946ddb409cf1341ffa10e3f40ea64cc` |
| Canonical G₂(4), and completeness of Aut(T) for simple T | [G₂(4) and outer-group deductions](../odd-completion/nonbruck-almost-simple-radical-bridge.md#proposed-complete-canonical-g24-exclusion), `6e016e1f1237545146e30786902ef92486c1524c` |
| Sporadic full socles with a solvable actual factor | Same bridge, `4e1449bce6a7c14f4b329aad8c4c01e65f10d650`, `fb4bb71c96277e01b50bc291f1251627a55dd949`, `6e016e1f1237545146e30786902ef92486c1524c` |
| No proper simple Bol loop with full action of rank three | [C0017](../../claims/0017.md), `7b1c9e8786ceb5e7d8e6a6709adee1aefe736efd` |
| Unique simple nonassociative loop of order 24 and its Mlt=A₂₄ | [C0011](../foundations/C0011.md), scoped uniqueness `af8e206c079c37de3fd393f5a3e604525b94bed5`; explicit Mlt witness `3313726ad58aa11de1c79e04d4618f28380925fb` |

These interfaces do not assert that G is primitive, nor promote the unrelated
aggregate parts of C0007. The classification endpoint in PROBLEM.md remains open.

## Exhaustive factorization reduction

Put S=Soc(M), G₀=G∩S and I₀=I∩S. Since both G and S are transitive,
M=GI=SI and n=[S:I₀]. If S≤G, the reviewed entire-canonical sporadic theorem
already applies. If either actual factor is solvable, use the reviewed
two-orientation sporadic solvable-factor deductions. Otherwise G and I are
proper core-free nonsolvable factors.

The source is **Giudici06**, precisely the 8 February 2006 preprint,
Theorems 1.1–1.2 (printed p.2), §3 and Tables 1–4 (pp.13–15);
[REFERENCES](../foundations/references.md#sporadic-full-multiplication-sources) records the
exact version and access. Theorem 1.1 lists actual factors of S, not just
maximal overgroups. If M=S.2 and G₀I₀=S, retain every compatible outer lift of
those actual factors. If G₀I₀≠S, Theorem 1.2 supplies the additional actual
factors in Table 4. This distinction is essential.

Only the following twelve sporadic full socles occur anywhere in these two
lists: M₁₁,M₁₂,M₂₂,M₂₃,M₂₄,J₂,HS,He,Ru,Suz,Fi₂₂,Co₁. Thus the other fourteen
(J₁,J₃,J₄,Co₂,Co₃,Fi₂₃,Fi₂₄′,McL,O'N,HN,Ly,Th,B,M) are already excluded.
For M₁₁, every remaining both-nonsolvable pair is PSL₂(11) with M₁₀; both
orientations have an entire canonical PSL₂ overgroup. Every M₂₃ pair has a
solvable factor. M₂₂ has no proper factorization of S; the only additional
both-nonsolvable pair in M₂₂.2 is PΣL₃(4) with PGL₂(11), excluded by the
odd-dimensional canonical linear and canonical PSL₂ theorems. The nine remaining
socles are handled below, with both orientations and all outer lifts retained.

## J₂ and HS

Giudici's J₂ pairs are U₃(3) with A₅×C₅ or A₅×D₁₀. The nonsolvable HS pairs
are M₂₂ with either of the two U₃(5).2 classes, or with A₅×C₅, A₅×D₁₀ or
A₅×(C₅:C₄). The new Table 4 pairs for J₂.2 and HS.2 have solvable partners.

If I₀=U₃(3) or M₂₂ respectively, the S-action has degree 100 and rank three.
The full outer actions J₂.2/U₃(3).2 and HS.2/M₂₂.2 also have rank three.
The complete maximal-class filters and all four permutation characters are
checked by [the J₂/HS certificate](../code/verify_j2_hs_full_socles.g). Thus C0017
excludes this orientation. Alternatively, the two nontrivial subdegrees sum
to 99, so they are unequal and cannot fuse under an outer extension.

In the other orientation G₀ is U₃(3), M₂₂ or U₃(5).2. Its simple perfect
residual L is U₃(3), M₂₂ or U₃(5); since G/L is solvable, L=G^(∞) is
characteristic. The complete maximal lists give N_S(L)=L for the first two,
and N_S(L)=U₃(5).2 for both HS classes in the last case. Those almost-simple
normalizers act faithfully on L, so C_S(L)=1. An outside element centralizing
L would square to 1. But the S-centralizers of all outside involutions have
orders 336 for J₂, and 40320,1920 for HS, all smaller than the relevant
|L|=6048,443520,126000. Hence C_Aut(S)(L)=1. Actual G therefore embeds into
Aut(L), contains L and is excluded by the reviewed canonical PSU₃ or sporadic
theorem. The second HS maximal table `HSM3` is identified as the second U₃(5).2
class by source metadata; equal character tables alone would not prove this.

## M₁₂

Giudici §3 (p.6) proves that every proper factorization of Aut(M₁₂) has one
factor contained in S. Since I maps onto M/S, that factor must be G. Therefore
G=G₀ even for an outer full group. Table 1 leaves M₁₁ with a subgroup transitive
in its degree-12 action, or PSL₂(11) with S₆, M₁₀ or M₁₀.2; other partners are
solvable. In the latter family every possible G is an almost-simple PSL₂ group.
If G=M₁₁, the canonical sporadic theorem applies.

If I₀=M₁₁, its self-normalizer in Aut(S) is M₁₁, so M=S and I=I₀. The two
M₁₁ classes are interchanged by the outer automorphism; transporting the
action reduces to the standard degree-12 action. The
[M₁₂ certificate](../code/verify_m12_transitive_nonsolvable.g) enumerates all
147 subgroup classes and identifies its ten transitive nonsolvable classes:
A₅, A₅×C₂, S₅, S₅×C₂, PSL₂(11), two A₆.2 classes, Aut(A₆), M₁₁, M₁₂.
It explicitly checks the derived A₆ isomorphisms and trivial centralizers in
the order-720 and order-1440 cases, rather than identifying them by order.
The canonical PSL₂/sporadic inputs leave only the two direct products.

For G=A₅×C₂ the perfect residual and center are characteristic. Inversion
fixes the center. If its action on A₅ is inner, it is inner on G, forbidden
by the component theorem. Otherwise that action is an outside involution of
S₅, hence a transposition. The formal outside coset then has two G-classes of
involutions, each of size 10, distinguished by the central bit. A nonempty
invariant Λ has size 10 or 20, not 12. For G=S₅×C₂, every automorphism of
S₅ is inner; the only additional possible automorphism is the central shear
from S₅/S₅′ to C₂. Canonical inversion acts trivially on G/G′=C₂² and fixes
the center, so this shear vanishes. Inversion is inner, again impossible.

## M₂₄

Here Out(S)=1. Table 2 gives M₂₃ with any actual degree-24 transitive partner,
or PSL₂(23) with exactly PΣL₃(4), PSL₃(4).S₃, 2⁴:A₇, 2⁴:A₈, M₂₂.2 or M₂₂.
The proof on p.7 explicitly resolves proper subgroups of the maximal partners;
there is no arbitrary subgroup of 2⁴:A₈ still to enumerate in this list.

If G=M₂₃ or PSL₂(23), use the corresponding canonical theorem. If I=M₂₃,
then n=24, so C0011 identifies Q with Q₂₄, whose full multiplication group is
A₂₄ rather than M₂₄. This removes all 173 transitive partners at once.
If I=PSL₂(23), the two linear partners and the two M₂₂ partners are excluded
by their canonical theorems. The factor 2⁴:A₇ has order n=40320, so G is
regular. Then K=G and the loop is associative, impossible here.

The last actual factor is the whole natural affine group AGL₄(2)=2⁴:A₈.
[The affine certificate](../code/verify_m24_affine_factor.g) constructs it
as affine matrices, checks its center is trivial and Aut(G)=Inn(G), and counts
j(G)=1696 elements squaring to 1. Write inversion as conjugation by u∈G.
Since it is involutory and Z(G)=1, u²=1. The homomorphism E→G taking t to u
is injective on the outside coset, and sends Λ to elements squaring to 1.
Thus n≤1696<40320, contradiction. No claim that every PSL₂(23) subgroup of
M₂₄ lies in M₂₃ is used; the maximal PSL₂(23) embedding is retained.

## He and Ru

Giudici Table 2 gives the He pairs Sp₄(4), Sp₄(4).2 with
B=F₇²:SL₂(7). Compatible outer lifts are retained. The genuinely new Table 4
He.2 pairs have solvable partners. The minimum degree in these orientations
is [He:Sp₄(4).2]=2058.

The complete maximal lists give the normalizer Sp₄(4).2 of T=Sp₄(4), and
the maximal subgroup B itself. Their indicated actions give C_He(T)=C_He(B)=1.
Every outside involution in Aut(He) has He-centralizer order 15120, less than
both |B|=16464 and |T|=979200. An outside centralizer element would square
into the trivial inner centralizer, so C_Aut(He)(T)=C_Aut(He)(B)=1 as well.

If G₀ is Sp₄(4) or Sp₄(4).2, its perfect residual T=G^(∞) is characteristic
and actual G embeds in Aut(T). Here Out(T)=C₄. For G=T, inner inversion is
forbidden; the only outer involution class has size 1360, so n≤1360<2058.
For G>T, every involution of Aut(T) has its outer label in the unique
subgroup of order two, hence belongs to G. Restriction Aut(G)→Aut(T) is
injective, so the canonical inversion is inner on G, again forbidden.

If G₀=B, perfection gives B=G^(∞), characteristic in G. Its characteristic
radical V=O₇(B)=F₇² carries the faithful natural SL₂(7)-action. The linear
normalizer is GL₂(7). A cocycle for this action is a coboundary: applying the
cocycle identity to the central element −I shows that multiplication by 2
solves it. Thus Aut(B)=AGL₂(7). Its elements squaring to 1 number
1+49+56·7=442: the linear parts are I, −I and the 56 diagonalizable
(+1,−1) matrices, with respectively 1,49,7 affine lifts. Since C_G(B)=1,
restriction to B is injective on the original outside coset, so n≤442<2058.
[The Held certificate](../code/verify_he_ru_full_socles.g) checks these counts,
the two outside class counts and the stated maximal-list filters.

For Ru, Out(Ru)=1 and the only actual pair is PSL₂(29) with ²F₄(2).
The first orientation is canonical PSL₂. In the second,
²F₄(2)=Aut(²F₄(2)′), the full automorphism group of the simple Tits group.
Restriction to the characteristic socle proves this automorphism group is
complete. Therefore canonical inversion is inner and its component makes
this impossible. The Tits and Sp₄(4) identifications are primary ATLAS inputs,
not deductions from abstract orders.

## Suz

Table 2 gives G₂(4) with U₅(2) or 3⁵:M₁₁. Table 4 adds, among pairs with
both factors nonsolvable, G₂(4).2 with 3⁵:(PSL₂(11)×2). If I₀=G₂(4), the
degree is 1782 and both the socle and outer full actions have rank three;
[the Suz certificate](../code/verify_suz_full_socles.g) checks the unique
maximal classes and both characters. Thus C0017 applies. Unequal nontrivial
subdegrees (their sum is 1781) also prevent outer fusion.

In the opposite orientation G₀=L is G₂(4) or U₅(2), a centerless simple
maximal subgroup of S. Hence C_S(L)=1. The S-centralizers of all outside
involutions have orders 1209600 and 190080, both less than
|U₅(2)|=13685760 and |G₂(4)|=251596800. Therefore C_Aut(S)(L)=1 by the
same squaring argument. Since L=G′ is characteristic, G is an actual
almost-simple overgroup of L, excluded by the canonical G₂(4) or odd-dimensional
unitary theorem. This includes the outer Table 4 orientation.

## Fi₂₂

Table 3 gives only L=2.U₆(2) with ²F₄(2)′, and Table 4 has no new Fi₂₂ row.
All inherited outer lifts must therefore be treated. If I₀=L, its unique
maximal class gives degree 3510 and rank three. The unequal nontrivial
subdegrees (sum 3509) cannot fuse in the outer action, so C0017 excludes it.

If G₀=L, then L=G^(∞) is characteristic and |Z(L)|=2. Its maximality gives
C_S(L)=Z(L). An outside element centralizing L has its square in Z(L), so
has order two or four. The S-centralizer orders of the outside order-two
classes are 1045094400,3317760,2903040; for order four they are
663552,122880,9216,6144,1536. Every one is smaller than |L|=18393661440.
Thus C_G(L)=Z(L), including all outer lifts.

Put T=L/Z(L)=U₆(2). An automorphism of perfect L acting trivially modulo
Z(L) is trivial: its central error is a homomorphism L→Z(L). Consequently
the kernel on G of the action on T is C_G(L), of order two. Each fiber on
the original outside coset has at most two elements. The full automorphism
group U₆(2).S₃ has j=1529056 elements squaring to 1. It follows that
n≤2j=3058112, whereas n=[Fi₂₂:²F₄(2)′]=3592512, a contradiction.
[The Fi₂₂ certificate](../code/verify_fi22_full_socles.g) checks the unique
maximal class, rank, every outside order-two/four class, and the exact bound.

## Co₁

Here Out(Co₁)=1. Giudici Table 3 lists Co₂ and Co₃ with 3.Suz or (3.Suz).2,
and respectively all T≤B≤(A₄×T).2 or T.2≤B≤(A₄×T).2, where T=G₂(4).
The Co₂/Co₃ canonical orientations are excluded by the sporadic theorem.
In the reverse orientations the degrees are 98280 and 8386560.

First set D=3.Suz. This perfect central cover has center C₃, and its outside
automorphism inverts that center. Automorphisms of a perfect central cover
embed in automorphisms of its simple quotient; D.2 induces the full Aut(Suz).
If G=D, center-fixing forces canonical inversion to induce an inner
automorphism of Suz, hence to be inner on D, impossible. If G=D.2, D is
characteristic and every automorphism of D is induced by G. After an inner
adjustment, any automorphism β of G fixes D elementwise. Its remaining error
is a cocycle of C₂ on C_G(D)=Z(D)=C₃, with inversion action. Such a cocycle
is a coboundary (multiplication by 2 is invertible on C₃), so β is inner.
Again inversion is impossible. Center-fixing is used only when G=D.

For T=G₂(4)≤G≤(A₄×T).2, T=G^(∞) is characteristic, and the outside 2 acts
by the nontrivial outer automorphism on T. Thus C_G(T)≤A₄ has order at most
12. The image of Λ in Aut(T) consists of involutions or the identity, each
fiber having at most 12 elements. By T-invariance, the fiber multiplicity
is constant over each image class. The two inner involution classes have
sizes 4095 and 65520; the single outside class has size 20800. Hence

    n = d + 4095 a + 65520 b + 20800 c,    0 ≤ d,a,b,c ≤ 12.

Here a,b,c are fiber multiplicities, not necessarily counts of T-orbits.
All three nonidentity class sizes and both degrees are divisible by 65, so
d=0. Both degrees are divisible by 4095 and gcd(4095,20800)=65, so 63|c,
giving c=0. For n=8386560 this requires a+16b=2048, impossible. For
n=98280 it requires a+16b=24, forcing a=8,b=1.

Choose λ∈Λ inducing conjugation by an involution x in the larger T-class.
Then ξ=λx centralizes T and ξ²=1. Therefore the entire class ξx^T lies in Λ,
and its square is (x^T)². The exact character-table coefficients
c(3,3,2)=1200 and c(3,3,3)=152 show that this square contains both nontrivial
T-involution classes. The collision condition forces H∩T to have odd order.
But [T:H∩T]=[TH:H] divides [G:H]=n, while |T|₂=4096 and n₂=8.
Thus |H∩T|₂≥512, a contradiction.

[The Co₁ certificate](../code/verify_co1_full_socle.g) checks the cover center
fusion, all component involution classes, both class-product coefficients
also by the explicit irreducible-character formula, and all bounded integer
tuples above. The stored normalizer quotient onto G₂(4).2 has kernel order
12, retaining its outer action. The interpretation as the actual subgroup
of Co₁ remains a group-data input. Giudici's Table 3 describes (3.Suz).2 as
an order-three centralizer; the stored fusion instead merges the two
nonidentity central classes of 3.Suz. This proof uses the explicit center
fusion, not that conflicting descriptive label.

## Evidence, limitations and next obligation

All listed deductions together cover every actual factorization and its
orientation from the cited version, including all possible outer lifts.
This supplies the proposed theorem under the stated classification, table and
reviewed research inputs. It does not classify alternating or Lie-type full
socles, nor operations inside their surviving canonical groups.

The source authors read and ran the seven supporting GAP sources with GAP4.15.1;
the five character-table sources additionally pin CTblLib1.3.11. The code
README gives exact commands and limitations. No raw logs or table PDFs are
committed. Source classifications, table/fusion correctness and GAP's group
algorithms are inputs, not independently formalized here. Independent exact-revision review of this assembly is recorded below; no human
review, formal verification or remote CI pass is asserted. C0010 and the main classification
remain open. The next structural obligation is an exhaustive reduction for the
remaining alternating and Lie-type full socles with both factors nonsolvable.


## Independent exact-source review

automated-model reviewers reviewer A, reviewer B and
reviewer C each independently accepted the complete proposed
all-26-sporadic full-Mlt exclusion at exact source
`8cd335ea73dadc72b38b75c294e690bdbeb7c155`. Each checked the actual-factor
exhaustion, both orientations and inherited/new outer extensions, the rank-three
routes, M12 and M24 distinctions, Held characteristic-group and automorphism
arguments, Fi22 central-cover fibers, and Co1 cover-center and original marked
class-square arguments. Each inspected Giudici's indexed primary 8 February 2006
preprint, Theorems1.1–1.2 and Tables1–4; reviewer A additionally
reported checking §3 including the p.6 Aut(M12) passage.

Each reviewer read, independently extracted and ran all seven committed GAP
sources with `gap --quitonbreak -q -b`, obtaining exit0 for every
file under GAP4.15.1 and CTblLib1.3.11 where used. This includes the147 M12
subgroup classes,1696 affine involutions including identity, the Fi22 strict
capacity inequality and all Co1 class-product and bounded-fiber assertions.
The source authors independently ran those sources and Python3.12.14 `check.py`:
115 integrity tests passed. Integrity is separate from mathematical acceptance.

The reviews retain all explicitly pinned prior mathematical inputs and the
Giudici, ATLAS/CTblLib and GAP algorithm assumptions. They did not reconstruct
the external classifications, subgroup/character tables or group algorithms,
and are independent model mathematical reviews, not human or formal
certification or GitHub approval. No inference about the other full socles or
unrestricted C0010 follows.
