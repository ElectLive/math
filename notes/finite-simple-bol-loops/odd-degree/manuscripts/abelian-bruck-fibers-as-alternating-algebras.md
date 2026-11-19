# Every finite odd Bol loop with abelian Bruck associate, as an alternating algebra

**Mira Cult**

All Bol loops are **left** Bol. The class in the title is intrinsic and includes nonassociative, centerless, non-prime-exponent and mixed-order loops. This is not a classification of every Bol loop of prime-power degree.

## An explicit, reversible normal form

Take a finite abelian group A of odd order and a biadditive alternating operation b:A×A→A. Write J=⟨b(A,A)⟩ and B_x(y)=b(x,y). The exact conditions are

```math
b(J,J)=0,qquad I-B_x\text{ is invertible on }J\quad(x\in A).
 \tag{1}
```

The second condition is equivalent on A itself since B_x maps to J. Define the actual table by

```math
x*y=x+y+(I-B_{x+y})^{-1}b(x,y).                          \tag{2}
```

These and only these are the desired multiplications, **on the given labeled A with precisely its given addition as the Bruck associate**. In particular every such labeled table has just one b. Using composition of permutations right-to-left and [g,h]=g⁻¹h⁻¹gh, its intrinsic inverse is

```math
b(x,y)=\tfrac12\,[L_x,L_y](0),                \tag{3}
```

where the half is taken in A. This is a bilinear algebra; **no Jacobi identity is required**.

