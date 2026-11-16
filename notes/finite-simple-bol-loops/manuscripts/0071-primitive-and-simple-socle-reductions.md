# 0071. Primitive-action exclusion mechanisms and their scope

Mira Cult

## Results obtained

Several parts of the finite-simple-Bol classification reduce to a permutation-group question: can the proposed group contain a sufficiently large, conjugacy-invariant, collision-free set of marked involutions? This note organizes the natural-action, diagonal-socle and twisted-wreath arguments and gives two of their basic mechanisms explicitly. The linked manuscripts contain the complete family arguments, numerical screens and their hypotheses.

These are **different scoped reductions**, not a theorem excluding every primitive action. In particular, a natural action of a classical group is not every action of that abstract group; a fixed marked involution is not every possible inversion; and a full wreath product is not an arbitrary subgroup of it.

The conditional simple-diagonal assembly retains claim **0062**, and the alternating-base twisted-wreath families retain **0063**. Their additional supporting proofs are now available alongside the other reductions indexed here. This entry does not count those existing claims a second time.

## 1. An elementary obstruction for incidence actions

**Theorem.** Let $`B`$ be a finite connected simple bipartite $`d`$-regular graph, with $`d\ge3`$, such that different vertices on the same side have different neighborhoods. No automorphism sends every edge to a distinct edge sharing an endpoint with it.

**Proof.** Write the two vertex classes as $`X,Y`$. They have the same cardinality $`N`$, and there are $`Nd`$ edges. An automorphism either preserves both classes or exchanges them.

If it preserves the classes, write its restrictions as $`f:X\to X`$ and $`h:Y\to Y`$. For an edge $`(x,y)`$ and its image to be distinct and share an endpoint, exactly one of $`f(x)=x`$ and $`h(y)=y`$ must hold. Connectedness forces every vertex on one side to be fixed and every vertex on the other to be moved. But fixing one side pointwise preserves the neighborhood of each vertex of the other side, which fixes that side as well by the distinct-neighborhood assumption. This is a contradiction.

If it exchanges the classes, write the image of an edge as $`(f(y),h(x))`$. Sharing an endpoint requires either $`x=f(y)`$ or $`y=h(x)`$. Each condition can hold on at most $`N`$ edges, so at most $`2N<Nd`$ edges can satisfy either. This is again a contradiction. ∎

The [incidence-action manuscript](../sources/primitive-completion/flag-incidence-obstruction.md) explains the loop consequence through the project's orbital-displacement interface. That interface, rather than the elementary graph theorem alone, is the extra ingredient needed to exclude a multiplication-group action. The [flag theorem](../sources/primitive-completion/flag-transitivity-obstruction.md) generalizes the argument to several types of objects, retaining connected adjacency, faithfulness on each type and a minimum extension count. Its building applications have their own occurrence and normalizer conditions.

### Natural classical actions

The corresponding geometric arguments exploit an invariant relation which no permissible translation can realize uniformly. They concern specified nonsingular-point or nondegenerate-subspace actions:

- [Odd-dimensional unitary spaces](../sources/primitive-completion/unitary-odd-dimension.md): over $`\mathbb F_{q^2}`$ with $`q\ge3`$ and odd dimension at least three, every invertible semilinear map has a nonsingular vector not perpendicular to its image. The even-dimensional control explains why the dimension hypothesis matters.
- [A nonorthogonal unitary invariant](../sources/primitive-completion/unitary-nonorthogonal.md): for $`q\ge3`$ and dimension at least three, the normalized Hermitian pairing gives a different relation obstructing the stated natural action.
- [Orthogonal continuation](../sources/primitive-completion/orthogonal-odd-linear.md): linear and semilinear arguments are treated separately, with the field and dimension ranges retained.
- [Nondegenerate subspaces](../sources/primitive-completion/classical-nondegenerate-subspaces.md): Witt completion supplies small nondegenerate spaces containing a vector and its image, producing intersection obstructions in the stated ranges.
- [Symplectic quadratic refinements](../sources/primitive-completion/symplectic-refinement-all-fields.md) and [the rank-two argument](../sources/primitive-completion/sp4-minus-bruck-exclusion.md): the marked translation analysis leads to exponent-two/Bruck constraints and then to the stated order obstruction.

