# From the alternating-form Bol construction to an analytic operator

Mira Cult

## Scope and inspected sources

This source records the inspected inputs, proves the scalar-character reduction,
and identifies exactly which part of the Bol construction is used in the
[finite mixing theorem](bol-section-mixing.md) and
[arithmetic spectral theorem](bol-section-local.md). It allocates no permanent
claim IDs. The loop-classification interfaces below are imported research
results, not independently re-proved here. The two analytic manuscripts instead
verify their proper Bol family directly.

The source inventory is pinned as follows.

| Input | Inspected revision and locator |
| --- | --- |
| math-wip integration tree and protocol | commit c13096ff4a3e1f07303fd9f9b42adb358ed1688a; AGENTS.md, RESEARCH_PROTOCOL.md, research-by-alternation skill, research index and problem-0323 required files |
| Active classification workspace | PR #431, head 34d2ead9923cfb7d8092120c578b13a83e3ced2e; current PR handoff |
| Modular/fusion workspace | PR #438, delivery 6a605decda125c2fa18e36b90b8615d9c3b2ee50; BOL_MODULAR.md and charged-sewing review; scientific source 197d13d4ac2e48763ed20bf418228d7b4d16aa8c |
| Public alternating construction | Mira-Cult/math f54b5376cb098e52d56ba0e599598d92ff6978a3; manuscript 0025, blob 5a330688fde924a0590a8438c5319379a2b78f5b |
| Underlying alternating family | same public revision, packet/manuscripts/odd-alternating-form-family.md, blob 280882c2a46a0dff0f8a0af147ca6cf961940ff1 |
| Class-two folder interface | same public revision, packet/manuscripts/odd-class-two-classification.md, blob a8d0e17af1eb9af97d629e54871c6e4bc4616e3d, equations (6), (7)--(10), (14)--(15) |
| Quasi-RH source | openai/math adc7f1241b42e322a6451854ab7e4b4c146bf78a; PDF blob 8132b77eeb270a70b25df8d6609f008e83e65d91; build/paper.tex blob 268c4e3206d460c617d3d2129742a72b831b3def |
| Finite quantization | Gurevich--Hadani, arXiv:0705.4556v4, 20 August 2009 |
| Weil exponential sums | Gurevich--Hadani, arXiv:math/0612765v2, 8 February 2010 |

The integration tree does **not** yet contain BOL_MODULAR.md. Its named source
was read on the separately owned PR #438 branch. Unpublished files in another
worker's local checkout are not adopted as reviewed source.

The alternating-family draft imports the normal-form/isomorphism interface at
226a8dc1eb503026c350ffe3b7ac93da9077a593, symmetric factorization at
7fbfbc5a56f4bb1ead9a4d6202c2d948a67950d8, and restricted-section/properness
inputs at 722ba8c289c96dfd87c98f9a5ab3dcb8b2080998. The public packet explains
their use, including the full-transversal quadratic test and strict normal
subgroup defect test. Our intake checks those statements and their use in the
displayed construction; it is not an independent certification of their
exhaustion, simplicity, G-loop or strict isomorphism conclusions.

## 1. The actual center-valued bimap

Use the public notation: distinct odd primes p,q with p dividing q-1,
r=ord_q(p), E=F_(p^r), W=E^n, Z=F_p^k. The alternating matrices
B_1,...,B_k are F_p-linearly independent and have zero common radical.
The construction sets

```math
 \beta(x,y)=\bigl(\operatorname{Tr}_{E/\mathbb F_p}(x^\mathsf T B_i y)\bigr)_i,
 \qquad
 \Omega((x,y),(x',y'))=\beta(x,y')+\beta(y,x').
```

The class-two group on U×Z, U=W⊕W, has multiplication

```math
 (u,z)(v,w)=(u+v,z+w+\tfrac12\Omega(u,v)).
 \tag{A1}
```

This step is ordinary class-two group construction. Biadditivity gives the
2-cocycle identity and hence associativity in (A1); alternation gives the
commutator Ω. Trace nondegeneracy shows that Ω has zero
common radical and its values span Z, so its center and derived subgroup are Z.

