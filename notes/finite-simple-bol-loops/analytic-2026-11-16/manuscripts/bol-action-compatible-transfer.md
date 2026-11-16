# Action-compatible arithmetic transfer for reciprocal Bol sections

Mira

There is an arithmetic correspondence preserving the actual reciprocal Bol
section and every non-scalar defect. It is obtained by restricting the upper
loop to an explicitly polarized subloop and taking an actual loop quotient.
The same quotient extends to its associative envelope. Induction from that
arithmetic subgroup gives a faithful representation of the entire upper
envelope, retaining every upper section and correction before compression.
All measures, adjoints, conductor extensions and multi-level compositions
are explicit. A maximal trace polarization further retains four of the seven
relative field coordinates in an adjacent step, with the same sharp estimate.

The analytic consequence goes beyond a transported estimate on the quotient.
Let $`C^S:L^2(S_{a,b})\to L^2(\mathcal L_a)`$ be normalized fiber averaging,
and let $`\mathcal M_S`$ and $`\mathcal M_a`$ average the actual
translation-conjugated defects in those loops. For every integer $`t\ge1`$,

```math
 \mathcal M_S^t=(C^S)^*\mathcal M_a^t C^S+\mathcal E_t,
 \qquad
 \|\mathcal E_t\|=
 \left(\frac13+\frac23|E_a|^{-r_{\min}}\right)^t.
```

Here $`\mathcal E_t`$ is precisely the restriction to the fiber-average-zero
subspace, extended by zero on its orthogonal complement. Thus the entire
information lost by this quotient has a sharp, conductor-gap-uniform decay
rate. It is not only the lower copied subspace that is controlled. The
proved rate uses the lower field size. It does not improve the known numerical
rate for the different walk averaging over the full upper loop.

## 1. Model, checkpoint, and tested alternatives

### 1.1. Fixed arithmetic data

Fix $`n,k\ge1`$ and alternating matrices $`B_1,\ldots,B_k`$ over
$`E_1=\mathbf F_{729}`$, independent over $`\mathbf F_3`$ and with zero
common radical. They are base-changed, not reselected, throughout the tower.
Put $`r_\nu=\operatorname{rank}_{E_1}\sum_i\nu_iB_i`$ and
$`r_i=r_{e_i}=\operatorname{rank}B_i`$, $`r_{\min}=\min_i r_i`$. No constant-rank hypothesis is needed.
Let

```math
 R_j=\mathbf Z/7^j\mathbf Z,\quad
 E_j=\mathbf F_{3^{6\cdot7^{j-1}}},\quad Q_j=|E_j|,
 \quad U_j=E_j^n\oplus R_j^{2k},\quad
 Z_j=\mathbf F_3^k\oplus R_j.
```

Choose compatible scalars $`\lambda_j`$ of order $`7^j`$ with
$`\lambda_{j+1}^7=\lambda_j`$, and the order-three units $`\eta_j`$
lifting $`2\bmod7`$. The character convention is
$`e_m(x)=\exp(2\pi ix/m)`$. Define

```math
 \begin{split}
 \beta_j(w,w')_i&=\operatorname{Tr}_{E_j/\mathbf F_3}
                       (w^{\mathsf T}B_iw'),\\
 \gamma_j(v,v')&=\sum_i(v_{i1}v'_{i2}-v_{i2}v'_{i1}),\\
 b_j&=\beta_j\oplus\gamma_j,\\
 R_j(\alpha,t)(w,(v_i)_i)&=(\lambda_j^t w,(\eta_j^{\alpha_i}v_i)_i),\\
 (u,c)\circ_j(v,e)&=(u+R_j(c)v,c+e-b_j(u,v)).
 \end{split}
```

The symbol $`R_j`$ for the action is distinguished by its argument from
the residue ring. All Hilbert spaces carry normalized counting measure.
Pushforward unitaries satisfy $`U_gf=f\circ g^{-1}`$.
The section and full correction in a nucleus character $`\chi`$ are

```math
 \pi_{j,\chi}(u,c)|v\rangle
  =\chi(c-b_j(u,v))|u+R_j(c)v\rangle,
 \qquad J_{j,\chi}(h,g)=D_gM_{\chi b_j(h,\cdot)}.
```

For $`x=(u,c),y=(v,e)`$, set
$`g=b_j(u,v)`$ and
$`h=R_j(g)u-R_j(e)u+R_j(c+g)v-v`$. Then
$`\pi(x)\pi(y)=\pi(x\circ y)J(h,g)`$.
The [intrinsic manuscript](bol-associator-quantization.md), Sections 1--4,
proves the Bol law, divisions, this formula and its phase convention directly.
The present proofs preserve those actual operators, rather than their average.

### 1.2. Exact baseline and new obligation

The checkpoint inspected is PR #440 delivery
`f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`, with intrinsic scientific pin
`5771bfccb6707606078baf93be804f810276b8eb`. The collective manuscript at that
delivery is unchanged from its accepted source
`ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`; the conductor correspondence
is separately accepted at `f85696062308e2b2511af8c73744766ec62a9dc8`.
The current overview and the entire intrinsic independent-review/handoff
record were inspected. Later, PR #440 advanced to
`848d6640a7bc555c9d2814665e7ac990fdfbeef5`, with separately reviewed
intrinsic spectral separation at `bb49ab24465ef82be78f2a0d9cb8d0af8caa2695`.
That continuation was inspected and incorporated additively; the associator,
collective and conductor sources used here are unchanged. Its new spectral
comparison is not an input to this transfer proof or re-reviewed here. The GitHub discussion and submitted-review lists were
empty; the actual signed model reviews reside in the evidence file.

Three statements must be distinguished. The intrinsic theorem already holds
separately at every conductor. The
[conductor manuscript](bol-conductor-correspondence.md), Theorem T and
Sections 3--8, already constructs coherent norm-one readout/Gram maps with
their stated filtrations and stabilization threshold. Neither asserts
intertwining of every $`\pi(x)`$ and every $`J(h,g)`$ across levels.
The new obligation is such an action-compatible arithmetic construction,
with explicit actor correspondence, full defect law and a quantitative
consequence. No existing result is relabeled as completing this stronger task.

### 1.3. The additive obstruction and its exact scope

Suppose an additive map $`F:E_{a+1}^n\to E_a^n`$ satisfies
$`F(\lambda_{a+1}x)=\lambda_aF(x)`$, as required by intertwining the
specified faithful scalar actions through reduction of the full ring center.
Iteration gives

```math
 F((\lambda_{a+1}^{7^a}-1)x)=0.
```

The scalar $`\lambda_{a+1}^{7^a}`$ has order seven and is not one.
Its difference from one is invertible on the entire upper vector space,
so $`F=0`$. Additivity, full-domain invertibility and the specified actor
reduction are the essential hypotheses. Calling $`F`$ a trace does not
change them. This argument excludes that architecture, not induction,
correspondences or operator-valued kernels.

The successful construction restricts the scalar exponent to the subgroup
$`7R_{a+1}`$ and divides that exponent by seven. In the ring determinant
it simultaneously scales one vector coordinate. These changes are necessary
parts of the relationship between the two actions.

| Architecture tested | Result and reason | Remaining scope |
|---|---|---|
| Additive map with full-center reduction | Zero by the displayed invertible-multiplier argument | Excludes this actor reduction only |
| Existing trace/readout or stabilized Gram correspondence | Valid prior theorem, but does not intertwine section and defects | Not the new result |
| Restriction to the arithmetic subloop and its quotient | Actual loop and envelope homomorphisms; every lower section and defect survives | Upper actors outside that subgroup require extra labels |
| Only a scalar-orbit label | Scalar powers are trackable, but arbitrary upper vector translations move out of those linear pieces | Full envelope cosets supply the missing affine information |
| Premature compression of all upper actions | Explicit excursion-return error of norm one in Section 5 | Fails for this compression; does not refute enlargement |
| Arithmetic envelope induction | Faithful homogeneous upper action, with explicit coset cocycle and conductor projectors | Lower compression has precisely stated actor support |
| Operator-valued kernels in the original charge sectors | Norm-one supported fiber kernels intertwine the full compatible section/defect family | Not a full-upper quotient representation |

