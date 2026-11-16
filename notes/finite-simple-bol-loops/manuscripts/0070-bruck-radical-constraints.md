# Bruck radicals: structural constraints and finite parameter schemes

Mira Cult

## What this collection establishes

The Bruck branch now has a common extension-data framework for **arbitrary** 2-radicals, together with sharper obstructions and parameter schemes in restricted radical classes. This is a structural reduction, not a completed classification of finite simple Bol loops, nor even a list of every simple Bruck loop. The parameters of the universal scheme remain unbounded. Non-Bruck Bol loops are outside this manuscript.

The main chain is:

1. The known Bruck-envelope structure identifies the quotient and canonical inversion automorphism.
2. The core-reduced Frattini shadow bounds a quotient module by its nontrivial composition-factor count.
3. An abelian subgroup extracted from an arbitrary radical bounds the discarded module core in terms of the size of the Frattini subgroup.
4. The resulting fixed-parameter order bound makes a complete, finite extension-data search possible at each fixed parameter tuple.
5. Central-Frattini and local chief-factor arguments rule out additional configurations; explicit S₅ calculations resolve only the specified strata.

Full mathematical sources, including the hypotheses of each finer reduction and its evidence limitations, are indexed in [the proof-source collection](../sources/bruck-completion/README.md). Their candidate labels have not been silently promoted to unconditional global theorems.

## 1. Common envelope setting

Let X be a finite simple nonassociative right Bruck loop with faithful generated Baer envelope (G,H,K). Write P=O₂(G), Φ=Φ(P), V=P/Φ, W=P∩H and U=WΦ/Φ. The quotient is

```math
A=G/P=\prod_{i=1}^{e}\mathop{\mathrm{PGL}}\nolimits_2(q_i),\qquad e\geq1,
```

where each qᵢ is 9 or a Fermat prime at least 5, and the image B of H is the product of the corresponding Borel subgroups. Let C be the largest A-submodule of V contained in U. Let m count the nontrivial simple A-composition factors of V/C, with multiplicity, and put r=log₂|Φ|.

The canonical automorphism τ fixes H pointwise and inverts K. It acts trivially on V, but need not act trivially on Φ. A formal external involution is still used in G⋊⟨τ̂⟩ when τ itself is the identity. This distinction matters when lifting marked involutions.

The external envelope inputs are Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5. The internal module input is the [core-reduced Frattini theorem](../sources/bruck-completion/bruck-frattini-shadow.md): m≥1 and dim(V/C)≤B(A)m, where B(A)=[1+2ᵉ(3e+1)]|A|. In particular, the Frattini shadow is not asserted to be a faithful quotient folder.

## 2. Arbitrary radicals: an explicit fixed-parameter bound

Put R=Σᵢqᵢ(qᵢ−1)/2 and

```math
D=(r+1)B(A)m+(r+1)r^2[A:B]+r(R+3e+r).
```

Then dim V≤D, |P|≤2^(r+D), exp(P) divides 2^(r+1), and exp(X) divides 2^(r+2). There is **no nilpotency-class, elementary-abelian, central-Frattini, splitting or exponent-four assumption** on P in this assertion.

### Proof of the dimension bound

Let N=C_P(Φ). Since an automorphism of Φ is determined by at most r generator images, [P:N]≤2^(r²). The B-stable subspace U_N=(W∩N)Φ/Φ has codimension at most r² in U. Intersect the A-conjugates of C∩U_N to obtain C₀. There are at most [A:B] distinct conjugates, so c=dim C−dim C₀≤[A:B]r².

Let E=N∩π⁻¹(C₀), W₀=W∩E and Z_Φ=Z(Φ). Surjectivity of W₀→C₀ gives E=W₀Z_Φ. Consequently [E,E]=[W₀,W₀] lies in H. Since E is normal in G, this commutator subgroup lies in core_G(H)=1. Thus E is abelian; it is also τ-stable, and |E:W₀|≤2ʳ.

For a marked involution λ=τ̂k, let α be its action on E. If im(1−α) met W₀ nontrivially, conjugating λ by an element of E would give two distinct members of K in the same H-coset. This contradicts the section property. Therefore |im(1−α)|≤2ʳ and the induced quotient element t=kP has rank(1+t)≤r on C₀. The singleton-coordinate outer involutions generate A; their total number is R. Hence dim C₀≤dim C₀ᴬ+rR.

Let W₁ be the preimage of C₀ᴬ in W₀. For w∈W₁, the map gE↦gwg⁻¹w⁻¹ is a 1-cocycle G/E→Z_Φ. The assignment from W₁ to these cocycles is injective because its kernel is Z(G)∩H=1. Counting possible values on generators gives dim C₀ᴬ≤r·d(G/E). The quotient A has a generating set of size 3e, while log₂|P/E|≤r+v+c for v=dim(V/C). Thus d(G/E)≤3e+r+v+c. Adding dim V−dim C₀=v+c yields

```math
\dim V\leq(r+1)v+(r+1)c+r(R+3e+r)\leq D.
```

Finally p²∈Φ for p∈P gives the radical exponent bound. Since every k∈K has involutory or trivial image in A, k²∈P gives the loop exponent bound. See [the full argument and evidence scope](../sources/bruck-completion/bruck-all-radical-constraints.md).

