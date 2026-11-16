# Independent mathematical review: Bol section mixing and local spectra

**Reviewer:** ChatGPT, GPT-6 Astra Pro, agent `/root/independent_review`, session `f3f8e6697369`, 2026-11-16.

**Verdict:** Accepted within the stated hypotheses and scope at scientific commit `2d5c1f3e1d53fec8be802daab5194574af280c07`, tree `eb6e78f3de8ea6460db46c8a5b6a049e5b08fc8f`. No unresolved mathematical defect was found in the reviewed arguments. This is an independent model review, not human acceptance, formal proof certification, a GitHub approval, or certification of historical priority.

The reviewer contributed no manuscript construction or proof. The supplementary independent verification script was written during review; it checks the authors' proposed results and imports neither authored checker. Review suggestions about biadditivity, sector multiplicities and notation were resolved before the scientific pin.

## Exact scope and provenance

The review covers the complete finite and local manuscripts, the controlled comparisons, the intake's central-character calculations and source-use boundaries, and all three executable verifiers. The overview, bibliography, code guide and affected problem routing were checked for consistency with that scope. All 13 changed files were extracted with `git show` from the exact local commit and matched the working files byte for byte.

The preceding source `4565b713ab4d4af183805f08bde67c17f1c5a3b8` was reviewed and executed first. The sole subsequent change is the intake subsection assessing the existing modular construction. Its exact diff was checked against the inspected PR #438 overview and charged-sewing review, which retain scientific source `197d13d4ac2e48763ed20bf418228d7b4d16aa8c` and their own qualifications. The subsection accurately attributes those findings and imports none as a premise of the new averaging theorem. Every mathematical proof and executable is byte-identical between the two source pins. All three verifiers were nevertheless extracted and rerun at the final pin.

## Mathematical checks

### Finite family

The direct loop and left Bol calculations, inverse property, and explicit non-Moufang witness are valid for the stated odd finite fields and every scalar subgroup order `m>=2` dividing `Q-1`, including even orders. This directly verified family needs no simplicity or full-folder theorem.

The actual left translations have the stated correction shears. Their conjugation and coherence identities have the correct order and scalar factors; an ordinary multiplicative representation of the label subloop is not silently assumed. The invariant leaves and the exceptional zero-leaf components are correctly separated.

The Fourier decomposition gives the claimed complete spectrum, signed multiplicities and zero multiplicities. In particular, summing reflection fixed points over all channels handles even `m` correctly. The cubic operator identity, exact norm, all-time point-start total variation, the full-unit value `2/Q^2` after two steps, the exact weighted norm and the unique optimality of uniform weights follow as stated.

The exact sampler's stopping decision depends only on scalar coordinates, so conditioning does not bias the independent uniform vector inputs. Two distinct slopes give the required surjective linear map; the additional ordinary step makes the final scalar coordinate uniform. The stopping tail and expected total of `2+m/(m-1)<=4` transitions are correct.

### Arithmetic and compact local family

The ring loop law, reduction maps, normalized measures and additive-character conventions are compatible. The central-character Fourier formula correctly retains the actual scalar orbit and its stabilizer. Averaging over stabilizer fibers kills their nonconstant modes; the surviving space has dimension `h^2` and is acted on by `h^(-1)` times transposition. This verifies both signed multiplicities, including the `h=1` exceptions, without an extra fiber-dimension factor.

The full-unit conductor counts, all stated finite-ring exceptions, exact two-step total variation, and compact inverse-limit formula are correct. The primitive-leaf restriction is necessary and is retained. In particular, the compactness and Schatten conclusions concern a fixed primitive leaf, not the operator on the whole compact Bol loop.

For arbitrary closed scalar `H`, the formula in terms of its images modulo the conductor is complete. Infinite `H` gives growing orbit sizes and compactness; finite `H` gives a fixed nonzero singular value infinitely often. The possibility of additional fixed vectors when small-conductor images have size one is explicitly retained.

For the unramified rank-`kappa` family, the direct-summand hypothesis and the odd-prime exponential/logarithm give exactly `h_c=(Q-1)p^(kappa(c-1))`. Multiplying `h_c^2` by the number `(Q-1)Q^(c-1)` of central characters gives the displayed spectral zeta function and sharp threshold `D=2+f/kappa`. The weak endpoint, strong endpoint failure, rank-independent gap, exact Hilbert--Schmidt norms of powers and least smoothing/trace-class step counts follow. The finite Teichmuller control is correctly noncompact. The full-unit two-step TV formula is not extended without proof to the thin groups.

### Intake, controls and contribution boundary

The pencil radical and rank formulas, degenerate-specialization examples, Heisenberg dimensions, additional radical-character labels, and separation of character-preserving from sector-permuting symmetries are correct. Biadditivity supplies the class-two cocycle identity; alternation supplies the commutator. The stabilizer projection and section correction data are not discarded.

The symplectic affine-slab identification and metabelian marked-measure realization are valid. The arbitrary scalar-set control correctly shows that the finite incidence identity does not require multiplicative closure or Bol identities. The finite `1/m` norm already follows from the known polar-graph spectrum. Nica's finite-valuation-ring spectrum gives the stated full-unit compression baseline; its compact-limit consequence is labeled an inference. Delgado--Ruzhansky Theorem 3.5 and Remark 3.6 were checked directly in the primary PDF: compactness, invariance and the dimension-weighted symbol sum are accurately retained.

The gain proved for the selected family is its exact mixing/application and conductor-dependent spectral consequences, including the thin-unit rank versus smoothing law. It is not a new Weil bound or an analytic mechanism exclusive to Bol loops. The zero-measure thin subgroup range is not supplied by the stated positive-measure full-unit compression argument. This review does not establish literature-wide priority.

## Reproducible execution

All runs used Python 3.12.14 with assertions enabled. The finite and local authored checkers use only the standard library. The independent checker additionally used NumPy 2.3.5, with exact bounded integer matrix operations and rational probabilities, not numerical diagonalization. Every final-pin run exited zero with empty stderr and reproduced its previous output byte for byte.

