# A factorwise inversion obstruction for PSL₂ regular socles

**Mira Cult**

**Continuation of [0323:C0010](../../claims/0010.md), with scoped independent reviews below.** The bounded obligation is to test specified inversion automorphisms in the primitive twisted-wreath (TW) frontier. The argument is uniform in the number of simple factors and the stated field parameters. It excludes those marked automorphisms, not all TW groups or all inversion actions on a given group. The abstract obstruction below does not require primitivity.

## Statement and interfaces

Let T=PSL₂(q) and choose an involution α in Aut(T) in one of these two cases:

- q is odd, q≥5, and α belongs to PGL₂(q)\T;
- q=2^{2m}, m≥1, and α is the involutory field automorphism.

Identify N=T^k with Inn(T)^k in W=Aut(T) wr Sym(k), where k≥1. Let G=NH≤W be an internal semidirect product, so H∩N=1, and assume H≠1. Let b∈Aut(T)^k have each coordinate in the T-conjugacy class α^T. Assume b∉G, b normalizes G, and [b,H]≤N. Thus E=G⟨b⟩ is an extension by an outside involution, and b acts trivially on G/N. There is no set Λ⊂bG satisfying all of:

    b∈Λ;  every element of Λ is an involution;
    Λ is invariant under G-conjugacy;
    H∩Λ²={1};  ⟨bΛ⟩=G.

The canonical marked section of a simple nonassociative left Bol folder satisfies these conditions by the invoked inversion and twisted-subgroup input of [C0007](../foundations/C0007.md), Theorem 1.1(1), with b representing the inverting automorphism. Consequently it cannot have this group embedding and inversion action. For a TW group with characteristic regular socle N and C_G(N)=1, restriction embeds G faithfully in Aut(N), and an automorphism of G is represented by a normalizing element there; the theorem applies when that element satisfies the explicit hypotheses. It makes no assertion that every inversion automorphism does so.

## Local involutions

The source inputs are Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), 1315–1359, Appendix A, Lemma A.3, p.1355; the automorphism paragraph after Lemma A.4 and the finite Lang statement after Lemma A.5, p.1356 ([published PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf)). They give the involution classes and centralizers, Aut(T)=PΓL₂(q) for q>3, and conjugacy of a field-coset element to the field automorphism when their orders agree. The following consequences and the application to Λ are separate deductions.

Put C=α^T. This class is invariant under Aut(T). We claim: if d,ψ∈Aut(T) have orders dividing two and

    ψT=(αT)(dT) in Out(T),

then some T-conjugate ψ′ of ψ has the form cd, with c∈C and [c,d]=1.

For even square q, Out(T) is the cyclic field group. Its only nonidentity coset that can contain an involution is the one represented by α. The group T=PGL₂(q) has one inner involution class, and the finite Lang input gives one T-class of outer field involutions. The centralizer of α contains PSL₂(√q), which has an involution even for √q=2. Thus there are commuting representatives of the inner and the chosen outer class.

For odd q, Out(T) is the direct product of the diagonal C₂ and the cyclic field group. T has one involution class. There is one T-class C of diagonal outer involutions: their unique PGL₂-class does not split under T because the PGL₂-centralizer contains the outer involution itself. The T-centralizer of α has even order q−1 or q+1, so α commutes with an inner involution.

If the field degree is even, put q=s² and σ(x)=x^s. The coset with both diagonal and field components has no involutions. Indeed finite Lang conjugates every involution Mσ with M∈PGL₂(q) to σ, so M is a projective coboundary g⁻¹σ(g). Its determinant square class is trivial: det(g)^{s−1} is a square since s is odd, and changing matrix representatives only multiplies determinants by a square. Hence M∈T. Field involutions in Tσ can split into two T-classes; no uniqueness for them is assumed here. If d is in the field coset, the required ψ would be in the empty diagonal-field involution coset, and conversely. If the field degree is odd, these possibilities do not arise.

