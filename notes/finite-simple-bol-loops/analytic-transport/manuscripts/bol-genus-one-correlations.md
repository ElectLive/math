# Mode correlations and a closed colored-energy system for the Bol object

**Mira Cult**

The input is the actual graded object and operators of
[the fermion construction](bol-fermion-sewing.md), with its inherited
elementary odd class-two and strict-transport hypotheses. The original
positive-integer modes are retained throughout this manuscript. No vertex
algebra, additional zero modes, or change of vacuum is used here.

There are two different outcomes. Finite collections of fixed-mode currents
have exact determinant formulas, but those formulas do not by themselves
give modularity. A specific infinite mode sum, the colored-energy current,
does give a closed genus-one system: its one-point functions are modular of
weight two, its finite higher correlations are quasimodular, and they have
an explicit almost-holomorphic modular completion. Their finite coefficients
retain central-word phases that fusion-image dimensions and charged
zero-point traces can miss.

## Conventions and the original trace

Let $X=G\times_Z C$, $B=\operatorname{Fun}(X,\mathbb C)$, and $n=|X|$.
The left $G$-action $L_g$ and commuting right $Z$-action $R_z$ are
those of [CF3](bol-translation-class-fusion.md#induction-to-the-canonical-bol-action).
All function actions are pullbacks by inverse point permutations. For
$a\in B$, write $M_a$ for pointwise multiplication and


```math

 t(a)=\operatorname{tr}_B M_a=\sum_{x\in X}a(x).

```


Our space, grading, and currents are exactly


```math

 \mathcal F_B=\Lambda\!\left(\bigoplus_{m\geq1}B[m]\otimes\mathbb C^{24}\right),
 \qquad
 E_a^{mn}=\sum_{x,j}a(x)c^\dagger_{xjm}c_{xjn}.
                                                               \tag{GC0.1}

```


The degree operator is $D$. If $s$ is a permutation of $X$,
$\Gamma(s)$ denotes its exterior lift. Put


```math

 Z_s(\tau)=\operatorname{Tr}_{\mathcal F_B}(\Gamma(s)q^D),
 \quad \Phi_s(\tau)=q^n Z_s(\tau),
 \quad q=e^{2\pi i\tau},\quad \operatorname{Im}\tau>0.
                                                               \tag{GC0.2}

```


For odd-order $s$, Theorem F-C gives


```math

 \Phi_s(\tau)=\prod_{O\in X/\langle s\rangle}H(d_O\tau),
 \qquad H(\tau)=\frac{\Delta(2\tau)}{\Delta(\tau)},\quad d_O=|O|.
                                                               \tag{GC0.3}

```


This function is nonzero on the upper half-plane. The normalized expectation
of an insertion is
$\langle A\rangle_s=\operatorname{Tr}(\Gamma(s)q^D A)/Z_s$.
All finite-mode insertions below have absolutely convergent traces there.

## Exact fixed-mode correlations

For a finite-support one-particle map $Y$ on
$\bigoplus_{m\geq1}B[m]$, let $\mathsf E(Y)$ be its second quantization,
summed over the 24 species. Thus $\mathsf E(M_a\otimes e_{mn})=E_a^{mn}$,
where $e_{mn}$ sends mode $n$ to mode $m$. In any finite set of modes
containing the support of all insertions, put


```math

 A=\bigoplus_m q^m s,\qquad C=A(1+A)^{-1},\qquad
 C_m=q^m s(1+q^m s)^{-1}.

```


**Theorem GC1 (finite determinant and Wick correlations).** Near
$t_1=\cdots=t_r=0$,


```math

 \left\langle e^{t_1\mathsf E(Y_1)}\cdots
                      e^{t_r\mathsf E(Y_r)}\right\rangle_s
   =\left\{
      \frac{\det(1+A e^{t_1Y_1}\cdots e^{t_rY_r})}{\det(1+A)}
     \right\}^{24}.                                \tag{GC1.1}

```


Unused modes cancel, so the finite determinant is independent of the chosen
finite support enlargement. In particular,


```math

 \begin{split}
 \langle\mathsf E(Y)\rangle_s&=24\operatorname{tr}(CY),\\
 \langle\mathsf E(Y)\mathsf E(V)\rangle_s
       -\langle\mathsf E(Y)\rangle_s\langle\mathsf E(V)\rangle_s
   &=24\operatorname{tr}(CY(1-C)V).
 \end{split}                                                   \tag{GC1.2}

```


For two mode currents the connected term is


```math

 24\delta_{nr}\delta_{sm}
       \operatorname{tr}_B(C_m M_a(1-C_n)M_b)

```


for the ordered pair $E_a^{mn},E_b^{rs}$.

**Proof.** On a finite exterior algebra,
$\operatorname{Tr}\Gamma(T)=\det(1+T)$, and
$e^{t\mathsf E(Y)}=\Gamma(e^{tY})$ for one species. The exterior functor
respects products. Apply these identities in the affected modes and multiply
the 24 identical species factors. The unaffected oscillator factors cancel.
Differentiating once proves the first formula. The mixed derivative of the
logarithm is
$24\operatorname{tr}(CYV-CYCV)$, proving the second. The mode Kronecker
deltas follow by multiplying the matrix units. The finite-order eigenvalues
of $s$ have modulus one and $|q|<1$, so all denominators are invertible.
The remaining oscillator products converge locally uniformly. QED.

For example the connected trace of $E_a^{mn},E_b^{nm}$ has expansion


```math

 24\sum_{r\geq1,\,u\geq0}(-1)^{r+u-1}q^{mr+nu}
                    \operatorname{tr}_B(s^rM_a s^uM_b),          \tag{GC1.3}

```


where its finite coefficients have the explicit orbit interpretation


```math

 \operatorname{tr}_B(s^rM_a s^uM_b)
    =\sum_{x:\,s^{r+u}x=x} b(x)a(s^u x).             \tag{GC1.4}

```


These are correlations of the actual marked functions and permutations,
not functions solely of the dimensions of fusion images. For fixed modes
the entries of $C_m$ are rational in $q$: if $s^h=1$, a finite
geometric sum in $q^m s$ computes the inverse. Rationality in $q$ is
not a modular transformation theorem. In particular, the fixed-mode
obstruction proved in
[the architecture analysis](bol-genus-one-architecture.md) applies to the
nonconstant occupation functions appearing even when $s=1$.

## Actual symmetry and thermal Ward identities

The following identities are operator identities on the original space:


```math

 \begin{split}
 \Gamma(s)E_a^{mn}\Gamma(s)^{-1}&=E_{s\cdot a}^{mn},\\
 q^D E_a^{mn}q^{-D}&=q^{m-n}E_a^{mn},\\
 [E_a^{mn},E_b^{rs}]&=\delta_{nr}E_{ab}^{ms}
                         -\delta_{sm}E_{ab}^{rn}.
 \end{split}                                                   \tag{GC2.1}

```


They follow respectively from permutation covariance, degree, and the CAR
proof already given in F-B. Cyclicity of the convergent trace therefore gives
the thermal identity


```math

 \langle E_a^{mn}V\rangle_s
       =q^{m-n}\langle V E_{s\cdot a}^{mn}\rangle_s             \tag{GC2.2}

```


for every finite current word $V$. This statement does not assert that
the individual functions are modular.

The sandwich relation and positive-cocycle identity remain the actual
relations


```math

 \mathcal T_x\mathcal T_y\mathcal T_x=\mathcal T_{x\cdot(y\cdot x)},
 \qquad
 \mathcal U_{ab}=\mathcal U_a\mathcal A_a\mathcal U_b\mathcal A_a^{-1},
                                                               \tag{GC2.3}

```


with the source markings of F-A and F13. Thus substituting either side in
any convergent trace gives an exact Ward equality. No multiplicative law
$\mathcal T_x\mathcal T_y=\mathcal T_{xy}$ is introduced.

## Colored-energy correlations and their modular closure

Define the actual degree-zero operator


```math

 \mathcal H_a=t(a)\,1+\sum_{m\geq1}m E_a^{mm}.        \tag{GC3.1}

```


Every vector of the algebraic Fock space involves finitely many occupied
modes, so this sum is a well-defined operator. Its trace with $|q|^D$
converges absolutely: its absolute eigenvalue is bounded by
$|t(a)|+\max_x|a(x)|D$, and the differentiated dimension series converges
for $|q|<1$. The vacuum term is prescribed by the existing normalization
$q^n$: at $a=1$ this is exactly $D+n$.

These currents are linear in $a$, commute with each other, and satisfy


```math

 \Gamma(s)\mathcal H_a\Gamma(s)^{-1}=\mathcal H_{s\cdot a},
 \qquad
 [\mathcal H_b,E_a^{mn}]=(m-n)E_{ab}^{mn}.          \tag{GC3.2}

```


The second identity follows by summing (GC2.1). It explicitly ties this
infinite-mode subsystem to the original mode-resolved multiplication law.

For an orbit $O$ of an odd permutation $s$, write
$A_O(a)=\sum_{x\in O}a(x)$ and $d_O=|O|$. Put


```math

 F(\sigma)=\frac{1}{2\pi i}\frac{d}{d\sigma}\log H(\sigma)
          =2E_2(2\sigma)-E_2(\sigma),
 \quad
 E_2(\sigma)=1-24\sum_{m\geq1}\frac{m e^{2\pi i m\sigma}}
                                         {1-e^{2\pi i m\sigma}}.
                                                               \tag{GC3.3}

```


Only the logarithmic derivative is used, so no choice of logarithm enters
the definition. The series equality follows directly by differentiating
the discriminant product.

**Theorem GC3 (modular one-current trace in the original object).** If
$s$ has odd order $h$, then


```math

 \mathcal E_{s,a}(\tau)
   :=q^n\operatorname{Tr}(\Gamma(s)\mathcal H_a q^D)
   =\Phi_s(\tau)\sum_{O}A_O(a)F(d_O\tau).            \tag{GC3.4}

```


This is holomorphic on the upper half-plane and is a weight-two weakly
holomorphic modular form with trivial multiplier on $\Gamma_0(2h)$,
with possible poles
only at cusps. The normalized expectation is the weight-two expression
$\sum_O A_O(a)F(d_O\tau)$.

**Proof.** GC1 gives
$\langle E_a^{mm}\rangle_s=24\operatorname{tr}(C_mM_a)$.
On a cycle of odd length $d$, only the powers $s^{dk}$ contribute
to this diagonal trace. Its contribution is
$A_O(a)q^{dm}/(1+q^{dm})$. Therefore


```math

 \langle\mathcal H_a\rangle_s
 =\sum_O A_O(a)
        \left(1+24\sum_{m\geq1}\frac{m q^{d_Om}}{1+q^{d_Om}}\right)
 =\sum_O A_O(a)F(d_O\tau).

```


The constant term in (GC3.1) is necessary for this formula. Since $H$ is
a nonvanishing weight-zero modular function on $\Gamma_0(2)$,
differentiating its transformation law proves that $F$ has weight two.
For $\gamma=\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)
\in\Gamma_0(2h)$ and $d\mid h$, the matrix
$\left(\begin{smallmatrix}a&bd\\c/d&e\end{smallmatrix}\right)$
lies in $\Gamma_0(2)$, and its automorphy factor at $d\tau$ is
$c\tau+e$. Each $F(d\tau)$ consequently has the same weight-two
law. Multiply by the invariant function $\Phi_s$. Cusp behavior follows
from the local discriminant products, or their logarithmic derivatives.
QED.

