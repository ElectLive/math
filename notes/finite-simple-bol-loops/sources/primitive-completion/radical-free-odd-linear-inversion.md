# Odd-dimensional linear canonical groups in characteristic two

Mira Cult
**Independently reviewed continuation of [0323:C0010](../../claims/0010.md).** Let q=2^f, f≥1, and n=2m+1≥3. No finite simple nonassociative left Bol loop has canonical left multiplication group T=PSL_n(q) for any canonical inverting automorphism τ. The outer argument covers graph, field, graph-field and all their diagonal twists; the inner argument below treats every selected union of involution classes. This does not address even-dimensional linear groups, odd characteristic, or other radical-free groups.

The canonical faithful-folder and inverting-automorphism inputs are [C0001](../../claims/0001.md), reviewed at its recorded source revision, and [C0007, Theorem 1.1(1)](../foundations/C0007.md), scoped at its recorded source revision as recorded in C0011. C0007 aggregate review metadata remains unreviewed. The standard decomposition of automorphisms into inner, diagonal, field and graph parts is stated by Steinberg, *Automorphisms of finite linear groups*, [Theorem 3.2, printed p. 608](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16023F257E0F21D57873B1450E9F15E4/S0008414X00010245a.pdf/automorphisms-of-finite-linear-groups.pdf), DOI `10.4153/CJM-1960-054-6`. The source statement was directly inspected by the author and coordinator; the complete classification proof was not independently reverified here. The following deduction has the independent exact-source reviews recorded below.

## Symmetric forms and common involution representatives

Every nondegenerate symmetric bilinear form B on an odd-dimensional F_q-space is congruent to I_n. Let ℓ(x)=sqrt(B(x,x)); in characteristic two ℓ is F_q-linear. Nondegeneracy gives a unique w with B(w,x)=ℓ(x). The form cannot be alternating in odd dimension, so w≠0. Also B(w,w)=ℓ(w)=sqrt(B(w,w)), hence B(w,w) is 0 or 1. If it were 0, the even-dimensional hyperplane w⊥=kerℓ would carry an alternating form with one-dimensional radical ⟨w⟩, impossible since alternating forms have even rank. Thus B(w,w)=1 and w⊥ is nondegenerate alternating. A symplectic basis makes the isometry type unique; I_n is one representative. In particular, if A is nonsingular symmetric with det A=1, then A=B^TB for B∈SL_n(q): first choose B∈GL_n(q), then det(B)²=1, and squaring is injective in F_q×.

Every involution in SL_n(q) is unipotent with Jordan blocks of sizes at most 2 and has rank r=rank(u−I), 1≤r≤m. Its GL_n(q)-conjugacy class is a single SL_n(q)-class: there is a size-one block, on which the GL centralizer has arbitrary determinant. Every involution in T has an involutory SL lift, since the scalar center has odd order and its square map is bijective.

For each r≤m, let V be the n×r matrix whose columns are e_{2i−1}+e_{2i}, 1≤i≤r. Then V^TV=0, N=VV^T is symmetric, rank r and N²=0. Hence

    u_r=I+VV^T                                               (1)

is a determinant-one involution of rank r, defined over F₂, symmetric and fixed by inverse transpose, every field automorphism, and their composition. The rank is r because V is injective and V^T is surjective. Thus every T-involution class contains a representative fixed by each standard outer involution considered below.

## One involution class in each pure outer coset

Write γ(A)=(A^T)⁻¹. In each case below, prove that involutions in the *one actual coset* αT form a single T-class. No equality of classes across different diagonal cosets is asserted.

**Graph α=γ.** If (γ[A])²=1, for A∈SL_n(q) one has γ(A)A=zI for a central scalar z; equivalently A=zA^T. Transposition gives z²=1 and hence z=1. The symmetric-form lemma gives A=B^TB with B∈SL_n(q). Thus γ[A] is T-conjugate to γ.

The remaining two types require q=s², s even, and σ(x)=x^s. Let Z be the odd-order scalar center of SL_n(q), with σ acting as an involution. On this odd abelian group, the norm c↦cσ(c) surjects onto Z^σ, and c↦c/σ(c) surjects onto the norm-one subgroup: decompose Z into its ± eigenspaces using the inverse of 2 modulo |Z|.

**Field α=σ.** If (σ[A])²=1, then σ(A)A=zI with z∈Z; comparing the two product orders after σ shows σ(z)=z. Centrally rescale A using the norm map to arrange σ(A)A=I. Matrix Hilbert 90 gives A=B⁻¹σ(B) for B∈GL_n(q). Here an elementary descent proof suffices: for a semilinear involution F on F_q^n, choose η with η+σ(η)=1. Every vector v equals x+ηy with fixed vectors y=v+F(v) and x=v+ηy. This is a direct sum over F_s, since η is not in F_s; a basis of the fixed space is therefore a basis over F_q. Applying this to F(v)=Aσ(v) gives the stated matrix form after inverting the fixed-basis matrix. As det A=1, det B∈F_s×. Multiplying B on the left by a matrix in GL_n(s) of inverse determinant leaves B⁻¹σ(B) unchanged and makes B∈SL_n(q). Hence σ[A] is T-conjugate to σ.