From the repository root:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_section_mixing.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_section_local.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_section_independent.py
```

The finite checker passes six original-coordinate cases, including `m=2,4,6`; the smallest loop has exhaustive Bol, inverse, Latin and correction checks. The local checker passes seven orbit cases and six complete two-step path enumerations.

The independent checker passes six full integer cubic-matrix and rational TV calculations, nine ring two-step enumerations including dimension two, and a 486-state `Z/9` conductor-spectrum check. For its degree-54 integer adjacency matrix `K`, it verifies

```math
K(K-54I)(K^2-729I)(K^2-81I)=0
```

and six exact moments, yielding multiplicities `1,6,2,126,90,261` for eigenvalues `54,27,-27,9,-9,0`. These finite checks support the proofs; they do not prove the quantified finite-field or compact-local statements.

| Exact scientific file | SHA-256 |
| --- | --- |
| `manuscripts/bol-section-mixing.md` | `dc2b69332c808c11efee56b8bab3e14cf8758d58caa90048717b22ad820b26dc` |
| `manuscripts/bol-section-local.md` | `19721b36c9eb6a0ef58f403d15be64ff57ea036141c465190461b44f3ce110e9` |
| `manuscripts/bol-section-controls.md` | `47cec6ddaa9a5615d8833036abb946a4cc29804ec2c36bd0ea96b484060bb2b6` |
| `manuscripts/bol-metaplectic-intake.md` | `6644c7ea582645955bc3ea14409e5fe341ab3bce3c2fd6fcaf032c22d398ef50` |
| `code/verify_bol_section_mixing.py` | `3db91a4ae89ef54ccbdc56bbf341e000a8341ff9fc9d4e070a2c17a2cf4672b4` |
| `code/verify_bol_section_local.py` | `4fe2f39adddd25d3866fcc307db8710a4d561459bd12b3ba4ed716379632724e` |
| `code/verify_bol_section_independent.py` | `d1ac7121cbc976b5e02239b4736e5ee32edb13c2518d238a2775290212c8ebab` |

| Verifier output | SHA-256 of complete stdout |
| --- | --- |
| Finite | `6a5910b85f75e3e087c298f0ea4de8f1148e3621946a1f24f2262c2073eb7b21` |
| Local | `51a22d4cf5fb0e9efdd3da080096b2e44b329fbc07039a8e1619dfee2508d0c4` |
| Independent | `bc0023bddc451c688e215b551c772293101c05ecd9f04bc8d360b93b422e7915` |

## Limits and remaining obligation

Acceptance does not re-prove the imported simple-folder, G-loop or strict-isomorphism interfaces; certify the entirety of PR #438; or verify the quasi-RH paper's global zero-free theorem. The finite Heisenberg, local double-cover and global cubic-theta distinctions and the limited cocycle obstruction are appropriately scoped. No cubic automorphic lift, Euler product or quasi-RH consequence is established by this checkpoint.

The strongest remaining mathematical gap is an estimate using the full vector-valued pencil together with the reciprocal stabilizer graph, beyond this scalar-orbit family. The proposed next Gram-kernel calculation is concrete, but no such stronger result is accepted here.

Repository integrity and remote execution are separate from this mathematical review. The coordinator reports 115 local integrity tests passed and final-SHA GitHub run `43835069632` completed with conclusion **skipped**, not passed. The reviewer independently ran the three research checkers above, not that integrity suite. Actual-host rendered Markdown inspection was not completed: the coordinator reports the logged-out browser returned 404. Source review and mathematical acceptance do not certify hosted rendering.

**Signed:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, 2026-11-16. Acceptance binds to scientific source `2d5c1f3e1d53fec8be802daab5194574af280c07` and the file hashes above.


## Coordinator's execution and publication record

This section is by ChatGPT `/root`; the independent attestation above is
unchanged. Its original report SHA-256 is
`406cdd94fbdbd1b0d18acc011b825247f2974ee3efbf8f0804d2eca09b68e278`.

The coordinator separately read and ran all three delivered verifiers. All
passed on Python 3.12.14 and produced exactly the stdout hashes recorded
above. The standard-library local verifier gives two-step total variations
2/9, 56/243, 1514/6561, 2/25, 252/3125 and 2/49 for its six stated cases.
The finite verifier's exhaustive 54-element case and larger sampled cases
are explicitly distinguished in the code guide.

The coordinator ran `python check.py --base
c13096ff4a3e1f07303fd9f9b42adb358ed1688a` successfully: all 115 integrity/tool
tests passed. `git diff --check` also passed. These checks are separate from
the mathematical review and finite research verifiers. Historical review
objects required by unrelated repository integrity checks were restored from
exact GitHub objects; no verification rule or tracked baseline was changed.

The finite manuscript and its verifier were authored by `/root/weil_literature`;
local conductor proofs and their verifier by `/root/quasi_rh_bridge`;
operator ablations, incidence/compact-operator comparisons and thin-rank
consequences by `/root/bol_operator_attack`; the coordinator contributed the
scalar-pencil intake, independent frequency derivation, exact arithmetic TV
calculation and integration. These are collaborating model contributions,
not independent reviews. `/root/repo_integrity` restored Git provenance and
ran infrastructure checks only. Public exposition is attributed to Mira Cult.

The original scientific checkpoint is `4565b713ab4d4af183805f08bde67c17f1c5a3b8`.
The reviewed scientific pin adds only the modular-source assessment. The later
delivery commit adds this record and changes overview/navigation status; the
four scientific manuscripts and three verifiers remain byte-identical to the
reviewed scientific pin. No permanent claim IDs were allocated or changed.

[PR #440](https://github.com/Mira-Cult/math-wip/pull/440) is the canonical
workspace. Its body records the full delivery head and latest CI state.
[Scientific CI run 43835069632](https://github.com/Mira-Cult/math-wip/actions/runs/43835069632)
completed as skipped with no steps executed. The separate browser's logged-out
404 prevented actual-host rendering inspection; authorized connector content
was retrieved and compared successfully. Neither limitation is reported as a
successful CI or rendering check. No repository permissions or CI gates were
changed, and no merge or formal GitHub approval was performed.


---

# Independent review: collective reciprocal-word cancellation

**Reviewer:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, session `f3f8e6697369`, 2026-11-16.

**Verdict:** Accepted within the stated hypotheses and scope at scientific commit `6437948a7c3a1d0e437f2fa51b114875351ae7d8`, tree `0b5187b191cc9ecdaba1973bf7938b1348e413db`. No unresolved mathematical defect was found in the continuation. This is independent model review, not human acceptance, formal proof certification, a maintainer's GitHub approval, or certification of historical priority.

The reviewer contributed no construction or manuscript proof to this continuation. The independently written incidence checker described below is review evidence. The earlier scalar-section acceptance at `2d5c1f3e1d53fec8be802daab5194574af280c07` remains separate; the present verdict follows a new review of the complete continuation.

## Exact scope

The complete canonical manuscript `manuscripts/bol-collective-cancellation.md`, Sections 1--9 and its reproduction statement, was reviewed. This includes the group/coset derivation, direct loop/Bol/properness proofs, actual two-state observable, both Gram identities, weights, same-rank comparison, tensor theorem, degree and counting corollaries, architectural controls, and the specified conductor-lift obstruction. The complete authored verifier and all five changed navigation/bibliography/code-guide files were inspected. All seven changed files were extracted from the exact local Git object and matched the reviewed working bytes.

A preliminary autocorrelation sign inconsistency was identified during review. The scientific source resolves it by explicitly using `R(b)=sum_j w_j e_3(-jb)`, and the checker now uses the manuscript's negative Fourier exponent in both coefficient calculations. The unordered weights, subspace masses and norm formulas were unaffected. The final source also explicitly restricts the degree formula to `1<=d<=h`, retaining the separate constant channel.

## Mathematical findings

### The observable comes from the actual reciprocal section

The class-two multiplication, balanced scalar action, stabilizer graph, right-coset reduction and inverted section give the displayed law with the stated signs. The direct division formulas establish the loop property. Balancedness and the vanishing of `b(U,R(c)U)` give the claimed left Bol identity. The flexibility witness has distinct vector coordinates `(1+lambda^(-1))e` and `2e`; properness therefore needs no imported simplicity or classification theorem.

The word calculation in Section 2 is correct. After the penultimate multiplication its last scalar coordinate is `s-F_B(u,a,y)`, and the final multiplication changes the first vector coordinate by `lambda^(s-F_B)e`. Taking the character of the difference between the last two states cancels the earlier `u+y` term. The definition cannot be replaced by the character of the final state alone.

The field trace gives the two-valued function `vartheta(0)=1`, `vartheta(t)=omega^(-1)` otherwise. Its Fourier weights are exactly `31/49` and six copies of `3/49`. The simultaneous label reversal for a nonresidue leaves every scalar kernel unchanged. Hence the round-trip Gram identity (4) is correct, with `18/49` occurring once overall, not once per block.

### Gram, weights and sharpness

All counting measures are normalized consistently. Averaging the adjoint product over the shared actor parameter removes unequal central labels; averaging over the vector parameter gives the exact radical indicator. The normalized Fourier transform of that indicator has density `Q^(-r_nu)` and support `im B_nu`. This proves both (5) and (6), including zero and degenerate specializations. The input is shared across sectors; it is not an orthogonal direct sum with independently chosen inputs.

The Gauss-period calculation, all 13 projective hyperplane masses, and the five line masses are correct. A nonzero good-pencil frequency imposes a nontrivial coefficient-row constraint, so its surviving parameter set is contained in a hyperplane. The maximal mass is `343/729`, and the displayed frequency attains it.

Both triples are independent with zero common radical, and every nonzero labeled specialization has rank four. The cross-product image calculation remains valid for isotropic parameter vectors. For the aligned pencil, independence of `1,lambda,lambda^2` makes the final alternating block regular; its common image supplies the maximizing nonzero frequency with mass `721/729`. Consequently the aligned norm proves sharpness of the bound available from separate sector norms and the same weights. This is an exact comparison with identical pointwise rank data, not merely matching rank histograms.

### Infinite-family and counting consequences

The direct-sum construction has the stated loop order and complete matching rank strata. Tensorization applies to every function in the full block-centered subspace, including correlated linear combinations. Theorem C's exact norm ratio `(343/721)^(h/2)` and its expression as `N^(-delta)` are correct, with fixed positive `delta` and no hidden dimension-dependent factor.

The degree refinement correctly uses the common constant multiplier `A_0`. Since both nonzero maxima are strictly smaller than `A_0`, the maximum on the degree-at-least-d space occurs with exactly d active blocks. Global mean zero gives only the stated constant-factor ratio; a proportional number of active blocks is necessary for the exponential comparison. The constant channel is excluded from that formula.

For centered input the exact identity `R_B f=(1-omega^(-1)) I_B f` holds, and its absolute scalar factor is `sqrt(3)`. Thus the incidence norm factor `sqrt(6)/7`, the sharp operator bound (20), and the multilinear discrepancy (21) follow with the displayed normalization and density factors. These are averaged-output estimates, not pointwise estimates at every output.

This is a substantive scoped analytic application: it gives a sharp inequality on an explicit infinite family of function spaces and a counting consequence for specified equations. The exponential ratio is tensorization of a fixed-block gain. It does not demonstrate a new cancellation mechanism between coupled blocks or improve the abstract exact weighted-incidence principle.

### Controls and arithmetic boundary

The fixed left-translation architecture has the stated central-character block decomposition. The uniform right-axis walk control is valid from the identity: its factorized scalar-invariant densities are preserved, and the two changes of variables eliminate the reciprocal scalar actions. This is not a claim about all starting distributions or nonuniform observables.

Rebracketing the chosen word, or deleting either reciprocal action, makes its displacement readout independent of the input variable and kills centered inputs. Ordinary Fourier analysis still analyzes the resulting kernel, and the marked enveloping-group/coset description preserves it. No faithful ordinary multiplicative representation of the loop is asserted.

The conductor-lift obstruction is valid for the stated finite characteristic-three scalar-field architecture. Equivariance at `t=7^A` forces an additive reduction to vanish on multiplication by `lambda_(A+1)^(7^A)-1`. That scalar is nonzero and invertible, hence the reduction is zero. The conclusion does not apply automatically to different local-ring models or correspondences.

## Literature and scope boundaries

The cited primary locators for Casazza--Kutyniok's projection frame operator, MacWilliams's complete-symbol identity, Gow--Quinlan's radical-line correspondence, the rank-support framework, and Friedlander--Shparlinski's double-exponential theorem were inspected. Their stated roles and restrictions are accurate. In particular, the Gram may have a kernel, and the frame interpretation is then on its range. The rank-only relaxation is improved; the established exact Gram principle is not.

The proof does not establish historical priority, reconstruction of the entire pencil from the weighted Gram, or nonisomorphism of the unmarked loops. It proves an estimate depending on joint image positioning that the given individual ranks cannot determine. It does not certify imported simplicity/G-loop interfaces, a new Weil representation, a cubic metaplectic lift, automorphy, or a quasi-RH consequence. Coupled pencils, nonproduct readouts and a compatible conductor correspondence remain distinct next obligations.

## Exact execution and independent evidence

Both runs used Python 3.12.14 with assertions enabled, only the standard library, exact arithmetic, exit code zero and empty stderr.

The authored checker was extracted from the scientific commit and executed. It checks all 729 field traces and nonzero inverses, both 27-entry scalar-rank profiles, common radicals and independence, maximizing incidences, exact cyclotomic weights and projective masses, and 64 sampled Bol/word cases per family with seed 20261116. Its direct one-way restriction has 27 inputs and 729 outputs and checks 19,683 readout pairs plus all 27 Fourier multipliers.

The reviewer separately wrote `verify_collective_incidence.py`, importing neither the authored checker nor its field/cyclotomic implementation. It uses the actual restriction `u in lambda*F_3^3`, `y in F_3^3`, with the second block zero. Here `beta=u cross y`. Exact counting in the incidence observable and exact arithmetic in `Q(sqrt(21))` and `Z[omega]` check all 27 Gram multipliers, 19,683 word-difference cases and 137,781 round-trip correlation terms. The restricted output has 5,103 points. Its centered squared norms are:

| Restricted observable | Exact squared norm |
| --- | --- |
| One-way | `343/6561` |
| Incidence | `14/2187` |
| Round trip | `14/729` |

The constant channels also match the full Gram formulas. These experiments do not enumerate the full `E^6` matrix or prove the arbitrary-h theorem; the written proofs supply those assertions.

| Artifact | SHA-256 |
| --- | --- |
| Canonical collective manuscript | `7a923a8e6d5f7eee85b44f43c9cffe8504e9f0a715e60c2661ecc8402cfe885d` |
| Exact committed authored verifier | `7899f013a8229ecfeb6c6ab518c24f11e7155e942e9724856440eb804c5b144e` |
| Complete authored stdout | `cf30b93684987e9afe190e2f42f805f5726a099750be394346ee505ea9defa3b` |
| Independent incidence verifier | `8011d23cef94dfa7ba23d056c06e9b35990bb54a049cff1a90fb64ffd83cd33a` |
| Complete independent stdout | `7a35631f68fa23e41023ec270c5a446c7d4e34541ec4081924a7537654676d1f` |

The independent verifier is reviewer-authored evidence produced after the scientific source; adding it in a delivery commit does not modify the reviewed mathematical proof. Repository integrity is separate: the coordinator reports 115 local integrity tests, 47 relative-link checks and `git diff --check` passed. The reviewer independently executed the research checkers above, not those repository checks. The coordinator reports final-source workflow `43846626606` completed with conclusion **skipped**, not passed. Actual-host rendered Markdown inspection remains unverified.

**Signed:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, 2026-11-16. Acceptance binds to scientific source `6437948a7c3a1d0e437f2fa51b114875351ae7d8` and the scientific hashes above.


Coordinator provenance: the preceding continuation attestation is reproduced verbatim.
Its original report SHA-256 is
`7f342f77d01432be5bb6bc23d2c6bed57c1ebc14b106a95c4788a295c7ea29f5`.
The subsequently added coupled Theorem D requires a new exact-source review;
this earlier tensor-checkpoint acceptance is retained as history.


---

# Independent review: coupled pencils on all mean-zero inputs

**Reviewer:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, session `f3f8e6697369`, 2026-11-16.

**Verdict:** Accepted within the stated hypotheses and scope at scientific commit `ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`, tree `f081043266b29bdfcb0b3e77ab8e4e5376d80441`. No unresolved mathematical defect was found in the coupled continuation. This is independent model review, not human acceptance, formal proof certification, a maintainer's GitHub approval, or certification of historical priority.

The reviewer did not devise the coupled construction, Lemma M, or the manuscript proofs. The independent tests described below are reviewer-authored evidence. The accepted scalar checkpoint `2d5c1f3e1d53fec8be802daab5194574af280c07` and tensor checkpoint `6437948a7c3a1d0e437f2fa51b114875351ae7d8` retain their original scopes. Their acceptance alone was not treated as acceptance of this new theorem.

## Exact scope and source binding

The complete new Section 6A of `manuscripts/bol-collective-cancellation.md` was reviewed, including the field choices and injections, both alternating pencils, admissibility, scalar ranks, trace-dual image condition, Lemma M, attainment, Theorem D, the absolute power bound, and the arbitrary-subset incidence estimate. The interfaces with the existing section construction, actual two-state Bol observable, Gram formulas, exceptional scalar sector and counting normalization were checked. The complete diff from the accepted tensor source was inspected, including the changed lead, literature comparison, remaining-bottleneck statement, overview, problem routing, bibliography, code guide and historical evidence.

All ten changed files were extracted from the exact Git object and matched the reviewed working bytes. The unchanged original collective verifier was extracted as an eleventh file. The prior tensor review is embedded verbatim in the evidence history. Both reviewer-authored checkers in the source match their original scratch files byte for byte. The five collective verifiers were read and independently replayed from this extracted source. Exact file hashes, complete stdout/stderr and run metadata are preserved in the review evidence.

The earlier Bol-law, properness, word, Gram and arithmetic-obstruction proofs are unchanged by this continuation. Their earlier review remains applicable. The current stronger claim is supplied by the new coupled pencil, not by an extension of tensorization beyond its valid input space.

## Mathematical findings

### Admissibility and trace geometry hold for every stated parameter

The injections from `F_3^(2h+1)` into `L_h=F_(729^h)` and `M_h=F_(729^(2h-1))` exist for every `h>=1`, including the endpoint `h=1`. The lexicographic irreducible-polynomial prescription supplies an explicit uniform family, while the theorem correctly allows every pair of injections.

For nonzero `t`, the trace-determinant form has radical exactly `L_h(t,t^3,t^9)`, hence E-rank `2h`. A vector outside this line makes the determinant surjective as a function of the second argument, so the nonzero trace functional does not enlarge the radical. Doubling gives rank `4h`. Radical lines for two nonzero parameters coincide only when those parameters are proportional over F3; the parameter space supplies distinct lines and therefore zero common radical.

For the aligned pencil, the star block has rank two, and the trace-symplectic block has rank `4h-2`. Their total dimension is `6h`, their nonzero ranks are `4h`, and the common radical is zero. Thus the two constructions have identical ranks at every labeled scalar specialization, not merely equal rank histograms. Their F3-linear independence follows from the nonzero ranks. Independence over E is neither required nor generally true. The stated loop order `3^(38h+1) 7^(4h+3)` is correct.

The trace-dual identification is valid even when three divides an extension degree. Annihilation of the entire L-radical line gives an equation in L, rather than merely a zero absolute trace of one distinguished generator. Consequently every nonzero spatial frequency imposes a nonzero linearized polynomial of degree at most nine, and its compatible parameter space has F3-dimension at most two. The zero scalar parameter must still be removed: its matrix image is `{0}`, although the polynomial equations are vacuous there. The theorem subtracts precisely this atom.

The manuscript correctly separates the spatial trace-dual identification from the word readout. The latter retains an E-linear functional taking value one at the chosen vector. A bare extension trace at the vector `1` would destroy the readout when `3` divides `h`; that replacement is explicitly excluded. These distinctions were also tested independently at `h=3`.

### The product-measure maximum and its attainment are correct

Lemma M holds as stated for every probability distribution used identically in all coordinates over a finite field, with `1<=d<k`. Coordinate pivots express a d-plane as the graph of `r=k-d` linear forms in independent variables of law w. Hölder reduces its mass to a geometric mean of r moments. Each nonzero linear form has a law that is a mixture of affine permutations of w; rearrangement bounds the corresponding moment by `P_(r+1)`. A zero form gives `w(0)^r`. Both alternatives are attained by the displayed graph choices. This establishes the exact maximum, not just the weaker maximum-atom bound.

For the reciprocal weights, `P_2=13/27>2/9`; Jensen therefore selects the `P_(r+1)` alternative. All subspaces of dimension at most two have mass at most `P_(2h)`, with equality at `{(s,...,s,t)}`. The explicit degree-nine polynomial in (27) has exactly the nine roots in any prescribed parameter plane. Its coefficient vector is a nonzero spatial frequency realizing that plane. Thus the maximizing subspace is accessible to the actual pencil for every allowed injection; there is no gap between the abstract mass bound and the operator norm.

### The exact norm gives the claimed unrestricted analytic gain

Let `a=2/9`, `b=(7-sqrt(21))/18`, `m=(7+sqrt(21))/18`, `P_j=a^j+b^j+m^j`, and `Q=729`. Combining the image constraint with the already verified normalized Gram identity gives exactly

```math
 \|\mathcal R_{\mathrm{sp},h}|_{L^2_0}\|^2
   =\frac{18}{49}Q^{-4h}(P_{2h}-a^{2h+1}),
 \qquad
 \|\mathcal R_{\mathrm{al},h}|_{L^2_0}\|^2
   =\frac{18}{49}Q^{-4h}(1-a^{2h+1}).
