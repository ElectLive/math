# Two Bol-loop families distinguished by their associativity probabilities

Mira, with AI assistance

## What the theorem says

For every integer $`h\ge1`$, the two explicit finite loops constructed below have the same order and identical ranks for every correspondingly labeled scalar form. Nevertheless, **they are not isomorphic as loops**. They have different probabilities that three uniformly chosen elements associate.

The statistic requires only a multiplication table, not coordinates, distinguished characters, or a chosen presentation. This is not a classification within either family, an isotopy invariant, a simplicity assertion, or an efficient black-box isomorphism test.

This note gives the complete construction, an intrinsic-statistic argument, and the precise spectral-counting lemma that proves the separation. The full derivation of that lemma and its dependencies are publicly included in the [scientific manuscript](analytic-2026-11-16/manuscripts/bol-intrinsic-spectral-separation.md) and the [associator manuscript](analytic-2026-11-16/manuscripts/bol-associator-quantization.md). Thus the proof package is public; the short note does not conceal the spectral calculation behind an assertion that a small numerical experiment proves the theorem.

## 1. Explicit construction

A **loop** is a set with a two-sided identity and unique left and right division. A left Bol loop satisfies

```math
x\circ(y\circ(x\circ z))=(x\circ(y\circ x))\circ z.
```

Fix $`h\ge1`$, put $`Q=729`$ and $`k=2h+1`$, and let

```math
E=\mathbb F_{729},\qquad L=\mathbb F_{729^h},\qquad M=\mathbb F_{729^{2h-1}}.
```

Choose injective $`\mathbb F_3`$-linear maps $`j:\mathbb F_3^k\to L`$ and $`i:\mathbb F_3^k\to M`$. They exist because the target dimensions over $`\mathbb F_3`$ are $`6h`$ and $`6(2h-1)`$. All assertions below hold for every such choice.

For $`t=j(\nu)`$ and $`z(t)=(t,t^3,t^9)`$, define an alternating form on $`L^3`$ by

```math
c_t(x,y)=\operatorname{Tr}_{L/E}\det[z(t),x,y].
```

The **spread pencil** is $`B^{\rm sp}_\nu=c_{j(\nu)}\oplus c_{j(\nu)}`$ on $`L^6`$, an $`E`$-space of dimension $`6h`$.

The **aligned pencil** is $`B^{\rm al}_\nu=S_\nu\oplus d_\nu`$. Here $`S_\nu`$ is the alternating matrix on $`E^{k+1}`$ with first row $`(0,\nu_1,\ldots,\nu_k)`$ and all other off-first-row/column entries zero, and

```math
d_\nu((x,y),(x',y'))=
\operatorname{Tr}_{M/E}\bigl(i(\nu)(xy'-yx')\bigr)
```

on $`M^2`$. The dimensions sum to $`k+1+2(2h-1)=6h`$. Choose an $`E`$-basis in either construction and write $`B_i=B_{e_i}`$, so $`B_\nu=\sum_i\nu_iB_i`$.

For either pencil, put

```math
W=E^{6h},\quad V=(\mathbb F_7^2)^k,\quad U=W\oplus V,\quad
Z=\mathbb F_3^k\oplus\mathbb F_7.
```

Choose $`\lambda\in E`$ of order seven. Such an element exists since $`7\mid728`$. For $`u=(w,(v_i))`$ and $`u'=(w',(v_i'))`$, define

```math
\begin{aligned}
\beta(w,w')_i&=\operatorname{Tr}_{E/\mathbb F_3}(w^{\mathsf T}B_iw'),\\
\gamma(v,v')&=\sum_i(v_{i,1}v'_{i,2}-v_{i,2}v'_{i,1}),\\
b(u,u')&=(\beta(w,w'),\gamma(v,v')),\\
R(a,s)(w,(v_i))&=(\lambda^s w,(2^{a_i}v_i)).
\end{aligned}
```

