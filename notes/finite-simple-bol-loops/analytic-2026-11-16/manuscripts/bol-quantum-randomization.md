# Sparse quantum randomization from reciprocal Bol operations

Mira Cult

## Results and scope

The translated-defect channel of the reciprocal Bol construction has a useful
two-rate Hilbert--Schmidt estimate. Its dense sampling law does not by itself
provide a sparse resource advantage. We determine several precise limits of
sparsifying it and give explicit implementable repairs.

* In every degenerate sector, **every distribution of native operations** fixes
  a density matrix at trace-norm distance $`2(1-|D_\chi|^{-1})`$ from uniform.
* In the fixed nondegenerate family over $`E=\mathbf F_{729}`$ with
  $`W=E^n`$, a list of $`K\leq2n`$ native operations has a nontrivial common
  fixed algebra, regardless of subsequent word lengths, weights, or correlations.
  An explicit list of $`2n+1`$ operations has scalar common commutant. This is
  a sharp **irreducibility threshold**, not a claimed optimal spectral gap.
* At conductor one, every Weyl operator followed by one fixed actor is an actual
  single translated defect. An explicit small-bias sampler consequently gives
  arbitrary-state trace error $`\varepsilon`$ with at most
  $`3969d/\varepsilon^2`$ equally likely seeds, where
  $`d=49\cdot3^N`$ and $`N=6n`$. It uses one native operation, $`O(N)`$ fixed
  qudit gates, constant quantum depth, no quantum ancilla, deterministic polynomial
  classical preprocessing, and expected polynomial fair-bit sampling.
  The exact $`d^2`$-seed twirl is used if smaller.
* In the fixed $`p=3,q=7,k=A=1`$ symplectic family, the original dense channel
  itself has a depolarizing component of weight $`512/1029`$. This gives the
  dimension-independent diamond bound $`2(517/1029)^t`$, rather than treating
  the generic dimension-dependent HS conversion as its actual mixing time.
* If the actual defect pair is held fixed and only its translating center varies,
  two independent uniform rounds depolarize exactly. A sparse version has an exact
  two-step HS norm and a sharper direct state-purity bound coming from two
  noncommutative matrix subalgebras. Its one-step coherence norm is **one**:
  the original dense channel's faster coherence rate does not survive this change.

These results do **not** demonstrate an efficiency advantage over the strongest
standard randomizers. The one-call construction is exactly a Weyl ensemble in
Bol coordinates, and a group-based control reproduces the complete channel at
the same gate and random-key cost. The new mathematical content here is the
native-operation obstruction, its sharp commutant threshold, explicit reachability,
the dense depolarizing component and the fixed-pair two-round estimate.
Polynomial small-bias sampling, Weyl
encryption, matrix concentration and gate compilation are established machinery.

The [non-scalar manuscript](bol-nonscalar-intertwiners.md) is denoted NI and its
[associator dependency](bol-associator-quantization.md) AQ. Both proof dependencies
are included in this public collection. All theorem and QR equation labels below
are local to this manuscript. Source provenance, review status and finite execution
evidence are recorded in the
[reproducibility record](../evidence/bol-randomization-reproducibility.md).

## 1. The channel, basis and sampling law

Let $`p,q`$ be distinct odd primes, $`p\mid q-1`$, $`m=q^A`$ with
$`A\geq1`$, and $`R_A=\mathbf Z/m\mathbf Z`$. Let $`E`$ have characteristic
$`p`$ and cardinality $`Q`$, containing $`\lambda`$ of order $`m`$. Choose
$`\eta\in R_A^\times`$ of order $`p`$, also modulo $`q`$. Let
$`B_1,\ldots,B_k`$ be alternating $`n\times n`$ matrices over $`E`$,
independent over $`\mathbf F_p`$, with zero common radical. Set

```math
 W=E^n,\quad V=(R_A^2)^k,\quad U=W\oplus V,\quad
 Z=\mathbf F_p^k\oplus R_A,\quad d=|U|,
```

```math
 b(u,u')=\left((\mathrm{Tr}_{E/\mathbf F_p}
 w^{\mathsf T}B_iw')_i,\ \sum_i\det(v_i,v'_i)\right),\qquad
 R(a,t)(w,(v_i))=(\lambda^tw,(\eta^{a_i}v_i)).                 \tag{QR.1}
```

The reciprocal loop, its sector translation, and its actual left-inner defect are

```math
 (a,c)\circ(v,e)=(a+R(c)v,c+e-b(a,v)),\qquad
 \pi_\chi(a,c)|u\rangle=\chi(c-b(a,u))|a+R(c)u\rangle,
```

```math
 \ell_{x,y}=L_{x\circ y}^{-1}L_xL_y=H_{h,g},\quad
 g=b(a,v),\quad h=R(g)a-R(e)a+R(c+g)v-v,
 \qquad J_\chi(h,g)|u\rangle=\chi(b(h,u))|R(g)u\rangle .     \tag{QR.2}
```

Here $`x=(a,c),y=(v,e)`$. AQ, Sections 1--4, proves the loop and Bol identities
and this correction formula directly; no simplicity/classification input is
needed. All new channel proofs below use these displayed finite operators.
Point kets are orthonormal. All finite averages are normalized; the matrix norm
is the ordinary $`\|T\|_2^2=\mathrm{Tr}(T^*T)`$.

Write $`\chi=(\nu,\rho)`$ with
$`\chi(a,t)=e_p(\nu\cdot a)e_m(\rho t)`$. Then

```math
 B_\nu=\sum_i\nu_iB_i,\qquad
 D_\chi=\ker_E B_\nu\oplus(\mathrm{ann}_{R_A}\rho)^{2k}.
                                                                    \tag{QR.3}
```

The dense starting channel uses independent uniform $`x,y,z\in\mathcal L=U\times Z`$:

```math
 V_{x,y,z}=\pi_\chi(z)^{-1}J_\chi(\ell_{x,y})\pi_\chi(z),\qquad
 \Phi_\chi(T)=\mathbb E_{x,y,z}V_{x,y,z}TV_{x,y,z}^*,\qquad
 \mathcal E(T)=\mathrm{Tr}(T)I/d.                              \tag{QR.4}
```

This is not the uniform measure on the generated defect group. The literal
sampler has $`(d p^k m)^3`$ triples and entropy
$`3\log_2(d p^k m)`$ per use; different triples can induce the same conjugation.
Its exact measure, not merely the generated group, matters for NI's rates.

The characteristic shear subgroup acts by $`M_h|u\rangle=\chi(b(h,u))|u\rangle`$.
Its dephasing map is

```math
 (\mathcal D_\chi T)_{uv}=\mathbf1_{\{u-v\in D_\chi\}}T_{uv}.
                                                                    \tag{QR.5}
```

If and only if $`D_\chi=0`$, this is ordinary point-basis diagonal projection.
Equivalently, $`B_\nu`$ is nonsingular and $`\rho`$ is a unit. The point basis
is then the intrinsic rank-one joint shear basis, up to its natural phases and
permutation. Every native operation is monomial, so the point-diagonal and
off-diagonal spaces are invariant for each operation, each distribution, and
every product. In a degenerate sector this point-diagonal decomposition must
not be confused with the larger blocks of (QR.5).

**Recovered theorem (NI, Q and Q1).** Under $`D_\chi=0`$, for all integers
$`t\geq1`$,

```math
 \|\Phi_\chi^t-\mathcal E\|_{2\to2}=\Lambda^t,\qquad
 \|\Phi_\chi^t(I-\mathcal D_\chi)\|_{2\to2}\leq p^{-2t},\qquad
 \Lambda=p^{-1}+(1-p^{-1})Q^{-r_{\min}},\quad
 r_{\min}=\min_i\mathrm{rank}_E B_i.                           \tag{QR.6}
```

The diagonal restriction attains $`\Lambda`$. Positivity and self-adjointness
of the dense channel give its exact powers. The coherence statement is an upper
bound, not an exact rate. NI's synchronized orbit spectrum proves it, and yields

```math
 \|\Phi_\chi^t(\rho)-I/d\|_2^2\leq
 \Lambda^{2t}\|\mathcal D_\chi\rho-I/d\|_2^2+
 p^{-4t}\|\rho-\mathcal D_\chi\rho\|_2^2.                            \tag{QR.7}
```

