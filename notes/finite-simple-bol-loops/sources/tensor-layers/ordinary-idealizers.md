# Effective rank-code idealizers and odd dimensions

**Mira Cult**

This proves the odd-dimensional branch of the [ordinary tensor theorem](../../manuscripts/0108-ordinary-tensor-idealizers.md). The first bound applies to any prime-field additive code of matrices, without a Bol hypothesis. It is useful precisely because restricting to the span of the code's images removes directions on which the code sees no action.

## A rank-code idealizer lemma with its prime-to-characteristic part

Let $`q=p^f`$; let $`W\ne0`$ be an additive subgroup of the $`d`$-by-$`d`$ matrices over $`\mathbf F_q`$, all its nonzero elements having rank at least $`\delta=\rho+1`$. Let $`L_0`$ be the $`\mathbf F_q`$-span of all images, of dimension $`a`$. Define the effective left idealizer

```math
{\cal B}=\{C\in \operatorname{End}_{\mathbf F_q}(L_0): CW\subseteq W\}.
```

It is a finite **$`\mathbf F_p`$-algebra** with identity; we do not enlarge it by ambient field scalars. Every nonzero $`C\in{\cal B}`$ has rank at least $`\delta`$ on $`L_0`$: otherwise all $`Cw,\ w\in W`$, are zero by the rank condition, contradicting the fact that the images of $`w`$ span $`L_0`$.

We claim

```math
|{\cal B}^{\times}|_{p'}\le
                  q^{\,a(\lfloor a/\delta\rfloor+1)/2}.               \tag{1}
```

Its Jacobson radical $`R`$ is nilpotent. By Artin--Wedderburn and the finite division-ring theorem, the quotient is a product $`\prod_i M_{n_i}(F_i)`$ of matrix algebras over finite fields of characteristic $`p`$. This quotient is separable over the **perfect prime field**, so Wedderburn's principal theorem embeds it as a semisimple complement inside $`{\cal B}`$; see [Baranov--Mudrov--Shlaka, Theorem 1(1) and the perfect-field remark](https://arxiv.org/abs/1609.05812), and [Farnsteiner, theorem (1) and proof](https://www.math.uni-bielefeld.de/~sek/select/RF6.pdf). Its identity is that of $`{\cal B}`$, since the difference is an idempotent in the nilpotent radical. Reduction on units has kernel $`1+R`$, a $`p`$-group, and is onto by the complement. Thus its prime-to-$`p`$ part is exactly that of the product of general linear groups over $`F_i`$.

In a fixed simple summand the $`n_i`$ diagonal primitive matrix units have equal $`\mathbf F_q`$-ranks $`c_i`$ on $`L_0`$, since the two complementary off-diagonal units induce mutually inverse maps between their image spaces. They are nonzero elements of $`{\cal B}`$, hence $`c_i\ge\delta`$. Orthogonality and the identity give $`\sum_i n_i c_i=a`$. The copy of $`F_i`$ in one diagonal corner acts on its $`c_i`$-space with every nonzero element invertible. Evaluating its unequal elements on any one nonzero vector gives distinct outputs, so $`|F_i|\le q^{c_i}`$, even if $`F_i`$ is not a subfield of $`\mathbf F_q`$. The prime-to-$`p`$ part of $`\mathrm{GL}_{n_i}(F_i)`$ is $`\prod_{j=1}^{n_i}(|F_i|^j-1)\le q^{c_i n_i(n_i+1)/2}`$. Now $`n_i\le\lfloor a/\delta\rfloor`$; multiplying the bounds gives (1).

Let $`N`$ be **any** subgroup of $`\mathrm{SL}_d(q)`$ preserving $`W`$ by pure left multiplication. Then it preserves $`L_0`$ and induces a subgroup of $`{\cal B}^\times`$ there. The kernel of this action induces a subgroup of $`\mathrm{GL}_{d-a}(q)`$ on the quotient natural space; those additionally trivial on that quotient are unipotent. Thus with $`x=d-a`$, (1) bounds $`|N|_{p'}`$ by

```math
q^{[a(\lfloor a/(\rho+1)\rfloor+1)+x(x+1)]/2}.
```

