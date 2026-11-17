# From Bol mode currents to genus-one fields: an obstruction and the required completion

**Mira Cult**

Construction and architectural analysis by model participant 2 for
the owned continuation of PR #438. Manuscript-local labels GA1--GA3 allocate
no permanent claim IDs. These arguments are proposed for independent review;
they do not change earlier source or review pins.

The input is the marked finite Frobenius algebra and actual Bol action in
[the translation-class construction](bol-translation-class-fusion.md), together
with the positive-integer-mode exterior space and currents in
[the fermion construction](bol-fermion-sewing.md). Their inherited elementary
class-two and strict-isomorphism hypotheses remain in force when the input
comes from the selected simple loops. The obstruction below itself needs only
a nonempty finite set. It is not a classification theorem about Bol loops.

## 1. The question and the competing architectures

Let B=Fun(X), n=dim B>0, H=B tensor C^24, and

    F_B=exterior( direct_sum_(m>=1) H[m] ).

Write D for the positive integer energy grading, and let

    E_a^(m,r)=sum_(x,j) a(x) c^*_(x,j,m)c_(x,j,r).

The exact definitions and the Bol, cocycle and CAR identities are owned by
the linked manuscripts. The present question is whether their ordinary traces
already form a closed finite genus-one modular system, or whether one must
change the analytic observables or complete the state space.

The first serious tests distinguish the following routes.

| Architecture | What its first mathematical step gives | Remaining boundary |
| --- | --- | --- |
| Keep individual positive mode currents | Exact finite-dimensional Gaussian determinant and Wick identities | GA1--GA2 prove that even one occupation trace has infinite modular orbit |
| Sum energy-weighted diagonal modes | Modular current responses, and derivative/quasimodular relations | Such summation changes the observable; the ordinary energy response alone is determined by the partition function |
| Complete charged fermions and retain spin/holonomy sectors | Bilateral elliptic kernels and determinant correlation functions | Add dual modes and zero modes; specify temporal signs and all sectors needed by modular transformations |
| Construct the flat-bundle kernel directly | A finite family of meromorphic kernels with a proved modular law | A geometric kernel is not automatically a trace on the original exterior space |
| Bosonize a completed complex fermion system | A lattice presentation of the same analytic mechanism | This does not remove the completion or supply a new Bol-specific identity |

The strongest route is to combine the exact current calculation with a stated
charged completion and the flat-bundle kernel. The canonical kernel proof is
owned by [the genus-one kernel manuscript](bol-genus-one-kernel.md). It must
retain the actual multiplication operators, distinguished translations and
positive cocycle, rather than replace them by their dimensions. The negative
result in the next section explains why a mere finite list of additional raw
mode traces cannot accomplish this.

## 2. A fixed-mode obstruction on every finite-index modular group

For m>=1 put q=exp(2 pi i tau) and

    f_m(tau)=q^m/(1+q^m),                 Im(tau)>0.       (GA1.1)

For k an integer use the usual weight-k slash action

    (f|_k gamma)(tau)=(c tau+d)^(-k) f((a tau+b)/(c tau+d))

for gamma=(a b; c d) in SL_2(Z). A finite closed system here means a finite
dimensional complex vector space of functions stable under this action. This
allows arbitrary additional components and arbitrary finite-dimensional
representations; it is not restricted to the span of the originally proposed
traces. Multiplying each slash operator by a nonzero scalar multiplier does
not change the conclusion.

**Theorem GA1 (infinite orbit of one occupation trace).** For every m>=1,
every integer k, and every finite-index subgroup Gamma of SL_2(Z), the span
of {f_m|_k gamma : gamma in Gamma} is infinite dimensional. In particular f_m
cannot be a component of a finite-dimensional vector-valued modular system of
fixed weight k on Gamma. No cusp-growth or finite-image hypothesis is needed.

**Proof.** Set T=(1 1;0 1) and U=(1 0;1 1). Since Gamma has finite index,
some common positive power T^N and U^N belongs to Gamma. For every integer
j>=0, take

    gamma_j=U^N T^(Nj)=(1 Nj; N N^2 j+1).