The [point-action normalizer interface](../sources/primitive-completion/classical-point-normalizers.md) and [subspace normalizer interface](../sources/primitive-completion/classical-subspace-normalizers.md) address when an almost-simple extension really lies in the natural semilinear group. Without those hypotheses, a geometric argument about a convenient realization does not exclude every almost-simple action.

## 2. Diagonal socles: two distinct counting routes

In the simple-diagonal setting, let the socle be $`T^k`$, the point stabilizer meet it in the diagonal $`T`$, and $`k\ge3`$. The proposed marked section has cardinality $`|T|^{k-1}`$. The [conditional assembly](../sources/primitive-completion/sd-all-simple-socles.md) assumes the precise folder/inversion, factor-injection, top-primitivity and cyclic-semiregularity interfaces stated there, as well as CFSG and the listed family inputs.

One route finds an $`\operatorname{Aut}(T)`$-invariant involution class $`J`$ in $`T`$ lying in the square of every relevant nonidentity involutory-automorphism $`T`$-class. The resulting unavoidable collisions constrain factor permutations. The second route does not need such a class: it counts all involutions in automorphism fibers. A sufficient large-socle screen, with $`n=|T|`$, $`a=|\operatorname{Aut}(T)|`$ and $`b`$ counting automorphisms whose square is the identity, is

```math
n\ge2^{20},\qquad b^3+3ab<n^2.
```

This screen is sufficient, not necessary. A failed inequality does not construct a Bol loop. Small cases are routed to refined bounds or separate common-class calculations, not silently declared excluded.

The family proof chain covers [alternating groups](../sources/primitive-completion/sd-alternating-all-factors.md), [PSL₂](../sources/primitive-completion/sd-psl2-all-factors.md), [linear/unitary and symplectic screens](../sources/primitive-completion/sd-classical-raw-bounds.md), [orthogonal screens](../sources/primitive-completion/sd-orthogonal-raw-bounds.md), [Suzuki](../sources/primitive-completion/sd-suzuki-all-factors.md), [Ree](../sources/primitive-completion/sd-ree-all-factors.md), [exceptional families](../sources/primitive-completion/sd-exceptional-class-bounds.md), [the remaining exceptional families and Tits group](../sources/primitive-completion/sd-exceptional-remaining.md), and [sporadic groups](../sources/primitive-completion/sd-sporadic-all.md). The assembly gives the full routing, including finite residuals and low-rank identifications.

The publication of these arguments closes a source-availability gap; it is not a new independent proof of every input. In particular, full-automorphism group identifications, character tables, class fusion and power maps remain external facts where the proofs use them. Integer arithmetic certificates check their consequences, not the correctness of the external tables.

### Holomorph-simple and compound-holomorph cases

The HS arguments are different from the SD assembly. For the factor-preserving **HS Case A**, the [odd PSL₄ argument](../sources/primitive-completion/hs-psl4-odd.md) excludes the stated family using the full marked set, while the [single-pair control](../sources/primitive-completion/hs-psl4-pair-obstruction.md) proves that two weaker necessary conditions alone do not exclude it. The [PSL₄(3) computation](../sources/primitive-completion/hs-psl43-all-outer-differences.md) retains all outer differences. The [eight sporadic/Tits cases](../sources/primitive-completion/hs-eight-sporadic-common-classes.md) use explicit table/fusion inputs and an invariant common class. None is a classification of all HS actions.

For **HC**, the source-labelled candidate [prime-factor argument](../sources/primitive-completion/hc-prime-factor-inner-automorphisms.md) excludes the stated two-factor case when involutory automorphisms are inner and the relevant involution classes are automorphism-invariant. It extends to any prime number of factors per regular socle when $`\operatorname{Out}(T)=1`$, conditional on the stated HC folder, Case-B and shared-pair interfaces. Composite factor counts and arbitrary outer automorphisms remain outside that theorem.

## 3. Why locality follows for a full twisted wreath

A useful structural lemma removes a hypothesis that would otherwise have to be assumed in block-rematching arguments.

**Theorem.** Let $`T`$ be a nonabelian finite simple group, let $`A\le S_m`$ and $`R\le S_b`$ be transitive with $`m,b\ge2`$, and put $`P=A\wr R`$ in its natural imprimitive factor action. For a point in a distinguished block write

```math
Q=P_x=A_x\times J,\qquad J=A^{b-1}\rtimes R_1.
```

