# Paired PSL₃ over prime fields with a large Singer prime

Mira Cult

**Independently reviewed continuation of [classification frontier](../../claims/0010.md).** Let p≥7 be prime and assume p²+p+1 has a prime divisor r>7. Put T=PSL₃(p). For every k≥1, in the faithful generated canonical setting G=T^k×T^k with inversion swapping the two blocks, the simple nonassociative Bol folders are as follows: none when p≡1 mod3, and exactly one loop-isomorphism class when p≡2 mod3, the path with a point/line parabolic and a Singer cyclic torus as endpoints. The latter has order |T|^k and is proper and non-Bruck by the reviewed path construction. No statement is made for other primes, prime powers or canonical socle actions.

## Dependencies and subgroup inputs

Use the [full-strip forest source](radical-free-strip-forests.md) reviewed, the [path construction and isomorphism law](radical-free-path-factorizations.md) and the recorded source revision, and the [support-parity source](radical-free-involution-support.md). The class-square interface uses the original H, not a projected quotient loop.

The maximal-subgroup input is Mitchell's classification as stated in Dieulefait–Vila, *On the images of modular and geometric three-dimensional Galois representations*, arXiv:math/0111043v1 (5 November 2001), §4, printed pp.6–7, items a)–j) ([versioned PDF](https://arxiv.org/pdf/math/0111043v1)). This includes the prime-field case t=1 used here. It attributes the list to H. H. Mitchell, *Determination of the Ordinary and Modular Ternary Linear Groups*, Trans. AMS 12 (1911), 207–242, DOI 10.2307/1988576. The original Mitchell theorem text and classification proof have not been independently inspected. The stated list is an explicit external dependency; no classification reproof is asserted.

Write d=gcd(3,p−1). A point or line parabolic has order P=p³(p−1)²(p+1)/d, and a Singer normalizer has order N=3(p²+p+1)/d. Other proper maximal types are split-triangle groups, conic stabilizers and exceptional groups of orders at most 360, whose prime divisors are at most 7. There are no proper subfield or unitary types when t=1; the list's subfield entry is used only for proper subgroups. Since r>7 divides p²+p+1, it divides none of p(p−1)(p+1) or the exceptional orders. Every proper r-bearing subgroup therefore lies in a Singer normalizer, of odd order. No proper subgroup contains both p and r. Every proper subgroup with full p-part p³ lies in a point or line parabolic, including p=7 because the exceptional subgroup's 7-part is only 7.

T has one involution class. An involution in the projective group lifts to one in SL₃(p) because its central kernel has odd order dividing 3. A nonidentity determinant-one involution has eigenvalues (−1,−1,1), and the GL-centralizer has arbitrary determinant, so its GL class is one SL class. This is also the involution input of the [three-dimensional source](radical-free-three-dimensional-linear-unitary.md), reviewed.

## Correlations reduce to paths

Let the forest have ℓ leaves and c components, and let R be its actual leaf group. Then |R|=|T|^(ℓ−c), with ℓ≥2c. The disjoint p/r supports each require at least ℓ−c leaves. Hence ℓ=2c, every component is a path, and exactly c leaves of each type occur. Each p-leaf carries full p³ and lies in a parabolic, while each r-leaf lies in a Singer normalizer. By the support-parity theorem, each component has at most one deficient Sylow-2 leaf. The odd r-leaves are deficient, so each path has exactly one of each type. Thus

R≤P₁×⋯×P_c×N₁×⋯×N_c,  |P_i||N_i|=3|T|/d.                         (1)

The point and line parabolics may vary with the component. No independence in R has yet been assumed.

## p congruent to one modulo three

Here d=3 and equality of orders in (1) forces R to be the full ambient product. Let ω∈F_p be a primitive cube root. The projective T-class represented by u=diag(1,ω,ω²) is inverse-stable and invariant under Aut(T). To verify this, the split diagonal centralizer has arbitrary determinant, so the GL class is one SL class. Multiplication by a central cube root permutes the eigenvalue triple; inversion and inverse transpose interchange ω and ω². The prime field has no nontrivial field automorphisms. Steinberg's inner/diagonal/graph description, with the source and scope pinned in the three-dimensional manuscript, accounts for every automorphism.

