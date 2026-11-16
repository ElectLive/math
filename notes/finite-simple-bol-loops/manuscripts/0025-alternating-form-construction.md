# 0025. Simple odd Bol loops from alternating-form tuples

**Mira Cult**

## Results obtained

An ordered tuple of alternating forms can be encoded in a finite simple proper left Bol loop. The resulting loop remembers the tuple up to simultaneous semilinear congruence and permutation, rather than arbitrary changes of basis in the space of forms. This is the interface used by [the matrix-pair embedding](0024-matrix-pair-embedding.md).

The construction and argument below are a research proof draft. The loop-theoretic conclusions use the folder, simplicity and isomorphism interfaces specified in Section 2. They are not an independent proof of the entire class-two classification.

**Theorem.** Let $p,q$ be distinct odd primes with $p\mid q-1$, let $r=\operatorname{ord}_q(p)$, and put $E=\mathbb F_{p^r}$. Fix $\lambda\in E$ of order $q$ and $\eta\in\mathbb F_q$ of order $p$. Let $n,k>0$, and let $B_1,\ldots,B_k$ be alternating $n\times n$ matrices over $E$ satisfying:

1. the matrices are linearly independent over $\mathbb F_p$;
2. their common radical is zero.

Subject to the interfaces in Section 2, they define a finite simple proper left Bol G-loop $L(B)$ of order

```math
|L(B)|=p^{nr+k}q^{2k+1}.
```

For fixed $p,q,n,k,\lambda,\eta$, two inputs give isomorphic loops exactly when there exist $\pi\in S_k$, $\theta\in\operatorname{Gal}(E/\mathbb F_p)$, and $L\in\operatorname{GL}_n(E)$ such that

```math
L^{\mathsf T} B'_{\pi(i)} L=\theta(B_i)
\qquad(1\le i\le k).
\tag{1}
```

Here $\theta$ acts entrywise. Independence over $E$ is not required. “Proper” means non-Moufang; “G-loop” means isomorphic to every loop isotope. Thus this is not the non-G-loop construction of claim0018.

## 1. From trace forms to a group with inversion

Put $W=E^n$, $Z=\mathbb F_p^k$, and define

```math
\beta(x,y)=
\bigl(\operatorname{Tr}_{E/\mathbb F_p}(x^{\mathsf T}B_i y)\bigr)_{i=1}^k.
\tag{2}
```

The values of $\beta$ span $Z$. Indeed, a linear functional on $Z$ annihilating all these values would give a matrix $B=\sum_i a_iB_i$, with $a_i\in\mathbb F_p$, such that $\operatorname{Tr}(x^{\mathsf T}By)=0$ for all $x,y$. Nondegeneracy of the trace pairing forces $B=0$, hence every $a_i=0$.

The radical of $\beta$ is also zero. If $\beta(x,y)=0$ for every $y$, replacing $y$ by $ty$, for every $t\in E$, shows $x^{\mathsf T}B_i y=0$ for every $i,y$. The common-radical hypothesis gives $x=0$.

On $W\oplus W$ set

```math
\Omega_p((x,y),(x',y'))=\beta(x,y')+\beta(y,x').
\tag{3}
```

Since $\beta$ is alternating, this is alternating as well. Define $P$ on $W\oplus W\oplus Z$ by

```math
(u,z)(u',z')=(u+u',z+z'+\tfrac12\Omega_p(u,u')).
\tag{4}
```

Thus $P$ has exponent $p$, nilpotency class two, and $Z(P)=P'=Z$.

For the other prime, take $V=\bigoplus_{i=1}^k\mathbb F_q^2$, with $\gamma$ the orthogonal sum of the standard alternating forms on the planes. The same construction on $V\oplus V\oplus\mathbb F_q$, using

```math
\Omega_q((v,w),(v',w'))=\gamma(v,w')+\gamma(w,v'),
```

gives an exponent-$q$ extraspecial group $Q$, with $Z(Q)=Q'=\mathbb F_q$.

Let $A=A_p\times A_q$, where $A_p=\mathbb F_p^k$ and $A_q=\langle c\rangle\cong C_q$. Define its action as follows:

- $c$ acts on the two $W$-axes by $\lambda,\lambda^{-1}$, and trivially on $Z$ and $Q$;
- $a=(a_i)\in A_p$ acts on plane $i$ in the two $V$-axes by $\eta^{a_i},\eta^{-a_i}$, and trivially on both centers and $P$.

