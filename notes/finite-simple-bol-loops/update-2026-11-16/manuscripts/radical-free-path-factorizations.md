# Connected-path factorizations with many simple socle factors

**Scoped construction for 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** Let T be a finite nonabelian simple group with an exact factorization T=AB, where A,B>1. For every k≥1 the construction below gives a finite simple proper non-Bruck left Bol loop of order |T|^k whose canonical left multiplication group is T^{2k}, with 2k minimal normal simple factors in k pairs exchanged by its canonical inversion. In particular, the known A₅=A₄·C₅ factorization yields examples of order 60^k for every k≥1. This is a uniform construction, not a classification of radical-free envelopes or a claim of literature novelty.

The faithful-folder, exact normal-subloop criterion and Moufang primitivity obstruction used below are [C0001](../proofs/C0001.md), reviewed at `9431ade99316d6bc62efb389492fef385b510b45`. The canonical inversion construction is [C0007, Theorem 1.1(1)](../proofs/C0007.md), scoped in C0011's review record at `932ead5db5f39045e2085caa6b062f6b981b2813`; the aggregate C0007 review metadata remains unreviewed. The [Bruck-stabilizer criterion](exact-factorization-criterion.md#bruck-stabilizers-and-necessary-witness-tests) is reviewed at `d9bc55095490d42e41c359bbb88b67c78f6d4998`. The exact-factorization family is the established baseline of C0002; the proof here verifies its particular inputs and simplicity without assuming its general construction is exhaustive. Independent exact-source reviews are recorded below.

## Factorization from a path

Fix k≥1 and label the k edges of a path by 1,…,k. Two-color the k+1 vertices. Attach A to one endpoint, B to the other, and a full copy of T to each internal vertex. Put N=T^k. For each vertex place its assigned group diagonally in the incident edge coordinates of N. Same-colored vertices have disjoint incident edge sets, so their vertex subgroups form an internal direct product. Denote the products for the two colors by L,R≤N.

Then L∩R=1: equality of a left-color and right-color edge assignment propagates a single common element along the connected path, which must lie in A∩B. There are k−1 internal vertices, so

    |L||R|=|T|^{k−1}|A||B|=|T|^k=|N|.

Therefore N=LR is an exact factorization. Neither L nor R contains a full coordinate factor of N: an endpoint group is proper in T, while an internal T is diagonal on two incident coordinates. Also L,R>1, hence L,R<N.

## The canonical folder

Let G=N_L×N_R, with τ exchanging its two copies of N. Set

    H=L_L×R_R,       K={(x,x⁻¹):x∈N}.                      (1)

Use a formal external involution t inducing τ and put Λ=tK. Every involution in tG has the form t(x,x⁻¹), and all are G-conjugate to t; hence Λ is the full outside involution class for this specific envelope. Products of two marked involutions are precisely the pairs (u,v)∈N_L×N_R with v N-conjugate to u⁻¹.

An exact factorization has L∩R^g=1 for every g∈N: write g=rℓ with r∈R, ℓ∈L, and conjugate L∩R^g by ℓ. Therefore H∩Λ²=1. Since |H|=|N|=|K|=[G:H], K is a transversal to H and all its conjugates. It is inverse-closed and sandwich-closed. The group N is perfect, so K generates G: products of anti-diagonal elements and their inverses generate N′×1 and 1×N′, as well as K. Every normal subgroup of the direct product of nonabelian simple coordinate factors is a product of such factors; no coordinate factor lies in H, so Core_G(H)=1. By C0001 this is a faithful generated Bol folder, and G is the canonical left multiplication group. Its canonical inverting automorphism is the displayed swap by uniqueness.

## Every normal quotient and simplicity

A normal quotient of G is specified by the retained coordinate sets I,J⊆{1,…,k} in N_L,N_R. Its K-image has size |T|^{|I∪J|}. Call a path vertex *active* when at least one of its incident half-edges is retained. Make a graph on the active vertices by keeping an edge exactly when both its half-edges are retained. This is a forest. Let c be its number of components, and let e_A,e_B∈{0,1} indicate whether the endpoints carrying A and B are active.

A vertex subgroup projects injectively to any nonempty subset of its incident coordinates, and same-colored vertex supports are disjoint. If the number of active internal vertices is i, then

    |π_{I,J}H|=|T|^i |A|^{e_A}|B|^{e_B}.

