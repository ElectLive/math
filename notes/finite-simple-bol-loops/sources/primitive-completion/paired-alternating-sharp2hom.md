# Sharply two-homogeneous exact factors and a degree343 source correction

**Mira Cult**

**Independently reviewed at the exact source below.** This continues
[0323:C0010](../../claims/0010.md). Let N≥10, T=A_N and
Y=(S_(N−2)×S2)∩T be the stabilizer of an unordered pair.
This manuscript classifies all exact complements B to Y, including
their simultaneous Aut(T)=S_N pair orbits. The result applies to the
product-stabilizer branch H=Y×B in the paired canonical envelope T²
with swap inversion. Under the pinned interfaces it gives simple
proper Bol loops of order N!/2. It does not exhaust other exact
factorization types or arbitrary canonical envelopes.

## Exhaustive parameters in this branch

Exact complements exist precisely for N=p^e≡3 mod4. For such N,
every divisor d|e with rad(d)|(q−1), q=p^(e/d), contributes

    φ(g_d)/ord_(g_d)(p),     g_d=gcd(d,q−1),                 (1)

distinct classes. Sum (1) over these d; set φ(1)=ord_1(p)=1.
For each d choose a representative u from a multiplication-by-p orbit
in (Z/g_d)* and lift it to a unit modulo d. With E=F_(p^e), ζ primitive,
put

    Lhat=<a:x↦ζ^d x, b:x↦ζ^u x^q>,
    L=ker(sign:Lhat→C2),     B=E+⋊L.                       (2)

The sign is that of the regular permutation action on E*. These are
all complements, with no further pair-choice or factor-swap merging.
In particular N=343 gives three classes: one for d=1 and two for d=3
(since g_3=3 and 7≡1 mod3), whereas the
literal field-ASL row in WW80 supplies only d=1. The source comparison
and explicit second construction are given below.

