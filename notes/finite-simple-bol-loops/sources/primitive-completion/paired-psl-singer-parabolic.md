# Paired PSL folders with parabolic and Singer-normalizer projections

**Mira Cult**

**The structural reduction and complete parameter classification are
independently reviewed at their respective sources below**, continuing
[0323:C0010](../../claims/0010.md). Let T=PSL_n(q), with n≥4 and q any prime
power. Let P be a projective point or hyperplane stabilizer, let S be a full
projective Singer group in PGL_n(q), and put T0=S∩T and N=N_T(T0).
Suppose a simple nonassociative paired canonical Bol folder has group T×T,
factor-swapping inversion, and actual stabilizer projections Y0≤P and Y1≤N.
Then

    Y0=P,    H=P×Y1,    Y1 acts regularly on the projective points

(or hyperplanes in the dual case). Conversely each regular Y1≤N gives such
a folder with H=P×Y1. In particular the two full projections P and N never
give a folder for n≥4. The appended continuation evaluates the surviving
Y1-orbits, with its separate review status.

There is no assumption that the projections are maximal or that Y0 contains
the derived subgroup of P; these properties are consequences where used.
This is one actual-factor branch, not an assertion that all PSL factorizations
are of this type. No ambivalence is assumed. The proof depends on the
[paired-folder interface](../factor-permutation/radical-free-paired-simple-envelopes.md), reviewed at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff), and its intersection criterion at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/e898d8a00b1fc97431ad8092b4e51b9217650187), retaining the stated C0001,
scoped C0007 and CFSG/FGS dependencies. The only additional classification
input is the usual simplicity of PSL_m(q), m≥3; the Singer normalizer facts
are sourced and also explained below.

## Parabolic and normalizer data

It suffices initially to use a point stabilizer. Put

    d=gcd(n,q−1),    D=(q^n−1)/(q−1),    m=n−1.

The preimage of P in SL_n(q) is U⋊GL_m(q), where U is the additive
unipotent radical and the Levi embedding sends A to diag(det(A)⁻¹,A).
Elementary-matrix commutators give GL_m(q)′=SL_m(q), perfection of SL_m(q),
and [U,SL_m(q)]=U for m≥3. Thus U⋊SL_m(q) is perfect. The scalar center
of SL_n(q) has order d; its image under the Levi determinant has order d.
Consequently

    P/P′ ≅ C_((q−1)/d),     P′ is perfect.                 (1)

The subgroup SL_m(q) embeds in P by diag(1,A): its intersection with the
scalar center is trivial. The same is true of U⋊SL_m(q).

