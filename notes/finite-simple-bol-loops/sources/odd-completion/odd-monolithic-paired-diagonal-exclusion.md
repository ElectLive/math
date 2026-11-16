# A paired-diagonal monolithic exclusion

Mira Cult
This note excludes a specified infinite family of faithful irreducible monolithic group/involution pairs from the canonical envelopes of finite simple nonassociative odd left Bol loops. It does not assert that every monolithic envelope has this form, or settle the remaining monolithic case.

The odd-folder inputs are in [odd-folder-radicals.md](odd-folder-radicals.md): the full inverted set and |H|=|C_G(τ)| at the recorded source revision, strict defect for proper invariant normal subgroups at the recorded source revision, and the derived-envelope identity G=HG′ at the recorded source revision. Oddness of G uses the source application recorded at the recorded source revision. The earlier rank-two monolithic module obstruction and its group control have a scoped independent review at the recorded source revision; the present higher-rank deduction has the separate exact-source reviews below.

## Statement

Let p be an odd prime, q a prime with ord_q(p)=p, and a≥1. Put

T=(C_q)^{2a},       A=(C_p)^a,       L=T⋊A.

Index the T axes by (i,+),(i,−), 1≤i≤a. The i-th generator of A raises its + axis to the p-th power and its − axis to the p⁻¹-th power, and fixes the other axes. Let θ∈Aut(L) swap the two axes of every pair and invert A.

Let V be a faithful irreducible F_p L-module with an involution σ satisfying

σ ρ(l) σ⁻¹ = ρ(θl) for all l∈L.

Set G=V⋊L and τ=(σ,θ). Then this (G,τ) is not the canonical left multiplication group and inverting automorphism of a finite simple nonassociative odd left Bol loop.

Faithfulness is a genuine part of the model. Since V is irreducible and L acts faithfully, C_G(V)=V, and every nontrivial normal subgroup of G meets V and contains it. Thus G is monolithic with unique minimal normal subgroup V. This observation is context, not a substitute for the folder contradiction below. The argument also applies to faithful θ-compatible irreducible modules without separately assuming monolithicity.

## All compatible irreducible modules

Extend scalars temporarily to an algebraic closure of F_p and choose a T-character χ in V. As T is a p′-group, restriction to T is semisimple. Write its two coefficients in pair i as (u_i,v_i)∈F_q². Faithfulness forces both coefficients to be nonzero in every pair: A and Frobenius preserve zero coordinates, so a zero coordinate makes the corresponding normal T-axis act trivially on all of V.

The existence of σ means the swapped character θχ is in the A-and-Frobenius orbit of χ. Thus there are t_i,e∈F_p such that

v_i=u_i p^{t_i+e},          u_i=v_i p^{−t_i+e}.             (1)

All exponents here are taken modulo p. Multiplying the relations gives p^{2e}=1 modulo q; because ord_q(p)=p is odd, e=0. Hence each ratio v_i/u_i belongs to ⟨p⟩. An A-shift makes the two coordinates equal on every pair, since 2 is invertible modulo p. A diagonal automorphism of T scaling both axes of each pair by the same nonzero element commutes with A and θ and normalizes these equal coefficients to 1. Applying such an automorphism is only a change of model for the group/involution pair.

The stabilizer in A of the Frobenius orbit of the normalized character is trivial. Indeed, if an A-shift by j and a common Frobenius exponent e preserve both entries of any pair, then j_i+e=−j_i+e=0; p odd gives j_i=e=0, and the remaining coordinates give j=0. This also explains the modular Clifford step explicitly: the T-isotypic components belonging to the p^a distinct A-translates are permuted transitively, and no nontrivial A element stabilizes a component. Any nonzero T-submodule of one component therefore induces the whole irreducible L-module, with no additional inertia-group representation. Each component is the irreducible p-dimensional F_p representation of T afforded by a Frobenius orbit of χ.

Consequently V is isomorphic to

V=⊕_{j∈F_p^a} E e_j,        E=F_{p^p},

