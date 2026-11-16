# Arithmetic lifts of the Bol section: exact orbit blocks and two-step mixing

**Mira Cult**

The results below concern a directly verified proper Bol law and its actual
section-averaging operator. No simplicity, classification, or G-loop conclusion
from the full folder construction is assumed.

## The integral Bol law and its averaging section

Let R be a commutative ring, let H be a subgroup of R^times, and let d>=1.
Write V=R^d x R^d and

```math
\gamma((x,y),(x',y'))=x\cdot y'-y\cdot x'.
```

On B_R=V x H x R define

```math
(u,a,s)*(v,b,h)=(u+av,\,ab,\,s+h-\gamma(u,v)).
\tag{1}
```

The two division problems solve successively in the H, V and R coordinates.
The identity is (0,1,0). Direct substitution proves the left Bol identity
X*(Y*(X*Z))=(X*(Y*X))*Z: its common vector coordinate is
(1+ab)u+a v+a^2 b w, and its common central coordinate is

```math
2s+h+j-(1+ab)\gamma(u,w)-a\gamma(v,w).
```

No parity restriction on |H| is needed. If H contains a!=1 and gamma(v,w)=1,
then X=(0,a,0),Y=(v,1,0),Z=(w,1,0) give central coordinates -a and -1 in
(XY)(ZX) and (X(YZ))X, so the loop is non-Moufang. In particular this verifies
the family directly over each ring and local field below. The law uses
polynomials with an invertible coordinate a, and is one common integral
model over Z, with underlying scheme A^(2d) x G_m x A^1.

Let X=R^d x {0}. The subset S=X x H x {0} is the associative semidirect
product R^d semidirect H. Its actual left translations on B_R are not a
multiplicative representation of S. When R is finite, average them using
uniform measures:

```math
(Af)(x,y,b,s)=\mathbb E_{\substack{a\in H\\u\in R^d}}
 f(u+ax,ay,ab,s-u\cdot y).
\tag{2}
```

Each translation is a permutation, so A is a Markov contraction on normalized
L^2(B_R). The invariant leaf label is

```math
r=b^{-1}y\in R^d.
```

In leaf coordinates (x,r,b,s), (2) becomes

```math
(Af)(x,r,b,s)=\mathbb E_{a,u}f(u+ax,r,ab,s-bu\cdot r).
\tag{3}
```

Every leaf has a uniform stationary distribution. All results below are
statements about this actual operator.

## Exact unit-orbit flip identity

Let R=O/pi^A, where O is a discrete valuation ring with finite odd residue
field of cardinality Q. Fix a primitive additive character psi_A of R, so the
pairing (xi,x)->psi_A(xi.x) identifies the additive dual of R^d with R^d.
Fix a central-character sector psi_A(nu s) and a leaf r. Put z=nu r.
Fourier transformation in x with convention

```math
\widehat F(\xi,b)=\mathbb E_x F(x,b)\psi_A(-\xi\cdot x)
```

turns (3) into

```math
(A_{\nu,r}\widehat F)(\xi,b)
=\frac1{|H|}\sum_{\substack{v\in H\\vz=\xi}}\widehat F(bz,v).
\tag{4}
```

Indeed, substituting x'=u+a x makes the u average equal to the indicator
xi=a b z; then put v=ab. All zero and nonunit cases remain in (4).

Define H_z={a in H:a z=z}, h=[H:H_z], and G_z=H/H_z. Formula (4) annihilates
frequencies xi outside H z and annihilates the component orthogonal to
H_z-invariant functions of b. Its range is exactly the h^2-dimensional
subspace with xi in H z and with dependence on b only through bH_z.
Identify this subspace with functions of (u,v) in G_z x G_z via
xi=u z and bH_z=v. The inherited measure gives identical constant weights
on the two quotient coordinates, so the transposition J:F(u,v)->F(v,u)
is unitary. Formula (4) is the exact identity