For the scalar-label test, the union of the $`d`$ subspaces
$`\lambda_b^jE_a^n`$ has at most $`dQ_a^n`$ points, strictly fewer than
$`Q_b^n=Q_a^{dn}`$. A translation by a vector outside that union leaves
the proposed union. Thus retaining only those scalar labels is insufficient
for all upper translations; this does not exclude larger affine correspondences.
Here and below $`a<b`$, $`e=b-a`$, and $`d=7^e`$ unless a local
formula explicitly specifies a different dummy index.

## 2. The polarized subloop and its arithmetic quotient

Write `a<b`, `d=7^(b-a)`, `m=7^a`, `M=7^b=dm`, and
`Q=|E_a|`. The fixed matrices `B_i` are over `E_1`; use their scalar
extensions as in the conductor manuscript. The upper loop is `L_b`.
Inside it take

```math
 S_{a,b}=
 \{(w,((dx_i,y_i))_{i=1}^k,\alpha,dt):
 w\in E_a^n,\ x_i\in R_a,\ y_i\in R_b,
 \alpha\in\mathbf F_3^k,\ t\in R_a\}.
```

Multiplication of a lower residue by `d` is a well-defined injection
`R_a -> R_b`. Define

```math
 r_{a,b}(w,((dx_i,y_i)),\alpha,dt)
       =(w,((x_i,\bar y_i)),\alpha,t),
 \qquad \bar y_i=y_i\bmod m.
```

These are an actual subloop and a surjective loop homomorphism, not a
putative homomorphism between all of `L_b` and `L_a`.

To verify this directly, first note that
`lambda_b^(dt)=lambda_a^t`, `eta_b mod m=eta_a`, and
`Tr_(E_b/F3)|_(E_a)=d Tr_(E_a/F3)=Tr_(E_a/F3)`, since `7=1` in `F3`.
The upper ring determinant on mixed coordinates is

```math
 \gamma_b((dx,y),(dx',y'))
 =d\sum_i(x_i\bar y'_i-y_i\bmod m\,x'_i)
 =d\gamma_a((x,\bar y),(x',\bar y')).
```

Consequently the upper law stays in `S`, and each coordinate reduces
to the lower law. The explicit left/right division and inverse formulas
from AQ Section 2.1 also stay in `S`, so closure is not being substituted
for the full subloop claim. Its kernel is

```math
 K_{a,b}=\{(0,((0,mj_i)),0,0):j_i\in\mathbf Z/d\},
 \qquad |K_{a,b}|=d^k.
```

Every fiber has this cardinality. This kernel is generally not central:
the `F3` coordinate acts on its `i`th ring coordinate by `eta_b`.

For `a<b<c`,

```math
 r_{b,c}^{-1}(S_{a,b})=S_{a,c},\qquad
 r_{a,b}r_{b,c}=r_{a,c}\quad\hbox{on }S_{a,c}.
```

The first statement means preimage inside `S_(b,c)`. It follows by
checking the first ring coordinate and center divisibilities and the field
inclusion. This is the exact arithmetic coherence relation.


## 3. Normalized transfer, conductor sectors and composition

All Hilbert spaces use normalized counting measure. Let `C^S` be fiber
averaging from `L2(S)` to `L2(L_a)`:

```math
 (C^SF)(z)=d^{-k}\sum_{r(s)=z}F(s),\qquad
 ((C^S)^*f)(s)=f(r(s)).
```

Thus `C^S(C^S)^*=I`, `(C^S)^*C^S=P^S` is fiber conditional expectation,
and `||C^S||=1`. The exact kernel is the functions with zero average on
every fiber; its dimension is `(d^k-1)|L_a|`. This is a kernel carrying
nonconstant dynamics, not discarded constants.

The relative density of `S` in `L_b` is

```math
 \delta_{a,b}={|S_{a,b}|\over|L_b|}
       =\left({|E_a|\over|E_b|}\right)^n d^{-(k+1)}.
```

The normalized support embedding and its adjoint are

```math
 I_SF=\delta^{-1/2}\mathbf1_SF,
 \qquad I_S^*G=\delta^{1/2}G|_S.
```

Define the full ambient coisometry

```math
 C_{a,b}=C^S I_S^*,\qquad
 (C_{a,b}G)(z)={\sqrt\delta\over d^k}
                         \sum_{r(s)=z}G(s).
```

Its normalized integral kernel (integration against uniform `L_b`) is

```math
 \mathscr K_{a,b}(z,s)
   ={|L_a|\over\sqrt\delta}
          \mathbf1_{\{s\in S,\ r(s)=z\}}.
```

Its adjoint is

```math
 C_{a,b}^*f(s)=\delta^{-1/2}\mathbf1_S(s)f(r(s)).
```

Hence `CC*=I` and `C*C=P_(a,b)`, where `P` is zero off `S` and fiber
conditional expectation on `S`. The constant `c` in `C*C=cP` is exactly
one. The full kernel is the off-`S` subspace plus all zero-fiber-average
functions on `S`; its dimension is `|L_b|-|L_a|`.

It is important that `C 1=√δ 1`, rather than `1`. This ambient
coisometry is not mean preserving on arbitrary inputs. The internal
`C^S` is mean preserving. `C*` maps centered lower functions to centered
upper functions, because `E_(L_b) C*f=√δ E_(L_a)f`.

The densities multiply and the fibers disintegrate, so on the entire
upper ambient Hilbert space,

```math
 C_{a,b}C_{b,c}=C_{a,c},\qquad
 C_{b,c}^*C_{a,b}^*=C_{a,c}^*.
```

No dimension-dependent constant appears in the composition.

### Exact conductor labels and normalized aliasing matrix

The actual right nucleus of `S`, proved below, is its pure center,
identified with `Z_a=F3^k ⊕ R_a`. Restricting an upper nucleus character
to this subgroup gives

```math
 \chi^{(b)}_{\nu,\rho}(\alpha,dt)
    =\chi^{(a)}_{\nu,\sigma}(\alpha,t),
       \qquad \sigma=\rho\bmod m.
```

Each lower label has `d` upper extensions. If `σ!=0` with
`v_7(σ)=v<a`, every extension has valuation `v`; its conductor is
`7^(b-v)=d 7^(a-v)`. If `σ=0`, its extensions are `ρ=mj`, whose
conductors are `7^(b-a-v_7(j))` when `j!=0`; the `j=0` lift is
trivial. Thus primitive upper labels do survive and become primitive
lower labels. This is restriction to the subgroup `dR_b`, not quotient
equivariance for all upper central translations.

The vector support density is

```math
 \delta_v=(|E_a|/|E_b|)^n d^{-k},\qquad \delta=\delta_v/d.
```

Define the vector coisometry

```math
 (AF)(w,x,y_0)=\sqrt{\delta_v}\,
   \mathbb E_{j\in(\mathbf Z/d)^k}
                  F(w,dx,y_0+mj).
```

Here `w∈E_a^n`; `A` includes the indicated field/lattice support
restriction just as `C` does. Let `G_(ν,ρ)` be the normalized central
Fourier coefficients of `G` on `L_b`. Then the exact coefficient formula
is

```math
 (C G)_{\nu,\sigma}
      ={1\over\sqrt d}\sum_{\rho\equiv\sigma\pmod m}
                                      A G_{\nu,\rho}.
```

Thus the conductor multiplicity is the coisometric row
`d^(-1/2)(1,...,1)`. Its adjoint distributes a lower sector equally
among its `d` extensions using `A*`. The kernel includes cancellations
between these extensions as well as the explicit vector kernel. There
is no hidden `√d` amplification.


## 4. Compatibility with every section and full correction

For every `s∈S`, actual upper left translation preserves `S` bijectively
and permutes its fibers according to lower left translation by `r(s)`.
Consequently, with pushforward unitaries,

```math
 C U^{(b)}_{L_s}=U^{(a)}_{L_{r(s)}} C,
 \qquad U^{(b)}_{L_s}C^*=C^*U^{(a)}_{L_{r(s)}}.
```

The first identity holds on the entire upper Hilbert space because
`L_s` also preserves the complement of `S`. It follows by taking
adjoints, products, and inverses that it intertwines every word in
these translations, all `L_(s∘t)^(-1)L_sL_t`, the reassociation
transports, and the Bol palindromes. These are identities with actual
upper loop elements `s,t∈S`.

