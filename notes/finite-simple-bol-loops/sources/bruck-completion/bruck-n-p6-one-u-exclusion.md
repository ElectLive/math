# Excluding the P₆ plus one U N-Frattini shadow

**Mira Cult**

**Theorem with scoped independent reviews, continuing [0323:C0010](../../claims/0010.md).** In the faithful simple nonassociative Bruck-envelope setting of [the marked-rank theorem](bruck-n-frattini-marked-rank.md), suppose $`G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, $`\Phi(P)=Z\cong N`$, and

```math
P/Z\cong P_6\oplus U.
```

Conditional on the central-socle and invariant-functional deductions in [the independently reviewed obstruction](bruck-n-central-socle-obstruction.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/bf11794257554b943a1b26ca15acd861f9faaa7f), on the reviewed marked-rank and quadratic-component inputs there, and on the finite identity checked below, no such envelope exists. The theorem and certificate have the scoped exact-source reviews below. This excludes one shadow, not the remaining $`N`$-Frattini family.

## The fixed vector and the finite cross-map identity

Let $`F=H/(H\cap P)\cong F_{20}`$, $`W=H\cap P`$, and $`\overline W\le V=P/Z`$ be its injective shadow. The invariant-functional obstruction gives $`\dim W=9`$: the nonfixed $`F`$-part of $`\overline W`$ has two copies of the four-dimensional simple $`S=N|_F`$, and its fixed part is an augmentation-one fixed line in $`P_6`$. The two augmentation-one $`F`$-fixed vectors in $`P_6`$ are interchanged by the $`S_5`$-module automorphism $`1+J_{\rm all}`$, so choose coordinates in which this vector is the singleton $`f`$ fixed by $`F`$.

Choose compatible $`F`$-isomorphisms $`P_{6,S}\cong S`$, $`D\cong S`$, and $`\mathop{\mathrm{soc}}\nolimits(U)\cong S`$, where $`U|_F=D\oplus\mathop{\mathrm{soc}}\nolimits(U)`$, and write $`\iota:S\to N`$ for the nonzero intertwiner. The $`d=0`$ marked-rank condition leaves a two-dimensional space of $`S_5`$-equivariant $`P_6`$-to-$`U`$ polar maps. It has a basis $`\beta_0,\beta_1`$ with

```math
\begin{aligned}
 \beta_0(f,D_s)&=\iota(s),&\quad \beta_0(f,\mathop{\mathrm{soc}}\nolimits_s)&=0,&\quad \beta_0(P_{6,S},U|_F)&=0,\\
 \beta_1(f,D_s)&=0,&\quad \beta_1(f,\mathop{\mathrm{soc}}\nolimits_s)&=\iota(s),&\quad \beta_1(P_{6,S},\mathop{\mathrm{soc}}\nolimits(U))&=0,\\
 &&&\quad \beta_1(P_{6,S},D)&\ne0.                              \tag{1}
\end{aligned}
```

Here the final inequality concerns the full bilinear restriction, not its diagonal. The independent $`U`$-square map is $`\mathop{\mathrm{top}}\nolimits:U\to N`$, and $`q|_{P_6}=0`$.

The standalone [certificate](../code/verify_bruck_n_p6_one_u.py) derives (1): it imports [the reviewed fixed-component equation solver](../code/verify_bruck_n_quadratic_support.py), including its [P₆ model](../code/verify_bruck_p6_frattini.py), and the $`F_{20}`$ generators and paired actions from [the one-M model](../code/verify_bruck_one_m_noncentral.py). It solves the full equivariance and marked $`d=0`$ equations for the cross-map space, solves the $`F`$-intertwiner equations for $`P_{6,S},D,\mathop{\mathrm{soc}}\nolimits(U)`$, verifies the fixed vector and its independence from $`P_{6,S}`$, and checks every restriction in (1), including the nonzero full bilinear map. It also checks that the remaining $`U`$-square map is top and has zero polar. These computations do not test existence of an envelope or certify the imported prior mathematical interfaces.

## Exclusion

Write the cross term as $`r_0\beta_0+r_1\beta_1`$, with $`r_0,r_1\in\mathbb F_2`$, and its $`U`$-square row as $`\ell\in\mathbb F_2`$. The nonfixed $`W`$-shadow has the form $`S\otimes B`$, with $`B`$ a two-dimensional subspace of the multiplicity space with coordinates $`(x,d,z)`$ for $`P_{6,S},D,\mathop{\mathrm{soc}}\nolimits(U)`$.

If $`(r_0,r_1)\ne(0,0)`$, the actual elementary group $`W`$ is abelian, so (1) and $`f\in\overline W`$ force

```math
B\subseteq\ker(r_0d+r_1z).
```

Both sides have dimension two, hence

```math
B=\mathop{\mathrm{span}}\nolimits\{P_{6,S},\ r_1D+r_0\mathop{\mathrm{soc}}\nolimits(U)\}. \tag{2}
```

If $`r_1=0`$, (2) puts the entire $`U`$-socle in $`\overline W`$. It is polar-radical: $`\beta_0`$ vanishes on the socle, the single $`U`$-square map is linear, and there is no $`U`$-pair term. This contradicts the actual-lift obstruction. If $`r_1=1`$, (1) gives

```math
\beta(P_{6,S},D+r_0\mathop{\mathrm{soc}}\nolimits(U))
 =\beta_1(P_{6,S},D)\ne0,
```

contrary to abelianness of $`W`$. Thus $`r_0=r_1=0`$.

The entire $`U`$-socle is now polar-radical, so the actual-lift obstruction gives $`B\cap\mathop{\mathrm{soc}}\nolimits(U)=0`$. Since $`\dim B=2`$, its projection to the multiplicity space of $`P_{6,S}\oplus\mathop{\mathrm{top}}\nolimits(U)`$ is onto. With the cross row zero, the only remaining possible square map is $`q=\ell\mathop{\mathrm{top}}\nolimits`$. Its vanishing on the actual elementary subgroup $`W`$ forces $`\ell=0`$. Hence $`q=0`$, its polar $`\beta=0`$, and

```math
\Phi(P)=P^2[P,P]=1,
```

contrary to $`\Phi(P)=Z\cong N\ne0`$. This proves the conditional exclusion.

Run the finite identity from the repository root with assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_n_p6_one_u.py
```

The source author ran it using the bundled Python 3.12.14; it printed `P6 one-U cross-map restrictions passed`. This run is evidence for the finite identity only, not independent mathematical review of the exclusion or its dependencies.

## Independent review

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1a8a1eddcdfaeb5fab6f3e7682a37c5597a3b522), reviewers contributor 1, contributor 2 and contributor 3 independently accepted the full exclusion, conditional on the pinned central-socle, invariant-functional, marked-rank, component and folder inputs. All checked the fixed-vector normalization, completeness and restrictions of the cross-map space, the full nonzero bilinear restriction and both kernel-plane contradictions, and the remaining square-row argument. All read the exact verifier and its three imported scripts, extracted the four committed files, and independently ran the certificate with the pinned Python 3.12 runtime; the folder and small-order reviewers specified 3.12.14. The printed cross-map checks passed. The script verifies the finite representation identities, while the scoped proof reviews cover the envelope deduction. No fresh primary-source audit, formal certification or exclusion for larger b is asserted.
