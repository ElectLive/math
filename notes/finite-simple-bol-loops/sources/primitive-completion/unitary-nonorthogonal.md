# A nonorthogonal invariant in nonsingular unitary actions

Mira Cult
**Status:** Independently reviewed under the scope recorded below. This is a bounded continuation of the nonsingular unitary action in [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). It depends on C0008 Lemma 2.1 for the loop consequence. The review covers the stated natural action; the extension to a specified almost-simple socle action is treated separately in [classical-point-normalizers.md](classical-point-normalizers.md). No conclusion about $`q=2`$ or about actions outside the stated group is asserted.

Let $`q=p^f\ge3`$, $`K=\mathbb F_{q^2}`$, and let $`(V,H)`$ be a nondegenerate Hermitian space of $`K`$-dimension $`m\ge3`$. Take $`H`$ linear in its first variable and $`q`$-semilinear in its second. Put $`Q(v)=H(v,v)`$, and let $`\Omega`$ be the nonsingular one-spaces. The group $`P\Gamma U(V,H)`$ means the natural projective group induced by semilinear unitary similitudes. For nonsingular $`x,y`$ define

```math
\eta([x],[y])=\frac{H(x,y)H(y,x)}{Q(x)Q(y)}\in\mathbb F_q.
```

This is well defined on one-spaces. A semilinear similitude with field automorphism $`\sigma`$ sends $`\eta`$ to $`\eta^\sigma`$, so the relation $`\eta=1`$ is invariant under the whole group.

## Theorem

No nonidentity element of $`P\Gamma U(V,H)`$ has $`\eta([v],[gv])=1`$ for every $`[v]\in\Omega`$. Consequently, conditional on C0008 Lemma 2.1, no loop on $`\Omega`$ has multiplication group contained in this natural action.

*Proof.* Write $`g(v)=M(v^\sigma)`$ with $`\sigma(t)=t^{p^j}`$, $`0\le j<2f`$, and $`M`$ invertible. Its similitude multiplier belongs to $`\mathbb F_q^\times`$; rescaling $`M`$ using surjectivity of the norm map, we may assume $`Q(gv)=Q(v)^\sigma`$. Put $`F(v)=H(v,gv)`$. The hypothesis becomes

```math
F(v)F(v)^q=Q(v)Q(v)^\sigma\qquad(Q(v)\ne0).\tag{1}
```


Fix a nonzero singular $`x`$. The quotient $`x^\perp/\langle x\rangle`$ is a nondegenerate Hermitian space of dimension $`m-2\ge1`$. Choose a representative $`y\in x^\perp`$ of norm one. Then $`Q(y+tx)=1`$ for **every** $`t\in K`$, so (1) gives

```math
F(y+tx)F(y+tx)^q=1\qquad(t\in K).\tag{2}
```

Set

```math
r=p^{(j+f)\bmod 2f},\qquad s=p^j,\qquad u=p^{j\bmod f}.
```

After reducing powers by $`t^{q^2}=t`$, $`F(y+tx)`$ has exponents among $`0,1,r,1+r`$, while $`F(y+tx)^q`$ has exponents among $`0,q,s,q+s`$. The coefficient of the highest exponent $`1+r`$ in the first polynomial is $`F(x)`$, and the coefficient of $`q+s`$ in the second is $`F(x)^q`$; these highest exponents are unique even when $`r=1`$ or $`s=1`$. Since $`\{r,s\}=\{u,qu\}`$, their product has degree at most

```math
D=1+q+r+s=(q+1)(1+u),
```

with coefficient $`F(x)F(x)^q`$ at $`t^D`$. As $`u\le q/p`$, $`D<q^2`$ for all $`q\ge4`$: indeed $`(q+1)(1+q/2)<q^2`$. For $`q=3`$, $`u=1`$ and $`D=8<9`$. Thus the polynomial in (2) minus 1 has degree below $`q^2`$ and vanishes at every element of $`K`$, so it is identically zero. Its coefficient at $`t^D`$ yields $`F(x)F(x)^q=0`$, hence