The spread/aligned families in NI, Section 9, have degenerate scalar sectors.
They do not satisfy this theorem's hypotheses. Their joint-trace distinction
does not give a randomizer for arbitrary states in those sectors.

## 2. Operational tasks and unavoidable costs

Our principal model is a **random-key, mixed-unitary** algorithm on a specified
logical $`d`$-dimensional Hilbert space. A classical key selects a unitary or a
schedule of unitaries, applied without measurements. We count seed cardinality,
random bits, classical preparation, physical gates, depth and ancillary space.
An abstract native-operation count is reported separately from its gate cost.

The three distinct errors are

```math
 e_1(\Psi)=\sup_{\rho\geq0,\mathrm{Tr}\rho=1}
             \|\Psi(\rho)-I/d\|_1,\qquad
 e_2(\Psi)=\|\Psi-\mathcal E\|_{2\to2},\qquad
 e_\diamond(\Psi)=\|\Psi-\mathcal E\|_\diamond.                       \tag{QR.8}
```

We do not divide trace norm by two. The diamond target replaces the input by
$`I/d`$ while retaining the reference marginal:
$`(\mathcal E\otimes\mathrm{id})(\rho_{AR})=I/d\otimes\rho_R`$.
It is not a statement that the reference becomes maximally mixed.

For any such channel, $`e_1\leq\sqrt{d-1}\,e_2`$ on states, and
$`e_\diamond\leq d\,e_2`$. The former follows from
$`\|\rho-I/d\|_2^2\leq1-1/d`$ and Schatten Cauchy--Schwarz. For the latter,
an ancillary dimension $`d`$ suffices in the diamond norm, the amplified HS norm
is still $`e_2`$, and $`\|X\|_1\leq d\|X\|_2`$ on the joint space.

Consequently the dense channel is sufficient for state error $`\varepsilon`$ at

```math
 t\geq\left\lceil\frac{\log(\sqrt{d-1}/\varepsilon)}{-\log\Lambda}\right\rceil,
 \qquad
 t\geq\left\lceil\frac{\log(\sqrt{d-1}/\varepsilon)}{2\log p}\right\rceil
 \quad\hbox{if }\mathcal D_\chi\rho=I/d.                           \tag{QR.9}
```

Use $`t\geq1`$ and replace a negative bound by zero as appropriate. A sufficient
diamond mixing time replaces $`\sqrt{d-1}`$ by $`d`$ in the first expression.
These are sufficient trace/diamond bounds, not asserted exact mixing times.
Each channel power requires fresh independent triple samples. Reusing one key
gives a different average of powers and is not covered.

**Lemma R (rank limits).** A mixture with $`M`$ keys obeys

```math
 e_1(\Psi)\geq2\max(0,1-M/d),\qquad
 e_\diamond(\Psi)\geq2\max(0,1-M/d^2).                            \tag{QR.10}
```

Indeed the output on any pure input has rank at most $`M`$. Measuring its support
against $`I/d`$ gives the first inequality. Applying the same argument to the
normalized Choi state in dimension $`d^2`$ gives the second. This also proves the
state lower bound for a class containing just one uniform-population pure state.
For a $`K`$-choice, $`t`$-round schedule, use $`M\leq K^t`$. These are support
or worst-case fixed-length-key bounds, not by themselves Shannon-entropy lower
bounds for arbitrarily nonuniform keys. For exact depolarization, the Choi state
is maximally mixed and the entropy upper bound for a mixture of pure states additionally
requires key entropy at least $`2\log_2d`$.

A uniform key on an odd-size set has entropy $`\log_2M`$ but cannot be drawn
exactly with a fixed finite number of fair bits. An exact interval sampler reads
binary digits of a uniform number in $`[0,1)`$ until its current dyadic interval
lies in one of the $`M`$ equal bins. Since
$`\Pr(T>j)\leq\min(1,(M-1)2^{-j})`$, it uses fewer than
$`\log_2M+3`$ bits in expectation. Its worst-case running time is unbounded.
This sampler, rather than an uncharged ideal real number, is our fair-bit model.

A fixed worst-case budget is also available. Stop that sampler after $`B`$
bits and use an arbitrary key if its bin is still undetermined. Coupling with
the exact sample bounds total variation by $`M2^{-B}`$ and the resulting
channel diamond error by $`2M2^{-B}`$. Thus
$`B=\lceil\log_2(2M/\tau)\rceil`$ gives sampling error at most $`\tau`$
in worst-case polynomial time. Splitting the desired error between sampling,
the mathematical randomizer and gate compilation makes this a bounded-time
variant. The extra $`\log_2(1/\tau)+O(1)`$ bits are charged explicitly.

If irreversible discard and fresh environments are allowed, exact depolarization
instead has a zero-classical-randomness implementation: prepare a maximally
entangled pair, swap the input into one half, and discard the old input and the
other half. It uses a pure environment of dimension $`d^2`$, which is necessary
by Choi rank. On the fixed qudit tensor product this costs $`O(\log d)`$ gates
and $`2\log d`$ worth of ancillary quantum dimension. This different resource
model does not support an unqualified claim of saving random bits.

### 2.1. A dimension-independent bound for the dense fixed family

The sufficient HS times in (QR.9) need not be sharp. We can remove their
dimension factor for the specific family (QR.15), without asserting this for
arbitrary pencils or conductors.

**Theorem QD (dense depolarizing component).** In (QR.15) the original dense
channel has the mixed-unitary decomposition

```math
 \Phi=\frac{512}{1029}\mathcal E+\frac{517}{1029}\mathcal R,
 \qquad
 \|\Phi^t-\mathcal E\|_\diamond\leq2(517/1029)^t,                 \tag{QR.9a}
```

where $`\mathcal R`$ is another unital mixed-unitary channel. Thus
$`t\geq\lceil\log(2/\varepsilon)/\log(1029/517)\rceil`$ suffices even
against a reference, with fresh independent dense samples. This is a proved
upper bound, not an exact diamond decay rate.

**Proof.** Write $`D=|W|=729^n`$. For independent uniform field vectors,
the alternating trace form is a uniform $`\mathbf F_3`$ functional when the
first vector is nonzero. Similarly the ring determinant is a uniform
$`\mathbf F_7`$ functional when its first vector is nonzero. Hence

```math
 \Pr(g_p\ne0)=\frac23(1-D^{-1}),\qquad
 \Pr(g_q\ne0)=\frac67(1-7^{-2})=\frac{288}{343},                 \tag{QR.9b}
```

and these events are independent. Condition on particular nonzero values of
both components of $`g`$. On the field block the actual defect is
$`h_W=\alpha a_W+\beta v_W`$, where
$`\alpha=\lambda^{g_q}-\lambda^{e_q}`$ and
$`\beta=\lambda^{c_q+g_q}-1`$. Both coefficients vanish for exactly one of
the 49 independent actor pairs $`(c_q,e_q)`$. For every other pair, the
constraint $`\mathrm{Tr}(a_W^{\mathsf T}B_1v_W)=g_p\ne0`$ makes
$`h_W`$ uniform on $`W\setminus\{0\}`$.

For example, if $`\beta\ne0`$, a prescribed $`h_W\ne0`$ determines
$`v_W=\beta^{-1}(h_W-\alpha a_W)`$, and leaves one nonzero linear trace
equation on $`a_W`$, with $`D/3`$ solutions. For $`h_W=0`$ it has none.
If $`\beta=0,\alpha\ne0`$, fix $`a_W=\alpha^{-1}h_W`$ and count
$`v_W`$ instead. This proves the assertion with all scalar coefficients retained.
The analogous determinant calculation on $`\mathbf F_7^2`$ has seven solutions
per nonzero $`h_V`$, and both actor coefficients vanish with probability $`1/9`$.
The two conditional laws are independent, and are exactly

```math
 \frac1{49}\delta_0+\frac{48}{49}\mathrm{Unif}(W\setminus\{0\}),
 \qquad
 \frac19\delta_0+\frac89\mathrm{Unif}(\mathbf F_7^2\setminus\{0\}).
                                                                    \tag{QR.9c}
```

