# One simple Bol tower with a universal countable class-two radical

**Mira Cult · Provisional research.** Author proof, not independently reviewed.

This proposed infinite construction uses the [finite nonabelian projective family](../../projective-radicals/proofs/multiplicity.md) and the [finite group-host theorem](../../projective-radicals/proofs/universal-group-host.md). It concerns subgroups of one radical rather than subloops. Compatibility of all the native finite-stage shears is new here, and is not part of either finite result’s review.

**Theorem.** There is a nested sequence of finite simple proper left Bol loops

```math
Q_0\ <\ Q_1\ <\ Q_2\ <\cdots,\qquad |Q_s|=20\cdot3^{119+57s},
```

all of exponent six. The displayed arrows preserve the actual native loop multiplication. Their union is a countable locally finite **simple** proper left Bol loop of exponent six. Its canonical group of left translations has the form

```math
G_\infty=P_\infty\rtimes\mathrm{PSL}_2(19),\qquad P_\infty=\mathrm{Rad}(G_\infty).
```

The radical has class exactly two, exponent three, and contains an isomorphic subgroup for **every countable group** of class at most two and exponent dividing three. Each embedding preserves the center in the sense $`F\cap Z(P_\infty)=Z(F)`$ inside the embedded $`F`$. One tower suffices for all input groups. This is a universal *subgroup* result in the actual left group, not a claim that these groups are subloops, normal or characteristic subgroups.

There is also a compatible finite bound. Write $`s(k)=\max\{1,\binom{k}{2},\lceil k/2\rceil\}`$ for $`k\ge1`$. The one coherent stage $`Q_{s(k)}`$ has radical of order $`3^{236+114s(k)}`$ containing all target groups of order at most $`3^k`$ with the same center intersection. The independent finite group counting argument in the finite-host manuscript shows that the quadratic order of growth of this logarithmic host size is optimal even among unrestricted finite group hosts. The present coefficients do not sharpen the separately constructed smaller finite-host constants.

## 1. Infinitely many compatible, actual affine shears

We use the notation of the nonabelian source. In particular $`T=\mathrm{PSL}_2(19)`$, $`B=19:9`$, $`M`$ is its 19-dimensional ternary augmentation representation, $`X_0,Y_0`$ have dimensions 117,119, and the true affine stabilizer uses $`f_0`$ and a derivation $`d`$. The source proves that a fixed signed covector $`\phi`$ distinguishes the genuine torus collision above $`r^3`$; extend it by zero on all coordinates subsequently added. A new paired copy of $`M`$ appends the actual graph

```math
f^+(x,v)=(f(x)+a(v),v),\qquad d^+=(d,0).
```

A $`B`$-equivariant shear $`a`$ is forbidden for this step if it belongs to

```math
D_f=f\mathrm{Hom}_T(M,X)+\mathrm{Hom}_T(M,Y);
```

the torus detector is preserved if $`\phi a(1-w)=0`$. For the original spaces together with $`N`$ pairs, the source proves $`\dim D_f\le 3+2N`$ and the detector costs at most seven constraints.

Construct in consecutive triples **passive, passive, active**, starting with no new pair. Insist that the shear of every pair has values in $`Y_0`$ and **earlier passive** minus slots only, even if it is appended *after* earlier active slots. Suppose there are $`t`$ passive and $`s`$ active pairs presently. The dimension of this restricted space of $`B`$-maps is $`14+3t`$: the chosen target is the direct sum $`Y_0\oplus M^t`$, and a $`B`$-map from $`M`$ is specified by the image of $`e_0-e_\infty`$ fixed by the nine-cycle subgroup. After the detector constraints this leaves dimension at least $`7+3t`$, while the full forbidden space on all earlier coordinates has dimension at most $`3+2(t+s)`$. At every choice $`t\ge2s`$, so the margin is at least four. Choose one allowed map outside the actual current $`D_f`$. For an effective choice use row-reduction in the fixed chronological module basis. No earlier shear is ever changed.