For $a=1$, the formula reduces to
$\mathcal E_{s,1}=(2\pi i)^{-1}\partial_\tau\Phi_s$.
For general $a$, its coefficients contain the cyclewise sums of the
specified seed function; it is not just an energy derivative of an
unmarked character.

**Theorem GC4 (all finite colored-energy correlations close).** For
$a_1,\ldots,a_r\in B$, define


```math

 \mathcal E_s(a_1,\ldots,a_r;\tau)
   =q^n\operatorname{Tr}\bigl(\Gamma(s)
                  \mathcal H_{a_1}\cdots\mathcal H_{a_r}q^D\bigr).

```


Its exact source function is, near $\mathbf t=0$,


```math

 q^n\operatorname{Tr}\left(\Gamma(s)
           e^{\sum_i t_i\mathcal H_{a_i}}q^D\right)
   =\prod_O H\left(d_O\tau+
                   \frac{\sum_i t_i A_O(a_i)}{2\pi i}\right).
                                                               \tag{GC4.1}

```


The connected normalized $r$-point function is


```math

 \kappa_s(a_1,\ldots,a_r;\tau)
  =\sum_O\left(\prod_i A_O(a_i)\right)
         \left[D_\sigma^{\,r}\log H(\sigma)\right]_{\sigma=d_O\tau},
 \qquad D_\sigma=(2\pi i)^{-1}\partial_\sigma.        \tag{GC4.2}

```


