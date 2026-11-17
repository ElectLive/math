# Translation Fock theory and the first nonassociative spectrum

**Mira Cult**

## Sandwich representations are actual Bol extension modules

For a left Bol loop L define the presented group

    U_B(L)=<u_x (x in L) | u_e=1, u_x u_y u_x=u_(x(yx))>.

A sandwich representation over a field K is a finite-dimensional K-space V
with invertible operators T_x satisfying those relations. A morphism
intertwines every T_x. Equivalently it is a representation of the group
algebra K[U_B(L)]. A loop isomorphism transports the generators, giving a
functorial equivalence of these representation categories. Direct sums,
tensor products with T_x acting diagonally, and contragredients all preserve
the sandwich relation; the one-dimensional trivial representation is the
tensor unit. The universal group need not be finite, and semisimplicity of
all its finite-dimensional representations is not assumed.

**Proposition O0 (split-extension interpretation).** Let T_e=1 and every T_x
be invertible. The multiplication

    (x,u)*(y,v)=(xy,u+T_x v)                         (O0.1)

on L x V is a left Bol loop if and only if T is a sandwich representation.
The projection onto L is a split loop homomorphism with abelian kernel V;
fiberwise addition and scalar multiplication commute with its multiplication.

**Proof.** The identity is (e,0), and both division equations are uniquely
soluble by first solving in L and then in V. In the Bol identity with entries
(x,u),(y,v),(z,w), the left side's V-coordinate is

    u+T_x v+T_x T_y u+T_x T_y T_x w,

whereas the right side's is

    u+T_x v+T_x T_y u+T_(x(yx)) w.

The base coordinates agree because L is Bol. Equality for every w is exactly
the sandwich relation. The splitting x -> (x,0) and the remaining assertions
follow by the displayed linear formula. QED.

