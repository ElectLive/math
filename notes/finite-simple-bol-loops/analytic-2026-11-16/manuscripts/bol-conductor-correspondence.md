# Conductor correspondences for reciprocal Bol words

Mira Cult

The reciprocal section readout admits explicit norm-one correspondences across
conductor levels. A correspondence at every level preserves the old additive
characters and records the new primitive channels as a positive Gram remainder.
Above the elementary threshold $`7^{A-1}>k^2`$, a second correspondence carries
the whole readout losslessly on the relevant range, with its full Gram operator
and an explicitly calculated redistribution of conductor channels.

For the coupled pencils of the
[collective manuscript](bol-collective-cancellation.md), this gives an exact
arithmetic theorem on all mean-zero inputs. Put
$`q_A=3^{6\cdot7^{A-1}}`$, $`k=2h+1`$, and

```math
 C_\ell=3^{-2\ell}\sum_{a+b+c=\ell}\binom{\ell}{a,b,c}^{\!2}.
```

For every $`h\geq1`$ and every $`A`$ satisfying $`7^{A-1}>(2h+1)^2`$,

```math
 \|\mathcal R_{A,\mathrm{sp},h}\|_0^2
 =\frac{18}{7^A}q_A^{-4h}(3C_{2h}-C_{2h+1}),\qquad
 \|\mathcal R_{A,\mathrm{al},h}\|_0^2
 =\frac{18}{7^A}q_A^{-4h}(1-C_{2h+1}).
 \tag{1}
```

The two pencils have identical labeled nonzero scalar ranks $`4h`$. Their exact
norm ratio is asymptotic to $`\sqrt{3\sqrt3/(4\pi h)}`$, uniformly over this
conductor range. The proof includes all primitive channels; an upper bound
is not inferred from a one-way contraction identity.

The normalized operators $`\sqrt{7^A}\,q_A^{2h}\mathcal R_{A,h}`$ form a
coherent bounded Hilbert-space limit. This is a specified arithmetic
correspondence for the marked word. Its full-range version need not
intertwine central translations through the quotient of the centers.
Section 8 proves why contractivity, quotient equivariance, and losslessness
cannot all be required of that architecture.

## 1. The fixed pencil and the arithmetic tower

Let $`E_1=\mathbf F_{729}`$, and fix alternating matrices
$`B_1,\ldots,B_k\in M_n(E_1)`$ which are independent over $`\mathbf F_3`$ and
have zero common radical. Write $`B_\nu=\sum_i\nu_iB_i`$,
$`\nu\in\mathbf F_3^k`$, and $`r_\nu=\operatorname{rank}_{E_1}B_\nu`$.
The correspondence kernel below allows variable ranks. The scalar norm and
limit theorems assume

```math
 r_\nu=r>0\quad\text{for every }\nu\ne0.                 \tag{2}
```

Every matrix in the tower is the base change of this fixed matrix. In
particular, the construction does not independently choose unrelated pencils
at different conductors.

Put

```math
 m_A=7^A,\quad R_A=\mathbf Z/7^A,\quad
 E_A=\mathbf F_{3^{\,6\cdot7^{A-1}}},\quad q_A=|E_A|,\quad W_A=E_A^n.
```

Choose compatible elements $`\lambda_A\in E_A`$ of order $`7^A`$ with
$`\lambda_{A+1}^7=\lambda_A`$. Such choices exist in a fixed algebraic closure.
Since $`\operatorname{ord}_7(3)=6`$ and $`v_7(3^6-1)=1`$, the binomial
valuation formula gives
$`\operatorname{ord}_{7^A}(3)=6\cdot7^{A-1}`$. Thus
$`[E_B:E_A]=7^{B-A}`$ for $`B>A`$.
Let $`\eta_A\in R_A^\times`$ be the compatible root of
$`X^2+X+1`$ reducing to $`2`$ modulo seven. The derivative is a unit there,
so successive lifting gives existence and uniqueness. It has order three.
For example $`\eta_1=2`$ and $`\eta_2=30`$.

Use the absolute additive character
$`\psi_A(x)=e_3(\operatorname{Tr}_{E_A/\mathbf F_3}x)`$ and define

```math
 \beta_A(u,y)_i=\operatorname{Tr}_{E_A/\mathbf F_3}(u^{\mathsf T}B_i y),
 \quad V_A^{\rm loop}=R_A^{2k},\quad
 \gamma_A(v,w)=\sum_i(v_{i1}w_{i2}-v_{i2}w_{i1}).
```

The letter $`V_A`$ without the superscript will later denote a Hilbert-space
isometry. Let $`(D_av)_i=\eta_A^{a_i}v_i`$. The actual section law is

```math
 (x,v,a,t)\circ(y,w,b,s)
 =
 (x+\lambda_A^t y,\ v+D_aw,\ a+b-\beta_A(x,y),\
 t+s-\gamma_A(v,w)).                                  \tag{3}
```