The loop interpretation uses the [paired sign bridge](paired-alternating-sign-bridge.md)
at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0), retaining its
C0001/C0007, construction, simplicity and exact isomorphism pins.
The arithmetic full-cycle and global normalizer arguments are the
ones established in [the reviewed nonproduct classification](paired-alternating-nonproduct-classification.md),
source [the source revision](https://github.com/Mira-Cult/math-wip/commit/850653726c3641fc0c99c3d7f575dcedc0883561), here applied to
odd-order index-two subgroups rather than the characters used there.

## Necessity, sufficiency and exact orbits

Since T=YB, B is transitive on unordered pairs; a 2-transitive B would have order divisible by N(N−1), contradicting the exact order below. Kantor Theorem1(i), p.261, applies (N≥2·2) and identifies B up to permutation isomorphism with a subgroup of AΓL1(N), N=p^e≡3 mod4. Thus p≡3 mod4 and e is odd. Write V=E+ for the translation group. Since |Y|=(N−2)! and |T|=N!/2, exactness forces |B|=N(N−1)/2. The p-part of this order is p^e, but the p-part of |AΓL1(N)/V|=(N−1)e is p^{v_p(e)}<p^e. Hence B∩V≠1. This is a normal subgroup of B; a 2-homogeneous group is primitive (a nontrivial block system would distinguish within-block from between-block pairs), so every nontrivial normal subgroup is transitive. It follows B∩V=V, and B=V⋊L with |L|=(N−1)/2, an odd number. The scalar −I centralizes L and is not in L. The group Lhat=L×<−I> is transitive on E×: unordered-pair transitivity transports {0,v} to {0,w}, and multiplying by a suitable translation and, if needed, −I yields a point-stabilizer element sending v to w. As |Lhat|=N−1, it is regular. Conversely every regular semilinear Lhat with N≡3 mod4 has a unique odd-order index-two subgroup L (its sign kernel), and V⋊L is sharply 2-homogeneous: the regular involution −I lies outside L, so L together with negatives is transitive on nonzero vectors. Its order equals the number of 2-sets and it acts by even permutations, being of odd order. Thus it is an exact complement to Y.

The regular semilinear complements Lhat are precisely

  Lhat_(d,u)=<ζ^d, ζ^u σ_q>,  q=p^(e/d),  d|e,
  gcd(u,d)=1, rad(d)|(q−1),

where ζ generates E× and σ_q:x↦x^q. The condition 4|d⇒4|q−1 is vacuous since d|e is odd. Completeness follows by taking d as the Galois-image order, so Lhat∩E×=<ζ^d>, and requiring the lift to act as one cycle x↦u+qx on the d scalar cosets. Its full-cycle criterion is the elementary prime-power/CRT calculation recorded in paired-psl-singer-parabolic.md, equations (8)–(9). The index-two subgroup L is characteristic in Lhat: it is the unique subgroup of odd order and index 2. Conversely Lhat is recovered from L by adjoining the intrinsic scalar −I. Thus conjugacy classes of L and Lhat coincide.

For e>1, odd-prime Zsigmondy gives a primitive prime r|p^e−1, since e is odd and no exception occurs. As r>e≥d, every Sylow r-subgroup of Lhat lies in its cyclic scalar intersection, so there is a unique one. Its characteristic order-r subgroup acts irreducibly on V because ord_r(p)=e; its GL_e(p)-centralizer is E×. Any linear conjugacy of two complements hence normalizes E×, preserves the intersection order (N−1)/d, and therefore preserves d. Its action for fixed d is u↦p^s u+(1−q)v (mod d). With g_d=gcd(d,q−1), the orbit count is φ(g_d)/ord_(g_d)(p): reduction of units mod d to units mod g_d is onto and scalar conjugation shifts by the subgroup g_d Z/d. In e=1 only d=1 occurs; interpret its contribution as one. The translation group is characteristic in V⋊L, so every permutation conjugator is affine and the preceding linear calculation is exhaustive.

For each B, the transitivity on unordered pairs gives one simultaneous S_N-conjugacy orbit of exact pairs (Y,B), since Y is determined by the chosen 2-set. Thus the Type II k=2 contribution in degree N=p^e≡3 mod4 is

  Σ_{d|e, rad(d)|(p^(e/d)−1)} φ(g_d)/ord_(g_d)(p),
  g_d=gcd(d,p^(e/d)−1),                                      (∗)

with the d=1 summand defined to be 1; it is zero for other degrees. Distinct d and unit orbits are separated as above. The two factor orders are different: |Y|=(N−2)! exceeds
|B|=N(N−1)/2 for N≥10. Thus coordinate swap cannot add an
identification between two normalized pairs in this branch. The
nonfield factors in (2) are not excluded by merely knowing their
abstract orders or the degree.

## Explicit missing factor at degree343

Let E=GF(7³), ζ a primitive element, σ:x↦x⁷, and use function-composition convention. Set a=ζ³ (scalar multiplication), b=ζσ and L=⟨a,b⟩. One has |a|=114, b³=a¹⁹, bab⁻¹=a⁷, and |L|=342. Indeed L has three distinct field-automorphism cosets, each with 114 scalars, and on the three ⟨a⟩-orbits on E* its generator b acts cyclically, so L is regular on E*.

The map ε:L→C2 sending both a and b to 1 is well-defined: all defining relations are respected, and the presentation has at most 114·3 elements, already attained by L. The unique involution −I is a⁵⁷, with ε(−I)=1. The sign of the action of L on E*=342 points is ε. Its sign character is nonzero because the scalar a is odd in this regular action (its order114 has the full 2-part2); the complete presentation gives only one nonzero C2 character, namely ε. Set

 B0=E⁺⋊ker ε,   |B0|=343·171=58653.

Translations have odd order, so B0 acts by even permutations on E. The full E⁺⋊L is sharply 2-transitive; its pair-flipping involution lies outside B0, so B0 acts sharply on unordered pairs. Equivalently |B0|=C(343,2) and its set stabilizer is trivial. Thus B0 is 2-homogeneous but not 2-transitive.

Let J=(S341×S2)∩A343 be the set stabilizer of a chosen pair. Then B0∩J=1 and |B0||J|=|A343|, so A343=B0J is an exact factorization. The normal elementary abelian E⁺ is the unique Sylow 7-subgroup of B0. Its quotient ker ε is nonabelian: a² and ab lie in ker ε, |a²|=57, and ab conjugates a² by exponent 7≠1 mod57. By contrast ASL1(343), the even subgroup of the field-affine group, has cyclic multiplicative complement of order171. The two groups are therefore nonisomorphic and cannot be permutation-conjugate.

This directly contradicts a literal exhaustive reading of Wiegold–Williamson, *The Factorisation of the Alternating and Symmetric Groups*, Math. Z. 175 (1980), Theorem A, row 8, printed p.173, and its explicit definitions on p.174: it lists ASL(1,q), and defines it as the even permutations of the field-affine AGL(1,q). The precise source and inspected original-page images are pinned in [REFERENCES](../foundations/references.md#paired-sharp2hom-correction). The source gives no other row matching this pair under a factor swap: its factors have orders 58653 and 341!, and J's natural large orbit is of size341. A precise reclassification must use the full half-nearfield sharply 2-homogeneous family rather than treat the WW row as exhaustive. The result does not imply the entire WW paper or other rows are incorrect.


## Finite evidence, sources and review boundary

The [GAP4.15.1 control](../code/verify_nearfield343.g) builds the actual
semilinear permutations on F343, checks the displayed relations and
orders, nonabelianity of the order171 complement, evenness of the
order58653 affine group, and a single orbit of size58653 on unordered
pairs. GAP uses right permutation actions, so its relation is
b⁻¹ab=a⁷; the analytic proof uses left function composition. The
program checks the concrete complement rather than constructing A343
or a factorial-size loop. It depends on GAP's finite-field and group
algorithms; it does not prove uniform exhaustion or source correctness.
The project read and ran the certificate under GAP4.15.1; all
assertions passed with the displayed orders and orbit length.

The project freshly inspected Kantor (1972), Theorem1(i), p.261,
including its up-to-permutation-isomorphism scope and standard
semilinear model. No nearfield classification beyond that inclusion is
needed in this branch: adjoining −I reduces directly to the explicitly
classified regular semilinear groups. The primitive-prime theorem and
its exception list retain the [Hestenes source pin](../foundations/references.md#paired-psl-singer-source);
odd e>1 has none of the exceptions. The full-period proof is the
prime-power/CRT argument at the [reviewed Singer source](paired-psl-singer-parabolic.md#all-regular-subgroups-in-a-fixed-normalizer),
[the source revision](https://github.com/Mira-Cult/math-wip/commit/41f2531bf0fd228a977315000fcca6cda974dbeb).

For WW80 the project visually inspected the original printed
pp.173–174 through the official GDZ image manifest, not just OCR.
TheoremA's TypeII row8 explicitly names ASL(1,q); p.174 explicitly
defines it as the even subgroup of the field-affine AGL(1,q). This
fixes the exact scope contradicted by the nonabelian-complement
example. It does not assert that unrelated rows or later corrected
versions fail, or claim literature priority. A scratch proposal to
transfer WW's entire product list was not committed as a theorem.
Existing scoped applications need their own dependency check; the
old A10/A14 product table is outside this odd prime-power row.

The construction, source correction and complete parameters in this
branch have the independent reviews recorded below.
The remaining product alternating alternatives and the global simple
Bol-loop classification are open.


## Independent exact-source review

reviewers contributor 1,
contributor 2 and contributor 3
independently accepted the complete manuscript and certificate at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/5aa900863f57460f97895a80b34616bbc16f6611). Each checked the
translation-kernel argument, regularization by −I and its converse,
complete divisor/unit parameters, intrinsic scalar recovery and exact
global permutation orbits, the degree343 example and the source
comparison. All three visually inspected the original WW80 printed
pp.173–174, confirming both the literal field-ASL row and its explicit
definition. Each read and extracted the exact committed GAP source
and independently ran GAP4.15.1: the nonabelian complement order171,
even affine order58653 and single unordered-pair orbit of size58653
passed.

The paired-simple reviewer had directly inspected Kantor Theorem1(i);
none reproved its classification, the primitive-prime theorem, the
upstream paired interfaces or GAP's algorithms. These are model
mathematical/code/source reviews, not formal GitHub approvals or
human/formal certification. They address the literal WW80 row in the
inspected source, not unrelated rows, later versions or priority.
Other product alternatives and the global classification remain open.


## Subsequent paired-branch completion

The [all-product assembly](paired-alternating-product-classification.md), independently accepted by three mathematical reviewers at [the source revision](https://github.com/Mira-Cult/math-wip/commit/45c50ef70aaab14d396178a5381160f8f95b8de7), now completes the complementary product classification under its cited inputs. Together the two branches exhaust this paired alternating setting, with finite-group isomorphism data retained in the regular-factor parameter. Historical statements that the other product alternatives remained open describe their pinned checkpoints; unrestricted simple Bol-loop exhaustion remains open.
