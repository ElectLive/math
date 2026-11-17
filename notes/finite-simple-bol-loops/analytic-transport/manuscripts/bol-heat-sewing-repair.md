# Marked reconstruction from separated mixed-heat correlations

**Mira Cult**



This note gives a positive analytic consequence of the retained true-dual
heat channel. A family of separated-point correlations reconstructs a
specified boundary operator, with a contour stability bound and an
exponentially convergent finite sampling procedure. It keeps the whole
matrix zero algebra and a fixed inversion/reference marking. An exact
proper-Bol control separates the established cubic isotopes even though
their corresponding individual translation spectra agree.

The kernel is classical. These are **new coupled observables**, not the
earlier Fock traces, and their information is a finite marked matrix tensor.
The additional theorem is an explicit analytic realization, converse and
stable recovery procedure for that tensor. It is not an identity independent
of all finite data, a new Felder system, or a completion of charged dynamical
fusion. In particular this note does not identify the heat sewing with the
finite dynamical tensorator or supply a heat-compatible fusion pentagon.

## HT1. The actual true-dual kernel and its domain

Let p be an odd prime, let k>0 be prime to p, set


```math

 \zeta=e^{2\pi i/p},\qquad \kappa=k/p,\qquad \delta=2k/p,
 \qquad H=\mathbb C^p\otimes F,\quad m=\dim F>0.
 \tag{HT1}

```


On the first factor use the marked holonomies and pair inversion


```math

 Ue_j=\zeta^{-kj}e_j,\qquad Ve_j=e_{j+1},\qquad Pe_j=e_{-j}.
 \tag{HT2}

```


Indices are in F_p. These are the marked-pair factors in
[CH3--CH4](bol-charged-heisenberg-obstruction.md), at scientific source
`197d13d4ac2e48763ed20bf418228d7b4d16aa8c`. The pair acts irreducibly on
C^p; F is its full multiplicity space, not a selected constituent. The
physical module may have additional distinguished operators acting on H.
The simultaneous conjugation-invariant algebra of U,V on H is exactly
I tensor End(F). Thus all its matrix zero modes are retained.
P in (HT2) implements inversion of this marked Weyl pair. It is a fixed
boundary operator, not a claim that inversion in the entire Bol loop
acts on one central-charge space by P tensor I.

Write theta(z;tau)=theta_1(pi z|tau), with its derivative taken in z, and


```math

 \phi(z,v;\tau)=
 \frac{\theta'(0;\tau)\theta(z+v;\tau)}
      {\theta(z;\tau)\theta(v;\tau)},\qquad
 K_{a,b}(u,v;\tau)=e^{2\pi iav}
               \phi(\delta u+a\tau-b,v;\tau).
 \tag{HT3}

```


Here Im(tau)>0. All functions are meromorphic on their covering variables;
the parameter cover is part of the marking. Integer changes of a or b do
not change K. Put


```math

 W_{r,s}=V^{-r}U^s P U^{-s}V^r,
 \qquad
 S_A(u,v;\tau)=\frac1p\sum_{r,s\in\mathbb F_p}
           K_{r\delta,s\delta}(u,v;\tau)(W_{r,s}\otimes A)
 \quad(A\in\operatorname{End}F).
 \tag{HT4}

```


The following elementary identities will be used throughout:


```math

 W_{r,s}^*=W_{r,s},\quad W_{r,s}^2=I,\quad
 \operatorname{tr}(W_{r,s}W_{t,w})=p\,1_{(r,s)=(t,w)},
 \quad \sum_{r,s}W_{r,s}=pI.
 \tag{HT5}

```


For example


```math

 W_{r,s}e_j=\zeta^{2ks(j+r)}e_{-j-2r}.
 \tag{HT6}

```


This formula proves involutivity and the orthogonality in (HT5): for r!=t
the product has a nonzero shift, and for r=t its trace is a nontrivial
character sum unless s=w. Summing (HT6) first over s proves the last
identity. In particular these p^2 operators are a basis of End(C^p).

**Proposition HT1.** S_A is the actual meromorphic section of the
true-dual bundle in [TH3a](bol-theta-fusion-connection.md), pulled back by
x=u+v, y=u-v. It obeys the full mixed heat equation


```math

 \mathcal H_\delta S_A=0,\qquad
 \mathcal H_\delta=\partial_\tau-
                          \frac1{2\pi i\delta}\partial_u\partial_v,
 \tag{HT7}

```


