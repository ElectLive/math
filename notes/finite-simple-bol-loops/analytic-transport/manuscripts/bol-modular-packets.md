# A canonical modular packet for alternating-rank data

**Mira Cult**

Mathematical source by model participant 3. See [the overview](../README.md)
for exact-source review and verification status. This note contains complete elementary proofs of the modular bridge;
the extraction of its inputs from the pinned Bol-loop constructions belongs to
the coordinate manuscript. It allocates no permanent claim IDs.

## 1. Input, scope and what is new here

Let p be a prime and let beta: W x W -> F_p be an alternating bilinear form on a
finite-dimensional vector space. Put V=W/rad(beta) and r=dim(V)=rank(beta).
The rank r is even, including in characteristic two. The modular construction below works also for an arbitrary
finite-dimensional F_p vector space V, so its analytic mechanism is standard
finite Fourier theory, not a theorem peculiar to Bol loops. Its proposed
loop-specific content is the *intrinsic indexed packet* of forms beta extracted
from cocycle phases and selfadjoint operators, and the reconstruction/detection
theorems proved from that packet.

No basis, polarization, positive definite lattice, or embedding in an unrelated
finite group is chosen. The necessary additional choice is the fixed additive
character psi(t)=exp(2 pi i t/p), with t interpreted modulo p. Isomorphisms of
alternating data transport the entire construction canonically.

## 2. Hyperbolic finite quadratic module and actual coherence

Set D(V)=V direct-sum V*, with

    Q(v,lambda)=lambda(v)/p in Q/Z,
    B((v,lambda),(w,mu))=(lambda(w)+mu(v))/p.

This is a nondegenerate finite quadratic module, of order p^(2r), with level p
when r>0. (For r=0 it is trivial, with level 1.) If one prefers to retain beta
explicitly, the isomorphism V -> V*, w |-> beta(-,w), identifies this with the
quadratic module V direct-sum V having Q(v,w)=beta(v,w)/p.

Write M=|V|=p^r and H_V=C[D(V)] with orthonormal basis e_(v,lambda). Define

    rho(T)e_x = exp(2 pi i Q(x)) e_x,
    rho(S)e_x = M^(-1) sum_(y in D) exp(-2 pi i B(x,y)) e_y,

where S=[[0,-1],[1,0]] and T=[[1,1],[0,1]].

**Proposition M1 (coherent, functorial modular action).** These operators extend
to a unitary representation rho_V of SL_2(Z), factoring through SL_2(F_p).
They obey rho(S)^2 e_x=e_(-x) and (rho(S)rho(T))^3=rho(S)^2. A linear
isomorphism f:V->V' induces e_(v,lambda) |-> e_(f(v),lambda compose f^(-1)),
intertwining the representations and preserving the vacuum e_0.

**Proof.** Introduce another orthonormal basis f_(v,w), indexed by V x V, and
the unitary partial Fourier transform

    U e_(v,lambda)=M^(-1/2) sum_(w in V) psi(-lambda(w)) f_(v,w).

Character orthogonality gives

    U rho(T) U^(-1) f_(v,w)=f_(v,w+v),
    U rho(S) U^(-1) f_(v,w)=f_(w,-v).

Let J=[[0,1],[1,0]]. For gamma in SL_2(F_p), let its operator on the f-basis
send the column (v,w) to J gamma J (v,w). This is a genuine permutation
representation because gamma |-> J gamma J is a group automorphism. Its S
and T operators are the two displayed operators. Pull it back through U and
reduction modulo p. This proves every group relation and finite-level claim,
without assuming an unproved categorical associator or metaplectic coherence.
The naturality assertion follows directly from evaluation and the Fourier sum.
The S-square assertion also follows from character orthogonality. QED.

In particular

    <e_0,rho(S)e_0> = p^(-r).                         (M1.1)

This is a modular transformation amplitude determined by the alternating rank.

## 3. A p+1-dimensional exact model

The entire space H_V is huge when r is large. Its vacuum cyclic subspace is
small and sufficient for the invariant below.

For a line ell=[a:b] in P^1(F_p), put

    u_ell=M^(-1/2) sum_(v in V) f_(a v,b v).

The vector depends only on ell, since changing (a,b) by a nonzero scalar
permutes V. The vacuum Ue_0 is u_[0:1]. The SL_2 action permutes these vectors
by J gamma J.