Thus in either of the two stated cases, the remaining d and ψ lie in the identity or chosen outer cosets. If d=1, take c=ψ. If d is inner and nonidentity, choose an outer involution ψ′ commuting with d by conjugating the commuting pair above; uniqueness of the outer T-class makes it a conjugate of ψ. Then c=ψ′d is an outer involution, hence lies in C. If d is outer and ψ=1, take c=d. If d is outer and ψ is an inner involution, conjugate a commuting pair so that its outer member is d, and take its inner member as ψ′; again c=ψ′d belongs to C. This proves the claim. It also explains why the argument does not apply unchanged to an odd-characteristic field involution as the chosen α.

## Conjugating a marked involution

The N-class b^N is the Cartesian product C^k and is contained in Λ. Given λ∈Λ, write λN=b sN with s∈H. Because b centralizes G/N and H∩N=1, λ²=1 implies s²=1. The permutation of the k factors induced by s has only fixed points and two-cycles; λ induces the same permutation.

At a fixed factor, s induces an automorphism d of order dividing two and λ induces ψ with outer coset αT·dT. The local claim supplies an inner conjugation making ψ=cd with c∈C commuting with d.

On a two-cycle i,j, write the two arrows of s as d_i,d_j∈Aut(T), with d_i d_j=1. Choose c_i∈C and put c_j=d_j c_i d_j⁻¹, which remains in C because C is Aut(T)-invariant. Then c commutes with s on this pair. If λ has arrows u_i,u_j, then u_i u_j=1, and u_i and c_i d_i have the same outer coset. In conjugating λ by an element of the two inner factors, keep the i-coordinate trivial and choose the j-coordinate to be u_i⁻¹c_i d_i∈Inn(T). The new i-arrow is c_i d_i, and involutivity forces the other arrow to be its inverse c_j d_j. This uses actual inner conjugations, not conjugation by a larger outer group.

Combining these independent conjugations gives an N-conjugate λ′=cs, where c∈C^k=b^N and [c,s]=1. Both c and λ′ belong to Λ. Hence s=cλ′ lies in H∩Λ² and is identity. Every λ therefore belongs to bN, so bΛ⊂N. Since H≠1, N<G and ⟨bΛ⟩ cannot equal G, the required contradiction.

## Scope and remaining TW actions

This proof uses no loop-order census or computation. It rules out factorwise diagonal inversion for every odd q≥5 and factorwise field inversion for every even square q, for arbitrary k and H satisfying the displayed embedding hypotheses. The case T=A₅ at q=4 or 5 is included with its indicated automorphism class. It leaves automorphisms that permute the factors or act nontrivially on G/N, and the odd-characteristic field-involution case, outside the theorem. The global primitive-LMlt question and the proper-loop two-family exhaustion remain open.

## Odd-characteristic field actions: a transversal-capacity obstruction

**Deduction with the scoped independent reviews below.** Retain the embedding and semidirect-product hypotheses of the statement, but now take T=PSL₂(s²), s an odd prime power at least three, and let every coordinate of b be a field involution. They may belong to either of its two T-classes. Suppose Λ⊂bG consists of involutions and |Λ|=|T|^k, as required of a marked transversal when N is regular. Put

    a=s(s²+1)/2,    t=|T|=s(s²−1)a,    M=1+sa,
    i₂(H)=|{h∈H : h²=1}|,

where i₂ includes the identity. Then a necessary condition is

    i₂(H) ≥ (t/M)^k.                                      (1)

This uses the full transversal cardinality but does not require factor transitivity, conjugacy invariance of Λ, or the collision condition. The two field classes must both be counted. Finite Lang gives one PGL₂(s²)-class of field involutions. Its projective centralizer is PGL₂(s): if a projective matrix is fixed by the field involution, scalar Hilbert 90 gives a representative over F_s. Every nonzero F_s element is a square in F_{s²}, so this centralizer lies in T. The PGL class therefore splits into two T-classes, each of size t/|PGL₂(s)|=a. These are consequences of the same source interfaces cited above, with the descent argument explicit here. The single inner involution class has size s²(s²+1)/2=sa, by Lemma A.3 and s²≡1 modulo four. The diagonal-field coset has no involutions, as already proved.

