# Exclusion for even-characteristic PSU₃ socles in all SD_k

Mira Cult
This manuscript-local argument on [C0010](../../claims/0010.md) is conditional on the primitive left-Bol folder and inversion results and the [SD counting and semiregularity arguments](sd-a5-all-factors.md) at its recorded source revision. Under those upstream hypotheses, the conclusion is that no primitive SD_k left multiplication group has socle T^k with T=PSU₃(q), q=2^f≥4, and k≥3. This is an exclusion for one diagonal socle family, not a classification of primitive Bol groups. The field-involution count and all-parameter argument have the scoped independent review below.

## Unitary involutions

Put d=gcd(3,q+1), n=q³(q³+1)(q²−1)/d and a=2fdn. The standard automorphism structure Aut(T)=PΓU₃(q), with PGU₃(q):T of order d and Aut(T):PGU₃(q) the cyclic Galois group of order 2f, is recorded in Gareth A. Jones, *Finite simple automorphism groups of edge-transitive maps*, arXiv:2107.05137v1 (11 July 2021), §7, https://arxiv.org/abs/2107.05137v1. Paul Bradley and Peter Rowley, *Orbits on k-subsets of 2-transitive simple Lie-type groups*, Algebraic Combinatorics 5 (2022), Lemma 2.7(i)–(iii), https://doi.org/10.5802/alco.195, give n, the q³+1 isotropic points, and the Sylow 2-subgroup with its q−1 involutions in an elementary abelian center. Involutions of T are transvections and form one T-class: each is a nonidentity central element of a Sylow 2-subgroup, with a unique fixed isotropic point; the two-point stabilizer acts transitively on the q−1 nonidentity elements of that center, using its centralizer order in Lemma 2.7(ii). The isotropic points give (q³+1)(q−1) such involutions.

We claim that

    b:=1+i(Aut(T)) = 1+(q³+1)(q²+q−1).

First, PGU₃(q)/T has odd order d, so every involution in PGU₃(q) lies in T. If an involution lies outside PGU₃(q), its image in the cyclic Galois quotient is the unique element σ of order two, acting on F_(q²) by z↦z^q. We show all such involutions form one PGU₃(q)-class, of size q²(q³+1).

Choose a nondegenerate Hermitian form h on V=F_(q²)^3 whose matrix has entries in F_q, and write an involution outside PGU as the projective class of an invertible σ-semilinear map s=Aσ. As it preserves the projective unitary group, it is a semilinear similitude of h: for some μ∈F_q^×,

    h(sv,sw)=μ h(v,w)^q.

The scalar μ lies in F_q because both sides are Hermitian forms. Projective involutivity gives s²=λI, with λ∈F_q^×, and applying the displayed identity twice gives μ²=λ^(q+1)=λ². Characteristic two implies μ=λ. Choose c∈F_(q²)^× with c^(q+1)=λ⁻¹. Replacing s by cs preserves its projective class and makes it an antiunitary isometry with square 1.

By finite-field Galois descent, its fixed space W is a 3-dimensional F_q-space and V=W⊗_(F_q)F_(q²). The restriction h|_W is a nondegenerate symmetric F_q-bilinear form. Conversely, such a form determines an antiunitary involution. All nondegenerate symmetric bilinear forms in odd dimension 3 over the perfect field F_q are isometric: after diagonalization and rescaling, the diagonal form is I₃. Therefore every such projective s is PGU-conjugate to σ. The linear unitary centralizer of σ is O₃(q)≅Sp₂(q), of order q(q²−1): the invariant characteristic vector has an alternating two-dimensional orthogonal complement.

This remains the centralizer after projectivizing. Indeed, if a unitary representative u commutes with σ only projectively, then uσu⁻¹=cσ for a scalar c of unit norm. Multiplying u by a unit scalar z replaces c by z²c. The unit scalars form a group of odd order q+1, so choose z²=c⁻¹; the adjusted representative commutes with σ linearly. Thus the PGU centralizer has order q(q²−1), and the external class has size |PGU₃(q)|/[q(q²−1)]=q²(q³+1). Adding the inner count establishes the claimed b.

Jones §7 reports an outer involution class size q²(q−1)(q²−q+1) in a Singer-element discussion. For even q this differs from the count just derived (already at q=4); its hypotheses and the apparent discrepancy require source review. The present proof does not use that class-size formula. The independent review below checked the conjugacy and count argument, including lifting and the bilinear-form classification; the source conflict is retained explicitly.

