# All A5-square embeddings in the binary symplectic minus action

**Independently reviewed bounded continuation of [0323:C0010](../foundations/research-C0010.md).** Let Q be a finite simple nonassociative loop whose full multiplication group is Sp₈(2) in its natural action on the 120 minus-type quadratic refinements of an eight-dimensional nondegenerate alternating F₂-space. Its actual canonical group G=LMlt(Q) cannot contain a normal subgroup N≅A₅×A₅. This treats every faithful embedding of N in Sp₈(2), and does not depend on completeness of the Li–Xia many-factor table or on an asserted tensor placement from that table.

The argument uses the actual action and the canonical identity G=HG′, where H=G₁. That identity was independently reviewed at `030ebb1d681efd8b12139efc7d0e3d4bdc9173ce` in [the almost-simple bridge](../odd-completion/nonbruck-almost-simple-radical-bridge.md). It holds for every finite simple nonassociative loop: HG′ is normal, and x↦LₓHG′ is a loop homomorphism to G/HG′ because Lₓᵧ⁻¹LₓLᵧ∈H. Simplicity and nonassociativity make the map trivial; its image generates the quotient, giving G=HG′. The separate factor-classification source correction is not used in this elementary identity.

## The complete eight-dimensional module alternatives

The characteristic-two A₅ simple-module roster is supplied by Boxer–Calegari–Gee–Pilloni, *Modularity theorems for abelian surfaces*, arXiv:2502.20645v1, §8.2 Lemma8.2.1, printed pp.181–182. Over an algebraically closed field the modules are 1, U, U^σ, W=U⊗U^σ, of dimensions 1,2,2,4. The two natural modules are Galois conjugate over F₄ and W is absolutely irreducible over F₂. Andersen–Oliver–Ventura, *Reduced fusion systems over 2-groups of small order*, AppendixA immediately before LemmaA.8, printed p.49 in the pinned author copy, also explicitly gives the three F₂-simple modules: 1, the four-dimensional restriction of the F₄ natural module, and the four-dimensional deleted permutation module. Exact versions and the actual source inspections are in [REFERENCES](../foundations/references.md). These module classifications remain external inputs.

For a direct product, absolutely simple modules are tensor products of the simple modules of its factors. Finite-field descent groups the absolute constituents into Frobenius orbits, each occurring once. These standard finite-dimensional algebra facts also follow by taking the semisimple quotient of the two group algebras, tensoring their full matrix components over a splitting field, and descending their Frobenius orbits. No semisimplicity of an arbitrary N-module is assumed.

An F₂-simple module on which both A₅ factors act nontrivially has dimension at least eight. At equality it is the restriction to F₂ of U⊗U or U⊗U^σ over F₄: their absolute dimension is four and each has a two-element Frobenius orbit. Every other two-factor tensor has larger descended dimension. The two relative twists differ by an automorphism of one A₅ factor, so have the same subgroup image up to a change of factor identification.

Let V be the faithful eight-dimensional natural N-module. Each simple factor of N must act nontrivially on at least one composition factor of V. Otherwise that A₅ factor would act by block upper-unitriangular matrices along a composition series, giving a homomorphism from A₅ into a finite 2-group, hence the trivial action. Dimension therefore leaves exactly two alternatives:

* V is the irreducible eight-dimensional tensor restriction above;
* V has two four-dimensional composition factors V₁,V₂, one supported on each A₅ factor.

In the second case the extension splits. Put A=A₅×1, B=1×A₅ and M=Hom_F₂(V₁,V₂). Then M^A=0, and the inflation–restriction sequence injects H¹(A×B,M) into H¹(A,M)^B. Since B acts only on V₂,

    H¹(A,M)=H¹(A,V₁*)⊗V₂,

whose B-fixed space is zero. Thus Ext¹_N(V₁,V₂)=0; the reversed extension vanishes in the same way. This proves V=V₁⊕V₂, including potentially nonsemisimple inputs. The distinct kernels of the two simple modules give Hom_N(V₁,V₂*)=0. Consequently every N-invariant alternating form is an orthogonal direct sum, and nondegeneracy makes both four-spaces nondegenerate.

## Both module alternatives make N intransitive

For an orthogonal direct sum, a quadratic refinement has Arf invariant equal to the sum of its two local Arf invariants. Minus refinements split into the two nonempty N-invariant sets of local signs (+,−) and (−,+). Hence N is intransitive, regardless of which four-dimensional modules occur or whether the larger G permutes their summands.

