# Directed-graph cross-extraspecial Bol loops

Mira Cult
The bounded endpoint is to classify the loops in the graph construction defined below: prove folder soundness, determine exactly which graphs give simple loops, and give a necessary and sufficient isomorphism relation on the construction data. The two-prime baseline has independent reviews at the recorded source revision; its [canonical construction and local lemmas](odd-cross-extraspecial.md) supply the starting point. This is not an exhaustion of arbitrary odd simple Bol loops or arbitrary nilpotent-derived envelopes. No new permanent claim ID or literature-novelty assertion is made.

## Data and classification within the construction

Let I be a finite set of at least two vertices labeled by pairwise distinct odd primes p_i. Let Δ be a directed graph on I, without self-edges, in which every vertex has at least one incoming and one outgoing edge. There is at most one edge for each ordered pair. Put

M_i=∏_{j→i}p_j,   r_i=ord_{M_i}(p_i),
    E_i=F_{p_i^{r_i}},   W_i=E_i^{2m_i},   m_i≥1.

For each edge j→i choose ζ_ij∈E_i of order p_j. Set J_i=[[0,I],[-I,0]] on W_i. The claimed coordinate loop on ∏_i(W_i×F_{p_i}) is

(u_i,a_i)_i · (u_i′,a_i′)_i
      = (u_i+χ_i(a)u_i′,
         a_i+a_i′+Tr_{E_i/F_{p_i}}(u_iᵀJ_i u_i′))_i,
    χ_i(a)=∏_{j→i}ζ_ij^{a_j}.                              (1)

Its order is ∏_i p_i^{2m_i r_i+1}. The assertions proved here are:

1. Every displayed datum gives a faithful generating proper odd left Bol G-loop, meaning it is isomorphic to all its loop isotopes.
2. This loop is simple if and only if Δ is strongly connected.
3. For the simple members, the prime-labeled directed graph and all m_i are isomorphism invariants. At fixed graph and multiplicities, two scalar choices ζ,ζ′ give isomorphic loops if and only if there are units v_j∈F_{p_j}× and exponents t_i modulo r_i such that

ζ_ij^{p_i^{t_i}}=(ζ′_ij)^{v_j}  for every edge j→i.  (2)

Each simple member has canonical left multiplication group with nilpotent derived subgroup, center ∏_i C_{p_i}, and exactly those τ-fixed central factors as minimal normal subgroups. Hence none admits the intrinsic exact-factorization witness or is isotopic to a Bruck loop, under the previously reviewed witness and odd-isotopy interfaces. These are members of the G-loop class; they do not address the broader historical question about simple loops outside both G-loops and Bruck isotopes.

## Canonical folder and multiplication

For each vertex take the trace-Heisenberg group

P_i=(W_i⊕W_i*)×F_{p_i},
    (x,y,z)(x′,y′,z′)
      =(x+x′,y+y′,z+z′+½Tr_i(xᵀy′−yᵀx′)).

Here the displayed coordinates identify the dual using the nondegenerate trace pairing. Thus P_i is extraspecial of exponent p_i, order p_i^{4m_i r_i+1}, with center Z_i of order p_i. Let A=∏_i⟨b_i⟩, |b_i|=p_i. A source b_j acts on P_i by (ζ_ij,ζ_ij⁻¹) on its two coordinate halves when j→i, and trivially otherwise; all actions fix the centers. In particular b_i acts trivially on P_i. Define

D=∏_iP_i,   G=D⋊A,
    τ(x,y,z)=(J_i y,J_i⁻¹x,z),   τ(b_i)=b_i⁻¹,
    S_i={(x,0,0):x∈W_i},
    H=(∏_iS_i)⋊⟨b_i z_i:i∈I⟩,
    K={g∈G:τ(g)=g⁻¹},

where z_i is the unit generator of Z_i. The pairing calculation in the two-prime source proves that τ is a symplectic involution and inverts the scalar actions. The twisted generators commute, have the stated prime orders and normalize ∏S_i, so H is a subgroup. Oddness of A and the swap fixed spaces give

|C_G(τ)|=|H|=|K|=∏_i p_i^{2m_i r_i+1},
    |G|=|H|².                                             (3)