These actions preserve the brackets. Set $G=(P\times Q)\rtimes A$. There is an involution $\tau$ swapping the two axes of each prime factor, fixing both centers and inverting $A$.

Write $S=W\times V$ for the product of the first axes, and identify $t\in\mathbb F_q$ with the exponent of $c^t$. The central graph

```math
F=\{(a,t; a,c^t):a\in\mathbb F_p^k,\ t\in\mathbb F_q\}
\le (Z(P)\times Z(Q))\times A
```

normalizes $S$. Define

```math
H=S\rtimes F,
\qquad
K=\{g\in G:\tau(g)=g^{-1}\}.
\tag{5}
```

The loop is the loop represented by the folder $(G,H,K)$.

## 2. Loop-theoretic interfaces and admissibility

We use the [class-two folder parameterization](../packet/manuscripts/odd-class-two-classification.md), specifically its full-transversal test (6), normal-subgroup description (7)–(10), and actual-loop isomorphism criterion (15). These are imported results, not consequences of the linear algebra alone. The G-loop assertion additionally uses the symmetric-factorization interface stated in the [source construction](../packet/manuscripts/odd-alternating-form-family.md): in this odd-order full-inversion setting, a faithful generating folder with $H\cap\tau H=1$ and $|H|^2=|G|$ has that property.

Here the two center involutions and center actions are trivial, the positive cocycle is $f(a,c^t)=(a,t)$, and both bimaps are alternating. The quadratic obstruction in the full-transversal test vanishes: the first-axis actions are scalar on $W$, and scalar on each symplectic plane of $V$, so every term has the form $\beta(x,sx)$ or $\gamma(v,sv)$ within such a block. The negative center eigenspaces are zero. Consequently that test reduces to $f(b)\ne0$ for $b\ne1$, which holds because the graph map is injective.

The canonical-group conditions can also be read directly. Since $\lambda-1$ is invertible, commutators with $c$ generate the vector quotient of $P$; their brackets generate its center. The coordinate characters similarly generate $Q$. Thus $G'=P\times Q$. The action of $A$ is faithful, and the generation/core-freeness argument of the stated folder interface applies.

The first axes meet their swapped axes trivially. If an element lies in both $H$ and $\tau H$, its torus and central labels agree with both signs in the graph; oddness forces those labels to vanish. Hence $H\cap\tau H=1$. Finally,

```math
|G|=p^{2nr+2k}q^{4k+2},
\qquad |H|=p^{nr+k}q^{2k+1}.
```

This proves the claimed order and verifies the inputs for the G-loop interface.

## 3. Why the resulting loop is simple

We spell out how the strict-defect test specializes, since it is the mechanism that prevents the central extensions from producing normal subloops.

For a $\tau$-stable normal subgroup $N\lhd G$, put $L_p=N\cap P$, $L_q=N\cap Q$, and $C_p=L_p\cap Z(P)$. Let $T_p,T_q$ be the primary parts of the image of $N$ in $A$, and $J_p,J_q$ those of the image of $N\cap H$. The imported normal-subgroup description includes nonsplit lifts; no quotient-folder assertion is needed.

Coprime averaging separates central and vector coordinates in each $L_p,L_q$. A vector in the first axis injects into the fixed-vector space by $v\mapsto v+\tau v$. Therefore

```math
\frac{|C_{L_p}(\tau)|}{|H\cap L_p|}\ge |C_p|.
\tag{6}
```

Any nontrivial normal subgroup of $Q$ meets its center, so if $L_q\ne1$,

```math
\frac{|C_{L_q}(\tau)|}{|H\cap L_q|}\ge q.
\tag{7}
```

The normal-subgroup test also gives $|J_p|\le |C_p|$ and $|J_q|\le q$; a nontrivial $J_q$ requires $L_q\ne1$. One way to see the central restriction is that the center involution is the identity, so the negative central lift homomorphism in that test is zero. Membership of a graph element in $N$ then requires its graph label to lie in the corresponding central intersection.

Now consider a proper nonidentity $N$.

