# Controls and literature boundary for the Bol subloop walk

Mira Cult

This note identifies the analytic operator within known incidence and group
constructions. It separates the applicable spectral baseline from the exact
consequences in the [finite](bol-section-mixing.md) and
[arithmetic](bol-section-local.md) theorems. Historical priority for the combined
results has not been established.

## 1. All torus orders work, including the full multiplicative group

Let `F=F_q` and `H<=F^*` have order `m>1`. Neither the direct Bol proof nor
the Fourier proof requires m odd. In multiplicative notation the loop is

```math
(u,a,s)(v,b,h)=(u+av,ab,s+h-\gamma(u,v)).
```

For x=(u,a,s), y=(v,b,t), z=(w,c,h), both x(y(xz)) and (x(yx))z have
coordinates

```math
((1+ab)u+av+a^2bw,\ a^2bc,
 2s+t+h-(1+ab)\gamma(u,w)-a\gamma(v,w)).
```

This verifies the left Bol identity over any commutative coefficient ring.
The inverse is (-a^{-1}u,a^{-1},-s), and direct substitution verifies the left
inverse property. For gamma(v,w)=1 and a!=1, put X=(0,a,0), Y=(v,1,0),
Z=(w,1,0). The central coordinates of (XY)(ZX) and (X(YZ))X are -a and -1.
Thus the loop is proper whenever such a exists. In particular m=q-1 is allowed
for every odd q>2. This is a directly verified extension of the displayed
restricted-section formula; it does not assert an embedding into every simple
folder from the source construction.

The spectrum's involution has m fixed basis vectors, not additional fixed
vectors when m is even. In exponent coordinates its permutation is
(j,t)->(j-t,-t). A fixed pair requires t=0 from the first coordinate, even if
2t=0 admits a second solution. Consequently the signed multiplicities remain
m(m+1)/2 and m(m-1)/2 per nonzero central character for even m.

## 2. Explicit symplectic-graph identification

Write V=F^d x F^d, gamma((x,y),(x',y'))=x.y'-y.x', and let the sampled
associative subloop be

```math
S=(F^d\times0)\times H\times\{0\}\cong F^d\rtimes H.
```

The state (x,y,b,s) remains on the leaf z=b^{-1}y. On a nonzero leaf, set
X=b^{-1}x. Sampling u uniformly in F^d and a uniformly in H sends

```math
b'=ab,\qquad X'=X+(ab)^{-1}u,\qquad
s'-s=-bb' z\cdot(X'-X).
\tag{C1}
```

The d-1 coordinates in ker(z.) reset uniformly at each step. For the effective
d=1 quotient write alpha=z.X, A=b alpha. Its vertices are (b,A,s) in H x F^2,
and the edge relation is

```math
t-s=cA-bB
\quad\text{between }(b,A,s),(c,B,t).
\tag{C2}
```

This is the orthogonality relation for the nondegenerate alternating form

```math
\omega((b,A,s,r),(c,B,t,r'))=bB-Ac+rt-sr'
```

on the affine chart r=r'=1 of projective 3-space. Thus the looped graph is
the induced subgraph on {[b:A:s:1]: b in H} of the ordinary symplectic polar
graph Sp(4,q) with a loop added at every vertex.

### The known spectral baseline already implies the norm bound

