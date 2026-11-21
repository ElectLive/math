# Distinct Frobenius graphs give simple odd Bol loops at the same two-prime degree

**Research proof; see the scope of verification.** [Verification and provenance](../VERIFICATION.md). Let p,q be distinct odd primes, p|(q−1), f=ord_q(p) even, p∤f, and d=pf. Write u for the largest odd divisor of f. At the actual degree p^(d+1)q there are at least
```math
                  2+\frac{f-u-1}{2}
```
pairwise **nonisotopic** finite simple proper left Bol loops. The first two are the [split abelian-core construction, source 2625d36b](two-prime-divisibility-existence.md) and the [separately audited duplicated-weight extraspecial construction](../../extraspecial-cores/extraspecial-odd-bol-construction.md). The remaining lower bound is supplied here by new genuine extraspecial constructions in which the projected native stabilizer Lagrangian is *not* stable under the entire two-axis group. No classification or completeness assertion for the count.

For p=3,q=61, f=10, this gives at least four at 3³¹·61. For p=3,q=193, f=16, it gives at least nine at 3⁴⁹·193. For the optional interpretation of these orders as the **first possible for their fixed prime pair**, the separate first-exponent necessity theorem has its own provisional review status [here](all-core-prime-pair-minimum.md). Neither that necessity theorem nor its nonabelian-core residual is required to build the new loops or to distinguish them; adding the two benchmark classes to the numerical lower bound uses their named construction inputs, with separate review histories. We do not infer infinitude of suitable pairs with unbounded f from Dirichlet or a conjecture about primitive roots.

## A nonscalar, anti-isometric graph

Fix α∈F_q of order p, k=F_(p^f), ζ∈k of order q, σ₀ the involution of k, x↦x^(p^(f/2)). Take 0≠c∈k with c^σ₀=−c. For an index i mod f write φ(x)=x^(p^i) and h₀=f/gcd(f,i) for its order. Our admissible indices have **odd h₀>1 or 4|h₀**. In particular h₀>2. Choose η∈k^× with
```math
                \eta\eta^{\sigma_0}=-c^\varphi/c ,
```
which is possible: the right side belongs to the fixed subfield, and the finite-field norm onto it is surjective.

On A=k^(Z/p) use the nondegenerate alternating trace form
```math
              g(x,y)=\sum_j\operatorname{Tr}_{k/\mathbb F_p}
                     (c x_j y_j^{\sigma_0}).
```
On U=A⊕A take the **orthogonal** sum ω=g⊕g rather than two mutually paired coordinate Lagrangians. Let P=⟨h⟩ of order p and V=F_q², X=V⋊P with h acting by (α,α⁻¹). A sign τ exchanges the two axes of V, inverts h and swaps the two copies of A. On the first A, (a,b) acts at j by multiplication by ζ to the power
```math
                       p^i\alpha^j a+\alpha^{-j}b ,
```
and h is the forward shift (Rx)_j=x_(j+1). On the second swap a,b and replace R by R⁻¹. This is a true action: shifting the weight by one gives exactly (α,α⁻¹), and τ implements the displayed signed action. The form is invariant because each ζ-power has σ₀-norm one and the sites are permuted. It is faithful on X: a nontrivial top shifts the sites, and a vector in V annihilated by every first-coordinate weight is zero using j=0,1 and α≠α⁻¹. Every nonidentity element on either pure axis is fixed-point-free on U.

Let T:A→A be (Tx)_j=η(x_(−j))^φ. The subgroup J=V₂⋊P, V₂=0×F_q, preserves the graph L={(x,Tx)}: the exponent p^i α^j in the second V₂-action is exactly the φ-translate of the first at −j, and site reversal interchanges the shifts. By trace invariance and the norm equation, g(Tx,Ty)=−g(x,y), so L is Lagrangian, as is τL. They are complementary exactly when 1−T² is invertible.