From the [defining-characteristic estimate](ordinary-profiles.md#a-defining-prime-valuation), or directly by an upper unitriangular flag on $`L_0`$, one also has $`|N|_p\le q^{D-\rho(2a-\rho-1)/2}`$, $`D=d(d-1)/2`$: deleting the first $`\rho`$ coordinates embeds the induced unipotent group into the unitriangular group of rank $`a-\rho`$, because any element in the kernel differs by rank at most $`\rho`$ on $`L_0`$; add the triangular kernel fixing $`L_0`$ pointwise. Combining gives

```math
|N|\le q^{D-\rho(2a-\rho-1)/2+
                [a(\lfloor a/(\rho+1)\rfloor+1)+x(x+1)]/2}.           \tag{2}
```

Transpose gives the corresponding right-sided estimate. These idealizer estimates are group-and-code lemmas, independent of the Bol hypotheses.

## The ordinary mass forces a larger pure kernel

In odd characteristic and odd dimension, the [profile calculation](ordinary-profiles.md) eliminates balanced profiles by an actual affine transvection collision, and the extremal $`\rho=1`$ case by pure rank-one restrictions. Keep its notation. Write $`m`$ for the **minimum** $`|r-s|`$ among selected even negative dimensions of the normalized pair of natural involutions, and $`\rho=d-m`$. Thus $`m\ge2`$ is even, $`\rho\ge3`$ odd, and every nonzero matrix in $`W`$ has rank at least $`\rho+1`$. The point stabilizer has projection $`J\le Y`$. Its *ordinary* index, not just its $`p`$-part, is precisely

```math
[Y:J]=|W|\sum_{(r,s)\ \mathrm{selected}}
                q^{-(r-s)^2}{d\brack r}_q{d\brack s}_q .              \tag{3}
```

Choose the side with the **larger** of the total image and total row dimensions $`a`$, interchanging coordinates when necessary; let $`x=d-a`$. The Singleton deletion bound on that side gives $`|W|\le q^{a(a-\rho)}`$, since the smaller side is at most $`a`$. The kernel $`N`$ of projection of $`J`$ to the opposite projective group $`T=\mathrm{PSL}_d(q)`$ is a genuine pure subgroup of $`\mathrm{SL}_d(q)`$ and preserves $`W`$. Since $`|Y|/|T|=|\mathrm{SL}_d(q)|`$,

```math
|N|\ge|\mathrm{SL}_d(q)|/[Y:J].                 \tag{4}
```

This only uses the size of the opposite projective image, not its surjectivity.

Bound (3) without assuming any cancellation. The Gaussian coefficient is at most $`2q^{i(d-i)}`$: the omitted denominator product $`\prod_{k\ge1}(1-q^{-k})`$ is at least $`1-\sum_{k\ge1}q^{-k}\ge1/2`$ for $`q\ge3`$. For a profile with $`|r-s|\ge m`$,

```math
r(d-r)+s(d-s)-(r-s)^2
 =\tfrac12\big(d^2-(r+s-d)^2-3(r-s)^2\big)
 \le (d^2-3m^2)/2.
```

There are at most $`(\rho+1)(\rho+3)/4`$ ordered even profiles of difference at least $`m`$. Also $`|\mathrm{SL}_d(q)|=q^{d^2-1}\prod_{j=2}^d(1-q^{-j})\ge(5/6)q^{d^2-1}`$. Consequently

```math
|N|\ge\frac{5}{6(\rho+1)(\rho+3)}
             q^{(d^2+3m^2)/2-1-a(a-\rho)}.                            \tag{5}
```

## Numerical separation in all ranks

Let $`B`$ be the exponent in (5) minus the exponent in (2). With $`k=\lfloor a/(\rho+1)\rfloor`$ and $`0\le x\le m-1`$, exact simplification gives

```math
2B=m^2+4mx-3x^2+\rho^2-\rho-2-ak
 \ \ge\frac{\rho(m-1)^2+\rho^3-\rho^2-4\rho-2}{\rho+1}.               \tag{6}
```

Indeed $`4mx-3x^2\ge0`$ and $`ak\le d^2/(\rho+1)`$. If $`\rho\ge5`$ and $`m\ge2`$, the last bound gives $`B\ge\rho`$, since $`\rho^3-3\rho^2-5\rho-2>0`$ for $`\rho\ge5`$. Also $`3^\rho>(6/5)(\rho+1)(\rho+3)`$ for $`\rho\ge5`$, by the value at 5 and successive ratios. Thus (5) strictly exceeds (2). If $`\rho=3,\ m\ge4`$, (6) gives $`B\ge31/8`$; already $`3^{7/2}>(6/5)\cdot4\cdot6`$. Again impossible, at every field size.

The remaining pair is $`(\rho,m)=(3,2)`$, so $`d=5`$ and $`a`$ is four or five. Here is the direct ordinary-mass comparison, not requiring any congruence sieve. Write $`g_i={5\brack i}_q`$. Even negative dimensions are $`0,2,4`$; the bounded normalized mass in (3), after dividing by $`|W|`$, is

```math
u=2g_2(1+g_1)/q^4+2g_1/q^{16}
\quad\text{as an upper bound.}
```

This includes both orientations of every possible difference. Since $`q\ge3`$, $`g_2\le(27/16)q^6`$, $`g_1<3q^4/2`$, and $`1+g_1<(8/5)q^4`$. It follows that $`u<6q^6`$. At $`a=4`$, (4) therefore gives $`|N|>(5/36)q^{14}>q^9`$; at $`a=5`$ it gives $`|N|>(5/36)q^8>q^6`$, since $`q^2\ge9`$. But the respective upper bounds from (2) are $`q^9`$ and $`q^6`$. At $`d=3`$ no positive odd $`\rho\ge3`$ remains once $`m\ge2`$; the balanced and extremal reductions exhaust it. This completes the ordinary branch in every odd dimension.

The [source checker](../code/verify_tensor_idealizer_bound.py) counts units in actual small matrix algebras. The [separate checker](../code/check_c96_effective_idealizer.py) enumerates 672 additive matrix codes over the four-element field, 600 not linear over that field, and handles the rank-five ternary cap without the earlier divisibility sieve. These finite controls do not prove the idealizer bound for arbitrary fields.

[Next: quadratic profiles in even dimensions](ordinary-quadratic.md).