```math
A_{\nu,r}=\frac1h J,\qquad (JF)(u,v)=F(v,u).
\tag{5}
```

on this subspace and is zero on its orthogonal complement. The averaging
factor is |H_z|/|H|=1/h, including h=1.

Consequences:

* A_(nu,r) is self-adjoint.
* Its eigenvalues are +1/h with multiplicity h(h+1)/2, -1/h with
  multiplicity h(h-1)/2, and zero with the remaining multiplicity
  |R|^d |H|-h^2.
* A_(nu,r)^3=h^(-2) A_(nu,r).
* Its norm is exactly 1/h, with no dimension-dependent constant.
* Every exceptional scalar character is accounted for by its actual unit
  orbit. If z=0, h=1 and the operator is a rank-one orthogonal projection.

The sign multiplicities are the dimensions of symmetric and antisymmetric
matrices on G_z. This argument includes even |H| and scalar units with
nontrivial stabilizers; no assumption that distinct units have unit
difference is needed.

## Full-unit prime-power theorem and conductor strata

Now take H=R^times. Its size is

```math
M_A=(Q-1)Q^{A-1}.
```

For z!=0 let c>=1 be the least exponent such that pi^c z=0; equivalently
c=A-min_i v_pi(z_i), with valuations truncated at A. Then

```math
H_z=\{a:a\equiv1\pmod{\pi^c}\},\qquad h=M_c=(Q-1)Q^{c-1}.
\tag{6}
```

The implication follows from a coordinate of z with minimal valuation;
other coordinates impose no stronger condition. Thus the complete local
observable is

```math
\|A_{\nu,r}\|_{2\to2}=\frac1{(Q-1)Q^{c-1}}.
\tag{7}
```

when nu r has conductor exponent c; if nu r=0 the norm is one.

In particular, call r primitive if at least one coordinate is a unit.
For central charge nu of conductor c, every primitive leaf has exactly the
norm (7). This gives a conductor saving at every prime-power depth, with
constant one, simultaneously for every dimension d. On a fixed primitive
leaf the central charge zero contributes only the constant eigenfunction;
therefore, writing Pi_r for averaging over that whole leaf,

```math
\|A^n-\Pi_r\|_{2\to2}=(Q-1)^{-n},\qquad n\ge1.
\tag{8}
```

Equality is attained in a conductor-one character sector. Equation (8)
is uniform in depth A and dimension d, while (7) gives the sharper value
on every individual conductor.

For complete counts on a charge-nu sector over all leaves, put e=v_pi(nu),
with e=A when nu=0. The number of leaves with nu r=0 is J=Q^(ed).
For 1<=c<=A-e the number with conductor c is

```math
Y_c=Q^{(e+c)d}-Q^{(e+c-1)d}.
```

The sector dimension is M_A Q^(2Ad). Its eigenvalue-one multiplicity is J.
For each c>=1 its eigenvalues +/-1/M_c have multiplicities

```math
\frac{M_c(M_c+1)}2Y_c\qquad\text{and}\qquad
\frac{M_c(M_c-1)}2Y_c,
\tag{9}
```

respectively. All remaining eigenvalues are zero. Thus its total rank is
J+sum_c M_c^2 Y_c. The exceptional leaf fraction is Q^(-(A-e)d).

The full-unit family includes a direct arithmetic extension of the restricted
section in public construction 0025: over F_q use all scalar units in place
of its order-p subgroup, then use the same law over O/pi^A. The full-unit
loop need not have odd order or be simple. Its Bol identity is proved above;
those additional loop-theoretic properties are not used.

## Exact two-step total variation on primitive leaves

The following estimate applies for every A,d>=1 and every primitive r.
For any starting point z_0=(x_0,b_0,s_0) of that leaf, let U_r be its uniform
probability measure. Then

```math
\operatorname{TV}\!\left(P^2(z_0,\cdot),U_r\right)
=\frac{2Q}{Q^3-1}\left(1-Q^{-3A}\right).
\tag{10}
```

