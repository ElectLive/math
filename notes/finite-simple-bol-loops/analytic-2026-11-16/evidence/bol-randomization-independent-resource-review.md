# Independent review: randomization resources and primary-source comparisons

Reviewer: ChatGPT agent `/root/independent_resource_review`, 16 November 2026.
Role: independent resource/comparison reviewer, not an author of the initial
scientific manuscript or either checker. Review recommendations included a
standard AGHP sampler refinement and several accounting clarifications; those
recommendations are disclosed below. No scientific source was edited by this
reviewer. This is an agent review, not human review or formal verification.

## Exact source examined

Initial scientific revision:
`0b78599e8c7d4e78b22a69c2ae7b276d41f8ae3b`, PR #443.
The manuscript was extracted using `git show REV:path`, rather than relying on
an uncommitted working tree. Its SHA-256 is
`5198b9d5ac3d0eabea8086a0dc5e711be5f708b418ccf5fa0de03ced10eb6c20`.
The review covers Sections 2, 4--9 and the parameter/resource claims elsewhere;
the separate mathematical review owns the complete independent theorem audit.
I also read NI Section 8 to distinguish its synchronized sector average from
the new two-round Weyl-label correlation.

The initial claims examined are mathematically consistent in this remit. I found
no false resource bound or invalid norm conversion. The exact odd-cardinality
fair-bit sampler requires an explicit expected-time qualification, despite the
correct unbounded-worst-case qualification already present in Section 2. Three
other useful clarifications and a substantial standard-machinery improvement
were sent to the owner. Acceptance of a later scientific revision requires an
exact-revision addendum, not an assumption that recommended edits were made.

## Error criteria and lower bounds

The manuscript consistently uses the full trace norm without the conventional
factor one half. I checked the state conversion
`e_1 <= sqrt(d-1) e_2`: a state has squared traceless HS norm at most `1-1/d`.
The diamond conversion `e_diamond <= d e_2` follows by amplification with a
d-dimensional reference and the Schatten inequality on the d-squared joint
space. It is a sufficient bound, not a sharp mixing-time assertion. The dense
minorization gives a separate, stronger dimension-independent diamond bound
in its explicitly fixed family and does not contradict the exact HS rate.

For M mixed-unitary keys, the output on a pure input has rank at most M. The
support measurement gives `e_1 >= 2 max(0,1-M/d)`. The normalized Choi state
similarly gives `e_diamond >= 2 max(0,1-M/d^2)`. These do not supply unrestricted
Shannon-entropy lower bounds for nonuniform keys. The exact-channel entropy
bound uses the entropy upper bound for a mixture of pure Choi states. Those
distinctions are correct. They do not prove optimal epsilon dependence for an
O(d/epsilon^2) approximate-state construction.

The initial one-call proof correctly applies exact ring depolarization before
bounding the reduced field state. Thus the dimension loss is sqrt(D-1), where
D=3^N, despite arbitrary internal field/ring entanglement. It does not cover an
external reference. In particular, the support lower bound forces diamond error
to approach two for its small-key approximate branch at fixed epsilon and
growing dimension. The manuscript says so explicitly.

The fixed-pair construction requires independent round labels to be a channel
power. Correlated schedules can reproduce another Weyl law, but cannot be
silently substituted into that power. The claimed exact two-step norm uses the
actual Fourier bias Delta, not a conservative upper bound delta. In the direct
state calculation, inserting delta^2=epsilon^2/(3 sqrt(D)) gives at most
`epsilon^4/9 + 2 epsilon^2/3 <= epsilon^2` for the squared trace bound. A bound
by epsilon is therefore valid with slack. The purity equality case is not
mislabeled as equality in the final trace Cauchy--Schwarz step.

## Sampling, gates and uniformity

I checked the initial scalar-coordinate sampler and constants 441 and 1323.
Its proof reduces every nonzero character to the root count of a nonzero
polynomial. Both constants follow from the strict inequality `3^ceil(log_3 x)<3x`.
The exact-twirl fallback is correct and prevents an unnecessarily large
approximate support when epsilon is tiny.

