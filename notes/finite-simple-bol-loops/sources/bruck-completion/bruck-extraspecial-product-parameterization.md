# Parameterization for extraspecial Bruck radicals

**Parameterization with scoped independent reviews below.** This construction concerns [C0010](../../claims/0010.md) and introduces no new claim ID. It targets finite simple nonassociative Bruck loops with faithful generated Baer envelope (G,H,K), extraspecial P=O₂(G), and product quotient A=G/P≅∏_{i=1}^e PGL₂(q_i), where e≥1 and each q_i is 9 or a Fermat prime at least 5. The proposed output is finite construction, admissibility and isomorphism data at each fixed A,m; it is not a classification of other non-elementary radicals, an efficient algorithm or a uniform bound on A or m.

The quotient, stabilizer and fiber inputs are Baumeister–Stein, *The finite Bruck loops*, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, under their stated faithful-envelope hypotheses. The [Frattini-shadow results](bruck-frattini-shadow.md), reviewed at the recorded source revision and the recorded source revision, provide the action of the canonical inversion automorphism on P/Φ(P) and the positive multiplicity input. The [extraspecial product constraints](bruck-extraspecial-product-constraints.md) give the bound below, with separate independent reviews at the recorded source revision. The construction and equivalence deductions have the scoped reviews recorded below.

## Parameters and nonabelian extensions

Put Z=Z(P)=Φ(P) and V=P/Z. Let B=∏B_i be the product of point-stabilizing Borels, W=H∩P, U=WZ/Z≤V, and C the largest A-submodule contained in U. Let m be the number, with multiplicity, of nontrivial simple A-composition factors of V/C. The cited constraints give m≥1 and

    dim V ≤ R + [1+2^e(3e+1)] |A| m,
    R=∑_{i=1}^e q_i(q_i−1)/2.                                  (1)

At fixed A,m≥1, enumerate even d≥2 within (1), the two extraspecial types P of order 2^{d+1}, and all normalized nonabelian factor systems. Choose maps α_a∈Aut(P), f(a,b)∈P satisfying, for all a,b,c∈A,

    α_a α_b = Inn(f(a,b)) α_{ab},
    f(a,b) f(ab,c) = α_a(f(b,c)) f(a,bc),
    α_1=id,  f(1,a)=f(a,1)=1.

Then G=P×_f A with multiplication

    (p,a)(q,b)=(p α_a(q) f(a,b), ab).

Conversely every such extension has this form after choosing a normalized section. Conjugation by lifts induces an A-action on V; automorphisms of P preserve its commutator and square forms. After choosing H below, compute C and require exactly m nontrivial composition factors in V/C. Since O₂(A)=1, the constructed P is automatically O₂(G). The bound (1) is an exhaustiveness and fixed-parameter finiteness input, not a new proof here.

## Stabilizers, inversion and the marked section

Enumerate every H≤π⁻¹(B) with π(H)=B and Core_G(H)=1. Equivalently, enumerate W≤P and elements h_b∈P, b∈B, with h_1=1, forming

    H=⋃_{b∈B} W(h_b,b).

Require each (h_b,b) to normalize W and require

    h_b α_b(h_c) f(b,c) h_{bc}^{−1} ∈ W                 (b,c∈B).

These equations are exactly closure of the displayed union; test core-freeness separately. They retain all nonabelian stabilizer lifts and do not assume that an arbitrary W is normal in P or that H is a linear cocycle graph.

Enumerate τ∈Aut(G) with τ²=1, τ|H=id, and τ inducing the identity on A and V=P/Z. For target Bruck envelopes, the cited Frattini-shadow input gives the V statement. Every element of K projects to an involution or 1 in A, so inversion on K and generation give the A statement. Here τ²=1 includes τ=id. In the formal external semidirect product G⁺=G⋊⟨hatτ⟩, enumerate every union Λ of G⁺-conjugacy classes of involutions in hatτ G that contains hatτ, and put K=hatτΛ. Thus 1∈K. Conjugation by hatτ preserves Λ, and each λ=hatτ k has order 2; consequently τ(k)=k⁻¹ and K is inverse closed. For k,l∈K, the conjugate (hatτ k)(hatτ l)(hatτ k) lies in Λ and equals hatτ(kl⁻¹k). Since K is inverse closed, it is closed under sandwich products.

Moreover Λ⁻¹Λ=K⁻¹K is G-conjugacy-invariant. Require

    H ∩ K⁻¹K = {1},     |K|=[G:H].                         (2)

