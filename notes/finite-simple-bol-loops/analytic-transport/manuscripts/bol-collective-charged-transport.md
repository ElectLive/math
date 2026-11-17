# Collective charged transport with a finite dynamical parameter

**Mira Cult**



## Contract and mathematical scope

This constructs a **collective** differential/difference system on the
charged modules of [CH](bol-charged-heisenberg-obstruction.md), and proves
compatibility with the finite dynamical twist of
[DD](bol-dynamical-fusion-construction.md). Collective means that a
marked group operation acts on all factors at once. Its infinitesimal
generator on a tensor product is therefore `rho(g) tensor rho(g)-I`,
not the sum of two one-factor generators. This is an explicit change of
tensor rule, not a restriction of the intertwiner category. All morphisms
in the specified representation category are retained.

The continuous parameters are a rational separated-point variable t and
the elliptic variables (z,tau). The dynamical parameter is **finite**.
This is not the CE Felder system, whose Cartan parameter is continuous;
nor is it a heat connection. The modulus direction here is the full
Chern connection. It has a modular law on the subgroup preserving the
chosen level and theta marking. There is no identification with the old
Fock traces. The noncoincident analytic consequences are the quantitative
observability and ordered-transport theorems in
[SA](bol-shifted-analytic-fusion.md).

The tensor coherence alone would be an insufficient payoff: its finite
part is the established DD twist. The additional assertions are the full
operator intertwining identity, convergent analytic parallel transport,
and explicit stable recovery/separation from separated boundary responses.
The analytic mechanism works for other finite marked groups as well.
The Bol content lies in the actual marked operators, the all-charge
representation interface, and the exact controls. No new universal
Yang--Baxter system or claim of literature priority is made.

## CT1. Physical objects, parameter covers, and all channels

