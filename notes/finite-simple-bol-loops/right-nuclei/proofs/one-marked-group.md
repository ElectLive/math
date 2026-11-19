# One fixed signed group, one fixed set of marks, every subgroup of U as the full native right nucleus

**Mira Cult**

**Theorem.** Fix any finite odd group U (including the trivial group). There are a single finite odd group Y, the same signed group D≤Y² with coordinate-swap involution, and the same entire set of marks T={d_y=(y,y⁻¹): y∈Y} such that for each H≤U a choice of point stabilizer in D makes those marks the translations of a finite simple non-Moufang left Bol G-loop on the *same literal set Y*. The whole U is a common native subgroup with exactly its given multiplication in every one of the loops. The right nucleus inside and outside that subgroup is **exactly H**, with its specified embedding. The left and middle nuclei, commutant and center of the abstract left multiplication group are trivial. All loops have the same degree and the same abstract left multiplication group, involution and marks; their actions on their points and their other multiplications can change. This is not the assertion that different nuclei occur in one loop or one isotope class.

Consequently any finite list of finite odd groups (of different orders or with different derived orders permitted) can be realized at one common degree with one common signed translation envelope and the same native subgroup containing all of them: take their direct product as U. Nonisomorphic nuclei distinguish the corresponding loops even up to isotopy, since each is a G-loop. The potentially large new common degree is that of the universal construction with input U, not the smaller individual degree for each H.

**Input and separation.** Use the verified transfer lemma, explicit coefficients, faithful module and native group calculations of [the universal right-nucleus theorem](all-odd-groups.md). That prior theorem realizes each target as an auxiliary regular top, with its own signed group, and a common degree for equal orders and equal |derived group|. It does not assert this fixed-*group*, common-native-subgroup result. In the prior notation call its second factor J and its graph subgroup T₀; the symbols H and T above refer to the desired nuclear subgroup and the signed *set of marks*, respectively. No modification of the representation or of the signed-cut proof is needed, but the changed first factor must still be core-free and complementary. We prove this and identify the genuine native multiplications.

Use k=F_(11³), primitive c∈k×, primitive seventh root ζ, F=k⁺⋊⟨z⟩ with z acting by ζ. Write a(x,z^j)=(x^11,z^{4j}), Θ(x,z^j)=(c x^11,z^{4j}), a₂=Θ a Θ⁻¹. The auxiliary is the SAME P=(B²)⋊(⟨s⟩×U), B=F^U, with s acting by (a,a₂) and U by left permuting the sites on both wings. The fixed factor T₀⋊(⟨s⟩×U) is the graph of Θ on these two wings extended by the top; denote it by J₀. P′∩Z(P)=C_{P′}(J₀)=1, N_P(J₀)=J₀ and J₀ normally generates P, independently of the choice below. Use the same faithful irreducible prime-field module V (dimension 49|U|), balanced W, Y=W⋊(V⋊P), π(w,p)=w(0)p on W⋊P, true second factor J=V⋊J₀ and the fixed D={ (g,h)∈Y² : g̅h̅=1 in Y_ab }. The degree is |Y|.

**The variable first graph.** For a binary subset C⊆U set ε_j=2 if j∈C and 0 otherwise. Let ψ_e(x,z^b)=(c^e x,z^b) and let Ψ_C act coordinatewise by ψ_{ε_j} on B. Put S_C=graph(Ψ_C)≤B² and K_C=π⁻¹(S_C); the point stabilizer is D∩(K_C×J). Every S_C is core-free in P: if a P-normal subgroup in S_C contains (b,Ψ_C b), conjugation by the first B alone forces b central, hence trivial. We claim P=S_C J₀ is exact. At a common element of the two graphs, ψ_e(u)=Θ(u); the C₇ grade must be zero, since it is both j and 4j. A nonzero additive solution would satisfy x=c^{1-e}x^11, hence c^{133(1-e)}=1 on cubing this semilinear map. But c^133 has order 10 and e∈{0,2}, impossible. Therefore the two base graphs intersect trivially; sizes and the complete top in J₀ give the exact factorization. The original universal transfer lemma applies *separately to each S_C with the same Y and D*.

Let the setwise stabilizer of C under U be U_C (left translates). A conjugacy S_C → S_{C′} by (x,y)s^i r∈P can exist only if in every destination coefficient j the two local arrows agree up to an inner automorphism of F. Their relative action on k⁺ is multiplication by c to the exponent

