# Non-scalar fusion and quantum mixing in reciprocal Bol loops

Mira Cult

## Abstract and scope

We construct explicit unitary fusion maps for the actual character-sector
operators of reciprocal Bol loops. Their tensor products retain a relative
coordinate with a non-scalar dilation and, in general, a residual bicharacter.
We characterize exactly when **any** unitary can eliminate the residual:
the scalar radical of the product character must equal the intersection of
the two input radicals. If this fails, an explicit residual model still
intertwines every left translation and every full correction, including zero
and imprimitive characters. The obstruction is followed by a construction,
not used as a no-go theorem for non-scalar quantization.

The derived subgroup of the intrinsic left-inner defect group gives a
canonical synchronized two-sector projection. Its exact normalized trace is
a joint-image statistic. On the previously constructed spread and aligned
pencils, all nonzero scalar ranks are $`4h`$, but these traces are
$`Q^{-6h}`$ and $`Q^{-(4h+1)}`$. Their ratio is $`Q^{-(2h-1)}`$.
This distinguishes the unmarked loops and measures an unavoidable fusion
coupling. It is a trace distinction, not a worst-case norm improvement.

A second consequence uses the loop's actual distribution of defects. On a
nondegenerate character sector, averaging conjugation by translated full
defects gives a positive, mixed-unitary quantum channel. Its exact
Hilbert--Schmidt contraction on trace-zero matrices is

```math
 \Lambda=\frac1p+\left(1-\frac1p\right)Q^{-r_{\min}}.
 \tag{NI.1}
```

The intrinsic coherence subspace contracts at most by $`p^{-2}`$ per step.
This gives a two-rate purity estimate, beyond the preceding scalar-state
spectrum and coercivity theorem. It supplies no bounded-degree quantum
expander or efficient circuit claim.

