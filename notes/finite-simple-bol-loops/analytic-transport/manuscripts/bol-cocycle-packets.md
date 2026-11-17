# Polarized central-character packets for the odd class-two Bol branch

**Mira Cult**

## Canonical inputs and what is actually loop-sensitive

Use [odd-class-two-classification.md](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-class-two-classification.md), at repository commit
`2a25b81e3efe5bdd8a3923e27c94aef16a559094`, especially construction equations
(1)--(4), exhaustion, and strict isomorphism equation (15). Its own exact-source
review is pinned to `226a8dc1eb503026c350ffe3b7ac93da9077a593`; that review and
all its dependencies are inherited inputs, not reviews performed here.

We restrict the new character construction to elementary abelian local W and Z
at an odd prime p. The normal data are (A,W,Z,sigma,R,T,b,f). A strict transport
to primed data consists of E:A->A', L:W->W', M:Z->Z' satisfying equation (15).
The source theorem says these transports are exactly loop isomorphisms for its
selected simple class-two data. No new proof of that classification is claimed.

The bimap has an intrinsic interpretation in the marked canonical folder:
write S=H intersect P for the first stabilizer axis and identify W with S;
then

    b(x,y) = [s_x, tau(s_y)] in Z(P).

This follows directly from its BCH commutator (1). Both S and tau(S) are
abelian. Thus b is the cross-commutator pairing of the two actual marked axes;
it is not chosen from an arbitrary presentation of the abstract group. The
antisymmetric combination b(x,y)-b(y,x) compares the two cross-commutators.
The cocycle f retains the position of H inside G. In the rigid isotope example,
G, tau, K, b, R and T stay fixed while f changes. An invariant forgetting f
therefore forgets exactly the information responsible for that example.

We do not identify this bimap with a categorical associator. The general loop
associator is a different object, and no pentagon or quasi-Hopf coherence is
asserted. A direct connection to actual multiplication defects is given in the
small family at the end. For an associative loop its canonical left action is
regular, H=1, and these stabilizer-axis packets have W=0.

## Definition: phased Heisenberg packet

For ell in Z*=Hom_Fp(Z,Fp) define the alternating form

    a_ell(x,y) = (1/2) ell(b(x,y)-b(y,x)).             (P1)

More generally for a specified Fp-linear operator P on W set

    a_{ell,P}(x,y)=(1/2)ell(b(Px,y)-b(Py,x)).          (P2)

This is alternating whether or not P is self-adjoint. The latter assumption
will only be used to identify its rank in the extraspecial case. Let r_{ell,P}
be its rank and V_{ell,P}=W/rad(a_{ell,P}).

Let zeta_p=exp(2pi i/p). The twisted algebra H_{ell,P} has basis u_x for x in W
and multiplication

    u_x u_y = zeta_p^{a_{ell,P}(x,y)/2} u_{x+y}.      (P3)

The exponent division is in Fp. Bilinearity proves the cocycle identity
directly, so (P3) is associative. Its basis commutator is
u_xu_y=zeta_p^{a_{ell,P}(x,y)}u_yu_x. This is a representation object attached
to marked nonassociative data, not a faithful multiplicative map of the loop
into matrices.

Retain the labels ell and P, the natural actions transporting them, and the
central phases

    zeta_p^{ell(f(a))}, zeta_p^{ell((T(a)-1)^j f(a))}
    for a in A and all j >= 0.                       (P4)

The full packet uses all these labels; choosing a displayed phase fiber for a
calculation is not part of the definition. Redundant phase labels may be
omitted when a finite bound on nilpotence is known.

### Proposition P-A: functoriality and simple degrees

A strict data transport (E,L,M) sends ell' to ell=ell' M and P to
P'=LPL^{-1}. It induces H_{ell,P} -> H'_{ell',P'} by u_x -> u'_{Lx}, and carries
every phase (P4) to the corresponding one at E(a). Consequently the packet is
intrinsic to the loop under the cited classification interface.

