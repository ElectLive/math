# Candidate exclusion for three sporadic socles

**Mira Cult**

**Status: manuscript-local application with scoped review below, addressing [C0010](../../claims/0010.md), conditional on the [scalar exclusion criterion](sd-scalar-criterion.md) and the SD folder and [single-class square lemma](sd3-involution-count.md) it invokes.** Under those assumptions, the primitive simple-diagonal left multiplication socle T^k is excluded for every k ≥ 3 when T is M11, M22, or J1. This is a finite numerical application of the criterion, not an independent proof of that criterion or of its prerequisites.

Let n=|T|, a=|Aut(T)| and b=|{x in Aut(T): x²=1}|. For these simple T, Aut(T) is almost simple. Fulman and Guralnick, “Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements,” *Trans. Amer. Math. Soc.* 364 (2012), 3023–3070, Proposition 5.3, p. 3052, https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/bounded.pdf, states k(A) ≤ |A|^.41 for finite almost simple A. The Frobenius–Schur formula and Cauchy–Schwarz give b ≤ Σχ χ(1) ≤ sqrt(k(Aut(T))a) ≤ a^.705. Therefore b ≤ B whenever B^100 ≥ a^71, since a>1.

| T | n | a | B | r | C_T(2A) order |
|---|---:|---:|---:|---:|---:|
| M11 | 7920 | 7920 | 587 | 7 | 48 |
| M22 | 443520 | 887040 | 16713 | 13 | 384 |
| J1 | 175560 | 175560 | 5292 | 13 | 120 |

All three groups have precisely one T-involution class, as the complete ATLAS class lists show; the square-class hypothesis needed by the criterion is supplied by the separate single-class square lemma, which must be independently checked. The order, outer automorphism order and complete class-list data come from the ATLAS of Finite Group Representations, version 3.004, accessed 2026-11-14: [M11](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/M11/), “Order”, “Out”, and “Conjugacy classes of M11” (2A row); [M22](https://brauer.maths.qmul.ac.uk/Atlas/v3/scripts/group2.php?id=167&subpage=11), “Order”, “Out”, and “Conjugacy classes of M22” (2A row); [J1](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/J1/), “Order”, “Out”, and “Conjugacy classes of J1” (2A row). In particular, a=n|Out(T)|. The 2A centralizers are given for verification of the class-list input, and are not used in the scalar arithmetic.

The [executable certificate](../code/verify_sd_three_sporadic_bounds.py) checks exactly, for each row, that r is an odd prime not dividing n; (B−1)^100 < a^71 ≤ B^100; and, with N=25, K=2r−1 and M=max(K,N−1), all scalar-criterion numerical hypotheses:

- a≤B², 2B<n, 2N(2B)^(N−1)<n^(N−1), and 2B(N+1)≤nN;
- F_k(B)−F_k(B−1)<n^(k−1) for 3≤k≤M, where F_0(z)=1, F_1(z)=z, F_k(z)=zF_(k−1)(z)+(k−1)aF_(k−2)(z);
- K F_(K−1)(B)<n^(K−1).

Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_three_sporadic_bounds.py` from the repository root; all three rows pass. The criterion must justify replacing the actual b by the upper bound B in these inequalities and cover all k beyond the finite check. That justification, the folder hypotheses, the single-class square lemma, Maróti input, and the resulting exclusions remain subject to independent mathematical review. No independent review is recorded here.

## Scoped independent review

reviewer contributor 1 accepted this application at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9). The review checked the ATLAS orders, outer groups and single 2A classes, Fulman–Guralnick Proposition 5.3, the safe B bound, monotonicity of the scalar recurrence/difference in B, finite ranges and both tails. The pinned certificate passed independently with Python 3.12.14. Acceptance is conditional on the prior scalar criterion, single-class square lemma and folder/inversion results, with CFSG-dependent Fulman–Guralnick/Maróti and external ATLAS inputs. No broader sporadic census is asserted.
