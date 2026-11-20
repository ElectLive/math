# Rational points of reduced height in the middle-third Cantor set

- [Read the paper (PDF)](cantor-rational-points.pdf).
- [Editable LaTeX source](paper.tex), with section sources and bibliography alongside.
- [Research overview](../README.md) and [verification scope](../VERIFICATION.md).

To build locally with a standard TeX Live distribution (including Latin Modern and BibTeX), run from this directory:

```sh
latexmk -pdf -halt-on-error paper.tex
```

The main theorem counts individual rational points by the denominator in lowest terms. The manuscript does not rely on a private dependency, a computational classification, or a formal proof file.