If d=dim_Fp W and r=r_{ell,P}, then r is even and

    H_{ell,P} is isomorphic to
       direct sum of p^(d-r) copies of Mat_{p^(r/2)}(C).       (P5)

Proof. Equation (15) gives a'_{ell',P'}(Lx,Ly)=a_{ell,P}(x,y), and its T and f
equations prove the phase assertion. To prove (P5), split W into its radical
and a symplectic complement. The radical algebra is the ordinary group algebra
of an elementary abelian group and has p^(d-r) one-dimensional characters.
For each symplectic pair, the two generators in (P3) can be represented by the
p-by-p shift and clock matrices, whose monomials span all Mat_p(C). Tensoring
r/2 pairs gives Mat_{p^(r/2)}(C). Dimension p^d proves the decomposition is
exhaustive. The result and the isomorphism class are independent of the chosen
symplectic complement; the argument only uses it to prove the decomposition.

Thus a loop-sensitive algebraic invariant is already present before any
modularization: the distribution of simple degrees in every phase fiber.

### A usable character theory fragment

Objects are finite-dimensional unital H_{ell,P}-modules; morphisms are linear
maps intertwining every u_x. They admit invariant positive Hermitian forms:
average any such form over the finitely many u_x, whose multiplication phases
have absolute value one. The algebra involution is u_x^*=u_{-x}.
Let R=rad(a_{ell,P}), t=p^(r/2), and let chi range over the ordinary characters
of the additive group R. The irreducible module labeled by chi has projective
character

    ch_chi(x)=t chi(x) for x in R, and 0 otherwise.   (P5a)

Indeed u_x is scalar chi(x) on R by Schur's lemma; outside R some conjugation
by u_y multiplies it by a nontrivial pth root of unity, forcing its trace to
vanish. Hence

    |W|^(-1) sum_(x in W) ch_chi(x) conjugate(ch_psi(x))
       =delta_(chi,psi).                             (P5b)

The normalization follows from t^2 |R|=|W| and ordinary finite-character
orthogonality. A maximal isotropic subspace containing R supplies each module
by inducing a one-dimensional character extending chi; its index in W is t.
This realizes the modules without invoking an unrelated ambient symmetry group.

For the same W and P, tensoring an ell_1-projective module with an ell_2-
projective module yields an (ell_1+ell_2)-projective module, by the diagonal
operators u_x -> rho_1(u_x) tensor rho_2(u_x). The cocycle factors multiply
because (P2) is linear in ell. This defines composition across phase sectors
and automatically retains the additive central-character labels.
It does not assert L_x L_y=L_(xy) for the original loop translations.

## The rigid principal-isotope calculation

Input: [odd-rigid-center-nongloop.md](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-rigid-center-nongloop.md) at
`2a25b81e3efe5bdd8a3923e27c94aef16a559094`, its Data, Obstruction to the shift
isomorphism, and Arithmetic evidence and review scope sections. Its source
review was at `88214700dc527d238d5754029711752495c9a292`; these dependencies are
not re-proved here.

Here p=3, E=F_(3^18), W=E^4, Z=F3[epsilon]/epsilon^3,
T(a)=1+epsilon, N=T(a)-1, and

    f=f(a)=1-epsilon+epsilon^2,
    f'=f-epsilon^2=1-epsilon.

Both f,Nf,N^2f and f',Nf',N^2f' are bases of Z. Select the phase fiber

    (ell(f),ell(Nf),ell(N^2f))=(1,0,1).               (P6)

For the original data the unique ell has coefficients (1,1,1) on
(1,epsilon,epsilon^2). For the isotope the unique ell' has coefficients
(2,1,1). Indeed Nf=Nf'=epsilon-epsilon^2 and N^2f=N^2f'=epsilon^2; the first
phase equation then gives the asserted constant coefficient. This is a
fiber of the full intrinsic phase-indexed packet, not an arbitrary choice of
an ambient coordinate functional.

