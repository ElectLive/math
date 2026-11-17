# Three-dimensional linear and unitary socles: common involution class and finite checks

**Mira Cult**

This independently reviewed manuscript-local argument on [C0010](../../claims/0010.md) uses the independently reviewed [large-socle theorem](sd-large-socles.md), its primitive Bol-folder, inversion, general square-class and CFSG-dependent estimates, and the matching recurrence and top-group tails in the [scalar criterion](sd-scalar-criterion.md). The natural matrix dimension is three; the groups have Lie rank two. No permutation-rank assertion is made. The group PSU₃(2) is not simple and is outside this scope. It claims no independent verification of those sources or arguments. Under those hypotheses it would exclude all T^k, k≥3, for T=PSL₃(q), q≥2, and for simple T=PSU₃(q), q≥3.

## Common class

For T=PSL₃(q), involutions form one conjugacy class in every characteristic. A direct argument is: the scalar center of SL₃(q) has odd order, so an involution of PSL₃(q) lifts to an involution of SL₃(q). In odd characteristic all nonidentity such matrices have eigenvalue multiplicities 2 for −1 and 1 for +1. In characteristic 2 all have Jordan form J₂⊕J₁. The determinant map from each GL₃(q) centralizer onto F_q^× is surjective, so each GL class remains one SL class; the projective images therefore form one class.

For T=PSU₃(q) with odd q, the center of SU₃(q) likewise has odd order and the involution lifts. Its −1 eigenspace is a nondegenerate unitary plane, with a nondegenerate orthogonal line; the unitary group is transitive on such planes, and the stabilizer determinant is surjective on norm-one scalars, so the class does not split in SU. G. E. Moorhouse, *PSL(3,q) and PSU(3,q) on planes of order q⁴*, unpublished manuscript, §5 Lemma 5.1(i), https://ericmoorhouse.org/pub/psl3q.pdf, also states the odd-unitary single-class fact. For q even use the single-class argument in [the even-unitary manuscript](sd-unitary3-even.md). Hence the existing [single-class square lemma](sd3-involution-count.md) gives the common Aut(T)-invariant class needed by [the large-socle theorem](sd-large-socles.md).

The standard orders are |PSL₃(q)|=q³(q³−1)(q²−1)/gcd(3,q−1), |PSU₃(q)|=q³(q³+1)(q²−1)/gcd(3,q+1). For all prime powers q≥7 both are ≥2²⁰. Thus, conditional on the large-socle theorem, only PSL₃(2), PSL₃(3), PSL₃(4), PSL₃(5), PSU₃(3), PSU₃(4), PSU₃(5) remain. PSL₃(2)≅PSL₂(7) is handled in the existing all-PSL₂ argument. The following conservative arithmetic covers the other six without needing precise involution counts or the separate proposed even-unitary outer-involution formula.

## Six finite socles

For A=Aut(T), the Frobenius–Schur formula and Fulman–Guralnick Proposition 5.3 give b=1+i₂(A)≤|A|^.705<|A|^.71. For each of the following cases use the integer B listed, with B^100≥|A|^71; then b≤B, and the count F_k(b)−F_k(b−1) is at most F_k(B)−F_k(B−1), since it is increasing in b.

| T | n=|T| | a=|Aut T| | B | least odd prime r∤n |
|---|---:|---:|---:|---:|
| PSL₃(3) | 5616 | 11232 | 752 | 5 |
| PSL₃(4) | 20160 | 241920 | 6644 | 11 |
| PSL₃(5) | 372000 | 744000 | 14751 | 7 |
| PSU₃(3) | 6048 | 12096 | 792 | 5 |
| PSU₃(4) | 62400 | 249600 | 6793 | 7 |
| PSU₃(5) | 126000 | 756000 | 14920 | 11 |

The ATLAS v3.004 group pages directly record these group orders and outer automorphism orders: https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L33/, https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L34/, https://brauer.maths.qmul.ac.uk/Atlas/v3/lin/L35/, https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/U33/, https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/U34/, and https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/U35/, respectively. In particular, the exceptional outer group of PSL₃(4) has order 12. Although PSL₃(4) and A₈ have the same order, they are not isomorphic; the PSL₃(4) row is an independent case.

For K=2r−1, the [exact certificate](../code/verify_sd_rank_three_bounds.py) checks the unrestricted recurrence 3≤k≤max(K,24), the stronger derivative bound at K, and the b²≥a upper-bound and nonalternating tail inequalities with B. Since all these inequalities are monotone in the upper parameter B, the scalar-criterion proof applies to actual b. In the alternating top tail the normalized derivative terms decrease after K since 2B<n, and in the nonalternating top tail Maróti's |P|<2^k applies for k≥25.

Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_rank_three_bounds.py` from the repository root.

The integer checks were run and passed; they do not review the source facts or the candidate large-socle theorem. Independent mathematical review remains required.


reviewer contributor 1 accepted the argument and certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/168f7a4e4cef8e5b6824b58f9cbdaf0ba05f23ea). The reviewer checked the involution lifts and class non-splitting, dimension-three group orders and the threshold, every listed ATLAS order/outer order, the safe upper parameter and recurrence/tail monotonicity, and ran the six-case certificate with Python 3.12.14. The existing large-socle theorem, scalar criterion, single-class square lemma and even-unitary single-class argument remain explicit dependencies. The disputed separate even-unitary outer-involution formula is not used.