For the coordinate full defects, set the mixed vector module

```math
 T=E_a^n\oplus\bigoplus_{i=1}^k(R_a\oplus R_b),
 \quad \bar T=E_a^n\oplus R_a^{2k},\quad q:T\to\bar T.
```

In mixed coordinates, the center is `Z_a`. The action on `R_a⊕R_b`
is multiplication by `(eta_a^α,eta_b^α)`. Define

```math
 b_S(u,v)=b_a(q(u),q(v)).
```

Then `q R_S(c)=R_a(c) q` and `b_S=b_a(q,q)` literally. The formula
`h=R(g)u-R(d)u+R(c+g)v-v`, `g=b_S(u,v)` gives

```math
 q(h_S(x,y))=h_a(r(x),r(y)),\qquad g_S=g_a.
```

Therefore for all parameters, not only parameters occurring in a
particular averaged defect,

```math
 C^S_\chi J^S_\chi(h,g)
     =J^a_\chi(q(h),g)C^S_\chi,
 \quad
 J^S_\chi(h,g)=D_gM_{\chi b_S(h,\cdot)}.
```

The finite shears/dilations satisfy exactly
`H_(h,g)H_(h',g')=H_(h'+R(g')h,g+g')` and
`H_(h,g)^(-1)=H_(-R(-g)h,-g)`. Parameters `h` in `ker q` give the
same shear, so one must not claim parameter faithfulness here.


## 5. Retaining the entire upper action before compression

For this section write $`U_{ab}`$ for the upper vector lattice in
$`S_{a,b}`$, $`Z_{ab}=\mathbf F_3^k\oplus dR_b`$,
$`F_{ab}:U_{ab}\to U_a`$ for first-coordinate division and second-coordinate
reduction, and $`\zeta_{ab}:Z_{ab}\to Z_a`$ for ring-center division by
$`d`$. Thus $`q_{ab}=(F_{ab},\zeta_{ab})`$ is the same loop quotient
denoted $`r_{a,b}`$ above. Write $`K_{ab}=\ker F_{ab}`$.
The induction maps in this section are denoted $`C^{\rm ind}`$ and
$`i^{\rm ind}`$ when distinction from Section 3's ambient regular transfer
is needed; the displayed local formulas suppress that superscript.

### 5.1. The actual envelope and arithmetic group quotient

Let `G_j=N_j semidirect Z_j`, where `N_j=U_j plus U_j plus Z_j` has law

```math
 (X,Y,z)(X',Y',z')=
 (X+X',Y+Y',z+z'+\tfrac12[b_j(X,Y')+b_j(Y,X')]).
```

The action of `c in Z_j` on `N_j` is `(R_j(c),R_j(-c),1)`. Explicitly,

```math
 (X,Y,z;c)(X',Y',z';c')=
 \bigl(X+R(c)X',Y+R(-c)Y',
 z+z'+\tfrac12[b(X,R(-c)Y')+b(Y,R(c)X')];c+c'\bigr).
```

The folder stabilizer and actual section are

```math
 H_j=\{(X,0,c;c):X\in U_j,c\in Z_j\},\qquad
 \kappa_j(u,c)=(-R_j(-c)u,u,0;-c).
```

Identify right cosets `G_j/H_j` with `L_j` by
`(X,Y,z;c)H_j -> (Y,z-c+(1/2)b_j(X,Y))`. The action of a general
envelope element on these coordinates is

```math
 (X,Y,z;c):(u,e)\longmapsto
 \bigl(Y+R(-c)u, e+z-c+\tfrac12b(X,Y)+b(X,R(-c)u)\bigr).
```

Substituting `kappa_j(a,c)` gives exactly the loop left translation
`(u,e) -> (a+R(c)u,e+c-b(a,u))`.

This action of `G_j` on `L_j` is faithful: the vector coordinate forces
`Y=0` and `R(c)=I`; faithfulness of `R` forces `c=0`; the remaining
center displacement is `z+b(X,u)`, so its vanishing for all `u` gives
`X=0,z=0` by the zero common radical and perfect ring pairing.
Therefore every identity between these actual permutations is an identity
of the corresponding envelope elements. In particular, the Bol palindrome,
inverses, and defect inverse pairing hold in `G_j` itself and hence in all
its unitary representations:

```math
 \kappa(x)\kappa(y)\kappa(x)=\kappa(x\circ(y\circ x)),\qquad
 \kappa(x)^{-1}=\kappa(x^{-1}).
```

For `h,g` in the intrinsic defect coordinates of AQ.12, the exact envelope
element is

```math
 d_j(h,g)=(R_j(-g)h,0,-g;-g)\in H_j.
```

Its action on the loop is `(w,e)->(R_j(g)w,e+b_j(h,w))`; in charge `chi`
it is precisely `J_chi(h,g)=D_g M_{chi b(h,.)}`. Thus the group defect
`kappa(x circ y)^(-1) kappa(x) kappa(y)` is this full non-scalar correction.

Define the arithmetic subgroup

```math
 G_{ab}=\{(X,Y,z;c):X,Y\in U_{ab},\ z,c\in Z_{ab}\}\subset G_b.
```

Apply `F_ab` to both vector axes and `zeta_ab` to both center coordinates.
The compatibility identities are, for $`u,v\in U_{ab}`$ and $`c\in Z_{ab}`$,

```math
 \zeta_{ab}b_b(u,v)=b_a(F_{ab}u,F_{ab}v),\qquad
 F_{ab}R_b(c)u=R_a(\zeta_{ab}c)F_{ab}u.
```

The resulting map `Phi_ab:G_ab -> G_a` is a surjective group homomorphism
by these identities. Its kernel is two copies
of `K_ab`, of size $`d^{2k}=7^{2ke}`$. It sends the actual section, products,
inverses, and defects exactly:

```math
 \Phi_{ab}(\kappa_b(s))=\kappa_a(q_{ab}s),\qquad
 \Phi_{ab}(d_b(h,g))=d_a(F_{ab}h,\zeta_{ab}g)
```

for `s in S_ab`, `h in U_ab`, `g in Z_ab`. It maps
`H_b intersect G_ab` onto `H_a`.

### 5.2. A faithful enlarged homogeneous space

Let

```math
 H'_{ab}=\Phi_{ab}^{-1}(H_a)
       =\{(X,Y,c;c):X\in U_{ab},Y\in K_{ab},c\in Z_{ab}\}.
```

This formula follows from the injectivity of `zeta_ab` on `Z_ab` and
`F_ab(Y)=0`. In particular, `b_b(X,Y)=0` for the displayed `X,Y`, because
the first ring coordinate of `X` is divisible by `d` and the second
coordinate of `Y` is divisible by `7^a`, and `a+e=b`.

The enlarged output is

```math
 \Omega_{ab}=G_b/H'_{ab},\qquad \mathscr H_{ab}=L^2(\Omega_{ab})
```

with normalized counting measure and the actual left action of `G_b`.
It is the induced module

```math
 \operatorname{Ind}_{G_{ab}}^{G_b}
   \bigl(\Phi_{ab}^{*} L^2(G_a/H_a)\bigr).
```

This is an arithmetic homogeneous space, not a product with an unrelated
lower system. It carries every upper section element `kappa_b(x)` and
every full upper defect `d_b(h,g)`, including those outside `G_ab`.

The action of `G_b` on `Omega_ab` is faithful. To prove this, let `D` be
the core of `H'_ab` in `G_b`. The center of `N_b` is exactly its `Z_b`
axis, by nondegeneracy of the doubled alternating form. Its intersection
with `H'_ab` is trivial. If `n in D intersect N_b`, then its commutator
with any `N_b` element lies in `D intersect Z(N_b)=1`; therefore `n` is
central and is trivial. For any `g in D`, commutators `[g,N_b]` lie in
`D intersect N_b=1`. Thus `g` centralizes `N_b`. Its action on
`N_b/Z(N_b)` is `(R(c),R(-c))`, forcing `c=0`. It follows that `g in N_b`
and `g=1`. This proves faithfulness. In this permutation representation,
every nonidentity upper defect acts nonscalarly: a scalar permutation
matrix must be the identity.

### 5.3. Explicit normalized induction and readout