Here is the exact norm check. Put k₁=k^φ, n=Norm_(k/k₁)(η). At each site T² multiplies φ²(x) by ηη^φ. A nonzero fixed point exists precisely when the φ²-norm of this scalar is 1, by cyclicity of finite-field units (equivalently the elementary multiplicative Hilbert 90). For h₀ odd the norm is n², while n n^σ₀=Norm_φ(−c^φ/c)=−1. So n cannot be ±1. For h₀ even we have φ^(h₀/2)=σ₀. The φ²-norm of ηη^φ then equals n, and
```math
 n=\prod_{j=0}^{h_0/2-1}(\eta\eta^{\sigma_0})^{\varphi^j}
   =(-1)^{h_0/2}c^{\varphi^{h_0/2}}/c=(-1)^{h_0/2+1}.
```
This is different from one exactly when 4|h₀. Thus the claimed L⊕τL=U holds for **all** admitted index choices and all η solving the norm equation. When h₀≡2 mod 4 the same ansatz actually has an intersection, not a further example.

## Native folder, all two-mark phases, normal cuts

Take the extraspecial Heisenberg group N=U×F_p with (x,s)(y,t)=(x+y,s+t+ω(x,y)/2); write z for its unit central generator. Let D=N⋊X with the indicated sign acting trivially on the center. Set
```math
 H=(L\times\{0\})\rtimes\langle V_2,z h\rangle.
```
This notation is an internal subgroup product: J normalizes the horizontal L lift, z is central and zh has order p. Its intersection with N is L×{0}. Let K be the entire set of elements of D inverted by τ; Kτ is the outside involution class, K² its product square (conjugacy invariant). Counts are
```math
   |K|=[D:C_D(\tau)]=p^{d+1}q=[D:H].
```
The generating subgroup ⟨K⟩ is normal in D (it is the even part of the normal subgroup generated by the outside involution class). Its projection contains h and the anti-diagonal in V, hence generates X. On N/Φ(N)=U the commutators with this subgroup span at least [U,V]=U, hence ⟨K⟩ contains N by Frattini. Its action on D/H is faithful: a normal subgroup disjoint from N centralizes N, but C_D(N)⊆N since the X-action on U is faithful and inner automorphisms of N act trivially there. Every nontrivial normal subgroup inside N meets its one-dimensional center; the center meets H trivially.

It remains to exclude *all* physical two-sign products in H. Above any projected involution s∈Xτ the actual involutions are (x,0)s, x∈E_s=ker(1+s), by squaring. For projected signs a,b, the two vector terms in the product live in E_a and E_(aba), giving half their symplectic pairing as central phase. Classify the possible projected product inside J:
* A nontrivial pure V₂ element cannot be inverted by an outside involution, since every such sign interchanges the distinct axes.
* For projected identity the two signs coincide. Every sign is V₂-conjugate to h^k τ: its translation part is in im(1−h^kτ) on V and this line is already the image of V₂. Conjugate by V₂, preserving H. The sign now exchanges L and M=τL since h stabilizes each, so its negative eigenspace meets L trivially. A sum in L must therefore be zero; opposite summands have zero central phase.
* For nontrivial top part, V₂-conjugate the projected product to h^j, j≠0 (the scalar on V₂ is fixed-point-free), again preserving the full physical H. Both projected signs must invert h^j, so neither has any V-translation part, by fixed-point-freeness on V. Thus a and a b a exchange L and M. If their two negative summands total an L-vector, they have the form (ay−y) and (−(aba)y+y) with y∈M: project to M and use L⊕M. Their pairing is zero, since L and M are isotropic and ω(sy,y)=0 for every symplectic involution s (alternation plus invariance). The true central phase is therefore zero whereas each H-element above h^j has nonzero central phase j. This includes both signs separately, not just the fiber over τ.

In particular the marked set is sharply transitive on D/H and sandwich closure gives a genuine left Bol loop with D its actual LMlt. This argument **does not** require V₁ to preserve L, or every unnormalized outside involution to exchange L with the same M. Conjugating within the actual stabilizer is the key difference from the earlier duplicate-character family.