Here P is the Markov kernel (3) and TV is one half the L^1 distance. There
is no asymptotic error or hidden constant. At depth one (10) is 2/Q^2;
at all depths it is less than 2Q/(Q^3-1). In particular two steps mix every
point to within O(Q^(-2)), uniformly in both depth and dimension.

Proof. Conditional on the past, uniform a_i makes b_i=a_i b_(i-1)
uniform in H. For each chosen a_i, the bijection
u_i -> x_i=u_i+a_i x_(i-1) makes x_i uniform in R^d independently of b_i.
Thus the pairs (x_i,b_i) are independent uniform pairs across steps.
Substituting u_i=x_i-(b_i/b_(i-1))x_(i-1) in the central recurrence gives

```math
s_2=s_0+(b_2-b_0)(x_1\cdot r)-b_1((x_2-x_0)\cdot r).
\tag{11}
```

Since r is primitive, x->x.r is a surjective homomorphism R^d->R.
Consequently v=x_1.r and l=(x_2-x_0).r are independent uniform residues.
Conditional on the final x_2,b_2, put

```math
j=v_\pi(b_2-b_0),\qquad h=v_\pi(l),
```

with both valuations truncated at A. The first random term in (11) is
uniform on pi^j R. The second is uniform on the valuation-h sphere when
h<A (and zero when h=A). These are independent. If h>=j their sum is
uniform on pi^j R. If h<j, addition of pi^j R preserves the uniform
valuation-h sphere. Thus its conditional TV distance from uniform R is
one minus the corresponding support fraction.

For uniform l, the probability of h>=j is Q^(-j), and the probability of
h=t<j is (Q-1)Q^(-t-1). Averaging the squared support fractions gives

```math
\mathbb E_l[\operatorname{TV}\mid j]
=\frac2{Q+1}(1-Q^{-2j}).
\tag{12}
```

Since b_2 is a uniform unit and b_0 is a fixed unit, the exact distribution
of j is

```math
\Pr(j=0)=\frac{Q-2}{Q-1},\qquad
\Pr(j=t)=Q^{-t}\quad(1\le t<A),\qquad
\Pr(j=A)=\frac1{(Q-1)Q^{A-1}}.
```

The final (x_2,b_2) already have their stationary joint distribution, so
full TV is exactly the average conditional TV, not merely bounded by it.
Substitution in (12) and summation of geometric series give (10).
The proof also covers j=A (zero difference), h=A (zero l) and d=1.

The estimate is specific to primitive leaves. On a nonprimitive leaf,
central increments lie in the ideal generated by r; its invariant cosets
must first be retained rather than claiming mixing to uniform central R.

## Reduction maps, compact local realization, and measures

Let K be a nonarchimedean local field of odd residue characteristic, O its
valuation ring and Q its residue size. Fix psi:K->C^times of conductor O
and self-dual Haar measure with vol(O)=1. Then
psi_A(s)=psi(pi^(-A)s) is a primitive character of R_A=O/pi^A.

Reduction B_(A+1)->B_A, including unit coordinates, is a loop homomorphism.
Uniform section measure pushes forward to uniform section measure. Pullback
i_A is an isometry of normalized L^2 spaces satisfying

```math
A_{A+1}i_A=i_A A_A.
\tag{13}
```

Central and x Fourier parameters transform as nu->pi nu and xi->pi xi.
Their conductor, the unit orbit, and the block scalar 1/M_c are therefore
unchanged under this embedding. These are explicit compatibility maps,
not an inferred Euler product.

The inverse limit is the compact analytic Bol loop

```math
B_{\mathcal O}=\mathcal O^{2d}\times\mathcal O^\times\times\mathcal O,
```