```

The common first coordinate in the aligned star images attains the separate-sector baseline. The spread norm is attained by the frequency just described. The factor `18/49` occurs once overall, as required by the shared final scalar state; it is not multiplied once per parameter coordinate or extension degree.

The displayed exact ratio, its bound `sqrt(343/721) m^(h-1)`, and its asymptotic equivalence to `m^h` are correct. With `N=Q^(6h)`, the absolute bound has the stated constant `sqrt(14)/(9m)` and fixed positive exponent improvement `log(1/m)/(6 log Q)`. No dimension-dependent constant cancels that gain. Unlike Theorem C, this result applies to every mean-zero input, without an active-block or product-input restriction.

On centered inputs, the existing identity between the round-trip and incidence operators divides squared norms by three. Cauchy--Schwarz then gives (31) for arbitrary input and output subsets with the stated density factors. The interpretation relative to the input-density share of the output set's total incidences is correct; uniform output degrees are not assumed. These remain normalized L2 and averaged-output estimates, not pointwise cancellation claims.

The result is a substantive analytic application within its stated family: an explicit unrestricted operator estimate, a matching aligned baseline with identical pointwise rank data, attained constants, and a counting consequence. The gain depends on joint image positioning across the character sectors, which their individual ranks cannot determine. It does not improve the general exact weighted-Gram identity itself.

## Literature and remaining mathematical boundaries

The new primary references were inspected at the cited versions: Sheekey, arXiv:1504.01581v2, Section 2's root-count paragraph before Theorem 2 and Remark 2; and Gow--Quinlan, arXiv:0709.0741v1, Section 2, especially Lemma 1, Corollary 1 and Lemma 2. Their roles in the manuscript are accurate. The degree bound and Moore/Gabidulin evaluation geometry, perfect trace pairing, and trace-based alternating constructions are established ingredients. The manuscript makes no new MRD-code claim. Lemma M has a direct Hölder/rearrangement proof; the review does not certify that its standalone statement or this exact application has no prior occurrence elsewhere.

The actual two-state observable and both reciprocal actions remain essential to the claimed Bol-derived application. The earlier controlled deletions and rebracketing tests are unchanged. Ordinary Fourier analysis of the marked section/enveloping-group data proves the estimate; no faithful ordinary multiplicative representation of a nonassociative loop is assumed. No conclusion about unmarked-loop nonisomorphism or an imported simple-loop classification is used.

The family is finite at fixed primes 3 and 7. The previously proved obstruction still excludes nonzero additive reductions equivariant with consecutive faithful 7-power scalar actions. The proposed replacement by a specified correspondence or induction, with compatible conductors, Gram operators and normalized measures, remains an open next task. Neither this theorem nor the scalar checkpoint establishes a cubic metaplectic lift, automorphy, an Euler product, or a quasi-RH consequence.

## Exact execution and independent evidence

All five committed programs were executed by the reviewer using Python 3.12.14 with assertions enabled. Every run exited zero with empty stderr. The coupled and plane-mass authored programs used NumPy 2.3.5 solely for bounded integer field tables and exact finite-field elimination. The other three programs use the standard library. The plane-mass program imports the authored coupled implementation, so those two are not independent implementations.

The authored coupled program checks every scalar parameter for `h=1,2` (27 and 243 parameters), including alternating matrices, F3-linearity, ranks, common radicals and the aligned common image. It tests every parameter against 260 sampled or constructed nonzero linearized polynomials per h, compares their kernel sizes with exact F3 nullities, and performs 324 and 2,916 direct scalar-image membership checks. It does not exhaust all polynomial coefficients or all spatial frequencies.

The authored plane-mass program exhausts all 13 two-planes in `F_3^3` and all 1,210 in `F_3^5`, using exact `Q(sqrt(21))` arithmetic. It obtains maximum masses `13/27` and `127/729`, then checks the explicit attaining polynomial and membership in exactly eight nonzero scalar images. The respective nonzero image masses are `343/729` and `10255/59049`.

The reviewer-authored `verify_bol_coupled_independent.py` imports no authored checker. It independently implements the field and the Artin--Schreier extension `E[T]/(T^3-T-lambda)` at `h=3`, where the trace of one is zero. The trace pairing still has rank three. On the parameter space `E + F3*T`, it checks 71 nonzero test parameters, single-copy rank six, duplicated rank twelve, zero common radical, F3 tuple rank seven and E tuple rank four. It exhausts all 2,187 parameters for the attaining subspace polynomial, finding precisely the required nine roots and plane mass `12598/177147`. It independently repeats the exhaustive 13-plane and 1,210-plane maxima. The seed is 20261117.

The unchanged original collective checker and reviewer-authored incidence checker were also rerun. They reproduced their previously recorded output hashes, including the direct small-restriction checks of the actual word, the shared Gram prefactor and all restricted Fourier multipliers. The new extension-field scripts do not independently rederive that prefactor. These finite experiments support the interfaces and edge cases; the written arguments establish the all-h statements and the general probability-distribution version of Lemma M.

| Artifact | Source SHA-256 | Complete stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_collective.py` | `7899f013a8229ecfeb6c6ab518c24f11e7155e942e9724856440eb804c5b144e` | `cf30b93684987e9afe190e2f42f805f5726a099750be394346ee505ea9defa3b` |
| `verify_bol_collective_independent.py` | `8011d23cef94dfa7ba23d056c06e9b35990bb54a049cff1a90fb64ffd83cd33a` | `7a35631f68fa23e41023ec270c5a446c7d4e34541ec4081924a7537654676d1f` |
| `verify_bol_coupled.py` | `9c9aa2ed62c23a2d32b68617d58f53a6dd027c55e00b749c67725e521f139c4a` | `a04e75cdf3320e8e8ace02b830d32b4c39dfe46e72f0de3fdd1046feb3d3cb59` |
| `verify_bol_plane_mass.py` | `e60fc1e264ce92e013548c6dcff9915615af93577f6ee7f5edb411ff091103e5` | `8f3fdd420090dd67541f52d55ecab50e36eec7cc628cf63fa1d0d75b8a45d1dc` |
| `verify_bol_coupled_independent.py` | `917fcf2102b48c153c35b8effbf79d8bd62a7ee2d57fdb9f46917663e7a75470` | `3d716ffaf493487de6401eee931dbb8ddbf9a2a656b519f8fd2f5cd512afc10f` |

The exact canonical manuscript SHA-256 is `8866a7e03f849cb0f78b1bc409d4038e40b92f6194227542b2c2568cbad48c06`. The complete extraction record is `coupled-pinned-hashes.json`; each execution has a corresponding `coupled-replay-*.run.json`, `.stdout` and `.stderr` in the review scratch evidence. These records bind actual reviewer runs, not coauthor runs attributed to the reviewer.

The reviewer also ran `git diff --check` between the accepted tensor pin and the new scientific pin; it passed. Repository-wide integrity tests and hosted CI are separate from this mathematical review. The coordinator reports 115 local integrity tests passing, 44 relative-link targets existing, and all seven older scalar proof/verifier files byte-identical to their accepted checkpoint. The coordinator observed scientific-source workflow `43850271556` completed with conclusion **skipped**, not passed, at `ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`. These coordinator checks are not attributed to the reviewer. Actual-host rendered Markdown inspection remains unverified. No full huge operator matrix, formal proof assistant, or exhaustive historical-priority search was used.

**Signed:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, 2026-11-16. Acceptance binds to scientific source `ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`, tree `f081043266b29bdfcb0b3e77ab8e4e5376d80441`, and the scientific hashes above.


## Coordinator's coupled-checkpoint delivery record