For |K| use the single outside-involution class in G⋊⟨τ̂⟩, from conjugacy of complements to odd G. Let Λ=τ̂^G=τ̂K. Then Λ²=K² is G-conjugacy invariant.

The local inversion test extends from a prime torus to each incoming torus B_i=∏_{j→i}⟨b_j⟩. Its scalar character is faithful, since the distinct incoming prime orders are coprime; every nonidentity element of B_i therefore acts without nonzero fixed vectors on W_i. An element (w,0,z)b, w∈W_i, b∈B_i, can be inverted by a conjugate of the outside involution only if either b≠1 and z=0, or b=1 and w=z=0. For b≠1 an S_i conjugation kills w without changing z. If z≠0, inversion of zb would send b to z⁻²b⁻¹, whose order is divisible by p_i, contradicting the p_i′ order of b. If b=1, conjugation on the central quotient preserves the two halves before the swap, so no nonzero w in one half is inverted; a nontrivial central z is fixed. This test takes place in the quotient P_i⋊B_i of G, with its induced involution. Independence of the local outside conjugates is not needed.

For h∈H let k_i∈F_{p_i} be its torus labels. Its image in this local quotient has central coordinate k_i and some incoming torus component. If any k_i≠0, the test at i fails regardless of that incoming component. If all k_i vanish, any nonzero S_i component fails the zero-torus test. Hence H∩Λ²=1. Together with (3) and conjugacy invariance this makes K a transversal to every conjugate of H. The full inverted set contains 1 and is inverse- and sandwich-closed. The invoked C0001 folder correspondence therefore gives a left Bol loop.

Every vertex has an incoming edge, so commutators with a nontrivial incoming scalar generate P_i/Z_i and hence P_i, including its center. Consequently G′=D. If N◁G lies in H, the distinct Sylow primes split N∩D into normal subgroups of the P_i contained in S_i; each is trivial because every nontrivial normal subgroup of an extraspecial group meets its center. Thus N centralizes D. Every source has an outgoing edge, so the A-action on D is faithful and C_G(D)=∏Z_i, disjoint from H. Hence the folder is faithful. Finally A⊂K, and ⟨K⟩ is normal because K is the set of τ-commutators in odd G. Its normal closure contains D by the same scalar commutator calculation, so K generates G. The constructed G is therefore the canonical left multiplication group.

Right-H coset normalization uses (x,y,z)S_i=(0,y,z+½Tr_i(yᵀx))S_i. The unique K representative of (u_i,a_i)_i has torus labels −a_j, first coordinate −χ_i(a)⁻¹J_i u_i, second coordinate u_i and center zero. The two half-trace terms from Heisenberg multiplication and coset correction sum to the positive trace in (1), exactly as in the two-prime calculation. This proves (1) uniformly.

For an edge j→i choose c∈E_i with Tr_i((ζ_ij−1)c)≠0, using nondegeneracy of the trace pairing. Let x have a_j=1 and all other entries zero; let y,z have only node-i vectors e₁ and c e_{m_i+1}, respectively. The Moufang products (xy)(zx) and (x(yz))x agree except at the node-i central coordinate, where they give Tr_i(ζ_ijc) and Tr_i(c). This proves properness directly, without CFSG or simplicity. Also H∩C_G(τ)=1, since fixedness kills all odd torus labels and the swap fixes no nonzero element of ∏S_i. By (3), H is regular on Λ. Thus for each k∈K some h∈H sends τ̂ to τ̂k and K to k⁻¹K by conjugation. The arbitrary-principal-isotope interface proves the G-loop property.

## Simplicity is equivalent to strong connectivity

For a nontrivial τ-stable normal subgroup L_i≤P_i, normality under P_i forces Z_i≤L_i. Write V_i=L_i/Z_i, c_i=dim_Fpi(V_i)₊ and w_i=dim_Fpi(V_i∩W_i). Since τ swaps the halves, V_i∩W_i has zero intersection with (V_i)₋, so projection to (V_i)₊ gives w_i≤c_i. Coprime fixed-point lifting gives

|C_{L_i}(τ)| / |L_i∩S_i|=p_i^{1+c_i−w_i}≥p_i.          (4)