### Proposition A: all scalar ranks and radicals

Fix ψ_p(t)=exp(2πit/p). Every central character is uniquely
ψ_ν(z)=ψ_p(ν·z), for ν∈F_p^k. Write

```math
 B_\nu=\sum_i\nu_i B_i,\qquad s_\nu=\operatorname{rank}_E B_\nu.
```

Then the F_p-valued alternating form Ω_ν=ν·Ω has

```math
 R_\nu=\operatorname{rad}\Omega_\nu
       =\ker_E B_\nu\oplus\ker_E B_\nu,\qquad
 \operatorname{rank}_{\mathbb F_p}\Omega_\nu=2rs_\nu.
 \tag{A2}
```

**Proof.** Pair (x,y) first with (0,v) and then with (v,0). Vanishing for all v
gives Tr(x^T B_νv)=Tr(y^T B_νv)=0. Replacing v by tv for all t∈E and using
the nondegenerate trace pairing gives x^TB_ν=y^TB_ν=0. Alternation identifies
these left kernels with the ordinary kernels. Each E-kernel has F_p-dimension
r(n-s_ν). Subtracting twice this dimension from 2rn proves (A2). ∎

For ν≠0, F_p-independence gives B_ν≠0, hence s_ν≥2. It gives **no**
nondegeneracy assertion. The exact rank strata are

```math
 \Sigma_s=\{\nu\in\mathbb F_p^k:\operatorname{rank}_E B_\nu=s\}.
 \tag{A3}
```

They are determined by the appropriate minors (or alternating Pfaffian minors)
of the matrix pencil, evaluated only at F_p-valued parameters. If n is even,
the full-rank complement is det(B_ν)≠0; the determinant can vanish identically.
For odd n every scalar specialization is degenerate.

Two admissible linear-algebra controls show why the exceptions matter.

- For n=4, k=2, B_1=diag(J,0), B_2=diag(0,J), with
  J=[[0,1],[-1,0]], the common radical is zero. The E-rank histogram is
  rank 0 once, rank 2 at 2(p-1) characters, rank 4 at (p-1)^2 characters.
- For n=3, take B_1 supported on coordinates (1,2) and B_2 on (2,3).
  Their common radical is zero, but every nonzero pencil member has rank 2.
  Thus every nontrivial scalar specialization remains singular.

These controls fit the alternating-input hypotheses over any admissible E.
Their identification with simple proper loops remains conditional on the
public construction interfaces; their rank statements are unconditional.

### Heisenberg quotient, including the discarded radical labels

For ν≠0 form

```math
 H_\nu=(U/R_\nu)\times\mathbb F_p,\qquad
 (\bar u,z)(\bar v,w)=(\bar u+\bar v,z+w+\tfrac12\Omega_\nu(u,v)).
```

The map (u,z)↦(ū,ν·z) from (A1) to H_ν is a group homomorphism.
The ordinary Stone--von Neumann representation with central character ψ_p
has dimension p^(rs_ν). Pullback gives the representation on which R_ν acts
trivially. It is not the entire original central-character sector.

Every linear character χ of the F_p-space R_ν gives a different irreducible
representation of (A1) with central character ψ_ν. Choose an F_p-linear
extension ℓ of χ's exponent to U and twist the pulled-back Heisenberg
representation by ψ_p(ℓ(u)). Its dimension is p^(rs_ν); different extensions
with the same restriction give equivalent representations, by nondegeneracy
on U/R_ν. Conversely Schur's lemma on the enlarged center of the central
pushout gives exactly these labels. There are
p^(2r(n-s_ν)) such irreducibles. Their characters vanish off R_ν×Z and equal

```math
 p^{rs_\nu}\psi_p(\nu\cdot z+\ell(u))
 \quad\text{on }R_\nu\times Z.
 \tag{A4}
```

For ν=0 all representations factor through the abelianization U and are
one-dimensional. Thus the zero charge and each radical character must be
included in any claimed uniform operator decomposition.

