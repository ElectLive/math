# Full fusion naturality leaves only the geometric degree current

**Mira Cult**



## Scope: which coherence equations are being imposed

Let P be a finite group and F its forgetful functor from finite-dimensional
complex P-modules to vector spaces. A natural current X assigns an operator
X_V to every module, commuting with every P-linear intertwiner. We do not
assume X_V itself is P-linear; allowing it to be an arbitrary operator makes
the result stronger. An *ordinary primitive tensor rule* means


```math

X_{V\otimes W}=X_V\otimes1+1\otimes X_W.              \tag{FN.1}

```


The same definitions make sense with coefficients in any characteristic-zero
field containing C, for example meromorphic functions of separated insertion
points, a torus modulus, and auxiliary parameters. No differential equation
is assumed in the following algebraic argument.

For a two-variable natural operator r_(V,W), the ordinary infinitesimal fusion
rules at a fixed common spectral parameter z are


```math

\begin{aligned}
r_{V\otimes W,X}(z)&=r_{V,X}^{13}(z)+r_{W,X}^{23}(z),\\
r_{V,W\otimes X}(z)&=r_{V,X}^{13}(z)+r_{V,W}^{12}(z).
\end{aligned}                                         \tag{FN.2}

```


These are equations for the unflipped operator; a corresponding exchange is
the flip followed by that operator. The hypotheses mean naturality for
**all** intertwiners and the ordinary, unshifted tensor product. In particular,
they do not describe a dynamical tensor product whose second factor sees a
shifted auxiliary variable. A spectral parameter shifted on one side of
(FN.2) is likewise outside the hypothesis.

## FN1. Finite group modules have no primitive natural current

**Lemma FN1.** A natural current for F satisfying (FN.1) is zero. Every
natural r satisfying either the first fusion equation in (FN.2), with
naturality in both variables, is zero.

**Proof.** Set A=C[P]. On its regular left module, define a=X_A(1). For
v in any V the map f_v:A -> V, b -> bv, is P-linear. Naturality gives
X_V(v)=f_v(a)=av. Thus every natural current is action by one a in A.
Applying the tensor rule on the regular modules says

    Delta(a)=a tensor 1 + 1 tensor a,

where Delta(g)=g tensor g. Write a=sum_g a_g g. For g != 1 the coefficient
of g tensor g forces a_g=0. The coefficient of 1 tensor 1 then forces
a_1=2a_1, so a=0.

For r, naturality similarly gives action by
r_(A,A)(1 tensor 1) in A tensor A. The first tensor rule makes every
coefficient in its second factor primitive in its first factor, so it
vanishes by the preceding calculation. QED.

This elementary fact is consistent with the usual finite-group tensor
category having discrete, rather than infinitesimal, symmetry. It does not
say that the actual marked Bol translations or the finite charge-changing
intertwiners vanish. They do not satisfy the natural primitive-current
hypothesis.

## The actual degree extension

Fix a central element c in P of exact prime order p and
zeta=exp(2 pi i/p). The central element in the charged bundle construction is
the commutator of the chosen marked Weyl holonomies. Define C(P,c) as follows.

An object is a finite-support integer-graded P-module

    V=direct_sum_(k in Z) V_k,       rho(c)|V_k=zeta^(-k) 1.

Morphisms are all degree-preserving P-intertwiners. Tensor products use
ordinary module tensors with additive integer degree; duals have opposite
degree and contragredient action. This is the full category of the degree
repair, with all central charge sectors retained. A nonhomogeneous object
is a finite direct sum of homogeneous ones. Write D_V=k·1 on V_k.

Every integer degree occurs. For example, inducing to P the character of
<c> which takes c to zeta^(-k) supplies a nonzero module in degree k.
The degree-zero subcategory is exactly Rep(P/<c>).

The integer k is a geometric bundle-degree label. It is **not** automatically
an oscillator energy, a conformal weight, or a ribbon twist. For the torus
bundle its slope is k/p; no vertex-algebra identification is assumed.

## FN2. The only primitive current is the degree

**Theorem FN2.** Every natural current of the forgetful functor on C(P,c)
satisfying (FN.1) has the form


```math

                    X_V=aD_V                              \tag{FN.3}

```


for one scalar a. This holds pointwise, and hence with meromorphic a, when
the coefficients depend meromorphically on external parameters.

**Proof.** On the degree-zero subcategory, FN1 applied to P/<c> gives
X=0. If V is nonzero and homogeneous of degree k, V tensor V* has degree
zero, so

    X_V tensor 1 + 1 tensor X_(V*)=0.                 (FN.4)