Their pointwise uniform components have respective weights
$`c_W=48D/(49(D-1))`$ and $`c_V=49/54`$, both at most one for this family.
Extract their product, with $`h`$ uniform on $`U`$. Conditional on these
nonzero $`g`$, the actor $`R(g)-I`$ is invertible on both blocks. Formula
(QR.11), with a uniform translating center $`a`$ and any fixed translating
actor $`C`$, sends independent uniform $`(a,h)`$ bijectively to a uniform
Weyl displacement pair. Its conjugation average is exactly $`\mathcal E`$.
The total extracted weight is

```math
 \frac23\frac{D-1}{D}\frac{288}{343}
 \frac{48D}{49(D-1)}\frac{49}{54}=\frac{512}{1029}.              \tag{QR.9d}
```

All residual weights remain nonnegative, so the remainder is mixed-unitary.
Unitality and trace preservation give $`\mathcal E\mathcal R=
\mathcal R\mathcal E=\mathcal E`$. Taking powers and using that the diamond
distance of two channels is at most two proves (QR.9a). $`\square`$

This dense theorem is an additional analytic improvement, not the sparse
algorithm. Its literal per-round entropy is still $`3\log_2(21d)`$ in this
family, and exact Weyl randomization already attains error zero with
$`2\log_2d`$ entropy. Theorem S below supplies the explicit sparse alternative.

## 3. Native normal form and distribution-independent obstructions

### 3.1. Affine normal form

Put $`z=(a,c)`$, $`C=R(c)`$ and $`R_g=R(g)`$. Reciprocity gives
$`b(R(c)u,v)=b(u,R(c)v)`$. Direct substitution in (QR.2) gives

```math
 V_{x,y,z}|u\rangle=
 \chi(b(h,a)+b(a,t))\,\chi(b(H,u))|R_gu+t\rangle,
 \quad t=C^{-1}(R_g-I)a,\quad H=Ch+(R_g-I)a.                       \tag{QR.11}
```

The leading scalar cancels in conjugation. Thus every native unitary is a
Weyl displacement times a block-scalar actor. This calculation retains the
actual defect and its translation, not merely the abstract generated group.

### 3.2. Degenerate sectors

**Theorem D (universal radical obstruction).** If $`D=D_\chi\ne0`$, define

```math
 P_D=|D|^{-1}\sum_{v\in D}X_v,\qquad
 \rho_D=\frac{P_D}{d/|D|}=d^{-1}\sum_{v\in D}X_v,
 \qquad X_v|u\rangle=|u+v\rangle .                                \tag{QR.12}
```

This is a stationary state for every native operation, every distribution and
every word schedule. It has uniform point populations and

```math
 \|\rho_D-I/d\|_1=2(1-|D|^{-1}).                                 \tag{QR.13}
```

**Proof.** $`P_D`$ is the orthogonal projection onto $`D`$-translation-invariant
vectors, of rank $`d/|D|`$. The radical is actor-invariant. Both a translation
matrix $`\pi_\chi(a,c)`$ and a defect $`J_\chi(h,g)`$ conjugate $`X_v`$ for
$`v\in D`$ to the corresponding actor translate, with phase one. They therefore
commute with $`P_D`$. Its normalized spectrum gives (QR.13), and only $`X_0`$
contributes to its diagonal. $`\square`$

This rules out a native repair even for uniform-population states in these
sectors. Merely changing sampling weights, conductor correlations or word lengths
cannot remove the obstruction.

### 3.3. Population support

**Theorem A (affine-span obstruction).** Set $`E_0=\mathbf F_p(\lambda)`$,
$`q_0=|E_0|`$, and $`n_0=\dim_{E_0}W`$. For any fixed list of $`K\geq1`$
native operations, some basis input remains supported in a field-coordinate
affine space of dimension at most $`\min(n_0,K-1)`$ under every word schedule.
Consequently its trace-norm distance from $`I/d`$ is at least

```math
 2\left(1-q_0^{\min(n_0,K-1)-n_0}\right).                         \tag{QR.14}
```

**Proof.** The field permutation of generator $`j`$ is
$`w\mapsto r_jw+t_j`$, with $`r_j\in\langle\lambda\rangle\subset E_0`$.
If $`r_j=1`$ then its native translation $`t_j`$ is zero by (QR.11). If all
actors are trivial, every field label stays fixed. Otherwise choose a fixed
point $`w_0=(1-r_1)^{-1}t_1`$ of one nontrivial actor. Relative to this point
its translation vanishes. The $`E_0`$-span of the other $`K-1`$ translations
is preserved by all generators and their inverses. The orbit of $`w_0`$ lies
there. The total allowed support, including all ring labels, occupies at most
the indicated fraction of the point basis; a support measurement proves the
bound. $`\square`$

This theorem concerns a fixed total list. A time-dependent algorithm that
introduces new generators is charged for their union; a large implicitly sampled
support is not prohibited. Monomiality alone does not imply this obstruction:
general linear permutations can mix coordinates, as in the Anshu et al. control.

### 3.4. A sharper quantum obstruction and its sharp threshold

For the remainder of the explicit algorithms fix

```math
 p=3,\ q=7,\ A=k=1,\ E=\mathbf F_{729},\ n=2h\geq2,\quad
 B_1=\bigoplus_{j=1}^h\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 \chi=(1,1),\quad N=6n,\quad D=3^N,\quad d=49D.                    \tag{QR.15}
```

Take $`\lambda`$ of order seven and $`\eta=2\pmod7`$. This is a
nondegenerate family; its dense rate is $`1/3+(2/3)729^{-n}`$.

**Theorem C (sharp common-commutant threshold).** Any list of $`K\leq2n`$
native unitaries in (QR.15) has a non-scalar common commutant. If a field actor
is nontrivial, this commutant has dimension at least

```math
 L_K=1+\frac{729^{2n-K+1}-1}{7},                                  \tag{QR.16}
```

and it contains a stationary density matrix for every word distribution with
trace error at least $`2(1-L_K^{-1/2})`$. If all field actors are trivial,
the field point projectors give error at least $`2(1-D^{-1})`$. In particular,
state error at most one requires $`K\geq2n+1`$. There is an explicit list
of exactly $`2n+1`$ native unitaries with scalar common commutant.

**Proof of the lower bound.** Work on the field factor; tensoring commuting
operators with the ring identity preserves commutation with every full native
unitary. Let $`\beta(h,v)=\mathrm{Tr}_{E/\mathbf F_3}h^{\mathsf T}B_1v`$.
Use symmetric Weyls

```math
 \widetilde W(v,h)=e_3(\beta(h,v)/2)X_vM_h,\qquad
 \Omega((v,h),(w,k))=\beta(h,w)-\beta(k,v).                         \tag{QR.17}
```

The division by two is in $`\mathbf F_3`$. These form an orthogonal operator
basis, their commutator is $`e_3(\Omega)`$, and actor conjugation is exactly
$`S_g(v,h)=(\lambda^gv,\lambda^{-g}h)`$. As $`3^3\equiv-1\pmod7`$,
the additive coordinate change $`(v,h)\mapsto(v,h^{27})`$ makes this action
scalar multiplication by $`\lambda^g`$ on $`E^{2n}`$.

Write the field generators, up to scalar, as
$`\widetilde W(a_j)D_{\lambda^{g_j}}`$. Conjugating all of them by
$`\widetilde W(z)`$ changes $`a_j`$ to $`a_j+(I-S_{g_j})z`$.
If $`g_1\ne0`$, choose $`z`$ to make $`a_1=0`$. The $`S`$-invariant
$`\mathbf F_3`$-span $`L`$ of the remaining displacements has dimension
at most $`6(K-1)`$: after the preceding coordinate change it lies in an
$`E`$-span of at most $`K-1`$ vectors. Its symplectic annihilator
$`L^\perp`$ is $`S`$-invariant and has size at least
$`729^{2n-K+1}`$.

For each actor orbit $`O\subset L^\perp`$ the sum
$`\sum_{a\in O}\widetilde W(a)`$ commutes with the centered generators.
Displacements contribute no phase and actors permute the summands. Every
nonzero orbit has seven elements, so these independent sums give (QR.16).
Conjugate back to the original generators.

For completeness, a finite-dimensional $`*`$-algebra of dimension at least
$`L_K`$ has a decomposition $`\bigoplus_i(M_{r_i}\otimes I_{m_i})`$.
It contains $`\sum_i r_i\geq\sqrt{\sum_i r_i^2}\geq\sqrt{L_K}`$
mutually orthogonal nonzero projections. One has rank at most
$`d/\sqrt{L_K}`$. Normalize that projection to obtain the stated stationary
state and trace error. At $`K=2n`$, $`L_K=105`$, so this error exceeds one.