It is defined on $`W_A\times V_A^{\rm loop}\times\mathbf F_3^k\times R_A`$.
The class-two group, stabilizer graph, and section calculation in
[Section 1 of the collective manuscript](bol-collective-cancellation.md#1-the-actual-reciprocal-section)
apply to these additive modules: halves exist in both odd characteristics,
the action is balanced, and $`b(U,R(c)U)=0`$. The direct division and Bol
calculations there use only these identities, so they prove (3) is a left
Bol law at every $`A`$. The same flexibility witness has vector coordinates
$`(1+\lambda_A^{-1})e`$ and $`2e`$, proving properness. No simplicity or
classification theorem is used.

Keep the original marked vectors $`(1,0)`$ and $`(0,1)`$ in each $`R_A`$-plane.
The same two-state section word gives the displacement
$`\lambda_A^{s-F_A(u,a,y)}e`$, where

```math
 F_A(u,a,y)=\sum_{i=1}^k\eta_A^{\,a_i-\beta_A(u,y)_i},\qquad
 \theta_A(t)=\psi_A(\lambda_A^t).
```

Choose an $`E_A`$-linear coordinate functional taking value one at $`e`$.
The operator studied throughout is exactly

```math
 (\mathcal R_Af)(u,a,s)
  =\mathbb E_{y\in W_A}f(y)\theta_A(s-F_A(u,a,y)).         \tag{4}
```

All finite spaces, including the later histogram space, carry normalized
counting measure. The domain is $`L^2(W_A)`$ and the output space is
$`L^2(W_A\times\mathbf F_3^k\times R_A)`$. The notation $`\|\cdot\|_0`$
means restriction to $`L^2_0(W_A)`$.

## 2. The exact readout and every conductor channel

Put $`\omega=e_3(1)`$ and $`c=\omega^{-1}-1`$. The relative Galois conjugates
of $`\lambda_{A+1}`$ are $`\lambda_{A+1}`$ times the seven seventh roots
of unity. Therefore

```math
 \operatorname{Tr}_{E_{A+1}/E_A}(\lambda_{A+1}^{t})
 =
 \begin{cases}
 0,&7\nmid t,\\
 \lambda_A^{t/7},&7\mid t.
 \end{cases}                                            \tag{5}
```

Here seven equals one in characteristic three. At level one the six
nontrivial seventh roots have trace $`-1`$, and $`\operatorname{Tr}(1)=0`$.
Induction gives

```math
 \theta_A(t)=1+c\,\mathbf1_{S_A}(t),\qquad
 S_A=7^{A-1}\{1,\ldots,6\}\subset R_A.                   \tag{6}
```

In particular the zero argument is outside the shell.
With $`\widehat f(\rho)=\mathbb E_s f(s)e_{m_A}(-\rho s)`$,

```math
 \widehat\theta_A(\rho)
  =\mathbf1_{\rho=0}
     +\frac{c}{m_A}\bigl(7\mathbf1_{7\mid\rho}-1\bigr).
 \tag{7}
```

For $`\rho\ne0`$, the additive-character conductor is
$`7^{A-v_7(\rho)}`$. The primitive weights are $`3/m_A^2`$; the nonzero
imprimitive weights are $`108/m_A^2`$. The constant weight is
$`1-18/m_A+108/m_A^2`$, and the total nonconstant energy is
$`18/m_A-108/m_A^2`$.

There is a useful all-channel Gram identity. For $`0\leq b\leq A`$, define
the collision operator $`\mathcal Q_{b,A}`$ by its normalized kernel

```math
 Q_{b,A}(y,z)=
 \mathbb E_{u,a}\mathbf1_{\{F_A(u,a,y)=F_A(u,a,z)\pmod{7^b}\}}.
```

Each is positive: it is a Gram of the partition by the indicated residue.
Also $`\mathcal Q_{0,A}=\Pi`$, where $`\Pi f=\mathbb Ef`$.
The intersection $`S_A\cap(S_A+d)`$ has size six if $`d=0`$, five if
$`d`$ is a nonzero multiple of $`7^{A-1}`$, and zero otherwise.
Using $`c+\bar c=-3`$ and $`|c|^2=3`$ gives

```math
 \boxed{\mathcal R_A^*\mathcal R_A
  =(1-18/m_A)\Pi+(15/m_A)\mathcal Q_{A-1,A}
                       +(3/m_A)\mathcal Q_{A,A}.}
 \tag{8}
```

At $`A=1`$ the displayed coefficient of $`\Pi`$ is negative. Positivity
belongs to the complete Gram identity; it is not claimed term by term
for that decomposition.

Equivalently, set
$`g_{A,\rho}(a)=e_{m_A}(-\rho\sum_i\eta_A^{a_i})`$ and
$`v_{A,\rho}=|\widehat\theta_A(\rho)|^2`$. Fourier orthogonality gives,
at a nonzero spatial frequency $`\xi`$,

```math
 \widehat{\mathcal R_A^*\mathcal R_A}(\xi)
 =\sum_{\rho\ne0}v_{A,\rho}
   \sum_{\nu\ne0}|\widehat g_{A,\rho}(\nu)|^2
      q_A^{-r_\nu}\mathbf1_{\{\xi\in\operatorname{im}_{E_A}B_\nu\}}.
 \tag{9}
```

The signs can simultaneously reverse $`\nu`$; its scalar image is unchanged.
Both $`\rho=0`$ and $`\nu=0`$ vanish on centered input. Formula (9) includes
all other ranks and conductors.

## 3. Trace inflation and a kernel-dependent coisometry

For $`B>A`$ let $`T_{A,B}=\operatorname{Tr}_{E_B/E_A}`$ coordinatewise,
and let $`K_{A,B}=\ker T_{A,B}\subset E_B`$.
The extension degree is one in $`\mathbf F_3`$, hence

```math
 E_B=E_A\oplus K_{A,B},\qquad T_{A,B}|_{E_A}=1.
```

The trace pairing makes this an orthogonal decomposition. Its restriction
to $`K_{A,B}`$ is nondegenerate, because the full pairing and the $`E_A`$
summand are nondegenerate. Write $`u=u_0+w`$ and $`y=y_0+z`$ accordingly.
Then

```math
 \beta_B(u,y)=\beta_A(u_0,y_0)+\beta_B(w,z).              \tag{10}
```

The normalized trace inflation

```math
 (J_{A,B}f)(y)=f(T_{A,B}y)                              \tag{11}
```

is an isometry and preserves the mean. It composes by transitivity of trace.

For every central label $`\nu`$, put

```math
 Z_{\nu,A,B}=\{w\in K_{A,B}^n:B_\nu w=0\},\qquad
 \mu_{\nu,A,B}=\mathbb P(w\in Z_{\nu,A,B})
             =(q_A/q_B)^{r_\nu}.                       \tag{12}
```

Indeed, Gaussian elimination over $`E_A`$ leaves $`n-r_\nu`$ free
coordinates in the $`E_A`$-space $`K_{A,B}`$ of dimension $`[E_B:E_A]-1`$.
In particular $`\mu_{0,A,B}=1`$.

Take Fourier transform only in $`a\in\mathbf F_3^k`$. For any additional
output variable $`t`$, define

```math
 \widehat{\mathcal C_{A,B}G}(\nu,u_0,t)
 =
 \mu_{\nu,A,B}^{-1/2}
 \mathbb E_{w\in K_{A,B}^n}
  \mathbf1_{Z_{\nu,A,B}}(w)\,
  \widehat G(\nu,u_0+w,t).                              \tag{13}
```

This is the explicit vector correspondence. Its adjoint is

```math
 \widehat{\mathcal C_{A,B}^*g}(\nu,u_0+w,t)
 =\mu_{\nu,A,B}^{-1/2}
   \mathbf1_{Z_{\nu,A,B}}(w)\widehat g(\nu,u_0,t).
 \tag{14}
```

Consequently $`\mathcal C_{A,B}\mathcal C_{A,B}^*=I`$ and
$`\|\mathcal C_{A,B}\|=1`$. Its kernel consists of the fiber functions
orthogonal to the normalized indicator in (13), sector by sector.
This replaces point restriction, whose ambient norm grows with the index.

For a phase $`\phi:\mathbf F_3^k\to\mathbf C`$, consider
$`\mathcal T_{A,\phi}f(u,a)=\mathbb E_yf(y)\phi(a-\beta_A(u,y))`$.
Equation (10) and additive orthogonality give the exact factorization

```math
 \widehat{\mathcal T_{B,\phi}J_{A,B}f}(\nu,u_0+w)
 =\widehat\phi(\nu)
   \left[\mathbb E_{y_0}f(y_0)e_3(-\nu\cdot\beta_A(u_0,y_0))\right]
   \mathbf1_{Z_{\nu,A,B}}(w).                           \tag{15}
```

Thus this output lies in the range of $`\mathcal C_{A,B}^*`$, and
$`\mathcal C_{A,B}`$ loses no norm on it. After applying $`\mathcal C`$,
the lower phase transform is multiplied in sector $`\nu`$ by
$`\sqrt{\mu_{\nu,A,B}}`$.

For $`C>B>A`$, the trace-zero decomposition splits into the two successive
trace-zero spaces. The kernel condition in (12) splits with it,
$`\mu_{\nu,A,C}=\mu_{\nu,A,B}\mu_{\nu,B,C}`$, and normalized averaging
disintegrates. Therefore

```math
 \mathcal C_{A,B}\mathcal C_{B,C}=\mathcal C_{A,C}.        \tag{16}
```

Under (2), all nonzero sectors have the common factor
$`\sqrt\mu=(q_A/q_B)^{r/2}`$. Centered input has no $`\nu=0`$ output, so
that scalar factor applies to the whole output of (15).

## 4. Correspondence preserving the old conductor labels

Let $`\mathcal P_{A,B}`$ be normalized averaging over the fibers of
$`R_B\to R_A`$. Its Fourier action retains precisely the upper labels
$`\rho=7^{B-A}\sigma`$ and sends them to $`\sigma`$.
The absolute conductor is unchanged.

On $`R_A`$ define the positive Markov contraction

```math
 (\mathcal M_A f)(s)=\frac16\sum_{j=1}^6
                  f(s+j7^{A-1}).                       \tag{17}
```

Its multiplier is one when $`7\mid\sigma`$ and $`-1/6`$ otherwise.
The negative primitive multiplier comes from a positive averaging kernel.
Equation (7) proves, for every $`B>A`$,

```math
 \mathcal M_A\mathcal P_{A,B}(\theta_B-1)
       =7^{A-B}(\theta_A-1).                            \tag{18}
```

Define

```math
 D^{\rm fil}_{A,B}
   =\mathcal M_A\mathcal P_{A,B}\mathcal C_{A,B}.
```

The factors act on the indicated separate variables, so (13), fiber averaging,
and (17) give its complete kernel. Its norm is at most one.
Let $`S_\mu`$ multiply the $`a`$-Fourier sector $`\nu`$ by
$`\sqrt{\mu_{\nu,A,B}}`$. Reducing $`\eta_B`$ to $`\eta_A`$, equations
(15) and (18) give the all-input identity

```math
 D^{\rm fil}_{A,B}\mathcal R_BJ_{A,B}f
 =7^{A-B}S_\mu\mathcal R_Af
       +(1-7^{A-B})(\mathbb Ef)\mathbf1.                 \tag{19}
```

For centered input and constant nonzero rank this becomes

```math
 \boxed{D^{\rm fil}_{A,B}\mathcal R_BJ_{A,B}
 =7^{A-B}(q_A/q_B)^{r/2}\mathcal R_A.}                  \tag{20}
```

The zero-channel correction in (19) is part of the construction.
Furthermore $`\mathcal P_{A,B}\mathcal M_B=\mathcal P_{A,B}`$, since
the shifts in (17) at level $`B`$ reduce to zero at level $`A`$. Together
with (16), this proves $D^{\rm fil}_{A,B}D^{\rm fil}_{B,C}
=D^{\rm fil}_{A,C}$.

The Gram statement distinguishes old and new characters. For adjacent levels,
let $`E_A^{\rm prim}`$ and $`E_A^{\rm imp}`$ project onto the nonzero central
frequencies with $`7\nmid\sigma`$ and $`7\mid\sigma`$, respectively.
On centered inputs, before applying $`\mathcal M_A`$,

```math
 J_{A,A+1}^*\mathcal R_{A+1}^*
  \mathcal P_{A,A+1}^*\mathcal P_{A,A+1}
  \mathcal R_{A+1}J_{A,A+1}
 =
 \frac{\mu}{49}\mathcal R_A^*
       (36E_A^{\rm prim}+E_A^{\rm imp})\mathcal R_A,
 \quad \mu=q_A^{-6r}.                                  \tag{21}
```

Here and in (21) the center averaging is understood to leave the upper
vector variable untouched. The vector coisometry may be inserted without
changing the Gram, by (15).
The amplitude ratios are $`-6/7`$ on lower primitive labels and $`1/7`$
on nonzero imprimitive labels. Multiplication by $`\mathcal M_A`$ gives
$`\mu\mathcal R_A^*\mathcal R_A/49`$.

The complementary upper primitive Gram is positive. On a lower nonzero
spatial frequency its multiplier is exactly

```math
 q_{A+1}^{-r}\frac{3}{m_{A+1}^2}
 \sum_{\substack{\rho\in R_{A+1}\\7\nmid\rho}}
 \sum_{\nu\ne0}|\widehat g_{A+1,\rho}(\nu)|^2
       \mathbf1_{\{\xi\in\operatorname{im}_{E_A}B_\nu\}}.
 \tag{22}
```

Thus the new primitive energy has not been silently discarded in a claimed
upper estimate. Equation (20) alone gives a lower bound upstairs.
At $`A=1`$ every nonzero lower label is primitive, so (21) is a scalar
multiple of the entire lower Gram. In particular the earlier exact
spread/aligned gain transfers unchanged to the old-conductor part.

## 5. Stabilization of the full Gram

For $`b\in\mathbf F_3^k`$, let $`\operatorname{hist}(b)=(c_0,c_1,c_2)`$
be its symbol counts. Let

```math
 \mathcal H_k=\{(c_0,c_1,c_2)\in\mathbf Z_{\ge0}^3:
                       c_0+c_1+c_2=k\},\quad
 M=|\mathcal H_k|=\binom{k+2}{2},\quad
 F_A(c)=c_0+c_1\eta_A+c_2\eta_A^2.
```

### Lemma H: exact histogram separation

If

```math
                    7^{A-1}>k^2,                       \tag{23}
```

then $`F_A(c)=F_A(d)`$ modulo $`7^{A-1}`$ or modulo $`7^A`$
if and only if $`c=d`$.

**Proof.** Put $`\delta_j=c_j-d_j`$, so $`\sum\delta_j=0`$, and the
sum of the positive $`\delta_j`$ is at most $`k`$. The difference is
$`(\delta_0-\delta_2)+(\delta_1-\delta_2)\eta_A`$. Multiplying by the
conjugate expression with $`\eta_A^2`$ gives the integer

```math
 \frac32\sum_j\delta_j^2
 =3(\delta_0^2+\delta_0\delta_1+\delta_1^2)=3S.
```

If the original difference is zero modulo $`7^{A-1}`$, that power of
seven divides $`3S`$, hence divides $`S`$. If $`c\ne d`$, then
$`0<S=\frac12\sum\delta_j^2\le k^2`$; the last inequality follows by
bounding the sums of squares separately on the positive and negative
coordinates by the square of their common total mass. This contradicts
(23). The converse is immediate. ∎

The separation assumption has content. At $`A=2,k=3`$, the distinct
histograms $`(0,0,3)`$ and $`(1,2,0)`$ both have section sum five modulo
seven. Their sums modulo 49 are five and twelve, respectively. Thus the
two collision operators in (8) need not coincide below the threshold.

Let $`\mathcal Q_{{\rm hist},A}`$ be the collision operator for equality of
$`\operatorname{hist}(a-\beta_A(u,y))`$ and
$`\operatorname{hist}(a-\beta_A(u,z))`$. Under (23), (8) becomes

```math
 \mathcal R_A^*\mathcal R_A
   =(1-18/m_A)\Pi+(18/m_A)\mathcal Q_{{\rm hist},A}.       \tag{24}
```

This is an exact arithmetic stabilization, including the primitive channels.
It replaces two residue tests by equality of three integer counts.

Put $`v_{A,c}(s)=\theta_A(s-F_A(c))`$.
The same shell calculation gives

```math
 \langle v_{A,c},v_{A,d}\rangle
       =(18/m_A)\mathbf1_{c=d}+1-18/m_A.                 \tag{25}
```

Distinct histogram readouts therefore form an explicit regular-simplex Gram
after restricting their coefficients to have sum zero.

## 6. Lossless correspondence for the full stabilized readout

Use normalized counting on $`\mathcal H_k`$. Define
$`V_A:L^2_0(\mathcal H_k)\to L^2(R_A)`$ by

```math
 V_Az(s)=\sqrt{\frac{m_A M}{18}}\,
             \mathbb E_{c\in\mathcal H_k}z(c)v_{A,c}(s).
 \tag{26}
```

Equation (25) proves $`V_A^*V_A=I`$. If $`Q_0`$ subtracts the uniform
histogram mean, its adjoint is explicitly

```math
 (V_A^*G)(c)=\sqrt{\frac{m_A M}{18}}\,
   Q_0\left(\mathbb E_s\overline{v_{A,c}(s)}G(s)\right).
 \tag{27}
```

For centered input put

```math
 (H_Af)(u,a,c)=\sqrt M\,\mathbb E_y f(y)
       \mathbf1_{\{\operatorname{hist}(a-\beta_A(u,y))=c\}}.
```

It takes values in $`L^2_0(\mathcal H_k)`$ pointwise in $`(u,a)`$, and

```math
                \mathcal R_A=\sqrt{18/m_A}\,V_AH_A.
 \tag{28}
```

The vector correspondence (13), now with histogram $`c`$ as a spectator,
satisfies $`\mathcal C_{A,B}H_BJ_{A,B}=\sqrt\mu\,H_A`$ under (2).
Its adjoint range contains $`H_BJ_{A,B}`$, by the same calculation as (15).

### Theorem T: explicit full transport and Gram identity

Suppose (2) and (23), and let $`B>A`$. Define

```math
 D^{\rm st}_{A,B}=V_A\mathcal C_{A,B}V_B^*,\qquad
 c_{A,B}=\sqrt{\frac{m_A}{m_B}}\left(\frac{q_A}{q_B}\right)^{r/2}.
 \tag{29}
```

Then $`\|D^{\rm st}_{A,B}\|=1`$, it composes coherently, and on all
mean-zero lower inputs,

```math
 \boxed{D^{\rm st}_{A,B}\mathcal R_BJ_{A,B}
                   =c_{A,B}\mathcal R_A,}              \tag{30}
```

```math
 \boxed{J_{A,B}^*\mathcal R_B^*\mathcal R_BJ_{A,B}
                   =c_{A,B}^2\mathcal R_A^*\mathcal R_A.} \tag{31}
```

**Proof.** Equations (26)--(28) and the factorization of $`H_BJ`$ prove
(30). Both $`V_B^*`$ and $`\mathcal C_{A,B}`$ are lossless on this actual
output range, and $`V_A`$ is an isometry, proving (31).
They are contractions on the whole ambient spaces. Since $`\mathcal C`$
is onto and the $`V`$ maps are isometries, the product has norm one.
It preserves histogram mean zero. Consequently
$`V_B^*V_B=I`$ can be inserted between successive factors, and (16) proves
$`D^{\rm st}_{A,B}D^{\rm st}_{B,C}=D^{\rm st}_{A,C}`$. ∎

There is no implicit polar-decomposition choice in this construction.
Its central kernel is

```math
 \mathscr K_{A,B}(s,t)=\frac{\sqrt{m_A m_B}}{18}
     \sum_{c\in\mathcal H_k}\widetilde v_{A,c}(s)
                               \overline{\widetilde v_{B,c}(t)},
 \quad
 \widetilde v_{A,c}=v_{A,c}-\mathbb E_dv_{A,d}.            \tag{32}
```

The full kernel, after Fourier transform in $`a`$, is

```math
 \widehat{D^{\rm st}_{A,B}G}(\nu,u_0,s)
 =\mu_{\nu,A,B}^{-1/2}
   \mathbb E_{w\in K_{A,B}^{\,n}}
    \mathbf1_{Z_{\nu,A,B}}(w)\,
    \mathbb E_{t\in R_B} \mathscr K_{A,B}(s,t)
                            \widehat G(\nu,u_0+w,t).
 \tag{33}
```

Here $`K_{A,B}^{\,n}`$ is the trace-zero space from Section 3, and
$`\mathscr K_{A,B}(s,t)`$ is the central kernel (32).

More intrinsically,
$(D^{\rm st}_{A,B})^*D^{\rm st}_{A,B}
 =V_B\mathcal C_{A,B}^*\mathcal C_{A,B}V_B^*$
is an orthogonal projection. Its orthogonal complement is exactly the
kernel of $`D^{\rm st}_{A,B}`$: central components orthogonal to the centered
histogram readout span, together with the trace-fiber components
orthogonal to (14) inside that span. This identifies the kernel on the
entire output space, rather than only on outputs of $`\mathcal R_B`$.

For uncentered input define
$`b_A(s)=\mathbb E_{c\in\mathcal H_k}v_{A,c}(s)`$ and
$`z_A(s)=\mathbb E_{a\in\mathbf F_3^k}v_{A,\operatorname{hist}(a)}(s)`$.
The same calculation gives the precise correction

```math
 D^{\rm st}_{A,B}\mathcal R_BJ_{A,B}f
 =\sqrt{\frac{m_A}{m_B}}\left[
 \sqrt\mu\,\mathcal R_Af
 +(1-\sqrt\mu)(\mathbb Ef)z_A-(\mathbb Ef)b_A\right].
 \tag{34}
```

Thus the constant input sector has not been asserted to follow (30).

### Exact conductor bookkeeping

For nonzero lower and upper labels $`\sigma,\rho`$, the central Fourier
matrix of (32) is

```math
 \frac{M\sqrt{m_A m_B}}{18}\,
 \widehat\theta_A(\sigma)\overline{\widehat\theta_B(\rho)}
 \operatorname{Cov}_{c\in\mathcal H_k}
 \left(e_{m_A}(-\sigma F_A(c)),\,e_{m_B}(-\rho F_B(c))\right),
 \tag{35}
```

where $\operatorname{Cov}(X,Y)=\mathbb E(X\overline Y)
-(\mathbb EX)\overline{\mathbb EY}$.
It is zero if either label is zero. All other coefficients are explicit.
This transport can mix nonzero conductor levels. Formula (35) records
that redistribution; it does not call it preservation of individual
character labels. The first transport (20) supplies that stricter
old-character property.

## 7. Full norms and a bounded arithmetic limit

Define the conductor-independent nonnegative histogram weights

```math
 \mu_k(\nu)=\sum_{c\in\mathcal H_k}
       \left|\mathbb E_{a\in\mathbf F_3^k}
          \mathbf1_{\{\operatorname{hist}(a)=c\}}e_3(-\nu\cdot a)
       \right|^2.
 \tag{36}
```

Their sum is one. Averaging over $`a,u`$ in the histogram Gram shows
that its nonzero spatial multiplier is

```math
 q_A^{-r}\sum_{\nu\ne0}\mu_k(\nu)
                \mathbf1_{\{\xi\in\operatorname{im}_{E_A}B_\nu\}}.
 \tag{37}
```

For a higher-field frequency, expand $`\xi=\sum_j e_j\xi_j`$ in an
$`E_A`$-basis of $`E_B`$. Since the matrices are over $`E_A`$,
$`\xi\in\operatorname{im}_{E_B}B_\nu`$ if and only if every $`\xi_j`$
belongs to $`\operatorname{im}_{E_A}B_\nu`$. A nonzero component therefore
has at least as large a weighted incidence. Conversely each lower
frequency embeds upstairs. Positivity of (36), not a reversed
contraction argument, proves

```math
 \boxed{\|\mathcal R_B\|_0^2
 =\frac{m_A}{m_B}\left(\frac{q_A}{q_B}\right)^r
                      \|\mathcal R_A\|_0^2}
 \quad(B>A,\ 7^{A-1}>k^2).                              \tag{38}
```

Thus $`\widetilde{\mathcal R}_A=\sqrt{m_A}\,q_A^{r/2}\mathcal R_A`$
has exactly the same mean-zero norm at all stable levels.

This also gives a specified limit operator. Let
$`X_A=L^2_0(W_A)`$ with isometric embeddings $`J_{A,B}`$, and let
$`Y_A`$ be the pointwise centered histogram readout span in the output,
equivalently the range of $`V_A`$ on
$`L^2(W_A\times\mathbf F_3^k;L^2_0(\mathcal H_k))`$.
The restriction of $`(D^{\rm st}_{A,B})^*`$ to $`Y_A`$ is an isometry
into $`Y_B`$. Losslessness in Theorem T gives

```math
 \widetilde{\mathcal R}_B J_{A,B}
       =(D^{\rm st}_{A,B})^*\widetilde{\mathcal R}_A.     \tag{39}
```

Coherence makes both Hilbert direct limits well-defined. Equation (38)
gives a bounded operator between them with the same exact norm.
The input limit is concretely
$`L^2_0(\varprojlim_A W_A)`$ for the trace reduction maps and normalized
Haar measure. The output limit is the specified Hilbert direct system;
no unproved identification with a local metaplectic representation is
part of this assertion.

## 8. What cannot be preserved simultaneously

The earlier additive-map obstruction remains valid: if a vector reduction
intertwined the faithful scalar actions with $`R_{A+1}\to R_A`$, then

```math
 F((\lambda_{A+1}^{7^A}-1)x)=0
```

would force $`F=0`$. The correspondences above are on function spaces and
do not assert such a vector reduction.

There is also an obstruction to combining the two conductor behaviors.
Suppose a **contractive** central operator $`L:L^2(R_B)\to L^2(R_A)`$
intertwines translations through the quotient $`R_B\to R_A`$.
For a translation in the kernel of the quotient, equivariance forces
$`L`$ to kill each character whose label is not divisible by $`7^{B-A}`$.
In particular it kills every upper primitive character.

The centered histogram readout span contains $`v_{B,c}-v_{B,d}`$ for
histograms differing by changing one zero symbol to one. Their phase
difference is $`\eta_B-1`$, a unit. Its primitive Fourier coefficient is

```math
 \widehat\theta_B(\rho)e_{m_B}(-\rho F_B(d))
       \bigl(e_{m_B}(-\rho(\eta_B-1))-1\bigr)\ne0
 \quad(7\nmid\rho).
```

A contraction killing that nonzero orthogonal component strictly decreases
the norm of this vector. Therefore it cannot be lossless on the whole
centered histogram readout span. Contractivity is essential to this
argument; no corresponding impossibility is claimed for amplifying maps.

Accordingly (20) preserves the old character labels and records a primitive
remainder, while (30) is lossless and has the explicit conductor mixing
(35). Neither is silently described as having both properties.

## 9. Sharp collective estimates throughout the stable conductor range

Take the two fixed $`E_1`$-pencils from
[Theorem D of the collective manuscript](bol-collective-cancellation.md#theorem-d-exact-coupled-norm-and-a-uniform-extra-exponent).
They have $`n=6h`$, $`k=2h+1`$, and $`r=4h`$ at every nonzero label.

For clarity, the spread pencil is the fixed matrix realization over $`E_1`$
of two copies of
$`\operatorname{Tr}_{L_h/E_1}\det[(t,t^3,t^9),x,y]`$,
where $`L_h=\mathbf F_{729^h}`$ and
$`t=j_h(\nu)`$ for an injective $`\mathbf F_3`$-linear map $`j_h`$.
The aligned pencil is the star form plus the trace-symplectic form on
$`\mathbf F_{729^{2h-1}}^2`$ with an injective parameter map.
Their verified common-radical and independence hypotheses persist under
base change. Even when $`7\mid h`$, no assertion that
$`L_h\otimes_{E_1}E_A`$ is a field is needed: we extend the fixed matrices.
A higher frequency decomposes into base-field components, so its compatible
parameter set is an intersection of sets of dimension at most two.
Every maximizing base-field plane and its attaining frequency remain
available. This avoids an unjustified extension-field compatibility premise.

### A product-mixture subspace lemma

Let $`\{w_t\}`$ be any measurable family of probability distributions on a
finite field $`F`$, with probability measure $`dt`$. Define
$`\mu(x)=\int\prod_{i=1}^k w_t(x_i)\,dt`$ and
$`P_j(t)=\sum_{a\in F}w_t(a)^j`$. Then, for $`1\le d<k`$,

```math
 \max_{\substack{D\le F^k\\\dim D=d}}\mu(D)
 =\max\left\{\int w_t(0)^{k-d}dt,\
              \int P_{k-d+1}(t)dt\right\}.             \tag{40}
```

**Proof.** Choose $`d`$ pivot coordinates and express the remaining
$`r=k-d`$ coordinates of $`D`$ as linear forms $`\ell_j(Z)`$.
Give $`(t,Z)`$ the joint probability law $`dt\prod_{i=1}^d w_t(Z_i)`$.
Hölder bounds the mass by the geometric mean of
$`\mathbb E w_t(\ell_j(Z))^r`$. If $`\ell_j=0`$, this moment is the first
quantity in (40); otherwise conditional rearrangement bounds it by the
second. The geometric mean is at most their maximum.
All-zero forms and all forms equal to $`Z_1`$ attain the two alternatives,
simultaneously for every $`t`$. This proof applies Hölder on the joint
space; it does not interchange a maximum and an integral. ∎

The histogram measure (36) is exactly such a mixture. For
$`z_0,z_1,z_2`$ independent uniform complex phases, put

```math
 w_z(j)=\left|\frac13\sum_{a=0}^2z_a e_3(-ja)\right|^2.
```

Parseval gives $`\sum_jw_z(j)=1`$. Expanding
$`\int\prod_iw_z(\nu_i)\,dz`$ retains exactly pairs of symbol sequences
with the same histogram, proving that this integral is $`\mu_k(\nu)`$.
Moreover

```math
 \int w_z(j)^\ell dz=C_\ell
 =3^{-2\ell}\sum_{a+b+c=\ell}\binom{\ell}{a,b,c}^{\!2},
 \quad \mu_k(0)=C_k.                                   \tag{41}
```

The moments are log-convex, and $`C_0=1,C_1=1/3`$, so
$`3C_{\ell+1}\ge C_\ell`$. Equations (40)--(41) yield

```math
 \max_{\dim D=d}\mu_k(D)=3C_{k-d+1}.                    \tag{42}
```

It is attained when $`k-d+1`$ coordinates are equal and the remaining
coordinates are free. All weights are nonnegative, so a smaller subspace
has no larger mass than a containing $`d`$-space.

For the spread pencil, each nonzero spatial frequency admits a parameter
space of dimension at most two. The degree-nine polynomial construction
in the preceding manuscript realizes every parameter two-plane, including
the maximizing one. Thus its exact nonzero image mass is
$`3C_{2h}-C_{2h+1}`$. In the aligned pencil the common star-image direction
attains the full nonzero mass $`1-C_{2h+1}`$.
Combining this with (24) and (37) proves (1).

The aligned value is the best bound obtainable by discarding joint image
conditions while retaining all scalar ranks and all actual readout weights.
This is a new conductor range for the specified marked family; it does not
improve the abstract weighted-Gram principle.

### Uniform size and the sharp asymptotic comparison

The collision moments also have the elementary Fourier integral

```math
 C_\ell=\frac1{(2\pi)^2}\int_{[-\pi,\pi]^2}
 \left(\frac{3+2\cos x+2\cos y+2\cos(x-y)}9\right)^\ell dx\,dy.
 \tag{43}
```

Write the expression in parentheses as $`\Phi(x,y)`$.
It equals
$`1-\frac49(\sin^2(x/2)+\sin^2(y/2)+\sin^2((x-y)/2))`$.
On this square it is bounded above by
$`\exp[-4(x^2+y^2)/(9\pi^2)]`$. Therefore, for $`\ell\ge1`$,

```math
                    C_\ell\le\frac{9\pi}{16\ell}.       \tag{44}
```

After substituting $`(x,y)=(X,Y)/\sqrt\ell`$, the integrand converges to
$`\exp[-(2/9)(X^2-XY+Y^2)]`$ and is dominated by the same Gaussian bound.
Its Gaussian integral gives

```math
                    C_\ell\sim\frac{3\sqrt3}{4\pi\ell}.
 \tag{45}
```

Consequently, uniformly in every choice of conductor satisfying (23),

```math
 \frac{\|\mathcal R_{A,\mathrm{sp},h}\|_0}
      {\|\mathcal R_{A,\mathrm{al},h}\|_0}
 =\sqrt{\frac{3C_{2h}-C_{2h+1}}{1-C_{2h+1}}}
 \sim\sqrt{\frac{3\sqrt3}{4\pi h}}.                     \tag{46}
```

Since $`C_\ell\le C_1=1/3`$, a simple absolute bound is

```math
 \frac{\|\mathcal R_{A,\mathrm{sp},h}\|_0}
      {\|\mathcal R_{A,\mathrm{al},h}\|_0}
 \le\min\left\{1,\frac{9\sqrt\pi}{8\sqrt h}\right\}.      \tag{47}
```

This is a polynomial collective improvement throughout the stable
conductor range. It is not the level-one exponential ratio; that stronger
fixed-conductor phenomenon has not been silently extrapolated.

For $`h=1`$, the exact ratio is $`\sqrt{26/53}`$.
For $`h=2`$, its square is $`350/1511`$.
The normalized limit operator of Section 7 has spread norm
$`\sqrt{18(3C_{2h}-C_{2h+1})}`$ and aligned norm
$`\sqrt{18(1-C_{2h+1})}`$.

The constant input frequency is exceptional. Under (2) its Gram eigenvalue is

```math
 1-\frac{18}{m_A}+\frac{18}{m_A}
       \left[C_k+q_A^{-r}(1-C_k)\right].                \tag{48}
```

It tends to one with conductor and does not have the centered scaling.

### Arithmetic counting consequence

Under (23), equality of the section sums modulo $`7^A`$ is precisely equality
of their integer symbol histograms. The histogram incidence operator $`H_A`$
has exact centered squared norms
$`q_A^{-4h}(3C_{2h}-C_{2h+1})`$ and
$`q_A^{-4h}(1-C_{2h+1})`$ for the two pencils.

For arbitrary input and output sets
$`X\subset W_A`$ and
$`Y\subset W_A\times\mathbf F_3^k\times\mathcal H_k`$,
with normalized densities $`\alpha,\sigma`$, Cauchy--Schwarz gives

```math
 \left|\mathbb E_{y,u,a,c}
   (\mathbf1_X(y)-\alpha)(\mathbf1_Y(u,a,c)-\sigma)
   \mathbf1_{\{\operatorname{hist}(a-\beta_A(u,y))=c\}}\right|
 \le
 \frac{q_A^{-2h}}{\sqrt M}
 \sqrt{3C_{2h}-C_{2h+1}}\,
 \sqrt{\alpha(1-\alpha)\sigma(1-\sigma)}
 \tag{49}
```

for the spread pencil. The factor $`1/\sqrt M`$ follows from the precise
normalization of $`H_A`$. The equation can equivalently be written
$`F_A(u,a,y)=F_A(c)`$ in $`R_A`$. No product condition on either set or
uniform-output-degree assumption is used.

## 10. Relation to Heisenberg--Weil theory and remaining scope

The standard field-trace and symplectic-product mechanisms are relevant.
[Gurevich--Hadani, GH-Q](../REFERENCES.md#gh-q), Propositions 2.7.1 and
2.7.5, give tensor-product compatibility and isotropic reduction.
[GH-SR](../REFERENCES.md#gh-sr), Proposition 2.9 and Theorem 2.10,
identify the trace-center pullback and its Weil representation.
For the rank-$`r`$ scalar alternating quotient and one adjacent extension,
the transverse symplectic
phase space has $`E_A`$-dimension $`6r`$ and cardinality $`q_A^{6r}`$.
Its irreducible Heisenberg representation has dimension $`q_A^{3r}`$.
The factor $`q_A^{-3r}`$ in (20) is its inverse dimension, equivalently
the inverse square root of phase-space cardinality. The kernel proof
(12)--(15) establishes the normalization directly.

[Henniart--Wang](../REFERENCES.md#hw-shintani), Lemma 3.1(i) and Theorem
4.1, prove normalized class-function and twisted-character compatibilities
for the Heisenberg--Weil representation with trace-lifted additive character.
A selected reciprocal section word is not thereby a Shintani class function.
The shell identity, Markov correction, histogram separation, explicit
readout isometries and joint-image estimate supply the additional
compatibility used here.

The preceding finite Bol-law proof and the selected word remain indispensable
interfaces. Erasing either reciprocal action or rebracketing the initial
word still removes the centered readout. Once this observable is selected,
its analysis uses ordinary Fourier theory and kernel geometry; no faithful
ordinary multiplicative representation of the loop is asserted.

The commissioned consecutive-level correspondence is supplied by (20),
with full old-conductor bookkeeping, and strengthened by (30)--(31) and
the arithmetic estimates (1), (46), and (49). The next representation-level
question is to construct a larger output model supporting central translations
or the relevant section operators while retaining the bounded coherent
readout. Section 8 rules out asking for a contractive, lossless transport
through the ordinary quotient action on the present small readout span.
An induced model retaining the extra primitive representations would have
to replace that requirement.

The Hilbert limit above is fully specified, but it has not been identified
with a representation of a local metaplectic cover. No Euler product,
global automorphy, analytic continuation, or cubic-metaplectic/quasi-RH
consequence is inferred from it.

## Reproduction and source status

The [code guide](../code/README.md) records the exact central and vector
checks and their finite ranges. They include the preserved low-conductor
histogram collision showing why a separation hypothesis is necessary.
The all-level correspondences, mixture inequality, limit and asymptotic
are established by the proofs above, not by finite extrapolation.

The preceding scientific source is
`ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`, delivered at
`d6edc4f86ae6ff7fc5216afa1565958abac4418c`.
The current main revision inspected during this continuation is
`4ded8c4fb264235370a745100755a26a372918ba`; its repository instructions
match those of the working branch. The new exact scientific pin and
independent verdict are recorded in the [review evidence](../evidence/bol-metaplectic-review.md)
and [overview](../BOL_METAPLECTIC.md). This new continuation remains proposed
until that exact-source verdict is recorded. No permanent claim IDs are
allocated by these manuscript-local theorem labels.

