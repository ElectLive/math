# Transitive odd pure tops over one-mod-four PSL₂ fields

Mira Cult

**Independently reviewed under pinned inputs**, continuing [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let $`q`$ be an odd prime power with $`q\equiv1\pmod4`$, let $`T=\mathop{\mathrm{PSL}}\nolimits_2(q)`$, let $`Q`$ be a finite odd group acting faithfully and transitively by pure permutations on a nonempty set $`\Omega`$, and put $`G=T^\Omega\rtimes Q`$. No faithful generated canonical folder of a finite simple nonassociative left Bol loop has canonical left multiplication group $`G`$. Neither $`H\to Q`$ surjectivity nor nilpotence of $`Q`$ is assumed. This concerns the entire canonical left multiplication group, not the full multiplication group or arbitrary outer lifts.

The canonical folder, selected-mark class sum and original normal-subloop interfaces are [C0001](../../claims/0001.md) and [C0007](../foundations/C0007.md) with its scoped review. The $`q=5`$ case is the independently reviewed [transitive $`A_5`$ odd-top theorem](radical-free-a5-odd-top-surjectivity.md#singleton-factors-exclude-every-transitive-odd-top). For other fields, the local subgroup, automorphism, character and class-square inputs are [the fixed-factor source](radical-free-fixed-factors.md), its $`A_6`$ section, and its assembly. The original subgroup and semilinear-source qualifications there remain in force; no new primary-source audit is claimed. The relevant primary subgroup locator recorded there is Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Appendix Theorem A.1 and Lemmas A.2–A.3, printed pp. 1354–1355. The preceding input reviews do not review the new transitive-top deductions below.

## Common notation and direct sums

Put $`N=T^\Omega`$, $`H_0=H\cap N`$, and $`H_Q=HN/N\le Q`$. Write $`t=[Q:H_Q]`$. Let $`\widehat\tau`$ denote the formal outside involution and $`\Lambda=\widehat\tau K`$ the actual marked set. If $`\theta`$ is the induced involution of $`Q`$, every outside top involution $`x\theta`$ is $`Q`$-conjugate to $`\theta`$: $`\theta(x)=x^{-1}`$, and the odd-order square root of $`x`$ gives the conjugator. Put $`k=[Q:C_Q(\theta)]`$. Every selected mark has a top involution in this one class. Its induced involution on the odd transitive set $`\Omega`$ has $`f\ge1`$ fixed coordinates and $`c`$ swapped pairs, with

```math
|\Omega|=2c+f. \tag{1}
```

The numbers $`c,f`$ are independent of the selected mark. If the local outer labels of $`\tau`$ are $`[\alpha_i]`$, normalization of the pure $`Q`$-action shows $`[\alpha_{xi}]=[\alpha_i]`$ for all $`x\in Q`$. Transitivity therefore makes the local outer label constant on $`\Omega`$, including at every fixed coordinate of every selected mark.

For a coordinate $`i`$, let $`L_i=\pi_i(H_0)`$, and let $`J_i`$ be the image on $`T_i`$ of the actual $`H`$-stabilizer of $`i`$. Then $`L_i\triangleleft J_i`$. If $`L_i\ne1`$ is proper, $`J_i`$ is proper; if $`L_i=1`$, $`J_i`$ is an odd quotient of a subgroup of $`Q`$. On the direct sum of one nontrivial irreducible $`T`$-module at each coordinate, the $`N`$-constituents are distinct and $`Q`$ permutes them transitively; hence this is an irreducible $`G`$-module. A $`J_i`$-fixed vector transports over the **one actual $`H`$-orbit** of $`i`$; put zero on all other $`H`$-orbits. Thus it gives an $`H`$-fixed vector without any surjectivity assumption. If every selected mark has trace of one nonzero sign on a $`\tau`$-stable such module, its $`G`$-invariant marked class sum is a nonzero scalar, contradicting the original transversal identity on that fixed vector.

## Full strips and the singleton count

Suppose $`L_i=T`$ at every coordinate. Elementary subdirect-product induction makes $`H_0`$ a product of disjoint full twisted $`T`$-strips. If all strips have size at least two, let $`V`$ be the deleted projective-line permutation module of dimension $`q`$. The quadratic and cubic power sums on its sum-zero space are nonzero and $`\mathop{\mathrm{Aut}}\nolimits(T)`$-invariant; products give nonzero symmetric invariant tensors in every degree at least two. Transporting these tensors coherently gives an actual $`H`$-fixed vector in the irreducible $`N`$-tensor $`\bigotimes_{i\in\Omega}V_i`$, even when $`H`$ permutes and twists strips. For inner/id local label, each fixed mark contributes trace $`q`$ or $`1`$, and each swapped pair contributes $`q`$, so every marked trace is positive. For the nonexceptional fields treated below the same tensor also has a constant nonzero trace sign for either outer label: the fixed-coordinate sign is determined by the constant outer coset, and every swapped pair is positive. The class-sum contradiction therefore forces a singleton $`T_i\le H_0`$ in these situations.

For a singleton, suppose some selected mark has a nonidentity local automorphism at a fixed coordinate. Conjugate the mark by a pure element of $`Q`$ moving that coordinate to $`i`$; $`\Lambda`$ is $`G`$-invariant. Choose $`a\in T_i`$ moved by the local automorphism. Then $`\lambda^a\lambda`$ is a nonidentity element of $`T_i\cap\Lambda^2\subseteq H\cap\Lambda^2`$, impossible. Thus every selected fixed-coordinate local mark is identity. In the nonexceptional outer cases this already contradicts the nontrivial outer label.

In the inner/id case, above each selected top involution the marks form the unique $`N`$-class with identity fixed labels and have size $`|T|^c`$. Therefore $`|\Lambda|=k|T|^c`$. If $`s`$ is the number of full strips, original transversality gives

```math
|T|^s=|H_0|=|T|^{c+f}\frac{t}{k}. \tag{2}
```

Both $`t`$ and $`k`$ are odd, while $`|T|`$ is even, so $`s=c+f`$ and $`t=k`$. If $`Q=1`$, transitivity leaves a singleton factor normal in $`G`$ inside $`H`$, contradicting corefreeness. If $`Q\ne1`$ and $`H_Q\ne Q`$, the $`K`$-image in $`G/N`$ has exactly $`k=t`$ elements and covers the $`H_Q`$-cosets, contrary to the strict original normal-subloop criterion. If $`H_Q=Q`$, then $`k=1`$; all $`K`$-elements have trivial $`Q`$-image, contradicting $`G=\langle K\rangle`$. No quotient-folder assumption is used.

## Nonexceptional fields

For $`q\notin\{5,9,29\}`$, the reviewed one-mod-four subgroup calculation says every proper subgroup is intransitive on $`\mathbb P^1(q)`$, and hence fixes a vector of $`V`$. Its fixed-coordinate traces on selected marks are $`q`$ or $`1`$ in the inner/id coset, $`-1`$ in the diagonal outer coset, and $`\sqrt q>0`$ in the field outer coset. The remaining diagonal-field coset has no involutions. The direct-sum argument forces every $`J_i=T`$, and hence every $`L_i=T`$. The preceding singleton and count exclude all labels. These local facts and the natural $`\mathop{\mathrm{Aut}}\nolimits(T)`$-extension are precisely the inputs of [the reviewed odd-top tensor theorem](radical-free-psl2-odd-top-tensors.md).

## The $`q=29`$ inner label

For $`q=29`$, the reviewed proper-subgroup calculation leaves only $`A_5`$ as a possible proper $`J_i`$ without a $`V`$-fixed vector. The direct sum therefore gives $`J_i\in\{A_5,T\}`$, and normality plus the odd $`L_i=1`$ case gives $`L_i=J_i`$. Suppose the common outer label is inner/id and some $`J_i=A_5`$. Let $`\rho=\mathop{\mathrm{Ind}}\nolimits_{A_5}^{T}1`$, a degree-203 character, and write $`\rho-1=\sum m_\psi\psi`$. By Frobenius reciprocity, every nontrivial constituent $`\psi`$ has an $`A_5`$-fixed vector. For each $`\psi`$, its coordinate direct sum is $`G`$-irreducible and inner-$`\tau`$-stable, and it has an $`H`$-fixed vector transported over the one $`H`$-orbit of $`i`$. Thus the selected-mark class sum acts as zero on every such summand, including its multiplicity.

However $`|C_T(u)|=28`$ for an inner involution and $`A_5`$ has 15 involutions, so $`\rho(u)=28\cdot15/60=7`$. Hence $`(\rho-1)(1)=202`$ and $`(\rho-1)(u)=6`$. The sum of the marked traces over all constituents with multiplicity is strictly positive: each fixed block contributes 202 or 6. This contradiction avoids any assertion that an individual constituent has one trace sign. Thus all $`L_i=T`$, and the inner/id singleton argument applies.

## The $`q=9`$ inner label

Here $`T\cong A_6`$. The reviewed $`A_6`$ calculation says every proper subgroup except $`A_5`$ fixes a vector of the degree-nine deleted projective module. The same direct-sum reduction gives $`J_i\in\{A_5,T\}`$ and $`L_i=J_i`$. For an $`A_5`$ coordinate, its index-six coset action gives a real irreducible degree-five deleted character with an $`A_5`$-fixed vector and trace 1 on the unique inner involution class. Transport this character type by the pure $`Q`$-action, and a fixed vector only along the chosen $`H`$-orbit. Inner/id local $`\tau`$ preserves the representation, and every marked fixed-block trace is 5 or 1. The direct-sum class-sum contradiction excludes a proper $`A_5`$ coordinate. Hence all $`L_i=T`$, and the inner/id singleton argument applies. This does not assert that arbitrary correlated $`A_5`$ residuals have only coordinatewise tensor invariants.

## Outer labels for $`q=9,29`$

For $`q=29`$, the only outer involution coset is diagonal; its unique class has size $`406`$, and its square contains the unique inner involution class. Since $`|T|_2=4`$, original transversality gives

```math
|H_0|_2=2^{2c+f}>4^c. \tag{3}
```

For $`q=9`$, $`|T|_2=8`$. The reviewed $`A_6`$ source gives one diagonal-outer class of size 36, two field-outer classes of size 15 each, and no involutions in the fourth outer coset. The square of **each** selected local outer class contains the unique inner involution class. For diagonal label,

```math
|H_0|_2=2^{3c+f}>8^c. \tag{4}
```

For field label, let $`W`$ be the number of selected local field-class patterns at the $`f`$ fixed coordinates above one top involution. $`Q`$-conjugacy gives the same count above every selected top involution, and $`1\le W\le2^f`$. Thus

```math
|H_0|_2=2^{3c+3f-v_2(W)}>8^c. \tag{5}
```

The absent fourth coset cannot occur at a fixed coordinate.

Let $`P\in\mathop{\mathrm{Syl}}\nolimits_2(H_0)`$. On each swapped pair impose equality of identity/nonidentity support. Expanding these indicators modulo two gives terms imposing identity on at most one coordinate per pair. Each corresponding projection of $`P`$ has target 2-part at most $`|T|_2^c`$, strictly less than $`|P|`$ by (3)–(5). Its kernel is therefore a nontrivial finite 2-group, and the number of its involutions **including identity** is even: pair non-involutions with their inverses. Thus the number of matched-support involutions in $`P`$ is even, and some nonidentity one exists. At paired coordinates it gives conjugate involutions or identities; at fixed coordinates its value is in the square of the selected local outer class. Hence it is an actual nonidentity element of $`H\cap\Lambda^2`$, a contradiction. This argument does not assume $`P`$ abelian or form a quotient folder.

The $`q=5`$ input and the cases above complete the transitive pure odd-top theorem. Other tops, non-pure factor actions, multiple $`Q`$-orbits and unrestricted finite simple Bol loops remain outside scope.

## Independent mathematical review

Four separate automated mathematical reviews accepted the complete manuscript, conditional on its pinned local subgroup, character, class-square and canonical-folder inputs. They checked the actual one-H-orbit direct sums, coherent symmetric full-strip tensors, singleton collision and identity fixed-mark counts, the q=29 induced-character argument with all spherical constituents and multiplicities, q=9 inner and outer cases, and the class-pattern/parity argument for nonabelian Sylow-2 subgroups. They did not independently reprove every upstream input, run computations or conduct a fresh primary-source audit. These are model mathematical reviews, not human/formal certification or GitHub approval. The theorem concerns the entire stated canonical pure transitive odd-top group, not arbitrary composition factors or the full multiplication group.