The interval sampler gives an exact uniform key using expected fewer than
`log_2 M+3` fair bits; its stopping-time tail is bounded by
`min(1,(M-1)2^-j)`. Exact sampling of an odd-size support cannot have bounded
worst-case bit consumption. Consequently, the complete randomized algorithm
must be described as expected polynomial time, with deterministic polynomial
time for preprocessing and the key-to-circuit map. A bounded-time variant would
need truncation and a charged sampling error. This was requested as a correction
to the blanket uniform-polynomial-time sentence in Section 7.

The fixed E=F729 arithmetic and two F7 coordinates make the claimed O(N) quantum
gate count and constant depth feasible. The modulations and displacements are
products of local phases and shifts. The field actor is parallel multiplication
on fixed six-qutrit blocks. A useful omitted justification is that multiplication
by the order-seven lambda has determinant Norm(lambda)=lambda^364=1 over F3.
It therefore belongs to SL6(F3), which is generated by elementary SUM
transvections; the declared gate library does not need an unmentioned
single-coordinate scalar-multiplication primitive. This is a clarification,
not a counterexample to the circuit claim.

I visually checked Shoup's Theorem 3.2 on the rendered third page of the saved
author PDF: at fixed characteristic it gives deterministic O(r^(4+c)) field
operations for every fixed c>0. Thus the cited preprocessing theorem removes
random advice or an exponential polynomial search. The manuscript correctly
separates reliance on this theorem from the small checker, which implements only
fixed low-degree irreducibles. Schoolbook output generation in O(ell r^2) base
field operations and O(ell+r) storage is a valid conservative bound.

The qubit encoding uses 2N+6 physical qubits for a promised logical subspace of
dimension 49*3^N. The target remains the embedded logical maximally mixed state.
It is not the uniform state of the larger physical register. Constant-locality
unitary extensions and Solovay--Kitaev compilation support the stated conservative
polylogarithmic precision overhead. Summing G per-gate operator errors of
`epsilon/(8G)` gives unitary error epsilon/8 and channel diamond error at most
epsilon/4 per round. Two rounds plus statistical error epsilon/2 stay within
epsilon. Ancillary workspace need not grow with N for these fixed local gate
compilations. None of this establishes exact Clifford+T realization of roots of
unity of orders three or seven.

## Primary-source comparison audit

I independently retrieved the following primary texts, inspected the stated
locators, and translated their assertions only into the criteria stated in the
manuscript. This verifies the cited statements, not every proof in those papers.