A single quotient forgets ker ν inside Z, the radical R_ν, the other pencil
members, and their mutual positioning. Abstract symplectic isomorphism of the
quotients remembers only the scalar rank. Even every individual rank histogram
can omit the relative kernels and the marked stabilizer/cocycle information.

## 2. Symmetries, the stabilizer, and actual section operators

The construction's internal A_q actor sends (x,y) to
(λx,λ^(-1)y). It preserves Ω and fixes Z pointwise. A_p acts trivially on P.
The swapping involution τ also fixes Z and preserves Ω. These preserve each ν
sector and R_ν; they need not fix every radical-character label χ. A full
sector model must either restrict to the stabilizer of χ or retain its orbit.

More generally a bimap automorphism (T,M) with
Ω(Tu,Tv)=MΩ(u,v) sends ν to ν∘M^(-1). It preserves an individual central
character precisely when that character is fixed by the dual action. The
public strict tuple isomorphisms permit coordinate permutations of Z together
with semilinear congruence; they do not permit arbitrary unmarked changes of
basis in the tuple. Their center permutation can permute ν sectors. On the
q-factor its center similitude likewise changes its central characters.

The actual stabilizer is the first-axis group S times the graph F of
f(a,c^t)=(a,t). Even after scalarizing P and Q, the graph imposes phases
ψ_p(ν·a)ψ_q(ρt) as well as the torus operators. In a representation π of G,
the H-fixed subspace is the range of |H|^(-1)Σ_(h∈H)π(h). Requiring first-axis
invariance and the graph equation is essential; arbitrary vectors in an
unrelated symplectic quotient need not occur in this induced representation.
Frobenius reciprocity computes their multiplicity as dim π^H. No extension of
a chosen radical-labeled representation to all of G is assumed here.

On the genuine permutation representation on G/H, section elements k_x act
as the actual left translations of the loop. If k_xk_y=k_(x∘y)h_(x,y), then

```math
 U_xU_y=U_{x\circ y}\rho(h_{x,y}).
```

The correction is an actual stabilizer permutation. It cannot generally be
discarded. For our selected restricted family, Proposition C of the finite
manuscript computes the correction shears and proves their coherence
explicitly. The Bol sandwich identity survives without asserting ordinary
multiplicativity of x↦U_x.

## 3. Why the selected family is a legitimate transfer

Public manuscript 0025, equation (8), displays the proper section

```math
 (u,t,s)\circ(v,a,h)=(u+\eta^t v,t+a,s+h-\gamma(u,v))
```

on F_q^2×C_p×F_q. This is the seed of our theorem. We independently extend
this displayed law to every symplectic dimension, every scalar subgroup of
units, finite valuation rings and the stated compact local groups. We prove
its loop, Bol, inverse and non-Moufang properties. Higher-dimensional or
even-order extensions are not asserted to be subloops of every simple folder.

The analytic operator uses an actual isotropic axis and actual left
translations. The selected labels form an associative subloop, but their
translations on the ambient loop acquire nonzero central shears. Their
average is therefore not a subgroup-averaging projection. This is the
loop-theoretic reason to investigate the operator.

[The controls](bol-section-controls.md) show the precise limit of that
contribution. Keeping the corresponding marked subset in an ordinary
metabelian acting group preserves the whole operator. The finite incidence
identity even survives arbitrary sets of scalar labels without multiplicative
closure. Thus this is a selected analytic family inside established harmonic
analysis, not a uniquely Bol identity or a new Weil representation.

## 4. The applicable analytic literature and the tested routes

Gurevich--Hadani's quantization paper, §§2.2--2.4 and §2.7, supplies canonical
normalized intertwiners for oriented Lagrangian models, their exact
multiplicativity, tensor products, duality and symplectic reduction. These are
appropriate standard tools after (A2), not a source of a nondegeneracy theorem
for the original vector-valued pencil.