with the same polynomial law (1). Give O its probability Haar measure and
O^times its probability multiplicative Haar measure. Actual left translations
preserve their product: scalar units have absolute value one and the
coordinate maps are triangular. Average the compact section
O^d x {0} x O^times x {0}. On a leaf r, Fourier x parameters lie in
(K/O)^d and central parameters lie in K/O. A charge alpha of conductor c
and a primitive r have unit orbit of size M_c, stabilizer 1+pi^c O, and
the same finite matrix-transposition block as (5); the remaining b modes
are killed by conditional expectation onto that stabilizer.

Consequently on every primitive compact leaf,

```math
\operatorname{spec}(A)=\{1,0\}\cup\{\pm M_c^{-1}:c\ge1\},
\qquad \|A^n-\Pi_r\|_{2\to2}=(Q-1)^{-n}.
\tag{14}
```

Here Pi_r projects onto constants on that leaf. Both signs occur at every
conductor (Q odd implies M_c>=2). Formula (13), density of locally constant
functions, or directly (4) proves the local limit. For a nonprimitive
r of valuation t the correct fixed space includes central characters
annihilating pi^t O; this is exactly the orbit-one part of (5).

The point-start estimate also has an exact compact limit:

```math
\operatorname{TV}\!\left(P^2(z_0,\cdot),\operatorname{Haar}_r\right)
=\frac{2Q}{Q^3-1}.
\tag{15}
```

on a primitive leaf. The proof of (10) applies directly, now summing
j=1,2,...; the exceptional equality b_2=b_0 has Haar probability zero.
Equivalently the finite quotient TV distances increase to (15).

## Compactness, exact spectral zeta function, and a sharp Schatten threshold

Fix a primitive compact leaf r. Let Pi be its constant projection and set
T=A-Pi. The central coordinate O has Pontryagin dual K/O. There are exactly
Q^c-Q^(c-1)=M_c additive characters of exact conductor c. On each such
character sector, the complete Fourier analysis (4)-(5) leaves precisely
M_c^2 nonzero modes, all with singular value 1/M_c. Every other mode is
annihilated. On central charge zero, A is exactly Pi.

This accounts for the whole Hilbert space: Fourier transformation in x and s
is unitary; for each central character, Fourier parameters outside the one
finite unit orbit are killed; conditional expectation onto the corresponding
open unit stabilizer is orthogonal; and the remaining quotient block is the
finite transposition matrix. Locally constant cylinder functions form a dense
subspace, equivalently the finite quotients in (13). No extra continuous or
unaccounted nonzero spectrum remains.

Because M_c tends to infinity and each conductor contributes only finitely
many modes, T is compact. Its exact singular-value multiplicity is M_c^3 at
1/M_c. Consequently

```math
\operatorname{Tr}|T|^s
=\sum_{c\ge1}M_c^{3-s}
=\frac{(Q-1)^{3-s}}{1-Q^{3-s}},\qquad \Re s>3.
\tag{16}
```

For real s>0, T belongs to the Schatten class S^s if and only if s>3.
It belongs to weak S^3, but not S^3 and in particular not Hilbert-Schmidt.
The exact counting function at its singular values is

```math
\#\{\text{singular values}\ge M_C^{-1}\}
=(Q-1)^3\frac{Q^{3C}-1}{Q^3-1},\qquad C\ge1.
\tag{17}
```

Thus its weak-S^3 quasi-norm, with convention sup_n n^(1/3)s_n(T), is
(Q^3/(Q^3-1))^(1/3). The expression in (16) also gives a meromorphic
continuation of this operator's spectral zeta function; it has a simple
pole at s=3 with residue 1/log(Q). This spectral zeta function is not a
number-theoretic L-function, and no arithmetic Euler product is asserted.

At finite depth A the sum in (16) stops at c=A. As a useful quantitative
check and an additional mixing consequence, the two-step density satisfies

```math
\chi^2\!\left(P^2(z_0,\cdot),U_r\right)
=\frac{Q}{(Q-1)^2}(1-Q^{-A})
=\operatorname{Tr}|A-\Pi|^4.
\tag{18}
```