Proof. We use the known [Kinyon–Nagy–Vojtěchovský Proposition 5.3](https://arxiv.org/pdf/1611.05785) in the opposite convention: if the associate is associative (hence abelian), the actual D=LMlt(Q) has class at most two. It has odd order by [Foguel–Kinyon–Phillips Theorem 6.7](https://arxiv.org/pdf/math/0208231v2). For any such group, the addition g⊞h=gh[g,h]^(−1/2) is commutative and associative by centrality and bilinearity of commutators; it equals (g h² g)^(1/2) by the class-two square formula. The group commutator is biadditive for ⊞. Thus the actual mark map x↦L_x embeds (A,+) in (D,⊞). Here we used the fundamental odd twisted-set product ([FKP Definition 4.4, §5](https://arxiv.org/pdf/math/0208231v2)). Conversely every odd left Bol loop with D of class ≤2 has abelian Bruck associate, by the same calculation on its marks.

Use W=A⊕Λ²A as a two-step group with product (x,u)(y,v)=(x+y,u+v+(x∧y)/2) and marks k_x=(x,0). Here the exterior product is over ℤ; halves exist on all these finite odd groups. Because of the preceding identities there is a surjection W→D given by (x,u)↦L_x h(u), where h(x∧y)=[L_x,L_y]. In W every conjugate of k_x differs by phase in x∧A; more precisely K⁻¹K over x is exactly x∧A in the second coordinate, since k_t⁻¹k_(t+x) has phase −t∧x/2. This set is conjugacy invariant. Pulling the native point stabilizer back gives H≤W of index |A| avoiding K⁻¹K except at 1. Conversely every such H gives K sharply transitive on W/H, since the same avoidance holds at all conjugates of H. K is inverse- and sandwich-closed, hence yields left Bol multiplication by its action; k_x k_y² k_x=k_(2x+2y) recovers addition as the Bruck table.

Write K₀=H∩Λ²A, C=Λ²A/K₀, J=pr_A(H), β(x,y)=x∧y mod K₀. The index gives |J|=|C|. In W/K₀, the subgroup H/K₀ has trivial intersection with C, so is a graph over J. Its commutators force β(J,J)=0; therefore the graph is that of an additive homomorphism φ:J→C. Above nonzero j, avoidance says φ(j)∉β(j,A); hence φ is injective, thus bijective. Identify C with J using φ and put b=−φ⁻¹β/2. By surjectivity of the exterior map onto its additively generated image, J=⟨b(A,A)⟩. The avoidance statement is exactly (1), since b(j,A) is a subgroup, scalar factors of 2 do not affect it, and b alternates. Conversely for any data (1), the resulting W/K₀ is

```math
D_0=A\oplus J,\qquad (x,u)(y,v)=(x+y,u+v-b(x,y)),
 \qquad H_0=\{(j,j):j\in J\};
```

it has the necessary index and avoidance. To compute a native product write k_x k_y=k_z(j,j). Then j=x+y−z and −b(x,y)=(I-B_(x+y))j. This gives (2). A pure central phase (0,c) sends 0 to −c, so evaluating [k_x,k_y]=(0,−2b(x,y)) proves (3), even if the representation has a nontrivial kernel. No multiplication coincidence or sign convention is hidden by passage to an abstract group.

## Intrinsic algebra, normal structure and nuclei

The correspondence includes all homomorphisms: a native homomorphism preserves the Bruck term (it respects roots by uniqueness in odd finite loops) and preserves (3) by respecting inverse left translations. Conversely a bracket-preserving homomorphism of abelian groups preserves (2): apply it to the defining linear equation and use uniqueness of the solution. Thus isomorphism is ordinary isomorphism of the alternating algebras, and transports on fixed A are exactly Aut(A). Subloops are precisely additive subgroups U with b(U,U)≤U, since (2) restricts on U by injectivity and finiteness, while + and (3) restrict intrinsically. Normal subloops are precisely the ideals b(A,U)≤U: necessity from the quotient homomorphism and intrinsic terms, sufficiency since (1) passes to the quotient (I−B_x bijects U). In particular the abelian derived subloop is exactly J, not just contained in J: an abelian native quotient has its own native law as associate and bracket zero; conversely (2) modulo J is addition. J itself is an abelian group under the native product, so the class is metabelian.

Let Z₀={x:b(x,A)=0}, J₀=J∩Z₀. The commutant and center of Q both equal Z₀: commutation in (2) means b(x,y)=0 since 2 is invertible, and adding any element of Z₀ is central and associative by (2). The genuine group D has the presentation D₀/diag(J₀), precisely: conjugating (j,j) changes its phase by a multiple of b(j,a); no nonzero pure phase belongs to H₀, so diag(J₀) is exactly its action kernel. The normalizer of H₀ in D₀ consists of the (x,u) for which b(x,J)=0. Because the right nucleus consists exactly of the points fixed by the entire stabilizer (equivalently the normalizer orbit), this gives

```math
N_r(Q)=\{x:b(x,J)=0\},\qquad
 N_\ell(Q)=N_m(Q)=\{x:b(x,A)\le J_0\}.
```

Indeed (x,0) normalizes precisely as asserted, orbits being points on the mark labels. For the last equality x is left nuclear iff the residual (j,j) in k_xk_y=k_(x*y)(j,j) is in the physical core for every y. By the resolvent this is equivalent to b(x,y)∈J₀, independent of reversing the two arguments. On N_r the actual product simplifies to x+y+b(x,y), the associated two-step group law; this conclusion uses b(x,J)=b(y,J)=0, not a claim that the right nucleus of all finite Bol loops is two-step. The nuclear right translations in the actual LMlt are precisely those with labels in Z₀+J: they coincide with central permutations of D, and a pair (x,u) is central modulo diag J₀ exactly when x∈Z₀. Their value at 0 is x−u for such x (since b(x,u)=0 and b(u,u)=0). The two projections of the concrete marked double of D have kernel isomorphic to J₀: in D₀ the sign (x,u)↦(−x,u) carries diag J₀ to the opposite graph, with trivial intersection by oddness. Mapping D₀ into D×D by these two actions is injective and hits the native double because its marks generate D₀. This also illustrates how a true core need not be a subgroup of the central pure phases.

## Exact count at each odd prime cube in this fiber class

At order p³, counting over **all abelian associate types**, the class has precisely the five groups and (p+1)/2 further ordinary isomorphism classes. All the latter are centerless exponent-p proper Bol loops, with native N_r=Q′ of order p² and trivial N_ℓ=N_m. They constitute a **single entire isotopy class**, not just a linked subset.

For A=F_p³ write j=dim J. If j=0 there is only the additive group; j=3 contradicts b(J,J)=0. If j=1, any nonzero b(J,A) would fill J under fixing a generator on the J side, contradicting avoidance. Hence J⊆Z₀, and b is a nonzero alternating form on the two-dimensional quotient with values on the line J. All such algebras are isomorphic, giving the nonabelian group of exponent p. If j=2, choose a complement vector e and J as two-space. The entire law is described by b(e,v)=Fv. Since b has image generating J, F is invertible; (1) says that F has no eigenvalue in F_p (test all multiples of e). Conversely every such F works. The intrinsic J must be preserved by every isomorphism. Changing e by an element of J has no effect; scaling e and changing basis on J give exactly scalar and conjugacy equivalence on F. Its irreducible quadratic realizes multiplication by u∈F_(p²)∖F_p, unique modulo Frobenius. After scalar equivalence these are the nonidentity elements in the cyclic group of order p+1 modulo inversion, giving (p+1)/2. Formulae above give the stated nuclei and absence of center. The loops are nonassociative and not Moufang, for example their left and right nuclei differ (in a Moufang loop the nuclei coincide).

For A=C_(p²)×C_p the exterior square has order p, so J is zero or cyclic of order p. In the nonzero case, as before J⊆Z₀. The radical of a nonzero alternating pairing through Λ²A is pA (reduce to the nondegenerate area form on A/pA), hence J=pA. Scaling the order-p generator shows a single orbit. This is the nonabelian group of exponent p²; for cyclic A the bracket is zero. These are precisely the five group possibilities, distinguished directly by exponent and commutation.

For isotopy, conjugating H₀ by k_(s e) gives an actual base-point change with projected graph j↦(I−2sF)j, by the central commutator formula. Explicitly for any base point r, β(x)=k_x(r) is bijective and the new law satisfies β(x*ᵣy)=x*β(y), an actual isotopy. Thus F becomes (I−2sF)⁻¹F, or F⁻¹ becomes F⁻¹−2sI. Combining with scalar equivalence permits all affine changes u⁻¹↦a u⁻¹+b (a∈F_p^×, b∈F_p), which are transitive on F_(p²)∖F_p since {1,u⁻¹} is a basis. No other loops are in that isotopy class: under any loop isotopy its mark set becomes γ K a⁻¹γ⁻¹ for some a∈K (use the identity translation); ⟨K a⁻¹⟩=⟨K⟩. Moreover a⁻¹/² K a⁻¹/²=K by sandwich closure, so K a⁻¹ is a conjugate of K. This proves the isotope remains left Bol with isomorphic physical LMlt. Its associate is again abelian by the class-two criterion, and its translation group has order p⁵ whereas a group of this degree has only p³ left translations. These exhaust the nonassociative class.

**Literature and checks.** The class-two implication is already [KNV Proposition 5.3](https://arxiv.org/pdf/1611.05785), not ours. Compare Nagy's nilpotent matrix constructions, [dissertation §6.4](https://real-d.mtak.hu/722/7/NagyGaborPeter_doktori_mu.pdf), the early centerless order-27 examples of [Foguel–Kinyon](https://arxiv.org/pdf/0910.2429), and the full order-27 classification of [Grishkov–Kinyon–Vojtěchovský, Table 1 and Theorem 5.3](https://arxiv.org/pdf/2504.14646). At 27 our two nonassociative classes are the opposites of their B9,B10 (the two trivial-center loops); we do not claim their discovery. The result of this note alone is not the full classification at p³, nor the enumeration of its centrally nilpotent branch. The [author checker](../code/verify_abelian_bruck_algebra.py) tries every one of the 19,683 ternary three-space brackets, transports them by actual GL₃ generators, tests all rank-two matrices up through p=13 in the displayed prime list, and tests literal addition recovery, commutators, isotopies, all Bol triples for every elliptic representative at p=3,5, and non-Jacobi and unequal-exponent examples. [Frozen output](../evidence/abelian-bruck-algebra.out). No formal validation or historical-priority claim.

[Proof checks and replay](../verification.md) · [Overview](../README.md)
