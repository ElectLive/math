# Associator quantization and intrinsic mixing in reciprocal Bol loops

Mira Cult

The actual associators of a reciprocal Bol loop give an intrinsic Markov
operator with a sharp, dimension-independent spectral gap. Averaging its
conjugates by the actual left translations removes its stationary-orbit
obstruction and gives an exact gap to global constants. Let $`Q=|E|`$,
let $`B_1,\ldots,B_k`$ be the admissible alternating pencil defined below,
and put $`r_{\min}=\min_i\operatorname{rank}_E B_i`$. The two exact norms are

```math
 \boxed{\;
 \|\mathcal M-\Pi\|_{2\to2}
   =\Lambda:=\frac1p+\left(1-\frac1p\right)Q^{-r_{\min}},
 \qquad
 \|\mathcal A-P\|_{2\to2}=p^{-2}.
 \;}                                                       \tag{AQ.1}
```

Here $`\mathcal A`$ averages the actual left-inner defects,
$`P`$ projects onto their common fixed space, $`\mathcal M`$ averages
left-translation conjugates of those defects, and $`\Pi`$ projects onto
constants. Both operators are intrinsic under genuine loop isomorphisms.
They are positive semidefinite, so their powers have the exact respective
norms $`\Lambda^t`$ and $`p^{-2t}`$. The corresponding mean squared
failure of multiplicativity satisfies sharp lower bounds in terms of
distance to constants or to $`\operatorname{ran}P`$.

The proof retains the full operator-valued associator. In each character
sector of the right nucleus, an actual left translation is a finite Weyl
operator followed by a cotangent symplectic dilation. Its product correction
is another modulation-dilation operator, not a scalar. We prove its
isomorphism and section-gauge laws, its exact nonabelian reassociation
identity, and the additional inverse-pair relation imposed by the Bol law.
That relation makes the defect average reversible for every finite left Bol
loop. The explicit reciprocal geometry supplies positivity and the sharp
spectrum for the present family.

All results are proved uniformly for $`R_A=\mathbf Z/q^A\mathbf Z`$,
$`A\geq1`$, with all additive-character conductors retained. No simplicity,
G-loop, classification, or automorphy assertion is a premise. The complete
intrinsic spectrum records joint-image incidences of the pencil, although
the largest nonconstant eigenvalue of $`\mathcal M`$ needs only
$`r_{\min}`$. This distinction is part of the result: the global gap is
an intrinsic analytic consequence of the loop law, not a new separation
between pencils having identical individual ranks.

