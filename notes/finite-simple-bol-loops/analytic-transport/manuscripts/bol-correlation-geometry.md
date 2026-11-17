# Current correlations recover the marked commutator geometry

**Mira Cult**

Construction and proofs by model participant 14 for the owned PR #438
continuation. Results CG1--CG6 are manuscript-local and allocate no permanent
claim IDs. Exact-source review belongs in the continuation's review record.

The finite geometry below uses the canonical folder and elementary class-two
input of [CF1--CF8](bol-translation-class-fusion.md). Their source and review
pins, including the strict-isomorphism interface, remain inherited assumptions.
The analytic original-Fock construction is owned by
[the current-correlation manuscript](bol-genus-one-correlations.md); its
completed torus kernel is owned by
[the genus-one kernel manuscript](bol-genus-one-kernel.md).

The endpoint here is precise: low-degree coefficients of actual current traces
recover central words in actual translations, including information lost by
every higher-fusion dimension. Under a stated invertibility condition they
recover the original normal-form bimap, not just its alternating part.
An explicit pair of class-two group controls has identical entire class-fusion
algebras but inequivalent recovered alternating bimaps. A separate calculation
inside the huge proper Bol input distinguishes two conjugate cocycle operators
that every charge-projected zero-point trace identifies.

## A finite coefficient algebra for the current system

Use the notation


```math

 Q=\langle K\cap P\rangle,\quad Z=Z(P),\quad
 C=\operatorname{Conj}(Q),\quad X=G\times_Z C,\quad
 B=\operatorname{Fun}(X,\mathbb C),\quad n=|X|.

```


The left action is $L_g$, the commuting right action is $R_z$, and both
act on functions by inverse pullback. For $a\in B$, let $M_a$ be
pointwise multiplication by $a$. This is the one-particle operator underlying
the already constructed current $E_a^{mn}$.

**Proposition CG1 (finite product and cyclic-trace calculus).** The span


```math

 \mathscr A_X=\operatorname{span}_{\mathbb C}
                  \{M_aL_g:a\in B,\ g\in G\}

```


is a finite-dimensional algebra of actual operators, with


```math

 (M_aL_g)(M_bL_h)=M_{a(L_gb)}L_{gh}.                 \tag{CG1.1}

```


For $g=g_1\cdots g_t$ and $g_{<i}=g_1\cdots g_{i-1}$,


```math

 \operatorname{Tr}_B(M_{a_1}L_{g_1}\cdots M_{a_t}L_{g_t})
  =\sum_{\substack{x\in X\\gx=x}}
          \prod_{i=1}^t a_i(g_{<i}^{-1}x).          \tag{CG1.2}

```


If the $G$-orbits on $X$ are $\mathcal O$, the unmarked algebra is


```math

 \mathscr A_X\cong\bigoplus_{\mathcal O}
                       \operatorname{End}_{\mathbb C}(\mathbb C^{\mathcal O}).
                                                               \tag{CG1.3}

```


**Proof.** Inverse pullback gives $L_gM_b=M_{L_gb}L_g$, proving
(CG1.1). Iteration gives a multiplication operator followed by $L_g$.
Its diagonal entry at $x$ vanishes unless $gx=x$, and otherwise is the
displayed product. This proves (CG1.2).

All the operators preserve the spans of the point bases of the $G$-orbits.
Conversely, if $x,y$ are in one orbit, choose $g$ with $gy=x$. Then
$M_{\delta_x}L_gM_{\delta_y}$ is the matrix unit carrying $\delta_y$
to $\delta_x$. These matrix units prove (CG1.3). QED.

These are general finite-action identities, not new Bol identities. The
image algebra need not be the abstract crossed product: an action can give
relations among its nominal crossed-product generators. Equation (CG1.3)
also shows exactly how much forgetting the markings can lose.

The loop-specific data retained here are the distinguished $L_{k_x}$, their
sandwich relation, the canonical fiber idempotents, and the source cocycle
operators. Their relations remain literal equalities in $\mathscr A_X$.
For instance, $L_{k_x}L_{k_y}L_{k_x}=L_{k_{x\cdot(y\cdot x)}}$, and the
positive-cocycle relation is the equality of operators proved in CF4.
Inserting such equal operators in (CG1.2) or in a current trace preserves
the equality. This supplies finite coefficients and consistency conditions
for the analytic system; it does not derive its modular kernel by itself.