The double-edge graph has |I∩J| edges and i+e_A+e_B active vertices, so its forest identity gives |I∩J|=i+e_A+e_B−c. Hence the ratio between the K-image size and the quotient stabilizer index is

    |π_{I,J}K| / [π_{I,J}G:π_{I,J}H]
      = |π_{I,J}H| / |T|^{|I∩J|}
      = |T|^{c−e_A−e_B}|A|^{e_A}|B|^{e_B}.               (2)

If no endpoint is active, (2) is |T|^c>1. If exactly one is active, it is |T|^{c−1}|A| or |T|^{c−1}|B|, again greater than 1. If both are active, |A||B|=|T| reduces (2) to |T|^{c−1}. Equality requires c=1; a connected subgraph of a path containing both endpoints contains every edge. Thus every edge is double and I=J={1,…,k}, corresponding to the trivial kernel. The empty retained set is the trivial quotient. For every other normal quotient, (2) is strictly greater than 1. C0001's exact normal-subloop criterion therefore proves the loop simple, without assuming any factorwise section is a quotient loop.

## Properness and scope

H≠1, so the loop is nonassociative. Moreover H<L_L×N_R<G: the first inclusion is strict because R<N, and the second because L<N. Hence its canonical left multiplication action is imprimitive. C0001 Lemma 1.2 makes a simple nonassociative Moufang loop's left multiplication action primitive, so this loop is non-Moufang. It is non-Bruck: τ(H)=R_L×L_R differs from H because L∩R=1 and L,R>1, and the cited Bruck-stabilizer test applies. The loop order is [G:H]=|T|^k; it is even by the odd-order theorem for finite nonabelian simple groups.

The canonical group G=T^{2k} has exactly 2k minimal normal subgroups, one for each simple coordinate, and τ exchanges them in k pairs. Thus there is no universal bound on the number of minimal normal factors among radical-free canonical groups in the even non-Bruck simple proper branch. For k=1 and T=A₅, A=A₄, B=C₅, this recovers the known Q₆₀ folder up to the ordering of factors. The construction does not claim that all simple folders with these groups arise from paths. The following section gives an exact isomorphism criterion within this family. The construction, quotient proof and isomorphism criterion have the independent reviews recorded below.


## Isomorphism within the path family

Let Q(T,A,B,k) and Q(T′,A′,B′,k′) be loops from the displayed path construction. They are isomorphic if and only if k=k′ and there is an isomorphism ψ:T→T′ carrying the ordered pair (A,B) to either (A′,B′) or (B′,A′). This criterion is confined to the path family; it does not classify other folders with the same canonical group.

Sufficiency follows by applying ψ to every simple coordinate of G and, if the endpoint factors are interchanged, reversing the path, with the induced permutation of τ-pairs and the required interchange of the two members of each pair. These maps preserve the swap τ, the anti-diagonal K and the vertex-subgroup description of H, so they give canonical-folder and loop isomorphisms.

Conversely, a loop isomorphism induces an isomorphism of canonical folders and commutes with their canonical inversion automorphisms: the latter are uniquely determined by inversion on the generating section K. The canonical group isomorphism T^{2k}≅T′^{2k′} identifies the nonabelian simple direct factors, giving k=k′ and T≅T′. Choose an identification of T with T′. The isomorphism commutes with τ, so it permutes the k τ-pairs of simple factors, may interchange the two members of each pair, and applies the same automorphism ψ_i∈Aut(T) to both members of pair i.

For k≥2, the k−1 internal vertex subgroups are exactly the minimal normal subgroups of H isomorphic to T. Indeed H is their direct product with the two endpoint groups A,B. Neither proper endpoint group can contain a copy of T because its order is smaller, while a diagonal subgroup across two independent internal T factors is not normal in their direct product. Thus these internal groups are intrinsic. The support of each consists of one simple coordinate in each of two adjacent τ-pairs. Their supports, together with the τ-pairing and the two remaining endpoint supports, recover the path on k edges. Any folder isomorphism therefore induces the identity or reversal of that path.

