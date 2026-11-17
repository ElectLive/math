# Radical-free inner inversion and PSL₂ envelopes

Mira Cult

**Independently reviewed**, continuing [0323:C0010](../foundations/research-C0010.md). Suppose a finite simple nonassociative left Bol loop has a faithful generated canonical folder (G,H,K), G=T a finite nonabelian simple group, canonical inversion τ inner, and T has one conjugacy class C of involutions. Then no such envelope exists, conditional on the reviewed repointing and Bruck-structure inputs and the standard finite-group V4 input below. This first case makes no assertion for outer τ or several involution classes, and the construction does not require the original loop to have exponent two.

The repointing theorem used here is [odd-layers-in-even-envelopes](odd-layers-in-even-envelopes.md), exact reviewed source `17e56bdfb16097218249f42f10e91adcb9f5a4b8`, with its stated C0001/C0007 source qualifications. For a simple nonassociative exponent-two Bruck loop, the Baumeister–Stein structure input, recorded with source qualifications in [bruck-all-radical-constraints](../bruck-completion/bruck-all-radical-constraints.md), is that G/O₂(G) is a nonempty product of PGL₂(q_i) for q_i=9 or a Fermat prime at least 5. This is Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/abs/0908.2597v1), Theorem 1(b), equivalently v2 Theorem 1(c)(1),(3), with the primary source audit recorded at `6b719ad3026522f93cd9e0e027ae4027f6ee12df`. Each factor has a proper nontrivial normal subgroup PSL₂(q_i) of index two, so such a product is not a nonabelian simple group.

If τ=id, its inversion action on K gives k²=1 for every k∈K. The loop has exponent two and its identity inversion is an automorphism, so it is a Bruck loop (use the opposite loop if necessary for the cited right-Bruck convention). Its radical-free canonical group is T, contradicting the preceding structure theorem.

Assume τ≠id. Write τ=Int(a), where a∈T and a²=1 because τ²=1 and Z(T)=1. In the formal extension E=T⋊⟨τhat⟩ the outside involution c=a τhat is central. Let Λ=τhat K be the actual marked set, a G-invariant union of outside involutions, and write Λ=cS with S⊆T. As c is central and Λ consists of involutions, S⊆{1}∪C. Since τhat=ca lies in Λ, a∈S. Single-class conjugation invariance implies S=C or S={1}∪C.

If S={1}∪C then c∈Λ. Repoint at the actual mark c. The reviewed repointing theorem gives a faithful generated simple nonassociative folder with the same (G,H) and marked set, with τ′=Int(c)|G=id and section K′=cΛ={1}∪C. It is an exponent-two Bruck folder, contradicting the Bruck structure theorem as above. This step does not claim the repointed loop is isomorphic to the original or preserves its properness; nonassociativity and simplicity are what the theorem supplies and what the argument needs.

If S=C, then |K|=|Λ|=|C| and |H|=|T|/|C|=|C_T(a)|, an even number. By Cauchy's theorem H contains an involution. Every involution of T belongs to C²: choose any Klein four subgroup ⟨x,y⟩; then x=y(xy) is the product of two involutions in C, and conjugation transports this equality to every member of the unique class C. But Λ²=C², so H∩Λ² contains an involution, contradicting the original folder transversality condition H∩Λ²=1.