The first condition gives collision-freeness in H-cosets; its G-conjugacy invariance gives the same for every conjugate of H, and the second turns injections into transversals. Since τ fixes H pointwise and Λ is G⁺-invariant, H normalizes K. The folder criterion therefore constructs a Bol loop, and τ induces its inverse map as an automorphism; it is a Bruck loop.

For an optional and source-backed admissibility filter, let C_I⊂A be the class whose coordinates are outer involutions exactly on I⊆{1,…,e}, and let n₀=[P:W]. The cited Lemmas 4.4–4.5 give, for every x∈C_I,

    |K∩π⁻¹(x)| = n₀·2^{|I|}/∏_{i∈I}(q_i−1),                 (3)

with I=∅ giving n₀; no other quotient images occur. Check positivity, integrality and all fibers in the finite group. These source fiber restrictions apply to the stated general Bruck envelopes, not only to elementary radicals. They prune the general marked-class enumeration and are not used to justify an untested quotient folder.

## Admissibility and completeness

Require ⟨K⟩=G. Enumerate **all** nontrivial normal subgroups R◁G, including those with nontrivial image in A, and reject whenever HR<G and

    |KR/R| = [G:HR].                                        (4)

By C0001 Theorem 2.2 and core-freeness, (4) is exactly the occurrence of a proper nontrivial normal subloop: equality gives a quotient folder and a nontrivial kernel; every normal subloop is detected by the core of the corresponding intermediate subgroup. The inequalities in (4) can be checked by finite coset hashing without assuming a group quotient is already a loop quotient. Finally impose a finite nonassociativity test on the resulting folder; if selecting only the proper/non-Moufang branch, also impose the C0001 Moufang failure test. These identity filters avoid inferring properness from the quotient type alone.

Every accepted datum gives a finite simple nonassociative Bruck loop by the preceding argument. Conversely, the cited product theorem supplies A,B, the support and fiber restrictions, and the canonical inversion automorphism for every loop in the stated scope; a normalized extension section and the actual H,τ,Λ appear among the enumerated choices. The reviewed bound (1) puts its dimension in the fixed-A,m search. The Frattini-shadow input supplies m≥1. Thus, subject to those inputs, the scheme is exhaustive in the specified extraspecial branch. For each k∈K, π(k)²=1 and P has exponent at most 4, so k⁸=1; the loop exponent divides 8. No exponent-4 conclusion is inferred.

## Isomorphism test for the nonabelian data

For two accepted data, every envelope isomorphism preserves P=O₂(G). With chosen sections it has the form

    Φ(p,a) = (β(p) u(a), γ(a)),

where β:P→P' and γ:A→A' are isomorphisms and u:A→P' is normalized. Conversely such a map is a group isomorphism exactly when

    β ∘ α_a ∘ β⁻¹ = Inn(u(a)) ∘ α'_{γ(a)},
    β(f(a,b)) u(ab) = u(a) α'_{γ(a)}(u(b)) f'(γ(a),γ(b))

for every a,b∈A. Enumerate all β, γ and u satisfying these equations, retaining quotient isomorphisms that permute isomorphic factors and include their full automorphism groups. Require γ(B)=B' and test Φ(H)=H', Φτ=τ'Φ and Φ(K)=K' exactly. These conditions are necessary and sufficient for a faithful generated-folder isomorphism, hence for a loop isomorphism. A loop isomorphism intertwines the unique inversion automorphisms because K generates G; conversely a Φ satisfying the tests transports the folder multiplication. No chosen quotient-factor labels or extension sections are fixed by the equivalence relation.

At fixed A,m, (1) leaves finitely many extraspecial P of two types in each even dimension, and all factor systems, stabilizers, automorphisms, marked-class unions, normal subgroups and isomorphism candidates are finite. These restricted group extensions and their commutator/square geometry provide structural data beyond enumerating Latin squares, but no practicality or global finite parameter bound is claimed. The dimension bound and this manuscript's construction and isomorphism equivalence have the separate scoped reviews below.


## Independent review

Independent checks an independent check and an independent check independently accepted this parameterization at exact source the recorded source revision, conditional on the cited companion dimension bound and folder inputs. They checked nonabelian extension and stabilizer equations, the formal marked-involution construction, all-normal-subgroup simplicity tests, fixed-parameter finiteness, exhaustiveness and the full radical/quotient/section isomorphism equivalence. The companion bound was separately accepted at that same source by an independent check and an independent check; the parameterization reviewers did not independently certify that bound. Both parameterization reviews assessed the restricted construction data as structural information beyond Latin-square enumeration, with unbounded global parameters and no efficiency claim. No computation or formal verification was used.