At an internal vertex, its full diagonal subgroup must map onto the corresponding full diagonal subgroup. This forces ψ_i=ψ_{i+1} on its two incident τ-pairs. The connected path gives a single ψ on all pairs, and the endpoint supports then give (A′,B′)=(ψ(A),ψ(B)) or (ψ(B),ψ(A)). The allowable pairwise factor interchanges are fixed by the recovered half-edge incidences and do not add an independent endpoint transformation. For k=1 there are no internal vertices: the same conclusion follows directly from H=A×B and the centralizer of the swap in Aut(T×T), as in the independently reviewed [paired-simple reduction](radical-free-paired-simple-envelopes.md) at `4c93742a59ccdd786f23598f0374f674c6f75fff`. This proves the criterion.

No enumeration of all exact factorizations of simple T, all admissible endpoint pairs, or all radical-free Bol folders is claimed.

## Independent review

Three independent GPT-6.1 Terra mathematical reviewers — [model reviewer], [model reviewer] and [model reviewer] — accepted this construction and its within-family isomorphism criterion at exact source `1818e2c44bee176638f1212fd8b36c6a8a92e5ba`, conditional on the cited folder, normal-quotient, Moufang, canonical-inversion and Bruck-stabilizer inputs. Each checked every retained-coordinate quotient through the forest count and the intrinsic path reconstruction. No new computation, primary-source audit or novelty assessment was performed. The construction proves unbounded simple-factor count in this branch; it does not classify arbitrary radical-free envelopes.

## Connected twisted-diagonal graphs reduce to paths

**Continuation with scoped independent reviews below of the path theorem at exact reviewed source `1818e2c44bee176638f1212fd8b36c6a8a92e5ba`.** Let T be finite nonabelian simple and Γ a finite connected simple bipartite graph with at least one edge. Put N=T^{E(Γ)}. At each vertex of degree at least two attach a full T; at each leaf attach a nontrivial proper subgroup A_i<T. Embed a vertex group into its incident edge coordinates by arbitrary coordinate automorphisms of T, possibly different at different incidences. Let L,R be the products of the vertex subgroups in the two color classes, and suppose N=LR is an exact factorization. Then Γ is a path, and coordinate automorphisms of N turn this datum into the ordinary path construction above. This statement is confined to these vertex-diagonal data; it does not classify arbitrary factorizations of T^k or radical-free Bol envelopes.

