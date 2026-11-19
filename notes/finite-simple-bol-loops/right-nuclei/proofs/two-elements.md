# Two genuine commutation tests suffice despite arbitrarily large right nucleus

**Mira Cult**

This theorem concerns the [all-central realization](abelian-central.md) of nontrivial finite odd abelian right nuclei. There exist two specified elements with the following property: an element commuting with both must be the identity. Two is optimal. This is not asserted for every Bol loop or every realization of a right nucleus.

Recall the notation of that proof. D=N⋊X, N is the class-two central extension of L_0⊕L_1 by S, where S is the product of the prime-power coefficient rings. X=(A⊕B_*)⋊P with A,B_* copies of F_q^k, top P=∏C_{r_i} acting diagonally by the separate faithful factor characters χ_i and their reciprocals. The signed automorphism τ swaps the two axes and negates P, interchanges the two L copies and fixes S. The native loop is the coset space D/H with its full τ-inverted set T as left translations. H projects in X to B_*⋊P and on the nilpotent group has vectors only in L_0 (also at nonzero top). The L copies are E^P; the native q-shift z on E is fixed-point-free off identity even on the true product ring. The operations needed below are all evaluations of the original table: the element for a mark a is aH, and two marks a,b commute as loop elements iff abH=baH, equivalently [a,b]=a^{-1}b^{-1}ab∈H, not necessarily [a,b]=1 in D.

Choose a true top h₀ whose entry in every independent cyclic factor is a generator. It is one native mark. Let v=(e₁,−e₁) be the native antidiagonal on the *first* q-axis pair. At P-index zero v acts identically on both copies of E. Choose any nonzero e∈E, put w at that P-index with value e and zero elsewhere, and take the second mark

```math
b=\bigl((-w,w),0\bigr)v .
```

The pure vector and v commute as group elements, and both are τ-inverted, so b∈T including its actual zero central phase. No scalar norm or element-order data standing in for this mark is used.

Let a∈T commute in the loop with h₀ and b, and write its projection as y h with y∈V=A⊕B_* and h∈P. Project [a,h₀] into X. It belongs to V, and its A component is that of h^{-1}(h₀^{-1}−1)y. Each true A coordinate is multiplied by a nontrivial eigenvalue of h₀, so membership in B_* forces y_A=0. Inversion by τ means swap(y)=−h^{-1}y, hence also y_B=0. Next, the commutator of the projected h with v has A component zero precisely if χ₁(h)=1. Therefore h lies in K=ker χ₁ (its first cyclic coordinate is zero), and h now actually commutes with v in X.

Use the genuine homomorphism D→L_1⋊X that drops the Heisenberg center and the entire first L coordinate. It maps H into {0}⋊(B_*⋊P). The two projected commutators are already trivial on X, so in this affine quotient they must both be the identity. If the affine image of a is (α,h), comparing products in the two orders gives

```math
h_0\alpha=\alpha,\qquad (1-v)\alpha=(1-h)w .
```

Consider **all native indices j∈K**. On these, the exponent of v on L_1 is χ₁(j)^{-1}−χ₁(j)=0. The left side of the second equality is identically zero on K regardless of α. But a nonzero h∈K shifts the one-site address of w to a different point of K; w−hw is nonzero there. Thus h=0. The two equalities now say α is fixed by h₀ and v. The h₀ action is a pure shift on P-indices; every one of its orbits contains a j with χ₁(j)≠1, since its first projection is a generator. An odd-order nontrivial character value is different from its inverse, so v acts there by a genuinely nonidentity q-shift. Its difference kills no nonzero E-vector, implying α vanishes at that site and hence on its entire h₀-orbit. Thus α=0. Now a lies in N and τ-inversion forces its first L coordinate to be the negative of its second, and its central coefficient to be simultaneously fixed and negated. Both vanish by oddness. This proves the assertion for all m,q,P in the stated family.

A single test never suffices: a nonidentity b commutes with itself; identity commutes with the whole nontrivial loop. The address in the second test is significant: with w=0, every true pure h∈kerχ₁ commutes with both bare marks in D. This true multiplicity is nontrivial whenever P has more than one listed factor. More generally if w is supported on χ₁=1 but invariant under a subgroup K₀≤kerχ₁, each h∈K₀ remains a genuine commuting mark; symmetry of the actual address matters. For noncyclic P even the left translations of the **successful** two probes generate only a subgroup with cyclic top image <h₀>, while the true full left multiplication group projects onto P. The statement is therefore not deduced from two-generation or from usual group centralizers.

Review scope: these two prescribed loop elements force trivial common commutation, not trivial right nucleus; indeed their source family has arbitrarily large right nuclei. No blanket claim is made for all finite simple odd Bol loops, nor for the unrelated trivial-right-nucleus proposal.

[Review and replication](../verification.md) · [Right nuclei](../README.md)
