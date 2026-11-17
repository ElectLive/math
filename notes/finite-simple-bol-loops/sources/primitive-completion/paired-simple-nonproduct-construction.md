# A nonproduct paired simple construction

**Mira Cult**

**Independently reviewed at the exact source recorded below**, continuing [0323:C0010](../../claims/0010.md). Let $`T`$ be a finite nonabelian simple **ambivalent** group: every element is conjugate to its inverse. Suppose

```math
A\triangleleft Y<T,\quad [Y:A]=2,\quad Z<T,\quad T=AZ\text{ exactly},
 \quad Y\cap Z=\langle r\rangle\cong C_2,
```

and suppose a nonzero homomorphism $`\varepsilon:Z\to C_2`$ satisfies $`\varepsilon(r)=0`$. The exact factorization means $`A\cap Z=1`$; the displayed intersection order also follows from the order equation. Define $`\nu:Y\to Y/A\cong C_2`$ and

```math
X=\{(z,y)\in Z\times Y:\varepsilon(z)=\nu(y)\}\le T^2. \tag{1}
```

Then, conditional on the canonical-folder, simplicity and route criteria cited below, the full anti-diagonal in $`T^2`$ defines a finite simple proper Bol loop with canonical group $`T^2`$ and stabilizer $`X`$. It is non-Bruck and has neither an exact-factorization isotope nor a Bruck isotope. This supplies a conditional construction, not an exhaustion or a literature-novelty claim.