## Fiber-current phases recover central words

Let $e\in B$ be the indicator of the canonical identity fiber $[1,C]$.
It is right-$Z$-invariant and


```math

 \sum_{x\in X}e(x)=|C|.

```


For $\ell\in Z^*$, write $\chi_\ell(z)=\psi(\ell(z))$, where
$\psi(t)=\exp(2\pi it/p)$. Let


```math

 \pi_\ell=|Z|^{-1}\sum_{z\in Z}\chi_\ell(z)^{-1}R_z

```


be the finite one-particle right-charge projector. Put


```math

 m_\ell=\dim(A_C)_\ell=p^{d-r_\ell},\qquad
 K_\ell(c)=\operatorname{Tr}_B(M_e\pi_\ell L_c)
                     \quad(c\in Z).               \tag{CG2.1}

```


Here $c=0$ denotes the central identity in additive coordinates.

**Theorem CG2 (phase extraction).** For every $c\in Z$,


```math

 K_\ell(c)=m_\ell\psi(\ell(c)),\qquad
 \kappa_\ell(c):=\frac{K_\ell(c)}{K_\ell(0)}
                    =\psi(\ell(c)).               \tag{CG2.2}

```


The denominator is always nonzero. The complete labeled family of these
phases determines $c$. In particular, characters in a basis of $Z^*$
already determine it.

