# Collective cancellation through reciprocal Bol words

Mira Cult

The full alternating pencil can improve an analytic estimate beyond every
bound determined by its individual scalar ranks. For a coupled Galois family,
the actual reciprocal Bol-word operator has a uniformly better power bound
on **all mean-zero inputs** than an admissible aligned family with the same
pointwise scalar ranks. Both norms are computed exactly in Theorem D.
Writing $`N=729^{6h}`$ and $`m_*=(7+\sqrt{21})/18<1`$, its consequence is

```math
 \|\mathcal R_{\mathrm{sp},h}f\|_2
 \leq\frac{\sqrt{14}}{9m_*}\,N^{-1/3-\delta_*}\|f\|_2,
 \qquad
 \delta_* =\frac{\log(1/m_*)}{6\log729}>0,
 \qquad \mathbb E f=0.
```

The aligned norm is asymptotic to $`(3\sqrt2/7)N^{-1/3}`$. Thus even the
entire labeled scalar-rank function cannot supply the extra exponent.
The saving comes from how the scalar images meet at a common spatial
frequency. Both reciprocal actions occur in the observable, which is the
character of a displacement between two specified Bol-word states. All
finite spaces carry normalized counting measure. The primes remain fixed
at 3 and 7; $`h`$ measures the growing vector dimension.

The proof first treats a simpler tensor family in Theorem C, with exact ratio
$`(343/721)^{h/2}`$ on inputs centered in every block. Section 6 specifies
its input restrictions and exceptional channels. Section 6A then removes
that restriction by replacing the independent blocks with a coupled pencil.
Its proof uses a sharp product-measure subspace lemma and linearized
polynomials, rather than tensorization of the earlier norm.

Finite Fourier orthogonality, weighted subspace projections and the
MacWilliams transform are established tools. The contribution is their sharp
application to this specified loop-derived family, with a comparison pencil
proving that the scalar-rank baseline is optimal with only those data. The
literature comparison is in Section 8; historical priority is not asserted.

## 1. The actual reciprocal section

Let $`p,q`$ be distinct odd primes, $`p\mid q-1`$,
$`r=\operatorname{ord}_q(p)`$, $`E=\mathbf F_{p^r}`$, and
$`W=E^n`$. Choose $`\lambda\in E`$ of order $`q`$ and
$`\eta\in\mathbf F_q`$ of order $`p`$. Let
$`B_1,\ldots,B_k`$ be alternating matrices over $`E`$, independent over
$`\mathbf F_p`$, with zero common radical. Define

```math
 \beta(x,y)=\bigl(\operatorname{Tr}_{E/\mathbf F_p}
                  (x^{\mathsf T}B_i y)\bigr)_{i=1}^k,
 \qquad V=\bigoplus_{i=1}^k\mathbf F_q^2,
```

```math
 \gamma(v,w)=\sum_i(v_{i,1}w_{i,2}-v_{i,2}w_{i,1}),
 \qquad (D_a v)_i=\eta^{a_i}v_i.
```

The loop lives on $`W\times V\times\mathbf F_p^k\times\mathbf F_q`$:

```math
 (x,v,a,t)\circ(y,w,b,s)
 =\bigl(x+\lambda^t y,\ v+D_a w,
        a+b-\beta(x,y),\ t+s-\gamma(v,w)\bigr).       \tag{1}
```

