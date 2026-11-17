# Exact raw-F3 checks for finite symplectic residuals

**Mira Cult**

For T=PSp4(q), let n=|T|, a=|Aut(T)| and b=#{x∈Aut(T):x²=1}. The independently reviewed [raw-F3 criterion](sd-raw-involution-count.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499) excludes all primitive SD_k, k≥3, under its stated folder, semiregularity and CFSG-dependent inputs whenever n≥2²⁰ and b³+3ab<n². The following exact counts and applications have the scoped review below.

## Odd fields

Write q=p^f and n=q⁴(q²−1)(q⁴−1)/2, a=2fn. For q odd the inner-diagonal group PGSp4(q) is isomorphic to SO5(q); see Giudici–Glasby–Praeger, arXiv:2012.07213v1 §3.1. The full automorphism group is PGSp4(q) extended by field automorphisms; see Kleidman–Liebeck, Theorems 2.1.3–2.1.4 and Table 2.1.B, pp.15–16, https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf. Its involutions in SO5 have nondegenerate −1-eigenspace of dimension 2 or 4. For each dimension the two isometry types are transitive under SO5, and orthogonal-group order formulas give total class sizes q⁴(q²+1) and q⁴ respectively. Thus PGSp4(q) has q⁴(q²+2) involutions.

For q=5,7 there is no field coset. For q=9, the involutions in the single field coset all form one PGSp4(9)-class, with centralizer PGSp4(3), by Burness, *Fixed point ratios in actions of finite classical groups II*, Proposition 3.43(i)–(ii), p. 22, https://seis.bristol.ac.uk/~tb13602/docs/fpr2.pdf. Its order is 2n/51840=66420. Equivalently this follows from Lang, *Algebraic Groups over Finite Fields*, Amer. J. Math. 78 (1956), §2 Proposition 3, p. 559, https://wstein.org/papers/bib/Lang-Algebraic_Groups_Over_Finite_Fields.pdf. Hence b=1+q⁴(q²+2) for q=5,7 and b=1+9⁴(9²+2)+66420 for q=9.

## Even fields

For q=2^f>2, n=q⁴(q²−1)(q⁴−1), a=2fn, and Out(T) is cyclic of order 2f. It has one involution coset. By Burness, Proposition 3.43(i)–(ii), Remark 3.44 and proof of Proposition 3.52 in the source above, all its involutions form one T-class, with centralizer Sz(q) for f odd and Sp4(√q) for f even. Thus their count is n/c, c=q²(q²+1)(q−1) for f odd and c=|Sp4(√q)| for f even.

The number of inner elements with square 1, including identity, is q⁶+q⁴−q². Indeed x=I+N and N²=0; symplectic invariance makes N self-adjoint with totally isotropic image. Rank 1 gives q⁴−1 choices. Rank 2 has image a Lagrangian plane U, of which there are (q+1)(q²+1); with U fixed, N corresponds to an invertible symmetric 2×2 matrix, of which there are q²(q−1). Including N=0 yields 1+(q⁴−1)+(q+1)(q²+1)q²(q−1)=q⁶+q⁴−q². Hence b=q⁶+q⁴−q²+n/c.

## PSp6(2)

The [ATLAS S₆(2), version 3.004](https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/S62/) gives n=1451520, Out(T)=1, and four involution classes with centralizer orders 23040, 4608, 1536, 384. Hence a=n and their class sizes are 63, 315, 945, 3780, giving b=5104 including the identity. Thus b³+3ab=155189039104 < 2106910310400=n².

## Integer certificate and scope

The [integer certificate](../code/verify_sd_symplectic_finite_residuals.py) checks all seven cases, including divisibility, the threshold and the strict inequality. Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_symplectic_finite_residuals.py
```

Python 3.12.14 printed `symplectic finite residual checks passed`. This verifies arithmetic, not the source inputs or mathematical arguments.

No generic-class-number screen failure is interpreted as a possible loop. Together with the [classical raw screen and its refined symplectic section](sd-classical-raw-bounds.md), the [finite common-class PSp4(3), PSp4(4) certificates](sd-finite-common-classes.md), and the [PSL₂ family](sd-psl2-all-factors.md) for PSp4(2)'s derived subgroup A₆, these calculations would cover every simple PSp₂ᵣ(q), r≥2, under the stated dependencies. PSp4(2) itself is nonsimple. This is a conditional proposed symplectic-family result, not a global census. The source, the linear-algebra classification, and the action on outer cosets remain subject to independent review.

## Scoped independent review and family conclusion

reviewer contributor 1 accepted this manuscript and the appended refined symplectic screen in sd-classical-raw-bounds.md at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9). The review checked the FG/Gallagher rational bounds and grid/tail coverage; odd SO5 involution counts; even square-zero rank-one/two counts; field and graph-field cosets against Burness Proposition 3.43(i)–(ii), Remark 3.44 and the proof of Proposition 3.52; and the ATLAS Sp6(2) data. Both pinned certificates passed independently with Python 3.12.14. Together with the separately reviewed small cases, these results exclude every simple symplectic socle in the stated SD_k setting, k≥3, conditional on the raw theorem, upstream folder results, prior finite common-class/PSL2 reviews and cited published inputs. No broader census or unrestricted Bol-loop classification is established.