This section is by ChatGPT /root. The independent report immediately
above is reproduced verbatim; its original SHA-256 is
`61640424ac153422c95055e80494bb419c4e886ed64a8de16ec513ca8e626179`.

The coordinator separately read and ran all five collective programs. Each
passed with the exact source and stdout hashes in the review table. The
extension-field and plane programs use NumPy 2.3.5; the other three use only
the standard library. All delivered runs used Python 3.12.14. The
[code guide](../code/README.md) gives the commands and distinguishes exhaustive
parameter checks, sampled coefficient checks, independently implemented
checks, and the actual restricted-word enumeration.

The coordinator ran `python check.py --base c13096ff4a3e1f07303fd9f9b42adb358ed1688a`
successfully, with all 115 integrity/tool tests passing, and checked relative
links and `git diff --check`. These checks validate repository behavior and
presentation sources, separately from the mathematical review. The older
four scalar manuscripts and three scalar verifiers were compared byte for
byte with `2d5c1f3e1d53fec8be802daab5194574af280c07`; all are unchanged.

The complete coupled scientific source is
`ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`, tree
`f081043266b29bdfcb0b3e77ab8e4e5376d80441`. This delivery adds the review
and adjusts status, navigation and reproduction instructions only. The
collective manuscript and all five collective verifiers remain byte-identical
to that reviewed pin. The proof work was coordinated by /root with coauthor
support from /root/bol_operator_attack, /root/quasi_rh_bridge and
/root/weil_literature; those contributions are not independent review.
The noncontributing reviewer and the independently authored evidence are
identified in the signed report. No permanent claim IDs were allocated or changed.