Indeed, conditional on j in the proof of (10), the average reciprocal
support fraction is j+1: the ideal case contributes one and each of the j
possible lower-valuation spheres contributes one. Thus conditional chi^2
averages to j. Finally E(j)=sum_(t=1)^A P(j>=t)=sum_(t=1)^A 1/M_t,
which is (18). In the compact limit the exact value is Q/(Q-1)^2.

This separates the all-unit arithmetic lift from a fixed Teichmuller
subgroup of order m. On a primitive compact leaf the fixed-order operator
has singular value 1/m in every nonzero central sector, hence infinitely
often; after removing its constant projection it is not compact. Full unit
averaging produces increasing orbit sizes with conductor and therefore the
compactness and sharp exponent three in (16).

## Thin local unit groups: exact rank versus smoothing law

The orbit identity does not require full-unit averaging. Let H be any closed
subgroup of O^times, with probability Haar measure, and average the compact
section O^d x {0} x H x {0}. The compact loop now has unit coordinate in H.
For a primitive leaf r and a central character of conductor c, its orbit
has size

```math
h_c=\left|\operatorname{im}\bigl(H\to(\mathcal O/\pi^c)^\times\bigr)\right|.
```

The surviving block is again h_c^(-1) times transposition, with total rank
h_c^2. There are M_c=(Q-1)Q^(c-1) central characters at that conductor.
Writing Pi for the constant projection, the complete nonzero singular
spectrum of T_H=A_H-Pi therefore satisfies, wherever the sum converges,

```math
\operatorname{Tr}|T_H|^s=\sum_{c\ge1}M_c h_c^{2-s}.
\tag{19}
```

It is compact if and only if H is infinite. Indeed h_c is nondecreasing;
if bounded, the decreasing congruence kernels stabilize and their
intersection is the identity, so H is finite. If unbounded, h_c tends to
infinity and each conductor contributes only finitely many modes. The
finite-group case has a fixed nonzero singular value infinitely often.
When H is infinite, h_c=1 can occur only at finitely many small conductors;
these sectors give additional fixed vectors. This finiteness statement does
not apply to the trivial group H={1}, for which h_c=1 at every conductor.
No mixing-to-Pi assertion is made when these additional fixed sectors are
present. The family below avoids them by containing all residue-field units.

Take an unramified extension $`K/\mathbb Q_p`$ of degree $`f`$, with
$`p`$ odd and $`Q=p^f`$. Choose a rank-$`\kappa`$ direct
$`\mathbb Z_p`$-summand $`\Lambda\subset\mathcal O`$, where
$`1\le\kappa\le f`$, and define

```math
H_\kappa=\mu_{Q-1}\exp(p\Lambda)\le\mathcal O^\times.
\tag{20}
```

Here $`\kappa`$ denotes the lattice rank; $`r`$ continues to denote the
primitive leaf label. These are closed scalar subgroups. The $`p`$-adic
exponential and logarithm are inverse isometric group isomorphisms
$`p\mathcal O\leftrightarrow1+p\mathcal O`$, with respect to the additive
and multiplicative laws. To verify precisely the assertion used here, write
their convergent power series: for $`x\in p\mathcal O`$, every term after
$`x`$ in $`\exp(x)-1`$ or $`\log(1+x)`$ has strictly larger $`p`$-adic
valuation when $`p`$ is odd. The formal inverse and exponential addition
identities hold by convergence. This proves the isometry and group identity;
hence $`\exp(p\Lambda)`$ is a closed subgroup. The direct-summand condition gives

```math
\Lambda\cap p^{c-1}\mathcal O=p^{c-1}\Lambda,
```

so

```math
\left|\operatorname{im}\bigl(\exp(p\Lambda)\bmod p^c\bigr)\right|
=p^{\kappa(c-1)},
\qquad
h_c=(Q-1)p^{\kappa(c-1)}.
\tag{21}
```