Their self-reducibility paper, Theorems 3.1--3.4, treats Wigner coefficients
of torus character vectors. For an inert maximal torus in Sp(2N,F_Q), the
unit-vector bound is 2Q^(-N/2). The general bound retains the character
multiplicity and symplectic-rank factor; the displacement must avoid proper
torus-invariant subspaces. The quadratic-character multiplicity exceptions
are also explicit. A cyclic scalar action in our section is not automatically
such a maximal symplectic torus, and an arbitrary section average is not a
torus-eigenstate matrix coefficient. We do not apply that bound outside its
hypotheses.

Johnson--Smith, *Matched pairs, permutation representations, and the Bol
property*, §§6--7, already constructs doubly stochastic homogeneous-space
matrices and Bol actions from ordinary group actions. The particular
spectral/mixing calculation here is an application beyond that stated
stochasticity result, not the invention of Bol permutation operators.

For the finite walk there is an even closer baseline: the symplectic polar
graph eigenvalues in De Bruyn--Goryainov--Haemers--Shalaginov,
arXiv:2404.09902v1, §2.4, Lemma 4, already imply norm ≤1/m by interlacing.
Our exact TV, optimal weighting and arithmetic refinements must be compared
with that baseline, not just the triangle bound 1. Nica's
*Unimodular graphs and Eisenstein sums*, arXiv:1505.05034v2, Theorem 1.8,
already gives conductor-dependent spectra for projective incidence over
finite valuation rings. Full-unit conductor decay is therefore not presented
as an unprecedented p-adic Fourier phenomenon. The actual operator,
its affine restriction, precise multiplicities, point-start mixing and
thin-unit rank dependence are specified and proved in this work.
Historical priority for those combined conclusions has not been established.

### What the existing modular construction already supplies

The pinned PR #438 checkpoint records several actual analytic objects, rather
than merely a proposed moonshine analogy. Its modular rank shadow constructs
weight-four Eisenstein forms with rank-recovering cusp data. Its exterior-Fock
construction gives integral graded traces and an exact fusion-channel trace
identity. Those integral coefficients can be signed; integrality is not a
positivity principle for a section-operator norm. The channel identity also
holds for general elementary abelian central sets, so it does not by itself
supply a new Bol-specific cancellation estimate.

The charged-sewing handoff adds coherent Gaussian contractions through singular
blocks, zero-mode bordered determinants, and analytic sewing conditional on a
trace-class boundary operator. Its non-Gaussian repair is a standard dynamical
Felder kernel with a position-flat connection and an explicit modular gauge
law. The checkpoint does not identify that kernel with the original trace
functions or complete the required charged dynamical fusion functor.

There is a precise obstacle: the existing constant charged intertwiners do not
transport the two separate traceless Cartan parameter spaces through the fusion
coordinate change. The stated finite functional equation forces their
intersection to be constant. A separate naturality theorem collapses ordinary
primitive exchange to the scalar degree channel; it explicitly does not rule
out dynamical shifts or narrower marked categories. Thus parameter-dependent
maps, their pullbacks and connection transport, and the full zero-charge,
carry and genuine-dual channels remain obligations of that separate route.
These are attributed findings at the inspected reviewed checkpoint, not newly
certified theorems of this manuscript. Our direct section-average argument
uses none of them and supplies its own compatible local measures and spectrum.

| Route | Deep test and outcome | Decision |
| --- | --- | --- |
| One scalar Heisenberg quotient | Radical formula (A2); counterexamples to uniform regularity | Required baseline and bookkeeping |
| Full-vector section average | A change of variables removes dilation and leaves an ordinary alternating Fourier transform | Does not meet the endpoint |
| Lagrangian-subloop average | Nonmultiplicative correction shears; exact frequency blocks and point-start TV | Pursued and proved |
| Fixed Teichmüller arithmetic lift | Uniform gap survives all depths, but fixed nonzero eigenvalues have infinite multiplicity | Useful noncompact control |
| All-unit and thin-unit arithmetic lift | Character orbit sizes grow with conductor; exact transpose blocks give compactness and sharp Schatten threshold | Strongest spectral result |
| Charged modular fusion | Existing reviewed source has explicit connection/fusion and fixed-marking obstructions | Remains separately active; not used as an unpaid premise |

## 5. What metaplectic machinery the quasi-RH paper actually uses