The normalized ordinary moment is the sum over set partitions


```math

 \frac{\mathcal E_s(a_1,\ldots,a_r)}{\Phi_s}
   =\sum_{\pi\text{ partition of }\{1,\ldots,r\}}
       \prod_{A\in\pi}\kappa_s((a_i)_{i\in A}).      \tag{GC4.3}

```


For $r\geq1$, both the normalized moment and the unnormalized trace are
quasimodular of weight $2r$ and depth at most $r-1$ on
$\Gamma_0(2h)$, allowing the cusp poles of $\Phi_s$ in the latter.
For each fixed maximum insertion order, this is a finite closed system
over the finite-dimensional color space $B$.

**Proof.** The operator exponent at mode $m$ is the exterior lift of
$\exp(m\sum_i t_i M_{a_i})$. The point multipliers commute. Around
an odd cycle $O$, the product of their weights is
$\exp(m\sum_i t_i A_O(a_i))$, so its exterior determinant is


```math

 1+q^{d_Om}\exp\left(m\sum_i t_i A_O(a_i)\right).

```


Taking 24 species and multiplying the vacuum factors
$q^n e^{\sum_i t_i t(a_i)}$ gives precisely (GC4.1). For the literal
operator trace choose a sufficiently small neighborhood of zero satisfying
$|q|\exp(\operatorname{Re}\sum_i t_i a_i(x))<1$ at every site $x$.
The oscillator singular values then give a convergent absolute trace
product. The right side continues holomorphically to the possibly larger
domain where all displayed shifted cycle parameters have positive imaginary
part. Only equality and convergence in the smaller neighborhood are needed
for differentiation. Taking
the logarithm and differentiating proves (GC4.2); differentiating its
exponential gives (GC4.3).

