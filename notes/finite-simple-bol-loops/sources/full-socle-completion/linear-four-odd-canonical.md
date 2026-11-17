# Canonical PSL4(q) for every odd q

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010,
with exact-source independent reviews recorded below.** Let q=p^f be an odd prime power
with no further congruence restriction. No finite simple nonassociative Bol loop has its entire
canonical group G=LMlt(Q)=S=PSL4(q), conditional on the canonical and classical
inputs below. This concerns actual G=S, not an arbitrary section or G>S.
Use the definitions in [PROBLEM.md](../foundations/problem-contract.md), C0001 at
`9431ade99316d6bc62efb389492fef385b510b45` and scoped inversion at
`932ead5db5f39045e2085caa6b062f6b981b2813`. The original marks satisfy
|Λ|=[S:H] and H∩Λ²={1}.

Inner inversion is excluded at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`.
The [all-odd-field diagonal theorem](odd-linear-four-diagonal.md), independently
reviewed at `6c836d271832aa25cc0fcb120f31d8c4f1e2ebad`, covers pure diagonal
inversion. We handle graph, field and graph-field components, including every
diagonal twist, and every actual marked-class selection. The classical
automorphism description is Kleidman–Liebeck Theorem2.1.4 and Tables2.1.B–D,
pp.15–16,19, retained in [the earlier PSL4 source](../primitive-completion/hs-psl4-odd.md).

## Fields q congruent to one modulo four

Until the separate q≡3 section below, assume q≡1 mod4.

### Common collision and a necessary Sylow bound

Put e=v₂(q−1)≥2. The local proof in
[hs-psl4-odd.md, “The case q≡1 mod4: a common captured class”](../primitive-completion/hs-psl4-odd.md),
reviewed at `32b5918c4b3fa3b2686185006b80d41b1ece76aa`, shows that the square
of **each** S-class of nonidentity involutory automorphisms captures the
S-class I of diag(−1,−1,1,1). Only its determinant-one conjugators and the
PGL invariance of I are used; its HS-folder hypotheses are not imported.
Therefore H avoids I independently of its selected union.

The complete inverse image in SL4(q) of a Sylow 2-subgroup P of H has order
4|P| and unique involution −I: all other genuine SL involutions are of
eigenspace dimensions 2+2 and project into I. Conrad's unique-involution
theorem and generalized-quaternion cyclic-subgroup result, Theorems4.10 p.8
and3.2 p.2, pinned in [the diagonal proof](odd-linear-four-diagonal.md), give
an element of order at least 2|P|. Every 2-element of SL4(q), however, has
order at most 2^(e+1). Its irreducible eigenvalue degrees are at most four;
degrees1,3 have 2-part at most (q−1)₂, degree2 at most (q²−1)₂=2^(e+1),
and a degree-four orbit fills the space and determinant one forces order
dividing (q⁴−1)/(q−1), whose 2-part is four. Consequently

    |H|₂ ≤ 2^e.                                             (1)

## Graph and graph-diagonal labels

Let PGL=PGL4(q) and D=PGL/S=Fq*/(Fq*)⁴, of order four. A graph involution
is α_B=Int(B)γ, where γ is inverse transpose and Bᵀ=±B after scalar
normalization. Finite-field congruence gives three PGL orbits: symmetric
plus, symmetric minus and alternating. Symmetric plus and alternating
forms have square determinant and occupy the two even graph labels;
symmetric minus forms occupy the two odd labels.

For either orthogonal type the similitude multiplier is onto Fq*. In plus
dimension four, use diag(k,1) on each hyperbolic plane; in minus dimension
four use it on a hyperbolic plane and multiplication of norm k on the
anisotropic plane. These choices have determinant k². All similitudes
have determinant ±k², and reflections realize the other sign. Since −1
is square, their image in D is exactly D², of order two. Symplectic
similitudes likewise have all multipliers and determinant k² (use a
symplectic basis or the Pfaffian), with the same D-image.

The projective similitude centralizer orders are |O4±(q)| and |Sp4(q)|:
the multiplier factor q−1 cancels the scalar quotient q−1. Each meets S
in index two. Hence **each PGL orbit has two S-classes total**, not two
classes in each label. Conjugation by diagonal class δ changes the graph
label by δ², so those two S-classes occupy the two distinct labels of their
parity. Each even label has precisely one plus-symmetric and one alternating
class, with S-centralizer orders

    c_o = q²(q²−1)²,
    c_s = q⁴(q²−1)(q⁴−1)/2,
    R = c_s/c_o = q²(q²+1)/2.

If a,b∈{0,1} count the selected orthogonal and symplectic classes, with
a+b>0, original marked counting gives |H|=c_s/(aR+b). Nonintegral values
are impossible. Since R≡1 mod4, the denominator has 2-valuation zero for
a singleton and one when both classes occur. As v₂(c_s)=2e+2, every
integral selection has |H|₂≥2^(2e+1), contrary to (1).

Each odd graph label instead has exactly one symmetric-minus S-class.
Its S-centralizer is |O4−(q)|/2=q²(q⁴−1), of 2-part 2^(e+2). Thus
|H|₂=2^(e+2), again contradicting (1). This covers all four graph labels.

## Field and graph-field labels

A nontrivial field component of an involution requires q=r², r odd, and
is σ:x↦x^r, possibly accompanied by γ. There is one PGL-conjugacy orbit
of projective involutions of each semilinear kind. We spell out the scalar
descent instead of inferring it from a small-field table.

For the field kind, write the lift Aσ with A bar A=cI. Commutation makes
c∈Fr*. Norm surjectivity lets us rescale A to norm one; matrix Hilbert90
then conjugates Aσ to σ. For graph-field kind, the involution condition
gives A=c bar Aᵀ with c bar c=1. Scalar Hilbert90 rescales A to a Hermitian
matrix, and all nondegenerate Hermitian four-forms over F_(r²)/Fr are
congruent, so it is PGL-conjugate to γσ. These are also the classical
descent statements in Burness Proposition3.43(i), cited in the reviewed
local source. Their determinant-one witnesses there transfer by PGL
conjugation because I is PGL-invariant.

The PGL centralizers are PGL4(r) and PGU4(r). For the first, a matrix fixed
projectively by σ can be rescaled to an Fr matrix by scalar Hilbert90.
For the second, the projective fixed matrices are unitary similitudes;
norm surjectivity rescales each to a unitary isometry. The determinant
images of these centralizers in D have orders

    d_f = 4/gcd(4,r+1),        d_u = 4/gcd(4,r−1),

respectively, since determinants run over Fr* and the norm-one subgroup
of F_(r²)*. Thus their actual S-centralizer orders are

    c_f = |PGL4(r)|/d_f,       c_u = |PGU4(r)|/d_u.

Conjugating a semilinear label by δ∈D changes it by (1−β)δ, where β acts
as r on D for σ and as −r for γσ. The total numbers of S-classes in
these PGL orbits are 4/d_f and 4/d_u, while the numbers of actual labels
are 4/gcd(4,r−1) and 4/gcd(4,r+1). Their quotients are both two, because
one of r−1,r+1 has 2-valuation exactly one. D acts transitively on labels,
so every admissible actual label has exactly two equal-sized S-classes.
Labels with no involutions supply no possible τ. All diagonal twists are
therefore accounted for without assuming a single S-conjugacy class.

The marked set selects k=1 or2 classes, so |H|=c_f/k or c_u/k. Put
a=v₂(r−1), b=v₂(r+1), so e=a+b and min(a,b)=1. Standard group orders give

    v₂(c_f) = 3a+2b+1−v₂(d_f),
    v₂(c_u) = 2a+3b+1−v₂(d_u),

where v₂(d_f)=1 if b=1 and zero otherwise, and v₂(d_u)=1 if a=1 and
zero otherwise. In both cases v₂(c)−1>a+b. Even the two-class selection
therefore violates (1). Together with the inner, pure diagonal and graph
cases, this exhausts involutory canonical inversion and proves the proposed
G=S exclusion for all q≡1 mod4.

## Fields q congruent to three modulo four

Now suppose q≡3 mod4 and put t=v₂(q+1)≥2. Its prime-field exponent f is
odd, so the involutory outer field component is trivial. Inner and pure
diagonal inversion are already covered. It remains to consider the two
graph labels. The reviewed local roster in [hs-psl4-odd.md](../primitive-completion/hs-psl4-odd.md)
at `32b5918c4b3fa3b2686185006b80d41b1ece76aa` gives two symplectic S-classes
in the pure graph label, each of centralizer order C=|Sp4(q)|, together with
one symmetric-plus class of centralizer order O=q²(q²−1)². The graph-diagonal
label has one symmetric-minus class of centralizer order Q=q²(q⁴−1).
Their 2-parts are respectively 2^(2t+3), 2^(2t+2), 2^(t+2), and
|S|₂=2^(2t+3). Set R=C/O=q²(q²+1)≡2 mod8.

The projective involutions with SL4 lifts squaring to −I form one S-class
J_minus. Their minimal polynomial is the irreducible quadratic x²+1;
the GL centralizer is GL2(q²), whose determinant is the surjective norm.
Thus the GL class does not split in SL, and the projective class is
PGL-invariant. Its presence in the square of either symplectic class can
be seen explicitly. Put

    M=[[0,−1],[1,0]],   x=diag(M,Mᵀ),
    J=[[0,I2],[−I2,0]].

Then x²=−I, Jx is alternating and Pf(Jx)=Pf(J). Any congruence carrying
J to Jx consequently has determinant one, by the Pfaffian congruence
formula. Hence α_J and α_(Jx) are S-conjugate and their product is the
projective class of x (or its inverse, the same projective involution).
This lies in J_minus. PGL conjugation transfers the witness to both
symplectic S-classes.

Every subgroup of index at most two in a Sylow 2-subgroup of S meets
J_minus. Indeed take z∈F_(q²)* of order eight and view diag(z,z^−1) on
F_(q²)² as an Fq-linear matrix g. It has determinant Norm(1)=1,
g⁴=−I and g² noncentral. Its projective image has order four. Conjugate
that image into any Sylow subgroup P; its square belongs to Φ(P) and
projects into J_minus, so lies in every index-two subgroup. A selection
of one or both symplectic classes alone gives |H|=C or C/2. Its Sylow
subgroup has the required index at most two, contradicting H∩Λ²={1}.

If the symmetric-plus class is selected, its square contains the genuine
class I=diag(−1,−1,1,1) by the reviewed local symmetric-form witness.
The full inverse image of a Sylow subgroup of H in SL4 now has order
2|H|₂ and unique involution −I. The unique-involution theorem forces an
element of order at least |H|₂. The determinant-one eigenvalue argument
bounds it by 2^(t+1): degrees1,3 have 2-part two, degree2 at most
(q²−1)₂=2^(t+1), and degree4 fills the space and has determinant-one
factor (q⁴−1)/(q−1), also of 2-part 2^(t+1). Thus |H|₂≤2^(t+1).
If k∈{0,1,2} symplectic classes accompany the symmetric-plus class,
then |H|=C/(R+k). The denominator valuations are 1,0,2 respectively;
any integral selection has |H|₂≥2^(2t+1)>2^(t+1), a contradiction.
Finally the sole symmetric-minus class gives |H|=Q and
|H|₂=2^(t+2)>2^(t+1), with the same genuine-class collision.

This covers every graph selection. Together with the reviewed inner and
diagonal exclusions and the preceding q≡1 analysis, it proves the proposed
canonical PSL4(q) exclusion for every odd q. It does not identify any
larger canonical overgroup with S, nor replace the original loop by a
quotient.

## Sources, evidence and limits

Draisma, *Multilinear Algebra and Applications* (Fall2015), Theorem10.6.118,
printed p.75, [author notes](https://math-unibe.ch/jdraisma/publications/mlappl.pdf),
classifies symmetric forms by rank and determinant square class; the
coordinator freshly inspected its statement. Alternating bases, Hermitian
congruence, matrix Hilbert90, finite-field norms and the classical order
formulas are retained standard inputs, with the scalar/projective applications
and multiplier constructions written here. The older primary-source record
pins Burness's 8 July2006 manuscript, Proposition3.43(i), printed p.22; a fresh
fetch during this continuation timed out, so no new inspection is claimed.
The above descent supplies the application directly. The new proof introduces
no computation. contributor 1 developed the candidates; the
coordinator corrected the graph-class count before this canonical version.
Independent exact-source reviews are recorded below. Higher dimensions and canonical overgroups G>S remain outside this theorem.


## Independent exact-source review

GPT-6.1 Terra contributor 2, contributor 3 and contributor 4 independently accepted this deduction at exact source `99d2ea4385dd2ede08f98ca5ab35092acbc0a598`, conditional on its cited canonical, classical automorphism, finite-field form/descent, finite-group and prior-review inputs. Each checked the actual graph labels and two S-classes per PGL orbit in q≡1, the field/graph-field descent and centralizer determinant images, every selected union, q≡3 symplectic Pfaffian witness, order-eight Frattini construction and the determinant-one unique-involution bound. contributor 2 freshly inspected Draisma and Conrad and reread the exact inherited HS local proof at `32b5918c4b3fa3b2686185006b80d41b1ece76aa` for its scoped class-square application. The others retained recorded primary-source inspections; none newly reverified KL, matrix Hilbert90 or all classical form/order inputs. The retained Burness access limitation remains explicit. No new computation was used. These are scoped model mathematical reviews, not formal GitHub approvals. The conclusion concerns the entire canonical group G=S only; canonical overgroups G>S, larger dimensions and the full classification remain open.
