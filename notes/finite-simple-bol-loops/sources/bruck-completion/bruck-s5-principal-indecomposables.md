# One-M principal indecomposable candidates

This manuscript-local computation continues [C0010](../../claims/0010.md) and the [567-extension cover](bruck-s5-principal-enumeration.md). It assumes the cover and the [one-M support theorem](bruck-s5-principal-one-m.md), and the envelope consequences below also assume the [principal-envelope bound](bruck-s5-principal-envelope-bound.md). The cover and its generator construction were reviewed at source the recorded source revision under the recorded review scope; the new splitting test and deductions have the scoped independent review recorded below. 

## Splitting test and completeness

Let X be any module in the cover, with exactly one M composition factor and all other factors trivial. A decomposition of X has exactly one indecomposable summand containing M. Every other indecomposable has only trivial composition factors, so the perfect subgroup A₅ acts trivially and it is an indecomposable module for the sign quotient C₂. Over F₂ these are precisely the trivial module 1 and the regular module R=F₂C₂. Thus X is indecomposable if and only if neither 1 nor R is a direct summand.

For S=1 or R, S is a direct summand of X if and only if there are module maps i:S→X and p:X→S such that pi is a unit in End(S). One direction follows from a splitting; in the other, i(pi)⁻¹ is a section of p. For S=1 the endomorphism ring is F₂. For R, End(R)=F₂[e]/(e²), where e is the transposition action plus the identity; its units are exactly those with identity coefficient 1. In the swap basis, an endomorphism has matrix columns (a,b),(b,a), and the residue is a+b, the parity of either column. Identity and swap have residue 1; zero and identity-plus-swap have residue 0. Hence in either case the residue map End(S)→F₂ modulo its radical detects units. Composition followed by this residue is bilinear. It is nonzero for some pair of maps if and only if it is nonzero on some pair of basis maps. Computing bases of both Hom spaces by the generator-intertwining equations and testing all basis pairs is therefore an exact splitting test, without a module-isomorphism search.

The optional `--indecomposable` mode of [the enumerator](../code/enumerate_bruck_s5_principal_modules.py) applies this test to all 567 parametrized extension representatives. The surviving numbers are 5 with quotient M, 18 with quotient J, and 5 with quotient V₆. Their distribution is:

| dim X₀ | h₀ = dim Hom(X₀,1) | representatives |
|---:|---:|---:|
| 4 | 0 | 1 |
| 5 | 0 | 1 |
| 5 | 1 | 1 |
| 6 | 0 | 2 |
| 6 | 1 | 5 |
| 7 | 1 | 9 |
| 7 | 2 | 1 |
| 8 | 1 | 6 |
| 8 | 2 | 2 |

These 28 are parametrized extension representatives, not claimed distinct isomorphism classes. Since the cover contains a representative of every possible indecomposable one-M summand, the test retains at least one representative of each such summand. The program prints reproducible quotient, kernel, class-index, cocycle, dimension and h₀ labels. It computes h₀ as the codimension of the span of the two generator differences.

## Conditional envelope consequence

Write the principal block as X₀⊕1ᵘ⊕Rᵛ and put d=dim X₀. Under the cited envelope argument, h₀+u+v≤d−4. Thus its dimension is at most d+2(d−4−h₀)=3d−8−2h₀. The table gives the bound **14**, attained by the numerical pair (d,h₀)=(8,1); all other rows give at most 12. This is a necessary bound, not an assertion that an envelope attaining it exists.

The same inequality gives respectively 1, 3, 1, 12, 15, 54, 3, 60 and 12 labelled (representative,u,v) presentations for the table rows, totaling **161**. This includes the M-alone presentation, excluded separately by the cited envelope analysis; it also retains repeated isomorphism types. These counts do not classify the N-block, stabilizers, sections, group extensions, or loops.

## Reproduction

From the repository root, using the source revision containing this manuscript and script:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/enumerate_bruck_s5_principal_modules.py --indecomposable
```

The new mode reports the table, labels, bound and tail count and asserts 28, 14 and 161. The default and `--envelope-filter` modes retain their earlier output. This is finite computational evidence conditional on the cover and envelope inputs, not an independent mathematical review or a classification of loop envelopes.

## Independent review

an independent check accepted the splitting test and deductions at exact source the recorded source revision, conditional on the previously reviewed cover and envelope inputs. The reviewer checked the generator Hom equations and complete nullspaces, the unique M-containing summand argument, the bilinear residue test, and specifically the swap-basis unit residue a+b with all four controls. An independent Python 3.12.14 run of the exported pinned script with `--indecomposable` reproduced all 28 representatives, the dimension/h₀ table, bound 14 and 161 labelled tails. This acceptance does not remove duplicates, bound the N-block, assert sharpness or classify envelopes or loops.