Its unique preimage of infinity is

    t_j=-(N^2 j+1)/N=-Nj-1/N.                         (GA1.2)

The meromorphic function w -> exp(2 pi i m w)/(1+exp(2 pi i m w)) has
simple poles at

    w_r=(2r+1)/(2m),                 r in Z.

Consequently f_m(gamma_j tau) has infinitely many distinct simple poles
tau_(j,r)=gamma_j^(-1) w_r tending to t_j as |r| tends to infinity. At
most one w_r has inverse image infinity and may be omitted. The slash
factor is nonzero and finite at every remaining pole, because its only
zero or pole can occur at t_j. Thus these poles persist in f_m|_k gamma_j.

Consider a finite linear relation between these functions, and choose one
of its indices j. For every other index i, the function f_m|_k gamma_i is
meromorphic in a neighborhood of t_j, since t_i is different from t_j.
Choose a small punctured disk about t_j in which none of those finitely
many other terms has a pole. There are still infinitely many poles
tau_(j,r) of the j-th term in that disk. Near any one of them the asserted
identity, initially valid in the upper half-plane, continues meromorphically
by the identity theorem. Its j-th coefficient must be zero, because the
other terms are holomorphic there. Applying this to every index proves
linear independence. QED.

**Rational-trace extension.** The same conclusion holds for every nonconstant
rational function R(q), in place of q^m/(1+q^m), with meromorphic functions
allowed when R has poles in the unit disk.

**Proof.** Use the same matrices gamma_j and distinct points t_j. If R has
a pole zeta in C excluding zero, choose a logarithm w_0 with
exp(2 pi i w_0)=zeta. The inverse images gamma_j^(-1)(w_0+r), r in Z,
give infinitely many poles accumulating at t_j. The other terms are
meromorphic there, as in the preceding argument.

If R has no pole away from zero and infinity, it is a Laurent polynomial.
Since it is nonconstant, R(exp(2 pi i gamma_j tau)) has an essential
singularity at t_j. To see this directly, write gamma_j tau as a constant
plus a nonzero multiple of 1/(tau-t_j). Along a suitable ray approaching
t_j, the largest positive Laurent exponent grows exponentially faster than
every power and dominates the remaining terms. If there is no positive
exponent, use the most negative exponent and the opposite ray. A function
meromorphic at t_j cannot have this growth. A finite-order slash factor
does not remove an essential singularity.

For a proposed finite relation, all its terms are meromorphic on the complex
plane minus their finitely many t_j. The identity theorem extends the
relation from the upper half-plane to that connected domain. A nonzero
coefficient would express its term as a sum of functions meromorphic at its
own t_j. The accumulating poles, or the essential singularity in the Laurent
case, make this impossible. QED.

This argument identifies the obstruction, not just its growth rate. A modular
transformation moves the infinite string of occupation-denominator poles to
a new rational boundary accumulation point. These distinct points may lie
in the same Gamma-cusp class; the proof does not assert infinitely many
inequivalent modular cusps. Finitely many scalar components cannot absorb
the resulting independent functions.

### Application to the actual Bol currents

Let N_m=E_1^(m,m). There are 24n independent occupation choices at mode m.
Factoring the exterior trace one mode at a time gives

    Tr_F(N_m q^D)/Tr_F(q^D)=24n f_m(tau).             (GA2.1)

Indeed one occupied one-dimensional oscillator contributes q^m, whereas
its partition factor is 1+q^m. Summing over the 24n choices proves the
formula. It is an identity of convergent traces for |q|<1.

The previously established partition normalization is

    Phi(tau)=q^n Tr_F(q^D)=H(tau)^n,
    H(tau)=Delta(2 tau)/Delta(tau).

Here H is nonvanishing in the upper half-plane and is a weight-zero modular
function with trivial multiplier on Gamma_0(2).

**Corollary GA2.** Neither the normalized occupation expectation (GA2.1)
nor its partition-weighted version

    q^n Tr_F(N_m q^D)=24n Phi(tau) f_m(tau)           (GA2.2)