**Sharpness for the commutant.** Put $`g_*=(1,1)`$, $`R=R(g_*)`$.
Every pure shear $`M_h=J(h,0)`$ is an actual defect: in (QR.2) take
$`y=(0,g_*)`$ and $`a=(I-R)^{-1}h`$. A pure actor $`D_R=J(0,g_*)`$
is also actual: choose $`a_0,v_0`$ with $`b(a_0,v_0)=g_*`$, and take
$`x=(a_0,-g_*),y=(v_0,g_*)`$.

Let $`e_i`$ be the $`E`$-basis of $`W`$, set $`r_1=(1,0),r_2=(0,1)`$
in the ring plane and $`r_i=0`$ otherwise, and put $`t_i=(e_i,r_i)`$.
The following $`2n+1`$ operators are native:

```math
 D_R,\quad M_{t_i},\quad V_{t_i}=X_{t_i}M_{R^{-1}t_i}D_R
 \qquad(1\leq i\leq n).                                          \tag{QR.18}
```

The last operators are actual translation conjugates of the pure actor, as
proved in Section 6 below. Seventh powers of the shears remove ring components,
and conjugation by $`D_R`$ generates every field modulation because
$`\mathbf F_3(\lambda)=E`$. Third powers of the first two shears generate
all ring modulations. Then $`V_{t_i}D_R^{-1}`$ and these modulations give
$`X_{t_i}`$. The same powers and actor conjugations give all translations.
The generated group thus contains every Weyl operator, whose commutant is
scalar. This proves sharpness of the threshold. A lazy symmetric average of
these generators and inverses converges, but no useful quantitative gap for
this minimal list is claimed. $`\square`$

## 4. Sampling the original channel: an existence benchmark

For $`0<\eta<1-\Lambda`$, sample $`M`$ independent native operations from
the exact dense law (QR.4) and average their conjugations to obtain $`\widehat\Phi`$.
A conservative matrix-Hoeffding bound gives

```math
 \Pr\{\|\widehat\Phi-\Phi\|_{2\to2}>\eta\}
 \leq4d^2\exp(-M\eta^2/32).                                      \tag{QR.19}
```

To see the constants, represent conjugation on the $`d^2`$-dimensional HS
space. Each centered summand has norm at most two. Its Hermitian dilation has
dimension $`2d^2`$ and square bounded by $`4I`$. Apply the two-sided
matrix-Hoeffding inequality [TROPP, Theorem 1.3] to the dilation sum.
Thus $`M\geq32\eta^{-2}\log(4d^2/\zeta)`$ suffices with failure at most
$`\zeta`$. Every sample preserves the diagonal/off-diagonal decomposition,
so on success

```math
 \|\widehat\Phi^t-\mathcal E\|_{2\to2}\leq(\Lambda+\eta)^t,
 \qquad
 \|\widehat\Phi^t(I-\mathcal D_\chi)\|_{2\to2}
       \leq(p^{-2}+\eta)^t.                                      \tag{QR.20}
```

These are upper bounds; neither exactness nor self-adjoint positivity is
inherited. Online choices require $`t\log_2M`$ seed entropy and fresh keys.
Offline sampling costs $`3M\log_2(d p^k m)`$ entropy, in addition to storing
or regenerating the list. The union is a fixed $`O(\log d)`$-size list for
fixed $`\eta,\zeta`$, consistent with Theorem C.

This is a probabilistic existence/Monte Carlo construction, not our explicit
algorithm. Forming the exact $`d^2\times d^2`$ superoperator is already a
polynomial-in-$`d`$ task, and dense spectral certification uses $`d^4`$ memory.
No certification procedure polynomial in $`\log d`$ is supplied. The later
explicit constructions bypass this search and certification problem; they do
not claim to preserve the dense channel's two rates.

## 5. One-call Weyl reachability and an explicit sparse randomizer

Write $`\mathsf B(u,v)=\chi(b(u,v))`$ in the nondegenerate family (QR.15),
$`M_h|u\rangle=\mathsf B(h,u)|u\rangle`$, and
$`W_{v,h}=X_vM_h`$. The $`W_{v,h}/\sqrt d`$ form an orthonormal matrix basis.

**Theorem W (actual fixed-actor Weyl coset).** For every $`v,k\in U`$,
$`W_{v,k}D_R`$, up to a global phase, is one actual translated pair defect,
where $`R=R(1,1)`$ is fixed. Its loop labels can be computed in $`O(N)`$
fixed-field operations. Consequently any efficiently sampled Weyl ensemble can
be implemented with the same keys by single actual translated defects followed
by the same fixed actor on the input.

**Proof.** First realize every $`J(h,g_*)`$ as a single pair defect. Set
$`c=-g_*`$. Independently on the two blocks, choose $`e`$ as follows.
If $`h_W\ne0`$, take $`e_q=0`$ and
$`a_W=(\lambda-1)^{-1}h_W`$, then choose $`v_W`$ with
$`\mathrm{Tr}(a_W^{\mathsf T}B_1v_W)=1`$. Nondegeneracy gives such
a vector by solving at the first nonzero coordinate. If $`h_W=0`$, take
$`e_q=1`$ and a fixed pair with this trace equal to one. If $`h_V\ne0`$,
take $`e_p=0`$, $`a_V=(2-1)^{-1}h_V=h_V`$, and choose $`v_V`$ with
$`\det(a_V,v_V)=1`$. If $`h_V=0`$, take $`e_p=1`$ and a fixed determinant-one
pair. Then $`b(a,v)=g_*`$ and (QR.2) gives exactly
$`h=(R(g_*)-R(e))a`$, since $`R(c+g_*)-I=0`$.

For a requested $`W_{v,k}D_R`$, choose $`h=Rk-v`$ and center
$`a'=(R-I)^{-1}v`$. Conjugate the just constructed $`J(h,g_*)`$ by
$`\pi(a',0)`$. Formula (QR.11) gives translation $`v`$ and point modulation
$`h+v=Rk`$, exactly the action of $`W_{v,k}D_R`$, up to its displayed global
phase. All inversions are in fixed-size fields, and locating the nonzero
coordinate takes $`O(N)`$ work. $`\square`$

This one-call theorem is restricted to $`A=1`$. At higher conductor a unit
determinant pair forms a ring basis, and the coefficients in its actual defect
$`h_V`$ are each zero or a unit. Thus $`h_V`$ is zero or primitive; a nonzero
nonprimitive $`h_V`$ is impossible at fixed unit actor. In particular a target
with $`v_V=0`$ and nonzero nonprimitive $`k_V`$ cannot be obtained by changing
the conjugating actor either, since it only rescales this nonprimitive vector.
We do not extend Theorem W to all conductors.

**Lemma B (explicit blocked-coordinate polynomial sampler).** For $`\ell\geq2`$
and $`r\geq1`$, let $`F=\mathbf F_{3^r}`$, choose a power basis
$`e_0,\ldots,e_{r-1}`$ over $`\mathbf F_3`$, and put
$`s=\lceil\ell/r\rceil`$. Choose independent uniform $`a,b\in F`$, and output

```math
 T(a,b)_{jr+i}=\mathrm{Tr}_{F/\mathbf F_3}(ae_i b^j),
 \qquad 0\leq j<s,\quad0\leq i<r,\quad jr+i<\ell.                 \tag{QR.21}
```

For every nonzero $`z\in\mathbf F_3^\ell`$, set
$`c_j=\sum_{i:jr+i<\ell}z_{jr+i}e_i`$. Then

```math
 \mathbb E e_3(z\cdot T)=
 \frac{|\{b:\sum_j c_jb^j=0\}|}{3^r}\leq\frac{s-1}{3^r}.           \tag{QR.22}
```

Basis independence makes the displayed polynomial nonzero whenever $`z\ne0`$.
Averaging first in $`a`$ gives the equality by the perfect trace pairing;
its degree is at most $`s-1`$, so the root bound gives the inequality.
This is the standard Alon--Goldreich--Hastad--Peralta blocked-coordinate
small-bias construction, as presented in [DN, Appendix B, Proposition B.1],
with the same elementary argument over $`\mathbf F_3`$. Using all basis
coordinates removes the unnecessary squared-register-size overhead of the
unblocked version. We include the proof to fix constants and uniformity.

