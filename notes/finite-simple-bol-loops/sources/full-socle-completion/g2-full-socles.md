# All G₂ full multiplication socles

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md). Three independent exact-source mathematical reviews are recorded below.

**Conditionally proved theorem.** Under the canonical and group-classification inputs below, Soc(Mlt(Q)) is not G₂(q) for any finite simple proper left Bol loop Q and any prime power q>2. This assembles canonical and both proper-factor orientations; it makes no assertion about arbitrary G₂ sections inside larger envelopes. G₂(2) is nonsimple, and its derived PSU₃(3) belongs to the separately treated unitary family.

Use the notation and exact C0001/C0007/C0008/component source pins in [the exceptional field-involution proof](exceptional-field-involution-exclusions.md). That proof excludes S≤G for every G₂(q), where S=Soc(M), G=LMlt(Q) and M=Mlt(Q). The complete full-G₂(4) result is separately reviewed at source `c488dbb75c3ba1f7936d158b92ddb5c5951c20c5` in [g24-full-socle.md](g24-full-socle.md). The local odd-dimensional outer-involution class-square input is the n=3 theorem at `b436485f3c07c3413c19b319e51e8c7bc2c3a580`, with its diagonal normalization/precise local scope recorded at `114ce1b011fd47589eb762ed7cd5492a190002d8` in [the canonical overgroup proof](../factor-permutation/radical-free-three-dimensional-linear-unitary.md). The proof uses that local square statement, not a supposed implication from excluding an entire canonical group to excluding every component.

## Actual proper factors

Let I=M₁ and H=G∩I. Suppose S is not contained in G. Then M=GI is a factorization by core-free factors. Kazarin–Martínez-Pastor–Pérez-Ramos2015, Lemma11 proof pp.56–57, directly quotes the exceptional classification of Liebeck–Praeger–Saxl1990 TheoremB and explicitly gives **actual** socle intersections, not just maximal overgroups. Outside q=4 this leaves q=3^f. Up to interchanging the factors, put A₀=G∩S and B₀=I∩S. The quoted alternatives are

    A₀=SL₃(q) or SL₃(q).2,
    B₀=SU₃(q) or SU₃(q).2, or ²G₂(q) when f is odd,
    S=A₀B₀.                                             (2)

The ordering of A₀,B₀ in this display is purely for notation; both canonical-factor placements will be treated. The source's statement (2) is an explicit input. We do not infer it from M=GI in general. The quoted classification, including its standard normal subgroup identifications, has not been rederived; the original LPS/HLS classification proof was not newly accessed. The source authors inspected the later source and its bibliography, which identifies TheoremB as LPS1990.

Let L_A=SL₃(q), and let L_B be SU₃(q) or ²G₂(q) respectively. Set a=[A₀:L_A]≤2 and b=[B₀:L_B]≤2; in the Ree case b=1. The standard orders and (2) give

    |A₀∩B₀|=ab(q²−1)      in the unitary case,
    |A₀∩B₀|=ab(q−1)       in the Ree case.

The kernel of the homomorphism A₀∩B₀→(A₀/L_A)×(B₀/L_B) is L_A∩L_B, and its image has order dividing ab. Thus |L_A∩L_B| is a multiple of q²−1 or q−1, respectively, and is even. This retains the index-two extensions; it does not assume L_A L_B=S.

The groups L_A and SU₃(q) are centerless simple, since q is a power of3 and gcd(3,q±1)=1. The Ree group is simple for f≥3 odd. At f=1 replace L_B=²G₂(3) by X_B=L_B′≅PSL₂(8), of odd index3. Its intersection with L_A is still even, since the quotient of L_A∩L_B by L_A∩X_B embeds in L_B/X_B. The identification of the derived group is explicit in Burness–Thomas p.7, and the standard order1512 gives the index. In all other cases put X_A=L_A and X_B=L_B; also X_A=L_A at f=1.

