# A conditional exclusion for the Sp4 minus-refinement action

**Mira Cult**

This is a route with the scoped independent review recorded below for the rank-three reduction in [C0017](../../claims/0017.md) and the residual frontier [C0010](../../claims/0010.md). It is not a proof of the CFSG-free aggregate claim [C0016](../../claims/0016.md). The final group-theoretic step invokes the CFSG-dependent Bruck-loop structure theorem. The argument covers $`q=2^f`$ for every $`f\ge2`$; its $`q=4`$ geometric input is the local argument linked below, which has the scoped review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/a02c94ee44243d7ab1efff303dc49198b62844ef) recorded in C0016. The $`f\ge3`$ extension and the assembled argument have the scoped review below.

## Geometric setup and inputs

Let $`V`$ be a four-dimensional vector space over $`\mathbb F_q`$, $`q=2^f\ge4`$, with nondegenerate alternating form $`B`$ and a quadratic refinement $`Q`$ of minus type. Let $`\mathop{\mathrm{Tr}}\nolimits=\mathop{\mathrm{Tr}}\nolimits_{\mathbb F_q/\mathbb F_2}`$ and $`\Omega=\{v\in V:\mathop{\mathrm{Tr}}\nolimitsQ(v)=0\}`$. A vector $`v`$ labels the quadratic refinement $`Q_v(z)=Q(z)+B(v,z)^2`$; the set $`\Omega`$ labels the minus refinements. The action of $`\Gamma\mathop{\mathrm{Sp}}\nolimits(V)`$ on $`\Omega`$ is affine semilinear:

```math
g(v)=M(v^\sigma)+c,\qquad M\in\mathop{\mathrm{Sp}}\nolimits(V),\quad \sigma\in\mathop{\mathrm{Gal}}\nolimits(\mathbb F_q/\mathbb F_2).
```

The linear case satisfies $`Q(Mv)+Q(v)=B(Mv,c)^2`$. This action model, the identification of $`\Omega`$, and the following displacement relation are geometric inputs: $`g`$ is in the $`\Delta_0`$ displacement relation precisely when

```math
J_g(v):=Q(v)+Q(gv)+B(v,gv)+B(v,gv)^2=0.
```

