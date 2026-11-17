# All nonproduct paired alternating folders

**Mira Cult**

**Independently reviewed at the exact source recorded below.** This continues
[0323:C0010](../../claims/0010.md) in the precise canonical branch
G=A_n×A_n, n≥5, with inversion swapping the factors and full canonical
anti-diagonal section. Conditional on the pinned paired interfaces and
external classifications below, this manuscript constructs and exhausts
the nonproduct stabilizers and evaluates their loop-isomorphism classes.
Every resulting loop is simple and nonassociative of order n!/2, and all
its isotopes are isomorphic. Product stabilizers and other canonical
groups are outside this theorem.

## Statement and parameters

For n=5,6,7,8 the nonproduct count is zero, and for n=9 it is one.
For n≥10 the following disjoint families are exhaustive.

* If n=p^e is an odd prime power, define D(p,e) to consist of d|e with
  d≡2 mod4, q=p^(e/d)≡3 mod4, and rad(d)|(q−1). Put g_d=gcd(d,q−1).
  The number of nonproduct classes is

      2 Σ_(d∈D(p,e)) φ(g_d)/ord_(g_d)(p) + 1_(n=49) + 1_(n=529).  (A)

  An empty sum is zero. For each d, choose a representative u of a
  multiplication-by-p orbit in (Z/g_d)*, lifted to a unit modulo d.
  On E=F_(p^e), with ζ primitive, put

      a:x↦ζ^d x,  b:x↦ζ^u x^q,  L=<a,b>,  B=E+⋊L.

  Each such B gives two classes, represented by characters
  (ε(a),ε(b))=(0,1) and (1,0), extended trivially across E+.
  The additional classes at 49 and 529 use the exceptional complements
  2^-S4 and 2^-S4×C11, with their unique nonzero C2 character.
  Let Y=(S_(n−2)×S2)∩A_n preserve a chosen unordered pair, and ν be
  its pair-sign character. The stabilizer is

      H={(y,b)∈Y×B: ν(y)=ε(b)}.                              (B)

* If n=r²+1 with r an odd prime power congruent to 3 modulo4,
  there is exactly one class. Its projections are the even-embedded
  S_(n−3) fixing a point and a disjoint two-set, and the standard
  sharply 3-transitive group M(r²). Couple their unique C2 characters.

* In all other degrees the count is zero.

Odd prime-power degrees and degrees r²+1 are disjoint. The first formula
at n=7^6 has d=2,q=343 contributing two and d=6,q=7 contributing four,
so gives six classes in total. This strengthens the independently
reviewed [four-class lower bound](paired-alternating-dickson-multiplicity.md)
without changing its proof or historical review pins. No assertion about
literature priority or later corrected versions of GG24 is made.

## Exhaustive structural interface

Use the [all-degree sign bridge](paired-alternating-sign-bridge.md),
source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c5153a7ccd4a0de8e8f700341a78ac06f3b1caf0), with its explicit
C0001/C0007 and paired-folder dependencies. In particular every
nonproduct H has common Goursat quotient C2, both coordinate projections
are proper, admissibility is the intersection-bijection test, and the
isomorphism relation is simultaneous Aut(A_n) and optional swap.
The analytic source retains the paired construction at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff) and regular-subgroup/isotope
interface at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e898d8a00b1fc97431ad8092b4e51b9217650187).