```math
H(x,gx)=0\quad\text{for every singular }x.\tag{3}
```


Choose an orthonormal basis $`e_1,\dots,e_m`$ and write $`A_{ij}=H(e_i,g e_j)`$. For $`i\ne j`$ and each $`t\in K`$ with $`t^{q+1}=-1`$, the vector $`e_i+te_j`$ is singular. Equation (3) becomes

```math
A_{ii}+t^rA_{ij}+tA_{ji}+t^{1+r}A_{jj}=0.\tag{4}
```

The $`q+1`$ solutions of $`t^{q+1}=-1`$ form a coset of the cyclic norm-one group. Its characters with distinct exponents modulo $`q+1`$ are linearly independent over $`K`$.

If $`\sigma`$ is neither the identity nor conjugation, then $`u\ge2`$, $`u\le q/p\le q/2`$, and $`r\equiv u`$ or $`-u\pmod{q+1}`$. The four exponents $`0,1,r,1+r`$ are distinct modulo $`q+1`$. Thus (4) forces all four coefficients to vanish for every pair $`i\ne j`$, so $`M=0`$, contrary to invertibility.

If $`\sigma=1`$, then $`r=q\equiv-1\pmod{q+1}`$. Equation (4) gives $`A_{ij}=A_{ji}=0`$ and $`A_{ii}=A_{jj}`$ for each $`i\ne j`$. Hence $`g`$ is scalar and is the identity projectively. If $`\sigma(t)=t^q`$, then $`r=1`$ and (4) gives $`A_{ii}=A_{jj}=0`$ and $`A_{ij}+A_{ji}=0`$. Thus the $`K`$-bilinear form $`C(x,y)=H(x,gy)`$ is alternating and $`F(v)=0`$ for every $`v`$, contradicting (1) on a nonsingular $`v`$. The theorem's first assertion follows. $`\square`$

For the loop consequence, choose a norm-one vector $`e`$ and a nonzero singular vector $`w\in e^\perp`$. Such a $`w`$ exists because $`e^\perp`$ is nondegenerate of dimension at least two. Then $`[e]`$ and $`[e+w]`$ are distinct nonsingular points with $`\eta=1`$. The unitary group is transitive on $`\Omega`$: normalize the norms by the surjective norm map and extend the resulting one-space isometry by Witt's lemma. For a loop with multiplication group in the action, choose such a point $`x`$ relative to its identity $`e`$. C0008 Lemma 2.1 gives a nonidentity left translation $`L_x`$ carrying every point into the orbital of $`(e,x)`$. Since $`\eta=1`$ is group-invariant, this translation contradicts the first assertion.

For Hermitian-space conventions and Witt extension, see David Sprehn and Nathalie Wahl, *Forms over fields and Witt's lemma*, [arXiv:1811.12219v3](https://arxiv.org/abs/1811.12219v3), Theorem 3.4. The finite-field hyperbolic-pair and orthonormal-basis facts used here, the field-exponent reduction and the precise action convention should be checked in independent review. The independently reviewed odd-dimensional argument is in [unitary-odd-dimension.md](unitary-odd-dimension.md); this proposed argument additionally targets even dimensions.

## Boundary and evidence

An earlier draft used a singular hyperbolic line and applied only for $`q\ge5`$; the constant-norm line above proposes the extension to $`q=3,4`$. The estimate fails to establish the $`q=2`$ case, which is addressed separately in C0016 under its recorded review scope. automated reviewers a separate automated checker independently accepted the complete revised argument at its recorded source revision for every q≥3 and m≥3. The review checked the constant-norm line, field exponents including q=3,4, norm-circle character separation, and the loop consequence using C0008 Lemma 2.1 and the stated Hermitian facts. No finite calculation is used. This review does not cover q=2 or identify arbitrary permutation actions of the same abstract unitary socle.