**Graph-field α=γσ.** If (α[A])²=1, then A=zσ(A)^T for z∈Z with zσ(z)=1. Centrally rescale A using c↦c/σ(c) so that A=σ(A)^T. Every nonsingular Hermitian form over F_{s²}/F_s is congruent to I: A=σ(B)^TB with B∈GL_n(q). This standard finite-field fact follows by orthogonalizing a vector of nonzero Hermitian norm and inducting; if all vectors had zero norm, a suitable scalar combination of two vectors with nonzero pairing would have nonzero norm. Norm-surjectivity then scales diagonal norms to 1. Since det A=1, det B has norm 1. Left multiplication by a diagonal unitary matrix of any chosen norm-one determinant adjusts B to SL_n(q), preserving σ(B)^TB. Hence α[A] is T-conjugate to α.

## Diagonal twists and the marked collision

The diagonal quotient D=PGL_n(q)/T has odd order gcd(n,q−1). Steinberg's decomposition shows that an outer involution has nontrivial image in the field/graph quotient: a purely diagonal involution would lie in the odd group D. Its field component has order at most 2. Choose the corresponding standard α among γ, σ, γσ above, and view τ=αx with x∈PGL_n(q). Its image δ in D satisfies δ+α(δ)=0. For any involution α of an odd abelian group, ker(1+α)=im(1−α), so conjugation by an element of PGL_n(q) sends τ into αT. The preceding single-class result then sends it to α by a further T-conjugation. This handles diagonal twists without identifying different T-cosets or assuming a full marked set.

It therefore suffices to consider τ=α. Each u_r in (1) is α-fixed, so αhat u_r is an outside involution. By the single-class result it is T-conjugate to αhat. Hence u_r=αhat(αhat u_r) lies in (αhat^T)². Since these representatives cover every involution class of T and the square is T-invariant, it contains **every** involution of T.

For a hypothetical canonical folder, use the formal E=T⋊⟨αhat⟩ and its actual marked set Λ=αhat K. The latter contains αhat^T and is a union of involution classes within αhat T. As that coset has just one such T-class, Λ=αhat^T. The folder condition H∩Λ²=1 therefore forces H to have odd order. But |Λ|=[T:C_T(α)] and |Λ|=[T:H], so |H|=|C_T(α)|. The nonidentity involution u₁ in (1) lies in C_T(α); hence this centralizer and H have even order. This contradiction proves the theorem.

This completes the outer case. The argument and its finite-field descent details have the scoped independent reviews below.

# The inner case

Independently reviewed C0010 deduction. Let T=PSL_n(q), n=2m+1≥3, q=2^f, and suppose a faithful generated canonical folder of a finite simple nonassociative Bol loop has G=T and inner inversion τ. Then no such folder exists, conditional on the repointing and Bruck-structure inputs of [radical-free-inner-inversion](../odd-completion/radical-free-inner-inversion.md), independently reviewed at its recorded source revision. Together with the preceding outer argument, this proves the all-inversion theorem; even n remains outside its scope.

If τ=id, the folder is exponent-two Bruck and the simple-group quotient contradicts the reviewed Bruck structure theorem, exactly as in that source. Otherwise τ=Int(a), a²=1, and c=a τhat is a central outside involution in the formal extension. Write Λ=cS, where S⊆{1}∪Inv(T) is a union of T-classes and contains a. If 1∈S, repoint at c; the reviewed repointing theorem preserves faithful generation, simplicity and nonassociativity and gives an exponent-two Bruck folder on the same G, again impossible. Hence S is a nonempty union of involution classes with no identity.

In characteristic 2 every involution in GL_n(q) has the form 1+M with M²=0; its class is determined by r=rank M, 1≤r≤m. Such elements lie in SL_n(q). The corresponding GL class is one SL class because n−2r≥1 and the GL centralizer contains arbitrary determinant on the one-block summand. Passage to PSL is injective on involutions because its scalar kernel has odd order. Write C_r for this T-class. The number of such matrices is

 |C_r| = [n choose r]_q [n−r choose r]_q |GL_r(q)|.       (1)

