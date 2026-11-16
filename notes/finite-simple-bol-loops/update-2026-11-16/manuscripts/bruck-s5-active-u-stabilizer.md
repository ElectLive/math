# Candidate bounded active U-coordinates in a stabilizer

**Stabilizer normal form with scoped independent review below.** Assume a faithful Baer envelope of a finite simple exponent-two Bruck loop, V=O₂(G) elementary abelian, G/V≅S₅. Let the principal block have m M composition factors, and use the reviewed support theorem in [bruck-s5-uniform-principal-support.md](bruck-s5-uniform-principal-support.md) at `32b5918c4b3fa3b2686185006b80d41b1ece76aa` to write

V=X₀⊕A⊕N^a⊕U^b,   A=1^u⊕R^v,  R=F₂C₂, U=N⊗R,

d₀=dim X₀≤112m, a≤110m+1. Put W=H∩V. We propose that an S₅-module automorphism of U^b puts W in the form

W = W_active ⊕ T_standard^s,

where T_standard is an F₂₀-invariant 4-dimensional complement to soc(U)=N in U, W_active lies in X₀⊕A⊕N^a⊕U^{b−s}, and b−s≤111m+1. The automorphism need not preserve the original W; this is a normal form up to module automorphism. It does not imply a corresponding product decomposition of the loop, its section K, or its normal subloops. This continues C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`] without allocating a new claim ID. The deduction has the scoped independent review recorded below.

Let F=F₂₀=N_{S₅}(P), P=C₅. P averaging is exact and F-equivariant. Since A is P-trivial and Y=N^a⊕U^b is P-fixed-free, W^P lies in X₀^P⊕A. For the P-nonfixed part, put S=N|F, an absolutely irreducible projective 4D F-module with End_F(S)=F₂. Nagy arXiv:0709.4544v1 Lemma 4.1 identifies M|F≅N|F≅S, and each U|F is S⊕S. Choose the same fixed F-complement to soc(U) in every copy of U. Multiplication by ε identifies that complement with the socle, so the dual-number matrix shears used below are S₅-module automorphisms in these coordinates; no lift to an extension-group automorphism is assumed. The multiplicity coordinates identify

[P,V] ≅ S⊗(A₀⊕B₀⊕C₀⊕T),

where A₀=F₂^m is the principal nontrivial part, B₀=F₂^a the N copies, C₀=F₂^b the U socles, and T=F₂^b the U tops. The last identification C₀≅T comes from U=N⊗R and the common R-multiplicity basis. Write [P,W]=S⊗B for some subspace B, dim B=c. Each F-submodule of soc(Y)=N^{a+b} is S₅-invariant because End_F(S)=F₂, and core-freeness gives W∩soc(Y)=0. Thus

B∩(0⊕B₀⊕C₀⊕0)=0.                                        (1)

Let K=ker(B→T), h=dim K. By (1), the projection K→A₀ is injective; write its image L, dim L=h≤m. Let T₁=im(B→T), k=dim T₁=c−h. Choose a complement A₀=L⊕A', and choose linear sections T₁→B, adjusting each by an element of K so that its A₀-coordinate lies in A'. Write these sections

q ↦ (αq, βq, γq, q),  α:T₁→A', β:T₁→B₀, γ:T₁→C₀.

Extend γ to a linear map T→C₀. A shear in GL_b(F₂[ε]/ε²)=Aut_{S₅}(U^b) sends (z,q) to (z+γq,q), eliminating γ from all chosen sections while leaving K unchanged. Let K_s⊆C₀ be the U-socle coordinate image of K, with dim K_s≤h.

The common kernel of α and β has dimension at least k−(m−h)−a. Choose within it a subspace T₀ disjoint from K_s (under the fixed C₀≅T identification), with

s=dim T₀≥max(0,k−m−a).

Such a T₀ exists because one can discard at most dim K_s≤h further dimensions. Choose a complement C to T₀ in T containing K_s. This is possible because T₀∩K_s=0. A change of U multiplicity basis realizes T=T₀⊕C simultaneously in socle and top, and is an S₅-module automorphism. Since the sections over T₀ are pure top vectors and K has U-socle coordinates in C, the direct sum T₁=T₀⊕(T₁∩C), which follows from T₀≤T₁ and T=T₀⊕C, splits

B=T₀⊕B_active,

with B_active contained in A₀⊕B₀⊕C⊕C. Therefore W=W^P⊕S⊗B_active⊕S⊗T₀, giving the asserted stabilizer form. Any kernel graphs involving A₀, B₀ and U socles remain in the active component; no such graph is discarded.

To bound the active number, set m₀=dim W^P. The support theorem's core-free projection gives m₀≤d₀−4m. The transposition rank is at least 2m+a+4b+v, while the Bruck fiber-capacity inequality gives r≤m₀+4c+1. Thus

b−c ≤ (d₀−6m+1−a−v)/4.

As k=c−h and h≤m,

b−s ≤ b−k+m+a = b−c+h+m+a
     ≤ (d₀+2m+1+3a−v)/4
     ≤ 111m+1,

using d₀≤112m and a≤110m+1. For m=0 the envelope assumptions are themselves excluded by the reviewed N-block result, but the displayed algebra remains a conditional bound. If b is smaller than the bound, s=0 already satisfies the numerical conclusion; the construction above still gives its (possibly larger) value of s.

This is a uniform stabilizer normal form at fixed m. It does not bound m or b, provide a finite list of radical sections, classify group-extension classes or prove an isomorphism criterion for loops. In particular standard U-complements in W do not by themselves imply standard behavior of K or a quotient by the corresponding U-submodules.

No independent review of this manuscript has occurred; the cited review applies to the pinned support input only.

## Independent review

GPT-6.1 Terra reviewer [model reviewer] accepted this module-level normal form at exact source `7ee728cc65fcaa28ffac8850185d0fdfe9a8bc48`, conditional on the reviewed support, N-block and fiber inputs. The review checked the compatible F-complement and dual-number shears, injective projection of the kernel graph, section adjustment, selection of T₀ disjoint from the socle image, and retention of all kernel graphs and P-fixed data in the active part. It checked the capacity arithmetic and bound 111m+1, including small b. It does not establish a lift of the automorphism to a fixed extension G, a normalization of K, a loop product or a bound on m or total U multiplicity. No computation or formal verification was used.
