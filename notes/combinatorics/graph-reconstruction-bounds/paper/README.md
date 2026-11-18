# Counting and stability in graph reconstruction

*Mira · November 2026*

[Read the paper (PDF)](counting-and-stability.pdf) · [Main LaTeX source](counting-and-stability.tex) · [Research writeup](../README.md)

The paper begins with the count of all ordinary-deck parents and the consequent LWPP upper bound for recognition. The [structural section](matching.tex) proves that ambiguity requires a linear matching of pairs with low neighborhood disagreement. The [metric section](edits.tex) uses that matching in two different ways: marking a pair to make a graph reconstructible, and ruling out all such matchings throughout a random edit ball. The LaTeX sources include the proofs and the bibliography; no graph data, external figures or computation are needed to derive these results.

## Build

Use a standard TeX Live installation with pdfLaTeX. With the three TeX files in the same directory:

```sh
mkdir -p build
pdflatex -no-shell-escape -halt-on-error -output-directory=build counting-and-stability.tex
pdflatex -no-shell-escape -halt-on-error -output-directory=build counting-and-stability.tex
```

The second run resolves cross-references and citations. The resulting file is `build/counting-and-stability.pdf`.
