# A finite dynamical fusion law from completed marked bilinear forms

**Mira Cult**



This is an explicit finite dynamical twist, with a shifted pentagon through
every physical central charge, including zero and degenerate charges. It is
not yet the requested meromorphic charged intertwiner for the position
connection in [CE4--CE5](bol-charged-exchange.md). Its parameter is a finite
central character, not the continuous Cartan variable q of that system.
The new finite construction is a specialization of the exchange mechanism
of Etingof--Nikshych, not a new general theory of dynamical twists.

The main additional input is an affine completion of the marked bilinear
family. The rigid construction admits such a completion directly from its
retained field scalar and a compatible symmetric form. The resulting marked
twisted products recover the entire original bimap, independently of that
auxiliary completion. Their abstract matrix-algebra ranks do not do so.
Section DD5a realizes the exchange intertwiners as a coherent auxiliary
bundle action and proves horizontality for the independently specified
projectively flat Chern connections, including the varying elliptic modulus.
This is a same-point geometric compatibility theorem; its non-scalar data
remain finite, and it supplies no additional Bol-specific analytic relation.

## DD1. Input, parameter space and an everywhere regular auxiliary family

Use the actual marked class-two group P, ordered axes and bilinear map b
of [CH1](bol-charged-heisenberg-obstruction.md#ch1-the-marked-axes-give-a-genuine-charged-representation).
Write N=|W|, A=Z, A*=Hom_Fp(Z,Fp), and psi(t)=exp(2 pi i t/p).
The physical objects remain all finite-dimensional complex P-modules X.
The central weight-mu space is denoted X[mu]. No regularity of b_mu is
assumed for these physical objects.

For lambda in A*, let B_lambda:W -> W* be the map

    B_lambda(x)(y)=lambda(b(x,y)).

An *affine completion* is an F_p-bilinear form C:W x W -> F_p such that

    F_lambda=C+B_lambda : W -> W*

is invertible for every lambda in A*. C denotes both the form and its
associated linear map; this convention is used only in this manuscript.
This is an explicit extra hypothesis, not a consequence of the Bol identity.
The finite dynamical parameter space is A*, with pullbacks

    t_nu(lambda)=lambda-nu.

Thus lambda is the auxiliary dynamical parameter; mu and nu below
are the physical input charges. They are separate roles.

The initial construction fixes C. The choice-free enriched family retains
all completions C, together with their transport under marked data
isomorphisms. These isomorphisms carry b and C by the same ordered-axis
change of variables. They preserve the completion condition. No preferred
completion or independence of the resulting gauge class is asserted.

**Proposition DD1 (auxiliary projective representations).** For every
lambda define V_lambda=Fun(W,C), with counting inner product, by


```math

 (\pi_\lambda(x,y,z)\phi)(u)
 =\psi\bigl(\lambda(z)+F_\lambda(u,y)
                  +\tfrac12F_\lambda(x,y)\bigr)\phi(u+x).
 \tag{DD1}

```


These are irreducible projective P-modules of dimension N, all having
the same multiplier


```math

 \omega_C(g,h)
 =\psi\!\left(\tfrac12[C(x,y')-C(x',y)]\right),
 \quad g=(x,y,z),\ h=(x',y',z').                       \tag{DD2}

```


Consequently all V_lambda lift to honest representations of the same
central extension P_hat=P x mu_p with multiplication
(g,s)(h,t)=(gh,st omega_C(g,h)). The physical P-modules are inflated to
P_hat with trivial action of its additional central kernel.

**Proof.** The calculation in CH1, replacing B_lambda by C+B_lambda,
has exactly the extra phase (DD2). The projection P -> W plus W is a
group homomorphism. The exponent in (DD2) is an alternating bilinear
form on that quotient, so it is a group 2-cocycle. The second-axis
operators in (DD1) give every character of W because F_lambda is
invertible. Their commutant is diagonal; the first-axis translations
make that diagonal constant. This proves irreducibility. QED.

The new V_lambda are auxiliary projective modules. They are not claimed
to be the old linear H_lambda or to give a multiplicative loop
representation. In particular regularizing a physical degenerate charge
has not deleted that physical charge: only the auxiliary Hom realization
has changed.

**Proposition DD2 (all-charge dimension identity).** For all lambda,mu,


```math

 V_\lambda\otimes V_{\lambda-\mu}^*
           \simeq \operatorname{Ind}_Z^P\psi_\mu
 \quad\text{as linear P-modules}.                    \tag{DD3}

```


**Proof.** The common projective multipliers cancel. The trace of
pi_lambda(g) is N psi(lambda(z)) for g=(0,0,z), and zero otherwise:
a nonzero first coordinate has no fixed delta basis vector, and a
nonzero second coordinate gives a nontrivial character sum. Thus the
tensor character in (DD3) is N^2 psi(mu(z)) on Z and zero outside Z.
This is exactly the induced character, since Z is central and
[P:Z]=N^2. Equality of complex finite-group characters proves the
assertion. QED.

This verifies Etingof--Nikshych Definition 4.5 for (G,A,K)=(P,Z,P).
The hypothesis and identity are proved here, rather than inferred from
the name "Heisenberg representation."

## DD2. Explicit expectation-normalized intertwiners

Write X_a=(a,0,0), Y_y=(0,y,0). For chi in W*, define the second-axis
projector on any physical module X by


```math

 \Pi^X_\chi=N^{-1}\sum_{y\in W}\psi(-\chi(y))\rho_X(Y_y).
 \tag{DD4}

```


The projectors are pairwise orthogonal and sum to I. In a unitary
realization they are orthogonal projections.

For x in X[mu], define


```math

 \Phi_X(\lambda,x):V_\lambda\longrightarrow
                       V_{\lambda-\mu}\otimes X

```


on the delta basis by


```math

 \Phi_X(\lambda,x)\delta_t
  =\sum_{s\in W}\delta_{s+t}\otimes
       \rho_X(X_{-t})\Pi^X_{-F_{\lambda-\mu}(s)}x.
 \tag{DD5}

```


Let epsilon:Fun(W,C) -> C send every delta_s to 1. This is an
expectation functional, not an invariant vector or a trace.

**Theorem DD3 (explicit Frobenius map).** Equation (DD5) is a natural
linear isomorphism


```math

 X[\mu]\ \xrightarrow{\ \sim\ }\
 \operatorname{Hom}_{\widehat P}
         (V_\lambda,V_{\lambda-\mu}\otimes X),
 \tag{DD6}

```


whose inverse is T -> (epsilon tensor I)T delta_0. In particular it
works at mu=0 and for reducible or degenerate physical modules X.

**Proof.** At delta_0 the second-axis intertwining equation forces
the coefficient of delta_s to lie in X's weight
-F_(lambda-mu)(s). Equation (DD5) has precisely that property.
The first-axis intertwining equation forces the value at delta_t
from the value at delta_0, and gives the displayed rho_X(X_-t).
For a direct check on Y_y, commuting rho_X(Y_y) across rho_X(X_-t)
contributes psi(B_mu(t)(y)); the full output phase is therefore

    F_(lambda-mu)(s+t,y)-F_(lambda-mu)(s,y)+B_mu(t,y)
      =F_lambda(t,y),

as required on the input delta_t. Central weights add correctly.
These axes and the center generate P_hat; the common projective
multiplier was fixed in DD1. This proves intertwining.

Conversely, the second-axis equation makes any T delta_0 a sum of
the same weight components. Because F_(lambda-mu) is invertible,
every second-axis weight occurs at exactly one s. Summing those
components gives x, and the first-axis equation reconstructs all
of T by (DD5). The inverse is therefore the stated expectation.
Every physical P-intertwiner commutes with rho_X and the projectors,
which proves naturality. QED.

## DD3. A closed formula for the finite dynamical fusion operator

The target category has finite-dimensional A*-graded vector spaces
as objects and functions T(lambda) taking values in grade-preserving
linear maps as morphisms. Composition is pointwise. Objects tensor
by adding grades; morphisms tensor by

    (T bar_tensor S)(lambda)|_(X tensor Y[nu])
          =T(lambda-nu) tensor S(lambda).

The two threefold tensors agree because both evaluate the first
map at lambda minus the sum of the two later grades, the second
at lambda minus the last grade, and the third at lambda. This
defines a strict monoidal category, with the usual unit in grade
zero. The functor from physical P-modules forgets to their central
grading and sends every P-intertwiner to its constant function.
We now construct its invertible tensorator.

For Y homogeneous of central weight nu, set


```math

 J_{X,Y}(\lambda)
   =\sum_{s\in W}\rho_X(X_{-s})\otimes
                 \Pi^Y_{-F_{\lambda-\nu}(s)}.
 \tag{DD7}

```


For arbitrary Y, apply (DD7) on each central-weight summand.
Thus J is the action of one explicit element of C[P] tensor C[P]:
insert the central idempotent e_nu in its second factor and sum
over nu. This gives naturality for every physical P-intertwiner.
It preserves the separate central weights of X and Y.

**Theorem DD4 (shifted fusion and pentagon).** J has invertible
values, satisfies J_(1,Y)=J_(X,1)=I, and obeys


```math

 J_{X\otimes Y,Z}(\lambda)
     \bigl(J_{X,Y}(\lambda-\operatorname{wt}Z)\otimes I\bigr)
 =J_{X,Y\otimes Z}(\lambda)
     \bigl(I\otimes J_{Y,Z}(\lambda)\bigr).
 \tag{DD8}

```


On nonhomogeneous Z the shift is applied separately on each of
its central-weight summands. For unitary physical modules, J is
unitary. The complete pentagon for four objects follows, including
all paths through zero central weight.

**Proof.** The inverse of (DD7) replaces X_-s by X_s: the
second-factor projectors are mutually orthogonal. The same
observation proves unitarity. For X=1 all projectors sum to I.
For Y=1 only its zero second-axis weight occurs; invertibility of
F_lambda forces s=0, so the other unit equation holds.

For x in X[mu] and y in Y[nu], compute the composition


```math

 (\Phi_X(\lambda-\nu,x)\otimes I)\Phi_Y(\lambda,y).
 \tag{DD9}

```


It maps V_lambda to V_(lambda-mu-nu) tensor X tensor Y.
Apply its expectation to delta_0 using (DD5). The sum over the
first projector index collapses to I, and the result is exactly
J_(X,Y)(lambda)(x tensor y). By the uniqueness in DD3,


```math

 (\Phi_X(\lambda-\nu,x)\otimes I)\Phi_Y(\lambda,y)
 =\Phi_{X\otimes Y}
       (\lambda,J_{X,Y}(\lambda)(x\otimes y)).          \tag{DD10}

```


Associate a triple composition of the actual Phi operators in the
two possible ways. Equation (DD10) identifies the two expectation
vectors as the two sides of (DD8). Injectivity in DD3 proves
equality. Fourfold composition supplies the pentagon: every route
is the same composition of four actual linear maps. No regularity
of mu,nu or their partial sums is used. QED.

In Hopf notation, (DD8) is exactly

    (Delta tensor id)J(lambda) J^12(lambda-h^3)
      =(id tensor Delta)J(lambda) J^23(lambda),

the dynamical twist condition of EN Definition 2.3. It is outside
the ordinary unshifted rules of [FN1--FN4](bol-fusion-naturality-obstruction.md).
The proof above is the exchange construction of EN Section 6 made
explicit for this completed class-two family.

The operator J is generally not a P-intertwiner for the ordinary
diagonal tensor action. It intertwines the conjugated action


```math

 \rho^{J}_{X,Y;\lambda}(g)
    =J_{X,Y}(\lambda)^{-1}
          (\rho_X(g)\otimes\rho_Y(g))J_{X,Y}(\lambda)
 \tag{DD11}

```


with that ordinary action. Each is an honest representation of P.
Therefore distinguished group-word identities are retained under
this change of tensor action. A claim about all marked Bol
translations additionally needs the indicated equivariant
extension across the retained torus; DD7 below supplies it for
the fixed C in the rigid coordinates. No sandwich identity for
the auxiliary projective pi_lambda is being asserted.

## DD4. Minimality and recovery of the full bimap

Let F_0[P]=Fun(P/Z,C). It has Fourier basis


```math

 e_{\xi,\eta}(x,y,z)=\psi(\xi(x)+\eta(y)),
            \qquad \xi,\eta\in W^*.

```


Give it the product obtained from right translation by J(lambda):


```math

 (f\star_\lambda g)(h)
      =(f\otimes g)((h\otimes h)J(\lambda)).           \tag{DD12}

```


The second factor has central weight zero. Equation (DD7) and
Fourier orthogonality therefore give the explicit multiplication


```math

 e_{\xi,\eta}\star_\lambda e_{\xi',\eta'}
   =\psi\bigl(\xi(F_\lambda^{-1}\eta')\bigr)
                    e_{\xi+\xi',\eta+\eta'}.
 \tag{DD13}

```


**Theorem DD5 (nontriviality and marked reconstruction).** For every
lambda, this algebra is Mat_N(C). If W is nonzero, J is not gauge
equivalent to the identity dynamical twist. The family (DD13),
retaining its Fourier labels and central parameter, recovers every
B_lambda and hence b, independently of C.

**Proof.** The coefficient in (DD13) is a bilinear group 2-cocycle,
so the product is associative. Its alternating commutator form is

    ((xi,eta),(xi',eta')) |->
       xi(F_lambda^-1 eta')-xi'(F_lambda^-1 eta),

which is nondegenerate. More explicitly, send e_(xi,eta) to
V_(-F_lambda^-1 eta) U_xi on Fun(W), where
U_xi phi(u)=psi(xi(u))phi(u) and V_a phi(u)=phi(u+a).
The product is (DD13), and these N^2 operators are an orthogonal
basis of End(Fun(W)). This proves the matrix-algebra assertion.

For completeness use the EN gauge convention

    J^t(lambda)=Delta(t(lambda)^-1) J(lambda)
                    (t(lambda-h^2) tensor t(lambda)).

On F_0[P] all central weights are zero. Thus the shift disappears,
and right translation by t(lambda) is an algebra isomorphism
between the corresponding products (DD12). The identity twist
gives the commutative pointwise algebra C^(N^2), which is not
isomorphic to Mat_N(C) for N>1. Hence no such gauge can trivialize J.
This is also EN Remark 3.2 and Definition 3.9 in this example.

Finally, the coefficients with eta=xi'=0 determine
psi(xi(F_lambda^-1 eta')) for every xi,eta'. Faithfulness of psi
and nondegeneracy of the evaluation pairing recover F_lambda^-1,
and inversion recovers F_lambda. Now

    B_lambda=F_lambda-F_0.

Since all lambda in Z* separate Z, these scalar forms recover b.
The auxiliary C=F_0 cancels in the difference. QED.

All abstract fibers in DD5 have the same dimension and are the
same matrix algebra. Their marked multiplication constants retain
the bimap. Forgetting those labels and products loses precisely
the information used by this reconstruction statement. This is
a finite structural result, not a new modular or analytic identity.

## DD5. Zero sectors, duals and the degree/carry factors

The parameter shifts are finite translations lambda -> lambda-nu.
There is no pole at nu=0, lambda=0, or a degenerate b_nu: every
inverse in DD5--DD7 is an auxiliary F_lambda inverse. Thus the
full physical neutral endomorphism sectors of CH2--CH3 remain in
the domain, with their full zero algebras. They have not been
replaced by a scalar or by the auxiliary simple algebra of DD5.

Retain also the integer degree k of [CH4](bol-charged-heisenberg-obstruction.md#ch4-a-geometric-integer-extension-and-coherent-carry-lines).
The group-algebra operator J preserves each physical degree
summand, since P preserves it. Tensor degrees still add. The
normalized carry line L^n(mu,nu) is unchanged; J acts trivially
on that line. The carry cocycle equation and the shifted equation
(DD8) hold together because the line factors commute with the
finite operators. True duals still have degree -k and central
weight -mu; all channels required by those duals are present.

In the target dynamical category the evaluation and coevaluation
transported by this strong monoidal functor are explicitly

    ev_X^J(lambda)=ev_X J_(X*,X)(lambda),
    coev_X^J(lambda)=J_(X,X*)(lambda)^-1 coev_X.

Their two triangle identities follow by applying (DD8) to the
three factors in each triangle and then using the unit equations
and the original evaluation identities. The shifts in the
tensoring of these maps are the target-category shifts just
defined. Ordinary evaluation cannot simply be kept without
these tensorator factors. This duality operation does not remove
the other states in X tensor X*.

At the bundle level, conjugate the tensor holonomy pair by J as
in (DD11). The scalar automorphy factor of degree k_X+k_Y
commutes with J, so J gives a holomorphic map from that conjugated
bundle to the ordinary tensor bundle. Existing CH fusion
intertwiners can be composed with it where appropriate, with the
full zero decomposition used instead of an inverse B_0.

More explicitly, if C_(mu,nu) is the regular-sum CH intertwiner,
the finite-parameter charged fusion map is

    F_(mu,nu)(lambda)=C_(mu,nu) J_(H_mu,H_nu)(lambda).

It maps the conjugated tensor action (DD11) to
H_(mu+nu) tensor Fun(W), with the CH carry line included for
normalized degree representatives. At nu=-mu use the full
endomorphism identification instead. At a degenerate nonzero
sum, the physical tensor module remains an object of the
construction, with its full canonical isotypic decomposition;
no inverse B_(mu+nu) or choice of multiplicity basis is assumed.
Combining the J tensorators with the actual CH changes of fusion
tree gives the corresponding shifted coherence: (DD8) equates
the J composites, while CH supplies the finite reassociation.

This last geometric statement is deliberately limited: J is
constant in the analytic variables z,tau. Defining a connection
by the same conjugation would give transport of that connection,
not an independently forced analytic sewing law. In particular
it does not establish compatibility with the separate continuous
Cartan systems of CE4--CE6.

For auxiliary projective modules the true contragredient of
V_lambda^C is V_(-lambda)^(-C), not another module with multiplier
omega_C. If auxiliary duals are used, retain both completion
families C and -C. The physical modules X and their duals are
ordinary P-modules throughout.

## DD5a. A horizontal auxiliary bundle action with actual carry lines

Fix the marked holonomy pair u_0,v_0 of CH4, write
c=[u_0,v_0], and put

    d_C=C(x_(u_0),y_(v_0))-C(x_(v_0),y_(u_0)) in F_p.

The auxiliary holonomies satisfy

    pi_lambda(u_0) pi_lambda(v_0)
       =psi(lambda(c)+d_C) pi_lambda(v_0) pi_lambda(u_0).

This follows from DD2's multiplier ratio and the central commutator
in P. Choose an integer s_lambda representing -lambda(c)-d_C
for each lambda, and set kappa_lambda=s_lambda/p. These are chosen
integer lifts, not additional identities on the physical charges.

The continuous parameter base is the universal elliptic curve

    E_univ=(C x H)/Z^2 -> H,
    (m,n).(z,tau)=(z+m+n tau,tau),  Im(tau)>0.

The complete parameter base is A* x E_univ. Its auxiliary pullback
for a physical charge mu is

    t_mu(lambda,z,tau)=(lambda-mu,z,tau).

All physical bundles and carry lines below are pulled back from
E_univ; every insertion is at this same point (z,tau). There is
no position-configuration space and no continuous Cartan variable q.
No descent by SL_2(Z) is asserted here.

Let E_lambda^C have covering fiber V_lambda and factors

    J_1=pi_lambda(u_0),
    J_tau(z)=exp(-pi i kappa_lambda tau-2 pi i kappa_lambda z)
                 pi_lambda(v_0).

Their consistency follows exactly as in CH4 from
kappa_lambda == -(lambda(c)+d_C)/p modulo integers. These are
honest holomorphic bundles despite the projectivity of pi_lambda
as a P-module. Give them the CH Hermitian metric

    h_kappa(z,tau)=exp(-2 pi kappa (Im z)^2/Im tau) I.

Physical unitary X of homogeneous charge mu, with any integer
k congruent to -mu(c) modulo p, has its separately defined CH
bundle E_(X,k) with this metric at slope k/p. Let L be the CH
degree-one theta line with metric h_1. Define the actual integer
carry


```math

 n(\lambda,\mu;k)
       =\frac{s_\lambda-s_{\lambda-\mu}-k}{p}\in\mathbb Z.
 \tag{DD16}

```


Negative powers of L are its genuine dual line bundles. Integrality
in (DD16) uses the two displayed residue conditions; no inverse
of a physical charge form is involved.

**Theorem DD5a (horizontal module action).** The expectation map


```math

 \mathcal U_{\lambda,X}(v\otimes x)=\Phi_X(\lambda,x)v
 \tag{DD17}

```


is a unitary isomorphism on fibers and descends to a holomorphic,
Chern-parallel bundle isomorphism


```math

 \mathcal E_\lambda^C\otimes\underline{X[\mu]}
   \longrightarrow
 \mathcal E_{\lambda-\mu}^C\otimes\mathcal E_{X,k}
                  \otimes\mathcal L^{n(\lambda,\mu;k)}.
 \tag{DD18}

```


Here the underlined multiplicity space has the constant metric,
trivial holonomy and trivial connection. It is not E_(X,k).
The finite tensorators J in DD7 are precisely the comparison
maps for composing these auxiliary bundle actions. With the
actual line identifications they obey the shifted pentagon,
including zero charges, degenerate physical charges and true
physical duals.

**Proof.** Choose the P-invariant Hermitian metric on X used in
CH4. For x,y in X[mu], the operator Phi_x^* Phi_y commutes with
the irreducible unitary P_hat-module V_lambda, so it is scalar.
Its delta_0 matrix coefficient, from DD5 and the orthogonal
projectors DD4, is

    sum_s <Pi_(-F_(lambda-mu)(s)) x,
           Pi_(-F_(lambda-mu)(s)) y> = <x,y>.

Thus <Phi_x v,Phi_y w>=<v,w><x,y>. The total map (DD17) is an
isometry. Source and target have the same dimension N dim X,
so it is unitary and onto. The action on its input is pi_lambda
on V_lambda and the trivial P_hat-action on the multiplicity
label X[mu]; the output uses pi_(lambda-mu) tensor rho_X.
This is exactly the equivariance proved in DD3.

The constant matrix (DD17) intertwines both holonomy matrices.
For the scalar factors the required slope equality is the exact
integer identity

    kappa_lambda=kappa_(lambda-mu)+k/p+n(lambda,mu;k).

Consequently it descends to (DD18). The same equality makes the
product output metric equal to the input metric, since the finite
map is unitary. One can also check the connection equation
directly, with no connection defined by conjugating U. In the
covering holomorphic frames, the independently defined Chern
connection one-form on a slope-kappa bundle is


```math

 \mathcal A_\kappa
 =-2\pi\kappa\,\partial\!\left(
                   \frac{(\operatorname{Im}z)^2}{\operatorname{Im}\tau}
                            \right)I
 =2\pi i\kappa\left(
       \frac{\operatorname{Im}z}{\operatorname{Im}\tau}\,dz
       -\frac{(\operatorname{Im}z)^2}{2(\operatorname{Im}\tau)^2}
                                                        \,d\tau
                         \right)I.                  \tag{DD19}

```


The partial derivative is on C x H, in both z and tau. The
source has A_in=A_(kappa_lambda); the target has
A_out=A_(kappa_(lambda-mu))+A_(k/p)+A_n=A_in. Since the matrix
U is constant in these frames,


```math

 d\mathcal U+\mathcal A_{\rm out}\mathcal U
                     -\mathcal U\mathcal A_{\rm in}=0.\tag{DD20}

```


This is a statement for the full Chern connection, whose (0,1)
part in these frames is bar_d. It includes variation in tau.
Its curvature is generally nonzero: on an elliptic fiber it is
-2 pi i kappa dx wedge dy/Im(tau) times I. The connections are
projectively flat, not flat local systems.

For X[mu],Y[nu] of degrees k,l, the two carry exponents satisfy


```math

 n(\lambda,\nu;l)+n(\lambda-\nu,\mu;k)
          =n(\lambda,\mu+\nu;k+l).                 \tag{DD21}

```


Both sides telescope to
(s_lambda-s_(lambda-mu-nu)-k-l)/p. Thus DD10 is an equality of
the actual line-valued, horizontal bundle maps: the sequential
action equals the action of X tensor Y after its multiplicity
input is acted on by J_(X,Y)(lambda). Repeated telescoping
identifies the line powers for every tree; DD8 and the actual
composition of Phi maps prove its shifted pentagon. If X is
followed by its true dual, the degrees k,-k give total degree
zero, and (DD21) gives total carry zero. The full physical
endomorphism object remains, as in DD5. No channel was omitted.
QED.

This construction gives an explicit solution of a connection
intertwining equation between independently specified systems,
including genuine multiplicities and carry lines. It is an
auxiliary module action: the input in (DD18) contains a constant
multiplicity space, whereas the output contains the physical
bundle. It is not a fusion map between separated physical
insertion points or a horizontal map for the CE q-connection.

For a meromorphic display, use the CH theta section
theta(z;tau) of L. In the local carry frame theta^n, equation
(DD18) has matrix theta(z;tau)^(-n) U. Its coefficients have the
corresponding zeros or poles of order -n at the theta divisor.
The carry connection in this frame is A_n+n d log(theta), which
must still be included in A_out; (DD20) then remains true.
This analytic dependence and its divisor are forced by the
chosen degree/holonomy geometry and standard theta theory.
The non-scalar information is the finite Phi/J family. No new
coupling of inequivalent holonomies or additional Bol-specific
analytic rigidity is inferred from this scalarization.

If auxiliary duals are also taken, their labels are
(-C,-lambda,-s_lambda), so the dual bundle has the exact opposite
slope. Replacing that integer by a normalized representative
requires its actual extra theta-line power. Physical true duals
already use the exact degree -k in the theorem above.

## DD6. A compact sufficient criterion and the rigid completion

**Theorem DD6 (field-degree completion).** Suppose W=E^m for
E=F_(p^r), and

    B_lambda(x,y)=Tr_(E/Fp)(x^t M_lambda y),

where every M_lambda has entries in F_p. Let S be any invertible
m by m matrix over F_p and alpha in E have degree r>m over F_p.
Then

    C(x,y)=Tr_(E/Fp)(alpha x^t S y)

is an affine completion.

**Proof.** For each lambda the polynomial
det(t S+M_lambda) is nonzero of degree m, with leading coefficient
det S. It cannot vanish at alpha, whose minimal polynomial has
degree r>m. Thus alpha S+M_lambda is invertible over E. The
nondegenerate field trace pairing then makes the corresponding
F_p-bilinear form nondegenerate. QED.

For the pinned
[rigid source](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-rigid-center-nongloop.md#data),
E=F_(3^18), m=4, and the retained d-action is multiplication by
alpha of order 19. Since ord_19(3)=18, this alpha has degree 18.
The matrices M_lambda are the specified combinations of B_0,B_1,B_2.
Take


```math

 S=\operatorname{diag}\!\left(
       \begin{pmatrix}0&1\\1&0\end{pmatrix},
       \begin{pmatrix}0&1\\1&0\end{pmatrix}\right).
 \tag{DD14}

```


Theorem DD6 proves regularity simultaneously for all 27 auxiliary
parameters. No field table or 3^72-dimensional operator is enumerated.

For R=diag(J_2,J_2), J_2=((1,1),(0,1)), direct multiplication gives
R^t S=S R. Hence

    C(Rx,R^-1 y)=C(x,y).

The d-scalar action also preserves C because the two axes scale
inversely. Thus this particular completion is compatible with the
retained split torus. The matrix S is additional coordinate data;
under a marked isomorphism it must be transported along with C.
No assertion that this displayed S is invariant under every
automorphism of the original unaugmented data is made.

## DD7. Marked torus transport and the positive cocycle boundary

Suppose a marked torus element a satisfies

    b(R(a)x,R(a)^-1 y)=T(a)b(x,y),
    C(R(a)x,R(a)^-1 y)=C(x,y).

Set a.lambda=lambda composed with T(a)^-1. Then
F_(a.lambda)(R(a)x,R(a)^-1 y)=F_lambda(x,y).
Coordinate transport A_a phi(u)=phi(R(a)^-1u) intertwines the
auxiliary projective modules, with the same multiplier transported
by the P-automorphism. The formulas for Phi and J transport as
well, because their projectors and X_s are transported by those
same marked axes. This supplies the equivariant extension needed
for the tensor action on the corresponding local semidirect
group. The other factors may act trivially as in CH1.

For the outside involution exchanging the axes, the general
completion transforms as C -> -C^t. In the symmetric rigid
choice this is -C, not C. The transformed completion is still
regular because the scalar form becomes -F_lambda^t after the
corresponding central-character transport. One must retain that
completion/polarization orbit; a fixed-C outside action is not
asserted. This is separate from the physical dual convention.

Fixed positive-cocycle markings can be retained as the graph
operators

    U_a^f|_(lambda)=psi((a.lambda)(f(a))) A_a

together with the separately fixed A_a and outside marking.
Their scalar ratio recovers all characters of f(a), so retaining
these marks retains f. The J family alone is determined by b,C
and contains no f.

The old erasure remains exact. If f changes to f+(1-T)z, define
D_z|_(lambda)=psi(lambda(z)). These scalar charge phases intertwine
the graph transports as in CH5. J preserves the separate physical
central weights, so it commutes with their tensor phases; the
shifted fusion law does not obstruct that graph-only equivalence.
Thus this new twist does not itself supply an unmarked analytic
separator of the rigid isotope pair. Fixed split/outside/boundary
markings must survive a later analytic construction.

## DD8. Small control, literature position and the remaining analytic task

A small completion exists over W=F_3^2, Z=F_3 with
B_lambda=lambda I and C=((0,2),(1,0)). Every C+lambda I is
invertible. On delta bases of the physical Schrödinger modules
H_mu,H_nu, the twist has the exact permutation form


```math

 J_{H_\mu,H_\nu}(\lambda)
       (\delta_x\otimes\delta_y)
 =\delta_{\,x-F_{\lambda-\nu}^{-1}(\nu y)}
                                  \otimes\delta_y.   \tag{DD15}

```


The zero physical charge is included. The
[exact script](../code/verify_bol_dynamical_twist.py) and its
[calculation record](../evidence/bol-dynamical-twist-certificate.md)
check the projective multiplier, intertwiners, twist identities,
Fourier products, reconstruction, total expectation-map unitarity,
integer carries, and compact rigid completion conditions. The
full Chern-connection identity is proved in DD5a; the finite
controls do not establish it by numerical testing. Universal
proofs are above, not inferred from tests.

The precise primary reference is P. Etingof and D. Nikshych,
*Dynamical twists in group algebras*, IMRN 2001(13), 679--701,
DOI 10.1155/S1073792801000356; arXiv:math/0101046v2 (29 January 2001).
The accessible [PDF](https://arxiv.org/pdf/math/0101046) identifies
that exact version on its first page. Definition 2.3 fixes the
shift convention, Definition 2.5 the gauge convention, Section 3
equation (12) and Remark 3.2 the algebra and its gauge invariance,
Definition 4.5 the datum, and Section 6 equations (25)--(27) and
Theorem 6.4 the exchange construction. The nilpotent construction
in Section 7, Lemma 7.1 and Proposition 7.2, is an analogous use
of an extra central multiplier to keep a whole family regular.
Those original passages were inspected. The mathematical
mechanism here is an explicit specialization, with a separate
compact completion criterion and marked reconstruction argument;
no literature-priority claim is made.

The dynamical variable lambda is discrete. Replacing it or the
finite-field scalar alpha by an arbitrary complex variable would
destroy the finite-character formulas and is not an analytic
extension. Spectral Baxterization or transport of an arbitrary
connection by J would require their own hypotheses and would
still need the standard-mechanism ablation.

The actual remaining task is an independently specified
noncoincident analytic connection, with explicit continuous
parameter bases and pullbacks, that is compatible with this
shifted law (or a justified replacement), with the complete
zero/carry channels and the fixed cocycle marks. No such elliptic
noncoincident compatibility, new Bol-forced coefficient relation,
modular isotope invariant or arithmetic consequence is proved
by DD1--DD8.
