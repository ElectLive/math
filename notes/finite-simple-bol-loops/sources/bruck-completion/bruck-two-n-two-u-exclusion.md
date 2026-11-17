# Excluding the two-N, two-U P₆ shadow

**Mira Cult**

**Scoped exclusion**, continuing [0323:C0010](../../claims/0010.md). In the faithful simple nonassociative Bruck-envelope setting of [the multiple-N source](bruck-multiple-n-frattini.md), suppose $`G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, and

```math
Z=\Phi(P)\cong N^2,\qquad V=P/Z\cong P_6\oplus U^2.
```

Subject to the cited inputs and the new finite check below, no such envelope exists. This is not a loop-order census, a quotient-folder argument, or an exclusion for larger $`U`$-multiplicity.

The original marked-rank and fiber inputs are reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/123933cc594b601dd317d62b333a949d20431d35); the multiple-N transport, including the invariant-functional pushout and actual-lift conditions, is reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6fe18de73836f5babe8bff5be255ff80fc864fb7). The affine-fiber parity and the actual fixed-line polar constraint are independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3c3cafff03f9e9d79640b68f03883c22e57210d6). The paired module and full component solver inputs are in [the quadratic-support source](bruck-n-frattini-quadratic-support.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b40066d01085772606b1d1160d58c033b8ba3302). The finite enumeration and arbitrary-central-multiplicity stable-shadow bound have the independent exact-source reviews recorded below.

## Necessary shadow conditions

Let $`F\cong F_{20}`$, $`W=H\cap P`$, and $`\overline W\le V`$ be its injective shadow. The multiple-N dimension bounds and affine parity theorem give $`\dim W=14`$: its nonfixed $`F`$-part has three copies of the four-dimensional simple $`S=N|_F`$, and its fixed part is the entire two-dimensional $`F`$-fixed plane of $`P_6`$. In particular the fixed plane contains the $`S_5`$-fixed constant vector $`\mathbf1`$. The reviewed actual fixed-line obstruction gives

```math
\beta(\mathbf1,-)\ne0.                                        \tag{1}
```

The square map $`q:V\to N^2`$ has two linearly independent scalar coordinate maps: its values generate $`Z=\Phi(P)`$, and a dependence would put all values in a proper $`S_5`$-submodule of $`N^2`$. Because $`W`$ is elementary, both scalar maps and all their polar pairings vanish on $`\overline W`$.

For a selected marked involution over a transposition $`t`$, the original fiber bound gives $`\mathop{\mathrm{rank}}\nolimits\ell\le2`$. The intrinsic marked map $`d`$ has image in two copies of the natural two-dimensional $`\mathbb F_2S_3`$-module and has rank at most $`\mathop{\mathrm{rank}}\nolimits\ell`$. Thus at least one nonzero scalar central projection of $`q`$ has $`d=0`$. This is a necessary component condition, not a quotient-loop construction.

## Exact finite shadow test

The [verifier](../code/verify_bruck_two_n_two_u.py) imports the committed component solver [verify_bruck_n_quadratic_support.py](../code/verify_bruck_n_quadratic_support.py), which imports [verify_bruck_p6_frattini.py](../code/verify_bruck_p6_frattini.py) and [verify_bruck_one_m_noncentral.py](../code/verify_bruck_one_m_noncentral.py); it also directly imports the last file for the paired $`F`$-intertwiners. No temporary-path imports are used. It constructs the complete scalar quadratic space $`Q(P_6\oplus U^2,N)`$, of dimension 11: one $`P_6`$ component, two on each $`U`$, two on each $`P_6`$–$`U`$ cross, and two on the $`U`$–$`U`$ cross. The $`d=0`$ subspace has dimension 8. Each direct-sum quadratic map is determined by its summand maps and pairwise polar cross maps.

Choose compatible $`F`$-intertwiners and denote the five simple multiplicity coordinates by $`(x,D_1,Z_1,D_2,Z_2)`$, where $`x=P_{6,S}`$, $`D_i`$ is an $`F`$-complement to $`\mathop{\mathrm{soc}}\nolimits(U_i)`$, and $`Z_i`$ is that socle. The verifier exhausts all 155 binary 3-planes in this five-dimensional space. For each it includes both fixed vectors, evaluates each scalar quadratic map on a basis and every pair sum, and tests the polar condition. It retains a plane only if the solution space has dimension at least two, its intersection with $`d=0`$ has positive dimension, and (1) can hold for some solution. Every actual two-component map satisfies these necessary tests; no assertion of group-extension or section existence is made.

Exactly six planes survive. Every one has $`c=1`$, contains the pure $`x`$-coordinate, and has remaining part

```math
\langle Z_z,\;D_z+Z_w\rangle
```

for some nonzero binary multiplicity vector $`z`$ and some $`w`$. The verifier checks these last properties for every survivor. Their scalar solution spaces have dimension 6, their $`d=0`$ intersections dimension 5, and their possible $`\beta(\mathbf1,-)`$ images dimension 1.

The fixed plane and pure $`x`$ together form the entire $`S_5`$-module $`P_6`$. The two displayed $`F`$-simple copies span an $`S_5`$-submodule isomorphic to $`U`$: for $`g\in S_5`$, the difference between $`gD_s`$ and $`D_{gs}`$ lies in the corresponding socle, and the common top multiplicity $`z`$ places this correction in $`Z_z`$; the graph $`Z_w`$ is itself $`S_5`$-stable. Thus each surviving shadow contains an $`S_5`$-submodule

```math
A\cong P_6\oplus U,\qquad \mathop{\mathrm{rank}}\nolimits(1+t)|_A=3+4=7. \tag{2}
```


## Actual stable-shadow rank bound

The following extension of the reviewed one-N argument works for any central $`Z\cong N^a`$. If an $`S_5`$-submodule $`A`$ lies in $`\overline W`$, let $`E_A`$ be its full preimage in $`P`$, and $`W_A=W\cap E_A`$. Since $`W\cap Z=1`$, $`W_A`$ maps isomorphically onto $`A`$. Thus $`E_A=ZW_A`$ is elementary abelian; $`\tau`$ fixes it pointwise because it fixes $`Z`$ and $`H`$. For a selected marked involution $`\lambda`$ over $`t`$, the action of $`\lambda`$ preserves $`E_A`$. Put $`D=(1+\lambda)E_A`$. The original condition $`H\cap\Lambda^2=1`$ gives $`D\cap W_A=0`$. Moreover $`D`$ maps onto $`(1+t)A`$ and contains $`(1+t)Z`$, of dimension $`a`$. Hence

```math
\mathop{\mathrm{rank}}\nolimits(1+t)|_A+a\le\dim E_A-\dim W_A=4a,
 \quad\text{so}\quad \mathop{\mathrm{rank}}\nolimits(1+t)|_A\le3a.        \tag{3}
```

For $`a=2`$, (3) bounds the rank by 6, contradicting (2). Therefore the assumed envelope cannot exist, conditional on the stated inputs and the finite check.

Run the certificate with assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_two_n_two_u.py
```

Root read and ran the certificate with its committed imports using Python 3.12.14; all assertions passed, including the compatible top/socle coordinates and fixed-plane checks. Passing the finite check verifies the stated representation calculations; it is not independent mathematical review of the group argument or its cited source interfaces.

## Independent review

Three independent proof/code reviewers — `review_folder_criterion`, `review_psl2_allq` and `review_small_order_complete` — accepted the proof and certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/a1f42ac3a21ce22edef96845f6cdf379511b2a51), conditional on the cited envelope, marked-fiber, affine-parity, fixed-line and module-component inputs. Each extracted the exact committed verifier and its three imports to a separate temporary directory and ran Python 3.12.14. All obtained scalar dimension 11, d-zero dimension 8, all 155 planes and the stated six survivors, and checked the actual stable-shadow rank contradiction. These are model reviews and exact finite checks, not formal certification or a classification of larger multiplicities.
