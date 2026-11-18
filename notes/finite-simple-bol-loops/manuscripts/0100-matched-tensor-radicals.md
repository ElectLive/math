# 0100. No matched natural tensor radical over a centerless special linear square

**Mira Cult**

A nonabelian simple group can occur twice in a Bol envelope with canonical inversion interchanging the two copies. Can an additive matrix layer sit underneath that square, with each copy acting naturally on its own tensor factor? Under the precise centerless, matched-action hypotheses below, the answer is **no** in every rank at least three, over every finite field. The smallest binary case requires a different argument from the rank estimates.

## The theorem

Let $`q`$ be a prime power, $`d\ge3`$, $`\gcd(d,q-1)=1`$, and $`T=\mathrm{SL}_d(q)=\mathrm{PSL}_d(q)`$. No finite simple nonassociative **left** Bol loop has faithful left multiplication group in an exact sequence

```math
1\longrightarrow \mathrm{Mat}_d(q)^+
 \longrightarrow G\longrightarrow T\times T\longrightarrow1
```

in which $`(a,b)`$ acts by $`X\mapsto aXb^{\mathsf t}`$ and the canonical inversion induces the ordinary swap on those same natural coordinates. There is no prescribed point stabilizer, splitting or complement. Both possible transpose signs in odd characteristic are covered. This is about the **whole indicated canonical extension**, not the occurrence of its groups or module as sections of a larger group. Unmatched, scalar-central and factor-preserving actions are not contained in this theorem.

## Why matrix rank constrains the folder

Write $`H`$ for the stabilizer of the loop identity and $`K`$ for its sharply transitive set of left translations. The canonical inversion $`\tau`$ inverts every member of $`K`$. In the extension by an auxiliary involution $`t`$ inducing $`\tau`$, the outside set $`\Lambda=tK`$ is a union of involution classes; two distinct selected involutions cannot multiply to a member of $`H`$. This is the [canonical-folder criterion](../sources/foundations/C0001.md) and the [inversion construction](../sources/foundations/C0007.md).

In the quotient the selected marks form the **single swap class**, since an outside involution is determined by one element of $`T`$. Hence above each quotient mark there are equally many actual marks, say $`r`$. Let $`W=H\cap V`$, $`J=HV/V`$, $`V=\mathrm{Mat}_d(q)^+`$. The original sharp transversals give a multiplicity $`m=[V:W]/r`$, and

```math
m>1,\qquad |J|=m|T|.
```

Equality at $`m=1`$ would induce a nontrivial quotient loop; in general the blocks need not themselves define one. The two projections of $`J`$ give a factorization of $`T`$. Thus an **actual** stabilizer must pass both a group-factorization bound and a geometric bound on its intersection $`W`$ with the matrix layer.

After the large-sheet and full-endpoint alternatives are eliminated, differences of selected marks above the same quotient label fill an alternating matrix space. Its conjugates contain every even-rank matrix. Consequently every nonzero difference of elements of $`W`$ has odd rank. View each element as a graph subspace in $`\mathbf F_q^d\oplus\mathbf F_q^d`$ and count intersections of projective points modulo a prime dividing $`q+1`$. The incidence Gram matrix is the identity in odd dimension and the all-ones matrix minus the identity in even dimension. Removing vertical points gives

```math
|W|\le q^d\frac{q^d-1}{q-1}+[d\text{ even}]<q^{2d}.
```

Here the bracket is one if its condition holds, zero otherwise. The argument works for additive subgroups and does not assume linearity over the whole field. On the other hand the multiplicity equation in this sheet is $`m|W|=q^{d(d+1)/2}`$. The possible endpoint factorizations cannot accommodate so large an $`m`$. Special treatment of rank four in characteristic two and of the small exceptional group $`A_8`$ is essential.

The remaining case $`d=3,q=2`$ shows why a quotient count alone cannot settle the question. The natural module has a nonprincipal derivation and the full group extension may initially be nonsplit. Its restriction to the actual stabilizer, after the necessary coefficient quotient, has a complement. On the only possible mixed cohomology class this restriction is injective, forcing the candidate extension to split. Even then the actual stabilizer can have its own nonprincipal cocycle. A specific pair of marked sheets over a transvection meets **every** possible stabilizer cocycle, contradicting $`H\cap\Lambda^2=1`$.

## Complete arguments and inputs

1. [The original marked square, odd-field splitting, both transpose signs and the odd rank-three foundation](../sources/tensor-layers/odd-field-foundation.md). The odd rank-three maximal-subgroup step uses [Gill, Theorem 19](https://cage.ugent.be/geometry/Files/148/psl3alltogether.pdf), not a prime-field-only subgroup list.
2. [Finite-field rank capacity, genuine binary mark phases and the rank-four endpoints](../sources/tensor-layers/tensor-capacity.md). The proper-factor input is [Li–Xia, Theorem 2.15 and Appendix Tables A.1 and A.2](https://arxiv.org/pdf/1408.0350v3), restating the maximal-factorization theorem of Liebeck–Praeger–Saxl. The binary rank-four argument also uses [the transitive linear-group classification in Lemma 3.1](https://www.ma.imperial.ac.uk/~mwl/REGFINAL.PDF) and the maximal-subgroup rosters for [A₈](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A8.html) and [A₇](https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A7.html).
3. [The exceptional binary rank-three extension class and actual stabilizer collision](../sources/tensor-layers/binary-three.md). In particular, it is not correct here to assume that every extension splits or that the stabilizer is principal.

## Evidence

The all-field capacity proof (excluding the binary rank-three residual) received one independent AI mathematical acceptance at source c4791c77dfb778c368006c71abad7eef2b58a777. The same reviewer separately accepted the binary rank-three proof at source d9c959216f10dea547baf82fdabc18c17dd36ca5. These are not two reviewers of one argument. Neither result has been human-refereed or formally verified here.

The independent [capacity checker](../sources/code/check_c479_even_phase_and_algebra.py) tests 18,000 actual congruences over the four-element field, all 255 nonzero diagonal phases in four coordinates, and the finite algebra used at the rank-four boundary. The [binary three-dimensional checker](../sources/code/check_d9c9_bar_obstruction_independent.py) tests the nonzero mixed extension class and all 1,024 and 128 concrete stabilizer cocycles in the two relevant quotients. These computations stress the exceptional steps; the infinite-family exclusion is a mathematical deduction from the cited inputs.

[Review provenance, contributions and all runnable controls](../normal-layer-evidence.md).