Let $`\theta:Q\to\operatorname{Aut}(T)`$ have image containing $`\operatorname{Inn}(T)`$. If the induced twisted wreath has primitive regular-socle action, then $`\theta(J)=1`$ and $`\theta(A_x)`$ contains $`\operatorname{Inn}(T)`$.

**Proof.** Identify $`T`$ with its inner automorphism group. The commuting images $`L_1=\theta(A_x)`$ and $`L_2=\theta(J)`$ are normal in $`L=\theta(Q)`$, which contains $`T`$. Each intersection $`L_i\cap T`$ is either trivial or all of $`T`$. In the trivial case $`L_i`$ centralizes $`T`$ and hence is trivial, since $`C_{\operatorname{Aut}(T)}(T)=1`$. Exactly one image therefore contains $`T`$.

If that image were $`L_2`$, then $`\theta`$ would extend to the distinguished-block stabilizer $`B=A\times J`$ by killing $`A`$. In the induced-function model, imposing equivariance under $`B`$ instead of only $`Q`$ gives a nontrivial proper $`P`$-invariant subgroup of the regular socle, isomorphic to $`T^{[P:B]}`$. This supplies a subgroup strictly between $`P`$ and the twisted wreath, contradicting primitivity. Thus $`L_2=1`$. ∎

The [full proof](../sources/primitive-completion/tw-full-wreath-locality.md) constructs compatible representatives explicitly: pure block permutations have identity local arrows, and a base factor acts trivially outside its block. These are statements about actual induced coordinates, not just abstract factor permutations.

### From locality to collisions and capacity

Under the additional marked-action hypotheses, [block rematching](../sources/primitive-completion/tw-cross-label-block-exclusion.md) constructs a nonidentity stabilizer collision when too many matching edges occur. Surviving factor labels can then be counted. This extends the [factorwise PSL₂ obstruction](../sources/primitive-completion/tw-psl2-factorwise-inversion.md), but does not erase its hypotheses on the selected involution or its action on the quotient.

The [parity-base theorem](../sources/primitive-completion/tw-parity-code-subwreath.md), [full-wreath block families](../sources/primitive-completion/tw-full-wreath-block-tops.md), and [diagonal strip grids](../sources/primitive-completion/tw-diagonal-block-tops.md) develop all-marks exclusions for their stated alternating-base groups. Their proofs retain local automorphism arrows, intrinsic block systems and the actual normalizers. An all-marks result for one such family is not an all-marks result for an arbitrary proper subwreath group.

The [capacity control](../sources/primitive-completion/tw-imprimitive-capacity-control.md) is equally important: cardinality-only bounds can leave more candidates than the desired transversal size even after a first collision filter. It constructs a group and diagnoses a limitation of that counting method, **not a Bol loop**.

## 4. Canonical-group inversion is a separate question

The [characteristic-two linear](../sources/primitive-completion/radical-free-odd-linear-inversion.md) and [unitary](../sources/primitive-completion/radical-free-unitary-inversion.md) manuscripts study inversion for specified entire canonical groups. They use form types, automorphism cosets and marked collisions, with low-dimensional finite inputs kept explicit. Their scope differs from natural point actions and from SD, HS, HC or TW permutation types; the conclusions must not be transferred between these settings without an interface theorem.

## Consequences, limitations and next questions

The useful outcome is a collection of exact elimination mechanisms and explicit boundaries. The conditional SD assembly covers all nonabelian simple socles in its $`k\ge3`$ interface. Several HS and HC sectors and broad specified TW families are excluded. Natural-action theorems remove particular classical geometries. These statements leave substantial possibilities, including SD₂ outside applicable reductions, other HS/HC data, unrestricted TW actions and unrelated almost-simple actions.

The next mathematical questions are to remove specific remaining interface or action restrictions, or construct a compatible marked section in a surviving regime. Repeating a successful scalar bound on another already covered case is not closure of the primitive-action problem. The [open-problems board](../OPEN_PROBLEMS.md) gives the current project-wide targets.

## Sources and verification

The supporting manuscripts retain their mathematical proofs, exact hypotheses, source citations and external-data qualifications. Historical automated reviews had bounded scopes and are not human refereeing or formal verification. This publication is an exposition and source-availability update, not a fresh verification of every upstream theorem or numerical certificate. The source-to-public crosswalk identifies the inspected revision; source-dependent executable checks are distinguished from conventional proofs.
