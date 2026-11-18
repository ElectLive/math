# 0111. No nilpotent transitive action on an entire projective-line socle power

**Mira Cult**

The projective line gives a special advantage in rank one: a nontrivial subgroup of translations determines its rational fixed point. This lets a slope recorded in a correlated stabilizer be lifted to an element of the stabilizer itself, not just to entries at its individual coordinates.

**Theorem.** Let the faithful canonical left multiplication group $`G`$ of a finite simple non-Moufang left Bol loop have **entire socle** $`S=\operatorname{PSL}_2(q)^n`$, for a prime power $`q\ge4`$ and $`n\ge2`$. The permutation image of $`G`$ on the simple factors cannot be both nilpotent and transitive. No regularity, splitting over the socle, or independence of stabilizer projections is assumed.

The [even-field proof](0106-nilpotent-transitive-even-field-psl2.md) includes the four-element field by a separate argument. We treat the odd fields here. This does not exclude a single rank-one factor, a rank-one section, intransitive actions, or arbitrary nonnilpotent transitive actions.

The obstruction in odd field degree is not simply a bound on outer automorphisms. One first places an all-paired mark and an actual stabilizer transporter for the same permutation in a **common Sylow 2-group**. Their field arrows then agree on an explicit subfield, even when their full projective arrows are different. An eigenvector in the true multiplier image lifts to one point-stabilizer element that a genuine mark square would hit.

## Local possibilities and actual paired packing