For λ∈bNh, involutivity forces h²=1. On a swapped pair of factors, its two automorphism arrows must be inverse, and one arrow has a prescribed outer coset. There are exactly t choices. At a fixed factor, let d be the local involution or identity induced by h. If d is inner or identity, λ lies locally in the field coset, giving 2a choices. If d is a field involution, λ lies locally in T, giving 1+sa choices. If d is diagonal outer, there are no choices, because the resulting diagonal-field coset contains no involution. These exhaust the possible local d.

Thus if h has r swapped pairs, its entire involution fiber has at most t^r M^{k−2r} elements. Since M²≥t (already (sa)²/t=s²(s²+1)/(2(s²−1))>1), this is at most M^k. Summing over h gives t^k=|Λ|≤i₂(H)M^k, proving (1). More precisely, if a label h has x fixed inner/identity sites and y fixed field sites, its capacity is exactly t^r(2a)^x M^y, unless a fixed diagonal site makes it zero. The sum of these capacities must be at least t^k; the collision and conjugacy conditions can further reduce the usable capacity.

For s=3 the bound is i₂(H)≥(180/23)^k. In particular, any six-factor embedding satisfying these hypotheses with H abstractly S₆ is excluded, since S₆ has 1+15+45+15=76 elements of order dividing two. This is conditional on the stated embedding and inversion action, not a claim that such an embedding is primitive TW or that every inversion action is covered.

The earlier conjugation proof does not extend unchanged: for a chosen field class C, the local equation ψ′=cd fails when d=1 and ψ belongs to the other class, or ψ=1 and d belongs to the other class. Also diagonal automorphisms exchange the two field classes, so [b,H]≤N does not ensure H preserves b^N. The capacity bound avoids that assumption. It does not exclude arbitrary H, whose involution count may exceed (t/M)^k, and supplies no universal bound on k. The remaining task must use the actual class compatibility and full transversal constraints or a stronger structural restriction on H.

### Natural alternating and symmetric factor actions

**Deduction with the scoped independent reviews below.** Under the odd-field hypotheses of the preceding section, suppose additionally that G is primitive of TW type and that its action on the k simple factors contains A_k. Then no marked transversal exists.

The TW source interface is Liebeck–Praeger–Saxl, *On the O'Nan–Scott theorem for finite primitive permutation groups*, J. Austral. Math. Soc. (Series A) 44 (1988), 389–396, §1 III(c), printed p.391, and §2 ([published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9286080793AA683DFB749077A44F9305/S144678870003216Xa.pdf/on-the-onan-scott-theorem-for-finite-primitive-permutation-groups.pdf)). In the TW representation the factor stabilizer H_i has a local homomorphism into Aut(T_i) whose image contains Inn(T_i). This is a necessary interface for the TW type, not a sufficient criterion for primitivity.

For clarity the faithful-factor-action deduction can also be made inside our embedding. Let R be the kernel of H on the factors. Since R≤Aut(T)^k and R∩N=1, it embeds in Out(T)^k, which is abelian for this T. For each i its local image is a solvable normal subgroup of the image of H_i, which contains the nonabelian simple group Inn(T_i). Such a subgroup is trivial: its intersection with Inn(T_i) is trivial, its commutators with Inn(T_i) lie in that intersection, and C_Aut(T_i)(Inn(T_i))=1. Hence R acts trivially on every factor, so R=1. We may identify H with its factor permutation group, which is A_k or S_k. This argument also shows that a solvable factor point stabilizer is impossible, but does not classify all possible transitive H.

Put n=k−1. The factor stabilizer is A_n or S_n and has an image in Aut(T) containing T. For n≤4 it is solvable, impossible. For n≥5, the normal subgroups of A_n and S_n show that any such image forces T≅A_n: a nonsolvable image of A_n is A_n; a nonsolvable image of S_n is S_n, whose only nonabelian simple normal subgroup is A_n. If n≥8, A_n contains C₂⁴ from the two disjoint Klein-four groups on eight letters, whereas PSL₂(s²) has no elementary abelian 2-subgroup of rank greater than two. The latter follows from the dihedral centralizer of any inner involution in Lemma A.3: an elementary abelian 2-subgroup lies in the centralizer of each of its nonidentity elements, and a dihedral group has elementary abelian 2-rank at most two. Thus 5≤n≤7. The orders rule out n=5 and 7: the smallest |PSL₂(s²)| for odd prime powers s≥3 are 360 at s=3 and 7800 at s=5, while |A₅|=60 and |A₇|=2520. The remaining case is n=6, s=3, k=7.

