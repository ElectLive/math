# Local analytic rigidity of the finite dynamical fusion architecture

**Mira Cult**



This note tests a concrete proposed analytic promotion of the finite
dynamical twist in [DD](bol-dynamical-fusion-construction.md). It proves
local rigidity under the full finite dynamical gauge group, then classifies
connections preserving the minimal linking algebra, its sector idempotents
and the fixed group action. Neither hypothesis is automatic for the
function-space dynamical system in [CE4](bol-charged-exchange.md#ce4-a-real-dynamical-repair-on-every-forced-matrix-block).
The result does not rule out Bol moonshine, global monodromy, fixed markings
outside this gauge category, nonlocal transforms or additional graded states.

The ingredients are finite semisimple algebra and the established dynamical
twist architecture of Etingof--Nikshych. No historical-priority claim is made
for semisimple deformation rigidity. The application identifies exactly what
an analytic family of these finite fusion maps can and cannot supply.

## AR1. A finite linking algebra for the shifted pentagon

Let G be a finite group, A an abelian subgroup, and Lambda=A* its complex
character group, written additively. A normalized dynamical twist is an
invertible zero-weight family J(lambda) in C[G] tensor C[G] satisfying


```math

 (\Delta\otimes1)J(\lambda)
       \bigl(J(\lambda-h^{(3)})\otimes1\bigr)
 = (1\otimes\Delta)J(\lambda)\bigl(1\otimes J(\lambda)\bigr),
 \qquad (\epsilon\otimes1)J=(1\otimes\epsilon)J=1.
 \tag{AR1}

```


The shift is evaluated on the A-weight of the third tensor factor. Let


```math

 F_\mu[G]=\{f:G\longrightarrow\mathbb C:
               f(ga)=\mu(a)f(g)\}.

```


For each ordered pair alpha,beta take a separately labeled copy
D_(alpha,beta)=F_(beta-alpha)[G], and define D_J as the direct sum of all
these copies. Noncomposable blocks multiply to zero. On composable blocks,
put


```math

 (f_{\alpha\beta}\star g_{\beta\gamma})(h)
       =(f\otimes g)((h\otimes h)J(\gamma)).
 \tag{AR2}

```


Functions are extended linearly to group-algebra arguments. The constant
function 1 in D_(alpha,alpha) is denoted e_alpha. The fixed left G-action
is (r.f)(h)=f(r^{-1}h); it preserves every block.

**Proposition AR1.** D_J is a finite-dimensional unital semisimple G-algebra
with fixed orthogonal idempotents e_alpha. The products by e_alpha are the
fixed block projections. Its dimension is |A||G|. If every diagonal corner
B_alpha=D_(alpha,alpha) is a full matrix algebra Mat_N, then


```math

                  D_J\cong\operatorname{Mat}_{|A|N}(\mathbb C).
 \tag{AR3}

```


**Proof.** In a composable triple the third function has right A-weight
delta-gamma. Applying AR1 at delta gives associativity, because the shifted
argument is delta-(delta-gamma)=gamma. Zero weight gives the required
right A-weight of each product; the counit gives the idempotents and units.
Left G-equivariance follows directly from AR2. There are |A|^2 blocks,
each of dimension |G|/|A|.

For semisimplicity we use precisely Etingof--Nikshych, arXiv:math/0101046v2,
Proposition 3.3 and Proposition 3.8. They prove that each B_alpha is
semisimple and that multiplication of the off-diagonal blocks gives
isomorphisms of the corresponding tensor products of bimodules. Their
formula (12) is the diagonal case of AR2; in Proposition 3.8 take
lambda=beta, mu=beta-alpha, nu=gamma-beta.

Fix e=e_beta. Surjectivity of those block products implies D_J e D_J=D_J,
so e is a full idempotent. For completeness, the standard corner argument
is elementary here. Choose x_i in D_J e and y_i in e D_J with
sum_i x_i y_i=1. Left multiplication identifies D_J with
End_(e D_J e)(D_J e): injectivity follows from fullness, and a right-module
endomorphism T is left multiplication by sum_i T(x_i)y_i. Since the corner
is semisimple, its finite module D_J e is semisimple, and that endomorphism
algebra is semisimple. If the corner is Mat_N, each of the |A| summands of
D_J e is its regular right module, by Etingof--Nikshych Corollary 3.7.
The endomorphism algebra is then Mat_(|A|N). QED.

This linking algebra includes the zero-weight blocks and their full matrix
corners. It does not replace them by one scalar channel.

## AR2. Every holomorphic finite twist family is locally dynamical gauge

The parameter below can include positions, auxiliary complex parameters
and a torus modulus, on an open set avoiding their poles. Its dimension is
arbitrary and finite. No modular identity is assumed.

**Theorem AR2.** Let J_s(lambda) be a holomorphic family of normalized
dynamical twists for fixed finite (G,A), on a complex manifold B. For any
s_0 in B there is a neighborhood U and a holomorphic zero-weight family
t_s(lambda) in C[G]^times, with t_(s_0)(lambda)=1 and epsilon(t_s)=1, such that


```math

 J_s(\lambda)
 =\Delta(t_s(\lambda))J_{s_0}(\lambda)
    \bigl(t_s(\lambda-h^{(2)})^{-1}\otimes t_s(\lambda)^{-1}\bigr).
 \tag{AR4}

```


Thus J_s is locally gauge-equivalent to its value at s_0 in the established
finite dynamical gauge sense. The same assertion holds on the regular locus
of a meromorphic family; no removal of its singularities is claimed.

**Proof of equivariant relative algebra trivialization.** Use the same
underlying vector space D for all linking algebras, and write mu_s for
their products. Every mu_s is associative and semisimple by AR1; its unit,
the idempotents e_alpha, the left and right block projections and the
G-action are independent of s.

Work on a small coordinate neighborhood with s_0=0. For a fixed small s,
put mu_t=mu_(ts), 0<=t<=1, and c_t=partial_t mu_t. Differentiating
associativity gives the Hochschild cocycle identity


```math

 a c_t(b,c)-c_t(ab,c)+c_t(a,bc)-c_t(a,b)c=0.
 \tag{AR5}

```


All products in this formula are mu_t. Differentiating the fixed unit and
block projections gives c_t(a,1)=c_t(1,a)=0 and
c_t(a,e_alpha)=c_t(e_alpha,a)=0.

The regular trace form B_t(a,b)=Tr(L_(ab)) is nondegenerate on a semisimple
algebra. Choose a fixed vector-space basis x_i, and its B_t-dual basis y_i.
The tensor sum_i x_i tensor y_i depends holomorphically on (s,t) and has


```math

 \sum_i x_i y_i=1,\qquad
 \sum_i a x_i\otimes y_i=\sum_i x_i\otimes y_i a.
 \tag{AR6}

```


One verifies these identities in each matrix summand: for Mat_n, the trace
form is n Tr(ab), and the dual of E_ij is E_ji/n. They are therefore
basis-independent. The tensor is G-invariant because regular trace is
invariant under algebra automorphisms.

Define the explicit linear operator


```math

                   D_t(a)=\sum_i x_i c_t(y_i,a).
 \tag{AR7}

```


Using AR5 and AR6 gives


```math

 c_t(a,b)=aD_t(b)-D_t(ab)+D_t(a)b.
 \tag{AR8}

```


For clarity, centrality in AR6 changes the first term on the right to
sum_i x_i c_t(y_i a,b); AR5 then makes the full expression
sum_i x_i y_i c_t(a,b)=c_t(a,b). Also D_t(e_alpha)=0, and D_t is
G-equivariant. Solve the finite linear ODE


```math

                  \partial_t g_t=-D_t g_t,\qquad g_0=I.
 \tag{AR9}

```


The solution is invertible, holomorphic in s, fixes every e_alpha, and
commutes with G. Differentiating
mu_t(g_t a,g_t b)-g_t mu_0(a,b), using AR8, shows that it satisfies the
homogeneous equation with coefficient -D_t and zero initial value. It
therefore vanishes. At t=1 we obtain a holomorphic G-equivariant algebra
isomorphism Phi_s:D_(J_0)->D_(J_s) fixing all e_alpha. Holomorphic parameter
dependence follows from the convergent finite-dimensional linear ODE
series on a sufficiently small neighborhood; no integration around a
parameter loop is required for this local construction.

**Recovery of a dynamical gauge.** Phi_s preserves every labeled block
because it preserves the e_alpha. A G-equivariant endomorphism of
F_mu[G] is right convolution by an element of e_mu C[G] e_mu, where
e_mu is the character idempotent in C[A]. For each fixed right endpoint
beta, collect those elements over all mu=beta-alpha. Their sum is an
invertible element t_s(beta) commuting with A. Consequently


```math

            (\Phi_s f_{\alpha\beta})(h)=f(h t_s(\beta)).
 \tag{AR10}

```


Fixing e_beta gives epsilon(t_s(beta))=1. Multiplicativity of Phi_s and
AR2 imply, on each pair of right-weight spaces,


```math

 \Delta(t_s(\gamma))J_0(\gamma)
 =J_s(\gamma)\bigl(t_s(\gamma-h^{(2)})\otimes t_s(\gamma)\bigr).

```


Those weight spaces exhaust the dual of C[G] tensor C[G], so this is an
identity in that algebra. Rearrangement is AR4. QED.

In particular, merely allowing the coefficients of a finite dynamical
twist to vary holomorphically in z,q,tau cannot supply local analytic
moduli after quotienting by the full gauge group. This does not say that
all coordinate expressions or all globally defined objects are constant.

## AR3. Compatible connections on the minimal finite sector system

For the completed class-two construction DD, the linking algebra is


```math

 D\cong\operatorname{End}(V),\qquad
 V=\bigoplus_{\lambda\in\Lambda}V_\lambda,
 \tag{AR11}

```


where the V_lambda are irreducible projective G-modules with one common
multiplier and are pairwise inequivalent with that fixed multiplier.
Their central characters already distinguish them in DD. The action on D
is conjugation, which is a genuine G-action. Its sector idempotents project
onto the summands V_lambda.

Consider a holomorphic connection nabla=d+K on the constant vector bundle
with fiber D, required to satisfy all three conditions:

1. The multiplication is parallel: nabla(ab)=(nabla a)b+a(nabla b).
2. Every e_lambda is parallel.
3. The fixed G-action is parallel, so nabla commutes with it.

These are substantive hypotheses on the entire finite linking algebra.
They do not follow solely from the existence of a matrix solution of
dF+A_out F-F A_in=0 between two selected bundles.

**Theorem AR3.** Under these hypotheses there are scalar one-forms
omega_lambda, unique up to adding one common one-form, such that on
D_(alpha,beta)=Hom(V_beta,V_alpha),


```math

             \nabla_{\alpha\beta}
                =d+(\omega_\alpha-\omega_\beta)I.
 \tag{AR12}

```


The connection is flat exactly when
d omega_alpha-d omega_beta=0 for every pair. On a sufficiently small
simply connected neighborhood a flat such connection is removed by a
block-scalar gauge. Along every closed composable sector cycle, the scalar
connection forms telescope to zero.

**Proof.** For a tangent vector, condition 1 says that K is a derivation
of End(V). Every derivation is inner. Here is an explicit verification:
with matrix units E_ij, fix an index r and put
Omega=sum_i K(E_ir)E_ri. The derivation rule applied to E_kl E_ir gives
[Omega,E_kl]=K(E_kl), hence K=ad Omega.

Conjugation by the projective G-matrices is an honest action on End(V).
Condition 3 says that ad Omega commutes with this action. Averaging Omega
over that finite action leaves ad Omega unchanged and gives a G-invariant
lift. Schur's lemma for the pairwise inequivalent summands in AR11 makes
this lift sum_lambda omega_lambda e_lambda. This also gives condition 2
and yields AR12. The ambiguity is a common scalar form because the center
of End(V) is C I. Curvature on a block is d omega_alpha-d omega_beta;
the scalar wedge-square is zero. Flat differences are locally exact, and
their primitives give the asserted diagonal gauge. The closed-cycle
statement is the literal telescoping sum of the differences. QED.

Combining AR2 with AR3 applies the same conclusion to a holomorphically
varying minimal twist family whose connection preserves its varying
product, fixed idempotents and fixed G-action: first trivialize the
algebra family by AR2, then apply AR3. The two kinds of gauge must not be
confused with a claim that a nontrivial finite twist is gauge-equivalent
to the identity twist; DD's minimal twist is not.

## AR4. Markings, global geometry and the remaining analytic target

The statements above permit the full finite dynamical gauge group. A
holomorphic invariant of the linking algebra, its multiplication, sector
idempotents and fixed left G-operators is locally constant under AR2.
For AR3's flat connections, closed-cycle transport constructed from these
parallel operations has only the finite product data; it has no surviving
scalar connection difference around the cycle.

There are several genuine boundaries:

- A gauge that must additionally preserve specified operators which are
  not part of the fixed G-action can be smaller than the gauge group in
  AR2. Their relative position may vary and is not classified here.
- AR2 is local on the regular parameter locus. It does not trivialize
  global descent, monodromy, a theta line of nonzero degree, or a pole.
- Scalar carry-line connections in local frames are additional data;
  global carry/divisor information from CH is not erased by this local
  algebra theorem. No identification with a conformal grading is made.
- Multiple copies of the same irreducible auxiliary module enlarge its
  commutant. Arbitrary additional graded multiplicities and infinite
  function-space fibers do not satisfy AR11's multiplicity-free hypothesis.
- CE's differential operators act on functions of dynamical variables
  and need not make the entire finite linking multiplication or fixed
  G-action parallel. AR3 does not assert that they do.

Thus the new finite shifted pentagon is a concrete advance, but making its
coefficients meromorphic is not itself the missing genus-one interaction.
A successful further construction must supply and justify analytic data
outside this rigid finite architecture, while retaining the required
cocycle markings. The theorem does not imply that the prescribed rigid
isotopes have equal invariants in every marked or graded theory.

## Primary source and exact scope

P. Etingof and D. Nikshych, *Dynamical twists in group algebras*,
arXiv:math/0101046v2, 29 January 2001; International Mathematics Research
Notices 2001(13), 679--701, DOI 10.1155/S1073792801000356.
[Versioned primary PDF](https://arxiv.org/pdf/math/0101046v2).
Definitions 2.3 and 2.5 fix AR1 and the gauge convention; formula (12),
Propositions 3.3 and 3.8 and Corollary 3.7 supply the finite algebra and
bimodule input in AR1. The local analytic trivialization and the complete
connection classification are proved above, rather than inferred merely
from finiteness of the gauge-equivalence classes in Theorem 6.6.

All new assertions here are analytic or algebraic proofs. No finite
numerical experiment is used as a proof of local holomorphic rigidity.