The displayed source matrices obey B1^T=B1. Hence the two alternating forms
(P1), apart from the invertible scalar 1/2, are the trace forms of

    C=(B2+B0)-(B2+B0)^T,
    C'=(B2-B0)-(B2-B0)^T.

For c in F3 let A(c)=(B2+cB0)-(B2+cB0)^T. Explicitly,

    A(c) = [[0,1,2,1], [2,0,1,1-c],
            [1,2,0,0], [2,c-1,0,0]].                (P7)

Its Pfaffian is 2(c+1), so det A(c)=(c+1)^2. Therefore A(1) has rank four,
while A(2) has rank exactly two: its determinant vanishes and its upper-left
two-by-two minor is nonzero. At c=2 its radical has E-basis
(1,1,1,0) and (0,0,1,1), which is an additional exact check.

For an E-matrix C the radical of (x,y)->Tr_E/F3(x^T C y) is its E-linear
radical. Nondegeneracy of the trace pairing proves this: if C^T x is nonzero,
choose an individual y-coordinate with nonzero trace pairing. Thus F3-rank is
18 times E-rank. The two ranks in (P6) are consequently

    original: r=72,  isotope: r=36.                   (P8)

The full W dimension is 72 in both cases. By (P5) the corresponding algebras
are Mat_(3^36)(C) and a direct sum of 3^36 copies of Mat_(3^18)(C).

Why is this an isomorphism obstruction and not only a labeled comparison?
In this precise pair, the q-side scalar R_q(a)=eta I, |eta|=9, forces the
p-torus generator to map a->a in every strict transport, exactly as in the
pinned manuscript. Its two relevant W_q maps are F19-linear, so no field
automorphism changes this conclusion. Thus N and the phase fiber (P6) must
be preserved. A possible Frobenius action on E does not change ranks, and
trace forms are invariant under the associated semilinear transport.
The different ranks/degrees contradict an isomorphism. No table of order
3^75*19^3 is generated or used.

### Ablation

The unphased multiset {H_ell:ell in Z*} is identical for the two examples:
b and W have not changed. The phased packet separates them. This is a sharp
loss-of-information statement for this architecture. It explains why merely
attaching a construction to the unmarked abstract canonical group fails on
this prescribed test, while retaining the stabilizer cocycle succeeds.
More explicitly, among the 27 center characters the F3-rank histogram is
rank 0: 3 characters, rank 36: 12, rank 72: 12, in both loops. To see this,
the symmetric B1 contributes zero and the Pfaffian of the skew part of
x B0+z B2 is a nonzero scalar multiple of z(x+z). The two distinct lines
z=0 and x+z=0 each contain two nonzero pairs; these have rank two over E,
the other four nonzero pairs have rank four, and the zero pair has rank zero.
There are three choices of the B1 coefficient for every pair.

## Complete rank-packet recovery in the extraspecial branch

