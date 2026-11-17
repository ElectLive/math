# Candidate uniform HS Case A exclusion for odd PSL4(q)

**Mira Cult**

Scoped independently reviewed result for [C0010](../../claims/0010.md) and [C0014](../../claims/0014.md), conditional on the stated Case A folder inputs, standard classical-group automorphism and finite-field form facts, and the displayed exact rational certificate: no factor-preserving HS folder has socle factors T=PSL4(q), for any odd prime power q. This does not concern arbitrary primitive types. It strengthens the q=3 calculation without contradicting the accepted single-pair obstruction: the latter does not impose the size and B-conjugacy closure of the entire Λ.

## The case q≡3 mod 4: involutory automorphism roster

Put n=|T|=q⁶(q²−1)(q³−1)(q⁴−1)/2, d=diagonal outer involution, g=inverse-transpose. Write q=p^f. Since f is odd, every involution in Aut(T) has trivial field component, and possible outer images are 1,d,g,dg. Here Out(T) is abelian: field automorphisms act trivially on the diagonal quotient of order two, and graph inversion acts trivially there as well. Standard full-automorphism and order data: Kleidman–Liebeck, *The Subgroup Structure of the Finite Classical Groups*, Theorem 2.1.4 p.16 and Tables 2.1.B–D pp.15,19, https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf. Define

 c1=q²(q−1)(q+1)²(q²+1), c2=q²(q−1)³(q+1)²,
 c3=|GL3(q)|/2, c4=|Sp4(q)|=q⁴(q²−1)(q⁴−1),
 c6=q²(q²−1)², c7=q²(q⁴−1).