belongs to a finite-dimensional modular system of any fixed integer weight
on any finite-index subgroup of SL_2(Z).

**Proof.** The first assertion is GA1. For the second, intersect the proposed
group with Gamma_0(2). On this finite-index subgroup the slash orbit of
Phi f_m is Phi times the corresponding slash orbit of f_m. Multiplication
by the nonzero function Phi is injective, so GA1 again applies. QED.

This current is present for every nonempty seed and is invariant under all
its permutations. Therefore imposing the sandwich relation or the positive
cocycle relations does not remove it. Those relations cannot make the entire
collection of unchanged individual-mode traces into a finite modular system.
The conclusion concerns this architecture and fixed-weight modular closure.
It does not exclude resummed fields, Jacobi variables, an infinite-dimensional
system, or a different graded theory.

## 3. A positive test: resumming modes changes the answer

The ordinary energy operator is

    D=sum_(m>=1) m N_m.

Its vacuum-shifted response satisfies

    q^n Tr_F((D+n) q^D) = (1/(2 pi i)) d Phi/d tau.  (GA2.3)

Because Phi has weight zero, differentiating its transformation law makes
the right side a weight-two modular form, possibly meromorphic at cusps,
on Gamma_0(2). Its normalized value is

    n [2 E_2(2 tau)-E_2(tau)],

with the conventional E_2(tau)=1-24 sum_(r>=1) r q^r/(1-q^r).
The added scalar n is essential: the expectation of D alone is this
expression minus n. Thus an infinite energy-weighted sum can restore a
modular law that no fixed occupation mode has. The same idea extends to
colored energy currents and twined responses; their full theorem belongs
to [the current-correlation manuscript](bol-genus-one-correlations.md),
rather than this architectural test.

The example also controls the meaning of progress: an energy response
derived solely by differentiating Phi cannot contain more information
than Phi. To go beyond cycle profiles and fusion dimensions, the correlations
must retain multiplication and translation matrices in their coefficients.

## 4. Why a full integer-moded fermion requires a larger vacuum

The exterior space F_B supplies creation and annihilation operators for
nonzero integer modes. It does not supply zero modes. The difference is
algebraic, not a matter of notation.

**Proposition GA3 (zero-mode enlargement is necessary).** Let E be a complex
vector space with a nondegenerate symmetric bilinear form and dimension
2r>=2. Suppose operators psi_j(v), for j in Z and v in E, satisfy

    psi_j(v) psi_l(w)+psi_l(w) psi_j(v)
       =delta_(j+l,0) (v,w) 1,
    [D,psi_j(v)]=-j psi_j(v).

Every finite-dimensional nonzero lowest-grade space has dimension divisible
by 2^r. In particular such a system cannot act with the stated grading on
a positive-mode exterior space whose degree-zero part is one dimensional.

**Proof.** The zero modes preserve each grade and satisfy the defining
relations of the complex Clifford algebra Cl(E). A maximal isotropic
decomposition E=W direct_sum W^* realizes this algebra on exterior(W):
the two summands act by exterior multiplication and contraction. These
operators generate all endomorphisms of exterior(W), so

    Cl(E) is isomorphic to Mat_(2^r)(C).

For completeness, products of the r occupation projections and their
complements give the projections onto individual exterior basis vectors;
creation and contraction then give every matrix unit. Both algebras have
dimension 2^(2r), proving the isomorphism. Every finite-dimensional module
over this matrix algebra is a direct sum of its 2^r-dimensional simple
module. Apply this to the lowest-grade space. QED.

This proposition does not exclude an unrelated vertex structure on the same
graded vector space. It excludes the stated full integer-moded CAR extension
while keeping its one-dimensional vacuum.

### A canonical charged completion

The kernel continuation uses a specific repair. With H=B tensor C^24, form

    Fhat_B=exterior(H[0]) tensor
       exterior( direct_sum_(m>=1) (H[m] direct_sum H^*[m]) ).