The only external finite-group input for the last case is that a finite nonabelian simple group containing an involution contains a Klein four subgroup. If a Sylow 2-subgroup has no Klein four, it has a unique involution and is cyclic or generalized quaternion. A cyclic Sylow 2-subgroup gives a normal 2-complement by Burnside transfer, while generalized quaternion Sylow 2-subgroups are excluded for finite nonabelian simple groups by Brauer–Suzuki, [“On finite groups of even order whose 2-Sylow group is a quaternion group,” PNAS 45 (1959), 1757–1759](https://pmc.ncbi.nlm.nih.gov/articles/PMC222795/), DOI `10.1073/pnas.45.12.1757`, Theorem 1 on p. 1757, which explicitly includes both quaternion and generalized quaternion Sylow 2-subgroups. The source authors directly checked the statement in the [original page image](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/809a/222795/856bc3e51e82/pnas00199-0111.png); the proof was not reverified here. The simple group here already contains an involution by assumption, so Feit–Thompson is not needed for this step. The classification of finite 2-groups with one involution and the cyclic-Sylow transfer input are invoked as standard finite-group facts and have not been freshly source-audited in this note.

## The outer case for PSL₂(q)

**Independently reviewed outer case**, continuing [0323:C0010](../foundations/research-C0010.md). Suppose the faithful generated canonical folder of a finite simple nonassociative Bol loop has G=T=PSL₂(q), q≥4, and its inverting automorphism τ is outer. Then no such folder exists, conditional on the cited automorphism and square-class inputs. This does not assert an exclusion for arbitrary radical-free groups. Combined with the inner/one-class deduction it excludes G=PSL₂(q) for all q in the canonical nonassociative simple setting.

Use the square-class lemma in [sd3-involution-count](../primitive-completion/sd3-involution-count.md), independently accepted at `65c54aff108cc70208bf6f7271b1e5cf6a0a76bc`: T has one involution class I and, for every nonidentity involution α∈Aut(T), I⊆(α^T)². Its proof uses Glauberman Z* and retains the cited C0001/C0007 source qualifications. That source also records Aut(T)=PΓL₂(q), the PGL/field-coset automorphism formulas, and the Guralnick–Zieve Annals 2010 Appendix source; the reviewing agent directly inspected Lemma A.3 but could not access the full publisher text of Glauberman and corroborated the isolated-involution consequence separately.

Since τ is outer, E=T⋊⟨τhat⟩ embeds faithfully into Aut(T), identifying τhat with α=τ. The actual marked set Λ=τhat K is a T-invariant nonempty union of involution classes in the single coset Tα, and contains α^T. By the square-class lemma I⊆(α^T)²⊆Λ². Thus H∩Λ²=1 forces H to have odd order. We show that the class count and |Λ|=[T:H] instead force |H| even.

If q is odd and α has no field component, it belongs to PGL₂(q)\T. Projective involutions have semisimple eigenvalue ratio −1, so there are two PGL₂(q)-conjugacy types, split and nonsplit, of respective sizes q(q+1)/2 and q(q−1)/2. The determinant square class is constant on each type and different for the two; consequently precisely one type lies outside T. Its PGL centralizer is the even-order dihedral normalizer of the corresponding torus, and it contains an element outside T (the involution itself); hence that PGL class is one T-class. Therefore Λ is that class, and |H|=|C_T(α)|, which is q−1 or q+1 and is even.

If α has nontrivial field component, the extension degree is even; put q=s² and σ(x)=x^s. The reviewed Hilbert-90 calculation says all involutions of PGL₂(q)σ form one PGL₂(q)-class with centralizer PGL₂(s). For q even, PGL₂(q)=T, so the outside involutions are a single T-class and |H|=|PGL₂(s)|, which is even.

For q odd, PGL₂(s) lies in T because every element of F_s* is a square in F_{s²}*. The PGL class therefore splits into two equal T-classes. They both lie in the same coset Tσ: for B∈PGL₂(q), the square class of det(Bσ(B)⁻¹) is trivial since det(B)^{1−s} is a square. Thus an outer involution with nontrivial field part is T-conjugate to one of these two classes, and the other possible T-coset in PGL₂(q)σ contains no involutions. Λ is either one or both of these equal T-classes, so

 |H|=|PGL₂(s)|/r,   r∈{1,2}.

Since s is odd, 8 divides |PGL₂(s)|=s(s²−1), and |H| is even in both cases. This includes q=9 (s=3) without identifying Aut(A6) with S6.

In every case H is both even and odd, contradiction. The proof counts only actual T-conjugacy classes in the given outer coset; it does not assume Λ is the full coset of involutions if it contains two classes, and does not use a quotient folder. The PGL involution-class counts and dihedral centralizers are stated in Guralnick–Zieve, [Annals of Mathematics 172 (2010), Appendix, Lemma A.3, p. 1355](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf); the lemma statement was directly inspected, not its full proof. The deduction and the odd-field splitting calculation have the independent scoped reviews below.

Combining the inner case above with this outer case excludes a finite simple nonassociative Bol canonical envelope with $`G=\mathop{\mathrm{PSL}}\nolimits_2(q)`$, $`q\ge4`$, for **any** canonical inversion, subject to all cited inputs. It does not exclude other radical-free groups.

## Independent mathematical review

automated-model reviewers `review_s5_h3`, `review_hs_full` and `review_presentations` independently accepted both arguments at exact source `88f2b7c0260426c220b3d5ec4272fed9d7801255`, conditional on the pinned canonical-folder, repointing, Bruck-structure, square-class and finite-group inputs. They checked the actual selected-set alternatives, the preservation needed for repointing, the odd-square field-coset splitting (including q=9), and the stabilizer parity contradictions. `review_s5_h3` had previously inspected Guralnick–Zieve Lemma A.3; the other two made no fresh primary-source audit. `review_presentations` verified prerequisite commits locally and inspected the repository square-class and Hilbert–90 arguments. None freshly audited the Glauberman or Brauer–Suzuki primary proofs. These are independent model reviews, not formal or human certification; their scope is the stated inner single-class and all-PSL₂ exclusions, not arbitrary radical-free groups.

The later [general inner-inversion reduction](../factor-permutation/exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup), independently reviewed at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`, excludes inner inversion whenever O₂(G)=1, without an involution-class hypothesis. The earlier proof above and its review pin are retained as historical source; the new reduction also applies to nonsimple canonical groups.


## All almost-simple PSL2 canonical overgroups

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, with three independent mathematical reviews below.** No finite simple nonassociative left Bol loop has canonical left multiplication group G with

    S=PSL2(q) ≤ G ≤ Aut(S),    q≥4.                         (1)

Here S is the socle of G. No assumption identifies it with the socle of the full multiplication group. This strengthens the reviewed entire-group G=S theorem above; it does not exclude PSL2 factors inside arbitrary larger canonical groups.

Use the same pinned canonical and square-class inputs as above, the [general inner-inversion theorem](../factor-permutation/exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup) reviewed at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`, and the canonical identity G=HG′ from C0001, also used in [the all-parity metabelian argument](nonbruck-almost-simple-radical-bridge.md#proposed-all-parity-exclusion-of-metabelian-left-multiplication-groups) at `a49fcc00652e8226ffab4dbc33e9d708ec835f0a`. The standard Aut(S)=PΓL2(q) input includes q=9; its outer quotient is C_(2,q−1)×C_f for q=p^f. The reviewed field-coset calculation at `88f2b7c0260426c220b3d5ec4272fed9d7801255` supplies the particular involution information used below.

First G′=S: its quotient in Out(S) is abelian, while S is perfect. Thus S is characteristic in G. Restriction embeds Aut(G) into Aut(S). Indeed, with G embedded by conjugation on its centerless socle, an automorphism of G restricting to β on S satisfies

    ρ(a(g)) = β ρ(g) β^−1.

The faithful map ρ:G→Aut(S) makes restriction injective, and identifies the restrictions of inner automorphisms with G itself. Since Out(S) is abelian, every automorphism of G acts trivially on G/S. Canonical inversion τ acts as inversion on G/G′ because it inverts the generating section K. Consequently A=G/S is elementary abelian: its rank is at most one if q is even, and at most two if q is odd.

The almost-simple G has O2(G)=1. The reviewed general inner-inversion theorem therefore forces τ to be outer. Its restriction β is an involution of Aut(S) outside G. The natural conjugation action embeds the entire formal extension E=G⋊⟨τhat⟩ into Aut(S): a kernel element outside G would express β as an element of G, contrary to outerness. Let Λ=τhat K be its actual canonical marked set. It is a union of G-classes of involutions, includes τhat, satisfies H∩Λ²=1, and |K|=[G:H].

The reviewed square-class lemma says that for every nonidentity involution β∈Aut(S), the unique S-class of internal involutions is contained in (β^S)². Applied in this faithful E, it places all S-involutions in Λ². Hence

    H∩S has odd order.                                    (2)

For A=1 the previously reviewed G=S theorem gives the contradiction; no assertion that all automorphisms of S are inner is made. Suppose A≠1. If q is even, the only possible nontrivial elementary outer subgroup is the field-involution subgroup, requiring f even. Every involution of Aut(S) has outer image either trivial or that field involution. Both images lie in A, forcing β∈G, a contradiction. For q odd with f odd, the only possible A is the diagonal subgroup C2, and again every involution image lies in A, with the same contradiction.

It remains that q=s² is odd. Write d for the nontrivial diagonal outer label and f0 for the field-involution label. Every involution of Aut(S) has outer image in {1,d,f0}; the mixed coset df0 contains no involutions. The latter fact is proved in the reviewed outer-case section above: every involution in PGL2(q)σ is PGL2(q)-conjugate to σ, and the conjugating coboundary Bσ(B)^−1 has square determinant because s is odd. Hence it lies in Sσ, never in the mixed diagonal-field coset. This concerns actual outer labels, not a conjugacy assertion between different cosets.

If A=⟨d,f0⟩ then every involution image lies in A, contradicting β∉G. If A=⟨d⟩, β must have image f0. The outer images available in βG are f0 and df0; the second has no involutions. Thus every mark in Λ has image f0, so every element of K=τhatΛ has trivial outer image. This gives ⟨K⟩≤S<G, contradicting generation. The case A=⟨f0⟩ is identical with d and f0 interchanged.

Finally suppose A=⟨df0⟩. The identity G=HG′=HS says H maps onto this order-two quotient. Together with (2) this gives |H|₂=2. By Cauchy's theorem H has an involution, which must lie outside S because H∩S is odd. Its outer label is df0, contradicting the empty mixed involution coset. This exhausts A and proves (1), under the stated inputs.

The source authors and a research reviewer developed the outer-label argument; the earlier same-socle normalizer route is unnecessary for this stronger statement. No new computation or external classification is used in this canonical-overgroup argument. The existing source-limit qualifications for the square-class/Glauberman and canonical inputs remain in force.

### Independent review of the canonical PSL2 overgroups

automated-model reviewer A, reviewer B and reviewer C independently accepted this section at exact source `47b07688a82d3df93f537946fe0780112200383b`. They checked restriction to the socle, the elementary outer quotient, exclusion of inner inversion, every outer-label case including q=9, the empty mixed coset, actual-mark generation and the stabilizer-surjectivity contradiction. They retain the pinned canonical, automorphism, square-class/Glauberman and inner-inversion inputs; this pass did not reprove those external results. The separate full-multiplication assembly and its computation have their own review record in [the bridge manuscript](nonbruck-almost-simple-radical-bridge.md#independent-review-of-the-full-psl2-socle-exclusion). This is independent model review, not formal or human certification.
