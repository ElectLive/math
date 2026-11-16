# Starter tasks

These are bounded tasks, not a claim that every branch has complete public proof closure. Record the repository commit before beginning. Check [current advances](CURRENT_RESULTS.md) for superseding results.

## T1. Reproduce and review the specialized existence proof

**Start:** [direct proof](0018-non-g-loop-non-bruck-existence.md), [packet interfaces and commands](packet/README.md).  
**Question:** do the specialized lemmas establish the claimed simple proper loop and its isotope obstructions without the general exhaustion theorem?  
**Work:** rerun both small checks; independently review one lemma and its precise use in the main theorem; check the conventions on isomorphism and isotopy.  
**Deliverable:** exact-source review with equations checked, commands/output and any repair.  
**Boundary:** arithmetic success alone does not prove the theorem; this task need not recertify the whole class-two framework.

## T2. Make the A₅ simple-diagonal subcase publicly auditable

**Start:** [SD dependency map](SD_DEPENDENCIES.md).  
**Question:** what is the minimal complete public chain for the A₅ subcase of the SDₖ exclusion?  
**Work:** obtain the listed family proof and each actual folder/inversion/semiregularity input, preserving source versions. Separate local deductions from imported published facts.  
**Deliverable:** an accessible dependency list and proof package, then a scoped review.  
**Boundary:** the current packet does not contain all these inputs. Request the missing material rather than infer that the all-socle theorem is already self-contained.

## T3. Test an actual Bruck lifting obstruction

**Start:** [actual two-N residual](update-2026-11-16/manuscripts/bruck-two-n-cross-residual.md) and the Bruck section of [the catalogue](CURRENT_RESULTS.md).  
**Question:** can the remaining affine compatibility conditions be solved in a precise fixed model, or is there a uniform obstruction?  
**Work:** identify all missing dependencies first; retain extension, stabilizer, inversion and marked-section data together. Reproduce the supplied toy control only as a check of its formulas.  
**Deliverable:** an actual admissible datum or a proved obstruction with exact scope and negative controls.  
**Boundary:** a toy shadow solution or ordinary group extension is not a Bruck-loop construction.

## T4. Simplify a parameter orbit without changing equivalence

**Start:** [mixed matrix model](update-2026-11-16/manuscripts/radical-free-mixed-matrix-classification.md).  
**Question:** can its exact length-preserving permutation/column-sign equivalence be simplified for one explicitly bounded parameter slice?  
**Work:** state the selected slice; derive invariants; test completeness on small cases; compare canonical representatives only under the actual allowed maps.  
**Deliverable:** exact invariant or orbit algorithm with proof, or a counterexample to a proposed simplification.  
**Boundary:** do not substitute graph isomorphism or matrix similarity without proving equivalence, and do not claim global loop classification.

## T5. Add a source that changes a researcher's next move

**Start:** public references linked from the [catalogue](README.md) and a chosen result.  
**Question:** is there an overlooked theorem, counterexample, convention or computational resource relevant to it?  
**Work:** supply author/title/year, accessible source or DOI, exact theorem/page, and a short comparison of hypotheses.  
**Deliverable:** a reference contribution or correction. No new proof or full novelty audit is expected.

## Reproducibility infrastructure still needed

The current packets contain selected controls, not the entire internal computational platform. A future infrastructure contribution should publish a minimal working small-loop example with its actual imports, versions, inputs and tests. Do not assume that a missing internal `bol_engine.py`, `perm_group.py`, `known_constructions.py` or test suite is present merely because a manuscript mentions it.

For any proposed run, list every imported module and data file before advertising the command as reproducible. A useful small example should construct a table, check the loop/Bol identities and stated invariants, and state exactly how simplicity is checked. This is separate from constructing an astronomically large example symbolically.