For simplicity use the [independently reviewed odd signed full-mark strict normal-cut criterion](../../packet/manuscripts/odd-folder-radicals.md#candidate-simplicity-criterion-using-τ-stable-normal-subgroups) at 65a3e58df517df59656ab948ac9d122208f62c4a. Every proper nontrivial τ-stable normal I≤N contains z, and so I is the complete preimage of a τ-stable subspace Y≤U. The actual orbit size [I:I∩H] has exponent 1+dim Y−dim(Y∩L); its inverted-mark size [I:C_I(τ)] has exponent dim Y⁻. The first is strictly larger, since projection of Y∩L on Y⁺ is injective by L∩U⁻=0. If a τ-stable normal I has nontrivial image in X then that image contains V: the distinct reciprocal axes are permuted by τ, and any nonzero top acts fixed-point-freely on V. Thus [N,I] maps onto U by [U,V]=U, giving N≤I. The only remaining proper possibility is I=NV. There the orbit and mark sizes are p^(d+1)q and p^d q, still strict. This proves simplicity. H≠1 gives nonassociativity; finite odd Moufang loops are solvable, so the loop is proper.

## Distinguishing the actual isotope classes

The p-core N is characteristic in the genuine LMlt (O_p(X)=1 since V is self-centralizing there). The elementary V is likewise characteristic in X= D/N (it is O_q(X)). For two such models, any loop isotopy induces an isomorphism of signed groups sending the point stabilizer to a conjugate. Indeed an isotope takes its mark set to γ K a⁻¹γ⁻¹ for a∈K; sandwich closure gives K a⁻¹=a^(1/2)K a^(−1/2). After this conjugation the generating marks determine the sign by inversion. One must allow changes of base point, but these only conjugate H. The distinguished V₂ line in X is (HN/N)∩V, unchanged by conjugation in X and sent to the analogous line. The signed isomorphism then preserves also V₁=τV₂, and, because it commutes with the sign exchanging the axes, the induced scaling on the axes is **the same**. Comparing the spectral supports below is therefore an invariant of the native isotope class.

Over a splitting field, write a V-character as an ordered pair in F_q². Normalize the common V₂-coordinate support to S=⟨p,α⟩≤F_q^×, of order pf because p∤f. The factorization r=p^k α^j in S is unique (mod f,p), and ξ(r)=p^k α^(−j) is an automorphism. The two blocks of U give precisely the two distinct graphs
```math
        \{(p^i\xi(r),r):r\in S\},\qquad
        \{(p^{-i}\xi(r),r):r\in S\}.
```
Indeed the first is obtained by taking field conjugates of the actual site weights; the second transposes the first. Each character has multiplicity one. In pairwise comparison the common scaling δ must preserve S, hence δ∈S; it multiplies the graph constants by δ/ξ(δ)∈⟨α⟩ and cannot change their Frobenius exponents modulo f. Thus indices not equivalent by i↦−i give **nonisotopic** loops. The duplicated-weight extraspecial construction has just one graph with character multiplicity two at this same degree, and the standard split construction has abelian p-core; neither can be one of the new classes.

The graph L is genuinely not X-invariant. Were it invariant then its T would intertwine both V-axis actions. On the first V₁-action at −j, applying φ multiplies the exponent by p^i a second time; to match the second-block V₁-action at j would require p^(2i)=1 mod q. This is exactly h₀≤2, already excluded. Finally, in the cyclic group of f indices there are u elements whose order has 2-part exactly 2 (one order-two 2-primary component and any odd component), and one of order one. The remaining f−u−1 have h₀ odd >1 or divisible by four and pair freely under ±. This proves the advertised bound.

The [author checker](../code/verify_frobenius_graph_extraspecial.py) constructs actual finite fields and trace forms. At q=61 it tests the bad i=1 rank, both good i=2,4 tilts, all actual 183 projected outside involutions, all 33,489 pairs per tilt and all 549 potentially physical stabilizer-phase systems in genuine native coordinates, not merely after rechoosing an L-preserving complement. At q=193 it checks three genuine 96-dimensional transverse models with Frobenius orders 16,8,4. [Frozen stdout](../evidence/frobenius-graph-extraspecial.out). It does not enumerate the enormous full native loops or replace the all-parameter proof. No historical-priority assertion.