This manuscript answers the finite representation-theoretic part of Mira's
research order 2 of 16 November 2026. The starting scientific source is
`5771bfccb6707606078baf93be804f810276b8eb`, delivered in
[PR #440](https://github.com/Mira-Cult/math-wip/pull/440) at
`f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`.
The [baseline associator manuscript](bol-associator-quantization.md), cited
below as AQ, remains unchanged. The new work is in
[PR #441](https://github.com/Mira-Cult/math-wip/pull/441). Theorem labels here
are local; no permanent claim IDs or classification claims are changed.
Independent review and finite evidence are recorded separately in the
[review record](../evidence/bol-nonscalar-review.md).

## 1. The actual loop and the quantitative questions

### 1.1. Hypotheses and conventions

Use exactly AQ, Section 1.1. Thus $`p,q`$ are distinct odd primes,
$`p\mid q-1`$, $`A\geq1`$, $`m=q^A`$, and $`R_A=\mathbf Z/m\mathbf Z`$.
The field $`E`$ has characteristic $`p`$, cardinality $`Q`$, and an element
$`\lambda`$ of order $`m`$. The unit $`\eta\in R_A^\times`$ has order
$`p`$, also modulo $`q`$. The alternating matrices $`B_1,\ldots,B_k`$
over $`E`$ are independent over $`\mathbf F_p`$ and have zero common
radical; independence over $`E`$ is not assumed. Set

```math
 \begin{split}
 W&=E^n,\quad V=(R_A^2)^k,\quad U=W\oplus V,
       \quad Z=\mathbf F_p^k\oplus R_A,\quad d=|U|,\\
 b((w,v),(w',v'))
   &=\left((\operatorname{Tr}_{E/\mathbf F_p}
                    w^{\mathsf T}B_iw')_i,
          \sum_i\det(v_i,v_i')\right),\\
 R(a,t)(w,(v_i)_i)&=(\lambda^t w,(\eta^{a_i}v_i)_i).
 \end{split}                                                   \tag{NI.2}
```

The loop and its character-sector matrices are

```math
 \begin{split}
 (a,c)\circ(u,e)&=(a+R(c)u,c+e-b(a,u)),\\
 \pi_\chi(a,c)|u\rangle
   &=\chi(c-b(a,u))|a+R(c)u\rangle .
 \end{split}                                                   \tag{NI.3}
```

In (NI.3), $`a,u\in U`$ and $`c,e\in Z`$. The right nucleus is
intrinsically $`N=N_r(\mathcal L)=\{0\}\times Z`$. Its characters are
$`\chi=(\nu,\rho)`$, where
$`\chi(a,t)=e_p(\nu\cdot a)e_m(\rho t)`$.
Write $`B_\nu=\sum_i\nu_iB_i`$, $`r_\nu=\operatorname{rank}_E B_\nu`$,
$`a_\rho=A-v_q(\rho)`$ with $`v_q(0)=A`$, and

```math
 D_\chi=\ker_E B_\nu\oplus(\operatorname{ann}_{R_A}\rho)^{2k},
 \qquad |D_\chi|/d=Q^{-r_\nu}q^{-2ka_\rho}.
 \tag{NI.4}
```

Point kets are orthonormal, equivalently normalized point vectors in
normalized counting $`L^2`$. All averages are normalized. Composition is
right-to-left. We use ordinary
$`\|T\|_{\rm HS}^2=\operatorname{Tr}(T^*T)`$ for matrix-space norms,
and explicitly write $`\operatorname{tr}_0=\operatorname{Tr}/D`$ on
a Hilbert space of dimension $`D`$ when a normalized trace is intended.
Thus $`\|T\|_{{\rm HS},0}^2=\operatorname{tr}_0(T^*T)`$.

For $`x=(a,c)`$, $`y=(v,e)`$, define

```math
 g=b(a,v),\qquad h=R(g)a-R(e)a+R(c+g)v-v.
 \tag{NI.5}
```

The actual left-inner defect and its full sector correction are

```math
 \begin{split}
 \ell_{x,y}=L_{x\circ y}^{-1}L_xL_y&=H_{h,g},
 &H_{h,g}(u,z)&=(R(g)u,z+b(h,u)),\\
 J_\chi(h,g)|u\rangle&=\chi(b(h,u))|R(g)u\rangle,
 &\pi_\chi(x)\pi_\chi(y)&=\pi_\chi(x\circ y)J_\chi(h,g).
 \end{split}                                                   \tag{NI.6}
```

AQ, Sections 2--4, directly proves the loop divisions, proper left Bol
identity, right nucleus, these signs, and

```math
 \begin{split}
 H_{h,g}H_{h',g'}&=H_{h'+R(g')h,g+g'},\\
 \pi_\chi(x)\pi_\chi(y)\pi_\chi(x)
     &=\pi_\chi(x\circ(y\circ x)),\\
 J_\chi(\ell_{x,y\circ x})J_\chi(\ell_{y,x})&=I,
 &\ell_{x,y}^{-1}&=\ell_{y,x\circ y}.
 \end{split}                                                   \tag{NI.7}
```

Here $`J_\chi(\ell)`$ denotes the restriction of that permutation with
its parameters in (NI.6). The actual defects generate all
$`H=\{H_{h,g}:h\in U,g\in Z\}`$. These are recovered baseline results.

### 1.2. Baseline and chosen targets

AQ proves the full spectrum of the one-vector average
$`\mathcal A=\mathbb E_{x,y}U_{\ell_{x,y}}`$ and the sharp scalar-state
norm of its translation conjugates. Its complete spectrum already contains
joint-image tests. We do not claim that our invariants are unrecoverable from
that entire spectrum. The new obligations are simultaneous full-correction
fusion, explicit non-scalar intertwiner spaces, a canonical two-sector trace,
and a theorem on **matrix** coherences for the actual translated-defect channel.

The scales are fixed: the pair trace is normalized by $`d^2`$; the worked
comparison varies $`h\geq1`$ at $`Q=729`$; the channel estimate is uniform
in dimension and conductor, with time $`t\geq1`$. Degenerate sectors are
retained in the construction; depolarization has an explicit nondegeneracy
hypothesis.

## 2. Alternatives, failed equations and the selected framework

| Approach | Concrete test and outcome | Decision |
| --- | --- | --- |
| Operator-valued sector fusion | A relative-coordinate transform retains modulation and dilation; decoupling is a joint-radical condition | Prove the criterion and residual repair |
| Heisenberg polarizations with section data | Reciprocal actors fail scalar symplecticity; cotangent doubling repairs the action but alone gives established Weyl transport | Retain exact polarization covariance |
| Category-valued modules | Existing higher weak actions require actual coefficient categories; a transported pentagon gives no bound | Legitimate alternative, unnecessary for this finite theorem |
| Algebra of translations and defects | Synchronized tensor and Hom actions retain joint geometry and the selected defect distribution | Use it for intertwiners and quantum estimates |

The failed polarization equation is precise. Field symplecticity of
multiplication by $`\lambda`$ in a nonzero scalar sector requires
$`(\lambda^2-1)B_\nu=0`$, impossible since $`\lambda^2\ne1`$ and
$`B_\nu\ne0`$. On a ring plane it requires
$`\rho(\eta^2-1)=0`$, impossible for any $`\rho\ne0`$, including
imprimitive $`\rho`$, because $`\eta^2-1`$ is a unit. One cannot simply
declare these reciprocal actors symplectic on the scalar quotient. AQ's
doubled Weyl realization repairs that specific equation.

The scalar-projective collapse in AQ, Proposition 4.1, rules out only the
specified scalar closure. We retain $`J`$ and never impose
$`\pi(x)\pi(y)=\pi(x\circ y)`$. Associative matrix multiplication is
compatible with this aim: the loop-selected labels, corrections and probability
measure remain visible.

## 3. Two intrinsic subgroups and a canonical section

**Theorem I (intrinsic affine coordinates and shears).** Let $`X`$ be the
right-$`N`$ orbit set, with origin the identity orbit. Let $`G_0`$ be
generated by the induced left translations on $`X`$. Then

```math
 G_0=T_U\rtimes R(Z),\qquad [G_0,G_0]=T_U,
 \qquad [H,H]=S:=\{H_{h,0}:h\in U\}.
 \tag{NI.8}
```

The characteristic subgroup $`T_U`$ acts regularly on $`X`$, recovering
an intrinsic additive group structure. Each nucleus orbit has a unique
representative whose induced left translation lies in $`[G_0,G_0]`$;
this representative is $`(u,0)`$. This section is canonical for this family.

Every actual isomorphism between two admissible reciprocal loops has the form

```math
 \phi(u,c)=(Fu,\theta c),\qquad
 FR(c)=R'(\theta c)F,\qquad
 \theta b(u,v)=b'(Fu,Fv),
 \tag{NI.9}
```

where $`F,\theta`$ are additive group isomorphisms. Conversely these
conditions suffice. No $`E`$-linearity of $`F`$ is asserted.

**Proof.** The left action on $`X=U`$ is $`T_aR(c)`$. All translations
occur at $`c=0`$ and all actors at $`a=0`$. Both factors are abelian,
so the derived subgroup lies in $`T_U`$. Choose $`c_*`$ with ring
coordinate one and every $`p`$-coordinate one. Then $`R(c_*)-I`$ is
invertible: its field scalar is $`\lambda-1\ne0`$ and each ring scalar
is the unit $`\eta-1`$. Commutators with this actor produce every
translation. Faithfulness of $`R`$ gives $`T_uR(c)\in T_U`$ exactly
when $`c=0`$, proving the section characterization.

Similarly $`H/S`$ is abelian by (NI.7), and conjugation by $`H_{0,g}`$
sends $`H_{h,0}`$ to $`H_{R(-g)h,0}`$. The invertibility of
$`R(-c_*)-I`$ makes these commutators generate all $`S`$.

An isomorphism transports the right nucleus, induced left actions, and their
characteristic derived groups. Its coset permutation $`F`$ fixes the origin
and conjugates the regular translation groups, hence is additive. Initially
right-nucleus equivariance gives
$`\phi(u,c)=(F(u),s(u)+\theta c)`$. The canonical section forces
$`s(u)=0`$. Transport of actors and of the central coordinate in (NI.3)
gives (NI.9). Conversely substitute (NI.9) into (NI.3).
$`\square`$

This strengthens AQ's general isomorphism transport for this particular
family. It does not identify arbitrary pencil-coordinate changes or isotopies
with loop isomorphisms. A nonlinear representative change remains a gauge.

## 4. Full sector fusion, its exact obstruction and repair

### 4.1. Explicit residual intertwiners

Fix $`\chi,\psi`$, put $`\sigma=\chi\psi`$, and choose any additive
$`K:U\to U`$ commuting with all $`R(c)`$. Define

```math
 \begin{split}
 F_K|u,v\rangle&=|r=u+K(v-u),t=v-u\rangle,\\
 C_K(a,t)&=\frac{\psi(b(a,t))}{\sigma(b(a,Kt))}.
 \end{split}                                                   \tag{NI.10}
```

The inverse is $`u=r-Kt`$, $`v=r+(I-K)t`$. Thus $`F_K`$ is an
explicit norm-one unitary even for singular $`K`$, onto
$`\mathbf C[U_r\times U_t]`$ of dimension $`d^2`$. Define

```math
 \begin{split}
 \Pi_{\sigma,C}(a,c)|r,t\rangle
   &=\sigma(c-b(a,r))C(a,t)^{-1}
                 |a+R(c)r,R(c)t\rangle,\\
 \mathcal J_{\sigma,C}(h,g)|r,t\rangle
   &=\sigma(b(h,r))C(h,t)|R(g)r,R(g)t\rangle .
 \end{split}                                                   \tag{NI.11}
```

**Theorem F (full fusion compatibility).** For every admissible family,
every pair of characters, and every such $`K`$,

```math
 \begin{split}
 F_K(\pi_\chi(x)\otimes\pi_\psi(x))F_K^{-1}
     &=\Pi_{\sigma,C_K}(x),\\
 F_K(J_\chi(h,g)\otimes J_\psi(h,g))F_K^{-1}
     &=\mathcal J_{\sigma,C_K}(h,g).
 \end{split}                                                   \tag{NI.12}
```

The target satisfies the corrected product, Bol sandwich and inverse-defect laws

```math
 \begin{split}
 \Pi(x)\Pi(y)&=\Pi(x\circ y)\mathcal J(\ell_{x,y}),\\
 \Pi(x)\Pi(y)\Pi(x)&=\Pi(x\circ(y\circ x)),\\
 \mathcal J(\ell_{x,y\circ x})\mathcal J(\ell_{y,x})&=I.
 \end{split}                                                   \tag{NI.13}
```

Zero, degenerate and imprimitive sectors are included literally.

**Proof.** Tensor translation sends $`u,v`$ to
$`a+R(c)u,a+R(c)v`$. Thus $`t'=R(c)t`$ and $`r'=a+R(c)r`$.
The phase is

```math
 \chi(c-b(a,r-Kt))\psi(c-b(a,r+(I-K)t))
      =\sigma(c-b(a,r))C_K(a,t)^{-1}.
```

The same substitution in the full defect gives
$`\sigma(b(h,r))C_K(h,t)`$ and both dilations in (NI.11), proving
(NI.12) with phases and supports. Conjugating the tensor versions of
(NI.6)--(NI.7) proves (NI.13). No character division or radical quotient
has been used. $`\square`$

Taking $`K=0`$ always works. If $`\sigma=1`$ but $`\psi\ne1`$,
the target still contains $`C_0=\psi\circ b`$. Dropping that coupling
in the zero-total sector changes the operators.

### 4.2. When any unitary can decouple the fusion

Write $`\chi=(\nu,\rho)`$, $`\psi=(\mu,\tau)`$, so
$`\sigma=(\nu+\mu,\rho+\tau)`$, and
$`D_c|t\rangle=|R(c)t\rangle`$.

**Theorem D (complete decoupling criterion).** The following are equivalent:

1. A unitary $`V`$ satisfies
   $`V(\pi_\chi(x)\otimes\pi_\psi(x))V^{-1}
      =\pi_\sigma(a,c)\otimes D_c`$ for every $`x=(a,c)`$.
2. A unitary intertwines all full defects with
   $`J_\sigma(h,g)\otimes D_g`$.
3. $`D_\sigma=D_\chi\cap D_\psi`$.
4. $`\operatorname{im}_E B_\mu\subseteq
       \operatorname{im}_E B_{\nu+\mu}`$ and
   $`\tau\in(\rho+\tau)R_A`$.
5. An additive $`R`$-equivariant $`K`$ satisfies $`C_K=1`$.

When they hold, choose $`E`$-linear $`K_W`$ solving
$`B_{\nu+\mu}K_W=B_\mu`$, and on each ring plane use scalar $`k_0`$
with $`(\rho+\tau)k_0=\tau`$. Then $`F_K`$ supplies both intertwiners.

**Proof.** Condition 4 solves these equations, giving 5; (NI.12) gives 1
and 2. Condition 1 gives 2 by taking the corrected product at the actual
label $`x\circ y`$. Its multiplicity correction is exactly
$`D_{c+e-(c+e-g)}=D_g`$.

For necessity, each $`H_{h,0}`$ is itself an actual defect: take
$`y=(0,c_*)`$ and $`x=(u,c)`$, giving
$`h=(I-R(c_*))u`$ ranging over $`U`$. Trace invariance in 2 requires

```math
 \begin{split}
 \operatorname{tr}_0(J_\chi(h,0)\otimes J_\psi(h,0))
      &=\mathbf1_{D_\chi\cap D_\psi}(h),\\
 \operatorname{tr}_0(J_\sigma(h,0)\otimes I)
      &=\mathbf1_{D_\sigma}(h).
 \end{split}                                                   \tag{NI.14}
```

Thus 2 implies 3 for arbitrary unitaries, not just linear ansatzes.
Always $`D_\chi\cap D_\psi\subseteq D_\sigma`$. Field equality is
equivalent to $`\ker B_{\nu+\mu}\subseteq\ker B_\mu`$, hence by
alternation to the image containment in 4. Ring equality requires
$`\operatorname{ann}(\rho+\tau)\subseteq\operatorname{ann}\tau`$,
equivalent to $`v_q(\tau)\geq v_q(\rho+\tau)`$, including zero,
or exactly the divisibility in 4. Therefore 3 implies 4. $`\square`$

For nondegenerate $`k=1`$ field blocks and nonzero $`\nu+\mu`$,
one may take $`K_W=\mu/(\nu+\mu)`$; unit ring totals allow
$`k_0=\tau/(\rho+\tau)`$. These explicit nontrivial intertwiners
exist at every dimension and conductor. In contrast, total-zero fusion
decouples only when both inputs are zero: (NI.4) and independence give
$`D_\chi=U`$ exactly when $`\chi=1`$. Theorem F repairs all other cases.

Even a decoupled fusion needs its multiplicity correction. For $`g\ne0`$,

```math
 \inf_{|z|=1}\|D_g-zI\|_{{\rm HS},0}^2
    =2\left(1-\frac{|\operatorname{Fix}R(g)|}{d}\right)>0.
 \tag{NI.15}
```

Expand the norm and use the permutation trace. This is the exact failure of
replacing the multiplicity dilation by a scalar phase.

## 5. Composition, reassociation and covariance

### 5.1. Barycenter choices and actual isomorphisms

For $`K'=K+T`$, where $`T`$ is additive and $`R`$-equivariant, define
$`A_T|r,t\rangle=|r+Tt,t\rangle`$. Then

```math
 F_{K'}=A_TF_K,\qquad
 C_{K'}(a,t)=C_K(a,t)\sigma(b(a,Tt))^{-1}.
 \tag{NI.16}
```

This $`A_T`$ intertwines both target operator systems. If both residuals
are trivial it intertwines the decoupled systems; no arbitrary solution is
declared canonical. For (NI.9), transport characters by
$`\chi'=\chi\circ\theta^{-1}`$, $`\psi'=\psi\circ\theta^{-1}`$
and $`K'=FKF^{-1}`$. The point unitary $`C_F|u\rangle=|Fu\rangle`$
obeys

```math
 F_{K'}(C_F\otimes C_F)=(C_F\otimes C_F)F_K.
 \tag{NI.17}
```

It transports all operators and residuals. Additive $`R`$-equivariance
suffices; an $`E`$-linear subclass need not survive every field presentation.

### 5.2. Section and polarization changes

Changing representatives to $`(u,s(u))`$ changes the chart by
$`G_\chi|u\rangle=\chi(s(u))|u\rangle`$ from new kets to old ones.
New matrices are $`G_\chi^{-1}\pi_\chi G_\chi`$ and
$`G_\chi^{-1}J_\chi G_\chi`$. In fused coordinates the gauge is

```math
 G_{\rm fus}|r,t\rangle
  =\chi(s(r-Kt))\psi(s(r+(I-K)t))|r,t\rangle,
 \qquad G_{\rm fus}=F_K(G_\chi\otimes G_\psi)F_K^{-1}.
 \tag{NI.18}
```

It generally does not factor into a $`\sigma`$ gauge in $`r`$ and a
trivial gauge in $`t`$. This is precise section covariance; Theorem I
also supplies a preferred intrinsic section for this family.

An explicit alternative polarization without a radical quotient is

```math
 \mathscr F|u\rangle=d^{-1/2}\sum_{\xi\in\widehat U}
                   \overline{\xi(u)}|\xi\rangle.
```

Writing $`B_\chi(h)(u)=\chi(b(h,u))`$, Fourier orthogonality gives

```math
 \mathscr FJ_\chi(h,g)\mathscr F^{-1}|\xi\rangle
       =|(\xi B_\chi(h))\circ R(-g)\rangle.
 \tag{NI.19}
```

Every degenerate and zero sector is retained. For any specified unitary
polarizations $`P_\chi,P_\psi,P_{\rm out}`$, the map
$`P_{\rm out}F_K(P_\chi^{-1}\otimes P_\psi^{-1})`$ intertwines the
conjugated translations and full corrections by (NI.12). This is established
Fourier/basis transport, not by itself the analytic contribution.

### 5.3. Reassociation without erasing intermediate sectors

For a binary fusion tree on $`j`$ inputs, let $`F_T`$ be its invertible
coordinate map from $`U^j`$, retaining every relative coordinate and
residual phase. Compose (NI.10); $`K=0`$ is always permitted. Define
tree operators by conjugating the original tensor products. Then

```math
 R_{T,T'}=F_{T'}F_T^{-1},\qquad
 R_{T',T''}R_{T,T'}=R_{T,T''}.
 \tag{NI.20}
```

These unitary recouplings intertwine every translation and full correction.
Intermediate zero characters cause no singularity. Composition and the
pentagon have correctly matched spaces. This telescoping is formal; it is
not the source of an analytic estimate.

For an explicit regular example, take scalar charges
$`\chi=\varphi^a,\psi=\varphi^b,\omega=\varphi^c`$ with
$`a+b,b+c,a+b+c`$ units in the primary coordinate rings. Weighted
barycenters give total $`r=(au+bv+cw)/(a+b+c)`$. If the left-tree
coordinates are $`s=v-u`$, $`t=w-(au+bv)/(a+b)`$, the right-tree ones are

```math
 s'=t-\frac{a}{a+b}s,\qquad
 t'=\frac{b(a+b+c)}{(a+b)(b+c)}s+\frac{c}{b+c}t.
 \tag{NI.21}
```

The coefficient matrix has determinant $`-1`$. This non-scalar permutation
commutes with simultaneous actors, including the full $`D_g`$ corrections.
When a denominator is not a unit, use (NI.20), not (NI.21). Tensor recoupling
does not equate $`(x\circ y)\circ z`$ and $`x\circ(y\circ z)`$:
their transported AQ.24 identity retains the actual factor
$`\Pi(x\circ(y\circ z))^{-1}\Pi((x\circ y)\circ z)`$.

## 6. A canonical joint-defect trace and quantitative obstruction

The intrinsic $`S=[H,H]`$ selects an orthogonal projection

```math
 Q_{\chi,\psi}=\mathbb E_{s\in S}J_\chi(s)\otimes J_\psi(s).
 \tag{NI.22}
```

It averages a finite group action. This is not the distribution of individual
loop pairs $`(x,y)`$ used in Section 8. No external pencil marking is in
the definition.

**Theorem T (exact synchronized trace).** Put
$`r_{\nu,\mu}=\operatorname{rank}_E[B_\nu\ B_\mu]`$. Then

```math
 \boxed{\quad
 \operatorname{tr}_0Q_{\chi,\psi}
    =Q^{-r_{\nu,\mu}}q^{-2k\max(a_\rho,a_\tau)}.
 \quad}                                                       \tag{NI.23}
```

For $`P_\sigma=\mathbb E_{s\in S}J_\sigma(s)`$, the exact ratio is

```math
 \frac{\operatorname{tr}_0Q_{\chi,\psi}}
      {\operatorname{tr}_0(P_\sigma\otimes I)}
   =Q^{-\delta}q^{-2k(\max(a_\rho,a_\tau)-a_{\rho+\tau})},
 \qquad \delta=r_{\nu,\mu}-r_{\nu+\mu}\geq0.
 \tag{NI.24}
```

It is one exactly in the decoupled cases. For every unitary $`V`$,

```math
 \|VQ_{\chi,\psi}V^{-1}-P_\sigma\otimes I\|_{{\rm HS},0}^2
   \geq\operatorname{tr}_0(P_\sigma\otimes I)
         -\operatorname{tr}_0Q_{\chi,\psi}.
 \tag{NI.25}
```

The bound is sharp over arbitrary unitaries. If ranks differ, their
operator-norm distance is one for every $`V`$.

**Proof.** Shear orthogonality retains exactly
$`B_\nu u_W+B_\mu v_W=0`$ and $`\rho u_i+\tau v_i=0`$.
The field map has image size $`Q^{r_{\nu,\mu}}`$; the ring map has
image $`(\rho R_A+\tau R_A)^{2k}`$ of size
$`q^{2k\max(a_\rho,a_\tau)}`$. Kernel density gives (NI.23).
The single-character density is (NI.4), giving (NI.24). The ratio is one
exactly when the contained radicals in Theorem D have equal size.

Projections of ranks $`r\leq s`$ in dimension $`D`$ have squared
normalized HS distance
$`(r+s-2\operatorname{Tr}(PQ))/D\geq(s-r)/D`$.
Nesting the smaller range attains equality. If $`r<s`$, the larger range
has a unit vector orthogonal to the smaller, giving norm at least one;
a difference of orthogonal projections has norm at most one. $`\square`$

Equivalently (NI.23) is
$`\mathbb E_{s\in S}\operatorname{tr}_0J_\chi(s)
\operatorname{tr}_0J_\psi(s)`$, a cross-sector correlation. Independent
shear averaging instead gives
$`Q^{-r_\nu-r_\mu}q^{-2k(a_\rho+a_\tau)}`$. The synchronized-to-independent
ratio is exactly
$`Q^{r_\nu+r_\mu-r_{\nu,\mu}}q^{2k\min(a_\rho,a_\tau)}`$.

For a Fourier interpretation, restrict to $`E`$-linear $`K_W`$. The
minimum rank of $`B_\mu-B_{\nu+\mu}K_W`$ is exactly $`\delta`$:
quotient by $`\operatorname{im}B_{\nu+\mu}`$ for the lower bound;
choose a complement and cancel the image component with a right inverse
to attain it. For residual matrix $`C`$, the normalized operator
$`f\mapsto\mathbb E_t e_p(\operatorname{Tr}(a^{\mathsf T}Ct))f(t)`$
has rank $`Q^{\operatorname{rank}C}`$ and all nonzero singular values
$`Q^{-\operatorname{rank}C/2}`$. Character orthogonality proves this
ordinary Fourier fact; the new datum is the forced residual, not a general
uncertainty theorem or optimality over every possible framework.

## 7. Explicit intertwiners of the full defect systems

On $`\operatorname{Hom}(\mathcal H_\psi,\mathcal H_\chi)`$, let

```math
 \mathsf P_{\chi,\psi}(T)
    =\mathbb E_{h,g}J_\chi(h,g)T J_\psi(h,g)^*.
```

This projects orthogonally onto $`\operatorname{Hom}_H(J_\psi,J_\chi)`$.
Define

```math
 K_{\chi,\psi}=\{(s,t):B_\nu s_W=B_\mu t_W,
                   \ \rho s_i=\tau t_i\ (1\leq i\leq k)\}.
 \tag{NI.26}
```

**Theorem H (explicit full-defect intertwiners).** For each diagonal
$`R(Z)`$-orbit $`O\subseteq K_{\chi,\psi}`$, set

```math
 C_O=|O|^{-1/2}\sum_{(s,t)\in O}|s\rangle\langle t|.
 \tag{NI.27}
```

These are an orthonormal HS basis of the full-defect intertwiner space,
with $`\|C_O\|_{\rm op}\leq1`$. They intertwine every actual correction,
not only its scalar phase or rank. The exact dimension and correlation are

```math
 \boxed{\begin{split}
 \dim\operatorname{Hom}_H(J_\psi,J_\chi)
  &=\left(1+\frac{Q^{2n-r_{\nu,\mu}}-1}{m}\right)
    \left(1+\frac{q^{4A-2\max(a_\rho,a_\tau)}-1}{p}\right)^k\\
  &=\mathbb E_{h,g}\operatorname{Tr}J_\chi(h,g)
                      \overline{\operatorname{Tr}J_\psi(h,g)}.
 \end{split}}                                                 \tag{NI.28}
```

**Proof.** On $`|s\rangle\langle t|`$, shear phase is
$`\chi(b(h,s))\overline{\psi(b(h,t))}`$. Averaging imposes (NI.26);
the remaining average is the simultaneous actor-orbit average. Disjoint
orbit sums give exactly (NI.27); operator norm is bounded by HS norm.
The field kernel has $`Q^{2n-r_{\nu,\mu}}`$ elements, every nonzero
pair having orbit length $`m`$. Each ring-plane kernel has
$`q^{4A-2\max(a_\rho,a_\tau)}`$ elements, and each nonzero pair has
orbit length $`p`$, even for imprimitive coordinates, since differences
of distinct powers of $`\eta`$ are units. Actors on these factors are
independent. Multiplying orbit counts proves the first equality. Taking the
matrix-space trace of the group average proves the second. $`\square`$

Composition is explicit. For $`O\subseteq K_{\chi,\psi}`$,
$`P\subseteq K_{\psi,\omega}`$ and $`Q\subseteq K_{\chi,\omega}`$,
let $`n_Q`$ count middle vectors $`v`$ with $`(s,v)\in O`$ and
$`(v,t)\in P`$ for any $`(s,t)\in Q`$. Actor equivariance makes it
constant on $`Q`$, and it is zero if no such middle vector exists. Then

```math
 C_OC_P=\sum_Q n_Q\sqrt{\frac{|Q|}{|O||P|}}\,C_Q,
 \qquad C_O^*=C_{O^{\rm op}}.
 \tag{NI.29}
```

The middle-kernel equations imply the outer one, and matrix multiplication
counts the middle vectors. Identity is the sum over diagonal orbits with
coefficients $`\sqrt{|O|}`$. This is ordinary associative composition,
with matched source and target; it is not by itself a new analytic result.

Actual isomorphisms transport these spaces by
$`T\mapsto C_{F,\chi}TC_{F,\psi}^{-1}`$, and section changes by
the gauges of Section 5. Norms, dimensions, traces and ranks are preserved.

An essential boundary: these intertwiners need not intertwine left
translations. Indeed an invertible same-label intertwiner between
$`\pi_\chi`$ and $`\pi_\psi`$ forces $`\chi=\psi`$. Their traces
at $`(0,c)`$ are $`\chi(c)|\operatorname{Fix}R(c)|`$ and
$`\psi(c)|\operatorname{Fix}R(c)|`$, and the fixed-point factor is at
least one. Fusion avoids this obstruction by changing the target and
retaining the relative action. Theorem H is not the stronger, false claim
of equivalence of distinct character sectors with all translation labels fixed.

## 8. The actual defect measure and quantum coherence

### 8.1. Synchronized two-point spectrum

Now average actual pair defects, not uniformly over the generated group:

```math
 \mathsf A_{\chi,\psi}(T)
   =\mathbb E_{x,y}J_\chi(\ell_{x,y})T J_\psi(\ell_{x,y})^*.
 \tag{NI.30}
```

For a pair $`(s,t)`$, put $`w'=B_\nu s_W-B_\mu t_W`$ and
$`z_i'=\rho s_i-\tau t_i`$. Its diagonal actor-orbit characters are
$`(\alpha,\zeta)\in\mathbf F_p^k\oplus R_A`$, with
$`\alpha_i=0`$ if $`s_i=t_i=0`$ and $`\zeta=0`$ if $`s_W=t_W=0`$.

**Lemma Q1.** The exact eigenvalue at an allowed orbit character is

```math
 Q^{-r_\alpha}
  \left[m^{-2}+(1-m^{-2})
         \mathbf1_{\{w'\in\operatorname{im}B_\alpha\}}\right]
 q^{-2ka_\zeta}
 p^{-2\#\{i:z_i'\notin\zeta R_A^2\}}.
 \tag{NI.31}
```

In particular,

```math
 0\leq\mathsf A_{\chi,\psi},\qquad
 \|\mathsf A_{\chi,\psi}-\mathsf P_{\chi,\psi}\|_{{\rm HS}\to{\rm HS}}
       \leq p^{-2}.
 \tag{NI.32}
```

**Proof.** Vectorize $`|s\rangle\langle t|`$ in the sectors
$`\chi,\overline\psi`$. The full tensor correction has exactly their
synchronized phase and common dilation. Equivalently this is the residual
fusion of Theorem F with $`K=0`$. The inverse-defect Bol relation and
the bijection $`(x,y)\mapsto(y,x\circ y)`$ make (NI.30) self-adjoint.

Here is the full summation interface, extending AQ, Section 5. Choose the
orbit Fourier convention in which dilation by $`g`$ has eigenvalue
$`e_p(\alpha\cdot g_p)e_m(\zeta g_q)`$. Impose $`b(a,v)=g`$ using
the character of $`b(a,v)-g`$. Apart from its constant factor
$`e_p(-\alpha\cdot g_p)`$, the field exponent is exactly

```math
 \operatorname{Tr}\left(a_W^{\mathsf T}B_\alpha v_W
          +A_0a_W^{\mathsf T}w'+A_1v_W^{\mathsf T}w'\right),
 \qquad
 A_0=\lambda^{g_q}-\lambda^{e_q},\quad
 A_1=\lambda^{c_q+g_q}-1.
```

Averaging in $`v_W`$ imposes $`B_\alpha a_W=A_1w'`$. If
$`w'\in\operatorname{im}B_\alpha`$, solutions have density
$`Q^{-r_\alpha}`$ and the residual phase vanishes by alternation.
Otherwise solvability and averaging on the kernel require $`A_0=A_1=0`$.
Their independent actor coordinates give probability $`m^{-2}`$.
This includes $`\alpha=0`$ and proves the first factor in (NI.31).

On a ring plane the same averaging imposes $`\zeta a_i=A_1z_i'`$,
where actor differences are zero or units. If
$`z_i'\in\zeta R_A^2`$, the density is $`q^{-2a_\zeta}`$ and
the residual phase vanishes. Otherwise both actor differences must be zero,
with probability $`p^{-2}`$. The perfect ring pairing proves this also
for imprimitive $`\zeta`$. Multiplying and Fourier-inverting in $`g`$
gives (NI.31). The image and divisibility tests are constant on the pair
orbit, so this is convolution on exactly the stated actor quotient.

All eigenvalues are nonnegative. The eigenvalue-one space is exactly
$`K_{\chi,\psi}`$ with trivial orbit character, as in Theorem H.
If $`\alpha\ne0`$, even alternating rank is at least two, giving
$`Q^{-r_\alpha}\leq p^{-2}`$; if $`\zeta\ne0`$, the ring factor
is at most $`q^{-2k}<p^{-2}`$. At $`\alpha=\zeta=0`$, a failed
kernel condition gives either $`m^{-2}<p^{-2}`$ or a factor
$`p^{-2}`$. This proves (NI.32). $`\square`$

This extends the preceding spectrum to synchronized matrix sectors. The
analytic application uses its compatibility with actual translations, rather
than treating the extension alone as a new quantization theory.

### 8.2. Exact depolarization and a stronger coherence bound

Fix $`\chi`$, put $`\mathsf U_z=\operatorname{Ad}\pi_\chi(z)`$,
and define

```math
 \begin{split}
 \Phi_\chi
   &=\mathbb E_z\mathsf U_z^{-1}\mathsf A_{\chi,\chi}\mathsf U_z\\
   &=\mathbb E_{x,y,z}\operatorname{Ad}
       \bigl(\pi_\chi(z)^{-1}J_\chi(\ell_{x,y})\pi_\chi(z)\bigr),\\
 \mathcal D_\chi&=\mathbb E_{s\in[H,H]}\operatorname{Ad}J_\chi(s),
 \qquad \mathcal E(T)=\operatorname{Tr}(T)I/d.
 \end{split}                                                   \tag{NI.33}
```

These are intrinsic to the nucleus sector and transport under actual loop
isomorphisms with the character label. The first is unital, trace-preserving,
completely positive and mixed-unitary. Lemma Q1 also makes it self-adjoint
and positive as an operator on HS space.

**Theorem Q (quantum mixing and two-rate purity).** Suppose
$`D_\chi=\{0\}`$, equivalently $`B_\nu`$ is nondegenerate and
$`\rho`$ is a unit. Then $`\mathcal D_\chi`$ is intrinsic dephasing
onto rank-one joint shear eigenspaces, ordinary diagonal projection in the
point chart. For every integer $`t\geq1`$,

```math
 \|\Phi_\chi^t-\mathcal E\|_{{\rm HS}\to{\rm HS}}=\Lambda^t,
 \qquad
 \|\Phi_\chi^t(I-\mathcal D_\chi)\|_{{\rm HS}\to{\rm HS}}
       \leq p^{-2t},
 \tag{NI.34}
```

where $`\Lambda`$ is (NI.1), $`r_{\min}=\min_i r_i`$. Every density
matrix $`\varrho`$ satisfies

```math
 \boxed{\quad
 \|\Phi_\chi^t(\varrho)-I/d\|_{\rm HS}^2
 \leq\Lambda^{2t}\|\mathcal D_\chi\varrho-I/d\|_{\rm HS}^2
      +p^{-4t}\|\varrho-\mathcal D_\chi\varrho\|_{\rm HS}^2.
 \quad}                                                       \tag{NI.35}
```

The first rate is exact. The second is a bound, not a claimed exact
off-diagonal norm. The unique stationary density matrix is $`I/d`$.

**Proof.** Nondegeneracy makes shear characters at distinct point labels
distinct, so the intrinsic shear average is diagonal projection. Theorem H
gives $`K_{\chi,\chi}=\{(s,s):s\in U\}`$, and hence
$`\mathsf P_{\chi,\chi}`$ vanishes on off-diagonal matrices.
Every $`J`$ and $`\pi`$ is monomial, so diagonal and off-diagonal
subspaces are orthogonal invariant subspaces for each conjugation in
(NI.33). On the latter Lemma Q1 gives
$`0\leq\mathsf A_{\chi,\chi}\leq p^{-2}I`$. Averaging its unitary
conjugates gives the same bound for $`\Phi_\chi`$ there.

On diagonal matrices all phases cancel. The translation action becomes
$`u\mapsto a+R(c)u`$, the defect action $`u\mapsto R(b(a,v))u`$.
Therefore this restriction is exactly AQ's zero-nucleus-character
translated-defect operator. Its additive-frequency multiplier is

```math
 \kappa_{S(\xi_V)}\tau_A^{\mathbf1_{\{\xi_W\ne0\}}},\qquad
 \kappa_S=p^{-|S|}\sum_{\operatorname{supp}\alpha\subseteq S}Q^{-r_\alpha},
 \quad
 \tau_A=m^{-1}\left[1+\sum_{a=1}^A(q^a-q^{a-1})q^{-2ka}\right].
 \tag{NI.36}
```

Here $`S(\xi_V)`$ is the set of nonzero ring-plane frequencies.
Averaging the affine base point keeps a frequency precisely when the actor
fixes it; field and ring bilinear orthogonality then give (NI.36), as
proved in AQ, Section 6.3. The largest nonconstant multiplier is
$`\Lambda`$, attained on one ring plane of minimal $`r_i`$:
$`\kappa_{\{i\}}=p^{-1}+(1-p^{-1})Q^{-r_i}`$, simultaneous-zero
probabilities are no greater, and $`\tau_A<p^{-1}`$.

The two restrictions thus have norms $`\Lambda`$ and at most
$`p^{-2}<\Lambda`$. Positivity gives the exact powers and diagonal
extremizer. Squaring the two orthogonal components proves (NI.35).
Since $`\Lambda<1`$, only scalar matrices are fixed. $`\square`$

For an explicit infinite family take $`p=3,q=7,k=1`$,
$`E=\mathbf F_{3^{\operatorname{ord}_{7^A}(3)}}`$, $`W=E^{2h}`$,
standard symplectic $`B_1`$, and $`\chi=(1,1)`$. Then
$`d=Q^{2h}7^{2A}`$, $`\Lambda=1/3+(2/3)Q^{-2h}`$, and coherences
contract by at most $`1/9`$ per step for all $`h,A\geq1`$. A pure
state with uniform shear-basis populations satisfies

```math
 \operatorname{Tr}(\Phi_\chi^t(\varrho)^2)
       \leq d^{-1}+3^{-4t}(1-d^{-1}).
 \tag{NI.37}
```

Indeed the first term of (NI.35) vanishes and purity minus $`d^{-1}`$
is squared HS distance. More generally Cauchy--Schwarz gives
$`\|\Phi_\chi^t(\varrho)-I/d\|_1
 \leq\sqrt d\,\Lambda^t\|\varrho-I/d\|_{\rm HS}`$.
No dimension-free trace-distance bound is inferred.

### 8.3. Exceptional sectors are a real boundary

For $`D_\chi\ne0`$, universal depolarization is false. Choose nonzero
$`v\in D_\chi`$. Direct substitution gives
$`\pi_\chi(a,c)T_v\pi_\chi(a,c)^{-1}=T_{R(c)v}`$:
the possible phase is $`\chi(-b(a,v))=1`$. Thus the non-scalar orbit sum
$`\sum_{w\in R(Z)v}T_w`$ commutes with all $`\pi_\chi(x)`$ and
their defects and is fixed by $`\Phi_\chi`$. It has no diagonal entries,
so is not scalar. Its nonzero traceless Hermitian part gives, after a
sufficiently small real perturbation of $`I/d`$, a stationary density
matrix different from $`I/d`$. This includes the zero character.

The fusion, trace, Hom and two-point spectral theorems retain these sectors.
The off-radical matrix subspace, spanned by pairs with $`s-t\notin D_\chi`$,
still contracts by at most $`p^{-2}`$: the invariant projection vanishes
there, and the affine actions preserve that condition. We do not suppress
the remaining fixed algebra or apply Theorem Q without its hypothesis.

## 9. Worked matched-rank pencils and unmarked-loop distinction

Use the coupled families in the
[collective manuscript, Section 6A](bol-collective-cancellation.md#6a-coupled-pencils-and-an-exact-norm-on-all-mean-zero-inputs).
Here $`E=\mathbf F_{729}`$, $`Q=729`$, $`p=3,q=7,A=1`$,
$`k=2h+1,n=6h`$ for every $`h\geq1`$. To specify the actual forms, let
$`L_h=\mathbf F_{729^h}`$, $`M_h=\mathbf F_{729^{2h-1}}`$ and choose
injective $`\mathbf F_3`$-linear maps $`j_h:\mathbf F_3^k\to L_h`$,
$`i_h:\mathbf F_3^k\to M_h`$. For $`t=j_h(\nu)`$, set
$`z(t)=(t,t^3,t^9)`$ and

```math
 c_t(x,y)=\operatorname{Tr}_{L_h/E}\det[z(t),x,y].
```

The spread form is $`c_t\oplus c_t`$ on $`L_h^6`$. The aligned
form is the star matrix
$`S_\nu=\left(\begin{smallmatrix}0&\nu^{\mathsf T}\\-\nu&0\end{smallmatrix}\right)`$
on $`E^{k+1}`$, plus
$`\operatorname{Tr}_{M_h/E}(i_h(\nu)(xy'-yx'))`$ on $`M_h^2`$.
Both have dimension $`6h`$ over $`E`$. The injections can be made fully
uniform by choosing lexicographically first irreducible extension polynomials
and the first $`k`$ vectors of the induced $`\mathbf F_3`$-bases.

Determinant surjectivity and perfect trace pairing give radical $`L_hz(t)`$
for $`c_t`$. For nonzero $`\nu`$, the aligned star block has rank two
and its other block has rank $`4h-2`$. Common radicals are zero and the
parameter maps are injective, as in the cited construction. These are actual
admissible proper Bol loops, with $`r_\nu=4h`$ at every nonzero parameter.

If $`\nu,\mu`$ are $`\mathbf F_3`$-independent, the spread radical
lines are distinct: proportional $`z(s),z(t)`$ imply
$`s/t=(s/t)^3`$, hence $`s/t\in\mathbf F_3^\times`$. Their
intersection is zero in both copies. The aligned common radical is the
intersection of two independent star hyperplanes, of dimension
$`k-2=2h-1`$; the trace-symplectic block contributes none. Alternating
images annihilate radicals, so

```math
 r_{\nu,\mu}^{\rm sp}=6h,\qquad
 r_{\nu,\mu}^{\rm al}=4h+1.
 \tag{NI.38}
```

For pure $`p`$-characters $`\chi=(\nu,0),\psi=(\mu,0)`$:

| Quantity | Spread | Aligned |
| --- | --- | --- |
| Individual ranks $`r_\nu,r_\mu,r_{\nu+\mu}`$ | $`4h,4h,4h`$ | $`4h,4h,4h`$ |
| Joint shear projection trace | $`Q^{-6h}`$ | $`Q^{-(4h+1)}`$ |
| Decoupled sum trace | $`Q^{-4h}`$ | $`Q^{-4h}`$ |
| Forced field residual rank $`\delta`$ | $`2h`$ | $`1`$ |
| Full-defect Hom dimension | $`(Q^{6h}+6)7^{-1}((7^4+2)/3)^{2h+1}`$ | $`(Q^{8h-1}+6)7^{-1}((7^4+2)/3)^{2h+1}`$ |

The shear-trace ratio is exactly $`Q^{-(2h-1)}`$; the aligned-to-spread
Hom-dimension ratio is asymptotic to $`Q^{2h-1}`$. These quantify coupling
and trace sensitivity, not a better mixing norm for these degenerate sectors.
Theorem Q is separately realized by the nondegenerate family in Section 8.

Remove character labels by averaging (NI.23) over all ordered independent
pairs in the $`p`$-primary character subgroup of the intrinsic nucleus.
This set is nonempty and every such pair has the same value within each
family. Actual isomorphisms preserve the subgroup, independence, $`[H,H]`$
and the sector actions. The averages differ, proving the unmarked loops
nonisomorphic for every $`h\geq1`$. No isotopy or classification conclusion
is asserted. Nor is independence from every invariant of the full AQ spectrum
claimed: this is a distinct two-sector observable with an explicit evaluation.

## 10. Controls and contribution boundary

* **Scalarizing corrections.** The multiplicity dilation fails the scalar
  test (NI.15). Scalar corrections give identity conjugation channels;
  Theorem Q's strict coherence contraction disappears.
* **Forgetting sector correlations.** Independent shear averages give the
  different trace after (NI.25). Individual ranks cannot distinguish the
  matched families in Section 9.
* **Forgetting a section.** Retaining its induced gauge gives exact covariance
  (NI.18); dropping the relative gauge changes the fused operators. Theorem I
  reconstructs an intrinsic preferred section for this family.
* **Forgetting the selected measure.** The trace and Hom theorems retain only
  the intrinsic group and its sector action, not the frequency of individual
  defects. Theorem Q uses that frequency through (NI.31).
* **Rebracketing.** Tensor recouplings retain all residuals. Loop-label
  reassociation retains AQ.24's actual transport. The stronger Bol palindrome,
  not generic pentagon telescoping, provides the inverse-defect pairing.
* **Associative control.** In a group, every $`\ell_{x,y}=1`$, and the
  translated-defect channel is identity. This is sensitivity to the specified
  nonassociativity, not superiority to unrestricted group/quantum averaging.
* **Erasing one reciprocal action.** AQ, Section 7's retained-loop controls
  have nonconstant populations fixed by translated defects. Their diagonal
  matrices obstruct depolarization. These controls are outside the full
  faithful-action hypotheses.

Positivity also uses alternation, perfect pairings, unit actor differences,
and pencil independence. The Bol identity alone does not supply every estimate
for every Bol loop. Trace suppression is geometric sensitivity; the analytic
advantage actually proved is quantified contraction for the **specified**
matrix channel, with a separately faster coherence bound. Arbitrary
depolarizing channels and unrestricted uniform sampling have different goals.

## 11. Primary literature and remaining questions

[Gurevich--Hadani, GH-Q](../REFERENCES.md#gh-q), Theorem 2.2.3,
Propositions 2.3.1--2.3.2 and Section 2.4, supplies canonical normalized
Heisenberg intertwiners; Propositions 2.7.1, 2.7.3 and 2.7.5 treat tensor
products, duality and symplectic reduction. Those are established tools.
Section 2's incompatible symplectic equation explains why they do not simply
intertwine reciprocal actors without additional data. Our map is a finite
relative-coordinate transform retaining the Bol corrections, not a new Weil
representation.

[Smith, SMITH-QR](../REFERENCES.md#smith-qr), Section 4.2.4, printed
pages 26--27 and equations (4.8)--(4.12), treats quasigroup modules using
universal stabilizers and section corrections. Our $`H`$ is the actual
finite left-inner group, not that universal group. [Johnson--Smith,
JS-ACTION](../REFERENCES.md#js-action), Definition 7.1 and Theorem 6.1,
already studies Bol sandwich actions and stochastic representations. We do
not claim a first theory of loop representations.

[Bunk--Müller--Szabo, BMS-2REP](../REFERENCES.md#bms-2rep), Definitions
4.12 and 4.16 and Theorem 5.7 of the cited PDF, constructs genuine weak
category-valued actions through gerbe parallel transport. Remark 5.9 describes
a higher weak coboundary yielding bare associative pullbacks. This is a serious
alternative, not an automatic Bol estimate. The simpler Hilbert-space
construction here suffices; no new category is claimed.

[Ben-Aroya--Schwartz--Ta-Shma, BST-QE](../REFERENCES.md#bst-qe), Definitions
1.1--1.2, printed pages 48--49, gives the mixed-unitary and trace-zero HS
contraction framework, with efficient bounded-degree constructions elsewhere
in the paper. [Hastings, HASTINGS-QE](../REFERENCES.md#hastings-qe), opening
discussion and equations (1)--(2), pages 1--2, gives random-unitary quantum
expanders. Theorem Q evaluates
a particular loop-selected channel; averaging $`|\mathcal L|^3`$ triples
does not establish bounded degree or efficient implementation. No improvement
of general quantum-expander bounds is claimed.

The complete fusion criterion, residual repair, intrinsic trace and two-rate
channel estimate are proved under the stated hypotheses. This bounded source
comparison does not certify literature-wide priority. There is no new local
metaplectic cover, theta theory, automorphic identity, or arithmetic
cancellation theorem. PR #438's parameter-dependent fusion/connection problem
and the conductor action-equivariance question remain separate.

The next substantive problem is the exact translated channel on degenerate
sectors and its full stationary algebra, where joint radical geometry survives.
A bounded-degree approximation preserving the loop-selected estimates is
another question. Neither is required for the finite identities proved here.

## 12. Reproduction and review

The [code guide](../code/README.md#non-scalar-intertwiners-and-quantum-mixing)
specifies exact arithmetic, dependencies, finite scopes and commands.
Authored fusion and orbit checks reuse selected accepted implementations and
are not independent implementations. The authored quantum checker has its own
field/loop code; the reviewer check is separately identified and also imports
no authored checker. None enumerates the growing families' entire operator,
and no finite experiment is used to infer the uniform theorem.

The [review record](../evidence/bol-nonscalar-review.md) binds the actual
source, theorem scope, reviewer identity and reproducible evidence.
Proof status, independent model review, repository integrity, remote CI and
integration remain separate. Contributors are not credited as independent
reviewers of their own construction.

