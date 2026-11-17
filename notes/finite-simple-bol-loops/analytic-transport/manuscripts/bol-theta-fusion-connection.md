# Theta heat transport, retained relative coordinates, and the true dual channel

**Mira Cult**



This is a separate geometric test of the charged compatibility problem.
It uses the actual bundles of [CH4](bol-charged-heisenberg-obstruction.md#ch4-a-geometric-integer-extension-and-coherent-carry-lines).
It does not construct a fusion map for the Felder position system in
[CE4--CE6](bol-charged-exchange.md), and it introduces no dynamical Cartan
variables. The positive construction retains a relative elliptic coordinate;
deleting that coordinate obstructs every finite-order differential heat
intertwiner in the stated local architecture. Retaining the full mixed
quadratic form extends coordinate transport through zero total degrees.
An explicit mixed Kronecker section and a separate cohomological calculation
both recover the entire true-dual zero algebra. These are not asserted to
give dimension-reducing signed-degree sewing or the requested Felder functor.

The analytic mechanism here is classical theta heat transport and Serre
duality. No Bol-specific analytic rigidity or historical priority is claimed.
In particular the graph-only cocycle erasure in CH5 persists in this route.

## TH1. The actual charged bundle carries a heat operator

Throughout, p is an odd prime, as in CH1. Write the integer degree label
as k and its slope as kappa=k/p. Let M have
constant holonomy matrices U,V satisfying


```math

 UV=e^{-2\pi i\kappa}VU.

```


The covering functions for the CH4 bundle satisfy


```math

 s(z+1,\tau)=Us(z,\tau),\qquad
 s(z+\tau,\tau)
   =e^{-\pi i\kappa\tau-2\pi i\kappa z}Vs(z,\tau).
                                                        \tag{TH1.1}

```


For kappa nonzero define


```math

 H_\kappa=\partial_\tau-
                   \frac{1}{4\pi i\kappa}\partial_z^2.    \tag{TH1.2}

```


The parameter space is the upper half-plane in tau; functions are
holomorphic on the covering z-plane and in tau. Locally meromorphic
versions are allowed away from their divisors. The matrices U,V are held
fixed in this trivialization.

**Proposition TH1.** H_kappa preserves (TH1.1). It therefore defines the
usual theta heat connection on the family of holomorphic section spaces,
whenever these spaces form a vector bundle. Constant maps intertwining
U,V and having the same slope commute with this connection.

**Proof.** The unit-period equation is immediate. Put
J=exp(-pi i kappa tau-2 pi i kappa z)V. Differentiating the second equation
at fixed z gives


```math

 (\partial_\tau s)(z+\tau)
 =J\bigl(\partial_\tau s-\partial_zs+\pi i\kappa s\bigr),

```


where the derivative of the translated argument has been included.
Two z-derivatives give


```math

 (\partial_z^2s)(z+\tau)
 =J(\partial_z-2\pi i\kappa)^2s.

```


Substitution cancels both the first derivative and scalar terms, proving
(H_kappa s)(z+tau)=J(H_kappa s)(z). Constant intertwiners commute with the
scalar differential operator. QED.

Here is a completely explicit rank-p holonomy model. For k>0 let
U_k e_j=exp(-2 pi i k j/p)e_j and V e_j=e_(j+1), j modulo p. The associated
rank-p bundle will be denoted B_k. For a=0,...,k-1 define its vector theta
sections componentwise by


```math

 \Theta^{k,p}_{a,j}(z,\tau)=
 \sum_{n\in\mathbb Z}
 \exp\left(
 \frac{\pi i p}{k}(a+kn-kj/p)^2\tau
       +2\pi i(a+kn-kj/p)z\right).                     \tag{TH1.3}

```


These series converge normally on compact subsets of C times the upper
half-plane. They satisfy (TH1.1) with slope k/p and are H_(k/p)-horizontal.
They are a basis of H^0(B_k), so its dimension is k.

To check these claims, the positive quadratic term gives normal
convergence and termwise differentiation. Translation by 1 gives U_k.
Completing the square after translation by tau changes j to j-1; the wrap
at j=0 is absorbed by n->n+1. Every summand satisfies (TH1.2).
Conversely, the first component of any section has a Fourier expansion
sum_m a_m exp(2 pi i m z). The second automorphy relation, iterated through
all p components, relates a_(m+k) to a_m. There are exactly k free residue
classes modulo k, and their resulting series are (TH1.3). Their first
components have disjoint Fourier supports, proving independence.

For k<0 the same recurrence forces superexponential growth of nonzero
Fourier coefficients in both directions, impossible for a holomorphic
periodic function on horizontal strips. Thus H^0(B_k)=0 for k<0.
This is a direct Fourier argument; no classification of vector bundles
on elliptic curves is needed.

## TH2. Deleting the relative coordinate forbids finite-order heat fusion

Let kappa,lambda,kappa+lambda be nonzero complex constants. The next
statement is local on the z,tau cover and concerns all local holomorphic
solutions, not only finite-dimensional global theta section spaces.
Input and output vector spaces are finite-dimensional and their heat
operators act componentwise.

Consider a bilinear differential expression of finite spatial order


```math

 B(f,g)=\sum_{i+j\le r}b_{ij}(z,\tau)
                 \bigl((\partial_z^if)\otimes(\partial_z^jg)\bigr),
                                                        \tag{TH2.1}

```


where each b_ij is a meromorphic linear map from the tensor of the input
spaces to the output space. Its coefficients may contain any fixed
finite charged intertwiner and may depend on all auxiliary parameters,
held fixed by the heat operators. Both inputs are evaluated at the same
z. There is no retained relative coordinate or additional heat channel.

**Theorem TH2.** If H_(kappa+lambda)B(f,g)=0 for every pair of local
solutions H_kappa f=H_lambda g=0, then B=0 as a bilinear differential
operator. In particular a nonzero parameter-dependent multiplication
matrix cannot repair pointwise heat fusion.

**Proof.** Put a_kappa=(4 pi i kappa)^(-1), and use the input heat
equations to eliminate tau derivatives. At any regular coefficient
point, the part of total spatial order r+2 is the product of the
matrix-valued highest symbol of B with the scalar polynomial


```math

 Q(\xi,\eta)=a_\kappa\xi^2+a_\lambda\eta^2
                           -a_{\kappa+\lambda}(\xi+\eta)^2.
                                                        \tag{TH2.2}

```


This polynomial is nonzero: its mixed coefficient is
-2 a_(kappa+lambda). Arbitrary finite spatial jets of the two inputs can
be prescribed at a point. For example, choose polynomial initial data
there and apply the finite heat series; it gives an entire local solution.
The assumed identity therefore implies Q sigma_r(B)=0 as a polynomial
with matrix coefficients. The scalar polynomial ring is an integral
domain, so every matrix entry of sigma_r(B) is zero. Descending in r
proves that every coefficient vanishes. Meromorphic continuation gives
the assertion throughout the coefficient domain. QED.

For the uncorrected pointwise product m(f,g)=f tensor g, the exact defect is


```math

 H_{\kappa+\lambda}m(f,g)
 =\left.
 \frac{(\lambda\partial_x-\kappa\partial_y)^2}
      {4\pi i\kappa\lambda(\kappa+\lambda)}
                  (f(x)\otimes g(y))\right|_{x=y=z},    \tag{TH2.3}

```


when the inputs are horizontal. The proof is direct differentiation.
Equation (TH2.3) identifies the missing relative heat operator.

For an actual p=3, k=l=1 theta control, the j=0 component is
sum_n q^(3n^2/2)w^n, with q=exp(2 pi i tau), w=exp(2 pi i z).
Its square has coefficient 2 at q^(3/2)w. The normalized output operator
H_(2/3)/(2 pi i) multiplies this monomial by
3/2-1/(2(2/3))=3/4. The resulting coefficient is exactly 3/2, not zero.
The two summands (n,m)=(0,1),(1,0) are the complete contribution at this
exponent, so this is not a truncation-based claim. A constant finite
Clebsch--Gordan change of component basis cannot remove a nonzero vector
defect.

The theorem does not rule out integral or infinite-order transforms,
extra relative variables, operations restricted only to global theta
sections, or an interacting connection different from (TH1.2).

## TH3. An explicit relative-coordinate heat repair on an isogeny cover

Now let k,l be positive integer labels, K=k+l, and put
kappa=k/p, lambda=l/p. Consider the product of the two actual bundles on
E_tau times E_tau, with coordinates x,y, and the operator


```math

 H_{\mathrm{in}}=\partial_\tau-
 \frac1{4\pi i}\left(\kappa^{-1}\partial_x^2
                              +\lambda^{-1}\partial_y^2\right).
                                                        \tag{TH3.1}

```


The integer matrix defines the isogeny


```math

 T_{k,l}:E_\tau^2\longrightarrow E_\tau^2,
             (u,v)\longmapsto(x,y)=(u+lv,u-kv).           \tag{TH3.2}

```


Its determinant is -K and its degree is K^2. The parameter base is
therefore an explicit cover, rather than an unidentified common q-space.
The product quadratic form becomes


```math

 \kappa x^2+\lambda y^2
       =\frac Kp u^2+\frac{klK}{p}v^2.                  \tag{TH3.3}

```


Independently define the output heat operator by these two slopes:


```math

 H_{\mathrm{out}}=\partial_\tau-
 \frac1{4\pi i}\left(\frac pK\partial_u^2
                              +\frac p{klK}\partial_v^2\right).
                                                        \tag{TH3.4}

```


**Theorem TH3.** Pullback along T_(k,l) intertwines (TH3.1) and (TH3.4).
Composing pullback with any fixed finite P-intertwiner C gives a horizontal
map on the corresponding vector-valued section spaces. It retains the
relative elliptic coordinate v and all finite multiplicity channels.

**Proof.** The chain rule, or inversion of the congruence (TH3.3), gives


```math

 T_{k,l}^*\left(\frac p{k}\partial_x^2
                         +\frac p{l}\partial_y^2\right)
   =\left(\frac pK\partial_u^2
                         +\frac p{klK}\partial_v^2\right)T_{k,l}^*.

```


The coordinate matrix is independent of tau. This proves the differential
identity, and C commutes with the scalar operators. To check the geometric
descent, the pulled-back unit-period holonomies are


```math

 U_u=U_M\otimes U_N,\qquad U_v=U_M^l\otimes U_N^{-k},

```


and the tau-period holonomies are


```math

 V_u=V_M\otimes V_N,\qquad V_v=V_M^l\otimes V_N^{-k}.

```


Their scalar automorphy factors have respectively slopes K/p and klK/p.
Indeed kx+ly=Ku and kl(x-y)=klKv. Cross commutators are trivial, since
kl-lk=0, so these four factors satisfy the product-torus consistency laws.
Conjugating the constant matrices by C gives their explicit matrices in
the fused finite basis. QED.

The target is the pulled-back bundle with these four specified factors.
The relative holonomies need not act only on the finite multiplicity
factor in C:M tensor N -> M_gamma tensor F. If the retained pair in P
is u_0,v_0, exact commutation with every diagonal P-operator holds if and
only if l ell-k mu vanishes on the span of [P,u_0] and [P,v_0] in Z.
Indeed these two relative operators acquire respectively the commutator
phases (l ell-k mu)([g,u_0]) and (l ell-k mu)([g,v_0]). The stronger
condition l ell=k mu as central functionals is sufficient, not necessary.
It holds in the relevant one-dimensional-center proportional case; it
is not automatic for the rigid three-dimensional center. In general the coupled relative
holonomies are retained on the whole fused space. Discarding them would
change the theorem.

Likewise, pullback of global sections is injective but generally not
surjective onto all sections of the pulled-back bundle. Its image has
the canonical descent data for the isogeny kernel. No equality of the
two global-section dimensions is asserted.

For more than two positive labels, iterate (TH3.2) along a binary fusion
tree. The result is an integer matrix of nonzero determinant from one
product torus to the original ordered product. Every target heat operator
is defined by the resulting quadratic form, and every tree retains all
n-1 relative coordinates. Between two trees, the rational matrix relating
their coordinates is defined on a common finite isogeny cover: clear its
denominators, and retain the induced descent data. Every sequence of
reassociations composes to the same rational coordinate transformation.
Together with the actual finite tensor associators, this proves the
pentagon on such common covers. This is coordinate-change coherence,
not a new Bol associator or a claim of a common finite theta basis after
forgetting the descent data.

The finite central charge may be zero while K is positive. Such channels
are included, and CH4's carry line keeps the correct degree. The true
dual label -k is not in this positive cone. At l=-k, the displayed
diagonalizing isogeny has determinant zero. The following construction
repairs that failure by retaining a mixed quadratic form.

### All signed nonzero input slopes and mixed zero-total channels

Let G be a nonsingular symmetric r by r rational matrix and consider
constant matrices U_i,V_i such that all U_i commute, all V_i commute,
and


```math

 U_iV_j=e^{-2\pi iG_{ij}}V_jU_i.

```


Use the factors


```math

 J_{e_i}=U_i,\qquad
 J_{\tau e_j}(z)=
       e^{-\pi iG_{jj}\tau-2\pi i(Gz)_j}V_j.           \tag{TH3.5}

```


They define the corresponding bundle on E_tau^r. Its heat operator is


```math

 H_G=\partial_\tau-
            \frac1{4\pi i}\partial_z^tG^{-1}\partial_z. \tag{TH3.6}

```


The verification that H_G respects (TH3.5) is the same direct calculation
as TH1: the gradient of log J_(tau e_j) is -2 pi i G e_j, so the
inverse G cancels the derivative of the shifted argument. No positivity
of G is used in this operator or bundle calculation. Indefinite G does
not imply a convergent positive-definite theta series or nonzero global
holomorphic sections.

For any integer matrix T with nonzero determinant, z=Tw is an isogeny
cover and


```math

 G_{\mathrm{out}}=T^tG_{\mathrm{in}}T,
 \qquad H_{G_{\mathrm{out}}}T^*=T^*H_{G_{\mathrm{in}}}. \tag{TH3.7}

```


These statements follow respectively from the factors and the chain
rule. Thus arbitrary signed, nonzero input slopes k_i/p are covered by
starting with G=diag(k_i/p) and retaining the whole transformed matrix.
At every binary node one may use x=u+v,y=u-v, rather than divide by a
possibly zero sum. Every resulting tree matrix is integral and invertible
over Q; reassociation is its rational coordinate change on a common
finite cover. Matrix congruences and the finite tensor associators compose
exactly, proving the same pentagon at this enlarged-coordinate level.
All original coordinates and descent data are retained. A zero partial
sum may make a diagonal entry of G_out vanish; it does not make G_out
singular.

For a true dual pair of slopes kappa,-kappa, x=u+v,y=u-v gives


```math

 G_{\mathrm{out}}=
 \begin{pmatrix}0&2\kappa\\2\kappa&0\end{pmatrix},
 \qquad
 H_{\mathrm{out}}=\partial_\tau-
                 \frac1{4\pi i\kappa}\partial_u\partial_v.
                                                        \tag{TH3.8}

```


The tau factors are exp(-4 pi i kappa v)V_u and
exp(-4 pi i kappa u)V_v. The pure u and pure v slopes are zero, but
their cross curvature and cross holonomy are not. Calling this one
trivial flat sector would erase the mixed data.

On any local horizontal section holomorphic near v=0, let
J_m(u,tau)=(partial_v^m s)(u,0,tau). Then


```math

 \partial_\tau J_m=
            \frac1{4\pi i\kappa}\partial_uJ_{m+1}
                         \qquad(m\ge0).                \tag{TH3.9}

```


No finite normal-jet truncation closes for all local solutions. For
any N, polynomial initial data s(u,v,tau_0)=u v^(N+1) have every
J_0,...,J_N identically zero as a function of u at tau_0, but
partial_tau J_N=(N+1)!/(4 pi i kappa) is nonzero there. The finite heat
series of that polynomial is an exact local solution. Thus there is no
induced homogeneous evolution operator determined only by those N+1
jets, even if their u derivatives are included. This concerns local
solution sheaves; special finite-dimensional subspaces can have extra
relations.

### A nonzero meromorphic true-dual section with every matrix residue

The mixed equation also admits an explicit genus-one solution, so this
signed construction is not only an empty global-holomorphic control.
Let k be positive and prime to p, put kappa=k/p and delta=2k/p, and use
the marked rank-p holonomy model U=U_k,V of TH1. Its parity operator
R e_j=e_(-j) satisfies URU=VRV=R and tr(R)=1. On End(C^p), put


```math

 W_{r,s}=V^{-r}U^s R U^{-s}V^r,
                  \qquad r,s\in\mathbb F_p.            \tag{TH3.10}

```


These are joint eigenvectors for the commuting sandwich maps
A->UAU and A->VAV, with eigenvalues exp(2 pi i r delta) and
exp(2 pi i s delta). They form a basis. Moreover


```math

 \sum_{r,s}W_{r,s}=pI.                                  \tag{TH3.11}

```


The eigenvalues follow directly from UV=exp(-2 pi i k/p)VU.
They are distinct because 2k is invertible modulo p. The sum is the
conjugation average of R, so it is p tr(R)I=pI; this also follows by
commuting the sum with U,V and taking traces.

Let phi be the Kronecker function of CE4, and set


```math

 K_{a,b}(u,v;\tau)=
 e^{2\pi iav}\phi(\delta u+a\tau-b,v;\tau),

```



```math

 S_A(u,v;\tau)=\frac1p
 \sum_{r,s\in\mathbb F_p}
 K_{r\delta,s\delta}(u,v;\tau)\,W_{r,s}\otimes A,
                 \qquad A\in\operatorname{End}(F).     \tag{TH3.12}

```


The kernel K is unchanged when a or b changes by an integer, so this
formula is independent of representatives r,s. Here the original
charged holonomy module is C^p tensor F. Its full diagonal zero algebra
is I tensor End(F), as in CH3.

**Proposition TH3a.** S_A is a meromorphic section of the actual
true-dual bundle pulled back by x=u+v,y=u-v. It obeys (TH3.8), depends
linearly and injectively on A, and


```math

                 \operatorname*{Res}_{v=0} S_A=I\otimes A.
                                                        \tag{TH3.13}

```


The domain is Im(tau)>0 away from the indicated polar divisors. Besides
v in the period lattice, the allowed center poles occur where
delta u+a tau-b is in that lattice for some a=r delta,b=s delta;
their union is 2ku in the period lattice. These additional center
divisors are part of the theorem and are not suppressed.

**Proof.** The elementary Kronecker laws give


```math

 \begin{aligned}
 K_{a,b}(u+1,v)&=K_{a,b-\delta}(u,v),\\
 K_{a,b}(u+\tau,v)&=e^{-2\pi i\delta v}K_{a+\delta,b}(u,v),\\
 K_{a,b}(u,v+1)&=e^{2\pi ia}K_{a,b}(u,v),\\
 K_{a,b}(u,v+\tau)&=e^{-2\pi i\delta u+2\pi ib}K_{a,b}(u,v).
 \end{aligned}                                          \tag{TH3.14}

```


Conjugation by U sends W_(r,s) to W_(r,s+1), and conjugation by V
sends it to W_(r-1,s). Together with their sandwich eigenvalues,
(TH3.14) is exactly the four factors of the pulled-back bundle.

The standard mixed heat identity is


```math

       2\pi i\partial_\tau\phi(z,v;\tau)
                          =\partial_z\partial_v\phi(z,v;\tau).
                                                        \tag{TH3.15}

```


For completeness, its difference is holomorphic in z: at z=0 the
residue of phi is the constant 1, killed by both relevant derivatives.
The mixed heat operator preserves the factors of the Poincare bundle,
by (TH3.5)--(TH3.6) with off-diagonal entries 1. Thus the difference
has multipliers 1 and exp(-2 pi i v) in z. For v outside the period
lattice, a holomorphic section with those multipliers is zero by its
Fourier expansion. Meromorphic continuation proves the identity.

Differentiating K, the derivative of a tau contributes a phi_z term,
which is exactly supplied by differentiating exp(2 pi i a v) in its
mixed spatial derivative. Equation (TH3.15) therefore gives
H_out K=0 and hence H_out S_A=0. Every K has residue 1 at v=0;
(TH3.11) gives (TH3.13), which also proves injectivity. The pole
description follows from the theta quotient defining phi. QED.

This is the classical shifted-Kronecker mechanism applied to an actual
charged true-dual bundle. It includes the full matrix residue but does
not add a new Yang--Baxter or Bol identity. In fact S_A=S_basic tensor A:
the matrix zero algebra is retained as a spectator in this analytic
kernel, not given a new interaction by the formula. The relative collision
expansion is not identified with the holomorphic normal-jet hierarchy
(TH3.9), and its residue is not identified with a Dolbeault cup product.
Those are different operations, even though their finite zero algebra
has the same marked origin.

## TH4. True-dual cohomological sewing recovers the full zero algebra

Fix a regular Heisenberg module of dimension p^d and a symplectic
holonomy pair with commutator phase exp(-2 pi i/p). The representation
of that marked pair decomposes as C^p tensor F, where dim F=p^(d-1).
One may define F as its intertwiner space from the displayed U_1,V
model, so no irreducible constituent of the entire P-module is being
silently chosen. Its degree-label-one bundle is


```math

 E=B_1\otimes F,
 \qquad E^*=B_1^*\otimes F^*.
                                                        \tag{TH4.1}

```


Choose the nonvanishing differential dz on the parameter cover, and let
epsilon_tau in H^1(O_(E_tau)) pair to one with dz under Serre duality.

**Theorem TH4.** There are canonical identifications relative to that
marked pair and the indicated model,


```math

 \begin{aligned}
 H^0(E)&\cong H^0(B_1)\otimes F,\\
 H^1(E^*)&\cong H^0(B_1)^*\otimes F^*,\\
 H^1(\operatorname{End}E)&\cong
                     \operatorname{End}(F)\otimes H^1(O).
 \end{aligned}                                          \tag{TH4.2}

```


Under these identifications the cup product is


```math

 (t\otimes v)\cup(\alpha\otimes\eta)
     =\frac{\alpha(t)}p\,(v\otimes\eta)\otimes\epsilon_\tau.
                                                        \tag{TH4.3}

```


Here End(F) is embedded in End(E) by I_(B_1) tensor End(F). Since
dim H^0(B_1)=1, this cup product is an isomorphism from the tensor of
the two displayed input cohomology spaces onto H^1(End E). In
particular it reaches every matrix zero mode, not only its scalar trace.

**Proof.** The first line follows from the constant F factor, and TH1
gives dim H^0(B_1)=1. Serre duality with dz gives the second line.
The adjoint holonomies on End(C^p) commute. Their p^2 Weyl eigenlines
have all p^2 different character pairs, of which only the identity line
is trivial. A nontrivial finite-unitary degree-zero line has no
holomorphic sections: its unit-modulus Fourier multiplier conditions
force its frequency to be zero and both multipliers to be one. Its
H^1 also vanishes by Serre duality. Therefore only the identity line
contributes to H^1(End B_1), giving the third line of (TH4.2).

The cup product followed by tr_(B_1) is exactly the Serre pairing.
On the surviving identity line tr_(B_1)(I)=p, which supplies the
factor 1/p in (TH4.3). Tensoring the F and F* factors gives v tensor eta.
This proves the formula and the isomorphism. QED.

More generally, with B_k for positive k prime to p, the same argument
gives H^0(B_k) of dimension k and the formula (TH4.3), now with its
perfect k-dimensional theta pairing. The map onto End(F) is surjective;
it is an isomorphism only when k=1. The unitary-flat End(B_k) calculation
uses primeness to p, since otherwise the holonomy commutant is larger.

The classical input is Serre's original compact-manifold duality theorem,
*Un theoreme de dualite*, Comment. Math. Helv. 29 (1955), 9--26,
doi:10.5169/seals-23275, Section 3 no.13 Theorem 4 (printed p.22), with
the cup-product interpretation in no.15 (printed p.23). The
[original scan](https://www.college-de-france.fr/media/jean-pierre-serre/UPL35645220559164287_Un_theoreme_de_dualite.pdf)
was inspected. This invokes a proved classical theorem, not a new
cohomological duality assertion for Bol loops.

## TH5. Horizontal dual sewing and the exact remaining boundary

On the tau-cover, equip H^0(B_k) with the heat connection of TH1. Equip
its Serre dual with the dual connection using dz; equip the constant F
factors and the line framed by epsilon_tau with their trivial
connections. These choices are explicit and are made before the cup
map is considered. The usual dual-connection identity


```math

 d(\alpha(t))=(\nabla^*\alpha)(t)+\alpha(\nabla t)

```


and (TH4.3) prove that the true-dual cup map is horizontal. Consequently
one neutral product channel has a complete finite-dimensional geometric
heat model retaining its entire matrix zero algebra.

This is a statement on the specified parameter cover. A modularly
coherent system on all charge sectors additionally requires the Hodge
line factors, choices of holonomy transport and metaplectic conventions.
No such global signed-degree sewing structure is asserted here.

Dolbeault cup products themselves are associative, with the usual
cohomological grading: tensor the (0,*) forms and apply the actual finite
bundle maps. This ensures the ordinary cup-product coherence at a fixed
curve. It does not make positive-positive cup multiplication horizontal
for the heat connections, as TH2 already proves in its local setting
and the explicit theta control demonstrates globally. TH3's retained
relative-coordinate map and TH4's true-dual cohomological map have not
been combined into a single connection-compatible pentagon.

There is a further precise limitation on a derived repair that leaves
the product on cohomology unchanged. A chain-homotopy correction to the
heat-compatibility equation induces zero correction on cohomology. In
the p=3, k=l=1 control above, the nonzero defect is a holomorphic section
of the positive-degree output bundle, hence a nonzero H^0 class. It
cannot be removed by a Dolbeault chain homotopy. An A-infinity or derived
construction must therefore change the induced connection/product,
retain an additional channel, or use another input object; merely adding
the word "derived" to the same cup multiplication does not solve its
horizontal compatibility equation.

If the positive cocycle changes by f -> f+(1-T)z, the scalar charge maps
of CH5 act on every bundle and its cohomology. Their inverse factors
cancel in (TH4.3), and the constant finite maps in TH3 transform by the
same conjugation. Thus graph-only closed constructions here still erase
those shifts. Fixed split-torus, outside-involution or boundary data
cannot be omitted from a future isotope-sensitive construction.

The useful conclusion is therefore specific. Ordinary heat transport
forces a relative channel and forbids finite-order diagonal repairs.
Retaining all coordinates and the full mixed form gives coherent
transport for arbitrary signed nonzero input slopes on identified
covers, including zero partial sums. It does not reduce the number of
coordinates or produce finite closure after diagonal restriction.
The true neutral channel has both a meromorphic mixed-heat realization
and a cohomological realization containing its full zero algebra. The
missing theorem is a compatible dimension-reducing, marked, dynamical
sewing, with a noncoincident constraint not generated by these standard
theta and Serre mechanisms.

## Reproduction

The [exact standard-library certificate](../code/verify_bol_theta_fusion.py)
checks rational heat symbols, positive and signed coordinate changes,
the mixed quadratic forms across a four-input reassociation pentagon,
the finite Weyl/parity identities underlying (TH3.10)--(TH3.13), the
normal-jet counterexamples and vector-theta exponent shifts. It also
computes the exact p=3 defect coefficient 3/2 above. Run with assertions
enabled from the repository root:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_theta_fusion.py
```

The output includes the executable's SHA-256 and the checked counts.
These are finite exact controls, not a proof of convergence, Serre duality,
the universal pentagon, or the stronger Bol-specific analytic target.

For the classical normalization background see the official
[DLMF Section 20.2](https://dlmf.nist.gov/20.2), Fourier series and
quasiperiodicity, and [Section 20.13](https://dlmf.nist.gov/20.13),
equation 20.13.1, after converting its pi-periodic spatial variable to
the unit-period convention used here. The heat and defect identities
above are derived directly, so their constants do not depend on an
unstated normalization conversion.
