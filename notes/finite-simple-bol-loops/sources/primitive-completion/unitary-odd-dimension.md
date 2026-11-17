# Odd-dimensional nonsingular unitary actions

**Mira Cult**

The [primitive point-action interface](classical-point-normalizers.md) separately addresses almost-simple extensions of this natural action; that interface remains unreviewed.

**Status:** Bounded argument with the scoped independent review below. This is a bounded continuation of the residual unitary action in [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md); it does not resolve the full unitary or S1 frontier and introduces no new claim ID. The UOD consequence below depends on C0008 Lemma 2.1 and on the stated natural action. Identification with arbitrary almost-simple extensions is treated separately by the linked interface.

Let $`q=p^f\ge3`$ be a prime power, $`K=\mathbb F_{q^2}`$, and let $`(V,H)`$ be a nondegenerate Hermitian space of **odd** $`K`$-dimension $`m\ge3`$. We take $`H`$ linear in its first argument and $`q`$-semilinear in its second. Let $`\Omega`$ be the set of nonsingular one-spaces $`[v]`$ with $`H(v,v)\ne0`$. The natural projective semilinear unitary similitude group $`P\Gamma U(V,H)`$ acts on $`\Omega`$ and preserves perpendicularity. In particular, the group consists of projective transformations represented by invertible $`\sigma`$-semilinear maps $`g`$, where $`\sigma`$ is a field automorphism of $`K`$, satisfying $`H(gx,gy)=\mu H(x,y)^\sigma`$ for some nonzero $`\mu`$.

## No-perpendicular-UOD theorem

For every invertible semilinear map $`g:V\to V`$, there is a nonsingular vector $`v`$ for which $`H(v,gv)\ne0`$. Consequently no element of $`P\Gamma U(V,H)`$ sends every point of $`\Omega`$ to a perpendicular point.

*Proof.* Choose a basis, put $`\sigma(t)=t^{p^j}`$ with $`0\le j<2f`$, and write $`g(v)=M(v^\sigma)`$. We do **not** need $`M`$ to be unitary. Let
$$F(v)=H(v,gv),\qquad r=p^{(j+f)\bmod 2f}.$$
Suppose $`F`$ vanishes on all nonsingular vectors. We first extend this vanishing to singular vectors. Given a nonzero singular $`x`$, choose a singular $`z`$ with $`H(x,z)\ne0`$, by extending $`\langle x\rangle`$ to a hyperbolic plane. On the line $`x+tz`$,
$$H(x+tz,x+tz)=t^qH(x,z)+tH(z,x).$$
This expression is zero for exactly $`q`$ values of $`t\in K`$: $`t=0`$ and the $`q-1`$ solutions of one equation $`t^{q-1}=a`$ with $`a`$ of norm one. Hence $`F(x+tz)=0`$ for $`q^2-q`$ values of $`t`$. The latter is a polynomial in $`t`$ with exponents among $`0,1,r,r+1`$ and degree at most $`q^2/p+1`$. For every $`q\ge3`$,
$$q^2/p+1<q^2-q,$$
so the polynomial is zero and in particular $`F(x)=0`$. Thus $`F=0`$ on all of $`V`$.

For all $`x,y`$ and $`t\in K`$, expansion now gives
$$0=F(x+ty)=tH(y,gx)+t^rH(x,gy).$$
If $`r\ne1`$, the monomials have distinct degrees below $`q^2`$, so both coefficients vanish. In particular $`H(x,gy)=0`$ for all $`x,y`$, contradicting nondegeneracy of $`H`$ and invertibility of $`g`$. If $`r=1`$, then $`j=f`$ and $`\sigma`$ is conjugation. The form $`C(x,y)=H(x,gy)`$ is $`K`$-bilinear and $`C(x,x)=0`$ for all $`x`$. It is therefore alternating and, in odd dimension, singular. But $`C`$ is nondegenerate because $`H`$ is nondegenerate and $`g`$ is invertible. This contradiction proves the theorem. $`\square`$

## Loop consequence

There are perpendicular nonsingular points $`[e_1],[e_2]`$: use two vectors of norm one in an orthonormal basis. Nonsingular one-spaces form a single unitary orbit: normalize each vector to norm one using surjectivity of $`K^\times\to\mathbb F_q^\times`$, and extend the resulting one-space isometry by Witt's lemma. For finite-field Hermitian spaces, see David Sprehn and Nathalie Wahl, *Forms over fields and Witt's lemma*, [arXiv:1811.12219v3](https://arxiv.org/abs/1811.12219v3), Theorem 3.4; the hyperbolic-plane and orthogonal-basis facts used above are standard finite Hermitian-space facts and should be independently checked for the exact conventions here.

Suppose a loop on $`\Omega`$ has multiplication group contained in $`P\Gamma U(V,H)`$. For its identity $`e`$, transitivity provides a point $`x`$ perpendicular to $`e`$. By C0008 Lemma 2.1, the left translation $`L_x`$ sends every $`y\in\Omega`$ to a point in the orbital of $`(e,x)`$; this orbital is contained in the perpendicularity relation, since the group preserves it. This contradicts the theorem. Thus, conditional on the stated action and UOD lemma, **no loop** has multiplication group contained in this natural action. No classification of the perpendicular orbital is needed.

## Even-dimensional control

The parity restriction is essential to this perpendicularity approach. For even $`m`$, choose standard $`H(x,y)=x^T y^q`$ and let $`M`$ be a direct sum of blocks $`\begin{pmatrix}0&1\\-1&0\end{pmatrix}`$ over $`\mathbb F_q`$. Then $`g(v)=Mv^q`$ is an invertible semilinear unitary transformation, and $`H(v,gv)=v^TMv=0`$ for all $`v`$. It is therefore a perpendicular UOD element on nonsingular points. This does not construct a loop or settle any even-dimensional action.

## Evidence and remaining work

No computational certificate is used in the proposed proof.

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/037cec7af0c10f7daf3172c0dd06e065be868c7b), contributor 1 accepted the polynomial root count, hyperbolic-partner and Hermitian arguments, UOD implication for the stated natural action and the even-dimensional control. The review covers q≥3 and odd m≥3, including characteristic two for q≥4, under the standard finite Hermitian-space facts and C0008 UOD. It does not classify all almost-simple action extensions or exclude even-dimensional actions; no computational or formal verification is claimed.