**Theorem S (explicit one-call state randomizer).** For (QR.15) and
$`0<\varepsilon\leq1`$, set $`\delta=\varepsilon/\sqrt D`$ and

```math
 r=\left\lceil\log_3\frac{3\sqrt D}{\varepsilon}\right\rceil.
                                                                    \tag{QR.23}
```

Use (QR.21) with $`\ell=2N`$ as the field Weyl label $`(v_W,k_W)`$,
and choose $`(v_V,k_V)\in\mathbf F_7^4`$ independently uniformly. Compile
$`W_{v,k}D_R`$ with Theorem W. The channel $`\Psi`$ satisfies

```math
 e_1(\Psi)\leq\varepsilon,\qquad e_2(\Psi)\leq\delta,
 \qquad M=7^4 3^{2r}<3969d/\varepsilon^2.                         \tag{QR.24}
```

If $`M>d^2`$, use the exact uniform Weyl-coset twirl instead, giving
$`e_\diamond=0`$ with $`d^2`$ keys. For the approximate choice the key entropy is

```math
 \log_2M<\log_2d+2\log_2(1/\varepsilon)+\log_2 3969.
                                                                    \tag{QR.25}
```

**Proof.** Weyl conjugation multiplies each Weyl basis vector by a character
of its label. The nondegenerate commutator pairing identifies all nontrivial
field labels with nonzero linear functionals on $`\mathbf F_3^{2N}`$.
Since $`N`$ is a multiple of 12 and $`\varepsilon\leq1`$, we have
$`r\geq N/2+1`$ and $`s=\lceil2N/r\rceil\leq4`$.
Lemma B therefore bounds every nonconstant field multiplier by
$`3/3^r\leq\delta`$. The ring
Weyl twirl is exact depolarization, so even for states entangled between the
field and ring factors the output is the field channel on a reduced state,
tensored with $`I_{49}/49`$. Its trace error is at most
$`\sqrt{D-1}\delta\leq\varepsilon`$. Precomposing with the fixed unitary
$`D_R`$ does not change this supremum or the HS norm. Finally
$`3^r<9\sqrt D/\varepsilon`$ gives (QR.24). $`\square`$

This is a worst-case state theorem, including arbitrary mixed inputs and
entanglement between the two internal factors. It does not promise small error
against an external reference. For fixed $`\varepsilon`$ and increasing $`d`$,
(QR.10) in fact gives $`e_\diamond\geq2(1-M/d^2)=2-o(1)`$ for this approximate
ensemble. Its low key count is compatible with this large diamond error.

## 6. Holding the defect pair fixed: exact two-round mixing and purity

There is a distinct repair which changes only the translation average and retains
one actual defect pair. Choose the pure actor pair in Theorem C, and for each
$`t\in U`$ use center $`(R-I)^{-1}t`$. Direct substitution gives

```math
 V_t|u\rangle=\mathsf B(t,u)|Ru+t\rangle,
 \qquad V_t=X_tD_RM_t=X_tM_{R^{-1}t}D_R.                           \tag{QR.26}
```

This section works for any nondegenerate odd-order reciprocal sector with an
actual pure actor $`J(0,g)`$ for which $`R-I`$ and $`R^2-I`$ are invertible.
In particular the $`k=1`$ symplectic family works at every conductor when
$`\rho`$ is a unit. Its efficient gate bounds below are asserted only for
the fixed-conductor family (QR.15).

For a distribution $`\mu`$ on $`U`$ put
$`\mathcal C_\mu=\mathbb E_{t\sim\mu}\mathrm{Ad}V_t`$ and
$`\widehat\mu(w)=\mathbb E_t\mathsf B(t,w)`$. Let
$`\Delta=\max_{w\ne0}|\widehat\mu(w)|`$ be its **actual** bias. Then

```math
 \mathcal C_\mu(W_{v,h})=
 \widehat\mu(v+R^{-1}h)W_{Rv,R^{-1}h},
```

```math
 \mathcal C_\mu^2(W_{v,h})=
 \widehat\mu(v+R^{-1}h)\widehat\mu(Rv+R^{-2}h)
 W_{R^2v,R^{-2}h}.                                                \tag{QR.27}
```

Both formulas follow by conjugating successively by the modulation, actor and
translation in (QR.26); the two phase factors multiply, with no missing scalar.
The map from $`(v,h)`$ to the two tested arguments is bijective, since its
kernel requires $`h=-Rv`$ and $`(R-R^{-1})v=0`$.

**Theorem F (fixed-pair exact norms and twirl).**

```math
 \|\mathcal C_\mu-\mathcal E\|_{2\to2}=1,\qquad
 \|\mathcal C_\mu^2-\mathcal E\|_{2\to2}=\Delta.                  \tag{QR.28}
```

The first equality uses any nonzero $`(v,-Rv)`$; the second upper bound follows
because at least one argument is nonzero, and equality follows by making the
other zero and choosing a bias-maximizing argument. These are singular-norm
statements, not assertions about eigenvalues. Uniform $`\mu`$ therefore gives
$`\mathcal C_\mu^2=\mathcal E`$ exactly, including diamond norm.

For uniform $`\mu`$, one round annihilates every nonconstant diagonal, while its
off-diagonal norm is one. The density matrix
$`I/d+(W_{v,-Rv}+W_{v,-Rv}^*)/(4d)`$ is positive with uniform populations and
has unchanged HS error after that round. Thus this repair does not inherit
NI's $`p^{-2}`$ one-step coherence bound.

The complete two-round channel has a standard group control. Up to global phase,

```math
 V_sV_t=W_{s+Rt,\,R^{-1}s+R^{-2}t}D_{R^2}.                        \tag{QR.29}
```

This pair-label map is bijective because $`R^2-I`$ is invertible. Uniform
independent $`s,t`$ give precisely a full Weyl twirl, with $`d^2`$ keys and
entropy $`2\log_2d`$. Correlated $`s,t`$ can instead compile any prescribed
Weyl distribution into two actual operations. Such a correlated schedule is
not the power $`\mathcal C_\mu^2`$ unless its two marginals are independent.

### 6.1. A sharper direct state bound

**Theorem P (two-subalgebra purity bound).** Write $`d=s^2`$ and assume
$`\Delta\leq\delta\leq1`$. Every density matrix satisfies

```math
 \|\mathcal C_\mu^2(\rho)-I/d\|_2^2\leq
 \delta^4(1-1/d)+2(\delta^2-\delta^4)(1/s-1/d),
```

```math
 e_1(\mathcal C_\mu^2)^2\leq
 (d-1)\delta^4+2(s-1)(\delta^2-\delta^4).                          \tag{QR.30}
```

The purity bound is sharp for the stated fixed symplectic family and the
mixture $`\mu=\delta\delta_0+(1-\delta)\mathrm{Unif}(U)`$.
Sharpness of the final trace conversion is not asserted.

**Proof.** For an invertible self-adjoint actor $`A`$, the graph Weyls
$`\{W_{v,-Av}:v\in U\}`$ span a $`*`$-algebra $`\mathcal A_A`$ of dimension
$`d`$. Their commutator is $`\mathsf B(-2Av,w)`$, a nondegenerate pairing.
Any central element has zero nonidentity Weyl coefficients, so the center is
scalar. Finite-dimensional $`*`$-algebra structure therefore identifies
$`\mathcal A_A\cong M_s\otimes I_s`$ acting on dimension $`d=s^2`$.
Its HS projection is the conditional expectation
$`P_A(\rho)=\mathrm{Tr}_2(\rho)\otimes I_s/s`$ in these coordinates.
In particular
$`\|P_A\rho-I/d\|_2^2\leq1/s-1/d`$.

The exceptional graphs where one argument of (QR.27) vanishes are
$`\{(v,-Rv)\}`$ and $`\{(v,-R^3v)\}`$. They intersect only at zero.
Their traceless spans are orthogonal. On these spans the multiplier is at most
$`\delta`$; on their complement it is at most $`\delta^2`$. Orthogonal
decomposition gives the stronger state-dependent inequality