Identify the natural vector space with E=F_(q^n). The Singer group S is
the image of multiplication by E*, modulo F_q*. Its intersection T0 with
PSL has order D/d. Its normalizer is the intersection with T of the
projectivized semilinear group E*⋊Gal(E/F_q). These normalizer identities
and orders are Hestenes, Theorems 2.7–2.8 and the preceding paragraph,
printed p.497; the exact source is in
[REFERENCES](../foundations/references.md#paired-psl-singer-source).

Here is a direct justification of the potentially delicate projective
normalizer step. Choose a linear lift t∈E* of a generator of T0. Its order
is at least D/d≥D/(q−1)>q^(n−2)≥q^(n/2), whereas a proper subfield of E
has multiplicative-group order at most q^(n/2)−1. Hence F_q[t]=E.
A linear lift g of a projective normalizer satisfies
gtg⁻¹=λt^r for λ∈F_q* and some r, so it normalizes this field algebra.
It is therefore semilinear over E. Conversely those semilinear maps that
belong to PSL normalize T0. Every Frobenius power can be multiplied by an
element of prescribed norm to make its determinant one. It follows that

    T0 ◁ N,    N/T0 ≅ C_n,    |N|=nD/d.                 (2)

In particular N and its subgroups are solvable.

## The actual parabolic projection must be full

The paired interface supplies T=Y0Y1. Thus T=PY1 and Y1 is transitive
on the D projective points. Since |Y1| divides |N|, orbit–stabilizer gives

    |P∩Y1|=|Y1|/D divides n/d.                           (3)

Also P=Y0(P∩Y1), so k=[P:Y0] divides |P∩Y1| and k≤n. Consider the
coset action P→S_k. Every nontrivial image of the embedded SL_m(q) has
order at least |PSL_m(q)|: perfection and simplicity modulo the center
imply that each proper normal subgroup of SL_m(q) is central. But

    |PSL_m(q)| ≥ |SL_m(2)| > (m+1)! = n! ≥ k!.

For completeness, the first inequality follows from
|PSL_m(q)|=q^(m(m−1)/2)∏_(i=2)^m(q^i−1)/gcd(m,q−1), bounding its
denominator by q−1 and using (q²−1)/(q−1)=q+1≥3. The second starts at
|SL_3(2)|=168>4! and follows inductively from the ratio
|SL_m(2)|/|SL_(m−1)(2)|=2^(m−1)(2^m−1)>m+1.

Thus the coset action kills SL_m(q). It also kills U=[U,SL_m(q)], and
therefore P′≤Core_P(Y0)≤Y0. Equation (1) now shows that k also divides
(q−1)/d. Since

    gcd(n/d,(q−1)/d)=1,

we obtain k=1 and Y0=P. This gcd identity follows directly from the
definition of d; it does not require a separate restriction on q or n.

## Trivial coupling and the converse

Write α:P→C and β:Y1→C for the common Goursat quotient of H. The paired
interface gives |C|=|P∩Y1|, so (3) bounds its order by a divisor of n/d.
Since Y1 is solvable, C is solvable. The image of the perfect subgroup
P′ in C is trivial. Hence C is a quotient of P/P′ and its order divides
(q−1)/d. Coprimality forces C=1. We have H=P×Y1 and P∩Y1=1, so Y1
is regular on the projective points and |Y1|=D.

Conversely a regular subgroup Y1≤N has P∩Y1=1 and T=PY1. These are
nontrivial proper factors, giving a paired folder by the reviewed exact-
factorization case of the intersection criterion. The paired theorem supplies
faithfulness, simplicity, properness and non-Bruckness. Its usual simultaneous
Aut(T)/swap relation gives the exact isomorphism test for these data; no new
identification or enumeration of regular subgroups is claimed.

## Why the full normalizer cannot occur

The T0-orbits on projective points are the d classes of the norm label in
F_q*/(F_q*)^n. Indeed changing a vector by a scalar changes its norm by an
nth power, and the kernel of this label on E*/F_q* is exactly T0.
A semilinear map x↦a x^(q^j) representing an element of N may be chosen
with determinant one. Therefore Norm(a)=det(Frob_q^j)⁻¹∈{1,−1}, since
Frobenius permutes a normal basis. Frobenius itself preserves the norm
label. The action of N on the labels consequently has image contained in
the subgroup generated by the class of −1.

Transitivity, already forced by T=PY1, implies d=1 or d=2 with q≡3 mod4.
In either case n/d>1 for n≥4. By (2), |P∩N|=n/d, so N is not regular
and cannot equal Y1 in a folder. This transitivity restriction is used for
this last exclusion only. The graph automorphism interchanges point and
hyperplane stabilizers and sends a Singer torus to a conjugate Singer torus,
giving the dual statement.

## Evidence and review boundary

The project inspected Hestenes's exact published normalizer statements.
The proof above uses direct parabolic, field, order and coset-action arguments;
no finite experiment is used to prove the uniform bound. Standard finite-field
facts, elementary-matrix identities and the stated PSL simplicity input remain
dependencies. Independent review of this exact source is recorded below. The unexplored regular-subgroup parameters and other
factorization types remain open, as do other canonical envelopes.


## Independent exact-source review

reviewers contributor 1,
contributor 2 and contributor 3
independently accepted the full manuscript at exact source
[the source revision](https://github.com/Mira-Cult/math-wip/commit/9f69b6875f084e385e0af798c503322e610b6e03). They checked the projective
field-algebra normalizer argument, the small-index coset action including
(n,q)=(4,2), the two coprime divisibilities, the regular-subgroup converse,
the full-normalizer obstruction and hyperplane duality. All three inspected
the cited Hestenes normalizer statements on printed p.497, the folder-criterion
reviewer during the preceding source audit. No finite computation was used.

The acceptances retain the standard finite-field and PSL simplicity inputs
and the pinned paired-folder/FGS interfaces; these upstream results were not
independently reproved. They do not enumerate the regular subgroups or classify
other factorizations or envelopes. These are model mathematical reviews, not
human/formal certification or formal GitHub approval.

## Complete parameters and counts in this branch

**Independently reviewed at the exact source recorded below.** Fix n≥4 and q=p^f,
and retain d,D as above. The point/hyperplane parabolic–Singer-normalizer
branch is nonempty exactly when

    d=1, or d=2 with n≡2 mod4 and q≡3 mod4.                (4)

When (4) holds, form the finite set of integers k satisfying

    k divides gcd(n,D),   d divides k,   j=n/k,
    every prime divisor of k divides q^j−1,
    if 4 divides k then 4 divides q^j−1.                   (5)

For each such k put g_k=gcd(k,q^j−1). The loop-isomorphism classes are
indexed by k and the orbits of multiplication by p on (Z/g_k)*. Thus their
number is

    Σ_(k satisfying (5)) φ(g_k)/ord_(g_k)(p),              (6)

where φ(1)=ord_1(p)=1 and (Z/1)* has one element. If (4) fails the count
is zero. This includes (n,q)=(6,2), whose exceptional proof is given below;
the formula itself needs no correction there. Counts are for fixed T and
the stated projection branch, not all canonical T² folders or all simple
Bol loops of order |T|. Low-rank identifications such as PSL4(2)≅A8 must
still be respected when combining branches.

Here are explicit representatives. Fix a primitive ζ∈F_(q^n)*, let z be
projective multiplication by ζ, and let σ:x↦x^q. Choose a unit residue u
modulo k mapping to a representative of the selected unit orbit modulo
g_k. Then

    Y(k,u)=⟨z^k,z^uσ^j⟩,    H=P×Y(k,u).                 (7)

Use the full anti-diagonal section in T². The theorem below proves that
all such groups lie in T and are regular on the points, that the data
exhaust the branch, and that precisely the equivalences in (6) identify
loops. The earlier reduction at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9f69b6875f084e385e0af798c503322e610b6e03)
supplies the canonical construction and exhaustive passage to regular Y.

### All regular subgroups in a fixed normalizer

The full projective Singer group is ⟨z⟩ of order D, with T0=⟨z^d⟩.
For regular Y≤N its order is D. If its image in N/T0 has order k, then
k divides n, Y∩T0=⟨z^k⟩, k divides D and d divides k. Choose a lift of
σ^j with j=n/k. It has the form h=z^uσ^j, with u uniquely determined
modulo k, and Y=⟨z^k,h⟩. Conversely such generators have order D once
h^k∈⟨z^k⟩.

The projective torus ⟨z^k⟩ has k orbits on the points, labeled by the
exponent modulo k in F_(q^n)*/F_q*. The generator h acts on these labels by

    x ↦ u+q^j x  (mod k).                                 (8)

This affine permutation is a single k-cycle exactly when

    gcd(u,k)=1,    rad(k) divides q^j−1,
    4|k implies q^j≡1 mod4.                               (9)

We give the elementary full-period proof. Write a=q^j. Necessity modulo
each prime ℓ|k follows because an affine map with a≠1 modulo ℓ has a
fixed point; when a=1 the translation must be nonzero. If 4|k and a≡3
mod4, its second iterate returns 0 modulo4, excluding a full cycle.
For sufficiency use prime powers and the Chinese remainder theorem.
The t-th iterate of 0 is u(1+a+⋯+a^(t−1)). For an odd prime ℓ dividing
a−1, the valuation of this sum is v_ℓ(t); the same holds for ℓ=2 when
a≡1 mod4. Indeed write t=ℓ^v s, ℓ∤s: the initial s-term sum is a unit,
and successive ℓ-term geometric factors each have valuation one by the
binomial expansion. For a single factor 2 the nonzero translation check
already suffices. Thus the period modulo ℓ^e is ℓ^e, and their least
common multiple is k. This proves (9), including k=1.

A full cycle in (8) forces k|u(1+q^j+⋯+q^((k−1)j)), so h^k∈⟨z^k⟩
automatically. The generated group has order D and is transitive on D
points, hence regular. Conversely a regular Y necessarily gives the full
cycle and (9).

It remains to impose membership in PSL. Write ε_j=0 for even q, and
ε_j=((q−1)/2)(n−j mod2) for odd q. The determinant of σ^j is
(−1)^(n−j), by a normal basis. The norm of ζ generates F_q*, so the
projective determinant condition is

    u+ε_j≡0 mod d.                                       (10)

The norm-label argument already proved that transitivity requires d=1
or d=2,q≡3 mod4. In the latter case u is odd, so (10) requires j odd.
Then k contains the entire 2-part of n. Condition (9) excludes 4|k
because q^j≡3 mod4, proving n≡2 mod4. Conversely if d=1, condition (10)
is automatic; if the second alternative of (4) holds, every k in (5)
is even with j odd, and every unit u satisfies (10). This proves the
parameter list. It is nonempty whenever (4) holds: use k=1 in the first
case and k=2 in the second.

### Recovering the Singer torus and the global isomorphism relation

Classification inside a fixed normalizer alone would not suffice: a regular
subgroup could a priori lie in two different Singer normalizers. Except at
(n,q)=(6,2), the primitive-prime input cited below supplies r with
ord_r(q)=n, and hence r>n and r∤q−1. Since r∤k, the Sylow r-subgroup of
Y lies in its normal cyclic subgroup Y∩T0; it is unique and characteristic.
Its unique subgroup R of order r is therefore characteristic too.

For 1≠x∈R choose a linear lift of order r; this is possible since
r∤q−1. Its degree over F_q is n, so its linear centralizer is the
multiplication group F_(q^n)*. If a projective linear map centralizes x,
its linear lift conjugates x to λx with λ∈F_q*. Taking r-th powers forces
λ^r=1 and then λ=1. Consequently C_(PGL_n(q))(R)=⟨z⟩. Intersecting
with T recovers T0 intrinsically from Y. Any PΓL conjugacy between two
displayed Y's must therefore normalize T0.

The full normalizer of T0 in PΓL_n(q) is generated by z and the
p-Frobenius ρ:x↦x^p. The same field-algebra argument used for (2), now
allowing base-field automorphisms, gives this assertion. In particular k
is invariant, and its action on the residue u is

    u ↦ p^s u+(1−q^j)v  (mod k),    s,v integers.          (11)

Conjugating the two generators proves the formula directly. Translations
in (11) identify exactly the fibers modulo g_k=gcd(k,q^j−1). Every prime
of k divides g_k by (5), so u is a unit modulo k exactly when its reduction
is a unit modulo g_k; every such unit lifts. The remaining action is
multiplication by p. It is free on the units in the sense that every orbit
has length ord_(g_k)(p): p^s u=u implies p^s=1 modulo g_k. Since
g_k divides D, p is invertible and this order divides fn. This proves the
count in (6) for the regular-subgroup PΓL-orbits.

The exceptional case (n,q)=(6,2) has D=63 and k=1 or3. At k=1 the
subgroup is cyclic C63. At k=3 the residues u=1,2 are exchanged by ρ;
the representative h=zσ² has h³=z²¹ and order9. Together with z⁹ it
generates a nonabelian C7⋊C9, with h acting on C7 by exponent4. Thus the
two k cases cannot be conjugate, and each gives one class. These are also
the two contributions of (6), handling the only absent primitive prime.

Finally the standard automorphism theorem gives Aut(PSL_n(q)) generated
by PΓL and the inverse-transpose graph automorphism. The latter exchanges
point and hyperplane parabolics, so all data can first be represented in
the point branch. Between two point-branch pairs, an automorphism preserving
the parabolic type lies in PΓL; point and hyperplane stabilizers are not
conjugate by a semilinear map for n≥4. Once Y is fixed, its regular action
on the points aligns any two point stabilizers by conjugation. Also
|P|≥168q^(n−1)>D=|Y|, so ordering the larger projection first resolves
the paired coordinate swap and introduces no additional identification.
The paired isomorphism theorem therefore turns exactly the subgroup orbits
above into loop-isomorphism classes. This use of the automorphism theorem
includes PSL4(2)≅A8; its graph automorphism is not omitted.

### Sources and finite controls

The additional external inputs are the primitive-prime statement quoted in
the proof of Hestenes Theorem2.12, printed p.499, and the classical
automorphism theorem in Kleidman–Liebeck, Theorem2.1.4 with Table2.1.B,
printed pp.15–16. The project inspected these exact statements; details
and limits are in [REFERENCES](../foundations/references.md#paired-psl-singer-source).
Apply the quoted primitive-prime theorem to p^(fn)−1. Since fn≥4, its
only possible exception is p=2,fn=6, and with n≥4 this means n=6,q=2.
It gives ord_r(p)=fn and therefore ord_r(q)=n as used above. No assertion
that all regular projective subgroups are cyclic is imported from the
closing discussion of Hestenes §2.

The noncyclic possibilities are essential. Besides C7⋊C9 at (6,2), for
n≡2 mod4, n≥6, q≡3 mod4 and d=2, the k=2,u=1 group is
⟨z²,zσ^(n/2)⟩. It is regular by the preceding proof and nonabelian,
since conjugation acts on ⟨z²⟩ by q^(n/2), with
0<q^(n/2)−1<D/2. This gives an infinite family, including q=3 and
n=6,10,14,… . At n=6,q=3 it has order364 and (zσ³)²=z²⁸.

The project read and ran [verify_paired_psl_singer_examples.g](../code/verify_paired_psl_singer_examples.g)
under GAP4.15.1. It independently enumerates regular subgroups in the
actual permutation normalizers on projective exponent labels for four
controls, and fuses them in the full normalizer. The counts are1,2,1,0
for (n,q)=(4,2),(6,2),(6,3),(4,3), respectively. It checks normalizer
orders and the relevant determinants using actual finite-field matrices.
These controls corroborate the cyclic, noncyclic, exceptional and empty
cases; they do not prove the uniform arithmetic or global-orbit argument.
No network or output files are used. The source statements, GAP algorithms
and pinned analytic interfaces remain explicit dependencies. Independent
exact-source review of this complete parameter/count continuation follows.


### Independent review of the complete parameter classification

reviewers contributor 1,
contributor 2 and contributor 3
independently accepted the complete appended parameter/count theorem and
finite-control code at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/41f2531bf0fd228a977315000fcca6cda974dbeb).
They checked construction and exhaustion, the full-period criterion and
determinant/existence condition, recovery of the torus from a characteristic
primitive-prime subgroup, the global semilinear/graph/swap isomorphism relation,
the unit-orbit count and the exceptional (6,2) argument. All three read,
extracted and reran the exact committed GAP4.15.1 verifier; all four controls
and determinant/order checks passed.

The paired-simple and strip-forest reviewers independently inspected Hestenes
p.499 and the Kleidman–Liebeck §2.1 definitions, Table2.1.B and Theorem2.1.4.
The folder-criterion reviewer had inspected the earlier Hestenes normalizer
statements but did not freshly audit these two additional source inputs.
None reproved the primitive-prime theorem, classical automorphism theorem,
GAP algorithms or upstream paired-folder results. These are model proof/code
reviews of construction, exhaustion and exact isomorphism data in this
specified projection branch, not human/formal certification, formal GitHub
approval or a classification of other PSL factorizations or global envelopes.