The Teichmuller and principal-unit factors intersect trivially and their
orders multiply. This proves (21) at every $`c\ge1`$, including $`c=1`$.

Substitution in (19) gives the exact spectral zeta function

```math
\operatorname{Tr}|A_{H_\kappa}-\Pi|^s
=
\frac{(Q-1)^{3-s}}{1-p^{\,f+\kappa(2-s)}},
\qquad
\Re s>D,
\qquad
D=2+\frac f\kappa.
\tag{22}
```

Consequently the centered averaging operator is compact, lies in $`S^s`$
exactly for real $`s>D`$, and lies in weak $`S^D`$ but not $`S^D`$.
The critical exponent depends on the rank $`\kappa`$ of the local unit
group, not on horizontal dimension $`d`$. Meanwhile the mixing norm is
unchanged for every $`1\le\kappa\le f`$:

```math
\|A_{H_\kappa}^{\,n}-\Pi\|_{2\to2}=(Q-1)^{-n},
\qquad n\ge1.
\tag{23}
```

This follows from $`h_1=Q-1`$ and strict growth thereafter. At conductor
$`c`$, the exact norm is $`((Q-1)p^{\kappa(c-1)})^{-1}`$.

For completeness, the exact singular-value count through conductor $`C`$ is

```math
N_C=(Q-1)^3\frac{p^{(f+2\kappa)C}-1}{p^{f+2\kappa}-1}.
\tag{24}
```

At that point the singular value is
$`((Q-1)p^{\kappa(C-1)})^{-1}`$, and $`\kappa D=f+2\kappa`$.
Thus (24) proves the weak endpoint directly, while at $`s=D`$ every
conductor contributes the same nonzero constant to (22), proving failure
of strong $`S^D`$.

There is a concrete smoothing consequence. Put
$`T=A_{H_\kappa}-\Pi`$. Since $`A_{H_\kappa}\Pi=\Pi`$,
$`T^n=A_{H_\kappa}^{\,n}-\Pi`$; self-adjointness makes the singular
values of $`T^n`$ the $`n`$-th powers of those of $`T`$. For every
positive integer $`n`$,

```math
T^n\in S^2\quad\Longleftrightarrow\quad 2n>D,
\qquad
T^n\in S^1\quad\Longleftrightarrow\quad n>D.
\tag{25}
```

Whenever $`2n>D`$, its exact squared Hilbert--Schmidt norm is

```math
\|T^n\|_{S^2}^2
=\frac{(Q-1)^{3-2n}}{1-p^{\,f+\kappa(2-2n)}}.
\tag{26}
```

On the normalized Haar probability space of a primitive leaf,
Hilbert--Schmidt operators are exactly operators with an $`L^2`$ integral
kernel. The constant projection has the kernel one, so the least number of
steps for $`A_{H_\kappa}^{\,n}`$ to have an $`L^2`$ kernel is
$`\lfloor D/2\rfloor+1`$. The least number for trace class is
$`\lfloor D\rfloor+1`$. Equality at either threshold fails. For example,
in an unramified quadratic extension, full units give an $`L^2`$ kernel
after two steps, whereas a rank-one principal-unit direction first gives
one after three steps, despite the same spectral gap (23).

The finite quotient images $`H_{\kappa,A}`$ reduce onto each other, so the
exact operator intertwinings (13) and the same additive-character convention
hold for this thinner arithmetic family. For $`\kappa=f`$, the direct
summand is $`\mathcal O`$ and $`H_\kappa=\mathcal O^\times`$, recovering
the sharp exponent three in (16). The rank-zero endpoint is the finite
Teichmuller group and is noncompact. For example, over an unramified
quadratic extension, full units give threshold three, while a rank-one
principal-unit direction gives threshold four, despite the same exact
spectral gap in (23).