Here i₂(H)≤i₂(S₇)=1+21+105+105=232, while (1) requires i₂(H)≥(180/23)^7>232. This contradiction excludes every natural alternating or symmetric factor action under the displayed odd-field inversion hypotheses. It leaves other transitive factor groups and all inversion actions outside those hypotheses open. No loop-order enumeration or classification of all TW groups is used.

### Excluding every primitive factor action

**Deduction with the scoped independent reviews below.** Under the odd-field hypotheses above, the factor permutation group H cannot be primitive. If it contains A_k, the preceding argument excludes it. Otherwise the unnumbered theorem on p.303 of Praeger–Saxl, *On the orders of Primitive Permutation Groups*, Bull. London Math. Soc. 12 (1980), 303–307, gives |H|<4^k. On the other hand

    t/M=(s²−1)·sa/(1+sa) ≥ 8·45/46=180/23 >4,

because s≥3 and a=s(s²+1)/2. The transversal-capacity inequality gives |H|≥i₂(H)≥(t/M)^k>4^k, a contradiction. The theorem statement was directly inspected in the publisher's first-page image and independently in the original-paper PDF; the published DOI is [10.1112/blms/12.4.303](https://doi.org/10.1112/blms/12.4.303).

Therefore any remaining primitive TW envelope with this factorwise odd-field inversion must have an imprimitive action on its simple factors. The action on loop elements remains primitive by hypothesis; these are different permutation actions. Primitive TW groups can have imprimitive factor actions, so this is not a TW exclusion. The local involution-class compatibility and full transversal geometry remain unresolved for those actions.

## Independent review

reviewers contributor 1, contributor 2, and contributor 3 independently accepted the displayed obstruction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/abe9074d72269cd9d8b1363cde8ce16677b701e6). All checked the local commuting-representative argument, the fixed-factor and two-cycle inner conjugations, and the marked collision followed by failure of generation. Their acceptances retain the explicit embedding, semidirect-product and marked-section hypotheses, including H≠1 and b∈Λ⊂bG, and the invoked C0007 interface. The first and third reviewers directly checked Guralnick–Zieve's published Appendix A, Lemma A.3 and the automorphism and finite Lang passages; the second relied on these stated source inputs. No review assumes uniqueness of odd-characteristic field-involution T-classes. These are scoped mathematical/source reviews, without computation or formal verification; they do not certify general TW exclusion or primitive-LMlt nonexistence.

reviewers contributor 2 and contributor 3 independently accepted the odd-field capacity and natural alternating/symmetric factor-action sections at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6033272fbbd42f39c07ae59808ca122c9d60348e). They checked both field classes, the local and paired-factor capacities, faithful factor action, alternating normal-subgroup and rank/order reductions, and the remaining seven-factor contradiction. Both directly inspected the LPS §1 III(c) interface; the second also directly inspected Guralnick–Zieve, while the first retained those previously stated inputs. Their reviews retain every embedding and inversion hypothesis and do not cover arbitrary TW actions or the subsequently added all-primitive-factor deduction. No computation or formal verification was used.

The same two reviewers independently accepted the all-primitive-factor-action deduction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/0f95563fbefd29f3d54c671238a98b9968fdbfed), conditional on the capacity and natural-action results reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6033272fbbd42f39c07ae59808ca122c9d60348e). Both directly inspected the publisher's first-page statement of the unnumbered Praeger–Saxl theorem and checked the uniform numerical inequality. They explicitly distinguished the factor action from the loop action: imprimitive factor actions and inversion actions outside the manuscript's hypotheses remain open. No computation or formal verification was used.