The nonidentity involution T-orbits and centralizers are 1: c1,c2; d: c3; g: c4,c4,c6; dg: c7. The following derivation uses the cited automorphism description, finite-field classification of symmetric and alternating forms, and classical-group order formulas. The canonical bibliography is [REFERENCES.md](../foundations/references.md). For the symmetric-form classification see Jan Draisma, *Multilinear Algebra and Applications* (Fall 2015), Theorem 10.6.118, p. 75 of the [author notes](https://math-unibe.ch/jdraisma/publications/mlappl.pdf).

A projective involution represented by A has A² scalar. If the scalar is square, rescale A to an ordinary involution. Modulo projective sign, the nontrivial eigenspace multiplicities are 1+3 and 2+2. The first has nonsquare determinant and the second square determinant. If the scalar is nonsquare, the natural four-space has dimension two over Fq²=Fq[A], giving a single nonsplit PGL class; its determinant is square. In each case the determinant map on the GL centralizer is onto, so each PGL class is one PSL class. In the 2+2 case the projective centralizer additionally swaps equal-dimensional eigenspaces; in the nonsplit case it also contains field conjugation of Fq²/Fq, acting on two copies and having determinant +1. Counting these projective centralizers and intersecting with PSL yields the stated orders. For the reflection, the determinant-one block subgroup is isomorphic to GL₃(q), and its projection has kernel {±I}.

A graph-coset projective automorphism has form α=conj(A)γ, γ inverse transpose. Its square is inner conjugation by AA^(−T), so involutivity forces A^T=±A. Up to projective congruence there are two symmetric types and one alternating type. Every symmetric projective congruence stabilizer contains an isometric reflection of determinant −1, a nonsquare, so each of its two PGL orbits is already one PSL orbit. The alternating stabilizer is the group of symplectic similitudes, all of whose determinants are multiplier squared; it lies projectively inside PSL and its PGL orbit splits into two PSL orbits.

For the alternating case, PGSp₄(q) is contained in T and has order |Sp₄(q)|. For a symmetric form, the multiplier map of its orthogonal similitude group is surjective. Modulo scalars the projective similitude group has order |O₄^ε(q)|. The determinant of a similitude is ± its multiplier squared; reflections show both signs occur, and because −1 is nonsquare exactly half are in T. Hence the centralizer is |O₄^ε(q)|/2. The alternating form has square determinant (a Pfaffian square), and the plus/minus symmetric forms have square/nonsquare determinant respectively; this determines their graph or graph-diagonal coset.


Source applications and the form arguments need independent review.

## A common captured class

Let I be the T-class of t=diag(−1,−1,1,1). It is PGL-invariant, since its GL centralizer has surjective determinant. For every nonsymplectic involutory automorphism α, I⊂C(α)=(α^T)²:

* For split linear involutions, choose opposite-sign coordinates and a 2×2 skew permutation block w in SL4. Then α(w)w^-1=t in those coordinates.
* For nonsplit linear involutions take A=diag(M,M), M=[[0,d0],[1,0]] for nonsquare d0. With h=diag(I2,diag(1,−1)), hAh^-1=diag(M,−M) and their product projects to t. The determinant of h can be adjusted to one using C_GL4(A)≅GL2(q²), whose Fq determinant is the surjective norm; hence the factors are T-conjugate.
* For symmetric graph α_B, choose a basis with B block diagonal in dimensions 2+2 and t=diag(−I2,I2). The forms B and Bt have the same dimension and discriminant and are congruent over Fq. A congruence has determinant ±1, and an orthogonal reflection adjusts it to determinant one. Thus α_B and α_B c_t are T-conjugate, so t belongs to their product set. Both orthogonal types are covered.

The split 2+2 class I has only one T-orbit by determinant adjustment, making the class statement independent of representatives. No assertion is made that symplectic graph involutions capture I; indeed their failure for this q is part of the separate explicit-pair obstruction.

## Bounding all of Λ

For a hypothetical Case A folder, every λ∈Λ induces a pair of involutions (α,β)∈Aut(T)², with fixed outer difference δ∈{1,d,g,dg}; Λ has size n and is stable under B=T² conjugation. Its B-orbit products and Λ²∩H={1}, H∩B=Δ(T), give C(α)∩C(β)={1} for every λ. Moreover the map λ↦(α,β) is injective: two elements with equal action differ by an element of G∩C_ext(B)=C_G(B)=1. All these hold including identity coordinates.

Set A=n/c1+n/c2, D=n/c3, S=2n/c4, O=n/c6 and H=n/c7. Any nonidentity pair of nonsymplectic types is forbidden by the common I. Pairs in the same T-class are also forbidden: their captured sets agree and are nontrivial. Thus an upper bound on |Λ| in each case is

 δ=dg: 2H+2DS;  δ=g: 2(S+O)+2AS;
 δ=d: 2D+2SH;  δ=1: 1+2A+2SO+S²/2.

The last term counts the two ordered cross-pairs of the two symplectic classes; the same-class pairs are forbidden. These are conservative counts of automorphism pairs, not an assumption that all pairs occur. For each bound U, [the exact GAP certificate](../code/verify_hs_psl4_odd.g) forms 1−U/n over Q(q), substitutes q=3+x separately in numerator and denominator, and verifies all resulting coefficients are positive. It thus proves U<n for all real q≥3, not merely sampled prime powers. The script passes in GAP 4.15.1. The certificate constructs all four bounds directly from n and the centralizers, then asserts positivity of every shifted numerator and denominator coefficient; it does not verify the group-theoretic inputs. Independent review is still required. Contradiction to |Λ|=n.

Run `gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_hs_psl4_odd.g`. The coefficient checks use exact rational arithmetic.

## The case q≡1 mod 4: a common captured class

Let ζ∈Fq satisfy ζ²=−1. The class I of t=diag(−1,−1,1,1), with its PGL-invariance established above, lies in C(α) for every nonidentity involutory α∈Aut(T). For projective linear involutions, the split and nonsplit witnesses above apply unchanged. It remains to consider graph, field and graph-field automorphisms. The standard full automorphism decomposition is Kleidman–Liebeck, Theorem 2.1.4, p. 16, cited above.

For a graph involution α_B(x)=B x⁻ᵀ B⁻¹, Bᵀ=±B up to scalar. If B is symmetric, choose a basis in which B is diagonal and put w=diag(ζ,ζ,−1,1)∈SL4(q). Then α_B(w)w⁻¹=w⁻²=t. If B is alternating, take B=diag(H,H), H=[[0,1],[−1,0]], and w=diag(ζ,1,−ζ,1)∈SL4(q). Direct multiplication gives α_B(w)w⁻¹=ζ⁻¹diag(1,1,−1,−1), whose projective class lies in I. PGL conjugation preserves I, so the result holds for all representatives of the indicated form types.

If an involution has a nontrivial field component, then q=s² and its field component is φ:x↦x^s; the graph bit is either absent or present. Burness, *Fixed point ratios in actions of finite classical groups, II* (author manuscript, 8 July 2006), [author PDF](https://seis.bristol.ac.uk/~tb13602/docs/fpr2.pdf), Proposition 3.43(i), printed p. 22, says order-two elements of either field or graph-field coset are conjugate by the inner-diagonal group, here PGL4(q), to the standard field or graph-field involution. For φ choose z≠0 with z^s=−z, and put w=diag(z,z⁻¹,1,1)∈SL4(q); then φ(w)w⁻¹=t. For γφ, where γ is inverse transpose, choose z with z^(s+1)=−1 using norm surjectivity and use the same w; then γφ(w)w⁻¹=t. PGL invariance of I transfers these witnesses to every involution in the respective cosets.

Thus C0014's two nonidentity components both capture I, contradicting their required trivial intersection. Combining the two congruence cases gives the stated candidate exclusion for every odd q. The common-class argument in this section and the source applications await independent mathematical review.

## Independent review

reviewer contributor 1 accepted the conditional exclusion at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/32b5918c4b3fa3b2686185006b80d41b1ece76aa). The review checked the odd-field automorphism roster, centralizer factors and orbit splitting, nonsymplectic captured class and all four conservative pair counts for q≡3 mod 4, and the determinant-one linear, graph and field/graph-field witnesses for q≡1 mod 4. An independent GAP run verified all shifted numerator and denominator coefficient inequalities. The review retains the stated Case A folder/inversion, Burness, classical automorphism and finite-field form dependencies. Its scope is factor-preserving HS Case A for PSL₄(q) with odd q only, not all HS configurations or arbitrary primitive types.