Whichever of X_A,X_B lies in the actual canonical factor is its perfect residual X=G^(∞). Indeed X is perfect normal in G₀=G∩S, the quotient G₀/X is solvable of order1,2 or3, and G/G₀ is solvable as a subgroup of Out(S). Therefore G^(∞)≤X and perfection gives the reverse inclusion. In particular X is characteristic in G and H∩X is even by the preceding actual-intersection argument.

## A component collision in the original extension

Let X be a characteristic nonabelian simple subgroup of canonical G. Suppose every nonidentity involution β∈Aut(X) has an X-class whose square contains every involution of Inn(X)=X. If H∩X is even, no such canonical folder exists.

To prove this, work with the original Λ in E=G⋊⟨τ̂⟩. At least one λ∈Λ acts nontrivially on X: otherwise all products τ̂λ, which comprise K because τ̂∈Λ, centralize X; then G=⟨K⟩ centralizes its own nonabelian subgroup X, impossible. Its action β has order2. For x,y∈X, the product λ^xλ^y lies in X, since λ normalizes X and λ²=1. Its action on X is β^xβ^y. As X→Inn(X) is faithful, the assumed local square statement puts every X-involution into the **actual** Λ². An involution in H∩X contradicts Λ²∩H={1}. This argument does not assume C_G(X)=1 and does not construct a quotient folder.

For X=SL₃(q) or SU₃(q), q=3^f, the pinned local theorem covers all noninner involutions of Aut(X). Inner involutions form one X-class: the characteristic is odd, the center is trivial and the −1-eigenspace has dimension2. Diagonal determinant-one sign matrices form a Klein four subgroup. The product of two distinct such involutions is the third, so the square of the unique inner class contains that class. This establishes the required property for every β.

For X=²G₂(q), f≥3 odd, Out(X) has odd order, so β is inner. The unique involution class and involution centralizer C₂×PSL₂(q) are the pinned source inputs from Bäärnhielm **arXiv:1206.0411v3**, Propositions3.3(4),3.6 and3.7(1), also used in the reviewed [small-Ree support argument](../factor-permutation/radical-free-involution-support.md) at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`. The centralizer contains a Klein four subgroup, which proves the same class-square property. For X=PSL₂(8), Out(X)=C₃; its single involution class and elementary abelian unipotent subgroup of order8 give the property directly, using the previously reviewed PSL₂ input at `47b07688a82d3df93f537946fe0780112200383b`.

Thus the component collision excludes either canonical-factor placement in (2), including the nonsimple Ree3 factor through its simple derived subgroup. Together with the field-involution canonical proof, the proper-factor classification outside characteristic three, and the reviewed q=4 full result, this proves the proposed all-q theorem under the stated inputs.

## Evidence and remaining scope

This assembly uses exact source statements, finite-group order identities and the original marked-set argument; it adds no research computation. The prior q=4 certificate and its three exact-source mathematical/code reviews remain pinned separately. Independent reviews of this uniform assembly and its linked field-involution proof are recorded below. Passing repository integrity does not certify these deductions, and the complete classification remains open.


### Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted this manuscript and its linked companion at exact source `cd5bf6a31bc63eb838b3150e51dd7aaec57be838`. All checked the cyclic outer reduction, original outside-class collision, split subfield correspondence, inverse-triality parameter-one roots, actual G₂ factor placements and even intersections, Ree3 derived subgroup, and the component collision without assuming faithful centralizer action. Each freshly inspected the KMP2015 Lemma11 actual-factor statement. The paired reviewer additionally freshly inspected BGH v2 Table2/Example3.22, Dudas–Michel Theorem7.3, Burness–Thomas Remark2.2/Proposition2.3 and Aschbacher–Seitz18.2/19.1–19.2; that reviewer retained the exact exceptional-isogeny construction as a cited input. The other two retained the recorded external automorphism/class/root inspections without freshly browsing those sources. None rederived the underlying classifications. No research computation was required; the source authors's separate Python3.12.14 integrity run passed115 tests. These model mathematical reviews have exactly the displayed family scope and are not formal/human certification, GitHub approvals or a solution of unrestricted C0010.