The first logarithmic derivative $F$ is modular of weight two.
Differentiating the modular transformation rule shows that each further
$D_\sigma$ raises the weight by two and raises the quasimodular depth
by at most one. Thus a connected block of size $j$ has weight $2j$
and depth at most $j-1$, also after evaluation at $d_O\tau$.
Every term in (GC4.3) has weight $2r$ and depth at most
$r-|\pi|\leq r-1$. Multiplication by $\Phi_s$ changes neither.
There are finitely many cycles and basis colors, and at bounded order only
finitely many products of the derivatives in (GC4.2). This proves the
specified finite-order closure. QED.

Here "quasimodular" means that the transformed function divided by
$(c\tau+e)^{2r}$ is a polynomial of degree at most $r-1$ in
$c/(c\tau+e)$, with holomorphic coefficient functions independent of
the particular group element. The proof derives this law; it does not
infer it from finitely many coefficients. The analytic building blocks
are the differential algebra generated by the finitely many
$F(d\tau)$, $d\mid h$, with the weight-zero factor $\Phi_s$.

### A canonical almost-holomorphic modular completion

Put $y=\operatorname{Im}\tau$ and use the weight-$k$ raising operator


```math

 \delta_{k,\sigma}=D_\sigma-\frac{k}{4\pi\operatorname{Im}\sigma}.

```


For a connected block of size $r$, replace its analytic derivative in
(GC4.2) by


```math

 \widehat F_r(\sigma)
 =\delta_{2r-2,\sigma}\cdots\delta_{4,\sigma}
                           \delta_{2,\sigma}F(\sigma),
 \qquad \widehat F_1=F.                             \tag{GC4.4}

```


Each raising step transforms covariantly from weight $k$ to weight
$k+2$. This follows directly by differentiating the weight-$k$ rule
and using $\operatorname{Im}(\gamma\sigma)
=\operatorname{Im}\sigma/|c\sigma+e|^2$; the derivative error is canceled
by the displayed $1/\operatorname{Im}\sigma$ term.

Consequently substituting $\widehat F_r$ in (GC4.2), and then in the
partition formula (GC4.3), gives an almost-holomorphic modular completion
of weight $2r$ with the original moment as its holomorphic part. It is
polynomial in $y^{-1}$. Crucially, at a cycle of length $d$ the
denominator is $\operatorname{Im}(d\tau)=d y$, not $y$.

For a concrete two-point identity, let $P_s a$ be the average of $a$
on each $s$-cycle, equivalently the finite averaging projection onto
$B^{\langle s\rangle}$. The completed connected two-point function is


```math

 \widehat\kappa_s(a,b)
   =\kappa_s(a,b)
      -\frac{1}{2\pi y}\kappa_s\bigl((P_s a)(P_s b)\bigr).
                                                               \tag{GC4.5}

```


Indeed the cycle sum of $(P_s a)(P_s b)$ is
$A_O(a)A_O(b)/d_O$, exactly the factor required by (GC4.4).
The completion of the ordinary two-point moment has the same correction,
since the product of the one-point terms is already modular. This is a
specific lower-order correction using the actual multiplication and
transport averages of seed functions.