```math
1-11^i+11^i\epsilon_{r^{-1}j}-\epsilon'_j .
```

Indeed a₂^i acts as c^{1-11^i} times the i-th Frobenius; one first transports the graph from the physical source r⁻¹j, then removes a^i and compares the destination graph. Inner automorphisms act on the additive kernel only by seventh-root scalars; the exponent must be divisible by 190. For i=1 its possibilities are −12,−10,10,12; for i=2 they are −122,−120,120,122. None works. With i=0, equality is possible exactly when every color matches. In this case the pure r works, and the remaining normalizer of the base graph in B² is precisely the graph itself by centerlessness of B. Thus

```math
N_P(S_C)=S_C \rtimes U_C .
```

There is no extra permutation swapping color names in this calculation. The general normalizer formula in the input and the fixed second factor imply |Nuc_r(Q_C)|=|U_C|.

**The common literal subgroup and associator probes.** Regard u∈U as the same pure top element of Y in every model. Distinct u's give distinct loop elements d_u H_C, with H_C=D∩(K_C×J), since U∩K_C=1. In fact for any u,v∈U

```math
d_{uv}^{-1} d_u d_v=(1,uvu^{-1}v^{-1})\in H_C.
```

The right component is in U′≤J, and the discrepancy is in D; the genuine native product of these two marks is d_{uv}. If u∈U_C, d_u normalizes H_C: its first component normalizes K_C and its second belongs to J. Its identity image therefore has a commuting-right-translation in the coset centralizer and is genuinely right-nuclear. Counting with the preceding equality shows that no other site in the whole native loop is right-nuclear. Taking C=H≤U gives U_C=H, including H=1 and H=U.

There are even literal associator witnesses inside the common marked envelope. Fix j and let A_j,B_j∈P be respectively (z,z) at j and (u₀,c^{ε_j}u₀) at j, identities elsewhere, where u₀∈k⁺ is any fixed nonzero element. Both belong to S_C. Under the identification of points with signed marks, their native product is their *reversed ambient product* B_j A_j: the right-coordinate discrepancy is identity, the first is k_j=(B_j A_j)⁻¹A_j B_j∈S_C. Here k_j is a nonzero additive element in the graph at j, since ζ≠1; its two coordinates have ratio c^{ε_j}. The actual left inner mapping is then (k_j,1). It fixes the r-mark for r∈U iff (r⁻¹ k_j r,1)∈H_C, equivalently ε_j=ε_(r⁻¹j). Consequently

```math
(A_j\circ B_j)\circ r=A_j\circ(B_j\circ r)
                 \quad\Longleftrightarrow\quad 1_C(j)=1_C(r^{-1}j).
```

The number of failing sites is exactly |C△rC|; for C=H it is 2|H| for every r outside H, and zero inside. The choice of B_j uses the color, but the color itself can be read from a *color-independent* marked query: replace B_j by (u₀,u₀). Its native product with the same A_j is its reversed ambient product iff the true color there is zero, by the same nonzero commutator test on the genuine stabilizer. These are marked tests, not claims that recovery from a completely unmarked multiplication table retains the coordinate labels.

**Honest scope at the group-action level.** The transitive actions of the IDENTIFIED group D have conjugate point stabilizers iff C′ is a left translate of C. In one direction project a putative D-conjugacy to its first Y-factor: the true projection of H_C onto K_C is onto because J surjects onto E. The projection of K_C onto the affine V⋊P is the pure P for every C by surjectivity of W evaluations. Its normalizer there is just P since V^P=0. The first Y-conjugator thus lies in W⋊P and pushing it through π gives a real P-conjugator S_C → S_{C′}. The local computation above forces C′=rC. Conversely d_r conjugates the two H's when C′=rC. For example there are at least [2^n−(n−1)2^(n/3)]/n inequivalent faithful transitive D-actions of this kind with trivial full right nucleus when n=|U|>1, since each nonidentity left translation has cycles of lengths at least three and each free orbit of colorings has size n. We do NOT infer that all these choices are nonisomorphic as unmarked loops: an isomorphism can induce an outer automorphism of the abstract marked D. The finite-list conclusion above, which uses distinct nuclear group isomorphism types, does not have this caveat.

A separate AI proof review and finite controls cover this common-group assertion, including unequal derived orders at the very same U. The universal existence proof and its earlier independent audit remain different sources. No smallest-degree or historical-priority claim.

[Review and replication](../verification.md) · [Right nuclei](../README.md)
