# Finite extension cover for one-M principal modules

**Finite extension cover with scoped independent review recorded below.** Let $`X`$ be an $`\mathbb F_2S_5`$-module with exactly one composition factor $`M`$ and all other factors trivial. The construction below gives a finite superset of the possible indecomposable summands containing $`M`$. It does not classify modules up to isomorphism or classify loop envelopes.

This manuscript continues [C0010](../../claims/0010.md), allocates no claim ID, and uses the one-$`M`$ support theorem in [bruck-s5-principal-one-m.md](bruck-s5-principal-one-m.md), independently reviewed at exact source the recorded source revision. The enumeration and optional envelope filter below have not been reviewed. The $`N`$-block and group extensions, stabilizers, sections and simplicity remain outside this parametrization.

## Complete parameter domain

The cited support theorem writes $`X\cong X_0\oplus\mathbf1^u\oplus R^v`$, where $`X_0`$ is the indecomposable summand containing $`M`$, $`R=\mathbb F_2C_2`$ is the regular sign module, and $`X_0`$ can be represented by an extension

```math
0\longrightarrow\mathbf1^a\oplus R^b\longrightarrow X_0
\longrightarrow Q\longrightarrow0,\qquad Q\in\{M,J,V_6\}.
```

The permitted ranges are $`0\le a\le1`$ for $`Q=M,V_6`$, $`0\le a\le2`$ for $`Q=J`$, and $`0\le b\le2`$ in every case. The bounds come from the support-reduction argument and the reviewed cohomology dimensions, not from an assumption that an extension chosen in this larger list has a maximal sign-only kernel. Allowing every class in these ranges deliberately includes decomposable modules and repeated isomorphism types.

For fixed identifications of kernel and quotient, extension classes form

```math
H^1\!\left(S_5,\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}
  (Q,\mathbf1^a\oplus R^b)\right).
```

Additivity in the kernel and the previously reviewed $`H^1`$ dimensions give dimension $`ae_1+be_R`$, where $`(e_1,e_R)=(1,2)`$ for $`Q=M`$, $`(2,2)`$ for $`J`$, and $`(1,2)`$ for $`V_6`$. Thus there are $`2^{ae_1+be_R}`$ classes for each choice; a single triple has at most 256. Summing over the complete displayed domain gives

```math
\begin{array}{c|c|c}
Q & \sum_a2^{ae_1}\sum_b2^{be_R} & \text{classes}\\\hline
M &(1+2)(1+4+16)&63\\
J &(1+4+16)(1+4+16)&441\\
V_6 &(1+2)(1+4+16)&63
\end{array}
\qquad\text{total }567.
```

These are **parametrized extension classes**, not 567 distinct isomorphism classes. Different triples and classes may yield isomorphic modules, and this list has not been filtered for indecomposability or maximality of the chosen sign-only submodule.

## Reproducible construction

[enumerate_bruck_s5_principal_modules.py](../code/enumerate_bruck_s5_principal_modules.py) is a self-contained Python 3.11+ construction. Its $`M,J,V_6`$ generator matrices use the explicit six-point conventions of [verify_s5_principal_h1_bounds.py](../code/verify_s5_principal_h1_bounds.py), while Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 3.1, gives the two-generator group presentation. For every one of the 21 triples $`(Q,a,b)`$, the program constructs the action on $`\mathop{\mathrm{Hom}}\nolimits(Q,\mathbf1^a\oplus R^b)`$, imposes cocycle consistency along all edges of the 120-element Cayley graph, and quotients by explicitly computed principal cocycles. It constructs a pair of block generator matrices for every resulting class, with the upper-right block $`f(g)Q(g)`$, and checks all four presentation relators for each pair. The output counts are checked against the displayed analytic dimensions. Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/enumerate_bruck_s5_principal_modules.py
```

The generator conventions, cocycle-to-block conversion, completeness of the linear algebra, and this implementation require independent exact-revision review. The analytic sum of 567 is separate from the implementation, but depends on the cited reviewed module and cohomology inputs.

## Optional candidate envelope filter

The proposed [principal-envelope bound](bruck-s5-principal-envelope-bound.md) gives necessary conditions for a one-$`M`$ envelope. For a representative $`X_0`$ and sign tail $`\mathbf1^u\oplus R^v`$, write $`h_0=\dim\mathop{\mathrm{Hom}}\nolimits_{S_5}(X_0,\mathbf1)`$. The proposed invariant-functional injection and the candidate 19-dimensional principal-block bound imply

```math
h_0+u+v\le\dim X_0-4,\qquad \dim X_0+u+2v\le19.
```

With `--envelope-filter`, the program computes $`h_0`$ from the span of the generator differences and counts the pairs satisfying these inequalities for every parametrized class. It reports 6,302 labelled $`(\text{extension class},u,v)`$ presentations. This is an optional computational count conditional on the envelope-bound argument and exact-script review, not an isomorphism count. It retains decomposable and nonmaximal representatives, and it neither bounds the $`N`$-block nor enumerates $`H`$, $`K`$, ambient group extensions, or simple loops.

## Scoped independent review

Independent checks an independent check accepted the analytic 567-class cover and its implementation at exact source the recorded source revision, conditional on the reviewed support and cohomology inputs. The reviewer checked the complete parameter domain, Hom action, Cayley cocycle propagation, nullspace and coboundary quotient, block conversion and relators. Both Python 3.12.14 modes passed independently: 567 fixed-kernel/quotient extension classes and 6302 labelled presentations after the necessary envelope filter. The reviewed source predates the new indecomposability mode, which has its own review boundary in [the indecomposable manuscript](bruck-s5-principal-indecomposables.md). These are not isomorphism counts and do not classify H, K, group extensions or loops.