The two-step TV formulas (10) and (15) were proved for **full unit averaging**
and are not asserted for $`H_\kappa`$ with $`\kappa<f`$. The rank-sensitive
spectral conclusion is a distinct consequence of the same verified orbit
identity.

## Fixed-order and other scalar subgroups

For any m>1 dividing Q-1, choose a Teichmuller eta of order m and take
H=<eta> in all finite quotients and in O^times. Every nonzero z in the
finite additive dual has trivial stabilizer in H, because eta^t-1 is a unit
for nonzero t. Thus, for each fixed nonexceptional central-character/leaf
sector (nu,r) with nu r!=0, h=m and the exact norm is 1/m. In that sector
the eigenvalues +1/m and -1/m have multiplicities m(m+1)/2 and m(m-1)/2,
respectively. These are not multiplicities summed over all central charges
on a leaf. This includes even m; the transposition proof has no parity
exception. Choosing p=3,q=7 in the original restricted section gives
eta=2 mod7,30 mod49,324 mod343 at the first three depths.

More generally (4)-(5) apply to ANY scalar subgroup H, including principal
units and ramified roots of unity: the sole change is the orbit size h.
An orbit of size one is a genuine exceptional projection and must never
be included in a strict uniform-cancellation claim. This is a precise
rank/character stratification, rather than an assertion that a common
zero radical rules out all scalar degeneracy.

## Contribution and limits

The strongest additional arithmetic range is the thin-unit theorem (20)-(24):
it gives the exact threshold $`D=2+f/\kappa`$, all conductor-dependent
singular values and multiplicities, and a spectral gap independent of
$`\kappa`$. For $`\kappa<f`$, the averaging subgroup has measure zero
inside $`\mathcal O^\times`$; its probability measure is its own Haar
measure. The positive-measure compression argument for full-unit averaging
does not directly supply this range.

The applicable full-unit baseline must be retained. Nica, *Unimodular graphs
and Eisenstein sums*, [arXiv:1505.05034v2](https://arxiv.org/abs/1505.05034v2),
Theorem 1.8 and its Section 6 proof, gives the projective incidence spectrum
over finite valuation rings. The precise slab identification and comparison
are recorded in [the controls and literature audit](bol-section-controls.md),
Section 7. Passing that known conductor spectrum through the compatible
projective inverse system and compressing to the full-unit slab already
implies an $`S^s`$ upper bound for $`s>3`$. This is an inference from
Nica's theorem, not a statement attributed verbatim to it. Thus the full-unit
upper threshold three is not claimed as an unprecedented regularization
phenomenon. The exact slab multiplicities, failure at the endpoint, and the
thin-unit rank formula are established here by the explicit orbit identity.
The literature search documented in the controls is bounded and does not
establish historical priority for those consequences.

The direct Bol construction supplies a specific averaging operator and its
section correction phase. The joint nontrivial orbit block is exactly
$`h^{-1}`$ times transposition, whereas individual unit slices have norm
one. Equality proves sharp parameter dependence for this observable. On an
associative group, averaging an actual subgroup in a unitary representation
is an orthogonal projection; the associative subloop $`S`$ acting on this
nonassociative ambient loop instead gives the blocks (5). Erasing the phase
$`s-u\cdot y`$ makes the subgroup average a projection. As the controls
also show, the resulting analytic operators admit ordinary incidence-graph
and group realizations; their spectrum is not exclusive to Bol loops, and
no new representation theory is asserted.

These results do not construct a cubic metaplectic cover, a global
automorphic form, or a new zero-free region. The full alternating-form
simple folder in manuscript 0025 has additional reciprocal $`p,q`$ action
and graph data. Its naive fixed-rank faithful prime-power lift is obstructed
by bounded prime-to-residue-characteristic torsion in a fixed local field.
The proper-section model above supplies a different arithmetic lift, with
all compatibility maps and measures explicit, without asserting those
full-folder properties.

