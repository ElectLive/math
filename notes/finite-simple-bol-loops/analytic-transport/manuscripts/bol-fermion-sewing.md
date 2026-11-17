# Integral fermion traces with Bol action and charge sewing

**Mira Cult**

The object constructed here is one graded algebra with actual Bol operators,
commuting central-charge operators, and operators that couple its charges and
grades. Its specified permutation and fusion-intertwiner traces are modular
functions with integer coefficients. The scalar trace
alone does not retain the whole object: the pointwise multiplication and its
current operators are essential additional data.

## Input, markings, and the two central actions

Take an odd-order canonical Bol folder $(G,H,K)$ in the elementary local
class-two setting of
[the canonical input](bol-cocycle-packets.md#canonical-inputs-and-what-is-actually-loop-sensitive).
Write $k_x\in K$ for the distinguished element representing the loop element
$x$. In particular


```math

 k_xk_yk_x=k_{x\cdot(y\cdot x)}.                         \tag{F1}

```


Fix one local prime $p$, put $Z=Z(P)$, and use


```math

 Q=\langle K\cap P\rangle,\qquad
 C=\operatorname{Conj}(Q),\qquad
 X=G\times_Z C,\qquad B=\operatorname{Fun}(X,\mathbb C).
                                                               \tag{F2}

```


The equality of $Q$ with the preimage of the negative eigenspace of the
canonical involution, and the inclusion $Z\leq Q$, are proved in
[the local translation subgroup](bol-translation-class-fusion.md#the-local-translation-subgroup).
Here $Z$ acts on conjugacy classes by central multiplication and
$[gz,c]=[g,zc]$ is our convention for the induced set. The product in $B$
is pointwise multiplication. Its delta-function basis is canonical.

There are two commuting permutation actions on $X$:


```math

 L_g[h,c]=[gh,c],\qquad R_z[h,c]=[h,zc]
 \quad(g,h\in G,\ z\in Z).                              \tag{F3}

```


The right action is well-defined because $Z$ is abelian. It commutes with
every left action, including all distinguished Bol translations. On functions
we always use pullback by the inverse permutation. Although $Z$ need not be
central in $G$, it is normal. On the fiber over $hZ$ one has


```math

 L_z=R_{h^{-1}zh}\quad(z\in Z).                         \tag{F4}

```


Thus the left central action is tied to the right charge action through the
canonical fiber decomposition. These actions must not be conflated.

Let $\psi(t)=\exp(2\pi i t/p)$. For $\ell\in Z^*$, write
$\chi_\ell(z)=\psi(\ell(z))$, and let $B_\ell$ be the eigenspace of the
**right** action with character $\chi_\ell$. All $B_\ell$ are left
$G$-modules. The seed theorem in
[central-charge fusion](bol-translation-class-fusion.md#central-charge-fusion)
gives, with $I=[G:Z]$, $d=\dim_{\mathbb F_p}W$, and
$r_\ell=\operatorname{rank}a_\ell$,


```math

 \dim B_\ell=I p^{d-r_\ell},\qquad
 \operatorname{rank}(B_\ell\otimes B_\mu\longrightarrow B_{\ell+\mu})
   =I p^{\dim(\operatorname{rad}a_\ell\cap\operatorname{rad}a_\mu)}.
                                                               \tag{F5}

```


Its proof is fiberwise pointwise multiplication. If a single fiber is fixed,
the factor $I$ is omitted. The fiber idempotents are retained throughout.
For a complete packet use all admissible local primes, rather than selecting
one by an arbitrary name.

## One graded algebra with a faithful Bol action

Put $n=|X|$, fix a trivial multiplicity space $S=\mathbb C^{24}$, and set


```math

 U_B=\bigoplus_{m\geq1}B[m]\otimes S,
 \qquad \mathcal F_B=\Lambda(U_B).
                                                               \tag{F6}

```


The summand $B[m]$ has degree $m$; the empty exterior product has degree
zero. The degree operator is denoted $D$. Every graded part is finite:
only the finitely many modes $m\leq D$ can contribute. Both actions in
(F3) extend by the exterior functor, giving commuting graded operators
$\Gamma_L(g)$ and $\Gamma_R(z)$. Define
$\mathcal T_x=\Gamma_L(k_x)$.

If several local primes are present, their finite graded tensor product is
a single object $\mathcal F(L)$. Equivalently apply (F6) to the direct sum
of the $B_p$, retaining its prime factors and using the usual exterior
sign convention. The left loop action is diagonal and the right charge
group is the product of the local centers. The formulas below use the local
$n=|X|$; global traces are products of these local traces.

**Proposition F-A (actual action and functoriality).** The operators
$\mathcal T_x$ satisfy the Bol relation (F1) in every degree. The left
$G$-action on $\mathcal F_B$ is faithful. Strict transport of the source
normal data induces an isomorphism of these graded objects, intertwining the
indexed translations, central charges, fiber idempotents, and the marked
cocycle operators defined below. Consequently the full marked packet is a
loop-isomorphism invariant under the cited strict-isomorphism interface.

**Proof.** The exterior functor respects composition, so it carries (F1) to
the asserted identity. The singleton conjugacy classes of the elements of
$Z$ form a canonical regular $Z$-orbit inside $C$. Inducing that orbit
gives


```math

 G\times_Z Z\ \cong\ G,\qquad [g,z]\longmapsto gz,

```


with the regular left $G$-action. Hence the action on $X$, and already
on $(\mathcal F_B)_1=B\otimes S$, is faithful. A strict transport preserves
$G,H,K,P,Z,Q$ and induces compatible bijections of $C$, $X$, and their
fibers. Pullback gives an algebra isomorphism of the function algebras and
then an exterior-algebra isomorphism. The transport equations for $f$ and
$T$ give the last markings. QED.

This proposition uses sandwich representations, whose split Bol-extension
interpretation is proved in
[Proposition O0](bol-translation-fock.md#sandwich-representations-are-actual-bol-extension-modules).
It does not impose $\mathcal T_x\mathcal T_y=\mathcal T_{xy}$. Because the
group action is faithful, an actual multiplication defect remains a
nonidentity graded operator whenever its word in $G$ is nonidentity.

Morphisms of the marked objects here are the induced graded isomorphisms
intertwining the displayed markings and operators. Their compositions are
ordinary compositions; independence of coordinate choices follows from the
strict transport theorem. Forgetting the indexed translations or $f$ is a
specified forgetful operation, not our equivalence relation.

## Charge and grade coupling inside the same object

Let $e_x$ be the delta function at $x\in X$. For a mode $m\geq1$ and a
species $j\in\{1,\ldots,24\}$, let $c^\dagger_{xjm}$ be exterior
multiplication by $e_x\otimes e_j$ in mode $m$, and let $c_{xjm}$ be
contraction by its dual. On the algebraic exterior space these operators
satisfy the canonical anticommutation relations


```math

 \{c_i,c^\dagger_j\}=\delta_{ij},\qquad
 \{c_i,c_j\}=\{c^\dagger_i,c^\dagger_j\}=0.             \tag{F7}

```


For $a\in B$ and positive integers $m,n$, define the finite-sum operator


```math

 E_a^{mn}=\sum_{x\in X}\sum_{j=1}^{24}
        a(x)c^\dagger_{xjm}c_{xjn}.                  \tag{F8}

```


These are even operators of degree $m-n$. They are the second quantizations
of the maps that multiply by $a$ while carrying mode $n$ to mode $m$.
No choice of an eigenbasis for the charge decomposition enters (F8).

**Theorem F-B (charge sewing and exact current law).** For all $a,b\in B$,


```math

 [E_a^{mn},E_b^{rs}]
   =\delta_{nr}E_{ab}^{ms}-\delta_{sm}E_{ab}^{rn},      \tag{F9}

```


and


```math

 \Gamma_L(g)E_a^{mn}\Gamma_L(g)^{-1}=E_{L_g a}^{mn},
 \qquad
 \Gamma_R(z)E_a^{mn}\Gamma_R(z)^{-1}=E_{R_z a}^{mn}.
                                                               \tag{F10}

```


If $a\in B_\ell$, the operator $E_a^{mn}$ sends total charge $\mu$
to total charge $\ell+\mu$, while changing the grade by $m-n$. On the
one-particle mode-$n$ space of any fixed species, the map


```math

 B_\ell\otimes B_\mu\longrightarrow B_{\ell+\mu},
 \qquad (a,b)\longmapsto E_a^{mn}b[n]
                                                               \tag{F11}

```


is exactly $(a,b)\mapsto(ab)[m]$. Its rank is (F5), so the marked graded
object retains simultaneous radical intersections, not only the individual
numbers $r_\ell$.

**Proof.** For combined labels the CAR give


```math

 [c_i^\dagger c_j,c_k^\dagger c_l]
       =\delta_{jk}c_i^\dagger c_l-\delta_{li}c_k^\dagger c_j.

```


Indeed substituting $c_jc_k^\dagger=\delta_{jk}-c_k^\dagger c_j$
in the first product and the analogous identity in the second leaves two
quartic terms that cancel by the two same-type anticommutation relations.
Substituting (F8), the Kronecker deltas require the same point and species;
the coefficients multiply to $a(x)b(x)$. This proves (F9). Permutations
carry creation operators and their dual contractions to the corresponding
ones at the permuted point, proving (F10).

If $R_z a=\chi_\ell(z)a$, the second equation of (F10) gives adjoint
charge $\ell$. Applying it to a vector of charge $\mu$ proves the
charge-addition assertion. Direct contraction of a one-particle vector gives
$E_a^{mn}b[n]=(ab)[m]$, and (F5) proves the rank statement. QED.

This is a representation of the finitary matrix Lie algebra with coefficient
algebra $B$; the coefficient product is the translation-class product.
There is no assumed categorical associator, pentagon, vertex algebra, or
analytic sewing axiom. Here "sewing" means precisely (F9)--(F11).

For an ablation with the same complete indexed scalar-rank function and
different fusion ranks, see
[the controlled pencil comparison](bol-graded-architecture-audit.md).
Its two six-dimensional pencils have rank four at every nonzero character,
but the radicals of two independent characters intersect in dimension two
in one pencil and in dimension zero in the other. Thus (F11) has ranks
$I p^2$ and $I$, respectively. This comparison is at the stated local
alternating-data level; no unproved assertion that both are simple Bol
loops is needed. A decomposition into independent sectors retaining just
their dimensions would erase this distinction.

## The stabilizer cocycle is an operator identity

In the source normal form the pure torus $A$ is contained in $K$, and
the marked positive cocycle satisfies


```math

 f(ab)=f(a)+T(a)f(b),\qquad T(a)\sigma f(a)=f(a).
                                                               \tag{F12}

```


Use its component in the selected $Z$, and put
$\mathcal A_a=\Gamma_L(a)$,
$\mathcal U_a=\Gamma_L(f(a))$, and
$\mathcal Q_a=\Gamma_R(f(a))$. Then the first relation becomes


```math

 \mathcal U_{ab}=
 \mathcal U_a\mathcal A_a\mathcal U_b\mathcal A_a^{-1}.
                                                               \tag{F13}

```


This follows from conjugation by $a$ acting as $T(a)$ on $Z$.
The right operator $\mathcal Q_a$ acts by the literal scalar
$\psi(\ell(f(a)))$ on total charge $\ell$. Formula (F4), retained through
the fiber idempotents and currents, relates these literal phase measurements
to the actual left operators. The two roles have different formulas.
The finite-seed proof and full/local cocycle distinction are owned by
[Proposition CF4](bol-translation-class-fusion.md#the-stabilizer-cocycle-as-an-actual-operator-relation);
(F13)--(F16) are its exterior-functor lifts.

There is also an inversion coherence. The canonical involution $\tau$
preserves $Q$, since it inverts each generator in $K\cap P$. Hence it
acts on $C$, and


```math

 [g,c]\longmapsto[\tau(g),\tau(c)]

```


is a well-defined involution of $X$. Its exterior lift $\Theta$ obeys


```math

 \Theta\mathcal T_x\Theta^{-1}=\mathcal T_x^{-1},
 \qquad
 \Theta\mathcal U_a\Theta^{-1}
       =\mathcal A_a^{-1}\mathcal U_a\mathcal A_a.      \tag{F14}

```


The first equality is $\tau(k_x)=k_x^{-1}$, and the second is
$\sigma f(a)=T(a)^{-1}f(a)$, the second relation of (F12). No claim below
about odd-order trace products is applied to $\Theta$.

In characteristic three a useful marked probe is obtained without assigning
an independent phase label to a formal rank sector. Define


```math

 \mathcal V_a=\mathcal U_a\mathcal A_a\mathcal U_a\mathcal A_a^{-1},
 \qquad
 \mathcal W_a=\mathcal V_a\mathcal A_a\mathcal V_a\mathcal A_a^{-1}.
                                                               \tag{F15}

```


All factors are actual graded operators, and direct use of conjugation gives


```math

 \mathcal W_a=\Gamma_L(z_f),\qquad
 z_f=(1+T(a))^2 f(a)
     =\bigl(T(a)+(T(a)-1)^2\bigr)f(a).                \tag{F16}

```


The last equality uses characteristic three. The collection over all $a$
is natural under strict transport; no generator is generally assumed fixed.
In the rigid-center comparison the source's rigid secondary-prime action
forces the displayed generator $a$ to be preserved, as recorded in
[the phase-fiber obstruction](bol-cocycle-packets.md#the-rigid-principal-isotope-calculation).

## Integral traces and a common modular transformation law

Let $s$ be any odd-order permutation of $X$, let $h=\operatorname{ord}(s)$,
and let $c_d(s)$ be its number of cycles of length $d$. Each $d$ is odd.
For $\tau$ in the upper half-plane and $q=e^{2\pi i\tau}$, define


```math

 \Phi_s(\tau)=q^n\operatorname{Tr}_{\mathcal F_B}
                   (\Gamma(s)q^D).
                                                               \tag{F17}

```


The exponent is a fixed normalization, corresponding to $\delta=-n$ in
$\sum_m\operatorname{Tr}(\Gamma(s)|\mathcal F_m)q^{m-\delta}$.
It is not asserted to be a conformal vacuum shift.

**Theorem F-C (honest integral modular traces).** The series (F17) converges
locally uniformly on the upper half-plane and satisfies


```math

 \begin{aligned}
 \Phi_s(\tau)
 &=q^n\prod_{m\geq1}\det(1+q^m s\mid B)^{24}\\
 &=\prod_{d\mid h}
       \left(\frac{\Delta(2d\tau)}{\Delta(d\tau)}\right)^{c_d(s)},
 \end{aligned}                                                   \tag{F18}

```


where
$\Delta(\tau)=q\prod_{m\geq1}(1-q^m)^{24}$.
It is a weight-zero modular function with trivial multiplier on
$\Gamma_0(2h)$, holomorphic and nonvanishing in the upper half-plane and
meromorphic at all cusps. Every coefficient before the common shift $q^n$
is a nonnegative integer, and


```math

 \Phi_s(\tau)=q^n\bigl(1+24\operatorname{Fix}_X(s)q+O(q^2)\bigr).
                                                               \tag{F19}

```


**Proof.** On a finite-dimensional space the exterior trace is
$\operatorname{Tr}_{\Lambda V}(t^{\mathrm{degree}}g)=\det(1+tg)$,
as follows by diagonalizing the finite-order operator and choosing an
exterior monomial basis. Applying this to each mode and species gives the
first equality. For a $d$-cycle,


```math

 \det(1+t s)=1-(-t)^d=1+t^d

```


because $d$ is odd. Hence the unshifted trace is
$\prod_{d,m}(1+q^{dm})^{24c_d(s)}$, proving its integral nonnegative
coefficients. The identity


```math

 \frac{\Delta(2d\tau)}{\Delta(d\tau)}
      =q^d\prod_{m\geq1}(1+q^{dm})^{24}

```


and $\sum_d dc_d(s)=n$ prove (F18). The products converge locally
uniformly because $\sum_{m\geq1}|q|^m<\infty$ uniformly on compact
subsets, and their factors are nonzero for $|q|<1$. The degree-one part
is $B\otimes\mathbb C^{24}$, giving (F19).

For $\gamma=\begin{pmatrix}a&b\\c&e\end{pmatrix}\in\Gamma_0(2h)$
and $\delta\mid2h$, the matrix
$\begin{pmatrix}a&b\delta\\c/\delta&e\end{pmatrix}$ is in
$\mathrm{SL}_2(\mathbb Z)$. The ordinary discriminant law therefore gives


```math

 \Delta(\delta\gamma\tau)
     =(c\tau+e)^{12}\Delta(\delta\tau).

```


Apply this with $\delta=d,2d$. Each quotient in (F18) has weight zero
and trivial multiplier, proving the claimed transformation law. Cusp
meromorphy follows by applying the eta rescaling formula at a rational cusp:
each factor is a constant times a rational power of the local parameter
times a convergent product with constant term one; modularity makes the
exponents integral in the appropriate cusp parameter. The source used for
the eta/discriminant law and this cusp step is Scheithauer, §6,
Propositions 6.1--6.2, listed in
[the modular references](../REFERENCES.md#modular-analytic-sources). QED.

The 24 species have a precise analytic purpose: the eta multiplier is
removed by the power $\eta^{24}=\Delta$. The exterior algebra and its
integral traces exist before this simplification. This is not denominator
clearing of a rational Eisenstein series and supplies no evidence for a
Monster action or a special significance of 24 for the loop family.

## Actual sector traces at one common weight

Define orthogonal idempotents on the same graded object by


```math

 P_\ell=\frac1{|Z|}\sum_{z\in Z}
             \chi_\ell(z)^{-1}\Gamma_R(z),\qquad
 \mathcal F_{B,\ell}=P_\ell\mathcal F_B.               \tag{F20}

```


Character orthogonality proves that their images are exactly the total-charge
eigenspaces and that their sum is the identity. Exterior multiplication adds
charges. Every $\Gamma_L(g)$, hence every Bol operator, preserves every
$\mathcal F_{B,\ell}$.

**Corollary F-D (common-level charge projection).** Put
$e_G=\exp(G)$. For every $g\in G$,


```math

 \Phi_{g,\ell}(\tau)
 :=q^n\operatorname{Tr}_{\mathcal F_{B,\ell}}
                      (\Gamma_L(g)q^D)
 =\frac1{|Z|}\sum_{z\in Z}\chi_\ell(z)^{-1}
                     \Phi_{L_gR_z}(\tau).            \tag{F21}

```


These are weight-zero modular functions with trivial multiplier on the
single group $\Gamma_0(2e_G)$. The weaker common group
$\Gamma_0(2|G|)$ is available without computing the exponent. For
$g\in Z$ and elementary abelian $Z$ of exponent $p$, all the functions
in (F21) are already modular on $\Gamma_0(2p)$.

**Proof.** The trace of an idempotent times a commuting operator is the trace
on its image, giving (F21). Because left and right actions commute,
$(L_gR_z)^{e_G}=1$. These permutations have odd order, so Theorem F-C
applies to each summand on a common subgroup. If $g,z\in Z$, their
commuting permutations have order dividing $p$, proving the sharper
level. QED.

For $g=1$, every coefficient before the common shift is an actual
nonnegative integer dimension. For general $g$, coefficients are algebraic
integers, being traces of finite-order operators on finite-dimensional
spaces; rationality is not asserted. Division by $|Z|$ in (F20)--(F21)
is the formula for a genuine projection, not a prescription to round or
clear denominators. In particular the current maps in Theorem F-B connect
these very same sectors whose graded traces have the common modular law.

## A symbolic marked trace separating the rigid isotope pair

Use the canonical local input and exact counts proved in
[the rigid-center seed calculation](bol-translation-class-fusion.md#the-rigid-center-pair-exact-graded-seed-counts).
The original loop and its displayed principal isotope have order
$3^{75}19^3$. Their reported simplicity, properness, and isotope relation
are inherited from the pinned source and its stated dependencies; they are
not proved again here.

Set


```math

 M=3^{36},\qquad |G|=3^{149}19^6,\qquad
 I=[G:Z_3]=3^{146}19^6,\qquad n=3I(M+2)^2.
                                                               \tag{F22}

```


The relevant center is $Z_3=\mathbb F_3[\epsilon]/(\epsilon^3)$,
$T(a)=1+\epsilon$, and the two marked cocycle values are


```math

 f(a)=1-\epsilon+\epsilon^2,\qquad f'(a)=1-\epsilon.

```


The actual operator word (F15) is the left action of


```math

 z_f=1+\epsilon^2,\qquad z_{f'}=1.

```


Its fixed-point counts on $X$ are, respectively,


```math

 F_+=I(M^2+M-2),\qquad F_-=I(M-1)^2,
 \qquad F_+-F_-=3I(M-1).                              \tag{F23}

```


These are counts for the **left** central action. The induction average
over torus conjugates is essential; replacing them by the unaveraged right
central-action counts would give incorrect exponents for (F15). All
remaining cycles have length three.

**Corollary F-E (integral modular isotope obstruction).** With
$H(\tau)=\Delta(2\tau)/\Delta(\tau)$, the two marked traces are


```math

 \Phi_\pm(\tau)
    =H(\tau)^{F_\pm}
       H(3\tau)^{(n-F_\pm)/3}.                        \tag{F24}

```


They are integral graded traces, holomorphic on the upper half-plane and
weight-zero modular functions with trivial multiplier on $\Gamma_0(6)$.
They are unequal; more precisely,


```math

 \frac{\Phi_+(\tau)}{\Phi_-(\tau)}
   =\left(\frac{H(\tau)^3}{H(3\tau)}\right)^{I(M-1)},
                                                               \tag{F25}

```


and their coefficients of $q^{n+1}$ differ by $72I(M-1)$.

**Proof.** Apply (F18) to the cycle counts (F23). The ratio follows by
subtracting those exponents: the fixed-cycle difference is $3I(M-1)$
and the three-cycle difference is $-I(M-1)$. Equation (F19) gives the
coefficient difference. It is positive, since $M>1$. The source rigidity
condition and strict transport carry the marked word (F15) to its counterpart
in the second loop, so this unequal trace is an isomorphism obstruction
within the stated input interface. QED.

The two unmarked graded spaces can be isomorphic, and forgetting $f$ can
even leave the same group, transversal, and unmarked permutation action.
The theorem compares the naturally marked cocycle operators. It does not
claim that their dimensions or their identity traces distinguish the loops.
Equations (F22)--(F25) require field, center, and operator calculations only;
no loop or $X$ table is enumerated.

There is an equally explicit sector-dimensional witness. The prescribed
phase triple


```math

 \bigl(\ell(f(a)),\ell((T(a)-1)f(a)),
                 \ell((T(a)-1)^2f(a))\bigr)=(1,0,1)
                                                               \tag{F26}

```


selects $\ell_+=(1,1,1)$ in the original data and
$\ell_-=(2,1,1)$ in the isotope. Corollary CF6 of
[the seed calculation](bol-translation-class-fusion.md#the-rigid-center-pair-exact-graded-seed-counts)
gives $\dim B_{\ell_+}=I$ and $\dim B_{\ell_-}=IM$. Consequently
the actual total-charge Hilbert functions of this one graded construction
satisfy


```math

 \Phi_{1,\ell_+}(\tau)=q^n(24I q+O(q^2)),\qquad
 \Phi'_{1,\ell_-}(\tau)=q^n(24IM q+O(q^2)).           \tag{F27}

```


Both have nonnegative integer coefficients and the common weight-zero,
trivial-multiplier law on $\Gamma_0(6)$ from Corollary F-D. There is no
vacuum term because both charges are nonzero. Their higher coefficients are
dimensions of charge spaces in the same exterior algebra, with the current
operators (F8) connecting them to the other sectors. They are not Fock
spaces separately defined from the dimensions $I$ and $IM$.

The unprojected obstruction (F25) also survives the single global tensor
product over all primes. On a factor induced from a different prime's
normal center $Z_q$, a nontrivial order-three element of $Z_3$ fixes no
fiber of $G/Z_q$, since it cannot belong to $Z_q$. Its cycles on that
factor all have length three. Thus $z_f$ and $z_{f'}$ give identical
extra factors, which cancel in the ratio (F25).

## Fusion itself has an integral modular trace

The multiplication operators give more than an extra invariant carried
alongside modular functions. They produce modular traces that detect the
interaction of sectors.

For a nonempty finite tuple of charges
$\boldsymbol\ell=(\ell_1,\ldots,\ell_t)$, define the actual image
subspace in $B$


```math

 U_{\boldsymbol\ell}
   =\operatorname{image}\bigl(B_{\ell_1}\otimes\cdots\otimes B_{\ell_t}
                         \xrightarrow{\mathrm{multiplication}}B\bigr),
 \qquad
 s_{\boldsymbol\ell}=\dim U_{\boldsymbol\ell}.
                                                               \tag{F28}

```


The product is pointwise, so the subspace is independent of parenthesization.
It is $G$-invariant and lies in right charge $\sum_i\ell_i$. By the
canonical counting Hermitian form on $B$, it has an orthogonal projector
$\Pi_{\boldsymbol\ell}$. Because both left $G$ and right $Z$ act
unitarily and preserve the subspace, this projector commutes with both.
It is canonically transported by strict data isomorphisms. The current
realization (F11), iterated, realizes this same image on one-particle spaces.

Let $E_p$ be the augmentation space of the regular cyclic representation:


```math

 E_p=\{v\in\mathbb C[\mathbb F_p]:\textstyle\sum_x v(x)=0\},
 \qquad C_p:e_x\longmapsto e_{x+1}.

```


It has dimension $p-1$, and the eigenvalues of $C_p|E_p$ are precisely
the nonidentity $p$-th roots of unity. On $B\otimes E_p$ put


```math

 J_{\boldsymbol\ell}
   =(1-\Pi_{\boldsymbol\ell})\otimes1
                    +\Pi_{\boldsymbol\ell}\otimes C_p.           \tag{F29}

```


This is a unitary order-dividing-$p$ Bol intertwiner, not generally a
permutation of $X$ or a distinguished loop translation. Its exterior lift
acts on the one common tensor enlargement


```math

 \mathcal F_B^{[p-1]}
 =\Lambda\!\left(\bigoplus_{m\geq1}(B\otimes E_p)[m]
                              \otimes\mathbb C^{24}\right).

```


After choosing a basis of $E_p$, this is the ordinary graded tensor power
$\mathcal F_B^{\otimes(p-1)}$. All tuples act on this same space; no
graded space is chosen from the numerical value of $s_{\boldsymbol\ell}$.
The diagonal loop action commutes with every $\Gamma(J_{\boldsymbol\ell})$.

**Theorem F-F (joint-fusion modular character).** For odd $p$, set
$s=s_{\boldsymbol\ell}$. The actual trace


```math

 \Psi_{\boldsymbol\ell}(\tau)
 =q^{(p-1)n}\operatorname{Tr}_{\mathcal F_B^{[p-1]}}
                      (\Gamma(J_{\boldsymbol\ell})q^D)

```


has integer coefficients and the exact formula


```math

 \boxed{\displaystyle
 \Psi_{\boldsymbol\ell}(\tau)
       =H(\tau)^{(p-1)n-ps}H(p\tau)^s.}
                                                               \tag{F30}

```


It is a weight-zero modular function with trivial multiplier on
$\Gamma_0(2p)$, holomorphic and nonvanishing in the upper half-plane and
meromorphic at all cusps. Its first coefficient is


```math

 \Psi_{\boldsymbol\ell}(\tau)
 =q^{(p-1)n}\bigl(1+24((p-1)n-ps)q+O(q^2)\bigr).     \tag{F31}

```


Hence the graded modular trace determines the actual fusion-image dimension.
For the translation-class seed,


```math

 s_{\boldsymbol\ell}
      =I\left|\bigcap_{i=1}^t\operatorname{rad}a_{\ell_i}\right|.
                                                               \tag{F32}

```


**Proof.** The complement of $U_{\boldsymbol\ell}$ contributes the
eigenvalue one with multiplicity $(p-1)(n-s)$ to (F29). Its image
contributes each nonidentity $p$-th root with multiplicity $s$.
For an indeterminate $u$, the cyclotomic identity at odd $p$ gives


```math

 \det(1+uJ_{\boldsymbol\ell})
  =(1+u)^{(p-1)(n-s)}
       \left(\frac{1+u^p}{1+u}\right)^s
  =(1+u)^{(p-1)n-ps}(1+u^p)^s.

```


The first expression is a polynomial with integer coefficients because
$(1+u^p)/(1+u)=1-u+u^2-\cdots+u^{p-1}$. Applying the exterior determinant
formula independently at each mode and for 24 species proves that every
graded trace coefficient is an integer. It also gives (F30), since the
leading power of its right side is
$q^{(p-1)n-ps+ps}=q^{(p-1)n}$. The same convergence and discriminant
transformation argument as in Theorem F-C proves the analytic assertions.
Reading the coefficient of $q$ proves (F31).

Finally the seed basis product is zero unless every input has the same
$w$, and otherwise its output is the basis vector of charge
$\sum_i\ell_i$ at $w$. The admissible common $w$ are precisely the
intersection in (F32). Distinct fibers give independent images. This proves
(F32), extending the binary calculation (F5). QED.

The exponent $(p-1)n-ps$ can be negative. The resulting coefficients
remain integers but need not be nonnegative: they are traces of genuine
finite-order operators on actual graded spaces, rather than dimensions.
The construction does not assert that $J_{\boldsymbol\ell}$ preserves
every current operator; the required property is that it intertwines the
Bol action and is defined intrinsically from its charge multiplication.
The same proof applies to any subspace $U\leq B$ invariant under the
left and right actions; write $J_U$ and $\Psi_U$ for its projector
construction. In particular sums and intersections of fusion images are
allowed, on the same enlarged graded space.

Equivalently, put $\Omega=1+(\zeta_p-1)\Pi_{\boldsymbol\ell}$ on $B$
and use $\Omega,\Omega^2,\ldots,\Omega^{p-1}$ on the $p-1$ tensor
factors. The augmentation formulation (F29) makes independence of a
primitive root or an eigenbasis explicit. Choosing the enlarged space from
the outset puts all the fusion probes and all the earlier operators on a
single graded object. Its diagonal original norm-word traces are
$\Phi_\pm^{p-1}$, so the large-isotope separation remains strict.

In the controlled pencils of
[the architecture audit](bol-graded-architecture-audit.md), take $p=3$
and the local class algebra before induction. Both have
$n=3^6+8\cdot3^2=801$, identical indexed ranks, and therefore identical
ordinary central characters. For two independent charges their binary
fusion images have dimensions 9 and 1. The corresponding functions are


```math

 H(\tau)^{1575}H(3\tau)^9,
 \qquad H(\tau)^{1599}H(3\tau),                       \tag{F33}

```


and their ratio is $(H(3\tau)/H(\tau)^3)^8$. Their coefficients of
$q^{1603}$ are 37800 and 38376, differing by $-576$. This is an
analytic distinction that all the individual scalar-rank data and all the
central permutation traces of the seed miss. Induction multiplies
$n$ and both fusion dimensions by $I$ and preserves the distinction.

**Corollary F-G (analytic reconstruction of the central class geometry).**
Retain $G,Z$, their inclusion, and the charge indexing. The family of
modular functions $\Psi_{\boldsymbol\ell}$, over all nonempty finite
charge tuples, determines $C$ up to $Z$-equivariant bijection and hence
determines its pointwise function algebra with counting Hermitian form.
Tuples of length at most $\max(1,\dim_{\mathbb F_p}Z)$ already suffice.

**Proof.** The common leading exponent recovers $n$; equation (F31)
recovers every $s_{\boldsymbol\ell}$. Since $I=[G:Z]$ is known, (F32)
recovers every simultaneous radical-intersection count. For a subspace
$J\leq Z$, use a basis of $J^\perp$ as the charge tuple, or the tuple
$(0)$ when $J=Z$. The resulting count is the function $h(J)$ of
[Theorem CF7](bol-translation-class-fusion.md#higher-fusion-reconstructs-the-central-conjugacy-class-geometry).
Its subspace Möbius inversion recovers the number of central orbits of each
stabilizer $J$, proving the assertion. QED.

This reconstructs the central class geometry, not the loop, the full bimap,
or its stabilizer cocycle. Parenthesization coherence comes from associative
pointwise multiplication of class functions, not from attributing a
categorical pentagon to a loop associator.

**Proposition F-H (an exact binary/triple-channel functional identity).**
Fix an output charge $\nu$, and put


```math

 U=B_\ell B_{\nu-\ell},\qquad
 V=B_\rho B_{\nu-\rho},\qquad
 W=B_\ell B_\rho B_{\nu-\ell-\rho}.

```


Then $U\cap V=W$. The sum $U+V$ is the image of the map into
$B_\nu$ obtained by adding the two binary multiplication maps. These
actual channels satisfy both


```math

 J_UJ_V=J_{U+V}J_W,\qquad
 \boxed{\Psi_U(\tau)\Psi_V(\tau)
             =\Psi_{U+V}(\tau)\Psi_W(\tau).}          \tag{F34}

```


**Proof.** In each fiber, the charge-$\nu$ basis is indexed by
$w\in R_\nu$, where $R_\alpha=\operatorname{rad}a_\alpha$.
The support of $U$ is $R_\ell\cap R_{\nu-\ell}=R_\nu\cap R_\ell$;
this equality follows from linearity of $a_\alpha$ in $\alpha$.
Similarly $V$ has support $R_\nu\cap R_\rho$. Their intersection
is $R_\nu\cap R_\ell\cap R_\rho$, which is precisely the support
of the triple image $W$. This proves the intersection assertion.

These are coordinate-support subspaces in the same orthogonal basis of
$B_\nu$. Thus their orthogonal projectors commute, with
$\Pi_U\Pi_V=\Pi_W$ and
$\Pi_{U+V}=\Pi_U+\Pi_V-\Pi_W$. On the four simultaneous membership
subspaces, each side of the operator identity acts on $E_p$ by the same
power $1,C_p$, or $C_p^2$, proving that identity. Finally
$\dim U+\dim V=\dim(U+V)+\dim W$; substitution in (F30) proves
the displayed functional identity, including its common $q$-shift. QED.

The binary/triple-channel identity holds more generally for the pointwise
function algebra of any finite abelian Z-set. On an orbit Z/J a character
occurs exactly when it annihilates J; the same support argument then applies.
For elementary abelian Z, the stabilizer-count reconstruction in F-G likewise
has this broader scope. The Bol loop supplies the canonical seed, its actual
translations, the selected channels and the cocycle markings. These functional
identities do not characterize Bol loops. In particular (F34) is not obtained
by incorrectly treating the trace of an operator product as the product of
traces, and it is not asserted to be a Lie-algebra denominator identity.

The elementary bilinear input supplies additional restrictions that arbitrary
Z-sets need not satisfy. Theorem CF8 in
[the seed manuscript](bol-translation-class-fusion.md) proves that the
induction-normalized simultaneous fusion dimensions are powers of p and that
their recovered codimensions form a monotone submodular function of charge
subspaces. Its 51-point comparison has identical individual characters and
central graded traces, but its alternative fusion dimension 2 violates the
necessary power-of-three condition. The corresponding functions are
H(tau)^99 H(3tau) and H(tau)^96 H(3tau)^2, with first normalized coefficients
2376 and 2304. The generic modular construction exists in both cases; the
new necessary condition detects which finite geometry cannot be an elementary
class-two translation-class seed. It does not give sufficient realizability
conditions or a new analytic transformation law peculiar to Bol loops.

## What is established and the next mathematical boundary

The construction gives the four requested ingredients simultaneously in the
sense of a coupled graded object from the canonical finite seed:

| Requirement | Mathematical realization |
| --- | --- |
| One natural graded object joining phase sectors | (F2), (F6), and the actual charge projectors (F20) |
| A justified loop action | Faithful left action, distinguished translations, and the Bol relation in Proposition F-A |
| Modular traces separating the huge marked isotope pair | Integral trace formula (F18) and exact obstruction (F24)--(F25) |
| An intersector and grade law beyond individual ranks | The current commutator (F9), its one-particle realization (F11), joint-fusion modular traces and reconstruction (F30)--(F33), the channel identity (F34), the necessary bilinear-input constraints in CF8, and cocycle/inversion coherence (F13)--(F16) |

The exterior functor, CAR, character projections, and discriminant modularity
are established machinery. The proposed contribution is their attachment to
the subgroup generated by local Bol translations and its class-fusion
algebra, with the positive stabilizer cocycle represented by operators and
with the displayed exact loop-sensitive consequences. No literature-priority
claim is inferred from this construction.

The proof does not establish a vertex algebra, genus-zero property,
replicability, a denominator identity, or a modular transformation rule for
arbitrary inserted current correlation functions. The common-level modular
law is still a standard exterior-Fock mechanism. The fusion-derived
finite-order insertions are a proved exception to the absence of a general
current-insertion transformation theorem: (F30) supplies an exact law for
them. The loop information is supplied by the canonically built finite seed,
its fusion, the actual translations, and the cocycle words. The conditional
scope of the imported class-two classification remains unchanged.

A decisive next question is whether the mode-resolved current operators and
cocycle identities force a closed system of genus-one correlation functions
beyond the fusion-projector functions (F30) and their channel law (F34),
with analytic behavior depending on more than the corresponding image
dimensions. A result deriving such a closure or a denominator identity from
these marked Bol relations would provide additional analytic rigidity for a
stronger moonshine claim. The construction above supplies concrete operators
and exact tests for that question; it does not assume its answer.
