# Large alternating full socles have the natural action

Mira Cult

Proposed continuation of
[0323-finite-simple-non-moufang-bol-loops:C0010](../foundations/research-C0010.md).
Three independent mathematical/code reviewers accepted exact source
`755086f70b7e26ae976b1062ffa48949993d562c`, under the stated inputs, as
recorded below. The main classification remains
open. This manuscript owns the new bounded-centralizer extension and the
resulting full-action reduction; the inherited alternating estimates remain
canonical in [C0007 Theorem3.1](../foundations/C0007.md).

## Problem and exact inputs

**Conditionally proved full-action theorem.** For every finite simple proper left Bol loop
Q whose full multiplication group has socle A_m with m≥54, the full action is
permutation isomorphic to the natural action of A_m or S_m on m points.
In particular |Q|=m and its full multiplication group is doubly transitive.
There is no solvability assumption on G=LMlt(Q) or I=Mlt(Q)₁.
This is a reduction of possible actions, not a classification of the loop
operations in the surviving natural action.

Use the faithful canonical folder (G,H,K), its inversion extension E=G⋊⟨t⟩,
and actual selected set Λ=tK as defined in [PROBLEM.md](../foundations/problem-contract.md).
The inputs are C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, the scoped
C0007 inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, and the reviewed
C0008 full-Mlt almost-simplicity/UOD result at
`06857e28349ca4529c31a9855ce12cfbb191c1b7`. Thus 1∈K, ⟨K⟩=G, Λ is an
invariant set of outside involutions, |Λ|=[G:H], and H∩Λ²={1}.
No primitivity of G is assumed.