**Proposition M2 (exact compression).** If r>0, the p+1 vectors u_ell are
linearly independent and span the vacuum cyclic subrepresentation. Their Gram
matrix is

    G_r=(1-p^(-r)) I_(p+1) + p^(-r) 1_(p+1)1_(p+1)^t.   (M2.1)

Thus all vacuum computations require p+1 coordinates and rational Gram data,
independently of r. For p=3 this is four coordinates.

**Proof.** Two distinct line subspaces
{(a v,b v):v in V} and {(c v,d v):v in V} intersect only at (0,0), because
ad-bc is invertible. Their normalized indicator vectors therefore have inner
product 1/M; each vector has norm one. The Gram eigenvalues are 1-1/M with
multiplicity p and 1+p/M with multiplicity one, which are positive for r>0.
The action is transitive on lines, so their span is exactly the vacuum cyclic
subspace. QED.

**Important ablation.** As an *unmarked abstract representation*, this cyclic
subspace is the same permutation representation on P^1(F_p) for every r>0.
The rank is retained by the vacuum and its invariant Hermitian pairing, or by
the full finite quadratic module. Discarding those data discards the invariant.

For gamma=[[a,b],[c,d]], the line [0:1] is sent by J gamma J to [c:a]. Hence

    <e_0,rho(gamma)e_0> = 1       if p divides c,
                         p^(-r) otherwise.              (M2.2)

This also holds for gamma inverse. It includes r=0, where both values are one.

## 4. A convergent modular form from the finite action

Let Gamma=SL_2(Z), Gamma_infinity={plus/minus T^n:n in Z}, and
j(gamma,tau)=c tau+d for gamma=[[a,b],[c,d]]. Define the H_V-valued Eisenstein
series

    E_V(tau)=sum_(gamma in Gamma_infinity\Gamma)
              j(gamma,tau)^(-4) rho(gamma)^(-1)e_0.       (M4.1)

There is no factor 1/2 here because Gamma_infinity already contains -I.
Equivalently one may sum over primitive pairs (c,d) with a factor 1/2.

**Theorem M3 (weight-four modular packet).** The series (M4.1) converges
absolutely and locally uniformly on the upper half-plane, defines a holomorphic
vector-valued modular form, and obeys

    E_V(gamma tau)=(c tau+d)^4 rho(gamma) E_V(tau).        (M4.2)

It is holomorphic at every cusp and has constant term e_0 at infinity. Its
vacuum scalar component

    F_(p,r)(tau)=<e_0,E_V(tau)>

is a holomorphic modular form of weight 4 on Gamma_0(p), with trivial character,
and equals

    F_(p,r)(tau)
      =p^(-r) E_4(tau)
       +(1-p^(-r)) [p^4 E_4(p tau)-E_4(tau)]/(p^4-1)
      =[(p^(4-r)-1)E_4(tau)+p^4(1-p^(-r))E_4(p tau)]/(p^4-1),  (M4.3)

where E_4(tau)=1+240 sum_(n>=1) sigma_3(n) q^n and q=exp(2 pi i tau).

**Proof.** The coset term is well defined: rho(T)e_0=e_0,
rho(-I)e_0=e_0 and weight 4 is even. Since rho is unitary, the norm of each
term is |c tau+d|^(-4). The sum over primitive pairs is bounded by the usual
absolutely convergent weight-four Eisenstein sum; standard lattice estimates
give local uniform convergence. For completeness, on a compact subset of the
upper half-plane, |c tau+d|^2 is bounded below by a positive constant times
c^2+d^2, and sum_((c,d) not (0,0)) (c^2+d^2)^(-2) converges. Reindexing by
right multiplication on left cosets and using
j(alpha,gamma tau)=j(alpha gamma,tau)/j(gamma,tau) proves (M4.2).
Holomorphicity follows from local uniform convergence.

The c=0 coset contributes e_0. For c nonzero, grouping by c and comparing the
sum over d to an integral bounds the remaining norm by O(y^(-3)) as
tau=x+iy, uniformly for bounded x. Thus the constant term is e_0 and there
is no negative Fourier term. The transformation law gives the same bounded
behavior after any cusp change of coordinates, hence holomorphicity at every
cusp.

Using (M2.2), write

    F_(p,r)=p^(-r) E_4+(1-p^(-r)) H_p,

