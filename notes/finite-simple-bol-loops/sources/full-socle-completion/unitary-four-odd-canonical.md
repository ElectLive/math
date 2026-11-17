# Canonical PSU4(q) for every odd q

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010,
with exact-source independent reviews recorded below.** Let q=p^f be any odd prime power.
No finite simple nonassociative Bol loop has its entire canonical group
G=LMlt(Q)=S=PSU4(q), conditional on the canonical, automorphism and form inputs
specified here. Definitions are in [PROBLEM.md](../foundations/problem-contract.md). Use C0001 at
`9431ade99316d6bc62efb389492fef385b510b45`, scoped inversion at
`932ead5db5f39045e2085caa6b062f6b981b2813`, and the original marked identities
|Λ|=[S:H], H∩Λ²={1}. No quotient loop or larger canonical overgroup is used.

Inner inversion is excluded at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8` and
pure diagonal inversion by [the reviewed odd-unitary diagonal theorem](odd-unitary-four-diagonal.md)
at `7e9eb857e2eae81aece06273632e926448c10d28`. The standard unitary automorphism
description, pinned to Steinberg Theorem3.2 and statements3.3–3.6 p.608 in
[the canonical unitary source](../primitive-completion/radical-free-unitary-inversion.md), has diagonal
group C_gcd(4,q+1) and cyclic field group C_(2f). Thus every remaining involution has
field component σ:x↦x^q on F_(q²), with an appropriate diagonal label. We derive the
inventories and all selected-union exclusions for both congruences below. GU denotes the full
unitary isometry group; SU its determinant-one subgroup.

## Fields q congruent to one modulo four

Until the separate q≡3 section below, assume q≡1 mod4.

### Rational outside classes and projective centralizers

Put μ={c∈F_(q²)*:c^(q+1)=1}; PGU/S=μ/μ². A semilinear projective involution
has a unitary lift F=Aσ with F²=cI. Commuting F with F² gives c=c^q=c^−1,
so c=±1. Multiplication of F by a norm-one scalar does not change this sign.
The center of SU4(q) has order two.

If F²=1, fixed-space descent gives a nondegenerate symmetric four-space (W,b)
over Fq. In an orthonormal Hermitian basis, if B is a matrix of an Fq basis
of W, then A=B(bar B)^−1 and det b=Norm(det B). The square character of
det A in μ equals that of det b in Fq*: writing det B as a power of a generator
of F_(q²)* makes both characters its exponent modulo two. Thus plus forms
occupy the square diagonal label and minus forms the nonsquare label.
Classification by dimension and discriminant gives one GU-conjugacy class
for each type. Its actual GU centralizer is O4±(q), with determinant image
{±1}. Since q+1≡2 mod4, −1 is nonsquare in μ. The projective centralizer
therefore maps onto PGU/S, so each type is a single S-conjugacy class.

For x∈SU with xFx^−1=cF projectively, determinants give c⁴=1. There is no
order-four element in μ, so c=±1. The commuting subgroup is SO4±(q).
The anticommuting coset exists: choose trace-zero η∈F_(q²)* and set
k=Norm(η)^−1, which is nonsquare in Fq. A quadratic four-space of either
type has a similitude y of multiplier k and determinant k². On each
hyperbolic plane use diag(k,1); on an anisotropic plane use multiplication
by an element of norm k in F_(q²). The minus four-space is a hyperbolic plane
plus an anisotropic plane. Then x=ηy is unitary, det x=η⁴k²=1, and
Fx=−xF. This doubles the commuting subgroup before dividing by the scalar
center of order two. Consequently the S-centralizer orders are

    o_plus = q²(q²−1)²,       o_minus = q²(q⁴−1).

If F²=−I, antiunitarity gives h(v,Fv)=0. Choose a nonsingular vector, normalize
its norm to one, and repeat on the orthogonal complement of its pair v,Fv.
Every such F is GU-conjugate to Jσ, where J=diag(J2,−J2) and
J2=[[0,1],[−1,0]]. Its centralizer in GU is Sp4(q), of determinant one.
For a direct descent explanation, choose λ∈F_(q²) with Norm(λ)=−1. The involution λF
has a four-dimensional fixed space on which h takes trace-zero values and is
alternating; division by a nonzero trace-zero scalar gives a nondegenerate
Fq alternating form. Its isometry group is precisely the centralizer.

In the projective GU centralizer, xFx^−1=cF implies xAxᵀ=cA. The Pfaffian
congruence formula gives det x=c². Hence its image in μ/μ² is trivial, so
the projective GU orbit splits into exactly two S-classes. Both have square
diagonal label: A is skew, and Pf(A) has norm one (use bar A=−A^−1 and the
four-dimensional Pfaffian inverse formula), so det A=Pf(A)². The real unitary
matrix X=[[0,I2],[−I2,0]] anticommutes with J, has determinant one, and
satisfies X²=−I. It supplies the anticommuting SU coset. As before, the
doubling cancels the scalar center, so both S-centralizers have order

    s = |Sp4(q)| = q⁴(q²−1)(q⁴−1).

Scalar changes of F do not add types: in the positive-square case they scale
the descended form, preserving its four-dimensional discriminant; the
negative-square case has the single GU class just derived. Thus the square
semilinear label has exactly two symplectic classes and one orthogonal-plus
class, and the other label has one orthogonal-minus class. These are actual
S-classes, not merely geometric types.

## The two inner classes and original class-square witnesses

There are exactly two nonidentity involution S-classes. A lift u∈SU has
u²=±I. Positive-square noncentral lifts have a nondegenerate 2+2 eigenspace
decomposition. Negative-square lifts have paired isotropic ±i eigenspaces
of dimension two, since i^q=i and i^(q+1)=−1. In the first case the GU
centralizer GU2×GU2 has surjective determinant; in the second the centralizer
GL2(q²) has determinant image c/bar c=μ. Thus neither type splits in SU,
and each gives one S-class, invariant under PGU. Call the second class J_minus.

Here is a useful conjugator. For a unitary X with X²=−I and F(X)=−X,
choose d satisfying Norm(d)=1/2 and d⁴=1/4. If 1/2 is a square in Fq,
take d²=1/2 with d∈Fq; otherwise take d²=−1/2 with bar d=−d. Then
B=d(I+X) is unitary and has determinant one: (I+X)* (I+X)=2I and
det(I+X)=4. Also B F(B)^−1=±X. Thus F and FX are S-conjugate projectively,
so the class square contains J_minus. The matrix X from the preceding
paragraph supplies this witness for one symplectic class; PGU conjugation
transfers it to the other, preserving J_minus.

For an orthogonal class, work in its F-fixed quadratic space (W,b). Choose
a nonsquare k∈Fq and trace-zero η with η²=−1/k. Realize W as F_(q²)² with

    b_a(v,w)=Tr_(q²/q)(v1w1+a v2w2).

Varying Norm(a) gives either discriminant: the trace pairing on a single
quadratic extension has determinant of nonsquare class, and multiplication
by a changes the determinant by Norm(a). Thus the four-dimensional trace
form has discriminant Norm(a) up to squares. Multiplication K by √k is
b_a-self-adjoint, K²=kI, and det_Fq K=k². It is a similitude of multiplier k.
Then X=ηK is unitary, det X=1, X²=−I and F(X)=−X. The same conjugator B
shows that the square of either orthogonal S-class contains J_minus.

It also contains the positive-square inner class. Choose a real orthogonal
involution u which is −1 on a nondegenerate plane and +1 on its complement.
It has determinant one, and Fu is positive-square with the same diagonal
outer label as F. The uniqueness of the orthogonal S-class in that label,
proved above, makes Fu S-conjugate to F. Therefore each orthogonal outside
class square contains **both** inner involution classes. No such assertion
is made for the symplectic classes.

## A uniform Sylow witness and all marked unions

Every subgroup of index at most two in a Sylow 2-subgroup P of S meets J_minus.
Choose t of order eight in F_(q²)* and, in hyperbolic paired coordinates, put

    g=diag(t,t^(−q),t^(−1),t^q) ∈ SU4(q).

Then g⁴=−I and g² is not scalar: its first and third entries are opposite.
Its projective image has order four. Conjugate that image into P; its square
belongs to the Frattini subgroup Φ(P), hence to every subgroup of index two,
and lies in J_minus. This proves the assertion without a Sylow census.

Set R=s/o_plus=q²(q²+1). For q≡1 mod4 put e=v₂(q−1)≥2. Standard group
orders give v₂(|S|)=v₂(s)=2e+3. The two symplectic classes alone, selected
as a singleton or both, force |H|=s or s/2. A Sylow subgroup of H has index
at most two in a Sylow subgroup of S, so the uniform witness contradicts
H∩Λ²={1}.

If the orthogonal-plus class occurs with a∈{0,1,2} symplectic classes, then
|H|=s/(R+a). A noninteger value is impossible. Since R≡2 mod8, the three
denominator valuations are respectively 1,0,2; every integral |H| is even.
The selected orthogonal class captures both inner involution classes, so
Cauchy's theorem gives a collision. In the other label there is only the
orthogonal-minus class, forcing |H|=o_minus, again even, and the same argument
applies. This exhausts both semilinear labels and proves the proposed result
when combined with the reviewed inner and diagonal exclusions.

## Fields q congruent to three modulo four

Now let q≡3 mod4 and t=v₂(q+1)≥2. The center of SU4(q) has order four,
and D=PGU/S=μ/μ⁴ is cyclic of order four. Its q-field involution σ inverts
D, so all four semilinear labels δ^aσ are involutory, with diagonal
conjugation changing a by two. Inner and pure diagonal inversion retain
the preceding reviewed exclusions. The field-group quotient has unique
involution σ; no additional field component is omitted.

The preceding antiunitary square-sign, quadratic-form descent,
quaternionic-pair, norm-minus-one descent and Pfaffian arguments apply in
this congruence too. There is one GU orbit of each of orthogonal plus,
orthogonal minus and symplectic types. The first and third have even
semilinear label, the second odd. Their actual GU centralizers are O4+,
O4− and Sp4, respectively. The **projective GU** centralizer permits
xFx^−1=cF for every c∈μ, not only c∈μ4. For each c, F and cF are
GU-conjugate: their lift-square sign agrees; for a positive-square lift,
choose η/bar η=c, so the fixed quadratic form is scaled by Norm(η),
which preserves a four-dimensional discriminant; negative-square lifts
have the unique GU orbit already derived.

For the symplectic type the Pfaffian equation gives det x=c². For the
orthogonal types, determinants give det x=±c². Both signs occur by
multiplying by a reflection in the actual orthogonal centralizer. Since
−1 is square in μ, these determinant images in D are exactly D², of
order two, for every t. Each projective GU centralizer has the same order
as its actual centralizer: the q+1 possible scalars c multiply the order,
and the q+1 norm-one scalar matrices cancel them on projectivizing.
It follows that every geometric PGU orbit consists of two S-classes total,
one in each compatible actual label. Thus each even label has precisely
one symplectic and one orthogonal-plus class, with S-centralizer orders

    s=|Sp4(q)|/2,        o_plus=|SO4+(q)|=q²(q²−1)²,

and each odd label has just one orthogonal-minus class, with centralizer
order o_minus=|SO4−(q)|=q²(q⁴−1). This counts the full scalar centralizer
before intersecting with S; it does not assume a unique scalar lift or
silently reuse the q≡1 class splitting.

Let C2 be the projective S-class of genuine SU involutions with a
nondegenerate two-dimensional negative eigenspace. The determinant image
of their GU2×GU2 centralizer is onto, so C2 is one S-class and is
PGU-invariant. Each orthogonal outside class square contains C2: choose
a real orthogonal involution u negative on a nondegenerate plane. Fu is
positive-square with the same diagonal label as F, hence is S-conjugate
to F by the inventory. For a symplectic class and t≥3, take F=Jσ with
J=diag(J2,J2) and B=diag(−1,1,1,1). Then BJBᵀ=J u for
u=diag(−I2,I2). Since −1 is a fourth power in μ, a scalar multiple of B
belongs to SU and conjugates F to Fu projectively. Transport by PGU
covers the other even label while preserving C2.

For t=2, C2 is the only nonidentity involution S-class. Indeed a lift
u∈SU has square in the center μ4. A square of ±1 can be centrally
rescaled to square one, yielding the genuine 2+2 class unless projectively
trivial. If u² is a central element of order four, its eigenvalues ±a
have order eight, and a^(q+1)=−1 since v₂(q+1)=2. Their eigenspaces are
paired isotropic planes, forcing determinant u=a⁴=−1, contrary to u∈SU.
Thus this last case is impossible. The reviewed general
[automorphism-class-square lemma](marked-involution-vector-obstruction.md#an-involution-in-an-automorphism-class-square)
at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`, using Glauberman
Corollary1 p.404, then puts C2 in every nontrivial outside involution class
square. This invokes its simple-group statement directly, not its separate
odd-central lifting application. For t≥3 additional projective involution
types can occur; they are unnecessary, since C2 alone is captured.

