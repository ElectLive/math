# A closed genus-one completion of the marked Bol currents

**Mira Cult**

## Scope and the additional analytic structure

Use the canonical finite algebra, actions, fiber idempotents and strict
transport interface of [F2--F5](bol-fermion-sewing.md). In particular


```math

 B=\operatorname{Fun}(G\times_Z\operatorname{Conj}Q,\mathbb C),\qquad n=\dim B,

```


with its counting inner product, left operators $L_g$, commuting right
operators $R_z$, and actual translations $L_{k_x}$. The odd group
$\mathcal P=\langle L(G),R(Z)\rangle$ is a quotient of $G\times Z$.
Its exponent is denoted $e$. The source and classification dependencies are
exactly those of [the canonical seed](bol-translation-class-fusion.md);
this manuscript does not independently prove those inputs.

The original positive-mode exterior algebra already has genuine modular
energy-current traces: see [the current theorem](bol-genus-one-correlations.md).
Here we add a canonical dual oscillator space and zero-mode space, and then
use both cycles of a torus. This addition is explicit. The Bol and cocycle
identities alone do not imply analytic boundary conditions. The analytic
ingredient is the standard free complex fermion/Kronecker kernel, whose
uniqueness and modular covariance are proved below. See
[MTZ07](../REFERENCES.md#mtz07) for the established fermion precedent.

## K1. The finite holonomy family and its unique kernel

Let $s,t\in\mathcal P$ commute. Choose
$(\epsilon,\delta)\in\{\pm1\}^2\setminus\{(1,1)\}$, and set


```math

 U=\epsilon s,\qquad V=\delta t.                         \tag{K1}

```


All eigenvalues of $s,t$ have odd order. Consequently $U,V$ have no
common fixed vector: whichever sign is negative excludes eigenvalue one
for that operator. Let $\mathscr H$ denote this finite set of ordered
operator pairs; duplications, if any, are identified. This is a family of
unitary flat boundary conditions, including the three nontrivial sign pairs.

**Theorem K1.** For $\tau\in\mathbb H$ there is a unique
$\operatorname{End}(B)$-valued meromorphic function $K_{U,V}(z;\tau)$
such that


```math

 K(z+1)=UK(z),\quad K(z+\tau)=VK(z),\quad
 K(z)=I/z+O(1)\quad(z\longrightarrow0),                  \tag{K2}

```


and its only poles are simple poles at $\mathbb Z+\tau\mathbb Z$.
It is holomorphic in $\tau$, away from those position divisors. For
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$
in $SL_2(\mathbb Z)$, put


```math

 (U',V')=(U^dV^c,U^bV^a).

```


Then $(U',V')\in\mathscr H$ and


```math

 K_{U',V'}\left(\frac z{c\tau+d};\gamma\tau\right)
       =(c\tau+d)K_{U,V}(z;\tau).                       \tag{K3}

```


**Proof.** Simultaneously diagonalize the commuting unitaries, writing
$U=\sum e^{2\pi i\alpha}\Pi_{\alpha,\beta}$ and
$V=\sum e^{2\pi i\beta}\Pi_{\alpha,\beta}$. Here $\alpha,\beta$ are
rational modulo integers, with no joint pair $(0,0)$. Use the odd Jacobi
theta function with periods $1,\tau$, and define


```math

 K_{\alpha,\beta}(z;\tau)=e^{2\pi i\alpha z}
 \frac{\theta_1'(0;\tau)\theta_1(z+\alpha\tau-\beta;\tau)}
 {\theta_1(z;\tau)\theta_1(\alpha\tau-\beta;\tau)},
 \qquad K_{U,V}=\sum\Pi_{\alpha,\beta}K_{\alpha,\beta}.  \tag{K4}

```


The denominator theta constant is nonzero: if
$\alpha\tau-\beta\in\mathbb Z+\tau\mathbb Z$, taking imaginary parts
forces both $\alpha$ and $\beta$ integral. The theta quasi-periods give
(K2), its simple zero at zero gives residue one, and integer changes of
$\alpha,\beta$ cancel between the exponential and theta quotient.
Thus (K4) is basis independent and holomorphic on the stated domain.

For uniqueness, the difference of two such functions is entire: residues
at every lattice point are prescribed by (K2). Each column has unitary
multipliers. Its norm is bounded on one fundamental parallelogram, hence
on the plane; Liouville's theorem makes it constant. Its value must be fixed
by both $U,V$, so it is zero.

The transformed lattice is the original lattice scaled by $(c\tau+d)^{-1}$.
As a function of $z'=z/(c\tau+d)$,
$(c\tau+d)K_{U,V}((c\tau+d)z';\tau)$ has residue $I$, and its
two multipliers are $U^dV^c$ and $U^bV^a$. Uniqueness proves (K3).
The odd parts remain commuting elements of $\mathcal P$; the sign pair
remains nontrivial since the induced matrix is invertible modulo two. QED.

Thus the normalized kernel has weight one and a finite **permutation**
multiplier on $\mathscr H$, with no unspecified scalar anomaly. Each
component is fixed by the principal congruence subgroup $\Gamma(2e)$.
It is a meromorphic function of the position on the flat bundle, rather than
a scalar elliptic function when its multipliers are nontrivial. Rational
theta characteristics give convergent fractional-power expansions at infinity;
at other cusps the position is rescaled as in (K3), away from collision
divisors. This is not a blanket scalar meromorphy claim at a cusp while
holding an unrescaled position fixed. The domain excludes position
collisions, not points of $\mathbb H$.

## K2. A closed correlation hierarchy

Put $H=B\otimes\mathbb C^{24}$, and let the kernel act trivially on the
second factor. For vectors $u_i\in H$, dual vectors $v_j\in H^*$,
and pairwise noncolliding positions, define


```math

 \mathcal C^{(k)}_{U,V}(\mathbf z,\mathbf w;\mathbf u,\mathbf v;\tau)
 =\det_{1\leq i,j\leq k}
       \big[v_j(K_{U,V}(z_i-w_j;\tau)u_i)\big].         \tag{K5}

```


The order of the fermion fields is chosen as plus fields followed by the
minus fields in reverse order, so that the Wick sign is the determinant
sign in (K5). In the ordinary-trace realization of K3, this residue-normalized
function is $(-2\pi i)^k$ times the literal normalized $2k$-field
trace. Arbitrary bilocal matrix insertions are obtained by linear
contraction of these vector and covector indices; in particular they include
the multiplication matrices $M_a$, all translation matrices, and their
finite products. This construction does not require the insertion matrices
to commute with $U,V$. Such insertions are tensors in the flat bundle;
their position monodromies should not be replaced by scalar periodicity.

**Theorem K2.** At every fixed insertion number $k$, (K5) is a finite
holonomy-indexed modular system of weight $k$:


```math

 \mathcal C^{(k)}_{U',V'}
   \left(\frac{\mathbf z}{c\tau+d},
         \frac{\mathbf w}{c\tau+d};\tau'\right)
       =(c\tau+d)^k\mathcal C^{(k)}_{U,V}
          (\mathbf z,\mathbf w;\tau).                 \tag{K6}

```


Here the insertion tensors are unchanged; simultaneous conjugation of all
matrices and tensors gives the same scalar. The determinant expansion along
one row expresses every $k$-pair function in terms of one kernel and
$(k-1)$-pair functions. Collision residues give the corresponding lower
correlator times the canonical pairing, with its determinant sign. Position
derivatives and regular Laurent coefficients remain in the hierarchy with
their specified increased weights. It contains no independent higher
correlation data beyond the kernel and insertion tensors.

**Proof.** Apply (K3) to each determinant entry. Each term has $k$
factors, giving (K6). Row expansion is the asserted recursion. At
$z_i=w_j$, the residue of that entry is $v_j(u_i)$, while the cofactor
is the lower determinant. Differentiating (K3), or comparing the Laurent
coefficients after its prescribed rescaling, gives the last assertion.
All operations are finite at a fixed number of insertions. QED.

This is a closed hierarchy: its size grows with insertion number, while its
holonomy-label set is fixed and finite. It does **not** say that all individual
Fourier modes lie in one finite-dimensional space of modular functions of
$\tau$ alone. That false interpretation is excluded by
[the fixed-mode obstruction](bol-genus-one-architecture.md).

## K3. Actual traces and the original current modes

There is a canonical charged Ramond completion of the original graded object:


```math

 \mathcal R_B=\Lambda H_0\otimes
       \Lambda\!\left(\bigoplus_{m\geq1}(H[m]\oplus H^*[m])\right).
                                                               \tag{K7}

```


The zero-mode space has degree zero, and each positive mode has its indicated
integer degree. Every degree is finite. Permutations act on $H$,
contragrediently on $H^*$, and by the exterior functor on all factors.
This is an ordinary honest action, with no choice of a spin lift.
The original $\mathcal F_B$ is the first positive-oscillator factor;
its currents act on that factor and identically on the others. They therefore
retain exactly their former normalized correlation functions.

**Proposition K3.** For $t\in\mathcal P$, the shifted trace is


```math

 \widehat Z_t(\tau)=q^{2n}\operatorname{Tr}_{\mathcal R_B}
       (\widehat\Gamma(t)q^D)
   =\det(1+t|B)^{24}\Phi_t(\tau)^2
   =2^{24\kappa(t)}\Phi_t(\tau)^2,                    \tag{K8}

```


where $\kappa(t)$ is the number of permutation cycles and
$\Phi_t=\prod_O H(|O|\tau)$,
$H(\tau)=\Delta(2\tau)/\Delta(\tau)$, as in F-C. The shift $2n$
is the sum of the two original oscillator shifts. The normalized two-field
trace is the kernel $K_{1,-t}$, up to the explicit scalar normalization
$-2\pi i$. Every normalized finite original current correlation is a
finite linear combination of joint position-Fourier coefficients of (K5)
at its own and lower arities, with the CAR contact contractions included.

**Proof.** The exterior trace identity gives the product of the zero factor
$\det(1+t|H)$ and the positive factors
$\det(1+q^m t|H)\det(1+q^m t^{-1}|H)$.
Permutations have identical eigenvalue multisets on $B$ and $B^*$.
An odd permutation cycle contributes $1+q^{m|O|}$ and has
$\det(1+t|O)=2$, proving (K8). None of these factors vanishes in
$|q|<1$.

For clarity fix a $t$-eigenline with eigenvalue $\lambda$. Use CAR
modes $\psi_r,\psi^*_s$, $r,s\in\mathbb Z$, with
$\{\psi_r,\psi_s^*\}=\delta_{r+s,0}$.
For $m>0$, $\psi_{-m}$ creates $H[m]$,
$\psi^*_{-m}$ creates $H^*[m]$, and their paired positive modes
annihilate. The zero modes wedge and contract $H_0$. Directly tracing
the two states of each oscillator gives


```math

 \langle\psi_r\psi^*_{-r}\rangle_t
        =\frac1{1+\lambda^{-1}q^r}.                  \tag{K9}

```


In particular its $r=-m$ value is
$\lambda q^m/(1+\lambda q^m)$, the original occupation trace.
For $\psi(z)=\sum_r\psi_r e^{2\pi i r z}$, the bilateral sum is


```math

 K_{1,-\lambda}(z;\tau)
       =-2\pi i\sum_{r\in\mathbb Z}
          \frac{e^{2\pi i r z}}{1+\lambda^{-1}q^r}.
                                                               \tag{K10}

```


It converges absolutely and locally uniformly on
$0<\operatorname{Im}z<\operatorname{Im}\tau$. The usual geometric
series continuation, or the theta expression (K4), shows its spatial
multiplier one, temporal multiplier $-\lambda$, and residue one.
For completeness the residue follows from the positive-frequency part
$\sum_{r\geq0}e^{2\pi i r z}\sim-1/(2\pi iz)$; the remaining
terms are regular near zero after separating a convergent thermal correction.
Uniqueness K1 identifies the functions.

The finite-dimensional exterior trace is Gaussian: expanding by occupied
basis subsets and applying the CAR yields the determinant of two-point
contractions. Taking limits over modes is justified by absolute convergence
on radially ordered subdomains; meromorphic continuation then gives (K5).
Equivalently this elementary Wick calculation is the complex-fermion
determinant theorem [MTZ07, Proposition 6.4]. For the field order specified
in K2, take the common expansion chamber
$0<\operatorname{Im}(z_i-w_j)<\operatorname{Im}\tau$ for every pair.
The coefficients of
$e^{-2\pi i m z}e^{2\pi i n w}$ in the uncontracted bilocal field are
$\psi_{-m}M_a\psi^*_n$, hence the original $E_a^{mn}$ after
summing species. Before extracting coefficients for a product of these
bilinears, reorder its finite creation/annihilation word by the CAR into
normal-ordered monomials. Each is a coefficient of (K5); each contraction
is the explicit Kronecker delta and gives a lower-arity term. For example
$(c^\dagger c)^2=c^\dagger c$, although the normal-ordered four-field
term alone vanishes. Thus one must not extract all products from one
uncorrected common-chamber determinant coefficient. This finite CAR reduction
proves the stated recovery of all finite current words. Factoring the dual
and zero-mode traces proves their normalized correlation equality. QED.

Other members of $\mathscr H$ are the flat-bundle completions of this
Ramond block. One may realize them by rationally shifted CAR modes on the
joint eigenlines, as in [MTZ07, Sections 4 and 6]; that general twisted-module
identification is not required for K1--K2. We do not silently treat every
new spatial sector as a trace on the original integer-graded space.

## K4. The loop and cocycle identities survive as exact correlation laws

Let $A_x=L_{k_x}$, and retain the marked positive-cocycle operators
$U_a=L_{f(a)}$, $V_a=L_a$, and the canonical involution $\Theta$.
The notation $U_a,V_a$ here refers to these inherited operators, distinct
from a holonomy pair $(U,V)$. Their exact relations are


```math

 A_xA_yA_x=A_{x\cdot(y\cdot x)},\quad
 U_{ab}=U_aV_aU_bV_a^{-1},\quad
 \Theta U_a\Theta^{-1}=V_a^{-1}U_aV_a.                 \tag{K11}

```


These are [F-A and F13--F16](bol-fermion-sewing.md), not extra matrix-group
multiplicativity assumptions on the loop. Permutations carry
$M_a$ to $M_{ga}$, while right charge conjugation sends a coefficient
of charge $\ell$ to $\chi_\ell(z)M_a$.

**Proposition K4.** Substitution of either side of (K11) into any matrix word,
or any compatible holonomy label, gives identical correlations (K5).
Simultaneously conjugating the holonomies and all insertion tensors gives
identical scalar functions. Right-charge covariance gives the same charge
addition and selection rules as the original currents. These identities
hold on the actual completed graded space, as well as in the kernel system.

**Proof.** The exterior action on (K7) respects products and inverses, so
(K11) holds there. Simultaneous conjugation carries the unique kernel of K1
to the kernel for the conjugate pair, by (K2); index contractions and
determinants are invariant under change of basis. Multiplication operators
satisfy $M_aM_b=M_{ab}$, and their right-charge adjoint action is exactly
F10. Applying this to a trace in a right-invariant background yields the
selection rule, or the corresponding covariance when insertions have open
charge indices. Equality of words is preserved by every linear contraction
in (K5). QED.

These are genuine loop-indexed Ward equalities. They are not a proof that
Bol identities alone force an unfamiliar theta or Fay identity. The Wick
recursion is universal to free fermions; the nonassociative input is the
distinguished translation and cocycle word system occurring in it.

## K5. What the analytic system recovers

Let $e_0\in B$ be the idempotent of the identity coset fiber, and let
$P_\ell$ be the right one-particle charge projector. For local
translations $k_x,k_y$, write $c(x,y)=[k_x,k_y]\in Z$.
The finite theorem [CG2](bol-correlation-geometry.md) proves


```math

 K_\ell(x,y):=\operatorname{Tr}_B
   (M_{e_0}P_\ell L_{c(x,y)})
     =p^{d-r_\ell}\psi(\ell(c(x,y))).                 \tag{K12}

```


This coefficient is recovered from actual weight-two energy traces on the
original object by [the extraction theorem](bol-genus-one-correlations.md).
It also occurs directly in K3. Define the residue-normalized bilocal
contraction with its essential base-fiber insertion by


```math

 \mathcal B_{c,z}(u;\tau)
       =24\operatorname{Tr}_B\big(M_{e_0}K_{1,-L_cR_z}(u;\tau)\big).

```


Fourier-average these functions over $z\in Z$ with coefficient
$\chi_\ell(z)^{-1}/|Z|$. The coefficient of
$e^{-2\pi i m u}q^m$, divided by $-2\pi i\cdot24$, is
precisely (K12). This normalization is for the kernel contraction
$\mathcal B$, which is $-2\pi i$ times the actual normalized
bilocal trace. Here $z\in Z$ is a group element and $u$ is a
position difference. The Fourier average is taken **after separate
normalization of each block**; it is not incorrectly identified with a
charge-projected trace divided by a common partition function.

The positive real factor in (K12) is known, so the phases for all $\ell$
recover $c(x,y)\in Z$. Thus the marked analytic family determines the
alternating commutator bimap, not just its scalar ranks or their simultaneous
radicals. With an axis actor for which $R-R^{-1}$ is invertible,
[CG3](bol-correlation-geometry.md) recovers the full original bilinear map
using commutators with conjugated actual translations. This conclusion uses
the retained linear labels and axis action, and is equivariant under their
strict transport; it is not reconstruction of the entire loop from an
unmarked single function.

The two explicit quartic-pencil controls in
[CG4](bol-correlation-geometry.md) have identical entire indexed fusion data,
but inequivalent recovered commutator bimaps. They consequently have different
marked modular current families. These controls are class-two groups, not
new claims of simple proper Bol loops.

For the specified rigid proper-Bol isotope pair, the previously proved actual
norm-word trace ratio is


```math

 \frac{\Phi_+}{\Phi_-}
   =\left[\frac{H(\tau)^3}{H(3\tau)}\right]^{I(M-1)},
 \qquad M=3^{36},\quad I=3^{146}19^6.                 \tag{K13}

```


This is the exact marked-source statement of
[the rigid evaluation](bol-fermion-sewing.md), with the inherited source
dependencies retained. Both the original modular energy traces and the
completed system retain it. For example, the normalized shifted energy of
the original factor, $D+n$, has response difference


```math

 3I(M-1)\big(F(\tau)-F(3\tau)\big),\qquad
 F(\tau)=2E_2(2\tau)-E_2(\tau).                       \tag{K14}

```


This follows by applying $q\,d/dq$ to (K13); its first coefficient is
$72I(M-1)q$. It is also the response of that retained factor in (K7).
The completed object's total shifted energy has twice (K14), since (K8)
squares $\Phi$; its zero-mode factor is independent of $\tau$.
No huge table or graded-space expansion is needed.

## Precise endpoint

The literal fixed-mode question has a negative finite-dimensional answer.
The energy-resummed traces already give a closed quasimodular hierarchy,
with an explicit almost-holomorphic modular completion, and a modular detector
of the full marked local bimap under the stated axis-invertibility hypothesis.
The explicit charged flat-bundle completion gives
a closed, finite-holonomy genus-one correlation hierarchy containing those
original modes. The proof of closure uses the added fermionic analytic
architecture. The loop forces its marked word and charge identities and
supplies data that the modular coefficients genuinely recover.

It remains open whether the Bol/cocycle relations impose a new analytic
restriction beyond this universal free-fermion mechanism, for example a
relation among inequivalent background sectors not already a matrix-word
equality, Wick identity, or the standard theta identities. No Monster,
genus-zero, replicability, denominator identity, or historical priority claim
is made here.