The canonical faithful-folder and normal-subloop inputs are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), and the canonical inverting automorphism is [C0007](../foundations/C0007.md) with its scoped review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The intrinsic exact-factorization witness criterion is reviewed in [the exact-factorization source](../factor-permutation/exact-factorization-criterion.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e3a39be22fe1390d3717bdeee8f81d82f6817aef); isotope invariance of that witness route is reviewed in [the bipartite-witness source](../factor-permutation/radical-free-bipartite-witness.md#isotopy-invariance-of-the-witness-route) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9d1c0af909166459fbbeb87b881c28dff353aa3f). The no-Bruck-isotope input is [the generalized-Fitting theorem](../factor-permutation/exact-factorization-criterion.md#inner-inversion-and-the-generalized-fitting-subgroup) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/84eba0ffd4dfab4b6d64853a3131010ad2b945b8). The separate review of the present deduction is recorded below.

## Regularity and the canonical folder

The two quotient maps in (1) are surjective, so $`X`$ is a subgroup with full coordinate projections $`Z,Y`$, nontrivial common quotient $`C_2`$, and

```math
|X|=|Z||Y|/2=|Z||A|=|T|. \tag{2}
```

It is therefore not the product of its projections. Also $`r\notin A`$ by $`A\cap Z=1`$, and hence $`\nu(r)=1`$.

For each $`g\in T`$, the exact factorization gives a unique expression $`g=az`$, $`a\in A,z\in Z`$. Set $`\delta=\varepsilon(z)`$ and

```math
u=z^{-1}r^\delta,\qquad v=ar^\delta.
```

Since $`\varepsilon(r)=0`$ and $`\nu(r)=1`$, $`(u,v)\in X`$, and $`v u^{-1}=az=g`$. Thus the map $`(u,v)\mapsto vu^{-1}`$ is onto $`T`$, and by (2) it is bijective. Equivalently, the usual left–right action of $`X`$ on $`T`$ is regular. A nonidentity $`(u,v)\in X`$ therefore cannot have $`u`$ conjugate to $`v`$.

For the formal swapping involution $`\widehat\tau`$, put

```math
G=T\times T,\quad \tau(u,v)=(v,u),\quad
 K=\{(t,t^{-1}):t\in T\},\quad \Lambda=\widehat\tau K.
```

All outside involutions are one $`G`$-class and

```math
\Lambda^2=K^2=\{(a,b):b\text{ is }T\text{-conjugate to }a^{-1}\}.
```

Ambivalence makes the forbidden conjugacy relation here equivalent to $`a`$ conjugate to $`b`$, so regularity gives $`X\cap\Lambda^2=1`$. Since $`\Lambda^2`$ is $`G`$-conjugacy invariant and $`|K|=[G:X]=|T|`$, $`K`$ is a transversal to every conjugate of $`X`$. It is inverse-closed and closed under sandwiches. It generates $`G`$, because $`T`$ is perfect. No identification of the two conjugacy relations is made without the ambivalence hypothesis.

The subgroup $`X`$ is core-free: the only proper nontrivial normal subgroups of $`G`$ are its two coordinate factors, neither of which lies in $`X`$ because $`Z,Y<T`$. The cited faithful-folder interface identifies $`G`$ as the canonical left multiplication group and $`\tau`$ as its canonical inversion.

## Simplicity and route exclusions

The image of $`K`$ in either coordinate quotient has size $`|T|`$. The corresponding quotient stabilizer indices are $`[T:Y]`$ and $`[T:Z]`$, respectively, strictly smaller because $`Y,Z\ne1`$. Thus the original normal-subloop criterion is strict for both proper nontrivial normal subgroups of $`G`$, so the loop is simple. Since $`X\ne1`$, it is nonassociative. Its canonical action is imprimitive because $`X<Z\times T<G`$; the reviewed simple nonassociative Moufang-primitivity criterion makes it non-Moufang, hence proper.

Any intrinsic exact-factorization witness must be a normal subgroup of $`T^2`$ of order $`|T|`$, so it is one of the two coordinate factors. For either choice, the witness equality $`XM\cap X\tau(M)=X`$ fails: its left side is the product $`Z\times Y`$, strictly larger than the nonproduct fiber subgroup $`X`$. The cited witness criterion therefore excludes the exact-factorization route; its reviewed isotope invariance excludes every exact-factorization isotope. Also $`O_2(G)=1`$, so the cited generalized-Fitting theorem excludes every Bruck isotope. These conclusions use the stated original canonical and isotope interfaces; they do not claim any broader classification.

## A source-qualified $`\mathop{\mathrm{Sp}}\nolimits_6(2)`$ instance

Galt–Gubarev, [arXiv:2509.04961v1](https://arxiv.org/html/2509.04961v1), §3 Lemma 2 and Example 1, identify in $`T=\mathop{\mathrm{PSp}}\nolimits_6(2)=\mathop{\mathrm{Sp}}\nolimits_6(2)`$ subgroups

```math
A=\mathop{\mathrm{SU}}\nolimits_3(3)\triangleleft Y=\mathop{\mathrm{SU}}\nolimits_3(3):2,
 \qquad Z=S_5\times C_2,
```

with $`T=AZ`$ exact and $`|Y\cap Z|=2`$, citing the factorization source Table 10.7. This use is confined to that stated example and its subgroup data; no conclusion from the paper's separate $`\mathop{\mathrm{PSL}}\nolimits_2`$ counting theorem is used. Since $`\dim_{\mathbb F_2}\mathop{\mathrm{Hom}}\nolimits(Z,C_2)=2`$, some nonzero $`\varepsilon`$ vanishes on the nonidentity element of $`Y\cap Z`$.

The standalone certificate [verify_paired_sp6_nonproduct.g](../code/verify_paired_sp6_nonproduct.g) uses the 28-point generators and subgroup word from the [ATLAS $`S_6(2)`$ page](https://brauer.maths.qmul.ac.uk/Atlas/clas/S62/) and checks, within the represented permutation group, simplicity, all 30 conjugacy classes and their inverse stability, the subgroup orders and exact intersections, and an explicit nonzero $`\varepsilon`$ killing $`Y\cap Z`$. The asserted orders are

```math
|T|=1451520,\quad |Y|=12096,\quad |A|=6048,\quad |Z|=240,
 \quad |Y\cap Z|=2.
```

The independent reviews below cover this application and exact finite certificate, with the stated source and algorithm dependencies; the certificate is not a proof of arbitrary instances. In this concrete instance (1) gives a simple proper loop of order $`1451520`$ with a nonproduct stabilizer, conditional on those inputs and the cited canonical interfaces.

## Reproducible finite evidence

Run `gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_paired_sp6_nonproduct.g` with GAP 4.15.1. The release archive is pinned in code/README.md. The project read and ran this exact working source successfully after adding explicit membership checks for both supplied subgroup generators in the ambient permutation group. The script asserts ambient simplicity, 30 actual conjugacy classes whose sizes sum to the group order, and inverse stability by `IsConjugate` for every representative. No character-table database is used for this step. It also asserts all subgroup orders, normality, intersections and the nonzero character killing the common involution. The output sizes are `[1451520,12096,6048,240,120,2]` for the ambient group, Y, A, Z, the separate S5 subgroup and Y∩Z.

The project independently downloaded the two ATLAS generator files, checked the SHA-256 hashes embedded in the certificate and compared their cycles with its a,b. The displayed subgroup word matches the ATLAS v2 maximal-subgroup entry. The other two subgroup generators are explicit permutations whose membership and required properties are checked by the certificate. The group name Sp6(2) uses ATLAS identification; the actual permutation-group properties needed by the proof are checked directly. The general argument, GAP algorithms and earlier canonical-folder interfaces remain mathematical/computational dependencies. This is a finite certificate for this input, not a formal proof, a complete subgroup census, or a reproof of all upstream inputs.

## Independent exact-source review

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete analytic argument and certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/393f6714639ad5dd6dfe46756220acde5b690502), conditional on the pinned canonical-folder, simplicity, properness and route/isotope interfaces. Each read the committed source and independently ran the exact committed GAP certificate under GAP 4.15.1, with all assertions passing. They checked the regularity construction, essential ambivalence step, both original normal cuts, nonproduct witness failure and isotope exclusions.

The paired-simple and strip-forest reviewers also independently downloaded both ATLAS generator files and matched the recorded SHA-256 hashes; the paired-simple reviewer checked the displayed ATLAS subgroup word and the cited Galt–Gubarev example. The other two reviewers did not perform a fresh ATLAS source audit. No reviewer independently reproved all upstream classification results, GAP algorithms or the ATLAS group-name identification. These are independent model mathematical/code reviews of this scoped construction, not a complete stabilizer classification, a novelty audit, human/formal certification or GitHub approval.