The exponents are well-defined because $`\lambda`$ has order seven and $`2\in\mathbb F_7`$ has order three. On $`\mathcal L=U\times Z`$, set

```math
(u,c)\circ(u',c')=(u+R(c)u',\ c+c'-b(u,u')).
```

The identity is $`(0,0)`$. The divisions and the left Bol identity are verified directly in [Sections 2.1–2.3 of the associator manuscript](analytic-2026-11-16/manuscripts/bol-associator-quantization.md). These loops are proper (non-Moufang). Both have order

```math
N_h=3^{38h+1}7^{4h+3}.
```

For both pencils, $`B_0=0`$, every $`B_\nu`$ with $`\nu\ne0`$ has rank $`4h`$ over $`E`$, and the common radical is zero. Independence over $`E`$ is not required: the parameters are $`\mathbb F_3`$-linear.

## 2. A statistic intrinsic to any finite loop

For a finite loop $`\mathcal L`$, define

```math
a(\mathcal L)=\frac{\#\{(x,y,z)\in\mathcal L^3:
 x\circ(y\circ z)=(x\circ y)\circ z\}}{|\mathcal L|^3}.
```

Let $`L_x(z)=x\circ z`$, define the permutation
$`\ell_{x,y}=L_{x\circ y}^{-1}L_xL_y`$, and let $`U_gf=f\circ g^{-1}`$. On the space of complex functions on $`\mathcal L`$, put

```math
\mathcal A=\frac1{|\mathcal L|^2}\sum_{x,y}U_{\ell_{x,y}}.
```

**Lemma.** For every finite loop,

```math
a(\mathcal L)=\frac{\operatorname{Tr}\mathcal A}{|\mathcal L|}.
```

**Proof.** The trace of a permutation operator is its number of fixed points. The equation $`\ell_{x,y}(z)=z`$ is exactly the associativity equation in the definition of $`a(\mathcal L)`$. Average the fixed-point count over $`x,y`$ and divide by $`|\mathcal L|`$. The trace is the ordinary linear-algebra trace even when the function-space inner product uses normalized counting measure.

A loop isomorphism conjugates every $`L_x`$ to the corresponding left translation, and therefore conjugates $`\mathcal A`$. Thus $`a(\mathcal L)`$ is an invariant under **all** loop isomorphisms, not only additive or pencil-preserving ones. ∎

## 3. Separation theorem

**Theorem.** For every $`h\ge1`$ and every pair of allowed injections in Section 1,

```math
\mathcal L_{{\rm sp},h}\not\cong\mathcal L_{{\rm al},h}.
```

More precisely, with $`k=2h+1`$ and $`Q=729`$,

```math
\begin{aligned}
N_h\bigl(a(\mathcal L_{{\rm al},h})-a(\mathcal L_{{\rm sp},h})\bigr)
={}&\frac{48}{343}(3^k-3)(Q^{2h-1}-1)\\
&\times\left[(1+42\,49^{-k})(49^k-17^k)
+6\bigl((19/3)^k-(25/9)^k\bigr)\right]>0.
\end{aligned}
```

### Why the spectral calculation sees a difference

The key distinction is between **intersections of images**, not ranks of individual matrices. For nonzero parameters $`\alpha,\nu`$ independent over $`\mathbb F_3`$,

```math
\dim_E(\operatorname{im}B^{\rm sp}_\nu\cap\operatorname{im}B^{\rm sp}_\alpha)=2h,
\qquad
\dim_E(\operatorname{im}B^{\rm al}_\nu\cap\operatorname{im}B^{\rm al}_\alpha)=4h-1.
```

For the spread form, its radical is the full $`L`$-line through $`z(t)`$. The nondegenerate trace pairing identifies the image with the hyperplane $`\xi\cdot z(t)=0`$ in $`L^3`$. Equality of two radical lines forces $`s/t=(s/t)^3`$, hence $`s/t\in\mathbb F_3^\times`$. Independent parameters give two distinct hyperplanes, whose intersection has one $`L`$-dimension in each copy: $`2h`$ dimensions over $`E`$.

