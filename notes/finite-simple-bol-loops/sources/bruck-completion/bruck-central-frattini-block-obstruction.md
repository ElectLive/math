# A local-factor obstruction with central Frattini subgroup

**Theorem with scoped independent reviews below, conditional on the cited inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md), without a new permanent ID. Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative right Bruck loop of 2-power exponent. Set $`P=O_2(G)`$, $`\Phi=\Phi(P)`$, $`V=P/\Phi`$, $`W=H\cap P`$, and $`U=W\Phi/\Phi`$. Assume $`\Phi\le Z(G)`$. The central-Frattini envelope inputs give $`\Phi`$ elementary, $`W\cap\Phi=1`$, $`W\Phi`$ elementary, and $`\tau`$ fixing $`W\Phi`$ pointwise. Let $`\pi:G\to A=\prod_j A_j`$, $`A_j=\mathrm{PGL}_2(q_j)`$ as in Baumeister–Stein, with $`\pi(H)=\prod_j B_j`$ for the point Borels. Fix one singleton factor $`A_i`$, put $`q=q_i`$, and let $`T=\langle t\rangle`$ be a prescribed nonsplit outer involution with odd $`R\le C_{A_i}(t)`$.

Assume on the restricted $`A_i`$-module $`V`$:

1. $`H^1(A_i,V)=H^2(A_i,V)=0`$.
2. $`V|_{B_i}`$ is semisimple and projective, and $`V^{B_i}=0`$.
3. There is one fixed odd prime dividing every nonzero $`R`$-orbit size in $`H^1(T,V)`$.