[PR #440](https://github.com/Mira-Cult/math-wip/pull/440) is ready for maintainer
integration and records the exact delivery head and current remote CI state.
[Scientific run 43850271556](https://github.com/Mira-Cult/math-wip/actions/runs/43850271556)
completed **skipped**, so it is not a successful remote validation.
Actual-host rendered Markdown remains unverified because the separate
logged-out browser could not access this private repository. Authorized
connector retrieval and exact Git tree matching confirmed source publication.
No CI gate or repository permission was changed; no merge or formal GitHub
approval was performed.


---

# Independent review: arithmetic conductor correspondences

**Reviewer:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, session `f3f8e6697369`, 2026-11-16.

**Verdict:** Accepted within the stated hypotheses and scope at scientific commit `f85696062308e2b2511af8c73744766ec62a9dc8`, tree `bc8c3ba096ae14213c5bc991715ec12740edc0dd`. No unresolved mathematical defect was found in this continuation. This is independent model review, not human acceptance, formal proof certification, a maintainer's GitHub approval, or certification of historical priority.

The reviewer contributed no construction or manuscript proof to the conductor continuation. The standalone independent checker described below is review evidence. The earlier scalar, tensor and coupled-pencil acceptances remain bound to their respective scientific checkpoints. Their acceptance was not automatically extended to the new arithmetic statements.

## Exact scope and source binding

The complete `manuscripts/bol-conductor-correspondence.md`, Sections 1--10, equations (1)--(49), and reproduction statement were reviewed. This includes the actual prime-power Bol models and marked word, all trace and conductor channels, vector kernel and its norm, filtered descent and corrections, full stable transport, kernels and coherence, full norm comparison, Hilbert limit, equivariance obstruction, product-mixture extremum, sharp arithmetic estimates, asymptotic and counting consequence.

The two authored verifiers, the independently written verifier, the source/baseline citations and all five revised navigation/bibliography/code-guide files were inspected. All nine changed files were extracted from the exact Git object and matched the reviewed bytes at extraction. The unchanged `verify_bol_collective.py`, imported by the authored vector verifier, was extracted as a tenth file and matched its previously accepted source hash. All three new verifiers were actually executed by the reviewer from this extraction. The independent committed verifier matches the reviewer's original scratch program byte for byte.

The predecessor delivery is `d6edc4f86ae6ff7fc5216afa1565958abac4418c`, whose coupled scientific checkpoint is `ab2af8ae4f8437ca9451bb71a1bc66592daa57ce`. The new scientific diff changes none of the earlier mathematical proof or verifier files. Exact extraction hashes, stdout/stderr and run metadata are preserved separately from the report.

During preliminary review, a representation-dimension explanation was corrected: a transverse symplectic quotient of cardinality `q_A^(6r)` has Heisenberg representation dimension `q_A^(3r)`. The correspondence factor is the inverse of the latter, not its inverse square root. The numerical kernel factor was already correct. The final source also explicitly retains contractivity in the translation-equivariance obstruction, mean-zero hypotheses in the overview identities, and the actual finite control family used by the authored vector experiment. No outstanding correction remains.

## Mathematical findings

### The actual model and conductor readout are correctly retained

The order formula for three modulo `7^A`, compatible roots `lambda_A`, and unique order-three lifts `eta_A` give the stated nested fields and ring actions. The section and direct Bol calculations require balancedness, the alternating self-pairing identity and invertibility of two; these hold over the displayed additive modules with `Z/7^A` planes. The same flexibility witness proves properness. Neither simplicity nor an unverified classification interface is used.

The original marked vectors and the two-state word are retained. Its final vector increment is `lambda_A^(s-F_A)e`, and the chosen E_A-linear functional takes value one at e. The relative trace identity (5) is correct. It yields the six-point shell formula, including the exceptional zero argument, and every Fourier coefficient in (7). The primitive, nonzero imprimitive and constant weights have the stated values and sum to one.

Direct shell-intersection counting proves (8), including its potentially negative coefficient of the constant projection at level one. The complete identity is positive; the manuscript does not incorrectly claim that each displayed summand has a positive coefficient. Formula (9) follows by the normalized Fourier/orthogonality calculation with all scalar ranks retained. The zero center frequency and zero pencil label vanish on centered input for their stated, distinct reasons.

### The vector correspondence has the correct measures, kernel and scaling

Every relative extension degree is one in characteristic three. Thus trace restricts to the identity on the lower field, and the higher field splits orthogonally as the lower field plus its trace kernel. The trace pairing on the complementary summand is nondegenerate. This gives the exact decomposition (10), the isometric trace inflation, and the indicator factorization (15).

For each pencil label, the transverse kernel density is exactly `(q_A/q_B)^(r_nu)`. The zero label has density one. Gaussian elimination over the lower field justifies this count, including degenerate nonzero specializations. Normalized averaging against the indicator, multiplied by its inverse square-root density, gives the adjoint pair (13)--(14). Their product in the stated order is the identity, so the map is a norm-one coisometry with the claimed fiberwise nullspace.

The actual trace-inflated phase outputs lie in the adjoint range. Compression is therefore lossless on that range; the remaining square-root density is intrinsic dilution already present in the higher-level operator. Successive orthogonal trace decompositions split both the kernel conditions and normalized measures, giving the stated coherent composition. This argument is not point restriction with an uncontrolled ambient norm.

### The filtered and full correspondences have different, accurately stated scopes

The filtered center averaging preserves absolute additive conductors among the retained labels. The Markov multiplier is one on divisible labels and `-1/6` on primitive lower labels. Its positive averaging kernel is consistent with that negative Fourier multiplier. The exact shell relation yields the all-input correction (19); the centered scalar formula (20) follows only after the zero sector is removed and the nonzero ranks are constant.

The old-character Gram (21), its factors 36 and 1, and the positive new primitive multiplier (22) are correct. These formulas explicitly retain the energy that filtered descent discards. A contraction identity alone would provide a lower bound upstairs, and the manuscript correctly avoids reversing it into an upper estimate.

Histogram separation under `7^(A-1)>k^2` follows from the Eisenstein norm `3S`, with `0<S<=k^2` for distinct histograms and seven coprime to three. The stronger threshold without an unnecessary factor three is justified. The preserved collision at `A=2,k=3` shows that unconditional separation would be false.

In the separated range, the translated readouts have the exact Gram (25). With normalized histogram measure, the factor `sqrt(m_A M/18)` makes V_A isometric on the mean-zero histogram space. Its adjoint, the factorization (28), central kernel (32), complete kernel (33) and conductor covariance (35) have the correct normalization and conjugations. The two different averages b_A and z_A are not conflated: the full-input correction (34) distinguishes the uniform histogram average from the symbol-sequence average.

Theorem T's transport and compressed-Gram identities follow because both intermediate compressions are lossless on the output of a trace-inflated centered input. The stated nullspace is exactly the complementary central readout space plus the transverse complement within it. The adjoint-composition operator is the displayed orthogonal projection. Coherence follows from the vector coisometries and the identity `V_B* V_B=I` on histogram mean zero.

Losslessness here concerns the specified trace-inflated output range; it is not asserted for every possible higher-level input. The whole higher-level norm is handled by the separate positive-incidence argument below. Full transport can mix additive conductors, with its matrix explicitly recorded. Conversely a quotient-translation-equivariant contraction must kill the new primitive characters and strictly loses norm on a histogram difference with unit phase difference. Contractivity is essential and is explicitly assumed in the final statement.

### Full norms and the Hilbert limit do not rely on reverse descent

The histogram weights are nonnegative, conductor-independent and sum to one. A higher-field frequency decomposes into lower-field components; membership in a scalar image holds precisely when every component belongs to the corresponding lower image. A nonzero component therefore has at least as large a weighted incidence, and lower frequencies remain available upstairs. This proves the full norm identity (38) on all centered inputs, independently of the one-way transport inequality.

For a fixed pencil satisfying the constant-rank hypothesis and stable conductor levels, the normalization `sqrt(m_A) q_A^(r/2)` gives exactly constant mean-zero norms. The specified input embeddings and output adjoint embeddings are isometries and compose coherently. Losslessness upgrades descent to the forward intertwining identity (39), so these operators define a bounded map between the Hilbert direct limits, with the same norm.

The input limit is correctly identified with the mean-zero L2 space of the additive inverse limit under trace, with normalized Haar measure. The output is the stated Hilbert direct system. This does not construct a projective limit of the original loops, assert quotient equivariance of the faithful scalar actors, or identify a local metaplectic representation. The exceptional constant input mode is retained in (48); it tends to eigenvalue one and does not share the centered normalization.

### The sharp arithmetic consequence is proved for the stated family

The product-mixture lemma (40) is valid. Hölder is applied to the joint law of the mixture parameter and the pivot variables. Each nonzero linear form is bounded by the integrated rearrangement moment, while a zero form gives the integrated zero-atom moment. The two alternatives are simultaneously attained by fixed coordinate graphs. The proof does not exchange an integral with a pointwise maximum.

The random-phase representation of the histogram weights and their moments in (41) are correct. Moment log-convexity selects `3C_(k-d+1)` as the exact subspace maximum. The previously reviewed degree-nine construction attains every parameter two-plane. Base change of the fixed matrices preserves the needed bound and attainable planes, including when seven divides h; it does not require the scalar-extended auxiliary algebra to stay a field.

Consequently the two complete centered squared norms are exactly

```math
 \frac{18}{7^A}q_A^{-4h}(3C_{2h}-C_{2h+1})
 \quad\hbox{and}\quad
 \frac{18}{7^A}q_A^{-4h}(1-C_{2h+1})
```

throughout the stated stable conductor range. The aligned family attains the bound obtained by keeping scalar ranks and weights but discarding joint image conditions. This is a sharp comparison of families with identical labeled scalar ranks, not just an invariant distinguishing two examples.

The Gaussian domination in (44), the rescaled dominated-convergence proof of (45), its constant `3sqrt(3)/(4pi)`, and the norm-ratio asymptotic and uniform bound in (46)--(47) are correct. The gain is polynomial in h in this range; it is properly distinguished from the level-one exponential gain. The exact ratios for h=1 and h=2 are reproduced independently. The counting bound (49) follows with `1/sqrt(M)` from the precise histogram normalization and applies to arbitrary subsets, without a product assumption or uniform output degrees.

This is a substantive arithmetic analytic continuation of the specified marked word: full conductor bookkeeping, explicit coherent kernels, exact norms including all primitive channels, a bounded normalized limit and a counting consequence. It does not improve the general exact weighted-Gram principle.

## Primary-source comparison and remaining boundaries

The new cited primary interfaces were inspected: Henniart--Wang, arXiv:1303.5141v1, Lemma 3.1(i) and Theorem 4.1; Gurevich--Hadani, arXiv:math/0612765v2, Proposition 2.9 and Theorem 2.10; and Gurevich--Hadani, arXiv:0705.4556v4, Propositions 2.7.1 and 2.7.5. Their stated roles are accurate. Normalized Shintani class-function compatibility, trace-center pullback, tensor products and isotropic reduction do not by themselves transport a marked reciprocal word. The manuscript proves the additional kernel, shell, histogram and joint-image identities directly.

The current output model does not support a claimed compatible quotient action of every central translation. The explicit obstruction explains why a larger induced model retaining primitive representations is a concrete remaining task. No representation of a local metaplectic cover, Euler product, global automorphy, analytic continuation or cubic-metaplectic/quasi-RH consequence is established. Historical priority of the exact application or standalone mixture lemma is not certified by this review.

## Exact execution and independent evidence

All three committed conductor programs were executed from the exact Git extraction using Python 3.12.14 with assertions enabled. Every run exited zero with empty stderr. The central authored program used NumPy 2.3.5 only for bounded integer arrays. The vector authored program and independent program use the standard library. The vector program imports the earlier authored field implementation and is not an independent implementation.

The authored central program checks every trace power and central Fourier character through A=4, all conductor strata and central transfers in that range, compatible marked shifts, all histogram weights for k=3,5, and all 13 and 1,210 parameter two-planes. It checks the full finite histogram Gram at `(A,k)=(3,3),(4,5),(3,5)`, including the sharper separation range, and preserves the collision below threshold.

The authored vector program checks the actual extension `E1[t]/(t^7-lambda)`, traces and pairings, and all 27 labels of the earlier six-dimensional cross-product/star controls. It checks trace splittings, sampled Bol triples and both word bracketings at central orders seven and 49. Its exact restricted coisometry/coherence test enumerates 19,683 phase terms in two identified trace blocks. It does not enumerate the full transverse fiber or claim to test every general coupled pencil.

The reviewer-authored standalone program imports no authored checker. It independently constructs `F3[X]/Phi_(7^A)` for A=1,2, tests 48 actual Bol/word cases per level for the explicit `n=2,k=1` alternating pencil, checks all 42 relative-trace basis elements, the trace-kernel ranks and 64 orthogonal trace splittings. For the sparse readout expression it directly computes translated-readout Grams at A=3,4,5, verifies adjoint moments on a basis of the zero-sum histogram space and an extra complex coefficient vector, and checks normalized transport energies. It finds the old-projection energy fraction `6/7` for a unit phase difference. It independently recomputes histogram weights and exhausts two-planes for k=3,5 using pairs of projective points, obtaining squared ratios `26/53` and `350/1511`. Its seed is 2026111607.

The full vector-space operators are too large to have been enumerated in these checks. The all-level constructions, exact kernel counts, mixture theorem, Hilbert limit and asymptotic rely on their written proofs, not finite extrapolation. The independent finite program was frozen before the scientific pin and copied into it verbatim.

| Program | Source SHA-256 | Complete stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_conductor_central.py` | `3a6109c727892c6b466d2863e4e2cb1c5c875ffc43a2a98e56bc3bb2f6754012` | `7a463ccb6895cd57aab74d13736f91db6b885b481b657dda5fde41a4e2de07e0` |
| `verify_bol_conductor_vector.py` | `b1e4eaf64236ab454fd3fe83481574f55a6512f33c4b7c08065dd05b3bf4ad7e` | `833f9b5644966856f150d273306db47643021cbeaf3101cc5972ca62da38324f` |
| `verify_bol_conductor_independent.py` | `fc12b58d2bf205e137603cccfd7cd44de0ec4edd0cc93938e15a772165ea83ce` | `031c6fd40bda49d1d8a1d6aa2c630616c97bf21b840a82245c548ff75b258fd5` |

The exact conductor manuscript SHA-256 is `c1aae8551d970a27caefcd53c324cf7a0ffaee2e5e1a80450b49817b09d6c2c6`. The imported, unchanged authored field dependency has SHA-256 `7899f013a8229ecfeb6c6ab518c24f11e7155e942e9724856440eb804c5b144e`. The extraction record is `conductor-pinned-hashes.json`; each replay has `conductor-replay-*.run.json`, `.stdout` and `.stderr` records in the reviewer scratch evidence.

The reviewer independently ran `git diff --check` between the predecessor delivery and the scientific pin; it passed. Repository integration and hosted CI are separate. The coordinator reports that a separately prepared merged checkout passed 115 integrity tests against main revision `4ded8c4fb264235370a745100755a26a372918ba`, with only two navigation files changed by that integration. Those are coordinator checks, not reviewer runs. The coordinator observed scientific-source workflow `43870112685`, event `pull_request_target`, completed with conclusion **skipped**, not passed. Actual-host rendered Markdown inspection remains unverified. This report binds the scientific pin above; a later integration/provenance commit must preserve its mathematical source bytes.

**Signed:** ChatGPT, GPT-6 Astra Pro, `/root/independent_review`, 2026-11-16. Acceptance binds to scientific source `f85696062308e2b2511af8c73744766ec62a9dc8`, tree `bc8c3ba096ae14213c5bc991715ec12740edc0dd`, and the scientific hashes above.


## Coordinator's conductor-checkpoint delivery record

This section is by ChatGPT /root. The independent conductor report immediately
above is reproduced verbatim; its original SHA-256 is
`a9d8fa8a96eca27d119e2d54e9a293b09b31cce9c0ec205acbf4390a2e85dafb`.
The exact scientific pin is
`f85696062308e2b2511af8c73744766ec62a9dc8`, tree
`bc8c3ba096ae14213c5bc991715ec12740edc0dd`.

The coordinator read and ran both authored conductor programs and the standalone
independent program. All exited zero with empty stderr and reproduced the source
and complete-stdout hashes in the signed table. The runtime was Python 3.12.14,
with NumPy 2.3.5 for the central integer arrays. The
[code guide](../code/README.md#arithmetic-conductor-correspondences) gives the
commands, seeds, finite ranges and shared-implementation distinction. Full raw
logs and extraction manifests remain outside Git; the reproducible sources and
this concise evidence record are versioned.

The proof was coordinated by /root with construction/proof support from
/root/bol_operator_attack, /root/quasi_rh_bridge and /root/weil_literature.
Those contributions are not independent review. The noncontributing mathematical
reviewer and reviewer-authored checker are identified in the signed report.
/root/repo_integrity separately prepared and checked the navigation integration.
No permanent claim IDs were allocated or changed.

Current main `4ded8c4fb264235370a745100755a26a372918ba` changes only the
research index and this problem's README relative to the original integration
base. The additive resolution retains main's classification routing verbatim
and the complete analytic routing. In an isolated merged checkout, the integrity
agent confirmed that all other 5,671 tracked entries matched the arithmetic
scientific pin and ran
`python check.py --base 4ded8c4fb264235370a745100755a26a372918ba` successfully,
with all 115 tests passing. These repository checks are separate from the
mathematical verdict. The final delivery appends review evidence and updates
status; its conductor manuscript and all three conductor verifiers remain
byte-identical to the accepted source. The preceding scalar and collective
scientific files and signed reports are also preserved.

After adding the signed report and final status, the coordinator reran the same
integrity command successfully: 115 tests passed. The changed analytic documents
and modified index row have 60 checked relative links and 12 checked heading or
explicit anchors. `git diff --check` also passed. These are source checks, not
an assertion of successful hosted-page visual inspection.

The new bounded obligation is complete within the stated hypotheses: (20)
supplies all-level filtered correspondence, while (30)--(31), (38), (46) and
(49) supply lossless stable transport, exact full norms, a bounded normalized
limit and arithmetic discrepancy. The next representation-level attack is an
enlarged output model retaining primitive representations while supporting the
central translations or section operators. The present small-span obstruction
specifies why quotient-equivariant lossless contraction cannot supply that model.
No local metaplectic identification or global automorphic consequence is included.

[PR #440](https://github.com/Mira-Cult/math-wip/pull/440) records the full final
delivery head and current remote CI state. The scientific-source workflow
[43870112685](https://github.com/Mira-Cult/math-wip/actions/runs/43870112685)
completed **skipped**, not passed. Actual hosted-page visual inspection remains
unverified after the earlier logged-out browser returned 404 for this private
repository. Authorized connector retrieval and exact Git-tree matching confirm
source publication. No CI gate, repository permission or runner setting was
changed. No PR merge or formal GitHub approval was performed.


## Coordinator's intrinsic-associator source checkpoint

This section records authored research and finite replay by ChatGPT `/root`,
2026-11-16. It is not the independent mathematical verdict. The continuation
starts from delivery `76d987909254eabf93073648818838fc09fb32b7`, tree
`c90df3928cb74472e96f770caa7bfa62c8bcee8a`, with main
`4ded8c4fb264235370a745100755a26a372918ba` already incorporated.
The prior scalar, collective and conductor scientific files and signed
reports are preserved. No permanent claim IDs are allocated or changed.

The canonical proof is
[Associator quantization and intrinsic mixing](../manuscripts/bol-associator-quantization.md).
The bounded obligation is an actual-translation construction natural under
loop isomorphisms, retaining non-scalar correction operators, with a proved
intrinsic spectral or energy consequence. The complete inner-defect spectrum
has exact norm p^(-2) off its fixed space; conjugating by actual translations
has exact global norm 1/p+(1-1/p)Q^(-r_min). The written proof includes the
right nucleus, all conductor/rank exceptions, genuine isomorphism transport,
Weyl corrections, the no-group-image obstruction, general reassociation and
the additional Bol inverse-defect law. Positivity is proved for this family;
only reversibility is asserted for every finite left Bol loop.

The root coordinated construction with `/root/associator_operators` and
`/root/associator_theory_routes`; those agents are coauthors, not independent
reviewers. `/root/associator_independent_review` did not contribute construction
or proof. That reviewer independently tested formulas and supplied the three
standalone checks listed below. Its final mathematical verdict is to be
recorded separately against the published scientific commit.

Root read and replayed all five programs with assertions enabled, Python
3.12.14, and NumPy 2.3.5 only for the direct independent ring arrays. Each
exited zero with empty stderr. The authored Weyl checker imports the earlier
authored conductor/field implementation; the bilinear checker and all three
reviewer-authored programs import no other checker. The independent sources
were frozen before canonical copying and retain their original bytes.

| Program | Source SHA-256 | Complete stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_associator_bilinear.py` | `50c15561521761c67c4b7f9ab6d2269e0ec7caded1c38cfb1b74acf028c1f0d9` | `e385ca21eb7cae54e641634ece4c9ba902bf4562cd6c022d64923d35609c131d` |
| `verify_bol_associator_weyl.py` | `c59a03f6804f1d57217d29d282d5d5bad7484e531dcd5466fc837a41ae9c943c` | `788f202579077fd6e7844d396b3cda2245589ef1585943b87e1bd86b983f8946` |
| `verify_bol_associator_independent.py` | `116e4a3f41c75c990e6e5e11b7a6ff8933ac2ec576b205ae1be85ca09fe655af` | `fdc1589996da9bf47e4bd35a004e520718bd25286ca2e1cea9f80f9033a0a11e` |
| `verify_bol_associator_ring_independent.py` | `93726c49ac0bce9b82141cbe0bbb6a7386740c022def94b84c7f5fc7b6d2760e` | `caa0e450a19a5bb7b71b84db642d15d28ebc03b60f789a5bec6e0bba756fd3d8` |
| `verify_nonbol_reversibility_control.py` | `dbb26b41adb855f87eb97169407282cd893e97c0a832db39829a383244d37afe` | `648e762dac7b17cdd03dd65b93ed6c9fdb5dc8f71eb42063794dac3c153e6f05` |

The [code guide](../code/README.md#intrinsic-associator-quantization-and-mixing)
gives commands, exact ranges, seeds and implementation dependencies. Evidence
includes 6561 exhaustive field bilinear sums, 290 ring-plane averages,
96 authored permutation and 480 basis/character samples, 128 independent
actual-loop samples, 415065672 directly enumerated ring-character terms,
and all 125 compositions of an explicit non-Bol control. These checks do
not enumerate a full large loop matrix or prove the uniform theorem by
extrapolation. Raw logs remain outside Git.

The full spectrum of the inner-defect operator retains joint-image tests.
The two sharp worst-case norm formulas do not provide a further
collective-pencil separation. The repaired global operator's nonzero
right-nucleus-character blocks have sufficient bounds, not a complete
spectral evaluation. Uniform left-translation averaging already samples
uniformly for every finite loop; the new endpoint is the constrained
associator spectrum and sharp multiplicativity-defect coercivity, not a
faster unrestricted sampler. Existing quasigroup representation, Markov
and Weyl theories are acknowledged. Higher categorical quantization and
an action-equivariant enlargement of the earlier conductor readout remain
open; no historical priority, local cover, automorphy or quasi-RH result is
claimed.


## Independent mathematical review of the intrinsic associator continuation

Reviewer: **ChatGPT, GPT-6 Astra Pro, agent
`/root/associator_independent_review`**. Date: 2026-11-16.

**Verdict: accepted within the stated hypotheses and scope.** I found no
blocking mathematical error in Theorems A and B, their energy consequences,
the actual-isomorphism and correction identities, or the associative-target
obstruction in the scientific source below. No mathematical change is
requested at this pin. This is an independent agent's conventional
mathematical review, not formal verification, a journal referee report, or
certification of historical priority.

### Exact source and reviewer role

The reviewed scientific commit is
`5771bfccb6707606078baf93be804f810276b8eb`, with Git tree
`aa6893c2cc8c55ea59e69d285cfff837cbdbcb21` and parent
`76d987909254eabf93073648818838fc09fb32b7`.
The canonical manuscript is
[bol-associator-quantization.md](../manuscripts/bol-associator-quantization.md),
whose SHA-256 is
`20d5ae96b5b4228282679cb892ee367034a7873c5c2d79d62567ac7bddbf3ff1`.
I verified the commit's tree and extracted the thirteen changed files
directly with `git show` into an isolated review directory. I read the
entire canonical manuscript, the five new programs, the relevant unchanged
runtime dependencies, and all changed scientific, bibliographic, routing
and evidence text. I reviewed the changed index and prior-report material
as diffs; this does not assert a fresh review of every older repository
claim or every line of the historical report.

I was assigned as a noncontributing reviewer before the final construction.
The root, `/root/associator_operators`, and
`/root/associator_theory_routes` constructed the operators and proofs and
are coauthors for this review purpose. I did not originate their proposed
spectral theorem, global repair, or proofs. My work was hostile checking of
supplied candidates, scope and convention checks, independent verification
programs, and the order-five negative control. The three reviewer-authored
programs were frozen before canonical copying; their committed bytes match
the frozen sources. I made no canonical source edit, publication, merge,
or formal GitHub approval.

### Mathematical obligations checked

1. **Actual loop and section.** Section 2.1 recovers the displayed law from
   the reciprocal stabilizer graph and section. Both division formulas,
   the two-sided inverse, and the direct Bol calculation are correct.
   The flexibility witness proves non-Moufangness at every stated ring
   level. These checks use the explicit balancedness and alternating
   identities; they do not require the public source's conditional
   simplicity or classification conclusions. The concrete infinite family
   in Section 1.2 satisfies the admissibility conditions and has the stated
   cardinality.

2. **Defects, invariant spaces and character exceptions.** Equations
   (AQ.12)--(AQ.15) have the correct composition order and signs. The
   shears and bimap values generate exactly the asserted defect group.
   Its orbit description accounts for the entire fixed vector axis.
   The intrinsic right nucleus is correctly distinguished from the loop
   center. The scalar radical and its density in (AQ.16) include the zero
   pencil parameter, degenerate nonzero parameters, the zero ring character
   and every imprimitive conductor. In particular, common-radical zero is
   not being substituted for nondegeneracy of every scalar specialization.

3. **Representation interfaces and naturality.** I checked (AQ.17)--(AQ.23)
   directly with the stated pushforward convention and normalized point
   vectors. The Weyl half-phase vanishes for the stated reason; the full
   correction is modulation followed by the displayed dilation, in the
   specified order. The construction uses the doubled finite abelian phase
   space and does not assume that the reciprocal action preserves the
   scalar bicharacter. The nucleus-character transport and intertwiner
   (AQ.18) hold for an actual loop isomorphism without assuming that its
   coordinate permutation is additive. A nonlinear change of coset
   representatives is correctly treated as a basis gauge, and no isotopy
   invariance is claimed.

4. **Associative-target obstruction.** Proposition 4.1 is valid at every
   stated prime-power level. Associativity in the target identifies the
   two displayed words and kills the pure field vectors using
   invertibility of `lambda^(-1)-1`. Pencil independence then kills the
   p-part of the nucleus; the unit `eta-1` kills each ring plane, and
   the determinant values kill the remaining nucleus. The scalar-projective
   corollary follows by passing to the projective unitary group. The
   unital associative quotient of the complex loop algebra is indeed the
   augmentation copy of C, because the basis elements have two-sided
   inverses. These statements do not rule out Beck modules, nonabelian
   corrections or category-valued constructions.

5. **Reassociation versus Bol input.** Equation (AQ.24) is the correct
   nonabelian transport identity. Its telescoping and pentagon consequence
   are properly identified as formal for arbitrary loops. The additional
   Bol identity (AQ.25), together with the bijection of parameter pairs,
   really proves inversion symmetry of the uniform defect distribution.
   Thus self-adjointness is valid for every finite left Bol loop; positivity
   is proved only for the explicit reciprocal family. The order-five
   control is Latin with an identity and has the stated nonsymmetric
   defect counts and 57 Bol failures. It disproves generic-loop
   reversibility, without asserting that reversibility characterizes Bol
   loops.

6. **Complete spectrum of the intrinsic operator.** The alternating
   bilinear identity (AQ.31) is correct, including the incompatible-image
   and zero-matrix cases. In the ring calculation, the two linear
   coefficients are zero or units; compatible covectors have zero residual
   phase, while incompatible covectors force both coefficients to vanish.
   The conductor factor and the extra `p^(-2)` factor per bad plane are
   therefore correct. The factors are constant on each scalar orbit, and
   the allowed orbit characters in (AQ.27) account for the orbit
   stabilizers even at nonprimitive ring vectors. The resulting blocks
   exhaust the regular Hilbert space. Theorem B gives the complete
   spectrum of A, with exactly the claimed eigenvalue-one spaces. The
   even-rank bound and the explicit one-plane mode prove the sharp
   `p^(-2)` norm off P, its power formula and the sharp local energy
   coefficient. The P-fixed space is not incorrectly called a
   translation-invariant multiplicative subrepresentation.

7. **Exact global norm and coercivity.** I checked the support, phase and
   normalized mass of the auxiliary kernel (AQ.34). Conjugation moves the
   radical to an affine coset; every surviving displacement is in that
   radical, so the two translation phases cancel. Its row mass is exactly
   the radical density. The resulting positive-operator inequality bounds
   every nonzero nucleus-character block of M strictly below `1/p`.
   The trivial-character Fourier multipliers are exactly (AQ.37)--(AQ.38).
   Joint zero events are bounded by each single-coordinate event, and a
   single frequency plane of minimum rank attains (AQ.39). The gamma-zero
   probability is strictly below `1/p`, with all conductors included.
   This proves the exact global norm
   `Lambda = 1/p + (1-1/p) Q^(-r_min)`, its powers, the correlation and
   total-variation consequences, and the sharp lower coefficient in the
   globally translated energy inequality. The proof correctly bounds,
   rather than completely diagonalizes, the nonzero-character blocks of M.

8. **Controlled attribution.** For an associative group the defects and
   their conjugates are identity, so the global norm is one. Erasing
   either reciprocal action preserves the Bol law but makes every function
   of that vector coordinate invariant under each conjugated defect;
   the ablated global norm is again exactly one. The manuscript explicitly
   places these ablations outside the full faithful-action hypotheses.
   It also correctly states that uniform left-translation averaging already
   gives the constant projection for every finite loop. The new result is
   therefore a sharp theorem about the specified associator measure and
   multiplicativity-defect coercivity, not a faster unrestricted sampler.

### Exact-source computational replay

After reading their source, I ran all five programs from the extracted
scientific commit with assertions enabled. The runtime was Python
**3.12.14** (`Clang 22.1.3`) on Linux x86-64; the independent ring program
used **NumPy 2.3.5** only for exact integer arrays. The other four use the
standard library. The commands, from the extracted repository root, were:

```bash
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_bilinear.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_weyl.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_independent.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_associator_ring_independent.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_nonbol_reversibility_control.py
```

Every command exited zero and produced empty stderr. The complete stdout
hashes reproduced the coordinator's record exactly:

| Program | Source SHA-256 | Complete stdout SHA-256 |
| --- | --- | --- |
| `verify_bol_associator_bilinear.py` | `50c15561521761c67c4b7f9ab6d2269e0ec7caded1c38cfb1b74acf028c1f0d9` | `e385ca21eb7cae54e641634ece4c9ba902bf4562cd6c022d64923d35609c131d` |
| `verify_bol_associator_weyl.py` | `c59a03f6804f1d57217d29d282d5d5bad7484e531dcd5466fc837a41ae9c943c` | `788f202579077fd6e7844d396b3cda2245589ef1585943b87e1bd86b983f8946` |
| `verify_bol_associator_independent.py` | `116e4a3f41c75c990e6e5e11b7a6ff8933ac2ec576b205ae1be85ca09fe655af` | `fdc1589996da9bf47e4bd35a004e520718bd25286ca2e1cea9f80f9033a0a11e` |
| `verify_bol_associator_ring_independent.py` | `93726c49ac0bce9b82141cbe0bbb6a7386740c022def94b84c7f5fc7b6d2760e` | `caa0e450a19a5bb7b71b84db642d15d28ebc03b60f789a5bec6e0bba756fd3d8` |
| `verify_nonbol_reversibility_control.py` | `dbb26b41adb855f87eb97169407282cd893e97c0a832db39829a383244d37afe` | `648e762dac7b17cdd03dd65b93ed6c9fdb5dc8f71eb42063794dac3c153e6f05` |

The empty stderr SHA-256 for each run is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The authored Weyl program's two imported dependencies were also extracted
from the same commit:

| Dependency | SHA-256 |
| --- | --- |
| `verify_bol_conductor_vector.py` | `b1e4eaf64236ab454fd3fe83481574f55a6512f33c4b7c08065dd05b3bf4ad7e` |
| `verify_bol_collective.py` | `7899f013a8229ecfeb6c6ab518c24f11e7155e942e9724856440eb804c5b144e` |

The authored runs remain authored-implementation evidence after my replay.
The three reviewer programs import no authored checker. The independent
field program checks 96 actual-loop samples at level 7 and 32 at level 49,
with seed `2026111609`; it tests phases before character evaluation.
The independent ring program directly enumerates all vector pairs and all
nine actor-coordinate pairs in eight selected cases, totaling 415065672
exact character terms. Its integer ranges do not overflow the chosen
arrays, and cyclotomic reduction is exact. The non-Bol control enumerates
all 125 point compositions. The authored bilinear and Weyl scopes are
accurately described in the code guide. None of these finite checks is a
full enumeration of a large reciprocal-loop matrix or a proof of the
all-parameter theorems by numerical extrapolation.

### Provenance, literature and limitations

The prior review record's entire 64331-byte content is an exact prefix of
the record at the reviewed commit. Its SHA-256 is
`d54ec50023839e1d4981408ed80f117bf2ddad1fe0e5459d63c5fe322e895943`.
The collective and conductor manuscripts and the two runtime dependencies
above are unchanged from the parent scientific delivery. The new review
does not replace or enlarge the earlier signed verdicts.

The primary-source comparisons are appropriately limited. I inspected
Smith's *Four Lectures on Quasigroup Representations* at the cited
representation/Markov interfaces; Smith's 1999 paper is used only at its
stated first-page interface. I checked Johnson--Smith, *Matched pairs,
permutation representations, and the Bol property*, Theorem 6.1 and
Section 7, directly in the author PDF. I also checked Bunk--Müller--Szabo
arXiv:1804.08953v2, Definitions 4.12 and 4.16 and Theorem 5.7, and the
stated categorical-versus-matrix distinction, together with the cited
Bakas--Lüst alternative at arXiv:1309.3172v3. The new finite spectral proof
does not invoke their higher constructions. The prior Gurevich--Hadani
and quasi-RH intake remains separately scoped; this review does not certify
the quasi-RH paper's global conclusion or an exhaustive literature search.

The complete A spectrum retains joint-image tests. Its extremal norm and
the exact M norm do not prove a new worst-case saving from all joint-rank
strata. Similarly, validity at every conductor is not a new intertwining
theorem between levels. The earlier readout correspondence is preserved;
extending it to a larger output model carrying the actual section and all
correction operators remains a stronger open task. A categorical
quantization with additional analytic control is also open. The scalar
group-image obstruction, graph-twirl reduction, and older conditional
transport obstructions do not exhaust those alternatives.

No new local metaplectic cover, global theta construction, Euler product,
automorphy, classification result or historical-priority claim is accepted
by this verdict. The accepted payoff is the stated intrinsic finite-loop
spectral and energy theorem, with an explicit infinite family and uniform
constants. This is materially stronger than merely attaching Weyl matrices
to the loop, while its ambient Weyl and permutation machinery remains
established theory.

Repository integrity and remote CI are separate from this mathematical
review and replay. I do not reattribute coordinator checks to myself, and
I certify no remote CI pass. In particular, the coordinator's observed
skipped `pull_request_target` workflow is not a successful CI run. Raw
review logs remain outside Git; the source and complete-output hashes
above identify the actual replay.

Signed: **ChatGPT, GPT-6 Astra Pro,
`/root/associator_independent_review`, 2026-11-16**.


## Coordinator's intrinsic-associator delivery record

This section is by ChatGPT `/root`. The independent report immediately
above is reproduced verbatim; its SHA-256 is
`e53964158cb26cdae7d492591d9a62b199d41ee6f3aafa1d4d464f1ff1038dc2`.
Its acceptance binds scientific source
`5771bfccb6707606078baf93be804f810276b8eb`, tree
`aa6893c2cc8c55ea59e69d285cfff837cbdbcb21`. The manuscript SHA-256 is
`20d5ae96b5b4228282679cb892ee367034a7873c5c2d79d62567ac7bddbf3ff1`.
The delivery changes review evidence and status only. The accepted manuscript
and all five new programs are byte-identical to that pin; previously tracked
scientific manuscripts and programs also remain unchanged. No new permanent
claim IDs are allocated.

After appending the signed verdict and updating status, the coordinator ran
`python check.py --base 4ded8c4fb264235370a745100755a26a372918ba` successfully:
115 tests passed. These are repository-integrity tests, separate from the
mathematical review and research replay. The five research programs had
already reproduced all frozen source and complete-output hashes, and the
independent reviewer replayed the exact Git extraction separately.

A coauthor source check resolved 73 relative links and 16 heading/explicit
anchors across the changed analytic documents, manuscript and affected index
row. In the mathematical manuscript, that check preceded only the final
action-erasure paragraph, which introduces no links. The subsequent status
and signed-report links point to existing local files and were checked by
root. Root rechecked the entire final manuscript's 71 display formulas,
460 protected inline formulas and 41 sequential equation tags for balanced
braces, environments and delimiters. This is a static source check. The
available local TeX executable lacked its format file, so it did not render
the mathematics; no successful rendering is inferred. Actual hosted-page
visual inspection remains unverified after the earlier logged-out browser
returned 404 for this private repository. Authorized connector publication
and exact remote/local Git-tree equality verify the delivered source.

The original source and new delivery remain additive commits on the owned
PR. Main remained `4ded8c4fb264235370a745100755a26a372918ba` at publication.
The scientific-source Actions run
[43879873549](https://github.com/Mira-Cult/math-wip/actions/runs/43879873549),
event `pull_request_target`, completed **skipped**, not passed. The PR body
records the full delivery head and its own observed CI state. No CI gate,
runner setting or repository permission was changed. No merge or formal
GitHub approval was performed.

The bounded intrinsic-operator obligation is complete under the stated
hypotheses: actual corrections and isomorphism transport, a full intrinsic
spectrum, a sharp global norm and quantitative multiplicativity-defect
coercivity have independent exact-source acceptance. The full joint-image
geometry remains present in the spectrum but does not improve these
worst-case norms. The next analytic test must use a finer intrinsic observable
or a genuinely collective compression. A category-valued construction and
an enlarged arithmetic model carrying the actual section/correction actions
remain separate open targets. The already accepted conductor readout
correspondences retain their own scope and are not reclassified as missing.


## Coordinator's intrinsic spectral separation source checkpoint

This continuation is by ChatGPT `/root`, session `cb2507a57d10`, with
contributing agents `/root/incidence_derivation` and
`/root/literature_analytic`, commissioned by Mira on 2026-11-16. The
noncontributing mathematical reviewer is `/root/independent_spectral_review`.
This paragraph records preparation, not a verdict on an as-yet-unpublished
revision; the exact-source signed verdict will follow separately.

The recovered PR head is `f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`.
GitHub comparison to `5771bfccb6707606078baf93be804f810276b8eb` shows one
subsequent status/review commit affecting only BOL_METAPLECTIC.md,
PROBLEM.md and this evidence file. Both scientific manuscripts are unchanged.
The new canonical proof is
[Intrinsic spectral separation](../manuscripts/bol-intrinsic-spectral-separation.md).
No permanent claim IDs or classification interfaces are changed. Its obligation
is exact separation of the unmarked spread/aligned loops with identical
labeled scalar ranks, followed by an intrinsic collective estimate.

The written proof establishes all-h nonisomorphism, exact positive-moment
and return-probability differences, the full compressed spectral multiset,
a canonical large spectral subspace, two limiting laws, and the fixed
quadratic collective RMS ratio asymptotic to 27·3^(−h). The input normalization
and fixed-space exceptions are explicit. Its result does not improve either
previously sharp worst-case norm. The quadratic is applied after an intrinsic,
h-dependent cutoff and scale, and is a signed observable, not a claimed
bounded-length Markov sampler. The higher moments of unfiltered M remain open.

### Frozen executable evidence

The coordinator read both new programs and ran them with Python 3.12.14.
Both exited zero with empty stderr. The new programs use only the standard
library; the frozen independent source was copied byte for byte from the
reviewer's separately authored scratch program. The coordinator's complete
output hashes match the contributors' frozen runs.

| Source | Source SHA-256 | Complete stdout SHA-256 |
|---|---|---|
| `verify_bol_intrinsic_spectrum.py` | `4e6d31b9244f5a662b4da7521f56cbff20f06c60d7868935c276d499f87d4b8a` | `9fd56f9a82d3a80dfd6282f6278f5a92c71058a7b3199f342ff90e7782b10b3a` |
| `verify_bol_intrinsic_incidence_independent.py` | `944bf3286604edd85da5e8b771e08bd2e48e47884171b5fcaab4cd8b6d66414b` | `451b97df7c5bdb3c7d0e676878dbecc9a5a004b298aab7cc900e96f3950c476c` |

The manuscript SHA-256 is
`fb801468b532b2096587e957ecff5891ad79bb90d9d5e1ef462133eabf7626d6`.
The exact rational record digest of the authored checker is
`7f3c947d438cc1cec24c8c1847172c6413e874e5b77d666219b9ced1b9fcdfa9`.
The [code guide](../code/README.md#intrinsic-spectral-separation) owns commands
and finite ranges. The independent h=1 calculation uses all 729 ordered
parameter pairs per family and 181440 orbit-label contributions per family.
It gives trace difference `6207245000998912/22235661` on the common regular
dimension `3337453428382706771853981`. Finite checks support the written
proof, rather than enumerate full loop tables or establish a universal
claim by extrapolation. The independent final reviewer also checked the
quadratic energy against the matrix-derived h=1 spectrum in a separate
scratch execution; its formal verdict will state the exact scope reviewed.

### Repository and publication limits

The authorized GitHub connection supplied the exact source blobs and recursive
Git tree. Direct Git cloning had no authenticated credential in this runtime,
so an isolated sparse checkout was reconstructed with exact Git object hashes;
no other worker's checkout was used. The complete remote tree is preserved
when publishing changed paths. The earlier scientific files and signed reviews
are retained unchanged.

`git diff --check` passed. A static check resolved 77 local navigation links
in the affected sources against the complete Git tree inventory, and checked
35 unique sequential equation tags plus math delimiters and braces. These
are source checks, not hosted mathematical rendering.

The required `python check.py` was attempted. It cannot certify this sparse
checkout: repository-wide index targets and some unchanged dependencies are
not materialized. It exited nonzero (99 discovered tool tests, one failure
and one import error caused by unavailable repository content), separately
from the passing new mathematical programs. No full-repository integrity
pass or remote CI pass is claimed. Successful repository-wide validation
remains an integration requirement; no CI gate, permission or runner setting
has been changed. No merge or formal GitHub approval is performed here.


## Independent mathematical review of intrinsic spectral separation

Reviewer: **ChatGPT, GPT-6 Astra Pro, agent
`/root/independent_spectral_review`**. Date: 2026-11-16.

**Verdict: accepted within the stated hypotheses and scope.** I found no
blocking mathematical error in Theorems 1, 3, 4, and 5, Lemma 2, the limiting
spectral laws, or the stated passage from the coordinate calculation to
unmarked loop invariants. No mathematical change is requested at the source
pin below. This is independent conventional mathematical model review, not
formal verification, human acceptance, or a literature-wide priority claim.

### Exact source, extraction, and reviewer role

The reviewed scientific commit is
`bb49ab24465ef82be78f2a0d9cb8d0af8caa2695`, with Git tree
`1751336a4275ffbb8f92025e2e3d4e4907aa5c21` and parent
`f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`.
The canonical manuscript is
[bol-intrinsic-spectral-separation.md](../manuscripts/bol-intrinsic-spectral-separation.md),
whose SHA-256 is
`fb801468b532b2096587e957ecff5891ad79bb90d9d5e1ef462133eabf7626d6`.

I verified the local commit and tree, extracted all nine changed files with
`git show` into a separate review directory, and read the entire new
manuscript, both final programs, and all changed documentation, bibliography,
and evidence text. I reviewed the latter as diffs; this does not assert a
fresh review of every earlier historical report. I also extracted the two
unchanged mathematical dependencies and checked the relevant construction,
action convention, trace-dual, character-sector, and AQ.27--AQ.30 interfaces.
The complete prior all-conductor theorem remains a separately reviewed
dependency, not a theorem re-proved by the finite checks here.

The root and the agents `/root/incidence_derivation` and
`/root/literature_analytic` supplied the proposed construction, formulas,
proofs, and strengthening. I was assigned as the noncontributing reviewer.
My work was hostile checking of those candidates, independent implementation
of the h=1 incidence/orbit calculation, and final exact-source replay. I did
not originate the claimed separation or analytic theorems, edit the canonical
proof, publish source, merge a PR, or issue a formal GitHub approval.

### Mathematical findings

1. **The incidence is the one occurring in AQ.29.** The condition is
   membership of `B_nu w` in the full E-linear image of `B_alpha`, with
   `w` in the entire E-space of dimension 6h. The perfect trace pairing
   identifies this image with the appropriate annihilator. In the spread
   construction, the equation in the trace-dual coordinates must hold in
   `L_h`, since the whole radical line must be annihilated. Nondegeneracy
   of the trace pairing does not require the trace of 1 to be nonzero.
   I checked that the argument remains valid when 3 divides an extension
   degree and does not replace an E-dimension by an absolute dimension.

2. **The two intersection dimensions and exceptional cases are correct.**
   Nonzero independent prime-field parameters give distinct spread radical
   lines, because equality forces the ratio to equal its cube, hence to
   lie in `F3^*`. The two copies contribute 2h intersection dimensions.
   For the aligned construction, prime-field vectors proportional over E
   are already proportional over F3. The star images intersect in one
   E-line, and the nonsingular block contributes 4h-2 more dimensions.
   This gives 4h-1. The inverse-image count in IS.10 then gives
   `Q^(4h)` and `Q^(6h-1)`. The zero-parameter and proportional cases in
   the displayed table are exhaustive. Both families retain the same
   labeled scalar ranks and zero common radical for all allowed injections.

3. **Orbit and character multiplicities are complete.** Every nonzero W
   scalar orbit has seven points. Each active F7^2 plane has sixteen
   nonzero three-cycles. For a support of size j there are exactly `3^j`
   allowed alpha labels, while sigma has seven choices only when W is
   nonzero. The separate singleton W=0 orbit explains all the `-1`
   corrections in IS.12. The ring factors and multiplicities are
   `1` with multiplicity 1, `9^(-j)` with multiplicity 6, and
   `49^(-k)` with multiplicity 42 in the nonzero-W case. In particular,
   the last exponent is k, not the active support size. The table sums
   to the full regular dimension `7ST49^k`, not just a selected set of
   character sectors. Eigenvalue one has precisely the common multiplicity
   `(S+a_0)(17^k+6)`, including constants, the fixed vector axis,
   radicals, and zero characters.

4. **The trace separation survives the full aggregation.** Increasing the
   compatible-vector count changes `a_1` by the positive integer delta
   in IS.16 and decreases `b_1` by the same amount. The available
   multiplicities permit every asserted upward transfer. Numerical
   collisions among eigenvalues do not invalidate this coupling. Summing
   its positive t-th moment difference gives IS.3 for every real t>0,
   including the exact specialization IS.4. All transferred eigenvalues
   lie below one, so subtracting the common intrinsic fixed projection
   preserves these differences. This is spectral ordering, not an
   unproved operator inequality between arbitrarily identified spaces.

5. **The nonisomorphism statement concerns the actual unmarked loops.**
   An arbitrary loop isomorphism conjugates all actual left translations,
   hence the full defects, their generated group, A, M, and P. The proof
   does not assume that the induced coordinate map is additive or that it
   preserves a pencil chart. The fixed-point trace identity gives exactly
   the probability of an associative triple after division by the loop
   order. The A-power traces give averaged return probabilities, with the
   same stationary limit in both families. For M, right division makes
   its diagonal constant, so the first trace separates its one-step
   return probability at every point. The manuscript correctly makes no
   deduction about higher moments of M from this identity.

6. **The spectral cutoff and the power estimate are intrinsic.** The
   inequality `Q^(-4h)<49^(-k-1)` separates all alpha-nonzero modes from
   all alpha-zero modes. The projection in IS.22 is therefore genuinely
   spectral, while h itself is recoverable from the loop order. Its rank,
   top multiplicity, and the singleton correction `6S` in IS.24 are
   correct. The normalized top multiplicity is asymptotic to
   `1/(49*9^h)` for spread and tends to `1/(49Q)` for aligned. All
   other scaled eigenvalues are at most 1/9. This proves the power
   mean-square bounds and the ratio asymptotic to `27*3^(-h)`.

7. **The fixed quadratic strengthening is valid.** The polynomial
   `(49x^2-x)/48` preserves 1, kills both 0 and 1/49, and has absolute
   value at most x on [0,1]. The rho-nonzero, sigma-zero contribution
   has normalized mass factor `6(T+6)/(49T)`; summing its squared
   ceiling yields exactly `b_k` in IS.31. The nonzero-sigma mass is
   `(6/7)(1-1/T)`. These give the explicit error in IS.31, which is
   negligible relative to `9^(-h)`, and hence IS.32. The comparison is
   a full-basis or independent-sign RMS statement on the whole regular
   Hilbert space, with the specified filter zero on its complement.
   Both worst-case norms remain one. The text correctly identifies the
   observable as signed and the cutoff as h-dependent; it does not claim
   a fixed-length Markov sampler, a fixed-degree polynomial of A before
   the cutoff, or a small bound for every individual unit input.

8. **The limiting laws and remaining question have the stated scope.**
   The rho=sigma=0 band has limiting mass 1/49, split according to the
   top multiplicity. The other bands tend to zero; for the rho-nonzero
   band this follows from the displayed support-count estimate. The two
   limiting measures in IS.34 have total mass one and the stated atoms.
   The unscaled spectra both tending to a point mass at zero is consistent
   with these rescaled limits. The unfiltered translated-defect second
   centered moment and higher return profile remain separate questions.

### Exact-source replay and independent finite evidence

From the Git extraction I ran, under Python 3.12.14:

```text
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_intrinsic_spectrum.py
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_intrinsic_incidence_independent.py
```

Both exited zero with empty stderr. The source and complete stdout hashes
reproduced the coordinator's frozen record exactly:

| Program | Source SHA-256 | Complete stdout SHA-256 |
|---|---|---|
| `verify_bol_intrinsic_spectrum.py` | `4e6d31b9244f5a662b4da7521f56cbff20f06c60d7868935c276d499f87d4b8a` | `9fd56f9a82d3a80dfd6282f6278f5a92c71058a7b3199f342ff90e7782b10b3a` |
| `verify_bol_intrinsic_incidence_independent.py` | `944bf3286604edd85da5e8b771e08bd2e48e47884171b5fcaab4cd8b6d66414b` | `451b97df7c5bdb3c7d0e676878dbecc9a5a004b298aab7cc900e96f3950c476c` |

The authored program checked the exact compressed multiset for h=1,2,3,4,
moments 1 through 4, fixed spaces, cutoff, both collective estimates, and
the h=8 asymptotic illustration. Its rational record digest was
`7f3c947d438cc1cec24c8c1847172c6413e874e5b77d666219b9ced1b9fcdfa9`.

My independent program, copied into this commit without alteration,
constructs the h=1 pencils using separate standard-library field arithmetic.
It checks all 729 ordered parameter pairs per family, then aggregates
181440 allowed-label contributions per family using the matrix-derived
incidence counts rather than assuming the proposed intersection table.
The intersection histograms are `{0:53,2:624,4:52}` and
`{0:53,3:624,4:52}`. Its absolute trace pairing has rank six although
`Tr(1)=0`. It checks actual order-seven scalar and order-three plane
orbits, total and per-nucleus-sector dimensions, P, the low band and its
top multiplicities, and the first four moment differences. The independent
finite-loop control checks arbitrary relabeling and the fixed-point/
associative-triple identity, including a non-Bol order-five loop and an
associative cyclic-group control.

At h=1, the common dimension is `3337453428382706771853981`, the common
P-rank is `105473644441986798333`, and the exact trace difference is
`6207245000998912/22235661`. I separately evaluated the quadratic
observable on the independently matrix-derived h=1 spectrum and verified
its exact lower and upper energy bounds and norm one. The complete
programs take the prior AQ.29 formula as mathematical input; they do not
enumerate enormous loop tables or replace the written uniform proofs.

### Literature, preservation, and limitations

I checked the new comparison interfaces directly in the primary sources:
Kepka's Section 1 and Theorem 5.5 concern associative-triple counts in
commutative Moufang loops; Levin's pinned arXiv v1 states the nuclear-
commutator hypothesis for its Moufang bound and separately treats
conjugacy-closed loops; Evans's report Section 1 gives the fixed-point
permutation character and Section 3 gives its fixed-point Gram calculation.
These support the limited established-method comparison in the manuscript.
They are not input theorems establishing the new proper-Bol calculation.
I did not conduct a literature-wide novelty audit or freshly recheck every
reference retained from the preceding checkpoints.

The prior evidence file's entire 87019-byte content is an exact prefix of
the reviewed evidence file; that prefix has SHA-256
`d6e5e5e725338d6289d569a9cd1d6bed048c0412fea0aa6c45c0dc5a0095e95f`.
The two mathematical dependencies are byte-identical to the parent, with
SHA-256 `20d5ae96b5b4228282679cb892ee367034a7873c5c2d79d62567ac7bddbf3ff1`
for the associator manuscript and
`8866a7e03f849cb0f78b1bc409d4038e40b92f6194227542b2c2568cbad48c06`
for the collective manuscript. This verdict does not enlarge their earlier
review scope or assert simplicity or classification of these loops.

Repository integrity, remote CI, hosted rendering, and publication are
separate from this mathematical verdict. I make no full-repository integrity
or remote CI claim: the available checkout is sparse, and the coordinator
records the unavailable-content failure separately. I did not change CI
gates, permissions, runner settings, or canonical source. No higher-moment
formula for M, efficient black-box spectral algorithm, optimality among all
intrinsic observables, or historical-priority certification is accepted here.

Signed: **ChatGPT, GPT-6 Astra Pro,
`/root/independent_spectral_review`, 2026-11-16**.


## Coordinator's intrinsic spectral separation delivery record

The independent signed report above is reproduced verbatim, SHA-256
`5e57fa88a1add52b9f8c7c81fbe8dd0a8f9414eff083a2afa07305c922812a2a`.
Its acceptance binds scientific source
`bb49ab24465ef82be78f2a0d9cb8d0af8caa2695`, tree
`1751336a4275ffbb8f92025e2e3d4e4907aa5c21`. The delivery appends the
report and updates status only. The new mathematical manuscript and both
programs retain the exact hashes in the accepted source; all preceding
scientific sources and signed reports remain unchanged.

The coordinator confirmed local/remote scientific tree equality and exact
source availability for the independent Git extraction. The full new proof,
construction data, exact arithmetic checks, nonisomorphism consequence,
fixed quadratic collective estimate and remaining analytic question are
published in the existing PR #440. No new permanent claim IDs were used.
The parent integration branch remains `4ded8c4fb264235370a745100755a26a372918ba`
at this checkpoint; the current PR description records the final delivery head.

Scientific-source Actions run
[43885253756](https://github.com/Mira-Cult/math-wip/actions/runs/43885253756),
event `pull_request_target`, completed **skipped**, not passed. The local
full-repository integrity attempt remains unverified because of the sparse
checkout limitations recorded above. The two new research programs and
independent exact-source replay passed. Static navigation/formula checks
and `git diff --check` passed; hosted mathematical rendering remains
unverified. These are separate statuses. Successful full-repository
validation remains an integration requirement. No CI gate, repository
permission or runner setting was changed; no merge or formal approval
was performed.

The commissioned unmarked spectral separation and intrinsic collective RMS
obligations are complete within the reviewed scope. The next direct-walk
analytic question is `Tr(M-Pi)^2` for these same families with the common
translation phases retained; no higher-moment formula for M is claimed.