These finite coefficients are obtained from actual original-Fock modular
current traces. With the notation and construction of GC3--GC5 in
[the colored-energy correlation section](bol-genus-one-correlations.md#colored-energy-correlations-and-their-modular-closure),
set


```math

 \mathcal H_e=|C|\mathbf1+\sum_{m\ge1}mE_e^{mm},\qquad
 \mathcal E_{c,e,\ell}(\tau)
  =q^n\operatorname{Tr}_{\mathcal F_{B,\ell}}
          \bigl(\Gamma_L(c)\mathcal H_eq^D\bigr).

```


Then


```math

 24K_\ell(c)=
 [q^{n+1}]\mathcal E_{c,e,\ell}
       -|C|[q^{n+1}]\Phi_{c,\ell}.                 \tag{CG2.3}

```


The functions $\mathcal E_{c,e,\ell}$ are modular forms of weight two,
holomorphic in the upper half-plane and possibly meromorphic at cusps;
for elementary $Z$ they have trivial multiplier on $\Gamma_0(2p)$.
The subtraction in (CG2.3) is an extraction from Fourier coefficients,
not a claim that subtracting weight zero from weight two preserves a weight.

**Canonical proof.** GC5 of the linked current-correlation manuscript proves
the finite base-fiber identity, positivity of $m_\ell$, character recovery,
and the coefficient interface (CG2.3). GC3 there proves the analytic law.
We retain the statement here as the interface to the finite-word
reconstruction below, rather than duplicating that proof.

All these objects transport under the strict source isomorphisms. In
particular the identity fiber maps to the identity fiber. Retaining it is
essential: averaging over all $G/Z$-fibers replaces an individual phase
by an average over conjugates, as in CF3.

## Actual translation words recover the bimap

Identify $W$ with the negative diagonal in $P/Z$. For $x\in W$,
choose any lift


```math

 t_x\in K\cap P,\qquad t_xZ=(x,-x)+Z.

```


Such lifts exist by CF1; $(x,-x,0)$ is one in the source coordinates.
They are actual distinguished translations, not independently adjoined
Heisenberg operators. Two choices differ by an element of $Z$.
Use the group convention $[u,v]=uvu^{-1}v^{-1}$.

**Theorem CG3 (alternating and transported reconstruction).** Define


```math

 c_0(x,y)=[t_x,t_y].

```


Then $c_0(x,y)\in Z$, it is independent of the chosen central lifts, and


```math

 c_0(x,y)=-b(x,y)+b(y,x).                           \tag{CG3.1}

```


The current coefficients in (CG2.3), indexed by $\ell,x,y$, determine
this entire alternating $Z$-valued commutator bimap. Equivalence of the
phase arrays under one pair of linear changes $W\to W'$, $Z\to Z'$
is exactly equivalence of the recovered alternating bimaps.

More generally, let $a$ be an actual pure-torus translation in $K$, and
write $R=R(a)$ for its retained action on the first canonical axis. Put


```math

 c_a(x,y)=[t_x,a t_y a^{-1}].

```


Then


```math

 c_a(x,y)=-b(x,R^{-1}y)+b(Ry,x),                    \tag{CG3.2}

```


and hence


```math

 c_a(x,y)-c_0(x,Ry)=b(x,(R-R^{-1})y).              \tag{CG3.3}

```


If $D_a=R-R^{-1}$ is invertible, the original bimap is recovered by


```math

 b(x,z)=c_a(x,D_a^{-1}z)
             -c_0(x,RD_a^{-1}z).                  \tag{CG3.4}

```


This recovers its symmetric part as well as its alternating part, given
the canonical axis labels and action $R$. No assumption $T(a)=1$ is
needed for these identities.

**Proof.** The subgroup $P$ has class at most two and $Z=Z(P)$. In
BCH coordinates, a group commutator of vector parts $u,v$ is
$\Omega(u,v)$, with the sign convention just specified. Substituting
$u=(x,-x)$, $v=(y,-y)$ in CF0.1 proves (CG3.1). Central changes of
the lifts cannot affect this commutator. By CG2, all its character
evaluations are recovered, so its value in $Z$ is recovered.

If the phase arrays transport by linear isomorphisms $L:W\to W'$ and
$M:Z\to Z'$, character separation gives
$c'_0(Lx,Ly)=M c_0(x,y)$ for every pair. The converse follows by
evaluating this equality at characters. This proves the equivalence statement.

The source normal action of $a$ on $P/Z$ is
$(u,v)\mapsto(Ru,R^{-1}v)$. Thus $a t_ya^{-1}$ has vector part
$(Ry,-R^{-1}y)$. Its possible central part again has no effect on
commutators in $P$. Substitution in $\Omega$ proves (CG3.2).
Subtracting (CG3.1) evaluated at $(x,Ry)$ cancels $b(Ry,x)$ and proves
(CG3.3). Substitution $y=D_a^{-1}z$ proves (CG3.4). QED.

The word $c_0$ has four translation factors; $c_a$ has at most eight,
including inverses. The inverse factors belong to $K$, by the canonical
inversion relation. Consequently these are finite words in the actual
sandwich action, to which the original-Fock correlation theorem applies.
The commutator words are central in $P$, even though their factors need
not commute.

The recovery is compact. Given bases of $W,Z$, bilinearity reduces the
needed phase evaluations to $O((\dim Z)(\dim W)^2)$ field entries; it
requires neither the loop table nor the induced set $X$. Recovery of
$c_0$ alone does not recover the original $b$, its symmetric part, or
the cocycle $f$. Formula (CG3.4) has its additional explicit hypothesis.
No completeness claim for an unlabelled multiset of these coefficients is made.

## Equal complete fusion data with inequivalent pairing geometry

The following is a class-two group control. It does not assert that either
datum is realized by the selected simple proper Bol construction.

Work over $\mathbb F_3$, take $Z=\mathbb F_3^2$, $W=\mathbb F_3^8$,
and let $C_1,C_2$ be the companion matrices of


```math

 f_1(t)=t^4+t+2,\qquad f_2(t)=t^4+t^2+2.

```


Explicitly,


```math

 C_1=\begin{pmatrix}
 0&0&0&1\\1&0&0&2\\0&1&0&0\\0&0&1&0
 \end{pmatrix},\qquad
 C_2=\begin{pmatrix}
 0&0&0&1\\1&0&0&0\\0&1&0&2\\0&0&1&0
 \end{pmatrix}.

```


Define the alternating bimap $\omega_i:W\times W\to Z$ by its scalar
forms at a character $(s,t)$:


```math

 (s,t)\omega_i\ \longleftrightarrow\
 A_i(s,t)=
 \begin{pmatrix}
 0&sI_4+tC_i\\-(sI_4+tC_i)^T&0
 \end{pmatrix}.                                   \tag{CG4.1}

```


Let $Q_i=W\times Z$ with group law


```math

 (x,z)(y,u)=(x+y,z+u+\omega_i(x,y)/2).

```


**Theorem CG4 (all fusion data agree; phase geometry does not).** The
groups $Q_1,Q_2$ have order $3^{10}$. Their central class $Z$-sets
are both isomorphic to


```math

 Z\ \sqcup\ (3^8-1)\{\text{fixed point}\}.           \tag{CG4.2}

```


In particular each has 6569 classes, and their entire pointwise
$Z$-Frobenius algebras are isomorphic. Every individual central permutation
trace and every higher-fusion image dimension agree. The character
dimensions are $3^8$ at zero and 1 at every nonzero character.

Nevertheless their alternating bimaps are inequivalent under
$\operatorname{GL}(W)\times\operatorname{GL}(Z)$, and the groups are
nonisomorphic. Their complete commutator-phase arrays, hence the modular
current coefficients extracting those arrays, cannot be equivalent under
these linear changes of labels.

**Proof.** First, both quartics are irreducible. Their values at $0,1,2$
are respectively $(2,1,2)$ and $(2,1,1)$, so they have no linear
factor. The three monic irreducible quadratics and the remainders are

| Quadratic divisor | Remainder of $f_1$ | Remainder of $f_2$ |
| --- | --- | --- |
| $t^2+1$ | $t$ | $2$ |
| $t^2+t+2$ | $t+1$ | $2t+2$ |
| $t^2+2t+2$ | $t+1$ | $t+2$ |

A reducible quartic without a linear factor must have an irreducible
quadratic factor. The table excludes this, proving irreducibility.
Consequently $sI+tC_i$ is invertible for every nonzero $(s,t)$.
Thus all nonzero scalar forms have rank eight and radical zero.

For $w\ne0$, the image $J_w=\omega_i(w,W)$ must equal $Z$:
otherwise a nonzero character annihilates that image, putting $w$
in the zero radical of its scalar form. For $w=0$, the image is zero.
The conjugacy classes over $w$ form $Z/J_w$, proving (CG4.2).
It follows at once that all the pointwise charge multiplications agree.
In the radical formula a tuple containing a nonzero character has image
dimension one; an all-zero tuple has image dimension $3^8$.

To distinguish the bimaps, consider their binary Pfaffian polynomials.
The block Pfaffian identity in size eight gives


```math

 \operatorname{Pf}A_i(s,t)=\det(sI+tC_i),

```


and therefore


```math

 F_1(s,t)=s^4+2st^3+2t^4,\qquad
 F_2(s,t)=s^4+s^2t^2+2t^4.                         \tag{CG4.3}

```


Under a change of basis of $W$, a Pfaffian is multiplied by the nonzero
determinant of that basis change. A change of basis of $Z$ makes an
invertible linear substitution in $s,t$. These Pfaffian rules are
integral polynomial identities, so they remain valid in characteristic
three; equivalently they follow from the perfect-matchings expansion.
No division by $4!$ in characteristic three is being used.

In characteristic three the vanishing of the $s^2t^2$ coefficient is
preserved by every invertible substitution. Indeed cubes have no mixed
terms, so the source monomials $s^4,s^3t,st^3,t^4$ contribute no
$s^2t^2$ term after substitution. For the remaining monomial,


```math

 [s^2t^2](\alpha s+\beta t)^2(\gamma s+\delta t)^2
 =\alpha^2\delta^2+\alpha\beta\gamma\delta+\beta^2\gamma^2
 =(\alpha\delta-\beta\gamma)^2.                   \tag{CG4.4}

```


Thus that coefficient is a relative invariant, multiplied by the square
of the variable-change determinant and by any overall Pfaffian scalar.
It is zero for $F_1$ and nonzero for $F_2$. No allowed changes can
identify the bimaps.

Their centers equal $Z$, because the common radical is zero. Their
derived subgroups equal $Z$, because a character killing every
commutator would give a zero scalar form. A group isomorphism would
therefore induce linear isomorphisms on $Z$ and $Q_i/Z=W$ preserving
commutators, contradicting the bimap obstruction. Finally CG3 identifies
equivalence of the complete phase arrays with bimap equivalence. QED.

For a concrete entry, write $W=\mathbb F_3^4\oplus\mathbb F_3^4$, with
bases $e_j$ and $f_j$. For


```math

 x=e_2+2e_3,\qquad y=f_4,\qquad \ell=(0,1),

```


the commutators have values $(0,2)$ and $(0,1)$, respectively.
Both are nonzero and have identical unprojected central cycle shapes.
Their normalized phases are $\zeta_3^2$ and $\zeta_3$.
This one entry illustrates the measurement; inequivalence of the whole
arrays is established by (CG4.3)--(CG4.4), not by fixing an arbitrary basis.

If an explicit induced representation is desired for these group controls,
take $G_i=Q_i$ and $X_i=Q_i\times_Z\operatorname{Conj}(Q_i)$.
The left actions are actual group translations and hence satisfy the Bol
sandwich relation. This uses the finite induction construction outside the
selected simple-loop interface; it is not a claimed realization of that
interface. Here $I=3^8$, the two induced dimensions agree, and (CG2.3)
applies. The displayed eight-by-eight matrices suffice for all computations.

## Conjugate cocycle operators separated by a current

The following supplies a correlation effect inside the inherited huge
proper Bol example, rather than only in the group controls.

**Proposition CG5 (a partition-blind distinction).** Suppose $c,c'\in Z$
are conjugate in $G$, with $c'=aca^{-1}$. Then, for every right charge
$\mu$, the entire zero-point functions agree:


```math

 \Phi_{c,\mu}=\Phi_{c',\mu}.                        \tag{CG5.1}

```


If $\ell(c)\ne\ell(c')$, the weight-two base-fiber current functions are
unequal, with


```math

 [q^{n+1}](\mathcal E_{c,e,\ell}-\mathcal E_{c',e,\ell})
      =24m_\ell\bigl(\psi(\ell(c))-\psi(\ell(c'))\bigr).
                                                               \tag{CG5.2}

```


**Proof.** The right charge projector commutes with $\Gamma_L(a)$ in
every degree. Conjugation by that operator identifies the two zero-point
traces, proving (CG5.1). Subtract (CG2.3) for $c,c'$; the partition
terms cancel. Apply (CG2.2), proving (CG5.2). QED.

The current is not conjugation invariant under all $G$: conjugating it
moves the identity-fiber idempotent to another fiber. This is exactly the
retained geometric information that permits (CG5.2). It is not a violation
of cyclic invariance of traces.

For the rigid-center example use


```math

 M=3^{36},\quad d=72,\quad
 Z=\mathbb F_3[\epsilon]/(\epsilon^3),\quad T(a)=1+\epsilon,
 \qquad f(a)=1-\epsilon+\epsilon^2.

```


All the source formulas, dependencies, and the stated properness and
simplicity remain those of
[the pinned input and its existing calculation](bol-translation-class-fusion.md#the-rigid-center-pair-exact-graded-seed-counts).
Take the live cocycle operators


```math

 c=f(a),\qquad c'=T(a)f(a)=1.

```


They are conjugate by the actual torus translation $a$. The intrinsic
phase conditions


```math

 \bigl(\ell(f(a)),\ell((T(a)-1)f(a)),
                    \ell((T(a)-1)^2f(a))\bigr)=(0,1,0)
                                                               \tag{CG5.3}

```


select $\ell=(1,1,0)$ in the basis $1,\epsilon,\epsilon^2$. The
three vectors used in (CG5.3) are a basis, so the selection is unique.
The existing rank calculation gives $r_\ell=36$, hence $m_\ell=M$.
Consequently


```math

 \Phi_{f(a),\mu}=\Phi_{T(a)f(a),\mu}
                     \quad\hbox{for every }\mu,

```


while


```math

 [q^{n+1}]
 \bigl(\mathcal E_{f(a),e,\ell}
           -\mathcal E_{T(a)f(a),e,\ell}\bigr)
       =24M(1-\zeta_3)\ne0.                       \tag{CG5.4}

```


Both current functions have weight two on $\Gamma_0(6)$, by the analytic
theorem cited in CG2. Their common normalization is the existing
$n=3I(M+2)^2$, $I=3^{146}19^6$. This comparison takes place inside
one marked loop. It is not a new claim that this particular pair of
operators distinguishes the loop from its principal isotope; the earlier
isotope obstruction remains separate.

## The huge input also exposes the hidden symmetric component

**Corollary CG6 (a transported phase absent from all local commutators).**
In the same rigid input let $d_0$ denote the torus generator called $d$
in the source, of order 19. Its action on $W=E^4$, $E=\mathbb F_{3^{18}}$,
is $R(d_0)=\lambda I$, where $\lambda$ has order 19.
Then $R(d_0)-R(d_0)^{-1}$ is invertible, so (CG3.4) recovers all of
the source bimap $b$ from current phases.

There is an explicit nontrivial phase in a charge annihilating every
untransported $Q$-commutator. Namely, put


```math

 x=2\lambda e_1,\qquad
 y=(\lambda-\lambda^{-1})^{-1}e_4,\qquad
 \ell_\epsilon=(0,1,0).

```


Then


```math

 \kappa_{\ell_\epsilon}(c_0(u,v))=1
                       \quad\hbox{for all }u,v,
 \qquad
 \kappa_{\ell_\epsilon}(c_{d_0}(x,y))=\zeta_3^2.    \tag{CG6.1}

```


**Proof.** An element of order 19 is neither 1 nor -1, so
$\lambda-\lambda^{-1}\ne0$. The source order
$\operatorname{ord}_{19}(3)=18$ makes the conjugates of $\lambda$
all the nonidentity nineteenth roots. Their sum is -1. Thus
$\operatorname{Tr}_{E/\mathbb F_3}(2\lambda)=1$.

The source entries in position $(1,4)$ of $B_0,B_1,B_2$ are
$0,2,1$. Hence its displayed trace-bimap formula gives


```math

 b(2\lambda e_1,e_4)=2\epsilon+\epsilon^2.

```


By (CG3.3),


```math

 c_{d_0}(x,y)-c_0(x,\lambda y)=2\epsilon+\epsilon^2.

```


Every $Q$-commutator belongs to $Z^+=\operatorname{span}(1,\epsilon^2)$,
which $\ell_\epsilon$ annihilates. Evaluating this last equality at
$\ell_\epsilon$ proves (CG6.1) by CG2. QED.

The charge $\ell_\epsilon$ can itself be specified from the live
cochain by the phase triple $(2,1,0)$, without selecting a center basis.
It has rank zero and $m_{\ell_\epsilon}=3^{72}$. Thus the measured
nontrivial phase is carried by an existing genuine charge sector.
All untransported commutator phases in this sector are trivial; transporting
a translation through the cross action reveals the part of $b$ that those
commutators and their class-fusion seed omit.

## Scope, novelty boundary, and next use

The finite action algebra, Fourier character separation, Pfaffian identities,
and induced-representation mechanisms are established algebra. The claimed
contribution is the extraction theorem for these canonically marked
Bol-current observables, its explicit equal-fusion controls, and its compact
proper-loop applications. No historical priority claim is inferred.

The analytic closure and transformation laws are those proved in the linked
correlation and kernel manuscripts. The algebraic coefficient formulas here
do not alone establish a VOA, a denominator identity, genus zero, or new
analytic laws peculiar to Bol loops. Conversely, the correlation information
is more than a list of independent fusion dimensions: it recovers actual
pairing values, and in CG5 separates operators whose entire charged
zero-point trace families coincide.

The remaining structural question is whether these marked correlation
relations constrain or recover further normal-form actions without retaining
their axis labels as input. CG3 recovers the full bimap when the displayed
cross-action invertibility holds; it does not assert an unconditional
classification of all Bol loops or of unlabelled scalar trace multisets.