For n≥10 the cited actual-factor theorem gives the intransitive/
k-homogeneous alternatives, k=1,…,5, and the degree-ten exception.
The proof in that source already excludes a common C2 quotient for
k=1,4,5 and for the degree-ten exception: the relevant simple factor has
no such quotient, or the only proper quotient on one side is C5 or C3.
Thus only k=2 and k=3 remain. The following arguments handle all actual
projections and their simultaneous embedding orbits, not only maximal
overgroups. At n≤9 use the separately reviewed small-degree results
and the exact evaluation at [the source revision](https://github.com/Mira-Cult/math-wip/commit/f15f63f39bfe8bb913573a4bdc2369178d483963).
In particular n=9 is handled by that evaluation, rather than an
unproved general normalizer formula at its quaternion exception.

## The two-homogeneous branch

Let T=A_N, N≥10, in the k=2 actual-factor alternative. The
intransitive projection must be Y=(S_(N−2)×S2)∩A_N, with unique
index-two kernel Y0=A_(N−2), and the other projection B is
2-homogeneous. The order equation |H|=|Y0||B|=|T| gives
|B|=N(N−1). A finite faithful 2-homogeneous permutation group of even
order is 2-transitive: an involution interchanges some pair; conjugating
by 2-homogeneity supplies a flip on any pair, which upgrades unordered-
pair transitivity to ordered-pair transitivity. Thus B is sharply
2-transitive. Its intersection with Y consists of the identity and the
unique pair-flipping involution r. The character ν:Y→C2 is nonzero on r,
so admissibility forces the character ε:B→C2 to kill r. In particular
Y0 B is exact. This argument uses no classification of index-two
extensions or Rota–Baxter maps.

Conversely, take B≤A_N sharply 2-transitive and a surjection ε:B→C2 killing the unique element r∈B which interchanges two fixed points. Y∩B=<r>, A_N=Y0 B is exact, and the fiber product H={(y,b)∈Y×B:ν(y)=ε(b)}, ν:Y→Y/Y0, is a nonproduct C2 folder by the reviewed sign-bridge theorem. A permutation of the N letters simultaneously conjugating B and ε gives an isomorphic folder; the unequal projection orders prevent an extra identification by swapping coordinates. After a conjugacy of (B,ε), an element of the target B aligns the chosen pair, by sharp two-transitivity; inner conjugacy preserves ε. Thus it suffices to classify such (B,ε) under S_N conjugacy, with no additional orbit of pairs.

Grundhöfer–Hering Theorem2.4 and Corollary3.1 give B=V⋊L with V elementary abelian regular and L regular on V−{0}; the seven exceptional complements are treated at the end. In the nonexceptional case, write |V|=N=p^e, E=F_(p^e), and L≤ΓL1(E). If p=2, every homomorphism B→C2 kills V: its restriction is a complement-invariant linear functional and L is transitive on V−{0}. It also kills L, whose order N−1 is odd. Hence p is odd. All involutions in B are conjugate; the unique involution in L is −I. Every ε kills V and corresponds to a character of L, with ε(r)=0 equivalent to ε(−I)=0.

Let d be the order of the image of L in Gal(E/Fp), q=p^(e/d), choose ζ primitive in E, and σ(x)=x^q. Then d|e and d|(N−1); the scalar intersection is A=L∩E×=<a>, a=ζ^d, and choosing a lift of σ gives b=ζ^uσ and L=<a,b>, where u is determined mod d. On the d A-orbits in E×, b acts by i↦u+qi. This is a d-cycle exactly when

 gcd(u,d)=1, rad(d)|(q−1), and 4|d ⇒ 4|(q−1).   (1)

Necessity is immediate modulo each prime divisor and modulo 4; sufficiency follows from the valuation of 1+q+⋯+q^(t−1) at each prime divisor and the Chinese remainder theorem. The d-cycle condition gives d|(1+q+⋯+q^(d−1)), since u is a unit modulo d. Thus d|(N−1), t below is an integer, and b^d∈A. The generated L has order N−1 and is transitive on E×, hence regular. This also proves sufficiency starting from the parameters (1), without separately assuming d|(N−1). This proves completeness of the parameterization directly from semilinearity. With left composition,

 a^M=1, b^d=a^(ut), b a b⁻¹=a^q, M=(q^d−1)/d, t=M/(q−1).   (2)

The representation gives all these relations as a complete presentation: their normal form has at most Md=N−1 elements, the actual group has that order, and the relations hold.

For ε(a)=x, ε(b)=y in F2, the relations are Mx=0 and dy=utx. Suppose q is odd. If d is odd, LTE gives v2(M)=v2(N−1), so a has the full 2-part of |L| and is odd in its regular action on E×; hence B is not contained in A_N. If d is even and q≡1 mod4, LTE gives v2(M)=v2(q−1), t odd, and u odd. Equation (2) then shows b has the full 2-part of |L|, so b is odd. Thus admissible B requires q≡3 mod4 and d≡2 mod4. Conversely these two congruences, with (1), give 4|M and 2|t by LTE. Both x and y are free; all three nonzero characters kill the unique involution a^(M/2). Their independence shows the Sylow 2-subgroup P of L is noncyclic: restriction Hom(L,C2)→Hom(P,C2) is injective, since a nonzero character has an index-two kernel that cannot contain P. For a finite group acting regularly on itself, an element is odd exactly when its order contains the full 2-part of the group order; a noncyclic Sylow 2-subgroup precludes such an element. Thus L acts evenly on E×, and the odd-order translation group acts evenly, proving B≤A_N.

Count these characters and complements under S_N. Every conjugator of two B groups preserves their characteristic translation subgroups (the unique Sylow p-subgroups) and is affine; after aligning point stabilizers it is Fp-linear. For e>2, Zsigmondy's theorem gives a primitive prime r dividing p^e−1; it exceeds e≥d, so all Sylow r-subgroups lie in cyclic A, hence there is a unique one. Its characteristic order-r subgroup is irreducible on V because ord_r(p)=e, and its GL_e(p)-centralizer is S=E×. Consequently every linear conjugator preserves S and A=L∩S. Distinct d are distinguished by |A|=(N−1)/d. A linear normalizer of S is S⋊Gal(E/Fp); it changes the lift parameter by

 u ↦ p^s u+(1−q)v (mod d).                                      (3)

Put g=gcd(d,q−1). The scalar shifts in (3) are exactly the multiples of g modulo d, so their orbits are the fibers of reduction modulo g. Under (1), d and g have the same prime divisors, so these shifts preserve unit residues; reduction of units modulo d onto units modulo g is surjective. Multiplication by p has orbit length ord_g(p) on every unit. The number of complement orbits for this d is φ(g)/ord_g(p). The scalar ζ^{d/g} normalizes L and sends b to a^(±(q−1)/g)b; this exponent is odd in the admissible case. Hence it exchanges the two characters with x=1, while intrinsic A separates them from the sole nonzero character with x=0. There are exactly two character orbits for each complement.

For e=2 the only admissible d is 2 and g=2, so there is only one complement parameter orbit. If a primitive prime is unavailable then p is a Mersenne prime. For p>3, every element outside A has square in Fp× and order dividing 2(p−1), whereas |a|=(p²−1)/2>2(p−1); hence A is characteristic in L, giving the same two character orbits. The boundary p=3 gives N=9 and Q8; it is excluded from the present N≥10 scope and is handled by the existing reviewed finite small-degree control.

Therefore the Dickson contribution in degree N=p^e≥10 is exactly

  2 Σ_{d|e, d≡2 (mod 4), p^(e/d)≡3 (mod 4), rad(d)|(p^(e/d)−1)}
      φ(g_d)/ord_(g_d)(p),   g_d=gcd(d,p^(e/d)−1).             (4)

Grundhöfer–Hering Theorem 2.4 also lists the seven exceptional multiplicative complements: SL2(3), 2−S4, SL2(3)×C5, SL2(5), 2−S4×C11, SL2(5)×C7, SL2(5)×C29, in degrees 5²,7²,11²,11²,23²,29²,59² respectively, one nearfield type each. Only the two 2−S4 cases have a nontrivial C2 character. Their unique involution lies in the derived subgroup, by Lemma2.3 and its following paragraph, so the character kills it. Their Sylow 2-subgroups map onto a Sylow D8 of S4 and therefore are noncyclic; their sharply 2-transitive actions are even by the regular-sign criterion above. Each yields one character class in degrees 49 and 529. The source gives one nearfield type in each exceptional row and Corollary3.1 gives the permutation-isomorphism scope. An isomorphism of nearfields is additive, hence Fp-linear, and intertwines left multiplication, so it conjugates their linear complements. Its unique C2 character requires no further character-orbit computation. The exceptional cases are disjoint from the Dickson cases by that classification. The five remaining exceptional rows have no nonzero C2 character: SL2(3) has abelianization C3, SL2(5) is perfect, and the added cyclic factors have odd order.


## The three-homogeneous branch

Put m=n−3≥7. By the paired normal form the common quotient is C2. In Chen et al.'s k=3 case one projection A satisfies A_m≤A≤(S_m×S3)∩A_n, and the other B is 3-homogeneous. The quotient of that overgroup by A_m is S3; its four inverse images are A_m, A_m×C3, even-embedded S_m, and the full overgroup. Only the last two admit a C2 quotient. Their unique index-two kernels are respectively A_m and A_m×C3. Put F=n(n−1)(n−2). From |H|=|ker(A→C2)|·|B|=|T|, the two cases force |B|=F and |B|=F/3 respectively.

The full-overgroup case is impossible. A 3-transitive B has order divisible by F. Otherwise Kantor's theorem applies, since n≥10≥2·3. In its projective case B contains PSL2(q), with n=q+1 and q≡3 mod4; that simple subgroup has order F/2>F/3. The affine cases of degree eight are too small, and AΓL1(32) has order F/6, not F/3.

For A=S_m, |B|=F. If B is not 3-transitive, Kantor's projective case would have PSL2(q)◁B of index two, q≡3 mod4. The field-extension degree of q is odd, so the order-two image of B in PΓL2(q)/PSL2(q) has trivial field component. It is the diagonal outer subgroup, making B=PGL2(q), which is 3-transitive: contradiction. The only other degree≥10 Kantor case AΓL1(32) has order F/6. Thus B is sharply 3-transitive.

The cited Zassenhaus restatement gives PGL2(q) in degree q+1, or M(r²) in degree r²+1 for r odd. If q is even, PGL2(q)=PSL2(q) is simple in this range and has no C2 quotient. If q is odd, multiplication by a primitive scalar is an odd permutation on the projective line, so PGL2(q) is not contained in A_n. Therefore B is the standard twisted M(r²), whose unique C2 quotient has kernel PSL2(r²).

Let σ:x↦x^r on P¹(F_{r²}), and let δ be a diagonal projectivity with nonsquare determinant. The simple subgroup PSL2(r²) consists of even permutations. The field involution fixes r+1 projective points, so its sign is (−1)^((r−1)/2), while δ is odd. Hence M(r²)=PSL2(r²)<δσ> lies in A_n exactly when r≡3 mod4.

Every involution of M(r²) lies in PSL2(r²). Otherwise it has semilinear representative Aσ with det A nonsquare and Aσ(A)=λI. Applying σ and conjugating by A yields λ∈F_r*. Taking determinants gives Norm(det A)=λ², impossible because the norm of a nonsquare in F_{r²} is a nonsquare in F_r. Thus the unique quotient B→C2 kills every involution.

For the converse take r≡3 mod4 and the standard sharply 3-transitive B=M(r²)≤A_n. Let A be the even-embedded S_m fixing one of three designated points and preserving the other two as a set. Sharp 3-transitivity gives |A∩B|=2: the identity and the unique element fixing the first designated point and swapping the other two. Its nontrivial element r0 lies in PSL2(r²) by the preceding paragraph, but lies outside A_m because its action on the distinguished two-set is odd and its total permutation is even. Thus the two quotient maps A→C2 and B→C2 differ on r0. Their fibre product satisfies the reviewed paired index-two admissibility criterion and produces the claimed folder.

The sharply 3-transitive classification is a classification of permutation groups in the stated standard actions, so it gives one S_n-conjugacy class of B for each r. After fixing B, its sharp action on ordered triples is transitive, and therefore all choices of the distinguished point and two-set yield conjugate A. Both C2 maps are unique and their intersection condition above fixes their relative identification. Simultaneous Aut(A_n)=S_n and optional coordinate swap consequently give exactly one class. No GG24 Rota–Baxter orbit count is used.

## Sources, evidence and review boundary

The [alternating source record](../foundations/references.md#paired-alternating-sign-sources)
pins Chen et al., arXiv:2111.06579v2, Theorem2.6; Kantor (1972),
Theorem1(ii)–(iii), p.261; Jones's multiply-transitive list; and
Pavlíková–Širáň, arXiv:2009.12963v1, §1. The last states the sharply
3-transitive classification as permutation groups, including the
standard twisted action. The project's earlier source inspection
and the producer's fresh checks retain the underlying classification
proofs as cited inputs. Aut(A_n)=S_n for n≥10 uses the previously
pinned alternating automorphism theorem; n=6 is covered separately.

The new [nearfield source record](../foundations/references.md#paired-nearfield-source)
pins Grundhöfer–Hering (2017), §2 definition, Lemma2.3 and following
paragraph, Theorem2.4, and Corollary3.1. The project and a source
auditor directly inspected the published HTML statements. Their cited
projective-subgroup and original nearfield-classification proofs were
not independently reproved. The primitive-prime input is the theorem
and exceptions quoted in Hestenes (1970), proof of Theorem2.12, p.499,
as [previously pinned](../foundations/references.md#paired-psl-singer-source). For
odd p and e>2 there is no exception; for e=2 the absent-prime case is
p+1 a power of two. The elementary affine full-period proof is also
written out in [the reviewed Singer continuation](paired-psl-singer-parabolic.md#all-regular-subgroups-in-a-fixed-normalizer),
source [the source revision](https://github.com/Mira-Cult/math-wip/commit/41f2531bf0fd228a977315000fcca6cda974dbeb); its cyclic-coset lemma
is used here independently of the projective group setting.

The separate [degree-49 control](../code/verify_nearfield49.g) enumerates
all subgroup conjugacy classes of GL2(7), filters order48 complements
by det(g−I)≠0 for every nonidentity element, tests actual permutation
parities on all 49 vectors, and fuses eligible index-two kernels under
the actual linear normalizer. It reports 84 ambient subgroup classes,
three fixed-point-free complement classes, one odd exclusion, and two
even classes with respectively one and two kernel orbits, total three.
The normalizer orders are 144 and 96; the eligible kernel counts are
one and three. These controls use GAP4.15.1's complete subgroup,
normal-subgroup and conjugacy algorithms. They do not independently
classify all sharply 2-transitive groups or prove the uniform theorem.
The project read and ran this certificate under GAP4.15.1 and obtained
the displayed results. Exact review records follow only after actual review.

The count (A), both infinite branches, their construction and exact
isomorphism orbits have the independent reviews recorded below. No
aggregate C0010 status is promoted. Product alternating
factorizations and the unrestricted Bol-loop classification remain open.


## Independent exact-source review

reviewers contributor 1,
contributor 2 and contributor 3
independently accepted the complete manuscript and certificate at
[the source revision](https://github.com/Mira-Cult/math-wip/commit/850653726c3641fc0c99c3d7f575dcedc0883561). Each checked actual-factor
exhaustion, the even-order two-homogeneous upgrade, all semilinear
parameters, parity and character restrictions, scalar recovery and
global conjugacy including the Mersenne boundary, distinct divisors d,
exceptional contributions, the twisted three-transitive branch, and
the construction and exact simultaneous-pair orbits. Each read and
extracted the exact committed GAP certificate and reran it under
GAP4.15.1, obtaining 84 subgroup classes, three regular complements,
one odd exclusion, and kernel-orbit counts one and two for the even
classes.

The paired-simple and strip-forest reviewers freshly inspected
Grundhöfer–Hering's published Lemma2.3 and following paragraph,
Theorem2.4 and Corollary3.1. The strip-forest reviewer also freshly
inspected Pavlíková–Širáň §1. The folder-criterion reviewer did not
freshly audit Grundhöfer–Hering. None reproved the external
classifications, primitive-prime theorem, GAP algorithms or pinned
upstream folder interfaces. These are model mathematical/code/source
reviews of the nonproduct paired alternating branch, not formal
GitHub approval, human/formal certification, or a solution of product
stabilizers and other canonical envelopes.


## Subsequent paired-branch completion

The [all-product assembly](paired-alternating-product-classification.md), independently accepted by three mathematical reviewers at [the source revision](https://github.com/Mira-Cult/math-wip/commit/45c50ef70aaab14d396178a5381160f8f95b8de7), now completes the complementary product classification under its cited inputs. Together the two branches exhaust this paired alternating setting, with finite-group isomorphism data retained in the regular-factor parameter. Historical statements that the other product alternatives remained open describe their pinned checkpoints; unrestricted simple Bol-loop exhaustion remains open.