### Interspersed translations and cocycle words

All words made from these energy currents and actual permutation lifts
reduce to the same closed system. Explicitly,


```math

 \begin{split}
 &\Gamma(g_0)\mathcal H_{a_1}\Gamma(g_1)\cdots
             \mathcal H_{a_r}\Gamma(g_r)\\
 &\qquad=\Gamma(g_0g_1\cdots g_r)
       \prod_{i=1}^r\mathcal H_{(g_i g_{i+1}\cdots g_r)^{-1}\cdot a_i}.
 \end{split}                                                   \tag{GC4.6}

```


This follows by repeatedly using
$\mathcal H_a\Gamma(g)=\Gamma(g)\mathcal H_{g^{-1}\cdot a}$.
The energy currents commute with one another, so no hidden ordering
correction remains. This applies to distinguished translations, their
inverses, the actual positive-cocycle operators, and the right central
permutations. Equations (GC2.3) therefore give exact equalities within the
closed correlation family, with transported colors when necessary.

The Bol and cocycle identities force these label and transport equalities.
The modular or quasimodular transformation law is supplied by the exterior
determinant and the weighted mode sum. No claim that Bol identities alone
force an arbitrary graded theory to be modular is made.

## Actual charge projection and the finite phase coefficient

Distinguish the two genuine projectors


```math

 p_\ell=\frac1{|Z|}\sum_{z\in Z}\chi_\ell(z)^{-1}R_z
       \quad\text{on }B,
 \qquad
 P_\ell^{\mathcal F}=\frac1{|Z|}\sum_{z\in Z}
              \chi_\ell(z)^{-1}\Gamma_R(z)
       \quad\text{on }\mathcal F_B.                 \tag{GC5.1}

```


The latter projects onto **total** Fock charge. It is not obtained by
taking the exterior algebra of the one-particle charge space, and it is
not $\Gamma(p_\ell)$.

For $a$ invariant under the right $Z$-action, $\mathcal H_a$
preserves every total-charge space. Define its actual charged trace by


```math

 \mathcal E_{g,a,\ell}(\tau)
 =q^n\operatorname{Tr}_{\mathcal F_{B,\ell}}
                     (\Gamma_L(g)\mathcal H_a q^D).

```


Projection gives the exact formula


```math

 \mathcal E_{g,a,\ell}
   =\frac1{|Z|}\sum_{z\in Z}\chi_\ell(z)^{-1}
                        \mathcal E_{L_gR_z,a}.       \tag{GC5.2}

```


It has weight two on the common group $\Gamma_0(2\exp G)$. For
$g\in Z$ and elementary $Z$ of exponent $p$, the sharper group
$\Gamma_0(2p)$ applies. For tuples of right-invariant colors the same
averaging gives the actual higher charged quasimodular correlations and
their completions. Projected traces are used directly;
division by a projected partition function, which could vanish, is not
needed. Coefficients of charged twined functions may be cyclotomic rather
than rational integers.

**Theorem GC5 (a modular correlation recovers the finite phase kernel).**
For any $g\in G$ and right-invariant $a$,


```math

 \begin{split}
 [q^{n+1}]\mathcal E_{g,a,\ell}
    &=24\operatorname{tr}_B(p_\ell L_gM_a)
        +24t(a)\operatorname{tr}_B(p_\ell L_g),\\
 [q^{n+1}]\Phi_{g,\ell}
    &=24\operatorname{tr}_B(p_\ell L_g).
 \end{split}                                                   \tag{GC5.3}

```


Let $e\in B$ be the indicator of the canonical base fiber $[1,C]$,
so $t(e)=|C|$. For every central word value $c\in Z$, the finite
kernel


```math

 K_\ell(c)=\operatorname{tr}_B(M_e p_\ell L_c)

```


is recovered from the weight-two and weight-zero modular traces by


```math

 \boxed{\displaystyle
 K_\ell(c)=\frac{[q^{n+1}]\mathcal E_{c,e,\ell}
                    -|C|[q^{n+1}]\Phi_{c,\ell}}{24}.}           \tag{GC5.4}

```


In the translation-class seed this is


```math

 K_\ell(c)=p^{d-r_\ell}\chi_\ell(c).              \tag{GC5.5}

```


Thus all these modular coefficients determine $c$ by finite character
separation, with its specified word label. They retain phases, not merely
the dimensions $p^{d-r_\ell}$.