Write $`q=p^f`$ with $`p`$ odd and $`q\ge5`$, $`T=\operatorname{PSL}_2(q)`$, $`L=|T|=q(q^2-1)/2`$, $`A=H\cap S`$. The [whole-socle projection theorem](0105-nilpotent-socle-stabilizer-projections.md) gives $`H\to C`$, and actual transports identify the nontrivial proper subgroups $`U_i=\pi_i(A)<T_i`$ with $`U`$. By [rectangular incidence and the homogeneous endpoints](0109-nilpotent-socle-actions-are-two-groups.md), $`C`$ is a 2-group, $`n`$ is a power of two, the signed and unsigned coordinate images agree, and there is a selected outside involution pairing every coordinate. We use the general [parity and packing lemmas](0110-nilpotent-transitive-alternating-socles.md#a-central-involution-in-the-actual-stabilizer-layer), not the alternating-family conclusion. The notation is that of the [marked-square model](0103-radical-free-socle-coordinates.md#marked-square-membership-from-cycle-transport): $`H`$ is the real loop point stabilizer, $`K`$ is the set of canonical left translations and $`\Lambda`$ the corresponding set of marked involutions in the signed group. In particular $`H\cap\Lambda^2=1`$.

The group $`T`$ has a single class of involutions. Thus $`A`$ and $`U`$ have odd order: a transitive Sylow 2-subgroup of $`H`$ would otherwise centralize an involution in the actual $`A`$, nontrivial and inner-conjugate at every site, which is a product of two actual conjugates of the all-paired mark. This is not an assumption that arbitrarily chosen local involutions lift together.

We use Guralnick and Zieve, [*Polynomials with PSL(2) monodromy*, Appendix A, Theorem A.1, Lemmas A.2–A.4, and the Lang discussion after A.5](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf). By the subgroup list, the odd $`U`$ either lies in a cyclic split or nonsplit torus, or lies in a rational Borel with nontrivial normal translation $`p`$-subgroup. Indeed the odd subgroups of the dihedral cases are cyclic, the exceptional $`A_4,S_4,A_5`$ themselves have even order, as do all nontrivial simple or full projective subfield groups in the list. An odd subgroup of a Borel with trivial translation kernel is cyclic of order prime to $`p`$, hence semisimple and lies in a split torus. Nontrivial $`p`$-elements in an affine Borel have a common unique rational fixed point. Thus in the latter case $`O_p(U)`$ determines a point intrinsic to $`U`$, transported between factors by $`H`$.

In the toral case choose its containing full cyclic torus of order at most $`(q+1)/2`$. The classes of full tori of each type are invariant inner classes in $`T`$. For example $`\operatorname{PGL}_2(q)`$ transports any two eigenpairs of the same rationality type; multiplying a transporter by a member of the split or nonsplit torus in the full projective group can adjust determinant square class. In the nonsplit case this follows from surjectivity of the norm from $`\mathbb F_{q^2}^{\times}`$ to $`\mathbb F_q^\times`$. Field automorphisms preserve rationality. The same observation applies on passage to the corresponding cyclic inner tori. In general, for $`U\le M\le T`$ contained in a single such automorphism-stable inner class of **containers $`M`$**, aligning $`M`$ on each edge by inner conjugations of the one all-paired mark and packing its $`|M|^{n/2}`$ actual translated elements in distinct $`A`$-cosets in $`M^n`$ gives $`|A|\le |M|^{n/2}`$. No assumption $`H\le N(M^n)`$ is needed.

## A common Sylow group kills the prime-to-characteristic slopes from the odd subfield

In the remaining Borel case choose rational point frames making all the intrinsic points infinity. Write $`D`$ for the image of $`A`$ under the actual affine slope homomorphism at all sites. This is an abelian group of odd order prime to $`p`$, in the product of local square-multiplier groups; its kernel in $`A`$ consists of translations and is a $`p`$-group. For $`z\mapsto a z^{p^e}+b`$ between the chosen frames, conjugation takes slope $`u`$ to $`u^{p^e}`$. Consequently $`H`$ acts on $`D`$ by its real coordinate permutations and field arrows alone. Let $`f_0`$ be the odd part of $`f`$ and $`q_0=p^{f_0}`$. We claim
```math
                            \gcd(|D|,q_0-1)=1.                        \tag{1}
```

Suppose an odd prime $`r\mid(q_0-1)`$ divides $`|D|`$. Then $`D[r]\ne0`$ is an actual $`\mathbb F_r`$-module of slopes in $`\mu_r^n`$, with $`\mu_r\subseteq\mathbb F_{q_0}^\times`$. Let $`P`$ be a Sylow 2-subgroup of $`H`$. Its image in the 2-group $`C`$ is all of $`C`$; extend $`P`$ to a Sylow 2-subgroup $`Q`$ of the formal $`E=G\rtimes\langle t\rangle`$. Choose a conjugate $`\lambda`$ of a selected all-paired mark that lies in $`Q`$, still selected and all-paired. This only requires the actual $`G`$-conjugacy invariance of the mark set: $`E=QG`$, so a conjugation into $`Q`$ by $`e=yg`$, $`y\in Q,g\in G`$, already conjugates into $`Q`$ by $`g`$. There exists $`h\in P`$ with the same coordinate permutation $`\sigma`$ as $`\lambda`$. Neither $`h^2=1`$ nor a section of the full outer quotient is asserted.

Now $`h^2`$ and $`\lambda h^{-1}`$ belong to $`Q`$ and fix every coordinate. At any single site their actual field exponents lie in the 2-primary subgroup of $`\operatorname{Gal}(\mathbb F_q/\mathbb F_p)`$. Its fixed field is $`\mathbb F_{q_0}`$. Thus the linear action of $`h`$ on $`D[r]`$ has square one, and the field arrow of $`h`$ from site $`i`$ to $`\sigma i`$ agrees **on $`\mu_r`$** with that of $`\lambda`$ on this edge. Individual arrows of either element at exchanged sites need not have field order two. Merely having equal coordinate permutations would not prove the agreement.

Since $`r`$ is odd, $`h`$ has a nonzero eigenvector $`d\in D[r]`$ of eigenvalue $`+1`$ or $`-1`$. In multiplicative coordinates this pairs the entries $`d_i,d_{\sigma i}`$ by the true field arrow of $`\lambda`$, possibly followed by inversion. Lift this **single word** to an element $`w\in A`$ of order $`r`$: the preimage of $`\langle d\rangle`$ has a $`p`$-kernel, so a Sylow $`r`$-subgroup of order $`r`$ maps isomorphically onto $`\langle d\rangle`$. At a zero (multiplicative identity) coordinate $`w_i=1`$, since a translation of order dividing $`r`$ is identity. Else $`w_i`$ is semisimple and conjugate by a translation in $`T`$ to its actual slope $`d_i`$. The $`T`$-class of a nonidentity split element of this odd order is determined by its unordered ratio $`\{d_i,d_i^{-1}\}`$: coordinate swaps reverse the ratio, and a split diagonal projective centralizer contains both determinant parities, so the projective conjugator can be taken in $`T`$. Realness also follows directly from the determinant-one Weyl representative. An arbitrary semilinear arrow acts on this unordered ratio by its field exponent, regardless of whether it fixes the chosen point.

It follows on every paired edge that $`w_{\sigma i}`$ is $`T`$-conjugate to the inverse of the image of $`w_i`$ under the actual $`\lambda`$-arrow. The [same-class marked pair product](0103-radical-free-socle-coordinates.md#marked-square-membership-from-cycle-transport), independently on each edge in $`S`$, expresses $`w`$ as a product of two actual $`S`$-conjugates of $`\lambda`$. This contradicts $`1\ne w\in H,\ H\cap\Lambda^2=1`$ and proves (1). In particular for odd $`f`$, all slopes are killed and $`A`$ lies in a product of Sylow $`p`$-subgroups of order $`q`$. The Sylow classes are automorphism-stable, so paired packing gives $`|A|\le q^{n/2}`$. This bound also holds in the toral case since $`(q+1)/2\le q`$.

For even $`f`$, a simpler bound suffices. Here $`q\equiv1\pmod8`$. In a rational Borel $`T_\infty`$ of order $`q(q-1)/2`$, take the preimage $`M`$ of the odd part of the multiplier group. It contains the odd $`U`$ and has order at most $`q(q-1)/8`$. Its full inner class is transported by every automorphism: the Borels are point stabilizers in one $`T`$-orbit, their translation kernels are intrinsic and the odd multiplier subgroup is characteristic in the cyclic quotient. Paired packing yields
```math
          |A|\le (q(q-1)/8)^{n/2}\quad(f\ \mathrm{even}).
```
This covers the toral alternative too, since $`(q+1)/2\le q(q-1)/8`$ at $`q\ge9`$. No claim that (1) kills *every* slope in even field degree is needed.

## Exact signed counts in the two ranges

Let $`V=|\operatorname{Aut}(T)|=f q(q^2-1)`$ and $`I`$ count all square-one elements of that full group, identity included. The ordinary $`\operatorname{PGL}_2(q)`$ contributes $`q^2+1`$ from its two involution classes and identity. When $`f`$ is even there is one further projective conjugacy class of square-one semilinear arrows, conjugate to the half-field Frobenius by the projective Lang result quoted above. Its centralizer in the projective group is $`\operatorname{PGL}_2(\sqrt q)`$ (normalize a projective matrix by its first nonzero entry), of index $`\sqrt q(q+1)`$. Thus $`I=q^2+1`$ in odd degree and $`I=q^2+1+\sqrt q(q+1)`$ in even degree. In particular $`I^2\ge V`$ since $`f\le q`$.

The true transversal satisfies $`|K||A|\ge L^n`$. The [actual symmetric Sylow moment upper bound](0110-nilpotent-transitive-alternating-socles.md#a-sharp-signed-count-in-a-symmetric-sylow-2-group-closes-degree-six) gives both $`|K|<(2I)^n`$ and, for $`2V<I^2`$,
```math
                         |K|\le
                     \{ I(1-2V/I^2)^{-1/4}\}^{n}.                    \tag{2}
```
It counts all involutory coordinate permutations in a binary Sylow group: $`F_1=I,\ F_{2m}=F_m^2+2^{m-1}V^m`$. This does not assume independent actual selection of outer labels.

If $`f`$ is odd and $`q\ge17`$, then $`L>2I\sqrt q`$: equivalently $`\sqrt q>4(q^2+1)/(q^2-1)`$, true at 17, with the left increasing and the right decreasing. Together with $`|A|\le q^{n/2}`$ this is already impossible. At $`q=7,11,13`$, use (2) instead; in each case $`2V<I^2`$ and
```math
                          q^2 I^6 < L^4(I^2-2V),
```
equivalently $`I(1-2V/I^2)^{-1/4}<L/\sqrt q`$. The remaining odd-degree field $`q=5`$ gives $`A_5`$, already covered by the reviewed $`q=4`$ even-characteristic theorem via the standard $`A_5\cong\operatorname{PSL}_2(5)\cong\operatorname{PSL}_2(4)`$ isomorphisms.

For even $`f`$, at $`q=9`$ the local container has size at most nine, while $`I=112,\ V=1440,\ L=360`$ and $`112^6<120^4(112^2-2880)`$. Thus (2) gives $`|K|<120^n`$, impossible. For the remaining squares $`q\ge25`$,
```math
 \frac I{q^2}\le\frac{756}{625},\qquad
 \frac{2V}{I^2}<\frac{2f}{q}\le\frac6{25}.
```
Indeed $`f\le\log_3 q`$, $`\log(q)/q`$ decreases here, and $`\log_3(25)<3`$. Moreover
```math
 \frac{756}{625}(25/19)^{1/4}<\sqrt2,\qquad
 \frac{L}{q^2\sqrt{q(q-1)/8}}
       =\sqrt2(1+1/q)\sqrt{1-1/q}>\sqrt2 .
```
For the latter compare $`(1+x)^2(1-x)=1+x-x^2-x^3>1`$ at $`x=1/q\le1/2`$. Substitution in (2) now contradicts $`|K||A|\ge L^n`$. This completes the odd-characteristic conclusion.


## Reproducibility and scope

The [author's slope and mass checks](../sources/code/verify_odd_psl2_nilpotent_slopes.py) and [independent semilinear controls](../sources/code/check_odd_psl2_transporter_independent.py) are standalone Python 3 programs. The latter enumerates every actual automorphism at $`q=9`$ and realizes distinct full field arrows, both slope eigensigns, and the two actual conjugate marks at $`q=49`$. They check these mechanisms; the inequalities above, not a finite search, give the unbounded statement. The [evidence record](../normal-layer-evidence.md#odd-field-projective-line-whole-socles) separates the two field ranges and proof dependencies. Under Mira Cult's research direction, OpenAI models contributed the proof, computations, independent review and public exposition. The particular model versions are not established here. This is not human peer review or formal verification.
