# Candidate A₅ SD_k exclusion for every primitive top group

Mira Cult
This manuscript-local argument has scoped independent review under the hypotheses recorded below. It uses no new claim IDs. The all-factor-count conclusion uses CFSG through Maróti’s primitive-group bound; the alternating-top subargument does not invoke that bound. It is conditional on the folder and inversion results invoked in `problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/sd3-involution-count.md`; in particular, it does not independently establish the upstream loop-theoretic construction. The relevant existing interfaces are `finite-simple-non-moufang-bol-loops:C0010`, `:C0014`, and their C0001/C0007 dependencies. The earlier upstream source examined is the recorded source revision.

## Folder setting and semiregularity

Let a finite group G act faithfully and primitively on Ω, with point stabilizer H, and let its socle B=T^k, k≥3, act in simple diagonal type, with H∩B=Δ(T). Suppose there is an automorphism τ of G preserving B and a subset K⊆G with G=⟨K⟩, τ(x)=x⁻¹ for x∈K, 1∈K, and xKx⊆K for x∈K. Let G̃=G⋊⟨t⟩, where t²=1 and conjugation by t is τ, and put Λ=tK. Assume |Λ|=[G:H]=|T|^(k−1) and Λ²∩H={1}. These are precisely the folder hypotheses used below; their applicability to the loop question is a separate upstream obligation. The condition τ(B)=B makes the factor action of all of G̃ well-defined. Write P for the image of G, not G̃, on the k simple factors.

Every element of Λ is an involution. Moreover Λ is conjugation-invariant under G̃: τ(K)=K because x⁻¹=τ(x)∈K and τ²=1. For x∈K, conjugation of tK by x or x⁻¹ replaces K by xKx or x⁻¹Kx⁻¹, respectively, and these equal K: the inclusions follow from twisted-subgroup closure and equality from finiteness. Since K generates G, Λ is G-invariant; it is also t-invariant. Hence Λ² is G-invariant, so no nonidentity element of Λ² fixes a point of Ω, by Λ²∩H={1}.

More is true: for every z=λμ∈Λ², the cyclic group ⟨z⟩ acts freely on Ω. Indeed, for every integer r,

    z^(2r)   = (z^r λ z^(−r)) λ,
    z^(2r+1) = (z^r λ z^(−r)) μ.

Conjugation invariance puts both factors on the right in Λ. Thus every power of z lies in Λ², and every nonidentity power is fixed-point-free. Consequently |z| divides |Ω|=|T|^(k−1). In particular, for T=A₅ no z∈Λ² can have order divisible by 7. The order of its permutation of factors divides |z|.

The action of Λ on B by conjugation is injective. For C=C_G(B), normality and primitivity imply that nontrivial C is transitive. Since B is transitive, C is semiregular, hence regular. Its centralizer in Sym(Ω) is then regular, forcing the transitive group B within that centralizer to be regular, contrary to B∩H=Δ(T)≠1. Thus C=1. Two elements of tG inducing the same action on B differ by an element of C.

## General counting lemma

Suppose T has a single conjugacy class I of involutions and, for each nonidentity involutory α∈Aut(T), the square (α^T)² contains I. Let n=|T|, a=|Aut(T)|, and let i be the number of nonidentity involutions in Aut(T). Then every λ∈Λ has at least one factor fixed by its top permutation on which it acts identically.

Indeed, suppose otherwise. The top action of λ is an involution. On each fixed factor its restriction α is nonidentity and involutory, so any prescribed v∈I can be obtained as a product of two independent T-conjugates of α. On each transposed pair, write the action as (x,y)↦(θ⁻¹(y),θ(x)). Independent conjugation in the two factors allows a product of two B-conjugates of λ to have coordinates (v,v): choose g with g⁻¹θ(v)g=v, possible because automorphisms preserve the unique involution class. Choices on distinct cycles are independent. Consequently (v,…,v)∈(λ^B)²⊆Λ²∩Δ(T), a contradiction.