Input: [odd-extraspecial-classification.md](https://github.com/Mira-Cult/math-wip/blob/87a90248685c58835815e36ec673f82fb0f0e77a/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-extraspecial-classification.md) at
`87a90248685c58835815e36ec673f82fb0f0e77a`, especially Complete operator
isomorphism criterion and Character and partition parameters, equations
(7), (13). Its complete continuation was reviewed at
`dce010e03e56d50af4fbfbb4aba69806228ec518` under the listed dependencies.
The classification and paired-Jordan normal form are inherited results.
The extraction from packet ranks is the deduction here.

In that branch Z_i=Fp_i, b_i=beta_i is nondegenerate alternating on W_i, and
the commuting operators R_i(a) are beta_i-self-adjoint. Let B_i be the
coprime part of A, N_i=R_i(b_i)-1 (with b_i here the source's torus generator,
not the bimap), and xi a nontrivial irreducible Fp_i-character orbit of B_i.
Let e_xi be its spectral idempotent and d_xi its field degree. Since the
group algebra acts by commuting self-adjoint operators, e_xi and all

    P_{xi,k}=e_xi N_i^k,   0<=k<=p_i                (P9)

are self-adjoint. Fix the identity nonzero center character; any other
nonzero center character merely scales the form and gives the same ranks.

For self-adjoint P, (P2) becomes beta_i(Px,y). Its radical is ker P because
beta_i is nondegenerate. Thus

    r_{xi,k}=rank_Fp_i(P_{xi,k}).                    (P10)

Let the inherited normal form have 2 n_{i,xi,l} Jordan blocks of length l
over F_(p_i^d_xi). Then

    r_{xi,k}=2 d_xi sum_{l=1}^{p_i} n_{i,xi,l} max(l-k,0),
    n_{i,xi,k}=(r_{xi,k-1}-2r_{xi,k}+r_{xi,k+1})/(2d_xi).  (P11)

Use r_{xi,p_i}=r_{xi,p_i+1}=0 at the endpoint. The first equation is the rank
of each Jordan block; taking the second finite difference proves the second.
Consequently the labeled collection of simple degrees (P5) for (P9) recovers
every normal-form integer n. The source-unit action b_j->b_j^{v_j} pulls back
the character labels xi, while replacing N_i by (1+N_i)^{v_i}-1, which is N_i
times a commuting invertible polynomial and changes none of these ranks.

Therefore the full packet, considered modulo that single consistent family
of source units, is a complete isomorphism invariant for precisely this
restricted extraspecial-derived class. This completeness assertion is
conditional on the pinned classification, and is not a classification of
all simple Bol loops. The cross-action graph is reconstructed by checking
which occupied xi are nontrivial on each source generator; its strong
connectivity is then the source theorem's exact simplicity test.

### Concrete non-order-only comparison

At p=3,q=13, take E=F27 and W_p=E^4, W_q=F13^2, with the same cross scalar
actions and symplectic forms. Compare own-prime R_p(b_p)=1 with
R_p(b_p)=1+N, where N=diag(J_2(0),J_2(0)^T) is square-zero, self-adjoint and
has E-rank two. These satisfy the source's strongly connected construction,
and both loops have order 3^13*13^3. The packet P=N has F3-rank zero in the
first loop and six in the second. Hence its Heisenberg simple degrees are
1 versus 3^3. The two loops are nonisomorphic by the same complete packet.
This comparison changes the associativity-defect action while holding order,
prime set, center dimensions and cross-action graph fixed.

## Contrasting root-graph parameters

Input: [nonbruck-root-graph-parameters.md](https://github.com/Mira-Cult/math-wip/blob/d07303ed0c50e12322e78ada7725173c2978af2f/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/nonbruck-root-graph-parameters.md) at
`d07303ed0c50e12322e78ada7725173c2978af2f`, Isomorphism reduction and normalizer,
equation (1). The precise loop-isomorphism interface remains conditional at
the scope stated there; its parameter-level calculations below are elementary.

For an Fp-linear map phi:Fq->Fq let m_s denote multiplication by s, and define

    C_phi(s,t)=m_s phi-phi m_t,
    r_phi(s,t)=rank_Fp C_phi(s,t),      s,t in Fq.     (P15)

Also retain rank phi. Suppose psi=m_c sigma phi m_d sigma^(-1), the source's
normal-form equivalence, where c,d are nonzero and sigma is a common field
Frobenius. Then

    C_psi(sigma(s),sigma(t))
       =m_c sigma C_phi(s,t) m_d sigma^(-1).

Thus the full rank array is preserved up to common Frobenius relabeling;
independent input/output scalar normalizations disappear. The common scalar
field is recovered in the source as the commutant of the natural SL2(q)
module, so it is not an arbitrary selected coordinate field. The marked graph
phi is essential: the abstract affine group is the same for every parameter.

For phi(x)=x^(p^k),

    C_phi(s,t)(x)=(s-t^(p^k))x^(p^k).

Its rank is zero exactly on the graph s=t^(p^k), and is f otherwise. Common
Frobenius preserves each such graph. Therefore (P15) separates all f monomial
classes, even though all their maps have full rank and all underlying affine
groups, loop orders and construction dimensions agree.

At q=4 the source's exact parameter classification has three classes,
represented by x, x^2 and x+x^2. The last has rank one and the first two rank
two. At s=t=omega, omega^2+omega+1=0, the two first maps have ranks zero and
two in (P15), respectively. Thus this compact rank packet is complete for
that three-class parameter family. It is not asserted complete for general q.

Modularization may now use the canonical hyperbolic finite quadratic module
im C_phi(s,t) plus its dual, or equivalently the weight-four modular form associated
to its rank in [the companion modular construction](bol-modular-packets.md). This does not identify the
root-graph loops with odd class-two loops; it demonstrates a second marked
operator source of loop-sensitive rank data. In characteristic two it does
not use the odd-characteristic twisted-algebra formula (P3).

## Direct proper Bol controls and defect calculation

For any odd prime power q, a positive integer m dividing q-1, an element
alpha in Fq of exact order m, and a nonzero symplectic Fq-space W of dimension
2d, define Q=W x C_m x Fq by

    (u,t,s)*(v,r,h)=(u+alpha^t v,t+r,s+h-beta(u,v)).   (P12)

Both division equations are uniquely soluble. Direct expansion of
x*(y*(x*z)) and (x*(y*x))*z gives vector component
(1+alpha^(t+r))u+alpha^t v+alpha^(2t+r)w and central component
2s+h+l-(1+alpha^(t+r))beta(u,w)-alpha^t beta(v,w). Hence this is a left Bol
loop. If alpha!=1, let x=(0,1,0), y=(e,0,0), z=(f,0,0) with beta(e,f)=1.
Then (xy)(zx) and (x(yz))x have central coordinates -alpha and -1, so the loop
is proper. When alpha=1 the formula is the associative central-extension
group law; it supplies an ablation.

For x=(u,t,s),y=(v,r,h), the actual left-translation defect
D_xy=L_(xy)^(-1)L_xL_y acts by

    D_xy(w,k,l)=(w,k,l+beta(c,w)),
    c=(1-alpha^r)u+(alpha^t-1)v.                    (P13)

The vector and C_m components of L_xL_y and L_(xy) agree; subtracting their
central components proves (P13). If c=0 the defect is identity. Otherwise
beta(c,-) is a surjective Fq-linear functional, so exactly
F=m q^(2d) of the n=m q^(2d+1) elements are fixed. All other orbits have
length p=char Fq. Thus its cycle type is 1^F p^((n-F)/p).

This gives an exact compact family for any translation/Fock modular shadow.
For q=3,m=2,d=1, alpha=-1, n=54 and a nonzero defect has cycle type 1^18 3^12.
For q=19,m=3,d=1,alpha=7, it is exactly the coordinate subloop used in the
pinned rigid-center manuscript's direct Moufang witness, of order 20577.
No simplicity of these small control loops is asserted.

For completeness, the number of ordered (x,y) yielding a nonidentity defect
when m>1 is

    q^2 (m^2-1) (q^(4d)-q^(2d)).                    (P14)

Indeed when (t,r)=(0,0) all q^(4d) vector pairs give c=0; otherwise one
nonzero scalar coefficient makes (u,v)->c surjective with kernel size q^(2d).
The two central coordinates contribute q^2. The complementary count is the
identity-defect count. At n=54 this gives 1944 nonidentity defects out of
2916 ordered pairs, and the total can be checked by a 54-element table.

## Exact checks requested for integration

Use independent integer modular row reduction on (P7), solve both phase
fibers, verify the radical basis at c=2, check (P11) on finite paired-Jordan
blocks, and exhaust the n=54 left Bol identity and defect distribution.
Those checks validate arithmetic and a small instance, not the symbolic
classification interface or huge-loop construction. No such computation
should be described as a proof of those inherited results.