where H_p=1/2 sum_(gcd(c,d)=1, p|c) (c tau+d)^(-4).
Split E_4(p tau)=1/2 sum_(gcd(m,n)=1) (p m tau+n)^(-4)
according to whether p divides n. The part p not dividing n is H_p. In the
other part n=p n', necessarily p does not divide m, and this contributes
p^(-4)(E_4-H_p). Thus

    H_p=[p^4 E_4(p tau)-E_4(tau)]/(p^4-1),

proving (M4.3). Every element of Gamma_0(p) fixes e_0, by (M2.2) and unitarity
(a unit vector with inner product one with e_0 equals e_0). This and (M4.2)
prove the scalar modular transformation with trivial character. QED.

The q-series converges absolutely for Im(tau)>0. Explicitly,

    [q^n]F_(p,r)=240/(p^4-1) times
      [(p^(4-r)-1)sigma_3(n)
       +p^4(1-p^(-r)) 1_(p|n) sigma_3(n/p)].             (M4.4)

## 5. Rank recovery from modular behavior

**Corollary M4 (rank tomography).** The normalized scalar form determines r:

    (F_(p,r)|_4 S)(i infinity)=p^(-r),                  (M5.1)
    [q]F_(p,r)=240(p^(4-r)-1)/(p^4-1).                 (M5.2)

Thus F_(p,r)=F_(p,s) if and only if r=s. Equivalently,

    p^(4-r)=1+(p^4-1)[q]F_(p,r)/240.

**Proof.** The vector constant term and (M1.1) give (M5.1). Alternatively,
the ordinary E_4 S law gives

    (H_p|_4 S)(tau)=[E_4(tau/p)-E_4(tau)]/(p^4-1),

whose constant term is zero. Formula (M5.2) follows from (M4.3), since
E_4(p tau) has no q term. Distinct integer ranks give distinct powers of p.
QED.

The invariant is far more compact than D(V): it needs the integers p,r or one
rational cusp amplitude. This is a strength for the enormous construction and
also an honest limitation: a single component sees exactly the rank, no more.

For the phase sector calculated in the
[coordinate manuscript](bol-cocycle-packets.md), r=72 in the original and
r=36 in its principal isotope, at p=3. Using that calculation and retaining
its pinned loop-construction and strict-isomorphism dependencies,

    S_00(original)=3^(-72),   S_00(isotope)=3^(-36),
    [q]F_(3,72)=-3+3^(-67), [q]F_(3,36)=-3+3^(-31).    (M5.3)

The selected forms are therefore different without constructing a single
element of the full multiplication table or a 3^144-dimensional matrix.

## 6. Family reconstruction through modular cusp data

Suppose the coordinate classification supplies a symplectic F_p space
(W,beta), a commuting semisimple coprime-order action with selfadjoint spectral
idempotents e_xi, and a selfadjoint nilpotent operator N commuting with them.
Assume its xi-primary Jordan blocks occur in paired multiplicities n_(xi,j),
where the field degree is d_xi. For k>=0 define

    beta_(xi,k)(u,v)=beta(e_xi N^k u,v),
    r_(xi,k)=rank(e_xi N^k).

Selfadjointness and p odd make beta_(xi,k) alternating, since
beta(Pu,u)=beta(u,Pu)=-beta(Pu,u), and beta nondegenerate implies
rank(beta_(xi,k))=rank(P). Attach the form F_(p,r_(xi,k)) to each indexed test.

**Proposition M5 (recovering paired Jordan data).** The indexed modular packet
recovers every multiplicity by

    n_(xi,j)=[r_(xi,j-1)-2r_(xi,j)+r_(xi,j+1)]/(2 d_xi).  (M6.1)