An involution on k points with j transpositions has f=k−2j fixed points and can be chosen in k!/(2^j j! f!) ways. Its transposed pairs have a^j possible factor isomorphisms, and its fixed factors have at most (i+1)^f−i^f assignments with an identity restriction. Injectivity gives

    |T|^(k−1) ≤ A_k := Σ_{j=0}^{⌊k/2⌋} k!/(2^j j! (k−2j)!) · a^j · [(i+1)^(k−2j)−i^(k−2j)].

Equivalently A_k=F_k(i+1)−F_k(i), where F_0(x)=1, F_1(x)=x, and F_k(x)=xF_{k−1}(x)+(k−1)aF_{k−2}(x). These are upper counts, not claims that every counted automorphism occurs in Λ.

## A₅ and top image containing A_k

**Candidate proposition.** In the above setting with T=A₅, no such folder exists if P≥A_k. Thus, conditional on the cited upstream loop-theoretic reduction, the corresponding primitive SD_k left multiplication groups are excluded for every k≥3. The extension below removes the top-group restriction for A₅; no claim about other socles is made here.

For A₅, Aut(T)=S₅, a=120, and i=25. The 15 involutions in T form one T-class I. If α is a transposition in S₅, the product of two disjoint transpositions in its A₅-conjugacy class is in I. If α is a double transposition, two distinct nonidentity members of one Klein four group have product in I. T-conjugation therefore gives I⊆(α^T)² in either case. Hence the counting lemma applies.

Suppose s is the top permutation of an element λ∈Λ, with j transpositions and f fixed points. Because P≥A_k and Λ is G-invariant, any A_k-conjugate of s is the top permutation of another element μ∈Λ. The S_k-conjugacy class of s is a single A_k-conjugacy class when j≥1: the centralizer of s contains an odd transposition, namely one of its transposed pairs. Consequently any conjugate in S_k can be used.

If j≥3 and f≥1, choose seven points on which s=(12)(34)(56) fixes 7, and choose a conjugate u agreeing with s outside those points and having u=(23)(45)(67) on them. Then su is a 7-cycle on those points. If f=0 and j≥7, choose fourteen points on which s=(12)(34)…(13 14), and a conjugate u agreeing elsewhere and having u=(23)(45)…(12 13)(14 1) there. Their union is a 14-cycle, so su has two 7-cycles on those points. In either case lift an even conjugator through G to obtain μ, and λμ has top permutation su; its order is divisible by 7, contradicting the semiregularity argument above.

For k≥13 this leaves only j≤2: the full-support exceptions with 3≤j≤6 have k≤12. Therefore the general count may be truncated at j=2. Using b^f−(b−1)^f≤f b^(f−1) when f≥1 and the fact that the difference is zero when f=0, one gets

    A_k^(≤2) / 60^(k−1)
      ≤ k (26/60)^(k−1) Σ_{j=0}² [120k²/(2·26²)]^j / j!.

Each summand is a positive constant times k^(2j+1)(26/60)^(k−1). For k≥13, its ratio at successive k is at most (14/13)^5(26/60)<1. At k=13 the entire right-hand side is exactly

    77838902394209021 / 1062882000000000000 < 1.

Hence the truncated upper bound is smaller than |Λ|=60^(k−1) for every k≥13.

For the remaining finite range, the recurrence gives the following exact arithmetic; in each row A_k<60^(k−1):

| k | A_k | 60^(k−1) |
|---:|---:|---:|
| 3 | 2311 | 3600 |
| 4 | 103071 | 216000 |
| 5 | 4672951 | 12960000 |
| 6 | 217254951 | 777600000 |
| 7 | 10391339071 | 46656000000 |
| 8 | 511542865311 | 2799360000000 |
| 9 | 25905323196871 | 167961600000000 |
| 10 | 1348261712420151 | 10077696000000000 |
| 11 | 72037502774184751 | 604661760000000000 |
| 12 | 3946796710617543471 | 36279705600000000000 |

