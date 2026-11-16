# Principal S₅ modules with one four-dimensional factor

**Module result with scoped independent review recorded below.** Let $`X`$ be a finite-dimensional $`\mathbb F_2S_5`$-module with exactly one composition factor $`M`$ and all remaining factors trivial, in the notation of [bruck-s5-radical.md](bruck-s5-radical.md). Then $`X`$ has a decomposition $`X\cong X_0\oplus A_1`$, where $`A_1`$ is a module for the sign quotient $`S_5/A_5\cong C_2`$, and $`X_0`$ has dimension at most 42. Consequently, the unique indecomposable summand containing $`M`$ has dimension at most 42. The separately described finite calculation sharpens this bound to 11 and is included in the scoped review below.

This manuscript continues [C0010](../../claims/0010.md) and allocates no new claim ID. It is a statement about modules: it does not assert that sign-only summands can be removed from a loop envelope while preserving its stabilizer, section, or simplicity.

## Inputs and the six-point module

Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemmas 3.1 and 4.1, supplies the two-generator presentations and the simple module $`M`$. Put $`P_6=\mathbb F_2^6`$ for the projective-line action of $`S_5\cong PGL_2(5)`$, $`E`$ for its even-weight submodule, and $`J=P_6/\mathbf1`$, where $`\mathbf1`$ is the constant line. The preceding [radical manuscript](bruck-s5-radical.md) records $`E/\mathbf1\cong M`$, the one-dimensional space $`H^1(S_5,J)`$, the unique nonsplit $`0\to J\to V_6\to\mathbf1\to0`$, and $`H^1(S_5,V_6)=0`$. Its dimension-six review is pinned at the recorded source revision; the dimension-seven argument and its cohomology interface have a separate review at the recorded source revision. Those reviews do not cover the new module theorem here.

The submodule lattice of $`P_6`$ used below is $`0<\mathbf1<E<P_6`$. To see this, first $`J^{S_5}=0`$: a fixed coset $`x+\mathbf1`$ defines a homomorphism $`S_5\to C_2`$ by $`gx+x`$; it vanishes on a point stabilizer $`F_{20}`$, which contains odd permutations, so it is zero and $`x`$ is constant. The dot product identifies $`E^*`$ with $`J`$, so $`E`$ has no nonzero invariant functional. As $`E/\mathbf1\cong M`$ is simple, this rules out a complement to $`\mathbf1`$ in $`E`$, and its only submodules are $`0,\mathbf1,E`$. A submodule not contained in $`E`$ contains an odd-weight vector. The six-point action is sharply 3-transitive; the orbit of an odd-weight vector of weight 1, 3, or 5 spans $`P_6`$ (for weight 3, differences of triples generate all even-weight vectors). Thus no further submodules occur.

## Fixed-free modules

If $`X^{S_5}=0`$, then $`X\cong M,J,`$ or $`V_6`$. If no trivial factor occurs, $`X=M`$. Otherwise $`C_X(P)\ne0`$ for a 5-cycle subgroup $`P`$, and the 2-group $`F_{20}/P`$ fixes a nonzero vector $`v`$ there. Its orbit map $`P_6\to X`$ cannot be injective, since the constant vector is fixed, and cannot have kernel $`E`$ or $`P_6`$, since then $`v`$ is fixed. Hence its kernel is $`\mathbf1`$ and $`J\le X`$.

The quotient $`B=X/J`$ has only trivial composition factors. Its image is a 2-group, so the perfect group $`A_5`$ acts trivially and $`B`$ factors through sign. From the exact sequence, the kernel of $`B^{S_5}\to H^1(S_5,J)`$ is the image of $`X^{S_5}`$, so fixed-freeness and $`\dim H^1(S_5,J)=1`$ imply $`\dim B^{S_5}\le1`$. Every sign module is a direct sum of $`\mathbf1`$ and the 2-dimensional regular module $`R`$. If $`\dim B\ge2`$, the only possibility with one-dimensional fixed space is $`B=R`$. Fixed-freeness makes the inverse image of its fixed line the nonsplit extension $`V_6`$, but $`H^1(S_5,V_6)=0`$ splits the remaining trivial quotient and produces a fixed vector, contradiction. Thus $`B=0`$ or $`\mathbf1`$, yielding $`J`$ or $`V_6`$. Dually, a module of this kind with no trivial quotient is $`M,J^*,`$ or $`V_6^*`$.

