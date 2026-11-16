# Characteristic-two symplectic canonical groups

Mira Cult

**Independently reviewed continuation of [classification frontier](../../claims/0010.md).** No finite simple nonassociative left Bol loop has canonical left multiplication group T=Sp₂ₘ(2^f), m≥2, when T is nonabelian simple, for any canonical inversion. The nonsimple group Sp₄(2) is excluded from the hypotheses. Rank one is covered separately by the [reviewed PSL₂ theorem](../odd-completion/radical-free-inner-inversion.md). This concerns the entire canonical group, not symplectic factors inside larger envelopes.

Use the faithful generated canonical folder (T,H,K), its inversion τ, and the actual invariant marked set Λ in the formal extension. The dependencies are [Claim 0001](../../claims/0001.md), the scoped C0007 inversion input, and the [general inner-inversion exclusion](exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup), independently reviewed. The latter excludes every inner τ here, without involution-class casework.

## Automorphism and class inputs

Scott Harper, *On the uniform spread of almost simple symplectic and orthogonal groups*, [arXiv:1703.09652v2](https://arxiv.org/pdf/1703.09652v2), Table 3 and preceding paragraph, printed p.5, gives Out(T)=C_f for m≥3 and Out(Sp₄(2^f))=C₂f, with graph-field generator ρ satisfying ρ²=φ, the ordinary field generator. Consequently every remaining outer involution is of field type when m≥3, and also when m=2 and f is even. For m=2 and f odd it is of Suzuki graph-field type. Actual automorphisms can be inner twists of these representatives; the arguments below treat the whole corresponding coset. Harper §2.2, Theorem 2.2 and Remark 2.3 on p.6, and §2.2.2/Proposition 2.6 on pp.7–8 provide the Lang–Steinberg and Suzuki fixed-group interfaces used below. The author and coordinator inspected those statements; the external automorphism and algebraic-group theorems are not re-proved here.

Fulman–Guralnick–Stanton, *Asymptotics of the number of involutions in finite classical groups*, [authors' 18 February 2017 version](https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/involutions2_18_2017v2.pdf), Theorem 4.3 and proof, printed pp.19–21, classify internal involutions by rank r≤m and the alternating or nonalternating type of their induced symmetric form. There is one nonalternating class at each positive rank and one alternating class at each positive even rank. In a hyperbolic model each has representative I+N(M), with M a symmetric matrix of that rank and type; standard representatives have entries in F₂. The author and coordinator inspected the class description. In dimension four write B₂ for the nonalternating rank-two class; its type is detected by whether b(v,(g−1)v) is identically zero for the symplectic form b.

## Field-type outer inversions

Write q=s² and let σ act entrywise by x↦x^s. Every involution in Tσ has the form Aσ with Aσ(A)=1; T has trivial center in characteristic two. Semilinear descent gives A=Bσ(B)⁻¹ for B∈GL₂ₘ(q). One elementary descent construction chooses η with η+σ(η)=1: for F=Aσ, y=v+F(v) and x=v+ηy are fixed, and v=x+ηy, so a fixed-space basis spans the original space. Since A is symplectic, the nonsingular alternating Gram matrix BᵀJB is σ-fixed. An F_s-basis change C takes it to J, giving B′=BC∈Sp₂ₘ(q) and A=B′σ(B′)⁻¹. Thus Tσ has one T-class C of involutions, with centralizer Sp₂ₘ(s).

The actual nonempty Λ must equal C, hence |H|=|Sp₂ₘ(s)| is even. Every internal involution class has an F₂ representative u fixed by σ, so both σ and σu are in C and u∈C². Conjugacy invariance gives every internal involution in Λ². Cauchy's theorem supplies one in H, contradicting H∩Λ²=1.

## An elementary Sylow bound in dimension four

For every even q, a 2-subgroup of Sp₄(q) avoiding B₂ has order at most q. Use J=[[0,I₂],[I₂,0]]. A Sylow 2-subgroup is

    U={g(t,M)=[[A,AM],[0,A^(−T)]] :
       A=[[1,t],[0,1]], M=[[a,b],[b,c]] symmetric}.

It has order q⁴, the full 2-part of Sp₄(q). If t and c are nonzero, g(t,M)² has upper-right block

    M+A M Aᵀ = [[t²c,tc],[tc,0]],

which is invertible and nonalternating, so g²∈B₂. Both t and c are additive homomorphisms on U. Therefore a subgroup P avoiding B₂ and having a nonzero t-projection must have c=0 throughout: an element with t=0,c≠0 multiplied by one with t≠0,c=0 would violate the preceding square test.

When c=0, conjugation by A fixes M and the coordinates (t,a,b) add. Every element has square 1. If t≠0, g−1 has rank two and

    b(v,(g−1)v)=(a+tb)y₁²,  v=(x₁,x₂,y₁,y₂),

so g∈B₂ exactly when a+tb≠0. For t=0,c=0, g∈B₂ exactly when ab≠0. Fix an element (t,a,b) of P with t≠0. Avoidance gives a=tb. If (0,a₀,b₀) is in the t-kernel, comparison with its sum with (t,a,b) gives a₀=tb₀, while kernel avoidance gives a₀b₀=0. Hence a₀=b₀=0. Projection onto t is injective and |P|≤q.

If the t-projection vanishes, P is an additive subgroup of symmetric 2×2 matrices whose nonzero members are rank one or nonsingular alternating. Two rank-one symmetric matrices with different image lines have invertible, nonalternating sum. Indeed their images make the sum invertible, while cancellation of diagonals would make the two matrices equal, because in characteristic two a rank-one symmetric 2×2 matrix is determined by its diagonal. Adding any nonzero alternating matrix s[[0,1],[1,0]] to a rank-one matrix has determinant s² and retains a nonzero diagonal, also forbidden. Thus P lies in one q-element rank-one image line or in the q-element alternating line. Again |P|≤q. This completes the bound without a maximal-subgroup classification or finite census.

## Suzuki-type outer inversions

Let m=2 and f≥3 be odd. On the connected algebraic group X=Sp₄ over the algebraic closure of F₂, take the Suzuki Steinberg endomorphism ρ₀ with ρ₀²=F_q. Its restriction α to T=X^(F_q) is the graph-field involution and X^(ρ₀)=Sz(q). Harper §2.2.2 and Proposition 2.6 give this model and fixed-group identification. The Suzuki order is q²(q²+1)(q−1), also stated in Bamberg–Popiel–Praeger, [*Point-primitive, line-transitive generalised quadrangles of holomorph type*](https://api.research-repository.uwa.edu.au/ws/portalfiles/portal/24880071/Bamberg_et_al._2017_Point_primitive_line_transitive_generalised_quadrangles_of_holomorph_type_.pdf), J. Group Theory 20 (2017), 269–287, Table 1 on p.280.

Every involution Aα in Tα satisfies Aρ₀(A)=1. Lang–Steinberg surjectivity, in the convention supplied by Harper's §2.2, gives A=Bρ₀(B)⁻¹ for B∈X. Thus

    1=Aρ₀(A)=Bρ₀²(B)⁻¹=B F_q(B)⁻¹,

so B∈T. Consequently all outside involutions are one T-class C, and its centralizer is Sz(q). The actual Λ equals C and |H|=|Sz(q)|, whose 2-part is q².

Apply the preceding Sylow bound first to a Sylow 2-subgroup of the fixed subgroup Sz(q). As q²>q, it contains some u∈B₂. Both α and αu are outside involutions in C, so u∈C² and the full T-class B₂ is contained in C². Apply the same bound to a Sylow 2-subgroup of H, also of order q². It meets B₂, contradicting H∩Λ²=1. This finishes the graph-field case and the theorem.

The exact-source independent reviews are recorded below. The elementary Sylow proof replaces a discarded provisional calculation that incorrectly called every t≠0,c=0 element nonalternating; the correct invariant is a+tb, and M=0 is alternating. No classification of arbitrary symplectic extensions or unrelated outer groups follows.


## Independent mathematical and source review



## Recorded source review scope

Automated source reviewers an automated checker, an automated checker and an automated checker independently accepted the complete symplectic theorem and the odd outer-order applications in the linked criterion source at exact revision the recorded source revision. They checked the actual field and Suzuki cosets, descent, the corrected elementary Sylow bound, its two uses, and the entire-group scope, conditional on the pinned folder/inner-exclusion and external group-theoretic inputs. All directly inspected Harper v2 Table 3 and the Suzuki/Shintani interface and the Bamberg–Popiel–Praeger outer/order statements; an automated checker and an automated checker also directly inspected the FGS involution class proof. None re-proved Lang–Steinberg, the automorphism/classification theorems, or aggregate C0007. These are independent model mathematical/source reviews, with no finite census or formal certification.