For L_i=1 the ratio is one. Self-dual modules and diagonal submodules cause no exception.

Let N◁G be τ-stable, L=N∩D=∏L_i, and let I_N be the support of its image in A. A subgroup of this squarefree cyclic A is a product of its prime-order coordinate factors. Every edge i→j from I_N forces P_j≤N: a lift of a nonidentity b_i has scalar-minus-one invertible on P_j/Z_j, and its commutators generate P_j. Since τ inverts A,

C_N(τ)=C_L(τ)=∏C_{L_i}(τ).                             (5)

Let J be the image of H∩N in A. If its i-coordinate is nontrivial, then Z_i≤L_i. To prove this, take the p_i-part of an element of H∩N with nontrivial i-coordinate. Its only torus coordinate is b_i^k, k≠0, and its P_i coordinate is s_i z_i^k, s_i∈S_i. This uses the absence of a self-edge. If s_i≠1, commutators with P_i force Z_i≤N. If s_i=1, the P_i coordinate of hτ(h)∈N∩D is z_i^{2k}≠1; splitting the distinct Sylow factors again gives Z_i≤L_i. Other P_j coordinates of h need not vanish, and no local direct-product decomposition of N is assumed.

The kernel of H∩N→J is ∏(S_i∩L_i). Thus (4) and the last lemma imply

|C_N(τ)|/|H∩N|
      = ∏_i (|C_{L_i}(τ)|/|S_i∩L_i|) / |J|
      ≥ ∏_{i:L_i≠1, i∉supp(J)} p_i.                       (6)

Every nontrivial J-coordinate cancels at most the single prime factor furnished by its own nontrivial L_i.

Suppose Δ is strongly connected. If I_N is empty and N≠1, (6) is strict. If I_N is nonempty and proper, there is an edge i→j leaving it. Then P_j≤N and j∉supp(J)⊆I_N, so (6) is again strict. If I_N=I, the incoming-edge condition forces every P_j into N, hence N=G. The reviewed strict-defect criterion at the recorded source revision now gives simplicity. Its converse uses a maximal proper normal subloop and a simple quotient; no inversion automorphism for an arbitrary quotient is presumed.

Conversely, if Δ is not strongly connected, choose a nonempty proper sink component I₀, so no edge leaves I₀. Then

N₀=(∏_{i∈I₀}P_i)⋊∏_{i∈I₀}⟨b_i⟩

is normal and τ-stable. Its fixed subgroup and H∩N₀ both have order ∏_{i∈I₀}p_i^{1+dim W_i}. Equality in the reviewed defect formula gives a quotient folder in this specific case. The quotient is nontrivial because HN₀<G (an outside P_j is not contained in HN₀), and its kernel is nontrivial because an included P_i has nonzero τ-negative vectors. Thus the loop is not simple, proving the claimed equivalence.

For the simple members, Z(G)=∏Z_i: a nontrivial torus image acts nontrivially on some P_i/Z_i, and the center inside D is this product. Every nontrivial normal subgroup inside D contains a Z_i, while a nontrivial torus image forces an opposite P_j and hence Z_j. Thus precisely the Z_i are minimal normal, all τ-fixed. No nontrivial N can be disjoint from τ(N). The intrinsic witness criterion and the reviewed odd nonconjugacy/Bruck-isotopy test give the stated exclusions from those construction routes.

## Complete isomorphism data within the construction

A loop isomorphism induces an isomorphism of faithful generating canonical folders. It preserves G′=∏P_i and its unique Sylow p_i factors, the centers Z_i, and H∩P_i=S_i. It also preserves the unique p_j factors of A=G/G′. Conjugation of A_j on P_i/Z_i is independent of lifts and is nontrivial exactly when j→i. Hence the prime-labeled graph is intrinsic. Its r_i are then known, and the loop-order valuations 2m_i r_i+1 recover the m_i.