Let `T=G_b/G_ab`, choose representatives `tau_t`, and let `t0=G_ab` with
`tau_t0=1`. Write `I=|T|`. In fiber coordinates the Hilbert space is
`L^2(T;L^2(L_a))`, with normalized counting on `T`. If

```math
 g\tau_t=\tau_{t'}h,\qquad h\in G_{ab},
```

then the induced action sends the `t` fiber to the `t'` fiber using
`U_a(Phi_ab(h))`. This explicit coset cocycle satisfies the group law
because the factorization is unique; its inverse is obtained by the same
factorization for `g^{-1}`. Section multiplication therefore has exactly
the defect `rho(d_b(h,g))`, not a scalar substitute. The Bol identities
follow from their envelope identities in Section 5.1.

Put

```math
 (i_{ab}f)_t=\sqrt I\,\mathbf1_{t=t_0}f,\qquad
 C_{ab}F=I^{-1/2}F_{t_0}.
```

These are adjoints, $`C i=\operatorname{Id}`$, and `i C` is exactly the orthogonal projection
onto the base fiber. Both have norm one. The kernel of `C` is the space
of all vectors whose base-fiber coordinate is zero, of dimension
$`(I-1)|\mathcal L_a|`$. With integration against normalized counting on
$`T\times\mathcal L_a`$, its integral kernel is

```math
 \mathscr K^{\rm ind}(x;(t,y))
 =\sqrt I\,|\mathcal L_a|\,\mathbf1_{t=t_0}\mathbf1_{y=x}.
```

In particular $`(C^{\rm ind})^*C^{\rm ind}`$ is precisely the base-fiber
projection with scalar coefficient one. The normalization is

```math
 I=[G_b:G_{ab}]
   =\left(\frac{|L_b|}{|S_{ab}|}\right)^2
   =\left(\frac{|E_b|^n}{|E_a|^n}7^{(k+1)e}\right)^2.
```

For every `h in G_ab`,

```math
 C_{ab}\rho_b(h)=U_a(\Phi_{ab}h)C_{ab},\qquad
 \rho_b(h)i_{ab}=i_{ab}U_a(\Phi_{ab}h).
```

For every `g in G_b`, including arbitrary upper words,

```math
 C_{ab}\rho_b(g)i_{ab}=
 \begin{cases}U_a(\Phi_{ab}g),&g\in G_{ab},\\0,&g\notin G_{ab}.
 \end{cases}
```

The zero in the second line is the effect of **compression**. The full
upper action is retained in the other induced fibers.

For an arbitrary weighted word sum `T_b=sum_w alpha_w rho_b(w)` with
`w in G_ab`, let `T_a=sum_w alpha_w U_a(Phi_ab(w))`. Then exactly

```math
 T_b i_{ab}=i_{ab}T_a,\qquad C_{ab}T_b i_{ab}=T_a,
 \qquad i_{ab}^*T_b^*T_b i_{ab}=T_a^*T_a.
```

This gives readout and Gram identities for every such word operator,
not only an averaged associator. Scalar matrix coefficients are equal
without a normalization loss.

### 5.4. Every conductor, including zero charge

The center `Z(N_b)=Z_b` intersects `G_ab` in `Z_ab`. Suppose the lower
sector is `chi_a=(nu,rho)` with `rho in R_a`. Its pulled-back center
character has exactly `7^e` upper extensions:

```math
 \chi_b=(\nu,\rho'),\qquad \rho'\equiv\rho\pmod{7^a}.
```

The ambient upper center moves the base fiber through `7^e` disjoint
fibers. If `P_chi_b` is its orthogonal character projector, then

```math
 \|P_{\chi_b}i_{ab}f\|^2=7^{-e}\|f\|^2
```

for every compatible extension, and the projection vanishes for all
incompatible characters. This follows directly by expanding
`P_chi_b=E_z conjugate(chi_b(z)) rho_b(z)` and observing that a central
element can return to the base fiber only when it lies in `Z_ab`.

Consequently

```math
 i_{ab,\chi_b}=7^{e/2}P_{\chi_b}i_{ab},\qquad
 C_{ab,\chi_b}=i_{ab,\chi_b}^*
```

are respectively an isometry and coisometry. All the subgroup, section,
full-defect, word-readout and Gram identities above hold in this selected
upper charge. The written `7^{e/2}` is exactly canceled by the projection
norm; the transfer operator still has norm one. Equivalently this
constituent is induction from `G_ab Z_b`, extending the pulled-back lower
representation by the chosen upper center character.

For this **selected-charge** corner, the outside-subgroup support criterion
changes from `G_ab` to `G_ab Z_b`. More precisely,

```math
 C_{ab,\chi_b}\rho_b(hz)i_{ab,\chi_b}
   =\chi_b(z)U_a(\Phi_{ab}h)\quad(h\in G_{ab},z\in Z_b),
```

and this corner is zero for `g outside G_ab Z_b`. The formula is
well-defined because the two characters agree on the intersection.
The unprojected corner's `G_ab` support statement must not be copied
unchanged after charge projection.

If `rho!=0` has conductor exponent `a-v_7(rho)`, every upper extension
has conductor exponent `b-v_7(rho)`, an increase of `e`. If `rho=0`, the
extensions have labels `7^a j` for `j mod7^e`; their conductor exponents
are `e-v_7(j)`, with zero character convention `v_7(0)=e`. For an adjacent
step, lower zero charge has one upper zero extension and six extensions
of conductor seven. No sector is silently discarded.

### 5.5. Induction in stages

For `a<c<b`,

```math
 G_{ab}=\Phi_{cb}^{-1}(G_{ac})\subset G_{cb},\qquad
 \Phi_{ab}=\Phi_{ac}\Phi_{cb}\quad\hbox{on }G_{ab}.
```

The first identity follows coordinate by coordinate: first ring axes
must acquire the additional factor `7^{c-a}`, the second axes remain
unrestricted, and the field axes must lie in `E_a`. It includes the
kernel of `Phi_cb`. Thus induction in stages, proved directly by
factoring the same coset representatives in two stages, gives a canonical
unitary equivalence

```math
 \operatorname{Ind}_{G_{cb}}^{G_b}\Phi_{cb}^*
 \left(\operatorname{Ind}_{G_{ac}}^{G_c}\Phi_{ac}^*V\right)
 \simeq \operatorname{Ind}_{G_{ab}}^{G_b}\Phi_{ab}^*V.
```

The indices multiply and normalized counting therefore introduces no
factor. The base-fiber inclusions and coisometries compose exactly.
After sector decomposition, an upper label `rho_b` chooses the unique
intermediate reduction `rho_c=rho_b mod7^c`; compatible conductor paths
are preserved. This functorial statement does not identify the induced
representation of `G_c` with the original `L^2(L_c)` representation.

### 5.6. Original charge sectors and the excursion obstruction

There is also a smaller transfer directly inside the *original* upper
regular charge sector. Let

```math
 \delta_U=|U_{ab}|/|U_b|
          =( |E_a|/|E_b|)^n d^{-k}=( |E_a|/|E_b|)^n7^{-ke}.
```

For compatible `chi_a,chi_b` define, on normalized coordinate Hilbert
spaces,

```math
 I_{ab,\chi_b}f(u)=\delta_U^{-1/2}\mathbf1_{U_{ab}}(u)f(F_{ab}u),
```

```math
 (C_{ab,\chi_b}F)(u_0)
   =\sqrt{\delta_U}\,\mathbb E_{u\in F_{ab}^{-1}(u_0)}F(u).
```

These are adjoints, `CI=Id`, and `IC` projects onto supported,
fiber-constant functions. Their norms are one. They intertwine every
actual section `s in S_ab`, and every full `J_b(h,g)` with
`h in U_ab,g in Z_ab`, by the explicit phase formula AQ.17/AQ.21.
The ring phase is constant on the fibers because `K_ab` is radical for
the restricted form. The formulas compose exactly in several levels.

They cannot make full upper section multiplication descend. For
`t in R_b` not divisible by `d`, `lambda_b^t notin E_a`; hence
`lambda_b^t E_a^n intersect E_a^n={0}`. For the actual pure scalar
section `s_t=(0,(0,t))`,

```math
 C\pi_{b,\chi_b}(s_t)I=\chi_b(0,t)P_{w=0}.
```