Recall the exact one-step defect argument: for $`T`$-submodules $`J\subset X^+`$, $`Z\subset Y^+`$ with $`f^+(J)\subset Z`$, the nonnegative differences of the dimensions in the negative $`w`$-spaces add under intersection and projection to the new top $`M`$. Nonnegativity below follows from injectivity of $`e f`$ on $`eX`$, with $`e=(1-w)/2`$; on top it follows from inclusion. At zero the lower pair is zero by induction. The two top images coincide, since the top is simple and $`eM\ne0`$. A nonzero such pair would be two $`T`$-linear graphs over $`M`$, forcing $`a\in D_f`$. Thus no nonzero zero-defect pair appears. The triangular negative injection and fixed detector are also preserved. In particular one need **not** assume that all countably many shears have been chosen independent modulo some original passive forbidden space.

## 2. Brackets for which adding a new block never changes an old product

Index the active pairs by $`(i,j)`$, all positive integer pairs ordered by increasing $`i+j`$ and within a diagonal by increasing $`i`$. Name the passive output slots $`1,2,\ldots`$ in order of appearance. The active slot $`a=(i,j)`$ enters with output $`j`$ already present (its ordinal position is at least $`j`$ and two passive slots have been added per position). If $`j=1`$ put $`(C_1)_{a,a}=1`$. If $`j>1`$, put

```math
(C_j)_{(i,1),a}=(C_j)_{a,(i,1)}=1.
```

All other coefficients are zero. The slot $`(i,1)`$ occurs before $`(i,j)`$ for $`j>1`$. Each new nonzero entry involves the newly appended active slot. In particular there is **no** new output on any pair of old inputs. An infinite coefficient array with finite truncations which failed this last condition would not give group embeddings.

At a completed stage arrange the active slots last for inspection only. The restriction on the shear targets makes the active minus coordinate of $`f(x)`$ exactly the matching active plus coordinate, including for later passive inputs. Define the genuine bracket on active coordinates by (3) of the nonabelian source, with the specified symmetric matrices, the physical $`20`$-point product $`\beta`$ on $`M`$, and values in the central passive minus slots. The law $`v*v'=v+v'+[v,v']/2`$ makes a group $`P_s`$ of class at most two and exponent three. For $`s\ge1`$ the first coefficient and a nonzero product in $`M`$ give class two. The $`3s`$ new pairs give $`|P_s|=3^{236+114s}`$. As in the source adjoin the actual $`T`$ and sign $`z`$, take the physical $`H_s`$ over $`B`$ with entries $`(x,f(x)+d(g))`$, and the section $`K_s=z\Lambda_s`$, where $`\Lambda_s`$ consists of **all** outside involutions.

For clarity, none of the sharpness or simplicity inputs from the finite proof requires equal numbers of active and passive coordinates. The graph pairs commute in the kernel because on every active coordinate they are diagonal and the coefficients and $`\beta`$ are symmetric. In a vertical collision, reducing modulo the entire passive-minus output makes the kernel abelian; the opposite two true sign equations force every active component of an inverted diagonal pair zero. Such a pair is central in the kernel, so the linear vertical injection now applies to its actual conjugated sign. In nonvertical collisions, the same quotient preserves the original over-$`r^3`$ obstruction, since $`\phi`$ kills every passive slot, every newly appended graph denominator and $`(r^3-1)Y`$. All mark fibers therefore remain the original signed affine spaces with sizes summing to $`20|Y|`$, the physical index of $`H_s`$.

Every normal cut inside $`P_s`$ is a bracket ideal and an additive $`T`$-subspace, even without sign stability. Its true cosets are its additive cosets. The strict-cut calculation in §3 of the nonabelian proof then applies unchanged, because the only possible equality forces a nonzero zero-defect admissible $`T`$-pair, excluded above. For a normal surjecting onto $`T`$, the true perfect $`T`$ dies in the residual 3-group and so do all the passive central copies of $`M`$, which are spanned by $`T`$-differences. Only the old one-dimensional coinvariant can survive, hit by both the stabilizer and the marks. These are exactly the same generation, faithfulness and strictness tests from the source. They prove that the native coset loop $`Q_s`$ is simple, that its faithful canonical left group is $`G_s=P_s\rtimes T`$ with radical $`P_s`$, and that its order is $`20|Y_s|=20\cdot3^{119+57s}`$. At $`s=0`$ take the audited explicit base. This is not a simplicity argument based on isomorphism of additive quotients.

