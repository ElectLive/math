# Independent mathematical review: Bol quantum randomization

## Reviewer, revision and verdict

Reviewer: ChatGPT `/root/independent_math_review`, 16 November 2026.
I was a noncontributing reviewer of this research checkpoint. I did not write
or modify its manuscript, proofs, checkers or source catalogue. I extracted the
reviewed files with `git archive` from the exact published scientific revision
`0b78599e8c7d4e78b22a69c2ae7b276d41f8ae3b` of
[PR #443](https://github.com/Mira-Cult/math-wip/pull/443), rather than reviewing
an uncommitted working tree.

**Verdict:** I found no mathematical blocker in the new theorem-and-proof
arguments under the intended AQ hypotheses. The results are acceptable as
conventional mathematical proofs with the scopes stated below. Before public
delivery, Section 1 should replace the ambiguous phrase “Fp-linear alternating
matrices” by the exact source assumption: alternating n-by-n matrices **over E**,
independent **over Fp**, with zero common radical. This clarification does not
change the proofs, but prevents a broader Fp-linear interpretation under which
the actor reciprocity need not hold. Any subsequent new mathematics requires an
exact-revision addendum; this review does not automatically transfer to it.

This is an independent agent review, not human review, formal verification,
an implementation benchmark, an exhaustive literature/priority audit, or proof
of a Bol-specific resource advantage. The matching Weyl/actor control means
that no such advantage is established here. I did not independently replay the
old NI/AQ programs; I read the exact NI/AQ definitions and the proof dependencies
used by the recovered channel theorem.

## Source binding

All paths below are relative to
`problems/0323-finite-simple-non-moufang-bol-loops/` at the reviewed revision.

| Source | SHA-256 |
| --- | --- |
| `manuscripts/bol-quantum-randomization.md` | `5198b9d5ac3d0eabea8086a0dc5e711be5f708b418ccf5fa0de03ced10eb6c20` |
| `manuscripts/bol-nonscalar-intertwiners.md` | `c3a0b0a451314826b27d1ce998311dc93c6b37c0ff76a1faa1e251b5603fffbf` |
| `manuscripts/bol-associator-quantization.md` | `20d5ae96b5b4228282679cb892ee367034a7873c5c2d79d62567ac7bddbf3ff1` |
| `code/verify_bol_randomization.py` | `52c3d4857fd1c367ad95335bb1ccf185583ebcf7455b39b52e49e9a4a36bdce7` |
| `code/verify_bol_small_bias.py` | `11b41c1625fce8ce97bf4c50efee24e4369c12df87053b1bc8a54e3bb536d881` |

The recovered scientific baseline is `ec122a2a890971141caf960dd27fdb50fed77154`,
delivered in PR #441 at `59d77073b15a25fb2cf6915a602836be68e2c93f`.
The current review accepts the recovery at the displayed hypotheses; it does
not erase the prior source/review distinction or review unrelated classification
claims in the same workspace.

## Mathematical audit

### Actual channel, normalizations and exceptional sectors

I compared (QR.1)--(QR.7) with NI Sections 1.1, 8.1--8.3 and AQ Sections 1--2.
The basis, normalized counting measures, ordinary matrix Hilbert--Schmidt norm,
actual defect parameters and independent uniform triple law agree. The dense
law is not replaced by a uniform average over its generated group.

The recovered exact global rate is the diagonal rate
$`\Lambda=p^{-1}+(1-p^{-1})Q^{-r_{\min}}`$. NI's positive synchronized
orbit operator bounds off-diagonal contraction by $`p^{-2}`$; it does not
assert equality there. Monomiality preserves both point-diagonal and
off-diagonal spaces. Positivity of the dense channel makes the global powers
exact. Nondegeneracy means both nonsingular $`B_\nu`$ and unit $`\rho`$.
The spread/aligned joint-trace examples do not satisfy that hypothesis and are
correctly excluded from arbitrary-state depolarization.

I rederived the translated-defect normal form directly from the three factors.
The output translation is $`C^{-1}(R_g-I)a`$, the point modulation is
$`Ch+(R_g-I)a`$, and the global phase is
$`\chi(b(h,a)+b(a,t))`$. The signs agree with the displayed convention for
$`\pi_\chi`$. Global phases are immaterial only after conjugation.

Theorem D's radical average is an orthogonal projection of rank $`d/|D_\chi|`$.
Each sector translation and defect permutes its translation summands without
phase. Its normalized projector is therefore fixed by every native unitary,
not merely by the original dense average. The exact trace error
$`2(1-|D_\chi|^{-1})`$ and uniform point populations follow from its spectrum
and diagonal. The obstruction consequently survives reweighting and arbitrary
word distributions, including in the zero-character sector.

### Native fixed-list obstructions and sharp commutant threshold

Theorem A correctly uses the extra native fact that trivial field actor implies
zero field translation. Centering at a fixed point of one nontrivial actor
leaves at most $`K-1`$ independent translations over $`\mathbf F_p(\lambda)`$.
That affine span is preserved by the full generated group. A support measurement
gives the stated trace lower bound. This is a fixed-union-of-generators result,
not an obstruction to large efficiently sampled supports or arbitrary monomial
expander constructions.

For Theorem C I checked the symmetric Weyl phase convention: it produces
commutator $`e_3(\Omega)`$ and exact actor covariance without an extra label
phase. Since $`3^3=-1\pmod7`$, the Frobenius twist of the second coordinate
turns the field action into scalar multiplication on $`E^{2n}`$. Centering one
nonzero actor displacement is valid because $`I-S_g`$ is invertible. The remaining
invariant displacement span has F3 dimension at most $`6(K-1)`$; its symplectic
annihilator consequently has size at least $`729^{2n-K+1}`$.

Actor-orbit sums of Weyls in that annihilator commute with every centered
unitary. Every nonzero orbit has size seven. Disjoint orbit supports make these
sums independent, proving the lower bound
$`1+(729^{2n-K+1}-1)/7`$ on the common-commutant dimension. Tensoring with the
ring identity is legitimate because each native unitary factors across the two
physical factors, even though its classical labels are coupled.

The conversion from algebra dimension to a stationary state is valid: a
finite-dimensional C*-algebra $`\bigoplus_i(M_{r_i}\otimes I_{m_i})`$ contains
$`\sum_i r_i\geq\sqrt{\sum_i r_i^2}`$ orthogonal nonzero projections. A minimum-rank
one gives the stated trace bound. At $`K=2n`$ the algebra lower bound is 105,
so the guaranteed error exceeds one.

For the upper threshold, all displayed $`2n+1`$ operators are actual defects
or actual translation conjugates. Seventh powers isolate field shears, third
powers isolate the two ring directions, and actor conjugation spans all of E.
The translated actors then supply all shifts. The resulting group contains the
full Weyl group, so its commutant is scalar. This proves the exact irreducibility
threshold. It does not prove an efficient spectral gap at that minimum support,
and the manuscript does not claim one.

### Dense depolarizing component

I independently counted the conditional fibers in Theorem QD. Given fixed
nonzero $`g_p,g_q`$, exactly one of the 49 field actor pairs has both coefficients
zero. Every other pair maps a fixed nonzero trace-pairing fiber uniformly onto
$`W\setminus\{0\}`$: the prescribed nonzero target leaves one nonzero F3-linear
functional, with $`D/3`$ solutions; the zero target leaves none. The ring analogue
has exactly one zero coefficient pair among nine and seven preimages per
nonzero target. The conditional field and ring laws are independent.

Their pointwise uniform components have weights
$`48D/(49(D-1))`$ and $`49/54`$. Multiplying by the probabilities of the two
nonzero defect components gives exactly $`512/1029`$. With the translating
center independent and uniform, (QR.11) is an invertible affine transformation
of the two uniform Weyl labels. The extracted component is therefore a genuine
completely depolarizing channel, with nonnegative residual mixed-unitary law.

The resulting diamond estimate $`2(517/1029)^t`$ follows from
$`\mathcal E\mathcal R=\mathcal R\mathcal E=\mathcal E`$. It is dimension independent
but an upper bound, not an exact diamond rate. The proof is restricted to the
specified symplectic $`p=3,q=7,k=A=1`$ family. It does not extend itself to
arbitrary pencils or higher conductors.

### Sparse construction and norm criteria

Theorem W's loop-pair prescription solves the two blocks independently while
retaining $`b(a,v)=(1,1)`$. Choosing $`c=-(1,1)`$ removes the unwanted second
vector coefficient. The translation center then gives every requested Weyl
operator followed by the fixed actor, up to a global phase. The one-call result
is valid at conductor one. For its stated higher-conductor extension with one
ring plane, a unit determinant pair is a ring basis and zero-or-unit coefficients
force a zero-or-primitive correction; the claimed obstruction is sound.

Lemma B is an exact character-sum identity. Averaging in its first field seed
turns every nonzero character into the root fraction of a nonzero polynomial.
The root bound gives the asserted bias, without treating random existence as an
explicit sampler. Theorem S uses a perfect commutator pairing to apply that bound
to all nonconstant field Weyls, and exact ring depolarization justifies using
$`D=3^N`$, rather than full $`d=49D`$, in the state trace conversion even for
states entangled between the internal factors. The constants 441 and the exact
$`d^2`$-key fallback are correct.

The rank/Choi-rank bounds correctly distinguish state trace error from diamond
error. A state randomizer with the displayed sparse support generally has
asymptotically maximal diamond error at fixed epsilon, so it is not being sold
as reference-secure encryption. The inequalities
$`e_1\leq\sqrt{d-1}e_2`$ and $`e_\diamond\leq d e_2`$ use ordinary HS norm and
the manuscript's trace norm without a factor one half. The mixing times derived
from those conversions are explicitly sufficient, not exact. Fresh independent
samples are necessary for the stated channel powers.

The matrix-concentration calculation has a legitimate Hermitian dilation of
dimension $`2d^2`$, summand norm at most two and variance bound $`4M`$. The
reported conservative two-sided Hoeffding bound and sample size follow. Every
sample is monomial, so the preserved decomposition suffices for the separate
power upper bounds without assuming sampled-channel positivity. Efficient
certification is correctly left unproved.

### Fixed-pair joint channel and sharp purity inequality

I rederived the exact weighted-Weyl formulas (QR.27). The tested arguments are
$`v+R^{-1}h`$ and $`Rv+R^{-2}h`$; their joint map is invertible precisely under
the stated square-minus-identity assumption. Thus the one-step HS norm is one,
and the two-step norm is the actual bias $`\Delta`$, including attainment.
These are singular norms, not eigenvalue identities. Uniform centers give
exact two-round depolarization with a bijection to full Weyl keys. The supplied
uniform-population density matrix witnesses failure of the original one-step
coherence bound in this repair.

For Theorem P, the exceptional graph Weyls span C*-algebras of dimension d.
Their commutator bicharacters $`\mathsf B(-2Av,w)`$ are nondegenerate for the
invertible self-adjoint actors, so their centers are scalar. The representation
is consequently $`M_s\otimes I_s`$, where $`d=s^2`$. The HS projection is a
conditional expectation with output purity at most $`1/s`$ on density matrices.
The two graph subspaces intersect only at the identity and their traceless parts
are orthogonal. Splitting exceptional weights from the remaining weights proves
(QR.31) and then (QR.30), including when delta is only an upper bound on the
actual bias.

The actor-stable Lagrangian subgroup gives a pure state attaining both graph
projection bounds simultaneously. Counting its Weyl support proves sharpness
of the HS/purity inequality for the displayed mixture law. Sharpness of the final
trace Cauchy--Schwarz step is not asserted. The independent-round sampler costs
and epsilon substitution in (QR.32)--(QR.33) are consistent. Its exact matching
correlated-Weyl control shares the same purity mechanism, as the manuscript says.

### Controls and second moments

The phase-plus-classical-permutation control has exactly the indicated zero
coherence rate; full phase keys are charged. The Fourier/dephasing identity
$`\mathcal D\operatorname{Ad}_F\mathcal D=\mathcal E`$ is valid only for full
rank-one dephasing, so the degenerate caveat is essential and retained.
The scalar, permutation-only, untranslated and associative literal-defect
ablations have the stated fixed-state obstructions.

For Proposition M, $`Q_\Delta`$ is fixed by every monomial tensor square, while
its Haar average is $`2\Pi_{\rm sym}/(d+1)`$. Their difference is nonzero and
Haar-orthogonal. Every tensor-square conjugation preserves the Haar subspace
and its orthogonal complement, so the average has norm at most one there.
This proves the claimed **equality** in induced HS norm. The trace discrepancy
$`2(d-1)/(d+1)`$ is also the correct two-eigenspace calculation. First-moment
randomization therefore does not establish a second design.

## Independent finite replay

I read both checker sources before interpreting their outputs and executed the
following from the extracted exact revision, with Python 3.12.14:

```text
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_randomization.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_small_bias.py
```

Both exited zero and had empty stderr. Stdout SHA-256 values were respectively
`52ec69e7544e56fe74d78b4a91db4696b61ccba4b636c70fbc402bea55572669`
and
`6059e0498daf8d3cc6e77ca9b42cb4b20a464322c9f9d63e771174453921a239`.
These agree with the owner's record.

The channel checker includes 800 actual five-factor ket/phase comparisons,
160 fixed-pair comparisons, 214 prescribed defects, 216 Weyl-coset realizations,
531441 field scalar label pairs, the complete 2401-element ring Weyl basis,
300 radical covariance checks, 112 common-commutant covariance checks, all 400
F7^4 Lagrangian planes and the eight equality cases, and exact dense conditional
ring counts and specified field trace-rank tests. Its finite field presentation
is also checked. The baseline-rate routine is arithmetic substitution into the
proved formulas; it is not an independent enumeration of the large spectrum.
The population support example is explicitly a tiny affine toy, not the actual
26,040,609-dimensional channel.

The small-bias checker exhausts five small-field cases, 1629 seed pairs and 904
nonzero characters, and tests nine larger parameter inequalities. The programs
neither enumerate the full large channel nor implement the cited general
irreducible-polynomial construction or compiled quantum circuits. Their proper
role is finite corroboration of the separate conventional proofs.

## Remaining scope and delivery conditions

The intended outcome is a precise native obstruction together with a proved,
implementable repair. The exact group control prevents a claim of general
Bol-specific resource superiority. The minimum-list spectral gap, a certified
explicit O(log d)-support approximation preserving the original two rates,
full higher-conductor one-call reachability, and a useful genuinely distinct
loop-specific task remain unproved.

I checked the internal mathematical cost scalings and norm conversions relevant
to the proofs, but did not independently re-verify every current primary-source
benchmark or produce a physical circuit implementation. A separate resource/
literature audit is appropriate. Repository integrity, remote CI, public target
rendering and integration status are separate from this mathematical verdict.


## Addendum: strengthened scientific revision f6f415a

Reviewer: ChatGPT `/root/independent_math_review`, 16 November 2026.
I independently examined the complete scientific diff from the original reviewed
revision `0b78599e8c7d4e78b22a69c2ae7b276d41f8ae3b` to
**`f6f415a5b05ce38b51adc9d2894c9795af500b3e`**, whose tree is
`f1e1e9f4c97abb32bbfdb0a50968e9063a85c0c9`. I extracted the revised source with
`git archive`, read both changed checker implementations, and replayed them from
that exact snapshot. The preceding original review is preserved unchanged.

**Revised-source verdict: accept the mathematical results at this exact revision.**
The E-matrix/Fp-independence clarification is present, and the strengthened sparse
bounds and added algebraic ablation are proved correctly. I found no remaining
mathematical blocker in the reviewed changes. All original scope restrictions
remain: this is conventional independent agent review, not formal verification,
physical circuit validation, or a claim of Bol-specific efficiency superiority.

### Revised source and replay binding

| Item | SHA-256 |
| --- | --- |
| Revised randomization manuscript | `fd219c96216b5b0ad43dafc08a74f131c088b173529d89cd49ba49f36dc465f7` |
| Revised `verify_bol_randomization.py` | `1bfd231605751f5d091466dbd5557285dd79a2bb8daba6b5542a268fe8928425` |
| Its independent stdout | `6032535acfa0f4b41f4411e1880726e100b2d7735d48926872111c1d1e8c2afe` |
| Revised `verify_bol_small_bias.py` | `7e542e411b57da30d370f8eee1e6b940372c3bdefaed3fbadd0195de91f58326` |
| Its independent stdout | `dd32bb4ad062ffd5e383240dbc6b8355fedd542fcd1e75eb38f7271e5f211960` |

The same two commands listed above both exited zero under Python 3.12.14, with
empty stderr. The old NI/AQ mathematical dependencies are unchanged by this
revision.

### Blocked sampler and improved resource bounds

For the new Lemma B, basis independence guarantees that a nonzero F3 character
produces a nonzero polynomial over $`F=\mathbf F_{3^r}`$ with coefficients
$`c_j=\sum_i z_{jr+i}e_i`$, even when the final coefficient block is truncated.
Averaging in the first seed gives exactly its root fraction. The degree is at
most $`\lceil\ell/r\rceil-1`$, so the improved bias statement follows.
The one-block case is genuinely unbiased. This establishes the characteristic-three
version directly; the source correctly credits the standard AGHP/DN method
rather than treating the sampling machinery as a new Bol result.

For Theorem S, $`r\geq N/2+1`$ implies $`\lceil2N/r\rceil\leq4`$, hence bias
at most $`3/3^r\leq\varepsilon/\sqrt D`$. Also
$`3^r<9\sqrt D/\varepsilon`$, giving
$`7^4 3^{2r}<3969d/\varepsilon^2`$. The prior Weyl-channel proof and internal-ring
depolarization argument apply unchanged. The new entropy formula has no
logarithmic-register overhead. At fixed positive epsilon it is within an
additive constant of the support lower bound; the manuscript correctly does
not infer optimal epsilon dependence from that lower bound.

For the independent fixed-pair rounds,
$`\delta^2=\varepsilon^2/(3\sqrt D)`$ and the fact that N is a multiple of twelve
give $`r\geq N/4+2`$ and $`\lceil N/r\rceil\leq4`$. Thus
$`K=49\cdot3^{2r}<11907\sqrt D/\varepsilon^2`$. The direct trace bound from
Theorem P is still at most $`\varepsilon^4/9+2\varepsilon^2/3\leq\varepsilon^2`$.
The total two-round key count and entropy in (QR.33) follow. These are genuine
improvements over the earlier unblocked constants, with the unchanged matching
Weyl control and no claimed native spectral-gap improvement.

The revised small-bias checker correctly assembles extension-field coefficients
from base-three digits and enumerates the resulting characters and roots. It
retains five cases, 1629 seeds and 904 nonzero characters, including a truncated
block and an exactly unbiased case. Its nine larger exact-rational cases now
verify both one-call and fixed-pair costs and the fixed-pair trace-error bound.

### Sampling time and exact gate set

The clarified resource model separates deterministic polynomial preprocessing
and key evaluation from expected polynomial fair-bit sampling. Its bounded-time
variant is also correct: coupling the truncated interval sampler to the exact
one makes key disagreement probability at most $`M2^{-B}`$. Consequently the
mixture-channel difference has diamond norm at most $`2M2^{-B}`$, and the stated
bit budget makes this at most tau. Allocating the desired error among sampling,
statistical randomization and compilation gives the claimed bounded-time option
with the explicitly charged extra bits.

The SUM-only implementation of the field actor is justified by
$`\det(m_\lambda)=\operatorname{Norm}(\lambda)=\lambda^{364}=1`$. Elementary
transvections generate $`\operatorname{SL}_6(\mathbf F_3)`$, so the fixed field
multiplication matrix needs no unstated coordinate scaling gate. The fixed
six-coordinate size makes its gate count and depth constant per block. Computing
trace values on demand preserves the stated sampler storage bound after
preprocessing; storing a full trace Gram matrix is unnecessary.

The added IJJS comparison's error-allocation argument is sound: per-use unitary
error eta gives at most $`2\eta`$ channel diamond error, hence at most
$`2T\eta`$ over T uses. The precise current-paper oscillator/compilation bounds
remain within the separate resource/literature audit's remit; I do not present
this mathematical addendum as an independent source verification of those facts.

### Fused-sector decorrelation

Independently keying the two conjugate vectorized factors gives
$`A\otimes\overline A`$, with $`A=\mathbb EV`$, hence the completely positive
map $`T\mapsto ATA^*`$. Trace preservation would require $`A^*A=I`$, making A
unitary; the displayed mean-square identity then forces every positive-weight
unitary representative to be identical. The diagnostic therefore loses trace
preservation for a nontrivial operator law. Its dependence on representative
global phases is explicitly acknowledged, so it is not used as a fair physical
randomizer comparison.

For the exact fixed-pair representatives, the unique center contributing to
entry (s,u) is $`s-Ru`$, and $`b(Ru,u)=0`$ gives
$`A_{s,u}=\mathsf B(s,u)/d`$. The perfect bicharacter pairing makes the normalized
matrix Fourier-unitary. Thus $`A^*A=I/d`$, the decoupled output trace is exactly
$`1/d`$, and renormalization gives only a unitary channel. This is distinct from
decorrelating the two-round Weyl labels.

The new exact ring-factor check verifies all 2401 matrix entries and 117649
Gram character terms, with 49 diagonal entries and 2352 vanishing off-diagonal
entries, obtaining $`A^*A=I/49`$. This is finite corroboration of the general
proof at the correct 49-dimensional factor, not a full-channel enumeration.

### Final acceptance scope

The accepted scientific checkpoint is now **f6f415a**, not merely the preliminary
0b78599 source. It contains a rigorous fixed-list obstruction, sharp commutant
threshold, dimension-independent dense-channel diamond upper bound, explicit
$`O(d/\varepsilon^2)`$-support state randomizer, and a separate fixed-pair purity
and sampling result. The original caveats about native degeneracy, exact versus
upper rates, reference security, higher conductors, minimal-list gaps and
second moments remain necessary and are retained.

The results support the commissioned obstruction-plus-serious-repair outcome.
They do not establish a general efficiency advantage over the matching standard
Weyl randomizer. No further scientific correction is requested by this review.