In finite-dimensional vector spaces, A tensor 1+1 tensor B=0 forces
A=a_V 1 and B=-a_V 1. To see this in bases, all off-diagonal entries of A
and B vanish, and the remaining equations say that every diagonal entry
of A is the negative of every diagonal entry of B. Thus X_V is scalar.

If V,W have the same degree k, V tensor W* also has degree zero, giving
a_V=a_W. Write the common scalar a(k). Applying (FN.1) to any nonzero
modules of degrees k and l proves a(k+l)=a(k)+a(l). Since all integer
degrees occur, a(k)=k a(1). Naturality with direct-sum inclusions and
projections proves the formula on all objects. QED.

If c=1, the same definition allows only degrees in pZ; after rescaling
degree by p the identical proof applies. No special property of a Bol loop
is used in this theorem. Its relevance is that this is a tempting *full*
intertwiner category for the loop's actual finite Heisenberg packets.

## FN3. Ordinary infinitesimal exchange is scalar

**Theorem FN3.** A natural family r_(V,W)(z) on C(P,c) satisfying both
equations (FN.2) is necessarily


```math

             r_{V,W}(z)=a(z)D_V\otimes D_W.               \tag{FN.5}

```


In particular, on homogeneous degrees k,l it is the scalar a(z)kl.

**Proof.** Fix W and expand r_(V,W) in a basis of End(W). Naturality in V
and the first fusion equation make every coefficient a primitive natural
current. FN2 gives

    r_(V,W)=D_V tensor B_W

for an operator B_W. Choose any nonzero object of degree one; it shows that
B_W is natural in W. The second fusion equation makes B primitive, so FN2
gives B_W=a(z)D_W. Direct sums extend the formula. QED.

This proves more than a rank or spectrum constraint: under these explicit
coherence hypotheses there is no nonabelian exchange residue at all.
It also proves less than a general analytic no-go: the scalar function a(z)
is unrestricted by (FN.2), and the theorem deliberately excludes shifted
fusion and a narrower marked class of intertwiners.

## FN4. Formal ordinary exchange adds no hidden higher-order term

Let R_(V,W)(z,hbar) be natural, formal in hbar, and congruent to the identity
modulo hbar. Assume the ordinary unshifted tensor hexagons


```math

\begin{aligned}
R_{V\otimes W,X}&=R_{V,X}^{13}R_{W,X}^{23},\\
R_{V,W\otimes X}&=R_{V,X}^{13}R_{V,W}^{12}
\end{aligned}                                          \tag{FN.6}

```


at the same value of z in every factor. No Yang--Baxter or modular condition
is needed for the next conclusion.

**Theorem FN4.** On C(P,c) there is a scalar formal series
F(z,hbar) in hbar M[[hbar]], where M is the meromorphic coefficient field,
such that


```math

        R_{V,W}=\exp\bigl(F(z,\hbar)D_V\otimes D_W\bigr). \tag{FN.7}

```


On Rep(P) without the integer extension, every such R is the identity.

**Proof.** The first nonzero hbar coefficient of (FN.6) obeys (FN.2), and
is scalar of the form (FN.5). Multiplying R by the inverse of the
corresponding scalar exponential removes that coefficient and preserves
both hexagons. Repeat by increasing hbar degree. Formal completeness gives
(FN.7). With no integer extension use FN1 instead at every step. QED.

This is a formal statement; it asserts no convergence in hbar. The ordinary
flip and pre-existing nontrivial finite braidings are not classified by the
assumption R=1 modulo hbar. In particular, no claim is made about all
elliptic quantum groups.

## Consequence for the present research target

The charged degree repair can give coherent bundles and honest intertwiners,
including the charge-zero channels. It cannot by itself turn a sectorwise
nonabelian elliptic exchange into an exchange natural for **all** ordinary
finite P-intertwiners with (FN.6). Such a proposed system would contradict
FN3 already in its first nonzero infinitesimal coefficient.

Changing bases in the same finite fusion spaces does not affect this
coordinate-free obstruction. A possible repair must change an actual
hypothesis: for example, use variable-dependent intertwiners with dynamical
shifts, retain fewer marked morphisms, or add an infinite-dimensional
interaction algebra. These alternatives require their own coherence proof.

The theorem is a scoped failure of an architecture, proved rather than
inferred from numerical experiments. It does not establish the requested
Bol-specific noncoincident identity, distinguish the rigid isotope pair,
or produce an arithmetic consequence. It identifies precisely why an
ordinary full-intertwiner promotion would not achieve those goals.