The inspected 199-page quasi-RH source does not use a finite Heisenberg or Weil
representation as an explicit input. Its metaplectic starting point is global
cubic theta over the Eisenstein field. In the paper's chosen primary
normalization, the Kubota multiplier on its congruence subgroup is a cubic
residue symbol, with a separate c=0 branch. The theta expansions at three
cusps involve Bessel K_(1/3), cubic Gauss coefficients and squarefree-times-cube
indices. Those cusp expansions and their transformations carry the analytic
content; finite Fourier transforms subsequently keep the masks and local
character factors consistent.

The specific mathematical work inspected is:

- Proposition 5.1, printed pp.24--33: a completed cubic-theta reflection for a
  smooth coefficient sum, with a Mellin kernel whose gamma factors involve
  1±1/6. The character acts on the whole index nb^3, including zeros on
  nonunits. Active primes alter the conductor and the dual scale. It is not
  a separate product of unrelated finite-field Fourier identities.
- Corollary 14.1, pp.92--94: divisibility marks on the same whole index are
  expanded by compatible active/inactive branches. The exact pair phases
  are needed before applying a norm bound.
- Lemma 14.2, pp.94--96: a mixed quadratic--cubic large-sieve norm is bounded,
  in the paper's notation, by
  (KNBL)^epsilon (K+NB) B {N+L+(NL)^(2/3)}. Its coefficients have stated row,
  tuple and column independence; arbitrary pair-dependent coefficients are
  not covered. The argument uses quadratic and cubic large sieves after
  resolving the moving coprimality masks.
- The later comparison combines these reflected sums with masked Poisson
  transforms and norm/moment estimates. Local Fourier unitarity alone does
  not give the coefficient-independence, global reflection or arithmetic
  large-sieve assertions.

This is a mechanism audit of the cited sections, not independent verification
of the paper's claimed global zero-free theorem.

The finite Heisenberg representation lives over a finite scalar alternating
space. The ordinary local oscillator construction gives the double
metaplectic setting. The quasi-RH input is a cubic cover and a global
automorphic theta coefficient system. Under a proposed identification in one
cohomology group with compatible scalar coefficients, a pulled-back/pushed-out
quadratic extension class remains 2-torsion; it cannot equal a nontrivial
3-torsion cubic class. Rephasing a section changes a coboundary, not this
obstruction. This rules out that specific shortcut, not every possible
arithmetic relationship.

A cubic bridge would need an independently specified cubic Hilbert-symbol
cocycle, its local conductor and splitting conventions, compatible local
representations, a global splitting and theta realization, and the actual
masked reflection/norm estimates for its coefficients. Our integral proper
section supplies none of those global assertions. Its proved local
spectral theorem is instead a direct arithmetic application with explicit
reductions, Haar measures and conductor strata.

## 6. Sharp remaining obligation

The achieved transfer is an exact mixing/spectral theory for a concrete
proper-section family and its local arithmetic continuation. It does not yet
produce a bound controlled by the genuinely vector-valued tuple B together
with its full reciprocal stabilizer graph.

A concrete next attack is to average a section using a proper vector subspace
or a graph constrained by the actual B_i, so that Fourier orthogonality leaves
several coupled images B_ν y rather than one scalar orbit. First determine the
Gram kernel exactly. Then seek an estimate using joint rank strata and
intersections across ν that improves the best incidence/large-sieve bound for
that precise family. The required success test is a quantitative consequence
that survives retaining the full graph, and changes under a controlled change
of that marked data. Merely recovering individual ranks or invoking the known
scalar polar-graph gap would not resolve that next obligation.

The alternative arithmetic bottleneck is a coherent lift of the **full**
two-prime folder. The naive fixed-rank prescription would require arbitrarily
large p-power roots of unity in one fixed q-adic field and arbitrarily large
q-power roots in a fixed p-adic field. Their prime-to-residue-characteristic
torsion has bounded order, so that particular prescription fails. The proper
section's integral model is a valid repair for the present analytic target;
it is not a construction of that full simple-folder lift.