The classification input is Baddeley, Praeger and Schneider, *Intransitive Cartesian decompositions preserved by innately transitive permutation groups*, Transactions Amer. Math. Soc. **360** (2008), 743–764, [doi:10.1090/S0002-9947-07-04223-7](https://doi.org/10.1090/S0002-9947-07-04223-7), Theorem 4.3 and Table 3, printed p. 751. Their theorem states that a strong multiple factorization of a finite nonabelian characteristically simple group has exactly three members and gives the listed simple-group possibilities. The theorem and table were directly inspected; their classification-dependent proofs have not been independently reverified here. The zero-leaf cycle argument additionally uses Fried–Guralnick–Saxl, *Schur covers and Carlitz's conjecture*, Israel J. Math. **82** (1993), Lemma 12.1, [authors' PDF §12 p. 26](https://www.math.uci.edu/~mfried/paplist-ff/sch-carlitz.pdf): T has an involution class invariant under Aut(T). Both inputs use CFSG.

Write ℓ for the number of leaves and b=|E(Γ)|−|V(Γ)|+1 for the cycle rank. Vertex groups in one color class have disjoint edge supports, so they form a direct product and

    ∏_{i=1}^ℓ |A_i| = |T|^{ℓ−1+b}.                         (10)

If ℓ≥1, every A_i is proper, so the left side is strictly less than |T|^ℓ. Equation (10) forces b=0. If ℓ=0, it gives b=1. A connected graph without leaves has all degrees at least two; with b=1, the degree sum forces every degree to be two, so Γ is one cycle. Propagating an element of L∩R around that cycle through its incidence automorphisms identifies the intersection with C_T(α) for the resulting holonomy α∈Aut(T).

No automorphism α of T is fixed-point-free. To see this from FGS Lemma 12.1, choose an Aut(T)-invariant involution class and c in it. An inner twist β of α fixes c. If C_T(α)=1, the map x↦x⁻¹α(x) is injective and hence bijective, so all elements of the coset Tα in T⋊⟨α⟩ are T-conjugate to α. In particular β would be T-conjugate to α and have trivial fixed-point subgroup, contradicting c∈C_T(β). Thus the zero-leaf cycle has nontrivial L∩R and cannot be exact. Every exact datum is therefore a tree with at least two leaves.

On a tree, choose a root vertex and reparametrize its vertex group. Moving outward, use an automorphism of each new edge coordinate and a reparametrization of the newly reached vertex group to make both incidence maps on that edge the identity. There is no cycle to create a compatibility condition. This gauges the twisted diagonals to ordinary diagonals; the leaf subgroups are carried to their automorphic images.

Let A₁,…,A_ℓ denote those transformed leaf groups. Equality of the two color assignments propagates one element along the tree, so exactness gives ∩_i A_i=1. Equation (10) with b=0 becomes

    ∏_i [T:A_i]=|T|.                                        (11)

Consequently the diagonal T-action on ∏_i T/A_i is regular: its base-point stabilizer is ∩A_i and its orbit has the whole product's cardinality. In particular, projection to any three coordinates is transitive. For distinct i,j,h this implies

    T=A_i(A_j∩A_h)=A_j(A_i∩A_h)=A_h(A_i∩A_j).             (12)

The leaf subgroups are pairwise distinct, since a diagonal action on two copies of the same proper coset space cannot be transitive. Thus ℓ≥3 gives a strong multiple factorization. By the cited BPS theorem ℓ≤3. If ℓ=3, regularity also gives A₁∩A₂∩A₃=1. The BPS Table 3 groups have instead

    |A₁∩A₂∩A₃|=|A₁||A₂||A₃|/|T|²>1.                       (13)

For the first table row, T=Sp_{4a}(2), a≥2, the value is

    2^{2a²−4a+3} ∏_{i=1}^{a−1}(2^{4i}−1) ≥120.

For the PΩ₈⁺(3) row it is 144. For Sp₆(2) it is 12 for (G₂(2),O₆⁻(2),O₆⁺(2)), and 6 for each listed variant with one factor replaced by its index-two derived subgroup. These values follow from the standard classical-group orders: in the latter two rows the respective orders of T and the three listed factors are

    4,952,179,814,400; 4,585,351,680; 4,421,589,120; 174,182,400,
    1,451,520; 12,096; 51,840; 40,320.

For reproducibility, the symplectic order is |Sp_{2n}(q)|=q^{n²}∏_{i=1}^n(q^{2i}−1). The first-row orthogonal orders are |O_{2n}^±(2)|=2·2^{n(n−1)}(2^n∓1)∏_{i=1}^{n−1}(2^{2i}−1); substituting n=2a and the extension-field symplectic order gives the displayed product. In the second row use |PΩ_8^+(q)|=q^{12}(q^4−1)∏_{i=1}^3(q^{2i}−1)/gcd(4,q^4−1), |Ω_7(3)|=|Sp_6(3)|/2 and |PSL_4(3)|=3^6∏_{i=2}^4(3^i−1)/gcd(4,2). Root independently checked the finite ratios by exact integer arithmetic and inspected the BPS theorem/table in the [repository PDF](https://api.research-repository.uwa.edu.au/ws/files/1469669/11339_PID11339.pdf); this does not certify the classification input or replace mathematical review.

Thus ℓ=3 is impossible. A finite tree with exactly two leaves is a path, proving the claim. The external table interface and classical-order calculations have the scoped independent reviews below. In particular, this result does not rule out branching with different vertex-group models or a non-vertex-diagonal radical-free folder.

### Independent review of the graph reduction

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the connected twisted-diagonal graph section at exact source `c1be0daa47ca5f6befeb96378bc1937544acbde1`, conditional on FGS Lemma 12.1, BPS Theorem 4.3/Table 3 and the stated classical-group orders. All three directly inspected the BPS primary PDF, printed p.751, and checked the cycle/holonomy argument, tree gauge, regular leaf-coset action and intersection values. [model reviewer] had separately inspected the FGS statement; the other two claimed no fresh FGS audit. None independently reverified the CFSG classification proofs. [model reviewer] also checked the ratio 144 by exact integer arithmetic. Acceptance concerns this graph model, not arbitrary subgroup embeddings or radical-free envelopes.