Choose image U of dimension r, kernel K of dimension n−r containing U, and an isomorphism V/K→U; this gives (1). Equivalently, with s=n−2r and a basis ordered by image, one-block summand, and complementary r-space, the centralizer consists of block matrices [[A,B,C],[0,D,E],[0,0,A]] with A∈GL_r(q), D∈GL_s(q) and B,C,E arbitrary of compatible sizes. Its order is q^{r²+2rs}|GL_r(q)||GL_s(q)|, which independently gives (1). The determinant map on this centralizer is surjective because s≥1, and the odd scalar quotient preserves the class count as explained above. As q is even, the Gaussian coefficients and the factors q^i−1 are odd, so

 v₂(|C_r|)=f·r(r−1)/2.                                   (2)

Let r be the least rank selected in S. The values (2) strictly increase for positive r≥1, so the sum |Λ|=|S| has 2-part q^{r(r−1)/2}; there is no cancellation with other selected classes. Since |K|=[T:H] and |T|₂=q^{n(n−1)/2}, a Sylow 2-subgroup Q of H embeds, after conjugation of H and the collision test together in T, into the standard upper-unitriangular Sylow U with

 [U:Q]=q^{r(r−1)/2}.                                     (3)

Let X be the elementary abelian rectangle of matrices 1+[0 M;0 0], M∈Mat_{r×(n−r)}(F_q), relative to the first r and last n−r coordinates. Its order is q^{r(n−r)}, strictly greater than (3), so X∩Q contains a nonidentity element. Such an element has rank j with 1≤j≤r. The following matrix fact makes it an element of C_r², a contradiction to H∩Λ²=1 because C_r⊆S and Λ²=S².

**Matrix fact.** For every 1≤j≤r and q even, any rank-j r×(n−r) matrix N is a sum M+M′ of two rank-r matrices. Reduce N by row and column bases to [diag(I_j,0)|0]. If q>2, choose M=[A|0] with A diagonal, entries α∉{0,1} on the first j positions and 1 thereafter. Then M′=M+N also has rank r. For q=2 and j even, use j/2 diagonal blocks [[0,1],[1,1]] on the first j positions of A and identity elsewhere; both A and A+diag(I_j,0) are invertible. For q=2 and j odd, use those blocks on j−1 positions, a zero singleton in position j, identity on the rest, and take the additional column e_j. The resulting M=[A|e_j] has full row rank, while M+N already has invertible first r columns. The additional column is available because n−r≥r+1. Undoing the basis changes proves the assertion. The two rectangular involutions commute, and their product is 1+N.

All calculations occur in the original folder, with no quotient-folder assumption. The proof and the finite-field matrix fact have the independent exact-source reviews below; the Bruck-structure and repointing inputs retain their reviewed scope and primary-source qualifications. For n odd and q even the central scalar quotient has odd order, as used in the 2-part calculation.

## Source verification and limitations

automated reviewers `review_s5_h3`, `review_hs_full` and `review_presentations` independently accepted both outer and inner arguments at its recorded source revision, conditional on the cited canonical-folder, repointing, Bruck-structure and Steinberg automorphism inputs. All three checked central rescaling, field/Hermitian descent and determinant normalization, diagonal twisting, involution-rank class coverage, the selected minimum-rank 2-valuation and Sylow intersection, including the q=2 matrix construction. They performed no fresh primary-source audit or computational certification. These independent model reviews cover odd n≥3 and q=2^f only, and do not assert an exclusion of arbitrary semisimple canonical groups.

<a id="even-dimensional-continuation"></a>
## Even-dimensional continuation

**Independently reviewed extension of [0323:C0010](../../claims/0010.md).** Let n=2m≥4 and q=2^f. Under the same canonical-folder, repointing, Bruck-structure and Steinberg inputs as above, no finite simple nonassociative left Bol loop has canonical left multiplication group T=PSL_n(q), for any canonical inverting automorphism τ. The review record immediately above applies only to the earlier odd-dimensional source; this continuation has its own exact-source record below. Together with that source and the n=2 simple cases in [radical-free-inner-inversion](../odd-completion/radical-free-inner-inversion.md), this gives the exclusion of all simple canonical groups PSL_n(2^f), n≥2; the n=2 exclusions retain their own source and review scope.

### Inner τ

The proof in the preceding inner section applies with these two changes. For an involution of maximal rank r=m, its GL centralizer has determinant (det A)² on the two equal Jordan-block multiplicity spaces. Since q is even, squaring permutes F_q^×, so its GL class is still one SL class. The rank-class cardinality, minimum-rank 2-valuation, rectangle and Sylow-intersection arguments are unchanged.

For the matrix fact at q=2, retain the preceding extra-column construction when r=1: n≥4 supplies that column. For r≥2 and even j use the preceding 2×2 blocks. For odd j<r use those blocks on j−1 positions, a swap block on one selected and one unselected diagonal position, and identity elsewhere. For odd j=r≥3 use a 3×3 companion matrix of x³+x+1 and the preceding 2×2 blocks on the remaining positions; neither 0 nor 1 is a root, so both the chosen matrix and its sum with I are invertible. These are square r×r constructions and remain valid when there are extra columns. Thus the same selected-class collision proves the inner case, including the identity-τ and repointing cases under the cited inputs.