Thus this is a concrete fragment of the established abelian-extension module
framework, not an assertion that a nonassociative loop embeds multiplicatively
in a matrix group. The canonical finite quotient U_B(L) -> LMlt(L),
u_x -> L_x, distinguishes its generators since L_x(e)=x. For representations
factoring through this finite quotient over C, averaging over LMlt(L) gives
invariant positive Hermitian forms and complete reducibility, and the ordinary
group character orthogonality applies on the full group. Its restriction to
the n distinguished translations is not asserted to be an orthogonality law.
The phase-packet construction supplies its own explicit orthogonality,
induction and tensor rules in [the cocycle manuscript](bol-cocycle-packets.md#a-usable-character-theory-fragment).

For antecedents and the larger universal-stabilizer theory, see
[Smith and Fuad--Smith](../REFERENCES.md#existing-representations-genuine-foundations-and-information-loss).

## The marked representation and its graded extension

For a loop L with identity e, let V_L=C[L] with its orthonormal basis e_z.
Put A_x e_z=e_(x z). Retain the indexed A_x and the vector e_e. A loop
isomorphism induces their unitary intertwiner. The marked pointed object
recovers multiplication from A_x e_y=e_(xy). Forgetting the marking/point
can lose isotope information; no faithfulness claim is made after forgetting.

For a left Bol loop, A_x A_y A_x=A_(x(yx)). This is the operator relation
used here. We do not impose the false multiplicative relation A_x A_y=A_(xy).
The latter's defect is

    D_(x,y)=A_(xy)^(-1) A_x A_y.

It fixes e_e. Its degree-one trace is the exact integer

    tr(D_(x,y))=# { z in L : x(yz)=(xy)z }.             (O1)

Thus summing these traces counts associative triples, and every defect is
identity if and only if the loop is associative.

Define the graded oscillator space

    F_L=Sym( direct-sum_(m>=1) V_L[m] ),

where V_L[m] is a copy of V_L placed in degree m. Each graded piece is finite
dimensional. Any permutation g of L acts diagonally on all copies, hence gives
a graded automorphism Gamma(g) of F_L. This is functorial, so the Bol operator
relation holds in every degree and every loop defect remains the corresponding
three-operator word. It is already faithful in degree one.

If n=|L| and g has c_d cycles of length d, its convergent graded trace is

    Z_g(tau)=sum_(m>=0) tr(Gamma(g)|F_L[m]) q^(m-n/24)
      =q^(-n/24) product_(m>=1) det(1-q^m g)^(-1)
      =product_(d>=1) eta(d tau)^(-c_d).                 (O2)

The first equality follows by taking the symmetric-algebra trace in an
eigenbasis. A d-cycle contributes det(1-tg)=1-t^d, proving the eta formula.
Absolute convergence follows from |q|<1 and the finite number of cycles.
All coefficients before the q shift are nonnegative integers: Gamma(g) is a
permutation of the monomial basis, so its trace counts fixed monomials.
This is an honest graded construction; it is not the normalized rational
Eisenstein scalar series from [the companion rank packet](bol-modular-packets.md).

Let N=ord(g) and c=sum c_d. For gamma=[[a,b],[c0,d0]] in Gamma_0(N), let
gamma_delta=[[a,b delta],[c0/delta,d0]] for delta|N. The ordinary Dedekind
eta law gives

    Z_g(gamma tau)
      =product_delta nu(gamma_delta)^(-c_delta)
       (c0 tau+d0)^(-c/2) Z_g(tau).                    (O3)

Here nu is the usual eta multiplier and the square-root convention is the
same in each factor. Thus weight is -c/2, which varies with the cycle shape;
there is no assertion that all these functions form a common-weight vector.

## A weight-zero scalar normalization retaining cycle shape

Put Delta=eta^24 and define

    M_g(tau)=Delta(tau)^c / product_d Delta(d tau)^(c_d)
      =product_(d>=2) [Delta(tau)/Delta(d tau)]^(c_d).    (O4)

It is a meromorphic weight-zero modular function on Gamma_0(N), with trivial
multiplier, holomorphic and nonzero in the upper half-plane and meromorphic at
cusps. Its pole order at infinity is

    sum_d (d-1)c_d = n-c = rank(1-g).                  (O5)

No elliptic curve, j-invariant, genus-zero property or Monster is asserted.
The modularity follows directly by using the weight-12 Delta law in every
factor: the common (c0 tau+d0) powers cancel. The cusp claim follows from the
finite eta product transformation and its q expansion at rational cusps.

With n known, M_g recovers the entire cycle shape. To see this put
A=sum_(d>=2)c_d and r=sum_(d>=2)(d-1)c_d. Then

    q^r M_g=product_(m>=1)(1-q^m)^[24(A-sum_(d|m,d>=2)c_d)].

The Euler exponents are uniquely determined inductively by the formal series.
The exponent at m=1 gives A. For each m>=2, subtract the already determined
proper-divisor terms to recover c_m. Finally c_1=n-sum_(d>=2)d c_d.
In particular M_g=1 if and only if g=1. This is an exact spectral invariant,
not a complete invariant of the loop after its marked word labels are removed.

## Theorem O1: nonassociative spectra first occur at word length three

Let L be a finite left Bol loop of odd order n, and let S={A_x:x in L}.
Then:

1. Every g in S has uniform cycle shape d^(n/d) for some odd d dividing n.
2. Every product of two elements of S is conjugate in Sym(L) to an element
   of S, and therefore has uniform cycle shape too.
3. If L is nonassociative, some product of three elements of S has mixed
   cycle lengths. A witness can be chosen as a defect D_(x,y).
4. If L is a group, every word in S has uniform cycle shape.

Consequently a finite odd-order left Bol loop is nonassociative exactly when
mixed cycle shape first appears among three-translation words. Equivalently,
its one- and two-translation Fock traces are all of the form

    eta(d tau)^(-n/d),

while some three-translation trace is a genuinely mixed eta product.

**Proof.** The Bol identity says S is closed under g h g and contains 1.
For each g in S, induction from 1,g gives g^k in S for every k>=0. If g^k
fixes a point z, write g^k=A_u; then u z=z=e z and right cancellation force
u=e, so g^k=1. Therefore every cycle of g has length ord(g), proving (1).
In particular ord(g) divides odd n. Each g has a unique group-theoretic
square root h inside its cyclic subgroup, and that root belongs to S by the
power argument. For g=h^2 and k in S,

    h^(-1) (g k) h = h k h in S.

This proves (2). Every inverse g^(-1) is also a positive power and belongs
to S. If L is nonassociative, some D_(x,y) is nonidentity by (O1). It is a
product of three elements of S and fixes e; therefore it has a 1-cycle and
also a cycle of length greater than one. This proves (3). In a group the
translations form the regular permutation group, so every word is a
translation and the argument for (1) applies, proving (4). The eta conclusion
uses (O2) and uniqueness of the cycle-shape Euler product. QED.

The twisted-subgroup algebra behind this theorem is standard. Its precise
graded/minimal-spectrum formulation is a deduction in this continuation;
no literature-priority claim is made.

## Compact proper-Bol family

Use the [coordinate manuscript](bol-cocycle-packets.md)'s proved family Q=W x C_m x F_q with multiplication
(u,t,s)(v,r,h)=(u+alpha^t v,t+r,s+h-beta(u,v)), where q is odd, m|q-1,
alpha has order m and dim_Fq W=2d. Its actual defect is

    (w,k,l) |-> (w,k,l+beta(c,w)),
    c=(1-alpha^r)u+(alpha^t-1)v.

For c nonzero, if p=char(F_q), n=m q^(2d+1), F=m q^(2d), and
C=(n-F)/p, the exact formulas are

    Z_D=eta(tau)^(-F) eta(p tau)^(-C),
    M_D=[Delta(tau)/Delta(p tau)]^C,
    pole_infinity(M_D)=(p-1)C.

For q=3,m=2,d=1 these are n54,F18,C12 and M_D=(Delta/Delta_3)^12, with
pole24. This even-order example directly validates the Fock-defect formula;
the minimal-word theorem above is only claimed for odd order. An odd-order
control is q=7,m=3,d=1, where n1029,F147,C126, or the source's actual proper
subloop q=19,m=3,d=1,alpha=7, where n20577,F1083,C1026.

When alpha=1, c vanishes identically and the central-extension product is a
group. Thus the same family gives an associativity ablation rather than an
unrelated comparison.

## Two bounded information-loss results

The following controls distinguish failure of a specific architecture from a
general obstruction to a Bol theory.

**Proposition O2 (ordinary Latin-incidence spectrum loses the loop).** Form the
graph on the n^2 multiplication-table cells, joining distinct cells when they
share a row, a column, or a symbol. Its adjacency spectrum is

    3(n-1) once,
    n-3 with multiplicity 3(n-1),
    -3 with multiplicity (n-1)(n-2).

Thus this spectrum depends only on order, for every Latin square, including
all loop tables. This does not say that the graph itself, or its labeled
incidence structure, is order-only.

**Proof.** Let B be the n^2 by 3n incidence matrix of cells versus the n rows,
n columns and n symbol classes. Then adjacency is BB^t-3I. The block matrix
B^t B has diagonal blocks nI and all off-diagonal blocks the all-ones matrix.
On the three separate zero-sum subspaces it has eigenvalue n, with total
multiplicity 3(n-1). On the three-dimensional constant-block subspace it has
eigenvalues 3n,0,0. Transfer the nonzero eigenvalues to BB^t and add its
remaining (n-1)(n-2) zero eigenvalues. Subtract 3I. The n=1 case is read
separately as a one-vertex graph. QED.

**Proposition O3 (strong associative loop grading).** Suppose an associative
algebra is a direct sum of nonzero subspaces A_x indexed by a loop L, and
the linear span of A_x A_y equals A_(xy) for every x,y. Then L is associative.

**Proof.** Associativity of products of subspaces gives
A_((xy)z)=(A_x A_y)A_z=A_x(A_y A_z)=A_(x(yz)). Nonzero summands of a direct
sum are equal only when their indices agree. QED.

This excludes this strong-grading definition for proper Bol loops. It does
not exclude the operator modules in O0, nonassociative algebras, weaker
gradings, or new vertex-like identities. For a separate proved coherence
and erasure result about scalar categorical associators, see
[the central cubic case](bol-cubic-isotopes.md#what-a-scalar-categorical-associator-would-forget).

## Limits

The modularity of permutation Fock traces is a universal oscillator mechanism.
The loop-specific content is its retained distinguished translations, exact
Bol relation, minimal-three-word spectral constraint, and calculable defect
cycle types. The separate phased-character packet is what distinguishes the
prescribed nonisomorphic isotope pair and reconstructs restricted families.
Neither mechanism yet supplies a loop-dictated vertex algebra, a denominator
identity or genus-zero moonshine. These are foundations with explicit losses
of information, not a claim of a new Monster-like phenomenon.

The eta multiplier and rational-cusp laws used above are the standard ones in
Scheithauer, section 6, Propositions 6.1--6.2; see
[the bibliography](../REFERENCES.md#modular-analytic-sources).