Then the envelope cannot exist, conditional on the cited envelope, singleton-fiber, marked-invariance and central-extension-detector inputs. No global complement, global triviality of $`\tau`$, or separately assumed vanishing of the Frattini core is needed. The test is vacuous at condition 3 when the cohomology space is zero. This extends the [elementary-radical local-factor theorem](bruck-elementary-block-obstruction.md), with scoped independent reviews at the recorded source revision. It uses the [central extension detector](bruck-elementary-product-constraints.md#central-extension-detector-and-invariant-functionals), reviewed at the recorded source revision, and the [central-Frattini inputs](bruck-central-frattini-constraints.md), reviewed at the recorded source revision. The Baumeister–Stein v1 quotient, marked-set and singleton-fiber locators are those in the elementary local-factor theorem; its reviewed source interfaces apply here. The present extension has the separate exact-revision reviews below.

## Normalize only the local shadow

Set $`G_i=\pi^{-1}(A_i)`$ and $`H_i=H\cap\pi^{-1}(B_i)`$, with $`A_i,B_i`$ embedded at singleton support. As $`\pi(H)=\prod B_j`$, the map $`H_i\to B_i`$ is onto with kernel $`W`$. The local shadow extension $`1\to V\to G_i/\Phi\to A_i\to1`$ splits by the $`H^2`$ hypothesis. Semisimplicity and projectivity of $`V|_{B_i}`$ make its submodule $`U`$ and quotient $`V/U`$ projective. The image of $`H_i`$ in $`(\pi^{-1}(B_i)/\Phi)/U`$ complements $`V/U`$; vanishing of $`H^1(B_i,V/U)`$ conjugates the local shadow complement by a vector of $`V`$ so that

```math
G_i/\Phi=V\rtimes A_i,\qquad H_i\Phi/\Phi=U\rtimes B_i.\tag{1}
```

The automorphism $`\tau`$ fixes $`V`$ and induces the identity on $`A_i`$. Its difference on this local shadow complement is a derivation $`\delta_i:A_i\to V`$ vanishing on $`B_i`$. By $`H^1(A_i,V)=0`$, $`\delta_i(a)=(1+a)v`$, and $`v\in V^{B_i}=0`$, so $`\tau`$ is the identity on $`G_i/\Phi`$.

## Lift local triviality of inversion

Define $`\epsilon(g)=\tau(g)g^{-1}\in\Phi`$ for $`g\in G_i`$. Centrality of $`\Phi`$ makes $`\epsilon:G_i\to\Phi`$ a homomorphism. Because $`\tau`$ fixes $`\Phi`$, the restriction $`\epsilon|_P`$ factors through $`V`$ and is $`A_i`$-invariant. Condition 2 gives $`\mathop{\mathrm{Hom}}\nolimits_{B_i}(V,\mathbf1)=0`$: a semisimple module with no trivial submodule has no trivial quotient. Hence $`\mathop{\mathrm{Hom}}\nolimits_{A_i}(V,\Phi)=0`$, so $`\epsilon|_P=0`$. Thus $`\epsilon`$ factors through a homomorphism $`A_i\to\Phi`$. It vanishes on $`B_i`$, since $`H_i`$ surjects onto $`B_i`$ and $`\tau`$ fixes $`H_i`$. The Borel surjects onto $`A_i^{ab}\cong C_2`$ via determinant square class, so $`\epsilon=0`$. Therefore

```math
\tau|_{G_i}=1.\tag{2}
```

The marked set $`\widehat\tau K`$ is $`G`$-conjugacy invariant; (2) consequently makes $`K`$ invariant under ordinary conjugation by $`G_i`$, with no assertion about conjugation by all of $`G`$.

## Find a local central-extension splitting

Use the original singleton-support fiber $`K_t=\{k\in K:\pi(k)=t\}`$. The source fiber theorem gives it positive power-of-two cardinality. Every $`k\in K_t`$ belongs to $`G_i`$ and is an involution by (2) and $`\tau(k)=k^{-1}`$. Its shadow in (1) is $`xt`$ with $`x\in\ker(1+t|V)`$, defining a label in $`H^1(T,V)`$. A lift in $`G_i`$ of each pure shadow element of $`R`$ conjugates $`K_t`$ to itself and acts on these labels by $`R`$. Hence all selected label fibers in an $`R`$-orbit have equal cardinality. Condition 3 and the power-of-two fiber size force a zero label. Conjugating a selected element by a suitable element of $`P`$ then yields an involution $`k\in K_t`$ whose shadow is pure $`t`$.

Let $`E`$ be the inverse image in $`G_i`$ of the pure complement $`A_i\le G_i/\Phi`$. Then

```math
1\to\Phi\to E\to A_i\to1\tag{3}
```

is central and contains $`k`$, an involution over $`t`$. Moreover $`E\cap H_i`$ maps isomorphically onto $`B_i`$: (1) makes it surjective, and its kernel is $`H_i\cap\Phi=W\cap\Phi=1`$. Thus (3) splits over the **actual** Borel subgroup $`E\cap H_i`$.

For every linear functional $`\ell:\Phi\to C_2`$, push (3) out along $`\ell`$. Its actual Borel complement and the image of $`k`$ satisfy the reviewed central $`C_2`$-extension detector, so the pushout splits. The extension class in $`H^2(A_i,\Phi)\cong H^2(A_i,C_2)\otimes_{\mathbb F_2}\Phi`$ has zero image under every functional; it is therefore zero. Choose a complement $`A_i^*\le E`$. Its Borel subgroup and the actual $`E\cap H_i`$ differ by the graph of a homomorphism $`B_i\to\Phi`$. Every such homomorphism extends to $`A_i`$: the odd unipotent subgroup maps trivially, and the cyclic $`q-1`$ torus maps into the elementary 2-group $`\Phi`$, so it factors through the determinant-square-class character. Twisting the chosen complement by this extension yields

```math
E=\Phi\times A_i^*,\qquad B_i^*:=A_i^*\cap H_i\cong B_i.\tag{4}
```

This argument needs only the local detector and does not construct a global product complement.

## Pure-class collision

The selected element $`k\in E`$ over $`t`$ has the form $`z t^*`$, where $`z\in\Phi`$ and $`t^*\in A_i^*`$ is the lift of $`t`$. Since $`z`$ is central and $`K`$ is invariant under $`G_i`$, every $`z(t^*)^a`$ with $`a\in A_i^*`$ lies in $`K`$. The outer involution class in $`A_i`$ has $`q(q-1)/2`$ elements and none belongs to the point Borel. There are only $`q`$ other Borel cosets, and $`q(q-1)/2>q`$ for $`q\ge5`$. Thus two distinct elements of this class have the same $`B_i^*`$-coset; multiplying both by the same central $`z`$ preserves their equal $`H`$-coset. This violates the transversal property of $`K`$.

The proof and its application of the original fiber and detector inputs have the exact-revision reviews below. It does not by itself prove the three module conditions for any specified $`V`$, classify loops, or cover noncentral $`\Phi`$.

## Block-support consequences

The separately reviewed finite-field block lemma and module consequences in [the elementary argument](bruck-elementary-block-obstruction.md#consequences-for-elementary-radical-block-support) apply to the binary shadow V=P/Φ, independent of whether P itself is elementary. Consequently the preceding proof extends all its necessary restrictions to central-Frattini radicals: for each quotient factor A_i, if V|A_i has no principal-block summand, it must have nonprojective simple summands whose associated odd-torus character orders have greatest common divisor one. A restriction supported on one nonprincipal block is excluded even with arbitrary projective multiplicities. For q_i=5,9,17 a principal-block summand is required; at q_i=257, absence of a principal component forces nonprojective summands of both character orders 3 and 43. These conclusions use the same character, cyclic-defect, descent and standard algebra inputs as the reviewed block lemma.

The new extension concerns actual Frattini shadow data and the original selected fiber; it does not infer a quotient loop from G/Φ. It does not establish centrality of Φ in general or sufficiency of the remaining block patterns. No new computation is used or claimed. The theorem and these consequences have the independent mathematical reviews below.

## Independent review

Independent checks an independent check and an independent check independently accepted this central-Frattini extension and its block-support consequences at exact source the recorded source revision, conditional on the pinned Bruck-envelope, central-Frattini, central-C₂-detector and block-module inputs. Both checked the actual shadow stabilizer normalization, lifting local inversion-triviality through ε, the original fiber's zero label, the actual Borel complement in E, all functional pushouts, and complement adjustment by extended Borel characters. Both checked that the fixed central multiplier z persists over the pure outer class and gives the stated collision. No global complement, core-vanishing hypothesis or quotient loop is assumed. The block consequences retain the previously disclosed character, descent and standard algebra inputs. No new computation or formal verification was used; noncentral Frattini subgroups and sufficiency of the surviving module patterns remain outside the result.