The [single-involution-class square lemma](sd3-involution-count.md) gives I⊆(α^T)² for every nonidentity involution α∈Aut(T), so the fixed-identity counting lemma applies. This invocation retains the square-lemma source and review scope of that manuscript.

## Uniform exclusion for q≥128

The exact formula gives b≤2q⁵ and b≥q⁵/2. Also q⁸/4≤n≤2q⁸ and a≤12q⁹, because d≤3 and f≤q. Thus for q≥128, a≤b². Put x=b/n and y=a/n². Then x≤8/q³ and y≤24/q⁷.

Choose a prime r with q²+q+1<r<2(q²+q+1), by Bertrand's postulate. Since n=q³(q−1)(q+1)²(q²−q+1)/d, r∤n. Let K=2r−1<5q². The recurrence F_0(z)=1, F_1(z)=z, F_m(z)=zF_{m−1}(z)+(m−1)aF_{m−2}(z) satisfies F_k(b)−F_k(b−1)≤kF_{k−1}(b)≤k(b+√((k−2)a))^(k−1). For 3≤k≤K,

    [b+√((k−2)a)]/n ≤ 8/q³+√120/q^(5/2) < 1/2.

Hence the unrestricted count is below n^(k−1); in particular K F_{K−1}(b)<n^(K−1).

For k≥K and top image P≥A_k, the [forbidden-prime matching argument](sd-a5-all-factors.md) leaves at most j≤(r−3)/2 transpositions. The normalized j-th derivative summand at consecutive k has ratio [(k+1)/(k−2j)]x≤[2r/(r+2)]x<1. The sum at K is at most K F_{K−1}(b)/n^(K−1)<1, so it remains below one. For P not containing A_k and k≥25, Maróti, *On the Orders of Primitive Groups* (2002), Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k; this is a classification-dependent input. Because a≤b², the coset count is <2k(2x)^(k−1)<1, decreasing for k≥25. All smaller k are already covered. Both top cases contradict |Λ|=n^(k−1).

## Exact small-field certificate

For q=4,8,16,32,64, the following integer computation takes the least odd prime r not dividing n, checks the full unrestricted count for 3≤k≤max(2r−1,24), checks the derivative bound at 2r−1, and checks the a≤b² and nonalternating-tail inequalities. The matching and monotonicity arguments above then apply to all larger k. It uses the proposed b formula, so it is not independent evidence for that formula.

```python
from math import gcd, isqrt

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

for f in range(2,7):
    q = 2**f
    d = gcd(3,q+1)
    n = q**3*(q**3+1)*(q*q-1)//d
    a = 2*f*d*n
    b = 1+(q**3+1)*(q*q+q-1)
    r = next(p for p in range(3,100) if prime(p) and n%p)
    K = 2*r-1
    M = max(K,24)
    F, E = [1,b], [1,b-1]
    for k in range(2,M+1):
        F.append(b*F[-1] + (k-1)*a*F[-2])
        E.append((b-1)*E[-1] + (k-1)*a*E[-2])
    assert all(F[k]-E[k] < n**(k-1) for k in range(3,M+1)), q
    assert K*F[K-1] < n**(K-1), q
    assert a <= b*b and 2*b < n
    assert 50*(2*b)**24 < n**24
    assert 2*b*26 <= n*25
print('passed')
```

The certificate was run with Python 3 and passed. The finite arithmetic and new argument have the independent review below, under the stated upstream dependencies.

## Source verification and limitations and finite control

At exact revision the recorded source revision, a separate automated checker accepted the all-q, all-k argument conditional on the stated folder, inversion, square-class and CFSG-dependent primitive-group inputs. The reviewer checked semilinear normalization, descent, the symmetric-form classification, projective centralizer and all bounds, and ran the five-field integer certificate with Python 3.12.14. The reviewer directly inspected the conflicting Jones statement and did not use it to corroborate the new count.

A separately written [GF(16) matrix enumeration](../code/verify_unitary3_q4_involutions.py) enumerates all 312000 unitary matrices and 62400 projective classes. Directly testing A times its fourth-power conjugate for being scalar gives 1040 projective semilinear involutions; there are also 60 unitary matrices with entries in F₄. The producer ran Python 3.12.14. Independent reviewer a separate automated checker accepted this certificate at its recorded source revision, inspecting its field arithmetic, exhaustive orthonormal-basis construction, matrix-product convention, scalar quotient and coverage of projective similitudes. Python 3.12.14 reproduced the counts. The direct count of 1040 is independent of the separately printed quotient 62400/60; the code does not by itself prove projective-centralizer equality or the all-q formula.