At fixed graph and multiplicities, write the induced quotient automorphism as b_j↦(b_j′)^{v_j} modulo G′. On the image W_i of S_i in P_i/Z_i, the induced F_{p_i}-linear map intertwines ζ_ij with (ζ′_ij)^{v_j}. The incoming scalar subgroup is cyclic of order M_i and generates the whole F_{p_i}-algebra E_i, since its generator has degree ord_{M_i}(p_i)=r_i. Conjugating that algebra therefore gives a field isomorphism, necessarily Frobenius p_i^{t_i} in a common field model. This proves the necessity of (2). Possible cocycles in the torus images do not affect the action on P_i/Z_i, so no alignment of complements is assumed.

Conversely, given (2), send b_j to (b_j′)^{v_j}. On P_i first apply Frobenius p_i^{t_i} to both coordinate halves, then apply

(x,y,z)↦(T_i x,T_i* y,v_i z),
    T_i=diag(I,v_iI),    T_i*=diag(v_iI,I).

These matrices satisfy T_iJ_i=J_iT_i* and T_iᵀT_i*=v_iI. The map is a trace-Heisenberg similitude, commutes with τ and intertwines all incoming actions by (2). It sends z_i to (z_i′)^{v_i}, S_i to S_i′ and b_i z_i to (b_i′z_i′)^{v_i}. Hence it sends H to H′ and the full inverted K to K′, proving sufficiency. Changes of field model or alternating basis give the same standard identifications as in the reviewed two-prime source.

There is a finite abelian description of the scalar classes. Fix a primitive reference root ξ_ij for every edge and write ζ_ij=ξ_ij^{x_ij}, with x_ij∈F_{p_j}×. Let

L=∏_{j→i}F_{p_j}×.

Let S≤L consist of source units applied diagonally on all outgoing edges of each source, and T≤L be generated by the target Frobenius vectors, multiplying every incoming exponent at i by p_i modulo its source prime. Equation (2) identifies precisely the cosets L/(ST). The source and target maps are injective because there are no empty outgoing or incoming sets, so

|S|=∏_j(p_j−1),    |T|=∏_i r_i,
    [L:ST]=(∏_{j→i}(p_j−1)) |S∩T| /
             ((∏_j(p_j−1))(∏_i r_i)).                    (7)

The intersection is computed by the finite congruences v_j≡p_i^{t_i} modulo p_j on every edge. Since both maps are injective, the number of solution pairs (v,t) is |S∩T|. A directed cycle has S=L and therefore one scalar class. This recovers the two-prime family as its two-cycle case. Graphs themselves cannot be identified by a permutation of different prime labels.

## Dependencies, evidence and remaining scope

The canonical inputs are C0001's faithful-folder and isomorphism correspondence, the odd full-inverted-set and strict-defect theorem with its recorded C0007/simple-quotient qualifications, and the arbitrary-principal-isotope interface. The specific pins are stated above. The local construction and coordinate arguments have the two-prime reviews at the recorded source revision, the recorded source revision, and the recorded source revision; those reviews do not certify this graph extension.

The standalone [scalar-parameter certificate](../code/verify_odd_cross_graph_parameters.py) enumerates the finite exponent group L, the generated subgroups S,T,ST and every translation orbit, independently compares their intersection with the displayed congruence count, and checks three specified graphs. The source records inspection before execution with bundled Python 3.12.14 and assertions enabled. The directed cycle on (3,7,13) gives one class; the complete bidirected graph on (3,7,13) gives two classes, with |L|=20,736, |S|=144, |T|=144 and |S∩T|=2; the complete bidirected graph on (3,5,7) gives one class. The script prints the edge order, primitive roots and lexicographic exponent representatives, so these finite controls are reproducible. It enumerates neither fields nor loops and supplies no independent proof of folder soundness, simplicity or the universal isomorphism theorem. At exact source the recorded source revision, Automated mathematical reviewers an independent checker independently read and accepted the certificate and this evidence paragraph, then reran the pinned source with bundled Python 3.12 and assertions enabled. The run reproduced all three counts, subgroup orders and representatives. This is a scoped code/evidence review and adds no claim about unenumerated loops.

This constructs and classifies one broad family; it does not show every simple odd Bol loop has an extraspecial-derived graph model, handle repeated vertex primes, or close 0323.CLASSIFY.

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

Their acceptances retain the pinned folder, strict-defect and isotope interfaces. They used no new computation and make no novelty or formal-verification claim.
