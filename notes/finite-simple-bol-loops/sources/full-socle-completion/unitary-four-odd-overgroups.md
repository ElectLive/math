# All odd-field canonical overgroups of PSU4(q)

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010,
with exact-source independent reviews recorded below.** For every odd prime power q, no
finite simple nonassociative Bol loop has canonical group
S=PSU4(q)≤G=LMlt(Q)≤Aut(S), under the canonical, classical and finite
arithmetic inputs below. The equality case is independently reviewed in
[unitary-four-odd-canonical.md](unitary-four-odd-canonical.md), exact source
`99d2ea4385dd2ede08f98ca5ab35092acbc0a598`. We extend it to every actual
overgroup; the final paragraph separately assembles a full-Mlt consequence.

Use the canonical definitions in [PROBLEM.md](../foundations/problem-contract.md), C0001 at
`9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at
`932ead5db5f39045e2085caa6b062f6b981b2813`, and the inner-inversion obstruction
at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. Put H=G₁ and H0=H∩S.
Always |Λ|=[G:H] and H∩Λ²={1}; importantly [H:H0]≤[G:S]. Involutions
used for collision below belong to H0, not merely to H outside S.

## A finite outer-group reduction

The socle S is characteristic in G and C_G(S)=1, so restriction
Aut(G)→Aut(S) is injective: an automorphism fixing S pointwise displaces
each g by an element centralizing S. Write α for the restriction of τ.
If α∈G, the same injectivity makes τ inner, excluded by the cited
component theorem. Thus α∉G and the original formal group G⋊⟨τ⟩ embeds
in Aut(S). In particular all original marks are actual involutions there.

The retained Steinberg automorphism description gives, for q=p^f odd,

    Out(S)=C2×C_(2f)                 if q≡1 mod4,
    Out(S)=D8×C_f                   if q≡3 mod4.

In the second line f is odd and the field generator inverts the diagonal
C4. In both lines the odd direct factor is central. Every mark and τ
have trivial odd outer coordinate. Since G=⟨τΛ⟩, A=G/S lies in the
Sylow-two outer factor. For q≡1, this factor is abelian; the occurring
outer labels αa and α have order at most two, so generation forces
A≤Ω1(Out(S))=C2². Since α∉A, either A=1 or A is one of the three
order-two subgroups. Denote the diagonal label by δ and the q-field
label by σ.

For q≡3 write D8=⟨r,s:r⁴=s²=1,srs=r^−1⟩, with diagonal rotation r.
The outside involution label normalizes A and lies outside it. A=D8 is
therefore impossible. If A is either V4 subgroup, its outside coset has
two order-four rotations and two opposite reflections. Only the latter
can be marks, and their products with the selected α generate at most
⟨r²⟩, contrary to A=V4. Thus A is trivial, C4, or C2; order-two types
are central, even reflection and odd reflection, up to conjugacy.
This reduction uses actual mark generation as well as outer group orders.

## Fields q congruent to one modulo four

Let h=v₂(q−1)≥2 and use the exact inventories and class-square proofs at
`99d2ea4385dd2ede08f98ca5ab35092acbc0a598`. Write

    s=|Sp4(q)|,  o_plus=q²(q²−1)²,  o_minus=q²(q⁴−1),
    c=|GU3(q)|/2,
    R_plus=s/o_plus=q²(q²+1),  R_minus=s/o_minus=q²(q²−1).

The pure diagonal label has one S-class of size |S|/c, whose square
captures the genuine 2+2 inner involution class C2, by the reviewed
[diagonal proof](odd-unitary-four-diagonal.md) at
`7e9eb857e2eae81aece06273632e926448c10d28`. The σ label has two symplectic
S-classes of size |S|/s and one orthogonal-plus class of size |S|/o_plus;
the δσ label has one orthogonal-minus class of size |S|/o_minus. Each
orthogonal class square captures both inner S-involution classes. The
symplectic classes capture the square-minus-one class. There are exactly
these two inner classes in this congruence.

If A=⟨δ⟩, G conjugacy fuses the two symplectic classes and retains the
orthogonal ones. For selected flags e,a,b∈{0,1}, not all zero, original
counting gives

    |H|=2s/(2e+a R_plus+b R_minus).

When an orthogonal class occurs, every integral value has 2-part at least
four: v₂(s)=2h+3, while the nonzero denominators have valuations among
1,2,h+1. Specifically R_plus has valuation1, R_minus has h+1,
R_plus+R_minus has1, 2+R_plus has2, 2+R_minus has1, and
2+R_plus+R_minus has2. Then H0 is even and Cauchy gives a captured
involution. If only the fused symplectic orbit occurs, |H|=s, so
|H0|₂≥|S|₂/2. The uniform order-eight/Frattini witness in the reviewed
canonical proof puts the captured square-minus-one class in H0.

If A=⟨σ⟩, the outside coset has just the diagonal and orthogonal-minus
S-classes. If A=⟨δσ⟩, it has the diagonal class, the fused symplectic
pair, and orthogonal-plus. For the fusion, σ fixes the representative
Jσ with real J used in the canonical proof, whereas δ exchanges its
two S-classes; consequently δσ exchanges them too.

Singleton selections are already impossible. The diagonal singleton
gives |H|=2c and |H0|₂≥2^(h+2). Avoiding C2 makes the full Sylow
preimage in SU4 have unique involution −I, forcing an element of order
at least |H0|₂, whereas the reviewed determinant-one bound is 2^(h+1).
A symplectic singleton means the fused pair and is handled by the
preceding Sylow witness. An orthogonal singleton gives H0 even and
captures both classes.

Every mixed selection captures both inner classes. For diagonal plus
orthogonal-minus,

    |H|=2c o_minus/(c+o_minus),   v₂(c+o_minus)=h+3,

so v₂(|H|)=h+2≥4. To check the sum, remove q²(q²−1)/2; the remaining
factor q(q+1)(q³+1)+2(q²+1) is 8 modulo16. For the other S.2 group,
the general denominator is e(s/c)+2a+b R_plus, e,a,b∈{0,1}.
Here v₂(s/c)=h+1≥3 (valuation on rational numbers is intended).
The mixed denominators have valuation1, or valuation2 when a=b=1.
Thus |H| is divisible by four whenever integral, H0 is even, and a
captured involution contradicts H∩Λ²={1}. This exhausts the q≡1 overgroups.

## Fields q congruent to three modulo four

Put t=v₂(q+1)≥2. Every individual semilinear S-class square captures
the genuine 2+2 inner class C2, by the reviewed all-odd canonical proof.
Every pure-diagonal S-class square also captures C2, by the reviewed
diagonal proof. Hence H0 avoids C2 for all remaining outer configurations.
Its full Sylow preimage in SU4 has order4|H0|₂ and unique involution −I;
the reviewed unique-involution and eigenvalue bounds give

    2|H0|₂ ≤ 2^(t+1).                                    (2)

Use the reviewed q≡3 semilinear inventory, one S-class of each compatible
geometric type in each actual label, and put

    s=|Sp4(q)|/2,  o_plus=q²(q²−1)²,  o_minus=q²(q⁴−1),
    R=s/o_plus=q²(q²+1)/2≡1 mod4,
    T=s/o_minus=q²(q²−1)/2,   k=(q−1)/2.

Their valuations are v₂(s)=v₂(o_plus)=2t+2, v₂(o_minus)=t+2,
v₂(T)=t, and k is odd. For t≥3 the diagonal label has just the
nonsplit class, of centralizer c=k o_minus. For t=2 it also has a
split class of centralizer |GU3(q)|/4, explicitly retained below.

If A=C4, diagonal conjugation fuses the corresponding classes in the
two even and the two odd reflection labels. The three G-orbit sizes
are 2|S|/s, 2|S|/o_plus and 2|S|/o_minus. A nonempty selection gives
|H|=2s/(a+bR+dT), a,b,d∈{0,1}. If a or b is nonzero the denominator
has valuation at most one; otherwise its valuation is t. Dividing the
resulting lower bound by [H:H0]≤4 yields |H0|₂≥2^(t+1), contrary to (2).

If A=⟨r²⟩, its outside coset has two reflection labels of the same
parity. Its conjugation fixes the individual S-classes because r² lies
in the corresponding projective-centralizer image D². In even parity
select a,b∈{0,1,2} symplectic and orthogonal-plus classes. Then
|H|=2s/(a+bR); for nonzero a+b the denominator valuation is at most two.
Consequently |H0|₂≥2^(2t), impossible by (2). In odd parity one or two
orthogonal-minus classes give |H0|₂≥2^(t+1), again impossible.

If A is a reflection C2, its normalizer is a V4. The outside coset
therefore consists of the central diagonal label r² and the opposite
reflection. Mark generation forces both these labels to occur: if all
marks had the label of τ, every element of τΛ would lie in S.
For t≥3 and an even reflection label, the three possible S-class sizes
give |H|=2ks/[k(a+bR)+dT], a,b,d∈{0,1}. If a or b is nonzero the
denominator valuation is at most one; a diagonal singleton instead
gives |H0|₂≥2^(t+2). Thus even the enlarged selection list violates (2).

For an odd reflection label and t≥3, generation requires the diagonal
and orthogonal-minus classes. Their count gives

    |H|=2k o_minus/(k+1),    v₂(|H|)=4,

so |H0|₂≥8. Here we use a second captured class instead of (2) alone.
There are exactly two inner S-involution classes for t≥3: C2 and the
1+3 class C1 represented by a·diag(−1,1,1,1), a∈μ with a⁴=−1.
To see completeness, a lift squares into μ4. Squares ±1 can be
centrally rescaled to1. A primitive order-four square has eigenvalues
±a of norm one and determinant one forces an odd eigenspace dimension.
Dimensions1 and3 are projectively equivalent, scalar choices differ by
the central μ4, and GU1×GU3 has onto determinant, so it gives one S-class.

For an orthogonal-minus outside lift F, choose a real orthogonal
reflection u on its fixed quadratic space and put x=a u. It is unitary
of determinant one and projects into C1, with F(x)=x^−1. Thus Fx is
positive-square and in the same actual outer label as F; the unique
orthogonal S-class in that label makes it S-conjugate to F. Its square
therefore captures C1 as well as C2. H0 would have to be odd, contradicting
the lower bound eight.

## The extra diagonal class when q is three modulo eight

For t=2, C2 is the only inner S-involution class, as proved in the
reviewed canonical manuscript. The odd-reflection coset can contain
the orthogonal-minus class and either or both diagonal classes. The
split diagonal class size has valuation2, while the orthogonal-minus
and nonsplit diagonal sizes have valuation3; the ratio of the latter
two is k=(q−1)/2≡1 mod4. If the split class occurs, the total has
valuation2. Otherwise the possible total valuation is3 or4. Since
|S|₂=2⁷, this gives |H0|₂≥8, contradicting capture of C2.

In the even-reflection coset all four S-classes must be retained as
possible selections. Their sizes, in the certificate's order, are

    q²(q³+1)/2,                  q⁴(q³+1)(q²+1)/4,
    q³(q−1)(q²+1),               q⁴(q+1)(q³+1)/2.

They are respectively symplectic, orthogonal-plus, diagonal split and
diagonal nonsplit, obtained by dividing |S| by the reviewed centralizers.
Generation requires at least one of the first two and one of the last
two, giving exactly nine masks. We do not assume that valuations of
individual class sizes control their sum: cancellation actually occurs.

The [integer polynomial certificate](../code/verify_unitary_four_overgroups.py)
checks each mask as follows. Write the rational prospective order
2|S|/(sum of selected sizes) as N(q)/D(q), with integer polynomials.
The certificate verifies its cross-multiplied identity, not a numerical
fit. It then verifies integer polynomial A,B and positive integer k
with AN+BD=k. If N(q)/D(q) is integral, D(q) divides k. Each coefficient
of D(1027+x)−k is checked positive, proving D(q)>k for all integers
q≥1027 and hence nonintegrality throughout the tail. For every smaller
integer q=3,11,…,1019, it checks the original class-size sum directly:
every integral prospective |H| is divisible by four. There are exactly
128 such integers, a safe superset of the admissible prime powers.
Thus whenever H could exist, H0 is even. Its involution belongs to
C2 and collides with the selected class square. This closes the final
outer configuration and proves the proposed canonical-overgroup theorem.

## Source, evidence, and full-socle assembly

The standard outer automorphism description and all S-class inventories,
class-square witnesses, eigenvalue bounds and field conventions retain
the exact sources and three reviews in the canonical manuscript at
`99d2ea4385dd2ede08f98ca5ab35092acbc0a598` and the diagonal theorem at
`7e9eb857e2eae81aece06273632e926448c10d28`. The new ingredients are the
outer-generation reduction, actual overgroup fusions, H0 counts, C1
witness and the nine-mask arithmetic. The coordinator read and ran the
certificate with Python3.12.14 and assertions enabled; it passed all
identities, tail and finite checks. It uses only the standard library.
The stored integer Bézout data are self-verifying; their development
generator used SymPy1.14.0. Run from the repository root:

    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_unitary_four_overgroups.py

The contributor contributor 1 developed the overgroup argument;
contributor 2 independently checked it in development
and ran the scratch certificate. Neither is a substitute for independent
review of this exact canonical source, recorded below.

With the independent reviews below, the theorem also completes the **full-Mlt
socle PSU4(q)** exclusion for proper simple Bol loops. In odd characteristic,
the corrected solvable-factor reductions (source
`fbc63aab2c35d93038789802c01d0c04fad82a3b`) exclude proper solvable G or I.
For both proper nonsolvable factors, LWX unitary Theorem1.2/Table1.1 in
dimension four is exhausted by the line/parabolic pairs, symplectic pair,
and finite q=3,5 pairs. Their two actual orientations are excluded by the
[parabolic completion](even-unitary-line-parabolic-factors.md),
[component-intersection theorem](even-unitary-component-intersections.md)
and [finite-pair theorem](unitary-finite-factor-pairs.md), independently
reviewed at `5bc50f40f63047aab89343dece4fc981c1df1afd`, with their actual
embedding and source-correction qualifications intact. The only remaining
case has S≤G and is covered above. In characteristic two the separately
reviewed [full unitary assembly](characteristic-two-unitary-full-socles.md)
already applies, at the same 5bc source. This is an assembly of conditional
deductions, not a reproof of the external factor classification or an
operation classification. Other classical socles and C0010 remain open.


## Independent review of the overgroup theorem and full-socle assembly

GPT-6.1 Terra contributor 3, contributor 4 and contributor 5 independently accepted both deductions at exact source `a88c1a1cd84e8c9da09630570a8a6abe41c6fd5c`, conditional on the cited canonical, automorphism/form, class-square, corrected factor-classification and prior-review inputs. Each checked faithful restriction, the outer generation reduction, all actual C2²/D8 subgroups and cosets, class fusions, original H0 index losses, the C1 witness and internal-class completeness, and both t=2 diagonal types. Each checked the final actual-factor routing rather than inferring a full-socle result from G=S alone.

All three read, extracted and independently ran the committed standard-library certificate with Python3.12.14 and assertions enabled. Every nine-mask cross-identity, integer Bézout identity, strict coefficient tail and all 128 integer-prefix checks passed. contributor 3 freshly inspected LWX unitary v2 Table1.1, GLWX v4 §2.2(V) and Conrad Theorem4.10; the other two retained the recorded primary-source inspections. Earlier rational-class and factor-source inputs were retained rather than rederived wholesale, and unchanged older certificates were not rerun. These are model mathematical/code reviews, not formal GitHub approvals or a proof of C0010/operation classification.