Here `P_{w=0}` is the orthogonal projection onto functions supported
at the zero field vector, with all ring coordinates retained. Therefore

```math
 (C\pi(s_{-t})I)(C\pi(s_t)I)=P_{w=0},\qquad
 C\pi(s_{-t})\pi(s_t)I=\operatorname{Id}.
```

The lost excursion-return operator is `Id-P_{w=0}`, of norm one. This is
an exact obstruction for this compression architecture, not a no-go for
induction. The enlarged homogeneous model above retains the missing
scalar-orbit/coset labels and preserves all upper multiplication exactly.


## 6. Complete mixed-module associator spectrum

Define

```math
 \mathcal A_S=\mathbb E_{x,y\in S}
 U_{L_{x\circ y}^{-1}L_xL_y},\qquad
 P_S=\text{orthogonal projection onto the common fixed space of these defects}.
```

This is the useful analytic extension: the intrinsic `A_S` and globally
translated `M_S` formed from uniform actual `S` elements have the same
sharp gap constants as `L_a`, including all extra fiber modes. It is
not a claim that the original AQ hypotheses directly include `S`:
`b_S` has a nonzero vector radical. The following calculation treats it.

### Defect group and right nucleus

The same division calculation gives `ell_(x,y)=H_(h,g)` on `S`.
Choose `c` with ring component `1` and every `F3` component `1`.
Then `I-R_S(c)` is invertible on `T`: `1-lambda_a` is nonzero,
and both `1-eta_a` and `1-eta_b` are units. Pairs `(u,0),(0,c)`
therefore generate all shears `H_(h,0)`. The values of `b_S` generate
`Z_a` by the original pencil independence and ring determinant argument,
since `q` is onto. Removing shears from defects then gives every
dilation `H_(0,g)`.

Hence the full intrinsic group consists of these shear/dilation
permutations, with `h` understood modulo the vector radical. Its orbit is

```math
 R_S(Z_a)z\times(e+b_S(T,z)).
```

A right-nuclear `(z,e)` is fixed by every actual defect, hence by every
`H_(0,g)`. The independent scalar actions force `z=0`: they have no
nonzero common fixed vector even in `ker q`. Conversely `(0,e)` is
right nuclear directly from the law. Thus

```math
 N_r(S)=\{0\}\times Z_a.
```

### Orbit labels and formula

Fix a nucleus character `χ=(ν,ρ)`, a vector
`z=(w,z_1,...,z_k)∈T`, with `z_i=(x_i,y_i)∈R_a⊕R_b`, and write
`bar z_i=(x_i,y_i mod m)∈R_a²`. The actual vector orbit has an
`m`-cycle if `w!=0` and a `3`-cycle for each **actual** `z_i!=0`.
Consequently its Fourier labels are

```math
 (\alpha,\sigma)\in\mathbf F_3^k\oplus R_a,
 \quad \alpha_i=0\ \hbox{if }z_i=0,
 \quad \sigma=0\ \hbox{if }w=0.
```

An actual plane can be nonzero while its reduced plane is zero; these
additional orbit labels are precisely where a careless quotient argument
would lose information.

Set `c_σ=a-v_7(σ)`, with `v_7(0)=a`, and

```math
 t_\alpha(w,\nu)=Q^{-r_\alpha}
  \left[m^{-2}+(1-m^{-2})
    \mathbf1_{\{B_\nu w\in\operatorname{im}B_\alpha\}}\right],
```
```math
 j_{\rho,\sigma}(\bar z)
   =\#\{i:\rho\bar z_i\notin\sigma R_a^2\},\qquad
 s_\sigma(\bar z,\rho)
    =7^{-2k c_\sigma}3^{-2j_{\rho,\sigma}(\bar z)}.
```

Then the full `A_S` eigenvalue at this allowed orbit character is

```math
             t_\alpha(w,\nu)s_\sigma(\bar z,\rho).
```

The formula uses actual support to decide allowed labels and reduced
support to decide the phase tests. Both roles are indispensable.

### Proof of the formula, including the new radical

The Bol identity, inherited as an actual subloop identity, proves
inversion symmetry of the defect distribution, so compute its pullback.
Balancedness gives

```math
 b_S(h,z)=b_S(u,(R_S(g)-R_S(d))z)
             +b_S(v,(R_S(c+g)-I)z).
```

Insert Fourier orthogonality for `b_S(u,v)=g`. The field integral is
exactly AQ.31 with `B_α`, `-B_νw`, and scalar coefficients
`lambda_a^(g_t)-lambda_a^(d_t)` and `lambda_a^(c_t+g_t)-1`.
It is `Q^(-r_α)` on the image incidence; off that incidence both
coefficients must vanish, with probability `m^(-2)`. This gives `t_α`.

Every ring phase and the equation `b_S(u,v)=g` depend only on the
uniform reductions of each `u_i,v_i∈R_a⊕R_b` to `R_a²`. Every
fiber of those reductions has cardinality `d`. Normalized integration
therefore removes that fiber with factor exactly one. The remaining
ring integral is literally

```math
 \mathbb E_{u_i,v_i\in R_a^2}
 e_m\{\sigma\gamma(u_i,v_i)
  -\rho[A\gamma(u_i,\bar z_i)
                   +A'\gamma(v_i,\bar z_i)]\},
```

where `A=eta_a^(g_i)-eta_a^(d_i)` and
`A'=eta_a^(c_i+g_i)-1` are zero or units. Averaging `v_i` forces
`σu_i=-A'ρ bar z_i`. If `ρ bar z_i∈σR_a²`, the solution density
is `7^(-2c_σ)` and the remaining phase vanishes by alternation. If
not, only `A=A'=0` survives; their independent actor probability is
`1/9`. Multiplying these factors gives `s_σ`.

The coefficient of dilation by `g` is thus

```math
 {1\over|Z_a|}\sum_{\alpha,\sigma}
 e_3(-\alpha\cdot g_p)e_m(-\sigma g_t)
                  t_\alpha(w,\nu)s_\sigma(\bar z,\rho).
```

It is unchanged on the actual orbit, because multiplying actual vectors
by the scalar units multiplies their reductions by the corresponding
lower units. Fourier inversion on the actual orbit proves the asserted
formula with its full additional labels.

### Inner invariant projection and intrinsic norm

The character annihilates all shears precisely if

```math
 B_\nu w=0,\qquad \rho\bar z_i=0\quad(1\le i\le k).
```

If these hold, `P_S` is uniform averaging on the actual vector orbit;
otherwise it vanishes on this sector/orbit. These are exactly the
eigenvalue-one spaces. Every other eigenvalue is in `[0,1/9]`:
`α!=0` gives `r_α≥2` and `t_α≤Q^(-2)≤1/9`; `σ!=0` gives
`s_σ≤7^(-2k)<1/9`; for `α=σ=0` outside the shear annihilator,
either `t_0=m^(-2)<1/9` or `s_0≤1/9`.

Equality `1/9` occurs by taking `w=0`, a ring vector whose reduction
has one primitive nonzero plane, `ρ` a unit, and trivial orbit label.
Consequently

```math
 0\le A_S\le\tfrac19 I+\tfrac89 P_S,\qquad
 \|A_S^t-P_S\|=9^{-t}\quad(t\ge1).
```


## 7. Sharp spectral transport and control of the quotient kernel

Let

```math
 M_S=\mathbb E_{x,y,z\in S}
 U_{L_z}^{*}U_{L_{x\circ y}}^{*}U_{L_x}U_{L_y}U_{L_z}.
```

It is the original constrained global associator measure, now on the
actual mixed subloop. It is positive by the previous spectral formula.

For a nucleus character `χ=(ν,ρ)`, the scalar radical in `T` is

```math
 D_\chi=\{(w,z_i):B_\nu w=0,\ \rho\bar z_i=0\ (1\le i\le k)\}.
```

Let `c_ρ=a-v_7(ρ)`. Its density is exactly

```math
 d_\chi={|D_\chi|\over|T|}=Q^{-r_\nu}7^{-2k c_\rho}.
```

The extra ring fibers lie in the radical in both numerator and
denominator and cancel. The radical need not be zero, even for
nondegenerate lower scalar forms.