**Proof.** The degree-one space is $B\otimes\mathbb C^{24}$.
There $\mathcal H_a=M_a+t(a)\,1$ and the total-charge projector is
$p_\ell\otimes1$. This proves (GC5.3) and (GC5.4). On the base fiber,
the left central action agrees with the right action. Hence it acts by
$\chi_\ell(c)$ on its charge-$\ell$ space, whose dimension is
$p^{d-r_\ell}$ by CF2. This proves (GC5.5). These dimensions are
positive for every character. Dividing by them recovers every
$\chi_\ell(c)$; characters of the finite elementary abelian group
separate its elements. QED.

There is also a raw fixed-mode version, which is not a modularity claim:


```math

 [q^m]\operatorname{Tr}_{\mathcal F_B}
       (\Gamma_L(c)E_e^{mm}P_\ell^{\mathcal F}q^D)=24K_\ell(c).
                                                               \tag{GC5.6}

```


The insertion annihilates every state with empty mode $m$. Its first
possible nonzero grade is $m$, where the state has exactly one particle
in that mode and no other particles. This proves the formula for every
positive $m$; there are no zero modes in the original space. Formula
(GC5.4) is the modular replacement obtained by the proved weighted sum.

The algebraic consequences for commutator words, including recovery of the
scalar alternating pairings and further normal-form bimap data, are proved
in [the correlation geometry](bol-correlation-geometry.md#fiber-current-phases-recover-central-words).
That manuscript owns the finite-word and construction-parameter arguments;
the coefficient-to-correlation interface is (GC5.4).

## A current sees what all charged zero-point traces miss

The following consequence uses the compact computation in
[the conjugate-cocycle example](bol-correlation-geometry.md#conjugate-cocycle-operators-separated-by-a-current).
Its proper simple-loop status retains the pinned source qualifications.

In the actual rigid-center example put $M=3^{36}$, and choose the two
central values


```math

 c=f(a),\qquad c'=T(a)f(a)=a c a^{-1}.

```


For every charge $\ell$, the right-charge projector commutes with
$\Gamma_L(a)$, so conjugation proves the identity of entire series


```math

 \Phi_{c,\ell}(\tau)=\Phi_{c',\ell}(\tau).          \tag{GC6.1}

```


Nevertheless the intrinsic phase condition
$(\ell(f(a)),\ell((T(a)-1)f(a)),\ell((T(a)-1)^2f(a)))=(0,1,0)$
selects the character $\ell=(1,1,0)$. Its local charge dimension is
$M$, and $\chi_\ell(c)=1$,
$\chi_\ell(c')=\zeta_3$. Therefore (GC5.4) gives


```math

 [q^{n+1}]\bigl(\mathcal E_{c,e,\ell}
                    -\mathcal E_{c',e,\ell}\bigr)
       =24M(1-\zeta_3)\ne0.                         \tag{GC6.2}

```


Both functions are actual weight-two current traces on $\Gamma_0(6)$.
The partition baseline cancels because of (GC6.1). This is a comparison of
two canonically marked word operators inside the same large loop, rather
than a claim that two conjugate group elements have different ordinary
characters. The base-fiber current provides the retained incidence data.
No large loop table or induced point set is enumerated.

## What the closure establishes and what remains open

The exact determinant formulas give all finite-mode correlations and their
thermal and sandwich Ward identities. The colored-energy source gives a
closed quasimodular system for every finite insertion order, with a canonical
almost-holomorphic modular completion. Interspersed loop translations and
positive-cocycle operators remain inside this system after the explicit
transport rule (GC4.6). Its finite coefficients determine marked central-word
phases, and the actual large-loop witness (GC6.2) is invisible to every
charged zero-point trace.

The transformation laws still come from free exterior oscillators and the
discriminant function. The coefficients are dictated by the loop's marked
finite action and multiplication data. This is a proved correlation mechanism
beyond fusion-image dimensions, not an assertion of a Bol-exclusive modular
law or of historical priority for free-fermion methods.

The full unsummed fixed-mode family does not inherit this conclusion; its
finite modular-closure obstruction is proved in the architecture manuscript.
A position-dependent geometric completion and its additional charged fermion
space are constructed separately in
[the genus-one kernel manuscript](bol-genus-one-kernel.md). Those additions
are not silently identified with the original $\mathcal F_B$.

What remains unresolved is whether Bol identities or their cocycle geometry
force further analytic restrictions beyond the explicit free-field closure
and the finite phase kernels proved here: for example a genuinely new
recursion, a denominator identity, or a classification consequence that
cannot already be expressed through the recovered marked bimap. No such
stronger assertion is needed for GC1--GC6.
