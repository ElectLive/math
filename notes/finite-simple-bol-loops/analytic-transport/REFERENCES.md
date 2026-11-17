# References

Source key **ALGEBRA.SIMPLE_PROPER_BOL**; stable problem ID **0323**.

## Sources

Primary construction baselines below; scope and review limits are recorded separately.

### N07

Gábor P. Nagy, *A class of simple proper Bol loops*, arXiv:math/0703919v1, 30 March 2007.
[Primary version](https://arxiv.org/html/math/0703919v1).
- §1: left/right Bol conventions, proper meaning non-Moufang, and comparison with the finite simple Moufang classification.
- §2: Bol folders, multiplication groups and normal-subloop arguments.
- §§3–4: exact-factorization construction and simple proper examples.

Used as a construction baseline, not a complete classification. The abstract's historical existence question is answered by the paper itself and must not be repeated as still open.

### N07E

Gábor P. Nagy, *A class of finite simple Bol loops of exponent 2*, arXiv:0709.4544v1, 28 September 2007.
[Primary version](https://arxiv.org/html/0709.4544v1).
- Abstract and §1: infinite right-Bol exponent-2 family; right multiplication group an extension of an elementary abelian 2-group by S5; smallest member of this family has order 96.
- §§3 and 5: initial construction and infinite family.

Translate right to left using the opposite operation, as specified in PROBLEM.md. Use N07 §1 for the standard Bol identities rather than copying ambiguous or typographically suspect formulas from rendered sources. The 96 statement is family-specific.

## Source and review limits

These two primary versions were inspected for problem intake on 2026-11-13. Their arguments have not been independently re-proved or formalized in this workspace. A comprehensive subsequent-literature audit, including equivalences and possible overlaps among constructions, remains a first research obligation. No claim that every narrower classification question remains open is made.

Mira's request fixes the unrestricted non-Moufang classification as its own problem rather than an instance of a Moufang classification or a generic discovery-engine benchmark.

## JS: simple Bol permutation rank

Johnson–Smith, On the smallest simple, unipotent Bol loop, §§1.1,2.1 ([author PDF](https://jdhsmith.math.iastate.edu/math/BolBoolf.pdf)). The full multiplication-group double-transitivity question is adopted; the precise loop-character-theoretic conjugacy bridge requires checking before an equivalence claim.


# Bol modular continuation: literature audit and architectural consequences

Source check conducted 2026-11-15 by model participant 2.
This is a scoped audit, not a proof of novelty or a complete literature search.
The formulas in [the cubic-isotope manuscript](manuscripts/bol-cubic-isotopes.md)
were derived during this investigation; historical priority for the uniform
coordinate and trace formulas has not been established.
The two order-27 isomorphism types have now been identified with known loops,
as detailed below.

## Code-loop precedent: what was actually checked

**[DV10]** A. Drápal and P. Vojtěchovský, *Code loops in both parities*,
Journal of Algebraic Combinatorics **31** (2010), 585--611.
[Author-hosted preprint](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-0809.pdf).
Checked: §1; Lemma 2.2; Definitions 3.1--3.4; Proposition 4.3 and Theorem 4.4;
Theorem 5.6; §6.1 and Lemma 6.4; Propositions 7.3, 8.1 and Theorem 8.2;
§9; §10.3. Locator numbers refer to this preprint.

The introduction identifies the Parker loop's role in Conway's construction and
Richardson's odd-code-loop p-local work. In characteristic two, the code-loop
structure is controlled by a cubic polarization datum; in odd characteristic
the form model is a central extension with a symmetric characteristic trilinear
form `f` and `theta(u,v)=f(u,u,v)/2`. The four definitions are equivalent by
Theorem 8.2. Section 6.1 proves that Richardson's definition lies in this class,
but the converse fails. Odd code loops are conjugacy closed, not generally
Moufang or Bol. These source facts motivate the obstruction below rather than
an identification with the simple proper Bol examples.

**[G86]** R. L. Griess, Jr., *Code loops*, Journal of Algebra **100**
(1986), 224--234,
[DOI](https://doi.org/10.1016/0021-8693(86)90075-X).
The [institutional PDF](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/26195/0000274.pdf?sequence=1)
and its alternative institutional URL returned access errors in this session.
The original proof was therefore **not independently inspected**. Its binary
construction is used here only through the explicitly inspected treatment [DV10],
not as a newly checked theorem of [G86].

**[R95]** T. M. Richardson, *Local subgroups of the Monster and odd code loops*,
Transactions of the American Mathematical Society **347** (1995), 1453--1531,
[DOI](https://doi.org/10.1090/S0002-9947-1995-1266532-4).
The [original AMS PDF](https://www.ams.org/journals/tran/1995-347-05/S0002-9947-1995-1266532-4/S0002-9947-1995-1266532-4.pdf)
and article page could not be retrieved. Consequently the exact p-local-group
construction is **unverified here and is not used as a mathematical premise**.
The historical connection and the odd-loop definition are attributed to the
checked [DV10, §1 and §6.1], which cites [R95, pp. 1468--1469] for elementary
loop properties. No group shape or embedding theorem from [R95] is asserted on
the basis of search snippets.

## A precise obstruction to directly importing odd code loops

**Proposition.** Let `Q` be a central extension of an abelian group `V` by an
abelian group `Z` having no nonzero element killed by 2. Suppose its associator
descends to a triadditive map `A:V^3 -> Z` symmetric in its first two variables.
If `Q` is left alternative, then `Q` is associative. In particular an odd code
loop in the [DV10] form model is left Bol if and only if it is an elementary
abelian group.

**Proof.** Left alternativity gives `A(x,x,z)=0`. Expand
`A(x+y,x+y,z)=0` using triadditivity and symmetry. The result is
`2A(x,y,z)=0`. The hypothesis on `Z` implies `A=0`, which is associativity.
Left Bol implies left alternativity by setting the middle variable to the
identity. In the form model, `A=f` by the defining cocycle calculation;
therefore `f=0` and `theta=f(x,x,y)/2=0`. The multiplication is elementary
abelian. Conversely such a group is left Bol. This is an elementary consequence
of the stated architecture; no claim of a new general no-go theorem is made.

The proof suggests an actual repair: allow associators alternating in the first
two inputs. [The cubic family (S1)--(S2)](manuscripts/bol-cubic-isotopes.md) implements this repair and leads to the
nontrivial ablation results there. Characteristic two escapes the argument
because multiplication by 2 is zero; this explains why the familiar Parker-loop
precedent does not transfer literally to odd proper Bol loops.

## Existing representations: genuine foundations and information loss

**[S07]** J. D. H. Smith, *Four lectures on quasigroup representations*,
Quasigroups and Related Systems **15** (2007), 11--42;
[author's corrected local PDF](https://jdhsmith.math.iastate.edu/math/4LQR.pdf).
Checked: §§2.2--2.3 and §§4.1--4.2, particularly §§2.2.4, 2.3.1,
4.2.1--4.2.5. The local PDF has 30 pages, so section numbers are the stable
locators used here.

Smith's modules are abelian group objects over the quasigroup in a specified
variety. Universal stabilizers give a group-based description (§4.2.4);
identities impose relations through quasigroup differentiation (§4.2.5).
Thus inventing abelian-extension modules or universal stabilizers alone would
rediscover established foundations. Combinatorial characters instead use
orbits of the multiplication group on ordered pairs. They have orthogonality,
but all finite rank-two quasigroups of a fixed order have the same character
table (§2.3.1). This is a concrete limitation for a classification invariant.
Marked translations, their products, and their defect words retain additional
data; calling an arbitrary group representation a loop representation would
not establish that retention.

**[FS96]** T. S. R. Fuad and J. D. H. Smith, *Quasigroups, right quasigroups
and category coverings*, Algebra Universalis **35** (1996), 233--248;
[author-hosted original](https://jdhsmith.math.iastate.edu/math/QRQCC.pdf).
Checked: Definition 1.3, Definition 1.4, and Theorem 4.6 (p. 243).
Theorem 4.6 equates quasigroup modules, modules of the universal stabilizer,
representations of the fundamental groupoid of the labeled Cayley diagram,
and appropriate abelian coverings. A labeled-geometry or groupoid foundation
therefore has substantial precedent. No claim that an unmarked covering graph
reconstructs the loop follows from this theorem.

## What forces classical moonshine

**[B92]** R. E. Borcherds, *Monstrous moonshine and monstrous Lie superalgebras*,
Inventiones Mathematicae **109** (1992), 405--444;
[author-hosted original](https://math.berkeley.edu/~reb/papers/monster/monster.pdf).
Checked: Theorem 1.1, Theorems 6.1--6.2, §§7--9, particularly (8.3) and (9.1).

The theorem starts with the Frenkel--Lepowsky--Meurman graded representation.
The no-ghost theorem identifies the doubly graded pieces of the Monster Lie
algebra with the required module pieces. A twisted denominator identity then
couples traces of powers of each Monster element across grades; (8.3) is the
decisive relation. Section 9 uses these relations and initial coefficients of
all relevant powers to identify the genus-zero functions. Five coefficients of
one isolated trace are insufficient, as the paper explicitly explains.

For the present investigation, eta modularity from symmetric powers is an
established analytic mechanism. What requires proof is that the *marked family*
obeys useful identities or reconstructs loop data. A Bol relation inherited by
its operators is meaningful, but it is not yet a counterpart of Borcherds's
denominator recursion. No Monster module, genus-zero property, or sporadicity
is produced by merely attaching oscillator spaces to finite permutations.

## Status of the proposed contribution

**[GKV27]** A. Grishkov, M. Kinyon and P. Vojtěchovský, *Bol loops of order 27*,
International Journal of Algebra and Computation **36** (2026), no. 2, 191--205,
[DOI](https://doi.org/10.1142/S0218196726500049),
[author-hosted version](https://cs.du.edu/~petr/data/papers/bol_loops_of_order_27.pdf),
accessed 2026-11-15. Checked: §1, §3 including Tables 1--2, and Theorems 5.1,
5.3. The authors work with right Bol loops. Their complete classification and
Table 1 identify our `Q_0,Q_1` at `p=3` as the opposites of `B_6,B_2`: each has
center order 3 and 14 elements of order 3, and Bruck status selects the row.
The source already records this pair as isotopic. Thus the order-27 loops and
their isotopy are rediscovered controls, not new examples. The proof and
coordinate formulas in this continuation remain self-contained.

**Inherited:** central-extension arithmetic; the code/form precedent; abelian
group objects and universal stabilizers; oscillator determinant and eta
identities; the general fact that marking translations can preserve a loop.

**Derived in this continuation:** the explicit cubic `Q_k` presentation,
its principal-isotope formulas, conjugate left multiplication group/stabilizer,
equal marked associator-defect traces, and the inverse-property trace separating
its two isomorphism classes. These statements have symbolic proofs and exact
small-instance calculations. The p=3 isomorphism types and their isotopy are
known as just noted; historical novelty of the remaining formulas and trace
comparison is unverified.

**Graded continuation:** the [translation-class seed](manuscripts/bol-translation-class-fusion.md)
and [fermionic construction](manuscripts/bol-fermion-sewing.md) now realize the
phase sectors in one graded Bol object, with integral modular isotope traces,
actual multiplication currents, fusion-projector modular functions and a
central-class reconstruction theorem. Their elementary class-two scope and
inherited source dependencies remain explicit. A closed genus-one system for
more general current correlations, a VOA structure, and a loop-derived
denominator identity remain unresolved. The earlier rational Eisenstein
functions are not being reinterpreted as traces of this new object.
A broad search did not locate an existing proper-Bol moonshine theorem, but
search absence is not evidence of novelty or nonexistence.


## Modular analytic sources


- Nils R. Scheithauer, *The Weil representation of SL_2(Z) and some
  applications*, IMRN 2009, no. 8, 1488–1545: sections 2, 4 and 5 give the
  general finite quadratic module, Weil representation and modular-lift
  framework. Author PDF: https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/scheithauer/publications/Weil_representation.pdf .
  Its sign convention is dual to some other references; this note proves its
  displayed convention independently by the permutation model.
  For the graded continuation, section 6, Propositions 6.1--6.2 (printed
  pp.29--30) give the eta transformation and rescaling formulas used at cusps;
  these locators were checked against the author PDF on 2026-11-15.
- Markus Schwagenscheidt, *Eisenstein series for the Weil representation*,
  J. Number Theory 193 (2018), 74–90; arXiv:1803.10550v2; DOI
  10.1016/j.jnt.2018.05.014. Its section 1.1 defines the general vector-valued
  Eisenstein series; more general Fourier coefficient formulae are standard.
  https://arxiv.org/abs/1803.10550v2 . The exact hyperbolic specialization above
  is proved directly rather than cited as novel.

These sources establish antecedents, not novelty of the loop-specific packet.

## Moufang control

**[NV03]** G. P. Nagy and P. Vojtěchovský, *Octonions, simple Moufang loops
and triality*, Quasigroups and Related Systems **10** (2003), 65--94;
[author-hosted version](https://cs.du.edu/~petr/data/papers/octonions_simple_Moufang_loops_and_triality.pdf).
Checked on 2026-11-15: §4.1, Theorem 4.1 (Paige), giving the nonassociative
simple Moufang loop of norm-one Zorn matrices modulo the center, of order
`q^3(q^4-1)/gcd(2,q-1)` over F_q. Only this construction and its Moufang and
nonassociative properties are used as symbolic controls here. The paper's
global classification and its finite-simple-group dependencies are not needed.

## Graded Bol continuation: fermions and the VOA boundary

The following original research sources were opened during this continuation.
They delimit what is inherited and what would be required for a future VOA
claim; the elementary eta/current proofs do not invoke their deeper theorems.

- **Bakalov--Horozov--Yakimov**, *Highest weight modules over W_(1+infinity)
  algebra and the bispectral problem*, [author preprint, v2](https://arxiv.org/pdf/q-alg/9602012v2),
  Appendix, equations (A.1)--(A.4), printed p.20. These give the CAR,
  fermionic matrix-unit action, and the additional normal-ordering step
  required for a centrally extended infinite-matrix algebra. Our finite-mode
  sums use the elementary matrix-unit identity, not that central extension.
- **Dong--Li--Mason**, *Modular-invariance of trace functions in orbifold
  theory*, [author preprint, v2](https://arxiv.org/pdf/q-alg/9703016v2), Theorem 5.4
  and equations (5.8)--(5.10), printed pp.29--30; Theorem 10.1, printed p.43.
  The modular action is on torus one-point-function spaces with transformed
  commuting pairs. Identifying those spaces with twisted-module traces uses
  the stated rationality and C2 hypotheses. A graded CAR representation alone
  does not establish these VOA hypotheses or the differential identities.
- **Dong--Ren**, *Congruence Property in Orbifold Theory*,
  [author preprint, v1](https://arxiv.org/pdf/1610.05291v1), Theorem 4.1 and Lemma 4.3,
  printed pp.6--7. The congruence-kernel theorem assumes a regular, selfdual
  VOA of CFT type and a finite automorphism group. This is a possible future
  bridge, not a theorem automatically applicable to the present object.
- **Duncan--Mack-Crane**, *The moonshine module for Conway's group*,
  Forum Math. Sigma 3 (2015), e10, [original article](https://doi.org/10.1017/fms.2015.7),
  section 4.3, equations (4.19)--(4.20), Lemma 4.6, printed pp.33--34, and
  Lemma 4.8, printed p.36. Fermionic eta traces are a genuine precedent;
  the distinguished super-VOA, twisted sector and subsequent trace identity
  are additional structure responsible for its much stronger moonshine
  conclusion. Sharing an exterior-product formula does not import that
  structure into a Bol loop.

For a detailed accessible exposition of the finite bilinear CAR identity, see
also Alexandrov--Zabrodin, *Free fermions and tau-functions*,
[author preprint, v3](https://arxiv.org/pdf/1212.6049v3), section 2.1,
equations (2.1)--(2.5), printed p.6. This source explicitly reviews the
established free-fermion formalism; it is not a priority claim for A7.

## MTZ07

Geoffrey Mason, Michael P. Tuite and Alexander Zuevsky, *Torus n-Point
Functions for R-graded Vertex Operator Superalgebras and Continuous Fermion
Orbifolds*. [arXiv:0708.0640v1, 4 August 2007](https://arxiv.org/html/0708.0640v1);
[MPI preprint PDF, dated 31 August 2007](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/103.pdf).
Inspected during the genus-one continuation on 2026-11-15 by
model participant 2 and model participant 5. The HTML and MPI PDF equation
numbering differ; proposition numbers provide stable locators.

- Section 2.2: twisted bilateral series, Proposition 2.7 (holonomy modular
  covariance), Proposition 2.16 (theta/prime-form expression). In the MPI
  PDF the corresponding equations are (20), (35), and (49); the arXiv HTML
  labels them (36), (58), and (101).
- Proposition 6.4: complex-fermion determinant correlation formula, equations
  (127)--(128) in the MPI PDF, (199)--(200) in the HTML.
- Proposition 6.6: treatment of the trivial flat line/zero-mode case.
- Propositions 6.12--6.14: partition and correlation modular laws, with their
  multipliers and transformed commuting boundary conditions.

The genus-one kernel in this continuation is a standard analytic mechanism.
Its elementary uniqueness/covariance proof and charged Ramond normalization
are given directly in [K1--K3](manuscripts/bol-genus-one-kernel.md).
In particular we do not import an ambiguous real-fermion Ramond prefactor
from the source: the actual complex-fermion exterior product fixes our
normalization. The local contribution is its attachment to the marked Bol
seed, the current-phase recovery and its explicit controls; no priority
claim for fermion kernels, Wick determinants, or modularity is made.

## Mat19

Nils Matthes, *An algebraic characterization of the Kronecker function*,
Research in the Mathematical Sciences **6** (2019), article 24.
[Original article](https://link.springer.com/article/10.1007/s40687-019-0186-0);
[author preprint](https://arxiv.org/abs/1806.04948).
Checked: Section 2.1, Definition 2.1 and Proposition 2.3, equation (2.1),
for the theta-quotient Kronecker function and its Fay identity. The broader
characterization theorem is context, not a premise of the new Bol results.

This source makes an important boundary explicit: a Fay identity in a
free-fermion completion is already standard elliptic geometry. It would not
by itself establish a new identity forced specifically by Bol loops.

## Genus-one continuation: what changes the earlier boundary

The earlier statement that current-correlation closure was unresolved refers
to its original checkpoint. [GC1--GC6](manuscripts/bol-genus-one-correlations.md)
now prove exact fixed-mode Gaussian identities and a closed colored-energy
quasimodular hierarchy with an almost-holomorphic modular completion on the
original graded space. [CG1--CG6](manuscripts/bol-correlation-geometry.md)
prove recovery beyond all fusion dimensions and a partition-blind current
distinction inside the inherited huge proper-loop input. K1--K5 give an
explicit position-dependent completion, while
[GA1--GA3](manuscripts/bol-genus-one-architecture.md) exclude finite modular
closure of unchanged individual mode traces and record the zero-mode price.
These are scoped new arguments, not independently established historical
novelty. No Bol-specific denominator identity or extra analytic rigidity
beyond the proved free-fermion/marked-data mechanism is asserted.

## Analytic rigidity continuation and further sewing requirements

[HR1--HR6](manuscripts/bol-holonomy-rigidity.md) prove a scoped monodromy
obstruction and bounded-pole normal form. [FS1--FS8](manuscripts/bol-fourier-sewing.md)
add commutator Fourier operations on the existing seed and a geometric
four-sector identity, including a conditional isotope-separating existence
test. The identity uses a new finite support relation; it is not forced
by the abstract group-valued word relations or universal oscillator laws
alone. Its modular realization still uses those standard oscillator laws.
These are proved constructions with explicit controls, not independently
verified historical-priority claims or a new interacting field theory.

Two primary sources clarify what a stronger theory would still require.
They were opened and their displayed locators checked during this continuation.
Neither theorem is applied as a black box to the Bol loop.

- Simon Willerton, *The twisted Drinfeld double of a finite group via gerbes
  and finite groupoids*, Algebraic & Geometric Topology **8** (2008),
  1419--1457, DOI 10.2140/agt.2008.8.1419,
  [publisher PDF](https://msp.org/agt/2008/8-3/agt-v8-n3-p08-s.pdf).
  Section 1.3.3, Theorem 3 (p.1435) constructs cocycle transgression;
  Section 3.1, Theorem 20 (p.1453) identifies the twisted double with a
  twisted inertia-groupoid algebra. An actual group 3-cocycle is input.
  A loop associator does not supply that cocycle or its coherence without
  a separate proof.
- Nora Ganter, *Hecke operators in equivariant elliptic cohomology and
  generalized Moonshine*, [arXiv:0706.2898v2](https://arxiv.org/html/0706.2898v2).
  Definition 6.2 and Proposition 6.3 give the isogeny/Hecke operation,
  with twisting alpha changing to n alpha. Definition 6.10, equation (14),
  imposes replicability as an additional exterior-power identity. Thus
  possession of isogeny or power operations alone would not prove
  replicability for the present construction.

## Keller17

Christoph A. Keller, *Introduction to Vertex Operator Algebras*, ETH Zurich
lecture notes, version dated 18 October 2017,
[author's course PDF](https://metaphor.ethz.ch/x/2017/hs/401-3177-67L/sc/VOAv2.pdf).
Checked: Section 3.3, Proposition 3.11 and equations (3.13)--(3.16), pp.13--14,
for the local Jacobi/Borcherds identity and its mode commutator. Taking both
mode indices zero gives [a_0,b_0]=(a_0 b)_0. This is background for the
explicit [matrix-current test](manuscripts/bol-local-current-obstruction.md),
whose algebraic obstruction is proved directly and does not depend on an
unverified vertex-algebra construction. The notes label themselves as under
construction; only the displayed elementary identity is used.

## TZ11

Michael P. Tuite and Alexander Zuevsky, *Genus Two Partition and Correlation
Functions for Fermionic Vertex Operator Superalgebras I*, Communications in
Mathematical Physics **306** (2011), 419--447,
DOI 10.1007/s00220-011-1258-1,
[arXiv:1007.5203v2](https://arxiv.org/html/1007.5203v2).
Checked: Theorem 5.1, equation (58), for the determinant partition formula
and its stated sewing domain; Proposition 5.5 and Theorem 5.6, equation
(67), for the Schur identity and separated-point correlation determinant.
Their analytic estimates are separate from a finite Berezin calculation.
The companion *The Szego Kernel on a Sewn Riemann Surface*, CMP **306**
(2011), 617--645, DOI 10.1007/s00220-011-1310-1,
[arXiv:1002.4114v2](https://arxiv.org/html/1002.4114v2), constructs the sewn
kernel; its Section 3 concerns two sewn surfaces. These are the established
Gaussian sewing baseline, not a theorem about an interacting Bol object.

## Felder94

Giovanni Felder, *Elliptic quantum groups*, December 1994,
[arXiv:hep-th/9412207v1](https://arxiv.org/html/hep-th/9412207v1).
Checked: equations (3)--(4), printed pp.3--4, for the position KZB system
and classical dynamical Yang--Baxter condition; equation (5) displays the
weight-dependent shifts in quantum exchange. The source is an announcement
and explicitly points elsewhere for complete proofs. The charged-exchange
continuation supplies its own theta/matrix-unit and gauge calculations and
states its sign convention. No new discovery of this standard dynamical
mechanism or a tau-heat connection is claimed.

## Arithmetic moonshine benchmarks

The following user-supplied sources were opened and their theorem statements
checked during the charged-sewing continuation. Neither is applied to a Bol
loop or used to infer an arithmetic consequence from mere modularity.

- John F. R. Duncan and Ken Ono, *The Jack Daniels Problem*, Journal of
  Number Theory **161** (2016), 230--239,
  [arXiv:1411.5354v2](https://arxiv.org/html/1411.5354v2).
  Theorem 1.1 and Section 2 recover characteristic-p supersingular
  j-invariants other than 0 and 1728 from the U(p)-image of the specified
  Fricke prime-order Monster trace. The proof combines replicability
  (Lemma 2.1) with the Dwork--Koike congruence; it is not a consequence of
  an arbitrary modular trace or a statement about prime distribution.
- John F. R. Duncan, Michael H. Mertens and Ken Ono, *O'Nan Moonshine and
  Arithmetic*, [arXiv:1702.03516v4](https://arxiv.org/html/1702.03516v4),
  the final version dated 17 March 2019. Theorem 1.1 states a **virtual**
  graded O'Nan module with weight-three-halves trace forms; the character
  at order 16 is nontrivial. Theorem 1.2 gives class-number congruences.
  Theorem 1.3's specified Selmer/Tate--Shafarevich statements assume BSD;
  the following remark isolates an unconditional rank consequence. These
  distinctions matter when using the work as a benchmark for the strength
  of a proposed new moonshine theory.

## EN01: finite dynamical twists

Pavel Etingof and Dmitri Nikshych, *Dynamical twists in group algebras*,
International Mathematics Research Notices **2001** (13), 679--701,
DOI 10.1155/S1073792801000356;
[arXiv:math/0101046v2, 29 January 2001](https://arxiv.org/pdf/math/0101046v2).
Checked locators: Definitions 2.3 and 2.5 (shift and gauge conventions),
equation (12), Propositions 3.3 and 3.8, and Corollary 3.7 (semisimple
diagonal algebras and invertible linking bimodules), Definition 4.5
(dynamical datum), and Section 6, equations (25)--(27) and Theorem 6.4
(exchange construction). Section 7, Lemma 7.1 and Proposition 7.2,
provide the nilpotent-group precedent.

[DD](manuscripts/bol-dynamical-fusion-construction.md) is an explicit
specialization retaining the Bol bimap and its full zero channels.
[AR](manuscripts/bol-finite-dynamical-rigidity.md) uses the cited
semisimple-algebra input and proves its local holomorphic and connection
statements separately. Neither the general finite twist mechanism nor
the mere existence of a shifted pentagon is claimed as new. The added
analytic assertions are in [CT](manuscripts/bol-collective-charged-transport.md)
and [SA](manuscripts/bol-shifted-analytic-fusion.md), with their stated
collective tensor rule and finite dynamical base.

## DLMF20: theta normalization and modular transformations

NIST *Digital Library of Mathematical Functions*, version 1.2.8,
release date 2026-09-15, Chapter 20. Inspected formulas
[20.2.1](https://dlmf.nist.gov/20.2.E1),
[20.2.6](https://dlmf.nist.gov/20.2.E6), and
[20.2(iv)](https://dlmf.nist.gov/20.2.iv) fix the Fourier, period and
zero conventions; [20.7.26](https://dlmf.nist.gov/20.7.E26) and
[20.7.30](https://dlmf.nist.gov/20.7.E30) give the modular generators.
Our spatial convention replaces the DLMF variable by pi z.
[TH](manuscripts/bol-theta-fusion-connection.md) and
[HT](manuscripts/bol-heat-sewing-repair.md) prove their mixed heat,
principal-symbol and marked reconstruction assertions explicitly.
The classical theta, Cauchy-integral and Fourier-sampling mechanisms
are baseline tools, not new moonshine consequences.