Define `B_S=E_z U_(L_z)^* P_S U_(L_z)` (a different letter from the
transfer `C`). In sector `χ`, the direct phase computation of AQ.34
uses only balancedness and `R`-invariance of the scalar radical and
gives

```math
 (B_S)_\chi f(x)=d_\chi
   \mathbb E_{v\in D_\chi}\mathbb E_{c\in Z_a}
             f(x+(R_S(c)-I)v).
```

For completeness the phase vanishes as follows. In the conjugated
projection the intermediate vector is `y=u+R_S(d)x∈D_χ`; a dilation
returns it to `x'=x+R_S(-d)(R_S(c)-I)y`. The difference lies in
`D_χ`, so the product of the two section phases,
`χ(b_S(u,x'-x))`, equals one. Uniform `u` makes
`v=R_S(-d)y` uniform, and restricting to the radical gives density
`d_χ`. This proves the formula on the full mixed module.

Hence `||(B_S)_χ||=d_χ`. For `χ!=0`, this is at most `1/9`, and

```math
 \|(M_S)_\chi\|
 \le\tfrac19+\tfrac89 d_\chi
 \le\tfrac{17}{81}<\tfrac13.
```

In the zero-nucleus-character sector, all additive vector characters
diagonalize `M_S`. If `ξ` is a character of `T`, let `I(ξ)` be the
indices of the planes on which its mixed-module character is nontrivial.
Then the exact multiplier is

```math
 \kappa_{I(\xi)}\tau_a^{\mathbf1_{\{\xi_W\ne0\}}},
```
```math
 \kappa_I=3^{-|I|}
 \sum_{\operatorname{supp}\alpha\subseteq I}Q^{-r_\alpha},
 \quad
 \tau_a={1\over7^a}
   \left[1+\sum_{c=1}^a(7^c-7^{c-1})7^{-2kc}\right].
```

Indeed, affine conjugation kills an additive frequency unless the
defect dilation fixes it. On `E_a^n` a nonzero character has trivial
stabilizer under `lambda_a`; on a mixed ring plane a nonzero character
has trivial stabilizer under the order-three action because every
nontrivial `eta-1` difference is a unit on **both** ring coordinates.
The conditions are therefore `β_i=0` for `i∈I` and, if `ξ_W!=0`,
`γ_a=0`. These random variables separate. The displayed finite Fourier
formulas follow from the field bilinear sum and the uniformly reduced
ring determinants.

For nonempty `I`, its probability is bounded by each singleton and

```math
 \kappa_{\{i\}}=\tfrac13+\tfrac23 Q^{-r_i}.
```

For empty `I` and nonzero `ξ_W`,
`τ_a≤1/7+(6/7)7^(-2k)<1/3`. Thus, writing
`r_min=min_i r_i`,

```math
 \Lambda_a=\tfrac13+\tfrac23Q^{-r_{\min}},\qquad
 \|M_S^t-\Pi_S\|=\Lambda_a^t\quad(t\ge1).
```

Equality is attained by a character supported in one mixed ring plane
of minimum `r_i`, with zero field and nucleus frequencies.

### The kernel is controlled with the same exact constant

Since `C^S M_S=M_a C^S` and both operators are self-adjoint,
`L2(S)=ran((C^S)^*)⊕ker C^S` is a reducing decomposition. The first
summand is unitarily equivalent to the entire lower operator `M_a`.
The second is the genuine extra fiber information. For `b>a`, choose
a minimal-rank plane `i` and the character

```math
                  f(w,x,y,\alpha,t)=e_{7^b}(y_i).
```

Its average over a fiber `y_i=y_{i,0}+7^a j` is zero, since `d>1`.
Thus it lies in `ker C^S`. It is an exact `M_S` eigenvector with
eigenvalue `κ_{\{i\}}=Λ_a`. Therefore

```math
 \boxed{\ \|M_S|_{\ker C^S}\|=\Lambda_a,\qquad
       \|M_S^t|_{\ker C^S}\|=\Lambda_a^t.\ }
```

The same rate consequently controls the lower transported modes and
every discarded fiber mode, without norm inflation. This is stronger
than merely pulling back a lower estimate to the fiber-constant code.

### Main quantitative transfer identity and sharp correlation remainder

Here work internally with `C=C^S` and `P=C*C` on `L2(S)`, to avoid
confusing the fiber projection with the intrinsic invariant projection.
Intertwining and self-adjointness make `P` commute with `M_S`. Thus
for every integer `t≥1`,

```math
 \boxed{\quad M_S^t=C^*M_a^t C+R_t,\qquad
 R_t=(I-P)M_S^t(I-P),\qquad \|R_t\|=\Lambda_a^t.\quad}
```

Equivalently, for all `f,g∈L2(S)` (centering is unnecessary here),

```math
 \left|\langle M_S^tf,g\rangle
             -\langle M_a^tCf,Cg\rangle\right|
 \le\Lambda_a^t\|(I-P)f\|_2\|(I-P)g\|_2.
```

The constant is sharp for each `t`, using the same minimal-rank
pure-fiber additive character on both sides. This is an exact spectral
splitting into transported lower dynamics and a quantitatively controlled
remainder consisting **precisely** of the information lost by transfer.
Its bound is independent of `b-a`; it is not inferred merely from a
coisometric readout or from a separate lower-level norm estimate.

For every centered `f,g∈L2(S)`,

```math
 |\langle M_S^t f,g\rangle|
       \le\Lambda_a^t\|f\|_2\|g\|_2.
```

The translated defect energy has sharp coercivity

```math
 2(1-\Lambda_a)\|f-\Pi_Sf\|_2^2
 \le\mathbb E_{x,y,z\in S}
 \|U_{L_x}U_{L_y}U_{L_z}f-U_{L_{x\circ y}}U_{L_z}f\|_2^2
 \le2\|f-\Pi_Sf\|_2^2.
```

These constants are independent of `b-a`. They retain `Q_a`, not
`Q_b`: no claim is made of the stronger large-field rate for the full
upper loop `L_b`. Since `Q_a≥729` and `r_min≥2`, they have the
conductor-uniform upper bound
`Λ_a≤1/3+2/(3·729²)`. The sharp rate tends to `1/3` as `a` grows.


## 8. Exact reciprocal readouts and Gram relations

For any finite linear combination `T_a` of actual section/defect
words at level `a`, choose arbitrary lifts of its actor labels into
`S`. Let `T_b^S` be the identical linear combination of upper words.
Then

```math
 T_b^S C^*=C^*T_a,
 \qquad C T_b^S C^*=T_a,
 \qquad C(T_b^S)^*T_b^S C^*=T_a^*T_a.
```

The first equality holds wordwise, including inverse and correction
operators; it implies the Gram identity without a separate polar
choice. Independence of arbitrary lifts holds on the `C*` code,
not necessarily on the extra fiber modes. Averaging actors uniformly
in `S` pushes forward to uniform actors in `L_a` and is therefore a
canonical lift for the averaged intrinsic and global operators.

For the earlier marked reciprocal readout there is also a literal
arithmetic formula. Use the actual upper marks `(d,0)` and `(0,1)`
in each ring plane, central argument `ds`, field inputs `u,y∈E_a^n`,
and the original `e∈E_1^n`. The displacement of its fixed
parenthesized word is

```math
 \lambda_b^{d(s-F_a(u,\alpha,y))}e
       =\lambda_a^{s-F_a(u,\alpha,y)}e.
```

The upper absolute field character restricted to this displacement is
the lower one, because the extension degree is `1` in `F3`. With
normalized averages over these subloop input/output parameters, the
readout is **exactly** $`\mathcal R_a`$, and its Gram and sharp collective norm
are unchanged. This is a full-action realization of that arithmetic
word, whereas the previous conductor manuscript only had function-space
correspondences for its original marks.

The marks and domain have changed at the upper level: the original
upper mark `(1,0)` lies outside the subloop, and the unrestricted
upper input field is not being averaged. If one instead uses the
original normalized average over `E_b^n` and a normalized support
embedding of a lower input, the amplitude acquires the square root
of the field density. It would be incorrect to hide that factor or
describe this as the old full-upper readout without modification.

## 9. Analytic scope of the full induced module


