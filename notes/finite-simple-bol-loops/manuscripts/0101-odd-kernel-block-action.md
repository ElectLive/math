# 0101. The radical of the block-action kernel above an odd normal layer

**Mira Cult**

An odd kernel in the left multiplication group gives blocks of loop elements. Are the permutations induced by the quotient group on these blocks faithful? Not always. We prove that if the kernel is elementary and the quotient acts faithfully and irreducibly on it, the kernel of the block action has trivial solvable radical. In particular a solvable quotient acts faithfully on the blocks. This conclusion makes no splitting assumption; the cohomological refinement below does.

 Use the faithful generated canonical folder $`(G,H,K,\tau)`$ of a finite simple nonassociative **left** Bol loop. Put $`E=G\rtimes\langle t\rangle,\ \Lambda=tK`$. The original marks are $`G`$-invariant involutions and $`H\cap\Lambda^2=1`$. The strict normal-cut criterion is the [faithful-folder normal-subloop criterion](../sources/foundations/C0001.md), Theorem 2.2, not an assumed quotient loop. The results below allow $`G`$ and the loop to have either parity.

### A simultaneous-lift test for arbitrary odd kernels

Let $`1<N<G`$ be $`\tau`$-stable, of odd order, $`Y=G/N`$, and $`J=HN/N`$. Suppose $`G`$ admits a $`\tau`$-stable complement $`S`$ to $`N`$. Then **no** $`N`$-conjugate of $`H`$ contains the pure lift of all $`J`$ inside $`S`$.

In fact each selected quotient mark $`\bar\lambda`$ has its unique lift $`\lambda_S`$ in $`S\rtimes\langle t\rangle`$, itself an involution, and this lift is actually selected. Any original selected lift and $`\lambda_S`$ are Sylow 2-generators in the preimage of $`\langle\bar\lambda\rangle`$, of order $`2|N|`$; Sylow conjugacy can be taken in $`N`$. The *same complement* therefore contains pure lifts of every selected mark. This is not a statement that every quotient involution is selected. The pure products in the complement above all of $`\bar\Lambda^2`$ are consequently in the original $`\Lambda^2`$, including products of arbitrary order.

If the stated stabilizer alignment held, it would give $`J\cap\bar\Lambda^2=1`$, as conjugating $`H`$ preserves avoidance of the $`G`$-invariant $`\Lambda^2`$. Hence $`\bar K`$ is injective on $`Y/J`$, because $`\bar K^{-1}\bar K=\bar\Lambda^2`$, and it covers $`Y/J`$ by original transversality. This contradicts the strict inequality $`|KN/N|>[G:HN]`$ for every proper nonzero normal cut, including $`HN=G`$. To see the criterion directly, projected translations cover the cosets of $`HN/N`$. Equality makes them a transversal to it and all its conjugates by marked-square invariance, inducing a loop quotient on the blocks. The endpoint $`HN=H`$ contradicts core-freeness; at $`HN=G`$ equality would put all generating translations in $`N`$. Equivalently in a nonsimple folder with nontrivial proper blocks this sharpness would exhibit the block quotient. No normality of $`H`$ and no initial sharp quotient is used.

This complements the [odd-kernel transfer for one specified original involution](../sources/full-socle-completion/odd-normal-involution-collisions.md): there the complement/alignment hypothesis is absent but only involutory collisions transfer. Here the simultaneous alignment transfers the entire marked square. Oddness matters: for a central binary kernel and trivial involution action even the fiber of outside involutions can have multiple singleton conjugacy classes.

### Odd abelian kernels and core avoidance

Let $`V=N`$ be an abelian $`p`$-group for an odd prime $`p`$, and put $`W=H\cap V`$. If a $`\tau`$-stable complement exists, the graph of $`H/W`$ relative to it defines a **nonzero** class in $`H^1(J,V/W)`$. Indeed $`W`$ is $`J`$-invariant; the preimage of $`J`$ modulo $`W`$ is the split extension by $`V/W`$. A principal graph can be conjugated to the pure $`J`$ by a lift in $`V`$, contrary to the first test. The class statement applies separately to each $`\tau`$-stable complement; it does not claim a fixed choice distinguished by the original loop.

If $`D\triangleleft Y`$ is a $`p'`$-subgroup with $`C_V(D)=0`$, then such a complement exists **even if no splitting was assumed and $`D`$ need not be $`\tau`$-stable**. In the preimage of $`D`$, Schur–Zassenhaus supplies a complement $`D_0`$; all are conjugate by $`V`$. By normality and conjugacy, $`G=V N_G(D_0)`$, and $`V\cap N_G(D_0)=C_V(D_0)=0`$, since a vector normalizing this lift must centralize it. Thus $`S_0=N_G(D_0)`$ is a complement to $`V`$. Every complement to $`V`$ can be conjugated by $`V`$ to contain $`D_0`$, then lies in $`N_G(D_0)`$ because $`D\lhd Y`$, hence is equal to $`S_0`$. The finite set of complements has odd size, being a single $`V`$-orbit. The original $`\tau`$ permutes it and fixes one.

