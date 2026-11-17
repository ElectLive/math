# Binary symplectic full socles and direct geometric action obstructions

**Mira Cult**

## Binary full-socle theorem

Under the canonical, primitive almost-simple, subgroup-classification and geometric inputs of the proofs, no finite simple proper left Bol loop has full multiplication socle Sp₂ₘ(2), for any m≥3. The two smaller binary symplectic groups themselves are not nonabelian simple.

There is also a positive operation classification inside a specified action: on either full orbit of quadratic refinements of a binary symplectic space of dimension 2m, m≥3, a loop whose left and right translations lie in the induced symplectic group must be the Paige loop of order 120. This occurs only for m=4 on the minus orbit. Conversely that Paige loop realizes the action. The forward theorem requires only a loop and allows its translation-generated group to be proper in the ambient symplectic group. Thus it excludes both actions for the proper-Bol target without excluding the Paige loop itself.

## Why invariant relations obstruct translations

An invariant relation on ordered pairs of loop points, if nonempty, contains some pair (e,y) after transport. Every left translation sends it to (x,x·y). Therefore the right translation by y sends every point into that relation. To exclude a proposed action, it suffices to construct a nonempty invariant relation for which every ambient group element has at least one point whose displacement lies outside the relation.

The [high-rank proof](../sources/full-socle-completion/binary-symplectic-extension-spreads.md) applies maximal factorizations to the original point stabilizer. Subspace and decomposition actions are excluded geometrically. Quadratic-refinement actions use the operation theorem. The remaining extension-field actions map equivariantly onto orbits of spreads of isotropic subspaces. Separated spreads make a suitable relation nonempty, while nearly invariant isotropic subspaces prevent universal displacement. This proves all ranks at least five. The [small-rank proof](../sources/full-socle-completion/binary-symplectic-small-full-socles.md) handles Sp₆(2) and Sp₈(2), using complete maximal-subgroup inputs, orbital witnesses and exact plane/class certificates in their stated scopes.

## Rigidity of the refinement multiplication

In the [operation proof](../sources/full-socle-completion/binary-refinement-loop-rigidity.md), choose the identity quadratic form q. Refinements of the same type are labeled by the singular vectors of q. Left and right translations extend affinely, and interpolation forces the multiplication to have the form F(x,y)=x+y+μ(x,y), with μ bilinear. A degree-two vanishing lemma gives

```math
q(F(x,y))=q(x)+q(y)+q(x)q(y).
```

Polarization gives both adjoint matrix identities needed for the dimension argument; neither reverse identity nor characteristic-two coefficient independence is assumed. The resulting representation and composition-algebra analysis force the stated dimension and Paige operation. The linked source supplies the full argument and converse.

## Larger even fields and the correction boundary

For q even, the [original-stabilizer theorem](../sources/full-socle-completion/symplectic-even-maximal-stabilizers.md) bounds the number of nonabelian composition factors of the actual identity stabilizer by one. Its direct geometric proof avoids the historically contested many-factor induction.

The [field-action theorem](../sources/full-socle-completion/even-symplectic-field-actions.md) excludes actual subfield stabilizers Sp₂ₘ(r), q=rˢ, s≥2; quadratic extension-field stabilizers Sp₂ₐ(q²).2 for q≥4 and a≥3; and the stated odd-prime extension cases with a≥2 and gcd(a,s)=1, or a decomposable into such block sizes. These are not exhaustive exclusions for larger fields. Containment in a convenient maximal overfactor does not identify that overfactor with the original stabilizer.

The [many-factor source reduction](../sources/full-socle-completion/symplectic-many-factor-stabilizers.md) remains globally unverified and its earlier global acceptances were withdrawn. The corrected Sp₆(4) omission and the separate conflict within the source induction are not erased by these direct action results. All independent model reviews and finite certificates retain their exact local scopes; unrestricted classification remains open.