Average actual defects and their translated conjugates over `s,t,z in S_ab`
with normalized counting. On the base-fiber image and its charge-projected copies, these operators
are exactly the lower `A_a,M_a`, because `q_ab` is surjective with equal
fiber size. Therefore all lower word Gram identities, the norm `1/9`
off local invariants, and the global lower-centered norm

```math
 \Lambda_a=\tfrac13+\tfrac23|E_a|^{-r_{\min}}
```

transport without loss, in each compatible upper conductor constituent,
and their powers have the same exact norms. In particular the uniform
upper bound `Lambda_1<1` holds along every tower on the transported
lower-centered spaces. This adds an actual action-compatible transport,
not a stronger numerical estimate than the separate lower theorem.

Do not extend this to global mean zero on the entire induced space.
Take lower charge zero and its lower constant vector. A nonzero upper
extension `rho'=7^a j` gives a transported vector with nontrivial upper
center character, so it is globally mean-zero upstairs, but it is fixed
by the lifted lower `M_a`. The ambient mean-zero norm of that lifted
distribution is therefore one. One must remove the copied lower constant
projection even in these nonzero upper conductor sectors. The separately
known operator averaging over all of `L_b` has a different distribution
and its known global gap is not contradicted.


The sharp remainder in Section 7 is on $`L^2(S_{a,b})`$. It is not
asserted on the off-subloop part of $`L^2(\mathcal L_b)`$ or on every
induced fiber. In particular, the nonzero upper extensions of the entirely
trivial lower nucleus character contain copied constants, which must be
removed even though they have zero mean for the upper homogeneous space.

## 10. A maximal coherent trace polarization

The basic construction above admits a stronger arithmetic subloop retaining
additional actual upper field modes. The construction and its precise
maximality are proved here; all earlier basic-sublattice formulas retain their
original scope.

### 10.1. Explicit coherent trace polarization

The script letter $`\mathscr P`$ denotes a field subspace, while
Section 3's $`P=C^*C`$ denotes an orthogonal projection. We abbreviate
the field subspace by $`P`$ in local arguments below.

For `a<b`, write `e=b-a`, `d=7^e`, and use the compatible roots
`lambda_b^d=lambda_a`. The degree of `E_b/E_a` is `d`, so
`1,lambda_b,...,lambda_b^(d-1)` is an `E_a` basis. Define

```math
 A_e=\{0\}\cup\{1\le j<7^e:
 \text{the least significant nonzero base-seven digit of }j
                       \text{ belongs to }\{1,2,3\}\}.
```

Set

```math
 \mathscr P_{a,b}=\operatorname{span}_{E_a}
                 \{\lambda_b^j:j\in A_e\}\subset E_b,
 \qquad N_{a,b}=\mathscr P_{a,b}\cap\ker\operatorname{Tr}_{E_b/E_a}.
```

For adjacent levels this is simply
`P_(a,a+1)=span_(E_a){1,lambda_(a+1),lambda_(a+1)^2,lambda_(a+1)^3}`.

Every nonzero exponent `j` is paired with `d-j`. Their least significant
nonzero digits are `s` and `7-s`, so exactly one lies in `A_e`.
Thus `|A_e|=(d+1)/2` and `dim_(E_a) N=(d-1)/2`.

The relative trace satisfies, for `0≤j≤2d-2`,

```math
 \operatorname{Tr}_{b/a}(\lambda_b^j)=
 \begin{cases}
 1,&j=0,\\
 \lambda_a,&j=d,\\
 0,&\text{otherwise}.
 \end{cases}
```

Indeed the Galois conjugates are `lambda_b` times all `d`th roots of
unity, and `d=1` in characteristic three. No two positive exponents
in `A_e` sum to `d`. Therefore, writing `T=Tr_(b/a)`,

```math
 \boxed{T(xy)=T(x)T(y)\quad(x,y\in \mathscr P_{a,b}).}
```

This does **not** say `P` is a subalgebra: its multiplication need not
stay in `P`. It says the symmetric trace pairing restricted to `P`
factors through its one-dimensional quotient `T:P→E_a`.
In particular `P=E_a⊕N`, and `N` is totally isotropic and orthogonal
to `P` for the trace pairing.

This dimension is maximal within the scalar trace-factorization
architecture: if an `E_a`-linear subspace `P'⊂E_b` contains `1` and
satisfies `T(xy)=T(x)T(y)` for all `x,y∈P'`, then
`N'=P'∩ker T` is totally isotropic for the nondegenerate trace pairing
on `ker T`. The latter pairing is nondegenerate because
`E_b=E_a⊕ker T` is an orthogonal decomposition with nondegenerate
`E_a` summand (`T(1)=1`). Therefore `N'⊂(N')^perp` gives
`2dim N'≤d-1`, and `dim P'≤(d+1)/2`, attained by `P_(a,b)`.
This is not a maximality claim among arbitrary loop correspondences,
nonlinear reductions, or vector subspaces tailored to a specific pencil.

The exact compatibility across `a<b<c` is

```math
 \boxed{\mathscr P_{a,c}=\{x\in \mathscr P_{b,c}:T_{b,c}(x)\in \mathscr P_{a,b}\}.}
```

To see this, expand `x=sum_(j∈A_(c-b)) lambda_c^j x_j` with
`x_j∈E_b`. The relative trace is `x_0`. Expanding each `x_j` in the
`E_a` basis of `E_b` gives exponents `j+7^(c-b)i`. If `j!=0`, its
lowest nonzero digit decides membership independently of `i`; if
`j=0`, membership is exactly the condition on `i` from `A_(b-a)`.
This is precisely `A_(c-a)`.

### 10.2. Larger actual subloop and quotient

Replace the field condition in the basic subloop by `w∈P_(a,b)^n`:

```math
 S^{\rm pol}_{a,b}=
 \{(w,((dx_i,y_i))_i,\alpha,dt):
 w\in \mathscr P_{a,b}^n,
 x_i,t\in R_a,\ y_i\in R_b,\alpha\in\mathbf F_3^k\}.
```

Define

```math
 r^{\rm pol}_{a,b}(w,((dx_i,y_i)),\alpha,dt)
     =(T_{b/a}w,((x_i,\bar y_i)),\alpha,t).
```

The restriction of the upper scalar action is multiplication by
`lambda_a^t∈E_a`, which preserves `P`. Since every `B_i` has entries
in `E_a`, the boxed trace pairing identity gives, coordinatewise,

```math
 \beta_b(w,w')=\beta_a(Tw,Tw')\quad(w,w'\in P^n).
```

Thus the actual upper section law, its divisions, inverse, and Bol
identity close on `S^pol`, and `r^pol` is a surjective loop
homomorphism to `L_a`. Its kernel is

```math
 K^{\rm pol}_{a,b}=N_{a,b}^n\oplus
          \{((0,7^a j_i))_i:j_i\in\mathbf Z/d\},
```
```math
 |K^{\rm pol}_{a,b}|=Q_a^{n(d-1)/2}d^k.
```

In particular the kernel is no longer merely an artifact of the ring
reduction: it retains an explicit half-dimensional isotropic part of
the actual larger field. The upper scalar actions outside the subgroup
`dR_b` are still retained by induction, rather than falsely forced
through lower scalar reduction.

The exact preimage and composition identities remain

```math
 (r^{\rm pol}_{b,c})^{-1}(S^{\rm pol}_{a,b})=S^{\rm pol}_{a,c},
 \qquad r^{\rm pol}_{a,b}r^{\rm pol}_{b,c}=r^{\rm pol}_{a,c}.
```

The first preimage is taken inside `S^pol_(b,c)`. The field part is
the preceding boxed polarization relation; ring and center parts are
the original divisibility identities.

### 10.3. Normalization and information retained

The subloop density improves to

```math
 \delta^{\rm pol}_{a,b}
 =Q_a^{-n(d-1)/2}d^{-(k+1)}.
```

The previous choice `w∈E_a^n` had field density
`Q_a^(-n(d-1))`. All transfer formulas apply with the new kernel
cardinality and density:

```math
 (C^S F)(z)=\mathbb E_{r(s)=z}F(s),\qquad
 (CF)(z)=\sqrt\delta\mathbb E_{r(s)=z}F(s),
 \quad C^*f=\delta^{-1/2}\mathbf1_S(f\circ r).
```