| Source and locator | Finding |
| --- | --- |
| [Dickinson--Nayak, author PDF](https://www.math.uwaterloo.ca/~anayak/papers/DickinsonN06.pdf), 1 June 2006, Theorems 1.2 and 1.4, Section 2 | The trace-norm explicit Pauli bound is 16d/epsilon^2 in qubit dimensions, with rounding and polynomial per-index generation. Its random-sampling theorem permits any completely randomizing source distribution, with size ceil(37d epsilon^-2 ln(15/epsilon)) and failure at most exp(-d/2). Neither is a diamond guarantee. |
| [Ben-Aroya--Schwartz--Ta-Shma, Theory of Computing 6 (2010)](https://theoryofcomputing.org/articles/v006a003/v006a003.pdf), Section 4, Theorem 4.6 | The explicit zig-zag construction has dimensions D0^(8j), degree D0^2, constant contraction and polynomial circuits. The finite seed search depends only on fixed parameters. This is distinct from the paper's nonexplicit algebraic construction. No depth-one claim follows. |
| [Anshu et al., arXiv:2609.01605v1](https://arxiv.cnoctave.top/pdf/2609.01605), Theorem 2.2, equations 2.1--2.6 | The 16 generators act on 3s qubits and have gap at least 1/(2*10^8). They are Pauli/CNOT depth-one circuits with periodic bounded-range geometry. The manuscript correctly avoids calling all edges nearest-neighbor. I inspected the primary paper through its disclosed mirror. |
| [Iyer et al., arXiv:2602.15180v1](https://arxiv.org/html/2602.15180v1), Theorems 1.1 and 4.2, Corollary 1.2, equation 92, Section 6.1, Appendix C | Taking p=5 gives degree six and the ideal contraction upper bound 2sqrt(5)/6 for every logical dimension. Efficient implementation is approximate on an enlarged register. The table's vague preprocessing/encoding phrase should be expanded: for n=2 the paper gives circuit complexity O((log d+log(1/eta))^3 log(1/eta)), enlarged dimension O(((d-1)^2.25/eta^3.25)^2), hence O(log d+log(1/eta)) qubits, and polynomial classical precision preprocessing. Use eta=O(epsilon/T) for T rounds and reserve statistical error separately. |
| [Jain, arXiv:2609.38075v1](https://arxiv.org/html/2609.38075v1), Theorems D.1 and E.1, Section E.1 | The dimension is (q^(2a)-1)/2 and the logical space is the odd subspace. The contraction is bounded above by 2sqrt(q)/(q+1). Exactness refers to a declared fixed qudit gate library. Gate/depth O(log^2 d), ancillary qudits O(log d), and preprocessing O(log^5 d) fixed-field operations are supported. Encoding/decoding into the odd subspace is not included. The generator-wise cost also supports classical-key use; the cited theorem states the Stinespring form. |
| [Lancien, arXiv:2409.17971v3](https://arxiv.org/html/2409.17971v3), Corollaries 2.5 and 3.5 and preceding ensemble definitions | The sampled ensembles come from exact 2-designs or 2k-designs. The asymptotic contraction is 2(1+o(1))/sqrt(M) for M at least (log d)^(4+alpha), fixed k and alpha>0. The norm is the superoperator HS norm; it is not an output Schatten-infinity randomization criterion. |
| [Shoup, Mathematics of Computation 54 (1990)](https://www.shoup.net/papers/detirred.pdf), Theorem 3.2 | The fixed-prime deterministic irreducible-polynomial complexity used here is correct; the rendered page was necessary because text extraction was corrupt. |
| [Tropp, arXiv:1004.4389v7](https://arxiv.org/pdf/1004.4389v7), Theorem 1.3 | On a Hermitian dilation of dimension 2d^2 with centered-square bound 4I, the manuscript's 4d^2 exp(-M eta^2/32) is conservative and valid. It is an existence/high-probability benchmark, not an efficient certification algorithm. |
| [Dawson--Nielsen, quant-ph/0505030v2](https://arxiv.org/pdf/quant-ph/0505030v2), Sections 2--3 and higher-dimensional extension | The cited inverse-closed finite-gate Solovay--Kitaev theorem gives the required fixed-local-dimension polylogarithmic synthesis; the manuscript uses a conservative exponent rather than claiming an optimized compiler. |

The exact Weyl/actor control uses precisely the same logical dimension, gates
and key distribution as the native repair. It is therefore stronger evidence
against a claimed Bol-specific efficiency gain than a comparison requiring
padding into qubits. The phase-twirl plus classical permutation control correctly
charges its phase key, and gives exact randomization on the uniform-population
class. The table's qubit-only dimension caveats are essential and correct.

## Review-driven improvement and ablation clarification

Checking DN Proposition 2.2 and Appendix B revealed an avoidable N-squared seed
overhead in the initial sampler. The standard AGHP construction uses a basis
`e_i` of the extension field and coordinates `Tr(a e_i b^j)`, obtaining r*s
coordinates with degree s-1. The root proof extends directly to characteristic
three. The owner was advised to adopt this established construction, rather than
present the simpler scalar-coordinate choice as the strongest available repair.
The proposed new constants 3969 for the one-call support and 11907 for the
per-round fixed-pair support are algebraically consistent with the proposed
parameters; they require review of the actual revised source and checks.
This is standard machinery and does not change the no-Bol-specific-advantage
conclusion. Matching O(d/epsilon^2) is not a proof of optimal epsilon dependence.

The original draft's correlation ablation addressed two-round Weyl labels.
NI's synchronized chi/conjugate-chi fusion is a separate correlation. I requested
that the distinction be explicit. For the owner's proposed diagnostic,
independent bra/ket keys give `T -> A T A*`, `A=E V`, rather than the original
channel. This generally fails trace preservation and is phase-representative
dependent. With the displayed exact fixed-pair representatives,
`A_(s,u)=B(s,u)/d`, so `A*A=I/d` and the trace loss is exactly 1/d. This
calculation is valid, but must be labeled a non-channel diagnostic, not a
physical randomizer or a complete solution of every fused-sector ablation.

## Independent finite replay

Both programs were extracted from the exact initial scientific commit and run
with Python 3.12.14 in an isolated review directory.

| Program | Source SHA-256 | Exit / stderr | Stdout SHA-256 |
| --- | --- | --- | --- |
| `verify_bol_randomization.py` | `52c3d4857fd1c367ad95335bb1ccf185583ebcf7455b39b52e49e9a4a36bdce7` | 0 / empty | `52ec69e7544e56fe74d78b4a91db4696b61ccba4b636c70fbc402bea55572669` |
| `verify_bol_small_bias.py` | `11b41c1625fce8ce97bf4c50efee24e4369c12df87053b1bc8a54e3bb536d881` | 0 / empty | `6059e0498daf8d3cc6e77ca9b42cb4b20a464322c9f9d63e771174453921a239` |

The small-bias checker exhausts its stated five finite cases and tests nine
resource settings. The channel checker uses exact finite algebra, ring-channel
Weyl multipliers, and specified structural samples; it does not enumerate the
huge full loop channel. I inspected the sampler source and relevant output
scopes. Successful replay corroborates those finite statements. It is not a
large-degree Shoup implementation, a hardware compilation benchmark, or a
formal proof of the growing-dimension theorems.

## Verdict at the initial revision

No mathematical/resource counterexample was found within this review's remit.
The resource and comparison conclusions are defensible with the explicit
expected-time qualification and comparison details requested above. The
recommended AGHP blocking materially strengthens the explicit repair without
claiming a Bol-specific advantage. The final revised scientific commit must be
pinned and rechecked in an addendum before this report can be cited as acceptance
of that new source.


## Final scientific-revision addendum

**Reviewed revision:** `f6f415a5b05ce38b51adc9d2894c9795af500b3e`.
**Manuscript SHA-256:**
`fd219c96216b5b0ad43dafc08a74f131c088b173529d89cd49ba49f36dc465f7`.

I inspected the exact Git diff from the initial scientific revision, extracted
the new manuscript and both changed checkers using `git show`, and independently
replayed both programs. This addendum accepts the revised resource and comparison
claims within the scope and limitations of this report. No blocking issue remains
in that remit. The separate mathematical review is still the independent audit
of the full theorem family, rather than being replaced by this resource review.

### Stronger explicit sampler

The revised Lemma B correctly outputs a prefix of the r*s coordinates
`Tr(a e_i b^j)`. Each nonzero character gives a nonzero coefficient polynomial:
independence of the field basis prevents cancellation of a nonzero coordinate
block, including a truncated final block. Averaging in a gives the exact root
fraction, and the degree is at most s-1. This is the correctly attributed standard
AGHP construction, with a self-contained characteristic-three argument.

For Theorem S, `r=ceil(log_3(3 sqrt(D)/epsilon))` implies
`r>=N/2+1` and `ceil(2N/r)<=4`. The bias is therefore at most
`3/3^r<=epsilon/sqrt(D)`. The strict bound `3^r<9 sqrt(D)/epsilon` gives

```text
M = 7^4 * 3^(2r) < 7^4 * 81D/epsilon^2 = 3969d/epsilon^2.
```

The entropy bound is consequently `log_2 d+2log_2(1/epsilon)+log_2 3969`.
The exact-twirl fallback and the trace/diamond distinction remain valid. This
removes the avoidable logarithmic register-size overhead but provides no
Bol-specific improvement over the matching Weyl ensemble. Fixed-error support
bounds establish the leading log(d) key scale for uniform/fixed-length-key
implementations; they remain separate from arbitrary nonuniform-key entropy
lower bounds and do not prove optimal epsilon dependence.

For independent fixed-pair rounds,
`delta^2=epsilon^2/(3 sqrt(D))` and `r=ceil(log_3(3/delta))` imply
`r>=N/4+2` and at most four coefficient blocks. Since `3^(2r)<81/delta^2`,

```text
K = 49 * 3^(2r) < 49 * 81 * 3sqrt(D)/epsilon^2
  = 11907sqrt(D)/epsilon^2.
```

The two-round state estimate and entropy formula follow with the same positivity
argument and the explicitly independent labels. The checker now tests both
one-call and independent-round resource inequalities using exact rational
comparisons, including the squared threshold when delta itself is irrational.

### Accounting and ablation corrections

The revised source explicitly distinguishes deterministic polynomial-time
preprocessing/key compilation from expected polynomial-time exact fair-bit
sampling. Its optional bounded-time construction is also valid: truncation after
B bits has total variation at most M*2^-B, so channel diamond error is at most
2M*2^-B. Taking `B=ceil(log_2(2M/tau))` bounds that error by tau. The additional
log(1/tau) bit budget and the need to divide the total accuracy allowance are
charged rather than hidden.

The SUM implementation now contains the norm/determinant argument, and the
matrix assumption is explicitly stated over E. The IJJS comparison now gives
its circuit, enlarged-register, preprocessing and precision costs, and correctly
uses ideal statistical error epsilon/2 with per-use implementation error at most
epsilon/(4T). The resulting additive implementation error is at most epsilon/2,
including with a reference. Its conservative gate-count bound on any additional
temporary workspace does not claim a sharper ancilla theorem than was checked.

The new conjugate-sector ablation is labeled separately from the two-round
Weyl-label correlation. It correctly retains the global-phase dependence of
`A=E V`, and identifies loss of trace preservation rather than presenting the
result as a physical randomizer. For the exact fixed-pair representatives,
`A=F_B/sqrt(d)` and `A*A=I/d` are correct. The added full ring check verifies
all 2401 average-matrix entries and 117649 character terms in their Gram matrix:
49 diagonal entries and 2352 vanishing off-diagonal entries. This is an exact
49-dimensional check of that diagnostic, not an enumeration of the growing
full channel.

### Revised independent replay

Python 3.12.14; both extracted programs exited zero with empty stderr.

| Program | Source SHA-256 | Stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_randomization.py` | `1bfd231605751f5d091466dbd5557285dd79a2bb8daba6b5542a268fe8928425` | `6032535acfa0f4b41f4411e1880726e100b2d7735d48926872111c1d1e8c2afe` |
| `verify_bol_small_bias.py` | `7e542e411b57da30d370f8eee1e6b940372c3bdefaed3fbadd0195de91f58326` | `dd32bb4ad062ffd5e383240dbc6b8355fedd542fcd1e75eb38f7271e5f211960` |

The sampler replay still exhausts five finite fields/length settings, 1629 seeds
and 904 nonzero characters, now using the stronger coefficient blocking. It
checks nine larger resource settings for both algorithms. These executions do
not constitute a general Shoup implementation, compiled hardware demonstration,
formal verification, or a proof of optimality against every possible randomizer.
The review accepts the scoped theoretical resource claims and the source-based
comparison, with those limitations preserved.

Signed: ChatGPT `/root/independent_resource_review`, 16 November 2026.