## Splitting off sign-only summands

Let $`A`$ be the sum of all submodules of $`X`$ with only trivial composition factors. Each is acted on trivially by $`A_5`$, so their sum is as well; thus $`A\cong\mathbf1^a\oplus R^b`$. The quotient $`Q=X/A`$ has no nonzero fixed vector: the preimage of a trivial submodule would have only trivial composition factors, hence would also be sign-only and larger than $`A`$. It still has exactly one $`M`$ factor. Therefore $`Q\cong M,J,`$ or $`V_6`$.

The extension class lies in

```math
\mathop{\mathrm{Ext}}\nolimits^1(Q,A)\cong
\mathop{\mathrm{Ext}}\nolimits^1(Q,\mathbf1)^a\oplus\mathop{\mathrm{Ext}}\nolimits^1(Q,R)^b.
```

The subgroups $`GL_a(\mathbb F_2)`$ and $`GL_b(\mathbb F_2)`$ of the automorphism group of $`A`$ allow independent row operations on these tuples; no semisimplicity of $`R`$ is assumed. Hence after a basis change the class is supported on at most $`\dim\mathop{\mathrm{Ext}}\nolimits^1(Q,\mathbf1)`$ copies of $`\mathbf1`$ and $`\dim\mathop{\mathrm{Ext}}\nolimits^1(Q,R)`$ copies of $`R`$. If $`A=A_0\oplus A_1`$ is this support decomposition, the zero $`A_1`$-coordinate splits and $`X\cong X_0\oplus A_1`$, with $`0\to A_0\to X_0\to Q\to0`$.

By Shapiro, $`\mathop{\mathrm{Ext}}\nolimits^1(Q,\mathbf1)\cong H^1(S_5,Q^*)`$ and $`\mathop{\mathrm{Ext}}\nolimits^1(Q,R)\cong H^1(A_5,Q^*)`$, since $`R\cong\mathop{\mathrm{Ind}}\nolimits_{A_5}^{S_5}\mathbf1`$. Both $`S_5`$ and $`A_5`$ have two generators, so each $`H^1`$ space has dimension at most $`2\dim Q`$: a cocycle is determined by its values on generators. Consequently

```math
\dim X_0\le \dim Q+2\dim Q+2(2\dim Q)
=7\dim Q\le42.
```

Krull–Schmidt leaves a unique indecomposable summand containing $`M`$; it is a summand of $`X_0`$. All other indecomposable summands have only trivial factors and hence are sign modules. This gives the proposed analytic 42 bound, conditional on the cited inputs and review of this argument.

## Candidate finite sharpening

[verify_s5_principal_h1_bounds.py](../code/verify_s5_principal_h1_bounds.py) constructs the dual matrices of $`M,J,V_6`$, verifies the generated $`S_5`$ and $`A_5`$ matrix groups have orders 120 and 60, and imposes cocycle consistency on every Cayley edge. It checks principal cocycles satisfy the resulting equations. The reported dimensions $`(\dim H^1(S_5,Q^*),\dim H^1(A_5,Q^*))`$ are $`(1,2)`$ for $`Q=M`$, $`(2,2)`$ for $`J`$, and $`(1,2)`$ for $`V_6`$. Substitution into the support bound would give dimensions at most 9, 11, and 11, respectively, and an indecomposable bound of 11.

This sharpening is a new finite calculation, not part of the earlier reviews. Its matrix identification, inverse-transpose convention, Cayley checks, and the module argument above require independent review. The analytic 42 bound does not depend on this new calculation.

## Scoped independent review

Independent checks an independent check accepted both the analytic bound 42 and the finite sharpening to 11 at exact source the recorded source revision, conditional on the cited prior module and cohomology inputs. The review checked the six-point submodule lattice, fixed-free classification, maximal sign-only submodule, Ext-coordinate row operations and Shapiro identifications. The reviewer inspected the inverse-transpose and Cayley consistency code, principal-cocycle inclusion and A5 generators, then independently ran it with Python 3.12.14: the displayed H¹ dimensions (1,2), (2,2), (1,2) were reproduced. Hence X splits as a sign-only summand plus a summand of dimension at most 11; its unique indecomposable containing M has dimension at most 11. This is a module statement only, with no asserted operation on a loop stabilizer or section and no formal verification.