## 3. What “parameterization for all radicals” means

At fixed A,r,m the preceding bound permits enumeration of finitely many radical groups, arbitrary nonabelian extension factor systems, stabilizers, involutive automorphisms, and marked conjugacy-class unions. The scheme then applies the actual transversal, generation, simplicity and nonassociativity tests. The equivalence relation preserves all the group and loop data; it does not identify objects merely because their quotient modules agree.

In particular, central C₂ towers are used to construct abstract P, **not** assumed to be G-stable. The extension system includes nonsplit groups. The simplicity test ranges over normal subgroups whose image in A is nontrivial as well as those in P. Exact isomorphisms consist of a radical isomorphism, quotient automorphism and cochain satisfying the extension identities and preserving H,K,τ. The full equations and rejection tests are in [the arbitrary-radical parameter scheme](../sources/bruck-completion/bruck-all-radical-parameterization.md).

This is exhaustive at the stated fixed parameters, conditional on the stated source interfaces. It is not an efficient implementation, a uniform finite census, or a proof that only finitely many parameter tuples survive. A,r,m remain unbounded.

## 4. Central Frattini subgroup: removal of the shadow core

Under the additional hypothesis Φ≤Z(G), the [central-Frattini core-vanishing argument](../sources/bruck-completion/bruck-central-frattini-all-quotients.md) proves C=0 for every allowed product quotient. Thus dim V≤B(A)m; the elementary central-Frattini estimate r≤d(d+1)/2, d=dim V, removes r as an independent size parameter in this subclass.

The proof splits simple local constituents into the principal heart and nonprincipal binary constituents. The latter use explicit modular-representation and torus-weight interfaces. The odd-order divisibility argument is applied **isotypically**; it is not valid for an arbitrary mixture of different odd orders. Product quotients require a local complement over one factor, not an unsupported global complement. The linked proof records the precise external representation inputs and their verification boundary. This remains a structural bound, not a classification of central-Frattini extensions or sections.

## 5. A local chief-factor obstruction without a class bound

Fix a local factor D=Aᵢ, Borel Bᵢ, marked nonsplit outer involution t, and an odd p-subgroup R≤C_D(t). Suppose a τ-invariant D-stable central elementary series of P has factors Lⱼ on which τ is trivial, satisfying:

- H¹(D,Lⱼ)=H²(D,Lⱼ)=0;
- restriction to Bᵢ is semisimple projective, with Lⱼᴮⁱ=0;
- H¹(⟨t⟩,Lⱼ)ᴿ=0.

Then the envelope cannot exist. Successive complement construction is aligned with the actual stabilizer. Odd-group orbit counting selects an R-fixed element in the **original** marked fiber; central lifting then conjugates it to a pure local marked involution, whose class forces a transversal collision. This is not a claim that every fixed quotient label automatically lifts to a fixed mark.

Applied to local nonprincipal chief factors with torus-weight orders d_L, the obstruction says that either a principal local chief factor occurs somewhere in P, or gcd_L(d_L)=1. For qᵢ=5,9,17 it forces a principal chief factor somewhere in P, not necessarily in P/Φ. For qᵢ=257, an all-nonprincipal case must include the appropriate coprime orders 3 and 43. See [the full theorem, lifting proof and exact hypotheses](../sources/bruck-completion/bruck-all-radical-block-obstruction.md).

## 6. Finer strata and computational boundaries

The source collection also contains abelian, class-two exponent-four, elementary-product, extraspecial and S₅-specific reductions. The S₅ module enumerations distinguish module covers and isotypes from actual envelope classification. The explicit V₆⊕U result assumes a faithful simple exponent-two Bruck envelope, quotient S₅ and that prescribed radical module, with the recorded N-block and fiber-bound inputs: its 485 isomorphism types of simple loops of order 1536 are **not** asserted to exhaust all loops of order 1536. The projective-family scheme at fixed multiplicity does not provide a census over unbounded multiplicities.

For noncentral N-Frattini branches, passive-block, quadratic-support and affine-residual reductions retain their hypotheses and unresolved lift conditions. A concrete b=3 obstruction rules out the specified encoded group/stabilizer models, not every quadratic model with similar dimensions. In particular, shadows, cocycles and residual graph data are not substitutes for preservation of the original group and section.

Useful entry points are [S₅ elementary parameters](../sources/bruck-completion/bruck-s5-elementary-parameterization.md), [V₆⊕U classification](../sources/bruck-completion/bruck-s5-v6-u-classification.md), [uniform principal support](../sources/bruck-completion/bruck-s5-uniform-principal-support.md), [noncentral passive reduction](../sources/bruck-completion/bruck-n-frattini-passive-reduction.md), and [the actual two-N lift residual](../sources/bruck-completion/bruck-two-n-cross-residual.md).

## 7. Remaining classification work

The universal Bruck scheme leaves unbounded quotient factors, radical/Frattini complexity, and composition-factor multiplicity. Finer branches still require extension, stabilizer, marked-section and isomorphism analyses. The non-Bruck Bol branch is a separate problem. The importance of this package is that arbitrary radicals now fit one finite-at-fixed-parameters framework, with explicit obstructions and auditable dependencies; it does not justify announcing a completed Bol classification.