The starting section is the one identified in
[bol-collective-cancellation.md](bol-collective-cancellation.md), inspected
at workspace revision `76d987909254eabf93073648818838fc09fb32b7`.
Its public construction source is
[BOL-0025](../REFERENCES.md#bol-0025), pinned there at
`f54b5376cb098e52d56ba0e599598d92ff6978a3`. We verify the loop identities
needed here directly. All theorem and equation labels in this manuscript
are local.

## 1. Admissible family, operators, and theorem statements

### 1.1. The prime-power reciprocal family

Let $`p,q`$ be distinct odd primes with $`p\mid q-1`$. Fix $`A\geq1`$,
write $`m=q^A`$, and let $`E`$ be a finite field of characteristic $`p`$
containing $`\lambda`$ of exact order $`m`$. Write $`Q=|E|`$.
Choose $`\eta\in R_A^\times`$ of order $`p`$ whose reduction modulo
$`q`$ has order $`p`$. Thus every nonzero difference of powers of
$`\eta`$ is a unit of $`R_A`$.

Let $`n,k\geq1`$, and let $`B_1,\ldots,B_k`$ be alternating
$`n\times n`$ matrices over $`E`$, independent over $`\mathbf F_p`$,
with zero common radical. Define

```math
 \begin{split}
 W&=E^n,\qquad V=\bigoplus_{i=1}^kR_A^2,\qquad U=W\oplus V,\\
 Z&=\mathbf F_p^k\oplus R_A,\\
 \beta(w,w')_i
   &=\operatorname{Tr}_{E/\mathbf F_p}(w^{\mathsf T}B_iw'),\\
 \gamma(v,v')&=\sum_{i=1}^k
      (v_{i,1}v'_{i,2}-v_{i,2}v'_{i,1}),\\
 b((w,v),(w',v'))&=(\beta(w,w'),\gamma(v,v')),\\
 R(a,t)(w,(v_i)_i)
   &=\bigl(\lambda^t w,(\eta^{a_i}v_i)_i\bigr).
 \end{split}                                                \tag{AQ.2}
```

All finite measures in this manuscript are normalized counting measures.
In particular, $`\mathbb E_X=|X|^{-1}\sum_{x\in X}`$ and all Hilbert norms
are normalized $`L^2`$ norms. The loop is $`\mathcal L=U\times Z`$ with

```math
 (u,c)\circ(v,d)
   =\bigl(u+R(c)v,\ c+d-b(u,v)\bigr).                         \tag{AQ.3}
```

The scalar actions satisfy

```math
 b(R(c)u,v)=b(u,R(c)v),\qquad b(u,R(c)u)=0.                  \tag{AQ.4}
```

For a permutation $`g`$ of $`\mathcal L`$, use pushforward unitaries
$`U_gf=f\circ g^{-1}`$. Thus $`U_gU_h=U_{gh}`$.
Write $`L_x(y)=x\circ y`$, and define

```math
 \ell_{x,y}=L_{x\circ y}^{-1}L_xL_y,\qquad
 \mathcal A=\mathbb E_{x,y\in\mathcal L}U_{\ell_{x,y}}.
                                                               \tag{AQ.5}
```

Let $`H=\langle\ell_{x,y}:x,y\in\mathcal L\rangle`$ and
$`P=\mathbb E_{h\in H}U_h`$. The global operator is

```math
 \mathcal M
   =\mathbb E_{z\in\mathcal L}U_{L_z}^{*}\mathcal A U_{L_z}
   =\mathbb E_{x,y,z\in\mathcal L}
      U_{L_z^{-1}\ell_{x,y}L_z},
 \qquad
 \Pi f=\mathbb E_{\mathcal L}f.                              \tag{AQ.6}
```

Both are averages of specified permutations of the actual loop. They
involve neither a chosen basis of the pencil nor a chosen right-nucleus character.

### 1.2. Main analytic theorem

**Theorem A (intrinsic and global mixing).** For every admissible family
in Section 1.1, $`\mathcal A`$ and $`\mathcal M`$ are self-adjoint,
positive semidefinite Markov operators. For every integer $`t\geq1`$,

```math
 \|\mathcal A^t-P\|_{2\to2}=p^{-2t},
 \qquad
 \|\mathcal M^t-\Pi\|_{2\to2}=\Lambda^t,
 \quad
 \Lambda=\frac1p+\left(1-\frac1p\right)Q^{-r_{\min}}<1.
                                                               \tag{AQ.7}
```

Define the local and globally translated multiplicativity-defect energies by

```math
 \begin{split}
 \mathcal E_{\rm loc}(f)
   &=\mathbb E_{x,y}
      \|U_{L_x}U_{L_y}f-U_{L_{x\circ y}}f\|_2^2,\\
 \mathcal E_{\rm glob}(f)
   &=\mathbb E_{x,y,z}
      \|U_{L_x}U_{L_y}U_{L_z}f
        -U_{L_{x\circ y}}U_{L_z}f\|_2^2 .
 \end{split}                                                \tag{AQ.8}
```

Then

```math
 \begin{split}
 2(1-p^{-2})\|f-Pf\|_2^2
   &\leq \mathcal E_{\rm loc}(f)\leq2\|f-Pf\|_2^2,\\
 2(1-\Lambda)\|f-\Pi f\|_2^2
   &\leq \mathcal E_{\rm glob}(f)\leq2\|f-\Pi f\|_2^2.
 \end{split}                                                \tag{AQ.9}
```

Both lower constants are sharp. The operators, projections, spectra and
energies are transported by every actual loop isomorphism.

The exact spectrum of $`\mathcal A`$ is given in Theorem B below. In
particular, there is no omitted exceptional scalar character. The fixed
space of $`\mathcal A`$ is generally larger than the constants and is
generally not invariant under all left translations. The use of
$`\mathcal M`$ is what gives a global gap.

For a concrete infinite family, take $`p=3`$, $`q=7`$, $`k=1`$,
$`E=E_A=\mathbf F_{3^{\operatorname{ord}_{7^A}(3)}}`$,
$`W=E_A^{2h}`$ for $`h\geq1`$, and $`B_1`$ the standard nondegenerate
alternating matrix. Choose the order-three unit lifting $`2\bmod7`$ and
an element of order $`7^A`$ in $`E_A`$. These data meet every hypothesis.
Here

```math
 |\mathcal L|=3\,7^{3A}|E_A|^{2h},
 \qquad
 \|\mathcal A-P\|=\frac19,\qquad
 \|\mathcal M-\Pi\|=\frac13+\frac23|E_A|^{-2h}.               \tag{AQ.10}
```

Thus the gap persists while dimension or conductor grows. More generally,
the theorem applies to the coupled and aligned pencils in the earlier
collective-cancellation construction whenever they meet Section 1.1.

A direct consequence is the correlation estimate

```math
 |\langle\mathcal M^t f,g\rangle|
 \leq\Lambda^t\|f\|_2\|g\|_2,
 \qquad \mathbb E f=\mathbb E g=0.                           \tag{AQ.11}
```

For the corresponding random walk, a point mass has total-variation
distance at most $`\tfrac12\sqrt{|\mathcal L|-1}\,\Lambda^t`$ from
normalized counting measure after $`t`$ steps. This follows by
Cauchy--Schwarz from (AQ.7); no claim about the computational cost of
sampling one step is needed.

## 2. The actual section and its intrinsic defects

### 2.1. Section identification and direct Bol verification

The class-two group on $`U\oplus U\oplus Z`$ has product

```math
 (X,Y,z)(X',Y',z')
 =\left(X+X',Y+Y',z+z'
   +\frac12\{b(X,Y')+b(Y,X')\}\right).
```

Adjoin $`Z`$ acting as $`(R(c),R(-c))`$ on the two vector axes
and trivially on the center. The action is by automorphisms because of
(AQ.4). The reciprocal stabilizer graph and inverted section are

```math
 \mathsf H=\{(X,0,c;c):X\in U,c\in Z\},
 \qquad
 \mathsf K=\{(X,-R(-c)X,0;c):X\in U,c\in Z\}.
```

Right reduction modulo $`\mathsf H`$ gives coordinates
$`(Y,z-c+\tfrac12b(X,Y))`$. The section point of coordinates
$`(Y,d)`$ is $`(-R(-d)Y,Y,0;-d)`$. Multiplying and reducing yields
(AQ.3). Thus the analytic loop uses the actual reciprocal graph and section,
rather than a symplectic space introduced independently of them.
The group $`\mathsf H`$ here is the source's folder stabilizer;
the intrinsic defect group $`H`$ in (AQ.5) will be computed separately.

The identity in (AQ.3) is $`(0,0)`$. Both divisions are explicit. If the
left factor $`(u,c)`$ and product $`(X,e)`$ are fixed, the right factor is

```math
 v=R(-c)(X-u),\qquad d=e-c+b(u,v).
```

If instead the right factor $`(v,d)`$ and product are fixed, the left
factor is

```math
 c=e-d+b(X,v),\qquad u=X-R(c)v.
```

The second formula uses $`b(R(c)v,v)=0`$. The two-sided inverse of
$`(u,c)`$ is $`(-R(-c)u,-c)`$.

For $`x=(u,c)`$, $`y=(v,d)`$, $`z=(w,e)`$, expanding
$`x\circ(y\circ(x\circ z))`$ and
$`(x\circ(y\circ x))\circ z`$ gives the same vector coordinate

```math
 u+R(c)v+R(c+d)u+R(2c+d)w
```

and the same central coordinate

```math
 2c+d+e-b(u,w)-b(v,R(c)w)-b(u,R(c+d)w).
```

Only (AQ.4) is used. Hence (AQ.3) is a left Bol loop at every level
$`A`$, independently of any source simplicity theorem.

It is not Moufang. Choose $`e\ne0`$ in $`W`$ and
$`v,w`$ in one ring plane with $`\gamma(v,w)=1`$.
For $`x=(e,v,0,0)`$, $`y=(0,w,0,0)`$, the $`W`$ coordinates of
$`(x\circ y)\circ x`$ and $`x\circ(y\circ x)`$ are respectively
$`(1+\lambda^{-1})e`$ and $`2e`$. They differ, violating flexibility.

### 2.2. Exact correction permutations, group, and orbits

For $`x=(u,c)`$, $`y=(v,d)`$, put

```math
 g=b(u,v),\qquad
 h=R(g)u-R(d)u+R(c+g)v-v .
```

Direct use of the division formulas gives

```math
 \boxed{\;
 \ell_{x,y}=H_{h,g},\qquad
 H_{h,g}(w,e)=\bigl(R(g)w,e+b(h,w)\bigr).
 \;}                                                       \tag{AQ.12}
```

The sign in this definition is fixed throughout. Balancedness gives

```math
 H_{h,g}H_{h',g'}
    =H_{h'+R(g')h,\;g+g'},\qquad
 H_{h,g}^{-1}=H_{-R(-g)h,\,-g}.                              \tag{AQ.13}
```

The intrinsic group $`H`$ consists of all $`H_{h,g}`$.
Indeed, choose $`d`$ with $`q`$-coordinate $`1`$ and all
$`p`$-coordinates $`1`$. Then $`I-R(d)`$ is invertible.
The pairs $`((u,c),(0,d))`$ yield every $`H_{h,0}`$.
Removing these shears from (AQ.12) yields every $`H_{0,b(u,v)}`$.

The values of $`b`$ generate $`Z`$. The $`\gamma`$ values contain
$`1`$. If a nonzero $`\nu\in\mathbf F_p^k`$ annihilated all
$`\beta`$ values, nondegeneracy of the trace pairing would give
$`B_\nu:=\sum_i\nu_iB_i=0`$, contradicting independence.
Thus the $`\beta`$ values span $`\mathbf F_p^k`$.
This proves the asserted generation. Zero common radical and faithfulness
of $`R`$ also make the displayed parameters of $`H`$ faithful.

Let $`I_w=b(U,w)\leq Z`$. The exact orbit of $`(w,e)`$ is

```math
 \boxed{\quad R(Z)w\times(e+I_w).\quad}                     \tag{AQ.14}
```

Balancedness implies $`I_{R(g)w}=I_w`$. Every point on the axis
$`w=0`$ is fixed. Consequently $`\mathcal A`$ alone cannot mix to
global constants; its correct stationary projection is $`P`$.

### 2.3. The right nucleus

The right nucleus of a loop consists of the elements $`n`$ satisfying
$`x\circ(y\circ n)=(x\circ y)\circ n`$ for all $`x,y`$.
For (AQ.3),

```math
 N_r(\mathcal L)=\{0\}\times Z.                              \tag{AQ.15}
```

Pure $`Z`$ is visibly right nuclear. Conversely, a right-nuclear
$`(w,e)`$ must be fixed by every defect. Taking the pairs used above
forces $`b((I-R(d))u,w)=0`$ for every $`u,d`$.
Taking $`d=(0,1)`$ and using $`1-\lambda\ne0`$ forces
$`\beta(W,w_W)=0`$, hence $`w_W=0`$ by zero common radical and the
perfect trace pairing. Taking $`d`$ supported in a single
$`p`$-coordinate forces $`w_i=0`$, because $`1-\eta`$ is a unit
and the ring symplectic form is perfect. Thus $`w=0`$.

This nucleus is intrinsic. It is not being identified with the loop
center; the latter terminology would erase its nontrivial left action.

## 3. Character sectors and corrected Weyl quantization

### 3.1. Scalar radicals and what scalar reduction forgets

Use the characters

```math
 \chi_{\nu,\rho}(a,t)=e_p(\nu\cdot a)e_m(\rho t),
 \qquad
 (\nu,\rho)\in\mathbf F_p^k\oplus R_A ,
 \quad e_s(x)=\exp(2\pi i x/s).
```

Set $`v_q(0)=A`$ and $`a_\rho=A-v_q(\rho)`$.
The radical of the scalar alternating bicharacter
$`(u,v)\mapsto\chi_{\nu,\rho}(b(u,v))`$ is exactly

```math
 D_{\nu,\rho}
   =\ker_E B_\nu\ \oplus\
      \bigoplus_{i=1}^k\{v_i\in R_A^2:\rho v_i=0\},
 \qquad
 d_{\nu,\rho}:=\frac{|D_{\nu,\rho}|}{|U|}
   =Q^{-r_\nu}q^{-2k a_\rho},                              \tag{AQ.16}
```

where $`r_\nu=\operatorname{rank}_E B_\nu`$.
For the field component, the trace pairing turns scalar radical membership
into $`B_\nu w=0`$. For the ring component, perfectness of the determinant
pairing gives $`\rho v_i=0`$. This proves (AQ.16), including the trivial
character and every imprimitive ring character.

Thus zero common radical of the vector-valued pencil does not make every
scalar specialization nondegenerate. All rank strata $`r_\nu`$ and all
annihilator ideals of $`\rho`$ are present. Quotienting by
$`D_{\nu,\rho}`$ gives the familiar nondegenerate finite Heisenberg
problem. It forgets the radical and, if treated one character at a time,
the intersections and images relating different $`B_\nu`$.

The reciprocal action preserves $`D_{\nu,\rho}`$ by balancedness.
It need not preserve the scalar alternating bicharacter itself:
$`b(R(c)u,R(c)v)=b(u,R(2c)v)`$ generally differs from $`b(u,v)`$.
One therefore cannot declare the entire reciprocal action symplectic on
that scalar quotient. The doubled cotangent Weyl realization below implements
the actual translations without making that false identification.

### 3.2. Intrinsic sectors and actual isomorphisms

Right translations by $`N_r(\mathcal L)`$ commute with every left
translation. Since this nucleus is abelian, the regular Hilbert space
decomposes canonically into its character sectors. With normalized point
vectors, use the coordinate basis

```math
 |u;\chi\rangle
  =|Z|^{-1/2}\sum_{e\in Z}\overline{\chi(e)}\,|u,e\rangle .
```

The right translation by $`n\in Z`$ acts as $`\chi(n)`$.
The actual left translations restrict to

```math
 \boxed{\quad
 \pi_\chi(a,c)|u\rangle
   =\chi(c-b(a,u))\,|a+R(c)u\rangle .
 \quad}                                                     \tag{AQ.17}
```

These unitary matrices projectively distinguish the loop elements:
their affine permutation supports determine $`a`$ and the faithful
$`R(c)`$. They are not an ordinary multiplicative representation.

Let $`\phi:\mathcal L\to\mathcal L'`$ be an actual loop isomorphism.
It restricts to a group isomorphism
$`\phi_N:N_r(\mathcal L)\to N_r(\mathcal L')`$, and transports the
character to $`\chi'=\chi\circ\phi_N^{-1}`$. In the chosen charts write

```math
 \phi(u,0)=(F(u),s(u)).
```

Right-nucleus equivariance then gives

```math
 \phi(u,e)=(F(u),s(u)+\phi_N(e)),\qquad
 C_{\phi,\chi}|u\rangle=\chi'(s(u))\,|F(u)\rangle.            \tag{AQ.18}
```

Here $`F`$ is a permutation of nucleus-coset sets; no additivity is
assumed. The regular unitary $`C_\phi|x\rangle=|\phi(x)\rangle`$
conjugates $`U_{L_x}`$ to $`U_{L'_{\phi(x)}}`$ and restricts to
(AQ.18). It therefore intertwines every full defect and every average
defined in (AQ.5)--(AQ.6). This proves the intrinsic naturality assertions.

Changing the representative of each right-nucleus coset changes the
Schrödinger chart by a diagonal unitary. This is a section-gauge change
of basis, not automatically a loop isomorphism. No invariance under
arbitrary isotopy is asserted.

### 3.3. The full Weyl correction

Let $`\widehat U`$ be the character group of the finite odd abelian
group $`U`$, and define
$`B_\chi(a)(u)=\chi(b(a,u))`$.
For $`\xi\in\widehat U`$, define

```math
 W(a,\xi)|u\rangle=\xi(u+a/2)|u+a\rangle,\qquad
 D_c|u\rangle=|R(c)u\rangle,\qquad
 M_\xi|u\rangle=\xi(u)|u\rangle.
```

The ordinary finite Weyl product is

```math
 W(a,\xi)W(b,\zeta)
  =\xi(b/2)\zeta(a/2)^{-1}W(a+b,\xi\zeta).                  \tag{AQ.19}
```

The cotangent symplectic map
$`S_c(a,\xi)=(R(c)a,\xi\circ R(-c))`$ has the exact implementation

```math
 D_cW(a,\xi)D_c^{-1}=W(S_c(a,\xi)).
```

Using additive notation in the character index, (AQ.17) becomes

```math
 \boxed{\quad
 \pi_\chi(a,c)
  =\chi(c)\,W(a,-B_\chi(R(-c)a))D_c.
 \quad}                                                     \tag{AQ.20}
```

The possible half-phase vanishes by $`b(R(-c)a,a)=0`$.
For (AQ.12), the correction is

```math
 J_\chi(h,g)=D_gM_{B_\chi(h)},\qquad
 \pi_\chi(x)\pi_\chi(y)
    =\pi_\chi(x\circ y)J_\chi(h(x,y),b(u,v)).                \tag{AQ.21}
```

Indeed $`H_{h,g}`$ sends $`|u;\chi\rangle`$ to
$`\chi(b(h,u))|R(g)u;\chi\rangle`$.
The correction has both a modulation and a cotangent symplectic dilation.
It is an explicit realization in the established finite
Heisenberg--Weil/Jacobi framework. Matrix multiplication remains associative;
the nonassociativity is retained in the correction to multiplication of
the loop labels.

The actual Bol identity gives

```math
 \pi_\chi(x)\pi_\chi(y)\pi_\chi(x)
   =\pi_\chi(x\circ(y\circ x)).
                                                               \tag{AQ.22}
```

In particular,

```math
 \pi_\chi(u,c)
  =\pi_\chi(0,c/2)\,
    \pi_\chi(R(-c/2)u,0)\,
    \pi_\chi(0,c/2).                                       \tag{AQ.23}
```

This ties the graph Weyl family to the actual Bol palindrome.

## 4. Scalar obstruction and reassociation coherence

### 4.1. Every associative group image is trivial

**Proposition.** Every operation-preserving map from the loop (AQ.3)
to an associative group is trivial, at every level $`A`$.

**Proof.** Let $`f:\mathcal L\to G`$ be such a map.
Its identity image is an idempotent in a group, hence is $`1`$.
Use $`f_W,f_V,f_Z`$ for its restrictions to the pure coordinate
elements. Pure $`W`$ and pure $`V`$ elements commute in the loop,
and every element factors as a vector element followed by a pure
$`Z`$ element.

Choose $`v_1,v_2\in V`$ with $`\gamma(v_1,v_2)=1`$.
For a pure $`w\in W`$, the words
$`(v_1\circ v_2)\circ w`$ and
$`v_1\circ(v_2\circ w)`$ have the same $`V`$ and $`Z`$
coordinates and have $`W`$ coordinates $`\lambda^{-1}w`$ and
$`w`$. Their images agree by associativity in $`G`$.
Factoring and cancelling gives
$`f_W(\lambda^{-1}w)=f_W(w)`$.
On every $`E`$-line $`Ew`$, all the alternating forms vanish, so
the pure-$`W`$ product is additive. Therefore
$`f_W((\lambda^{-1}-1)w)=1`$.
The scalar is invertible, so every pure $`W`$ element dies.

Pure-$`W`$ products now kill all $`\beta(w,w')`$ in the
$`p`$-part of $`Z`$. Those values span $`\mathbf F_p^k`$ by the
trace-and-independence argument of Section 2.2. Thus that whole subgroup
dies. Its action on one $`V_i`$ gives
$`f_V(\eta v)=f_V(v)`$.
The product on the $`R_A`$-line $`R_Av`$ is additive, so
$`f_V((\eta-1)v)=1`$. Since $`\eta-1`$ is a unit, all
$`V_i`$ die. Pure-$`V`$ products then kill the remaining
$`R_A`$ subgroup of $`Z`$ because the $`\gamma`$ values contain $`1`$.
These factors generate the loop, proving the proposition. $`\square`$

If unitaries satisfy
$`T_xT_y=\alpha(x,y)T_{x\circ y}`$ with scalar phases, their classes in
$`PU(\mathcal H)`$ form such a group image. All $`T_x`$ are therefore
projectively equal. A scalar-projective closure cannot retain this family.

Likewise, the universal unital associative quotient of the complex loop
algebra is just $`\mathbf C`$ via augmentation. Every basis element
has a two-sided inverse, so its image in an associative quotient is a
unit; the proposition makes all such images equal to $`1`$.

These are obstructions to specified scalar and associative constructions.
They do not exclude Beck modules, nonabelian correction operators,
nonassociative star products, or category-valued quantization.

### 4.2. General transport and the additional Bol identity

For any loop's translation operators write

```math
 D(x,y)=\pi(x\circ y)^{-1}\pi(x)\pi(y).
```

For $`P_0=(x\circ y)\circ z`$, $`Q_0=x\circ(y\circ z)`$, define
$`T_{P_0\to Q_0}=\pi(Q_0)^{-1}\pi(P_0)`$.
Expanding $`\pi(x)\pi(y)\pi(z)`$ in its two ways gives

```math
 T_{P_0\to Q_0}D(x\circ y,z)\,
       \operatorname{Ad}_{\pi(z)^{-1}}D(x,y)
   =D(x,y\circ z)D(y,z).                                   \tag{AQ.24}
```

The distinct loop values $`P_0,Q_0`$ remain present. Setting the
transport to the identity without an additional proof would erase
nonassociativity.

For any parenthesized word, transports defined from its actual evaluations
telescope. Consequently all reassociation paths with fixed endpoints,
including a pentagon, give the same transport. This coherence is formal for
any loop and supplies no analytic estimate by itself. It is not the
construction of a scalar $`3`$-cocycle on an associative group.

The Bol law adds the stronger identity

```math
 D(x,y\circ x)D(y,x)=I,
 \qquad
 \ell_{u,v}^{-1}=\ell_{v,u\circ v}.                          \tag{AQ.25}
```

For the first relation, cancel the intermediate
$`\pi(y\circ x)`$ and apply (AQ.22). The second is the same calculation
for the actual permutations. The map
$`(u,v)\mapsto(v,u\circ v)`$ is bijective by right division.
Thus the uniform defect distribution is invariant under inversion.
This proves self-adjointness of $`\mathcal A`$ for every finite left
Bol loop, before using any reciprocal coordinates.

For every such loop,

```math
 \mathcal E_{\rm loc}(f)
   =2\|f\|_2^2-2\langle\mathcal A f,f\rangle,                \tag{AQ.26}
```

because $`U_{L_{x\circ y}}^*U_{L_x}U_{L_y}=U_{\ell_{x,y}}`$.
The reciprocal calculation below adds positivity and a quantitative gap.

### 4.3. A non-Bol control

Reversibility of the uniform defect average is not automatic for arbitrary
loops. On $`\{0,1,2,3,4\}`$, consider the multiplication table

```math
 T=
 \begin{pmatrix}
 0&1&2&3&4\\
 1&0&3&4&2\\
 2&3&4&0&1\\
 3&4&1&2&0\\
 4&2&0&1&3
 \end{pmatrix}.
```

Every row and column is a permutation and $`0`$ is the identity. Directly
enumerating the 25 defects $`L_{xy}^{-1}L_xL_y`$ gives the transition
matrix below, with **rows denoting starting states and columns ending
states**:

```math
 \mathsf P=\frac1{25}
 \begin{pmatrix}
 25&0&0&0&0\\
 0&16&3&3&3\\
 0&3&11&5&6\\
 0&3&6&11&5\\
 0&3&5&6&11
 \end{pmatrix}.
```

It is doubly stochastic but not symmetric:
$`\mathsf P_{2,3}=5/25`$ while $`\mathsf P_{3,2}=6/25`$.
The Bol identity fails on 57 of the 125 triples; for
$`(x,y,z)=(1,0,2)`$ its two sides are $`4`$ and $`2`$.
Thus this control genuinely lies outside the Bol hypothesis, and shows
what (AQ.25) contributes beyond generic permutation reassociation.
The exact [enumerator](../code/verify_nonbol_reversibility_control.py)
and its finite scope are included in the reproduction record.

## 5. Complete intrinsic spectrum at every conductor

Fix a right-nucleus character $`\chi=(\nu,\rho)`$ and a vector
$`z=(w,(z_i)_i)\in U`$. Put
$`J(z)=\{i:z_i\ne0\}`$.
The orbit $`R(Z)z`$ is a product of an $`m`$-cycle if $`w\ne0`$
and a $`p`$-cycle for each $`i\in J(z)`$.
The first assertion uses the exact order of $`\lambda`$; the second
uses that every nonzero difference of powers of $`\eta`$ is a unit,
even when $`z_i`$ is imprimitive.

Its orbit-character labels are precisely

```math
 (\alpha,\sigma)\in\mathbf F_p^k\oplus R_A,\qquad
 \alpha_i=0\ \text{if }z_i=0,\qquad
 \sigma=0\ \text{if }w=0.                                  \tag{AQ.27}
```

Set $`B_\alpha=\sum_i\alpha_iB_i`$,
$`r_\alpha=\operatorname{rank}_E B_\alpha`$,
$`a_\sigma=A-v_q(\sigma)`$, and

```math
 \begin{split}
 t_\alpha(w,\nu)
  &=Q^{-r_\alpha}\left[
       m^{-2}+(1-m^{-2})
       \mathbf1_{\{B_\nu w\in\operatorname{im}_E B_\alpha\}}
                    \right],\\
 j_{\rho,\sigma}(z_V)
  &=\#\{i:\rho z_i\notin\sigma R_A^2\},\\
 s_\sigma(z_V,\rho)
  &=q^{-2k a_\sigma}p^{-2j_{\rho,\sigma}(z_V)}.
 \end{split}                                                \tag{AQ.28}
```

These definitions include $`\alpha=0`$, $`\sigma=0`$,
$`\nu=0`$ and $`\rho=0`$ literally.

**Theorem B (exact intrinsic spectrum).** In the nucleus-character
sector $`(\nu,\rho)`$ over the vector orbit $`R(Z)z`$,
$`\mathcal A`$ is convolution on that orbit. Its eigenvalue at the
allowed orbit character $`(\alpha,\sigma)`$ is

```math
 \boxed{\quad
 \lambda_{\nu,\rho;z;\alpha,\sigma}
    =t_\alpha(w,\nu)s_\sigma(z_V,\rho).
 \quad}                                                     \tag{AQ.29}
```

All eigenvalues are nonnegative. The projection $`P`$ in this block
vanishes unless

```math
 B_\nu w=0,\qquad \rho z_i=0\quad(1\leq i\leq k).             \tag{AQ.30}
```

If (AQ.30) holds, $`P`$ is uniform averaging on the vector orbit.
In that case its range is the trivial orbit-character line.
These are exactly the eigenvalue-one spaces of (AQ.29).

### 5.1. An alternating bilinear average

Let $`B`$ be an alternating matrix over $`E`$, let $`w'\in E^n`$,
and let $`a,a'\in E`$. For
$`\psi(x)=e_p(\operatorname{Tr}_{E/\mathbf F_p}x)`$,

```math
 \mathbb E_{u,v\in E^n}
  \psi(u^{\mathsf T}Bv+a\,u^{\mathsf T}w'
                        +a'\,v^{\mathsf T}w')
 =Q^{-\operatorname{rank}B}
   \begin{cases}
     1,&w'\in\operatorname{im}B\ \text{or }a=a'=0,\\
     0,&\text{otherwise}.
   \end{cases}                                             \tag{AQ.31}
```

To prove it, average over $`v`$. The equation is
$`Bu=a'w'`$. If $`w'=Bu_0`$, its solutions form
$`a'u_0+\ker B`$. The remaining phase vanishes because
$`u_0^{\mathsf T}w'=u_0^{\mathsf T}Bu_0=0`$ and $`w'`$
annihilates $`\ker B`$. The solution density is
$`Q^{-\operatorname{rank}B}`$.
If $`w'\notin\operatorname{im}B`$, solvability forces $`a'=0`$.
Averaging over $`\ker B`$ then forces $`a=0`$.
This includes $`B=0`$.

### 5.2. Fourier computation of the defect kernel

Compute pullback by $`H_{h,g}`$; this is the adjoint average and equals
$`\mathcal A`$ by (AQ.25). In the sector basis of Section 3, its phase
is $`\overline{\chi(b(h,z))}`$.
For a fixed $`g=b(u,v)`$, balancedness writes the argument as

```math
 b(h,z)=
 b(u,(R(g)-R(d))z)+b(v,(R(c+g)-I)z).                        \tag{AQ.32}
```

Impose $`b(u,v)=g`$ by normalized Fourier orthogonality:

```math
 \mathbf1_{\{b(u,v)=g\}}
   =|Z|^{-1}\sum_{\alpha,\sigma}
       e_p\bigl(\alpha\cdot(\beta(u_W,v_W)-g_p)\bigr)
       e_m\bigl(\sigma(\gamma(u_V,v_V)-g_q)\bigr).
```

The $`W`$ and $`V`$ integrations separate. Their actor variables
also separate: $`W`$ uses only $`c_q,d_q`$, while $`V`$ uses
only $`c_p,d_p`$.

For the $`W`$ factor, apply (AQ.31) with
$`B=B_\alpha`$, $`w'=-B_\nu w`$ and

```math
 a=\lambda^{g_q}-\lambda^{d_q},\qquad
 a'=\lambda^{c_q+g_q}-1 .
```

If $`B_\nu w\in\operatorname{im}B_\alpha`$, the answer is
$`Q^{-r_\alpha}`$. Otherwise both displayed coefficients must vanish.
They fix one value of $`d_q`$ and one of $`c_q`$, independently,
so their averaged probability is $`m^{-2}`$.
This gives exactly $`t_\alpha`$, independently of $`g`$.
The minus sign from the conjugate character does not change image membership.

For a single $`R_A^2`$ plane, the required average has phase

```math
 e_m\!\left(
   \sigma\gamma(u,v)
   +\rho'[a\gamma(u,z_i)+a'\gamma(v,z_i)]
       \right),\qquad \rho'=-\rho ,
```

where $`a=\eta^{g_i}-\eta^{d_i}`$ and
$`a'=\eta^{c_i+g_i}-1`$ are each either zero or a unit.

If $`\rho' z_i\in\sigma R_A^2`$, choose $`w_i`$ with
$`\sigma w_i=\rho' z_i`$. Averaging over $`v`$ forces
$`\sigma u=a'\rho' z_i`$. Its solution coset has density
$`q^{-2a_\sigma}`$. The remaining phase is zero: on its representative
$`a'w_i`$ it is
$`aa'\gamma(w_i,\rho' z_i)
 =aa'\sigma\gamma(w_i,w_i)=0`$;
on $`\ker\sigma`$ it vanishes by the same equation.
This uses the perfect additive pairing on $`R_A^2`$, whose
annihilator of $`\ker\sigma`$ is $`\sigma R_A^2`$.

If $`\rho' z_i\notin\sigma R_A^2`$, a unit $`a'`$ makes
the equation insoluble. If $`a'=0`$, averaging over
$`\ker\sigma`$ vanishes unless $`a=0`$.
Thus only $`a=a'=0`$ survives, again with value
$`q^{-2a_\sigma}`$. Averaging $`c_i,d_i\in\mathbf F_p`$
contributes $`p^{-2}`$ in this incompatible case.
Multiplication over the planes gives $`s_\sigma`$ in (AQ.28).
This argument includes $`\sigma=0`$ and all imprimitive conductors.

Consequently the coefficient of pullback by $`R(g)`$ is

```math
 K_z(g)=|Z|^{-1}\sum_{\alpha,\sigma}
       e_p(-\alpha\cdot g_p)e_m(-\sigma g_q)
       t_\alpha(w,\nu)s_\sigma(z_V,\rho).                   \tag{AQ.33}
```

The factors are unchanged when $`z`$ is replaced by $`R(c)z`$:
the image condition is invariant under scaling by an $`E`$-unit,
and multiplication by the units $`\eta^{c_i}`$ preserves the ring
module-image tests. The operator is therefore convolution on the orbit.
Passing to the quotient by the orbit stabilizer retains exactly the
characters in (AQ.27); Fourier inversion proves (AQ.29).

Finally, (AQ.14) shows that a nucleus character survives the shear average
precisely when it annihilates $`I_z`$, which is (AQ.30).
In that case the remaining action is uniform orbit averaging.
This proves the assertion about $`P`$. $`\square`$

### 5.3. Sharp intrinsic gap and energy

For $`\alpha\ne0`$, independence gives $`B_\alpha\ne0`$.
Alternating rank is even, so $`r_\alpha\geq2`$ and
$`t_\alpha\leq Q^{-2}\leq p^{-2}`$.
For $`\sigma\ne0`$, $`a_\sigma\geq1`$, so
$`s_\sigma\leq q^{-2k}<p^{-2}`$.
For $`\alpha=\sigma=0`$ outside (AQ.30), either
$`t_0=m^{-2}<p^{-2}`$ or at least one incompatible ring plane
gives $`s_0\leq p^{-2}`$.
Thus every eigenvalue off $`P`$ lies in $`[0,p^{-2}]`$.

The value $`p^{-2}`$ is attained. Take $`w=0`$, one primitive
nonzero $`V`$-plane, $`\rho`$ a unit, and the trivial orbit character.
Then $`t_0=1`$, $`s_0=p^{-2}`$, and (AQ.30) fails.
This proves the first identity in (AQ.7), including its powers.
Combining it with (AQ.26) gives the first energy inequality in (AQ.9)
and the sharp lower constant.

The full spectrum keeps the joint condition
$`B_\nu w\in\operatorname{im}B_\alpha`$ and the ring conditions
$`\rho z_i\in\sigma R_A^2`$. These are stronger data than the
individual scalar ranks. The extremal value $`p^{-2}`$ is nonetheless
attained in a simple reciprocal-plane sector and does not separate pencils.

The zero-energy space is $`\operatorname{ran}P`$. It must not be called
a translation-invariant multiplicative subrepresentation. In fact, if a
subspace is invariant under every $`U_{L_x}`$ and their restrictions
obey ordinary multiplication, Proposition 4.1 makes all restrictions the
identity. A regular state fixed by all left translations is constant.
The global operator now converts this qualitative obstruction into a
uniform quantitative statement.

## 6. Conjugated defects: exact global mixing

### 6.1. Averaging the stationary projection

Introduce the auxiliary positive Markov operator

```math
 \mathcal C=\mathbb E_{z\in\mathcal L}U_{L_z}^{*}P U_{L_z}.
```

In the sector $`\chi`$, write $`D_\chi=D_{\nu,\rho}`$ and
$`d_\chi=|D_\chi|/|U|`$. The orbit calculation gives

```math
 P_\chi g(x)
   =\mathbf1_{D_\chi}(x)\mathbb E_{c\in Z}g(R(c)x).
```

The exact averaged conjugate is a convolution:

```math
 \boxed{\quad
 \mathcal C_\chi g(x)
  =d_\chi\mathbb E_{v\in D_\chi}\mathbb E_{c\in Z}
       g(x+(R(c)-I)v).
 \quad}                                                     \tag{AQ.34}
```

To verify the phase as well as the support, work on basis vectors.
Conjugate $`P_\chi`$ by $`\pi_\chi(a,d)`$.
The intermediate vector is $`y=a+R(d)x`$, which must lie in
$`D_\chi`$. A term with dilation $`R(c)`$ returns to

```math
 x'=x+R(-d)(R(c)-I)y .
```

The product of the two left-translation phases is
$`\chi(b(a,x'-x))`$. The difference $`x'-x`$ lies in the
$`R`$-invariant radical, so this phase is one.
As $`a`$ ranges uniformly over $`U`$,
$`v=R(-d)y`$ ranges uniformly over $`U`$; restricting to the radical
has density $`d_\chi`$. The actor $`d`$ disappears.
This proves (AQ.34) on vectors. The same convolution formula for functions
follows by replacing $`v`$ by $`-v`$.

It follows that $`\|\mathcal C_\chi\|=d_\chi`$, with equality on
the vector-constant function. For $`\chi\ne0`$, (AQ.16) gives

```math
 d_\chi\leq p^{-2}.
```

Indeed a nonzero $`\nu`$ has alternating rank at least two; a nonzero
$`\rho`$ has $`a_\rho\geq1`$ and
$`q^{-2k a_\rho}<p^{-2}`$.

For the trivial nucleus character, $`D_0=U`$.
On an additive vector frequency $`\xi`$, (AQ.34) has multiplier

```math
 \mathbb P_c[\xi\circ R(c)=\xi]
   =m^{-\mathbf1_{\{\xi_W\ne0\}}}p^{-|S(\xi_V)|},           \tag{AQ.35}
```

where $`S(\xi_V)`$ is the set of nonzero plane frequencies.
A nonzero $`W`$ frequency has trivial stabilizer in the cyclic
$`m`$-action. A nonzero ring-plane frequency, including an imprimitive
one, has trivial stabilizer in the $`p`$-action because nonzero
differences of powers of $`\eta`$ are units.
Thus

```math
 \|\mathcal C-\Pi\|_{2\to2}=p^{-1}.
```

### 6.2. The nontrivial nucleus sectors are below the global maximum

The intrinsic spectrum gives the operator inequality

```math
 0\leq\mathcal A\leq p^{-2}I+(1-p^{-2})P .
```

Average its conjugates. Every nontrivial nucleus sector obeys

```math
 0\leq\mathcal M_\chi
 \leq p^{-2}I+(1-p^{-2})\mathcal C_\chi,\qquad
 \|\mathcal M_\chi\|
 \leq2p^{-2}-p^{-4}<p^{-1},\quad\chi\ne0.                  \tag{AQ.36}
```

All left translations preserve these sectors, so this comparison applies
to the full operator. It treats the primitive and imprimitive characters
simultaneously. The eventual extremal mode must lie in the trivial
nucleus sector.

### 6.3. Exact multiplier in the trivial sector

At $`\chi=0`$, (AQ.12) loses its shear phase and gives

```math
 \mathcal A_0=\mathbb E_{u,v\in U}D_{b(u,v)}.
```

Averaging its affine conjugates by $`\pi_0(a,d)=T_aD_d`$
makes every additive vector frequency an eigenvector. Its multiplier is

```math
 \mathbb P_{u,v}
   [\,\xi\circ R(b(u,v))=\xi\,].
```

For fixed $`g`$, averaging the affine base point kills the frequency
unless $`\xi\circ R(g)=\xi`$; if that holds the affine phase is one.
This proves the displayed probability with normalized measures.

The $`W`$ and $`V`$ components of $`b(u,v)`$ are independent.
Writing $`S=S(\xi_V)`$, the exact multiplier is

```math
 \kappa_S\,\tau_A^{\mathbf1_{\{\xi_W\ne0\}}},
 \qquad
 \kappa_S=\mathbb P[\beta_i(u_W,v_W)=0\text{ for all }i\in S],
 \qquad
 \tau_A=\mathbb P[\gamma(u_V,v_V)=0].                       \tag{AQ.37}
```

Both factors have exact finite Fourier expressions:

```math
 \kappa_S
  =p^{-|S|}
     \sum_{\substack{\alpha\in\mathbf F_p^k\\
                     \operatorname{supp}\alpha\subseteq S}}
       Q^{-r_\alpha},
 \qquad
 \tau_A=m^{-1}
   \left[1+\sum_{a=1}^{A}(q^a-q^{a-1})q^{-2ka}\right].
                                                               \tag{AQ.38}
```

For $`\kappa_S`$, Fourier orthogonality and the bilinear average
$`\mathbb E\psi(u^{\mathsf T}B_\alpha v)=Q^{-r_\alpha}`$
suffice. For $`\tau_A`$, a ring character of conductor
$`q^a`$ contributes $`q^{-2ka}`$, and there are
$`q^a-q^{a-1}`$ such characters. These formulas retain all rank strata
and all conductors.

If $`S\ne\varnothing`$, its simultaneous-zero probability is bounded
by each single-coordinate probability. Each is exactly

```math
 \kappa_{\{i\}}
   =p^{-1}+(1-p^{-1})Q^{-r_i}.                             \tag{AQ.39}
```

The largest is attained by a frequency supported in a single plane of
minimal $`r_i`$, with $`\xi_W=0`$.

If $`S=\varnothing`$ and $`\xi_W\ne0`$, reduction modulo
$`q`$ bounds the remaining multiplier by

```math
 \tau_A
 \leq q^{-1}+(1-q^{-1})q^{-2k}
 <\frac{q+1}{q^2}<p^{-1}.                                  \tag{AQ.40}
```

The last inequality follows from $`q>p`$: already
$`q\geq p+1`$ gives $`q^2>p(q+1)`$.
The zero frequency gives the constant eigenvalue one.
Together with (AQ.36), (AQ.39) proves the second identity of (AQ.7),
with the stated sharp eigenvector.

Positivity of $`\mathcal M`$ follows from positivity of
$`\mathcal A`$. Hence its power norm is exactly $`\Lambda^t`$.
Averaging (AQ.26) after replacing $`f`$ by $`U_{L_z}f`$ gives

```math
 \mathcal E_{\rm glob}(f)
   =2\|f\|_2^2-2\langle\mathcal M f,f\rangle .
```

The spectrum now proves the second inequality in (AQ.9), and the
single-plane extremal frequency proves sharpness of its lower constant.
This completes Theorem A. $`\square`$

For comparison, combining only the intrinsic order bound with
$`\|\mathcal C-\Pi\|=p^{-1}`$ would give
$`p^{-1}+p^{-2}-p^{-3}`$. The exact zero-sector calculation replaces
this with $`p^{-1}+(1-p^{-1})Q^{-r_{\min}}`$, including its
extremizer and all conductor dependence. General Markov contraction alone
would give only one. These comparisons explain exactly which quantitative
work the explicit reciprocal calculation adds.

## 7. Controlled routes and what the Bol data contributes

The intrinsic operators use the loop multiplication and its actual
translations. Their Weyl-coordinate formulas use the chosen presentation.
This isomorphism-versus-marking distinction is preserved in the theorem.

| Route | Exact mathematical outcome | Analytic role |
|---|---|---|
| Scalar character and radical quotient | Ordinary nondegenerate finite Heisenberg problem after (AQ.16); reciprocal actions need not preserve its pairing | Baseline and rank/conductor bookkeeping |
| Scalar-projective loop matrices | Every group image is trivial by Proposition 4.1 | A proved obstruction for this family |
| Graph Weyl overlaps | Exact commuting twirls; the actual translation channel reduces to the earlier scalar-orbit transpose | Useful control, no additional endpoint |
| Full inner-defect average | Joint-image spectrum (AQ.29), sharp gap $`p^{-2}`$ to orbit invariants | Intrinsic quantitative reassociation information |
| Left-translation conjugates of full defects | Exact global norm (AQ.7) and sharp energy rigidity | Main mixing theorem |
| Category-valued magnetic/translation quantization | A legitimate distinct construction requiring categories, actions and higher coherence | Open; no analytic bound borrowed from formal reassociation |

For clarity, the graph calculation in the third row can be made explicit.
In $`U\oplus\widehat U`$, put

```math
 \Gamma_c=\{(a,-B_\chi(R(-c)a)):a\in U\}.
```

Cotangent transport gives $`S_d\Gamma_c=\Gamma_{c+2d}`$.
The normalized conjugation twirl over $`W(\Gamma_c)`$ is an
orthogonal projection in Hilbert--Schmidt norm. It retains exactly the
Weyl indices in

```math
 \Gamma_c^\perp
   =\{(x,B_\chi(R(-c)x)):x\in U\}.
```

This follows directly from Weyl commutation and character orthogonality.
Thus the twirls commute, and their products project onto the corresponding
intersections. Averaging over $`c`$ gives the multiplier

```math
 \mathbb P_c[\xi=B_\chi(R(-c)x)].
```

Its nonzero values are $`m^{-\epsilon}p^{-j}`$, where
$`\epsilon=1`$ exactly when $`B_\nu x_W\ne0`$, and
$`j=\#\{i:\rho x_i\ne0\}`$, with matching momentum required.
The fixed algebra consists of the translations along the scalar radical.

Nevertheless, on the nondegenerate scalar quotient, the conjugation channel
of the actual left translations, writing momentum as $`B_\chi y`$,
is exactly

```math
 \mathbb E_{a,c}
  \operatorname{Ad}_{\pi_\chi(a,c)}
      W(x,B_\chi y)
  =\mathbb P_c[y=R(c)x]\;W(y,B_\chi x).                     \tag{AQ.41}
```

To see this, first conjugate by $`D_c`$, then average the Weyl
commutator phase over $`a`$. Orthogonality imposes
$`B_\chi R(-c)y=B_\chi x`$; after quotienting the radical this
is $`y=R(c)x`$. The surviving output index is
$`(y,B_\chi x)`$.
This is the earlier scalar-orbit transpose mechanism. The route gives a
representation bridge but does not by itself improve the prior scalar
spectral result. The full defects in (AQ.21) retain the information that
this twirl discards.

For an associative group, every $`\ell_{x,y}`$ is the identity.
Then $`\mathcal A=P=I`$ and $`\mathcal M=I`$; on a nontrivial
group the global mean-zero norm is one. The strict gap in Theorem A
is therefore an analytic consequence of nonassociativity in this specified
Bol family. It is not a universal theorem for all nonassociative loops.

There is also a useful sampling control. For every finite loop,
$`\mathbb E_z U_{L_z}=\Pi`$ already, since right division makes the
image of a fixed point under a uniform left translation uniform.
Theorem A is not an improvement over that one-step sampler. Its endpoint
is the sharp spectrum of a specified associator measure and the
multiplicativity-defect inequality (AQ.9). The latter fails for a
nontrivial group, whose defect energy is identically zero, and does not
follow from unrestricted translation averaging.

Both reciprocal actions are necessary for this particular global gap.
As controlled variants, retain $`b`$ but replace either the $`W`$ action
$`\lambda^t`$ or all the $`V`$ actions $`\eta^{a_i}`$ by the identity.
Balancedness and self-alternation still give a left Bol loop, although
the full faithful-action hypotheses of Section 1.1 no longer hold.
Every defect fixes the erased vector coordinate. A left translation acts
there by a translation, which cancels when conjugating a defect.
Consequently every function of that coordinate is fixed by $`\mathcal M`$.
A nonconstant additive character gives
$`\|\mathcal M-\Pi\|=1`$ in either variant. This identifies a necessary
input for the claimed strict gap, without excluding other estimates for
those variants.

The Bol law contributes the exact sandwich relation and inverse-pair
reversibility. The reciprocal graph contributes the explicit
modulation-dilation defect and its separated bilinear kernel. Alternation
kills the residual phases in (AQ.31) and its ring analogue. Pencil
independence supplies nonzero rank in every nontrivial auxiliary character;
the full pencil images remain visible in (AQ.29). The comparison with
an enveloping permutation group does not remove these inputs: it is the
particular loop-selected probability measure and its translated energy
that are calculated.

## 8. Literature, arithmetic scope, and remaining bridge

Permutation representations, universal multiplication groups,
universal stabilizers and Markov actions of quasigroups are established
subjects. [SMITH-QR](../REFERENCES.md#smith-qr), Sections 2.1.3--2.1.4,
3.2 and 4.2.3--4.2.4, supplies those general frameworks;
[SMITH-MARKOV](../REFERENCES.md#smith-markov) treats generalized
quasigroup Markov actions. For Bol loops from matched pairs,
[JS-ACTION](../REFERENCES.md#js-action), Theorem 6.1 and Section 7,
already studies stochastic/permutation actions. The present contribution
is the specified full-associator law, its exact spectrum and global
energy estimate, with isomorphism-natural sector transport. A claim to the
first general loop representation theory would be incorrect.

[GH-Q](../REFERENCES.md#gh-q) constructs canonical quantization and
intertwiners for symplectic vector spaces over finite fields.
[GH-SR](../REFERENCES.md#gh-sr) uses self-reducibility of the Weil
representation to control specified torus eigenstates and exponential sums.
Those results are the appropriate finite Heisenberg--Weil comparison;
their eigenstate hypotheses cannot be applied to arbitrary loop sections.
The proof here uses direct finite Fourier orthogonality and bilinear
averages. The appearance of ordinary Weyl and cotangent symplectic
operators in (AQ.20) does not claim a new metaplectic cover.

The local-cover, global-theta and arithmetic-estimate distinctions for the
quasi-RH source are recorded in
[bol-metaplectic-intake.md, Section 5](bol-metaplectic-intake.md#5-what-metaplectic-machinery-the-quasi-rh-paper-actually-uses).
Nothing in (AQ.7) constructs the cubic cover or global assembly used
there. The current theorem is an intrinsic finite-loop spectral
application, valid across every prime-power conductor with explicit
normalized measures and imprimitive sectors.

Validity at all levels is not an intertwining theorem between consecutive
levels. One may choose compatible units and extension fields, but the
actual reciprocal scalar actions and section readouts still require an
explicit correspondence. A claimed descent must give its kernel and
normalization and prove compatibility with those actions, the relevant
Gram operators and additive-character conductors. The existing
[bol-conductor-correspondence.md](bol-conductor-correspondence.md)
provides the separately audited arithmetic interface. No Euler product,
automorphy, analytic continuation, or quasi-RH consequence follows from
the present finite identities.

A materially different higher route remains open.
[BMS-2REP](../REFERENCES.md#bms-2rep), Definition 4.16 and Section 5.1,
constructs category-valued weak projective representations using gerbe
parallel transport and higher weak cocycles.
[BL-3COCYCLE](../REFERENCES.md#bl-3cocycle), Sections 3.3 and 4.2,
constructs nonassociative translation/star-product structures involving
three-cocycles. These are serious alternatives to scalar matrices, whose
collapse we proved. They do not automatically turn the loop-valued
reassociation transport (AQ.24) into a higher cocycle on an associative
translation group.

The next theory problem is therefore precise: construct a category and
action retaining the full $`J_\chi(h,g)`$, prove that its natural
transformations encode the genuine Bol relation (AQ.25), and identify an
analytic quantity controlled by the resulting higher coherence beyond
Theorem A. The next arithmetic problem is to extend the already proved
readout correspondences to an enlarged output model carrying the actual
section and full $`J_\chi(h,g)`$ actions, with an explicit kernel,
scaling, Gram identity and conductor behavior. The existing readout
correspondences solve their stated function-space problem; they are not
being relabeled as missing. Their action-equivariance obstruction remains
relevant to this stronger target. Neither new target is settled by the
scalar no-go theorem, the graph-twirl reduction, or formal pentagon
telescoping.

The proved endpoint is already stronger than merely attaching a known
analytic object: it gives exact intrinsic mixing and quantitative
multiplicativity-defect rigidity for an explicit infinite proper Bol
family. The full joint-image spectrum offers further observables, while
the worst-case global rate alone does not distinguish pencils with the
same minimal individual rank. Historical priority beyond the cited
comparisons is not asserted.

## 9. Reproducible checks and proof status

The proofs above are algebraic; experiments checked representation
interfaces and signs rather than supplying an unproved asymptotic premise.
The authored [Weyl checker](../code/verify_bol_associator_weyl.py) reuses
`verify_bol_conductor_vector.py`, itself importing
`verify_bol_collective.py`. This is a shared implementation, not an
independent implementation or independent review.

With seed `2026111609`, it checks the earlier six-dimensional cross-product
and star controls at central orders $`7`$ and $`49`$.
There are 24 sampled triples per family per level: 96 permutation cases.
Each compares direct $`L_{xy}^{-1}L_xL_y`$ using actual loop division
with (AQ.12), checks (AQ.13), and checks a genuine isomorphism to a
transformed pencil.

That isomorphism combines an $`E`$-linear diagonal change
$`P`$ on $`W`$, a cyclic permutation of the pencil parameters and
ring planes, and symplectic diagonal changes within the ring planes.
The new pencil entries are explicitly
$`P^{-\mathsf T}B_{\mathrm{permuted}\ i}P^{-1}`$.
The nucleus characters are transported consistently.

There are 480 sampled basis/character cases, including zero, primitive
and imprimitive right-nucleus characters. They check the Weyl factorization,
full correction, Bol sandwich, half-center palindrome, inverse-defect
identity, the genuine-isomorphism intertwiner and a deliberately nonlinear
section-gauge basis change. The gauge is not labeled a loop isomorphism.
All phases are exact exponents modulo $`3\cdot7^A`$; no floating-point
matrix comparison is used.

All checks passed with exit zero and empty stderr. Source and complete-output
hashes are preserved in the [review record](../evidence/bol-metaplectic-review.md).
The checker accepts the directory containing the two earlier verifiers as
its optional single argument; without it, it imports from its own directory.

The [reproduction instructions](../code/README.md#intrinsic-associator-quantization-and-mixing)
also include the authored exact bilinear/conductor checker, the independently
implemented reciprocal-defect checker, direct independent enumeration of
415065672 ring-character terms in eight selected cases, and the non-Bol
control from Section 4.3. They state the input ranges, seeds, toolchains,
dependencies and limits. These five programs check finite interfaces;
they do not enumerate a full large loop operator or replace the uniform proofs.

Theorems A and B, the group-image obstruction and the representation and
coherence identities are proved under Section 1.1. The source's independent
loop-theoretic dependency chain is not promoted into a new theorem here.
Independent review status and the reviewed source pin belong in the
repository's review record, separately from these authored checks.