At the identity $`0`$, the nonzero $`\Delta_0`$ points are exactly the nonzero $`Q`$-singular vectors. The relevant orbit and action conventions must be checked for the group being excluded; see [C0016, the $`q=8`$ action discussion](../foundations/C0016.md#q8-proposed-action-and-orbital-application). We use only the facts that these relations are invariant under the acting group and that they contain the specified pairs.

We also use the [binary quadratic zero-set lemma and $`q=4`$ $`\Delta_0`$ classification in C0016](../foundations/C0016.md#q4-zero-set-lemma-and-proposed-delta_0-classification): for a nondegenerate minus-type binary quadratic form in dimension at least six, a binary polynomial of degree at most two vanishing on its zero set is a scalar multiple of that form. In particular, componentwise over $`\mathbb F_q`$, $`J_g=0`$ on $`\Omega`$ implies

```math
J_g(v)=\gamma\mathop{\mathrm{Tr}}\nolimitsQ(v)\quad(v\in V)
```

for some $`\gamma\in\mathbb F_q`$. The linked $`q=4`$ argument supplies the classification in the next section when $`f=2`$. Its underlying inputs and the scope of its actual review must be carried along; this manuscript does not reproduce or extend the local review.

## The $`\Delta_0`$ classification for $`f\ge3`$

Suppose $`g(v)=M(v^\sigma)+c`$ has $`J_g(v)=0`$ on $`\Omega`$ and sends $`0`$ to a nonzero $`Q`$-singular vector. Polarization of the preceding identity gives

```math
B(x,y)+B(x,y)^\sigma+w(x,y)+w(x,y)^2
 =\gamma\mathop{\mathrm{Tr}}\nolimitsB(x,y),\qquad
 w=B(x,M(y^\sigma))+B(y,M(x^\sigma)). \tag{1}
```

Write $`\sigma:z\mapsto z^{2^j}`$, $`1\le j<f`$. For $`B(x,y)=0`$, put $`P=B(x,M(y^\sigma))`$ and $`T=B(y,M(x^\sigma))`$. Replacing $`x`$ by $`ax`$ in (1) yields, for every $`a\in\mathbb F_q`$,

```math
aP+a^{2^j}T+a^2P^2+a^{2^{j+1}}T^2=0. \tag{2}
```

Reduce $`a^q`$ to $`a`$. If $`1<j<f-1`$, the four exponents are distinct. If $`j=1`$, the coefficients of $`a`$ and $`a^4`$ force $`P=T=0`$. If $`j=f-1`$, the coefficients of $`a^2`$ and $`a^{2^{f-1}}`$ force the same conclusion. These cases include $`f=3`$. In each case the reduced polynomial has degree below $`q`$ and vanishes on the field, so the coefficient comparison is valid.

Thus $`B(x,M(y^\sigma))=0`$ whenever $`B(x,y)=0`$. Nondegeneracy gives $`M(y^\sigma)\in\langle y\rangle`$ for every $`y\ne0`$. For independent $`u,v`$, applying this to $`u`$, $`v`$, $`u+v`$ and $`u+av`$ for every $`a\in\mathbb F_q`$ forces $`a^\sigma=a`$ for all $`a`$, a contradiction. Hence $`\sigma=1`$.

Now (1) with $`B(x,y)=0`$ gives $`w+w^2=0`$. Scaling $`x`$ by $`a`$ and comparing the polynomial $`aw+a^2w^2`$ shows $`w=0`$ for all such pairs. For fixed nonzero $`x`$, the linear functional $`w(x,-)`$ is therefore a scalar multiple of $`B(x,-)`$; bilinearity and nondegeneracy make the scalar independent of $`x`$. Thus $`w=\mu B`$ for some $`\mu\in\mathbb F_q`$. Every $`z\in\mathbb F_q`$ is a value of $`B`$, and (1) becomes

```math
\mu z+\mu^2z^2=\gamma(z+z^2+\cdots+z^{2^{f-1}}).
```

For $`f\ge3`$, comparison of the coefficients of this polynomial of degree less than $`q`$ gives $`\gamma=\mu=0`$. Consequently $`M+M^{-1}=0`$, so $`M^2=1`$, and $`J_g=0`$ on all of $`V`$.

The square of $`g`$ is translation by $`d=Mc+c`$. It preserves $`\Omega`$ and its complement. If $`d\ne0`$, then $`\mathop{\mathrm{Tr}}\nolimits(Q(v+d)+Q(v))=\mathop{\mathrm{Tr}}\nolimits(Q(d)+B(v,d))`$ is not identically zero, since the trace pairing is nondegenerate; this contradicts preservation of both classes. Hence $`d=0`$ and $`Mc=c`$. The linear compatibility and $`J_g=0`$ now give

```math
0=J_g(v)=Q(c)+B(v,Mv)+B(v,Mv)^2.
```

At $`v=0`$ this gives $`Q(c)=0`$. Replacing $`v`$ by $`av`$ then yields $`B(v,Mv)=0`$ for every $`v`$. Thus, putting $`N=M+1`$,

```math
g(v)=(1+N)v+c,\qquad B(v,Nv)=0\quad(v\in V). \tag{3}
```

The linked $`q=4`$ classification provides (3) for $`f=2`$ as well, conditional on its stated inputs.

## Both translations and exponent two

Let $`*`$ be a loop on $`\Omega`$, with identity $`0`$, whose full multiplication group lies in the stated affine action. Every translation is uniformly displaced in the invariant relation of its pair $`(0,g(0))`$: for example, $`(y,x*y)=(R_y(0),R_y(x))`$. Therefore, for every nonzero $`Q`$-singular $`x`$, both $`L_x`$ and $`R_x`$ have the form (3). Write

```math
L_x(v)=v+N_xv+x,\qquad B(v,N_xv)=0,
```

and put $`N_0=0`$. For arbitrary $`y`$, write $`R_y(v)=T_y(v^\sigma)+y`$. Equality $`L_x(y)=R_y(x)`$ gives

```math
N_xy=T_y(x^\sigma)+x,\qquad
 B(y,T_y(x^\sigma)+x)=0 \tag{4}
```

for every singular $`x`$.

The singular vectors span $`V`$: in a Witt decomposition with singular hyperbolic pair $`e,f`$, each vector $`a`$ in the anisotropic complement is the sum of $`e+Q(a)f+a`$, $`e`$, and $`Q(a)f`$, all singular. If $`\sigma\ne1`$, substitute $`ax`$ into (4). The functions $`a^\sigma`$ and $`a`$ are linearly independent over $`\mathbb F_q`$, so $`B(y,x)=0`$ for every singular $`x`$, and hence $`y=0`$. Thus every nonidentity right translation has $`\sigma=1`$; the identity translation does as well. Equation (4) then implies $`T_y^{-1}y=y`$, because the singular vectors span. Consequently $`y*y=R_y(y)=T_yy+y=0`$ for every $`y`$.

The same argument with the classified right translations at singular $`x`$ and $`R_x(y)=L_y(x)`$ shows every left translation has trivial field part. Hence the original loop has exponent two and its left multiplication group lies in the $`\mathop{\mathrm{Sp}}\nolimits_4(q)`$ action on refinements. For a left Bol loop, its opposite is right Bol of exponent two; its inversion map is the identity, so the automorphic inverse property holds. It is therefore a Bruck loop; see also Baumeister–Stein, introduction, cited below.

## Bruck envelope and the invariant subspace

Let $`G=\mathop{\mathrm{LMlt}}\nolimits(\Omega,*)`$, equivalently the right multiplication group of the opposite Bruck loop. By Baumeister–Stein, *The finite Bruck loops*, `arXiv:0908.2597v2`, Theorem 1(c)(1),(3) and Remark 1.1(2), applied to its Baer envelope,

```math
F^*(G)=O_2(G),\qquad G/O_2(G)\cong\prod_i\mathop{\mathrm{PGL}}\nolimits_2(t_i),
```

where each $`t_i`$ is $`9`$ or a Fermat prime at least $`5`$. This source theorem uses CFSG-dependent classification; this manuscript therefore establishes no CFSG-free conclusion. The product may be empty.

The action is faithful and transitive on $`\Omega`$, so $`G`$ is nontrivial. A nontrivial finite group has nontrivial generalized Fitting subgroup, hence $`N=O_2(G)\ne1`$. The common fixed space $`W=C_V(N)`$ is nonzero, since a finite $`2`$-group acting on a nonzero characteristic-two vector space has a nonzero fixed vector; it is proper because $`N`$ acts faithfully. It is $`G`$-invariant. If $`W`$ were nondegenerate, then $`V=W\perp W^\perp`$, and the nonzero $`N`$-module $`W^\perp`$ would contain an $`N`$-fixed vector, contradicting the definition of $`W`$. Thus $`D=W\cap W^\perp`$ is nonzero, $`G`$-invariant and totally isotropic. Its dimension is one or two.

If $`D=\langle e\rangle`$, choose a minus refinement $`Q_0`$ with $`Q_0(e)=0`$ and a hyperbolic partner $`h`$ with $`Q_0(h)=0`$ and $`B(e,h)=1`$; the orthogonal complement is an anisotropic plane. Both $`Q_0`$ and $`Q_h`$ are minus refinements because $`Q_0(h)=0`$, but $`Q_0`$ vanishes on $`D`$ and $`Q_h(e)=1`$. The stabilizer of $`D`$ preserves whether a refinement vanishes on it, so $`G`$ cannot be transitive on $`\Omega`$.

If $`D`$ is Lagrangian, its stabilizer in $`\mathop{\mathrm{Sp}}\nolimits_4(q)`$ has a normal unipotent $`2`$-subgroup $`U`$ with quotient $`\mathop{\mathrm{GL}}\nolimits_2(q)`$. Let $`H`$ be the image of $`G`$ in this quotient. Since $`G\cap U\le O_2(G)`$ and the inverse image in $`G`$ of $`O_2(H)`$ is a normal $`2`$-group, 

```math
G/O_2(G)\cong H/O_2(H).
```

Every $`2`$-element of $`\mathop{\mathrm{GL}}\nolimits_2(q)`$ has order at most two: it is unipotent, and a nilpotent $`2\times2`$ matrix squares to zero. The same holds in every quotient of a subgroup: if a coset has $`2`$-power order, the $`2`$-part of any lift maps to a generator of the same cyclic coset subgroup. But for odd $`t`$, $`\mathop{\mathrm{PGL}}\nolimits_2(t)`$ has an element of order four in a split or nonsplit cyclic torus of order $`t-1`$ or $`t+1`$, one of which is divisible by four. Thus the product above must be empty and $`G`$ is a $`2`$-group. A transitive $`2`$-group cannot act on $`|\Omega|=q^2(q^2-1)/2`$, which has an odd divisor greater than one. This is a contradiction.

Subject to the stated geometric inputs, this excludes left Bol loops in the full semilinear action for all $`f\ge2`$ using the cited CFSG-dependent Bruck theorem. The assembled argument has the scoped independent review below; it does not by itself certify C0017 or the unrestricted classification.

## Scoped independent review

At exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/5c011bc5e8b375a1e85058811590bf0d672198f2), contributor 1 independently accepted the all-field exclusion for $`q=2^f\ge4`$, under the stated CFSG-dependent Baumeister–Stein theorem and standard refinement/Arf and Witt facts. The review checked the coefficient cases, both-side displacement argument, Bruck conversion, fixed-space and parabolic cases, and the order-four obstruction. It directly checked Theorem 1(c)(1),(3) and Remark 1.1(2) in the versioned primary source, and used the earlier bounded $`q=4`$ review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/a02c94ee44243d7ab1efff303dc49198b62844ef). It is not an aggregate C0016/C0017 review or a CFSG-free proof.