```math
 \|\mathcal C_\mu^2(\rho)-I/d\|_2^2\leq
 \delta^4\|\rho-I/d\|_2^2+
 (\delta^2-\delta^4)\sum_{A\in\{R,R^3\}}\|P_A\rho-I/d\|_2^2.
                                                                    \tag{QR.31}
```

Inserting the two projection bounds proves the first statement; multiplying by
$`d`$ proves the trace bound. The use of an upper bias $`\delta`$ is valid
directly from the separate bounds on the exceptional and remaining components.

For sharpness, choose the actor-stable Lagrangian subgroup $`L_0\subset U`$
given by the first coordinate of every symplectic pair. Its size is $`s`$.
The pure state $`s^{-1/2}\sum_{u\in L_0}|u\rangle`$ has Weyl support
$`L_0\times L_0`$. Each exceptional graph meets this support in exactly
$`s`$ labels. For the displayed mixture every nonzero Fourier bias is exactly
$`\delta`$, so the squared-error count gives equality in the purity bound.
$`\square`$

This improves the generic $`\sqrt d\,\Delta`$ state bound by exploiting
positivity and noncommutative subalgebras. Independent weak phase and weak
translation twirls have exceptional abelian diagonal algebras, whose projected
state purity can be one; this argument does not apply to them. The complete
correlated Weyl control (QR.29) has exactly the same subalgebras and bound.
The improvement is thus structural, not exclusive to Bol loops.

### 6.2. Explicit independent-round sampling

Apply Lemma B with $`\ell=N`$ on the field coordinates and sample the ring
translation uniformly. For $`0<\varepsilon\leq1`$ choose
$`\delta^2=\varepsilon^2/(3\sqrt D)`$ and
$`r=\lceil\log_3(3/\delta)\rceil`$. Here $`r\geq N/4+2`$, so
$`s=\lceil N/r\rceil\leq4`$ and the bias is at most $`3/3^r\leq\delta`$.
Each round has

```math
 K=49\cdot3^{2r}<11907\sqrt D/\varepsilon^2.                       \tag{QR.32}
```

The ring channel depolarizes after two independent rounds, so the state theorem
uses $`D`$ in place of $`d`$ in (QR.30), even on internally entangled inputs.
Its right side is at most $`\varepsilon^4/9+2\varepsilon^2/3\leq\varepsilon^2`$.
The total $`K^2`$ equally likely schedules have entropy

```math
 2\log_2K<\log_2D+4\log_2(1/\varepsilon)+2\log_2 11907.
                                                                    \tag{QR.33}
```

This is a genuine sparsification of the fixed-pair translation average. It is
weaker in key length than the one-call repair, but it retains that single pair.
Its diagonal HS restriction contracts by at most $`\delta^2`$ in two rounds,
while the full two-round norm is its actual bias $`\Delta`$. The direction of
the two rates has changed. More iterations give the safe bound
$`e_2(\mathcal C_\mu^{2t})\leq\Delta^t`$ with fresh independent samples;
we claim no preserved exact dense-channel rate.

## 7. Gate model, uniformity and compilation

The physical layout for (QR.15) is $`N`$ qutrits and two seven-level qudits.
The field $`E=\mathbf F_3[X]/(X^6+X+2)`$, its trace matrix and an order-seven
$`\lambda`$ are fixed once and for all; the checker verifies this presentation.
Standard symplectic coordinates turn $`M_h`$ into single-qudit phases, $`X_v`$
into single-qudit shifts, and the actor into parallel six-qutrit multiplication
blocks plus two seven-level permutations. A fixed finite gate set consisting
of qutrit shifts, phases and SUM gates, together with the seven-level shifts,
phases and multiplication by two, implements them exactly. The determinant of
the six-coordinate multiplication map is
$`\mathrm{Norm}_{E/\mathbf F_3}(\lambda)=\lambda^{364}=1`$.
It lies in $`\mathrm{SL}_6(\mathbf F_3)`$, which is generated by the
elementary SUM transvections. Gaussian elimination therefore decomposes it
using the stated gate set into a constant-size circuit; no extra coordinate
scaling gate is implicit.

Thus a sampled native operator has $`O(N)`$ gates, $`O(1)`$ quantum depth on
disjoint constant-size blocks, and no quantum ancillas. The classical description
has $`O(N)`$ field symbols. The same costs apply to the Weyl/group control;
calling the compiled circuit one defect does not reduce its physical gate count.
The fixed-pair repair uses two such rounds. A two-round product can also be
compiled as one Weyl displacement and a fixed squared actor, preserving its law.

For Lemma B, a degree-$`r`$ irreducible polynomial over $`\mathbf F_3`$ is
generated deterministically using Shoup [SHOUP, Theorem 3.2]. At fixed
characteristic its preprocessing costs $`O(r^{4+c})`$ field operations for any
fixed $`c>0`$; no lexicographic exponential search or random advice is hidden.
Precomputing the trace functional is polynomial in $`r`$. Schoolbook arithmetic
generates $`\ell`$ outputs in $`O(\ell r^2)`$ $`\mathbf F_3`$ operations,
with $`O(\ell+r)`$ storage including the whole output: compute
$`\mathrm{Tr}(ce_i)`$ on demand, without storing an $`r\times r`$ trace
matrix. The one-call construction has $`r=O(N+\log(1/\varepsilon))`$.
Preprocessing and the key-to-circuit map are deterministic polynomial time;
exact fair-bit sampling is expected polynomial time, with the unbounded
worst-case tail specified in Section 2. The finite checker uses
explicit small irreducibles, not an implementation or benchmark of Shoup's full
large-degree algorithm. Classical latency is charged separately from quantum depth.

For standard qubits, encode each qutrit in two qubits and each seven-level
qudit in three, using $`2N+6`$ physical qubits. The promise is an input in the
logical $`d`$-dimensional subspace, and the target remains $`I_d/d`$ there.
Mixing all physical qubits instead would give the wrong target. Extend every
fixed local gate unitarily to unused levels. Compiling to an inverse-closed finite
universal gate set, for example Clifford+$`T`$ with inverses, has the conservative
Solovay--Kitaev bounds $`O(N\log^c(N/\varepsilon))`$ gates and
$`O(\log^c(N/\varepsilon))`$ depth for a fixed constant $`c`$; the classical
compiler is polynomial in that precision parameter [SK]. These are approximation
bounds, not exact Clifford+$`T`$ realizations of third/seventh roots of unity.

More explicitly, for $`G=O(N)`$ gates per round, compile each local gate within
$`\varepsilon/(8G)`$ in operator norm. One round then has at most
$`\varepsilon/8`$ unitary error and $`\varepsilon/4`$ channel diamond error;
two rounds accumulate at most $`\varepsilon/2`$. Choose statistical error
$`\varepsilon/2`$ in the preceding samplers. The guarantee is for the encoded
input channel and allows correspondingly bounded leakage. Fixed local gate
synthesis needs no asymptotically growing quantum workspace.

## 8. Benchmarks in matched criteria

All trace errors below use (QR.8), and all expander comparisons use the sufficient
time $`T(\alpha)=\lceil\log(\sqrt{d-1}/\varepsilon)/(-\log\alpha)\rceil`$.
For diamond guarantees replace $`\sqrt{d-1}`$ by $`d`$ and account for circuit
error. Entropies are converted to fair bits as in Section 2. Gates/depth exclude
the separately stated classical key generation.

