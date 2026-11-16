# Candidate scalar criterion and Sz(8) application

Mira Cult
This manuscript-local criterion on [C0010](../../claims/0010.md), continuing the [general SD counting argument](sd-a5-all-factors.md) at its recorded source revision. It assumes the same upstream primitive Bol-folder and inversion results as the all-PSL₂ manuscript. No new permanent claim ID is allocated. The large-top-group estimate uses the CFSG-based theorem of Maróti. The numerical criterion is logically conditional on those folder results and on the stated finite simple group hypotheses; computation alone does not certify them. The [single-involution-class square lemma](sd3-involution-count.md) supplies the square-class hypothesis under its stated assumptions; the criterion keeps it explicit.

## Criterion

Let T be a finite nonabelian simple group with one involution conjugacy class I, and suppose I⊆(α^T)² for each nonidentity involutory α∈Aut(T). Put n=|T|, a=|Aut(T)|, b=1+(number of involutions in Aut(T)), and choose any integer c≥max(b,⌈√a⌉) with 2c<n. Let r be any odd prime not dividing n, K=2r−1, and choose N≥25 such that

    2N(2c)^(N−1) < n^(N−1),       2c(N+1) ≤ nN.

Define F_0(x)=1, F_1(x)=x, and F_k(x)=xF_{k−1}(x)+(k−1)aF_{k−2}(x). If

    F_k(b)−F_k(b−1) < n^(k−1)  for all 3≤k≤max(K,N−1),
    K F_{K−1}(b) < n^(K−1),

then the upstream folder hypotheses exclude a primitive SD_k left multiplication group with socle T^k for every k≥3. All tests are finite exact integer comparisons. The test is sufficient; failure does not imply that such a group exists. Choosing r or N differently may improve a failed test.

Proof. For k in the finite range, the established fixed-identity lemma and factor-action injection give |Λ|≤F_k(b)−F_k(b−1)<n^(k−1), contrary to |Λ|=n^(k−1). The top image P of G is primitive: a nontrivial invariant partition of factors yields an H-normalized subgroup strictly between Δ(T)=H∩B and B, hence a subgroup strictly between H and G. Also π(Λ)⊆π(t)P, a coset, with at most |P| top permutations.

If P does not contain A_k and k≥N, Maróti, *On the Orders of Primitive Groups*, Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, gives |P|<2^k. For a top involution with j transpositions and f=k−2j fixed points, at most a^j(b^f−(b−1)^f)≤k c^(k−1) induced actions occur; the bound is zero when f=0. Thus |Λ|/n^(k−1)<2k(2c/n)^(k−1). This is <1 at k=N by the first test and nonincreasing thereafter by the second test.

If P contains A_k and k≥K, the forbidden-prime matching argument applies: a top involution with at least (r−1)/2 transpositions and a fixed point, or with at least r transpositions and no fixed point, would have an A_k-conjugate whose product has an r-cycle (respectively two r-cycles). The symmetric conjugacy class does not split in A_k because the centralizer contains an odd transposition. Lifting the conjugator through G and using Λ-invariance gives an element z∈Λ² whose order is divisible by r, impossible because Λ²∩H={1} and conjugation invariance imply that every cyclic power of z lies in Λ² and acts fixed-point-freely unless it is the identity. Therefore |z| divides |T|^(k−1). So only j≤(r−3)/2 remain. Bound their contribution by the terms

    U_j(k)=[k!/(2^j j!(k−2j−1)!)](a/n²)^j(b/n)^(k−2j−1).

At k=K their sum is at most F'_K(b)/n^(K−1)=K F_{K−1}(b)/n^(K−1)<1. For k≥K, U_j(k+1)/U_j(k)=[(k+1)/(k−2j)](b/n)≤[2r/(r+2)](b/n)<1, because b≤c<n/2. Thus the surviving sum is <1 for all k≥K. The two top cases cover every primitive top image.

## Sz(8)

Take T=Sz(8). Basheer, *On a group extension involving the Suzuki group Sz(8)*, Afrika Matematika 34 (2023), article 96, §1, https://doi.org/10.1007/s13370-023-01130-z, records |T|=29120=2^6·5·7·13 and Out(T)=C3; thus |Aut(T)|=87360 and every automorphism involution is inner. The ATLAS of Finite Group Representations, Sz(8) version 3.004, conjugacy classes and maximal subgroups, https://brauer.maths.qmul.ac.uk/Atlas/v3/exc/Sz8/, lists one involution class 2A with centralizer 64, hence 455 involutions, and lists a subgroup 2^{3+3}:7. Its normal elementary abelian subgroup 2³ contains distinct nonidentity u,v with uv another involution. Since the involutions form one T-class and all involutory automorphisms are inner, (α^T)² contains I for every nonidentity involutory α. Thus n=29120, a=87360, b=c=456. Set r=3, K=5, N=25. The following exact certificate verifies every numerical condition:

```python
n, a, b, c, r, N = 29120, 87360, 456, 456, 3, 25
K = 2*r-1
assert n % r and 2*c < n and c*c >= a and c >= b
assert 2*N*(2*c)**(N-1) < n**(N-1)
assert 2*c*(N+1) <= n*N
F, E = [1,b], [1,b-1]
for k in range(2, max(K,N-1)+1):
    F.append(b*F[-1] + (k-1)*a*F[-2])
    E.append((b-1)*E[-1] + (k-1)*a*E[-2])
assert all(F[k]-E[k] < n**(k-1) for k in range(3,max(K,N-1)+1))
assert K*F[K-1] < n**(K-1)
print('passed')
```

The source group data and square-class argument give a candidate exclusion for Sz(8)^k for all k≥3, conditional on the upstream folder/inversion results. The comparison certificate was executed with Python 3; the new proof and its source inputs have the scoped independent review below; the upstream hypotheses retain their own review scopes.

## Source verification and limitations

automated reviewers a separate automated checker accepted this argument at its recorded source revision, conditional on the stated folder/inversion hypotheses, the earlier fixed-identity counting lemma and the CFSG-dependent Maróti bound. The review checked the finite criterion and/or all-Suzuki inequalities as applicable, the top-coset count, forbidden-cycle argument, and directly inspected the cited Suzuki sources. The embedded Sz(8) integer certificate in the scalar-criterion manuscript passed with Python 3.12.14. This is a review of the displayed conditional argument, not an independent reproof of the external group results or a classification of all primitive Bol folders.