This is the law of the actual marked section in
[BOL-0025](../REFERENCES.md#bol-0025), inspected at public revision
`f54b5376cb098e52d56ba0e599598d92ff6978a3`. Its upstream
`odd-alternating-form-family.md` and `odd-class-two-classification.md`
have blobs `280882c2a46a0dff0f8a0af147ca6cf961940ff1` and
`a8d0e17af1eb9af97d629e54871c6e4bc4616e3d` at that revision.
The following calculation identifies the section without importing a
simplicity, G-loop or classification assertion.

Put $`\mathcal U=W\oplus V`$ and
$`Z=\mathbf F_p^k\oplus\mathbf F_q`$. Write
$`b=\beta\oplus\gamma`$ and
$`R(a,t)=\lambda^t\oplus D_a`$. The class-two group on
$`\mathcal U\oplus\mathcal U\oplus Z`$ has multiplication

```math
 (X,Y,z)(X',Y',z')
 =\left(X+X',Y+Y',z+z'
       +\tfrac12\{b(X,Y')+b(Y,X')\}\right).
```

Adjoin $`Z`$ acting by $`(R(c),R(-c))`$ on the two axes and trivially
on the center. Balancedness follows from
$`b(R(c)X,Y)=b(X,R(c)Y)`$. The stabilizer graph and inverted section are

```math
 H=\{(X,0,c;c):X\in\mathcal U,c\in Z\},\qquad
 K=\{(X,-R(-c)X,0;c):X\in\mathcal U,c\in Z\}.
```

Right multiplication by $`H`$ reduces $`(X,Y,z;c)`$ to the unique coordinates
$`(Y,z-c+\tfrac12b(X,Y))`$. Here and below halves are taken separately
in the two odd characteristics. The section element of coordinates
$`(Y,d)`$ is $`(-R(-d)Y,Y,0;-d)`$, because
$`b(R(c)Y,Y)=0`$. Multiplying two such elements and reducing gives

```math
 (Y,d)\circ(Y',d')=(Y+R(d)Y',\ d+d'-b(Y,Y')),
```

which is (1). It retains the full ordered pencil and both directions of the
reciprocal graph.

### Direct verification of the loop and Bol identity

For completeness, the displayed law is a proper left Bol law independently
of the source's folder theorems. In the compressed notation just used, left
division is triangular. To solve $`(U,c)\circ(Y,d)=(X,e)`$ for the left
factor, first put

```math
 c=e-d+b(X,Y),\qquad U=X-R(c)Y.
```

Indeed $`b(R(c)Y,Y)=0`$. This also proves unique right division, and
$`(0,0)`$ is the identity.

For $`A=(U,c)`$, $`B=(Y,d)`$, $`C=(Z,e)`$, the central coordinate of
$`A\circ(B\circ A)`$ is $`2c+d`$. Expanding both sides of
$`A\circ(B\circ(A\circ C))=(A\circ(B\circ A))\circ C`$ gives the
same vector coordinate

```math
 U+R(c)Y+R(c+d)U+R(2c+d)Z
```

and the same central coordinate

```math
 2c+d+e-b(U,Z)-b(Y,R(c)Z)-b(U,R(c+d)Z).
```

The identities used are precisely balancedness and
$`b(U,R(d)U)=0`$, both true for the specified block scalar actions.

The loop is non-Moufang: choose $`e\ne0`$ in $`W`$ and $`v,w`$ in one
$`q`$-plane with $`\gamma(v,w)=1`$. For
$`A=(e,v,0,0)`$, $`B=(0,w,0,0)`$, the $`W`$-coordinates of
$`(A\circ B)\circ A`$ and $`A\circ(B\circ A)`$ are respectively
$`(1+\lambda^{-1})e`$ and $`2e`$. They differ, violating flexibility.
No simplicity claim is needed or made for the analytic theorem.

## 2. A shared-input observable using both reciprocal actions

For the rest of the note fix

```math
 p=3,\quad q=7,\quad E=\mathbf F_{729},\quad Q=729,
 \quad\eta=2,\quad\lambda^7=1,\quad\lambda\ne1.
```

Since 3 has order 6 modulo 7, $`\Phi_7`$ is irreducible over
$`\mathbf F_3`$, and $`1,\lambda,\ldots,\lambda^5`$ is a basis of $`E`$.
Write $`e_m(t)=\exp(2\pi it/m)`$ on $`\mathbf F_m`$ for $`m=3,7`$.

Set $`U=(u,0,0,0)`$, $`Y=(y,0,0,0)`$. In each $`q`$-plane choose
$`w_i=(1,0)`$, $`v_i^*=(0,1)`$, and put

```math
 W_a=(0,D_aw,0,0),\quad Z_s=(0,v^*,0,s),\quad X_e=(e,0,0,0).
```

Here $`e\in W`$ is fixed and an $`E`$-linear functional $`L`$ on $`W`$
is fixed with $`L(e)=1`$. Let $`A=(U\circ Y)\circ W_a`$. Direct use
of (1) gives

```math
 A=(u+y,D_{a-\beta(u,y)}w,-\beta(u,y),0),
```

```math
 A\circ Z_s=
 \left(u+y,
 D_{a-\beta(u,y)}w+D_{-\beta(u,y)}v^*,
 -\beta(u,y),\ s-F_B(u,a,y)\right),
 \quad
 F_B(u,a,y)=\sum_{i=1}^k2^{a_i-\beta_i(u,y)}\in\mathbf F_7.
```

The difference between the $`W`$-coordinates of
$`(A\circ Z_s)\circ X_e`$ and $`A\circ Z_s`$ is
$`\lambda^{s-F_B(u,a,y)}e`$. Observe its additive character
$`e_3(\operatorname{Tr}L(\text{difference}))`$. Thus this is a product
of the character at the final state and the conjugate character at the
preceding state. Using the final coordinate alone would give a different
operator with an extra $`u+y`$ contribution.

Define

```math
 \vartheta(t)=e_3(\operatorname{Tr}_{E/\mathbf F_3}\lambda^t),
 \qquad
 (\mathcal R_Bf)(u,a,s)
  =\mathbb E_{y\in W}f(y)\vartheta(s-F_B(u,a,y)).       \tag{2}
```

This maps $`L^2(W)`$ to
$`L^2(W\times\mathbf F_3^k\times\mathbf F_7)`$.
There is a **single input function** shared by all character sectors.
We first analyze the simpler one-way readout

```math
 h(a)=e_7\!\left(\sum_i2^{a_i}\right),\qquad
 (T_Bf)(u,a)=\mathbb E_y f(y)h(a-\beta(u,y)).           \tag{3}
```

It is the additive character of the $`q`$-vector of $`A`$.
The relation to the full two-way observable is exact, not an estimate.

**Lemma R (two-way Gram identity).** With $`\Pi f=\mathbb E f`$,

```math
 \mathcal R_B^*\mathcal R_B
   =\frac{31}{49}\Pi+\frac{18}{49}T_B^*T_B.           \tag{4}
```

**Proof.** The six nonzero powers of $`\lambda`$ are its Frobenius
conjugates, so their traces are all $`-1`$ in $`\mathbf F_3`$; the
trace of 1 is zero. Writing $`\omega=e_3(1)`$ gives
$`\vartheta(0)=1`$ and $`\vartheta(t)=\omega^{-1}`$ for $`t\ne0`$.
Its normalized Fourier weights on $`\mathbf F_7`$ are

```math
 |\widehat\vartheta(0)|^2=31/49,\qquad
 |\widehat\vartheta(\rho)|^2=3/49\quad(\rho\ne0).
```

Parseval in $`s`$ separates these terms. The zero frequency is the
constant-input projection. For a nonzero frequency the inner phase is
$`e_7(c\sum_i2^{a_i-\beta_i})`$ for a common $`c\in\mathbf F_7^\times`$.
If $`c\in\{1,2,4\}`$, shifting each $`a_i`$ preserves the Fourier
weights of $`h`$. If $`c\in-\{1,2,4\}`$, conjugation additionally
sends every label $`\nu`$ to $`-\nu`$. The Gram formula below is
unchanged, since $`B_{-\nu}=-B_\nu`$ has the same kernel.
All six nonzero $`\rho`$ terms therefore have Gram $`T_B^*T_B`$,
proving (4). The factor $`18/49`$ occurs once overall: there is one
shared $`q`$-central coordinate, even when the pencil has many blocks. ∎

## 3. The exact Gram kernel and all rank strata

Let

```math
 \widehat h(\nu)=\mathbb E_a h(a)e_3(-\nu\cdot a),\quad
 w(\nu)=|\widehat h(\nu)|^2,\quad
 B_\nu=\sum_i\nu_iB_i,\quad r_\nu=\operatorname{rank}_E B_\nu.
```

Parseval gives $`\sum_\nu w(\nu)=1`$. The trace form
$`(x,y)\mapsto\nu\cdot\beta(x,y)`$ has radical exactly
$`\ker_E B_\nu`$: if $`B_\nu y\ne0`$, nondegeneracy of the field trace
supplies an $`x`$ with nonzero pairing. Thus its $`\mathbf F_3`$-rank is
$`6r_\nu`$, including all degenerate specializations.

**Lemma G (joint-image identity).** The normalized convolution kernel of
$`T_B^*T_B`$ is

```math
 K_B(z)=\sum_\nu w(\nu)\mathbf1_{\{B_\nu z=0\}}.    \tag{5}
```

In the orthonormal Fourier basis
$`\chi_\xi(y)=e_3(\operatorname{Tr}(\xi^{\mathsf T}y))`$, its multiplier is

```math
 M_B(\xi)=\sum_\nu w(\nu)Q^{-r_\nu}
                   \mathbf1_{\{\xi\in\operatorname{im}_E B_\nu\}}.
                                                               \tag{6}
```

Consequently, on inputs with Fourier support $`\mathcal X\subseteq W`$,
the squared norm is exactly $`\max_{\xi\in\mathcal X}M_B(\xi)`$.

**Proof.** In the adjoint product, averaging over $`a`$ kills unequal
central Fourier labels. Averaging the remaining character over $`u`$
is one if $`B_\nu(y-z)=0`$ and zero otherwise. This proves (5).
The normalized Fourier transform of a subspace indicator is its density
times the indicator of its annihilator. Here the density is $`Q^{-r_\nu}`$
and the trace annihilator of $`\ker_E B_\nu`$ is
$`\operatorname{im}_E B_\nu`$, since the matrix is alternating. This
proves (6). A maximizing Fourier character proves sharpness. ∎

The zero character has $`B_0=0`$ and contributes only at $`\xi=0`$.
No estimate treats zero common radical as nondegeneracy of every scalar
specialization. Formula (6) records the whole rank stratification and the
joint intersections of scalar images. Dually, the higher intersections of
the kernels are retained in (5), rather than inferred from individual ranks.

The separate-sector estimate discards the image condition. In particular,
if every nonzero $`B_\nu`$ has rank $`r_0`$, then on mean-zero inputs

```math
 \|T_Bf\|_2^2\leq Q^{-r_0}(1-w(0))\|f\|_2^2.        \tag{7}
```

This is the applicable scalar baseline, not the sharp joint-incidence bound.
Below a comparison pencil attains (7), while another pencil with identical
labeled ranks has a strictly smaller exact norm.

## 4. Reciprocal weights and their subspace masses

For one center coordinate the Fourier weights are

```math
 w_0=\frac29,\qquad
 \{w_1,w_2\}=\left\{\frac{7-\sqrt{21}}{18},
                         \frac{7+\sqrt{21}}{18}\right\}.          \tag{8}
```

Their order depends on the Fourier sign convention and is immaterial to
the subspace masses below. Here is an exact derivation. If $`\zeta=e_7(1)`$
and $`S=\zeta+\zeta^2+\zeta^4`$, the six differences of distinct
nonzero quadratic residues run through $`\mathbf F_7^\times`$. Hence
$`|S|^2=2`$, $`S+\overline S=-1`$, and
$`S=(-1\pm i\sqrt7)/2`$. The autocorrelation

```math
 R(b)=\mathbb E_{a\in\mathbf F_3}
       e_7(2^a)\overline{e_7(2^{a+b})}
     =\mathbb E_a e_7(2^a(1-2^b))
```

has $`R(0)=1`$ and $`\{R(1),R(2)\}=\{z,\bar z\}`$ with
$`z=(-1+i\sqrt7)/6`$. Fourier inversion gives (8).
With our convention, explicitly $`R(b)=\sum_jw_j e_3(-jb)`$;
the opposite sign conjugates $`R`$ and leaves all subspace masses unchanged.

For a three-coordinate block put $`w(\nu)=\prod_{i=1}^3w_{\nu_i}`$.
Then $`w(0)=8/729`$. If $`c\ne0`$ in $`\mathbf F_3^3`$, character
orthogonality gives

```math
 \sum_{\nu\in c^\perp}w(\nu)
   =\frac13\left(1+2\operatorname{Re}\prod_iR(c_i)\right).        \tag{9}
```

The following table exhausts all 13 projective directions.

| Pattern of the nonzero coordinates of c | Directions | Mass in c-perp after removing zero |
| --- | ---: | ---: |
| One nonzero coordinate | 3 | 154/729 |
| Two coordinates with equal signs | 3 | 154/729 |
| Two coordinates with opposite signs | 3 | 343/729 |
| Three coordinates with equal signs | 1 | 280/729 |
| Three coordinates with mixed signs | 3 | 217/729 |

Indeed

```math
 \operatorname{Re}z=\operatorname{Re}z^2=-1/6,\quad |z|^2=2/9,
 \quad\operatorname{Re}z^3=5/54,
 \quad\operatorname{Re}(z^2\bar z)=-1/27.
```

Thus the largest nonzero mass in a proper subspace is $`343/729`$;
smaller subspaces are contained in hyperplanes and the weights are positive.
For completeness the masses of a line's two nonzero vectors, for the same
five patterns, are respectively

```math
 28/729,\quad70/729,\quad28/729,\quad196/729,\quad49/729.            \tag{10}
```

In general a constraint subspace $`C\leq\mathbf F_3^k`$ satisfies
$`w(C^\perp)=|C|^{-1}\sum_{c\in C}\prod_iR(c_i)`$.
This is the complete-symbol MacWilliams transform
([MACWILLIAMS, Lemma 2.7](../REFERENCES.md#macwilliams)), not a new
summation principle. Retaining its complex signs rather than bounding
each nonzero factor by its modulus is what gives the exact table.

## 5. Two pencils with the same pointwise scalar ranks

For $`\nu=(\nu_1,\nu_2,\nu_3)\in\mathbf F_3^3`$, define

```math
 C_\nu=\begin{pmatrix}
 0&-\nu_3&\nu_2\\
 \nu_3&0&-\nu_1\\
 -\nu_2&\nu_1&0
 \end{pmatrix},\qquad
 S_\nu=\begin{pmatrix}0&\nu^{\mathsf T}\\-\nu&0_3\end{pmatrix},
 \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
```

```math
 B_\nu^{\mathrm G}=\operatorname{diag}(C_\nu,C_\nu),\qquad
 B_\nu^{\mathrm A}=\operatorname{diag}(S_\nu,\ell(\nu)J),\qquad
 \ell(\nu)=\nu_1+\lambda\nu_2+\lambda^2\nu_3.                    \tag{11}
```

The superscripts denote the transverse-image and aligned-image examples;
they name marked pencils, not asserted loop isomorphism classes.

For $`\nu\ne0`$, $`C_\nu`$ has kernel $`E\nu`$, image $`\nu^\perp`$
and rank two. This remains true when $`\nu`$ is isotropic: a nonzero
coordinate supplies a nonzero two-by-two minor. The star matrix has

```math
 \ker S_\nu=\{0\}\oplus\nu^\perp,\qquad
 \operatorname{im}S_\nu=Ee_0\oplus E(0,\nu).
```

The independence of $`1,\lambda,\lambda^2`$ over $`\mathbf F_3`$
ensures $`\ell(\nu)\ne0`$ whenever $`\nu\ne0`$. Both pencils therefore
have rank four at every nonzero $`\nu`$. Each triple is independent,
and its common radical is zero: intersect the three coordinate radical
lines for $`C`$, or the three coordinate hyperplanes for $`S`$; the
last $`J`$-plane of the aligned pencil is already nonsingular.
These verify all the displayed construction's input hypotheses.

For the first pencil, writing $`\xi=(\xi^{(1)},\xi^{(2)})\in E^3\oplus E^3`$,

```math
 \xi\in\operatorname{im}B_\nu^{\mathrm G}
 \quad\Longleftrightarrow\quad
 \nu\cdot\xi^{(1)}=\nu\cdot\xi^{(2)}=0 \qquad(\nu\ne0).         \tag{12}
```

Expand these two vectors in an $`\mathbf F_3`$-basis of $`E`$ and let
$`C_\xi\leq\mathbf F_3^3`$ be the span of their coefficient rows.
For $`\xi\ne0`$, its dimension is at least one. Equations (6), (9)
therefore give

```math
 \|T_{\mathrm G}|_{L^2_0(E^6)}\|^2
       =\frac{343}{729Q^4}.                                      \tag{13}
```

Equality occurs at $`\xi^{(1)}=(0,1,-1)`$, $`\xi^{(2)}=0`$.
For the aligned pencil, every nonzero image contains $`Ee_0`$ in its
first four coordinates, so a nonzero frequency there gives

```math
 \|T_{\mathrm A}|_{L^2_0(E^6)}\|^2
       =\frac{721}{729Q^4}.                                      \tag{14}
```

This attains the separate-sector estimate (7). In particular the entire
pointwise scalar-rank function and the actual sector weights are
insufficient to imply (13).

### Theorem C: uniform collective cancellation

For each integer $`h\geq1`$, take the block diagonal direct sum of $`h`$
copies of either pencil (11), with $`n=6h`$ and $`k=3h`$. Apply (1)--(2)
with the same $`p,q,\lambda,\eta`$ and let

```math
 \mathcal H_h=\bigotimes_{j=1}^hL^2_0(E^6)
              \subseteq L^2((E^6)^h).
```

Equivalently, averaging $`f`$ in any one block, holding the others fixed,
gives zero. This includes arbitrarily correlated functions in that subspace,
not only products. Then

```math
 \left\|\mathcal R_{\mathrm G}^{(h)}|_{\mathcal H_h}\right\|
   =\frac{3\sqrt2}{7}
        \left(\frac{7\sqrt7}{27Q^2}\right)^h,
 \qquad
 \left\|\mathcal R_{\mathrm A}^{(h)}|_{\mathcal H_h}\right\|
   =\frac{3\sqrt2}{7}
        \left(\frac{\sqrt{721}}{27Q^2}\right)^h.                   \tag{15}
```

Both are exact norms, and their ratio is $`(343/721)^{h/2}`$.
The loops have order $`3^{39h}7^{6h+1}`$ and are directly verified proper
left Bol loops. For every $`\nu\in\mathbf F_3^{3h}`$ both pencils have

```math
 \operatorname{rank}_E B_\nu
       =4\,\#\{j:\nu^{(j)}\ne0\}.                               \tag{16}
```

Thus all exceptional character strata, not just the minimum rank, agree.

**Proof.** Direct sums preserve independence and zero common radical.
The law and properness were proved in Section 1. Formula (16) is block
additivity of rank. The one-way kernel (3) is a tensor product across the
blocks, with product sector weights and product Fourier multipliers.
The support of $`\mathcal H_h`$ consists exactly of Fourier vectors with
every block nonzero. Applying (13)--(14) in each block gives the tensor
norms. The maximizing frequencies displayed above in every block attain
them. Finally (4) multiplies the squared norms by $`18/49`$, since this
input space is globally centered. ∎

If $`N=|W|=Q^{6h}`$, the improvement over the sharp scalar-rank baseline is
$`N^{-\delta}`$, where

```math
 \delta=\frac{\log(721/343)}{12\log729}>0.                         \tag{17}
```

There is no hidden factor growing with dimension. This statement improves
the estimate for a fixed marked observable; it does not optimize over
all choices of section weights or claim a bound below every square-root
benchmark for arbitrary exponential sums.

## 6. Input strata and a counting consequence

Write

```math
 A_0=\frac{8+721Q^{-4}}{729},\qquad
 g_{\mathrm G}=\frac{7\sqrt7}{27Q^2},\qquad
 g_{\mathrm A}=\frac{\sqrt{721}}{27Q^2}.
```

The zero spatial frequency in one block has multiplier $`A_0`$ for
both pencils. Let $`\mathcal H_{h,\geq d}`$ consist of functions whose
Fourier support has at least $`d`$ nonzero blocks, $`1\leq d\leq h`$.
The same proof gives the sharp refinement

```math
 \|\mathcal R_{B}^{(h)}|_{\mathcal H_{h,\geq d}}\|
   =\frac{3\sqrt2}{7}A_0^{(h-d)/2}g_B^d,
 \qquad B\in\{\mathrm G,\mathrm A\}.                            \tag{18}
```

Indeed $`g_B^2<A_0`$, so the largest multiplier has exactly $`d`$
nonzero blocks. For ordinary global mean zero ($`d=1`$), the ratio is
only $`\sqrt{343/721}`$. Exponential improvement is obtained when
$`d`$ grows proportionally with $`h`$. The constant channel has the
additional $`31/49`$ term in (4) and is excluded from (18).

The theorem also bounds an explicit counting problem. Define

```math
 (I_Bf)(u,a,s)=\mathbb E_y f(y)
       \mathbf1_{\{\sum_i2^{a_i-\beta_i(u,y)}=s\}}.               \tag{19}
```

For every globally centered $`f`$, the two-valued formula for
$`\vartheta`$ gives $`\mathcal R_Bf=(1-\omega^{-1})I_Bf`$. Thus

```math
 \|I_{\mathrm G}^{(h)}f\|_2
 \leq\frac{\sqrt6}{7}
       \left(\frac{7\sqrt7}{27Q^2}\right)^h\|f\|_2,
 \qquad f\in\mathcal H_h,                                      \tag{20}
```

with sharp constant. The aligned bound replaces $`7\sqrt7`$ by
$`\sqrt{721}`$. More generally use (18) divided by $`\sqrt3`$.

For example, for arbitrary subsets $`A_j\subseteq E^6`$ of densities
$`\alpha_j`$, take
$`f(y)=\prod_j(\mathbf1_{A_j}(y_j)-\alpha_j)`$.
For every test function $`G(u,a,s)`$, Cauchy--Schwarz and (20) give

```math
 \left|\mathbb E_{u,a,s,y} f(y)\overline{G(u,a,s)}
       \mathbf1_{\{F_{\mathrm G}(u,a,y)=s\}}\right|
 \leq \frac{\sqrt6}{7}
       \left(\frac{7\sqrt7}{27Q^2}\right)^h
       \|G\|_2\prod_j\sqrt{\alpha_j(1-\alpha_j)}.                \tag{21}
```

This controls a multilinear discrepancy for a concrete family of equations
over $`\mathbf F_7`$ whose exponents are the whole trace-valued pencil.
The estimate is averaged in $`u,a,s`$; no pointwise bound at every output
or cancellation for arbitrary uncentered input is asserted.

## 6A. Coupled pencils and an exact norm on all mean-zero inputs

The block restriction in Theorem C can be removed by changing the pencil.
Keep the base field $`E=\mathbf F_{729}`$ and the reciprocal readout (2).
For each integer $`h\geq1`$, put

```math
 k=2h+1,\qquad L_h=\mathbf F_{729^h},\qquad
 M_h=\mathbf F_{729^{2h-1}},\qquad n=6h.
```

Choose $`\mathbf F_3`$-linear injections
$`j_h:\mathbf F_3^k\to L_h`$ and
$`i_h:\mathbf F_3^k\to M_h`$. These exist because
$`k\leq6h`$ and $`k\leq6(2h-1)`$, including $`h=1`$.
The estimates and equalities below hold for **every** such pair of injections.
For a completely specified family, represent each extension by the first
monic irreducible polynomial in a fixed lexicographic ordering over the
concrete base field $`E=\mathbf F_3[\lambda]/\Phi_7`$, and take the first
$`k`$ vectors of the resulting ordered $`\mathbf F_3`$-basis. This is a
finite uniform construction, with no unproved prime-distribution premise.

For $`t=j_h(\nu)`$, put $`z(t)=(t,t^3,t^9)`$ and define the alternating
$`E`$-bilinear form on $`L_h^3`$

```math
 c_t(x,y)=\operatorname{Tr}_{L_h/E}\det[z(t),x,y].                 \tag{22}
```

The spread pencil is $`c_t\oplus c_t`$ on $`W=L_h^6`$, viewed as an
$`E`$-space of dimension $`6h`$. Its matrices $`B_\nu^{\mathrm{sp}}`$
are taken in a fixed $`E`$-basis. The map $`\nu\mapsto B_\nu`$ is
$`\mathbf F_3`$-linear; parameter linearity over $`E`$ is not required.

For the comparison pencil, use the star matrix $`S_\nu`$ of size
$`k+1`$, with first row $`(0,\nu_1,\ldots,\nu_k)`$. Adjoin the
alternating form on $`M_h^2`$

```math
 d_\nu((x,y),(x',y'))
  =\operatorname{Tr}_{M_h/E}
       \bigl(i_h(\nu)(xy'-yx')\bigr).                            \tag{23}
```

The aligned pencil $`B_\nu^{\mathrm{al}}=S_\nu\oplus d_\nu`$ has
dimension $`(k+1)+2(2h-1)=6h`$ over $`E`$.

### Admissibility, ranks, and the shared-frequency constraint

For $`t\ne0`$, the radical of (22) is exactly $`L_hz(t)`$. Indeed,
if $`x\notin L_hz(t)`$, the determinant as a function of $`y`$ is
onto $`L_h`$, and the trace is not the zero map. Thus $`c_t`$ has
$`E`$-rank $`2h`$, and the spread pencil has rank $`4h`$. Distinct
nonzero parameters have the same radical line only if
$`z(s)=a z(t)`$, which forces $`s/t=(s/t)^3`$ and hence
$`s/t\in\mathbf F_3^\times`$. Since $`j_h(\mathbf F_3^k)`$ has
dimension at least three over $`\mathbf F_3`$, the common radical is zero.

For $`\nu\ne0`$, the star block has rank two, and (23) is nondegenerate
of rank $`4h-2`$ by nondegeneracy of the trace pairing. The star blocks
have zero common radical, and every nonzero trace-symplectic block is
already nonsingular. Both families therefore satisfy every matrix input
hypothesis of Section 1, and have the identical complete rank profile

```math
 \operatorname{rank}_E B_0=0,\qquad
 \operatorname{rank}_E B_\nu=4h\quad(\nu\ne0).                    \tag{24}
```

In particular the tuples are independent over $`\mathbf F_3`$. Independence
over $`E`$ is neither asserted nor needed. The corresponding loop orders
are $`3^{38h+1}7^{4h+3}`$.

Identify the spatial Fourier covectors of the spread family with
$`\xi=(\xi^{(1)},\xi^{(2)})\in L_h^3\oplus L_h^3`$ via the perfect
pairing $`\operatorname{Tr}_{L_h/\mathbf F_3}(\xi\cdot y)`$.
The image/annihilator condition in (6), for $`\nu\ne0`$, is exactly

```math
 \xi^{(j)}_1t+\xi^{(j)}_2t^3+\xi^{(j)}_3t^9=0,
 \qquad j=1,2,\quad t=j_h(\nu).                                  \tag{25}
```

It is an equation in $`L_h`$, because the covector must annihilate the
whole radical line $`L_hz(t)`$, not just its distinguished generator.
For $`\xi\ne0`$ at least one polynomial in (25) is nonzero and has
degree at most nine. Thus the common parameter space $`D_\xi`$ in
$`\mathbf F_3^k`$ has at most nine elements and dimension at most two.
At $`\nu=0`$, (25) is vacuous but the scalar image is only $`\{0\}`$;
the zero parameter must be removed for every nonzero spatial frequency.

The trace pairing remains nondegenerate when 3 divides either extension
degree. The spatial Fourier identification just used is distinct from the
word readout: in (2) keep an $`E`$-linear functional with value 1 at $`e`$.
Replacing it by a bare extension trace at $`e=1`$ would wrongly kill
the readout when $`3\mid h`$.

### Lemma M: the exact largest product mass of a linear subspace

Let $`w`$ be a probability distribution on a finite field $`F`$, used
identically in all $`k`$ coordinates, and put $`P_j=\sum_{a\in F}w(a)^j`$.
For $`1\leq d<k`$,

```math
 \max_{\substack{D\leq F^k\\\dim D=d}}
       \sum_{x\in D}\prod_{i=1}^kw(x_i)
   =\max\{w(0)^{k-d},P_{k-d+1}\}.                               \tag{26}
```

**Proof.** Choose $`d`$ coordinate projections giving an isomorphism
$`D\to F^d`$ and express the remaining coordinates as linear forms
$`\ell_1,\ldots,\ell_r`$, $`r=k-d`$. The mass is
$`\mathbb E\prod_{j=1}^r w(\ell_j(Z))`$, where the coordinates of
$`Z\in F^d`$ are independent with law $`w`$. Hölder gives the bound

```math
 \mathbb E\prod_{j=1}^r w(\ell_j(Z))
   \leq\prod_{j=1}^r
       \bigl(\mathbb E w(\ell_j(Z))^r\bigr)^{1/r}.
```

If $`\ell_j\ne0`$, condition on all but a variable with nonzero
coefficient. Its law is a convex combination of affine permutations of
$`w`$. The rearrangement inequality therefore gives
$`\mathbb E w(\ell_j(Z))^r\leq\sum_a w(a)^{r+1}=P_{r+1}`$.
If $`\ell_j=0`$, this expectation is $`w(0)^r`$. Their geometric mean
is at most $`\max\{w(0)^r,P_{r+1}\}`$, proving the upper bound. Taking all
$`\ell_j=0`$ attains the first alternative; taking every
$`\ell_j(Z)=Z_1`$ attains the second. ∎

For our reciprocal weights (8), put

```math
 a_* = 2/9,\qquad b_*=(7-\sqrt{21})/18,\qquad
 m_*=(7+\sqrt{21})/18,\qquad
 P_j=a_*^j+b_*^j+m_*^j.
```

Here $`P_2=13/27>a_*`$. Jensen gives
$`P_{r+1}\geq P_2^r>a_*^r`$ for every integer $`r\geq1`$.
Consequently the largest mass of a two-dimensional subspace of
$`\mathbf F_3^{2h+1}`$ is exactly $`P_{2h}`$, attained at
$`D=\{(s,\ldots,s,t):s,t\in\mathbf F_3\}`$.
Subspaces of dimension less than two have no larger mass, by extension
to a two-dimensional subspace and positivity of the weights.

Every such parameter two-plane can actually occur as $`D_\xi`$ in (25).
To see this, let its image under $`j_h`$ be
$`\langle a,b\rangle_{\mathbf F_3}`$, with $`a,b`$ independent.
Put $`P_a(X)=X^3-a^2X`$ and $`u=P_a(b)\ne0`$. The polynomial

```math
 P_D(X)=P_a(X)^3-u^2P_a(X)
       =X^9-(a^6+u^2)X^3+u^2a^2X                                \tag{27}
```

vanishes exactly on $`\langle a,b\rangle_{\mathbf F_3}`$:
$`P_a`$ is linear over $`\mathbf F_3`$, has kernel
$`\mathbf F_3a`$, and the inverse image of $`\mathbf F_3u`$ is
that nine-element plane. Equivalently, containment and the degree-nine
root bound prove equality. Taking
$`\xi^{(1)}=(u^2a^2,-a^6-u^2,1)`$ and $`\xi^{(2)}=0`$
realizes the desired constraint, at a nonzero frequency.

### Theorem D: exact coupled norm and a uniform extra exponent

For all $`h\geq1`$, all the choices of injections above, and the actual
two-way operator (2),

```math
 \|\mathcal R_{\mathrm{sp},h}|_{L^2_0(W)}\|^2
   =\frac{18}{49}\,Q^{-4h}
       \bigl(a_*^{2h}+b_*^{2h}+m_*^{2h}-a_*^{2h+1}\bigr),
```

```math
 \|\mathcal R_{\mathrm{al},h}|_{L^2_0(W)}\|^2
   =\frac{18}{49}\,Q^{-4h}(1-a_*^{2h+1}).                        \tag{28}
```

Their exact norm ratio is therefore

```math
 \sqrt{\frac{(1-a_*)a_*^{2h}+b_*^{2h}+m_*^{2h}}
                  {1-a_*^{2h+1}}}
 \leq\sqrt{\frac{343}{721}}\,m_*^{h-1},
 \qquad
 \frac{\|\mathcal R_{\mathrm{sp},h}\|}{\|\mathcal R_{\mathrm{al},h}\|}
       \sim m_*^h\quad(h\to\infty).                             \tag{29}
```

Both families have the same pointwise scalar ranks (24). In the aligned
family, the exact value is the sharp separate-sector baseline. The gain
for the spread family holds on the **whole mean-zero input space**.

**Proof.** For a nonzero frequency, (6), (24) and (25) give the one-way
multiplier $`Q^{-4h}(w(D_\xi)-a_*^{2h+1})`$. Lemma M bounds the
subspace mass by $`P_{2h}`$, and (27) realizes a plane attaining it.
The zero scalar sector is precisely the subtracted atom. The aligned
star image contains its first coordinate direction for every nonzero
parameter. A nonzero covector in that common image attains
$`Q^{-4h}(1-a_*^{2h+1})`$. Lemma R multiplies both squared norms by
$`18/49`$ on mean-zero inputs.

For (29), let $`F_h=(1-a_*)a_*^{2h}+b_*^{2h}+m_*^{2h}`$.
Since $`a_*,b_*<m_*`$, $`F_h\leq m_*^{2h-2}F_1`$,
$`F_1=343/729`$, and $`1-a_*^{2h+1}\geq721/729`$.
The asymptotic follows by dividing numerator by $`m_*^{2h}`$. ∎

In terms of $`N=|W|=Q^{6h}`$, (28) implies

```math
 \|\mathcal R_{\mathrm{sp},h}f\|_2
 \leq C_*N^{-1/3-\delta_*}\|f\|_2,
 \quad C_* =\frac{\sqrt{14}}{9m_*},\quad
 \delta_* =\frac{\log(1/m_*)}{6\log Q}>0,
 \quad \mathbb E f=0.                                           \tag{30}
```

The aligned norm is asymptotic to $`(3\sqrt2/7)N^{-1/3}`$.
All constants are absolute, and the scalar-rank baseline cannot gain the
extra exponent because the aligned family has exactly the same data.
Unnormalized sums over $`y`$ have the corresponding root-mean-square
bound $`C_*N^{2/3-\delta_*}\|f\|_2`$.

For the counting operator (19), its exact norm is (28) divided by three
at the squared-norm level. In particular (30) holds with
$`C_*/\sqrt3`$ in place of $`C_*`$. For arbitrary subsets
$`A\subseteq W`$ and $`B\subseteq W\times\mathbf F_3^k\times\mathbf F_7`$
of densities $`\alpha,\sigma`$, respectively,

```math
 \left|\mathbb E_{y,u,a,s}
       (\mathbf1_A(y)-\alpha)(\mathbf1_B(u,a,s)-\sigma)
       \mathbf1_{\{F_{\mathrm{sp}}(u,a,y)=s\}}\right|
 \leq\frac{C_*}{\sqrt3}N^{-1/3-\delta_*}
       \sqrt{\alpha(1-\alpha)\sigma(1-\sigma)}.                  \tag{31}
```

This follows from (19), Cauchy--Schwarz and the norms of the two centered
indicators. It compares the incidence count with the input-density share
of the same output set's total incidences; output degrees are not assumed
uniform. No product structure of either subset is required.

## 7. Obstructions and controlled comparisons

### Why a fixed average of left translations cannot do this

Every left translation in (1) commutes with translation in the state
coordinates $`(a,t)`$. A fixed scalar-weight average is therefore block
diagonal in their characters. Its operator norm is the largest sector
norm; different sector inputs can be chosen independently. This prevents
that architecture from exploiting the shared-frequency intersections in
(6). The common-input compression (3) changes the architecture, rather
than assuming that an orthogonal direct sum has collective cancellation.

### Why uniform right-axis walks lose the reciprocal actions

Right translations by pure vectors are

```math
 (x,v,a,t)\mapsto(x+\lambda^t u,v,a-\beta(x,u),t),
 \qquad
 (x,v,a,t)\mapsto(x,v+D_aw,a,t-\gamma(v,w)).
```

Let $`P,Q`$ average these separately and uniformly. Starting at the
identity, every word in $`P,Q`$ has the same distribution as after
deleting the two scalar actions. To prove this, suppose the density is
$`f(x,a)g(v,t)`$, with $`f`$ invariant under $`x\mapsto\lambda^b x`$
and $`g`$ invariant under $`v\mapsto D_c v`$. A $`P`$ step gives

```math
 f_t'(x',a')=\mathbb E_x
       f(x,a'+\beta(x,\lambda^{-t}x'))
       =\mathbb E_zf(z,a'+\beta(z,x')),
```

on substituting $`x=\lambda^t z`$. It is independent of $`t`$ and
retains the scalar invariance, by changing $`z`$ again. A $`Q`$ step
has the identical proof with $`v=D_aw`$ and $`\gamma`$. The identity
point mass satisfies both invariances and the factorization, so induction
proves the assertion for every finite word. This is an obstruction to
these uniform walks, not to all right-translation observables.

### What is supplied by the Bol data

Rebracketing the first three factors as $`U\circ(Y\circ W_a)`$ changes
the $`q`$-vector to $`D_aw`$. The later displacement is then
$`\lambda^{s-\sum_i2^{a_i}}e`$, independent of $`y`$, so (2) vanishes
on centered inputs. Deleting the $`p`$-center action on the $`q`$-planes
has the same effect. Deleting the $`q`$-center action on $`W`$ makes
the last displacement constant, also killing the centered observable.
The word therefore uses both directions of the actual reciprocal graph.

The joint-image bound is nevertheless an ordinary Fourier/incidence
calculation once the kernel has been selected. The same numeric kernel
can be defined without any loop, and the parenthesized section word can
be realized using the associative enveloping group and its coset action.
The loop supplies the marked family, the readout and the rebracketing
comparison; it does not supply a new multiplicative representation of a
nonassociative algebra. We do not claim that the two pencils must define
nonisomorphic unmarked loops, nor that the rank-profile distinction itself
is a new principle of linear algebra.

## 8. Comparison with the applicable literature

The strongest applicable general estimate is the weighted-projection
Gram bound, rather than a separate Weil bound. In the Fourier basis,
(6) is a sum of commuting coordinate projections with weights
$`w(\nu)Q^{-r_\nu}`$. Its sharp upper bound is the maximal weighted
image incidence. This fits [Casazza--Kutyniok, Definition 3.15 and
Proposition 3.16](../REFERENCES.md#subspace-frames); if there is a kernel,
the family is a Bessel family on the whole space and a frame on its range.
Our proof computes that incidence exactly for (11). It improves the
rank-only relaxation (7), whose sharpness across the comparison family is
proved by (14); it does not improve the abstract exact Gram principle.

[MacWilliams, Lemma 2.7](../REFERENCES.md#macwilliams) already supplies
the complete-symbol duality used in (9). [Gow--Quinlan, Theorem 10 and
the subsequent radical-line discussion](../REFERENCES.md#gow-quinlan)
also explain why an unweighted constant-rank pencil gives a familiar
projective-incidence calculation. That preliminary candidate alone was
insufficient. [Gorla--Jurrius--López--Ravagnani, Section 4](../REFERENCES.md#rank-support)
give a general setting for matrix-support data beyond individual ranks.
The present statistic additionally retains the specified reciprocal weights
and their coordinate labels.

The coupled construction uses the familiar degree bound for a linearized
polynomial and the associated Moore/Gabidulin evaluation geometry. See
[Sheekey, Section 2](../REFERENCES.md#linearized-polynomials), especially
the root-count paragraph before Theorem 2 and Remark 2. Galois-trace
alternating constructions are also established; see
[Gow--Quinlan 2007, Section 2](../REFERENCES.md#galois-alternating).
Theorem D does not claim a new rank-metric code construction. Lemma M
is proved directly using Hölder and rearrangement, and computes the exact
weighted-incidence constant needed here. The application combines
this evaluation with the actual two-way Bol word, a matching aligned
baseline, and the all-mean-zero counting bound.

[Friedlander--Shparlinski](../REFERENCES.md#double-exponential), Theorem
on page 1618, estimate scalar sums with phases $`e_P(c\eta^{xy})`$
over subsets of the exponent ring as the prime and subset sizes vary.
That is relevant nearby compound-exponential literature; it does not
evaluate the common-input vector-pencil norm with the retained shifts
used here. The primes in Theorem C are fixed, and its asymptotic parameter
and averaging set are explicitly different.

The earlier [Heisenberg/Weil and quasi-RH audit](bol-metaplectic-intake.md)
continues to apply. Gurevich--Hadani's quantization and self-reducibility
theorems do not directly give (15): the present sum combines the scalar
sectors through a common input and a nonpolynomial reciprocal readout.
The calculation constructs no new Weil representation or cubic
metaplectic cover. Its status is an application selected by loop data
inside established harmonic analysis.

The inspected primary sources did not supply this particular marked
operator and exact same-rank comparison. This bounded search is not a
literature-wide proof of novelty. Flat sector weights would define a
different operator and can produce a smaller norm; no optimality across
arbitrary choices of weights is claimed.

## 9. Arithmetic scope and the next obstruction

Theorem C is an infinite dimension family at fixed primes, not an
inverse system across residue characteristics or conductors. It supplies
the finite counting consequence (21). The previously proved
[local spectral lift](bol-section-local.md) belongs to the scalar-section
family and does not automatically extend this full reciprocal theorem.

A concrete obstruction rules out a natural attempted repair. Replace the
$`q`$-center by $`\mathbf Z/7^A`$, choose $`\eta_A`$ of order three
in its units, and choose $`\lambda_A`$ of order $`7^A`$ in a finite
extension of $`\mathbf F_3`$. Such data still give a directly verified
law (1). However, there is **no nonzero additive reduction** from the
next $`p`$-vector space to the previous one that intertwines these
faithful scalar actions with reduction of the $`q`$-center.

Indeed, if $`F`$ were such a reduction, equivariance at
$`t=7^A`$ would imply

```math
 F(\lambda_{A+1}^{7^A}x)=F(x),\qquad
 F\bigl((\lambda_{A+1}^{7^A}-1)x\bigr)=0.
```

The multiplier in parentheses is nonzero and therefore invertible on
the finite field vector space. Hence $`F=0`$. Trace maps cannot bypass
this obstruction. This excludes the stated additive, equivariant
reduction architecture; it does not exclude all correspondences or
other arithmetic models.

Theorem D answers the coupled-pencil question without requiring a
blockwise input restriction. The sharp remaining arithmetic bottleneck
is to replace the impossible additive reductions above by a specified
correspondence or representation induction and prove compatibility of
the Gram operators, additive-character conductors and normalized measures.
A concrete first test is whether an intertwining correspondence between
two consecutive 7-power levels carries the trace-determinant section
observable to a scalar multiple of the lower-level observable, with a
controlled norm and an explicitly described kernel. Within finite
analysis, nonidentical coordinate weights or nonproduct readouts require
a replacement for the identical-product extremal formula (26).
No Euler product, automorphy or quasi-RH consequence follows from the
finite identity without such additional structure.

## Reproducibility and status

The [exact verifier](../code/verify_bol_collective.py) checks the actual
finite-field law and word, the character ranks, the original cyclotomic
weights, all projective mass values, and a directly enumerated small
restriction of the actual readout. Its range and commands are in the
[code instructions](../code/README.md). The proofs above, rather than
finite tests or floating-point extrapolation, establish all $`h`$.
The separate coupled-pencil checker covers the extension-field matrices
and parameter kernels; its exact finite range is recorded in the same guide.

The [overview](../BOL_METAPLECTIC.md) and
[review record](../evidence/bol-metaplectic-review.md) distinguish the
exact scientific source, independent model review, finite evidence and
integration status. The new continuation is a proof proposed for review
until an exact-source verdict is recorded there. No permanent claim IDs
are allocated by the manuscript-local labels used here.