Let p be odd. Fix the CH1 marked class-two group

    P=(W+W)+Z,
    (x,y,z)(x',y',z')=
      (x+x',y+y',z+z'+[b(x,y')-b(x',y)]/2).

Let A be the finite retained split-torus group, with its possibly
nonfaithful marked action by automorphisms, and let K=P semidirect A.
Do not replace A by its image in Aut(P): the rigid a has order 9 even
though its local action has order 3. Thus A acts on the two ordered axes by R(a),R(a)^(-1)
and on Z by T(a), with

    b(R(a)x,R(a)^(-1)y)=T(a)b(x,y).

The positive cocycle f and the pure split elements a are separately
retained marks. The graph mark is the actual element g_f=f(a)a of K.
An outside-involution mark can be retained as additional data; no
outside action fixing one polarization/completion is assumed here.

Physical modules are finite-dimensional unitary K-modules, with their
P-central decomposition X=sum_mu X[mu]. One may instead use a
K-equivariant family of P-modules; all formulas are the same on its
finite direct sum. Every P-module, including every CH Schrödinger
module and every one of its degenerate constituents, occurs in the
restriction of Ind_P^K X. Every P-intertwiner induces an intertwiner of
these objects. No physical central charge is removed.

Choose an affine completion C as in DD1 and retain its A-orbit, not just
one representative if it is not invariant. Also retain the K-orbit of
an ordered holonomy pair h=(u_0,v_0) in P. On

    q=(C,h,lambda),      lambda in Z*,

K acts as follows: its P subgroup conjugates h and fixes C,lambda;
A transports C,h and lambda by its actual marked automorphism. This is
a finite parameter cover: explicitly take the chosen K-stable set of
(C,h) pairs times **all** lambda in Z*. It is closed under every t_mu.
When several (C,h) orbits are needed take their disjoint union. In
particular, no assertion that an arbitrary group
element preserves one fixed holonomy pair is used.

For a homogeneous physical input of weight mu, the dynamical pullback is

    t_mu(C,h,lambda)=(C,h,lambda-mu).

The covariance relation is a(lambda-mu)=a lambda-a mu. Incoming/outgoing
charge labels are additional finite indices; fusion sends (mu,nu) to
mu+nu and retains the actual multiplicity, rather than identifying these
indices by a fictitious continuous change of coordinates.

Write c_h=[u_0,v_0]. Over h, a weight-mu physical summand has **every**
allowed integer degree label k satisfying k=-mu(c_h) modulo p.
Its bundle E_(X[mu],k;h) has factors

    J_1=rho_X(u_0),
    J_tau=exp(-pi i(k/p)tau-2pi i(k/p)z)rho_X(v_0).

For one object or one finite diagram only finitely many integer labels
occur; the category includes every integer label and is closed under
tensoring and true duals. The K action transports h and mu together and
leaves k fixed. Admissibility is preserved since
(a mu)(a c_h)=mu(c_h); inner conjugation fixes c_h. Thus the finite
difference action is an action between the actual admissible bundles.

The continuous base is

    B = (C minus {0,1,2})_t times E_univ,
    E_univ=(C_z times H_tau)/Z^2,

with the finite indices just specified. The pole at 2 may be omitted
when its coefficient is zero. Parallel transport in t is on an arbitrary
piecewise C1 path avoiding the poles, or on the universal cover when
a single-valued fundamental solution is desired. No claim of trivial
monodromy on the punctured plane is made. The point t is the fourth
marked point relative to 0,1,infinity; t=2 is an optional additional
marked singularity. None of the estimates below takes a collision limit.

### Canonical multiplicity and zero decompositions

For a tensor product of P-modules the finite fusion decomposition is

    X tensor Y = direct_sum_R R tensor Hom_P(R,X tensor Y),

with R ranging over its actual irreducibles. Evaluation gives the
canonical isomorphism after choosing representatives R; changing a
representative transports its Hom factor contragrediently. Give the Hom
factor the inner product making evaluation unitary. This is a convenient
description, not a suppression of degenerate charges. Where CH2 applies,
use its explicit map C_(mu,nu) and its full Fun(W) multiplicity instead.

At nu=-mu use the full endomorphism/Weyl-character decomposition of CH2--CH3.
In particular the joint trivial-holonomy algebra, possibly Mat_(p^(d-1)),
is kept. The invariant evaluation is one map out of that object, not a
replacement of the object by its scalar trace. A genuinely zero degree
k=0 is allowed in all formulas in this manuscript.

## CT2. The collective operators and their independently specified connection

For any marked g in K, define the operator on sections of the finite
family by


```math

 (\mathsf T^X_g s)(q,z,\tau)
       =\rho_X(g)\,s(g^{-1}q,z,\tau).                 \tag{CT1}

```


Here rho includes the indicated transport between charge components.
For a K-equivariant family, use its specified transport map in place of
the single matrix. The pair label in the input is g^(-1)h g, so CT1
intertwines both holonomies and is a well-defined bundle map over its
finite base translation. These are genuine **difference** operators in
q. They obey T_g T_h=T_(gh), are unitary for the sum of the counting
fiber metrics, and preserve the slope k/p.

On the tensor of two objects the collective operator is


```math

 (\mathsf T^{X\boxtimes Y}_g s)(q)
       =(\rho_X(g)\otimes\rho_Y(g))s(g^{-1}q).        \tag{CT2}

```


The base is translated once. In particular this is not the operator
obtained by applying two independent base translations to one section.
In Hopf-algebra language CT2 is the group-like coproduct Delta(g)=g tensor g.

Fix marked g_0,g_1,g_2 and complex coupling constants u,v,w. For example,
g_0=f(a)a, g_1=a^(-1), and g_2=X_x can be a nonzero first-axis mark.
Let


```math

 \mathsf L_X(t)=\frac{u}{t}(\mathsf T_{g_0}^X-I)
             +\frac{v}{1-t}(\mathsf T_{g_1}^X-I)
             +\frac{w}{2-t}(\mathsf T_{g_2}^X-I).      \tag{CT3}

```


The augmented generator makes the tensor unit's physical fiber action
trivial. On arbitrary scalar functions of q it still acts as the base
difference s(q)->s(g^(-1)q)-s(q); on constant functions it vanishes.
Linear combinations of marked group elements are allowed by linearity;
the analytic proper-Bol control uses (rho(h)+rho(h^(-1)))/2 as one
contraction. Formula CT3 is specified on every physical representation
before choosing any charged fusion map.

On a slope-kappa block put


```math

 \nabla_X= d+\mathcal A_\kappa-\mathsf L_X(t)dt,
 \quad
 \mathcal A_\kappa=
 2\pi i\kappa\left(\frac{\operatorname{Im}z}{\operatorname{Im}\tau}dz
 -\frac{(\operatorname{Im}z)^2}{2(\operatorname{Im}\tau)^2}d\tau\right)I.
                                                               \tag{CT4}

```


This is the CH/DD Chern connection on the elliptic factor, including
both its (1,0) and (0,1) parts, and an independently defined Fuchsian
connection in t. Coupling constants are external parameters; flatness
in their directions is not asserted. Every CT1 commutes with the Chern
operator, because it is a constant unitary holonomy intertwiner of the
same slope. Hence mixed t--elliptic curvature is zero. The remaining
curvature is the known central Chern curvature. We claim projective
flatness on each slope orbit, not a flat elliptic connection.

The collective tensor connection uses CT2 in CT3 and adds the geometric
slopes. It is a specified monoidal rule on representation-generated
systems. It is not the ordinary tensor product of differential
connections; the distinction is essential. For example the generator
rho(g)-I acts on a tensor as rho(g) tensor rho(g)-I, which differs from
rho(g) tensor I+I tensor rho(g)-2I by
(rho(g)-I) tensor (rho(g)-I). This nonzero cross term is precisely what
the primitive-current obstruction FN excludes in its different category.

## CT3. Full charged operator compatibility

Let J_(X,Y)(q) be DD7, with its C and lambda dependence. It preserves
separate central weights and integer degrees, is unitary, and is
covariant under A transport of C and the marked axes. Give the incoming
dynamical tensor the **DD twisted action**


```math

 (\mathsf T_g^{J}s)(q)=
 J(q)^{-1}(\rho_X(g)\otimes\rho_Y(g))
                J(g^{-1}q)s(g^{-1}q).                \tag{CT5}

```


This is the representation of the finite action groupoid supplied by
the twist. Its geometric elliptic holonomies act at **fixed q**:

    U_in(q)=J(q)^(-1)[rho_X(u_h) tensor rho_Y(u_h)]J(q),
    V_in(q)=J(q)^(-1)[rho_X(v_h) tensor rho_Y(v_h)]J(q).

They have no finite-base pullback. In contrast the coefficient R_g^J(q)
in CT5 maps the fiber at q'=g^(-1)q to the fiber at q. These structures
are compatible: using u_(h')=g^(-1)u_h g gives

    R_g^J(q) U_in(q') = U_in(q) R_g^J(q),

by cancellation of J(q'), and the same equation holds for V_in. The
scalar automorphy factors agree because the slope is preserved. Thus
CT5 is a well-defined difference operator on the pointwise twisted
bundle; lattice translations are not identified with finite-base shifts.
This is the DD incoming object, not an assertion that
J commutes with the ordinary P action. The output uses the canonical
physical fused module and CT1--CT4. Its residue matrices come from its
actual representation, not from solving an equation for the fusion map.

For an actual finite fusion intertwiner C_(mu,nu), define


```math

 \mathcal F_{\mu,\nu}(q;z,\tau,t)
                  = C_{\mu,\nu}(q)J_{X,Y}(q),         \tag{CT6}

```


with the genuine carry line of CH18. For normalized degrees s(mu;h),s(nu;h),
where s(mu;h) is the unique integer in {0,...,p-1} congruent to -mu(c_h),
the exponent is

    n(mu,nu;h)=[s(mu;h)+s(nu;h)-s(mu+nu;h)]/p.

For arbitrary degrees k,l, the exact output degree is k+l. If that is
replaced by a chosen representative, include the corresponding integer
theta-line power. Zero-sum fusion uses its full canonical decomposition
instead of an inverse of B_0. In the local carry frame vartheta(z;tau)^n,
the displayed matrix is vartheta(z;tau)^(-n) C J. Its only extra
singularity is the indicated theta divisor. The invariant map CT6 is
line-valued and holomorphic; it is independent of t in the covering
frame, depends nontrivially on the finite dynamical parameter in general,
and has the stated z,tau dependence in a meromorphic carry frame.

**Theorem CT3 (complete operator equation).** After the stated finite
pullbacks and carry identifications,


```math

       \nabla_{\rm out}\mathcal F
                    =\mathcal F\nabla_{\rm in}^{J}.  \tag{CT7}

```


This is an equality of differential/difference operators on sections,
not just a fiberwise zero-order formula. It holds for every physical
central charge, degree, zero channel, and true-dual product.

**Proof.** For each marked group element, the actual equation is


```math

 \mathcal F(q)R_g^{J}(q)
              =R_g^{\rm out}(q)\mathcal F(g^{-1}q),  \tag{CT8}

```


where R is the coefficient of the base pullback in CT1 or CT5.
Insert CT5; J(q) cancels, and CT8 is exactly covariance of the actual
finite intertwiner C under the transported representation. For elements
of P it is ordinary P-intertwining. For A it is transport of the
canonical isotypic evaluation map (or of CH's explicit coordinate map).
Thus CT8 includes the shift of the coefficient F; replacing its right
side by R_out(q)F(q) would generally be incorrect. By linearity it
proves the full t-operator identity, including the augmented scalar terms.

For the elliptic operator, the source slope is (k+l)/p and the output
slopes, including the actual carry, have exactly the same sum. The
constant maps C,J intertwine the appropriate holonomies and are unitary.
The independently specified Chern forms therefore agree. In the
vartheta^n frame the output includes n dlog(vartheta), which cancels
d(vartheta^(-n)). The same argument uses both dz and dtau in CT4.
No inverse of a physical charge matrix, division by k, or restriction
on a partial charge sum was used. QED.

Nontriviality in the finite dynamical variable is not supplied by a
scalar carry frame. Already in the DD p=3, W=F3^2 control, J is the
parameter-dependent controlled translation DD15. Its conjugation changes
the simultaneous first-axis generator for suitable nonzero charges.
Taking w nonzero in CT3 therefore gives genuinely q-dependent
non-scalar position symbols. The exact certificate checks this statement.
The graph/pure-torus pair alone commutes with J by covariance; we do not
misdescribe that subcase as a new interaction created by J.

## CT4. Analytic sewing, shifted coherence, and actual dual evaluation

The incoming iterated tensor uses DD's rule

    (F bar_tensor G)(lambda)|_(X tensor Y[nu])
                       = F(lambda-nu) tensor G(lambda).

For a triple its total tensorator is


```math

 J_{X\otimes Y,Z}(\lambda)
       [J_{X,Y}(\lambda-\operatorname{wt}Z)\otimes I]
 =J_{X,Y\otimes Z}(\lambda)[I\otimes J_{Y,Z}(\lambda)]. \tag{CT9}

```


DD proves CT9 by composing actual expectation-normalized intertwiners,
not by defining an associator to make it true. Coassociativity of the
group-like coproduct supplies the same collective operator on three or
four physical factors, with one simultaneous base pullback. The
compatibility a(lambda-mu)=a lambda-a mu makes CT9 covariant under every
base shift. The carry exponents telescope exactly, including negative
degrees. Applying the actual finite multiplicity evaluation maps gives
the charged reassociation maps, including all product zero summands.

For a path gamma in the punctured t-plane let P_X(gamma) be the
parallel propagator of CT3 on the finite direct sum of parameter fibers.
**Theorem CT4 (analytic coherence).** These propagators exist, are
invertible, depend holomorphically on the couplings, and obey


```math

 \mathcal F\,P_{\rm in}^{J}(\gamma)
                  =P_{\rm out}(\gamma)\,\mathcal F.  \tag{CT10}

```


All charged reassociation routes, with their actual shifts,
multiplicities and carries, give the same analytic map. The pentagon
holds through zero intermediate charges and true duals.

**Proof.** Parametrize gamma on [0,1] and let B(s) be the pulled-back
coefficient. If R=int_0^1 ||B(s)|| ds, its ordered Picard series converges
in operator norm, with nth term bounded by R^n/n!, uniformly on compact
coupling sets. Thus ||P||<=exp(R), and the reversed-path solution is its
inverse. The tail after order m is at most
exp(R)R^(m+1)/(m+1)!. These facts prove convergence and permit termwise
application of the bounded finite maps. CT8 intertwines each ordered
product of coefficients, proving CT10 directly, or by uniqueness of the
linear ODE. CT9, coassociativity, and telescoping carries now identify
each coefficient along the two pentagon paths; convergence identifies
their analytic sums. This is a statement about actual propagators, not
an added arbitrary choice of analytic reassociation matrices. QED.

No endpoint at a pole is used in SA's [1/4,3/4] estimates. Consequently
there is no cutoff, divergent trace, or regularization whose independence
has been assumed. The only infinite operation is the absolutely
operator-norm-convergent Picard series. Finite-sector traces are ordinary
complex traces; their coefficients need not be positive multiplicities.

For a physical true dual X* use its contragredient representation and
degree -k. In the untwisted collective product, ev and coev are horizontal:
each diagonal group element acts as the identity on the evaluated
physical fiber and fixes coevaluation. The remaining base pullback is
exactly that on the tensor unit's scalar q-sections, so its augmented
residue is intertwined as well. They are also parallel for the opposite
geometric slopes. In the dynamical tensor
category they are precisely

    ev^J(lambda)=ev J_(X*,X)(lambda),
    coev^J(lambda)=J_(X,X*)(lambda)^(-1) coev.

CT9 and its unit equations give both shifted triangle identities, and
CT7 gives their horizontality. The entire X* tensor X remains present.
The connection on the representation-theoretic dual is the **dual for
the collective monoidal rule**. It is not generally the ordinary
linear-connection dual of CT3; confusing those two would incorrectly
restore the primitive-current requirement. The underlying CH bundle is
the genuine geometric dual, and the actual evaluation maps just written
satisfy the specified operator equation.

## CT5. A modular law compatible with position transport and fusion

The following is an explicit modulus-direction check. It does not infer
modularity from a formal heat equation. P has exponent p and the DD
auxiliary holonomy matrices also have pth power I. Work with the
subgroup Gamma(2p) of SL2(Z). It preserves the full p-torsion marking
and the theta characteristic; taking this subgroup is an intrinsic
marked-level restriction, not deleting physical module morphisms.

For gamma=((a,b),(c,d)) set D=c tau+d,

    tau'=(a tau+b)/D,       z'=z/D,
    M_(gamma,kappa)(z,tau)=exp(pi i kappa c z^2/D).

**Theorem CT5.** Multiplication by M_(gamma,kappa), with this pullback,
is a unitary holomorphic isomorphism of the actual slope-kappa bundles.
It preserves the full Chern connection, commutes with CT3 on the finite
parameter cover, obeys the modular group law, and intertwines all CT6
fusion maps with their actual carry factors.

**Proof.** More generally, transforming a pair of automorphy matrices
U,V with UV=exp(-2pi i kappa)VU gives


```math

 U'=e^{\pi i\kappa cd}U^dV^c,
 \qquad V'=e^{\pi i\kappa ab}U^bV^a.                 \tag{CT11}

```


Indeed a unit shift in z' is a shift by d+c tau in z. Multiplying its
old automorphy factor by M(z+D)/M(z) leaves exp(pi i kappa cd)U^dV^c.
The tau' shift is b+a tau; the same calculation leaves
exp(-pi i kappa tau'-2pi i kappa z') times the second CT11 matrix.
For gamma in Gamma(2p), b,c are multiples of 2p and a,d are 1 modulo
2p. Since kappa=k/p and U^p=V^p=I, both phases are 1 and U'=U,V'=V.
This proves the bundle map without an unspecified change of holonomy.

Write y=Im z, v=Im tau. Direct real algebra gives

    (Im z')^2/Im tau' = y^2/v - Im(c z^2/D).

Hence h_kappa(z',tau') |M_(gamma,kappa)|^2=h_kappa(z,tau).
A holomorphic isometry preserves the Chern connection; alternatively
differentiate this identity to obtain its gauge equation in dz,dtau.
The quadratic exponents compose exactly under matrix multiplication,
which proves the group law without choosing a square root. No claim
about a metaplectic action on a theta-section basis is needed.

All finite difference operators preserve kappa, so their matrices and
base pullbacks commute with this scalar gauge. This proves compatibility
with position transport. Finally M_(gamma,kappa+lambda)=
M_(gamma,kappa)M_(gamma,lambda). The exact slope/carry equality in CT3
therefore proves modular covariance of every fusion and dual map.
In a vartheta carry frame the theta section's own scalar transformation
must also be included; it is not silently set to 1. The invariant
line-valued assertion is independent of that frame. QED.

CT11 also describes the first step toward a larger modular action, but
no full SL2(Z) descent with all transformed characteristic conventions
is claimed here. The subgroup theorem covers the marked bundles used
in this construction and includes nonconstant tau transport.

## CT6. Fixed markings, analytic consequences, and comparison class

Allowed isomorphisms transport the actual marked group/folder data,
ordered axes, cocycle, retained pure split element, completion and
holonomy pair together. They transport every symbol in CT1--CT11,
including the reference boundary and charge projectors. Finite
intertwiner naturality is retained. A change of bundle frame is also
allowed if it transforms connections, fusion maps **and boundary data**
by the same rule. An independent reset of the boundary reference is a
change of the observable, not an allowed invariance argument.

For f'=f+(1-T)z, graph transports are conjugate by the old scalar
charge gauge D_z. Keeping only those graph operators therefore still
erases the shift. Keeping the pure split element at the boundary is
different: D_z generally does not preserve that mark. SA proves a
quantitative converse using a genuinely coupled response, recovering
all psi(mu(f(a))) and hence f(a). Its controls compare the same b,
the same charge modules/fusion dimensions, and conjugate individual
graph spectra, but a different response relative to the fixed split
reference. All gauges and reindexings in that statement are marked.

To compare the finite-family transport with SA's displayed physical
matrix ODE, use its marked boundary embedding at a fixed point of the
elliptic covering frame. For a genuine K-module X the normalized embedding

    E:X -> direct_sum_q X,       (Ev)(q)=v/sqrt(|Q|)

has T_g E=E rho_X(g). Consequently E* P_family E is exactly the
physical propagator of SA. Include all central charges at each q, with
their normalized degree representatives; every fiber has underlying
space X. One may take z=0, where all the Chern metrics have value 1,
so E is an isometry. On the J-twisted tensor source, the boundary realizing
the same ordinary physical tensor ODE is E_in=J^(-1)E, with readout E*J;
then T_g^J E_in=E_in(rho_X(g) tensor rho_Y(g)). Through F=CJ it becomes
F E_in=C E, with its readout transported by F^(-1). More generally
CT10 compares any boundary and readout transported by F and F^(-1);
these are not generally the q-constant boundary and readout of the output
decomposition. This is an explicit marked boundary source on the
cover, not an assertion that q-constant sections descend as global
elliptic sections. A change of covering frame transports E and E*
as boundary data. CT10 therefore supplies the precise fusion/transport
bridge for the analytic responses used here.

The optional first-axis residue is useful here: equation (CT5) makes the finite
dynamical symbol nonconstant, while a norm estimate shows that a small
nonzero coefficient preserves the phase-recovery accuracy. This does
not pretend that the graph/pure-torus subproblem by itself creates
a new dynamical twist.

The second analytic consequence in SA is an ordered-transport bound
for associative and two proper cubic Bol controls. Their individual
translation spectra agree, and the proper pair has equal labeled
associator defects and conjugate multiplication groups. A retained
inversion/translation pair nevertheless produces a rigorously positive
noncoincident transport defect in one proper control and exactly zero
in the other and in the associative control. This is a separate exact
control of the universal collective ODE mechanism on their regular
permutation modules. No identification of their entire inversion-extended
multiplication group with CT1's particular K, or instantiation of all
DD/theta channels for those modules, is inferred from that calculation.
It detects the stated marked compatibility; it does not characterize
nonassociativity.

These are constraints beyond individual seed spectra, separate
partition functions, fusion dimensions, or the unmarked graph packet.
They are **not** extra information beyond the complete marked finite
matrices: those matrices determine the analytic ODE. In particular,
the mixed low-order coefficient is a finite joint tensor. What is added
is its controlled noncoincident analytic realization, a dimension-free
remainder/stability estimate, and a specified comparison class that the
earlier separate invariants cannot distinguish. Generic Gaussian/Wick
identities do not impose the needed matrix commutation or fix the
reference cocycle; neither does the standard Felder flatness theorem.

The separate [coupled theta-boundary reconstruction](bol-heat-sewing-repair.md)
offers a complementary marked analytic observable. Its true-dual kernel
has full matrix probes and contour stability, but is not being identified
with CT's Fuchsian propagator or promoted to a unified theta-heat fusion
functor. The comparison is useful precisely because the outstanding
bridges remain visible.

## CT7. Applications, finite bridge, and remaining obligations

The construction enables well-defined charged transport diagrams with
fixed boundaries, quantitative recovery of a central cocycle from
separated observations, and a controlled test of inversion compatibility
in proper Bol examples. In the pinned rigid pair, recovering f(a)
determines the existing norm label

    z_f=(1+T(a))^2 f(a).

Thus it recovers z_f=1+epsilon^2 versus z_f=1 and hence the old marked
norm/Fourier test under its inherited strict-isomorphism hypotheses.
This is a **finite reconstruction bridge**: insert the recovered label
in the already proved CF/FS formulas. It is not an equality between
the new t-dependent response and a Fock trace, nor a new modular
classification theorem. The original huge-loop construction, properness,
and strict-isomorphism inputs retain their own source/review qualifiers.

The achieved object has a finite dynamical base, a collective tensor
rule, and a Chern modulus connection on Gamma(2p). The following remain
open: fusion for the original continuous-q Felder system; an interacting
heat connection compatible with position transport and all signed/zero
channels; an identification of the new observables with the old Fock
traces; and a new arithmetic moonshine consequence. An unmarked
classification theorem, Monster action or genus-zero assertion is not
part of this result.

The executable [collective transport checks](../code/verify_bol_collective_transport.py)
tests the finite-difference, nontrivial-twist, carry/dual and modular
polynomial identities. SA supplies independent exact loop controls and
the analytic bounds are proved, not inferred from truncation.