| Method | Dimension and guarantee | Key/support cost | Quantum execution and qualification |
| --- | --- | --- | --- |
| Exact Weyl twirl | Any finite abelian label group; exact $`\mathcal E`$, diamond zero | $`d^2`$ keys, $`2\log_2d`$ entropy | $`O(N)`$ local fixed-qudit gates, constant depth; exact same dimension/model as our family |
| Exact phase twirl | Every state with uniform point populations; exact $`I/d`$ | $`d`$ keys, $`\log_2d`$ entropy | $`O(N)`$ phase gates, depth one; no general reference guarantee |
| Dense channel, Theorem QD | Same fixed family; diamond error at most $`2(517/1029)^t`$ | Literal entropy $`3t\log_2(21d)`$ | $`O(tN)`$ fixed-qudit gates and $`O(t)`$ depth; exact twirling uses fewer keys |
| Theorem S | $`d=49\cdot3^N`$, arbitrary states, trace error $`\varepsilon`$ | $`M\leq\min(d^2,3969d/\varepsilon^2)`$ | One actual defect; $`O(N)`$ gates, constant qudit depth; identical Weyl control |
| Theorem P with (QR.32) | Same dimension, arbitrary states, trace error $`\varepsilon`$ | Two independent $`K`$-choice rounds, $`K=O(\sqrt d/\varepsilon^2)`$ | Two uses of one translated defect pair; same physical asymptotic gate/depth cost |
| Dickinson--Nayak [DN], Theorem 1.2 | $`d=2^a`$, arbitrary states in trace norm | At most $`16d/\varepsilon^2`$ Pauli keys, $`a+2\log_2(1/\varepsilon)+4`$ bits, with rounding | $`a`$ single-qubit Paulis, depth one, no quantum ancilla; deterministic index generation $`\widetilde O((\log M)^4)`$ |
| Ben-Aroya--Schwartz--Ta-Shma [BST], Theorem 4.6 | $`d=D_0^{8j}`$, constant-degree/gap HS expander | Degree $`D_0^2`$, $`2T(\alpha)\log_2D_0`$ entropy | Polynomial-size circuits in $`\log d`$; finite constant-size seed search; not a depth-one theorem |
| Anshu et al. [ABHHT], Theorem 2.2 | $`d=2^{3s}`$, $`\alpha\leq1-1/(2\cdot10^8)`$ | 16 choices, four fresh bits each step | Each generator a depth-one Pauli/CNOT circuit, $`O(\log d)`$ gates, periodic 1D bounded range |
| Iyer et al. [IJJS], Corollary 1.2, Section 6.1 | Every logical $`d\geq2`$, degree six, ideal rate $`2\sqrt5/6`$ | $`T(\alpha)\log_2 6`$ entropy, allowing the compiled error budget | Per-use gate count $`O((\log d+\log(1/\eta))^3\log(1/\eta))`$; enlarged oscillator registers, uniform precision preprocessing and accumulation are charged below |
| Jain [JAIN], Theorems D.1/E.1 | $`d=(q^{2a}-1)/2`$, fixed odd prime power $`q`$, rate $`2\sqrt q/(q+1)`$ | $`q+1`$ choices per step | $`O(\log^2d)`$ gates/depth, $`O(\log d)`$ ancilla, $`\widetilde O(\log^5d)`$ preprocessing; input already in the odd logical subspace |

The qubit-only rows do not directly act on our odd-dimensional logical space.
Padding and mixing a larger space changes the target and is not a free comparison.
The exact Weyl control is on precisely the same space and gates; IJJS also supplies
an arbitrary-dimension expander comparison. The DN result is an additional strong
benchmark when qubits are the requested hardware, not a silently padded proof
for our dimension. Theorem S matches the $`O(d/\varepsilon^2)`$ support scale,
with a larger displayed constant and no improvement in accuracy dependence or
depth. The matching Weyl control is exact in our dimension. For fixed
$`\varepsilon<1`$, the key entropy is within a constant of the support lower
bound (QR.10); we do not claim optimal dependence on $`\varepsilon`$ for all
mixed-unitary randomizers.

For the arbitrary-dimension IJJS comparison, their Theorem 1.1 and Algorithm 1
use two oscillator registers of size $`L=O((d-1)^{2.25}/\eta^{3.25})`$ each,
so their enlarged data space requires $`O(\log d+\log(1/\eta))`$ qubits.
This is ancillary space beyond a bare logical input, not a zero-ancilla claim.
The gate count in their equation (92) also provides a conservative upper bound
on depth and any additional temporary workspace; we do not assert an optimized
workspace bound for the underlying Hermite-transform implementation. Their
Section 1.1 gives classical angle preprocessing polynomial in
$`\log d,\log(1/\eta)`$, using $`O(\log(d/\eta))`$ precision bits.
For $`T`$ iterations, use ideal statistical error $`\varepsilon/2`$ and
per-use implementation error $`\eta\leq\varepsilon/(4T)`$; the induced
channel error accumulates by at most $`2T\eta`$, including with a reference.
Preparation and uncomputation of the oscillator encoding are included in their
gate bound. Neither their ideal spectral constant nor ours makes these costs free.

A simple classical control is also decisive. Let $`\mathcal P`$ be a permutation
channel whose classical mean-zero $`\ell_2`$ norm is $`\alpha`$, and let
$`\mathcal D`$ be the full phase twirl. Then $`\mathcal P\mathcal D`$ has
coherence rate zero and population rate at most $`\alpha`$. One phase key and
$`t`$ permutation keys suffice for $`\mathcal P^t\mathcal D`$, since permutations
commute with dephasing. Charge the $`\log_2d`$ phase entropy and the permutation
choices; they are not free. Uniform translations make this the exact Weyl twirl.
Rapid dephasing alone is therefore not a Bol-specific advantage.

For a nonconstructive state benchmark, DN, Theorem 1.4, samples
$`\lceil37d\varepsilon^{-2}\ln(15/\varepsilon)\rceil`$ unitaries from an exact
randomizing distribution, with failure at most $`e^{-d/2}`$. Theorem W supplies
such a native distribution. This gives a probabilistic native existence bound,
not an explicit efficiently certifiable list; charge its offline random sampling
and storage as in Section 4. Generic Haar sampling is not an efficient gate model.

## 9. Ablations and higher moments

| Change | Exact effect and interpretation |
| --- | --- |
| Replace full corrections by scalar phases | Every conjugation is identity; no state randomization. This tests the chosen correction, not all group channels. |
| Keep only the underlying scalar affine permutations | Population mixing can survive; $`|+\rangle\langle+|`$ is fixed, so arbitrary-state randomization fails. Nontrivial phases are necessary. |
| Remove translation conjugation | All defects fix the point ket at the origin up to phase. Its pure-state error remains $`2(1-1/d)`$. |
| Hold the pair fixed and average all centers | The one-step HS and coherence norm is one; two independent rounds equal $`\mathcal E`$. The actual joint channel is (QR.29). |
| Replace native labels by their Weyl/actor normal form | The complete channel, correlations, resources and every proved guarantee are unchanged. This is the matching group-based control. |
| Independently sample the conjugate factors in the fused adjoint sector | The average becomes $`T\mapsto ATA^*`$, where $`A=\mathbb E V`$; it loses trace preservation for every nontrivial law. For the fixed-pair uniform-center representatives its output trace is exactly $`1/d`$. This is an algebraic diagnostic, not a physical randomizer. |
| Remove correlations from the two-round Weyl labels | The selected distribution changes. Independent phase/translation controls can still randomize, but the exceptional subalgebras and Theorem P need not survive. |
| Use an associative loop's literal defects | They are identity. Independently chosen group Weyls remain an equally strong randomizer; associative loops are not generally weaker resources. |
| Add a Fourier basis change to full shear dephasing | $`\mathcal D\mathrm{Ad}_F\mathcal D=\mathcal E`$ for the finite abelian Fourier transform. This exact standard repair uses $`d^2`$ phase schedules and needs no Bol structure. |

The Fourier identity follows because dephasing makes an input diagonal and every
Fourier column has constant squared modulus $`1/d`$. With only the added Fourier
unitary there is no randomization; with the native full shear twirl the identity
holds. This analyzes the joint construction and also shows that its benefit is
already the standard complementary-basis dephasing mechanism. In degenerate
sectors (QR.5) is not full dephasing, so that formula cannot be invoked without
supplying the missing non-native phase operations.

### 9.1. Decoupling the fused conjugate sector

The adjoint channel is represented on vectorized matrices by the synchronized
average $`\mathbb E[V\otimes\overline V]`$, the conjugate-sector specialization
of NI's fusion. Independently sampling its two factors gives
$`A\otimes\overline A`$, where $`A=\mathbb EV`$, and hence the linear map
$`T\mapsto ATA^*`$. This map is trace preserving precisely when
$`A^*A=I`$. In equal input/output dimension this makes $`A`$ unitary, and

```math
 \mathbb E\|V-A\|_2^2=d-\|A\|_2^2=0
```

then forces every positive-probability representative $`V`$ to be identical.
The original dense law is nontrivial, so this independently keyed replacement
cannot retain its channel interpretation. Unlike conjugation, it also depends
on the chosen global phases of those representatives.

