# Verification and scope

The mathematical source is the exact scientific revision
`29a00faed29cf166dd54e95eed1861ce79b6428c` of Mira Cult's research workspace.
Both proof files and the certificate files are byte-identical to their canonical
sources at that revision. The original mathematical reviews examined revision
`77da2135811dac4f3e44ed3f4306dff9505a49ef`; independent ratifications then verified
that the current revision changes only mathematical presentation. Protected
inline math, named inequality commands and visible equation labels replace
delimiter forms mishandled by the target renderer. No private source is required
to read or reproduce these public proofs or finite certificates.

## Mathematical review

The covering theorem and its primorial corollary received two independent
nonauthor model reviews of the exact scientific revision. The first-occurrence
proof received independent nonauthor model reviews. Reviewers checked the
arbitrary-factor survivor classification, uniform Rankin estimate, reduced
residue count, Brun–Titchmarsh scale, cleanup budget, admissibility, proper
divisors, persistence, internal-period boundary and first-index conversion.
No blocking mathematical defect was found in these published results.

These were in-session model reviews, not external peer review, human expert
certification or a Lean verification. They do not certify endpoint primality,
a numerical asymptotic threshold, historical priority, or either Erdős question.

## Exact arithmetic

Python 3.12.14, standard library only. Both documented verifier commands passed:
90 even gaps, 180 prime endpoint proofs and 8,100 proper-divisor certificates.
An independent reviewer repeated endpoint primality using division by every
integer through the exact square root and checked divisors and quotients.
Composite endpoints, a missing factor, nondivisor, unit factor, improper
self-factor, duplicate gap and Boolean gap were all rejected in both ordinary
and optimized Python. These are occurrence certificates only.

## Source identity

| File | SHA-256 |
|---|---|
| `cover.md` | `e8cd57d6cf6efc42757137309f53e008219ab604259393f4c5907d64c125cf41` |
| `first-occurrence.md` | `1c8916c572a48e0084d376b1e5c3cdda56a1c229955b8bfe0f41ee47145a0563` |
| `code/gap_certificates.py` | `6e797d55aae9815672285ef3e501e06aca98afef77809e128e624cd50ccb4d1f` |
| `evidence/gaps-through-180.json` | `3fd93d5479ead6764abb2808ac3bae2248388ff2bbf7e20a80f74e7966cb4978` |

## Publication checks

Local links in the new note were checked against the publication files.
On 16 November 2026 the owner inspected GitHub's rendered public entry page,
both complete proof pages, their result and dependency tables, and the verifier
commands. The mathematical renderer produced 18, 250 and 81 formula elements
respectively, with no formula-renderer errors. Screenshots were checked across
the theorem statements, proof sections and conditional scope statements.
This is a publication-format check, separate from mathematical review.

The private full-repository integrity check was blocked by missing unrelated
files in the sparse local intake. Its workflow at the original reviewed
revision was skipped; that is not a successful CI result. The 114 available
scoped repository regression tests passed. No full integration CI pass is
claimed for this research checkpoint.