The all-degree canonical alternating proof, independently reviewed at exact
source `b03fdd414954bf1fc12186e13c8e3da404e87f95`, supplies C0007 Theorem3.1's
class-product Lemmas3.2–3.3, minimal-degree Lemma3.6 and the subsequent
gamma-vertex estimates and step-four induction. Its
[scoped assembly and source audit](../odd-completion/nonbruck-almost-simple-radical-bridge.md#proposed-exclusion-of-every-alternating-canonical-socle)
retain Dixon/Feit–Thompson, Praeger–Saxl and the other exact source qualifications.
We change the capacity by a factor of at most120 and verify new integer bases;
we do not claim that a finite computation proves the inherited analytic bounds.

## Bounded-centralizer component theorem

**Conditionally proved component theorem.** No such Q has a characteristic subgroup
T≅A_d of its canonical G with d≥49 and |C_G(T)|≤120.

Write c=|C_G(T)| and n=|Λ|. Characteristicity makes every formal mark act on
T, giving a map Λ→Aut(T)=S_d with each fiber of size at most c: two marks in
the same outside coset with equal actions differ by an element of C_G(T).
At least one mark acts nontrivially, since t∈Λ, K=tΛ and ⟨K⟩=G; if all marks
centralized T, G would centralize its nonabelian subgroup T.

Let C_k be the S_d-class of involutions of type 2^k1^(d−2k), including
C₀={1}. Its size is d!/(2^k k!(d−2k)!). For k≥1 the class does not split in
A_d, since a transposition occurring in a representative is an odd element of
its centralizer. If λ∈Λ induces an element of C_k, its T-conjugates realize
that entire class. Products of two such actual conjugates lie in T:
λ^u=λ[λ,u] with [λ,u]∈T, and λ²=1. The action T→Aut(T) is injective.
Consequently the entire class square C_k², which consists of even permutations,
is realized by actual elements of Λ²∩T. This retains the original selected set
and does not assert a folder on any quotient. Identity-image marks are allowed.

Put P=H∩T, q=⌊d/4⌋ and I(d)=Σ_{k=0}^{⌊d/2⌋}|C_k|. The actual T-orbit of the
base point has size [T:P], so

    n ≥ [T:P] = d!/(2|P|).

Let k_max≥1 be the largest selected nonidentity image label. If k_max≥q,
C0007 Lemma3.2 places every involution of T in C_(k_max)²⊆Λ²∩T. Hence P is
odd. The inherited Dixon bound gives |P|≤3^⌊(d−1)/2⌋. On the other hand
n≤cI(d), so necessarily cR(d)≥1, where

    R(d) = 2 I(d) 3^⌊(d−1)/2⌋ / d!.

The inherited recurrence R(d)≤3(R(d−1)+R(d−2))/d and the exact bases
120R(17)<1,120R(18)<1 prove 120R(d)<1 for all d≥17. This is a contradiction
in the high-support case.

If k_max<q, Lemmas3.2–3.3 put every 3-cycle and double transposition in
Λ²∩T. Thus P avoids both. Since P≤A_d, it has no transposition or 4-cycle
either, so its minimum degree is at least five. The inherited Lemma3.6 and
gamma-vertex argument give |P|≤max_i V_i(d), where

    V₁(d)=2·2^(d/5) Γ(d/2+1) Γ(d/5+1),
    V₂(d)=2·4^d Γ(d/5+1),
    V₃(d)=2·2^(d/2) Γ(d/2+1),
    V₄(d)=2·24^(d/4) Γ(d/3+1).

The inherited class-size ratio gives, including the identity fiber,

    n ≤ c Σ_(0≤k<q)|C_k| < 2c|C_q|/(d−2).

Combining the lower and upper bounds on n requires
c max_i V_i(d) ≥ RHS(d), with

    RHS(d) = (d−2)·2^q q! (d−2q)! / 4.

The exact integer ceilings in
[the arithmetic certificate](../code/verify_alternating_component_bound.py)
instead give 120 max_i V_i(d)<RHS(d) at d=49,50,51,52. For each gamma factor
and exponential, the certificate rounds its noninteger argument/exponent
upward; gamma is increasing in these ranges. The inherited analytic ratio
V_i(d+4)/V_i(d)<RHS(d+4)/RHS(d), valid for d≥42, preserves the factor120.
Step-four induction gives the strict inequality for all d≥49, a contradiction.
This proves the component theorem under the stated inputs.

**Actual-factor corollary.** If A_d×1≤G≤S_d×S_k with d≥49 and 1≤k≤5,
the canonical group G is impossible. Set T=A_d×1, so |C_G(T)|≤k!≤120.
For any automorphism φ of G, U=φ(T) is a normal simple subgroup isomorphic
to A_d. Either U∩T=T, giving U=T, or U∩T=1, giving an injection
U→G/T≤C₂×S_k, of order at most240. The latter is impossible by |A_d|>240.
Thus T is characteristic. This proof includes k=5 without asserting that
G/T is solvable.

## Exhaustive reduction of the high-degree full action

Put M=Mlt(Q), S=Soc(M)=A_m and I=M₁, where m≥54. Primitivity of the full
action makes I maximal and core-free. G is transitive, so M=GI.
If S≤G, the reviewed entire-canonical alternating theorem applies and excludes
Q. Otherwise both G and I are proper factors not containing S.

The exact primary statement is Chen et al., arXiv:2111.06579v2,
Theorem2.6, restating Liebeck–Praeger–Saxl TheoremD; see
[the reference audit](../foundations/references.md#alternating-full-action-sources).
It applies directly to A_m◁M≤Aut(A_m) and its actual factors M=GI, including
M=S_m. No assertion that (G∩S)(I∩S)=S is needed. Its exceptional degrees
6,8,10 are below our range. After interchanging the two factors, it gives

    A_(m−k) ◁ A ≤ S_(m−k)×S_k,    1≤k≤5,

with the other actual factor k-homogeneous in the natural degree-m action.
If A=G, put d=m−k≥49 and apply the actual-factor corollary above. Hence A=I.
The indicated set stabilizer J=(S_(m−k)×S_k)∩M is proper, and I≤J<M.
Maximality forces I=J. Therefore the full action is precisely the action on
k-subsets, and n=|Q|=binomial(m,k).

For 2≤k≤5, the reviewed Johnson disjointness argument
[C0009 Theorem1.2(1)](../foundations/C0009.md), also scoped reviewed in the
[earlier full-action reduction](../odd-completion/nonbruck-almost-simple-radical-bridge.md)
at `4922123613711b1884764a672d0091afabd5d991`, excludes every such loop action.
Indeed a translation taking the identity k-set E to a disjoint k-set must
displace every k-set to a disjoint one by C0008's UOD identity. A moved point
i and its image can be included in a k-set Y, contradicting that requirement.
The action has the Johnson orbitals and k<m/2 in this range.
Thus k=1, proving the stated natural-action theorem. Equality m=|Q| is a
conclusion, not an assumption identifying socle degree with loop order.

## Evidence and remaining gap

The source authors read and ran the exact integer certificate using Python3.12.14;
it verifies two high-regime bases and four low-regime bases. The high recurrence
and low step-four ratio are mathematical inputs from the independently reviewed
all-degree argument, not extrapolations from that finite run. The source authors
freshly inspected the primary Theorem2.6, including its almost-simple group
hypothesis. Its external factorization classification is retained as an input.
Independent exact-source review of this new extension and assembly is recorded below.

The remaining alternating obligations are the actual full actions with
5≤m≤53 and the operation/construction/isomorphism classification in natural
actions. Lie-type full socles remain separate. No global classification,
exhaustion of loop operations, or conclusion for an unbounded centralizer is
asserted.


## Independent exact-source review

automated-model reviewer A, reviewer B and
reviewer C each independently accepted the component theorem and
high-degree full-action reduction at exact source
`755086f70b7e26ae976b1062ffa48949993d562c`. They checked the original outside
fibers including identity images, generation forcing a nonidentity image,
actual T-conjugate class-square lifting, the T-orbit lower bound, both inherited
support regimes with factor120, the k=5 characteristic-subgroup argument and
actual maximal-stabilizer/Johnson-UOD assembly. Each retained the earlier
scoped acceptance of the C0007 alternating estimates at
`b03fdd414954bf1fc12186e13c8e3da404e87f95` and the other stated canonical inputs.

Each read and independently extracted the exact new Python source and ran it
with Python3.12.14, obtaining PASS for high bases17,18 and all four low vertices
at49–52. reviewer A and reviewer C freshly
inspected Chen et al. v2 Theorem2.6, including the actual almost-simple
factorization hypothesis and exceptional degrees6,8,10. reviewer B
used that cited statement without a fresh source inspection. None re-proved the
external LPS classification. The source authors's separate `check.py` run passed115
integrity tests; this is not a theorem check. These are independent model
mathematical reviews, not human/formal verification or GitHub approvals.
The reviews exclude neither small full-socle degrees nor natural loop operations.

## Proposed exclusion of the exceptional factorization clauses

This continuation has three independent mathematical acceptances at exact source
`fffcdec365c2a997f44eadc271279a059fbbe30a`, recorded below. It concerns exactly
Chen et al. Theorem2.6(b),(c), at socle degrees10 and8, in both actual factor
orientations. It does not
exclude every generic factorization at those degrees.

For m=10, one actual factor is PSL₂(8) or PSL₂(8).3, and the other lies between
N=A₅² and S₅ wr S₂. If the first is G, the reviewed canonical PSL₂ theorem
at `47b07688a82d3df93f537946fe0780112200383b` applies. If it is I, then
n=[M:I]≥|A₁₀|/1512=1200. In this orientation N=G^(∞) is characteristic,
because N is perfect and G/N is solvable. Its centralizer in S₅ wr S₂ is
trivial. Thus the original outside marked set injects into
Aut(N)=S₅ wr S₂. There are 1+10+15=26 involutions including identity in S₅.
The base coset of this wreath automorphism group has 26² such elements; the
swapped coset has120, since a pair (a,b) squares to 1 precisely when b=a⁻¹.
Therefore n≤26²+120=796<1200, a contradiction.

For m=8, one actual factor B is the natural AGL₃(2), while the other contains
an element of order15. The natural affine B lies in A₈: translations are
products of four transpositions, linear transvections are products of two,
and these generate B. If I=B, M=SI forces M=A₈, and n=20160/1344=15.
This contradicts the reviewed minimum-order24 result in C0011 (scoped source
`af8e206c079c37de3fd393f5a3e604525b94bed5`).

If G=B, let x∈I have order15. Its natural cycle type is (5)(3). If I were
primitive on the natural eight-point set, its 3-cycle x⁵ would force A₈≤I
by Jordan's prime-cycle theorem, impossible for the core-free full stabilizer.
The exact external statement is Jones2014 Theorem1.1, printed p.159, freshly
inspected and cited in REFERENCES. If I were transitive but imprimitive, it
would lie in S₂ wr S₄ or S₄ wr S₂. Both orders have only primes2 and3, so
neither contains x. Thus I is intransitive. Its orbits must be unions of the
two x-orbits; hence I preserves their 3+5 partition. Maximality in M gives
I=(S₃×S₅)∩M. The actual full action is the three-subset action, excluded by
the already reviewed Johnson/UOD argument. This proof covers M=A₈ and S₈
and requires no new automorphism-group or subgroup-table computation.

### Proposed residual alternating obligation

Combine these exceptional-clause exclusions with the earlier all-full-PSL₂
theorem, which excludes socles A₅≅PSL₂(5) and A₆≅PSL₂(9), and with the
reviewed high-degree theorem. Any remaining **nonnatural** full alternating
action must have 7≤m≤53 and the generic actual-factor orientation

    A_(m−k) ◁ G ≤ (S_(m−k)×S_k)∩M,  1≤k≤5,

where the actual full point stabilizer I is maximal and k-homogeneous in the
natural m-point action. To justify the orientation, if the generic intransitive
factor were I, maximality would make it the full k-set stabilizer. For
k≠m/2 its action is the subset action with subset size min(k,m−k); it is
natural for size1 and otherwise excluded by Johnson/UOD. For k=m/2, that
set stabilizer is strictly contained in the proper unordered-bipartition
stabilizer, contradicting maximality. This retains the small cases k>m/2
rather than assuming a simple large alternating component there. The k=1
canonical orientation is itself excluded by the reviewed entire-canonical
alternating theorem. Thus only k=2,3,4,5 remain in this explicit finite
socle-degree range. These reductions do not classify the natural-action loop
operations or address Lie-type full socles.


### Independent review of the exceptional clauses and residual range

automated-model reviewer A, reviewer B and
reviewer C each independently accepted this continuation at exact
source `fffcdec365c2a997f44eadc271279a059fbbe30a`. They checked the characteristic
A5²/wreath involution bound, even AGL3(2) embedding and degree15, the Jordan
and imprimitive-wreath alternatives for the order15 element, maximality and
Johnson contradiction, and the residual range including k=1, complementary
subsets, equal halves and the prior full A5/A6 exclusions. No new computation
was needed for these elementary deductions. All retained the stated Chen/LPS,
Jordan, canonical, minimum-order and UOD inputs. reviewer A
reported recent direct inspection of both primary statements;
reviewer C retained its prior direct Chen inspection and the
coordinator's Jones inspection; reviewer B retained the recorded source
audits without reopening them. None re-proved the external classifications.
The source authors's separate Python3.12.14 integrity run passed115 tests.
These are model mathematical reviews, not formal/human certification or
GitHub approvals, and leave the explicitly displayed generic residual open.


The independently reviewed [finite homogeneous-case completion](alternating-finite-homogeneous-exclusion.md) closes all four branches of this residual and the m<2k boundary under its stated inputs. Its three reviews are recorded there; this manuscript's previously recorded review scopes are unchanged.
