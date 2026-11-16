# Three-dimensional linear and unitary canonical groups in odd characteristic

Mira Cult

**Independently reviewed continuation of [classification frontier](../../claims/0010.md).** Let $`q=p^f\ge3`$ be an odd prime power and let $`T`$ be $`\mathop{\mathrm{PSL}}\nolimits_3(q)`$ or $`\mathop{\mathrm{PSU}}\nolimits_3(q)`$. No finite simple nonassociative left Bol loop has canonical left multiplication group $`T`$, for any canonical inverting automorphism $`\tau`$. Both displayed groups are nonabelian simple in this range. The canonical-folder interface is [Claim 0001](../../claims/0001.md), the canonical inversion is [C0007](../foundations/C0007.md) with its scoped C0011 review, and the inner single-class exclusion is [the inner-inversion theorem](../odd-completion/radical-free-inner-inversion.md). The characteristic-two arguments linked below do not review the new odd-characteristic deductions here.

For automorphism structure use Steinberg, *Automorphisms of finite linear groups*, statements 3.2–3.6, printed p. 608, and the twisted $`A_2`$, three-dimensional projective unitary case, §7, printed pp. 613–614, [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16023F257E0F21D57873B1450E9F15E4/S0008414X00010245a.pdf/automorphisms-of-finite-linear-groups.pdf). The displayed statements and unitary identification were inspected; the classification proof was not independently reverified. All uses of that source are conditional on its hypotheses.

## Internal involutions

The scalar center of each determinant-one covering group has odd order dividing 3. Every projective involution consequently has an actual involutory lift: if $`x^2`$ is central, multiply $`x`$ by the unique central square root of $`x^{-2}`$. In odd characteristic the eigenspaces of a nonidentity determinant-one involution have dimensions 2 and 1; in the unitary case they are nondegenerate and mutually orthogonal. Thus every involution is conjugate under the full general linear or unitary group to

```math
u=\mathop{\mathrm{diag}}\nolimits(-1,-1,1). \tag{1}
```

The corresponding class remains one class under the special group: the centralizer on the one-dimensional eigenspace realizes every nonzero determinant, respectively every norm-one determinant, correcting a general conjugator to determinant 1. Passage through the odd center preserves this single projective class. The cited inner-inversion theorem therefore excludes all inner $`\tau`$, including the identity case under its stated repointing and Bruck inputs.

## Linear outer involutions

In $`T=\mathop{\mathrm{PSL}}\nolimits_3(q)`$, the diagonal quotient has odd order dividing 3. The field/graph quotient is the product of the cyclic field group and the graph involution $`\gamma(A)=(A^t)^{-1}`$. An outer involution has image represented by $`\gamma`$, or, if $`q=s^2`$, by the order-two field map $`\sigma:x\mapsto x^s`$ or $`\gamma\sigma`$. Its diagonal component $`d`$ satisfies $`d+\alpha(d)=0`$; for an involution $`\alpha`$ of an odd abelian group, $`\ker(1+\alpha)=\mathop{\mathrm{im}}\nolimits(1-\alpha)`$. Conjugating by an inner-diagonal automorphism therefore reduces to the actual coset $`\alpha T`$.

Each such coset contains one $`T`$-class of involutions. For the graph case, an $`A\in\mathop{\mathrm{SL}}\nolimits_3(q)`$ representing a projective outside involution satisfies $`A=zA^t`$ with $`z`$ central. Transposing gives $`z^2=1`$, and the odd center gives $`z=1`$. The nonsingular symmetric form $`A`$ has determinant 1; symmetric forms of dimension three over a finite odd field are classified by determinant square class, so $`A=B^tB`$ for some $`B\in\mathop{\mathrm{GL}}\nolimits_3(q)`$. Since $`\det B=\pm1`$, an orthogonal reflection changes its sign if necessary, producing $`B\in\mathop{\mathrm{SL}}\nolimits_3(q)`$. The needed form classification has an elementary proof: diagonalize the form. Any nondegenerate binary diagonal form ax²+by² represents 1, since the sets of values ax² and 1−by² each have (q+1)/2 elements and intersect. Split off a vector of norm 1 twice; the remaining one-dimensional coefficient is a square precisely when the original determinant is a square, and then rescale it to 1.