In every case H avoids C2. Its full Sylow preimage in SU4 has order
4|H|₂ and unique involution −I. The finite unique-involution theorem
forces an element of order at least 2|H|₂, while the determinant-one
unitary eigenvalue bound in the reviewed
[odd-unitary diagonal proof](odd-unitary-four-diagonal.md), source
`7e9eb857e2eae81aece06273632e926448c10d28`, bounds all 2-element orders
by 2^(t+1). Hence |H|₂≤2^t.

For an even label, set R=s/o_plus=q²(q²+1)/2≡1 mod4. Both s and o_plus
have 2-part 2^(2t+2). Selecting the symplectic class, orthogonal class, or
both gives |H|=s, o_plus, or s/(1+R), respectively. Every integral choice
has |H|₂≥2^(2t+1), contradicting the bound. The odd label gives
|H|=o_minus with 2-part 2^(t+2), also impossible. Together with the
q≡1 case and the prior inner and diagonal exclusions, this proves the
proposed canonical PSU4(q) exclusion for all odd q. No restriction on
larger canonical overgroups follows from this equality-case theorem.

## Sources, evidence and limits

The finite-field symmetric-form input is Draisma, *Multilinear Algebra and
Applications* (Fall2015), Theorem10.6.118, printed p.75,
[author notes](https://math-unibe.ch/jdraisma/publications/mlappl.pdf), freshly
inspected by the coordinator. Hermitian and alternating bases, finite-field
norm surjectivity and order formulas are the standard form inputs retained
in the pinned unitary source. Descent, scalar signs, projective splittings,
similitude witnesses and every original marked union are calculated here.
This uniform proof introduces no new computation and does not depend on
the finite q=5 character table or Sylow certificate; that separately reviewed
case remains a consistency check with its original source history intact.
The contributor contributor 1 and coordinator developed and checked
the argument. Independent exact-source reviews covering the rational classes, Pfaffian
step and trace-form witness are recorded below. The cases G>S and other dimensions remain outside this proposed theorem.


## Independent exact-source review

GPT-6.1 Terra contributor 2, contributor 3 and contributor 4 independently accepted this deduction at exact source `99d2ea4385dd2ede08f98ca5ab35092acbc0a598`, conditional on its cited canonical, classical automorphism, finite-field form/descent, finite-group and prior-review inputs. Each checked both congruences, norm-minus-one descent, Pfaffian and projective centralizer images, the full c∈μ scalar range in q≡3, rational S-class splitting, every selected union, trace-form witnesses, the uniform order-eight Sylow argument, t=2 unique inner class and general Glauberman application, and the original-H eigenvalue bound. contributor 2 freshly inspected Draisma and Conrad; the other reviewers retained the recorded inspections. Steinberg, the stated standard descent/form inputs and the previously reviewed Glauberman theorem application remain inputs rather than newly certified external proofs. No new computation was used. These are scoped model mathematical reviews, not formal GitHub approvals. The conclusion concerns the entire canonical group G=S only; canonical overgroups G>S, larger dimensions and the full classification remain open.
