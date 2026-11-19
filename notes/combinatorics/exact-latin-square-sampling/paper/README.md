# Exact uniform generation of labeled Latin squares

- [Read the paper (PDF)](exact-uniform-latin-squares.pdf).
- [Editable LaTeX source](paper.tex). Its included files are in this directory.
- [Complexity breakdown](../complexity.md) and [verification scope](../VERIFICATION.md).

Build from this directory with a current LaTeX distribution:

```sh
latexmk -pdf -halt-on-error paper.tex
```

The paper proves the bound for a mathematical algorithm. The separate [reference sampler](../code/README.md) runs an exact finite version with conservative parameters, not the revised polynomial-time construction.