This contradiction completes the conditional candidate proof.

## Extension to arbitrary primitive top group

Let k≥3, T=A₅, B=T^k, G primitive with B in its simple diagonal action, H a point stabilizer, and P the image of G on the k factors. The top action P is primitive. Indeed, B is transitive, so G=BH, and H induces P. Any nontrivial P-invariant partition of the factors gives a subgroup D of B consisting of tuples equal within each block, with Δ(T)<D<B. As H normalizes Δ(T), each h∈H acts on the factors by a permutation followed by the same automorphism of T on every factor. Thus H normalizes D, and HD is a subgroup strictly between H and G, contrary to primitivity. (The common-automorphism statement follows by applying h to each diagonal element.)

Suppose first that P does not contain A_k. Let π be the action of G̃=G⋊⟨t⟩ on the factors. Since τ preserves B, π(Λ)⊆π(t)P, a coset of P, even though π(t) need not lie in P. Thus there are at most |P| possible top permutations among elements of Λ. Each such permutation is an involution. If it has j transpositions and f=k−2j fixed points, the general counting lemma bounds the number of induced B-automorphisms by

    120^j (26^f−25^f) ≤ k·26^(k−1).

For f≥1 this follows from 26^f−25^f≤f·26^(f−1) and 120≤26²; for f=0 the left side vanishes. Injectivity of the action on B then gives |Λ|≤|P| k·26^(k−1).

By Attila Maróti, *On the Orders of Primitive Groups*, 2002 preprint, Corollary 1.2, p. 3, https://www.renyi.hu/~maroti/primitive.pdf, every primitive P not containing A_k satisfies |P|<2^k for k>24. In particular, for k≥33,

    |Λ|/60^(k−1) < 2k(13/15)^(k−1) ≤ 66(13/15)^32 < 1.

The middle inequality follows since the successive ratio is (k+1)13/(15k)<1 for k≥33. The final comparison can be checked exactly as 66·13^32<15^32. This contradicts |Λ|=60^(k−1).

For 3≤k≤32, no top-group estimate is needed. The unrestricted recurrence F_0(x)=1, F_1(x)=x, F_k(x)=xF_{k−1}(x)+120(k−1)F_{k−2}(x) gives A_k=F_k(26)−F_k(25)<60^(k−1) for each of these thirty integers. A complete exact-arithmetic certificate is:

```python
f26, f25 = [1, 26], [1, 25]
for k in range(2, 33):
    f26.append(26*f26[-1] + 120*(k-1)*f26[-2])
    f25.append(25*f25[-1] + 120*(k-1)*f25[-2])
assert all(f26[k] - f25[k] < 60**(k-1) for k in range(3, 33))
assert 66 * 13**32 < 15**32
```

If P contains A_k, the seven-cycle argument above covers every k≥3. Therefore these two cases conditionally exclude all A₅ simple-diagonal folders in this setting. The independent review recorded below covers this continuation, the external theorem’s application and the alternating-top argument. The external theorem is a nontrivial published-group-theoretic dependency, not a result established by the Python certificate.

## Evidence and remaining review

The table and rational value were calculated with Python 3 integer arithmetic from the displayed recurrence and formula. The proof has scoped independent review; those reviewers did not separately audit the upstream assumptions. The top-group hypothesis is on G's image P; no primitivity assumption is made for the top image of G̃. The resulting arbitrary-top exclusion remains conditional on the upstream folder and inversion results with the review scope below.

automated reviewers a separate automated checker accepted exact revision the recorded source revision conditional on C0001/C0007. The review checked diagonal conjugate products, injectivity, top primitivity, alternating-top cycle constructions, the arbitrary-top coset count, and exact arithmetic for k=3,…,32 and 66·13³²<15³² with Python 3.12.14. The reviewer directly inspected Maróti Corollary 1.2 and its CFSG reliance. This is a scoped mathematical review, not acceptance of upstream aggregate claims or general folder exhaustiveness.