The Frobenius generator of a cubic Singer normalizer is represented in a normal basis by a 3-cycle matrix: it has determinant one and precisely these eigenvalues. Thus each N_i meets this class, as does every parabolic P_i. Choose elements of this class at both leaves and at every independent full strip in one component, and identity on all other components. Strip twists preserve the class, which is inverse-stable, so this produces a nonidentity member of H∩Λ². This contradicts the folder condition and excludes this congruence class of primes.

## p congruent to two modulo three

Here d=1, and R has index 3^c in the ambient product (1). Each N_i has a normal cyclic Singer torus C_i of order p²+p+1, prime to 3. Therefore C=∏C_i≤R: [C:C∩R] divides both |C| and the 3-power ambient index. Modulo C, write Rbar≤∏P_i×C₃^c. Its order is exactly ∏|P_i|.

Each P_i has no proper subgroup of 3-power index. Its normal p² unipotent radical lies in any such subgroup, by the coprime index argument. The quotient is GL₂(p). A subgroup of GL₂(p) with 3-power index meets SL₂(p) in 3-power index and contains its central involution and a Sylow p-subgroup. Dickson's prime-field list in Guralnick–Zieve, Appendix Theorem A.1 (pinned in [the PSL₂ source](radical-free-psl2-path-classification.md)), puts a proper p-bearing projective subgroup in a Borel; but a Borel has index p+1, even, which cannot divide a 3-power. Thus the SL₂(p) intersection is full. The determinant quotient has order p−1, prime to 3, so the GL₂(p) subgroup is full as well.

The no-proper-3-power-index property passes to products. If U≤A×B has 3-power index, the two indices [A:π_AU] and [B:U∩B] divide [A×B:U]. When both factors have the property, these indices equal one, and U=A×B. Induction applies to ∏P_i. Consequently Rbar projects onto this entire product. Since the projection preserves its order, Rbar is a graph of a homomorphism ∏P_i→C₃^c. This homomorphism is trivial, because a nontrivial image would supply a subgroup of 3-power index in some P_i. Hence

R=∏P_i×∏C_i.                                                       (2)

If c>1, a component's leaf projection has order |P_i||C_i|=|T|, contradicting the reviewed strict component inequality. Thus c=1. Tree gauges remove all twists, giving the standard path. The endpoint orders are coprime and multiply to |T|, so their product is an exact factorization.

There is one endpoint-pair orbit. Cyclic irreducible cubic tori are conjugate by linear changes of the field basis; the field-multiplication centralizer realizes every determinant through the surjective norm F_(p³)^*→F_p^*, so conjugacy can be chosen in SL₃(p). A Singer torus acts regularly on projective points: a nonidentity norm-one field multiplier fixes a projective point only if it lies in F_p^*, and the latter norm-one intersection is trivial because gcd(3,p−1)=1. It therefore acts transitively on the parabolics of either type. The graph automorphism interchanges points and lines. The reviewed path-isomorphism criterion gives exactly one loop class per k.

## Boundary and evidence

This is an analytic deduction with no computational certification. The coordinator inspected Dieulefait–Vila v1 §4; the original Mitchell classification remains an external, unreproved input. Independent reviews of this deduction are recorded below.

The disjoint-prime proof does not extend directly to square fields. For q=49, PSU₃(7) is a proper subgroup of PSL₃(49), and its order is divisible by both 7 and 43, while 43 divides q²+q+1. This follows from item g) of the same maximal list and the explicit unitary order formula. It refutes the proposed disjoint-support premise at q=49; it does not construct an additional folder or rule out another method.


## Independent review



## Recorded source review scope

Automated source reviewers an automated checker, `audit_c9_full` and an automated checker independently accepted the full deduction at exact source the recorded source revision. All checked the disjoint valuations and full p-parts, correlated-R support-parity use, invariant inverse-stable projective order-three class, no-3-power-index parabolics and products, graph elimination, connectedness, exact factorization and endpoint-orbit uniqueness. They retained the prime-field and r>7 hypotheses and verified the stated q=49 obstruction at the order-formula level. an automated checker and `audit_c9_full` directly inspected Dieulefait–Vila v1 §4, printed pp.6–7; an automated checker made no fresh primary-source inspection. None inspected or re-proved Mitchell's original classification. The acceptances are conditional on the pinned forest, support-parity, canonical-folder/path, Dickson, automorphism and maximal-list inputs. No new computation was used; these are model reviews, not human or formal certification.
