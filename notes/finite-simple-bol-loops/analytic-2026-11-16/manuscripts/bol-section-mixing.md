# Exact mixing from a Bol section

Mira Cult

## Scope and source

This manuscript proves a spectral theorem, an exact total-variation formula,
and an optimal-weighting statement for actual left translations of an explicit
infinite family of proper left Bol loops. The Fourier tools are standard. The
claimed contribution is the particular section-selected averaging operator and
its quantitative consequences; no new general representation theory or
historical-priority claim is made.

The starting formula is the restricted-section product in the public
[alternating-form construction, manuscript 0025, Section 4](https://github.com/Mira-Cult/math/blob/f54b5376cb098e52d56ba0e599598d92ff6978a3/notes/finite-simple-bol-loops/manuscripts/0025-alternating-form-construction.md).
Its displayed one-plane product is generalized here to an arbitrary symplectic
dimension and to any cyclic scalar subgroup. The loop axioms and proper Bol
property are proved directly below. Thus the results here do not assume the
public draft's simplicity, full-folder, isomorphism, or G-loop interfaces.
Identifying a member with a subloop of the entire simple-loop construction
continues to require that construction's stated interfaces. The loops used here
are not claimed to be simple.

Local theorem labels are manuscript labels, not permanent claim IDs. The
arithmetic extension is proved in [the local manuscript](bol-section-local.md).
The [controls and literature comparison](bol-section-controls.md) identify the
known spectral baseline and the precise contribution of the marked section.

## 1. Family, observable, and quantitative target

Let $Q$ be an odd prime power, let $d\geq1$, and let $m\geq2$ divide $Q-1$.
Choose $\eta\in\mathbb F_Q^\times$ of exact order $m$. The integer $m$ may be
even. Put

```math
X=Y=\mathbb F_Q^d,\qquad V=X\oplus Y,\qquad
\gamma((x,y),(x',y'))=x\cdot y'-y\cdot x'.
```

On $L=V\times C_m\times\mathbb F_Q$ define

```math
(u,t,s)\circ(v,a,h)
 =(u+\eta^t v,\ t+a,\ s+h-\gamma(u,v)).                 \tag{1.1}
```

The selected subloop and averaging measure are

```math
H=\{((u,0),t,0):u\in X,\ t\in C_m\},\qquad
\mu_H(h)=\frac1{mQ^d}\quad(h\in H).
```

Let $\ell_h(z)=h\circ z$ be the actual left translation, and let
$U_hf=f\circ\ell_h^{-1}$. Define

```math
P=\frac1{mQ^d}\sum_{h\in H}U_h.
```

The inverse map preserves $H$, so this also equals the direct-transition
Markov operator $Pf(z)=\mathbb E_{h\in H}f(h\circ z)$. All $\ell^2$ norms use
uniform probability measure on the invariant component under discussion.
This normalization makes $P$ a self-adjoint Markov contraction.

The asymptotic parameters are $Q,d,m$ subject to the displayed hypotheses.
The family contains all $Q$ with $m=Q-1$ and $d=1$, as well as fixed-$m$
families of unbounded field size and dimension. The nontrivial components have
$N=mQ^{d+1}$ states and transition degree $D=mQ^d$. We prove the exact
mean-zero norm $1/m$ and an exact mixing formula with no factor depending on
$N$. In particular, when $m=Q-1$ the two-step total-variation distance is

```math
\boxed{\ \|P^2(z,\cdot)-\mathrm{Unif}\|_{\rm TV}=\frac{2}{Q^2}.\ } \tag{1.2}
```

Every exceptional component and character sector is accounted for below.
The applicable symplectic-polar graph bound already implies the norm upper
bound $1/m$; see Section 8 and the controls. Individual fixed-$t$ averages have
norm one, so the triangle inequality alone gives no contraction. The usual conversion of an $\ell^2$ spectral bound to
point-start total variation introduces a factor of order $\sqrt N$; the exact
formula here removes it for this family. These are mathematical comparisons,
not assertions that this walk is absent from all graph-theoretic literature.

## 2. Direct loop verification and operator corrections

### Proposition L: the proper Bol law

Equation (1.1) defines a left Bol loop of order $mQ^{2d+1}$. Its identity is
$(0,0,0)$, and

```math
(u,t,s)^{-1}=(-\eta^{-t}u,-t,-s).
```

It satisfies the left inverse property and is not Moufang.

**Proof.** In each division equation the $C_m$ coordinate is determined first,
then the vector coordinate, and finally the central coordinate. Multiplication
by every $\eta^t$ is invertible, so both divisions are unique. The identity,
inverse formula, and $\ell_{x^{-1}}=\ell_x^{-1}$ follow by substitution and
$\gamma(u,u)=0$.

For the left Bol identity, write $A=(u,t,s)$, $B=(v,a,h)$,
$C=(w,b,k)$, $\alpha=\eta^t$, and $\beta=\eta^a$. Both
$A\circ(B\circ(A\circ C))$ and $(A\circ(B\circ A))\circ C$ have coordinates

```math
\left((1+\alpha\beta)u+\alpha v+\alpha^2\beta w,
      2t+a+b,
      2s+h+k-(1+\alpha\beta)\gamma(u,w)-\alpha\gamma(v,w)\right).
```

Choose $v,w\in V$ with $\gamma(v,w)=1$, and put
$A=(0,1,0)$, $B=(v,0,0)$, $C=(w,0,0)$. The two sides of

```math
(A\circ B)\circ(C\circ A)=(A\circ(B\circ C))\circ A
```

have central coordinates $-\eta$ and $-1$, respectively, and equal remaining
coordinates. They differ because $\eta\ne1$. This proves properness. $\square$

The restriction to $H$ is the associative semidirect product
$X\rtimes C_m$, because $\gamma$ vanishes on $X\oplus0$. Nevertheless its
left translations on all of $L$ are not a group representation.

### Proposition C: the correction shear and its coherence

For $c\in X$ define

```math
C_c(x,y,b,s)=(x,y,b,s+c\cdot y).
```

For $h=(u,t)$ and $k=(v,a)$ in $H$, identifying them with their selected loop
elements, one has

```math
\ell_h\ell_k=\ell_{hk}C_{c(h,k)},\qquad
c(h,k)=(1-\eta^a)u+(\eta^t-1)v.                     \tag{2.1}
```

For $l=(w,b)\in H$,

```math
C_c\ell_l=\ell_l C_{\eta^b c},
\qquad
c(hk,l)+\eta^b c(h,k)=c(h,kl)+c(k,l).               \tag{2.2}
```

**Proof.** The vector and cyclic coordinates of $\ell_h\ell_k$ and
$\ell_{hk}$ agree. Their central-coordinate difference, evaluated at
$(x,y,b,s)$, is
$((1-\eta^a)u+(\eta^t-1)v)\cdot y$. This proves (2.1). The first identity
in (2.2) follows from the scaling $y\mapsto\eta^b y$. Expanding either side
of the second identity gives

```math
(1-\eta^{a+b})u+(\eta^t-\eta^b)v+(\eta^{t+a}-1)w.
```

Thus (2.2) is also precisely the consistency condition obtained by associating
the three permutation factors in either order. $\square$

These are identities of genuine permutations and hence of their unitary
pullbacks. No faithful multiplicative representation of the nonassociative
loop is assumed.

## 3. The invariant components

In coordinates $(x,y,a,s)$ the Markov operator is

```math
Pf(x,y,a,s)=\frac1{mQ^d}
 \sum_{t\in C_m}\sum_{u\in X}
 f(u+\eta^t x,\eta^t y,a+t,s-u\cdot y).             \tag{3.1}
```

The quantity $r=\eta^{-a}y$ is unchanged by every selected left translation.
For $r\ne0$, let

```math
\mathcal C_r=\{(x,y,a,s):\eta^{-a}y=r\}.
```

It has $N=mQ^{d+1}$ points. In co-moving coordinates $X=\eta^{-a}x$,
the restriction to $\mathcal C_r$ becomes

```math
Pf(X,a,s)=\frac1{mQ^d}\sum_{b\in C_m}\sum_{Y\in X}
 f\bigl(Y,b,s-\eta^{a+b}(Y-X)\cdot r\bigr).          \tag{3.2}
```

If $r=0$, then $y=0$ and $s$ is unchanged. Each set with fixed $s$ is a
component of size $mQ^d$; (3.1) is uniform averaging on it in one step.

For $r\ne0$, the components are exactly $\mathcal C_r$. One direct check is
as follows. Fix initial torus coordinate $a_0$ and final coordinate $a_2$.
The two slopes in a two-step path through $a_1$ are
$\eta^{a_0+a_1}$ and $\eta^{a_1+a_2}$. If $a_2\ne a_0$, they differ.
Since $r\ne0$, the map from two vector increments to their sum and the
corresponding central increment is surjective onto $X\times\mathbb F_Q$.
Thus two steps reach every state with any $a_2\ne a_0$. One more step reaches
every remaining state. In particular each $\mathcal C_r$ is connected.

There are $Q^d-1$ generic components and $Q$ exceptional components, so the
whole operator has $Q^d+Q-1$ independent stationary functions. A claim of
mixing on the entire loop without this decomposition would be false.

## 4. Complete spectrum and a cubic operator identity

### Theorem S: exact spectrum

Fix $r\ne0$, and let $J_r$ be uniform averaging on $\mathcal C_r$. Then

```math
P^3=J_r+\frac1{m^2}(P-J_r),\qquad
\|P-J_r\|_{2\to2}=\frac1m.                         \tag{4.1}
```

The complete eigenvalue list on this component is

| Eigenvalue | Multiplicity |
|---|---:|
| $1$ | $1$ |
| $1/m$ | $(Q-1)m(m+1)/2$ |
| $-1/m$ | $(Q-1)m(m-1)/2$ |
| $0$ | $mQ^{d+1}-1-m^2(Q-1)$ |

The formulas hold for even as well as odd $m$.

**Proof.** Fix a nontrivial additive character $\psi$ of $\mathbb F_Q$.
Fourier expansion in $X$ and $s$ decomposes the space into functions

```math
f(X,a,s)=\psi(\xi\cdot X+\nu s)F(a),
\qquad \xi\in\mathbb F_Q^d,\quad \nu\in\mathbb F_Q.
```

Nondegeneracy of the finite-field trace pairing makes this a complete
orthogonal decomposition, including when $Q$ is not prime. Substitution into
(3.2) and orthogonality in $Y$ give

```math
Pf(X,a,s)=\frac1m
 \sum_{b:\,\xi=\nu\eta^{a+b}r}
 \psi(\xi\cdot X+\nu s)F(b).                       \tag{4.2}
```

For $\nu=0$, only $\xi=0$ survives and the remaining cyclic coordinate is
averaged uniformly. This contributes the single eigenvalue $1$ and otherwise
zero.

For $\nu\ne0$, the $m$ frequencies $\nu\eta^j r$ are distinct. All other
frequencies are killed. At $\xi=\nu\eta^j r$, equation (4.2) is

```math
\frac1mR_j,\qquad (R_jF)(a)=F(j-a).                 \tag{4.3}
```

Each $R_j$ is a permutation involution. Its multiplicities for $+1$ and $-1$
are $(m+f_j)/2$ and $(m-f_j)/2$, where
$f_j=\#\{a\in C_m:2a=j\}$. For odd $m$, $f_j=1$. For even $m$ it can be
zero or two, but in all cases

```math
\sum_{j\in C_m} f_j=m,
```

because each $a$ contributes once, to $j=2a$. Summing over all $m$ frequencies
and all $Q-1$ nontrivial central characters gives the displayed multiplicities.
The remaining dimensions give the zero multiplicity. The spectral list proves
(4.1). $\square$

For the integer adjacency matrix $K=DP$, $D=mQ^d$, the same identity is

```math
K^3=Q^{2d}K+(m^2-1)Q^{2d-1}\mathbf1\mathbf1^{\mathsf T}. \tag{4.4}
```

This is useful for an exact integer check, without inferring a theorem from
floating-point eigenvalues.

### Corollary P: powers and correlations

For $k\ge0$ in the odd formula and $k\ge1$ in the even formula,

```math
P^{2k+1}=J_r+m^{-2k}(P-J_r),
\qquad
P^{2k}=J_r+m^{-(2k-2)}(P^2-J_r).                    \tag{4.5}
```

In particular, for mean-zero $f,g\in\ell^2(\mathcal C_r)$,

```math
|\langle f,P^n g\rangle|
 \le m^{-n}\|f\|_2\|g\|_2.                         \tag{4.6}
```

The operator norm in (4.6) is sharp at every $n$. On the whole loop, replace
$J_r$ by conditional averaging over all the components described in Section 3.

## 5. Exact point-start mixing

Total variation is normalized as
$\|\mu-\nu\|_{\rm TV}=\tfrac12\sum_z|\mu(z)-\nu(z)|$.

### Theorem TV: the mixing formula

For every $r\ne0$, starting state $z\in\mathcal C_r$, and integer $n\ge1$,

```math
\|P^n(z,\cdot)-\mathrm{Unif}(\mathcal C_r)\|_{\rm TV}
 =m^{-(n-1)}(1-Q^{-1})
 \begin{cases}
 1,&n\text{ odd},\\
 1-(m-1)/Q,&n\text{ even}.
 \end{cases}                                      \tag{5.1}
```

**Proof.** The one-step distribution is uniform on $mQ^d$ states, one for
each pair $(Y,b)$ in (3.2). These states are distinct. Thus its distance from
the uniform measure on $mQ^{d+1}$ states is $1-Q^{-1}$.

For two steps, use the slope calculation in Section 3. Conditional on any
final torus coordinate $a_2\ne a_0$, the pair $(X,s)$ is exactly uniform.
When $a_2=a_0$, both slopes coincide. As $a_1$ ranges uniformly, their common
value ranges once over $\langle\eta\rangle$. Conditional on this final torus
coordinate, the two-step distribution is therefore the equal mixture of

```math
s-s_0=-c(X-X_0)\cdot r,
\qquad c\in\langle\eta\rangle.                     \tag{5.2}
```

The vector $X$ is uniform. Since $r\ne0$, the scalar
$\ell=(X-X_0)\cdot r$ is uniform in $\mathbb F_Q$. If $\ell=0$, all the
hyperplanes in (5.2) give the single value $s=s_0$, with conditional
distance $1-Q^{-1}$ from uniform $s$. If $\ell\ne0$, they give $m$ distinct
values, with distance $1-m/Q$. The final torus coordinate $a_0$ has
probability $1/m$. Thus

```math
\|P^2(z,\cdot)-\mathrm{Unif}\|_{\rm TV}
 =\frac1m\left[\frac1Q\left(1-\frac1Q\right)
       +\left(1-\frac1Q\right)\left(1-\frac mQ\right)\right]
 =\frac1m(1-Q^{-1})\left(1-\frac{m-1}{Q}\right).
```

Equations (4.5) now scale the one- and two-step differences by the stated
positive constants, proving (5.1). $\square$

For $m=Q-1$, (5.1) gives (1.2). For every fixed $m\ge2$, it also gives
a bound by $m^{-(n-1)}$ independent of $Q$ and $d$. This is an explicit
point-start consequence, not merely a reformulation of the spectral gap.

## 6. Optimal torus weights

Let $w=(w_t)_{t\in C_m}$ be any probability vector. Define $P_w$ by retaining
uniform $u\in X$ in (3.1) and choosing $t$ with distribution $w$.
The operator still preserves uniform measure and the components, but it need
not be self-adjoint. Let $\widehat w(\chi)=\sum_t w_t\chi(t)$.

### Theorem W: exact norm and minimizer

On every $\mathcal C_r$ with $r\ne0$,

```math
\|P_w-J_r\|_{2\to2}
 =\max\left\{\max_t w_t,
              \max_{\chi\ne1}|\widehat w(\chi)|\right\}. \tag{6.1}
```

The unique minimizing probability vector is $w_t=1/m$, and the minimum is
$1/m$.

**Proof.** On the trivial central sector, the operator kills every nonzero
$X$-frequency and is cyclic convolution by $w$ on the remaining coordinate.
Its mean-zero norm is the second term of (6.1).

For $\nu\ne0$, frequencies outside $\nu\langle\eta\rangle r$ are killed.
At frequency $\xi=\nu\eta^j r$, the surviving block is

```math
(A_jF)(a)=w_{j-2a}F(j-a).                           \tag{6.2}
```

This is a diagonal operator followed by a permutation, hence its norm is
$\max_a w_{j-2a}$. The maximum over all $j,a$ is $\max_t w_t$: choosing
$a=0,j=t$ attains any prescribed weight. This argument also handles even
$m$, where $a\mapsto j-2a$ need not be a permutation. Orthogonality of the
blocks proves (6.1).

Every probability vector satisfies $\max_t w_t\ge1/m$, with equality only
at the uniform vector. Uniform weights have all nontrivial cyclic Fourier
coefficients zero, proving the minimizer claim. $\square$

Taking $w$ to be a point mass proves that each individual fixed-$t$ slice
has norm one on the mean-zero space. Thus the gain from their uniform
combination is a simultaneous effect, with the sharp parameter dependence
specified by (6.1).

## 7. An exact forward sampler

The preceding calculation gives an exact sampler on a generic component,
using only forward transitions of the same walk.

Start from any state in $\mathcal C_r$, $r\ne0$. At each step choose the
ordinary independent uniform $u\in X$ and $t\in C_m$. Record the torus
coordinates $a_0,a_1,\ldots$ and the slopes

```math
c_j=\eta^{a_{j-1}+a_j}.
```

Let $T$ be the first $j\ge2$ with $c_j\ne c_1$. After step $T$, take one
additional independent ordinary step and return the resulting state. No
generated state is rejected or changed.

### Proposition E: exactness and expected transition count

The returned state is exactly uniform on $\mathcal C_r$, and

```math
\mathbb E[T+1]=2+\frac m{m-1}\le4.                 \tag{7.1}
```

For odd $m\ge3$, the bound is at most $3.5$. If the explicit finite field
and its arithmetic are supplied, each transition needs $O(d)$ field
operations and uniform sampling of one $d$-vector and one cyclic label.
Equation (7.1) counts transitions, not construction of a finite-field model.

**Proof.** Conditional on the torus path, put
$V_j=X_j-X_{j-1}=\eta^{-a_j}u_j$. These are independent uniform vectors.
The central increments are $-c_j V_j\cdot r$. At time $T$, at least two
$c_j$ differ, so the linear map

```math
(V_1,\ldots,V_T)\longmapsto
 \left(\sum_jV_j,\ -\sum_jc_jV_j\cdot r\right)
```

is onto $X\times\mathbb F_Q$. Its image is consequently uniform. The
stopping decision depends only on the torus path, so conditioning on that
decision does not change the independent vector inputs. Thus $(X_T,s_T)$
is uniform conditional on the entire stopped torus path. One additional
uniform cyclic increment makes $a_{T+1}$ uniform; the accompanying vector
translation and central shear preserve uniformity of $(X,s)$ for each fixed
cyclic increment. This proves exactness, also conditional on $T$.

At each step after the first, conditional on the preceding torus path,
$a_j$ is uniform and exactly one value gives $c_j=c_1$. Therefore
$\Pr(T>n)=m^{-(n-1)}$ for $n\ge1$. Summing the tail gives
$\mathbb E[T]=1+m/(m-1)$ and hence (7.1). $\square$

## 8. What the Bol data contributes, and what it does not

The operative data are the selected translations, the isotropic subspace
$X\oplus0$, the scalar action $\eta$, and the nonzero central pairing with
the transverse coordinate. Equations (2.1)--(2.2) record the correction that
would be lost by pretending that the selected associative subloop acts by a
group representation on the full loop. It produces the changing slopes in
(3.2), which in turn produce the exact mixing formula.

Two controls delimit this contribution; complete identifications and primary
source comparisons are in [the controls](bol-section-controls.md).

1. **Associative control.** Set $\eta=1$ in the same coordinate law, retaining
   an independent cyclic coordinate. This is a class-two group times $C_m$.
   The correction shears vanish. Averaging $H$ is a subgroup projection.
   At fixed $y$, the quantity $s+x\cdot y$ remains invariant, so there is no
   mixing over the proposed generic component. The nonassociative scalar
   coupling is therefore necessary for this particular comparison.
2. **Graph and enveloping-group controls.** Formula (3.2) is itself an
   explicit algebraic graph kernel. The calculation does not assert that its
   spectrum is inaccessible through ordinary group representation theory,
   or that the same graph cannot be realized by an associative group action.
   The explicit symplectic-polar embedding gives the existing norm bound
   $1/m$ by interlacing. The metabelian Cayley realization preserves the whole
   operator when its marked measure is retained. Even arbitrary scalar sets
   give the same finite incidence identity. The section selects the observable; the theorem does
   not establish an analytic property possessed exclusively by Bol loops.

The result is thus an application of established harmonic analysis to a
specified loop-derived family. No improvement on general Weil bounds is
claimed. The [local manuscript](bol-section-local.md) proves the conductor-sensitive
arithmetic extension, including a sharp rank-dependent smoothing law. Neither
result produces a cubic metaplectic automorphic form or a quasi-RH consequence.

## 9. Literature comparison and reproducibility

Gurevich--Hadani's
[quantization paper, arXiv:0705.4556v4](https://arxiv.org/html/0705.4556v4),
Sections 2.2--2.4 and 2.7, supplies canonical Heisenberg intertwiners and their
compatibilities. Their
[self-reducibility paper, arXiv:math/0612765v2](https://arxiv.org/html/math/0612765v2),
Theorems 3.1--3.4, treats torus-eigenstate matrix coefficients. Those theorems
have specific eigenstate and nondegeneracy hypotheses; they do not provide
the section-walk estimate by attaching their notation to a Bol loop. Here the
proof is elementary Fourier orthogonality followed by a finite reflection
calculation.

Johnson--Smith,
[*Matched pairs, permutation representations, and the Bol property*](https://jdhsmith.math.iastate.edu/math/MPBLPR.pdf),
Communications in Algebra 38(8) (2010), 2903--2914,
DOI [10.1080/00927870903095590](https://doi.org/10.1080/00927870903095590),
is a relevant prior interface: Theorem 6.1 concerns doubly stochastic action
matrices, and Section 7 defines Bol actions and gives constructions from
paired left/right group actions. The present claim is the explicit spectral
and mixing theorem above, not priority for stochastic Bol actions.

The [finite verifier](../code/verify_bol_section_mixing.py) builds transition
matrices from the original multiplication, checks the cubic identity in exact
integers, and checks total variation in exact rational arithmetic. Its six
parameter choices include even and odd torus orders, full multiplicative
groups, and dimensions one and two. The smallest 54-element loop is checked
exhaustively for the loop and Bol laws. Larger law checks are explicitly
sampled. [Reproduction instructions](../code/README.md) specify the inputs,
seed and limitations. These computations check the formulas; Sections 2--7
prove the quantified statements.

The sharp remaining question is how far this section-selected mechanism
survives beyond the scalar/isotropic model while preserving a useful
quantitative observable. The local-ring extension attacks one concrete
bridge. Sparse vector sampling, nonscalar stabilizers, and genuinely
interacting central-character rank strata are separate further obligations.

