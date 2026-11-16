# An abelian-by-abelian monolithic exclusion

Mira Cult
Let p be an odd prime, T a finite abelian p′-group, A a finite abelian p-group acting on T, and θ an involution of L=T⋊A that stabilizes T and inverts A. Let 1→V→G→L→1 be any extension in which V is a faithful irreducible FpL-module, and let τ be an involution of G preserving V and inducing θ on L. Then (G,τ) is not the canonical left multiplication group and inverting automorphism of a finite simple nonassociative odd left Bol loop. The final section reduces arbitrary extensions to the split model used in the main proof.

This excludes a class of monolithic group/involution pairs, including nonsplit presentations; it does not settle the general monolithic question, nonabelian kernels or complements, or involutions with different action on A. Faithfulness and irreducibility imply that V is the unique minimal normal subgroup of G: every nontrivial normal subgroup either meets V nontrivially, hence contains it, or centralizes V and is trivial because C_G(V)=V. After the final section's reduction, the main proof uses G=V⋊L and τ=(τ|V,θ). The argument uses no quotient loop.

The inputs are the full-inverted-set and fixed-point formulas for canonical odd folders in [odd-folder-radicals](odd-folder-radicals.md), strict defect at the recorded source revision, and G=HG′ at the recorded source revision. The quotient multitransversal and overlap p-core theorem used below are in [odd-elementary-layer-obstructions](odd-elementary-layer-obstructions.md). Oddness of the canonical group uses the source application at the recorded source revision. The previous special paired-diagonal argument is retained separately in [odd-monolithic-paired-diagonal-exclusion](odd-monolithic-paired-diagonal-exclusion.md).

## Projected stabilizer and overlap

Suppose such a canonical folder exists, with stabilizer H. Its canonical group is odd, so T is odd. The final section disposes of T=1; assume T≠1, so V is a proper normal subgroup. Use the compatible split coordinates supplied there and put σ=τ|V. Set J=HV/V≤L, W=H∩V, C=J∩T, n=|A|=p^a, and δ=dim V_+−dim W. Strict defect gives δ>0. Since L/T=A is abelian, G=HG′ implies that J maps onto A. Coprime fixed-point lifting gives |C_L(θ)|=|C_T(θ)|, because θ inverts A and A has odd order. From |H|=|C_G(τ)| we obtain

|C|=|C_T(θ)|,     δ=a,     dim W=dim V_+−a.              (1)

In particular A≠1. The reviewed overlap theorem applies to X=J∩θJ: its full θ-inverted subset generates a p-group. The θ-stable p′-subgroup D=C∩θC≤X is therefore fixed pointwise by θ. Indeed every θ-inverted element of D is both a p′-element and an element of that p-group; coprime inversion decomposition in D then gives D=D^θ.

Put B=C+θC, using additive notation in T. The map C→B/D identifies B/D with two summands C/D and θC/D exchanged by θ. Consequently |B^θ|=|C|=|T^θ|; fixed-point exactness for the involution on finite odd groups implies (T/B)^θ=0. Thus θ acts as −1 on T/B. Since θ inverts A, the action of each element of A on T/B equals its inverse; its odd p-power order makes it trivial. Coprime averaging for the action of A on the abelian p′-group T now yields

T=B+T^A.                                               (2)

This uses neither [T,A]=T nor any assertion that the projected full inverted set is a loop transversal.

## Character freeness and divisibility

Extend scalars to an algebraic closure of Fp, and choose a T-character χ occurring in V. All such characters form a single A-and-Frobenius orbit. Compatibility of σ means χ^θ is in that orbit. If s∈A fixes χ|C as an actual character, then s also fixes χ|θC: apply θ, using θ(s)=s⁻¹, and the fact that A and Frobenius commute and χ^θ is an A-and-Frobenius translate of χ. It fixes χ|T^A automatically. By (2), s fixes χ on T, and the same holds for every A-and-Frobenius translate of χ.

It follows that [T,s] acts trivially on V; faithfulness makes s centralize T. The subgroup C_A(T) is a normal p-subgroup of L and acts trivially on every irreducible FpL-module. Hence faithfulness forces s=1. Thus A acts freely on the actual characters χ|C.

Because C is a p′-group, V and W decompose into C-isotypic pieces. J normalizes C and acts through A on its character types. The absolute multiplicities in W are constant along both A- and Frobenius orbits. The free A-action on these characters consequently gives

n divides dim_Fp W.                                     (3)

Here J-invariance of W is essential; C-invariance alone would not give the orbit multiplicities.

## The two involution types

Let d be the Fp-degree of χ and I≤A the stabilizer of its Frobenius orbit. The restriction V|T is a direct sum of m=[A:I] distinct T-isotypic summands, each of dimension d, permuted transitively by A. For the modular Clifford step, work first over an algebraic closure. The stabilizer in A of a T-character is a p-group, so its action on the corresponding nonzero character space has a nonzero fixed vector. Its A-translates span a nonzero L-submodule; irreducibility makes that span the whole module. The distinct translates lie in distinct T-character spaces, so each such space is one-dimensional. This construction also shows that an A-orbit of T-characters determines a unique irreducible L-module over the algebraic closure. Over Fp, the endomorphism ring of V is a finite field. Its separability implies that scalar extension of V to the algebraic closure is a multiplicity-free sum of Galois-conjugate irreducible modules; their character A-orbits are disjoint by the uniqueness just proved. Therefore every rational T-type occurs once in V, with dimension d. This establishes the stated summand dimensions without assuming semisimplicity of A. Freeness of A on actual T-characters also implies |I| divides d, so n divides md=dim V.