For the aligned form, the two star images intersect in the line $`Ee_0`$. The nonsingular common block contributes $`4h-2`$ further dimensions. This gives $`4h-1`$.

The number of compatible vectors is consequently

```math
\#\{w:B_\nu w\in\operatorname{im}B_\alpha\}
=Q^{6h-\operatorname{rank}B_\nu+
\dim(\operatorname{im}B_\nu\cap\operatorname{im}B_\alpha)},
```

namely $`Q^{4h}`$ for spread and $`Q^{6h-1}`$ for aligned in the independent-parameter case. The zero and proportional cases coincide.

### The counting lemma completing the proof

The full orbit-spectrum derivation in the [spectral manuscript, Sections 3–4](analytic-2026-11-16/manuscripts/bol-intrinsic-spectral-separation.md), using [AQ.27–AQ.33](analytic-2026-11-16/manuscripts/bol-associator-quantization.md), gives for every real $`t>0`$:

```math
\begin{aligned}
\operatorname{Tr}\mathcal A_{\rm al}^{t}-\operatorname{Tr}\mathcal A_{\rm sp}^{t}
={}&\frac{(3^k-3)(Q^{6h-1}-Q^{4h})}{7}
 Q^{-4ht}(1-49^{-t})D_k(t),\\
D_k(t)={}&(1+42\,49^{-kt})(49^k-17^k)\\
&+6\left[(1+48\,9^{-t})^k-(1+16\,9^{-t})^k\right].
\end{aligned}
```

All factors are positive. In the multiplicity table, aligned transfers positive multiplicity from eigenvalue $`rs/49`$ to $`rs`$, where $`r=Q^{-4h}`$ and $`s`$ runs over positive ring multipliers. All other contributions are unchanged. This count retains the singleton zero orbit, seven-element nonzero field orbits, sixteen three-cycles per active ring plane, and all ring-character sectors. Its total multiplicity is exactly $`N_h`$.

Take $`t=1`$ and apply the intrinsic-statistic lemma. The stated strict probability inequality and nonisomorphism follow. ∎

## 4. Meaning and limitations

The simplest case has

```math
N_1=3337453428382706771853981,\qquad
\Delta\operatorname{Tr}\mathcal A=6207245000998912/22235661.
```

Its probability difference is about $`8.36\times10^{-17}`$. Thus this is an exact distinguishing invariant, not presently an efficient sampling test.

The full calculation also gives different positive trace moments and rescaled spectral laws, and a canonical filtered root-mean-square comparison asymptotic to $`27\,3^{-h}`$. Both filtered worst-case norms are one. That corollary is an average-square separation, not a uniformly faster Markov walk. See the complete manuscript for the cutoff and normalization.

## 5. Review and reproduction

The [targeted publication audit](analytic-2026-11-16/evidence/intrinsic-publication-audit.md) found no error in the checked proof chain and replayed both exact-arithmetic checks. It explicitly states which earlier spectral formulas it uses. The [original scientific review](analytic-2026-11-16/evidence/bol-metaplectic-review.md) is also preserved.

Both are **model reviews**, not external human peer review, formal verification, or certification of literature-wide novelty. A human expert is particularly invited to check the AQ spectrum-to-multiplicity passage and the exceptional zero-character bookkeeping.

From this directory, run:

```sh
python analytic-2026-11-16/code/verify_bol_intrinsic_spectrum.py
python analytic-2026-11-16/code/verify_bol_intrinsic_incidence_independent.py
```

These finite checks corroborate the uniform proof; they do not enumerate the enormous multiplication tables. The [release record](analytic-2026-11-16/README.md) gives source pins, mirror policy, and separate repository-validation status.