and has residue I tensor A at v=0. Its poles are contained in
v in Lambda_tau=Z+tau Z or 2ku in Lambda_tau. There is no assertion of
holomorphy at the extra center divisors.

**Proof.** The four automorphy factors follow from the elementary
Kronecker laws and (HT6), exactly as in TH3a. They are the factors of
E_(H,k)(x) tensor E_(H,k)^*(y), not a replacement scalar neutral sector.
For clarity the mixed heat identity can be proved without a theta
addition formula. The function
2pi i partial_tau phi-partial_z partial_v phi has the Poincare
automorphy factors in z. It has no pole at z=0 because the residue of phi
is the constant 1; transport gives no pole at any lattice translate.
For v outside Lambda_tau a holomorphic function with factors 1 and
exp(-2pi i v) is zero by its Fourier expansion. This proves
2pi i partial_tau phi=partial_z partial_v phi, first on that open set
and then meromorphically. Differentiating the a tau term in K gives
a phi_z; the derivative of exp(2pi iav) supplies precisely this term
in (HT7). Every K has v-residue 1, so (HT5) gives the residue assertion.
The pole set follows by multiplying the first argument of phi by p and
using gcd(2k,p)=1. QED.

The theta series converges normally with every derivative on compact
subsets of C times H: its absolute terms are bounded by
C exp(-pi y_0(n+1/2)^2+C'|n+1/2|) when Im(tau)>=y_0>0.
Consequently all quotients and their derivatives converge normally away
from the displayed divisors. Only finite sums occur in (HT4).
No regularization or formal summation convention is involved.

## HT2. A coupled heat system with a fixed boundary marking

Fix an arbitrary operator Q in End(H). Retain
$\mathcal P=P\otimes I_F$ as a separately fixed inversion boundary.
Define, for every A in End(F),


```math

 \mathcal C_A^Q(u,v;u',v';\tau)=
 \operatorname{tr}_H\!\left(
 S_A(u,v;\tau)Q S_I(u',v';\tau)\mathcal P\right).
 \tag{HT8}

```


The base consists of (u,v,u',v',tau) off the divisors of the two S
kernels. One may additionally require the four insertion points
u+v,u-v,u'+v',u'-v' to be pairwise distinct modulo Lambda_tau.
This is a nonempty open set. The theorem below holds on that separated
set and by meromorphic continuation wherever (HT8) is defined.
This is a correlation on the lifted marked parameter cover. The fixed
matrix Q is not asserted to be a parallel bundle morphism between
arbitrary independent insertion fibers, and no scalar descent to the
unmarked product of elliptic curves is asserted.

**Proposition HT2.** If Q is constant in the marked covering frame, then


```math

 \left[\partial_\tau-
  \frac1{2\pi i\delta}
       (\partial_u\partial_v+\partial_{u'}\partial_{v'})\right]
                           \mathcal C_A^Q=0.
 \tag{HT9}

```


The family transports under every unitary marked isomorphism carrying
the ordered pair, inversion, Q and the full zero-algebra probes together.
The result is a marked invariant. Replacing the inversion boundary by
Q^{-1} is a different observable and loses scalar multiples of Q.

**Proof.** Leibniz and (HT7) prove (HT9), with no derivative acting on
Q or the fixed boundary. A marked isomorphism conjugates every factor
in (HT8); trace is invariant. If the last boundary is Q^{-1}, replacing
Q by cQ cancels c against c^{-1}. QED.

This is a specified second-order system in the actual retained relative
variables. It is not a zero-order connection equation in disguise.
Its heat operator is standard; the usefulness below concerns its coupled
solutions and fixed marking.

For later bounds put


```math

 L(u,v;\tau)=p^{-1}\sum_{r,s}|K_{r\delta,s\delta}(u,v;\tau)|.
 \tag{HT10}

```


Then


```math

 \|S_A\|_{\rm op}\le L\|A\|_{\rm op},\qquad
 |\mathcal C_A^Q|\le pm\,L(u,v)L(u',v')
                         \|A\|_{\rm op}\|Q\|_{\rm op}.
 \tag{HT11}

```


Indeed each W is unitary, the boundary is unitary, and |tr T|<=pm||T||.
On any compact separated domain the right side is finite and directly
bounded by the normally convergent theta series and nonzero denominators.

## HT3. Exact reconstruction and a separated-contour stability estimate

Choose representatives r,s in {0,...,p-1}, put a_(r,s)=r delta, and
consider the marked lifted centers


```math

                  u_{r,s}=s-r\tau.
 \tag{HT12}

```


For fixed v not in Lambda_tau, exactly the (r,s) term of (HT4) has a
pole at this lift. In fact the argument of the (t,w) term there is
delta[(s-w)+(t-r)tau], which is a lattice element only if r=t,s=w.
Thus


```math

 \operatorname*{Res}_{u=u_{r,s}} S_A
    =\frac{e^{2\pi ia_{r,s}v}}{p\delta}(W_{r,s}\otimes A).
 \tag{HT13}

```


The choice of lifts is essential; monodromy on the elliptic quotient
permutes these matrix residues. It is already part of the fixed boundary
marking and is not suppressed in an unmarked scalar quotient.

Let E_ab be the matrix units of any chosen orthonormal basis of F. Set


```math

 t_{r,s,a,b}=\operatorname{tr}((W_{r,s}\otimes E_{ab})Q).
 \tag{HT14}

```


**Theorem HT3 (marked analytic reconstruction).** The separated
correlation family (HT8) determines Q uniquely. More precisely,


```math

 t_{r,s,a,b}=(p\delta)^2e^{-2\pi ia_{r,s}v}
 \operatorname*{Res}_{u=u_{r,s}}
 \operatorname*{Res}_{u'=0}\mathcal C_{E_{ab}}^Q,
 \qquad
 Q=\frac1p\sum_{r,s,a,b}t_{r,s,a,b}
                            W_{r,s}\otimes E_{ba}.
 \tag{HT15}

```


Consequently two Q give the same correlations on any nonempty open
subset of the connected separated cover if and only if they agree.
If the labels are transported by a marked isomorphism, the recovered
operators are transported by that same isomorphism.

**Proof.** At u'=0 the residue of S_I is
(P tensor I)/(p delta). Its product with the fixed final boundary is
I/(p delta). Equation (HT13) gives the first formula. By (HT5),
{p^(-1/2) W_rs tensor E_ab} is an orthonormal Hilbert--Schmidt basis,
which gives the second formula and also


```math

                     \|Q\|_{\rm HS}^2
                         =p^{-1}\sum_{r,s,a,b}|t_{r,s,a,b}|^2.
 \tag{HT16}

```


Equality on an open separated set implies equality meromorphically
and hence equality of the residues. Transport follows from HT2. QED.

The reconstruction can be performed without sampling at a pole or
coincident insertion. Take circles Gamma_i about u_i of radii rho_i
and Gamma_0 about u'=0 of radius rho_0, containing no other center
pole of the relevant kernel. Choose fixed generic v,v' and sufficiently
small circles so all four insertion points stay pairwise separated.
Replace each double residue in (HT15) by
(2pi i)^(-2) times the integral over Gamma_i times Gamma_0.
These integrals converge absolutely and are unchanged by contour
deformations enclosing exactly those same poles. No subtraction scheme
or choice of regularized diagonal value occurs.

For an explicit admissible scale, distinct center poles in the u-plane
are separated by at least min(1,Im(tau))/(2k). Thus radii smaller than
min(1,Im(tau))/(8k), and then decreased to respect the finite insertion
separations, suffice.

**Theorem HT4 (stability and finite sampling).** Suppose each measured
correlation for A=E_ab differs from its true value by at most epsilon
on every chosen product of circles. Use those data in the integral
formula and reconstruct Q_hat by (HT15). Put


```math

        M_0=\max_{r,s}
            |e^{-2\pi ia_{r,s}v}|\,\rho_{r,s}\rho_0.
 \tag{HT17}

```


Then


```math

 \|\widehat Q-Q\|_{\rm op}
 \le\|\widehat Q-Q\|_{\rm HS}
 \le \sqrt p\,m\,(p\delta)^2 M_0\epsilon.
 \tag{HT18}

```


There is also an explicit finite sampling bound. Suppose, for every
i=(r,s) and A=E_ab, the pole-cancelled function


```math

 f_{i,A}(w,w')=\rho_i\rho_0ww'
     \mathcal C_A^Q(u_i+\rho_iw,v;\rho_0w',v';\tau)
 \tag{HT19}

```


is holomorphic on a neighborhood of the closed bidisc |w|,|w'|<=R,
where R>1, and has absolute value at most M there. Such R exists after
shrinking the contours. Approximate its constant coefficient by the
average at the N^2 pairs of Nth roots of unity. The error in each
unnormalized residue is at most


```math

 \rho_i\rho_0\epsilon
       +M\bigl[(1-R^{-N})^{-2}-1\bigr].
 \tag{HT20}

```


The corresponding Hilbert--Schmidt error is bounded by
sqrt(p)m(p delta)^2 times the maximum of (HT20) multiplied by
|exp(-2pi i a_i v)|. In particular exact-data sampling converges
exponentially in N. This is a quantitative estimate for this observable,
not a bound on recovery from an arbitrarily conditioned finite matrix
of point evaluations.

When an a priori bound ||Q||_op<=B is known (B=1 for unitary marks),
an admissible M is obtained from (HT11): on the distinguished boundary
|w|=|w'|=R, bound each function in (HT19) by
rho_i rho_0 R^2 pm B L(u_i+rho_i w,v)L(rho_0 w',v').
Take the maximum over the finitely many i and the boundary variables.
Successive applications of the maximum principle give the same bound
on the closed bidisc. The L factors are explicit finite sums of theta
quotients with nonzero denominators there, so their bounds require no
unknown entries of Q. This identifies the data needed for an effective
sampling guarantee rather than assuming an unmeasured matrix norm.

**Proof.** The double integral of an error bounded by epsilon has
absolute value at most rho_i rho_0 epsilon. Apply the normalization
in (HT15), then the exact Parseval identity (HT16), which has p^2 m^2
coefficients. This proves (HT18). For (HT20), write
f=sum_(a,b>=0)c_ab w^a(w')^b. Cauchy's estimate gives
|c_ab|<=M R^(-a-b). Root-of-unity averaging retains exactly the
coefficients c_(jN,lN). The unwanted sum is at most
M sum_(j,l>=0,(j,l)!=(0,0)) R^(-N(j+l)), the displayed expression.
The noise contribution has absolute value at most rho_i rho_0 epsilon
because |w|=|w'|=1. Parseval gives the final bound. QED.

## HT5. Modular transport of the heat system and the marking

Let gamma=[[a,b],[c,d]] in SL_2(Z), j=c tau+d, and


```math

 \tau^\gamma=(a\tau+b)/j,\quad
 (u^\gamma,v^\gamma)=(u/j,v/j),\quad
 (r^\gamma,s^\gamma)=(dr+cs,br+as)\pmod p.
 \tag{HT21}

```


There is a unitary Clifford implementer C_gamma, unique up to scalar,
such that


```math

 C_\gamma W_{r,s} C_\gamma^{-1}
                      =W_{r^\gamma,s^\gamma},\qquad
 C_\gamma P C_\gamma^{-1}=P.
 \tag{HT22}

```


This can be checked on the generators. For gamma=S=[[0,-1],[1,0]],
use C_S e_j=p^(-1/2) sum_i zeta^(-kij)e_i; it sends (r,s) to (s,-r).
For gamma=T=[[1,1],[0,1]], use
C_T e_j=zeta^(k j^2/2)e_j, with 1/2 interpreted in F_p; it sends
(r,s) to (r,r+s). Both commute with P. Composing gives (HT22).
Any two such implementers induce the same action on the Weyl basis,
so their quotient is scalar; no choice of metaplectic phase enters the
conjugation laws below.

**Theorem HT5 (modular heat covariance).** With Q transported to
(C_gamma tensor I)Q(C_gamma tensor I)^(-1), the kernel and correlation
obey


```math

 S_A(u^\gamma,v^\gamma;\tau^\gamma)
 =j\exp\!\left(\frac{2\pi ic\delta uv}{j}\right)
 (C_\gamma\otimes I)S_A(u,v;\tau)(C_\gamma\otimes I)^{-1},
 \tag{HT23}

```



```math

 \mathcal C_A^{Q^\gamma}(u^\gamma,v^\gamma;
                         u'^\gamma,v'^\gamma;\tau^\gamma)
 =j^2\exp\!\left(\frac{2\pi ic\delta(uv+u'v')}{j}\right)
                                \mathcal C_A^Q(u,v;u',v';\tau).
 \tag{HT24}

```


These laws intertwine the differential operators, not just solutions.
Define the transformed function by
(M_gamma f)(u^gamma,v^gamma,tau^gamma)
=j exp(2pi i c delta uv/j)f(u,v,tau). Then


```math

 \mathcal H_{\delta}^{\gamma}(M_\gamma f)
   =j^3 e^{2\pi ic\delta uv/j}\mathcal H_\delta f.
 \tag{HT25}

```


For the four-variable operator in (HT9), the analogous factor is
j^4 exp(2pi i c delta(uv+u'v')/j).

**Proof.** The standard odd-theta modular formulas, with their scalar
multiplier cancelled in the quotient, give


```math

 \phi(z/j,v/j;\tau^\gamma)
           =j e^{2\pi iczv/j}\phi(z,v;\tau).
 \tag{HT26}

```


For alpha=r delta,beta=s delta put
alpha'=d alpha+c beta, beta'=b alpha+a beta. Then
alpha' tau^gamma-beta'=(alpha tau-beta)/j. Substitution into (HT26)
and c alpha tau-c beta+alpha'=j alpha give
K_(alpha',beta')(u/j,v/j;tau^gamma)
=j exp(2pi i c delta uv/j)K_(alpha,beta)(u,v;tau).
Integer shifts of the characteristics do not matter. Reindexing the
finite sum and using (HT22) proves (HT23); trace and the fixed transported
boundary give (HT24).

For the operator identity, in the inverse coordinate change
partial_(tau^gamma)=j^2 partial_tau+cj(u partial_u+v partial_v)
and partial_(u^gamma)partial_(v^gamma)=j^2 partial_u partial_v.
Differentiating j exp(2pi i c delta uv/j) cancels the two first-order
terms and the scalar term exactly. The surviving terms give (HT25).
For two pairs the same calculation has scalar prefactor j^2 and two
mixed derivatives; their scalar cancellations give j^4. QED.

Equations (HT23)--(HT25) transport the specified marked kernel system.
They do not prove modular compatibility of a different charged fusion
map, nor assert a scalar modular form after forgetting the marks.

## HT6. Comparison controls, phase ablation and applications

### Equal individual spectra do not determine the coupled observable

In the associative finite Heisenberg control take m=1 and Q=V.
For every c in mu_p, cV has the same characteristic polynomial t^p-1,
the same traces of all powers, and therefore the same oscillator/Fock
trace determined solely by these eigenvalues. Nevertheless


```math

                    \mathcal C_A^{cQ}=c\mathcal C_A^Q,
 \tag{HT27}

```


and this family is nonzero for Q!=0 by HT3. The fixed inversion boundary
distinguishes them. The graph-only ablation
tr(S_A Q S_B Q^(-1)) is unchanged under Q->cQ. These are exact statements
about a common kernel system, not an assertion that all finite joint
tensors or the complete marked seed agree.

### An actual proper-Bol isotope comparison

Use the established cubic loops Q_h, h in F_p, from
[the cubic-isotope manuscript, (S1)--(S12)](bol-cubic-isotopes.md):


```math

 (c,a,b)\cdot_h(d,u,v)
  =(c+d+bu(a+u)+h(av-bu),a+u,b+v).
 \tag{HT28}

```


They are proper left Bol loops; at p=3, Q_0 and Q_1 are the existing
nonisomorphic principal-isotope controls. All labeled individual left
translation cycle types and all associator-defect permutations agree
as stated in (S11),(S19) of that source. Their whole multiplication
groups are conjugate by F_h(d,u,v)=(d+huv,u,v), but their distinguished
left-translation transversals are not carried to each other.

The single left-translation label X=(0,0,1), transported to the common
group by F_h^(-1), is


```math

 Q_h=T_0(0,1,-2h,0):(d,u,v)\longmapsto
                                  (d+u^2-2hu,u,v+1).
 \tag{HT29}

```


On the nonzero central-character space consisting of functions
zeta^(-d)f(u,v), the ordinary representation by pullback with the
inverse permutation gives


```math

             Q_h=\operatorname{diag}_{u}
                       (\zeta^{u^2-2hu})\otimes V_v.
 \tag{HT30}

```


The common holonomy pair is the central shear
T_0(0,0,-1,0) and T_0(1,0,0,0). These act as U and V on u, so H=C^p_u
tensor C^p_v and **the whole zero algebra is Mat_p on v**. Both operators
come from the actual multiplication group; the shear is an associator
defect, not an arbitrary extra permutation. Under F_h they are the
corresponding marked shear and first-coordinate left translation in Q_h.

Every Q_h has every pth root of unity as eigenvalue with multiplicity p:
for each u, its v-block is a scalar pth root times the p-cycle V_v.
Thus even their corresponding charged individual spectra agree. But for
A=V_v^(-1), k=1 in the heat model, the extracted coefficient is


```math

 \operatorname{tr}((W_{r,s}\otimes V_v^{-1})Q_h)
                          =p\zeta^{r^2+2hr}.
 \tag{HT31}

```


Indeed the unique fixed index of the reflection W_(r,s) is u=-r,
where its phase in (HT6) is 1; the v trace is p. At p=3,r=1 this is
3zeta for h=0 and 3 for h=1. Hence the separated correlations differ.
This calculation uses a nontrivial zero-algebra probe and fixed
holonomy/inversion markings. It is a marked isotope comparison, not a
classification by the unmarked scalar correlation set. Their known
nonisomorphism follows independently from the inverse-property test in
the cited source; no new unmarked-isomorphism criterion is inferred.

### Charge-changing marks and the rigid central phase

There is a useful exact extension when a marked torus operator changes
the physical charge. Let H_1,H_2 have the same dimension pm and their
own marked-pair kernels with parameters delta_1,delta_2. Fix a unitary
reference map J:H_1->H_2. For Q:H_1->H_2 use


```math

 \operatorname{tr}_{H_2}\left(
 S_A^{(2)}Q S_I^{(1)}\mathcal P_1 J^{-1}\right).
 \tag{HT32}

```


The two center residues recover the coefficients of QJ^(-1) on H_2.
Replace (p delta)^2 in (HT15),(HT18) by
(p delta_1)(p delta_2). Thus Q is recovered. The mixed heat operator
uses the two respective coefficients, and its modular exponential is
2pi i c(delta_2 uv+delta_1 u'v')/j. All proofs above are unchanged.
The reference J and both holonomy pairs must be transported as markings.

In particular if Q_f(a)=chi_ell(f(a))J_a for a retained split-torus
reference J_a, with ell denoting the output charge, (HT32) detects the
scalar chi_ell(f(a)); replacing f(a)
by f(a)+z multiplies the correlation by chi_ell(z). Keeping all central
characters separates z whenever the kernel family contains a primitive
marked pair for each detecting character. For the rigid bimap, every
nonzero character has positive rank, so such a pair exists in each
nonzero sector. This is a symbolic conditional application to the
already specified rigid construction and strict marked interface; it
does not reprove its construction or nonisomorphism theorems. It does
not enumerate its enormous modules. Choosing J_a=Q_f(a) afresh for each
input would erase precisely this phase and is disallowed in this marked
comparison.

### What this enables, and what it leaves open

HT3--HT4 turn the retained boundary data into a recoverable analytic
observable with an effective error bound. They distinguish prescribed
marks invisible to individual spectra and quantify how separated
correlation measurements recover them. HT5 proves the exact modular
and heat transport needed for this observable. The comparison class is
all Q with fixed holonomy pair and the same individual spectrum; the
examples show an additional constraint beyond that class's individual
trace functions. No such additional claim is made relative to the entire
finite coupled matrix tensor (HT14), which is exactly reconstructed.

The all-charge finite dynamical tensorator and its Chern-compatible
auxiliary action remain a separate construction. A theorem identifying
this heat kernel with its fusion, through the actual shifts, multiplicities
and carry lines, is still needed for a combined functor. The relative-
coordinate heat repair and true-dual Serre contraction do not presently
supply it: the former retains all coordinates, while the latter cannot
make ordinary positive-degree multiplication heat-horizontal. The
principal-symbol and nonzero H^0 defect tests in TH2--TH5 remain in force.
This manuscript proves a scoped positive analytic reconstruction theorem,
not completion of the full charged dynamical sewing objective.

## Sources and reproduction

The theta normalization, Fourier series and period laws are NIST DLMF,
version 1.2.8 (2026-09-15), [20.2.1](https://dlmf.nist.gov/20.2.E1),
[20.2.6](https://dlmf.nist.gov/20.2.E6), and
[20.2(iv)](https://dlmf.nist.gov/20.2.iv). Modular generators are
[20.7.26](https://dlmf.nist.gov/20.7.E26) and
[20.7.30](https://dlmf.nist.gov/20.7.E30), after replacing its spatial
variable by pi z. These primary formulas were inspected; the mixed
operator identities, finite basis identities and reconstruction estimates
are proved above. No historical-priority claim is made for the classical
theta, Weyl-basis, Cauchy-integral or Fourier-sampling mechanisms.

Run the exact standard-library controls with assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_heat_repair.py
```

They verify the Weyl basis, exact reconstruction including all matrix
zero modes, modular-generator conjugations, equal-spectrum/phase-erasure
controls and the proper cubic control. The analytic convergence, contour
and heat statements are mathematical proofs, not inferred from those
finite computations or from floating-point theta evaluations.