### Field and graph-field τ

The field and graph-field descent and odd scalar-center normalization above do not depend on n being odd. When f is even they show that each actual standard field or graph-field coset contains one T-class of involutions, with diagonal twists reduced to that coset by the odd-order diagonal quotient. For each rank 1≤r≤m, the matrix u_r=I+VVᵀ from (1) is defined over F₂ and fixed by both automorphisms. At maximal rank, the determinant correction just proved shows its GL class remains one SL class. Hence every T-involution class meets the square of the selected outside class. The folder condition makes H odd, whereas |H| is the even centralizer order because u₁ centralizes τ. This excludes both types.

### Pure graph τ

Write γ(A)=(Aᵀ)⁻¹. Symmetric nonsingular forms in dimension 2m over F_q have exactly two congruence types, alternating and nonalternating. For the latter, define w by b(v,v)=b(v,w)². Then w≠0 and b(w,w)=0: otherwise w⊥ would be a nondegenerate alternating odd-dimensional space. Choose e with b(e,w)=1 and let U=(Fw+Fe)⊥. The restriction to U is nondegenerate alternating. In particular all nonalternating forms are congruent. Their orthogonal group fixes w and induces Sp(U) on w⊥/Fw. Every isometry is uniquely described by S∈Sp(U), u∈U and c∈F_q through

    g(w)=w,  g(v)=Sv+b(Sv,u)w (v∈U),  g(e)=e+u+cw.

Consequently its order is h=q^{2m−1}|Sp_{2m−2}(q)|. The alternating stabilizer has order |Sp_{2m}(q)|=h(q^{2m}−1). Both centralizers have 2-part q^{m²}. Congruence between determinant-one forms is achievable in SL, since the determinant of a GL congruence has square 1. The scalar center has odd order: if an element centralizes the projective graph involution, central rescaling by the unique square root in that center gives an actual form isometry. Thus these are also the two centralizer orders in T. The odd-order diagonal quotient reduces diagonal twists of graph involutions to these two classes, without identifying them.

Let C_N and C_A be the nonalternating and alternating outside classes, respectively. The square C_N² contains every involution class of T. For r<m use u_r above, whose symmetric form has an unchanged diagonal entry. For r=m use u=I+VCVᵀ with V as above and C an invertible symmetric m×m matrix with a zero diagonal entry: take C alternating if m is even, or C=H₂⊕I_{m−2} if m is odd. Then u is an involution of rank m, γ(u)=u, and its symmetric matrix is nonalternating. Hence γ and γu are in C_N, giving u∈C_N². If Λ=C_N, the collision condition forces H odd, but |H|=h is even.

It remains to exclude any actual selected set Λ containing C_A; it may be C_A alone or the union of both classes. In the first case |H|=|Sp_{2m}(q)|, and in the second class counting gives |H|=|Sp_{2m}(q)|/q^{2m}. Pick an odd prime r dividing q+1. It divides neither q−1 nor the odd scalar center. In the order of SL_{2m}(q), the factors divisible by r are precisely q^j−1 for even j, exactly those in |Sp_{2m}(q)|. Thus in either case |H|_r=|T|_r, so H contains a Sylow r-subgroup of T.

Choose an order-r element a in a nonsplit torus of SL₂(q). On a 4-space put J₄=[[0,I₂],[I₂,0]] and u₄=diag(a,aᵀ), and extend J₄ by a nonsingular alternating form and u₄ by the identity. For α=Int(J)γ, we have α(u)=u⁻¹, while Ju is nonsingular alternating. The determinant-one congruence argument shows αu∈C_A, so u=α(αu)∈C_A²⊆Λ². Its image in T has order r. Sylow conjugacy places a T-conjugate of u in H, contradicting H∩Λ²=1. This proves the even-dimensional outer case; no assumption that Λ is the full set of outside involutions was used.

### Independent review of the even-dimensional continuation

automated reviewers `review_s5_h3`, `review_hs_full` and `review_presentations` independently accepted the even-dimensional section at its recorded source revision, conditional on the cited canonical-folder, repointing, Bruck-structure and automorphism inputs and separately reviewed odd-dimensional source. All checked the maximal-rank determinant correction, q=2 matrix repairs, field descent, the two symmetric-form centralizers, and the original selected-class collisions. In particular they verified the full odd-prime Sylow argument for either selection containing the alternating class, including the explicit four-dimensional element. None performed a fresh primary-source audit or computational certification. Together with the separately reviewed odd-dimensional and n=2 cases, the result excludes all nonabelian simple PSL_n(2^f) as the entire canonical group; it does not exclude their occurrence as factors of larger groups.