- If $T_q\ne1$, its action forces $L_p=P$, because it is fixed-point-free on $P/Z(P)$. If $T_p<A_p$, the $p$-part of the defect is strict: $|C_p|=p^k>|J_p|$. If $T_p=A_p$, all coordinate characters also force $L_q=Q$, giving $N=G$, contrary to properness.
- If $T_q=1$ but $T_p\ne1$, some character on $Q$ is moved. Thus $L_q\ne1$, while $J_q=1$, and (7) is strict after division by the graph contribution.
- If $T_p=T_q=1$, a nontrivial $N$ has a nontrivial intersection with at least one prime factor. A nontrivial normal subgroup of a finite $p$-group meets its center. That factor supplies strict defect, with no torus denominator.

In every case the other prime contribution is at least one. Formula (10) of the imported criterion therefore gives

```math
|C_N(\tau)|>|H\cap N|
\qquad(1<N<G).
```

The strict-defect criterion proves simplicity.

## 4. A concrete failure of the Moufang identity

For a coordinate $i$, retain the torus line $\langle e_i\rangle\le A_p$, its matching line in $Z(P)$, the $i$-th symplectic plane and $Z(Q)$. The restricted-section calculation in the source construction gives a subloop with coordinates $(u,t,s)\in\mathbb F_q^2\times\mathbb F_p\times\mathbb F_q$ and product

```math
(u,t,s)\cdot(v,a,h)
=(u+\eta^t v, t+a, s+h-\gamma(u,v)).
\tag{8}
```

This section calculation is part of the imported construction interface; the identity failure following from it is explicit. Choose $\gamma(v,w)=1$, and set $X=(0,1,0)$, $Y=(v,0,0)$, $Z_0=(w,0,0)$. The two sides of

```math
(XY)(Z_0X)=(X(YZ_0))X
```

have the same first and second coordinates, but their central coordinates are respectively $-\eta$ and $-1$. Since $\eta\ne1$, the loop is non-Moufang.

## 5. Recovering the tuple from the loop

The actual-loop isomorphism criterion cited in Section 2 preserves the two prime factors, the first axes, the central graphs and the actions. On the $Q$ first axis, the distinct characters are precisely $a\mapsto\eta^{a_i}$, each on a two-dimensional plane. Because $\mathbb F_q$ is the prime field, their intertwining permits a permutation of these characters, but no field twist. Thus the induced map on $A_p$, and hence on $Z(P)$, is a coordinate permutation $e_i\mapsto e_{\pi(i)}$.

An axis map intertwining multiplication by $\lambda$ with multiplication by $\lambda^u$ must have $u=p^j\pmod q$, because these scalars must have the same minimal polynomial over $\mathbb F_p$. It is therefore $L\circ\theta$, with $L\in\operatorname{GL}_n(E)$ and $\theta(x)=x^{p^j}$. Preservation of (2), and nondegeneracy and Frobenius invariance of the trace, give exactly (1).

Conversely, take data satisfying (1). Use $L\circ\theta$ on both $P$-axes, the permutation $\pi$ on $Z(P)$, and send $c\mapsto c^u$, where $u=p^j\pmod q$. On $Q$, permute the character planes by $\pi$ and choose on each plane an alternating similitude with multiplier $u\in\mathbb F_q^\times$. Use the same map on the second axis and multiplication by $u$ on $Z(Q)$. In dimension two such a similitude exists for every nonzero multiplier. These maps preserve brackets, intertwine the torus actions and carry both central graphs to their counterparts. The imported criterion gives a loop isomorphism, proving the converse.

## 6. Scope and further questions

The result classifies inputs within this fixed-parameter construction. It does not exhaust all odd simple Bol loops, all class-two folders, or tuples under arbitrary linear combinations of the forms. It gives no efficient orbit algorithm or complexity-class hardness theorem.

The next structural question is to identify tractable subclasses of the semilinear congruence problem (1), while [0024](0024-matrix-pair-embedding.md) explains why a general closed list should not be expected from these parameters alone.

**Source.** This exposition follows [Simple odd Bol loops from alternating-form tuples](../packet/manuscripts/odd-alternating-form-family.md), content blob `280882c2a46a0dff0f8a0af147ca6cf961940ff1`. The source records the normal-form/isomorphism input at `226a8dc1eb503026c350ffe3b7ac93da9077a593`, the symmetric-factorization input at `7fbfbc5a56f4bb1ead9a4d6202c2d948a67950d8`, and the restricted-section construction input at `722ba8c289c96dfd87c98f9a5ab3dcb8b2080998`. These are dependency pins, not a claim that this exposition independently verifies all upstream theorems.