De Bruyn, Goryainov, Haemers and Shalaginov,
*Divisible design graphs from the symplectic graph*,
[arXiv:2404.09902v1](https://arxiv.org/html/2404.09902v1), Section 2.4,
definition of Sp(2e,q) and Lemma 4, give the symplectic graph's nonprincipal
eigenvalues q^{e-1}-1 and -q^{e-1}-1. For e=2, adding I gives q and -q.
Extend a mean-zero vector supported on our regular slab by zero to the full
graph. Its Rayleigh quotient lies in [-q,q]. Since the slab degree is mq,
this proves

```math
\|P-\Pi\|\le 1/m
```

without any Bol theory. Hence the norm exponent is not a new improvement over
the applicable existing spectral bound. The new application must be the
identification of an actual subloop average with this operator, plus exact
mixing/weight/conductor conclusions proved for that application.

## 3. Strong ablation: multiplicative closure is unnecessary for the graph

In (C2) replace H by ANY subset D of F, of cardinality m>1, even allowing 0.
The resulting looped graph remains regular of degree mq and has the same
exact spectrum and total-variation law. It need not arise from the Bol
subloop construction. This shows which analytic structure is doing the work.

For a nontrivial additive character psi, Fourier transform the s coordinate.
The unnormalized Fourier block on D x F is

```math
N_\psi((b,A),(c,B))=\psi(cA-bB).
```

Character orthogonality gives

```math
N_\psi^2((b,A),(e,E))
=q\,1_{b=e}\sum_{c\in D}\psi(c(A-E)).
\tag{C3}
```

The right side is q^2 times the projection onto the m Fourier frequencies
psi(c.) for each of the m first-coordinate fibers. Therefore

```math
N_\psi^3=q^2N_\psi,
\quad\operatorname{rank}N_\psi=m^2,
\quad\operatorname{tr}N_\psi=mq.
```

The eigenvalues are q with multiplicity m(m+1)/2, -q with multiplicity
m(m-1)/2, and 0 with multiplicity mq-m^2. The trivial central block is the
all-ones matrix. For the full adjacency matrix A_D,

```math
A_D^3=q^2 A_D+(m^2-1)qJ.
\tag{C4}
```

After division by (mq)^3 this is exactly
P^3=m^{-2}P+(1-m^{-2})Pi. The same identity and the same signed
multiplicities therefore hold for arbitrary D, not only multiplicative
subgroups or odd-order Bol data.

A direct common-neighbor count makes the two-step law transparent. For
v=(b,A,s) and w=(e,E,t):

- If b!=e, the number is m.
- If b=e and A!=E, the number is q when (t-s)/(A-E) is in D, and 0 otherwise.
- If b=e, A=E, s!=t, the number is 0.
- At v=w the number is mq.

Consequently, from every initial vertex,

```math
\|P^2(v,\cdot)-\pi\|_{TV}
=\frac{(q-1)(q-m+1)}{mq^2}.
\tag{C5}
```

This argument also demonstrates that the exact TV formula is part of the
finite incidence geometry, rather than a relation exclusive to Bol loops.

## 4. Relation to known partial geometric design machinery

Equation (C4) has the classical partial-geometric-design form
N N^T N=(beta-alpha)N+alpha J, with N=A_D, beta-alpha=q^2 and
alpha=(m^2-1)q. This is an identification, not a claim that the particular
slab design is historically new.

The identity appears as Lemma 2.4 of Song and Tranel,
*Partial geometric designs having circulant concurrence matrices*,
J. Combinatorial Designs 30 (2022), 420-460,
[DOI 10.1002/jcd.21834](https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21834).
Definition 2.1 and Lemmas 2.4 and 2.6 provide the conventions and spectral
framework. Their Section 3.8 discusses other symplectic constructions.

The primary paper Chai, Feng and Zeng,
*Constructions of 1 1/2-designs from symplectic geometry over finite fields*,
Acta Math. Sin. English Ser. 31 (2015), 1367-1378,
[DOI 10.1007/s10114-015-4716-4](https://link.springer.com/article/10.1007/s10114-015-4716-4),
is relevant prior art. Only its publisher abstract and bibliographic information
were accessible in this search; it announces constructions using isotropic
subspaces and generalized symplectic graphs. Its exact theorems were not
verified here, so this source prevents a confident priority claim but is not
used as a black box or asserted to contain (C2).

Targeted searches for Bol-loop/subloop random walks did not locate this
specific averaging/mixing statement. That absence is not a novelty proof.
The 2005 Markovski--Gligoroski--Markovski work on quasigroup transformations
and random walks concerns empirical string randomness, not this spectral
operator; it is not an applicable baseline for our theorem.

## 5. The actual acting group on a generic leaf is metabelian

On the fixed z leaf use coordinates (x,Z,b), where Z=b^{-1}s. Let

```math
G_z=(F^d\oplus F)\rtimes H,
\qquad a\cdot(v,c)=(av,a^{-1}c).
```

It acts regularly on (x,Z,b) by the standard affine left regular action.
The actual Bol translation indexed by (u,a,0) corresponds to

```math
k_z(u,a)=((u,-a^{-1}u\cdot z),a)\in G_z.
\tag{C6}
```

Indeed its coordinate action is
x'=u+ax, Z'=a^{-1}Z-a^{-1}u.z, b'=ab, exactly the normalized Bol action.
The set K_z of all these elements is inverse-closed, since

```math
k_z(u,a)^{-1}=k_z(-a^{-1}u,a^{-1}).
```

It generates G_z: the a=1 elements give translations along (u,-u.z), and
for a!=1, multiplication k_z(u,a) k_z(0,a^{-1}) gives translation
(u,-a^{-1}u.z). Their difference is a nonzero scalar multiple of u.z in
the second coordinate; since z!=0, that coordinate ranges over F. Together
these generate all translations and the torus.

K_z is NOT a subgroup. Its size is mq^d while |G_z|=mq^{d+1}; alternatively
the proved nontrivial eigenvalues +-1/m contradict idempotence of averaging
over a subgroup. Nevertheless S, the LABEL set in the original loop, IS
an associative subloop. The map S->G_z given by (C6) is not multiplicative.
The Bol identity guarantees the sandwich relation
L_x L_y L_x=L_{x(yx)} and hence twisted-subgroup closure of K_z; ordinary
multiplicativity is not claimed.

This is a complete group control: retain the group G_z and the marked
measure K_z and all spectral conclusions survive. Replace K_z by a genuine
subgroup and its uniform averaging is an orthogonal projection. Forget K_z
and keep G_z alone and the analytic operator is no longer specified.

The even-order case poses no problem. In particular, one must NOT write
L_(u,a,0)=L_(u,1,0)L_(0,a,0): the latter has central shear coefficient -a u.y,
whereas the former has -u.y. That incorrect factorization would erase the
essential section data and could falsely suggest a degeneracy at a=-1.

## 6. Honest contribution statement

The most defensible conclusion is an explicit sharp mixing theorem for
uniform averaging over a concrete associative subloop acting in a proper Bol
loop, with a coherent prime-power and local continuation when separately
proved. Its operator is a loop-selected twisted-subgroup measure inside
ordinary metabelian/finite-symplectic analysis. It does not improve the
known 1/m bound available from symplectic graph interlacing; it explains why
this particular loop average, unlike genuine subgroup averaging, mixes and
supplies exact laws and arithmetic refinements for it.

No literature-wide priority claim is warranted. The finite-field norm or
cubic polynomial alone should not be presented as a new metaplectic theory.

## 7. Local-field prior art: the full-unit exponent 3 has a classical baseline

The strongest directly applicable primary reference found is Bogdan Nica,
*Unimodular graphs and Eisenstein sums*, arXiv:1505.05034v2 (26 September
2016), published in Journal of Algebraic Combinatorics 45 (2017), 423--454:
https://arxiv.org/abs/1505.05034 and https://arxiv.org/pdf/1505.05034.
Definition 1.6, Theorems 1.7--1.8, and the proof of Theorem 1.8 in Section 6
were read. This is stronger relevant prior art than a general p-adic Radon
inversion citation.

For a finite valuation ring R=O/pi^A with residue cardinality Q, Nica's
projective incidence graph Um_0(R^4) has two copies of primitive vectors
modulo units as its vertex classes, with incidence x.y=0. One half has

```math
 Q^{3(A-1)}(Q^3+Q^2+Q+1)
```

vertices. Its degree is D_A=Q^{2(A-1)}(Q^2+Q+1), and its nonprincipal
adjacency singular values are Q^{2A-c}, 1<=c<=A. Multiplying one side by
the matrix of the standard symplectic form turns this into symplectic
polarity incidence without changing singular values.

Our effective full-unit graph is exactly the induced slab

```math
 [b:A:s:1],\qquad b\in R^\times,
```

with relation t-s=cA-bB. Its degree is
d_A=|R^\times||R|=(Q-1)Q^{2A-1}. Thus its normalized operator is the
compression of the ambient normalized incidence operator multiplied by

```math
 D_A/d_A=\frac{Q^2+Q+1}{Q(Q-1)}.
```

This is an exact identification, including over finite valuation rings.
In the compact inverse limit, the full-unit slab has positive measure in
projective three-space. The ambient conductor eigenvalues decay as Q^-c
and the dimension at conductor <=c grows as Q^{3c}. Consequently the
classical projective spectrum already implies an S^s upper bound for s>3
for this compression. This last implication is our inference from Nica's
finite theorem and the compatible inverse system, not a theorem attributed
verbatim to Nica. Exact slab multiplicities and endpoint failure still
require the orbit-flip calculation. One should not claim that exponent 3
is an unprecedented p-adic regularization phenomenon.

The general summation of symbol singular values is also established
machinery. Delgado--Ruzhansky, *Schatten classes and traces on compact groups*,
arXiv:1303.3914v2, Theorem 3.5 and Remark 3.6 (printed p.8), gives the exact
criterion for a compact invariant operator on a compact topological group:
sum over irreducibles of dimension times the Schatten power of the matrix
symbol. [Primary PDF](https://backoffice.biblio.ugent.be/download/8585438/8585439).
It does not compute our conductor orbit blocks or prove their compactness;
those are the family-specific inputs. After the blocks are known, the
Schatten summation is standard spectral theory.

Other primary references checked:

- Jonathan Wang, *Radon inversion formulas over local fields*,
  Mathematical Research Letters 23 (2016), 535--561,
  https://www.jonathanpwang.com/papers/Radon.inversion.pdf.
  Formula (2.1) and Theorem 3.2.6 concern inversion of integration over
  xi.x=1 between specified spaces of smooth K-finite functions with
  support conditions. They do not supply this compact slab's singular
  values, torus-rank dependence, or Schatten endpoint. No such result is
  inferred merely from the word Radon.
- J. P. Velasquez-Rodriguez, *Spectral properties of pseudo-differential
  operators over the compact group of p-adic integers and compact
  Vilenkin groups*, arXiv:1912.11407v1 (24 December 2019),
  https://arxiv.org/pdf/1912.11407. Theorem 5.3 gives Schatten criteria
  under a specified p-adic Hormander symbol-class hypothesis. No claim
  is made that our singular averaging operator belongs to that class;
  its exact spectrum is proved directly. This is background on the
  operator-ideal question, not a black box for the result.

Targeted primary-source searches for p-adic/non-Archimedean Radon,
symplectic averaging, compactness, and Schatten spectra did not locate
the exact torus-rank family below. This is a bounded search, not a proof
of priority.

## 8. Thin scalar groups provide a further arithmetic range

The canonical statement and proof are in
[the local manuscript](bol-section-local.md#thin-local-unit-groups-exact-rank-versus-smoothing-law).
For an unramified degree-f extension of Q_p, with p odd, take a rank-κ direct
Z_p-summand Λ of its ring of integers and the closed unit group
H_κ=μ_(Q-1) exp(pΛ), where Q=p^f and 1≤κ≤f. The exact Schatten threshold is
2+f/κ, while the mean-zero norm remains 1/(Q-1).

For κ<f this group has Haar measure zero inside the full unit group. The
positive-measure projective compression argument in Section 7 therefore does
not provide this theorem. Exact character orbit sizes give both the endpoint
failure and the number of steps needed for a square-integrable transition
kernel. The finite Teichmüller group is a noncompact control despite its same
mixing norm. These consequences give a precise distinction between mixing
rate and high-conductor smoothing, with compatible finite quotients at every
level.

The Bol data selects actual subloop translation averages and coherent
arithmetic models. The spectral proof remains ordinary Fourier analysis of a
marked section in a metabelian group. No new local metaplectic cover,
automorphy, or Euler product is asserted.