Zero-extension on old slots is an **actual group injection** on signed groups, since no old-old bracket gains a new component and every action on the original module sites remains the same. It takes old physical marks to marks and satisfies $`G_s\cap H_{s+1}=H_s`$ by triangular graph extension and unchanged derivation. For any two old cosets the old unique marked representative of their product is still a representative of that product upstairs; uniqueness there proves preservation of the native product. The order formula makes each embedding strict. Each stage retains the old right-alternative failure and an element of order six; no element has order above the exponent-six bound, since all marked lifts have projective order one or two over an exponent-three kernel as in the finite source.

## 3. The union, its true left group, and its group-theoretic age

The union is a loop, not merely a magma: two elements lie in a common finite subloop which contains their left/right divisions, and injectivity of translations in the union follows by putting two alleged solutions in a common finite stage. Its Bol identity, exponent and properness follow on finite tuples. It is countable and locally finite. Any nonidentity congruence relates two different elements of some stage; its restrictions there and at all later stages are universal by finite simplicity. Thus the union is simple.

Each element of $`G_\infty=\bigcup_s G_s`$ acts consistently on $`Q_\infty`$. Indeed the injections are the actual same coset actions on $`G_s/H_s`$, equivariant under old $`G_s`$; equivalently they give $`Q_\infty=G_\infty/(\bigcup_s H_s)`$ as sets with marked section $`\bigcup_s K_s`$. An element acting trivially on the union acts trivially on its own finite stage and hence is the identity. Conversely each $`G_s`$ is generated by its marks, which act as the native left translations even upstairs. Therefore $`G_\infty`$ is exactly the canonical left multiplication group. Its normal subgroup $`P_\infty=\bigcup_s P_s`$ has class two and exponent three, so is solvable. Every solvable normal subgroup has trivial image in the nonabelian simple quotient $`T`$, proving it is the full solvable radical.

Let $`F`$ be any countable group of class at most two, exponent dividing three. Use the abelian additive ternary coordinates $`V\oplus Z`$, with $`Z=Z(F)`$, $`V=F/Z`$, and alternating commutator $`\omega:V^2\to Z`$; the class-two product is addition plus half the commutator, as checked in the finite-host source. Both vector spaces have finite or countable bases $`v_i,z_j`$ indexed by initial segments of the positive integers. Fix $`e=e_0-e_\infty\in M`$ and $`w_*=\beta(e,e)\ne0`$. Send $`z_j`$ to $`w_*`$ in passive minus slot $`j`$. Send the basis lift $`v_n`$ to $`e`$ in active **plus** slot $`(n,1)`$ together with $`\omega_j(v_i,v_n)e`$ in active **minus** slot $`(i,j)`$ for $`i<n`$, where $`\omega_j`$ denotes the $`z_j`$ coefficient. Extend additively. There are only finitely many $`i<n`$, and for each of them $`\omega(v_i,v_n)`$ individually has finite support. Thus every image is an actual finite-stage element, not a vector in a prohibited direct product or completion. For $`i<n`$, the physical bracket is precisely $`\sum_j\omega_j(v_i,v_n)w_*^{(j)}`$; reversing the two rows contributes zero from the earlier vector's strictly lower minus support. The other symmetric entry at $`j>1`$ cannot contribute since all plus coordinates have column index one. Both the bracket and group law are preserved. The distinct plus and passive coordinates exhibit injectivity. Central elements have central images, and a noncentral element already fails to commute with an element of its own embedded group. This gives the asserted center intersection. Abelian inputs use only the passive coordinates; no infinite tensor products are taken.

If $`|F|\le3^k`$ then $`\dim V+\dim Z\le k`$, so all required active slots have $`i+j\le k`$ and all passive slots have $`j\le k`$. These occur by the claimed stage. The causal order of the construction is material: in the group on $`v_1,v_2,\ldots`$ with independent central $`[v_1,v_n]=z_n`$ for $`n>1`$ and all other basic brackets zero, assigning to $`v_1`$ its *entire* commutator column at once would require infinite support. Assigning the old-new interaction only when $`v_n`$ enters is why no such pathology occurs here.

On a nested sequence of finite target groups with center-reflecting inclusions, the embeddings may also be chosen coherently: the unions of the centers give the true center of the union, since each finite-stage central element remains central in every later stage and noncentrality is witnessed already at its own stage. Extend additive center and quotient bases and their chosen lifts from stage to stage, so later basis choices never alter old coefficients. This is not an ultrahomogeneity, uniqueness or extension-of-arbitrary-partial-automorphisms claim.

[Provisional results and replay](../README.md)