The exact fixed-pair representatives (QR.26) give a particularly explicit
control. Averaging all centers, for each output/input pair $`s,u`$ the unique
contributing center is $`t=s-Ru`$, whence

```math
 A_{s,u}=d^{-1}\mathsf B(s-Ru,u)=d^{-1}\mathsf B(s,u)
       =d^{-1/2}(F_{\mathsf B})_{s,u}.                            \tag{QR.33a}
```

The middle equality uses $`b(Ru,u)=0`$, and nondegeneracy makes
$`F_{\mathsf B}`$ unitary. The decoupled map is exactly
$`d^{-1}F_{\mathsf B}TF_{\mathsf B}^*`$; its trace on states is $`1/d`$.
Even if it were renormalized, it would be a unitary channel. The finite checker
verifies every matrix entry and the Fourier column orthogonality for the full
49-dimensional ring factor. This tests the lost conjugate-sector correlation,
separately from the two-round sampling correlations in (QR.29).

Independent *physical* channels on two tensor factors would instead have target
dimension $`d^2`$ and a different task. No claimed resource advantage is based
on comparing that task with a non-trace-preserving map or on silently assigning
the old dense NI spectrum to the decoupled average.

### 9.2. Higher moments

**Proposition M (quantitative monomial second-moment obstruction).** For every
ensemble of monomial unitaries in dimension $`d>1`$, let
$`\mathcal M_2(T)=\mathbb E U^{\otimes2}T(U^*)^{\otimes2}`$ and let
$`\mathcal H_2`$ be the Haar second-moment twirl. Then

```math
 \|\mathcal M_2-\mathcal H_2\|_{2\to2}=1.
                                                                    \tag{QR.34}
```

Indeed $`Q_\Delta=\sum_i|i,i\rangle\langle i,i|`$ is fixed by every tensor
square. Haar averaging gives $`\mathcal H_2(Q_\Delta)=2\Pi_{\rm sym}/(d+1)`$.
The nonzero difference is Haar-orthogonal and fixed by $`\mathcal M_2`$,
proving the lower bound. Haar projection commutes with and is fixed by each
conjugation; on its orthogonal complement the average is a contraction, giving
the upper bound. On the state $`Q_\Delta/d`$ the trace discrepancy is exactly
$`2(d-1)/(d+1)`$, by the two eigenvalues inside the symmetric subspace.
The obstruction survives every product and iteration of native operations.

Lancien [LANCIEN], Corollaries 2.5 and 3.5, instead samples unitaries from exact
2-designs or $`2k`$-designs to obtain, with high probability, first-moment or
$`k`$-copy expanders with contraction asymptotic to $`2/\sqrt M`$, for
$`M\geq(\log d)^{4+\alpha}`$, fixed $`\alpha>0`$. Its superoperator norm
is the induced HS norm, not an output Schatten-infinity error. The cost depends
on the design sampler. Our monomial ensembles do not meet its design hypothesis.
No higher-design construction is claimed here.

## 10. What has and has not been achieved

The native-operation restriction is natural when a given loop-derived dynamics
is the available hardware/interface. Within that restriction we have a sharp
generator obstruction and an explicit sparse state randomizer with deterministic
polynomial preprocessing and expected polynomial fair-bit sampling.
The proof also identifies exactly how the restriction can recover standard
randomization: at conductor one the full Weyl coset is already available.

The improved fixed-pair purity estimate is a noncommutative structural result,
with an exact equality case. Its source is the symplectic graph subalgebras, not
the existence of a nonassociative multiplication alone. Removing the Bol labels
while retaining their actual operators preserves it. We have found no general
advantage over the strongest applicable quantum or group-based baselines.

The following concrete questions remain open in this work:

1. An efficiently certifiable explicit $`O(N)`$-support approximation to the
   **original dense measure** retaining separate constant population and coherence
   rates; Theorem C gives the necessary support scale, while (QR.19) only gives
   existence. This is a structured native sampling question, not an open question
   about generic constant-degree expanders.
2. Exact one-call Weyl reachability at higher conductor, beyond the zero/primitive
   obstruction proved in Section 5; the two-call uniform repair remains available.
3. A useful operation restriction or a different task in which the actual loop
   marking/correlations improve resources beyond a matching Weyl/actor control.
   Such a benefit is not established by the current first-moment theory.

Neither this work nor its obstructions classify Bol loops. The nondegenerate
sector theorem, the degenerate fixed states and the monomial second-moment
obstruction have different quantifiers and are not interchangeable.

## References and reproducibility

The [code guide](../code/README.md) and [evidence record](../evidence/bol-randomization-reproducibility.md)
state exact commands, finite scopes, source pins and review status. The new
programs use exact arithmetic and do not build the enormous full channel.
They corroborate the proofs, not replace them. The scientific contribution and
the current-source comparison have been kept separate from claims of historical
priority.

* **NI/AQ:** The exact repository sources linked in the introduction; NI,
  Theorems Q/Q1 and Sections 8.2--8.3, is the recovered dense-channel baseline.
* **DN:** P. A. Dickinson and A. Nayak, *Approximate Randomization of Quantum
  States With Fewer Bits of Key*, 1 June 2006, Theorems 1.2/1.4, Section 2,
  and Appendix B, Proposition B.1 (the AGHP small-bias construction).
  [Author PDF](https://www.math.uwaterloo.ca/~anayak/papers/DickinsonN06.pdf).
* **BST:** A. Ben-Aroya, O. Schwartz and A. Ta-Shma, *Quantum Expanders:
  Motivation and Constructions*, Theory of Computing 6 (2010), 47--79,
  Theorem 4.6, DOI 10.4086/toc.2010.v006a003.
  [Primary PDF](https://theoryofcomputing.org/articles/v006a003/v006a003.pdf).
* **ABHHT:** A. Anshu, S. Balasubramanian, J. Haferkamp, A. W. Harrow and X. Tan,
  *Depth-1 expanders on the unitary group and applications*, arXiv:2609.01605v1,
  1 September 2026, Theorem 2.2. [Record](https://arxiv.org/abs/2609.01605).
  The full primary manuscript was inspected through an
  [arXiv mirror](https://arxiv.cnoctave.top/pdf/2609.01605) after the official
  PDF endpoint failed; its title page identifies the version. Bounded range on
  a periodic line is not silently identified with strict nearest-neighbor depth one.
* **IJJS:** V. Iyer, S. Jain, S. Jordan and R. D. Somma, *Efficient quantum
  circuits for high-dimensional representations of SU(n) and Ramanujan quantum
  expanders*, arXiv:2602.15180v1, 16 February 2026, Corollary 1.2, Section 6.1
  and Appendix C. [Primary text](https://arxiv.org/html/2602.15180v1).
* **JAIN:** S. Jain, *Ramanujan quantum expanders from the Weil representation*,
  arXiv:2609.38075v1, 29 September 2026, Theorems D.1/E.1 and Section E.1.
  [Primary text](https://arxiv.org/html/2609.38075v1).
* **LANCIEN:** C. Lancien, *Optimal quantum (tensor product) expanders from
  unitary designs*, arXiv:2409.17971v3, 19 February 2026, Corollaries 2.5/3.5;
  IMRN 2026, rnaf383. [Primary text](https://arxiv.org/html/2409.17971v3).
* **SHOUP:** V. Shoup, *New Algorithms for Finding Irreducible Polynomials over
  Finite Fields*, Mathematics of Computation 54 (1990), 435--447, Theorem 3.2,
  DOI 10.1090/S0025-5718-1990-0993933-0. [Author PDF](https://www.shoup.net/papers/detirred.pdf).
  The statement on rendered PDF page 3 was inspected; its text extraction is corrupt.
* **TROPP:** J. A. Tropp, *User-Friendly Tail Bounds for Sums of Random Matrices*,
  Foundations of Computational Mathematics 12 (2012), 389--434, Theorem 1.3,
  arXiv:1004.4389v7, 15 June 2011. [Primary preprint](https://arxiv.org/abs/1004.4389v7).
* **SK:** C. M. Dawson and M. A. Nielsen, *The Solovay--Kitaev algorithm*,
  Quantum Information and Computation 6 (2006), 81--95, Section 2 and the
  algorithmic bounds in Section 3, arXiv:quant-ph/0505030v2, 23 August 2005.
  [Primary preprint](https://arxiv.org/abs/quant-ph/0505030v2).