The involution σ permutes the summands by inversion followed by a translation on the odd abelian group A/I. Exactly one summand is fixed. On its character field, σ is a scalar times a field automorphism of order at most two.

If that field automorphism is nontrivial, d is even and the fixed space on this summand has dimension d/2: the scalar is removed by finite-field Hilbert 90. Paired summands contribute half their total dimension, hence dim V_+=md/2. Since n is odd and divides md, it also divides dim V_+. Equations (1) and (3) then give n|a, impossible for n=p^a with p odd and a≥1.

Otherwise σ is field-linear on the fixed summand. Since σ²=1, it acts there by ε=±1, so

dim V_+=d(m+ε)/2.                                      (4)

Its fixed character satisfies χ^θ=χ^b for some b∈A. Replacing χ by a suitable A-translate makes χ θ-fixed, using the unique square root in A. If sχ=χ^{p^e}, applying θ gives s⁻¹χ=χ^{p^e}; the free A-action on actual T-characters therefore gives s²=1 and s=1. Thus I=1 and m=n.

We next show that χ|C has the same degree d as χ. Since χ is θ-fixed, χ(C) and χ(θC) generate the same field, so the values on B generate the field of χ|C. Moreover θ acts as −1 on T/B, so t+θt∈B for each t∈T. Hence χ(t)²=χ(t+θt) is a value generated by χ(C). The image χ(T) has odd order, so squaring is bijective on it; consequently all χ(T) values lie in the field generated by χ(C). Thus χ|C has degree d. Every constituent of V|C has this degree, giving d|dim W. Equation (4) also gives d|dim V_+, so (1) yields d|a and d≤a.

Finally (1), (3), (4), m=n and oddness of n imply

n divides εd−2a.                                        (5)

The integer εd−2a is nonzero and has absolute value at most 3a. For odd p and a≥1, 3a<n except when p=3 and a=1. In that remaining case d|a forces d=1, but a nontrivial odd-order character cannot take values in F3×. Faithfulness makes χ nontrivial. This contradiction completes the exclusion.

The exact-source independent reviews are recorded below. The statement is a necessary exclusion for the displayed split group/involution model, not a classification of odd simple Bol loops or a proof of nonexistence of monolithic canonical envelopes.

## Removing the split-extension hypothesis

**Extension of the preceding exclusion, covered by the review below.** The conclusion holds for an arbitrary extension

1→V→G→L→1

with the same faithful irreducible F_p L-module V and an actual involution τ of G preserving V and inducing the specified θ on L. In particular, no abstract splitting or τ-compatible complement needs to be assumed.

Suppose first that T≠1. The subspace V^T is L-invariant because T◁L. Irreducibility makes V^T either 0 or V; the second possibility contradicts the faithful L-action. Thus V^T=0.

Form the formal semidirect product E=G⋊⟨τhat⟩. Its quotient by V is L⋊⟨θhat⟩. The inverse image U of T is normal in E, and V is its normal Hall p-subgroup. Schur–Zassenhaus gives a T-complement. It can be chosen normalized by the actual τhat: in the inverse image of T⋊⟨θhat⟩, the normal Hall subgroup V has a complement because the quotient has order 2|T|, prime to p. Its outside involution over θhat is V-conjugate to the actual τhat inside V⋊⟨τhat⟩. Conjugate the entire complement accordingly and take its T-part T₀. The action of T₀ on V is the specified T-action, so C_V(T₀)=V^T=0.

All T-complements in U are V-conjugate, and the Frattini argument gives E=V N_E(T₀). An element of V normalizing T₀ centralizes T₀: its commutators with T₀ lie in both V and T₀. Thus the kernel V∩N_E(T₀)=C_V(T₀) is trivial. The normalizer maps isomorphically onto L⋊⟨θhat⟩ and contains the actual τhat. Its inverse image of L is a τ-stable complement L₀≤G. The resulting isomorphism G≅V⋊L carries τ to (σ,θ), with no residual V-valued shear, so the preceding split-model exclusion applies.

If T=1, L=A is a p-group. Every irreducible F_p module for a finite p-group is trivial; faithfulness forces A=1. Then G=V is abelian, and its faithful transitive action is regular, so it cannot be the canonical left multiplication group of a nonassociative loop.

The Hall-complement input is the solvable normal Hall case of Schur–Zassenhaus, as in Craven, *Finite Group Theory*, Hilary Term 2012, §2.1, Theorem 2.1, printed p.22, recorded in [the all-radical obstruction manuscript](../bruck-completion/bruck-all-radical-block-obstruction.md#coprime-fixed-coset-input). This section uses the ordinary Frattini argument and does not require a quotient-folder construction. It and the preceding exclusion are covered by the exact-source reviews below; neither treats general monolithic envelopes outside the stated quotient/action hypotheses.

The result retains all stated quotient, action and faithful irreducible module hypotheses.

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

They checked the overlap fixed-point deduction, restricted-character freeness, modular Clifford descent, both involution types, equality of character fields, the final congruence and exceptional endpoint, and the normalizer split compatible with the actual τ. No computation, fresh primary-source audit or formal verification was performed. The result retains all stated quotient, action and faithful irreducible module hypotheses.
