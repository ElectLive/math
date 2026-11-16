# Proof sources for factor-permutation classification

Mira Cult

These mathematical source arguments support public claims **0064–0069** and the earlier reduction interfaces they use. Read the [results overview](../../RESULTS.md) and [claim catalogue](../../CLAIMS.md) first; the source notes are not competing results catalogues.

The current structural endpoint is the [all-path parameterization](../../manuscripts/0068-abelian-nilpotent-path-parameters.md): every odd abelian top, and the nilpotent branch with zero actual residual graph, in the pure A5 permutation model. Intermediate notes retain the scope of their individual lemmas. Their local statements of a remaining obligation may be answered by a later argument in the linked chain; the current [open problem board](../../OPEN_PROBLEMS.md) governs the programme's frontier.

The statements, proofs, counterexamples and mathematical qualifications have been preserved. Review-administration prose has been removed. The [source mapping](../../classification-source-map.json) records provenance; publication does not constitute a fresh proof of every imported interface. In particular, zero residual graph is an algebraic condition, not absence of proof dependencies.

The finite form certificate can be rerun with Python 3:

```sh
python sources/factor-permutation/code/verify_a5_exponent25_form_orbits.py
```

Run from `notes/finite-simple-bol-loops`, this enumerates 500 substitutions, 12,400 nondegenerate alternating forms and 88 orbits. It checks the finite form action, not independently the reduction from loop isomorphism to form orbits. That reduction is proved in the [regular census](../../manuscripts/0064-extraspecial-regular-census.md).
