# Candidate exact HS Case A pair obstruction for PSL4(q)

**Mira Cult**

This manuscript-local result with scoped independent review below for [C0010](../../claims/0010.md) concerns only the necessary pair conditions of [C0014](../../claims/0014.md); it does not construct a folder or loop. Let q≡3 (mod 4), T=PSL4(q), α a symplectic graph involution and β a projective reflection (a split PGL involution with 1- and 3-dimensional eigenspaces). Then both necessary conditions hold:

  C(α) ∩ C(β)={1},  |C_T(α)| |C_T(β)| > |T|,

where C(γ)=(γ^T)^2. Thus these conditions alone cannot exclude Case A for this family.

Write H=[[0,1],[-1,0]], J=diag(H,H), and take α([W])=[J W^(-T) J^-1]. For each element of C(α), an SL4 representative X satisfies XJ′=J′X^T for some nondegenerate alternating J′: before T-conjugation one may take J′=J and X=J W^(-T) J^-1 W^-1, while conjugation transports the form. Any polynomial in X is similarly self-adjoint relative to J′, hence has even rank, because its product with J′ is alternating. Also det(tI−X) is a square polynomial, by the Pfaffian of the alternating matrix (tI−X)J′. These properties persist under scalar multiplication and T-conjugation.

Represent β by D=diag(−1,1,1,1). After T-conjugating an element x∈C(β), which preserves membership in C(α), it has an SL4 representative X=D'D, where D' is SL4-conjugate to D. It fixes pointwise the intersection of the +1 hyperplanes of D and D', of dimension at least two. Thus its characteristic polynomial is (t−1)²(t²−at+1). If x also lies in C(α), since the center of SL4(q) is {±I}, either X or −X is self-adjoint; equivalently X is self-adjoint. Its characteristic polynomial is a square, forcing the remaining eigenvalues to be both +1 or both −1 (the latter statement holds over the algebraic closure, since the only possible reciprocal pairs with multiplicities even are 1,1 and −1,−1).

In the −1 case the +1 and −1 primary subspaces are orthogonal nondegenerate alternating planes. A self-adjoint endomorphism of an alternating plane is scalar, so X is conjugate in GL4 to diag(−I2,I2). This projective involution is not in C(α): if α([W])[W]^-1=[diag(−I2,I2)] for W∈SL4, then for a central scalar ζ∈Fq with ζ⁴=1 the alternating-form congruence is W J W^T=ζ^-1 diag(−I2,I2) J. Its Pfaffian gives det W=−ζ^-2. As q≡3 mod4, ζ=±1, contradicting det W=1. The full GL4 centralizer of diag(−I2,I2) has surjective determinant, so its PGL4-conjugacy class is one PSL4-conjugacy class; in particular the two scalar representatives give the same PSL4 class. Thus the Pfaffian argument excludes that whole projective class.

In the +1 case X is unipotent. Put N=X−I. Since X fixes a subspace of dimension ≥2, rank N≤2. Since N and N² are self-adjoint, both ranks are even; rank N²≤1, hence N²=0. If N≠0 then rank N=2 and im N=ker N. Let L and L' be the −1 eigenspaces of D and D'. Since im(D'D−I)⊆L+L', equality of dimensions gives im N=L+L'. In particular L⊆ker N, so D'D acts trivially on L. But D acts as −1 on L, hence D' does too, and L=L'. With a common −1 line, D'D−I has rank at most one, contradiction. Therefore X=I and x=1.

Finally C_T(α) contains PSp4(q), of order |Sp4(q)|/2. The block diagonal subgroup centralizing D in SL4 has order |GL3(q)|, and its image in T has order |GL3(q)|/2. As |T|=|SL4(q)|/2, the product of these lower bounds divided by |T| equals q(q−1)(q²−1)/2>1.

The explicitly displayed α and β suffice to demonstrate the obstruction. No classification of graph automorphisms, folder construction, or conclusion that an HS Case A loop exists is asserted. The independent mathematical review is recorded below.

## Independent review

contributor 1 accepted this explicit-pair obstruction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c314e6ed0153240a4712b08d59288501f560f977). The review checked Cartan-image self-adjointness and transported alternating forms, even polynomial ranks and the square characteristic polynomial, reflection-product eigenvalue and unipotent arguments, the Pfaffian obstruction with central ±I and determinant adjustment, and the centralizer-product lower bound. It establishes joint insufficiency of the two C0014 necessary tests in this family, not existence of a folder or a classification of automorphism types. No files were edited during the review.