**Proof.** Corollary M4 recovers each rank from its modular form. Apply the
rank reconstruction (P11) proved in the [coordinate manuscript](bol-cocycle-packets.md#complete-rank-packet-recovery-in-the-extraspecial-branch).
That source owns the block-rank argument and precise classification interface.
QED.

Consequently, if the restricted extraspecial classification says these indexed
paired multiplicities, modulo its stated simultaneous generator changes and
factor relabelings, classify its loops, then this indexed packet of level-p
weight-four forms is complete for precisely that restricted family. The
classification theorem is a separate pinned dependency; M5 alone does not
assert completeness for arbitrary Bol loops or recover forgotten labels.

There is a direct analytic compatibility law. Set

    a_(xi,k)=(F_(p,r_(xi,k))|_4 S)(i infinity)=p^(-r_(xi,k)).

Then 0<a_(xi,0)<=a_(xi,1)<=...<=1, the sequence is eventually one, and

    a_(xi,k)^2/[a_(xi,k-1) a_(xi,k+1)]
       =p^(2 d_xi n_(xi,k)).                            (M6.2)

Thus the cusp amplitudes are log-concave and their multiplicative second
differences belong to the discrete set {p^(2d_xi n): n>=0}. Conversely, any
finite indexed rank sequence with the required terminal zeros and these
nonnegative integral second differences determines the paired block partition.
This is a restriction on an admissible loop packet, rather than an arbitrary
list of unrelated modular forms. It does not by itself enforce additional
cross-action or simplicity hypotheses of a loop classification.

Direct sums obey an exact composition law. D(V direct-sum V') is canonically
D(V) orthogonal-sum D(V'), so rho_(V direct-sum V')=rho_V tensor rho_V' with
tensor-product vacuum. Cusp amplitudes multiply: a_(r+s)=a_r a_s. Writing
H_p as in section 4, the scalar Eisenstein shadows therefore obey

    F_(p,r+s)=H_p+(F_(p,r)-H_p)(F_(p,s)-H_p)/(E_4-H_p).  (M6.3)

The displayed quotient has removable singularities because each difference
is a constant multiple of E_4-H_p. Formula (M6.3) follows from that identity;
it is not a claim that Eisenstein series themselves commute with tensor products.

### Pinned cross-extraspecial inputs and controlled variation

The [coordinate construction](bol-cocycle-packets.md#complete-rank-packet-recovery-in-the-extraspecial-branch) uses the character-and-partition classification,
equation (13) of `odd-extraspecial-classification.md` at
`87a90248685c58835815e36ec673f82fb0f0e77a`. Its cross-extraspecial example has
W_3=F_27^2 with one degree-three order-13 character orbit and one paired
Jordan block of length one, so r_(3,xi,0)=6 and r_(3,xi,k)=0 for k>=1.
The other block W_13=F_13^2 has one degree-one order-three character and one
paired block of length one: its ranks are 2,0,0,... . Consequently the
nontrivial cusp amplitudes of its modular packet are 1/729 and 1/169.

For its controlled same-order variation, take W_3=F_27^4,
with either two paired blocks of length one or one paired block of length two,
and the same W_13 block. The sequences on W_3 are respectively

    r_k=(12,0,0,...)  and  r'_k=(12,6,0,...).

The resulting loops have the same order 3^13 * 13^3, the same cross-action
graph and center dimensions, while their k=1 cusp amplitudes are 1 and 1/729.
Both parameter choices satisfy the construction conditions as checked in the
coordinate manuscript; the loop conclusions retain its pinned simplicity and
classification dependencies. The modular calculation follows immediately from
M4, and M5 explains the differing
Jordan partitions exactly. The q coefficient of F_(3,6) is -8/3, whereas
F_(3,0)=E_4 has q coefficient 240.

## 7. Relation to moonshine and remaining mathematical target

The finite quadratic module, Weil action and Eisenstein construction are
established mathematics. The proposed new content is their extraction from
particular nonassociative cocycle/associator data, the phase-selected principal
isotope obstruction, and the reconstruction of a restricted family from
modular cusp amplitudes. The single scalar form is determined by one rank;
this is a modular encoding of a structural invariant, not evidence of a new
sporadic symmetry or a genus-zero moonshine theorem.

F_(p,r) does not in general have nonnegative integral coefficients. Indeed for
p=3 and r>4 its first coefficient is negative and usually nonintegral. Thus
it is not being claimed to be the dimension series of an honest graded space
or a trace of finite-order operators with these normalized coefficients.
For the two rigid sectors this is a rigorous obstruction: a finite-order
operator has eigenvalues that are roots of unity, so its trace is an algebraic
integer; a rational algebraic integer is an integer. The displayed nonintegral
rational first coefficients cannot be such traces. Negative integer traces
alone would not be an obstruction, and no obstruction to a different graded
realization or normalization is asserted.
One may clear denominators, but doing so does not create a canonical graded
loop representation. The natural next strengthening is a loop-dictated graded
object realizing the finite Fourier packet, with an additional identity or
positivity mechanism not already forced by the rank alone.

## 8. Sources and verification

See [the canonical bibliography](../REFERENCES.md#modular-analytic-sources)
for the verified Scheithauer and Schwagenscheidt sources and exact locators.
The proofs above establish this hyperbolic specialization directly. See
[code and verification](../code/README.md) for exact finite checks.
