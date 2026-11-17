# Candidate almost-simple / non-Bruck radical bridge

**Publication reading note.** This source preserves chronological proof sections and their local review records. Later assemblies supersede earlier pending PSL₂, odd-dimensional PSL/PSU, sporadic and F₄ full-socle boundaries. See the [current coverage index](../../CLASSIFICATION.md) and [publication checkpoint](../../PUBLICATION-2026-11-17.md); “proposed” headings are retained historical labels, not an assertion that every section remains unreviewed. The aggregate classification remains open.

Mira Cult

Scope: finite simple nonassociative left Bol Q, with G=LMlt(Q), H=G_1, n=|Q|, M=Mlt(Q), I=M_1, and τ the C0007 canonical inverting automorphism. Use C0001 for primitivity of M and C0008 for its almost-simple conclusion; C0008 now has two aggregate mathematical reviews, with their source and bibliographic limits recorded in the canonical claim. Write S=Soc(M), e=|Out(S)|, and use the classification-dependent Schreier theorem that Out(S) is solvable. This is a reduction with scoped independent review below, not a solved classification or new claim. It applies in particular to 0323.NONBRUCK_EVEN and does not require τ(H)=H.

## Factorization and τ-stable core

S is nontrivial normal in primitive M, hence transitive. Thus M=SI and n=[S:S∩I]. Set A=G∩S and J=A∩τ(A). Since S◁M, A◁G and G/A embeds in M/S≤Out(S). As τ is an automorphism, J◁G is τ-stable and J≤S. Indeed, [G:J]=[G:A][A:J], and the map A/J→G/τ(A) is injective, so [A:J] divides [G:τ(A)]=[G:A]. Consequently [G:J] divides [G:A]² and hence e². The J-orbits form a G-invariant block system: their number d=[G:JH] divides both n and [G:J], so d divides gcd(n,e²). Under Q≅S/(S∩I), this is the number of double cosets J\S/(S∩I). The analogous A-orbit number divides gcd(n,e).

If gcd(n,e)=1 then J is transitive, so S=J(S∩I). If Rad(G)≠1, J<S: indeed, if G≥S, then Rad(G)∩S is a solvable normal subgroup of simple S and is trivial, and [Rad(G),S]≤Rad(G)∩S=1. But C_M(S)=1 since M≤Aut(S) in its almost-simple embedding; hence Rad(G)=1, contradiction. Also S∩I<S because S is transitive on more than one point. Thus in the coprime, nontrivial-radical case S factors as a product of two proper subgroups, one J normal in G and τ-invariant.

Moreover Rad(G)∩J≠1 in that case. Otherwise Rad(G) injects into G/J, so its order divides e². Its orbits have a common size, dividing both n and |Rad(G)|; this common size is 1. Faithfulness then gives Rad(G)=1, contradiction. More generally, without coprimality the number of J-double cosets is bounded by gcd(n,e²), a concrete low-double-coset structural problem. If C0005's evenness is available and S=A_n in the natural degree-n action, G≤A_n=S, so J=G and S=G(S∩I) without a coprimality assumption. This can still be weak: for the order-24 loop the resulting ambient factorization A24=G A23 is a transitive-subgroup factorization, and alone does not classify folders.

The solvable residual G^(∞) is characteristic in G, hence τ-stable, and lies in A≤S: its image in the solvable group G/A is trivial. Do not assume A itself τ-stable; that is why J is used. For any prime p not dividing e, the normal p-subgroup O_p(G) lies in J, because its image in G/J is a p-subgroup of a group of order dividing e².

## A free commutator section of a radical

Let E◁G be τ-stable elementary abelian of order p^m; one canonical choice when P=O_p(G)≠1 is E=Ω₁(Z(P)), which is nonzero and characteristic in G. Put W=[E,τ]=im(τ−1)≤E. In the external semidirect product G̃=G⋊⟨t⟩, both t and t^x lie in Λ for x∈E, so each commutator t t^x lies in Λ²; these commutators constitute W. The C0007 folder identities give that Λ² is G-conjugacy invariant, closed under powers, and has trivial intersection with H. Therefore every nonidentity element of Λ² is semiregular on Q: a power fixing a point belongs to a conjugate of H and must equal 1. In particular W acts freely. It follows that |W| divides n and

    rank_Fp(τ−1 on E) ≤ v_p(n).

If p∤e, the preceding paragraph places P and E inside the τ-stable subgroup J≤S. For odd p, W is the −1-eigenspace of τ on E; for p=2, W⊆C_E(τ). No nontriviality of W follows: τ may centralize E, so this alone gives no universal bound on |E| or the radical.

## Next bounded mathematical obligation

For a selected almost-simple socle/action (S,S∩I) with n even, classify or bound τ-stable subgroups J≤S with at most gcd(n,e²) orbits and a nonzero normal elementary-abelian p-subgroup E≤J for p∤e, while imposing the free τ-commutator condition above. In the coprime, nontrivial-radical case this becomes S=J(S∩I) with J and S∩I proper. Work first in one nonalternating almost-simple action with an accessible factorization/subgroup theorem; do not assume J is a loop multiplication group by itself. A successful group-theoretic classification would supply structural envelope data; failure of a sufficient screen is not a loop construction. The derived bounds have the scoped independent review below, conditional on the stated inputs.

## First source check: the PSL₂ natural action is already excluded

The natural projective-line action is not a fruitful unresolved test for the preceding radical reduction. Aleš Drápal, *Multiplication Groups of Loops and Projective Semilinear Transformations in Dimension Two*, Journal of Algebra **251** (2002), 256–278, [doi:10.1006/jabr.2001.9120](https://doi.org/10.1006/jabr.2001.9120), Theorem 5.1, printed p. 276, proves that if $`F`$ is finite with $`|F|\notin\{3,4\}`$ and $`\mathop{\mathrm{Mlt}}\nolimits(Q)\le\mathop{\mathrm{P\Gamma L}}\nolimits_2(F)`$ in its natural action on $`F\cup\{\infty\}`$, then $`Q`$ is a group (indeed cyclic). The theorem concerns the **full** multiplication group and all loops; it does not follow merely from the left multiplication group embedding. The theorem statement and its exceptions were checked in the published text; the underlying proof, including its stated finite computation at $`|F|=8`$, was not independently reverified here.

Consequently a finite simple nonassociative left Bol loop cannot have its full multiplication group in the natural $`\mathop{\mathrm{P\Gamma L}}\nolimits_2(q)`$ action for $`q\ge5`$. For $`q=2,3,4`$ the respective degrees are $`3,4,5`$ and the prime-power nonexistence part of [C0011](../../claims/0011.md) excludes the target. This application does not assume C0008, any radical hypothesis, or the non-Bruck condition. It is stronger than the proposed first radical test in this action and prevents presenting that test as an open structural advance. It does not exclude other permutation representations of $`\mathop{\mathrm{PSL}}\nolimits_2(q)`$, other almost-simple socles, or groups whose left multiplication group alone has this embedding. A useful next test should choose an action outside this source theorem, after checking the corresponding known exclusions.

## Stabilizer intersections for arbitrary parity

A further necessary condition does not use almost-simplicity or odd order. Under the canonical C0007 marked-section hypotheses, for every λ∈Λ one has H∩H^λ=C_H(λ). Indeed, if h∈H∩H^λ, then h^λ∈H and λ^hλ=h⁻¹h^λ lies in H. Both λ^h and λ belong to Λ, so H∩Λ²=1 forces h^λ=h. The reverse inclusion is immediate. In particular H∩τ(H)=C_H(τ). This does not force that intersection to be trivial or equal to H.

The odd-order parameterization's converse uses oddness essentially. At even order, an element h=λλ′∈H that is centralized by λ can be a nonidentity involution; the displayed intersection equalities alone do not exclude it. Thus this necessary condition does not replace the full H∩Λ² collision test for even folders. This deduction has the scoped independent review below; no stronger centralizer dichotomy is asserted.


## Independent review

automated-model reviewer a research reviewer independently accepted the new group-theoretic reductions and parity-independent stabilizer intersection at exact source `0c9fac5ed9880a7038e54b501b32ed61744b5b57`, conditional on C0001/C0007, C0008's almost-simple conclusion and Schreier. The review checked the subgroup index and orbit bounds, coprime factorization, radical intersection, p-subgroup placement and free commutator section. At that historical review source C0008's aggregate review remained unreviewed, and the C0005 evenness input applies only within its own stated exact-factorization hypotheses. The reviewer did not inspect Drápal's primary theorem; that application retains the separate source-reading limits above. No computation, formal verification, general radical bound or classification was accepted.


## Proposed exclusion of the linear Singer row at even order

**Conditional deduction with scoped independent reviews below.** Continue [C0010](../foundations/research-C0010.md) for every finite simple nonassociative left Bol loop Q of even order N. Write G=LMlt(Q), H=G₁, M=Mlt(Q), I=M₁ and S=Soc(M). Assume the actual factorization M=GI lies in [Li–Xia arXiv:1408.0350v3](../foundations/references.md#lx16-solvable-factor), Theorem 1.1(d), Table 1.1 row 1, with S=PSL_n(q), q=p^f and n≥2. Use C0001/C0007's canonical generating section and inversion, C0008's primitive almost-simple conclusion and C0011's prime-power exclusion, with their exact scopes recorded in the [odd full-group assembly](odd-envelope-parameterization.md#right-translation-sign-and-the-odd-alternating-full-group). Then this row is impossible under these inputs. This is a theorem about the actual row containment, not all PSL permutation actions or every solvable envelope.

The row supplies `G₀=G∩S≤T_S:n` in a Singer normalizer and a normal subgroup `E=q^(n−1):SL_(n−1)(q)` of J=I∩S, with the source's projective conventions. Its characteristic p-core is the natural unipotent radical U; its common fixed space is the defining point. Thus `J≤N_S(U)=P`, a point parabolic or its dual, as in the reviewed odd Singer-row argument. Since S is transitive in primitive M,

    m=(q^n−1)/(q−1) divides N=[S:J]=[G:H].

This is divisibility, not a claim that J=P. Let T be the full projective Singer torus in PGL_n(q), of order m; it may be larger than the torus T_S in S.

### Metabelian groups with a 2-group stabilizer

For any finite simple nonassociative loop, if G=LMlt(Q) is metabelian and H=G₁ is a 2-group, then |Q| is odd. To prove this, HG′ is normal, because its image in G/G′ is a subgroup of an abelian group. The map `x↦L_x HG′` is a loop homomorphism to the abelian group G/HG′: indeed `L_(xy)^(-1)L_xL_y∈H`. Its image generates that quotient. Simplicity and nonassociativity force the homomorphism to be trivial, hence `G=HG′`. The abelian subgroup D=G′ is therefore transitive. An element of an abelian transitive permutation group that fixes one point fixes all points; faithfulness makes D regular. Thus `D∩H=1`, `G=D⋊H`, and `H′≤D∩H=1`, so `D=G′=[D,H]`.

If the 2-primary component D₂ is nontrivial, the nonzero vector space D₂/2D₂ has nonzero coinvariants under the 2-group H. For example the dual has a nonzero fixed vector, by the elementary fixed-vector theorem for a 2-group in characteristic two. Hence `[D₂,H]` is proper in D₂, contradicting `[D,H]=D`. Thus D, and consequently Q, has odd order. A second consequence used below is that any finite simple nonassociative loop whose metabelian G has odd derived subgroup already has odd degree, since G′ is transitive.

### Primitive prime case, including graph automorphisms

Suppose p^(nf)−1 has a primitive prime divisor ℓ. Then ℓ>nf, ℓ∤q−1, and ℓ divides m. No ℓ divides Out(S), whose order divides `2f gcd(n,q−1)`. The row therefore forces ℓ into G₀. Its Sylow ℓ-subgroup A lies in the cyclic T_S and is unique in G₀; every ℓ-subgroup of G lies in G₀, so A is unique in G and characteristic. The [cyclic-normal inversion argument](odd-envelope-parameterization.md#proposed-characteristic-section-inversion-obstructions), in its arbitrary-parity form, gives `G/C_G(A)` exponent at most two.

An order-ℓ element acts irreducibly over F_q. Its centralizer in PGL_n(q) is T: its linear field algebra has centralizer F_(q^n)^×, and an extra projective scalar in a centralizing equation must have ℓ-power order, hence be trivial because ℓ∤q−1. Every automorphism normalizing A normalizes this T. The standard full automorphism description consists of projective semilinear maps and inverse transpose (redundant for n=2). In the field model on F_(q^n), the semilinear torus normalizer acts modulo T by `x↦x^(p^j)`, j modulo nf. Under the trace pairing, the adjoint of scalar multiplication by a is multiplication by a, so the contragredient map acts on T by a↦a^(-1). It commutes with Frobenius modulo T. Consequently the normalizer quotient over T is contained in `C_(nf)×C₂`, acting on A by exponents `±p^j`.

Since `ord_ℓ(p)=nf`, the kernel of this exponent action has order at most two. Its image is in the cyclic automorphism group of A, so an image of exponent at most two has order at most two. The actual quotient `G/(G∩T)` therefore has order dividing four and is abelian. Thus G is metabelian and `|G|` divides 4m. As m divides `[G:H]`, it follows that `|H|` divides four. The preceding lemma contradicts even N. This retains graph automorphisms; their possible contribution to the kernel is why one must not replace the full centralizer by the smaller socle torus or assume all field/graph components vanish.

For sources, the full classical automorphism statement is Kleidman–Liebeck, *The Subgroup Structure of the Finite Classical Groups* (1990), §2.1 definitions, Table 2.1.B p.15 and Theorem 2.1.4 p.16, in the [publisher preview](https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf). Its exceptions are not simple PSL groups. The source authors inspected these primary pages, including the cached preview after a fresh fetch timed out. Hestenes, *Singer groups* (1970), p.497, the paragraph before Theorem 2.7 and Theorems 2.7–2.9, gives the linear/projective Singer normalizers and centralizers; the [exact source record](../foundations/references.md#paired-psl-singer-source) retains the directly inspected version. The graph/field normalizer deduction above is local, not a theorem attributed to Hestenes. Zsigmondy is used in the precise Li–Xia Theorem 2.3 form, with every exception treated next.

### Primitive-prime exceptions

If nf=2 and p+1 is a power of two, then n=2 and f=1. The Singer-row bound makes `|G₀|` divide p+1, and Out(S) has order two. Thus G is a 2-group, so its transitive degree is a power of two, contrary to C0011. The nonsimple PSL₂(2), PSL₂(3) parameters are already outside the socle hypothesis.

For `(p,nf)=(2,6)` there are three cases. Their normalizers follow from the same field/trace model and full automorphism description:

* `(n,q)=(3,4)`: m=21 and the row's C7 is the unique Sylow 7 subgroup of G, since 7 does not divide the outer order. It acts irreducibly over F4. The quotient over T has form `C6×C2`, with exponent action `±2^j` on C7, image of order six and kernel of order two. The inversion argument again bounds the actual quotient by four, making G metabelian with |G| dividing 4m and |H| dividing four. The lemma gives a contradiction.
* `(n,q)=(6,2)`: m=63, Out(S)=C2 and `G₀≤C63:6`. Its unique Sylow 7 subgroup is characteristic in G. The cyclic-normal argument bounds its conjugation image by exponent two. The inner C6 has image C3 on C7, so `G₀≤C63:2`. Since 63 divides N and the outer index is at most two, the intersection with C63 contains its full C9 and C7. These are the unique Sylow 3 and Sylow 7 subgroups of G₀, making C63 characteristic in G₀ and normal in G. Now G/C63 is a 2-group, so C63 is the unique normal Hall subgroup of odd order in G and is characteristic in G. Its full normalizer has quotient `C6×C2`, acting faithfully by `±2^j` modulo 63, since −1 is not a power of 2 modulo 63. Applying cyclic-normal inversion to C63 puts the actual quotient in its 2-torsion, of order four. Once again G is metabelian and |H| divides four. No irreducibility of C7 on the six-dimensional module is asserted.
* `(n,q)=(2,8)`: m=9, `G₀≤D18` and Out(S)=C3. If the 3-part of G₀ has order at most three, |G| divides 18; an even degree divisible by nine must equal 18, making G regular and the loop associative. Otherwise G₀ contains C9, its unique Sylow 3 subgroup. It is characteristic in G₀ and therefore normal in G. Hence `G≤N_Aut(S)(C9)=9:6`, with derived subgroup inside C9. The preceding transitive-derived-subgroup argument forces odd degree, contradiction. C9 need not be characteristic in G and no such assertion is used.

Together these exhaust the primitive-prime exceptions. Combined with the separately reviewed odd Singer-row exclusion at `b8c237d84f001b9a3d70ab725adab6b67e57c05b`, the reviewed even argument excludes this actual Li–Xia row at every parity under the combined stated inputs. Other classical rows, alternating actions and nonsolvable canonical envelopes remain separate obligations. No numerical computation or classification of their loop operations is claimed.

### Independent review of the even Singer-row exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted the entire even Singer-row deduction at exact source `10707e0947bfae06db707d8cc477372d197eabf7`. All checked the metabelian stabilizer lemma, degree and order divisibilities, characteristic cyclic subgroups, full-torus graph/field action and every primitive-prime exception. reviewer A retained its prior direct Hestenes and Kleidman–Liebeck primary-source inspections; reviewer B retained its earlier Li–Xia inspection but its attempted fresh publisher-preview fetch timed out, so it relied on the source authors's recorded inspection for that source. reviewer C accepted the local reasoning under the declared classical inputs. Separately, a research reviewer directly inspected the cached Kleidman–Liebeck pp.14–16 during the preliminary audit and checked the trace-pairing derivation; a research reviewer checked the preliminary metabelian lemma and row arithmetic. Those preliminary audits are distinct from the three exact-source acceptances. No reviewer reproved the cited classifications or ran a computation. The scope is the actual Singer row, not the whole even classification.

## Proposed all-parity exclusion of metabelian left multiplication groups

**Conditional theorem with three independent reviews below.** Let Q be any finite simple nonassociative left Bol loop. Under the canonical faithful-folder and inversion interfaces of [C0001](../../claims/0001.md) and [C0007](../foundations/research-C0007.md), and the pinned odd-envelope input used below, its actual group G=LMlt(Q) is not metabelian. This has no parity, Bruck, exponent, radical, full-multiplication socle or primitive-left-action hypothesis. It does not bound the derived length of solvable G from above or classify its admissible higher layers.

Assume G is metabelian and let H=G₁. The quotient-to-group argument in the preceding metabelian lemma gives `G=HG′`; the abelian group A=G′ is regular, so `G=A⋊H`, H is abelian and `A=[A,H]`. Use additive notation on A. The averaging calculation in [the odd metabelian argument](odd-folder-radicals.md#stabilizer-nonconjugacy-and-exclusion-of-metabelian-envelopes), reviewed at `e896039d004ff3882621aca115b1a39cc8fed207`, applies to arbitrary finite abelian A,H with this commutator equality: none of its averaging or p-group coinvariant steps uses oddness. Specifically, for each primary component A_p and `H=P×B_p` with P the Sylow p-subgroup, averaging gives `A_p=A_p^(B_p)⊕[A_p,B_p]`. A nonzero first summand would equal its P-commutator, contradicting the nonzero coinvariants of its reduction modulo p. Thus `A_p^(B_p)=0`. Averaging a 1-cocycle on B_p and then using the commuting action of P, exactly as in that canonical calculation, gives `H¹(H,A)=0`. It also gives `C_A(H)=0`, hence `N_G(H)=H`. These are the parity-free parts of that proof, not an invocation of its odd marked-class conjugacy conclusion.

Let `G⁺=G⋊⟨t⟩`, with formal involution t inducing the canonical τ, and let Λ=tK be the actual selected marked set. The C0007 interfaces give `t∈Λ`, G-conjugacy invariance of Λ and `H∩Λ²={1}`. We do not assert Λ is the full outside involution set or a single G-class. Since A is characteristic, τ(H) is a complement to A. The proved H¹(H,A) vanishing conjugates this complement to H, so choose d∈A such that `s=d t` normalizes H. Its square lies in `A∩N_G(H)={0}`, so s is an involution. Conjugation by s induces inversion on G/A, because t inverts K and K generates G. As s normalizes H, it acts by inversion on H itself. Let σ be its action on A.

We claim that `H¹(C₂,A)=0` for the **formal** C₂ acting through σ. For odd-primary A this follows by averaging. For A₂, put `B=O_(2′)(H)`. The preceding averaging gives `A₂^B=0`. Every layer `V_i=2^i A₂/2^(i+1) A₂` also has zero B-fixed space, since taking B-invariants is exact on finite 2-groups: a fixed coset has a fixed lift by averaging. Over an algebraic closure of F₂, the odd abelian B acts diagonally. Every occurring character χ is nontrivial, and conjugation by s sends χ to χ^(-1). These are distinct because χ has odd order. Thus σ interchanges the two isotypic spaces in every such pair. On their sum, an involution interchanging the summands has `ker(1+σ)=im(1+σ)`, so H¹(C₂,V_i)=0. Exact extension of scalars preserves this equality, and it therefore holds over F₂.

Induct through the finite 2-power filtration to get H¹(C₂,A₂)=0. Explicitly, if a is an involutory cocycle in A₂, its image modulo 2A₂ is a coboundary. Subtract a lifted coboundary; the remaining cocycle lies in 2A₂, where induction applies. This proves the claim without assuming the entire selected outside class is known.

As `t=(-d)s` is an involution, `d+σ(d)=0`. Vanishing gives `d=b−σ(b)` for some b∈A. Then, inside the actual G⁺,

    b^(-1) s b = (-b+σ(b)) s = (-d)s = t.

Hence s is an A-conjugate of the original selected t and belongs to Λ. Since s normalizes H, for every h∈H the element `s^h s=h^(-1)h^s` belongs to both H and Λ², so it is the identity. Therefore s centralizes H. It also inverts H, making H an elementary abelian 2-group (possibly trivial). The preceding metabelian stabilizer lemma now makes A and |Q| odd. The reviewed odd-envelope application of Foguel–Kinyon–Phillips, `arXiv:math/0208231v2`, Proposition 6.1 and Theorem 4.14, at `ab4059e6a9b8d5876e2bffa993bb98e7dac69025`, makes the canonical G odd. Thus its 2-subgroup H is trivial; G is regular and Q associative, contradiction.

The genuinely new step beyond the odd proof is involution cohomology on the 2-primary layers and its use to recover an **actually selected** normalizing involution. Complement conjugacy alone does not supply that membership at even order. This proposed deduction uses no quotient-folder assumption and no almost-simple classification. The affine reduction and new cohomology argument received preliminary scratch audits from a research reviewer and a research reviewer; those are proof-development checks, not exact-source independent acceptance. No computation or novelty claim is made.

### Independent review of the all-parity metabelian exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted the complete all-parity deduction at exact source `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`. They checked the parity-free averaging, complement normalization and involution square, the characteristic-two character-pair argument and filtration induction, the actual conjugation into Λ, the collision step and final odd-envelope implication. None assumed a single outside class, primitive LMlt, or an almost-simple full multiplication group. Acceptance is conditional on the specifically used canonical and odd-envelope inputs; no reviewer freshly reproved those inputs or ran a computation. This excludes metabelian LMlt for the stated full loop class, but neither classifies higher derived structures nor bounds their length. These are independent model mathematical reviews, not formal verification or GitHub approval.


## Proposed all-parity exclusion of the PSL4 symplectic-factor row

**Conditional deduction with three independent reviews below.** This continues [C0010](../foundations/research-C0010.md) without a new claim ID. Let X be a finite simple nonassociative left Bol loop, G=LMlt(X), M=Mlt(X), I=M₁. Assume the canonical generating section/inversion and primitive almost-simple full-multiplication inputs, with the exact canonical and standard-input review scopes recorded in the preceding sections. Suppose the actual factorization M=GI lies in [Li–Xia arXiv:1408.0350v3, Table 1.1 row 2](../foundations/references.md#lx16-solvable-factor): S=PSL4(q), q=p^f, G∩S≤U:((q³−1)/d).3 for the displayed Singer parabolic, U≅Fq³, d=gcd(4,q−1), and I∩S contains natural PSp4(q) normally. The [row-2 symplectic-normalizer calculation](odd-envelope-parameterization.md), with its scoped reviews at `a1eb46e7c4dcaa3200f1160e45cf464784d1746b`, gives degree divisible by q²(q³−1)/2 for q odd and q²(q³−1) for q even. This deduction makes no assumption that |X| or |G| is odd, or that X is Bruck or exponent two.

### Primitive-prime case

Assume (p,f)≠(2,2). Zsigmondy gives a primitive prime r for p^(3f)−1; ord_r(p)=3f, r>3f and r∤q−1. It divides the degree and |G|, but not |Out(S)|, which divides 2df. Therefore r divides |G∩S|. Its Sylow-r subgroup lies in the scalar Singer part and acts irreducibly on U as an Fp-space of dimension D=3f.

The degree contributes p^{2f}. For odd p the inner semilinear C3 and the outer group together contribute at most (3f)_p; p^{2f}>(3f)_p. For p=2 the inner complement is odd and the outer 2-part is at most (2f)_2; 2^{2f}>(2f)_2 even for f=1. Hence N=(G∩S)∩U is nonzero. It is r-invariant, and Fp-irreducibility gives N=U.

The quotient (G∩S)/U has a normal cyclic Sylow-r subgroup. Any normal p-subgroup centralizes it and lies in its p′ scalar centralizer, so U=O_p(G∩S) and U◁G. The common fixed line, or dual fixed hyperplane, recovers the parabolic type; a graph automorphism exchanges the two distinct parabolic types and cannot normalize U. Concretely the span of all images of u−1 has dimension one for the point radical and three for its dual, so they are not inner-conjugate. A Levi/field element acts on U by v↦(A/a)v^{p^j}; fixing every vector forces the field map trivial and A/a=1. Thus Q=G/U acts faithfully on U. It normalizes the irreducible r-action, so Q≤ΓL1(p^D). Its Sylow-r subgroup R is unique and characteristic because r>D. A normal p-subgroup centralizes R and lies in its p′ scalar centralizer; hence O_p(Q)=1 and U=O_p(G) is characteristic. Canonical τ descends to Q.

The reviewed characteristic-cyclic inversion obstruction makes Q/C_Q(R) have exponent at most two. Frobenius acts faithfully on R with order D, so Q has Frobenius image of order at most two. If it is trivial, Q is cyclic and G is metabelian; the preceding all-parity metabelian LMlt exclusion, independently accepted at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`, rules this out. In particular all odd f end here.

Suppose D even and the Frobenius image has order two. Put h=D/2 and T=Q∩F_(p^D)×. The image is generated by Frobenius p^h. The degree divisibility forces the entire odd part of p^D−1 into T: U is a p-group, the odd part of the degree is divisible by the odd part of q³−1, and Q/T has order two. Thus B=O_(2′)(F_(p^h)×) lies in T. It is nontrivial because h is a positive multiple of three and the odd number p²+p+1>1 divides p^h−1. The commutator [Q,Q] lies in the norm-one torus of order p^h+1; its intersection with B is trivial because gcd(p^h−1,p^h+1) divides two. Thus B embeds in Q_ab.

The characteristic R and its irreducible action force τ|U to be a scalar times Frobenius p^j. Since τ²=1, j=0 or h. Either possibility fixes B pointwise. But τ induces inversion on Q_ab because it inverts the generating canonical section. Its action on the embedded nontrivial odd B is therefore both identity and inversion, contradiction.

### Exceptional case q=4

Here p=2,f=2 and U≅F4³ is 6-dimensional over F2. The degree is divisible by 16·63. Since |Out(S)| divides4, 63 divides |G∩S|; also N=(G∩S)∩U is nonzero. In (G∩S)/N≤63:3, its intersection with the scalar C63 has order divisible by 21, so contains C7 and C3. The C3 acts on U as F4× scalars: for a scalar b on the GL3 block, the parabolic action on U is b⁴=b. Hence N is F4-linear. C7 is irreducible on F4³, so N=U. This crucial F4-linearity step is needed because C7 is reducible on the 6-dimensional F2-space. The step was independently suggested in preliminary discussion by a research reviewer; it is not a recorded exact-source review.

The inner p-core argument above gives U◁G. The fixed line/dual hyperplane and faithful-action argument exclude graph automorphisms and embed Q=G/U in ΓL3(4). The C7 action is irreducible over F4, so its normalizer gives Q≤ΓL1(64). The scalar subgroup T contains the unique normal C7. The degree's 3² factor implies T also contains C3, because the Frobenius quotient has order6 and contributes at most one factor3.

Before descending τ to Q, O2(Q)=1: a normal 2-subgroup centralizes both normal scalar C7 and scalar C3. A Frobenius exponent centralizing C7 is 0 or 3 modulo6; exponent3 inverts C3 and is excluded. The scalar kernel has odd order. Hence U=O2(G) is characteristic and τ descends.

The characteristic cyclic C7 of Q gives an exponent-at-most-two action of Q on it. Frobenius has order3 on C7, so Q/T has order at most two and its nontrivial element has field exponent3. The degree now forces the whole odd scalar group T=F64×, order63, into Q. The unique Sylow3 subgroup C9 of Q is characteristic and acts irreducibly on U over F2, since ord9(2)=6. Thus τ|U is scalar times Frobenius 2^j, and τ²=1 forces j=0 or3. Both fix C7 pointwise. The commutator [Q,Q] lies in the norm-one subgroup of order9, so C7 embeds in Q_ab. Canonical inversion on Q_ab contradicts pointwise fixation of this nontrivial odd subgroup.

This closes the row for all q, conditional on the canonical, Li–Xia, natural-module normalizer, primitive-prime and all-parity metabelian inputs. The abstract even-f affine semidirect group F_(p^D)^+⋊C_r with τ acting by Frobenius p^(D/2) on U and inversion on C_r remains a control for the inverse-module obstruction: its inverted elements generate it, but it lacks the full odd-torus divisibility and actual-folder hypotheses used above. The complete deduction has the exact-source independent reviews below.

The full automorphism description and source-access limits are the Kleidman–Liebeck inputs cited in the preceding Singer section; the present proof uses the natural projective Levi action on U and its field normalizer. The generic fixed-subfield argument received a preliminary scratch check by a research reviewer; a research reviewer independently supplied the q=4 scalar-linearity repair. Those development checks do not replace an exact-source review of this complete deduction. No computation is used.

### Independent review of the all-parity PSL4 row

automated-model reviewer A, reviewer B and reviewer C independently accepted the complete row-2 deduction at exact source `f58660c5f48adf6d9cd3953c89680ca1de095a22`. All checked the primitive-prime radical forcing, full group and graph interface, characteristic p-core before descending τ, even-field-exponent fixed-subfield obstruction, and the entire q=4 repair in its stated order. In particular no F₂-irreducibility of C7 is used at q=4: scalar C3 first forces F4-linearity, and the 2-core is proved trivial before quotient inversion. The acceptances retain the cited canonical, Li–Xia, normalizer, primitive-prime and independently reviewed metabelian inputs. The reviewers retained their earlier Li–Xia source inspections; reviewer B retained the source authors's cached Kleidman–Liebeck inspection after its fresh preview fetch timed out. No reviewer ran a computation or reproved the external classifications. The scope is this actual row for all q and both parities, not arbitrary PSL4 actions or the remaining classification.

## Proposed all-parameter exclusion of the even-characteristic symplectic rows

**Conditional deduction with three independent reviews below.** Continue [0323-finite-simple-non-moufang-bol-loops:C0010](../foundations/research-C0010.md). Let X be a finite simple nonassociative left Bol loop, G=LMlt(X), H=G₁, M=Mlt(X), I=M₁ and S=Soc(M). Assume the canonical C0001/C0007 section and inversion interfaces, the independently reviewed C0008 primitive almost-simple full-group conclusion, and that the actual factorization M=GI, with G solvable, satisfies [Li–Xia arXiv:1408.0350v3](../foundations/references.md#lx16-solvable-factor), Theorem 1.1(d), Table 1.1 row 3 or 4. Then these rows are impossible for every permitted q=2^f and rank, under the geometric and reviewed refinement inputs specified below. This neither assumes primitive G nor classifies other actions of the same abstract socle.

### The actual full action for q≥4

In row 3, S=Sp_(2m)(q), m≥2, and J=I∩S normally contains the displayed J₀=Ω⁻_(2m)(q). In row 4, S=Sp4(q) and J₀=Sp2(q²). Their natural normalizers N=N_S(J₀) are respectively O⁻_(2m)(q) and Sp2(q²).2, with N/J₀ of order two. The [natural normalizer argument](odd-envelope-parameterization.md#proposed-parity-exclusion-for-four-classical-rows), independently reviewed at `b8c237d84f001b9a3d70ab725adab6b67e57c05b`, supplies these facts, including the actual embeddings. Here J₀ is nonabelian simple and perfect (for m=2 it is PSL2(q²)). Thus J₀≤J≤N implies J′=J₀. Since I normalizes J, it normalizes J₀ and N. Also N′=J₀, so N_S(N)=N_S(J₀)=N; no maximal-subgroup assertion about N is needed for this equality.

The subgroup N_M(N) is proper, since otherwise the proper nontrivial N would be normal in simple S. Primitivity makes I maximal in M, so I=N_M(N) and I∩S=N. The actual S-set is therefore S/N. Its S-centralizer in the symmetric group is N_S(N)/N=1. Consequently the action of M is determined by its automorphisms of S, and belongs to the Aut(S)-stabilizer of the S-conjugacy class of N. This identifies the full multiplication action, rather than just an abstract point stabilizer.

For row 3 and m≥3, the standard classical automorphism description gives only field outer automorphisms; these act naturally semilinearly on the minus-type quadratic refinements. For m=2, choose the exceptional graph representative γ. Its square generates the field subgroup and Out(Sp4(2^f)) is cyclic of order 2f; see [Aschbacher–Seitz (19.3), pp.76–77](../foundations/references.md#as76-symplectic-outer). In particular γ need not be an involution. Li–Xia v3 Remark (ii), p.6, and the row-4 construction in Lemma 7.22, p.70, give its exchange of the minus-orthogonal and extension-field normalizer classes. We use that exchange, not the latter proof's order-two wording.

The two S-classes are distinct: SL2(q²) is transitive on the nonzero vectors of its natural four-dimensional Fq-module, whereas a nondegenerate minus quadratic form in dimension four has both singular and nonsingular nonzero vectors. Thus this extension-field subgroup cannot preserve such a form. Field automorphisms preserve each class, so even powers of γ preserve them and odd powers exchange them. The class stabilizer of the row-3 N is exactly the natural semilinear symplectic group. For row 4, transport the entire triple (M,I,S) by γ to the row-3 class; this transports its outer action as well. The resulting permutation action is the natural semilinear action on minus refinements.

The [all-field refinement exclusion](../primitive-completion/symplectic-refinement-all-fields.md), independently accepted at `13e21094894aed868a16d7859db036ca7cfc1a69`, excludes every left Bol loop with full multiplication group contained in that action for q≥4,m≥2. Its inputs are the general Δ₀ argument at `20ba07f5536f13153a074d7dc70ec54b8dd3f6dd`, the q=4 local exclusion at `a02c94ee44243d7ab1efff303dc49198b62844ef`, and Baumeister–Stein arXiv:0908.2597v2 Corollary 3.6, with the exact review scopes in that manuscript. This closes both rows for q≥4, conditionally on those reviewed inputs and their CFSG-dependent source theorem.

### The separate q=2 argument

Row 4 at q=2 has nonsimple Sp4(2), outside the socle hypothesis. In row 3, m≥3 and S=Sp_(2m)(2) has no outer automorphisms, so M=S. The table gives

    G ≤ U:(2^m−1):m,       I ▷ Ω⁻_(2m)(2),

where U is the elementary abelian radical of the natural Siegel parabolic. The preceding reviewed normalizer calculation gives

    d=2^(m−1)(2^m−1) dividing |X|=[S:I]=[G:H].

Only divisibility is used. Set A=G∩U and D=G/A≤C_(2^m−1):C_m. The degree has 2-part at least 2^(m−1)>m₂, while the scalar torus is odd, so A is nonzero and elementary abelian.

For m≠6, the primitive-prime theorem gives r with ord_r(2)=m and r>m. It divides d and |D|; the unique Sylow-r subgroup R of D is cyclic and lies in the scalar torus. Any normal 2-subgroup of D centralizes R, while its centralizer in C_(2^m−1):C_m is the odd scalar torus. Hence O₂(D)=1 and A=O₂(G) is characteristic. The canonical τ therefore descends to D. The [cyclic-normal inversion obstruction](odd-envelope-parameterization.md#proposed-characteristic-section-inversion-obstructions), reviewed at `e35278d2d2c6abe0919450a825917ee2560e8818`, makes D/C_D(R) have exponent at most two. The field C_m acts faithfully on R, so D's field image has order at most two. Since the full odd number 2^m−1 divides |D|, its scalar intersection is the entire T=C_(2^m−1). If the field image is trivial, G is an extension of abelian A by cyclic D and is metabelian, contrary to the preceding all-parity theorem reviewed at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`. Otherwise m=2h and D/T has order two, acting on T by 2^h.

For m=6, D≤C63:C6 and 63 divides |D|. The scalar intersection contains C7 and C3, because the field quotient contributes at most one factor of three. Both scalar subgroups are normal in D. A normal 2-subgroup centralizes both: a field exponent centralizing C7 is 0 or 3 modulo six, and exponent 3 inverts C3. Thus its field exponent is zero and its odd scalar kernel has trivial 2-part. Again O₂(D)=1 and A=O₂(G) is characteristic before τ descends. The unique Sylow7 subgroup is characteristic in D; cyclic-normal inversion kills the field action of order three on it. Hence the field image has order at most two, degree divisibility forces the full scalar T=C63, and the scalar-only case is metabelian and excluded. The remaining case is exactly the preceding field-half action.

In every surviving case m=2h≥4. A lift of the nontrivial D/T element generates D together with T; hence D′=[T,D] is the norm-one subgroup of T of order 2^h+1. The subgroup B=C_(2^h−1) injects into D_ab, since gcd(2^h−1,2^h+1)=1, and B is nontrivial. Meanwhile A is a 2-group and D/T has order two, so the odd part of |G| is exactly |T|. Because d divides |X| and |X| divides |G|, H is a 2-group.

For any finite simple nonassociative loop the quotient-to-group argument above gives G=HG′. Explicitly HG′ is normal and x↦L_x HG′ is a loop homomorphism into the abelian group G/HG′, since L_(xy)^(-1)L_xL_y∈H. Its image generates the quotient; simplicity and nonassociativity make it trivial. Thus H surjects onto every abelian quotient of G, including D_ab. A 2-group cannot surject onto the abelian group D_ab containing the nontrivial odd B. This contradiction closes every m≥3, including the exceptional m=6. It uses neither a module-weight computation nor a quotient loop.

The q=2 minus-refinement action is 2-transitive, not rank three; C0017 is not invoked. The two q-ranges use different obstructions and retain their separate inputs. This assembly received proof-development contributions from a research reviewer and a research reviewer; these are distinct from the independent exact-source acceptances below. The source authors directly inspected the Aschbacher–Seitz outer-automorphism statement and the Li–Xia graph-exchange passage. The original classifications remain cited inputs. No computation, novelty assertion, or completion of C0010 is claimed.
### Independent review of the even-characteristic symplectic rows

automated-model reviewer A, reviewer B and reviewer C independently accepted the complete rows 3–4 deduction at exact source `bdbc638eb788af4ddd1d5dafcdaeeb7304aced23`. They checked the actual full-action identification, perfect characteristic subgroup and self-normalizer steps, graph-class exchange with graph square in the field subgroup, and the separate q=2 proof, including m=6 and characteristic O₂ before τ descent. reviewer A independently inspected Li–Xia Theorem 1.1/Table 1.1, Remark (ii), Lemma 7.22, and Aschbacher–Seitz (19.3), pp.76–77. The other two retained these as stated source inputs; reviewer B explicitly did not freshly inspect the Aschbacher–Seitz PDF. All retain the separately reviewed normalizer, refinement and metabelian deductions and their original dependencies. None reproved the external classifications or ran a computation. The acceptance concerns these two actual factorization rows, not the unrestricted classification or aggregate C0010.

## Proposed odd-characteristic PSp4 row exclusion

**Conditional deduction with three independent reviews below.** Continue [C0010](../foundations/research-C0010.md) with X finite simple nonassociative left Bol, G=LMlt(X), M=Mlt(X), I=M₁ and S=Soc(M). Suppose the actual factorization M=GI lies in Li–Xia arXiv:1408.0350v3, Theorem 1.1(d), Table 1.1 row 5: S=PSp4(q), q odd, and J=I∩S normally contains its indicated J₀=PSL2(q²). Under C0008 and the natural group/action inputs below, this row is impossible for every odd q≥3, with no parity assumption on X.

The [reviewed natural normalizer calculation](odd-envelope-parameterization.md#proposed-parity-exclusion-for-four-classical-rows) at `b8c237d84f001b9a3d70ab725adab6b67e57c05b` gives N=N_S(J₀)=J₀.2 and index q²(q²−1)/2. Since J₀ is perfect, including q=3 where J₀=A6, both J′ and N′ equal J₀. As above, I normalizes N, N_S(N)=N, and maximality of I forces I=N_M(N) and J=N. Hence the actual S-action is S/N and its symmetric-group centralizer is trivial.

Under the B₂=C₂ identification S≅PΩ5(q), this N is the stabilizer of a nonsingular minus-type point, with embedded Ω4⁻(q) as its perfect subgroup J₀. Li–Xia v3 Proposition 5.7 and the row-5 construction in Lemma 7.22, printed p.70, explicitly use these identifications. The full abstract automorphism statement is Kleidman–Liebeck, §2.1, Theorems 2.1.3–2.1.4, printed p.16, applied in the **symplectic dimension-four model**, not to an orthogonal model below that theorem's dimension threshold. For odd q it gives all automorphisms as projective semilinear symplectic similarities, including q=3; the exceptional symplectic graph automorphism occurs only in even characteristic.

These similarities transport to semilinear orthogonal similarities on the five-dimensional model: in ∧²(Fq⁴), the wedge-product quadratic form is nondegenerate, and the symplectic form determines a nondegenerate invariant line. Its perpendicular has dimension five. A symplectic similarity preserves this decomposition, and its exterior square acts by an orthogonal similarity on that perpendicular. The classical B₂=C₂ identification is precisely this projective action. Thus every automorphism stabilizing the conjugacy class of N is realized on its natural minus-point set. The trivial S-centralizer identifies the full actual M-action with the corresponding subgroup of that semilinear point action.

The revised [odd-dimensional perpendicular-displacement proof](../foundations/C0016.md#odd-orthogonal-perpendicular-all-fields) rules out every loop in this natural action, conditional on C0008's UOD lemma. Its direct Witt-basis argument covers q=3 as well as every larger odd field and uses no finite rank certificate. It is a separately reviewed subpart of the still-partial C0016; its exact-source review together with this bridge is recorded below. This proves the row exclusion under the stated source inputs. The primary automorphism and Li–Xia statements were directly inspected by preliminary contributor a research reviewer; the exterior-square transport is the local interpretation given here. No aggregate C0016 promotion or unrelated action exclusion is asserted.

## Proposed all-field unitary row exclusion

**Conditional deduction with three independent reviews below.** In the same finite-simple-nonassociative setting, suppose M=GI lies in Li–Xia v3 Table 1.1 row 6: S=PSU_d(q), d=2m≥4, and J=I∩S normally contains the natural image J₀ of SU_(d−1)(q). Under C0008, the reviewed unitary natural-action theorem and the q=2 rank-three input below, this row is impossible for every q≥2. The proof uses the actual full multiplication action; it does not require G to act primitively.

Let P be the S-stabilizer of the nonsingular line fixed by J₀. Its perpendicular is an irreducible SU_(d−1)(q)-module, including SU3(2). An elementary verification works in an orthonormal basis: the determinant-one norm-one diagonal group has pairwise distinct coordinate characters for n=d−1≥3 and q+1≥3. Its order is coprime to the characteristic and all its characters split over F_(q²), so every invariant subspace is a coordinate sum. The even permutation matrices belong to SU_n(q) and act transitively on coordinates, proving irreducibility. Thus J₀ has just one invariant projective line in the full d-space. Its normalizer preserves that line, giving J₀≤J≤P, as in the reviewed natural-normalizer argument at `b8c237d84f001b9a3d70ab725adab6b67e57c05b`.

The quotient P/J₀ is cyclic, by determinant on the perpendicular unitary space followed by projectivization. Hence P normalizes every intermediate subgroup J. On the other hand N_M(J) is proper, since otherwise 1<J<S would be normal in simple S. Since I≤N_M(J) and I is maximal, N_M(J)=I, so N_S(J)=J. Therefore P≤J and J=P. This avoids any assertion that SU3(2) is perfect or that J₀ is characteristic in J.

The actual S-set is now the nonsingular-point set S/P, with trivial symmetric-group centralizer N_S(P)/P. Kleidman–Liebeck §2.1, Table 2.1.B and Theorems 2.1.3–2.1.4, pp.15–16, give the full unitary automorphism group as the natural projective semilinear unitary group in these dimensions and fields, including PSU4(2). In the unitary model inverse transpose is realized by field conjugation. Thus the full actual M acts inside PΓU_d(q) on these points. This extends the [reviewed classical point-action interface](../primitive-completion/classical-point-normalizers.md) to q=2 by the same automorphism and centralizer argument, rather than silently invoking its written q≥3 scope.

For q≥3 the [unitary nonorthogonal exclusion](../primitive-completion/unitary-nonorthogonal.md), independently reviewed at `13e21094894aed868a16d7859db036ca7cfc1a69`, already excludes every loop in this natural action. Its C0008 and Hermitian-space inputs and exact review scope are retained.

For q=2, the S-action has rank three in every even dimension d≥4. Normalize representatives of nonsingular points to norm one. An orthogonal ordered pair has fixed Gram matrix; a nonorthogonal ordered pair can be scaled to have Hermitian product one and also has fixed Gram matrix. Witt extension gives unitary transitivity in each case. It also gives **special** unitary transitivity: adjust the determinant of the extension on a nonsingular line in the common perpendicular, fixing the pair. For an orthogonal pair that perpendicular is nondegenerate of dimension d−2≥2; for a nonorthogonal pair it has radical of dimension one and nondegenerate quotient of dimension d−3≥1, so such a line exists in both cases. Every norm-one determinant is available on it. Both nontrivial orbits occur. Semilinear overgroups preserve orthogonality, so the actual M has the same rank three.

The point degree and orthogonal subdegree are respectively

    n=2^(d−1)(2^d−1)/3,       a=2^(d−2)(2^(d−1)+1)/3.

For example they give subdegrees 1,12,27 when d=4. These counts follow by using an orthonormal basis over F4: the norm is the parity of the number of nonzero coordinates, so the number of norm-one vectors in dimension k is (4^k−(−2)^k)/2, and each line has three representatives. The reviewed [C0017 rank-three theorem](../../claims/0017.md), with its CFSG and scoped dependency qualifications, leaves only the Paige loops M(2) and M(3), of orders 120 and 1080. Neither equals n: d=4 gives 40; for d≥6, n has 2-part 2^(d−1)≥32, whereas both Paige orders have 2-part eight. This rules out q=2 without a separate appeal to the degree-40 certificate or to the aggregate C0016.

The actual-action bridge and q=2 route were developed with a research reviewer. The classification, automorphism and reviewed natural-action/rank-three theorems remain stated inputs; this does not reprove them. No computation is used. The row-6 assembly has the exact-source independent reviews below, and C0010 remains open.

### Independent review of the odd PSp4 and unitary rows

automated-model reviewer A, reviewer B and reviewer C independently accepted the revised C0016 §3(2) perpendicular proof and both row-5 and row-6 deductions at exact source `67fcd25724552c730ecb9d94ede1a0c9ee06dcf5`. All checked the all-odd-field Witt-basis proof, including q=3, semilinearity without a similarity assumption, the actual-action normalizer arguments and odd-characteristic exterior-square transport, the unitary monomial irreducibility argument including SU3(2), and the special-unitary pair-orbit determinant adjustment and Paige-order contradiction at q=2. reviewer A retained direct Li–Xia row-5/row-6 and Lemma 7.22 inspections from the preceding review session. None freshly inspected Kleidman–Liebeck in this review; its precise primary-source check by the preliminary contributor remains recorded above. The other two retained the stated external source interfaces. All retain the specifically used C0008, C0017 and earlier unitary natural-action inputs; none reproved the external classifications, ran a computation or accepted aggregate C0016. C0010 remains open.

## Proposed completion of the infinite classical solvable-factor table

**Conditional deduction with three independent reviews below.** Let X be a finite simple nonassociative left Bol loop with solvable G=LMlt(X), and use M=Mlt(X), I=M₁ and S=Soc(M). Under C0008 and the source and reviewed geometric inputs below, an actual factorization M=GI in Li–Xia arXiv:1408.0350v3 Table 1.1 rows 7–9 is impossible in rows 7 and 8, while row 9 forces X≅M(q), the Paige loop. In particular none of these rows supports a simple proper Bol loop. Combined with the preceding reviewed deductions, this removes the whole Table 1.1 from the proper-loop solvable-G frontier. It leaves Table 1.2, the other alternatives of Li–Xia Theorem 1.1, and nonsolvable G outside this assertion.

### Recovering the actual point action

Put J=I∩S. Here 1<J<S and J is normal in I. Since N_M(J) is proper (otherwise J would be normal in simple S), maximality of the primitive point stabilizer gives N_M(J)=I and therefore N_S(J)=J. Li–Xia v3 Remark (ii) after Theorem 1.1, printed p.6, supplies the sharper uniform statement that, up to a graph automorphism of S, **N_S(J)** is the indicated nonsingular-point stabilizer. We use that assertion about the actual J, not merely its displayed normal subgroup. Thus J itself is that point stabilizer after the same transport.

Conjugate the entire abstract pair (M,I), inside Aut(S), by the indicated automorphism and transport its coset action. This is a permutation isomorphism of the actual action on X. In row 7 the resulting S-set is the minus-complement nonsingular-point action of Ω_(2m+1)(q), m≥3 and q odd. In row 8 it is a nonsingular-point orbit of PΩ⁺_(2m)(q), m≥5. In row 9 it is the corresponding orbit of PΩ8⁺(q), with the graph transport allowing triality. No assertion that all triality automorphisms preserve a chosen point class is made, nor any count of only three classes in odd characteristic. The trivial centralizer N_S(J)/J identifies actual extensions whenever the natural automorphism interface is used below.

### Row 7

Kleidman–Liebeck §2.1, Table 2.1.B and Theorems 2.1.3–2.1.4, pp.15–16, give all abstract automorphisms of the odd-characteristic type-B group in dimension 2m+1≥7 as projective semilinear orthogonal similarities. There is no D4 triality case here. A natural nonsingular point stabilizer fixes its line uniquely: its embedded Ω⁻_(2m)(q) acts irreducibly on the nondegenerate perpendicular complement and has no invariant line there. Hence an automorphism whose image of J is S-conjugate to J preserves that natural point orbit. The actual full M-action lies in its semilinear orbit stabilizer, by the trivial-centralizer argument.

The [odd-dimensional perpendicular lemma and loop consequence](../foundations/C0016.md#odd-orthogonal-perpendicular-all-fields), with three independent acceptances at `67fcd25724552c730ecb9d94ede1a0c9ee06dcf5`, exclude this action for every odd q, including q=3. Its finite-field/Witt and C0008 UOD inputs remain explicit; the argument does not require rank three. Thus row 7 is impossible.

### Rows 8 and 9 for q≥4

The [classical nonsingular-point interface](../primitive-completion/classical-point-normalizers.md), independently reviewed with its source update at `698ce5f6d50e7186f205a63f4a2c413145775915`, identifies the full primitive almost-simple action with the setwise stabilizer of the selected point orbit in PΓGO. This includes the dimension-eight triality qualification and distinguishes the two norm types in odd characteristic. Its q-ranges are even q≥4 and odd q≥5, exactly the ranges now used.

Apply the [odd and even semilinear orthogonal collapse theorems](../primitive-completion/orthogonal-odd-linear.md), reviewed respectively at `422cbf355aca69cc71a290176176f4169dcbd18e` and `037cec7af0c10f7daf3172c0dd06e065be868c7b`, with their composition-algebra and finite-field inputs. Any loop in these natural actions has dimension eight, plus type, and is M(q). This is impossible in row 8, whose dimension is at least ten, and gives exactly the asserted necessary Paige conclusion in row 9. It is not an existence assertion for every solvable-factor containment in the source table.

### Small fields: the actual socle and all overgroups

For q=2 or 3, put dim V=2m and take the plus-type nonsingular-point action, with m≥4 here. It has rank three already under S=PΩ⁺_(2m)(q). We give the socle orbit argument, so no claim about an outer graph group is substituted for the socle.

For q=2 normalize the identity vector e by Q(e)=1. Witt extension shows that O(V)_e is transitive separately on the points with B(e,y)=1 and on those with B(e,y)=0, y≠e. The stabilizer of e,y contains an element of nontrivial Dickson invariant: when B(e,y)=0, use the orthogonal symmetry centered at the nonsingular e; when B(e,y)=1, use one centered at a nonsingular vector in the nondegenerate (2m−2)-dimensional perpendicular of ⟨e,y⟩. Composing an extension with that symmetry if needed places it in Ω(V)_e. Both orbits are nonempty. In e⊥ the polar radical is ⟨e⟩ and each coset modulo e has exactly one norm-one vector, since Q(y+e)=Q(y)+1. Hence the degree and two nontrivial subdegrees are

    n₂=2^(m−1)(2^m−1),
    a₂=2^(2m−2)−1,       b₂=2^(2m−2)−2^(m−1).

For q=3 rescale Q so that Q(e)=1. Its type remains plus in even dimension. Represent a point by ±(te+z), z∈W=e⊥ and Q(z)=1−t². The subgroup Ω(W) fixing e is transitive on nonzero singular vectors of W and on each nonzero norm level. Indeed Witt extension gives an orthogonal map; its determinant and spinor norm can both be adjusted in the target-vector stabilizer, which contains reflections of both norm square classes. For a nonsingular vector its perpendicular has even dimension at least six; for a singular vector the radical can be split off leaving a nondegenerate subspace of dimension at least five. These spaces contain a hyperbolic plane and represent both square classes. Their reflections supply all determinant/spinor pairs. Thus extension can be taken in Ω(W).

At t=±1, projective negation permits the unique representative e+z, giving the identity and one orbit of nonzero singular z. At t=0 there is the other orbit of norm-one projective points in W. Consequently

    n₃=3^(m−1)(3^m−1)/2,
    a₃=3^(2m−2)−1,       b₃=3^(m−1)(3^(m−1)−1)/2.

The degree formulas are the standard plus-type quadratic norm-level counts, and the singular-vector count in odd dimension 2m−1 is 3^(2m−2)−1. These same counts and Witt/Dickson/spinor mechanisms underlie [C0009 Theorem 2.1(1)](../foundations/C0009.md), but the present general-rank derivation and full-extension argument require their own review. No assertion that −I belongs to Ω(V) for every m is used. For m=4 the pairs are (63,56) and (728,351), respectively.

In each field the two nontrivial subdegrees are unequal. Since I normalizes J=S_e, its permutations of the J-orbits preserve their sizes, so it cannot fuse them. Thus the actual full M also has rank three, without any small-field full-automorphism identification. The reviewed [C0017 theorem](../../claims/0017.md), retaining its CFSG and scoped dependencies, forces X=M(2) or M(3). Among these point degrees the match occurs only at m=4: n₂ has 2-part 2^(m−1), whereas both Paige orders 120 and 1080 have 2-part eight, so m=4 and n₂=120. For q=3, n₃ is strictly increasing and n₃≥9801 at m≥5, while m=4 gives 1080. Therefore row 8 has no possible degree, and row 9 gives M(2) or M(3) in its corresponding field.

This completes the proposed rows 7–9 assembly under the stated natural-action, automorphism, Witt/spinor/Dickson, composition-algebra and C0017 inputs. Proof-development contributions came from a research reviewer and a research reviewer. The source authors directly inspected the Li–Xia uniform normalizer statement; its graph transport is used only as a transport of the actual action. No finite computation is required by this proof. Independent exact-source reviews are recorded below; C0010 remains open and C0016 remains partial.

### Independent review of the infinite-table completion

automated-model reviewer A, reviewer B and reviewer C independently accepted the rows 7–9 assembly at exact source `93cab1c81aaab8988d79e207e2f0bd071d825600`. All checked self-normalization of the actual J, transport of the entire pair and permutation action, the row-7 and q≥4 geometric interfaces, and the direct small-field socle orbit arguments with Dickson/determinant/spinor adjustments. They also checked unequal-subdegree nonfusion and the Paige degree comparison, without assuming −I∈Ω in every rank or invoking a small-field full-automorphism classification. reviewer A retained its earlier direct Li–Xia Remark (ii) and Table 1.1 inspection; the others retained that stated source interface, and none freshly inspected Kleidman–Liebeck in this review. The cited C0008/C0017 and separately reviewed geometric collapse results remain inputs, not newly reproved external classifications. No computation was run. Together with the earlier row reviews this excludes simple proper loops in the stated infinite classical solvable-factor table, while leaving the other factorization alternatives and C0010 open.

## Proposed finite-table exclusions from orders and rank

**Conditional deductions with three independent reviews below.** Retain finite simple nonassociative left Bol X, solvable G=LMlt(X), full M=Mlt(X), I=M₁, S=Soc(M), and the C0008 and canonical inputs. For Li–Xia arXiv:1408.0350v3 Table 1.2, the following arguments exclude rows 2, 7, 8, 12–15, 17 and 19, and the PSL3(3)-stabilizer alternative of row 6, at either parity. They do not classify the remaining finite-table actions. The row-6 point-parabolic alternative of degree 40 remains open here.

### Row 2 and the impossible row-6 alternative

In row 2, S=PSL2(16), |X|=68 and G₀=G∩S≤D34. The outer group has order four, so |G| divides 136. Transitivity forces 17 to divide |G₀|. Its unique Sylow17 subgroup C is characteristic in G₀ and normal in G. Then G/C is a 2-group of order at most eight; its derived subgroup has order at most two. Since Aut(C) is abelian, G′ centralizes C, and G′/(G′∩C) is cyclic of order at most two. A group with central subgroup and cyclic quotient is abelian, so G′ is abelian. The all-parity metabelian exclusion reviewed at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a` gives the contradiction. No embedding identification is needed beyond the source containment.

In row 6, S=PSL4(3) and the displayed bound for G₀ is 2⁴:5:4, of order 320. Since |Out(S)|=4, |G| divides 1280 and is coprime to three. The alternative J=I∩S=PSL3(3) has degree 1080, divisible by 27, contradicting transitivity. This excludes that alternative without identifying it as a Levi or flag stabilizer. The other table alternative J=3³:PSL3(3), of index 40, is not excluded by this argument; its rank-two projective action is not by itself an obstruction.

### Reusing the PSL4 and PSp4 arguments

Rows 7 and 8 have S=PSL4(3) and PSL4(4), respectively, with exactly the same parabolic bounds on G₀ as the [all-field PSL4 argument](#proposed-all-parity-exclusion-of-the-psl4-symplectic-factor-row), reviewed at `f58660c5f48adf6d9cd3953c89680ca1de095a22`. That proof uses its stabilizer hypothesis only to obtain the degree divisibility; every subsequent step uses the stated parabolic embedding, that divisibility, outer automorphisms and the canonical inversion/metabelian inputs. Here the actual degrees are

    2106=18·117,       24192=24·1008,

and 117=3²(3³−1)/2, 1008=4²(4³−1). Thus both required divisibilities hold. The entire subsequent proof applies, including the q=4 scalar-linearity and characteristic-core repair. This is a reuse of the inspected proof under precisely its used hypotheses, not an assertion that these stabilizers are symplectic subgroups.

For rows 12–15, q is respectively 5,7,11,23, S=PSp4(q), and J is PSL2(q²) or its displayed extension of order two. The [odd-characteristic PSp4 proof](#proposed-odd-characteristic-psp4-row-exclusion), reviewed at `67fcd25724552c730ecb9d94ede1a0c9ee06dcf5`, uses no particular bound on G₀ after the naturally embedded J₀=PSL2(q²) is normal in J. The same source embeddings and natural normalizer apply here. Its characteristic-subgroup, maximality, full exterior-square action and perpendicular-displacement arguments therefore exclude these rows as well, even though their displayed solvable factors differ.

### Row 17 by regularity

Here S=PSp6(3), J=PSL2(27):3, and

    |S|=4,585,351,680,       |J|=9,828·3=29,484,
    |X|=[S:J]=155,520.

The source bound is G₀≤3₊^(1+4):2^(1+4).D10, of order 3⁵·2⁵·10=77,760. Here D10 has order **ten**, in Li–Xia's notation, not twenty. Its precise row determination also appears in v3 Lemma 7.6(c), printed p.55, whose source computation is retained as an external input. Since |Out(S)|=2, |G|≤155,520. Transitivity gives the reverse inequality, so G is regular. A loop with regular left multiplication group is associative: the products L_x L_y and L_(xy) take its identity to the same point and must agree, giving the group law. This contradicts the nonassociative hypothesis. No radical or inversion calculation is needed.

### Row 19, including all A7 classes

Here S=PSU3(5), |S|=126000 and J=A7 has order 2520, giving degree 50. There are three S-conjugacy classes of such subgroups; one must not assume a single class or an unproved outer fusion. The [pinned GAP/CTblLib certificate](../code/verify_u35_a7_rank.g) treats all three using GAP 4.15.1 and CTblLib 1.3.11. It checks the complete eight-entry maximal-subgroup metadata and that no other listed maximal group has order divisible by 2520. Thus, conditional on that complete ATLAS/CTblLib class list, every A7 subgroup is in one of the three displayed classes. The script requires each distinct stored fusion map, explicitly induces its trivial character to S, and checks degree 50 and inner product three with itself. For the coset permutation character π=1_J^S, the standard orbit-count identity ⟨π,π⟩ equals the number of S-orbits on ordered pairs. Hence each actual socle action has rank three.

The two nontrivial socle subdegrees sum to 49 and are therefore unequal. The actual I normalizes J and permutes its orbits preserving sizes, so it cannot fuse them. Consequently M has rank three, for every one of the three classes and every allowable outer extension. C0017, with its reviewed CFSG-dependent scope, leaves only Paige orders 120 and 1080, not 50. This gives the proposed exclusion. The certificate establishes finite permutation-character ranks from pinned data; the overgroup and loop deductions are the mathematical argument above. It neither enumerates loops nor independently constructs the ATLAS subgroup classification or stored fusions. The source authors read and ran the exact committed script successfully; the independent proof/code reviews and runs are recorded below.

The primary and dataset locators are in [REFERENCES](../foundations/references.md). In a separate arithmetic audit of all displayed Table 1.2 stabilizers, a research reviewer found the row-22 transcription 108 should be 1080: |Ω7(3)|=4,585,351,680 and |G2(3)|=4,245,696. The source authors checked the order formulas and corrected the [odd finite-table degree list](odd-envelope-parameterization.md#proposed-finite-classical-table-reduction). Its previous odd-order exclusion used only evenness, so its conclusion is unchanged. This does not itself exclude row 22 for even-order loops.

Proof-development contributions for these finite cases came from a research reviewer, a research reviewer and a research reviewer. Their scratch work is distinct from independent exact-source acceptance. The remaining finite rows and the general classification are open; no parity filter, table bound, or computation is being promoted to an unproved exhaustive loop classification.

### Independent review of the finite-table batch

automated-model reviewer A, reviewer B and reviewer C independently accepted the stated finite-table exclusions, source/code interfaces and row-22 correction at exact source `e4eb963d4091f8e3daa5554f3f45b6d610b552a8`. Each read the exact committed `verify_u35_a7_rank.g`, extracted it unchanged to a temporary path, and ran it under its asserted GAP 4.15.1 and CTblLib 1.3.11 versions. All three runs reported index 50 and rank three for `A7`, `U3(5)M2` and `U3(5)M3`. They checked the complete maximal-list coverage and stored-fusion induction logic, odd-sum nonfusion, prior-proof hypothesis reuse, and the degree/order arguments including D10 of order ten. reviewer A freshly inspected Li–Xia Table 1.2 and the CTblLib online subgroup metadata; the others retained the stated source interfaces. The maximal-subgroup classification, stored character/fusion correctness, and prior C0017 and geometric theorems remain external inputs, not established by these runs. The degree-40 row-6 alternative and the other finite rows remain open. This is model mathematical and code review, not formal verification or GitHub approval.


## Proposed all-class rank-three finite orthogonal exclusions

**Conditional deduction with three independent reviews below.** Continue 0323-finite-simple-non-moufang-bol-loops:C0010 with finite simple nonassociative left Bol X, solvable G=LMlt(X), primitive almost-simple M=Mlt(X), I=M₁ and S=Soc(M). Under C0008, C0017 and the finite subgroup/character inputs below, Li–Xia arXiv:1408.0350v3 Table 1.2 row 22 is impossible; rows 25 and 27 permit only the Paige conclusions M(2) and M(3), respectively. In particular all three rows are excluded for proper Bol loops. The statement concerns every displayed subgroup class and every actual outer extension, not just a chosen natural action.

Put J=I∩S. The relevant data are:

| Table row | S | J | Degree | Number of S-classes checked |
| --- | --- | --- | --- | --- |
| 22 | Ω7(3) | G2(3) | 1080 | 2 |
| 25 | PΩ8⁺(2) | Sp6(2) | 120 | 3 |
| 27 | PΩ8⁺(3) | Ω7(3) | 1080 | 6 |

The [finite classical rank certificate](../code/verify_finite_classical_ranks.g), run with GAP 4.15.1 and CTblLib 1.3.11, loads the complete `Maxes` lists for the three socle character tables. It tests the order of every listed maximal subgroup. The only maximal orders divisible by the indicated order of J are those of the listed J-classes themselves. Thus any subgroup isomorphic to J lies in a maximal subgroup of the same order and equals it. This proves coverage conditional on the completeness and class identification of the stored ATLAS/CTblLib maximal lists; an abstract subgroup name alone would not suffice.

For each of these eleven entries the script requires its distinct stored table identifier and its subgroup fusion map. It explicitly induces the trivial character along that fusion and checks its degree and self-inner-product. All eleven results are the displayed degree and rank three, since ⟨1_J^S,1_J^S⟩ is the number of S-orbits on ordered pairs. In particular the six Ω7(3) classes in PΩ8⁺(3) and both G2(3) classes in Ω7(3) are included individually; no triality or outer-conjugacy shortcut is assumed. The source authors read and ran the exact source successfully. This is a finite character-data calculation, not a reconstruction of the maximal-subgroup classification or of the stored fusions.

Because S is transitive and normal in primitive M, the actual restricted S-set is S/J. Its two nontrivial subdegrees sum to |X|−1, which is odd in all three rows, so they are unequal. The point stabilizer I normalizes J and therefore permutes its orbits preserving sizes. It cannot fuse the two nontrivial orbits. Consequently the actual full M has rank three in every listed class and allowable extension.

Apply the reviewed [C0017 rank-three theorem](../../claims/0017.md), retaining its CFSG and scoped supporting inputs. It forces X≅M(2) or M(3). The degree distinguishes M(2) in row 25 from M(3) in rows 22 and 27. Row 22 is then impossible even for nonassociative Moufang loops: [C0009 Theorem 2.1(1)](../foundations/C0009.md), using Nagy–Vojtěchovský, arXiv:math/0701707v1 Corollary 4.7, gives Mlt(M(3))=PΩ8⁺(3), whereas the actual row-22 socle is Ω7(3). Loop isomorphism conjugates the full multiplication groups, whose socles here have different orders. Rows 25 and 27 retain only the stated necessary Paige conclusions; no assertion that every listed solvable-factor containment is realized by such a loop is needed.

The character-library versions and primary dataset locators are in [REFERENCES](../foundations/references.md#finite-orthogonal-rank-data). Proof/code development used a research reviewer; this is distinct from independent review. The duplicate `L3(4)` entries for PSU4(3), which resolve to the same stored table/fusion, are deliberately outside this certificate: inducing that same character twice would not establish coverage of two classes. C0010 and the remaining finite and general classification obligations remain open.


### Independent review of the all-class orthogonal ranks

automated-model reviewer A, reviewer B and reviewer C independently accepted the three-row deduction and certificate at exact source `ae88d5ffa7c25ac899aa3187cd4c3c4ef0d74a8e`. Each extracted the exact committed GAP script to a temporary path, read it and ran it with the asserted GAP 4.15.1 and CTblLib 1.3.11 versions. All eleven entries passed: three degree-120 and eight degree-1080 rank-three actions. They checked every-maximal-order coverage, the class-specific identifiers and fusions, the actual-overgroup nonfusion argument and the distinction between row 22's socle contradiction and rows 25/27's necessary Paige conclusions. reviewer A freshly inspected the O7(3) online maximal list and Nagy–Vojtěchovský v1 Corollary 4.7; the other two retained the stated primary-source inputs without fresh web inspection. None reconstructed the maximal-subgroup classifications or character/fusion data, or reproved C0017. These are scoped model mathematical/code acceptances, not formal verification, GitHub approval or completion of C0010.


## Proposed degree-40 PSL4 exclusion

Scope: 0323-finite-simple-non-moufang-bol-loops:C0010, Li–Xia arXiv:1408.0350v3, Table 1.2 row 6. Let S=PSL4(3), G≤Aut(S), G0=G∩S≤2⁴:5:4, and suppose the canonical faithful simple nonassociative left Bol folder (G,H,K) has degree |K|=40. Use [C0007](../foundations/research-C0007.md), the [canonical cyclic-normal inversion obstruction](odd-envelope-parameterization.md#proposed-characteristic-section-inversion-obstructions), and the [all-parity metabelian exclusion](#proposed-all-parity-exclusion-of-metabelian-left-multiplication-groups), reviewed at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`. Here G is the actual LMlt(X), S=Soc(Mlt(X)), and H fixes the loop identity. The outside marked set Λ has cardinality 40, is a union of G-conjugacy classes of involutions, and H∩Λ²=1. No assertion that Λ is one class is used. The full classical automorphism input is Kleidman–Liebeck §2.1, Table 2.1.B and Theorem 2.1.4, printed pp.15–16: Aut(S)=PGL4(3) extended by inverse transpose, with Out(S)≅C2×C2. The independent exact-source reviews are recorded below.

Let U=2⁴ in the specified ambient subgroup, and N=G0∩U. Since |Out(S)|=4 and 40 divides |G|, 5 divides |G0|. An element of order 5 acts irreducibly on U, so N=1 or U. This also follows intrinsically from the linear embedding: if its action on U were trivial, its order-five lift to SL4(3) would centralize the inverse image E of U (the commutator signs have order dividing both two and five). An order-five linear transformation in dimension four over F3 is irreducible, so its linear centralizer is F81×, which is cyclic; this cannot contain E with quotient C2⁴. Thus the action on U is nontrivial, and every nontrivial irreducible F2C5-module has dimension four. If N=1, G0≤5:4 and its Sylow 5 is unique. All order-5 elements of G lie in G0, making that Sylow subgroup characteristic in G. The cyclic-normal inversion obstruction makes the conjugation image on C5 have order at most 2; the faithful action of 5:4 on its normal C5 yields |G0|≤10. Thus |G|≤40; transitivity forces regularity and the loop is associative. Hence N=U. Now O2(G0/U)=1, because G0/U≤5:4 contains C5 and acts faithfully on it; therefore U=O2(G0) is characteristic in G0 and normal in G.

### Actual centralizer of U

Lift U to E in SL4(3). Its central kernel is {±I}; the order-5 action on E/{±I} is irreducible. If E were abelian, simultaneous diagonalization over an algebraic closure gives at most four common eigenspaces. An order-5 normalizer fixes each, and hence centralizes E, contradiction. Thus the commutator form on U is nonzero; irreducibility makes its radical zero, so E is extraspecial. The square form is minus type since O4+(2) has order 72 and no element of order 5. Thus E≅Q8*D8.

For an explicit model over F3, take Q8 generated by i=[[0,1],[-1,0]] and j=[[1,1],[1,-1]], and D8 generated by X=[[0,1],[1,0]] and D=diag(1,-1); tensor the two representations. Both i,j square to −I and anticommute. The four matrices 1,i,j,ij span M2(F3), as do 1,X,D,XD. Their tensor products span M4(F3). Let z denote the central involution of E. The algebra A=F3[E]/(z+1) has dimension 16, with one basis vector for each coset of ⟨z⟩. The displayed representation maps A onto M4(F3), and is therefore an isomorphism. The actual embedding E≤SL4(3) likewise gives a unital algebra homomorphism A→M4(F3); simplicity of the matrix algebra makes it injective, hence an isomorphism. The matrix-unit relations then give a basis in which the actual representation is the displayed one. The Q8 factor preserves the standard alternating form J2 and the D8 factor preserves I2; E therefore preserves J=J2⊗I2. The automorphism α:g↦Jg^{-T}J^{-1} is an outer graph involution and fixes E pointwise.

A projective linear element centralizing U induces a linear character U→{±1} by its commutators with E. All 16 such characters are realized by E, because its commutator form is nondegenerate; after multiplying by E, the element centralizes E linearly and is scalar, as E spans M4(F3). Thus C_PGL4(3)(U)=U. Since Aut(S)=PGL4(3) extended by a graph involution, C_Aut(S)(U)=U×⟨α⟩ and C_S(U)=U.

### Quotient and splitting

Set Q=G/U and Q0=G0/U. The odd part of |Q| is 5, and Q0 contains its unique normal C5, call it Rbar. This subgroup is characteristic in Q, since every 5-element of Q lies in Q0 and Q0≤5:4 has unique Sylow 5. Let D=C_G(U)/U, of order at most 2. The map Q→GL(U) has kernel D and image normalizing the irreducible Rbar, hence image lies in ΓL1(16). Before applying inversion, U must be characteristic in G. Let ρ:G→GL(U) be conjugation. The image ρ(Rbar) is a normal C5 in ρ(G), and the normal 2-subgroup ρ(O2(G)) centralizes it. Its centralizer in GL4(2) is the odd-order group F16×, so ρ(O2(G))=1. Conversely C_G(U) is a 2-group containing U; hence O2(G)=C_G(U)=:P. If P=U then U is characteristic. If |P/U|=2, an order-5 complement R in the preimage of Rbar acts fixed-point-freely on U and fixes a unique element z in P\U: P is elementary abelian, and coprime averaging splits its fixed-free submodule U from the trivial quotient P/U. Since Rbar is normal in Q, conjugation by G sends R to a U-conjugate of R; P is abelian and centralizes U, so z is central in G. Consequently [P,G]=[U,G]=U, because [U,R]=U, and U is again characteristic. Thus τ descends to Q. The cyclic-normal inversion obstruction applied to Rbar forces the induced field exponent on Rbar to have order at most 2. As the odd part of |Q| is 5, its image is C5 or D10.

If the image is C5, Q is abelian, because D is central of order at most 2 and coprime lifting gives a normal C5 with central 2-complement of order at most 2. Thus G is metabelian, contradicting the cited exclusion. If the image is D10 and D=1, Q=D10. If |D|=2, then Q is D10×C2 or 5:C4, with the C4 acting on C5 through its quotient C2. The latter is impossible: Q0 contains C5 and meets D trivially, while the unique index-two subgroup of 5:C4 is C5×D; thus Q0=C5 and Q/Q0≅C4, contrary to the exponent-two outer quotient of S. Consequently Q=D10 or D10×C2.

The preimage of Rbar is U:C5 by Schur–Zassenhaus. All its C5 complements are U-conjugate; choose one R. Frattini's argument gives G=U N_G(R), and U∩N_G(R)=C_U(R)=1 because R acts fixed-point-freely. Thus G=U⋊Q. We have respectively G=B:=U:D10 or G=B×C2.

### Terminal marked-set exclusions

For B, U=O2(B) is characteristic. Aligning a C5 complement by a U-conjugation shows that every automorphism of B restricts to an element of ΓL1(16) on U, and, after aligning R by a U-conjugation, the restriction determines it: an automorphism fixing U and R sends a reflection r to ur, and normalizing R forces u∈C_U(R)=1. Conversely ΓL1(16) normalizes D10: conjugation of the fourth-power field involution by a scalar c changes it by c⁻³∈C5, and field automorphisms preserve C5. Together with inner translations this gives Aut(B)=U:ΓL1(16). The group B is centerless. Every element of square one in this affine normalizer lies in B. Indeed, its field exponent is 0 or 2; exponent zero forces scalar c²=1, hence c=1, while in the latter case the scalar c obeys c⁵=1, and the translation is fixed by cFrob². Hence every involutory automorphism of B is conjugation by an involution t∈B. The elements of B with square 1 number 36: identity, 15 nonzero vectors, and four elements in each of five reflection cosets. For τ=Inn(t), formal outside involutions τk correspond injectively to elements tk of square 1, contradicting |Λ|=40.

Now G=B×⟨z⟩. Here O2(G)=U×⟨z⟩ and [O2(G),G]=U, so U is characteristic; Z(G)=⟨z⟩ is characteristic. Every automorphism induces an automorphism of B and differs from its standard lift by a central transvection η(b,z^e)=(b,z^{e+χ(b)}), where χ is either zero or the unique nonzero homomorphism B→C2. If τ is involutory, the induced automorphism of B is involutory and therefore inner. If χ is nonzero, comparison of the central coordinate in τ(k)=k^{-1} forces χ(k)=0 for every k∈K. Then K cannot generate G.

Finally suppose τ=Inn(t) is inner, with t²=1. In the formal extension put c=τt; then c is central and c²=1. Every marked involution has the form ca with a²=1 in G, and multiplication by c identifies Λ with a conjugacy-invariant set of involutions of G while preserving its square: (ca)(cb)=ab. The subgroup U×⟨z⟩ has only 32 elements, and the involutions outside it lie in two reflection classes of size 20. A size-40 union of classes must therefore include a reflection class. Its square contains U: the five reflection cosets supply the five one-dimensional F4-subspaces of F16, whose union is U. Since |G/U|=20 and |H|=8, the image of H has order at most four and H∩U is nontrivial. This contradicts H∩Λ²=1. All cases are excluded, subject to the stated upstream inputs and review.

Proof development used a research reviewer and coordinator repairs, with a preliminary audit by a research reviewer. This is an analytic marked-set argument, not a computation or a claim that normal subgroups automatically define quotient loops. Independent exact-source reviews are recorded below.


## Proposed remaining geometric finite-row bridges

**Conditional deductions with three independent reviews below.** For 0323-finite-simple-non-moufang-bol-loops:C0010 retain finite simple nonassociative left Bol X, solvable G=LMlt(X), M=Mlt(X), I=M₁ and S=Soc(M). Under C0008 and the individually stated source and reviewed inputs, the actual factorization in Li–Xia arXiv:1408.0350v3 Table 1.2 cannot lie in rows 18, 20 or 24. No general acceptance of the partial C0016 is used.

### Row 18: the actual degree-36 unitary action

Here S=PSU3(3) and J=I∩S=PSL2(7), of order 168 and index 36. The complete ATLAS/CTblLib maximal list has orders 216,168,96,96. Only 168 is divisible by |J|, and it is a single listed subgroup class. Hence every such J is maximal and S-conjugate to the listed one, conditional on that complete finite-class data. In particular N_S(J)=J and the centralizer of S on S/J is trivial.

The reviewed [C0017 proof §3](../foundations/C0017.md) identifies the local degree-36 graph action P=G2(2)=PSU3(3):2, of order 12096. Its normal simple subgroup S is transitive; its point stabilizer has index 36, so by the class result it is precisely the actual S-action up to permutation isomorphism. The permutation normalizer of S injects into Aut(S), whose order is 12096 by the ATLAS outer-group identification. Since P is contained in this normalizer and already has that order, it is the full normalizer. Every actual M normalizes S, and is therefore contained in this fixed graph action.

The independent certificate review at `08e0fbb08fcc9b7da728e2ae6558695992ca2682`, with the corrected source pagination retained in C0017 §3, gives zero uniform-orbital-displacement candidates on P's 21-suborbit. C0008's elementary displacement lemma excludes any loop with multiplication group contained in P. This argument covers M=S as well: the socle action has rank four, with subdegrees 1,7,7,21, while P fuses the two 7-orbits. No rank-three theorem is incorrectly applied to that rank-four group. The new work is the all-class, actual-overgroup bridge to the already reviewed certificate, not a new execution of that certificate.

### Row 20: both degree-162 unitary classes

Here S=PSU4(3) and J=PSL3(4), of index 162. Crnković–Mikulić–Rodrigues, *Some strongly regular graphs and self-orthogonal codes from the unitary group U4(3)*, Glasnik Mat.45(65)(2010), §3, printed pp.309–310, Table 1 and preceding paragraph, give the complete sixteen maximal-subgroup classes. Exactly two are PSL3(4), of index 162; none of the other maximal indices is a proper divisor of 162. Therefore every such J is maximal and is one of the two listed classes. Both degree-162 actions have rank three; the same paragraph states that they are outer-equivalent. These are cited ATLAS-dependent source statements, separately inspected by the source authors and contributor, not a conclusion from twice inducing the same stored CTblLib fusion.

Since the two nontrivial socle subdegrees sum to 161, they are unequal. As before I normalizes J and cannot fuse unequal J-orbits, so the actual M has rank three in either class. The reviewed C0017 theorem gives only Paige degrees 120 and 1080, excluding 162. This short bridge uses the source's rank and class coverage and C0017; it does not need a new graph-group enumeration or a separate assertion about which abstract outer automorphisms preserve a selected class.

### Row 24: the actual odd-orthogonal point action

Here S=Ω9(3) and J is Ω8⁻(3) or its indicated extension by two. The embedding, rather than merely the abstract group name, is given by Li–Xia v3 Proposition 7.13, proof Case 2, printed pp.61–62: it places the maximal factor in the natural minus-point stabilizer N₁⁻ and derives Ω_(2m)⁻(q) normal in J≤N₁⁻, explicitly including (m,q)=(4,3) as Table 7.5 row 3. Thus J₀=Ω8⁻(3) acts on the perpendicular complement of a nonsingular line e in the natural nine-dimensional space.

Its normalizer in S is the line stabilizer N=J₀.2. The subgroup J₀ is perfect, acts irreducibly on e⊥, and fixes only the line e in the full space. Both displayed J choices satisfy J′=J₀, so I normalizes J₀. The group N_M(J₀) is proper: otherwise J₀ would be normal in S. By maximality of I, I=N_M(J₀), and consequently J=N_S(J₀)=N. The actual degree is 3240; the smaller displayed J₀, whose raw index is 6480, cannot occur as the stabilizer intersection in this primitive action.

Kleidman–Liebeck §2.1, Table 2.1.B and Theorems 2.1.3–2.1.4, printed pp.15–16, supply the natural B4 automorphism group PGO9(3); there are no nontrivial field or Dynkin graph automorphisms here. Every odd-dimensional similarity has square multiplier and becomes an isometry after scalar rescaling. Hence it preserves each norm-type point orbit. The unique fixed line of J₀ and the trivial centralizer N_S(N)/N identify the actual full M-action inside this natural projective orthogonal action, by the same reviewed point-normalizer interface used above.

The same norm-type orbit contains a point perpendicular to e, because the nondegenerate eight-dimensional complement represents the required norm. The invariant perpendicular relation is therefore nonempty. C0008's displacement identity would force a translation that sends every orbit point to a perpendicular point. The [all-odd-field perpendicular lemma](../foundations/C0016.md#odd-orthogonal-perpendicular-all-fields), independently accepted at `67fcd25724552c730ecb9d94ede1a0c9ee06dcf5`, excludes such a semilinear map in odd dimension at least five. This rules out row 24 at both parities, without a rank assumption on G or a quotient-loop assertion.

The primary input locators and inspection limits are in [REFERENCES](../foundations/references.md#finite-geometric-bridge-sources). Contributors a research reviewer, a research reviewer and a research reviewer developed the respective bridges; their contributions are not independent acceptance. C0010 and the unaddressed finite and general classification obligations remain open.


### Independent review of degree 40 and the three geometric bridges

automated-model reviewer A, reviewer B and reviewer C independently accepted the degree-40 argument and rows 18, 20 and 24 bridges at exact source `8f22211fbd9d0e3c48347ecf65a037155ed428dd`. They checked the intrinsic extraspecial-minus lift and group-algebra representation, actual automorphism centralizer, characteristic U before inversion descends, quotient classification and Frattini splitting, affine-normalizer involutions, and the actual marked-class-square contradiction, including the central-transvection alternative. They also checked all-class coverage and the actual-overgroup interfaces in the three geometric rows, distinguishing the rank-four socle in row 18 from its full graph normalizer and the source rank-three route in row 20. reviewer A freshly inspected the U3(3) CTblLib maximal list and Crnković–Mikulić–Rodrigues §3 pp.309–310. The others retained the stated primary-source interfaces without fresh source inspection. All retained the cited Li–Xia, Kleidman–Liebeck, canonical folder/inversion, metabelian and scoped C0016/C0017 inputs; none reran an earlier finite certificate or reproved these external classifications. Their acceptances concern these four bounded exclusions, not C0010 or the complete classification.


## Proposed finite Sp6 plus-action exclusion

**Computational deduction with three independent mathematical/code reviews below.** Continue 0323-finite-simple-non-moufang-bol-loops:C0010 with a finite simple nonassociative left Bol loop X, solvable G=LMlt(X), and an actual full-multiplication factorization in Li–Xia arXiv:1408.0350v3 Table 1.2 row 16. Under C0008, the canonical C0001/C0007 marked-set interface and the finite source/computational inputs below, this row is impossible. This is one finite action, not an experiment promoted to a universal parameter bound.

### Identifying the action and covering the solvable upper group

The socle S=Sp6(2) has trivial outer group, so M=Mlt(X)=S. The row gives I=A8 or S8. By primitivity I is maximal. The complete ATLAS/CTblLib maximal-subgroup list contains no A8 and exactly one S8 class of index 36, so I=S8 in that class. The actual action is the action on the 36 plus-type quadratic refinements of the natural alternating form, whose stabilizer is O6⁺(2)≅S8. This is a 2-transitive action, not the different degree-36 G2(2) graph action of row 18; no rank-three theorem is used.

The [finite certificate](../code/verify_sp6_plus36_folders.g) constructs Sp6(2) over F2 and all 64 refinements q_u(v)=v1v6+v2v5+v3v4+u·v. It checks distinctness, invariance under the group generators and faithfulness, and finds the orbits of sizes 28 and 36. It identifies the latter as plus type by checking that the zero-parameter form has 36 zeros and lies in that orbit; its induced action is faithful and primitive. This supplies the concrete action rather than importing a table of permutation generators.

The table places G inside a subgroup B of structure 3₊^(1+2):2.S4, of order 1296. Li–Xia §2.1 explicitly defines the plus notation for odd primes as extraspecial of exponent p and defines the extension notation. Thus B normalizes its extraspecial exponent-three subgroup E of order 27. The certificate enumerates all subgroup conjugacy classes in a Sylow 3-subgroup of S and finds exactly one class of nonabelian exponent-three order-27 subgroups. Every E lies in a Sylow 3-subgroup; Sylow conjugacy and this complete enumeration therefore put every such E in one S-conjugacy class. Its computed normalizer A=N_S(E) has order 1296 and 3-core E. Since B≤N_S(E) and has the same order, B=N_S(E). Accordingly every table-allowed G is conjugate into this particular computed A. The normalizer A is **not maximal in S**; maximality is neither asserted nor needed for this coverage argument.

The complete subgroup-class enumeration of A has 96 classes. Exactly five act transitively on the plus-36 set, with (|G|,|G′|,|G₁|) respectively

    (216,27,6), (216,54,6), (432,108,12),
    (648,216,18), (1296,648,36).

Conjugacy by A preserves the ambient action and candidate-loop existence. For a fixed transitive G all point stabilizers are G-conjugate, so it is enough to use its stabilizer H of point one. The certificate covers every actual pair (G,H) in this row, conditional on the standard exact GAP subgroup algorithms and the stated source identification.

### Necessary marked-set test and exhaustive rejection

C0001 gives trivial left nucleus in the simple nonassociative case. C0007 then supplies an automorphism τ of G with τ²=1 and τ(k)=k⁻¹ on the generating section K. Work in a formal extension with an external involution t inducing τ even when τ is the identity. The set Λ=tK has size 36, contains t, is G-conjugacy invariant and satisfies H∩Λ²={1}. These are necessary conditions only; the test need not assume or prove their sufficiency. In particular no assumption that τ fixes H is used.

For each of the five groups, the code enumerates every automorphism of order one or two. Let Inv(τ)={x∈G:τ(x)=x⁻¹}. A possible K lies in Inv(τ), so if this set has fewer than 36 elements or fails to generate G, discard τ. Conjugation of tx by g∈G corresponds to the twisted action

    x ↦ τ(g⁻¹) x g.

The code enumerates all its orbits on Inv(τ). A selected K must be a union of these orbits and include the orbit containing 1. For inverted x,y, (tx)(ty)=x⁻¹y, so an orbit containing distinct x,y with x⁻¹y∈H cannot occur. Discard such orbits and those with more than 36 elements. Discard any remaining orbit incompatible with the mandatory orbit. Enumerate every subset of the remaining orbit list whose union with that mandatory orbit has size 36, then test all pair collisions and generation. These filters cannot discard an actual canonical K, and the subset enumeration loses no admissible union.

The source authors read and ran the pinned source with `gap -A -q -b`. For the first three groups no automorphism has a large enough generating inverted set. In the group of order 648 there are 36 such automorphisms, and none has an admissible mandatory orbit. In the group of order 1296 there are 118 such automorphisms; only one has an admissible mandatory orbit, and no union containing it has size 36 after the stated filters. Thus no necessary marked set survives, proving the finite exclusion conditional on the mathematical interface and exact computational inputs. This is stronger than a count of inverted elements and does not replace the marked-set test by an unjustified quotient-loop construction.

The execution uses GAP 4.15.1 with `-A` to disable suggested-package autoloading; the loaded libraries are GAPDoc 1.6.7, PrimGrp 4.0.1, SmallGrp 1.5.4 and TransGrp 3.6.5, checked by the script. Its finite-field, group-order, Sylow, subgroup-class, normalizer, automorphism and orbit algorithms remain trusted computational dependencies; the run is not a formal proof of those algorithms. There are no downloaded generators, random search cutoffs or uncommitted imports. Proof/code development came from a research reviewer, followed by coordinator source and coverage checks. Independent exact-source reviews are recorded below; C0010 remains open.


### Independent review of the Sp6 plus-action certificate

automated-model reviewer A, reviewer B and reviewer C independently accepted the finite row-16 deduction and certificate at exact source `8c96ae3a6eef47209bf95fd96f20caf82752e660`. Each read and extracted the exact script, then ran it with GAP 4.15.1 using `-A -q -b`; all five groups failed the necessary marked-set conditions, with the stated stage counts and all four loaded-library version assertions passing. They checked the actual plus-36 action, unique Sylow-subgroup class and equal-order normalizer coverage without maximality, all transitive subgroup classes and all involutory automorphisms, the twisted action, mandatory identity orbit, collision tests and complete orbit-subset enumeration. reviewer A freshly inspected the CTblLib Sp6(2) maximal list and ATLAS Out=1; all retained Li–Xia's stated extraspecial notation and source containment. The other two did not freshly inspect those webpages. These reviews retain the canonical folder/inversion interfaces, external class-list statements and exact GAP algorithms as inputs; they are not formal verification or acceptance of C0010 as a whole.

## Proposed complete finite PSp4(3) stabilizer exclusion

**Conditional deduction with three independent mathematical/code reviews below.** Retain the finite simple nonassociative left Bol and actual primitive almost-simple full multiplication setting. For 0323-finite-simple-non-moufang-bol-loops:C0010, Li–Xia arXiv:1408.0350v3 Table 1.2 row 11 is impossible under C0008, C0017 and the finite class/character inputs below. This includes the displayed 2⁴:A5 stabilizer option as well as A5, S5, A6 and S6.

Here S=PSp4(3)≅PSU4(2) and Out(S)=C2. Hence the actual full group M is S or Aut(S). Put I=M₁ and J=I∩S. The source permits J of orders 60,120,360,720,960. Because S is transitive, IS=M, and therefore |I|=|M:S|·|J|. Because M is primitive, I is maximal. These two requirements concern I in the actual full M; it would be insufficient simply to discard a nonmaximal J in S.

The [finite stabilizer certificate](../code/verify_psp43_finite_stabilizers.g) checks the complete maximal-subgroup metadata and orders of both groups. The lists of maximal orders are respectively

    S:       960,720,648,648,576;
    Aut(S):  25920,1920,1440,1296,1296,1152.

Filtering by the possible actual I-orders leaves precisely one class each of degrees 27 and 36 in each ambient group. The Aut(S) subgroup S is not an allowable point stabilizer since IS=M. Thus J=A5,S5,A6 cannot occur; the remaining stabilizers in S are 2⁴:A5 and S6, and their full-outer counterparts are 2⁴:S5 and S6×C2. Class completeness and identifications are explicit ATLAS/CTblLib inputs; the script does not reconstruct the maximal-subgroup classification.

For each of these four actual ambient-group actions, the code requires a stored subgroup fusion and explicitly induces the trivial character. Under GAP 4.15.1 and CTblLib 1.3.11, the source authors read and ran the exact source: each induced character has the asserted degree 27 or 36 and self-inner-product three. Consequently each actual full M has rank three. In particular the degree-27 outer action is computed directly; no odd-sum argument is applied to its two nontrivial subdegrees, whose sum is even. C0017, with its reviewed CFSG and scoped supporting inputs, leaves only Paige orders 120 and 1080 and rules out both 27 and 36.

The primary dataset and automorphism locators are in [REFERENCES](../foundations/references.md#psp43-stabilizer-data). Development contributions came from a research reviewer; independent exact-source acceptance is recorded below. This proof uses neither an unreviewed aggregate finite-loop census nor an assumption that the actual stabilizer is maximal in the socle when M is larger. C0010 remains open.


### Independent review of the PSp4(3) stabilizer certificate

automated-model reviewer A, reviewer B and reviewer C independently accepted the complete row-11 argument and certificate at exact source `f448cb7258d6783674b977534f3b8ff5071ba1c0`. Each read and extracted the exact committed GAP script and ran it under the asserted GAP 4.15.1 and CTblLib 1.3.11 versions; all four actual-group actions had the stated degree 27 or 36 and rank three. They checked maximality in M, IS=M and the full-group stabilizer-order filter for all five displayed J choices, and the direct outer-action calculation at degree 27. reviewer A freshly inspected both CTblLib maximal lists and the ATLAS identification/outer-order statements. The other two retained the source inputs without fresh inspection. Class completeness, stored fusion/character correctness and the reviewed C0017 theorem remain explicit inputs. This is a scoped finite-row mathematical/code acceptance, not a loop census or completion of C0010.

## Proposed degree-960 orthogonal exclusion

**Conditional deduction with three independent mathematical/code reviews below.** Continue 0323-finite-simple-non-moufang-bol-loops:C0010 with finite simple nonassociative left Bol X, solvable G=LMlt(X), M=Mlt(X), I=M₁, S=Soc(M) and G₀=G∩S. Suppose the actual factorization lies in Li–Xia arXiv:1408.0350v3 Table 1.2 row 26: S=Ω8⁺(2), J=I∩S=A9 and |X|=960. Under the canonical C0001/C0007/C0008, the reviewed cyclic-normal inversion obstruction, and the source/data inputs below, this row is impossible. The argument controls outer extensions and does not assume this action has rank three.

### All A9 classes and the actual full orthogonal group

The [triality certificate](../code/verify_o82_a9_triality.g) uses GAP 4.15.1 and CTblLib 1.3.11. In the complete maximal-subgroup list of S, the only orders divisible by |A9|=181440 are those of three A9 classes and three Sp6(2) classes. A9 cannot lie in Sp6(2): that would be a subgroup of index eight in a simple group of order 1451520>8!, contradicting the faithful coset action. Hence every A9 subgroup is maximal and is one of the three recorded classes.

Induce the trivial character from the stored A9 subgroup fusion to obtain its degree-960 permutation character π. In the stored fusion from S to the actual extension S:3, two S-classes (positions 3 and 4) fuse while π has values 96 and 0 on them. Thus the outer C3 in this extension does not preserve this A9 conjugacy class: if it did, π would be invariant and constant on all these fusion fibers. An order-three permutation of a set of three classes that moves one class cycles all three. Since Out(S)=S3, each class has outer stabilizer of order two. This conclusion uses the actual extension's subgroup fusion, not an arbitrary formal symmetry of a character table. The source authors read and ran the exact script, obtaining that witness. Maximal-class completeness and character/fusion correctness remain external data inputs.

For the natural model take E={v∈F2⁹:Σv_i=0} and Q(v)=wt(v)/2 modulo two. Its polar form is nondegenerate, and it has 136 zero vectors, so E is an eight-dimensional plus space. Coordinate permutations embed S9 in O(E), and A9 lies in S=Ω(E). A coordinate transposition has rank one after subtracting the identity on E, and hence nonzero Dickson invariant; it realizes the nontrivial outer element of O(E)/S while normalizing A9. By the three-class result, transport the entire actual pair (M,I) by an automorphism of S so that J is this natural A9. Since M=SI and I normalizes J, its outer image stabilizes this class. The class stabilizer has order two and is already realized by O(E), so the full actual M embeds in O(E). This fixes the action of the relevant outer involution rather than assuming arbitrary triality preserves a natural module.

### Recovering a parabolic in that same model

Li–Xia v3 Proposition 7.16(e) gives S=G₀J when M>S; when M=S it follows directly. Thus G₀ is transitive on the 960 points. Proposition 7.16(a),(c),(d) and Table 7.7, applied to this socle factorization with J=A9, place G₀ in one of the three outer-node parabolics P1,P3,P4. The source explicitly obtains this finite classification using Magma; that computation is retained as an input and is not reproduced here. Transport preserves the set of those three parabolic classes.

In our natural model J has two orbits on the 135 nonzero singular vectors: weights four and eight, of sizes 126 and nine. If G₀≤P1 for a singular-point stabilizer, S=G₀J would make J transitive on these points, a contradiction. Therefore G₀ preserves a maximal singular four-space L, in P=P3 or P4.

Write P=V:GL4(2), where V consists of the maps (x,y)↦(x+B y,y) on L⊕L*, with B alternating; V≅∧²L has order 64. Liebeck–Praeger–Saxl, *Regular subgroups of primitive permutation groups*, author text REGFINAL, §11 case (11.10), printed p.60, identifies J∩P=2³:GL3(2) and J∩V=1 in this even-subset model. In its displayed representative L, the all-eight subset is the unique nonzero vector of weight eight and is fixed by J∩P. Thus its image in GL4(2) is the full point stabilizer, by order. The odd coordinate permutations in S9 exchange the two maximal-singular families while normalizing J, so the same identification holds for both, and transitivity of J on the relevant family follows also from S=G₀J.

The actual factorization P=G₀(J∩P) now makes D=G₀V/V transitive on the 15 nonzero vectors of L. The Hering classification as stated in LPS Lemma 3.1, printed p.13, puts every solvable such D inside ΓL1(16)=C15:C4: its other (4,2) alternatives contain SL2(4), SL4(2), Sp4(2), A6 or A7 and are nonsolvable. This is a bound in the same actual parabolic P. The later regular-subgroup inference in LPS is not used; G₀ is only assumed transitive here.

### The characteristic layer forces G into the socle

Put W=G₀∩V. Since 960 divides |G₀| and |D| divides 60, |W|≥16. The odd part of |G₀| forces D to contain its full scalar C15. This cyclic group acts on ∧²L with two irreducible F2-constituents, of dimensions four and two. Explicitly, if its generator has eigenvalue exponents 1,2,4,8 modulo 15 on L, the wedge exponents are 3,5,6,9,10,12, with Frobenius orbits {3,6,12,9} and {5,10}. Maschke's theorem and the distinct constituents show that a C15-invariant W of dimension at least four is the four-dimensional constituent or all V. In particular |W|=16 or 64.

A normal 2-subgroup of D centralizes its normal C15, whose centralizer in ΓL1(16) is the odd scalar group. Hence O2(D)=1 and W=O2(G₀). It is characteristic in G₀ and therefore normal in G; no claim that it is already invariant under the abstract canonical automorphism is needed at this stage.

The common kernel in L* of the alternating maps B∈W is invariant under the scalar C5 in D. That C5 acts irreducibly on the four-dimensional L*. Because W≠0, the common kernel is proper, hence zero. Consequently the common fixed space of W on E=L⊕L* is exactly L. Since G normalizes W and acts linearly on E, it preserves L. Its full-orthogonal stabilizer P lies inside Ω(E): on block-diagonal generators the rank of g−1 is twice a rank in dimension four, and on unipotent generators it is the even rank of an alternating matrix. The Dickson invariant is therefore zero on every generator of P. We conclude G≤S and thus G=G₀, even if M>S.

If |W|=16, then |G|≤16·60=960. Transitivity forces regularity and associativity, a contradiction. If |W|=64, W=O2(G) is now characteristic, so the canonical inverting automorphism descends to D=G/W. Its C15 is the unique normal Hall subgroup of odd order, hence characteristic. The reviewed cyclic-normal inversion obstruction forces the conjugation action on C15 to have exponent at most two. Thus D lies in C15:C2, with the possible field involution acting as a↦a⁴. The C3 factor survives in D_ab: the commutator of this field involution with C15 is contained in C5. Consequently G has an abelian quotient divisible by three.

But |G|≤64·30=1920 and |X|=960, so the loop point stabilizer H=G₁ has order at most two. The previously proved identity G=HG′ for finite simple nonassociative loops requires H to surject onto every abelian quotient, a contradiction. This closes row 26 without assuming an induced quotient loop or using the selected set as the full involution set.

Proof development used a research reviewer, a research reviewer, a research reviewer and coordinator repairs. The source authors directly inspected the Li–Xia factorization passage and LPS geometric and Hering statements; the class-fusion witness has been run separately. The exact primary versions and external-input limits are recorded in [REFERENCES](../foundations/references.md#degree960-source-interface). C0010 remains open.


### Independent review of the degree-960 exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted the complete conditional row-26 proof and triality certificate at exact source `758b3fe1a625ea77993270d02ea478e5cf90df80`. All three extracted and ran the committed certificate with GAP 4.15.1 and CTblLib 1.3.11; it passed with the stated class positions and values 96 and 0. They checked the three-class coverage, transport of the entire actual action, parabolic placement, use of the same actual intersection for the Hering bound, characteristic-subgroup ordering, fixed-space argument forcing G into S, and final quotient contradiction. reviewer A freshly inspected LPS Lemma 3.1, printed p.13, and §11 case (11.10), printed p.60. The other two retained the recorded primary-source inspections without fresh reads. All retain Li–Xia's cited finite classification, the character/fusion dataset and canonical folder results as inputs. These are scoped mathematical/code acceptances, not formal verification, independent reconstruction of those classifications, or acceptance of C0010 as a whole.

## Proposed combined classical solvable-factor table exclusion

**Conditional assembly with three independent mathematical reviews below.** For 0323-finite-simple-non-moufang-bol-loops:C0010, let X be any finite simple nonassociative left Bol loop and suppose its actual G=LMlt(X) is solvable. Put M=Mlt(X), I=M₁ and S=Soc(M). Under C0001/C0007/C0008, the precise reviewed inputs linked below and Li–Xia arXiv:1408.0350v3, the factorization M=GI cannot belong to **either Table 1.1 or Table 1.2**. This assertion includes Moufang loops and has no parity restriction. It does not yet cover the separate both-solvable, alternating or sporadic alternatives of the source, and it does not cover nonsolvable G.

First dispose of the possible Moufang exceptions. [C0001 proof Lemma 1.2](../foundations/C0001.md) gives G normal in M and the surjective loop homomorphism X→(M/G)^op, x↦R_xG. Simplicity forces its kernel to be X or 1. A trivial kernel would embed X in a group and make X associative, so M=G. C0008 supplies a nonabelian simple socle in M, contradicting solvability of G. Hence X is proper under the present hypotheses. This uses the Moufang identities only in this paragraph; no equality of left and full multiplication groups is asserted for proper loops.

The [infinite-table assembly](#proposed-completion-of-the-infinite-classical-solvable-factor-table), independently accepted at `93cab1c81aaab8988d79e207e2f0bd071d825600`, already excludes every Table 1.1 row for proper loops. Its sole nonassociative exception, Paige in row 9, is also impossible by the preceding paragraph. It remains to assemble the finite table. Since S is nontrivial normal in primitive M, S is transitive, and the degree is [S:J] for J=I∩S. The solvable-factor column bounds G∩S; it is not an equality unless the source explicitly says so.

The following table routes every finite row to its canonical proof and exact independently accepted source. Degrees are socle indices; a displayed degree can be rejected by primitivity before the loop argument.

| Table 1.2 rows | Degrees or alternatives | Reviewed route and source |
|---|---|---|
| 1,3,4,5,9,10,21,23,28 | respectively 11,57,203,1711,155,27,4617,3159,28431 | Odd full-group argument below |
| 2 | 68 | [First finite batch](#proposed-finite-table-exclusions-from-orders-and-rank), `e4eb963d4091f8e3daa5554f3f45b6d610b552a8` |
| 6 | 1080 or 40 | First finite batch at `e4eb963d4091f8e3daa5554f3f45b6d610b552a8`; [degree-40 proof](#proposed-degree-40-psl4-exclusion) at `8f22211fbd9d0e3c48347ecf65a037155ed428dd` |
| 7,8 | 2106,24192 | First finite batch at `e4eb963d4091f8e3daa5554f3f45b6d610b552a8`, reusing the checked all-field PSL4 divisibilities |
| 11 | 432,27,216,72,36 | [All actual PSp4(3) stabilizers](#proposed-complete-finite-psp43-stabilizer-exclusion), `f448cb7258d6783674b977534f3b8ff5071ba1c0` |
| 12–15 | q²(q²−1) or half, q=5,7,11,23 | First finite batch at `e4eb963d4091f8e3daa5554f3f45b6d610b552a8`, using the reviewed odd-field PSp4 action |
| 16 | 72 or 36 | [Sp6 plus action](#proposed-finite-sp6-plus-action-exclusion), `8c96ae3a6eef47209bf95fd96f20caf82752e660` |
| 17,19 | 155520,50 | First finite batch at `e4eb963d4091f8e3daa5554f3f45b6d610b552a8` |
| 18,20,24 | 36,162, and 6480 or 3240 | [Geometric bridges](#proposed-remaining-geometric-finite-row-bridges), `8f22211fbd9d0e3c48347ecf65a037155ed428dd` |
| 22,25,27 | 1080,120,1080 | [All-class orthogonal ranks](#proposed-all-class-rank-three-finite-orthogonal-exclusions), `ae88d5ffa7c25ac899aa3187cd4c3c4ef0d74a8e` |
| 26 | 960 | [Geometric/triality proof](#proposed-degree-960-orthogonal-exclusion), `758b3fe1a625ea77993270d02ea478e5cf90df80` |

For the odd-degree rows, apply the [odd full-multiplication theorem](odd-envelope-parameterization.md#right-translation-sign-and-the-odd-alternating-full-group), independently accepted at `9d264c0592297ba01a4d8d49b29a9e29ae6367e4`: M=A_n in its natural action, for n=|X|. None of the displayed S is A_n. In the degree-eleven row |S|=660<11!/2. In every other listed odd row n≥27, and the standard displayed classical group orders satisfy |S|<2^50<27!/2≤n!/2. For example the largest order in this odd-row list is |PSU4(8)|=34,693,789,777,920<2^50; no larger-order bound on all finite classical groups is claimed. Thus their socle orders disagree with that of M=A_n. This invokes the completed odd theorem, including its separately reviewed row-28 input, rather than the earlier historical odd assembly that left that row open. It adds no new reliance on C0011 beyond the existing dependencies of that theorem.

The other row proofs in the table supply exclusions directly, except the Paige conclusions for rows 25 and 27, which the Moufang paragraph eliminates. Row 22 has corrected index 1080, not the earlier transcription 108; its proof excludes the possible Paige M(3) by full-group socle mismatch. Row 11 includes the 2⁴:A5 alternative and treats maximal stabilizers in both actual ambient groups; it does not assume J is maximal in S. Row 26 is the distinct A9 action and uses its own geometric proof, not the rank-three certificate for row 25. All 28 rows and all nine infinite rows are thereby covered under their combined stated inputs.

This is an assembly of conditional, independently reviewed deductions; the assembly has the separate exact-source reviews below. It retains CFSG, the cited factorization and action classifications, pinned character/fusion data and the exact algorithms used by the finite certificates. It neither reproves these inputs nor turns their verification runs into a proof of unrestricted classification. The next separate obligations are Li–Xia's both-solvable, alternating and sporadic branches; the natural alternating action and nonsolvable LMlt, radicals and operation-level construction/isomorphism remain open even after this table conclusion.


### Independent review of the combined classical tables

automated-model reviewer A, reviewer B and reviewer C independently accepted this combined assembly at exact source `3313726ad58aa11de1c79e04d4618f28380925fb`. Each checked coverage of all nine infinite and all 28 finite rows, the distinct actual-action interfaces, the completed odd theorem and its noncircular dependency, the odd indices and order bound, and the Moufang quotient argument eliminating the Paige exceptions under solvable LMlt. They retained the prior exact-source reviews, classification and character/fusion inputs, and finite-certificate algorithms; they did not rerun unchanged certificates or newly reprove the underlying classifications. No additional fresh primary-source inspection was claimed. This acceptance closes the two-table deduction only, not the other factorization branches or C0010.

## Proposed alternating-socle reduction at arbitrary parity

**Conditional deduction with three independent mathematical reviews below.** In 0323-finite-simple-non-moufang-bol-loops:C0010, let X be finite simple nonassociative left Bol, G=LMlt(X) solvable, M=Mlt(X) with socle S=A_m, and I=M₁ **unsolvable**. Under C0001/C0008, the Johnson-orbital subproof [C0009 Theorem 1.2(1)](../foundations/C0009.md), the reviewed all-parity metabelian exclusion above and Li–Xia arXiv:1408.0350v3 Proposition 4.3/Table 4.2, the actual permutation action of M is the natural action of A_m or S_m, up to a socle automorphism. No parity hypothesis is imposed. This does not classify the natural-action loop operations; the case of solvable I belongs to the separate both-solvable analysis.

Apply Proposition 4.3 to the actual factorization M=GI; simplicity makes I maximal and core-free. In case (a), I lies in the natural point stabilizer and contains A_(m−1). Maximality makes it the full point stabilizer in M, giving the natural action. In (b) and (c), I lies respectively in the stabilizer of a two-subset or three-subset. Those proper subgroups must equal I by maximality. Here the two-subset case has m≥6, and the three-subset case has m=8 or 32, so 2≤k<m/2 throughout. The actual A_m or S_m action has the Johnson distance orbitals. Its disjointness relation contradicts C0008's uniform orbital displacement: a permutation a taking a fixed k-set E to a disjoint set has a moved point i, and a k-set Y containing i and a(i) satisfies a(i)∈Y∩a(Y). This is precisely the cited Johnson subproof; it makes no assumption that G itself is primitive.

In cases (d),(e), S=A6 and I is A5 or S5. Since S is transitive, M=SI, and the resulting index [S:I∩S] is six. Each A5 class gives a natural six-point action after an automorphism of A6. In Table 4.2 rows 1–4, the displayed A5 or S5 subgroup instead has IS properly between I and M (of index two or four in M), contradicting primitivity. Thus the exceptional almost-simple extensions do not introduce another primitive action.

Table 4.2 rows 5–6 have actual solvable factors among C15, C3×D10, ΓL1(16)=15:4, D30, S3×C5, S3×D10, C3×AGL1(5), and S3×AGL1(5). Each is metabelian: its derived subgroup is abelian, including in these direct products and cyclic-by-abelian semidirect products. The [all-parity metabelian theorem](#proposed-all-parity-exclusion-of-metabelian-left-multiplication-groups), independently accepted at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`, excludes G in all these cases. These are actual factor shapes, rather than an unjustified equality with an ambient upper bound.

The source authors inspected Li–Xia v3 Proposition 4.3 on printed p.28 and Table 4.2/p.29; preliminary contributor a research reviewer separately rechecked the exceptional A6 alternatives. The source classification and its stated Magma computations remain external inputs. No new computation is used here. The exact-source independent reviews are recorded below; the deduction does not restrict the admissible solvable transitive G in the surviving natural action beyond the other canonical results.


### Independent review of the alternating-socle reduction

automated-model reviewer A, reviewer B and reviewer C independently accepted the all-parity alternating-socle reduction at exact source `4922123613711b1884764a672d0091afabd5d991`. All checked the actual point/subset action from maximality, the Johnson displacement contradiction, the A6 automorphism and intermediate-subgroup cases, and every displayed metabelian factor. reviewer A freshly opened Li–Xia Proposition 4.3 and Table 4.2, pp.28–29; reviewer C retained a prior direct inspection, and reviewer B used the stated source inputs without a fresh read. No new computation was needed. They retain the source classification/Magma inputs and the prior canonical results. The acceptance assumes unsolvable I and classifies only the possible full action, not the natural-action operations.


## Proposed generic PSL2 both-solvable factor exclusion

**Conditional deduction for 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical/code reviews below.** Let X be a finite simple nonassociative left Bol loop, G=LMlt(X), M=Mlt(X), I=M₁ and S=Soc(M). Assume the canonical generating section/inversion, primitive almost-simple full-Mlt and minimum-order inputs C0001/C0007/C0008/C0011, with their recorded scopes. Suppose the actual factorization M=GI is in Li–Xia arXiv:1408.0350v3, Theorem 1.1(a), Proposition 4.1(a), printed p.27: S=PSL₂(q), q=p^f, d=(2,q−1); one socle intersection is contained in the nonsplit dihedral normalizer N of order 2(q+1)/d, and the other lies in the Borel B=U:C with U of order q and C of order (q−1)/d and contains U. Then this configuration is impossible, conditional on the stated standard subgroup/automorphism, primitive-divisor and finite-certificate inputs. The argument distinguishes the two orientations; it never assumes LMlt primitive or the marked set full.

### Borel point stabilizer

If I∩S is the Borel-side intersection, it contains U and lies in B; its p-core is U and U is characteristic in I∩S. Hence I normalizes U and the actual full action is the projective-line action. The G-side intersection lies in the nonsplit projective Singer normalizer. This is exactly the n=2 specialization of the reviewed all-parity linear Singer-row exclusion in [the preceding Singer section](#proposed-exclusion-of-the-linear-singer-row-at-even-order); its odd case also follows from the reviewed odd full-Mlt result. The source row-1 proof uses actual subgroup containment and the normal U, not an assumption that I∩S equals B.

### Nonsplit point stabilizer: actual action

Now let G be on the Borel side and J=I∩S≤N. The p-core of G₀=G∩S is U: G₀/U is a p′ subgroup of the Borel torus. Since G₀◁G, U is normal in G, and normalizing U forces the full G into the natural affine semilinear point stabilizer U:ΓL₁(q). Also |G|≤[q(q−1)/d]·2f, while |S|=q(q²−1)/d. Thus J≠1: otherwise transitivity would force |S|≤|G|, contrary to q+1>2f for q≥4. Since J◁I, I≤N_M(J). A nontrivial proper J cannot be normal in S, so N_M(J)<M. Primitivity makes I maximal, hence I=N_M(J) and N_S(J)=J.

A cyclic subgroup J of order 2 is not self-normalizing: its S-centralizer is dihedral of order at least four in odd characteristic, and contains the elementary unipotent group of order q in characteristic two. If J≅V₄, it is also not self-normalizing. For odd q, lift its generators to i,j∈SL₂(q) with i²=j²=−I and ij=−ji. Then t=(I+i+j+ij)/2 has determinant 1 and cyclically permutes their projective images; this is an explicit A₄≤N_S(J), also in characteristic 3. In characteristic two N has odd rotation order, so it contains no V₄. Every remaining subgroup of N is cyclic or dihedral with characteristic rotation subgroup C_d of order d>2. The S-centralizer of a nontrivial order>2 element of the nonsplit torus is that torus and its normalizer is N. As I normalizes C_d, it normalizes N; N_M(N) is proper. Primitivity forces I=N_M(N) and J=N.

Thus the actual S-set of loop points is S/N of degree q(q−1)/2, with trivial S-permutation centralizer. The actual full action is the corresponding Aut(S)-class stabilizer action, including field and diagonal outer automorphisms. PSL₂(2), PSL₂(3) are nonsimple and are excluded as socles. q=4 or 5 gives degree 6 or 10, excluded by the reviewed minimum order 24.

### Odd fields: perpendicular geometry

For odd q, the coset action S/N is the orbit Ω of anisotropic projective points of one fixed norm-square type on a nondegenerate 3-dimensional quadratic space. Its size is q(q−1)/2, and Aut(S)=PΓO₃(q) in this natural model (including the q=9 exceptional presentation). The perpendicular relation is invariant under the entire semilinear action and nonempty on Ω: the anisotropic binary perpendicular complement represents every nonzero field value. C0008's UOD consequence says that a loop translation to a perpendicular point would be represented by an invertible semilinear map g sending every point of Ω to a perpendicular point.

Write g(x)=A x^{p^s} with 0≤s<f and F(x)=B(x,A x^{p^s}), a homogeneous form of degree D=p^s+1. For a nonzero homogeneous form of degree D<q, its number of projective Fq zeros is at most D(q+1). The degree bound ensures that its evaluation is not identically zero on Fq³, by induction on the variables and the univariate root bound; choose a projective point P where it is nonzero. On each of the q+1 projective lines through P, the restriction is a nonzero binary form of degree D, so has at most D zeros. These lines partition all projective points other than P, proving the bound.

For s=0 and q≥7, |Ω|=q(q−1)/2>2(q+1). Thus F is identically zero. Its coefficient matrix is skew-symmetric, impossible for an invertible map in odd characteristic and odd dimension. For s>0, p^s≤q/3 and every nonprime odd q≥25 satisfies |Ω|>(q/3+1)(q+1)≥D(q+1). Hence F is identically zero; as p^s>1, the monomials x_i x_j^{p^s} are distinct, forcing the whole matrix of B A to vanish, again impossible. The sole nonprime odd field below 25 is q=9.

For q=9 take F9=F3[i]/(i²+1), encoding a+bi as a+3b. View Ω as the nonsquare-discriminant binary quadratic-form points (a,b,c), discriminant b²−ac. The nine points

 (1,0,4), (1,0,5), (1,0,7), (1,1,3), (1,1,5), (1,1,6), (1,2,3), (1,2,5), (1,3,3)

all have nonsquare discriminant. The 9×9 matrix whose row is (x_i x_j³)_(0≤i,j≤2) has determinant i. Thus no nonzero coefficient matrix can vanish on these nine points, excluding σ:x↦x³; the linear case is already covered by the preceding degree-2 bound. [The standalone exact-F9 certificate](../code/verify_psl2_q9_nine.py) was read and run by the source authors with Python 3.12.14: `9 nonsquare-discriminant points; determinant i; rank 9 over F9`. It uses only the displayed arithmetic and nine points, with no network, package or uncommitted-file dependency. Independent proof/code reviews are recorded below.

### Even fields: canonical inversion and the affine group

Let q=2^f≥8. In G≤U:ΓL₁(q), put D=G/U≤Fq×:C_f, C=D∩Fq× and c=|C|. The degree q(q−1)/2 divides |G|=q|D|, so the odd number n=q−1 divides c·e, where e=|D/C| divides f. Consequently n/c divides f.

We have ord_c(2)=f. Otherwise its value is a proper divisor ≤floor(f/2), giving c≤2^floor(f/2)−1, whereas c≥(2^f−1)/f and 2^f−1>f(2^floor(f/2)−1) for f≥3. For f=2k this follows by dividing by 2^k−1 and using 2^k+1>2k; for f=2k+1 use 2^(k+1)>2k+1 and 2^(2k+1)−1>2^(k+1)(2^k−1). Therefore C_D(C)=C. A normal 2-subgroup of D centralizes its normal odd subgroup C and lies in that odd centralizer; it is trivial. Consequently U=O₂(G), so canonical τ descends to D.

For f≠6, Zsigmondy gives a primitive prime r of 2^f−1, with ord_r(2)=f and r>f. As n/c divides f, C contains its full Sylow r-subgroup, which is unique and characteristic in D. The reviewed cyclic-normal inversion obstruction makes the D-conjugation image on it exponent at most 2. Since the field image acts faithfully on r, e≤2. For f=6, use r=7: C contains C7 because 63/c divides 6, the Sylow 7 is characteristic, and ord₇(2)=3; the same obstruction forces the field exponents to be divisible by 3, again e≤2. The primitive-prime input is the same source as the reviewed odd Singer-row arguments.

Since n is odd, n|ce and e≤2 force c=n; C is the full Singer torus. If e=1 then D=C, and τ induces inversion on it. Its restriction α=τ|U is an involutory F₂-linear map normalizing C, so α=a·Frob₂^j in the Singer normalizer ΓL₁(q). The condition α²=1 gives 2j≡0 mod f. Hence j=0 or, if f is even, f/2; neither exponent induces inversion on C for f≥3.

If e=2, f=2k and s=2^k. Write C=C₊×C₋ with orders s−1,s+1. The field coset centralizes C₊ and inverts C₋, so D′=C₋ and, since C_D(C)=C, Z(D)=C₊. Thus C=D′Z(D) is characteristic in D. Moreover C₊ embeds in D_ab, so τ inverts it. On U, α normalizes the full Singer C and is involutory, so its field exponent is 0 or k; both fix C₊ pointwise. As f≥4 gives |C₊|=2^k−1>1, contradiction. For f=2 the degree is 6, already excluded.

No inference from τ-inversion to inversion on a general derived cyclic subgroup is used: the characteristic C and the injective central C₊→D_ab are proved before applying it. This excludes the even branch conditional on Zsigmondy, Singer normalizer, the canonical inversion and the source subgroup inputs. Together with the odd perpendicular argument and q9 certificate, it completes this one generic PSL₂ factor orientation. It does not resolve Li–Xia's Table 4.1 exceptions or general nonsolvable LMlt.


The source factorization is Li–Xia arXiv:1408.0350v3 Proposition 4.1(a), printed p.27, directly inspected by the source authors. Its Theorem 2.3 supplies the same Zsigmondy input and exception convention as the earlier Singer proof. The full classical automorphism and Singer-normalizer inputs are those already cited in this manuscript (Kleidman–Liebeck §2.1, pp.14–16; Hestenes pp.497,499). The PSL2 involution centralizer and torus normalizer descriptions, natural degree-three orthogonal realization, and elementary quaternion calculation are explicit group-theoretic inputs/arguments subject to the requested review. Preliminary proof development came from a research reviewer and a research reviewer, with coordinator repairs to the projective zero count. No stronger statement about other factorization rows follows without their separate proofs.


## Proposed finite both-solvable PSp4(3) exclusion

**Conditional deduction with three independent mathematical/code reviews below.** For 0323-finite-simple-non-moufang-bol-loops:C0010, retain finite simple nonassociative left Bol X and solvable G=LMlt(X), with M=Mlt(X) primitive almost simple and I=M₁ now also solvable. Li–Xia arXiv:1408.0350v3 Proposition 4.1/Table 4.1 rows 9–11 have socle S=PSU4(2)≅PSp4(3). Under C0001/C0008/C0017 and the complete stored maximal-class/fusion inputs below, none of these rows occurs.

Here M=S or Aut(S), since |Out(S)|=2. The source lists the actual factors up to interchange, not merely upper bounds. Their possible orders, including all displayed outer choices and both orientations, belong to {80,160,320,162,324,648,1296}. In particular row 9 has 2⁴:5 and 3₊^(1+2):2.(A4.O), of orders 80 and 648|O|; row 10 has orders 160|O1| and 648|O2|; row 11 has first factor order 320 and second factor orders 162,162|O|,648,648|O|. These are sufficient upper sets for the comparison; no claim that every combination factors is needed.

Since I is maximal in the actual full M and IS=M, compare with both complete maximal lists. For S their orders are 960,720,648,648,576; for Aut(S) they are 25920,1920,1440,1296,1296,1152. Thus only |I|=648 in S or 1296 in Aut(S) can survive. Each ambient group has two such classes, all of degree 40. The [new certificate](../code/verify_psp43_both_solvable.g) checks the full metadata/order lists, filters all possible source-factor orders, and induces the trivial character along every surviving stored class-specific fusion. All four induced characters have degree 40 and self-inner-product three, so every actual M-action has rank three. No claim that I∩S is maximal in S is used for outer M.

The reviewed C0017 rank-three theorem permits only Paige degrees 120 and 1080, not 40. This excludes all three rows under its exact scope. The source authors read and ran the certificate with GAP 4.15.1 and CTblLib 1.3.11; all four checks passed. The subgroup-class completeness, abstract identifications, character/fusion values and exact GAP algorithms remain external computational inputs. No loop enumeration or uncommitted input is used. Proof/certificate development was by a research reviewer; independent exact-source reviews are recorded below. Other Table 4.1 rows and the unrestricted classification remain separate.


### Independent review of the generic PSL2 and finite degree-40 cases

automated-model reviewer A, reviewer B and reviewer C independently accepted both preceding deductions at exact source `9540690f778bcdb3977fae36f5811be0b6b5d6a2`. All checked the actual PSL2 orientations and normalizers, the quaternion V4 argument, odd-field projective bound and q=9 exception, and characteristic U before inversion, the primitive-prime/f=6 step, full Singer torus and central odd quotient at even q. For the finite case they checked both actual ambient maximal lists and all four degree-40 ranks. Each extracted, read and ran both exact scripts: the F9 determinant was i and every rank calculation passed. The first two used Python 3.12.14; reviewer C used its available `python3` and did not claim that version. All GAP runs asserted 4.15.1/CTblLib1.3.11. reviewer A retained its direct Li–Xia inspection in the preceding review; the other two used the recorded source inspections without fresh reads. Standard automorphism/torus and primitive-divisor inputs, complete class/fusion data, canonical results and C0017 remain dependencies. No formal verification or acceptance of C0010 as a whole is asserted.

## Proposed completion of the finite both-solvable factor table

**Conditional deduction with three independent mathematical reviews of the corrected source below.** For 0323-finite-simple-non-moufang-bol-loops:C0010, let X be finite simple nonassociative left Bol with solvable G=LMlt(X), primitive almost-simple M=Mlt(X), and solvable I=M₁. Under the canonical C0001/C0007/C0008/C0011 inputs, the reviewed odd full-group and all-parity metabelian results, the preceding degree-40 deduction, and Li–Xia arXiv:1408.0350v3 Proposition 4.1/Table 4.1, no finite-table row occurs. Put H=G∩I; the canonical section identifies H=G₁ and |H|=|G||I|/|M|. The source factors are the actual G,I, up to interchange. Throughout O≤C2, O1,O2≤O and O=O1O2. The already proved relation G=HG′ requires H to surject onto every abelian quotient of G.

### Rows 1–6 and 12

For row 1, one factor is 7:O or 7:(3×O), hence metabelian and impossible as G. If G=S4 is the other factor, the degree is 24 or 8. The first makes G regular, and the second is below the reviewed minimum 24. For row 2, 11:(5×O1) is metabelian; in the opposite orientation the full-group index is 12|O|/|O1|, hence 12 or 24. Degree 12 is below the reviewed minimum. Degree 24 requires O=C2, O1=1, O2=C2 and makes G=A4.2 regular of order 24, again impossible. (It also violates IS=M because I lies in S.) For row 3, 23:(11×O) is metabelian, while the opposite factor S4 has order equal to the degree 24 and acts regularly.

Row 4 has factors A=13:O or 13:(3×O), and B=3²:2.S4 of order 432 inside S=PSL3(3)=SL3(3). A is metabelian. If G=B, the degree is 432 or 144; the first is regular. To identify the actual B in the second, its displayed normal E≅3² has a nonzero fixed subspace W in the natural F3³ module, since a finite 3-group in characteristic three has fixed vectors. W is proper because E is nontrivial and the representation faithful. B normalizes E, hence preserves W, of dimension one or two. It is contained in the corresponding natural parabolic, also of order 432, and equals it. Block matrices identify either parabolic with AGL2(3); graph duality identifies the two. Thus no assertion about which double cover is denoted 2.S4 is needed.

For G=V:GL2(3)=AGL2(3), V=O3(G) is characteristic: GL2(3) has no normal 3-subgroup, since its Sylow 3-subgroups of order three are not normal. Every automorphism induces a linear f on V and quotient automorphism ψ with ψ(h)=f h f⁻¹, because the quotient action on V is faithful. After composing with an inner automorphism, f and ψ are identities. The remaining map is a 1-cocycle c:GL2(3)→V, which is a coboundary: the central element z=−I gives 2c(h)=(I−h)c(z). Hence all automorphisms are inner, and G is centerless. Any automorphism τ with τ²=1 is conjugation by an element t with t²=1, including t=1. Multiplication by t bijects the elements inverted by τ with {y:y²=1}. There are exactly 46 such elements: the identity, nine affine lifts of −I, and three affine lifts for each of the twelve linear involutions with eigenvalues 1 and −1. The latter linear centralizer has order four, hence class size 48/4=12. The canonical inverted translation set has 144 elements, a contradiction. This is an analytic count; no finite group enumeration is needed.

Rows 5,6,12 are exact factorizations by their displayed orders. For row 5 the factor orders are 39|O| and 144, whose product is 5616|O|=|M|. In row 6 they are 126|O| and 960, whose product is 120960|O|=|PSL3(4).(S3×O)|. In row 12 they are 55 and 144, whose product is 7920=|M11|. Thus H=1 in either orientation, G is regular, and the loop is associative.

### Rows 7 and 8, including overlapping outer factors

In both rows the product of the two displayed factor orders divided by |M| is |O1∩O2|, hence |H| is one or two. Trivial intersection gives regularity. It remains only O1=O2=O=C2.

In row 7 the factor A=73:(9×2) is metabelian. The other factor B=2^(3+6):7²:(3×2) has the displayed normal 2-group and an abelian quotient C3 from the final 3×2 quotient. If G=B, its stabilizer H has order two and cannot surject onto that quotient. No characteristic-section or inferred field action is needed for this row.

In row 8, S=PSU3(8) has order 5,515,776, M=Aut(S) has order 99,283,968, and the two factors have orders |A|=|57:9.2|=1026 and |B|=|2^(3+6):(63:3).2|=193536. If G=A and I=B, the degree is 513. The completed odd full-group theorem at `9d264c0592297ba01a4d8d49b29a9e29ae6367e4` forces M=A513 in its natural action, contradicting the displayed group order. This avoids treating the extension 57:9.2 as metabelian.

Suppose instead G=B and let U be its displayed normal 2-subgroup of order 512. Do not assume U≤S. Since |M:S|=18, W=U∩S has order at least 256 and is normal in B. Any nontrivial 2-subgroup W of PSU3(8) fixes a unique isotropic projective point in the natural Hermitian three-space. Here is an elementary verification of the needed assertion. Its preimage in SU3(8) is a central extension by the odd center C3, so it has a unique Sylow 2 complement (Schur–Zassenhaus conjugacy and centrality), giving a faithful lift of W. On the 8³+1=513 isotropic points a 2-group has a fixed point. A nontrivial involution z in the lifted W has N=z−I with N²=0 and rank one. Unitarity and z²=I imply N*=N; thus ker N=(im N)^⊥, and the line L=im N is isotropic. Its fixed plane L^⊥ has radical L and a nondegenerate one-dimensional Hermitian quotient, so its only isotropic projective point is L. Every common fixed point of W must be fixed by z, proving uniqueness.

Every automorphism of S acts in the natural projective semilinear unitary action (the graph operation is included in the field operation in this rank-one unitary setting). Since B normalizes W, it preserves that unique point. The full Aut(S) point stabilizer has order |M|/513=193536=|B|, so B is the whole point stabilizer. It surjects onto the field-automorphism group C6, hence onto C3: in a standard isotropic basis the six Frobenius maps fix the standard isotropic point, and conjugation transfers this to any point. This is the usual field map from PΓU3(8) to Gal(F64/F2); scalar/projective and diagonal automorphisms lie in its kernel. Again H has order two and cannot surject onto the C3 quotient, contradicting G=HG′.

This last argument uses the standard full unitary automorphism realization and field map already cited from Kleidman–Liebeck §2.1, pp.14–16, but supplies the fixed-point and order interface explicitly. It makes no assumption that the source's normal 2-group lies in the socle, and does not infer a semilinear action from its abstract group shape.

Rows 9–11 are exactly the preceding independently reviewed degree-40 exclusion at `9540690f778bcdb3977fae36f5811be0b6b5d6a2`. Together the preceding cases exhaust Table 4.1. The source authors read the displayed factorization table and checked the order products. Preliminary contributions came from a research reviewer and a research reviewer; the fixed-space identification in row 4 and final point-stabilizer argument in row 8 were coordinator repairs. The corrected finite-table assembly has the independent exact-source reviews recorded below. The classification/Magma inputs and cited earlier results are retained; no claim of unrestricted loop classification follows.

## Proposed sporadic solvable-factor exclusion

**Conditional deduction with three independent mathematical/code reviews below.** In the same C0010 setting, assume now S=Soc(M) is sporadic and I is unsolvable. Under C0001/C0008/C0011/C0017, the stated Q24 witness input and Li–Xia arXiv:1408.0350v3 Proposition 4.4/Table 4.3, this branch is impossible. This theorem concerns the actual full M and maximal I; solvable I belongs to Proposition 4.1 and is treated separately above.

Proposition 4.4(a) has M12≤M≤M12.2 and I=M11, giving degree 12 or 24. Degree 12 is below the reviewed minimum; in the outer case I is contained in the proper normal subgroup M12, so IS≠M contradicts socle transitivity. Part (b) has M=M24, I=M23 and degree 24. C0011's independently reviewed uniqueness identifies X with Q24. Its separately reviewed witness calculation at `3313726ad58aa11de1c79e04d4618f28380925fb`, recorded in [C0011 proof §3.6](../foundations/C0011.md), gives Mlt(Q24)=A24, whose order differs from M24. Thus part (b) is impossible.

In Table 4.3, rows 1,2,5,6 have degrees 11,12,22,23, below 24. Row 7 has degree 23 or 253; at degree 253 the actual G=23:11 has that order and acts regularly. For rows 3–4 the degree is 144 and the actual G is M9.2 or M9.S3, of orders 144 and 432. The former is regular. The latter has H of order three and the quotient S3 by its normal M9, hence a quotient C2, contradicting G=HG′. The notation M9=3²:Q8 has order 72; Li–Xia's proof of Lemma 8.27, printed p.89, explicitly identifies M9.2=3²:Q8.2, corroborating the orders and normal-series interpretation used here. No splitting of M9.S3 is required.

Rows 8–11 and 13 leave the actual actions J2.2/G2(2), HS/M22, HS.2/M22.2 of degree 100, and Suz.2/G2(4).2 of degree 1782. The row-10 alternative HS.2/M22 of degree 200 is impossible: perfect I=M22 maps trivially to M/S=C2, so IS=S<M. For the other four actions, [the new pinned character certificate](../code/verify_sporadic_factor_ranks.g) reads every complete maximal-class list of the actual full M, filters the required stabilizer order, and checks the stored class-specific subgroup fusion. Each list has exactly the specified class at that order, and each induced trivial character has self-inner-product three and the stated degree. Thus every actual action has rank three. The reviewed C0017 conclusion allows only degrees 120 or 1080 for a finite simple nonassociative Bol loop, excluding all four. This all-class character argument supplies the action coverage directly; no uninspected graph-class conjugacy assertion is required.

Finally row 12 has degree 2058=6·343 and five possible actual factors G, with normal subgroup E of order 343 and quotients C6, C6×C2, C6×C3, S3×C3, S3×C6. The corresponding |H| are 1,2,3,3,6, while the quotient abelianization orders are 6,12,18,6,12. Each exceeds |H|, contradicting G=HG′. These are the five actual quotient shapes in the source, not a guessed cyclic group of order 36. The source's multiple nonisomorphic groups of a listed shape do not affect their common quotient and order contradiction. No rank-three assertion is used for this Held action.

All alternatives of Proposition 4.4 are now covered under the stated inputs. The source authors directly inspected Li–Xia printed p.30 and the M9 identification on p.89, read the four primary CTblLib online maximal lists, and ran the exact certificate successfully using GAP 4.15.1 and CTblLib 1.3.11. Those complete subgroup lists, abstract identifications and character/fusion values remain external data inputs; the certificate does not reprove them. Contributions came from a research reviewer and its bounded Mathieu/action assistants, with the new all-class certificate from a research reviewer. Exact-source independent reviews of this assembly and certificate are recorded below. C0010 remains open.


### Independent review of the sporadic exclusion and finite-table repair

automated-model reviewer A, reviewer B and reviewer C independently accepted the sporadic section at exact source `4e1449bce6a7c14f4b329aad8c4c01e65f10d650`. All checked every Proposition 4.4 route, the small-order and separately reviewed Q24 interfaces, the M9 quotient, actual full-group maximal stabilizers, and all five Held quotients. All read/extracted the exact certificate and independently reran it with GAP 4.15.1/CTblLib1.3.11; its four degree/rank results passed. They retained the recorded primary-source/classification and complete dataset inputs without new primary-source reads in this pass. No formal verification or operation classification is claimed.

For the finite both-solvable section at the same source, reviewer B and reviewer C initially accepted, but reviewer A found that row 2's opposite orientation also permits a full-group index 24 when O1=1, O2=O=C2. The text now states this alternative and excludes it by regularity (and also IS≠M). The corrected finite section and the following combined theorem have the separate reviews at their new exact source recorded below; the earlier finite-section acceptances do not certify this repair. The reviewer accepted the remaining finite arguments subject to that correction.

## Proposed full-action theorem for solvable left multiplication

**Conditional assembly with three independent mathematical reviews below.** Let X be any finite simple nonassociative left Bol loop and suppose G=LMlt(X) is solvable. Under the canonical C0001/C0007/C0008/C0011/C0017 interfaces, CFSG and the precise reviewed factorization, action, character-library and finite-certificate inputs of the preceding sections, its full multiplication group is **A_n or S_n in the natural action on X**, where n=|X|≥24. In particular this full action is two-transitive. This is a necessary full-action theorem, not a classification of the loop operations or of the admissible solvable G.

Indeed C0001/C0008 make M=Mlt(X) primitive almost simple with socle S. The actual point stabilizer I is maximal and core-free. The solvable subgroup G cannot contain nonabelian simple S, so it too is core-free in the almost-simple M. Its transitivity gives M=GI. Li–Xia arXiv:1408.0350v3 Theorem 1.1, printed p.6, gives an exhaustive choice: (a) both factors solvable as in Proposition 4.1; (b) alternating socle as in Proposition 4.3; (c) sporadic socle as in Proposition 4.4; or (d) the classical Tables 1.1/1.2. These are alternatives for the actual factors, not a list inferred from a census.

The combined classical theorem at `3313726ad58aa11de1c79e04d4618f28380925fb` excludes (d), including its Moufang exceptions under solvable G. The generic PSL2 theorem and finite degree-40 cases at `9540690f778bcdb3977fae36f5811be0b6b5d6a2`, together with the corrected finite-table proof above, exclude all of (a). The sporadic theorem at `4e1449bce6a7c14f4b329aad8c4c01e65f10d650` excludes (c). Thus (b) remains with unsolvable I, and the alternating-action theorem at `4922123613711b1884764a672d0091afabd5d991` gives precisely the natural A_n/S_n action. C0011 supplies n≥24, so the transported degree-six exceptional presentation cannot survive. No compatibility of abstract τ with M is assumed; τ was used only on its canonical G and proved characteristic sections in the constituent arguments.

For odd n the previously reviewed sign argument sharpens this to M=A_n, but this new assembly does not claim that refinement at even n. Its remaining operation-level problem is substantial: every transitive subgroup G≤A_n already gives A_n=G A_(n−1), so the surviving factorization alone imposes no new restrictions on odd solvable G. The canonical marked section, subgroup-collision condition, simplicity and isomorphism data must still be classified. Nonsolvable LMlt is entirely outside this theorem. In particular neither C0010 nor 0323.CLASSIFY is closed by this reduction.


### Independent review of the corrected finite table and full-action theorem

automated-model reviewer A, reviewer B and reviewer C independently accepted both the corrected finite Table 4.1 section and the complete solvable-LMlt full-action assembly at exact source `7f456116c2e6ca420c7c15c789c96ee105050c1b`. Each checked the missing row-2 outer orientation and its regularity/IS≠M repair, core-freeness of solvable G, the exhaustive routing of Li–Xia Theorem 1.1(a)–(d), the stated prior exact-source dependencies, the n≥24 boundary and the odd-only sign refinement. reviewer B explicitly acknowledged that its earlier finite-table acceptance missed the row-2 orientation. All retain the precise canonical, CFSG, factorization, subgroup, character/fusion and finite-computation inputs; no reviewer claimed a fresh primary-source inspection or reran unchanged code in this assembly review. This is independent model review, not formal verification or a human approval. The accepted conclusion determines the full action when G is solvable; it leaves operation-level construction/isomorphism and nonsolvable G open.


## Proposed exclusion of every PSL2 full-multiplication socle

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical and code reviews below.** Under the cited canonical, almost-simple, factorization and finite-algorithm inputs, no finite simple nonassociative left Bol loop has full multiplication group with socle PSL2(q), for any q≥4. The left multiplication group may be solvable or nonsolvable. This excludes a full socle family, not every remaining almost-simple full action.

Write M=Mlt(Q), G=LMlt(Q), I=M_1, H=G_1, and S=Soc(M)=PSL2(q). C0001/C0008 make M primitive almost simple, I maximal and core-free, and M=GI. The identity G=HG′ and minimum |Q|≥24 have the same pinned inputs as the preceding full-action theorem. If G contains S, then S≤G≤M≤Aut(S), so the [new almost-simple canonical-overgroup theorem](radical-free-inner-inversion.md#all-almost-simple-psl2-canonical-overgroups) excludes it. This is a new dependency whose exact review is separate from the previously reviewed whole-group G=S case.

If G is solvable, the [full-action theorem](#proposed-full-action-theorem-for-solvable-left-multiplication), reviewed at `7f456116c2e6ca420c7c15c789c96ee105050c1b`, gives S≅A_n with n=|Q|≥24. This cannot be PSL2(q). For even q its Sylow 2-subgroups are elementary abelian, whereas A_n contains a nonabelian D8 (its regular degree-eight action consists of even permutations). For odd q, its Sylow 2-subgroups are dihedral and have elementary-abelian 2-rank at most two, whereas A_n contains V4×V4 on two disjoint four-point blocks. These PSL2 facts follow from the standard unipotent Sylow subgroup in even characteristic and the dihedral involution centralizer in odd characteristic, as in the pinned Guralnick–Zieve Lemma A.3 input of the canonical PSL2 proof.

We may therefore assume G is nonsolvable and does not contain S, so G is core-free in M. For q∉{4,5,9}, Li–Xia v3, Theorem 3.3, Table 3.1 and Corollary 3.4, printed pp.23–25, classify this nontrivial factorization. In dimension two its generic alternative has both factors solvable. The table's nonsolvable-factor possibilities are A5 at q=11,19,29,59, and the single q=16 factor (A5×2).2 of order 240. The A5 possibility is excluded by the reviewed canonical G=PSL2(4) theorem at `88f2b7c0260426c220b3d5ec4272fed9d7801255`.

In the q=16 row, the actual full group is PΓL2(16), the point stabilizer is 17:8 and the loop degree is 120. Thus |H|=240/120=2. In G=(A5×2).2, the displayed normal A5×2 has characteristic derived subgroup A5, so this A5 is normal in G. Its order-four quotient is abelian and A5 is perfect; hence G′=A5 and |G/G′|=4. The identity G=HG′ requires H to surject onto a quotient of order four, impossible for |H|=2. This uses the actual degree-120 action, not the natural degree-17 action.

For q=4,5, S=A5. Every proper subgroup of S is solvable, and G/(G∩S) is a subgroup of the abelian Out(S). Thus core-free G is solvable, contrary to the standing case. For q=9, S=A6. Every nonsolvable proper subgroup of A6 is A5: the finite certificate below checks that every nonsolvable maximal subgroup is A5 and that every proper subgroup of A5 is solvable. Consequently G∩S=A5. It is normal in G, and G/A5 embeds in Out(A6)≅C2², so G′=A5. Therefore

    |Q|=[G:H]=[A5:H∩A5] divides 60.

The minimum-order bound leaves 30 or 60. Neither is a primitive degree for any group A6≤M≤Aut(A6), as the complete finite check below establishes. This does not infer that A5 or G is regular merely from a degree bound.

The certificate [verify_psl2_small_full_socles.g](../code/verify_psl2_small_full_socles.g), pinned to GAP 4.15.1, constructs A5, A6 and Aut(A6), verifies the relevant maximal-subgroup types, and forms all five inverse images of subgroups of the outer V4. It computes all maximal subgroup conjugacy-class representatives in each inverse image and checks that neither index 30 nor 60 occurs. It includes maximal subgroups containing the socle as well; that does not weaken the exclusion. The five complete index multisets are recorded by the program. The mathematical argument retains GAP's finite automorphism, subgroup-enumeration, isomorphism and maximal-class algorithms as explicit computational inputs. The script supplies no stored maximal-subgroup list or character table and enumerates no loop tables; the internal algorithms and data shipped with GAP remain part of the pinned implementation.

The source authors directly inspected Li–Xia's exact theorem/table pages, read and ran the finite source, and assembled the proof with a research reviewer and a research reviewer. Li–Xia's classification, including its source computations, is an external input rather than a reproduced classification. The canonical theorem above uses the earlier reviewed square-class and inner-inversion interfaces with their source limitations. This assembly and its finite certificate have the independent exact-source reviews below; C0010 and the unrestricted classification remain open.

### Independent review of the full PSL2 socle exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted this assembly and the new canonical-overgroup section at exact source `47b07688a82d3df93f537946fe0780112200383b`. They checked the exhaustive partition according to G, the alternating Sylow contradiction, the actual q=16 degree and abelianization, and the A5/A6 exceptions. Each extracted the committed `verify_psl2_small_full_socles.g` and ran it with GAP 4.15.1: the A5/A6 maximal-type assertions and all five intermediate-group index exclusions passed. reviewer A freshly inspected Li–Xia v3 Theorem 3.3, Table 3.1 and Corollary 3.4; the other two retained the recorded source inspection without a fresh browse in this review. None rederived the source classification or GAP algorithms. The accepted theorem retains the stated canonical, CFSG/factorization and computational inputs and excludes only this full-socle family. C0010 remains open.

## Proposed exclusion of odd-prime-dimensional unitary full socles

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical reviews below.** Under the stated canonical, almost-simple, automorphism and Li–Xia inputs, no finite simple nonassociative left Bol loop has full multiplication socle PSU_n(q) with n≥3 an odd prime and that socle nonabelian simple. This includes n=3 and all q in the simple range; no solvability assumption is imposed on LMlt. Composite unitary dimensions are outside this full-socle conclusion.

Write M=Mlt(Q), G=LMlt(Q), I=M_1 and S=Soc(M). The pinned canonical C0001/C0007/C0008/C0011 interfaces used above give primitive almost-simple M, core-free maximal I, M=GI, G=HG′ for H=G_1, and |Q|≥24. If S≤G, the [new odd-dimensional almost-simple canonical theorem](../factor-permutation/radical-free-three-dimensional-linear-unitary.md#almost-simple-odd-dimensional-linear-and-unitary-canonical-groups) excludes G. This is a new dependency with its own exact-source review, not covered by the earlier entire-group G=S exclusions.

Otherwise G and I are both core-free in M. Li–Xia arXiv:1408.0350v3, Theorem 3.5, Table 3.2 and Corollary 3.6, printed pp.25–26, give the exhaustive list of such nontrivial factorizations. The table contains only S=PSU3(3), PSU3(5), PSU3(8). In particular its absence of larger prime-dimensional socles forces S≤G in those cases, not G=M; factors containing S are outside the source's meaning of nontrivial factorization. The source authors and reviewer A directly inspected this theorem and table. Its classification and source Magma computations remain external inputs.

If G is solvable, the reviewed full-action theorem at `7f456116c2e6ca420c7c15c789c96ee105050c1b` makes S≅A_N for N=|Q|≥24. The three possible unitary socle orders are 6048, 126000 and 5515776, using |PSU3(q)|=q³(q³+1)(q²−1)/(3,q+1). Each is less than |A24|=24!/2, giving a contradiction. Thus G is nonsolvable.

In Table 3.2 rows 1–2 the nonsolvable factor is PSL2(7) or PGL2(7), excluded as actual canonical G by the almost-simple PSL2 theorem reviewed at `47b07688a82d3df93f537946fe0780112200383b`. In rows 3–5 it is A7 or S7, excluded by the short canonical argument below. Row 6 has both factors solvable and was already removed. These are statements about the actual factors in the table, with either orientation allowed; no maximality of an abstract subgroup of the displayed order is inferred. They exhaust the core-free case.

### The small alternating canonical factors

Here is a direct argument in the nonassociative scope, avoiding dependence on the complete alternating-group exclusion in the aggregate C0007 statement. Retain the standard Aut(A7)=S7 automorphism input used in C0007 proof, Theorem 3.1, Step 1, together with the pinned general inner-inversion theorem. For G=S7, restriction to its characteristic socle A7 embeds Aut(G) into Aut(A7)=S7; every image is already an inner restriction. Thus τ is inner, contradicting O2(G)=1.

For G=A7, inner τ is again impossible. An outer τ is represented by an odd involution of S7. In its odd coset there are exactly two A7-conjugacy classes: transpositions, of size 21, and products of three disjoint transpositions, of size 105. Their S7 classes do not split under A7 because their centralizers contain the odd involution itself. The actual Λ is one class or both, so |H|=2520/|Λ| is respectively 120, 24 or 20, always even.

There is one internal A7 involution class, the double transpositions. It lies in the square of each outside class. For the transposition class use (12)(34). For the triple-transposition class use the two commuting involutions (12)(34)(56) and (12)(35)(46), whose product is (36)(45). A7 conjugation covers all double transpositions; that class does not split since its S7 centralizer contains (12). Thus every internal involution lies in Λ², contradicting Cauchy's theorem and H∩Λ²=1. This proves both small canonical exclusions using the actual selected classes, with no Moufang/proper distinction and no new computation.

The factorization assembly was developed by the source authors with a research reviewer and reviewer A. An early scratch inference G=M from the absence of nontrivial factorizations was corrected to S≤G before this canonical source: the proof does not assume primitive LMlt. The local A7/S7 automorphism fact, previous full-action and PSL2 results, and new almost-simple unitary proof remain explicit inputs. Independent reviews of this exact assembly are recorded below. The unrestricted classification and other full socles remain open.

### Independent review of the prime-dimensional unitary full-socle exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted this assembly and its new canonical-overgroup dependency at exact source `114ce1b011fd47589eb762ed7cd5492a190002d8`. They checked the core-free versus S≤G partition, all Table 3.2 orientations, the finite socle-order comparison, and both selected-class arguments for A7 and S7. reviewer A retained its direct Li–Xia Theorem 3.5/Table 3.2 inspection made during the immediately preceding discovery task; the other two retained the recorded source inspection. None reran the source Magma classification, rederived the external automorphism results, or used a new computation. These are independent model mathematical reviews with the stated canonical and classification inputs. Composite unitary full socles and C0010 generally remain open.

## Proposed odd-field prime-dimensional linear parabolic exclusion

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical reviews below.** Let Q be finite simple nonassociative left Bol, M=Mlt(Q), G=LMlt(Q), I=M_1, H=G_1 and S=Soc(M)=PSL_n(q), where n≥5 is an odd prime and q=p^f is odd. Under the pinned canonical and Li–Xia inputs, the generic parabolic-side alternative of Li–Xia v3 Theorem 3.3(a) is impossible. Together with the reviewed canonical-overgroup and solvable-factor results, this excludes every such S as the full multiplication socle. This theorem does not cover n=3, even characteristic or composite n.

### The actual affine action and characteristic radical

Put m=n−1 and G0=G∩S. In the alternative considered here, Li–Xia Theorem 3.3(a), printed p.23, gives simultaneously

    U:SL_m(q) ≤ G0 ≤ P1 or P_(n−1),
    I∩S ≤ projective Singer normalizer.

Here U has order q^m. The first displayed subgroup is normal in G0, as stated in the source. More explicitly its perfection, using [U,SL_m(q)]=U and perfect SL_m(q), together with the cyclic parabolic quotient shows that it is G0's derived residual and hence characteristic. Its p-core is U. Thus U is normal in G. Work with the point parabolic; the dual case is identical.

The normalizer of U in Aut(S) is the semilinear point parabolic. The point is recovered as the common fixed line of U in the natural n-space. A graph operation sends U to the opposite type, whose common fixed space has dimension n−1; no inner-diagonal or field operation changes that dimension. Thus an automorphism normalizing U cannot have graph component. The standard Steinberg automorphism description and these block matrices give a faithful affine semilinear realization

    G = U⋊D ≤ U⋊ΓL_m(q),       SL_m(q) ≤ D.             (1)

The Levi action on U is, up to the dual convention, A↦det(A)A. Its scalar kernel λ^(m+1)=1 is precisely the center removed in PSL_n(q); its SL_m(q) subgroup acts faithfully since gcd(m,m+1)=1. Equivalently the full PGL point parabolic has faithful affine Levi action GL_m(q). Since G contains U, every element of its projected D has its zero-translation lift in G, proving the splitting in (1); no complement is presumed for an arbitrary extension.

Write L=SL_m(q). This is normal in D and D/L is solvable. A normal p-subgroup of D intersects L trivially, because O_p(L)=1, and hence centralizes L. Its centralizer in ΓL_m(q) is the scalar F_q^×: commuting with all root transvections forces the field automorphism to fix every field element and the remaining linear map to be scalar. That centralizer has p′ order. Consequently O_p(D)=1 and O_p(G)=U, making U characteristic in G. Since L is perfect and D/L solvable, L=D^(∞) is characteristic as well. These elementary natural-module facts apply to m≥4, q odd; no small-rank exceptional automorphism is invoked.

### Realizing canonical inversion

An automorphism τ of G restricts on U to an F_p-linear map A, and the faithful conjugation action of D on U shows that A normalizes D and its characteristic L. The ring End_L(U) is exactly F_q: the root transvections generate the full matrix algebra Mat_m(F_q), whose centralizer on the underlying F_p-space consists of these scalars. Thus A normalizes that field, and composing A with the inverse of its induced field automorphism makes it F_q-linear. Therefore A∈ΓL_m(q).

Conjugation by the affine element (0,A) normalizes (1). Composing its inverse with τ gives an automorphism fixing U pointwise and acting identically on G/U=D, by faithfulness of the D-action. It has the form (u,d)↦(u+b(d),d) for a 1-cocycle b:D→U. The central element z=−I of L acts as −1 on U. For d∈L, the cocycle identity at zd=dz gives

    (z−1)b(d) = (d−1)b(z).

As z−1 is invertible, b|L is a coboundary. Subtract that coboundary from b. Because L is normal in D, the remaining cocycle values are L-fixed; U^L=0 makes them zero. Hence every τ is realized by an affine semilinear normalizer a of G. The centralizer of G in the affine semilinear group is trivial: centralizing all translations forces trivial linear part, and the resulting translation must be fixed by L. Thus τ²=1 implies a²=1.

The formal map G⋊⟨τhat⟩→U⋊ΓL_m(q), sending τhat to a, need not be injective on the entire extension if τ is inner. It is injective on G and consequently on the outside coset τhat G. In particular the actual |Λ|=|K| distinct marks give that many distinct affine semilinear elements of order at most two. This is all that the count uses; no extension of τ to M is assumed.

### Stabilizer and capacity bounds

The full projective Singer torus in PGL_n(q) acts regularly on all points, and also on all hyperplanes. Its intersection with S is therefore semiregular. The Singer normalizer inside S has quotient of order at most n over that cyclic intersection. Because H∩S lies simultaneously in that normalizer and in the point parabolic,

    |H∩S|≤n.

This statement is independent of the relative conjugacy of the Singer subgroup and the parabolic. The graph-free outer image of G has order at most df, where d=(n,q−1)≤n. Hence |H|≤n²f, a bound on the actual stabilizer H, not on the possibly larger factor I. It follows that

    |K|=[G:H] ≥ q^m |SL_m(q)|/(n²f).                    (2)

For linear involutions in GL_m(q), odd characteristic gives ±1 eigenspace dimensions r,m−r, so their number, including identity, is

    sum_(r=0)^m |GL_m(q)|/(|GL_r(q)| |GL_(m−r)(q)|)
    ≤ 4(m+1) q^(m²/2).

The inequality follows from |GL_k(q)|=q^(k²)∏_(i=1)^k(1−q^(−i)), with the product greater than 1/2 for q≥3, and 2r(m−r)≤m²/2. There is at most one nontrivial field component of order two. When f is even, matrix descent for σ:x↦x^(sqrt(q)) gives one GL_m(q)-class of semilinear involutions, with size |GL_m(q)|/|GL_m(sqrt(q))|≤4q^(m²/2). The elementary fixed-space descent is the same one proved in the odd-dimensional linear manuscript; no assertion about general automorphism-class counts is used. At most q^m translations occur above each semilinear map. Consequently

    |Λ| ≤ 4(m+2) q^(m²/2+m).                            (3)

On the other hand, |SL_m(q)|=q^(m²−1)∏_(i=2)^m(1−q^(−i)), and this product is at least 1−∑_(i=2)^∞3^(−i)=5/6. Comparing (2) and (3) would require

    q^(m²/2−1) ≤ (24/5)(m+1)² f (m+2).                 (4)

The reverse strict inequality holds uniformly. At m=4,p=3,f=1 its sides are 2187 and 720. For fixed m, q=p^f≥3^f, and 3^(f(m²/2−1))/f increases with positive integer f, so f=1 is the minimum ratio. Increasing even m by two multiplies the exponential by 3^(2m+2), whereas the polynomial ratio is ((m+3)/(m+1))² (m+4)/(m+2)<4 for m≥4. Thus the ratio increases with m as well. This proves the contradiction without finite arithmetic exceptions or group enumeration.

### Full-socle consequence

If S≤G, the odd-dimensional canonical-overgroup theorem reviewed at `114ce1b011fd47589eb762ed7cd5492a190002d8` excludes it. Otherwise M=GI is a nontrivial core-free factorization. In the present n≥5, odd-q range, Li–Xia Theorem 3.3 has no exceptional table row, so its generic alternative applies. If G is Singer-side, it is solvable, and the completed classical solvable-factor exclusion at `3313726ad58aa11de1c79e04d4618f28380925fb`, retained in the reviewed full-action theorem at `7f456116c2e6ca420c7c15c789c96ee105050c1b`, excludes it. The opposite orientation is exactly the parabolic case just proved. These cases exhaust this full-socle family.

The source authors and a research reviewer developed the characteristic-radical, cocycle and capacity proof; the sharper stabilizer bound removes an earlier unnecessary finite-arithmetic attempt. The source authors directly inspected Li–Xia Theorem 3.3 and its exception list. The factorization and Steinberg automorphism classifications and the pinned canonical interfaces remain external inputs. This proof and assembly have the independent exact-source reviews below. No new computation is claimed, and C0010 remains open.

### Independent review of the odd-field linear capacity theorem

automated-model reviewer A, reviewer B and reviewer C independently accepted this section at exact source `2843ddb186cdf07ad6717e88c68e5f1c215846f9`. Each checked the characteristic radical, actual affine splitting and projective kernel, recovery of the natural-module field, central-involution cocycle argument and marked-coset injection. They checked Singer semiregularity as a bound on H, the linear/field capacities, the strict boundary and monotonicity inequality, and the exhaustive full-socle routing. reviewer A retained its prior direct inspection of Li–Xia Theorem 3.3/Table 3.1; the other reviewers retained the recorded source inspections. None freshly audited Steinberg, rederived the factorization classification or used a new computation. Their acceptance retains the explicit canonical and classification inputs, and covers odd prime n≥5 and odd q only.

## Proposed three-dimensional odd-field linear continuation

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical reviews below.** The preceding full-socle exclusion extends to n=3 and every odd q. Together with the reviewed n≥5 theorem, it excludes every PSL_n(q) full multiplication socle for odd prime n≥3 and odd q, with no assumption that LMlt is solvable. The earlier n≥5 review does not certify this continuation.

For q≥5, let m=2 in the generic parabolic-side case of Li–Xia Theorem 3.3(a). The characteristic-radical and affine realization above remain valid: SL2(q) is perfect, O_p(SL2(q))=1, its natural F_p-module endomorphism ring is F_q, and its central −I acts as −1 on U. The common fixed dimensions of U and its graph image are one and two, so the graph exclusion also remains valid. Thus canonical inversion is realized by an affine semilinear involution, the actual outside marked coset injects, and |H|≤9f. In particular

    |K| ≥ q³(q²−1)/(9f).                                (5)

Use the exact number of permissible translations instead of the preceding coarse q^m bound. An affine element (v,A) squares to identity exactly when A²=1 and (1+A)v=0. In GL2(q), the identity admits one translation; −I admits q²; and the q(q+1) split involutions with eigenvalues 1,−1 each admit q translations. The total with trivial field component is therefore

    1 + q²(q+2).                                       (6)

If f is even, put s=sqrt(q). Matrix descent gives |GL2(q)|/|GL2(s)|=s(s+1)(q+1) linear parts with field component σ:x↦x^s. Each has a fixed F_s-space of dimension two, and in odd characteristic its additive −1 eigenspace also has dimension two over F_s. It consequently admits q translations, giving the additional count

    q s(s+1)(q+1).                                     (7)

If f is odd, no nontrivial field component has order two and (7) is absent. These counts include identity and so bound every possible marked coset, regardless of an inner-inversion kernel in the formal extension.

For f=1 and q≥5, (6) is less than (3/2)q³, whereas (5) is at least (8/3)q³. For f≥2, q≥9. The ratio of (6) to q³ is at most 1+2/9+1/729; when (7) occurs its ratio is (1+1/s)(1+1/q)≤40/27. Their sum is less than 3. But q²−1≥3^(2f)−1>27f for f≥2: the inequality starts with 80>54 and increases under f↦f+1. Thus (5) is greater than 3q³, again a contradiction. No finite arithmetic exceptions or group computation are required.

To assemble the full-socle conclusion, S≤G is excluded by the reviewed odd-dimensional canonical-overgroup theorem at `114ce1b011fd47589eb762ed7cd5492a190002d8`. For q≥5 odd, Li–Xia Theorem 3.3 has no n=3 exceptional row. The Singer-side G is solvable and excluded by the previously reviewed classical solvable-factor theorem; the parabolic side is excluded above. For q=3, the generic parabolic side is itself solvable because SL2(3), the unipotent radical and the remaining diagonal/field quotient are solvable. Both factors in the exceptional Table 3.1 row11 are also solvable. The reviewed full-action theorem would then make Soc(M)=A_N with N≥24, whereas |PSL3(3)|=5616<24!/2. This removes q=3. The nonsolvable-factor exceptions at q=4 are outside the present odd-field theorem and are not claimed solvable.

The source authors developed the sharper affine translation count, which a research reviewer checked in the scratch derivation before this source was committed. That check is not an exact-source independent review. The precise Li–Xia, automorphism and canonical inputs and their access limitations remain those of the preceding section. This continuation has the independent reviews below; even fields, composite linear dimensions and unrestricted C0010 remain open.

### Independent review of the three-dimensional odd-field continuation

automated-model reviewer A, reviewer B and reviewer C independently accepted this continuation at exact source `2a46606e2adac7ef5c08a07447dc73dbb76db267`. They checked transfer of the natural-module and cocycle arguments to SL2(q), q≥5, both exact affine translation counts, the inequalities in both f regimes including q=9 and25, and the separate q=3 generic/exceptional solvability. They retained the prior direct Li–Xia inspections and pinned canonical/automorphism interfaces, without a fresh classification-source audit or new computation. The combined accepted conclusion covers odd prime dimensions and odd fields, not even fields, composite dimensions or unrestricted C0010.

## Proposed exclusion of all odd-dimensional unitary full socles

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical and code reviews below.** Under the stated canonical, factorization, subgroup-list and local-class inputs, no finite simple nonassociative left Bol loop has full multiplication socle PSU_n(q), for any odd n≥3 and any q for which the socle is nonabelian simple. The reviewed prime-dimensional result at `114ce1b011fd47589eb762ed7cd5492a190002d8` handles prime n; the following closes odd composite dimensions. Even-dimensional unitary socles and unrestricted C0010 are outside the conclusion.

### Correct use of the maximal-factorization theorem

Retain M=Mlt(Q), G=LMlt(Q), I=M_1, H=G∩I and S=Soc(M). If S≤G, the independently reviewed odd-dimensional canonical-overgroup theorem applies. Otherwise G and I are core-free in M, M=GI, and IS=M by socle transitivity. Li–Xia arXiv:1408.0350v3, Lemma 2.18(b), printed pp.19–20, passes to M*=GS and a factorization there whose factors have the same intersections G0=G∩S and I0=I∩S with S. Both new factors surject onto M*/S, so part (a) permits core-free maximal overgroups in M*. Theorem 2.15, printed p.18, and Appendix Table A.3, printed p.96, apply to those overgroups. We do not infer maximal overgroups of G in the original M, nor that the actual I is one of the table's maximal factors.

Inspection of all Table A.3 rows leaves only S=PSU9(2) in odd composite dimension. Its row11 gives opposite containments of G0 and I0 in P1 and J3, in some order. This is all the proof requires from the maximal factors. The source authors directly inspected the precise lemma, theorem and table. Their classification, including the cited LPS input, is not reproduced here.

Put g=|G:G0|; it divides |M:S|≤6 by the standard unitary outer-automorphism description. Since |I|=|I0||M:S|, the actual product M=GI gives

    |S| = |G0||I0|g/|H|.

Let P be the one of G0,I0 contained in P1 and J the other, contained in J3. The group orders give |P1||J3|/|S|=1152. Hence, for d=[P1:P] and e=[J3:J],

    d e |H| = 1152 g,      g divides 6.                 (8)

In particular d divides 1152g≤6912. No descent of the factorization to S is assumed, and equality I0=J3 is not needed.

### The actual parabolic intersection is full

Here P1=U:T with T=PSU7(2), and U extraspecial of order 2^15 with center of order two. These projective identifications can be seen directly. On F4 e⊕F4^7⊕F4 f use the Hermitian matrix with e,f paired and the identity form in the middle. Writing bar for squaring, its upper unipotent radical consists of

    u(v,t) = [[1, bar(v)^t, t], [0, I7, v], [0,0,1]],
    v∈F4^7,    t+bar(t)=bar(v)^t v.

There are two t for every v. Multiplication adds the central term bar(v)^t w, and the commutator form on U/Z(U) is Tr_(F4/F2)(bar(v)^t w), nondegenerate on its 14-dimensional F2-space. Thus U is extraspecial and [U,U]=Z(U). A Levi matrix diag(a,B,bar(a)^−1) has B∈GU7(2) and det B=a. The scalar center of SU9(2) is C3; dividing it out removes precisely the scalar factor of GU7(2), leaving SU7(2)=PSU7(2), since gcd(7,3)=1. Its action on U/Z(U) is the natural F4^7 action viewed over F2.

Use the complete [ATLAS U7(2) maximal-subgroup list](https://brauer.maths.qmul.ac.uk/Atlas/clas/U72/), version 2.0, updated 15 April 2005, attributed there to Kleidman. The listed maximal indices are

    2709, 2752, 38313, 89397, 924672, 13561856,
    61997056, 756767784960.

Only 2709 and2752 are at most6912; neither divides1152g for g|6, since each has a factor43. The image of P in T must therefore be all of T: otherwise a maximal overgroup of that image would have index dividing [P1:P], contradicting (8). This uses the stated completeness of the source list, not merely the existence of these subgroups.

Let W=P∩U. Now [U:W]=[P1:P]=d, so its 2-part is at most 2^8 and |W|≥2^7. The T-action on U/Z(U) is irreducible: by the group-order formula T has an element of order43, and its faithful natural action on the 14-dimensional F2-space is irreducible because ord_43(2)=14. Indeed the only nontrivial irreducible F2 representations of C43 have dimension14, so a faithful representation of this dimension has no proper summand. Thus the nonzero image of W in U/Z(U), invariant under the full T image of P, is the entire space. Consequently WZ(U)=U; since Z(U) is central, [W,W]=[U,U]=Z(U), giving W=U. Hence

    P=P1.                                                (9)

The source authors inspected every listed maximal order and index in the primary ATLAS page. Its subgroup classification remains an external input.

### The two original stabilizer orientations

If I0=P1, then |Q|=|S:P1|=43605 is odd. The reviewed odd-order full-action theorem at `9d264c0592297ba01a4d8d49b29a9e29ae6367e4` forces full Mlt to be the natural A_43605. Its socle order differs from |PSU9(2)|=325473292721108444774400, a contradiction.

Suppose G0=P1. Then G/P1 embeds in Out(S) of order six. The group P1 is perfect: T is perfect and irreducibility gives [U,T]Z(U)=U; extraspecial commutators then give [U,T]=U. Thus P1=G^(∞) is characteristic, U=O2(P1) is characteristic in G, and T=P1/U is characteristic in G/U. No assertion that U=O2(G) or that the outer action on U is faithful is needed.

The canonical inversion τ therefore induces an automorphism of this characteristic T section. In the formal E=G⋊⟨τhat⟩, the action on T gives a homomorphism E→Aut(T). Its kernel on G has order |U|·|C_(G/U)(T)|. Since the latter centralizer meets the centerless T trivially, it embeds in (G/U)/T of order at most six. The entire kernel consequently has order at most12|U|=12·2^15. Every actual λ∈Λ is an involution, so its image has order at most two. This bounds the original marked set, with no projected-folder or injective-projection assumption.

From the reviewed unitary rank-class and outside-class formulas at `fa462cdffd3082b37b0f100ea7e0364a97832473`, the three internal involution classes of T have sizes2709,893970,10727640. Its outer involutions form one class, with centralizer Sp6(2) of order1451520 and size156930048. Here Out(T)=C2 because gcd(7,3)=1. Including identity, Aut(T) has168554368 elements of order at most two. It follows that

    |Λ| ≤ 12·2^15·168554368 = 66278274367488.             (10)

But I0≤J3 and the primary [ATLAS J3 order](https://brauer.maths.qmul.ac.uk/Atlas/spor/J3/) is50232960. Therefore

    |Λ|=|Q|=|S:I0| ≥ |S:J3| = 6479277604208640,          (11)

contradicting (10). This closes both orientations and the proposed all-odd-dimensional unitary full-socle exclusion.

The standard-library certificate [verify_psu9_residual.py](../code/verify_psu9_residual.py) checks the order formulas, all eight supplied maximal indices, the1152g divisibility screen, the internal and outer involution arithmetic, and the strict final bound. The source authors read and ran it with Python3.12.14; all assertions passed. The class counts are derived from the reviewed formulas, not supplied from a character table. The ATLAS completeness and Li–Xia factorization inputs remain external; this arithmetic is not a proof of either classification or of the new group-theoretic deduction.

The argument was developed with a research reviewer. An invalid early scratch inference about maximal factors in the original M was discarded before this canonical source; (8) preserves exactly the source's intersections after passage to M*. The canonical proof, matrix parabolic argument and certificate have the independent exact-source reviews below. C0010 remains open.

### Independent review of all odd-dimensional unitary full socles

automated-model reviewer A, reviewer B and reviewer C independently accepted this section and its certificate at exact source `5e9382749b716b55e65928d781df40adc5f067a8`. Each checked the corrected ambient-group reduction retaining G0/I0, index identity (8), explicit extraspecial parabolic/Levi model, maximal-index screen and order43 irreducibility, perfection and characteristic section, and the original marked-set capacity against a lower bound on the degree. Each extracted and ran the exact committed Python certificate; all assertions passed. The first two used the bundled Python3.12.14, while reviewer C reported the available `python3` without claiming that version. reviewer A freshly inspected Li–Xia Lemma2.18/TableA.3 and the ATLAS U7 list; the other two retained the source authors's source inspections. None rederived the external classifications or the previously reviewed unitary involution formulas. These are independent model reviews with explicit source inputs, not formal or human certification. Even-dimensional unitary full socles and unrestricted C0010 remain open.

## Proposed exclusion of all prime-dimensional linear full socles

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the pinned canonical, automorphism and factorization inputs, no finite simple nonassociative left Bol loop has full multiplication socle PSL_n(q), for any prime n and any q for which that socle is nonabelian simple. The all-PSL2 result at `47b07688a82d3df93f537946fe0780112200383b` covers n=2, and the odd-field prime-dimensional results at `2843ddb186cdf07ad6717e88c68e5f1c215846f9` and `2a46606e2adac7ef5c08a07447dc73dbb76db267` cover odd q. The new argument below handles odd prime n≥3 in characteristic two, including the actual exceptional factorization rows. Composite linear dimensions are outside this full-socle conclusion.

### Counting involutions in the original outside fibers

Retain the generic Li–Xia parabolic-side notation G0=G∩S, H0=H∩S, m=n−1, U=F_q^m and L=SL_m(q). Suppose m≥4, or m=2 with q≥4. In these ranges L is perfect, O_p(L)=1, End_L(U)=F_q and U^L=0. The characteristic-radical part of the preceding parabolic proof is valid in either characteristic: G0 has perfect residual U:L, its p-core U is normal in G, graph automorphisms cannot normalize its common fixed-space type, and the natural projective parabolic action gives faithful D=G/U≤ΓL_m(q). The scalar kernel is removed in PSL exactly as in that proof. Since O_p(D)=1 and D^(∞)=L, U and L are characteristic in the required groups.

Therefore canonical inversion acts on U by an F_p-linear map normalizing L. Normalizing End_L(U)=F_q makes it semilinear. The formal extension E=G⋊⟨τhat⟩ consequently acts on U through ΓL_m(q), with kernel on G exactly U. No vanishing of H¹(L,U), or affine realization of τ, is assumed.

Fix an image A of order at most two and one λ0 in the corresponding fiber of the outside coset τhat G. Every element of that fiber is uniquely uλ0, u∈U; because λ0²∈G and acts trivially on U, it belongs to U. In additive notation on U,

    (uλ0)² = (1+A)u + λ0².                              (12)

Thus the fiber contains either no involutions or exactly |ker(1+A)| involutions. The actual marked set Λ is bounded by the sum of these quantities over all semilinear A with A²=1. This is precisely the number of elements of order at most two in the affine semilinear group. The argument applies even when τ cannot be realized affinely and the formal extension action has a kernel; it counts the original marked elements within each outside fiber.

The lower bound also improves. The Singer semiregularity argument gives |H0|≤n. If g=|G:G0| and h=|H:H0|, the outer image of H is a subgroup of that of G, so h divides g. Hence

    |K|=[G:H]=[G0:H0]g/h ≥ |G0|/n
        ≥ q^m|SL_m(q)|/n.                              (13)

This cancels the outer factors rather than bounding them separately; it requires neither H surjectivity onto G/G0 nor a socle-level factorization.

### Even fields and m≥4

Let q be even and m≥4 even. A linear involution has rank r for A−I, 0≤r≤m/2, and its class size is

    |GL_m(q)| / (q^(r(2m−3r)) |GL_r(q)| |GL_(m−2r)(q)|).

This is the same Jordan-block centralizer count proved in the reviewed characteristic-two linear manuscript at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`. Put a_k(q)=∏_(i=1)^k(1−q^(−i)). Uniformly a_k(q)>1/4: for q=2 the first three factors give21/64, and the remaining product exceeds1−∑_(i=4)^∞2^(−i)=7/8, giving147/512>1/4; the shorter products and larger q are larger. The class-size ratio a_m/(a_r a_(m−2r)) is at most1/a_r<4, after canceling the first m−2r factors. Thus the total number of linear involutions, including identity, is less than

    4 q^(m²/2) sum_(t=0)^(m/2) q^(−2t²)
    ≤ (16/3) q^(m²/2),

where t=m/2−r and ∑_(t≥1)2^(−2t²)≤∑_(t≥1)4^(−t)=1/3. If the field quotient has a nontrivial involution, q=s² and descent gives at most |GL_m(q)|/|GL_m(s)|<4q^(m²/2) semilinear involutions with that field component. There is only one possible nontrivial field label of order two. Every kernel in (12) has at most q^m elements. It follows that

    |Λ| < 10 q^(m²/2+m).                               (14)

Meanwhile |SL_m(q)|>q^(m²−1)/2, since ∏_(i=2)^m(1−q^(−i))>1/2. Equations (13)–(14) are incompatible whenever q^(m²/2−1)≥20(m+1). At the smallest m=4,q=2, this is128>100. Increasing q only strengthens it, while increasing even m by two multiplies the left side by at least2^(2m+2), more than the linear ratio on the right. Thus every such generic parabolic case is excluded uniformly, with no small-field arithmetic exceptions.

### Even fields and m=2

Let q=2^f≥4. In GL2(q), there are q²−1 nonidentity involutions, each with a one-dimensional fixed space. Equation (12) gives q possible translations for each, and q² for the identity image. The linear-component contribution is exactly

    q³+q²−q.                                           (15)

When f is even, let s=sqrt(q). Semilinear descent gives |GL2(q)|/|GL2(s)|=s(s+1)(q+1) linear parts. Each has a two-dimensional fixed F_s-space and hence q vectors in ker(1+A). Its contribution is

    q s(s+1)(q+1).                                     (16)

When f is odd this contribution is absent. At q=4, (15)+(16)=196, while (13) gives q³(q²−1)/3=320. For q≥8, (15)/q³≤1+1/8 and, if (16) occurs, q≥16 and (16)/q³=(1+1/s)(1+1/q)≤(5/4)(17/16). Their sum is less than3. But (13) is at least21q³. This excludes the generic n=3 case for every even q≥4. No cocycle classification was used; the potentially nontrivial SL2 cohomology does not invalidate (12).

### Actual exceptional rows and the combined theorem

If S≤G, the reviewed odd-dimensional almost-simple canonical theorem applies. Otherwise Li–Xia v3 Theorem3.3/Table3.1, printed pp.23–25, gives either the generic alternatives above, or the listed exceptions. A generic Singer-side G is solvable and is excluded by the reviewed classical solvable-factor theorem at `3313726ad58aa11de1c79e04d4618f28380925fb`. The socle PSL3(2)=PSL2(7) was already excluded as a full socle by `47b07688a82d3df93f537946fe0780112200383b`.

For PSL3(4), row12 has factors PGL2(7) and M10. Each is an almost-simple PSL2 canonical group, excluded by that same reviewed theorem. Row13 has actual quotient M/S of order four and factors PGL2(7) and M10:2. If G=PGL2(7), the canonical theorem applies. In the opposite orientation I=PGL2(7), its perfect normal PSL2(7) is killed by any map to the abelian M/S; its abelian quotient has order two, so I cannot surject onto M/S as socle transitivity requires. This orientation does not require identifying M10:2 from its order.

Row14 likewise has quotient M/S of order four, with factors PGL2(7)×2 and M10. The orientation G=M10 is excluded by the canonical PSL2 theorem. In the other orientation I=M10 has perfect normal A6 and quotient C2, so again cannot surject onto M/S. The standard M10=A6.2c identification and its perfect derived subgroup are stated in the [ATLAS A6 primary data](https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/), directly inspected by the source authors and consistent with the previously reviewed PSL2 input. Row15, and the PSL3(8) row16, have both factors solvable; they are among the finite both-solvable cases already included in the reviewed assembly at `7f456116c2e6ca420c7c15c789c96ee105050c1b`. No degree56 rank computation is needed for these orientations.

Finally row17 has S=PSL5(2), M=PSL5(2).O with O≤C2, and actual factor orders155|O| and64512. Their product is |M|=9999360|O|, so the factor intersection H is trivial in either orientation. The left multiplication group then acts regularly, making the loop associative. This is the exact row's order calculation, not an inference from a merely maximal overgroup.

These cases exhaust the even-field prime-dimensional alternatives. Combined with the previously reviewed n=2 and odd-field results, they give the proposed all-prime-dimensional full-socle exclusion. The source authors supplied the outside-fiber argument and cancellation in (13), with a research reviewer checking the dimension-two repair, a research reviewer developing the higher-dimensional counts, and a research reviewer checking the exceptional orientations. The abandoned need for a characteristic-two cocycle classification is not a hypothesis of this proof. No new computation is required. All cited source qualifications remain in force; the exact-source independent reviews follow.

### Independent review of all prime-dimensional linear full socles

automated-model reviewer A, reviewer B and reviewer C independently accepted this section at exact source `c3f045c52e5e5dea344aba9823567834eb304218`, conditional on its stated canonical, automorphism, natural-module and Li–Xia inputs. Each checked the characteristic radical, the outside-fiber identity and its capacity bound without an affine lift or cohomology assumption, the outer-index cancellation in (13), the Jordan centralizer and product estimates, the uniform smallest case m=4,q=2, and the exact m=2 count including 196<320 at q=4. Each checked the exceptional orientations, especially the actual stabilizer's failure to surject onto M/S in rows13–14 and the regularity consequence in row17. They retained previously recorded primary-source inspections; none freshly browsed the factorization tables, ran a new computation or rederived the external classifications in this pass. These independent model reviews do not constitute formal or human certification. Composite linear dimensions and unrestricted C0010 remain open.

## Proposed exclusion of the linear Singer-parabolic family in every dimension

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Let Q be a finite simple nonassociative left Bol loop, with M=Mlt(Q), G=LMlt(Q), I=M_1, H=G∩I and nonabelian simple S=Soc(M)=PSL_n(q), n≥3. Under the canonical, automorphism and Li–Xia inputs used above, the actual factorization M=GI cannot have one socle intersection in the projective Singer normalizer and the other in a point or hyperplane parabolic. Both orientations are excluded, in every dimension and characteristic. This closes this particular family, including the reversed orientation of Li–Xia Table1.1 row1 with solvable I. It does not exclude every composite-dimensional linear full socle.

If G is the Singer-side factor, G is solvable, and the reviewed classical solvable-factor theorem at `3313726ad58aa11de1c79e04d4618f28380925fb` already excludes this actual configuration. Suppose instead I is the Singer-side factor and G the parabolic-side factor. Li–Xia arXiv:1408.0350v3, Lemma3.2, printed pp.22–23, applies in arbitrary dimension, despite the prime-dimension title of its surrounding chapter. It gives either

    U:SL_(n−1)(q) normal in G0=G∩S ≤ P1 or P_(n−1),

or one of its listed small exceptions with the actual parabolic-side factor G solvable. The latter is again covered by the reviewed solvable-factor exclusion. The source authors and a research reviewer directly inspected the lemma and its proof, including its stated source computation at (n,q)=(3,9). That computation and the factorization theorem remain external inputs; no new reproduction is claimed. The proof below never replaces the actual factors by maximal overgroups.

Dimension n=3 is already covered by the independently reviewed all-prime-dimensional full-socle theorem at `c3f045c52e5e5dea344aba9823567834eb304218`. Thus put m=n−1≥3. The characteristic-radical proof in that source works for either parity of m: L=SL_m(q) is perfect, U:L is the perfect residual of G0, its p-core U is normal in G, and normalizing U rules out a graph component. The faithful projective parabolic action gives

    G=U⋊D,       L≤D≤ΓL_m(q),       U=O_p(G), D^(∞)=L.

For clarity about the even-dimensional projective interface, the Levi action A↦det(A)A on U has scalar kernel λ^(m+1)=1, precisely the scalar center removed in PSL_(m+1)(q). Its restriction to SL_m(q) is faithful, since λ^m=λ^(m+1)=1 implies λ=1. The endomorphism-field and characteristic-subgroup arguments therefore apply with no parity qualification. Canonical inversion normalizes this field and acts semilinearly on U.

Use the original outside-fiber equation (12), not a projected folder or affine realization of inversion. It bounds |Λ| by q^m times the number J_m(q) of elements A∈ΓL_m(q) with A²=1, including identity. The same Singer semiregularity and outer-image cancellation as in (13) give

    |Λ|=|Q|=[G:H] ≥ q^m |SL_m(q)|/(m+1).              (17)

### A uniform semilinear count for both dimension parities

Put a_k(q)=∏_(i=1)^k(1−q^(−i)); the previously proved bound a_k(q)>1/4 applies to every k≥0 and q≥2. In odd characteristic, a linear involution is specified up to GL_m(q)-conjugacy by its −1 eigenspace dimension r, and its class size is

    |GL_m(q)|/(|GL_r(q)| |GL_(m−r)(q)|)
      < 4 q^(2r(m−r)).

Here a_m/(a_r a_(m−r))≤1/a_r<4 by cancellation. If m is even, putting t=r−m/2 and bounding the two tails gives a total at most (20/3)q^(m²/2): indeed ∑_(t≥1)q^(−2t²)≤1/3. If m is odd, the two central values of r give equal maxima (m²−1)/2; the remaining paired exponents drop by 2t(t+1), t≥1. The total is less than (32/3)q^((m²−1)/2), by the same geometric-tail bound.

In characteristic two the rank-r square-zero class formula from the preceding section applies. For even m its exponent is m²/2−2t², and for odd m it is (m²−1)/2−2t(t+1). There is only one class at each r, so the linear total is less than (16/3)q^floor(m²/2) in either dimension parity.

If q=s², the only possible nontrivial field component of an involution is the field automorphism of order two. Finite-field descent gives one GL_m(q)-class in that semilinear coset, of size |GL_m(q)|/|GL_m(s)|<4q^(m²/2). If q has no square-root field, no such component occurs. Consequently, in every characteristic and dimension parity,

    J_m(q) < 11 q^(m²/2).                             (18)

For odd q and odd m the coefficient is at most 32/(3√q)+4≤32/(3√3)+4<11; for odd q and even m it is at most20/3+4<11; in characteristic two it is at most16/3+4<10. No factor proportional to the field degree is needed, since the cyclic field group has at most one nonidentity element of order two.

Since ∏_(i=2)^m(1−q^(−i))>1/2, we have |SL_m(q)|>q^(m²−1)/2. Equations (17)–(18) contradict one another whenever

    q^(m²/2−1) > 22(m+1).                             (19)

For m≥4 this holds already at m=4,q=2, where128>110. Increasing m by one multiplies the left side by at least2^(m+1/2), greater than the ratio (m+2)/(m+1) of the right sides; increasing q also strengthens it. For m=3,q≥4 it holds at q=4, where128>88. Thus only (m,q)=(3,2),(3,3) require separate arithmetic.

### The two boundary counts

For m=3,q=2, GL3(2) has21 nonidentity involutions, all of rank one for A−I; their fixed spaces have order4. The identity fiber contributes8. The original outside-fiber bound is therefore

    |Λ|≤8+21·4=92 < 8·168/4=336 ≤[G:H].

The number21 follows from the Jordan centralizer formula, not a subgroup or loop enumeration. For m=3,q=3, the two scalar linear involutions contribute1 and27 translations. Each of the other two eigenspace classes has size117, directly from |GL3(3)|/(|GL1(3)||GL2(3)|). Their −1 eigenspaces have orders3 and9. Hence

    |Λ|≤1+27+117(3+9)=1432
         < 27·5616/4=37908 ≤[G:H].

Neither field has a nontrivial field automorphism. These count upper bounds for actual outside involutions via (12); they do not assert an affine lift exists. This completes the proposed all-dimensional Singer-parabolic exclusion.

### What remains in odd composite linear dimension

The complete maximal-factorization source does not reduce every odd composite dimension to this family. Li–Xia Theorem2.15 and TableA.1, printed pp.18 and95, leave an extension-field subgroup of type GL_a(q^b).b against P1 or P_(n−1), with ab=n and b prime. In odd composite n, a can exceed one. The source authors inspected every table row; rows2–4 require even dimension, while the other exceptional rows have prime dimension. As in the unitary argument, Lemma2.18 must be used preserving G∩S and I∩S when the ambient group changes, rather than asserting maximality of the actual factors.

For a>1 the extension-field subgroup can be nonsolvable, and the bound |H∩S|≤n used in (17) need not hold. Nor does its pairing with a parabolic force the actual parabolic-side factor to contain U:SL_(n−1)(q) by the Singer lemma. These two missing interfaces prevent claiming an odd-composite full-socle exclusion here. Even projective transitivity alone would not force the full displayed extension-field special linear group: for instance SL3(q^9) embeds in GL9(q^3) and is transitive on nonzero vectors of its underlying 27-dimensional F_q-space. This is a group-theoretic control, not a constructed Bol folder. The next obligation is to control the actual subfactors and selected involutions in this remaining family.

The uniform count and its boundary cases were developed with a research reviewer, and the composite-dimensional source audit with a research reviewer. Their development checks are not independent exact-source reviews. No new executable certificate is needed for these displayed formulas. All canonical, automorphism, descent and external classification qualifications remain in force; independent reviews follow. Unrestricted C0010 remains open.

### Independent review of the all-dimensional Singer-parabolic exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `472e2653976598a9666142e7f64e07a4601c61e8`, conditional on its stated inputs. Each checked the characteristic-radical and faithful projective Levi interface in both dimension parities, the original outside-fiber argument, the linear-class sums and unique possible field label, the uniform coefficient11 and monotone inequality, and the exact92 and1432 boundary counts. reviewer A and reviewer C freshly inspected Li–Xia Lemma3.2 and confirmed its dimension-unrestricted actual-factor statement; reviewer B retained the recorded source reading. The first reviewer retained a previous TableA.1 inspection, while the others retained the source authors's table audit. None reran the source classification computations, rederived the external classifications or ran new computation. The acceptance is confined to the actual Singer-parabolic family. The nonsolvable extension-field residual and unrestricted C0010 remain open.

## Proposed field reduction for the reversed unitary solvable-factor row

**Conditional application under 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Suppose the actual factorization M=GI has S=Soc(M)=PSU_(2m)(q), m≥2, and lies in Li–Xia arXiv:1408.0350v3 Table1.1 row6 with the full point stabilizer I as the solvable factor and G=LMlt(Q) as the other factor. Then the actual G must have field image of order two, generated by q-power conjugation. In particular G cannot lie in PGU_(2m)(q). This excludes the entire orientation without field automorphisms; it leaves the indicated semilinear orientation open.

The table gives a normal embedded L=SU_(2m−1)(q) in G0=G∩S. This embedding into PSU_(2m)(q) is injective: a block diag(1,A) that becomes a global scalar is already identity. The reviewed natural-line argument at `b8c237d84f001b9a3d70ab725adab6b67e57c05b` shows that the projective normalizer preserves the unique fixed nondegenerate line and its perpendicular complement. In PGU_(2m)(q) it is

    N=(GU1(q)×GU_(2m−1)(q))/diagonal scalars
      ≅ GU_(2m−1)(q),

where the isomorphism sends the class of diag(a,B) to a⁻¹B. It sends the embedded L identically to SU_(2m−1)(q); there is no hidden quotient of its odd center. The complete semilinear normalizer adds the standard cyclic field group of order2f, q=p^f, which preserves the chosen orthogonal decomposition. The usual unitary automorphism description and the unique fixed-line argument give this normalizer inside Aut(S).

Except for L=SU3(2), L is perfect with simple projective quotient. The cyclic quotient of the linear normalizer and the solvable outer quotient show L=G^(∞): first L=G0^(∞) is characteristic in G0 and normal in G, then G/L is solvable. Therefore the actual G embeds in the intermediate semilinear unitary setting of the [new canonical normalizer theorem](../factor-permutation/radical-free-three-dimensional-linear-unitary.md#odd-dimensional-unitary-normalizers-without-field-automorphisms). That theorem proves the field-image conclusion directly on the original canonical group. Its center-rigidity and central-cover dependencies are reviewed at `e7476945cf987cf1c654a385ac8f78fe2beb320a`; the present application and normalizer theorem have the independent exact-source reviews below.

In the small case (m,q)=(2,2), the linear normalizer GU3(2), the field group and thus G are solvable. The reviewed solvable-LMlt full-action theorem at `7f456116c2e6ca420c7c15c789c96ee105050c1b` would force S≅A_N, N≥24; but |PSU4(2)|=25920<24!/2. Hence this case is impossible. No perfectness or simple-projective-quotient claim is made for SU3(2).

The actual row6 containment, normalizer and source qualifications are those recorded in REFERENCES.md and the earlier reviewed rows3–6 argument. This is a reduction of this reversed solvable-factor orientation, not a classification of all even-dimensional unitary full socles or of arbitrary component extensions. No new computation was used.

### Independent review of the reversed unitary field reduction

automated-model reviewer A, reviewer B and reviewer C independently accepted this application and its new normalizer theorem at exact source `f0e3336ff80066f3c5dd6cec7065d728eeb8d471`. Each checked the projective line-normalizer isomorphism, injective SU block embedding retaining its center, characteristic perfect residual and the SU3(2) solvable boundary. They retained the earlier Li–Xia and classical automorphism source interpretations without fresh primary inspection or computation. The acceptance is conditional on the cited canonical, center and classification inputs and does not exclude the residual field-image orientation.

## Proposed complete exclusion of the reversed unitary solvable-factor row

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the pinned canonical, Li–Xia, natural-normalizer and unitary involution inputs, the actual factorization of a finite simple nonassociative left Bol loop cannot lie in Li–Xia Table1.1 row6 with the full point stabilizer as its solvable factor. This includes the field-image orientation left by the preceding reduction. Combined with the reviewed solvable-LMlt exclusion, it removes both orientations of this row for every parameter m≥2 and q. It does not exclude all even-dimensional unitary full socles.

Retain M=Mlt(Q), G=LMlt(Q), I=M_1 and S=Soc(M)=PSU_(2m)(q). Put I0=I∩S, d=2m−1, δ=gcd(2m,q+1), δ0=gcd(d,q+1), L=SU_d(q) in its injective line-fixing embedding, and T=L/Z(L). The preceding normalizer argument, independently reviewed at `f0e3336ff80066f3c5dd6cec7065d728eeb8d471`, makes L=G^(∞) characteristic and places G in its semilinear line normalizer. The exceptional (m,q)=(2,2) was excluded there using the solvable-LMlt theorem, so T is nonabelian simple throughout the following proof.

### Capacity in the original formal extension

The centralizer of L in the full semilinear normalizer is the scalar group of order q+1. Indeed a nontrivial field exponent has nontrivial field label on T by the pinned unitary automorphism description, so it cannot centralize L; the linear centralizer is scalar by the natural-module argument. An element of G inducing identity on T also centralizes L: its central discrepancy defines a homomorphism from perfect L to Z(L), hence is trivial. Thus the kernel of G→Aut(T) has order at most q+1.

The formal extension E=G⋊⟨τhat⟩ acts on T, since L is characteristic. Its full kernel has order at most2(q+1). Every actual mark λ∈Λ is an involution and maps to an automorphism of order at most two. If J denotes the number of such automorphisms, including identity, then

    |Q|=|Λ| ≤ 2(q+1)J.                               (20)

No injective mark projection or quotient folder is asserted. This counts the original marked set with the entire possible kernel included.

### A uniform bound for all involutions of Aut(T)

Write U_k=GU_k(q) and

    b_k=|U_k|/q^(k²)=∏_(i=1)^k(1−(−q)^(−i)), b_0=1.

Pairing factors of odd and following even index gives b_k≥1; each such pair is greater than1. Pairing even and following odd index after the first factor instead gives b_k≤1+1/q≤3/2, since each such pair is less than1. These bounds hold also for k=0.

Let J_int count identity and involutions of T. In odd characteristic each involution lifts uniquely to L through its odd center. Its −1 eigenspace has even dimension r; the corresponding class has size

    |U_d|/(|U_r| |U_(d−r)|).

The unitary classes do not split in L, since their centralizers realize every unitary determinant. In characteristic two the classes are indexed by r=rank(u−1), 0≤r≤m−1, with size

    |U_d|/(q^(r(2d−3r)) |U_r| |U_(d−2r)|).

The latter formula and splitting/projective arguments are reviewed at `fa462cdffd3082b37b0f100ea7e0364a97832473`; the odd-field eigenspace classes are reviewed at `b436485f3c07c3413c19b319e51e8c7bc2c3a580` and `d5e26dd6aef4ad09f61e0569e383782dea0d468b`. The source authors also freshly inspected the matching full-unitary counts in Fulman–Guralnick–Stanton, revised18 February2017, Proposition3.4 and equation(10), pp.15–16. The restriction to even r and passage to T are the separate special/projective arguments just stated.

Each class coefficient after factoring out q^(2r(d−r)) is at most3/2, by the b_k bounds. For odd d, r and d−r have opposite parity and equal exponents, so the even-r condition in odd characteristic selects exactly one member of every such pair. In characteristic two the rank range likewise gives one copy of each exponent. In both cases the multiset of exponents is

    2m(m−1)−2t(t+1),       0≤t≤m−1.

Consequently

    J_int ≤ (3/2) q^(2m(m−1)) ∑_(t≥0)q^(−2t(t+1))
          ≤ (8/5) q^(2m(m−1)),                       (21)

since 2t(t+1)≥4t and ∑_(t≥0)2^(−4t)=16/15.

In the unitary outer quotient D⋊C_(2f), D has odd order δ0. An automorphism of order at most two either lies in T or has the unique nonidentity order-two field label. There are δ0 actual T-cosets with that field label. Odd diagonal cocycle conjugacy and the reviewed one-class theorem show that each has one T-class of involutions, all of the same size. The standard q-power automorphism has fixed subgroup SO_d(q) when q is odd and Sp_(d−1)(q) when q is even. Its projective centralizer has precisely the same order: the scalar center of SU_d has odd order and is inverted by q-power, so the fixed-center kernel is trivial and fixed projective elements lift after central correction. The common order is

    q^((m−1)²) ∏_(j=1)^(m−1)(q^(2j)−1).

These are the fixed-form identifications in the reviewed local sources; the standard orders are also given by equations(2)–(3), pp.5–6, of the inspected Fulman–Guralnick–Stanton version (SO is index two in odd-characteristic O). Thus the total number of outer involutions is exactly

    J_out = δ0 |T|/|C_T(α)|
          = q^(m(m−1)) ∏_(j=1)^(m−1)(q^(2j+1)+1)
          > q^(2m²−m−1).                             (22)

This includes every diagonal label and does not multiply by the field degree. From (21)–(22),

    J_int/J_out < (8/5)q^(−(m−1)) ≤ 4/5 < 1,
    J=J_int+J_out < 2J_out.                          (23)

### The actual degree is larger than the capacity

The solvable-factor upper bound in Li–Xia arXiv:1408.0350v3, Table1.1 row6, printed p.7, is

    |I0| ≤ m q^(m²)(q^(2m)−1)/((q+1)δ).

The source authors freshly inspected the row, retaining that this is an upper bound on the actual intersection, not equality with a maximal subgroup. The socle is transitive in the primitive full action, so |Q|=|S:I0|. Cancelling the indicated factors in the unitary order formula gives the exact lower bound

    |Q| ≥ ((q+1)/m) J_out ∏_(j=1)^(m−1)(q^(2j)−1).  (24)

For m=2 and q≥3, the product is q²−1≥8=4m. For m≥3 and q≥2 it starts at (m,q)=(3,2) with3·15=45>12=4m, and increasing m multiplies the product by q^(2m)−1, greater than the increase from4m to4(m+1); increasing q also strengthens it. Hence (24) always gives |Q|≥4(q+1)J_out. But (20) and (23) give |Q|<4(q+1)J_out, a contradiction. The equality in the coarse product bound at m=2,q=3 causes no gap because (23) is strict. The excluded nonsimple-component case m=2,q=2 is not passed through these formulas as a simple group.

This completes the proposed reversed-row exclusion. The opposite orientation, with solvable canonical G, is already covered by the reviewed classical assembly at `3313726ad58aa11de1c79e04d4618f28380925fb`. The general canonical semilinear unitary classification remains open: the present contradiction uses the additional small full-stabilizer bound supplied by this actual factorization row.

The source authors derived the product estimate and exact cancellation with exploratory checks by a research reviewer and a research reviewer. No enumeration, finite scan or asymptotic inference is used. The primary formulas, local class theorems, normalizer and canonical inputs remain explicit; the complete deduction has the independent exact-source reviews below. C0010 remains open.

### Independent review of the complete reversed unitary row

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `84bf63ea8de881dab3d5ea6e52fee4c9dcbcaca4`, conditional on the stated canonical, characteristic-normalizer, local-class and factorization inputs. Each checked the original formal-extension kernel bound, unitary product coefficients and paired exponents in both characteristics, projective fixed SO/Sp orders and all odd-diagonal field labels, the exact J_out formula and strict J_int<J_out comparison, the actual stabilizer degree bound and cancellation, and the tight m=2,q=3 boundary. The nonsimple m=2,q=2 component was kept separate. reviewer A freshly inspected Fulman–Guralnick–Stanton equation(10)/Proposition3.4 and Li–Xia Table1.1; the other two retained the recorded primary-source inspections. None ran a computation or rederived the external classifications. The acceptance closes this actual row orientation and, with the prior solvable-LMlt result, both orientations of row6. It does not classify arbitrary semilinear unitary canonical groups, all even-dimensional unitary full socles or C0010.

## Proposed complete exclusion of the reversed symplectic extension-field rows

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the pinned canonical, classical-normalizer, automorphism and Li–Xia inputs, Table1.1 rows4–5 cannot be the actual factorization M=GI when the full point stabilizer I is the solvable factor. Together with the reviewed solvable-LMlt orientation, both rows are excluded for every permitted field. This is a row-specific conclusion, not an exclusion of every PSp4(q) full socle.

Here S=Soc(M)=PSp4(q), G=LMlt(Q), and the table gives T normal in G0=G∩S with T=PSL2(q²) in its natural extension-field embedding. The q=2 symplectic group is not a nonabelian simple socle and is outside these rows in the present setting. The natural normalizers N_S(T)=T.2 and their embeddings were independently reviewed at `b8c237d84f001b9a3d70ab725adab6b67e57c05b`. Thus T=G0′ is characteristic in G0 and normal in G. The full normalizer quotient by T is solvable under the cited classical automorphism description, so T=G^(∞) is characteristic in G. In particular canonical inversion acts on T, without projecting the loop to T.

### The projective centralizer, with the odd-field scalar retained

Write the natural four-dimensional F_q space as F_(q²)² with symplectic form Tr_(q²/q)(det(v,w)). The two elementary root-matrix families show that the linear commutant of SL2(q²) is the scalar field F_(q²). If a projective map centralizes T, its commutators with the perfect covering SL2(q²) are scalar and define a character; that character is trivial. This reduces projective centralization to the linear commutant calculation.

A scalar λ∈F_(q²)^× is a symplectic similitude exactly when λ²∈F_q^×, by nondegeneracy of the trace pairing. Modulo the ambient scalars F_q^×, these elements form the trivial group when q is even and a group of order two when q is odd. In the odd case, the second class has λ^q=−λ and λ² nonsquare in F_q, so it lies in PGSp4(q) outside PSp4(q). This centralizing involution must not be discarded.

A semilinear normalizer acts on the elementary matrices of SL2(q²) by a field exponent, possibly followed by the degree-two extension-field automorphism. If it centralizes T, the same perfect-group character argument and faithful field action on PSL2(q²) force the total exponent to vanish modulo2f, q=p^f. Hence it reduces to the preceding scalar calculation. For odd q the standard full automorphism group is projective symplectic similitudes extended by field automorphisms. For even q, odd powers of the exceptional graph generator exchange the extension-field and minus-orthogonal subgroup classes; they cannot normalize T. The exchange and the distinction of these classes are proved with source qualifications in the reviewed symplectic-row section at `bdbc638eb788af4ddd1d5dafcdaeeb7304aced23`, using Li–Xia Remark(ii), p.6, Lemma7.22, p.70, and Aschbacher–Seitz(19.3), pp.76–77. Even graph powers are natural field automorphisms. Therefore

    |C_Aut(S)(T)| = 1 for q even, and 2 for q odd.     (25)

If q is even, conjugation embeds the actual G into Aut(T), with T≤G. The independently reviewed all-almost-simple canonical PSL2 theorem at `47b07688a82d3df93f537946fe0780112200383b` excludes G immediately. This closes the reversed row4.

### Odd q≥5 by the original outside-coset capacity

Suppose q is odd. In the formal E=G⋊⟨τhat⟩, restriction to characteristic T gives E→Aut(T). Its kernel on G has order at most two by (25). The inverse image of any automorphism within the single outside coset τhat G is either empty or a coset of that kernel. Thus it has size at most two, even if the kernel on the whole E has order four. Counting actual outside marks gives

    |Q|=|Λ| ≤ 2 J,
    J=#{a∈Aut(PSL2(q²)):a²=1}.                       (26)

The PGL2(q²) involutions, including identity, number1+q⁴. The only possible nontrivial field label for an involution is q-power conjugation. Its coset in PΓL2(q²) has one PGL2(q²)-class, with centralizer PGL2(q), hence q(q²+1) involutions. For odd q this splits into two PSL2(q²)-classes in the same pure field coset; each has size q(q²+1)/2. The mixed diagonal-field coset has no involutions. These exact label and class facts are the reviewed Hilbert90 and square-determinant argument at `88f2b7c0260426c220b3d5ec4272fed9d7801255`, retained in `47b07688a82d3df93f537946fe0780112200383b`. In particular the total field contribution must not be halved. Hence

    J=1+q⁴+q(q²+1).                                  (27)

The actual row5 stabilizer intersection satisfies |I∩S|≤q³(q²−1). Socle transitivity and the symplectic order give

    |Q|=|S:I∩S| ≥ q(q⁴−1)/2.                         (28)

For q≥5, this exceeds2J. After multiplying the difference by2, it is

    q⁵−4q⁴−4q³−5q−4
      =q³(q²−4q−4)−5q−4 >0,

since q²−4q−4≥1 and q³−5q−4>0 there. At q=5 the bounds are1512<1560. Thus every odd q≥5 is excluded without a finite scan.

### The q=3 central-extension boundary

Here S=PSp4(3) has order25920, T=PSL2(9)≅A6, and (28) gives |Q|≥120. The full normalizer of T in Aut(S) is

    N=S6×C2,       T=A6×1.                            (29)

To see the particular embedding, N_S(T)=T⋊⟨σ⟩ has order720, with σ the F9/F3 field involution. The outside scalar λ satisfying λ³=−λ gives an involution w in PGSp4(3)\S and commutes projectively with σ, since σ sends λ to −λ. It centralizes T. Since Out(S) has order two, N=N_S(T)×⟨w⟩. The standard A6≅PSL2(9) identification makes T⋊⟨σ⟩ the field-type S6. Equivalently, the three index-two extensions in Aut(A6) have outside involution totals30,36,0 respectively; natural S6 has15 transpositions and15 triple transpositions, identifying the field label. The other two totals are the PGL and mixed counts above. The primary ATLAS U4(2)=PSp4(3) page lists S6 and S6×2 as maximal subgroups of S and Aut(S); the source authors directly inspected that page and the primary ATLAS A6 identification/standard-generator entries. These source identifications are explicit inputs to (29), not inferred from orders alone.

If G intersects the central C2 of N trivially, its faithful action on T makes it an almost-simple A6 overgroup, already excluded at `47b07688a82d3df93f537946fe0780112200383b`. Otherwise G contains that C2. Since N/T is a four-group, the remaining possibilities are G=A6×C2 or G=S6×C2.

For G=A6×C2, its derived A6 and center C2 are characteristic, so τ=β×1 for an involutory automorphism β of A6; there is no nontrivial homomorphism from perfect A6 to the center. If β is inner, τ is inner on G, contradicting the component form of the reviewed inner-inversion theorem at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. This contradiction does not require O2(G)=1. Otherwise the single outer βA6 coset has at most36 involutions, by (27) and the label roster. The two central coordinates give |Λ|≤72<120, a contradiction.

For G=S6×C2, every automorphism has the form

    (b,z) ↦ (β(b), z+χ(b)),

where β∈Aut(S6) and χ:S6→C2 is a homomorphism; the unique central factor is characteristic. For every τ-inverted generator k=(b,z), comparing the central coordinates gives χ(b)=0. The projections of K generate S6, hence χ=0 and τ=β×1, with β²=1. An inner β again contradicts the component theorem. Otherwise restriction identifies Aut(S6) with Aut(A6): it is injective on the characteristic centerless socle, and every automorphism of A6 normalizes the field-type S6 because Out(A6) is abelian. The outside coset βS6 consists of the diagonal and mixed A6 labels, with36 and0 involutions. Thus again |Λ|≤72<120. This exhausts (29) and closes q=3.

Both reversed rows4–5 are therefore excluded under the stated inputs. Their opposite solvable-LMlt orientations were already covered by the combined classical assembly at `3313726ad58aa11de1c79e04d4618f28380925fb`. The source authors developed the outside-coset bound and q=3 central-extension argument with a research reviewer and a research reviewer; the latter checked the natural centralizer and ATLAS normalizer shapes. The odd-field centralizer was retained after an incorrect trivial-centralizer shortcut was rejected, and both field classes are included in (27). No claim that Z(G)=1, normality of the right nucleus, or existence of a quotient loop on T is used. No new computation is needed. The independent exact-source reviews follow; unrestricted C0010 remains open.

### Independent review of the reversed symplectic extension-field rows

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `01e1be0bc7331170f94a3b1ef86abac077c81336`, conditional on the stated canonical, component, automorphism, classical-normalizer and Li–Xia inputs. Each checked the projective centralizer, including its odd-field C2, and the bound of two on fibers within the single original outside coset. Each retained both pure-field PSL2 classes in (27), the absence of mixed involutions, the strict q≥5 inequality and the q=3 normalizer interface, both central-extension alternatives, the central-character generation argument and the component form of the inner-inversion contradiction. reviewer A freshly reopened the ATLAS A6 and U4(2) pages for the identification and outer-group inputs; the other two retained the recorded source inspections. None ran new computation or rederived the external classifications. These independent model reviews concern the actual reversed rows4–5 only, not arbitrary PSp4 full socles or closure of C0010.

## Proposed complete exclusion of the reversed even-characteristic symplectic orthogonal row

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the pinned canonical, natural-normalizer, automorphism and Li–Xia inputs, Table1.1 row3 cannot be the actual factorization M=GI with solvable full point stabilizer I. Combined with the reviewed solvable-LMlt orientation, this closes both orientations of this row at all parameters. It does not exclude arbitrary symplectic full socles or classify all almost-simple orthogonal canonical groups.

Let S=Soc(M)=Sp_(2m)(q), q even, m≥2, G=LMlt(Q), and G0=G∩S. The table gives T=Ω^−_(2m)(q) normal in G0 and

    |I∩S| ≤ m q^(m(m+1)/2)(q^m−1).                  (30)

For m=2, the exceptional graph automorphism transports the minus-orthogonal T to the extension-field PSL2(q²) class, as in the reviewed graph-exchange argument at `bdbc638eb788af4ddd1d5dafcdaeeb7304aced23`. Its normalizer therefore acts faithfully on T by the even-field centralizer calculation at `01e1be0bc7331170f94a3b1ef86abac077c81336`. The canonical G is an almost-simple PSL2(q²) overgroup and is excluded by `47b07688a82d3df93f537946fe0780112200383b`. The case q=2 has no nonabelian simple Sp4(2) socle. Hence assume m≥3 below.

### Characteristic component and its full automorphism realization

Here T is nonabelian simple and perfect, including Ω6^−(2)≅PSU4(2). The natural normalizer N_S(T)=O^−_(2m)(q), with quotient of order two, is the reviewed input at `b8c237d84f001b9a3d70ab725adab6b67e57c05b`. Thus G0′=T; since G/G0 is solvable under the classical automorphism description, T=G^(∞) is characteristic in G. Canonical inversion therefore restricts to T.

For m≥4, Kleidman–Liebeck1990, Table2.1.B and Theorems2.1.3–2.1.4, printed pp.15–16, identify Aut(T) with the projective semisimilarities of the natural minus quadratic form F on V=F_q^(2m). The dimension-eight triality exception in that theorem is plus type, not minus type. For m=3, Giudici–Glasby–Praeger arXiv:2012.07213v1, proof of Theorem4.2, printed p.24, explicitly identifies PΓO6^−(q) with PΓU4(q)=Aut(PSU4(q)). The source authors directly inspected these primary statements, including the plus sign in the triality exception. They are automorphism-classification inputs, not new classification proofs.

Every ambient automorphism of S is a projective semilinear symplectic similitude when m≥3, by the same Kleidman–Liebeck theorem. A normalizer of T preserves F up to its scalar and field action. To check this last interface, absolute irreducibility of the natural T-module makes its invariant alternating form unique up to scalar. Quadratic forms with the same polar form differ by the square of a linear functional in characteristic two; T has no nonzero invariant linear functional. Thus its invariant quadratic form is likewise unique up to scalar. The natural normalizer therefore acts through PΓO^−_(2m)(q), whose action on T is faithful by the cited automorphism realization. In particular C_G(T)=1.

In characteristic two every projective semisimilarity of F has a unique representative that is a semilinear isometry: multiply by the unique scalar whose square cancels its multiplier. Uniqueness also makes these representatives a group; the only scalar isometry is identity. We may therefore realize all of Aut(T) faithfully as these semilinear isometries.

### No involution with a nontrivial field component

Suppose a semilinear isometry a has a²=1 and nontrivial field component. The field component has order two, so q=s² and it is σ:x↦x^s. Its fixed space W is a 2m-dimensional vector space over F_s and F_q⊗_(F_s)W=V. Here the descent step has an elementary proof even in characteristic two. Choose c∈F_q with c+c^σ=1. For every v∈V, both

    w1=v+a(v),       w2=c^σ v+c a(v)

are fixed by a, and v=w2+c w1. The representation as w2+c w1 is unique for w1,w2∈W, since applying a and subtracting uses c+c^σ=1. This proves the dimension and scalar-extension assertions.

The isometry identity gives F(W)⊆F_s. Its polar form descends to W and is nondegenerate there, since a vector orthogonal to W is orthogonal to its F_q-span V. Thus F is the scalar extension of a nondegenerate even-dimensional quadratic form over F_s. Every such form becomes plus type over the quadratic extension F_(s²): in its Witt decomposition only a possible anisotropic plane remains, and the irreducible quadratic defining that plane splits over F_(s²). This contradicts the minus type of F. Consequently every automorphism of T of order at most two lies in the linear group O^−_(2m)(q).

Apply restriction to T in the formal extension G⋊⟨τhat⟩. Within its single outside coset, each nonempty fiber has size |C_G(T)|=1, regardless of the kernel on the entire extension. The actual marked set therefore satisfies

    |Q|=|Λ| ≤ j_m(q),
    j_m(q)=#{a∈O^−_(2m)(q):a²=1}.                   (31)

Identity is included; no quotient loop or arbitrary choice of a projected transversal is used.

### A uniform count and the sole small boundary

Use Fulman–Guralnick–Stanton, author version revised18February2017, Theorem2.15 on printed p.11 and Theorem5.6(2) on pp.26–27. The source authors directly inspected these exact identities. Substituting u/q into the generating identity gives

    ∑_(m≥0) u^m q^(m²−m) j_m(q)/|O^−_(2m)(q)|
       = A(u)/(2(1−u)) − B(u)/2,
    A(u)=∏_(i≥1)(1+u/q^(2i−1))/∏_(i≥1)(1−u²/q^(2i)),
    B(u)=∏_(i≥1)(1+u/q^(2i))/∏_(i≥1)(1−u²/q^(2i)).  (32)

The zero-dimensional term uses the source's convention; only m≥3 is used here. Both A and B have nonnegative coefficients. The coefficient of u^m on the right is at most A(1)/2. The orthogonal order formula then yields

    j_m(q) ≤ q^(m²)(1+q^(−m))
                 ∏_(i=1)^(m−1)(1−q^(−2i)) A(1)
            < 4 q^(m²).                             (33)

Indeed ∏_(i≥1)(1−q^(−2i))>1−∑_(i≥1)q^(−2i)≥2/3, while ∏_(i≥1)(1+q^(−(2i−1)))≤exp(2/3)<2. Thus A(1)<3; also 1+q^(−m)≤9/8. This is a bound on every coefficient, not an inference from the asymptotic limit in Theorem5.7.

Socle transitivity in the primitive full action and (30) give

    |Q|=|S:I∩S|
       ≥ |Sp_(2m)(q)|/[m q^(m(m+1)/2)(q^m−1)]
       > (2/(3m)) q^((3m²−m)/2),                   (34)

using the symplectic order and the same product lower bound. Equations (31), (33) and (34) contradict one another whenever

    q^(m(m−1)/2) ≥ 6m.                              (35)

For m≥4 this holds at m=4,q=2, since64>24; increasing m multiplies the left side by at least2^m, more than (m+1)/m, and increasing q also strengthens it. For m=3 it holds for q≥4, starting with64>18. The sole remaining pair is m=3,q=2.

At that pair, |O6^−(2)|=51840. The five nonzero summands in Theorem5.6(2), in the source order A0,A2,B2,C1,C3, are

    1, 45, 270, 36, 540,
    j_3(2)=892 < 1080
       = |Sp6(2)|/[3·2^6·(2³−1)].                  (36)

For reproducibility the corresponding denominators are51840,1152,192,1440,96. They follow directly from the displayed source centralizers and |Sp2(2)|=6, |Sp4(2)|=720, |O2^−(2)|=6. Thus the endpoint is exact arithmetic in a published class formula, not a finite group or loop search.

This excludes the reversed row3 under the stated inputs. Its opposite solvable-LMlt orientation is already covered by `3313726ad58aa11de1c79e04d4618f28380925fb`. The source authors supplied the quadratic-descent repair and the automorphism-source audit; a research reviewer developed the uniform coefficient bound and boundary evaluation. Earlier bounds counting the larger symplectic semilinear group left artificial small-rank gaps; (31) removes those gaps by proving that the field component is impossible. No new executable certificate is necessary for (36). Independent exact-source reviews follow; unrestricted C0010 remains open.

### Independent review of the reversed even-characteristic symplectic orthogonal row

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `a7d778df81bb2fa70f8982f46754fbbe368a9487`, conditional on the stated canonical, natural/full-automorphism, Li–Xia and involution-formula inputs. Each checked the characteristic component and faithful natural-normalizer interface, unique semilinear-isometry representatives, explicit fixed-space descent and minus-type obstruction, injectivity on the single original outside coset, coefficientwise generating-function bound, uniform degree comparison and exact892<1080 endpoint. Each retained the separate m=2 graph-transport argument. reviewer A freshly inspected the FGS revised18February2017 Theorems2.15/5.6(2) and Giudici–Glasby–Praeger v1 dimension-six interface. reviewer C located the primary FGS PDF but retained the source authors's detailed formula inspection; reviewer B made no fresh primary-paper inspection. All retained the stated external classification inputs, and none ran a new executable computation or rederived those classifications. The acceptance concerns this actual reversed row; arbitrary symplectic full socles and C0010 remain open.

## Proposed complete exclusion of the reversed PSL4 symplectic row

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the stated canonical, classical-automorphism and Li–Xia inputs, Table1.1 row2 cannot be the actual factorization M=GI with solvable full point stabilizer I. Combined with the reviewed solvable-LMlt orientation, both orientations are excluded at every q. This is a factorization-family exclusion, not an exclusion of every PSL4(q) full socle.

Put S=Soc(M)=PSL4(q). The table gives the natural PSp4(q) normal in G0=G∩S, and the solvable-factor order bound

    |I∩S| ≤ 3q³(q³−1)/gcd(4,q−1).

The full socle is transitive, so cancellation in the linear order formula gives

    |Q|=|S:I∩S| ≥ D(q),
    D(q)=q³(q²−1)(q⁴−1)/3.                          (37)

### Retaining the graph centralizer

First let q≥3 and T=PSp4(q). The covering Sp4(q) is perfect. If a projective linear map centralizes T, its commutators with the covering group give a scalar character, which is trivial by perfectness. Absolute irreducibility of its natural module then makes the linear map scalar. Thus C_PGL4(q)(T)=1. Uniqueness up to scalar of the invariant alternating form identifies the natural semilinear normalizer as PΓSp4(q).

Let J be the standard alternating matrix, with entries0,1,−1, and define the graph automorphism

    γ0:[A] ↦ [J^−1 A^−T J].

It has order two projectively. For a symplectic similitude A with multiplier μ(A), γ0([A])=[μ(A)^−1 A]=[A]; it also commutes with the field maps. Hence γ0 centralizes PΓSp4(q). The full PSL4 automorphism description from the cited Kleidman–Liebeck Table2.1.B/Theorem2.1.4 gives

    N_Aut(S)(T)=PΓSp4(q)×⟨γ0⟩.

Inside PΓSp4(q), a nontrivial field component cannot centralize T: its field outer action is faithful and cannot be cancelled by an inner-diagonal automorphism. This includes even q=4; Harper arXiv:1703.09652v2, Table3, printed p.5, describes its field subgroup inside the exceptional cyclic outer group. Consequently

    C_Aut(S)(T)=⟨γ0⟩≅C2.                            (38)

The table's normal containment and the solvable quotient of this normalizer imply T=G^(∞), so T is characteristic in G. Restriction from the formal extension to Aut(T) therefore gives, within the single original outside coset, fibers of size at most two. Thus

    |Q|=|Λ|≤2 j(Aut(T)),                            (39)

where j counts elements of order at most two, including identity. The retained graph involution in (38) is essential; we do not assume G is itself almost simple.

### Even fields, including all graph-field involutions

Let q=2^f≥4. Fulman–Guralnick–Stanton's inspected Theorem4.3 gives

    j(Sp4(q))=q⁶+q⁴−q².

Harper Table3 gives Out(T)=C_(2f), whose only possible nonidentity involution label is ρ^f. If f is even this is the half-field label; if f is odd it is the graph-field label. In each case the Shintani map sends an involution to identity, so its class bijection and centralizer identity give a single T-class in that outer coset. The references are Harper Theorem2.2 and Remark2.3, printed p.6, equation(2.3) p.7 for the field case, and Proposition2.6 p.8 for the graph-field case. They give respective fixed groups Sp4(√q) and Sz(q). The source authors directly inspected these statements and the map's defining power, so the count uses the identity fiber, not just a formal analogy between cosets. Their standard orders give class sizes

    q²(q+1)(q²+1),         q²(q−1)(q+1)².

The second is smaller than the first. Therefore

    j(Aut(T)) ≤ q⁶+q⁵+2q⁴+q³ < (3/2)q⁶.           (40)

For q≥4, the product (1−q^−2)(1−q^−4)>3/4, hence D(q)>q⁹/4>3q⁶. This contradicts (39)–(40). No outer label or field-degree multiplicity is omitted.

### Odd fields: four rational types and the whole field coset

For odd q, Harper Table3 gives Aut(T)=PGSp4(q)⋊C_f. We first bound all projective linear involutions, including those whose lifts do not square to identity. Lift a nonidentity projective involution to A∈GSp4(q). Write A²=aI and let μ be its similitude multiplier. Then μ²=a², so μ=±a. There are at most four rational conjugacy types, indexed by the square class of a and the sign μ/a:

- If a is square, rescale A to square1. For μ/a=+1 its two eigenspaces are nondegenerate symplectic spaces, necessarily of dimensions2 and2. For μ/a=−1 they are paired Lagrangians, each of dimension2.
- If a is nonsquare, adjoining A makes V a two-dimensional space over F_(q²). For μ/a=+1, A is self-adjoint for the alternating form; the form is the trace of a nondegenerate alternating F_(q²)-form. For μ/a=−1, A is skew-adjoint; the form is Tr(c h), where h is nondegenerate Hermitian and c^q=−c.

These are rational descriptions over the indicated finite fields. Symplectic bases, and Hermitian orthogonal bases with norm rescaling, show uniqueness of each type up to GSp4(q)-conjugacy; no algebraic-closure class count is substituted. For example, in the nonsplit cases the adjoint relation is B(λv,w)=B(v,λw) or B(v,λ^q w), respectively, so the trace pairing recovers the asserted alternating or Hermitian form. The two eigenvalue signs, or the two conjugate roots of the fixed nonsquare a, do not add a form invariant.

The centralizer contains, respectively,

    Sp2(q)×Sp2(q),  GL2(q),  Sp2(q²),  GU2(q).

Each displayed group has order at least |GL2(q)| and meets the ambient scalar group in at most {±I}. Its image in PGSp4(q) therefore has order at least |GL2(q)|/2. Since |PGSp4(q)|=|Sp4(q)|, the sum of the at most four nonidentity class sizes gives the conservative bound

    j(PGSp4(q)) ≤ 1+8q³(q+1)(q²+1).                 (41)

If f is even, write q=s². The only nontrivial possible field label of an involution is σ:x↦x^s. Harper Theorem2.2/Remark2.3 and equation(2.4), pp.6–7, give one PGSp4(q)-class of involutions in the entire PGSp4(q)σ coset, with centralizer PGSp4(s). This counts both inner-diagonal labels together; splitting into T-classes is unnecessary. Its size is

    q²(q+1)(q²+1).

There is also a direct form-descent check. A lift b of such a projective semilinear involution has b²=cI with c∈F_s^×. Scalar norm rescaling makes b²=1. Its new multiplier μ has norm1; choose d with d/d^σ=μ. On the b-fixed F_s-space the form d^−1 B is F_s-valued, alternating and nondegenerate. A symplectic basis of that space supplies a similitude conjugating b to the standard field involution. Projective centralizing maps can likewise be scalar-adjusted to be defined over F_s, yielding the stated PGSp4(s) centralizer. This does not assume μ itself is a square in the norm-one group.

When f is odd there is no field term. In either case an upper bound is

    j(Aut(T)) ≤ 1+(8q³+q²)(q+1)(q²+1).              (42)

For every odd q≥5 this is less than D(q)/2. To check the entire range, divide by A(q)=q²(q+1)(q²+1). Then

    D(q)/A(q)=q(q−1)²(q+1)/3 ≥32q,
    2[1+(8q³+q²)(q+1)(q²+1)]/A(q)
       =16q+2+2/A(q)<16q+3<32q.

At q=5 the explicit bounds are319802<624000. This proves the required contradiction uniformly, without extrapolating a finite scan.

### The fields of size three and two

For q=3, T=PSp4(3)≅PSU4(2)≅Ω6^−(2). The automorphism identification and exact minus-orthogonal involution calculation in source `a7d778df81bb2fa70f8982f46754fbbe368a9487` give j(Aut(T))=892. The PSp4(3)=PSU4(2) identification is also the pinned ATLAS U4(2) input at `01e1be0bc7331170f94a3b1ef86abac077c81336`. Thus (39) gives at most1784 marks, whereas D(3)=5760. No new character-table computation is needed.

For q=2, S=PSL4(2)≅A8 and Aut(S)=S8; the source authors inspected the primary ATLAS A8=L4(2) identification and outer-group entries. The table's natural Sp4(2)≅S6 is not perfect. Its derived subgroup T≅A6 is characteristic in it and hence normal in G0. Every A6 subgroup of S8 fixes two points and acts naturally on the other six. Indeed a nontrivial orbit has size at least six by simplicity and |A6|>5!; seven does not divide360; an orbit of size eight would require a subgroup of order45. Such a subgroup would have a normal Sylow5 subgroup, centralize it since gcd(45,|Aut(C5)|)=1, and lie in its A6 centralizer of order5, a contradiction. Therefore

    N_S8(T)=S6×C2,       N_A8(T)≅S6.

It follows that G0 is this S6, T=G0′ is characteristic in G0, and G lies in S6×C2 with characteristic component T. If G acts faithfully on T, the reviewed almost-simple A6 canonical exclusion applies. Otherwise G contains the central C2, and its possibilities are A6×C2 or S6×C2. The q=3 central-extension argument at `01e1be0bc7331170f94a3b1ef86abac077c81336` applies verbatim to these abstract canonical groups: central characters vanish on the projected generating marks; inner inversion is impossible by the component theorem; the remaining outer cosets give at most72 marks. Equation(37) gives D(2)=120. This excludes q=2 without treating Sp4(2) as simple or assuming a particular exceptional S6 identification from its order alone.

The proof covers every q under its explicit inputs. The opposite orientation was already covered by `3313726ad58aa11de1c79e04d4618f28380925fb`. The normalizer argument was developed with a research reviewer; a research reviewer developed the class counts and field descent, and a research reviewer checked the four rational types and conservative projective centralizers. These are development checks, not independent exact-source review. No new executable certificate is required. Independent exact-source reviews follow; unrestricted C0010 remains open.

### Independent review of the reversed PSL4 symplectic row

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `793cb34657cdb232e7bb0be600e97acc42ec5c63`, conditional on the stated canonical, component, classical-automorphism, Harper/Shintani, FGS and Li–Xia inputs. Each checked the retained graph centralizer and characteristic component, original outside-fiber bound, even-field and Suzuki graph-field classes, four rational odd-field types and conservative projective centralizers, the entire PGSp field-coset count and both uniform inequalities. Each checked the q=3 transfer of the exact892 count and the q=2 A6 orbit/normalizer argument with the separately reviewed central-extension obstructions. reviewer A freshly inspected Harper arXiv:1703.09652v2 Propositions2.4/2.6 and the surrounding Shintani definitions; the other two retained the source authors's recorded primary inspections. None ran a new computation or rederived the external classifications. The acceptance is confined to this actual factorization family, not all PSL4 full socles or unrestricted C0010.

## Proposed complete exclusion of the reversed odd-orthogonal minus-component row

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the stated canonical, natural-normalizer, automorphism and Li–Xia inputs, Table1.1 row7 cannot be the actual factorization M=GI with solvable full point stabilizer I. With the previously reviewed opposite orientation, both orientations of this row are excluded. This does not classify arbitrary odd-orthogonal full socles or arbitrary orthogonal canonical groups.

Let S=Soc(M)=Ω_(2m+1)(q), m≥3 and q odd. The table supplies the natural L=Ω^−_(2m)(q) normal in G0=G∩S, fixing a nondegenerate line ℓ and acting on its minus-type perpendicular complement W, and

    |I∩S| ≤ (m/2) q^(m(m+1)/2)(q^m−1).             (43)

### Retaining the quasisimple lift and its centralizer

The embedded L is perfect and quasisimple; put T=L/Z(L)=PΩ^−_(2m)(q). Its possible center of order two is retained. In particular Ω6^−(3) is not silently replaced by its simple projective quotient. The normalizer N_S(L) is a nonsingular-line normalizer and has solvable quotient by L, using the reviewed natural embedding at `b8c237d84f001b9a3d70ab725adab6b67e57c05b` and Li–Xia Remark(ii), p.6. The outer quotient G/G0 is solvable under the classical automorphism description. Hence G/L is solvable and L=G^(∞) is characteristic in G.

Every automorphism of L acting trivially on T has a central error homomorphism L→Z(L), which is trivial because L is perfect. Thus Aut(L)→Aut(T) is injective. For m≥4 the natural projective semisimilarity realization Aut(T)=PΓO^−_(2m)(q) is the Kleidman–Liebeck1990 Table2.1.B/Theorems2.1.3–2.1.4 input, pp.15–16; the triality exception is plus type only. For m=3 the same realization follows from Giudici–Glasby–Praeger arXiv:2012.07213v1, proof of Theorem4.2, p.24, including q=3. These are the exact primary interfaces inspected in the reversed even-characteristic row, source `a7d778df81bb2fa70f8982f46754fbbe368a9487`.

The full automorphisms of S are natural semilinear similarities, by the same classical automorphism input. A centralizer of L preserves its unique common fixed line ℓ and W. Its restriction to W centralizes the projective T and is therefore projectively trivial by the faithful PΓO realization. Consequently its field component is trivial and its W action is scalar. In odd ambient dimension every similarity multiplier is a square, as follows by taking determinants in A^t B A=μB; rescale to an isometry and select the representative of determinant one. Its scalar on W is then ±1 and its scalar on ℓ is1. Therefore

    |C_G(L)|≤2.                                     (44)

This includes the possibility that diag(1,−I_W) lies outside L. In the formal extension E=G⋊⟨τhat⟩, restriction to characteristic L and then T has kernel on G exactly C_G(L), by the perfectness argument. Counting fibers within its single outside coset gives

    |Q|=|Λ|≤2j(Aut(T)).                              (45)

There is no assertion of a quotient folder on T.

### Projective field involutions cannot occur on a minus space

Suppose a projective semilinear similitude of W has order two and nontrivial field label. Then q=s² with field involution σ. A lift b satisfies b²=aI, and commuting b with b² shows a∈F_s^×. Choose c with c c^σ=a^−1 and replace b by cb, so b²=1. Its new quadratic multiplier μ has μ μ^σ=1. Choose d with d/d^σ=μ and replace the quadratic form F by d^−1F. Now b is a σ-semilinear isometry of the rescaled form. Its fixed F_s-space descends this nondegenerate form. Explicitly, choose e≠0 with e^σ=−e. For every v the two vectors (v+b(v))/2 and (v−b(v))/(2e) are fixed, and their combination with coefficients1,e is v. This decomposition is unique, proving that the fixed space has F_s-dimension2m and spans W over F_q. The restricted form has F_s-values and is nondegenerate.

Every nondegenerate even-dimensional quadratic form over F_s becomes plus type over F_(s²): a possible anisotropic plane splits over that quadratic extension. Scaling a form in even dimension does not change its discriminant square class or its type. This contradicts the original minus type. Thus every automorphism of T of order at most two has trivial field component and lies in PGO^−_(2m)(q). The order of operations in this argument matters: an isometry-normalized lift in odd characteristic could square to −I. We first normalize the square, and then rescale the form; no simultaneous square-root assumption is used.

### A uniform projective involution bound in odd characteristic

Write O=O^−_(2m)(q). Every scalar multiple of the even-dimensional quadratic form has the same type, so every nonzero scalar occurs as a similitude multiplier. Consequently |PGO|=|O|. A projective involution lifts to A with A²=aI and multiplier μ=±a, as in the preceding symplectic calculation. The following covers all actual projective types.

If a is square and μ=a, rescale A to an orthogonal involution. This contributes exactly j(O)/2 projective elements, including identity, since the two lifts differing by −I are both involutions. If a is square and μ=−a, its two eigenspaces would be complementary totally singular m-spaces, impossible in minus type.

If a is nonsquare and μ=a, the E=F_(q²) structure defined by A is self-adjoint and the F_q form is the trace of a nondegenerate symmetric E-form h of dimension m. Exactly one of the two E-discriminant types can induce the fixed minus type. Indeed the determinant square class of the trace form is

    disc(E/F_q)^m Norm_(E/F_q)(det h).

For E=F_q(√a), the trace pairing has determinant4a, a nonsquare; the norm sends the nonsquare class of E^× to the nonsquare class of F_q^×. Thus the two E-types have opposite F_q discriminant classes. Finite-field symmetric-form classification gives at most one actual conjugacy class for the admissible type. Its projective centralizer contains O_m^ε(q²)/{±I} for that type.

If a is nonsquare and μ=−a, the adjoint on E is its field involution, and the original symmetric form is the trace of a Hermitian E-form. Hermitian orthogonal bases and norm rescaling give at most one actual conjugacy class, with projective centralizer containing GU_m(q)/{±I}. This may be absent for some m; retaining it only enlarges the upper bound. In both nonsplit cases, choosing the other root of a can only identify classes: it does not add an independent form type. These are rational form arguments and centralizer subgroups, not an inference from an algebraic-closure class count.

We bound their sizes using the exact orthogonal and unitary orders. Put c_r=∏_(i=1)^r(1−q^−(2i)); for odd q≥3, c_r>7/8. For every k≥1 and either available type,

    |O_k^ε(q)|≥(4/3)q^(k(k−1)/2),
    |O|≤(56/27)q^(2m²−m).                           (46)

For odd k, the first coefficient exceeds7/4. For even k=2r with r=1 it is at least2(1−1/q)≥4/3; for r≥2 it exceeds2·(8/9)·(7/8)=14/9. The second inequality uses 1+q^−m≤28/27 and drops factors less than one. The formulas are Fulman–Guralnick–Stanton, revised18February2017, equations(3)–(4), printed p.6, with the usual odd-characteristic orders.

An ordinary orthogonal involution is determined by its nondegenerate eigenspace decomposition. For each dimension1≤r≤2m−1 there are at most two types, and the centralizer is O_r×O_(2m−r), as stated in FGS Lemma5.1, printed p.22. Hence (46), together with the two scalar involutions, gives

    j(O)/2 ≤ 1+(7/6)q^(m²)∑_(t∈Z)q^(−t²)
            ≤1+(7/3)q^(m²),                        (47)

since the sum is at most1+2/(q−1)≤2. The nonsplit self-adjoint type contributes at most (28/9)q^(m²), by applying (46) over F_(q²) and retaining the central quotient of size at most two. The Hermitian type contributes at most (112/27)q^(m²−m), since |GU_m(q)|≥q^(m²); the latter follows by pairing the factors (1+q^−(2i−1))(1−q^−(2i))>1 in its normalized order. Therefore

    j(Aut(T))=j(PGO^−_(2m)(q))
       ≤1+(7/3+28/9+112/729)q^(m²)
       <6q^(m²)                                    (48)

for all m≥3 and odd q≥3. Identity is included. The elementary form arguments above supply the projective types missing from a count of ordinary orthogonal involutions alone.

### Degree comparison and the m=3,q=3 boundary

The order of the actual odd-orthogonal socle has the factor1/2:

    |S|=(1/2)q^(m²)∏_(i=1)^m(q^(2i)−1).

This factor cancels the1/2 in (43). Socle transitivity therefore gives

    |Q|=|S:I∩S| > (7/(8m))q^((3m²−m)/2).           (49)

The right side exceeds the capacity in (45),(48) whenever

    q^(m(m−1)/2) ≥ 96m/7.                           (50)

For m≥4,q≥3 this starts at3^6=729>384/7 and strengthens with either parameter: increasing m multiplies the left side by at least3^m, more than (m+1)/m. For m=3 it holds for every odd q≥5, starting at125>288/7. Only m=3,q=3 remains.

Here |O6^−(3)|=26127360. FGS Lemma5.1(2), using the exact eigenspace orders, gives

    j(O6^−(3))=2+4·126+2·4536+2·2835+2·11340=37928.

The ordinary projective contribution is18964. The unique admissible E-symmetric type has centralizer at least |O3(9)|/2=720, and the Hermitian type has centralizer at least |GU3(3)|/2=12096. Thus

    j(Aut(T))≤18964+36288+2160=57412,
    |Λ|≤114824 <161280
       =4585351680/28431
       =|Ω7(3)|/[3·3^6(3³−1)/2].                  (51)

This uses the actual Ω7 order, not the twice-larger Sp6 order. The displayed integer formulas suffice to reproduce the endpoint without group enumeration or a new executable certificate. The source authors directly inspected FGS Lemma5.1 and Li–Xia Table1.1 row7 for this deduction.

The original marked set is therefore too small in every parameter, completing the proposed reversed-row exclusion. The opposite solvable-LMlt orientation was reviewed in `3313726ad58aa11de1c79e04d4618f28380925fb`. The source authors developed the projective field-descent repair, the uniform coefficient estimates and the trace-discriminant refinement; a research reviewer checked the rational types, arithmetic and estimates, while a research reviewer checked the characteristic quasisimple lift and its centralizer. An initial missing factor1/2 in the exploratory socle order was corrected before this canonical proof; the exact boundary uses (51). These development checks are distinct from the independent exact-source reviews below; unrestricted C0010 remains open.

### Independent review of the reversed odd-orthogonal minus-component row

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `0596f0e429f9f558e40ad542e83068a7f7828975`, conditional on the stated canonical, quasisimple-lift, natural/full-automorphism, Li–Xia and FGS inputs. Each checked the retained center of L and characteristic restriction, injectivity of Aut(L)→Aut(T), the at-most-two original outside fibers, the order of square normalization and form rescaling in field descent, and every projective rational form type. Each checked the trace-discriminant restriction, projective centralizer factors, uniform bound6q^(m²), the factor1/2 in the odd socle order and the exact2·57412<161280 boundary. reviewer A freshly inspected the revised2017 FGS Lemma5.1 and its eigenspace/centralizer statement; the other two retained the source authors's primary inspections. None ran a new group computation or rederived the external classifications. The acceptance covers this actual row, not arbitrary orthogonal full socles or closure of C0010.

## Proposed completion of both orientations of the infinite classical solvable-factor table

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the pinned canonical, natural-embedding, automorphism, class-count and Li–Xia inputs, no row of Li–Xia Table1.1 is the actual factorization M=GI of a finite simple nonassociative Bol loop when either factor is solvable. The solvable-LMlt orientation was reviewed at `3313726ad58aa11de1c79e04d4618f28380925fb`; the reversed rows1–7 are covered by the preceding reviewed sections. The proof below closes reversed rows8–9. This does not close Table1.2, the alternating, sporadic or both-solvable alternatives with solvable I, or any general operation-level classification.

Here S=PΩ^+_(2m)(q), m≥4, and the actual G0=G∩S normally contains the subgroup T named Ω_(2m−1)(q) in the table. In its natural point embedding T is Ω_(2m−1)(q) for odd q and Sp_(2m−2)(q) for even q. It is nonabelian simple in every present parameter. Dimension eight is retained, including all possible ambient triality automorphisms. The natural embeddings, including transport of the table's dimension-eight embedding to the point model, are the previously reviewed Li–Xia Remark(ii) and orthogonal-row inputs; no assertion is made that the actual point stabilizer I is this natural-point normalizer.

Writing d=gcd(4,q^m−1), the table gives |I∩S|≤m q^(m(m−1)/2)(q^m−1)/d. The projective orthogonal socle order and transitivity give

    |Q|=|S:I∩S| ≥ (1/m)q^(m(m−1)/2)
                         ∏_(i=1)^(m−1)(q^(2i)−1).  (52)

### A centralizer bound that retains triality

Let A≤Aut(S) be the subgroup of natural projective semilinear similarities. Kleidman–Liebeck1990 Table2.1.B and Theorem2.1.4, pp.15–16, give [Aut(S):A]=1 except at m=4, where it is3. We will prove |C_A(T)|≤2; it follows directly that

    |C_Aut(S)(T)|≤6,                                (53)

because [C_Aut(S)(T):C_A(T)]≤[Aut(S):A]. No claim that an outside triality coset preserves, or fails to preserve, the subgroup class of T is needed.

In odd characteristic, T fixes the nondegenerate point ℓ and acts absolutely irreducibly on W=ℓ^⊥. A centralizer preserves this unique fixed line. On W its semilinear action centralizes the natural Ω_(2m−1)(q). Faithfulness of its field outer action and scalar linear commutant make this action scalar. The multiplier on W is consequently a square, so a projective representative can be rescaled to an isometry. It acts by independent signs on ℓ and W; modulo the global sign there are at most two possibilities.

In even characteristic, write ℓ=⟨e⟩ with F(e)≠0 and use the alternating polar form B. The natural point stabilizer T acts on ℓ^⊥/ℓ as the full Sp_(2m−2)(q). Its common fixed space in the natural V is precisely ℓ. A fixed vector in ℓ^⊥ outside ℓ would contradict irreducibility on the quotient. A fixed vector outside ℓ^⊥ would give a fixed nondegenerate plane with e and a faithful action of Sp_(2m−2)(q) on its orthogonal complement of dimension2m−2, impossible because either orthogonal group there has smaller order than that symplectic group. Thus a centralizer preserves ℓ.

Normalize a semilinear similarity centralizing T to an isometry, using the unique square root of its multiplier. On ℓ^⊥/ℓ, the scalar-commutant and faithful field-action argument for Sp_(2m−2)(q) forces trivial field component and scalar action. This scalar has square1 and is therefore1; the isometry fixes e as well. For w∈ℓ^⊥ write g(w)=w+f(w)e. Preservation of F gives f(w)^2 F(e)=0, so f=0. The map fixes ℓ^⊥ pointwise. For a vector u with B(u,e)=1, its image is u+a e and the isometry equation is a²F(e)+a=0. There are only two possibilities: identity and the orthogonal symmetry about e. This proves |C_A(T)|≤2 in even characteristic too. The field automorphism descriptions used here are Harper Table3, p.5; the symplectic quotient dimension is at least six, so its exceptional dimension-four graph case never occurs.

Since T is normal in G0 by the actual table containment, conjugation of G0 on T has solvable kernel of order at most two and image modulo T in the explicitly solvable classical outer group. Thus G0/T is solvable. Its perfect residual is T, which is characteristic in G0 and normal in G. Since G/G0 is also solvable, T=G^(∞) is characteristic. In the formal extension, restriction to T has fibers of size at most six within the single original outside coset, by (53). Consequently

    |Q|=|Λ|≤6j(Aut(T)).                              (54)

This retains every possible centralizing triality element and uses no quotient-loop assertion.

### Full automorphism counts for the component

Put k=m−1≥3 and P_r(q)=∏_(i=1)^r(1−q^−(2i)). For even q, T=Sp_(2k)(q). FGS Theorem4.3 and generating identity(12), printed pp.19–21, give

    j(T)/q^(k²+k)
       ≤∏_(i≥1)(1+q^−(2i))/(1−q^−(2i))<3.         (55)

To check this uniformly, the generating identity has nonnegative product coefficients, so its degree-k coefficient after the factor1/(1−u) is at most the product evaluated at1. The finite factor P_k is at most1. For x_i=q^−(2i)≤1/4, log((1+x_i)/(1−x_i))≤2x_i/(1−x_i), whose sum is at most8/9; exp(8/9)<3. One must not cancel the finite P_k against the smaller infinite product in the opposite direction.

All outer automorphisms of this T are field automorphisms. There is at most one nontrivial field label of an involution. When q=s², the inspected Harper Theorem2.2/Remark2.3 and equation(2.3), pp.6–7, give one T-class in that coset with centralizer Sp_(2k)(s). Its size is

    q^(k²+k/2)∏_(i=1)^k(1+q^−i)
       <(3/2)q^(k²+k/2),

since q≥4 and the product is at most exp(1/3)<3/2. If q is not a square the term is absent. Hence

    j(Aut(T))<(9/2)q^(k²+k)              (q even).   (56)

For odd q, T=Ω_(2k+1)(q), and the full inner-diagonal group is SO_(2k+1)(q), with cyclic field quotient, by Harper Table3. For a coarse upper bound count all involutions in the larger O_(2k+1)(q). FGS Lemma5.1 and the order bounds in (46) give at most two rational classes for each nontrivial eigenspace dimension r, each of size at most (9/8)q^(r(2k+1−r)). The two scalar involutions contribute2. The exponent is largest at r=k,k+1, and the two tails have successive deficit t(t+1). Therefore

    j(SO_(2k+1)(q)) ≤ j(O_(2k+1)(q))
       ≤2+(9/4)q^(k²+k)·2∑_(t≥0)q^(−t(t+1))
       ≤2+(81/16)q^(k²+k)<6q^(k²+k).               (57)

Here ∑q^−t(t+1)≤1/(1−q^−2)≤9/8. This deliberately includes the entire diagonal group rather than only the simple Ω subgroup.

There is again at most one nontrivial involutory field label. For q=s², the connected odd-dimensional SO Shintani identity, Harper equation(2.5) with Theorem2.2/Remark2.3, pp.6–7, gives one SO(q)-class, centralizer SO(s), and size

    q^(k²+k/2)∏_(i=1)^k(1+q^−i)
       <(8/7)q^(k²+k/2),

since s≥3 and exp(1/8)<8/7. Thus the safe bound is

    j(Aut(T))<8q^(k²+k)                  (q odd).    (58)

The source class bijection is applied to the identity power, as in the preceding row; no multiplication by the field degree or uncounted diagonal-field coset remains.

### Uniform comparison, including the smallest even field

The product in (52) yields

    |Q|>(2/(3m))q^(3m(m−1)/2)       for even q,
    |Q|>(7/(8m))q^(3m(m−1)/2)       for odd q.       (59)

For even q, (54),(56) give |Λ|<27q^(m(m−1)). This contradicts (59) whenever q^(m(m−1)/2)≥(81/2)m. It holds at m=5,q=2 (1024>405/2) and m=4,q=4 (4096>162), and increases with either parameter. Thus only m=4,q=2 requires exact arithmetic.

At that pair, Aut(Sp6(2))=Sp6(2), and FGS Theorem4.3 gives its five contributions A0,C1,A2,B2,C3 as

    j(Sp6(2))=1+63+315+945+3780=5104.

The denominators in those class formulas are1451520,23040,4608,1536,384, with numerator |Sp6(2)|=1451520. Equation(52) gives degree at least45360. Hence even the retained factor six gives

    |Λ|≤30624<45360.                                (60)

This analytic evaluation avoids a new character-table or loop-enumeration dependency.

For odd q, (54),(58) give |Λ|<48q^(m(m−1)), whereas (59) is larger whenever q^(m(m−1)/2)≥(384/7)m. This holds already at m=4,q=3, since729>1536/7, and increases with both parameters. There is no remaining odd-field boundary.

Thus reversed rows8–9 are impossible. Combined with reversed rows1–7 and the earlier solvable-LMlt assembly, this gives the proposed both-orientations completion of Table1.1. The source authors supplied the index-three triality bound and uniform comparisons; a research reviewer checked the natural centralizers, and a research reviewer checked the counts and endpoint. An incorrectly cancelled finite/infinite product in an exploratory bound was rejected; (55) uses the weaker, correctly directed estimate. These development checks are distinct from the independent exact-source reviews below. Table1.2 and the other factorization alternatives with solvable I, as well as unrestricted C0010, remain open.

### Independent review of both orientations of the infinite classical table

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `39ba2fc7cb5b6d28ff0c37df0e5afd7dc82bcb91`, conditional on the stated canonical, natural-embedding, classical-automorphism, Li–Xia, Harper and FGS inputs. Each checked the natural centralizers, including the even-characteristic unique fixed line and quadratic elimination of shears, the index-three bound retaining all triality possibilities, the characteristic component and original outside-fiber bound. Each checked the correctly directed finite-product coefficient estimate, the full odd/even automorphism counts and field terms, the uniform degree inequalities and the exact6·5104<45360 endpoint. Each checked the assembly with previously reviewed rows1–7. reviewer A freshly inspected FGS Theorem4.3/equation(12) and Harper v2 equation(2.5)/Proposition2.5; the other two retained the source authors's recorded primary inspections. None ran new computation or rederived the external classifications. The acceptance covers both orientations of Table1.1, not the remaining reversed finite/nonclassical alternatives or unrestricted C0010.

## Proposed radical capacity lemma and reversed finite linear and unitary exclusions

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Retain the canonical generating section and inversion, the almost-simple primitive full-multiplication hypothesis, and the precise Li–Xia actual-factor inputs. Write G=LMlt(Q), M=Mlt(Q), I=M₁, S=Soc(M), G0=G∩S and I0=I∩S. Here I is solvable. Table1.2 of Li–Xia arXiv:1408.0350v3, printed p.8, specifies equality for the displayed G0 and an upper bound for I0. The source authors freshly inspected those different column conventions. Since S is transitive,

    |Q|=|S:I0|,       G/G0 ≤ Out(S).

No equality between I0 and its displayed overgroup is assumed.

### Capacity through the solvable radical

Suppose R0=Rad(G0) and G0/R0=T is nonabelian simple. Put R=Rad(G). The subgroup R0 is characteristic in G0, hence normal and solvable in G, so R0≤R. Conversely R∩G0 is solvable normal in G0; thus R∩G0=R0. The image T of G0 in G/R is normal simple with solvable quotient. Its centralizer intersects T trivially and injects into that solvable quotient, so it is a solvable normal subgroup of the radical-free group G/R and must be trivial. Consequently

    T ≤ G/R ≤ Aut(T),       (G/R)^(∞)=T.

Canonical inversion preserves R and this characteristic T. Conjugation therefore defines a map E=G⋊⟨τhat⟩→Aut(T). Its kernel on G is exactly R. Two elements of the single original outside coset τhat G with the same image differ by an element of R. Since the actual marked set Λ consists of involutions in this coset, its images have order at most two. With j(A)=|{a∈A:a²=1}|,

    |Q|=|Λ| ≤ |R| j(Aut(T))
              ≤ |R0| |G:G0| j(Aut(T)).

This needs neither a quotient-loop structure nor characteristicity of a chosen module inside R. The possible extra kernel in the whole formal extension does not introduce a factor two on its one outside coset. A parallel form for a simple characteristic subgroup T≤G is |Λ|≤|C_G(T)|j(Aut(T)). In particular, if G0^(∞)=T, then G^(∞)=T because G/G0 is solvable, and |C_G(T)|≤|C_G0(T)|·|G:G0|. These are general finite-group deductions under the canonical-marked-set hypothesis.

### Reversed Table1.2 rows6–8

The table and classical orders give the following exact lower bounds:

| Row | S | Stabilizer order upper bound | Loop order lower bound |
| --- | --- | ---: | ---: |
| 6 | PSL4(3) | 320 | 18954 |
| 7 | PSL4(3) | 1053 | 5760 |
| 8 | PSL4(4) | 12096 | 81600 |

Here |PSL4(3)|=6065280, |PSL4(4)|=987033600 and both ambient outer groups have order four. In the simple-component alternatives T=G0^(∞), the original-fiber bounds are:

| Row and actual G0 | T | Centralizer order bound | j(Aut(T)) | Capacity |
| --- | --- | ---: | ---: | ---: |
| 6: PSL3(3) | PSL3(3) | 4 | 352 | 1408 |
| 7: (4×PSL2(9)):2 | PSL2(9) | 32 | 112 | 3584 |
| 8: (5×PSL2(16)):2 | PSL2(16) | 40 | 324 | 12960 |

Each capacity is strictly less than its degree bound. For row7, the intentionally loose |C_G0(T)|≤|G0:T|=8 is enough; for row8 use ten. Thus no assertion about how the final involution acts on the component, or about an extension-field realization of those embeddings, is needed.

The counts use the reviewed odd-dimensional linear interface at `b436485f3c07c3413c19b319e51e8c7bc2c3a580` and `d5e26dd6aef4ad09f61e0569e383782dea0d468b`, and [the PSL2 counts](../primitive-completion/sd3-involution-count.md) assembled at `47b07688a82d3df93f537946fe0780112200383b`. For PSL3(3), the contributions are identity1, inner117 and graph234, the latter |PSL3(3)|/|SO3(3)|=5616/24. For PSL2(9) the full automorphism count is112. For PSL2(16) it is256+68=324: the unique field-involution class has size4080/60. These are evaluations of the cited formulas, without a new character-table dataset.

For row6's other actual equality G0=3³:PSL3(3), use the natural point-parabolic interface from the [all-dimensional Singer–parabolic proof](#proposed-exclusion-of-the-linear-singer-parabolic-family-in-every-dimension), reviewed at `472e2653976598a9666142e7f64e07a4601c61e8`. Its radical U=3³ has a unique common fixed point, so G normalizes that parabolic and has no graph part. The same faithful natural-action argument gives U=O3(G), G/U≤GL3(3), and characteristic derived subgroup SL3(3) in the quotient. The reviewed original-fiber calculation bounds the marks by affine involutions, without assuming an affine lift. The two scalar classes contribute1 and27; the two nontrivial eigenspace classes have size117 and translation counts3 and9. Thus

    |Λ|≤1+27+117(3+9)=1432<18954.

This finishes both actual alternatives in row6 and all of reversed rows7–8, conditional on the stated embedding, canonical and count inputs.

### Reversed Table1.2 row21

Now S=PSU4(8), |S|=34693789777920, and |I0|≤513·3=1539. Thus |Q|≥22543073280. The actual G0=2^12:SL2(64).7 has normal U of order4096, and G0/U has normal T=SL2(64)=PSL2(64) with quotient of order seven. Since |Out(T)|=6, the induced outer action is trivial. For a centerless simple T, its centralizer in this extension then has order seven: adjust each conjugating element by an element of T. Hence the extension is T×C7. Its radical is C7, and lifting it shows

    |R0|=4096·7,       G0/R0≅PSL2(64).

The ambient outer group has order six. The preceding radical lemma applies with no module-embedding or characteristic-U assertion. The reviewed PSL2 formula gives

    j(Aut(PSL2(64)))=4096+|SL2(64)|/|SL2(8)|
                   =4096+262080/504=4616.

The field quotient has order six and just one involutory label; its fixed group is SL2(8). Therefore

    |Λ|≤4096·7·6·4616=794099712<22543073280.

This excludes the reversed row21. The source authors supplied the radical argument; a research reviewer and a research reviewer checked it during development, and a research reviewer developed the linear-row counts. These are development checks, not independent exact-source reviews. The deduction neither classifies general radicals nor closes the remaining finite table or unrestricted C0010.

## Proposed reversed finite symplectic action and capacity exclusions

**Conditional continuation of C0010, with three independent exact-source reviews below.** In the preceding setting, reversed Table1.2 rows10–11 and16–17 are excluded as follows. This section does not yet assert rows12–15 or the complete finite table.

For rows10–11, both displayed solvable overgroups of I0 have order648. Since S=PSp4(3) is transitive, IS=M and |I| divides |M:S|·648. The actual I is maximal by primitivity. The complete maximal-order inputs of the [finite both-solvable PSp4(3) certificate](#proposed-finite-both-solvable-psp43-exclusion) list

    S:       960,720,648,648,576;
    Aut(S):  25920,1920,1440,1296,1296,1152.

Only orders648 in S or1296 in Aut(S) satisfy that divisibility. For all four surviving classes, [verify_psp43_both_solvable.g](../code/verify_psp43_both_solvable.g) gives degree40 and rank3. The scoped C0017 rank-three restriction excludes the actual nonassociative simple-loop action. Although the earlier theorem concerned solvable canonical G, this order/fusion/rank calculation uses only M and I. Its application here is a new, explicit rescoping requiring review. It covers every listed G0 alternative in row11, and does not replace the I0 containment by equality. Completeness and correctness of the pinned GAP4.15.1/CTblLib1.3.11 maximal and fusion inputs remain assumptions.

In row16, S=Sp6(2) has trivial outer group. Thus G=G0 is exactly A8 or S8. Its characteristic perfect residual is T=A8 and C_G(T)=1. Since Aut(A8)=S8,

    j(Aut(T))=∑_(k=0)^4 8!/((8−2k)!2^k k!)=764.

The table bounds |I0| by3³·2·24=1296, so |Q|≥1451520/1296=1120>764. This uses the already pinned ATLAS automorphism identifications and no new maximal-subgroup claim.

In row17, G0=PSL2(27):3 has characteristic perfect residual T=PSL2(27). The table's nontrivial field extension has C_G0(T)=1. Since |G:G0|≤|Out(PSp6(3))|=2 and G/G0 is solvable, T=G^(∞) is characteristic and |C_G(T)|≤2. The field quotient of Aut(T)=PΓL2(27) has odd order three, so all its involutions lie in PGL2(27), giving j=1+27²=730. Thus |Λ|≤1460. On the other hand |PSp6(3)|=4585351680 and |I0|≤3⁵·2⁵·10=77760, so |Q|≥58968, a contradiction.

The direct capacities avoid an unnecessary new subgroup-normalizer computation. a research reviewer developed the rows10–11 rescoping and a research reviewer developed rows16–17. Their development checks are not independent review of this source. The exact source table, full automorphisms, earlier rank restriction and canonical inputs remain explicit dependencies; the remaining finite and global cases stay open.

### Independent review of radical capacity and the first reversed finite rows

automated-model reviewer A, reviewer B and reviewer C independently accepted the preceding two sections at exact source `cc8c3324974c20359ea064cacf8b2750b5f293f3`, conditional on their stated canonical, Li–Xia, natural-embedding, automorphism/count and complete class/fusion inputs. Each checked the radical intersection, faithful radical-free quotient, characteristic simple residual and original outside-fiber bound without an extra factor two; the rows6–8 component and affine capacities; row21’s centralizer of order seven, lifted radical and4616 count; rows10–11 actual-maximal-stabilizer divisibility and rescoping; and the rows16–17 counts764 and730. Each extracted and read the exact committed `verify_psp43_both_solvable.g` and independently ran it with GAP4.15.1/CTblLib1.3.11, obtaining all four degree40, rank3 outputs. The first reviewer retained its earlier primary table and metadata inspections; the other two retained the recorded source inspections. None freshly rederived the external classifications. This acceptance covers only the displayed radical lemma and reversed rows6–8,10–11,16–17,21; the other finite cases and unrestricted C0010 remain open.

## Proposed completion of both orientations of the finite classical solvable-factor table

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Under the canonical, almost-simple full-multiplication, Li–Xia, classical-group and explicitly retained finite-data inputs, every actual Li–Xia Table1.2 row is excluded with solvable full stabilizer I. Combined with the earlier solvable-LMlt result, this completes both orientations of that finite table. It does not assert that the two classical tables exhaust unrestricted C0010. Retain G=LMlt(Q), M=Mlt(Q), I=M₁, S=Soc(M), G0=G∩S and I0=I∩S. The source table gives equality for G0 and containment for I0.

### Reversed rows12–15 without an embedding classification

Here S=PSp4(q), q=5,7,11,23, and G0 is T=PSL2(q²) or a split T:2. First exclude an inner action in that split extension, without assuming a particular embedding of T. If a nonidentity involution c∈S centralized T, lift c to A∈Sp4(q) with A²=±I. For A²=I, the two nonzero eigenspaces are nondegenerate symplectic planes, and the linear centralizer is Sp2(q)×Sp2(q). Passing to the projective centralizer can add at most the exchange of the two planes, a factor two, before dividing by the scalar center. For A²=−I, the centralizer is GL2(q) when −1 is a square, or GU2(q) when it is not: in the first case the two eigenspaces are paired totally isotropic planes; in the second case the induced quadratic-extension structure carries the corresponding Hermitian form. Projective centralization again allows only A↦±A and so adds at most a factor two. These elementary eigenspace descriptions show that every prime dividing C_S(c) divides 2q(q²−1).

But (q²+1)/2 is odd, greater than one, and coprime to q(q²−1); any prime divisor of it divides |T|=q²(q²−1)(q²+1)/2. Lagrange therefore forbids T≤C_S(c). If the complement of the displayed split T:2 acted by an inner automorphism, adjusting its involutory generator by the corresponding element of centerless T would give a centralizing involution outside T. Thus the action is outer and faithful. This argument uses only the table's split extension and the elementary involution centralizers, not a classification of copies of T in S.

Consequently G0 has trivial solvable radical and characteristic perfect residual T. The radical R=Rad(G) satisfies R∩G0=1 and |R|≤|Out(S)|=2. If R=1, the centralizer C_G(T) is a solvable normal subgroup (it injects into G/G0), hence trivial, and G is an almost-simple PSL2 group excluded by the reviewed theorem at `47b07688a82d3df93f537946fe0780112200383b`. If R has order two, it is central and G=G0×R.

Write B=G0 in this latter case. The canonical center-fixing theorem at `e7476945cf987cf1c654a385ac8f78fe2beb320a` forces τ to fix R. An automorphism of B×R has form (b,z)↦(β(b),z+χ(b)), with β∈Aut(B) and a homomorphism χ:B→C2. For every τ-inverted generator, χ(b)=0; since the actual section generates G, χ=0. If β is inner on B, τ is inner on G, contradicting the component version of the inner-inversion theorem at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`.

Put Q0=q². Since q is prime, Out(T)=C2×C2. The reviewed PSL2 formulas count the diagonal, pure-field and mixed outer involutions as

    Q0(Q0−1)/2,       q(q²+1),       0.

A faithful split T:2 is therefore diagonal or field, since the mixed coset has no involution. For either such B, restriction identifies Aut(B) with Aut(T): it is injective because C_B(T)=1, and every automorphism of T normalizes B because Out(T) is abelian. If β is outer on B, its coset βB is the union of the other nonmixed outer T-coset and the mixed one. For B=T there is just one outer coset. The original outside fibers have size two, so in all cases

    |Λ|≤2 max{q²(q²−1)/2,q(q²+1)}=q²(q²−1),

where the diagonal term dominates for q≥5. The exact comparisons are:

| Row | q | Solvable stabilizer order upper bound | Loop order lower bound | Mark upper bound |
| --- | ---: | ---: | ---: | ---: |
| 12 | 5 | 6000 | 780 | 600 |
| 13 | 7 | 49392 | 2800 | 2352 |
| 14 | 11 | 159720 | 80520 | 14520 |
| 15 | 23 | 6424176 | 3218160 | 279312 |

The degree formula is |PSp4(q)|/[displayed order], with |PSp4(q)|=q⁴(q²−1)(q⁴−1)/2. Each strict gap excludes its row. The source authors and a research reviewer developed this argument; it replaces an unnecessary natural-normalizer identification by a divisibility argument and retains the reviewed full outer-coset counts.

### Reversed row20 and both exceptional linear embeddings

For S=PSU4(3), the actual G0=T=PSL3(4) is normal in G. The certificate [verify_reversed_psu43_l34.g](../code/verify_reversed_psu43_l34.g), frozen at `33c16afc7f8497586e24e0e8d5bde25ffc46c3ec`, proves C_Aut(S)(T)=1 for every embedded copy, conditional on its ATLAS representation identification and complete CTblLib maximal list.

Explicitly, the embedded ATLAS generators give A=Aut(S) of order26127360, transitive on324 points. Its derived simple socle S has order3265920 and two point orbits of size162. For N=A₁ and T=S∩N, the verifier checks

    |N|=80640,       T≅PSL3(4),       |T|=20160,
    N_S(T)=T,       N_A(T)=N,         C_A(T)=1.

The isomorphism check distinguishes T from other simple groups of order20160. Because N is the full normalizer, the324 conjugates of T divide into two S-classes of size162, not two point orbits representing one subgroup class. They are A-conjugate. Every maximal subgroup of S whose order is divisible by20160 is one of the two listed PSL3(4) classes, checked against every maximal entry. Thus every embedded copy is maximal and belongs to these two classes. The primary ATLAS page identifies the degree324 representation, and Crnković–Mikulić–Rodrigues, published2010, §3/Table1, pp.309–310, independently displays the two degree162 classes and their outer conjugacy; the source authors inspected these statements. The group and subgroup classification inputs are not inferred from orders alone.

It follows that actual G≤N_A(T) embeds faithfully into Aut(T) and is almost simple with socle PSL3(4). The reviewed all-odd-dimensional almost-simple canonical PSL theorem at `114ce1b011fd47589eb762ed7cd5492a190002d8` excludes it. This avoids a projected-folder assertion. a research reviewer developed the finite input; exact-source independent review is still required.

### Reversed rows22–28: all subgroup classes and triality

The certificate [verify_reversed_finite_orthogonal.g](../code/verify_reversed_finite_orthogonal.g), also frozen at `33c16afc7f8497586e24e0e8d5bde25ffc46c3ec`, retains complete maximal lists, class-specific fusion maps and full automorphism-table identifications as external inputs. The following group arguments turn those data into the needed characteristic-component and centralizer bounds.

For row22, the only maximal subgroups of S=Ω7(3) with orders divisible by |G2(3)| are the two classes of that exact order. Thus actual T=G0=G2(3) is maximal, N_S(T)=T and C_S(T)=1. The same conclusion holds for row23, T=Sp6(2): its only additional candidate maximal overgroup is U=2.PSU4(3).2 of order13063680. This U has a normal subgroup D=2.PSU4(3) of index two. Perfectness of T would force T≤D, but |D|/|T|=9/2 is not an integer, contradicting Lagrange. All other candidates have exactly the order of T. Since |Out(Ω7(3))|=2, both rows have |C_G(T)|≤2.

For row25, the only maximal overgroups in S=Ω8⁺(2) whose orders are divisible by |Sp6(2)| are the three classes of precisely that order. For row26, the possible overgroups of A9 are its three maximal classes and the three Sp6(2) classes. A hypothetical inclusion A9<Sp6(2) has index eight; the coset action would embed simple Sp6(2) into S8, impossible by order. Hence every such A9 is maximal. In both rows C_S(T)=1 and |C_G(T)|≤|Out(S)|=6. This covers all classes without identifying them as natural point components.

For row28, the only possible maximal overgroups of T=Ω8⁺(2) in S=PΩ8⁺(3) are four classes of exactly the order of T. Thus C_S(T)=1 and the deliberately conservative bound is |C_G(T)|≤|Out(S)|=24.

For row27, the six maximal Ω7(3) classes likewise exhaust all possible embeddings by the maximal-order test. Put A=Aut(S), |A:S|=24. For each of those six classes, the verifier induces its trivial character to S and finds unequal values on two S-classes fused in the actual extension S:3. If triality preserved that subgroup's S-conjugacy class, the induced character would be invariant, contrary to this witness. Therefore the A-orbit of every such subgroup class has at least three elements. Its stabilizer in Out(S), namely N_A(T)S/S, has order at most eight. Since C_A(T)∩S=1,

    |C_G(T)|≤|C_A(T)|≤8.

This does not claim that all six classes are mutually fused. It does not apply Table1.1's natural-embedding remark to Table1.2 without proof. In all the preceding simple-component rows, G0=T and G/G0 is solvable, so T=G^(∞) is characteristic as needed for the original outside-fiber count.

Row24 instead has the natural quasisimple component L=Ω8⁻(3), with its center retained, in S=Ω9(3). The source placement is Li–Xia v3 Proposition7.13, proof Case2/Table7.5 row3, printed pp.61–62, already inspected and pinned for the earlier finite action. The characteristic-component, centralizer and full projective-involution arguments of the [reversed odd-minus row](#proposed-complete-exclusion-of-the-reversed-odd-orthogonal-minus-component-row), reviewed at `0596f0e429f9f558e40ad542e83068a7f7828975`, apply independently of that earlier solvable-factor bound. They give L=G^(∞), |C_G(L)|≤2 and j(Aut(L/Z(L)))<6·3^16. Automorphisms of perfect L inject into those of its simple central quotient, so the same outside-fiber bound applies. No simple-subgroup replacement of L is made.

Here are the complete comparisons; j includes identity. The five finite automorphism counts are calculated from all stored classes, with exact integer square maps and an independent agreement check against class orders.

| Row | Characteristic component or simple quotient | Kernel bound | j bound | Loop order lower bound | Mark upper bound |
| --- | --- | ---: | ---: | ---: | ---: |
| 22 | G2(3) | 2 | 10180 | 39312 | 20360 |
| 23 | Sp6(2) | 2 | 5104 | 161280 | 10208 |
| 24 | PΩ8⁻(3) | 2 | 6·3^16 | 1740735360 | 516560652 |
| 25 | Sp6(2) | 6 | 5104 | 725760 | 30624 |
| 26 | A9 | 6 | 2620 | 45360 | 15720 |
| 27 | Ω7(3) | 8 | 664120 | 14152320 | 5312960 |
| 28 | Ω8⁺(2) | 24 | 183376 | 6451200 | 4401024 |

The respective I0 order bounds from the actual table are116640,28431,37791360,240,3840,349920,767637. The full automorphism-table identifiers are `G2(3).2`, `S6(2)`, `A9.2`, `O7(3).2` and `O8+(2).3.2`; aliases are not silently substituted in the checks. Row24's value is a strict analytic upper bound. Each displayed capacity is smaller than its degree, so all seven rows are excluded under the stated inputs. a research reviewer developed the data and triality argument; the source authors supplied the actual-fiber and all-class coverage interfaces.

### Assembly, reproducibility and remaining scope

The source authors read both new certificates before running them with GAP4.15.1/CTblLib1.3.11. The PSU4(3) normalizer/centralizer checks passed. The orthogonal certificate passed every maximal-list check, all six triality tests, all five full automorphism counts and seven inequalities after two strict table-identifier aliases were corrected before freezing. Exact commands from the repository root are:

    gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_reversed_psu43_l34.g
    gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_reversed_finite_orthogonal.g

Source revision for both is `33c16afc7f8497586e24e0e8d5bde25ffc46c3ec`. Inputs, generator URL hashes, package versions, identifier checks and failure exits are committed. Raw logs are not Git inputs. The package's complete maximal lists, full automorphism identifications, stored class data and fusions remain cited assumptions; the runs do not reconstruct the underlying classifications or enumerate loop operations.

For the final table assembly, reversed rows1–5 are covered by the all-PSL2 full-socle exclusion at `47b07688a82d3df93f537946fe0780112200383b`; row9 has S=PSL5(2) and is covered by the all-prime-dimensional linear full-socle theorem at `c3f045c52e5e5dea344aba9823567834eb304218`; rows18–19 have PSU3(3), PSU3(5) and are covered by the odd-dimensional unitary full-socle theorem at `5e9382749b716b55e65928d781df40adc5f067a8`. The first finite-row continuation at `cc8c3324974c20359ea064cacf8b2750b5f293f3` covers rows6–8,10–11,16–17,21. The present arguments cover precisely the remaining rows12–15,20,22–28. Together with the earlier solvable-LMlt finite-table assembly at `3313726ad58aa11de1c79e04d4618f28380925fb`, both orientations of every Table1.2 row are now proposed excluded. Independent review of this exact assembly is pending. The nonclassical solvable-factor alternatives, factorizations with both factors nonsolvable, natural alternating/symmetric operation exhaustion, Bruck module parameters and unrestricted C0010 remain open.

### Independent review of both orientations of the finite classical table

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `97f9373535db767a158bbadc371737a23dc67677`, conditional on the stated canonical, earlier reviewed, Li–Xia, classical, ATLAS representation and CTblLib complete maximal/class/fusion inputs. Each checked rows12–15’s elementary centralizer-divisibility obstruction, faithful split extension, central radical and eliminated shear, and exact outer-label capacities. Each checked the two-class coverage and faithful normalizer in row20, all orthogonal maximal-order filters including row23’s perfectness and9/2 divisibility contradiction, row24’s retained quasisimple lift, and the separate triality noninvariance for all six row27 classes giving the bound8. Each checked the assembly of every Table1.2 row. Each extracted and read both exact committed certificates and independently ran them under GAP4.15.1/CTblLib1.3.11: both passed, including all six triality tests, five automorphism counts and seven capacity comparisons. reviewer A freshly inspected the ATLAS U4(3) representation page and opened Li–Xia v3; the other reviewers retained the recorded primary inspections. None reconstructed the external classifications or promoted a computation alone to a theorem. This completes the conditional two-orientation table deduction, not the remaining nonclassical alternatives or unrestricted C0010.

## Proposed complete reversed sporadic solvable-factor exclusion

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent exact-source reviews below.** Retain the actual canonical G=LMlt(Q), full group M=Mlt(Q), solvable point stabilizer I, and the canonical and primitive almost-simple inputs. Suppose the actual nontrivial factorization M=GI has sporadic socle. Li–Xia arXiv:1408.0350v3 Proposition4.4 and Table4.3, printed p.30, list all such factorizations with the solvable factor first. Here that factor is I; the listed nonsolvable factor is the actual G, not merely a maximal overgroup. The source authors freshly inspected the entire proposition and table. The source classification and its Magma computations remain external inputs.

First, if G=Aut(T) for a nonabelian simple T, every automorphism of G is inner. Indeed T is its unique minimal normal subgroup, hence characteristic, and C_G(T)=1. Restriction Aut(G)→Aut(T) is injective: an automorphism trivial on T sends each g to an element inducing the same conjugation on T, so fixes g. Its image already contains all Aut(T), through inner automorphisms of G. Thus every canonical inversion is inner. The component conclusion of the reviewed inner-inversion theorem at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`, namely F*(G)=O2(G), excludes this case. The same argument applies when G=T has trivial outer automorphism group. It is an argument about the actual canonical group, without a quotient-folder assertion.

Proposition4.4(a),(b) have G=M11 or M23. Both have trivial outer automorphism group, as the directly inspected ATLAS primary headers state, so the preceding observation excludes them regardless of the particular solvable transitive I.

For Table4.3, all thirteen rows are covered as follows:

| Rows | Actual canonical G | Deduction |
| --- | --- | --- |
| 1–4 | M10, PSL2(11), PGL2(11) | The reviewed all-almost-simple PSL2 canonical theorem at `47b07688a82d3df93f537946fe0780112200383b` applies, including M10 with socle A6=PSL2(9). |
| 5, and the linear alternative of7 | PSL3(4):2 | The reviewed odd-dimensional almost-simple PSL theorem at `114ce1b011fd47589eb762ed7cd5492a190002d8` applies. |
| 6 | M22 | The source has I=C23, and |M23|/23=443520=|M22|. The actual G action is regular, so the loop is associative. |
| 7, Mathieu alternative | M22 | Degree40320 exceeds the full automorphism mark count2872 below. |
| 7, affine alternative | 2⁴:A7 | Its radical is2⁴ and simple quotient A7. The reviewed radical lemma gives capacity16·j(S7)=16·232=3712<40320. |
| 8 | G2(2)≅PSU3(3):2 | The reviewed odd-dimensional almost-simple unitary theorem at `114ce1b011fd47589eb762ed7cd5492a190002d8` applies. |
| 9, and the simple alternative of10 | M22 | Degrees22176 and at least22176 exceed2872. |
| 10–11, full-automorphism alternative | M22.2=Aut(M22) | Every canonical inversion is inner, excluded by the component theorem above. |
| 12 | Sp4(4).4=Aut(Sp4(4)) | The same full-automorphism argument applies. |
| 13 | G2(4).2=Aut(G2(4)) | The same full-automorphism argument applies. |

The full automorphism identifications in the last two rows retain the classical symplectic outer-group source and the ATLAS G2(4) identification. In particular the order-four graph-field outer quotient of Sp4(4) is included, not replaced by its field subgroup. The source authors inspected the primary Sp4(4) and G2(4) pages. The small G2(2) identification and the almost-simple nature of the table's extensions remain the explicitly cited standard subgroup identifications of the source and earlier reviewed unitary interface.

For the only new finite count, [verify_reversed_sporadic_marks.g](../code/verify_reversed_sporadic_marks.g) pins GAP4.15.1/CTblLib1.3.11, the exact identifier `M22.2`, order887040 and the table construction description `Aut(M22)`. It totals every class with square equal to identity and separately checks class orders, centralizers and class sizes, giving

    j(Aut(M22))=2872.

The original outside-coset map E=G⋊⟨τhat⟩→Aut(M22) has kernel one on G=M22; it therefore bounds the actual marked set by2872 even if the whole formal extension has a larger kernel. Table4.3 row7 has |M|=10200960 and |I|=253, giving degree40320. Row9 has |M|=44352000 and |I|=2000, giving22176. Row10 has |M|=88704000 and |I|=4000, again22176. The verifier checks these arithmetic comparisons. No separate assertion that a projected marked set is a loop is used.

The source authors read and ran the certificate successfully with the stated pinned toolchain. Run from the repository root:

    gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_reversed_sporadic_marks.g

The certificate source is frozen at `b6b51197474139989786661ccc909964aef8b0b6`. The exact character table, its full automorphism identification and source classification remain external inputs, not reconstructed by the finite run. The certificate does not enumerate loop operations. Contributor a research reviewer developed this row-by-row reduction and count. This completes the proposed reversed sporadic factorization list; the opposite solvable-LMlt orientation has the earlier scoped review at `4e1449bce6a7c14f4b329aad8c4c01e65f10d650`. The remaining alternating case and factorizations with both factors nonsolvable, as well as unrestricted C0010, stay open.

### Independent review of the reversed sporadic list

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `fb4bb71c96277e01b50bc291f1251627a55dd949`, conditional on the cited canonical/inner-inversion, earlier almost-simple, Li–Xia, ATLAS and CTblLib inputs. Each checked all actual factor roles, the characteristic-socle proof that full automorphism groups have only inner automorphisms, the regular and affine cases, and the original M22 outside-fiber count without an extra factor two. Each read the frozen certificate and independently ran it with GAP4.15.1/CTblLib1.3.11, obtaining2872 and all required comparisons. reviewer A freshly inspected Li–Xia Proposition4.4 and every Table4.3 row, and the primary M22 and Sp4(4) identifications; the other two retained the recorded primary inspections. External classification and character-table completeness remain inputs. The reversed sporadic list is thereby conditionally closed; neither the alternating continuation nor unrestricted C0010 is certified by this review.

## Proposed complete reversed alternating solvable-factor exclusion

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `030ebb1d681efd8b12139efc7d0e3d4bdc9173ce` as recorded below.** Let Q be a finite simple proper left Bol loop with the retained faithful canonical and primitive almost-simple full-multiplication inputs. Write G=LMlt(Q), M=Mlt(Q), I=M₁, H=G∩I, and suppose I is solvable and the actual nontrivial factorization M=GI has alternating socle A_n. We exclude every alternative of Li–Xia arXiv:1408.0350v3 Proposition4.3 and Table4.2, printed pp.28–29. The source authors freshly inspected the entire list. Its natural n-point representation locates the abstract factors inside S_n; we do not identify it with the actual loop action M on Q. The cases n=5,6 are already covered by the reviewed all-PSL2 full-socle theorem at `47b07688a82d3df93f537946fe0780112200383b`; hence take n≥7 when using the natural A_n≤M≤S_n description.

The general alternating conclusion in C0007 Theorem3.1 has no recorded independent review covering its entire proof. Its aggregate is not promoted or imported here. We instead prove the narrower solvable-H lemma needed for Proposition4.3(a), using only the scoped canonical interfaces, a stated published order bound and the short calculation below. The new proof and its review do not certify the old theorem for arbitrary H.

### A scoped canonical alternating lemma with solvable H

Suppose G=A_m or S_m and H is solvable. For m=5,6, the reviewed almost-simple PSL2 theorem covers A5,S5,A6,S6. Let m≥7. Canonical inversion is induced by an involution t∈S_m, because Aut(A_m)=Aut(S_m)=S_m in this range and both groups are centerless. Restriction of the formal outside coset to automorphisms is injective on that coset. Thus the actual marks Λ=tK form a conjugacy-invariant union of involution classes, with

    |Λ| |H|=|G|,       H∩Λ²={1}.

Write C_k for cycle type2^k1^(m−2k), including C_0={1}, so |C_k|=m!/[2^k k!(m−2k)!]. None of the nonidentity classes splits in A_m: a constituent transposition is an odd centralizing permutation. Therefore Λ=∪_(k∈J)C_k with pure parity for A_m. For S_m, generation by K forces mixed parity. Including both possibilities below only enlarges the arithmetic screen; S_m could also be excluded directly by the inner-inversion component theorem. We have |Λ|>2 and |H|>1, since a loop of order at most two, or one with regular left multiplication group, is associative.

Here is the elementary class-square input, proved locally. For 1≤r≤min(k,⌊m/4⌋), C_(2r)⊂C_k². If 2r≤k, on each of r disjoint four-point sets take the two different fixed-point-free involutions whose product is the third; add k−2r common disjoint transpositions to both factors. Each factor has k transpositions, the product has2r, and2k≤m supplies the points. If r≤k<2r, use2r−k disjoint four-point sets on which the two factors have disjoint single transpositions, and k−r four-point sets with the preceding Klein-four products. There are4r≤m points and each factor again has k transpositions. Conjugating gives the entire class. Thus whenever max J≥⌊m/4⌋, every nonidentity involution of A_m lies in Λ² and H∩A_m has odd order. Separately C_1² contains all double transpositions and all three-cycles, by disjoint or overlapping transpositions respectively.

Dixon, *The Fitting subgroup of a linear solvable group*, J. Austral. Math. Soc.7 (1967), Theorem3, printed p.418, gives

    |H|≤24^((m−1)/3)

for every solvable H≤S_m. The source authors and contributor inspected that primary statement; its proof remains a cited input. Put j_m=|{s∈S_m:s²=1}|, with j_0=j_1=1 and j_m=j_(m−1)+(m−1)j_(m−2). For m≥26,

    m!/(2j_m)>24^((m−1)/3).

To verify the infinite range rather than extrapolate a finite experiment, set r_m=j_m/j_(m−1). The exact base at m=16 satisfies4≤r_16≤19/4. Inductively r_(m+1)=1+m/r_m lies between4 and(m+4)/4 for m≥16. Hence (m!/j_m)/((m−1)!/j_(m−1))≥4m/(m+3). This is increasing and exceeds the cube root of24 at m=26. The certificate checks the exact cubed base

    26!³ > 8·24^25·j_26³,
    j_26=532985208200576,

and (4·26)³>24·29³. Induction proves the displayed inequality for every m≥26, contradicting |Λ||H|=|G| for either group.

For7≤m≤25, [verify_alternating_solvable_stabilizer.py](../code/verify_alternating_solvable_stabilizer.py) enumerates every nonempty parity-permitted set J, exact divisibility of |G| by |Λ|, the integer form |H|³≤24^(m−1), and the necessary oddness condition above. For S_m its filter allows either possible index of H∩A_m; it does not assume equality with |H|/2. Exactly two arithmetic possibilities survive:

    (m,G,J,|H|)=(8,A8,{1},720), (8,A8,{1,3},45).

If |H|=720, a Sylow2-subgroup P of H has order16. Since H contains no double transposition, every involution of P is a fixed-point-free product of four transpositions on eight points. Any nontrivial point stabilizer in a2-group contains an involution, so P acts semiregularly, impossible when16 does not divide8. If |H|=45, Sylow's theorem forces a normal Sylow5-subgroup C5. Its generator is a five-cycle, and N_A8(C5) has order60: in S8 its normalizer is (C5:4)×S3 of order120, with both parities present. Lagrange forbids H≤N_A8(C5) because45 does not divide60. Thus neither survivor is possible. This proves the scoped solvable-H lemma without the unreviewed general C0007 theorem.

### The one-point and two-point alternatives

In Proposition4.3(a), the actual G lies between A_(n−1) and S_(n−1), hence is one of those groups. Its actual H=G∩I is solvable. The scoped lemma excludes it, including n=7 by the separately reviewed PSL2 boundary.

In part(b), n=p^f and the actual G contains T=A_(n−2) in S_(n−2)×S2, while I is one of the source's solvable2-homogeneous groups. Put m=n−2. For n≥9, T is simple, T=G^(∞) is characteristic, and |C_G(T)|≤2. The original outside-fiber lemma therefore gives |Λ|≤2j_m for every possible intermediate G; no universal canonical A_m exclusion is needed. Inspection of the exact source list gives

    |I|≤2n(n−1)f.

For the semilinear alternative this follows already from |AΓL1(n)|=n(n−1)f. The exceptional degrees25,49,81,121,529 have maximum displayed orders respectively25·24·4,49·24·6,81·32·20,121·24·10,529·24·22; the certificate checks each against the displayed bound. Consequently |Q|=[M:I]≥(n−2)!/(4f).

For completeness the comparison is uniform. The recurrence gives j_d≤d j_(d−1), hence j_d≥2j_(d−1) for d≥3 and j_(d+1)≤(1+d/2)j_d. Put R_n=(n−2)!/(4j_(n−2)). Then R_(n+1)/R_n≥2(n−1)/n>(n+1)/n for n≥5. The exact R_10>10 yields R_n>n≥2f for n≥10, because p^f≥2f. At n=9, f=2 and7!=5040>8·2·j_7=3712. These contradict the capacity bound for every n≥9. At n=7 the nonexceptional bound |I|≤42 gives |Q|≥60>2j_5=52, with Aut(A5)=S5.

At n=8 the source has I≤AΓL1(8), whose natural permutations are all even: translations are four transpositions, nontrivial multipliers are seven-cycles, and Frobenius is two three-cycles. Since the socle is transitive in the actual loop action, A8I=M, so M=A8. Therefore

    A6≤G≤(S6×S2)∩A8≅S6,

and G is A6 or S6. The reviewed all-almost-simple PSL2 theorem excludes both. No assumption that every abstract automorphism of A6 comes from S6 is made.

### The three-point and finite alternatives

In part(c), n=8 or32, G contains T=A_(n−3) in S_(n−3)×S3 and T=G^(∞) is characteristic. At n=8 the same parity argument for the listed I=AGL1(8) or AΓL1(8) forces M=A8, giving |C_G(T)|≤|A3|=3. Thus |Λ|≤3j_5=78, whereas |Q|≥20160/168=120. At n=32 the coarser |C_G(T)|≤6 suffices, and |I|=32·31·5=4960. The certificate uses the involution recurrence to check the exact comparison

    6j_29 < 32!/(2·4960) ≤ |Q|.

Parts(d),(e) and Table4.2 rows1–4 have actual G=PSL2(5) or PGL2(5), excluded by the reviewed canonical PSL2 theorem. In rows5–6, G=AGL3(2). Its characteristic U=O2(G)=2³ has centralizer C_G(U)=U, and the formal inversion extension acts on U through GL3(2). Each original outside fiber has at most eight elements. Every nonidentity involution of GL3(2) is I+vφ with v≠0 and0≠φ annihilating v; there are7·3=21 such maps. Thus |Λ|≤8·22=176. The source's actual solvable factors have order at most60 in M=A8 and at most120 in M=S8, respectively. Both actual degrees are at least336, a contradiction. This uses no affine realization of τ or cohomology assertion.

### Source, evidence and exact remaining boundary

The source authors read and ran the Python certificate with Python3.12.14 and assertions enabled; it passed the degree7–25 screen, the two retained degree-eight cases, all recurrence bases, exceptional-factor orders and degree32 comparison. It uses only integer arithmetic and the standard library. Run from the repository root:

    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_alternating_solvable_stabilizer.py

Its exact source revision is `c8062233517c1426cf97c0971b056ca98567b689`. The proof of the necessary class-square conditions, both degree-eight eliminations and the infinite inductions is supplied above; computation alone is not the exclusion. Li–Xia's factor classification, Dixon's published theorem and the explicitly retained earlier canonical results remain inputs. a research reviewer developed the factor-case assembly and a research reviewer developed the scoped solvable-H screen and exact arithmetic; their development checks are distinct from independent review of this source.

This completes the conditional reversed Proposition4.3/Table4.2 exclusion. Together with the reviewed classical and sporadic tables, the earlier solvable-LMlt theorem at `7f456116c2e6ca420c7c15c789c96ee105050c1b` (whose natural A_N/S_N full actions, N≥24, have nonsolvable point stabilizers), and Li–Xia Proposition4.2 ruling out exceptional socles with a solvable proper factor, it proves the following necessary reduction under the stated inputs: if the actual I is solvable, then the canonical G must contain Soc(M). This conclusion uses the nontrivial-factorization hypothesis correctly; it does not exclude the case G≥Soc(M), where Li–Xia's list of proper factors does not apply. The nonsolvable-factor, natural-operation and Bruck-parameter obligations remain open, and C0010 is not resolved.

### Independent review of the reversed alternating exclusion and reduction

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `030ebb1d681efd8b12139efc7d0e3d4bdc9173ce`, conditional on the cited Li–Xia, Dixon, canonical and earlier reviewed inputs. Each checked the class-square constructions, parity restrictions, infinite recurrence argument, both A8 survivors, all actual factor roles in Proposition4.3/Table4.2, the n=8 exceptional-automorphism boundary, the original AGL3(2) fiber count and the final necessary reduction. Each read and extracted the committed Python certificate and independently ran it successfully; the first two used Python3.12.14, while reviewer C used its available `python3` without claiming that exact version. reviewer A freshly read all of Li–Xia Proposition4.3/Table4.2 and Dixon Theorem3, p.418, with its constant on p.417. The other reviewers retained the documented primary inspections. An initial parity concern from reviewer A was explicitly retracted: 1∈K supplies t∈Λ, and an odd element of generating K supplies a mark of the opposite parity. The cited classifications and Dixon theorem remain inputs, not newly certified external proofs. These are scoped independent agent reviews, not formal GitHub approvals; they neither review aggregate C0007 nor exclude the remaining socle-containing case.

## Proposed exclusion of sporadic full socles with solvable stabilizer

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `6e016e1f1237545146e30786902ef92486c1524c` as recorded below.** Under the retained canonical and primitive almost-simple full-multiplication inputs, no finite simple proper Bol loop has both a sporadic full multiplication socle S and solvable full point stabilizer I. This statement uses the necessary reduction reviewed at `030ebb1d681efd8b12139efc7d0e3d4bdc9173ce`: the actual canonical G contains S. The calculation below concerns actual maximal I in M, not arbitrary solvable subgroups of S.

### Almost-simple automorphisms and original outer marks

We first record an elementary general observation. If S≤G≤Aut(S) with S nonabelian simple, then S is characteristic in G and C_G(S)=1. Restriction Aut(G)→Aut(S) is injective: if α fixes S pointwise, g and α(g) induce the same conjugation on S, so α(g)g⁻¹ centralizes S and is trivial. If |Out(S)| is odd, the restriction of an involutory τ has trivial image in Out(S), so is conjugation by some s∈S. Injectivity gives τ=Inn(s) on G. The reviewed inner-inversion theorem at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8` forbids this, since G has a nontrivial component S but that theorem forces F*(G)=O2(G). Thus every almost-simple canonical group with odd-order outer group of its socle is excluded, without a solvability assumption on its stabilizer. Likewise G=Aut(S) is always excluded: its inner automorphisms already fill the target of that same injective restriction, so all its automorphisms are inner.

For the sporadic groups, the ATLAS/library outer-group inventory has fourteen trivial outer groups and twelve of order two. The former are excluded immediately. For the latter, G is S or Aut(S), and only G=S with outer τ remains. The original formal outside coset embeds as the outside coset of A=Aut(S), since S is centerless. Its selected nonempty mark set Λ is an S-invariant union of outer involution classes and has size |Q|. An outer involution t has an outer element in C_A(t), namely itself, so its A-class is one S-class: C_A(t)S=A. Consequently

    |Q| is a nonempty subset sum of the sizes of the outer involution classes of A.

There is no identity class in this outside coset, and no extra factor two. On the full-action side M is S or A and I is a solvable maximal subgroup because the action is faithful and primitive. Therefore |Q|=[M:I] must also be an actual solvable-maximal-subgroup index in one of these two groups.

### Complete finite screen and source interface

The [pinned certificate](../code/verify_sporadic_outer_solvable_max.g) reads all twenty-six sporadic `ExtensionInfoCharacterTable` records, all twelve stored S→Aut(S) fusions, and every entry of the complete `Maxes` lists of the twenty-four S and S.2 groups. It tests solvability of each maximal subgroup's ordinary character table. The table below gives the complete union of distinct solvable-maximal indices over both possible M; repeated classes or equal indices are combined only for this displayed arithmetic comparison. The certificate retains every actual list entry.

| S | Outer involution class sizes | Solvable-maximal indices in S or S.2 |
| --- | --- | --- |
| M12 | 792 | 220,495,880,1320 |
| M22 | 330,1386 | none |
| J2 | 1800 | 525,2016 |
| J3 | 20520 | 25840,43605,293760 |
| HS | 1100,23100 | 22176 |
| McL | 113400 | 299376,779625 |
| He | 266560 | 437325,652800,3358656 |
| Suz | 370656,2358720 | 3203200 |
| O'N | 2624832 | 17778376,55978560,991001088 |
| HN | 75240000 | 136515456,2926000000 |
| Fi22 | 61776,19459440,22239360 | 12812800 |
| Fi24′ | 306936,5686767482760 | 101652551764711833600,3091639677809511628800 |

No entry in the last column is a nonempty subset sum from the middle column. The certificate asserts each class-size list, forms every subset sum using exact integers, and verifies the inequality for every solvable maximal entry. This rules out all twelve cases. In particular the argument uses exact class unions where a bound by the total number of outside involutions would fail, rather than discarding those smaller indices. It does not infer an upper bound on arbitrary solvable subgroups from a partial subgroup search.

The source interface is explicit. CTblLib manual §3.7-1 states that a stored `Maxes` list has one representative of every maximal-subgroup conjugacy class; §3.7-3 identifies its multiplier/outer-group metadata and full-automorphism table names. GAP reference §71.8-5 states that `IsSolvable` on an ordinary character table is solvability of the represented group. The source authors directly inspected those primary documentation sections and GAP4.15.1 `lib/ctbl.gi`: the solvability method uses normal-subgroup classes and chief-factor prime-power orders. The correctness of those stored character tables, fusions, complete maximal classifications and outer-group inventory remains external ATLAS/library input. Internal consistency and arithmetic checks do not reprove that classification. The source asserts GAP4.15.1/CTblLib1.3.11; current online overview pages labeled1.3.10 are not substituted for this executable dataset.

The source authors read and ran the certificate with the asserted toolchain, including all outer-group inventory, fusion/order, power-map, class-size, maximal-table and subset-sum checks. Run:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sporadic_outer_solvable_max.g

Its frozen source is `02f902e1691381bba49e59004a988b1abbe69f3a`, unchanged at `1b4ef1d31815938cc0b69eb30411734d5ab4ce61`. Contributor a research reviewer developed the finite screen; the source authors strengthened the source checks and supplied the exact outside-class comparison. Development is not independent review. The conditional conclusion excludes sporadic full socles only when I is solvable; nonsolvable-I sporadic operations and unrestricted C0010 remain open.

## Proposed complete canonical G2(4) exclusion

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `6e016e1f1237545146e30786902ef92486c1524c` as recorded below.** Suppose the entire canonical left multiplication group of a finite simple proper Bol loop satisfies S=G2(4)≤G≤Aut(S). This is impossible under the retained canonical/inner-inversion interfaces and the finite source inputs below. Neither solvability of H nor any hypothesis about the full multiplication group is required.

The primary ATLAS G2(4) header gives |S|=251596800 and |Out(S)|=2. The preceding restriction argument excludes G=Aut(S) and inner inversion for G=S. For G=S and outer inversion, the stored S→Aut(S) fusion and involution classes give exactly one outside involution class, of size20800. It is one S-class by the outside-centralizer argument above. Hence the nonempty actual selected Λ is this entire class, and |H|=|S|/20800=12096. For any t∈Λ, |C_S(t)|=12096.

Every subgroup of S of order12096 is conjugate to every other such subgroup. Indeed the complete maximal list has orders

    604800,184320,184320,124800,120960,12096,3600,1092,

with exactly one conjugacy class of order12096. The only maximal overgroups with order divisible by12096 are J2, 3.L3(4).2_3 and U3(3).2. The complete maximal list of J2 has largest order6048, so J2 contains no proper subgroup of order12096. In B=3.L3(4).2_3, let D=3.L3(4)◁B have index two and central quotient L3(4). If H≤B has order12096, then [B:H]=10 and [D:H∩D]≤10. The image of H∩D in L3(4) also has index at most ten. The complete maximal list of L3(4) gives least proper index21, so this image must be all of L3(4). But then |H∩D|≥20160>|H|, a contradiction. This argument does not require a separate perfect-cover exclusion or an assumed embedding from order alone: the central-cover structure is part of the cited actual maximal-group identification. The remaining overgroup U3(3).2 has the same order as H, so H equals it up to conjugation.

Apply the same argument to C_S(t), which has that order. Thus H=C_S(t′) for some conjugate t′ of t. By Cauchy's theorem choose a nonidentity involution x∈H. It commutes with t′, so t′x is also an outside involution and belongs to the unique class Λ. Both t′ and t′x are selected marks, while their product x belongs to H. This contradicts H∩Λ²={1}.

The source authors freshly inspected the primary ATLAS G2(4) group data and the complete online CTblLib lists for G2(4), J2 and L3(4), recording their identifications and all maximal entries. The [certificate](../code/verify_g24_outer_stabilizer.g), corrected and frozen at `1b4ef1d31815938cc0b69eb30411734d5ab4ce61`, reads all those actual lists, the unique outer class, its original centralizer, the central cover and its normal fusion; it does not replace them with a hard-coded partial subgroup list. An initial table-object equality dispatch failed and was repaired additively before this successful source run. The source authors read and ran the corrected certificate with GAP4.15.1/CTblLib1.3.11:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_g24_outer_stabilizer.g

All assertions passed. Correctness/completeness of the ATLAS/library classifications and table data remains external input; the new subgroup-order and selected-mark collision argument needs independent exact-source review. a research reviewer developed the subgroup restriction; the source authors supplied the centralizer collision and simplified the central-cover step. This excludes G2(4) only as the socle of the entire almost-simple canonical group, not its occurrence as a section or component of an arbitrary larger envelope. The overall classification remains open.

### Independent review of the sporadic and G2(4) deductions

automated-model reviewer A, reviewer B and reviewer C independently accepted both preceding deductions at exact source `6e016e1f1237545146e30786902ef92486c1524c`, with their different scopes retained. Each checked the characteristic-socle restriction, odd-outer-group argument, outside-class non-splitting and subset-sum condition against actual maximal full stabilizers. Each separately checked the G2(4) unique-class argument, all eligible maximal overgroups, the central-cover order contradiction and the collision inside the actual selected mark set. All three read, extracted and independently ran both exact committed GAP certificates with `--quitonbreak`, GAP4.15.1/CTblLib1.3.11, obtaining exit0 and every stated inventory, maximal-list, fusion, class, cover and arithmetic check. reviewer A freshly inspected the primary ATLAS G2(4) data and maximal shapes and the CTblLib `Maxes` documentation; the other two retained the source authors's recorded primary inspections. The external classifications, table correctness/completeness and earlier canonical results remain inputs. These reviews exclude neither sporadic full socles with nonsolvable I nor G2(4) sections in arbitrary larger envelopes, and do not certify unrestricted C0010 or constitute formal GitHub approval.

## Proposed uniform PSL4 small-stabilizer exclusion

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `1ebb2cb522d732f6116b0d205450f94f802d33d6` as recorded below.** Let Q be a finite simple proper Bol loop with entire canonical G satisfying S=PSL4(q)≤G≤Aut(S), q≥7, and actual stabilizer H. Put d=gcd(4,q−1). The explicit hypothesis

    |H∩S|≤24(q−1)³/d

is impossible under the retained canonical inversion and classical-group inputs. In particular this excludes stabilizer intersections contained in the monomial subgroup of that order. This is a conditional order-bound theorem, not an assertion that a table of solvable maximal stabilizers has been completely verified or that it exhausts arbitrary H. No full-multiplication action hypothesis is needed.

Because S is characteristic in G and C_G(S)=1, conjugation of the formal inversion extension on S is injective on its single outside coset. The actual selected marks Λ therefore inject into the elements of order at most two in Aut(S). Denote their number by j(Aut(S)). Independently,

    |Q|=[G:H]≥[S:H∩S]
       ≥q⁶(q²−1)(q³−1)(q⁴−1)/[24(q−1)³]>q¹²/24.

The last strict inequality follows by dividing each q^i−1 by q−1 for i=2,3,4. We prove j(Aut(S))<8q⁹. Since q³≥343>192, these bounds contradict |Q|=|Λ|.

### All four possible automorphism labels

The classical automorphism theorem identifies Aut(S) with PΓL4(q) extended by inverse-transpose γ; the relevant §2.1 definitions and Theorem2.1.4 of Kleidman–Liebeck1990 are cited in REFERENCES.md. Write q=p^f. The quotient by PGL4(q) is C_f×C2, so an element of order at most two has only the labels 1, γ, and, when f is even, σ or γσ, where σ is the field involution. There is no factor f in the count. All diagonal automorphisms are retained in PGL4(q).

For the identity label, [A]²=1 means A²=λI. In odd characteristic there are two scalar-square classes to consider. If λ is square, normalize to A²=I. Modulo changing A to −A, only minus-eigenspace dimensions zero, one and two are needed. The corresponding GL conjugacy-class sizes give the following upper bounds on projective possibilities:

    1, q³(q³+q²+q+1), q⁴(q²+1)(q²+q+1).

The middle two arise from |GL4(q)|/(|GLk(q)||GL_(4−k)(q)|), k=1,2. Projective centralizers can only reduce them; we do not assert equality for the equal-eigenspace case. If λ is nonsquare, scale it to one fixed nonsquare. Every such A has the same irreducible quadratic minimal polynomial, with centralizer GL2(q²), giving an upper bound

    |GL4(q)|/|GL2(q²)|=q⁴(q−1)(q³−1).

This covers every nonsquare λ because their ratios are squares. It does not normalize a nonsquare λ to1. In even characteristic every scalar is a square. After normalization A=I+N with N²=0, and nonzero N has rank one or two. Counting its image, kernel and induced isomorphism gives respectively

    (q⁴−1)(q³−1)/(q−1), q(q⁴−1)(q³−1).

For rank one, choose v≠0 and a nonzero functional vanishing on v, then divide by q−1. For rank two, choose its common image/kernel of dimension two and an isomorphism from the quotient to it. Add the identity. All the displayed odd- or even-characteristic sums are less than4q⁸, hence less than4q⁹, for q≥7: the rank/eigenspace-one term is less than2q⁶, the split two-dimensional term less than2q⁸, and the nonsplit or rank-two term less than q⁸; 1+2q⁶<q⁸.

For the graph label, ([A]γ)²=1 implies A^T=±A. This follows by transposing A^T=cA again, so c²=1. In characteristic two there is only the symmetric possibility. Counting all symmetric and alternating matrices, even allowing singular ones as an upper bound, gives

    (q¹⁰+q⁶)/(q−1)<2q⁹.

We divide only the nonzero invertible representatives by q−1; including zero in the numerator merely enlarges the upper bound.

### Field and graph-field labels with their scalar normalization

Let q=s², so s≥3. For the pure-field label, ([A]σ)²=1 gives Aσ(A)=λI. Applying σ and conjugating this equation by A show λ∈Fs*. Surjectivity of the finite-field norm lets us rescale A so that Aσ(A)=I. The required matrix descent can be seen directly. Define the σ-semilinear involution T(v)=Aσ(v). Choose a∈Fq with a≠σ(a). For every v, both v+T(v) and av+σ(a)T(v) are fixed by T; their two coefficient rows have nonzero determinant. Thus the fixed vectors span the entire space over Fq. Choose an Fq-basis from them and place it in a matrix B. Then Aσ(B)=B, so A=Bσ(B)⁻¹. All pure-field involutions are therefore one PGL4(q)-class.

Its projective centralizer is PGL4(s). Indeed σ(B)=cB implies cσ(c)=1. The map b↦b/σ(b) on Fq* has kernel Fs* and image the norm-one subgroup, so scalar rescaling makes B an Fs-matrix. Conversely any such matrix is fixed. It follows that the number in this label is

    |PGL4(q)|/|PGL4(s)|<4q^(15/2)<q⁹.

The product formula gives |PGL4(q)|<q¹⁵ and |PGL4(s)|=s¹⁵∏_(i=2)^4(1−s^(−i))>s¹⁵/4. For example that product is at least1−∑_(i=2)^4s^(−i)>1−1/[s(s−1)]≥5/6. This label occurs only for square q≥9, so4<q^(3/2). Norm surjectivity and the norm-one scalar argument use only cyclicity of the multiplicative group of a finite field.

For the graph-field label, the involution equation becomes

    A=λσ(A)^T,       λσ(λ)=1.

The same norm-one scalar argument gives c with σ(c)/c=λ, so B=cA satisfies B=σ(B)^T. The Hermitian 4×4 matrices form an Fs-vector space of dimension16: four diagonal entries over Fs and six arbitrary upper-triangular entries over Fq. Two nonzero Hermitian matrices give the same projective matrix precisely when their scalar ratio lies in Fs*. Counting all of them, including singular possibilities, gives an upper bound strictly below

    s¹⁶/(s−1)≤2q⁸/s<q⁹.

Adding the four label bounds proves j(Aut(S))<8q⁹ and the claimed contradiction. The calculation uses exact formulas and inequalities for every q≥7, not an inference from finite samples.

### Evidence, source boundary and remaining gap

The source authors checked all scalar normalizations, matrix counts and inequalities and freshly inspected the publisher-preview image of Kleidman–Liebeck Theorem2.1.4, printed p.16, retaining the already inspected §2.1 linear definitions. Contributor a research reviewer developed the four-label count; a research reviewer supplied a preliminary independent development audit, distinct from exact-source review. The elementary field-descent argument above removes the need to import a separately unverified projective Hilbert90 claim. No new executable or numerical census is needed.

The indexed text of Hua Zhang's2011 thesis suggests that the q≥7 monomial row is the only infinite even-dimensional linear alternative with solvable primitive stabilizer. However direct PDF/page-image access and comparison with the published Li–Zhang table were unavailable in this investigation, and another finite row's text extraction has a missing-factor ambiguity. Therefore that suggested exhaustion is not part of this theorem. The explicit order hypothesis above is the endpoint that is actually proved, and q<7, larger intersections and the general classification remain open. Exact-source independent review of this deduction is pending.

### Independent review of the uniform PSL4 bound

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `1ebb2cb522d732f6116b0d205450f94f802d33d6`, conditional on the stated canonical and classical automorphism inputs. Each read the complete frozen proof and checked the original-coset injection, index bound, split/nonsplit projective scalar cases, characteristic-two ranks, graph matrix spaces, pure-field norm normalization, elementary fixed-basis descent and projective centralizer, Hermitian representative count and final strict inequalities. All three retained the source authors's recorded Kleidman–Liebeck primary inspection rather than claiming a fresh inspection. No computation or new executable was needed. Their acceptances concern exactly q≥7 and the stated bound on H∩S; they do not verify Zhang-table exhaustion, cover smaller fields or resolve C0010. These are independent mathematical agent reviews, not formal GitHub approvals.

## Proposed complete canonical PSL4(3) exclusion

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `1a513b45925c25232e0c9e39ada341e5e9f86625` as recorded below.** No finite simple proper Bol loop has entire canonical left multiplication group S=PSL4(3)≤G≤Aut(S), under the retained canonical/inner-inversion interfaces and the explicit finite inputs below. H is arbitrary; neither a solvable stabilizer nor a specified full multiplication group is assumed.

We use the local outer-class and captured-class arguments of [hs-psl4-odd.md](../primitive-completion/hs-psl4-odd.md), independently reviewed at `32b5918c4b3fa3b2686185006b80d41b1ece76aa`. Only its q=3 automorphism roster and its subsection “A common captured class” are used, not its HS-folder hypotheses. Put I for the S-conjugacy class of the split projective involution diag(−1,−1,1,1). The cited local proof shows I⊂C² for each nonsymplectic outer involution class C. Its explicit determinant-one witnesses cover the diagonal and both symmetric graph types. We retain those source hypotheses and the classical automorphism description: |S|=6065280 and Out(S)=C2×C2, with labels d, g, dg for diagonal, graph and their product.

The original outer involution S-classes have sizes

    d: 1080;       g: 117,117,10530;       dg: 8424.

The two size117 classes are symplectic graph classes. The [certificate](../code/verify_psl43_canonical.g) independently checks these sizes from all three stored S→S.2 fusions and checks their further fusions into Aut(S). The complete Aut(S) class sizes are1080,234,10530,8424: precisely the two117 classes fuse. These source identifications, their class/fusion correctness and maximal-list completeness are explicit ATLAS/CTblLib inputs.

### Every subgroup with order divisible by sixteen meets I

The same certificate constructs GAP's natural PSL(4,3) permutation group on forty projective points and a Sylow2-subgroup P of order128. It enumerates every P-conjugacy class of subgroups of order16. There are43, and the counts of their involutions moving exactly32 points are distributed as

    (number of such involutions, number of subgroup classes)
    (1,13), (3,12), (5,12), (7,4), (9,2).

In particular every one contains such an involution. To interpret it, a projective involution lifts to A with A²=±I. A nonsquare scalar gives no eigenline over F3. A nonidentity split involution in S has two plus and two minus eigenvalues: an odd negative multiplicity would give nonsquare determinant. It fixes exactly4+4=8 of the forty projective points and moves32. Thus the tested permutations are precisely I, not an arbitrary same-order class. Every order16 subgroup of S is conjugate into P. Every subgroup whose order is divisible by16 contains an order16 subgroup of its Sylow2-subgroup. The complete finite enumeration therefore proves that every such subgroup meets I, conditional on the verified group construction and subgroup-enumeration algorithm. It is not a sample of subgroups or of loop orders.

### The simple canonical group

First G=S. Inner inversion is excluded by the reviewed component theorem. The selected nonempty Λ is a union of the S-classes in exactly one outer coset. A diagonal-only selection gives |Λ|=1080 and |H|=5616; a diagonal-graph selection gives |Λ|=8424 and |H|=720. Each |H| is divisible by16, whereas I⊂Λ², contradicting H∩Λ²={1}.

For graph marks, exact subset-sum divisibility by |S| leaves only |Λ|=117,234,10530. The last gives |H|=576, and the same nonsymplectic class-square contradiction applies. If both symplectic classes are selected, |Λ|=234 and |H|=25920 is again divisible by16. Here the cross-product of the two classes contains I. Explicitly take J=diag(J2,J2), J2=[[0,1],[−1,0]], and D=diag(−I2,I2). Both J and JD are nonsingular alternating forms, their Pfaffians have opposite square classes, and D is a symplectic isometry with D²=1. For the convention

    α_B(y)=B⁻¹(y⁻¹)^T B,

the product α_J α_(JD) is conjugation by D, projectively. These are marks from the two distinct symplectic S-classes, so conjugating proves I⊂Λ². This also contradicts the order16 result.

It remains to exclude one selected symplectic class of size117, giving |H|=51840. The complete S-maximal list has exactly two entries with order divisible by51840; each has exactly that order. Hence every such H is in one of these two maximal conjugacy classes. We now identify both and produce a collision for either selected class, without assuming solvability of H.

View V=F9² as a four-dimensional F3-space, with i²=−1. For a∈F9* define the alternating form

    B_a(u,v)=Tr_(F9/F3)(a·det_(F9)(u,v)),

and let X multiply both F9 coordinates by i. Then X²=−I, det_(F3)(X)=Norm(i)²=1, and

    B_a(Xu,Xv)=−B_a(u,v),       B_a(u,Xv)=B_(ai)(u,v).

In particular X is a similitude of multiplier−1, not an isometry. Its nontrivial projective involution x centralizes each α_(B_a). For a=1 and1+i, in the ordered basis (1,i) on each coordinate, the Pfaffians of B_a and B_aX are respectively(1,1) and(2,2). The certificate checks these explicit F3 matrices, their determinants, the alternating identities and α_(B_a)α_(B_aX)=conjugation by X⁻¹ on SL4 generators. Thus the same x belongs to the square of each of the two symplectic S-classes, and centralizes both chosen graph involutions.

For clarity, these Pfaffians distinguish exactly the two S-classes. Alternating forms are GL-congruent; a congruence multiplies the Pfaffian by its determinant. Equal Pfaffians therefore permit an SL-congruence, while projective scalar changes multiply a four-dimensional Pfaffian by a square, which is1 over F3. The two values1 and2 are distinct. Their centralizers H_1,H_2 in S each have order51840 by the class sizes. They are not S-conjugate. Indeed C_S(H_a)=1: H_a contains every symplectic transvection for B_a. If a projective matrix commutes with such a transvection, its lift commutes with it exactly, because a nontrivial scalar multiple would change the eigenvalue1. It consequently preserves the image line of each transvection minus identity. These include every line, so the lift is scalar. If H_1 and H_2 were conjugate, aligning them would make the product of the two corresponding graph involutions an element of C_S(H_1); both graph involutions have the same S-outer label, so their product lies in S. It would be trivial, contradicting their distinct S-classes. Hence H_1,H_2 represent the two maximal classes above.

After conjugating H, it is H_1 or H_2. The explicit x lies in both H_1,H_2 and in the square of either possible selected class Λ. Conjugation preserves that class, so in every case H∩Λ² contains a nonidentity element. This finishes G=S.

### All three index-two canonical groups

Let [G:S]=2. Restriction Aut(G)→Aut(S) is injective as before, and inner τ is forbidden. Consequently the formal extension E=G⋊⟨t⟩ embeds in Aut(S): a kernel element in its outside coset would make τ inner on G by restriction injectivity. By orders its image is all of Aut(S). The selected Λ is invariant under E, not just G. To see the extra invariance without any new quotient assumption, write λ=tk with k∈K; then tλt=kλk⁻¹∈Λ by G-conjugacy invariance.

The outside coset of G in Aut(S) has two S-outer labels. Both must occur among selected marks. Indeed t∈Λ because1∈K; if every mark had the same S-outer label as t, then K=tΛ would lie in S and could not generate G. Using the full Aut(S) classes, the possible sums are therefore

| G/S label | Possible mark cardinalities |
| --- | --- |
| d | 8658,18954,19188 |
| g | 9504 |
| dg | 1314,11610,11844 |

The certificate checks that only18954 divides |G|=12130560. It selects the two nonsymplectic classes of sizes10530 and8424 and gives |H|=640. Since [G:S]=2, |H∩S| is640 or320; both are divisible by16. No surjectivity of H onto G/S is needed. The order16 result forces H∩S to meet I, while the selected nonsymplectic classes have I in their squares. This is again impossible. Finally G=Aut(S) has only inner automorphisms by the characteristic-socle restriction argument and is already excluded by the inner-inversion theorem.

### Exact evidence and scope

The source authors read and ran the complete certificate, frozen at `9859cab42ef435ab57f5c6d423c2f32448de6f1c`, with GAP4.15.1/CTblLib1.3.11:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_psl43_canonical.g

All assertions passed. The source contains the exact matrices and checks their graph-product convention, all43 subgroup classes, all class sums and the sole intermediate-group survivor. It checks the normal class fusions, orders, class sizes and every stored maximal entry. The source authors freshly inspected the complete primary CTblLib online S-maximal list; its online1.3.10 metadata is distinguished from the executable1.3.11 data. The GAP natural projective constructor and exact subgroup enumeration are computational inputs, and the stored class and maximal classifications remain external inputs. The local interpretation of their outputs and the centralizer collision are supplied above. a research reviewer developed the finite subgroup/form certificates; the source authors supplied the F9 common-collision route and intermediate-group generation argument. This is development, not independent review. The result concerns the entire almost-simple canonical group and does not exclude PSL4(3) sections in larger envelopes or resolve C0010.

## Proposed PSL4(5) small-stabilizer boundary

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `1a513b45925c25232e0c9e39ada341e5e9f86625` as recorded below.** If S=PSL4(5)≤G≤Aut(S) is the entire canonical group, the explicit hypothesis |H∩S|≤1536 is impossible. This extends the small-stabilizer method to one finite boundary with a larger stated bound, without importing an unverified table of stabilizers.

There are no field labels at q=5. Specializing the split/nonsplit projective formulas derived in the reviewed q≥7 argument gives the identity-label upper bound

    1+19500+503750+310000=833251.

There are at most ((5¹⁰−1)+(5⁶−1))/(5−1)=2445312 graph-label projective matrices: count all nonzero symmetric and alternating matrices before projectivizing, allowing singular matrices only to enlarge the count. Therefore

    j(Aut(S))≤3278563.

The original marked-coset injection still applies, whereas |S|=7254000000 gives

    |Q|≥|S|/1536=18890625/4>3278563,

as4·3278563=13114252<18890625. This contradiction is exact rational arithmetic, not a group census. Contributor a research reviewer developed the specialization; the source authors checked the formulas and inequalities. The canonical and classical automorphism inputs are the same as in the reviewed uniform argument at `1ebb2cb522d732f6116b0d205450f94f802d33d6`; its formulas are derived for odd fields before imposing its q≥7 estimate. The independent review of this new boundary is pending. Neither the actual solvable-stabilizer-table scope nor cases with larger H∩S are asserted here.

### Independent review of the PSL4 small-field deductions

automated-model reviewer A, reviewer B and reviewer C independently accepted both preceding deductions at exact source `1a513b45925c25232e0c9e39ada341e5e9f86625`, retaining their different hypotheses. Each checked the complete Sylow2 subgroup coverage and the identification of the moved-point class, the inherited nonsymplectic captured-class argument, both explicit alternating-form products, the F9 common collision for both centralizers and either selected class, and the centralizer nonconjugacy proof. Each also checked actual E-invariance, generation and all intermediate-group sums, including the sole18954 survivor and both possible orders of H∩S. All three read, extracted and independently ran the exact committed GAP certificate with `--quitonbreak`, GAP4.15.1/CTblLib1.3.11, obtaining every stated class, matrix and subgroup check. reviewer A freshly inspected the ATLAS L4(3) group header and natural forty-point representation; the others retained the documented primary inspections and local source review. The data classifications and GAP subgroup algorithms remain specified inputs. Each separately checked the exact q=5 counts and index inequality. These reviews do not assert a full q=5 stabilizer classification, exclude arbitrary PSL4(3) components, resolve C0010, or constitute formal GitHub approval.

## Proposed single-outer-class canonical exclusions

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `7a5f36cfd2350927726aae26f850ca3c661bc1d5` as recorded below.** We exclude every entire almost-simple canonical group with socle G2(3), J2, J3, He or O'N, for arbitrary stabilizer H. These deductions use the retained canonical and inner-inversion inputs and the explicitly identified ATLAS/CTblLib data below. They do not assume a solvable full point stabilizer or concern these groups as sections of larger envelopes.

The reusable criterion is elementary. Let S be nonabelian simple with Out(S)=C2. Suppose the outside coset of A=Aut(S) has exactly one involution class, and for t in that class the order c=|C_S(t)| is even. Suppose also that every S-subgroup of order c is S-conjugate to every other one. Then S≤G≤A cannot be an entire canonical group of a finite simple proper Bol loop. The case G=A and inner inversion on G=S are already excluded by the reviewed characteristic-socle restriction and inner-inversion theorem. In the remaining case G=S with outer inversion, the original selected Λ is a nonempty union of S-classes of outside involutions. The single A-class is one S-class because t itself is an outside element of C_A(t). Thus Λ is that whole class and |H|=|S|/|Λ|=c. The actual centralizer C_S(t) is itself a subgroup of that order; the hypothesis forces H=C_S(t′) for a conjugate t′∈Λ. Choose an involution x∈H. The commuting product t′x is another outside involution and hence also a selected mark. Then x=t′(t′x) is a nonidentity element of H∩Λ², contradiction. No identification of C_S(t) by order alone is used.

The finite class data for the five applications are:

| S | Order of S | Unique outside class size | c |
| --- | --- | --- | --- |
| G2(3) | 4245696 | 2808 | 1512 |
| J2 | 604800 | 1800 | 336 |
| J3 | 50232960 | 20520 | 2448 |
| He | 4030387200 | 266560 | 15120 |
| O'N | 460815505920 | 2624832 | 175560 |

For G2(3), the complete maximal-class list has orders12096,12096,11664,11664,11232,11232,1512,1344,1092,576. The only orders divisible by1512 are the two U3(3).2 classes and the unique order1512 class L2(8).3. An H of order1512 in U3(3).2 would have index eight. Its intersection with the normal U3(3) would have index at most eight there. But the complete U3(3) maximal list has orders216,168,96,96, giving least proper index28 in the group of order6048. The intersection must therefore be all of U3(3), impossible since6048>1512. Hence every H of order1512 lies in, and equals, a conjugate of the unique maximal class of that order.

For J2, the complete maximal list has orders6048,2160,1920,1152,720,600,336,300,60. Only U3(3) of order6048 and the unique L3(2).2 class of order336 have orders divisible by336. The largest proper subgroup of U3(3) has order216 by the same complete list, so it cannot contain H of order336. Thus all such H belong to the unique order336 maximal class. For J3, the maximal orders are8160,3420,3420,2880,2448,2160,1944,1920,1152. Only the single L2(17) class has order divisible by2448, and its order is exactly2448. All subgroups of the required order are consequently conjugate. In each case the criterion applies.

For He, the complete eleven-class maximal list has only two entries with order divisible by15120: B=2².L3(4).S3 of order483840 and the unique3.A7.2 class of order15120. The source's actual normal-series structure supplies N◁B with N/2²≅L3(4) and |B:N|=6. If H≤B has order15120, then [B:H]=32. Put K=N∩H. The identity [B:H]=[B:NH][N:K] shows [N:K] divides32. Projection to L3(4) makes the index of the image of K divide [N:K], hence divide32. But the complete L3(4) maximal indices are21,21,56,56,56,120,120,120,280; none divides32. Any proper image would lie in a maximal subgroup whose index divides its own index, so the image must be all of L3(4). This forces |K|≥20160>|H|, impossible. Thus all subgroups of order15120 belong to the unique maximal class of that order. This uses the actual normal series in the cited maximal-group identification and makes no assumption about composition factors of H.

For O'N, the complete thirteen-class maximal list has only one entry with order divisible by175560: the unique J1 class of exactly that order. The two larger classes have order3753792, which is not divisible by175560, and every other maximal is smaller. Hence the required subgroup conjugacy follows immediately here as well. Both new c values are even, so the same selected-mark criterion applies.

The source authors freshly inspected the complete primary CTblLib online records for G2(3), U3(3), J3, He and O'N, and retained the already inspected complete J2 and L3(4) records. The primary ATLAS He maximal list supplies the stated2².L3(4).S3 normal-series identification. (That structural identification is an external input; the certificate does not reconstruct it from an order.) Their online1.3.10 metadata is distinguished from the executable's asserted GAP4.15.1/CTblLib1.3.11. The [certificate](../code/verify_single_outer_class_canonical.g) reads every maximal entry, checks the actual eligible entries and uniqueness, the full outer-group metadata, all normal S→Aut(S) fusions, involution power maps, class/centralizer sizes and the shared unitary-overgroup bounds. It retains subgroup-class completeness, actual group structures and character/fusion correctness as external inputs; arithmetic and consistency checks do not reprove the classifications.

The source authors read and ran the full certificate, first frozen for three cases at `5b1362e926458840e6275f41363b35b0d79da1b0` and extended to all five at `d8af1c51ecad8985f90c9f0770e463dc10c0ef0e`, with all assertions passing:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_single_outer_class_canonical.g

Contributor a research reviewer developed the G2(3) application and a research reviewer developed J2, J3 and He after the source authors's case routing; a research reviewer developed the O'N check. The source authors supplied the common criterion, the Held index argument and consolidated actual-list checks. These are development checks, not independent exact-source review. C0010 remains open.

### Independent review of the single-outer-class criterion

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `7a5f36cfd2350927726aae26f850ca3c661bc1d5`, covering the criterion and all five applications with arbitrary H, conditional on the cited canonical, inner-inversion, ATLAS/CTblLib and normal-series inputs. Each checked the outside-class non-splitting, alignment of H with an actual outside-involution centralizer and selected-mark collision. Each checked all eligible maximal overgroups, the U3(3) restrictions and Held's projection of index dividing32. Each read, extracted and independently ran the complete committed certificate with `--quitonbreak`, GAP4.15.1/CTblLib1.3.11, obtaining all five passing inventories, fusions, class/centralizer and complete-list checks. reviewer A freshly inspected the primary He maximal shapes and G2(3) group header; the other two retained the documented primary inspections. The Held normal series, subgroup classifications and character data remain external inputs. These reviews concern entire almost-simple canonical groups, not sections in larger envelopes, and do not certify C0010 or constitute formal GitHub approval.


## Proposed exclusion of all sporadic canonical socles

**Conditionally proved continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `39991d55d946ddb409cf1341ffa10e3f40ea64cc` as recorded below.** Let Q be a finite simple proper left Bol loop and let its entire canonical group G=LMlt(Q) be almost simple with sporadic socle S. Under the retained canonical inversion/selected-mark, inner-inversion and ATLAS/CTblLib inputs, no such Q exists. The stabilizer H=G₁ is arbitrary. This covers all26 sporadic socles for the entire G; it does not exclude sporadic sections of a larger G, or all sporadic socles of the full multiplication group M when G<S. The new [full-sporadic-socle assembly](../full-socle-completion/sporadic-full-multiplication-exclusion.md) closes that both-nonsolvable actual-factor problem under its stated inputs, with three independent acceptances at `8cd335ea73dadc72b38b75c294e690bdbeb7c155`.

The [odd-outer-order argument](#proposed-exclusion-of-sporadic-full-socles-with-solvable-stabilizer), independently reviewed at `6e016e1f1237545146e30786902ef92486c1524c`, excludes the14 sporadic groups with trivial outer group. Its complete26-group metadata certificate identifies exactly12 remaining outer groups, all C2. The [single-outer-class theorem](#proposed-single-outer-class-canonical-exclusions), independently reviewed at `7a5f36cfd2350927726aae26f850ca3c661bc1d5`, excludes J2,J3,He,O'N. We treat the other eight here, retaining those exact scopes rather than requiring a solvable H or I.

### Selected classes and three collision tests

Write A=Aut(S). Since Out(S)=C2, either G=A, already excluded by the reviewed characteristic-socle/inner-inversion argument, or G=S. Inner τ is also excluded in the latter case. Thus E=G⋊⟨t⟩ identifies with A, with the formal involution t acting by the outer τ. The actual selected set Λ=tK is a nonempty union of outside involution S-classes, satisfies |Λ|=[S:H], and obeys H∩Λ²={1}. Each outside A-involution class is one S-class: an outside involution u belongs to its own centralizer, so A=S C_A(u). Consequently Λ is a union of the outside A-classes as well. This makes Λ² A-invariant even when an internal A-class fuses distinct S-classes.

For A-classes C_i,C_j,D_k, the class multiplication coefficient c_ijk counts pairs (u,v)∈C_i×C_j with uv equal to a fixed element of D_k. Thus a positive coefficient places every element of D_k in Λ² when C_i,C_j are selected. The pinned certificate computes these coefficients both by GAP's operation and independently by the exact character expression

    |C_i||C_j|/|A| · Σ_(χ∈Irr(A)) χ(u_i)χ(u_j) overline(χ(d_k))/χ(1).

These two calculations use the same stored character data, whose correctness is an input; agreement does not independently validate those data. Three elementary collision tests suffice:

1. If |H| is even and Λ² contains every involution of S, Cauchy's theorem gives a forbidden element of H∩Λ².
2. Suppose Λ is one class C, and every S-subgroup of order |S|/|C| is conjugate to C_S(u) for u∈C. It suffices that C² contain any internal involution x. Write x=vw with v,w∈C. Since v,w,vw have order two, v and w commute, so x∈C_S(v). Conjugating v to the u whose centralizer is the aligned H gives a nonidentity element of H∩C². This test does not require that C be the only outside involution class.
3. Suppose H has even order and every involution it can contain lies in one A-class D, with c_DDD=0. A Sylow2-subgroup P of H has a central involution z. Any different involution u∈P would commute with z and make zu a third involution of P. All three would lie in D, contradicting c_DDD=0. Therefore P has a unique involution. The standard finite2-group theorem makes P cyclic or generalized quaternion, so P has an element of order at least |P|/2. An independent bound on2-power element orders can contradict this. The precise external source is Conrad, Theorem4.10 p.8 and Theorem3.2 p.2, recorded in REFERENCES.md; that classification is not inferred from the character calculation.

### Complete finite inventory

In each row, label outside classes C1,C2,C3 in the increasing-size order displayed. The admissible selections below are **all** nonempty unions whose size divides |S|; the certificate enumerates every subset. The H-orders in the next column have the same order as those selections.

| S | Outside class sizes | Admissible selected class indices | Corresponding H-orders | Collision test |
|---|---|---|---|---|
| M12 | 792 | {1} | 120 | 1 |
| McL | 113400 | {1} | 7920 | 1 |
| HN | 75240000 | {1} | 3628800 | 1 |
| M22 | 330;1386 | {1};{2} | 1344;320 | 1 for both |
| HS | 1100;23100 | {1};{2} | 40320;1920 | 1 for both |
| Suz | 370656;2358720 | {1};{2} | 1209600;190080 | 1 for both |
| Fi22 | 61776;19459440;22239360 | {1};{2};{3};{2,3} | 1045094400;3317760;2903040;1548288 | 2;3;3;1 |
| Fi24′ | 306936;5686767482760 | {1};{2} | 4089470473293004800;220723937280 | 2;1 |

There are15 admissible selections, all with even H-order. For every row marked test1, the computed coefficient matrix covers every internal involution A-class. In particular the Fi22 union {2,3} captures all three internal classes; no singleton-only assumption is made.

For Fi22 selection {1}, H has order1045094400. Of every entry of the complete S-maximal list, only the unique O8+(2).3.2 entry has order divisible by |H|, and its order equals |H|. As H is proper, it lies in a maximal subgroup and equals that subgroup. The actual C_S(u), u∈C1, has the same order: the outside class is one S-class, so its S-centralizer order is |S|/|C1|. It follows that every H of this order is conjugate to that actual centralizer. C1² contains an internal involution class, so test2 applies. This uses a complete class list to identify conjugacy; it never identifies a subgroup solely from its order.

For Fi24′ selection {1}, the same argument applies with |H|=4089470473293004800 and the unique eligible maximal Fi23. Every other S-maximal subgroup is smaller. C1² again contains an internal involution class. The library's canonical identifiers are F3+ and F3+.2, with Fi24′/Fi24′.2 as aliases.

For the two remaining Fi22 singletons {2} and {3}, Λ² contains internal A-class positions3 and4, missing only position2. Thus an admissible H could have involutions only in position2. The exact character calculation gives c_(2,2,2)=0. The two possible Sylow2-subgroup orders are8192 and1024, respectively. But the largest2-power order among all element classes of Fi22.2 is16. Test3 would require an element of order at least4096 or512, respectively, contradiction. These are class positions in the pinned A-table, not assumed S-class labels.

This closes every admissible selection for all eight groups. Together with the14 trivial-outer and four previously reviewed single-class cases it excludes all26 sporadic canonical socles, conditional on the explicit inputs.

### Reproducible evidence and limits

The source authors read and ran [verify_remaining_sporadic_canonical.g](../code/verify_remaining_sporadic_canonical.g) with GAP4.15.1/CTblLib1.3.11. It asserts the versions, sporadic/outer metadata, all stored S→A fusions and normal class-size sums, involution power-map agreement, all outside sizes and every integral subset. It computes every needed product coefficient twice with exact arithmetic. For Fi22 and Fi24′ it asserts every entry of the complete maximal lists and the unique eligible order; for Fi22 it also cross-checks the zero coefficient and largest2-power class order. All15 cases passed. Run from the repository root:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_remaining_sporadic_canonical.g

Contributor a research reviewer supplied the finite class-product reductions and initial scratch certificate; the source authors supplied the selected-class centralizer formulation, strengthened the fusion/metadata checks and assembled the all26 scope. These are development checks. Stored character/fusion correctness, maximal-list completeness, outer-group identification and the cited finite2-group theorem remain external inputs. No loop search, general sporadic-full-socle theorem or complete Bol classification is claimed. C0010 remains open.


### Independent review of the all-sporadic canonical exclusion

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `39991d55d946ddb409cf1341ffa10e3f40ea64cc`, conditional on the stated canonical/inner-inversion results, ATLAS/CTblLib data and finite2-group theorem. Each checked the complete14+4+8 assembly, non-splitting of outside classes, coefficient interpretation, all three collision arguments and all15 selections, and independently read, extracted and ran the full committed certificate under GAP4.15.1/CTblLib1.3.11 with `--quitonbreak`; all assertions passed. reviewer A freshly inspected Conrad's Theorems4.10 and3.2; reviewer B freshly inspected the unique-involution theorem and its generalized-quaternion input; reviewer C confirmed the primary notes' stated classification while retaining the recorded exact-locator inspection. The reviewers retained the documented complete-Maxes semantics and did not reconstruct the stored class/fusion data or maximal-subgroup classifications. These are scoped model mathematical/code reviews, not formal GitHub approval or a proof of C0010 in full. Larger canonical envelopes and sporadic full-Mlt cases with proper canonical factors remain open.


## Proposed exclusion of every alternating canonical socle

**Conditionally proved scoped continuation of 0323-finite-simple-non-moufang-bol-loops:C0010; independently reviewed at exact source `b03fdd414954bf1fc12186e13c8e3da404e87f95` as recorded below.** For every integer m≥5, no finite simple proper left Bol loop Q has entire canonical group A_m≤G=LMlt(Q)≤Aut(A_m). The stabilizer H is arbitrary. Here m is the alternating socle's standard permutation degree, not an identification of the loop order with m. This does not exclude an alternating full multiplication group whose canonical G fails to contain its socle.

The canonical proof for m≥7 is [C0007, Theorem3.1](../foundations/C0007.md), specifically its arbitrary-H cycle-class argument and two degree regimes. This assembly does not duplicate that proof or rely on C0007's unreviewed Lie-type aggregate. It supplies the separate exception interface and exact-source review obligation for the existing alternating proof. Standard Aut(A_m)=S_m for m≥7 leaves only A_m and S_m. For m=5,6 use A5=PSL2(4) and A6=PSL2(9) and the independently reviewed **all** PSL2 canonical-overgroup exclusion at `47b07688a82d3df93f537946fe0780112200383b`. This covers every exceptional A6 intermediate, not just the standard degree-six S6, without using the older BSGS/subgroup-enumeration certificate. The original proof and arithmetic source were introduced at `79b70a50b19bc728b349a2a6ed2bd958391e8b6e`; their historical status and pins are retained.

The finite obligations used from `code/test_lmlt_exclusions.py` are only `verify_am_sm_small_degrees_5_to_8()` and `verify_theorem_9_regimes_9_to_45()`, and their arithmetic helpers. The first supplies the needed m=7,8 cases (its additional standard m=5,6 cases are not the A6 exception argument). The second checks the m=9 high-class boundary, the m=10,11 induction bases, the four m=42..45 convexity/step-four induction bases and every low-class union in m=9..41. The source authors read these full paths and ran them with Python3.12.14: there were23 small-degree initial divisibility hits, all eliminated; the low-class range had208 hits, successively reduced by158,30,19 to the stated S11 case. Its impossible order is excluded analytically in the canonical proof by Bochert's bound. These finite checks do not establish the all-degree inequalities, the diagonal-strip bound or their classical permutation-group inputs.

For clarity about two compressed steps in that existing proof, its subdirect-diagonal argument applies after restricting to the kernel on the other orbits and the block permutations. A nontrivial alternating projection of the resulting normal subgroup is the full simple alternating block group. A strip on one block alone would contain a3-cycle in H, so every strip uses at least two blocks; this is what controls the factorial contribution. In the prime-cycle step, a transitive orbit of degree d≥p>m/2 containing a p-cycle is primitive: in a nontrivial block system both the number and size of its blocks are less than p, so an element of order p cannot act nontrivially. The subgroup fixing the complement contains the p-cycle and is normal in the local primitive action. If that action contained A_d, its nontrivial normal subgroup would contain A_d as well (C_(S_d)(A_d)=1); this would put a forbidden3-cycle in H. These are clarifications of the existing inference, not additional hypotheses.

The [primary source record](../foundations/references.md#alternating-canonical-source-audit) distinguishes Dixon's odd-order tournament bound from his solvable-group bound used earlier, retains Feit–Thompson, and verifies the exact Praeger–Saxl, Bochert and Jordan statements used. The citation DOI in C0007 is corrected from the erroneous DOI ending049 to **10.4153/CMB-1967-048-9**. The source authors freshly inspected the publisher's Dixon and Jones statements and the retained original Praeger–Saxl first-page image, including its explicit Bochert factorial. The quoted classical theorems remain inputs; neither their proofs nor all of C0007 are certified by source inspection.

Run the two required checks from the problem's code directory:

    python3 -c 'import test_lmlt_exclusions as a; print(a.verify_am_sm_small_degrees_5_to_8()); print(a.verify_theorem_9_regimes_9_to_45())'

Contributor a research reviewer performed the preliminary proof, code and source audit. The source authors separately read the proof and arithmetic paths, inspected the stated primary statements and reran both checks. These are development checks. C0007's aggregate review metadata remains unreviewed, C0010 remains open, and no classification of all loop operations or nonsocle-containing canonical factors is claimed.


### Independent review of the alternating canonical assembly

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `b03fdd414954bf1fc12186e13c8e3da404e87f95`, explicitly including the complete inherited C0007 Theorem3.1 argument for m≥7 with arbitrary H and this assembly's separately reviewed m=5,6 interface. Each checked the cycle products and parity constraints, both degree regimes, the normal-kernel and diagonal-strip factorial bound, gamma convexity and every step-four estimate, Sylow support and Jordan–Bochert screens. Each extracted both committed Python files and independently ran only the two specified arithmetic functions using Python3.12.14; all counts matched. reviewer C first ran with the system interpreter, then repeated with the mandated pinned runtime and both imports extracted from the exact source. reviewer A freshly inspected the Dixon tournament and Jones prime-cycle statements. The other source checks were retained from the documented coordinator/contributor inspections; none of the reviewers reproved the cited classical results, Feit–Thompson or alternating automorphism classifications. The acceptance is conditional on those and the pinned canonical inputs. C0007's unrelated Lie-type aggregate remains unreviewed, and C0010 remains open; these are model mathematical/code reviews, not formal GitHub approval.


The reviewed [all-odd-dimensional linear full-socle assembly](../full-socle-completion/odd-linear-full-socles.md) supplies the actual-factor and original-mark arguments missing from the earlier odd-composite residual discussion. It reuses only the scoped upper-bound component of the reviewed Singer/parabolic proof and adds a new lower bound. Its combined result has three independent exact-source reviews recorded there; earlier source/review pins retain their historical scopes.
