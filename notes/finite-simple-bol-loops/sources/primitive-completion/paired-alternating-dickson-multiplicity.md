# Four nonproduct paired folders over A_(7^6)

**Mira Cult**

**Independently reviewed at the exact source recorded below**, continuing
[0323:C0010](../../claims/0010.md). Put N=7^6=117649 and T=A_N. There are
at least four pairwise nonisomorphic simple proper Bol loops with entire
canonical left multiplication group T², factor-swapping inversion and a
nonproduct stabilizer with common quotient C2. Their order is |T|=N!/2,
not N. Their regular stabilizers also give at least four nonsplitting
Rota–Baxter classes under the equivalence specified in GG24 §4. Thus they
contradict the numerical assertion in arXiv:2404.14078v1, Theorem4(2)(b),
which gives two in this degree.

This is a lower bound and an exact-version source correction, not an
exhaustive classification in degree N or a claim of literature priority.
The Bol conclusion retains the [all-alternating paired normal form](paired-alternating-sign-bridge.md)
at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0) and its upstream canonical
folder inputs. The Rota–Baxter comparison uses the direct regular-subgroup
correspondence and orbit lemma in [the paired source](../factor-permutation/radical-free-paired-simple-envelopes.md)
at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e898d8a00b1fc97431ad8092b4e51b9217650187). Aut(A_N)=S_N is the
already pinned [alternating automorphism input](../foundations/references.md#lyons99-alternating-automorphisms).
No classification of nearfields is needed for this explicit construction.

## Two sharply two-transitive even groups

Let E=F_(7^6), choose primitive ζ∈E*, and use left composition of maps.
Write σ(x)=x^7 and use a scalar to denote multiplication by it. For u=1,5
define

    a=ζ^6,    b_u=ζ^u σ,    L_u=⟨a,b_u⟩≤GL_6(7),
    B_u=E^+⋊L_u acting affinely on E.

The scalar subgroup S0=⟨a⟩ has order M=19608, and

    b_u a b_u⁻¹=a^7,    b_u^6=a^(3268u).                  (1)

The Galois image of L_u has order six and (1) makes its scalar kernel
exactly S0: every word has a normal form a^i b_u^j, 0≤i<M, 0≤j<6.
These 6M normal forms are distinct by their Galois components and scalar
powers. Consequently |L_u|=6M=117648=N−1, and the presentation consisting
of (1) and a^M=1 is complete. This last observation ensures that characters
defined from those relations below have no unexamined extra relations.

The six S0-orbits on E* are labeled by the exponent modulo six. The map
b_u acts on them by i↦u+7i=i+u, a six-cycle for both choices of u. It
follows that L_u is transitive, and hence regular, on E*. Thus B_u is
sharply two-transitive on E.

Both groups B_u consist of even permutations. A translation by a nonzero
vector is a product of 7-cycles. The elements a and b_u fix 0 and act on
E* in their regular-group permutation representation. We have

    |a|=19608,    |b_u^6|=6,    |b_u|=36,
    (N−1)/|a|=6,    (N−1)/|b_u|=3268.

The order of b_u follows because its Galois image has order six and its
sixth power has order six. Both displayed numbers of even-length cycles
are even, so a and b_u are even permutations. These elements and the
translations generate B_u, proving B_u≤T.

An involution in L_u must be −I: over characteristic seven an involutory
linear map is diagonalizable with eigenvalues ±1, and regularity on E*
rules out eigenvalue1. In our cyclic subgroup this involution is

    −I=a^9804.                                             (2)

## Four correlated stabilizers

For x,y∈F2 define ε_xy on L_u by ε_xy(a)=x, ε_xy(b_u)=y. In the
complete presentation, M and 3268u are even and 7 is odd, so all four
assignments are homomorphisms to C2. Each nonzero assignment is onto.
Extend them to B_u by killing E^+. Equation (2) has even exponent, so
every ε_xy kills −I.

Fix the two field points 0,1, and let

    Y=(S_(N−2)×S2)∩A_N,    Y0=A_(N−2),
    ν:Y→Y/Y0=C2.

Here Y0 fixes both points, and ν records whether they are interchanged.
Sharp two-transitivity gives T=Y0 B_u exact and Y∩B_u=⟨r⟩, where
r:x↦1−x. Thus ν(r)=1 while ε_xy(r)=0. For each u=1,5 choose the two
characters (x,y)=(0,1),(1,0), and set

    H_(u,x,y)={(s,b)∈Y×B_u: ν(s)=ε_xy(b)}≤T².            (3)

Their common quotient is C2 and their intersection map on ⟨r⟩ is
bijective. The reviewed paired criterion therefore makes (3), with full
anti-diagonal section, a faithful simple proper Bol folder. Both projections
are nontrivial and proper. The stabilizer is not the product of its
projections. The C2 collision/regularity equivalence makes H_(u,x,y)
regular for the left–right action of T² on T, without any ambivalence
assumption on T.

## No equivalences between the four choices

First separate the two affine groups. The prime 43 has multiplicative
order six for 7: 7³≡−1 mod43, while 7 and 7² are not1 mod43. Since
43∤6, the Sylow43 subgroup of L_u lies in its cyclic normal subgroup S0.
It is unique and characteristic. A nonidentity element of its order43
subgroup has degree six over F7, so its centralizer in GL_6(7) is the
full field-scalar group S=E*.

It follows that any linear map conjugating L_u to L_v normalizes S.
The normalizer is S⋊⟨σ⟩: a normalizing linear map induces an F7-field
automorphism of the scalar algebra E, and after removing that automorphism
it is scalar. Conjugating b_u by ζ^wσ^j changes its scalar exponent to

    7^j u+(1−7)w ≡ u mod6.                               (4)

Equality of the two generated groups requires equality of this exponent
modulo six, because the scalar kernel is S0. Therefore L_1 and L_5 are
not GL_6(7)-conjugate.

The translation subgroup E^+ is the unique Sylow7 subgroup of B_u: it
is normal and |L_u| is prime to seven. Any permutation conjugacy between
the B_u must preserve this regular translation group. Its permutation
normalizer is AGL_6(7), since a normalizer fixing 0 is an automorphism of
the additive group and hence F7-linear. A target translation then aligns
the point stabilizers, producing the excluded linear conjugacy. Thus B_1
and B_5 are not S_N-conjugate.

Within either B_u, the same characteristic Sylow43 argument recovers S
from its linear point stabilizer and hence recovers S0=L_u∩S. A linear
normalizer preserves S0. A character that kills S0 cannot be carried to
one that is nontrivial on it. Aligning the affine point stabilizers by a
translation does not alter a character, since homomorphisms to C2 are
invariant under inner conjugation. Therefore the two selected characters
(0,1),(1,0) are inequivalent under the full permutation normalizer of B_u.
(The two assignments with x=1 do fuse: scalar ζ changes b_u by an odd
power of a. Only one of them is needed for our lower bound.)

The kernels and projections are recoverable from (3). Since
|Y|=(N−2)!>|B_u|=N(N−1), coordinate swap cannot identify two of our
larger-first ordered data. Simultaneous Aut(T)=S_N conjugacy has already
been excluded. The exact paired isomorphism criterion proves that the
four loops are pairwise nonisomorphic.

## The precise Rota–Baxter source discrepancy

GG24 §4 defines H_B={(B(g),gB(g)):g∈T}, defines Q(T) immediately before
Proposition11, and defines equivalence immediately after it by the Q(T)
action on these subgroups. The project directly inspected that exact
version. Its Q(T) is generated by diagonal Aut(T), one-coordinate inner
automorphisms and coordinate swap, exactly the action in the reviewed
paired correspondence. For a regular H, T²=ΔT H; writing a conjugator
as dh shows that its action on H equals diagonal conjugation by d.
Thus these extra inner actions do not fuse any of our four classes.
Their C2 fiber products are nonproduct, so their RB maps are nonsplitting.

Theorem4(2)(b) in §7 gives two equivalence classes at degrees q^m≠9
apart from its displayed exceptional degrees49,529. Our degree7^6 meets
all its numerical conditions: q=7≡3 mod4, m=6≡2 mod4, and both prime
divisors of m divide q−1. It is none of the exceptional degrees. The
four inequivalent regular graphs above therefore disprove that numerical
count in arXiv:2404.14078v1. The proof there counts two character types
for a fixed sharply two-transitive factor; the two distinct embeddings
L_1,L_5 show why that count cannot automatically be a total at fixed degree.
The exact source and locators are in
[REFERENCES](../foundations/references.md#paired-dickson-multiplicity-source).

This does not directly contradict the earlier A10-specific upper bound
used in the ambivalent table, which came from part(2)(c); nor does it
certify the rest of the paper. The general alternating counting problem
must retain the embedded sharply two-transitive factor as data. No claim
that our four examples are all examples in degree N is made.

## Verification and review boundary

The proof is uniform finite-field/group reasoning with explicit integer
values; it does not enumerate A_N or its loops. The project checked
7^6−1=117648, M=19608, M/6=3268, the sixth-power orders for u=1,5 and
the powers of 7 modulo43. These arithmetic controls do not prove the
normalizer or loop assertions. Independent mathematical reviews of the committed construction, separation
argument and exact-version source correction are recorded below.


## Independent exact-source review

reviewers contributor 1,
contributor 2 and contributor 3
independently accepted the full construction and exact-version source
correction at [the source revision](https://github.com/Mira-Cult/math-wip/commit/548422d3235f09ef41bfc42af11905f8123f81a6). They checked the
complete semilinear presentation, sharp two-transitivity, evenness, character
kernels, correlated-folder construction, affine and scalar-normalizer
separation, and the passage to four distinct Q(T)-equivalence classes.
Each independently inspected GG24v1 §4's Q(T) and equivalence definitions
and §7 Theorem4(2)(b), confirming that the stated numerical count is the
one contradicted. No finite enumeration of A_N or of its loops was used.

The acceptances retain the pinned canonical-folder, isomorphism and RB
correspondence inputs and the alternating automorphism theorem; these
upstream results were not independently reproved. They establish the four-
class lower bound and the discrepancy in that exact source version, not
an exhaustive classification at N, invalidity of the separate A10 part(2)(c),
claims about later source versions, or literature priority. These are model
mathematical/source reviews, not human/formal certification or formal GitHub
approval.