For the irreducible tensor module use V=F₄²⊗F₄² restricted to F₂, with alternating form

    b(x,y)=Tr_F₄/F₂((b₁⊗b₂)(x,y)).

The tensor form is alternating in characteristic two and is nondegenerate; the trace pairing preserves nondegeneracy after restriction of scalars. The commutant of N on this F₂-module is F₄. Indeed its absolute constituents form a two-element Frobenius orbit; alternatively an order-five element in the first SL₂(4) factor satisfies g+g⁻¹=ωI with ω∈F₄∖F₂, so any F₂-commuting endomorphism is F₄-linear, where the absolutely irreducible tensor commutant is scalar. All invariant bilinear forms therefore have the shape Tr(c(b₁⊗b₂)) with c∈F₄. Each nonzero one is alternating and nondegenerate. Scalar multiplication by a with a²c=1 identifies it with the displayed form. Thus the finite model below covers every symplectic form and both relative twists in the irreducible case.

The [standalone certificate](../code/verify_tensor_a5_minus_orbits.py) constructs F₄=F₂[ω]/(ω²+ω+1) and the tensor form, verifies its binary rank is eight, and enumerates all 256 quadratic refinements by their values on a fixed basis. It identifies the 120 refinements with exactly 120 zero vectors as minus type. The upper and lower elementary matrices of parameters 1,ω in each SL₂(4) factor generate the two natural factors; this follows from the elementary generators of SL₂ over a field. Their tensor permutations preserve the form and the minus set, as checked explicitly. Breadth-first orbit enumeration gives **two N-orbits of size 60**. Each individual factor is transitive on each of those two orbits, which the certificate also checks. This is an exhaustive finite action calculation on the stated module, not a loop census or a proof of the module classification.

## From the normal subgroup to the original loop

For every module alternative, C_Sp₈(2)(N)=1. In the tensor case the commutant is F₄ and a scalar c preserves the trace form only if c²=1, hence c=1. In the direct-sum case the cross-homomorphisms vanish. On an absolutely irreducible four-dimensional summand the commutant is F₂, so the only invertible scalar is 1. On a restricted-natural summand it is F₄ and all invariant forms are traces of scalar multiples of the natural alternating form, again giving c²=1. This proves the assertion for both four-dimensional module types.

Since N is normal in G≤Sp₈(2), conjugation embeds G in Aut(N); modulo N this embeds G/N in Out(A₅²)=C₂ wr C₂, a 2-group. Write P=G/N and let J be the image of H. From G=HG′ follows P=JP′. In a finite 2-group P′ lies in the Frattini subgroup, so J=P (otherwise a maximal subgroup containing J also contains P′). Therefore G=HN. In the original transitive action on G/H, this says that N is transitive, contradicting either of the two module alternatives above. This proves the proposed exclusion without assuming a quotient folder.

## Evidence and limits

Run with assertions enabled and Python3.11+:

    python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_tensor_a5_minus_orbits.py

The source is standard-library-only, deterministic and self-contained, with no files, random choices or network inputs. It establishes the stated finite tensor orbits; the direct-sum, extension-splitting, centralizer and canonical-loop arguments are written proofs. The result does not exclude every Sp₈(2) canonical factor or settle the full symplectic family. The coordinator read and ran the certificate with Python3.12.14; it returned the two60-orbit partition, representative parameters20,24 and both individual-factor orbit lengths60. Three independent mathematical/code reviewers accepted this exact source; their scope is recorded below.

## Independent mathematical and code review

Reviewers contributor 1, contributor 2 and contributor 3 independently accepted exact source `b8d09f1800271592c97d9e707dc08535994b22ce`, conditional on the stated module roster, finite-field representation and cohomology interfaces, and canonical-loop identity. All checked the complete eight-dimensional alternatives, cross-extension splitting, invariant forms and centralizers, the two intransitivity arguments, and the original quotient/transitivity contradiction. All read, extracted and independently ran the exact committed certificate under Python3.12.14, obtaining rank8 and two minus orbits of60, with each factor transitive on each orbit.

`review_paired_simple` freshly inspected Boxer–Calegari–Gee–Pilloni v1 §8.2 Lemma8.2.1; the other two retained the cited roster without a fresh primary inspection, and none freshly inspected the Andersen–Oliver–Ventura PDF in this review. None re-proved the external modular classification or certified wider Sp8(2) or C0010 coverage. These are independent model mathematical/code reviews, not formal GitHub approvals. They explicitly do not restore the separately withdrawn global many-factor dispatch acceptance at `864d262568e612f203e100b654375923f9940af0`.