For the field case, the projective square condition is $`A\sigma(A)=zI`$ with $`z`$ in the odd scalar center and fixed by $`\sigma`$. The norm map on this odd center onto its fixed subgroup allows a central rescaling to $`A\sigma(A)=I`$. For completeness, descent in odd characteristic uses a nonzero η with σ(η)=−η: for a semilinear involution F, both x=(v+F(v))/2 and y=(v−F(v))/(2η) are fixed and v=x+ηy. Thus a fixed-space basis spans the whole extension-field space. This semilinear descent (matrix Hilbert 90) gives $`A=B\sigma(B)^{-1}`$. Since $`\det A=1`$, $`\det B\in\mathbb F_s^\times`$; multiplying the fixed-basis matrix $`B`$ on the right by a matrix over $`\mathbb F_s`$ of inverse determinant makes $`B\in\mathop{\mathrm{SL}}\nolimits_3(q)`$. For graph-field, the projective square condition gives $`A=z\sigma(A)^t`$, with $`z\sigma(z)=1`$; central rescaling uses surjectivity of $`c\mapsto c/\sigma(c)`$ onto the norm-one subgroup of the odd center. The resulting nonsingular Hermitian form is congruent to identity; its determinant-one condition makes the congruence determinant norm one, and a unitary isometry of arbitrary norm-one determinant corrects it to 1. These are the same descent and determinant arguments as in [the reviewed linear source](../primitive-completion/radical-free-odd-linear-inversion.md),, with odd-characteristic symmetric forms treated separately above.

## Unitary outer involutions

For $`T=\mathop{\mathrm{PSU}}\nolimits_3(q)`$, Steinberg's unitary case gives an odd diagonal quotient of order dividing 3 and a cyclic field quotient of order $`2f`$. Its unique involution is represented by entrywise conjugation $`\alpha=\bar{\phantom{x}}:x\mapsto x^q`$ on the standard Hermitian space over $`\mathbb F_{q^2}`$. The same odd-diagonal argument reduces every outer involution to the actual coset $`\alpha T`$.

Let $`A\in\mathop{\mathrm{SU}}\nolimits_3(q)`$ and suppose $`A\alpha`$ has projective square 1. Then $`A\bar A=zI`$ for a scalar $`z`$ in the odd special-unitary center. Conjugating and comparing the two product orders gives $`z=\bar z`$; a unitary scalar also has $`\bar z=z^{-1}`$, so $`z^2=1`$ and $`z=1`$. The semilinear involution $`F=A\alpha`$ has a three-dimensional fixed $`\mathbb F_q`$-space $`E`$, whose scalar extension is the whole space. The Hermitian form restricts to a nondegenerate symmetric form on $`E`$. For a fixed-basis matrix $`B`$, $`A=B\bar B^{-1}`$; $`\det A=1`$ gives $`\det B\in\mathbb F_q^\times`$, and the Gram determinant is

```math
\det(\bar B^tB)=N_{\mathbb F_{q^2}/\mathbb F_q}(\det B)=(\det B)^2.
```

Thus this symmetric form has square discriminant and is isometric to the standard fixed-space form. The isometry extends by scalars to a unitary conjugator. Its determinant is $`\pm1`$, and an orthogonal reflection of the standard fixed space corrects the sign while preserving the form and commuting with $`\alpha`$. Hence all involutions in $`\alpha T`$ form one $`T`$-class. This determinant argument is specific to the actual special-unitary coset and does not identify distinct diagonal cosets.

## Marked collision and even-characteristic corollary

In every outer case, the involution $`u`$ in (1) is fixed by the standard $`\alpha`$, so $`\widehat\alpha u`$ is an outside involution in the same actual coset as $`\widehat\alpha`$. Its unique $`T`$-class contains both, and its square contains $`u`$, hence every internal involution. The actual canonical mark is nonempty and contains $`\widehat\alpha^T`$; uniqueness makes it exactly that class. The condition $`H\cap\Lambda^2=1`$ forces $`H`$ to have odd order. But $`|H|=|C_T(\alpha)|`$, and this centralizer contains $`u`$, so it has even order. This contradiction completes the odd-characteristic proof.

Together with the separately reviewed [characteristic-two linear theorem](../primitive-completion/radical-free-odd-linear-inversion.md) and [unitary theorem](../primitive-completion/radical-free-unitary-inversion.md) and its recorded review, this excludes both three-dimensional families for all prime powers. The corollary retains the cited dependencies and does not cover these groups as proper factors of a larger canonical group.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker and an automated checker independently accepted exact source the recorded source revision, conditional on the pinned folder, inversion, inner-repointing/Bruck and automorphism inputs. All checked the unique internal class, odd diagonal cocycles, actual outer cosets, fixed-form discriminants, central rescalings, determinant corrections and marked collision. an automated checker directly inspected Steinberg statements 3.2–3.6 on printed p.608 and the twisted-type discussion in §7; the other two made no fresh primary-source audit. None reverified the external classification proofs. These are model mathematical reviews, with no new computation or formal certification; the scope is these entire canonical groups, not their occurrence as factors.