Again `CC*=I`, `C*C` is the support/fiber projection, and the full
ambient kernel is its orthogonal complement. Densities and kernel
cardinalities multiply:

```math
 \delta_{a,b}\delta_{b,c}=\delta_{a,c},\qquad
 |K_{a,b}|\,|K_{b,c}|=|K_{a,c}|.
```

For the field factors use `Q_b=Q_a^(7^(b-a))`; the exponents telescope
as `(d1-1)+d1(d2-1)=d1d2-1`. Consequently normalized transfers
compose exactly on the full ambient Hilbert spaces.

Central conductors and the `d^(-1/2)` aliasing formula are unchanged.
The vector coisometry now also averages `w` over the explicit
isotropic affine fiber `w_0+N^n`, with the corresponding new vector
support density.

### 10.4. Complete spectrum and sharp transfer error

Use the actual mixed vector module

```math
 T=\mathscr P_{a,b}^n\oplus(R_a\oplus R_b)^k,
 \quad q(w,z_i)=(T_{b/a}w,\bar z_i).
```

Then `b_S=b_a(q,q)` and `qR_S=R_aq`. The detailed proof in
Sections 6--7 of this manuscript applies with these explicit changes:

1. The field phase and image test use `w_0=T_(b/a)w`, so
   `t_α(w_0,ν)` replaces `t_α(w,ν)`.
2. The **actual** field-orbit label `σ` is required to be zero when
   the actual `w=0`; if `w!=0`, every `σ∈R_a` is allowed. A nonzero field-kernel vector has a full
   `7^a` orbit even when `w_0=0`.
3. The field averages in the phase calculation factor through the
   uniform quotient `P^n→E_a^n`. All kernel factors cancel from
   normalized averages. Hence the same `Q_a^(-r_α)` and scalar
   incidence test are exact.
4. The scalar radical is the preimage of the lower scalar radical.
   Its density remains $`Q_a^{-r_\nu}7^{-2k c_\rho}`$, where
   $`c_\rho=a-v_7(\rho)`$ is the conductor exponent, with $`v_7(0)=a`$.
5. On the dual of the actual `P^n`, every nonzero additive character
   has trivial stabilizer under the cyclic `lambda_a` action:
   multiplication by `lambda_a^t-1` is an `E_a` unit for nonzero
   `t∈R_a`, hence bijective on `P^n`. Thus the zero-nucleus-sector
   global multiplier remains `κ_I τ_a^(1_(ξ_W!=0))`, with actual
   field-character support used in the indicator.

The complete intrinsic eigenvalue formula is therefore

```math
 t_\alpha(Tw,\nu)s_\sigma(\bar z,\rho),
```

at all actual orbit labels. It includes every new isotropic-field
fiber mode. The right nucleus remains pure `Z_a`, since the scalar
actions have no nonzero fixed vector even in `ker q`. Every earlier
constant, energy bound, and exact residual relation remains valid:

```math
 \|A_S^t-P_{\rm inner}\|=9^{-t},\qquad
 \|M_S^t-\Pi_S\|=\Lambda_a^t,
 \quad\Lambda_a=\tfrac13+\tfrac23Q_a^{-r_{\min}},
```
```math
 M_S^t=(C^S)^*M_a^t C^S+R_t,
 \qquad \|R_t\|=\Lambda_a^t.
```

The same pure ring-fiber character still proves sharpness in the
kernel. Pure field-fiber characters have multiplier `τ_a<1/3`, so
the larger retained field information creates no slower exceptional
sector. These estimates hold internally on `L2(S)`, not on the
entire complement of `S` in `L2(L_b)`.

### 10.5. The same faithful envelope induction

Define $`G^{\rm pol}_{ab}`$ by allowing both vector axes of Section 5's
upper envelope to lie in the polarized upper vector lattice, and both
center coordinates to lie in $`Z_{ab}`$. Apply the field trace and ring
reduction to each vector axis and divide both ring centers by $`d`$.
The trace-pairing identity and action identity already proved make this a
surjective group homomorphism $`\Phi^{\rm pol}_{ab}:G^{\rm pol}_{ab}\to G_a`$.
It maps every compatible actual section and full correction exactly.
Its kernel is two copies of $`K^{\rm pol}_{ab}`$.

The inverse image of $`H_a`$ has exactly the form of Section 5.2 with this
new lattice and kernel. In particular its intersection with $`Z(N_b)`$
is trivial. The identical two-commutator core argument in that section proves
that $`G_b/((\Phi^{\rm pol}_{ab})^{-1}H_a)`$ is a faithful homogeneous
upper model. No replacement of the upper section or abstract unrelated
factor is involved. The induction index is
$`I=[G_b:G^{\rm pol}_{ab}]=(\delta^{\rm pol}_{a,b})^{-2}`$; the homogeneous
space has $`I|\mathcal L_a|`$ points. The same normalized kernel, adjoint
and charge projectors apply.

The exact polarization-preimage identity gives
$`G^{\rm pol}_{a,c}=(\Phi^{\rm pol}_{b,c})^{-1}G^{\rm pol}_{a,b}`$.
Factoring coset representatives in stages therefore proves the same unitary
induction-in-stages identity, including the base-fiber maps and conductor
paths. This proves coherence for the enlarged upper actions as well as the
ambient regular coisometries.

### 10.6. Exact adjacent compression boundary

The action of the **full** upper scalar is retained in the induced
space, but compression to one lower block is not a multiplicative
representation. This can be seen without any general no-go theorem.
At adjacent levels put `P=span_(E_a){1,lambda,lambda²,lambda³}` and
`N=span_(E_a){lambda,lambda²,lambda³}`, with `lambda=lambda_(a+1)`.
Then

```math
                    P\cap\lambda P=N.
```

Let `I=C*` be the normalized support/fiber embedding and let `D_lambda`
be the actual upper defect dilation multiplying its field coordinate
by `lambda` and fixing the other coordinates. On the lower field
factor,

```math
 (C D_\lambda I f)(w)
       =\mathbf1_{\{w=0\}}\,\mathbb E_{v\in E_a^n}f(v)=:Rf(w).
```

Indeed the output can have lower trace only zero, and on the common
subspace `N^n` the coefficient of `lambda` is uniform; after dividing
by `lambda` this coefficient is exactly the input trace. Therefore

```math
 R^*R=Q_a^{-n}\Pi_W,
 \qquad C D_\lambda^{-1}D_\lambda I=\operatorname{Id},
 \qquad\|\operatorname{Id}-R^*R\|=1.
```

All other lower variables are spectator factors. This differs from
the smaller subfield architecture's point projection, so the two
compression formulas must not be conflated. The formula was separately
checked by contributing agent `/root/induction_routes`.
## 11. Evidence, provenance and remaining bridge

The proofs above are finite algebra and explicit normalized Fourier
calculations. The group induction is proved in coset coordinates; no external
representation-theoretic existence theorem is needed. The inputs from the
prior research are the fixed arithmetic tower and the verified Bol section;
the mixed-module spectrum is rederived because its bimap has a new radical.
This is a new result relative to the pinned workspace, not a literature-wide
historical-priority claim for induction or polarized reductions.

The authored envelope checker and separately authored independent checker
are linked from [the code guide](../code/README.md#action-compatible-arithmetic-transfer).
Exact revisions, hashes, reviewer roles, commands, finite scopes and remaining
integrity limits are recorded in
[the evidence record](../evidence/bol-action-transfer-review.md).
No permanent claim IDs are allocated. The earlier manuscripts and signed
reviews retain their original bytes and scope.

This completes the specified local version: actual arithmetic section and
defect transfer, a faithful enlarged model retaining all upper actions,
normalized coherent compression, all conductor extensions, and a sharp
quantitative bound on the lost fiber dynamics. It does not identify a
full-upper action with an action on the lower loop, or transport the original
unrestricted upper readout with its old marks unchanged. Those are materially
different demands, and the explicit excursion calculation identifies one
obstruction to imposing them on this compression.

No local metaplectic cover, automorphy, Euler product, global theta function
or quasi-RH consequence follows here. A global arithmetic construction would
additionally need compatible local structures at other places, a global
group or geometric object and its arithmetic lattice, a specified global
kernel with convergence, and any claimed functional or Hecke identities.
None of those bridges is supplied by finite induction alone.