The ground exterior factor realizes the zero-mode Clifford algebra of
H direct_sum H^*. This is canonical as a charged construction: no choice of
a polarization inside H is needed, since H and H^* are already distinguished.
The original F_B embeds by taking the vacuum in the new zero and dual-mode
factors. Its positive-H mode algebra and integer energy grading are retained.
The complete charged object has a larger ground space and a different
partition normalization; its construction and trace comparison are owned by
[the kernel manuscript](bol-genus-one-kernel.md).

In particular, this is an explicit enlargement, not an identification of the
old oscillator space with a complete Ramond module. Tensor factors not acted
on by an inserted original-mode observable cancel in the normalized trace
whenever their partition traces are nonzero. This gives a concrete bridge
to the old correlations while allowing full fields.

## 5. What the kernel and its modular closure must retain

A flat torus bundle requires commuting holonomies U,V. Two arbitrary Bol
translations need not commute and cannot simply be assigned to the two
cycles of an unpunctured torus. Noncommuting translation matrices can still
occur as insertions; a punctured-torus construction would have a different
fundamental-group relation and is a separate extension.

For the finite odd-order group acting on B, the three nontrivial sign pairs
in {+1,-1}^2 give a natural zero-mode-free family of boundary conditions.
At least one signed holonomy has no eigenvalue one, since an odd-order
operator has no eigenvalue minus one. This is a useful input-specific way
to avoid a trivial flat line. The family as a whole is preserved by modular
changes of the two cycles; a chosen individual sign pair generally is not.

The geometric kernel is uniquely determined by its unitary holonomies,
lattice poles, and identity residue when there is no common invariant vector.
Its modular covariance follows by transporting those conditions. This is
the mechanism proved in the canonical kernel manuscript. It is standard
elliptic/free-fermion geometry attached to the marked Bol data, not an
analytic consequence unique to Bol loops.

To identify this geometric object with a thermal field correlation, fix the
Fourier and trace conventions. For a temporal eigenvalue lambda and integer
spatial modes, the conventions

    psi(z)=sum_(r in Z) psi_r exp(2 pi i r z),
    K_lambda(z)=-2 pi i sum_(r in Z)
        exp(2 pi i r z)/(1+lambda^(-1)q^r)

give spatial multiplier +1, temporal multiplier -lambda, and residue one.
The bilateral series initially converges in 0<Im(z)<Im(tau). Thus an ordinary
g-twined Ramond trace corresponds to U=1,V=-g in these conventions. The
zero-mode term is lambda/(1+lambda). Reversing the Fourier sign requires
changing the corresponding holonomy convention; omitting that zero-mode
term is not the same elliptic kernel.

A finite holonomy/spin family at each fixed insertion arity is a meaningful
closed modular system. It is different from a finite vector containing every
individual mode and every derivative of every field. Fourier coefficients
of the resummed fields need not themselves form a finite modular system:
GA1 explains why infinitely many modes must mix when one changes the torus
cycle used to expand the field.

## 6. Standard mechanism, proposed attachment, and remaining test

The established free-fermion literature supplies elliptic kernels,
Pfaffian/determinant correlation formulas, zero-mode sectors and modular
transformation laws. Precise primary-source details are assigned to
[REFERENCES.md](../REFERENCES.md), under MTZ07 and Mat19. In particular a Fay
identity for the Kronecker kernel is already a standard analytic relation;
renaming it a Bol identity would not establish new moonshine.

The proposed contribution is the use of the canonical translation-generated
class algebra, actual multiplication currents, distinguished sandwich action,
and retained positive cocycle as simultaneous input to the completion. A
successful theorem must state how these matrices enter the correlations and
prove relations or reconstruction facts that survive the loss-of-information
controls. Universal Wick identities alone do not establish that dependence.

GA1--GA2 give a precise negative answer for unchanged fixed-mode closure.
GA3 records the exact algebraic price of an integer-moded completion. Neither
is a no-go theorem for Bol-loop moonshine. The positive question is whether
the completed, marked correlation family yields new constraints on admissible
Bol data beyond its universal free-fermion identities. That question is not
settled by this architectural manuscript.