where T acts on e_j with exponent vector

(p^{j₁},p^{−j₁}, …, p^{j_a},p^{−j_a}),

and A translates the index. Commuting with T makes an L-endomorphism scalar on each E-summand; commuting with the transitive A-action makes the scalar common. Hence End_L(V)=E. Let σ₀ be the E-linear index reflection e_j↦e_{−j}. Every θ-intertwiner is dσ₀ for some d∈E×, and σ₀ is E-linear; σ²=1 therefore gives d=±1. For ε∈{+1,−1},

dim_Fp V₊ = p(p^a+ε)/2.                                  (2)

The − sign is essential: it changes the contribution of the unique fixed index from +p to −p.

## Full projection and Clifford block sizes

Suppose for contradiction that (G,τ) is a canonical simple odd folder with stabilizer H. Put J=HV/V≤L and W=H∩V. Since [T,A]=T and [V,T]=V,

G′=V⋊T,       G/G′=A.

The reviewed identity G=HG′ therefore forces J to project onto all of A. Because θ inverts A, C_L(θ) lies in T and has order q^a. Coprime fixed-point lifting in 1→V→G→L→1 and |H|=|C_G(τ)| give

|J|=p^δ |C_L(θ)|,       δ=dim V₊−dim W.

The p-part of J has order p^a, so δ=a. Strict defect supplies δ>0. In particular

dim W=p(p^a+ε)/2−a,       |J∩T|=q^a.                     (3)

Let C=J∩T. It is invariant under all of A: J covers A and T is abelian. The 2a A-characters on T are the distinct characters ±the a coordinate characters, all defined over F_q. Therefore C is the direct sum of exactly a T-axes. Let b be the number of paired coordinate positions touched by C; then b≥⌈a/2⌉.

If C contains both axes of at least one pair, the restricted C-character types of the T-summands in V are indexed by their b active A-coordinates. Indeed equality up to one common Frobenius power on the complete pair forces that power and the difference of its A-index to be zero; all other active indices then agree. There are p^b distinct irreducible F_p C-types, each of degree p.

If C contains no complete pair, then it contains exactly one axis from each pair. Two restricted characters have the same Frobenius orbit precisely when their index differences are given by one common shift with the sign of the selected axis. There are p^{a−1} irreducible F_p C-types, each of degree p.

In both cases A permutes these types transitively. Because C is a p′-group, W decomposes into its C-isotypic pieces, and J-invariance makes all those pieces have equal F_p dimensions. For a≥2, the number of types is divisible by p^{⌈a/2⌉}; each piece has dimension divisible by p. Hence

p^{⌈a/2⌉+1} divides dim_Fp W.                             (4)

This counts F_p dimensions even when several T-summands coalesce into one C-isotypic piece. No assertion that W is a sum of whole T-summands is used.

## Contradiction and scope

Combining (3)–(4), and using a≥⌈a/2⌉, gives

2a ≡ εp (mod p^{⌈a/2⌉+1}).                               (5)

For a≥2, the integer 2a−εp is nonzero and has absolute value strictly less than the modulus, a contradiction. For a=1, C is one nontrivial q-axis; every irreducible F_p C-constituent has dimension p, so p divides dim W, while (3) gives dim W≡−1 mod p. This contradiction completes the exclusion for both signs of σ.

The proof uses no search or loop multiplication table and makes no quotient-folder inference. It does not cover nonsplit G/V, non-elementary q-layers, different actions of the p-quotient, or involutions that act differently on T or A. The full monolithic branch and the general odd classification remain open. The exact-source reviews below cover the modular descent, both signs and the use of the cited interfaces.

The scope remains the specified split paired-diagonal model.

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

They checked exhaustion and descent for all faithful compatible irreducible modules, both signs of σ, full A-projection, complete-pair and single-axis C-type counts, and the resulting dimension contradiction. No computation, fresh primary-source audit or formal verification was performed. The scope remains the specified split paired-diagonal model.
