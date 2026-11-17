# Charged elliptic exchange: forced zero modes, a dynamical repair, and its fusion obstruction

**Mira Cult**



This continuation tests an interaction rather than another permutation
character. Its strongest positive result is a noncoincident, dynamical
elliptic differential system, with a proved modular gauge law, on the
matrix algebra that charge-plus-dual fusion forces us to retain. That
system is the standard Felder mechanism, not a new Bol identity.
The canonical finite charged fusion does not preserve its separate
dynamical parameter spaces: CE6 proves an exact obstruction. No coherent
charged Bol modular functor, new denominator identity, or completion of
the user's stronger sewing target is asserted.

The inputs retain the marked folder, its first axis, and its charged
commutator forms. They are not invariants of an unmarked associated group
alone. Transport and the inherited simplicity assumptions are exactly
those in the linked finite construction.

## CE1. Product-reached zero modes obstruct a scalar-normalized elliptic residue

Let p be odd, let (V,omega) be a nondegenerate symplectic F_p-space of
dimension 2d, and fix psi(t)=exp(2 pi i t/p). On its irreducible
Heisenberg space H, of dimension n=p^d, use the normalized Weyl operators


```math

 T_xT_y=\psi(\omega(x,y)/2)T_{x+y},\qquad
 T_x^{-1}=T_{-x},\qquad
 \operatorname{Tr}(T_x)=n\,\mathbf1_{x=0}.               \tag{CE1.1}

```


These are the Weyl lines in the actual dual-fusion channel
H_ell tensor H_(-ell)=End(H_ell), not a newly attached representation.
For two selected Weyl lifts U=T_u and V_0=T_v, their adjoint actions
commute even when U and V_0 commute only projectively. Set


```math

 A_0=\{X\in\operatorname{End}(H):UX=XU,\ V_0X=XV_0\}.

```