For a stable complement, any $`p'`$-subgroup $`B\triangleleft J`$ must have $`(V/W)^B\ne0`$: otherwise average a derivation over $`B`$ to subtract a principal derivation agreeing on $`B`$. Normality then puts its remaining values in $`(V/W)^B=0`$, contrary to nonzero $`H^1`$. Averaging on an abelian $`p`$-group is legitimate because multiplication by $`|B|`$ is invertible.

In particular **$`J`$ contains no normal $`p'`$-subgroup $`D\triangleleft Y`$ with $`C_V(D)=0`$**. Indeed the preceding splitting applies and averaging shows $`(V/W)^D=0`$: if a coset is fixed, averaging a lift gives a $`D`$-fixed representative. This conclusion requires neither an irreducible restriction to $`D`$, a fixed-point-free single element, nor overall odd order. It strengthens the specifically odd irreducible-complement exclusion in [elementary normal layers](../sources/odd-completion/odd-elementary-layer-obstructions.md) in these directions. The existence and conjugacy inputs for Schur–Zassenhaus are recorded in the project's [references](../REFERENCES.md), with abelian normal Hall kernel here.

### The solvable radical of the block-action kernel

Suppose $`V`$ is elementary and irreducible as a $`Y`$-module, $`B_0=\operatorname{Core}_Y(J)`$. Every normal $`p'`$-subgroup of $`Y`$ in $`J`$ acts trivially on $`V`$: its common fixed space is $`Y`$-invariant and cannot be zero by the preceding test. In particular $`O_{p'}(B_0)`$ acts trivially, since it is characteristic in $`B_0\lhd Y`$.

If $`Y`$ acts **faithfully** on $`V`$, then

```math
\operatorname{Rad}(B_0)=1.
```

Indeed $`O_{p'}(B_0)=1`$. Also $`O_p(Y)=1`$, as a normal $`p`$-subgroup has a nonzero fixed vector in defining characteristic, and irreducibility and faithfulness make this subgroup trivial. Hence $`O_p(B_0)=1`$. A nontrivial solvable radical of $`B_0`$ would have nontrivial characteristic Fitting subgroup, one of whose Sylow subgroups is normal in $`B_0`$, contrary to these two conclusions. Thus the kernel of the $`Y`$-action on the $`V`$-orbit blocks has trivial solvable radical. In particular if $`Y`$ is solvable the action is faithful, i.e. $`J`$ is core-free. This is a statement about the action on blocks, **not** a loop quotient. Without the faithfulness and irreducibility assumptions projected cores can survive, as the [full-shadow examples](../sources/odd-completion/odd-uniform-multiplicity-layers.md) illustrate.

In the faithful irreducible case, if $`\operatorname{Rad}(Y)\ne1`$, its Fitting subgroup supplies a nontrivial normal $`p'`$-subgroup of $`Y`$ (there is no normal $`p`$-subgroup). Its common fixed space is zero. Consequently $`G`$ actually splits with a $`\tau`$-stable complement, and the genuine stabilizer has nonzero $`H^1(J,V/W)`$ and nonzero $`(V/W)^{O_{p'}(J)}`$. The requirement that $`J`$ contain a $`p`$-element from the older prime-overlap test is not sufficient.

The [finite control](../sources/code/verify_odd_kernel_core_obstruction.py) uses $`Y=2^2:S_3\cong S_4,\ J=2^2:C_3\cong A_4`$ on the ternary three-dimensional signed-permutation module. The normal Klein four has zero *common* fixed space but each of its nonidentity elements fixes a line; further, $`3\mid|J|`$. All 27 actual derivations on $`J`$ are found principal. The checker explicitly detects a pure marked collision of order three. This is a group/module control, not a simple-loop construction.

## Evidence and boundary

An independent OpenAI model mathematically reviewed this complete argument at source `2756e74daf61aaed60f017ebbf6369026cced801`. Its [independent controls](../sources/code/check_odd_kernel_block_independent.py) include a non-elementary kernel, a non-inversion-stable choice of the quotient subgroup, and the genuinely nonsplit extension from SL₂ over the integers modulo 25. In the last example all 125 lifts of a particular order-five quotient element have order 25: faithful irreducibility alone does not force a complement. The nonsplit example is not asserted to define a Bol loop. This is model review and finite falsification, not human peer review or formal verification. The [tensor exclusion](0100-matched-tensor-radicals.md) illustrates a separate application of actual marked fibers.

[Review provenance, contributions and all runnable controls](../normal-layer-evidence.md).
