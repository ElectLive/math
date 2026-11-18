# 0108. Matrix rank rules out the ordinary factor-preserving tensor layer

**Mira Cult**

Suppose the faithful left multiplication group of a simple proper left Bol loop has an additive layer of square matrices. Two special linear groups act on the layer, one on the rows and one on the columns. An inversion preserving the two factors would have to select certain eigenspace profiles. Those profiles require a stabilizer large enough to account for all actual loop points. But the stabilizer also preserves an additive code in which every nonzero matrix has restricted rank. The two requirements are incompatible.

**Theorem (ordinary branch).** Let $`q`$ be odd, $`d\ge3`$, and $`T=\mathrm{PSL}_d(q)`$ nonabelian simple. There is no finite simple proper left Bol loop with faithful left multiplication group $`G`$ in an exact sequence

```math
1\longrightarrow V=\mathrm{Mat}_d(q)^+\longrightarrow G
\longrightarrow Y=(\mathrm{SL}_d(q)\times\mathrm{SL}_d(q))/
 \{(zI,z^{-1}I):z^d=1\}\longrightarrow1
```

such that the quotient acts by $`(A,B)X=AXB^{\mathsf t}`$ and the canonical inversion acts on $`V`$ by an ordinary fixed-factor operator $`X\mapsto PXQ^{\mathsf t}`$, with $`P,Q\in\mathrm{GL}_d(q)`$. This assumes neither a split extension nor a product point stabilizer. It does specify the whole extension and its action, not merely a section of the left group. It is different from the [matched factor-exchange theorem](0100-matched-tensor-radicals.md).

### Where rank enters

Let $`H`$ stabilize the loop identity, $`K`$ be the left translations, and $`t`$ implement the canonical inversion in $`G\rtimes\langle t\rangle`$. The set $`\Lambda=tK`$ consists of actual marked involutions. It is invariant under conjugation and $`H\cap\Lambda^2=1`$. Write $`W=H\cap V`$ and $`J=HV/V`$. A marked involution over a selected quotient label has its whole negative eigenspace as its fiber once a compatible complement is chosen. The pairwise products in this fiber force $`W`$ to avoid that eigenspace and its conjugates. On the other hand, counting the same fibers gives the exact index $`[Y:J]`$. Both statements use the original folder; neither is a calculation in a hypothetical quotient loop.

There are three parts of the proof:

1. [Actual affine sheets, spectral bounds and the strict cut](../sources/tensor-layers/ordinary-profiles.md). This gives the compatible complement, proves the formula for each split eigenspace profile, excludes every balanced profile by an actual lift of a transvection and excludes the extremal rank-one case. It uses the [odd-kernel orbit theorem](0098-odd-kernel-stabilizer-orbits.md) and the [odd-kernel block theorem](0101-odd-kernel-block-action.md).
2. [The effective idealizer and odd ranks](../sources/tensor-layers/ordinary-idealizers.md). On the span of the images of $`W`$, every nonzero endomorphism preserving $`W`$ by multiplication has rank at least the minimum rank of $`W`$. The semisimple part of this algebra, over the **prime** field, bounds the prime-to-characteristic part of a pure stabilizer. Its defining-characteristic part comes from a unitriangular flag. In odd dimension the index forced by the sheets contradicts the two bounds together, including the ternary rank-five case.
3. [Even ranks: the quadratic class and the two-sided obstruction](../sources/tensor-layers/ordinary-quadratic.md). In even dimension the factors of an involution need not themselves be involutions: their squares can be reciprocal nonsquares. There is one such quadratic class when its determinant tag is admitted. Its negative sheet contains matrices of every even rank, with every determinant at full rank. The proof handles the split-only, quadratic-only and mixed selections separately. The decisive quadratic-only point is that two matrix-algebra corners on **both** sides would manufacture a nonzero codeword of even rank.

One must not count all possible labels in place of the selected ones, presume that the code is linear over the full field, or claim that simultaneous negative signs always give different operators. Each shortcut changes one of the inequalities.

### Scope and evidence

The odd-rank idealizer analysis and the even-rank quadratic analysis received **separate** independent AI mathematical reviews of their precise residual arguments. The preparatory reductions are proof dependencies, not a new joint review. These reviews do not cover rank two, even fields, a field automorphism, a factor exchange or arbitrary matrix modules. In particular they must not be reported as one independent verification of the all-inversions classification. The unrestricted finite simple proper left Bol classification is open.

[Exact review boundaries, source revisions and four executable controls](../normal-layer-evidence.md#ordinary-tensor-profiles-and-idealizers).