The finite result
[CH3](bol-charged-heisenberg-obstruction.md#ch3-two-holonomies-force-a-large-zero-mode-algebra)
gives


```math

 A_0=\operatorname{span}_{\mathbb C}
       \{T_x:x\in\langle u,v\rangle^\perp\}.             \tag{CE1.2}

```


More precisely, if s=dim(span(u,v)) and
rank(omega restricted to span(u,v))=2t, then


```math

 A_0\cong
 \mathbb C^{\,p^{s-2t}}\otimes
 M_{p^{d-s+t}}(\mathbb C).                              \tag{CE1.3}

```


In particular a symplectic pair leaves M_(p^(d-1)), whereas an independent
isotropic pair leaves C^(p^2) tensor M_(p^(d-2)). Nonscalar does not always
mean noncommutative: the latter algebra is commutative when d=2.

Let Omega_sl be the Casimir for the trace pairing on sl(H), so


```math

 \Omega_{\rm sl}
   =P_H-n^{-1}I\otimes I
   =n^{-1}\sum_{x\ne0}T_x\otimes T_{-x}.                \tag{CE1.4}

```


Here P_H is the flip on H tensor H.

**Theorem CE1 (the homogeneous elliptic residue obstruction).**
Fix tau in the upper half-plane. If dim A_0>1, there is no meromorphic
r(z) in sl(H) tensor sl(H) satisfying all three conditions:

1. Its periods are strictly homogeneous:


```math

   r(z+1)=(\operatorname{Ad}U\otimes1)r(z),\qquad
   r(z+\tau)=(\operatorname{Ad}V_0\otimes1)r(z).
                                                                  \tag{CE1.5}

```


2. Its only poles are simple poles at the lattice Z+tau Z.
3. Its residue at zero is Omega_sl.

**Proof.** Average the first tensor factor over the two finite commuting
adjoint actions. This is the projection Pi_0 onto A_0. The projected
function is doubly periodic. Its residue at zero is


```math

 (\Pi_0\otimes1)\Omega_{\rm sl}
   =n^{-1}\!\!\sum_{\substack{x\in\langle u,v\rangle^\perp\\x\ne0}}
                    T_x\otimes T_{-x},                 \tag{CE1.6}

```


which is nonzero because the Weyl tensors are linearly independent and
dim A_0>1. A nonzero matrix coefficient therefore gives an elliptic
function with exactly one simple pole of nonzero residue in a fundamental
domain. Integrating around that domain contradicts the residue theorem.
QED.

Thus every Weyl pair fails this architecture if d>1. Adding a scalar
multiple of I tensor I cannot cancel (CE1.6), which lies in the traceless
invariant block. This is an obstruction before imposing the classical
Yang--Baxter equation. It does not exclude additive quasiperiod anomalies,
extra poles, dynamical variables, other kinds of holonomies, or a quantum
R-matrix with a nonscalar leading term.

## CE2. The uniformly shifted Weyl ansatz leaves a spectator flip

Use the odd theta function theta(z;tau) with periods 1,tau and put


```math

 \phi(z,a;\tau)=
 \frac{\theta'(0;\tau)\theta(z+a;\tau)}
      {\theta(z;\tau)\theta(a;\tau)},\qquad
 \rho(z;\tau)=\frac{\theta'(z;\tau)}{\theta(z;\tau)}.     \tag{CE2.1}

```


This is the same Kronecker normalization as
[the existing genus-one kernel](bol-genus-one-kernel.md#k1-the-finite-holonomy-family-and-its-unique-kernel).
It has residue one at z=0, and
phi(z,a)=a^(-1)+rho(z)+O(a) as a tends to zero.

For x in V, choose alpha_x,beta_x in {0,1/p,...,(p-1)/p} representing
omega(u,x)/p and omega(v,x)/p. Define the natural uniform-shift candidate


```math

 R_\eta(z)=\frac1n\sum_{x\in V}
 e^{2\pi i\alpha_x z}
 \phi(z,\eta+\alpha_x\tau-\beta_x;\tau)
                 T_x\otimes T_{-x}.                   \tag{CE2.2}

```


It has residue P_H at z=0. Its temporal multiplier has the additional
scalar exp(-2 pi i eta), as is usual for this shifted ansatz.

**Proposition CE2.** The eta^(-1) coefficient of (CE2.2) is


```math

 \frac1n
 \sum_{x\in\langle u,v\rangle^\perp}T_x\otimes T_{-x}.  \tag{CE2.3}

```


It is a scalar tensor only when span(u,v)=V. If span(u,v) is a
symplectic plane, choose the orthogonal decomposition
V=V_1 orthogonal-sum V_2 and the corresponding Heisenberg tensor
factorization H=H_1 tensor H_2. After reordering the tensor factors,


```math

                   R_\eta(z)=R_\eta^{(1)}(z)\otimes P_{H_2}.
                                                                  \tag{CE2.4}

```


**Proof.** A torsion parameter alpha tau-beta belongs to Z+tau Z
exactly when alpha=beta=0 in the selected range. These and only these
terms have a pole as eta tends to zero. This proves (CE2.3).
Independence of the Weyl tensors proves its scalar criterion.
In the orthogonal decomposition, the coefficients of (CE2.2) depend
only on the V_1-label, while


```math

 \sum_{b\in V_2}T_b\otimes T_{-b}
       =(\dim H_2)P_{H_2}.

```


Since n=(dim H_1)(dim H_2), this gives (CE2.4). QED.

This is a limitation of the proposed repair, not a false quantum
Yang--Baxter no-go. A plane solution tensored with a flip can still
satisfy the quantum equation. The point is that it does not supply an
interaction in the remaining zero algebra. Multiplying away the
spectator flip changes the full flip residue. A single scalar
renormalization of eta cannot turn (CE2.3) into I tensor I when
dim H_2>1.

## CE3. An anomalous zero-block kernel fails its first flatness equation

One might try to keep the entire zero algebra by replacing the missing
elliptic scalar propagator with rho(z). This permits an additive
quasiperiod, since rho(z+tau)=rho(z)-2 pi i.

Let g=sl_m with m>=2 and let Omega be its trace Casimir. Consider
r(z)=rho(z)Omega. Write x=z_1-z_2 and y=z_2-z_3.

**Proposition CE3.** This r does not solve the spectral-parameter
classical Yang--Baxter equation. Its left side is


```math

 \bigl(\rho(x+y)(\rho(x)+\rho(y))-\rho(x)\rho(y)\bigr)
                       [\Omega_{12},\Omega_{13}].       \tag{CE3.1}

```


It is nonzero as a meromorphic function for every tau in the upper
half-plane. Scalar tensor counterterms cannot change this conclusion.

**Proof.** Invariance of the Casimir gives


```math

 [\Omega_{12},\Omega_{23}]=-[\Omega_{12},\Omega_{13}],
 \qquad
 [\Omega_{13},\Omega_{23}]=[\Omega_{12},\Omega_{13}],

```


and the last tensor is nonzero, already on an sl_2 subalgebra. These
relations give (CE3.1). Taking x to zero in its scalar factor gives


```math

                 \rho'(y)+\rho(y)^2=\theta''(y)/\theta(y).

```


If this were identically zero, theta'' would vanish identically; an
affine function cannot have the nontrivial theta quasiperiods and its
simple lattice zeros. Hence (CE3.1) is not identically zero. Scalar
operators commute with every tensor in this calculation. QED.

This is a genuine three-point test of an attempted exchange kernel. It
is distinct from the local matrix-current obstruction: the Lie algebra
sl_m is associative-matrix based and already legitimate. What fails here
is the proposed elliptic coefficient.

## CE4. A real dynamical repair on every forced matrix block

The repair below is standard Felder dynamical exchange. Its purpose is
to test the next equation rather than to leave “use KZB” as a proposal.
See [Felder's original source](../REFERENCES.md#felder94), equations
(3)--(4), for the established mechanism. With his
sigma(w,z)=phi(z,-w), our q=-lambda and kappa=-kappa_F change his
connection by an overall minus sign. The proof below fixes our own
conventions independently.

For a block M_m in (CE1.3), this construction chooses a Cartan algebra
and matrix-unit realization of that block. It is transported by
simultaneous conjugation of those choices. No preferred realization
across all charge sectors is asserted. Nor does a solution on this
zero block alone provide a solution on all of sl(H), with its other
holonomy characters.

For m>=2 let E_ab be the matrix units and h_a=E_aa-I/m. Let
q=(q_1,...,q_m), sum q_a=0, and exclude q_a-q_b in Z+tau Z for a!=b.
Functions of q can equivalently be extended to C^m invariant under
simultaneous translation of all q_a; this fixes the meaning of
partial derivatives below. Put


```math

 \begin{split}
 C_{\mathfrak h}&=\sum_a h_a\otimes h_a,\\
 r(z,q;\tau)&=\rho(z;\tau)C_{\mathfrak h}
       +\sum_{a\ne b}\phi(z,q_a-q_b;\tau)
                              E_{ab}\otimes E_{ba}.
 \end{split}                                                   \tag{CE4.1}

```


This is meromorphic for tau in H, with the displayed q-divisors and
z in Z+tau Z as its poles. The theta series is normally convergent
on compact subsets for tau in H; thus all differentiations used here
are valid away from those divisors. Its z-residue is the full sl_m
Casimir. Its invariant Cartan residue is accompanied by the additive
quasiperiod of rho, so CE1's homogeneous hypothesis is not satisfied.

**Theorem CE4 (dynamical exchange and position flatness).**
The kernel (CE4.1) obeys weight zero,


```math

 [h\otimes1+1\otimes h,r]=0,
 \qquad r_{21}(-z,q)=-r_{12}(z,q),                      \tag{CE4.2}

```


and the classical dynamical Yang--Baxter equation


```math

 \begin{split}
 &[r_{12}(x),r_{13}(x+y)]
  +[r_{12}(x),r_{23}(y)]
  +[r_{13}(x+y),r_{23}(y)]\\
 &\quad+\sum_a\bigl(
 h_a^{(1)}\partial_{q_a}r_{23}(y)
 -h_a^{(2)}\partial_{q_a}r_{13}(x+y)
 +h_a^{(3)}\partial_{q_a}r_{12}(x)\bigr)=0.             \tag{CE4.3}
 \end{split}

```


Let V_1,...,V_s be finite-dimensional sl_m-modules, with their chosen
representations used for the tensor factors, and let


```math

 M_0=\{v\in\bigotimes_iV_i:
       \textstyle\sum_i h_a^{(i)}v=0\text{ for every }a\}.

```


On meromorphic M_0-valued functions of q and of pairwise noncoincident
positions z_i, the differential operators


```math

 \mathcal D_i=\kappa\partial_{z_i}
       +\sum_a h_a^{(i)}\partial_{q_a}
       +\sum_{j\ne i}r_{ij}(z_i-z_j,q;\tau)             \tag{CE4.4}

```


commute for every complex kappa. The fiber consists of functions of
the dynamical variable q; this is not a claim of a finite-rank
connection after q has been fixed.

**Proof of the scalar identities.** The Kronecker function satisfies


```math

 \phi(x,a)\phi(y,b)
 =\phi(x-y,a)\phi(y,a+b)
  +\phi(y-x,b)\phi(x,a+b).                              \tag{CE4.5}

```


For completeness, fix y,a,b off the exceptional divisors and subtract
the right side from the left. As a function of x, the only possible
poles are x=0 and x=y, and their residues cancel. The difference has
multipliers 1 and exp(-2 pi i a). A holomorphic section with these
multipliers vanishes for a outside the period lattice: its 1-periodic
Fourier expansion would require exp(2 pi i n tau)=exp(-2 pi i a)
for some integer n. The general meromorphic identity follows by
continuation. This proves (CE4.5).

We will also need


```math

 \partial_a\phi(x,a)
   =\phi(x+y,a)\phi(y,-a)
       +\phi(x,a)\bigl(\rho(x+y)-\rho(y)\bigr).         \tag{CE4.6}

```


The right side is elliptic in y. Its possible poles at y=0 and
y=-x cancel, so it is constant. Its value as y tends to zero is


```math

 \partial_x\phi(x,a)+(\rho(x)-\rho(a))\phi(x,a)
    =(\rho(x+a)-\rho(a))\phi(x,a)
    =\partial_a\phi(x,a).

```


This proves (CE4.6), including exceptional parameter values by
meromorphic continuation.

**Proof of exchange.** Weight zero is immediate from the opposite
matrix-unit weights, and skew symmetry follows from
phi(-z,-a)=-phi(z,a) and oddness of rho. For (CE4.3) expand in matrix
units. The central subtraction I tensor I/m in C_h contributes
neither commutators nor q-derivatives.

For three distinct indices i,j,k, the coefficient of
E_ij tensor E_jk tensor E_ki is, with a=q_i-q_k and b=q_k-q_j,


```math

 -\phi(x,b)\phi(x+y,a)
 +\phi(x,a+b)\phi(y,a)
 -\phi(x+y,a+b)\phi(y,-b)=0,                            \tag{CE4.7}

```


which is (CE4.5). For two distinct indices i,j, the coefficient of
E_ij tensor E_ji tensor E_ii is, with a=q_i-q_j,


```math

 \phi(x,a)(\rho(y)-\rho(x+y))
 -\phi(x+y,a)\phi(y,-a)+\partial_a\phi(x,a)=0,           \tag{CE4.8}

```


which is (CE4.6). The coefficient with E_jj in the third place has
the opposite sign. Permuting tensor positions and reversing i,j
gives the remaining two-index coefficients. Diagonal triples vanish.
These exhaust the nonzero possibilities under
E_ij E_kl=delta_(jk) E_il. Thus (CE4.3) is proved.

**Proof of position flatness.** Weight zero preserves M_0. In the
commutator of (CE4.4), the position derivatives cancel using (CE4.2);
derivative operators left over from commutators with Cartan matrices
cancel for the same reason. Expanding the remaining terms and using
(CE4.3) gives


```math

 [\mathcal D_i,\mathcal D_j]
   =-\sum_a\Bigl(\sum_k h_a^{(k)}\Bigr)
              \partial_{q_a}r_{ij}(z_i-z_j,q).         \tag{CE4.9}

```


The derivative of r still has weight zero, so this expression
vanishes on M_0. QED.

For a tangible nontrivial subcase, on sl_2 the repair is


```math

 r(z,\lambda)=\tfrac12\rho(z)h\otimes h
    +\phi(z,\lambda)e\otimes f
    +\phi(z,-\lambda)f\otimes e.
                                                               \tag{CE4.10}

```


The derivative term in (CE4.8) is exactly what the three-point
calculation in CE3 omitted. It is not obtained by Wick contraction
of the old free-fermion currents.

## CE5. Explicit modular transport of the dynamical position system

This section proves covariance of the entire position system, not
merely a formula for individual theta coefficients. No tau-direction
heat equation is included.

Let gamma=(a b; c d) in SL_2(Z), j=c tau+d, and


```math

 \tau'=\frac{a\tau+b}{c\tau+d},\qquad
 z_i'=z_i/j,\qquad q'=q/j.

```


For fixed tau, put


```math

 \begin{split}
 Q(z,q)&=\sum_i z_i\sum_a q_a h_a^{(i)}
                         -\frac{\kappa}{2}\sum_a q_a^2 I,\\
 G_\gamma(z,q;\tau)
      &=\exp\!\left(\frac{2\pi i c}{j}Q(z,q)\right).
 \end{split}                                                   \tag{CE5.1}

```


All matrices in this exponent commute. Thus G_gamma is holomorphic
and invertible everywhere on the parameter cover.

**Theorem CE5.** After pulling the primed derivatives back to z,q,
on M_0 one has


```math

       j^{-1}\mathcal D_i'
           =G_\gamma\mathcal D_iG_\gamma^{-1}.          \tag{CE5.2}

```


These transformations satisfy the SL_2(Z) composition law, with
the indicated change of variables. In particular a solution of
the noncoincident system at tau transports to one at gamma tau.

**Proof.** The scalar transformation laws are


```math

 \begin{split}
 \phi(z/j,u/j;\tau')
     &=j\,e^{2\pi i czu/j}\phi(z,u;\tau),\\
 \rho(z/j;\tau')&=j\rho(z;\tau)+2\pi i c z.
 \end{split}                                                   \tag{CE5.3}

```


They can be obtained without a theta multiplier convention. Multiply
the left side of the first equation by
j^(-1) exp(-2 pi i czu/j). As a function of z, its multipliers
are 1 and exp(-2 pi i u): use
1/j=a-c tau' and tau/j=-b+d tau'. It has residue one and the
same pole lattice as phi(z,u;tau). The uniqueness argument in the
proof of (CE4.5) gives the first identity; comparing constant terms
as u tends to zero gives the second.

Put D(z,q)=diag(exp(2 pi i c z q_a/j)). Equation (CE5.3) gives


```math

 r(z/j,q/j;\tau')
    =j\,(\operatorname{Ad}D(z,q)\otimes1)r(z,q;\tau)
                           +2\pi i c z C_{\mathfrak h}. \tag{CE5.4}

```


For the i,j tensor factors, Ad G_gamma supplies exactly the
off-diagonal factor in (CE5.4), because the exponent uses
(z_i-z_j)(q_a-q_b). Write C_ik=sum_a h_a^(i)h_a^(k),
including C_ii. Differentiating (CE5.1) yields


```math

 G_\gamma\Bigl(\kappa\partial_{z_i}
            +\sum_a h_a^{(i)}\partial_{q_a}\Bigr)
 G_\gamma^{-1}
 =\kappa\partial_{z_i}+\sum_a h_a^{(i)}\partial_{q_a}
                    -\frac{2\pi i c}{j}\sum_k z_k C_{ik}.       \tag{CE5.5}

```


The two terms involving kappa q dot h^(i) cancel. On M_0,


```math

 \sum_{k\ne i}(z_i-z_k)C_{ik}=-\sum_k z_k C_{ik}.       \tag{CE5.6}

```


The remaining term of (CE5.4) is therefore precisely (CE5.5).
The chain rule gives the common derivative factor j, proving
(CE5.2).

Finally Q is homogeneous of degree two in z,q. The elementary
fractional-linear identity


```math

 \frac{c_{21}}{j_{21}}
     =\frac{c_1}{j_1}
          +\frac{c_2}{j_2(\gamma_1\tau)\,j_1^2}

```


and commutativity of the exponents give the composition law for
G_gamma. There is no unstated scalar multiplier. QED.

Thus the repaired system has genuine modular transport with a
nontrivial dynamical gauge. It has neither been identified with the
original Fock traces nor supplied with a Bol-dependent tau heat
connection or a charged sewing functor. The theorem is an established
elliptic mechanism with an explicit place for the forced matrix zero
algebra.

## CE6. Constant charged fusion does not preserve separate dynamical bases

Use the canonical regular fusion of
[CH2](bol-charged-heisenberg-obstruction.md#ch2-canonical-charged-fusion-and-its-dual-channel).
Let L_ell,L_mu,L_(ell+mu) be invertible scalar bilinear maps on the
finite vector space W. Write


```math

 A=L_{\ell+\mu}^{-1}L_\mu,\qquad
 B=L_{\ell+\mu}^{-1}L_\ell,\qquad A+B=I.

```


The finite intertwiner changes coordinates by


```math

 u=L_{\ell+\mu}^{-1}(L_\ell x+L_\mu y),\quad v=x-y,
 \qquad x=u+Av,\quad y=u-Bv.                           \tag{CE6.1}

```


In the canonical coordinate bases, separate Cartan parameters on
H_ell and H_mu act diagonally by f(x)+g(y). Separate parameters on
the fused module and its multiplicity space act by h(u)+k(v).

**Theorem CE6 (the separated-Cartan obstruction).**
If A,B are invertible and A+B=I, and complex-valued functions on W
satisfy


```math

        f(u+Av)+g(u-Bv)=h(u)+k(v)
                    \quad\hbox{for every }u,v\in W,    \tag{CE6.2}

```


then f,g,h,k are constant. Consequently the two separate traceless
Cartan parameter spaces meet only at zero under the canonical
constant fusion map.

**Proof.** Expand each function in the Fourier characters of W.
The nonconstant terms of f(u+Av) have frequency pairs


```math

                         (\xi,A^*\xi),\qquad \xi\ne0,

```


and those of g(u-Bv) have pairs


```math

                         (\eta,-B^*\eta),\qquad \eta\ne0.

```


They do not meet either coordinate axis, since A and B are
invertible. They do not meet one another: equality would imply
xi=eta and (A+B)^*xi=xi=0. The right side of (CE6.2) has frequencies
only on the two coordinate axes. Uniqueness of finite Fourier
expansion forces all nonconstant coefficients to vanish, on both
sides. QED.

The sharpening from a single counterexample to this exact theorem
was contributed by model participant 13. It is not an independent review of this
manuscript.

For W=F_3 and ell=mu=1, the change is
u=2(x+y), v=x-y, x=u+2v, y=u-2v. Choosing f=indicator_(0),
g=0 gives a mixed rectangle difference


```math

 f(0)-f(2)-f(1)+f(0)=2,

```


which cannot occur for h(u)+k(v). The theorem shows that this is
not an exceptional choice.

This is an obstruction to gluing the per-sector dynamical systems
using only the already proved, constant finite fusion intertwiners
and separate parameter spaces. It does not prohibit a
parameter-dependent intertwiner, an enlarged parameter space on
the multiplicity channel, a groupoid of compatible polarizations,
or other dynamical fusion laws. In particular CE4--CE5 alone do
not solve the charged coherence problem.

## CE7. A Weyl holonomy genus bound and the actual large input

**Proposition CE7.** For 2g Weyl holonomies labelled by
w_1,...,w_(2g) in a symplectic space V of dimension 2d, the common
commutant on H is scalar if and only if those labels span V.
Consequently a scalar-commutant construction using these holonomies
requires g>=d. As a statement about projective or adjoint
holonomies, the bound is attained by a symplectic basis.

**Proof.** In the Weyl basis the common invariant vectors are
precisely T_x with omega(w_i,x)=0 for every i. Their span is scalar
exactly when the orthogonal complement of span(w_i) is zero,
equivalently when that span is V. Since 2g vectors span at most
2g dimensions, g>=d follows. A symplectic basis attains equality.
Its Weyl commutators are scalar, so the surface relation holds
after passing to the projective or adjoint group. QED.

For honest general-linear flat lifts the additional relation is


```math

       \prod_{i=1}^g[T_{u_i},T_{v_i}]=I
       \quad\Longleftrightarrow\quad
       \sum_{i=1}^g\omega(u_i,v_i)=0\ \hbox{in }\mathbb F_p.

```


It must not be omitted. The proposition is restricted to Weyl
holonomies: arbitrary matrices of dimension p^d can have scalar
common commutant with far fewer labels. Nor does the bound by
itself construct a higher-genus kernel, remove holomorphic
differential ambiguities, or prove a modular functor.

For the full P polarization of the rigid-center proper Bol input,
the scalar bilinear ranks proved in the linked finite manuscript
are 0,36,72. The nonzero irreducible Heisenberg sectors therefore
have dimensions 3^36 and 3^72: here the symplectic space is the
quotient of W plus W, so its dimension is twice the scalar
bilinear rank. A symplectic torus pair leaves respectively


```math

                      M_{3^{35}}\quad\hbox{or}\quad M_{3^{71}}.

```


Thus the product-reached zero algebra is not a small correction to
a scalar normalization. In the restricted Weyl architecture a
scalar commutant would need genus at least 36 or 72. These are
symbolic consequences of compact ranks; no huge multiplication
table or matrices of those sizes are enumerated.

This use of the full bilinear b must be distinguished from the
earlier alternating b-b^op packet. An alternating rank 72 would
instead give a symplectic dimension 72 and d=36. The two meanings
of rank cannot be interchanged.

The central positive cocycle f supplies scalar phases on an
irreducible sector, so it disappears under adjoint conjugation.
The new exchange obstruction, by itself, does not distinguish
the principal-isotope pair. Its old phase-marked distinction
remains in the canonical current and holonomy constructions;
it is not a new consequence of CE4. The
[finite charged manuscript](bol-charged-heisenberg-obstruction.md#ch4-a-geometric-integer-extension-and-coherent-carry-lines)
separately tracks the integer degree labels needed before a
noncommuting Weyl pair can act as honest charged bundle
automorphy.

## The remaining charged sewing equation

There is now a precise surviving task. One needs dynamical
intertwiners between the actual charge sectors, with an explicitly
specified common parameter space, that intertwine the connection,
obey a pentagon under the finite F-moves, and retain the entire
dual-fusion algebra in every reached zero channel. Their exchange
maps must satisfy the corresponding dynamical braid compatibility.
In a connection notation, the first requirement is


```math

              \nabla_{\rm out}F_{\ell,\mu}(q)
                     =F_{\ell,\mu}(q)\nabla_{\rm in},

```


including the derivatives of F and the specified changes of
dynamical variables. A constant F with the separate Cartan
parameters used above fails CE6.

The old support-decomposition identity does not supply these
maps, and the explicit Felder repair does not make their
existence automatic. A successful family would still need a
proved relation that depends on the loop's b, its action maps,
or its positive cocycle beyond transported finite matrices and
the universal Fay identity. This manuscript supplies a
noncoincident, modularly covariant test system and exact failures
of two simpler repairs; it does not yet supply that new relation.
