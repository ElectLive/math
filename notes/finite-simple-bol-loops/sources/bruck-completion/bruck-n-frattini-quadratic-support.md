# Bounded quadratic support for an N-Frattini one-M shadow

**Theorem with the scoped independent reviews below.** In the faithful simple nonassociative Bruck-envelope setting of [C0010](../../claims/0010.md), assume $`A=G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, $`Z=\Phi(P)\cong N`$, and

```math
V=P/Z\cong X\oplus U^b,\qquad X\in\{J,P_6\},\quad b\ge0.
```

Here $`J,P_6,N,U`$ have the paired permutation models of [the one-M reduction](bruck-one-m-noncentral-reduction.md), at the recorded source revision. Let $`q:V\to N`$ be the square map and $`\beta`$ its polar. The marked-rank theorem at the recorded source revision forces $`d=0`$, equivalently $`\beta(v,tv)\in(1+t)N`$ for every $`v`$, for a transposition $`t`$. We also use the independently reviewed bound $`c\le3`$ in [the lifted-socle section](bruck-n-frattini-marked-rank.md#lifted-socle-bound), at exact source the recorded source revision, where

```math
c=\tfrac14\dim_{\mathbb F_2}\bigl(W\cap E\bigr),\quad W=H\cap P,\quad E=\pi^{-1}(\mathop{\mathrm{soc}}\nolimits(U^b)).
```

Subject to these inputs and the new fixed-component certificate, there is an $`S_5`$-module coordinate change of $`U^b`$ such that $`q`$ and $`\beta`$ are supported on $`X\oplus U^a`$, where

```math
a\le\min\{b,4c+2\}\le14. \tag{1}
```

Specifically, $`q`$ vanishes on the remaining $`U`$-summands and their polar with all of $`V`$ is zero. This is a normal form for the **quadratic data only**. It does not assert a splitting or normal form for $`P,G,\tau,H`$, the section, or a quotient loop. In particular the target and passive summands lie in the same $`N`$-block, so a complement in the group extension is not automatic.

## Fixed components

The [certificate](../code/verify_bruck_n_quadratic_support.py) imports the paired module models from [the P6 verifier](../code/verify_bruck_p6_frattini.py) and the $`F_{20}`$ generators from [the one-M verifier](../code/verify_bruck_one_m_noncentral.py). Its exact-source review scope is recorded below. It solves the full quadratic equivariance equations on basis vectors and pair sums. The full dimensions of $`Q(X,N),Q(U,N),\mathop{\mathrm{Hom}}\nolimits(X\otimes U,N),\mathop{\mathrm{Hom}}\nolimits(U\otimes U,N)`$ are $`1,2,1,2`$ for $`J`$, and $`1,2,2,2`$ for $`P_6`$. Imposing $`d=0`$ leaves dimensions $`0,1,1,2`$ and $`0,1,2,2`$, respectively. The surviving $`U`$-quadratic map is the linear top projection, so $`q|_X=0`$ and each $`q|_U`$ is a scalar multiple of this projection.

Put $`R=\mathbb F_2[\varepsilon]/(\varepsilon^2)`$, acting on $`U`$ through its reviewed dual-number endomorphism ring. The certificate verifies that the two $`U\otimes U\to N`$ maps are symmetric, and that precomposition with $`\varepsilon`$ on either input agrees and has rank one. Thus this two-dimensional space is free of rank one over $`R`$. On the $`X\otimes U`$ space the same precomposition has rank zero for $`J`$, respectively one for $`P_6`$: these spaces are $`R/(\varepsilon)`$ and $`R`$. Quadratic maps on direct sums decompose uniquely into summand restrictions and pairwise polar maps, so this fixed-component calculation gives the following structure for every $`b`$, rather than inferring it from the two-block calculation: the $`U`$-to-$`U`$ polar coefficients form an alternating matrix $`C\in M_b(R)`$; the $`X`$-to-$`U`$ terms form one row over the indicated $`R`$-module; and the $`U`$-diagonal terms form a binary top-linear row. The full $`d=0`$ equations on the individual and pairwise components are tested by the certificate.

Let $`D`$ be an $`F_{20}`$-simple complement to $`\mathop{\mathrm{soc}}\nolimits(U)`$. The certificate constructs one from the five- and four-cycle equations and verifies that the two $`U`$-pair maps restrict independently on $`D\times D`$; their restrictions on $`D\times\mathop{\mathrm{soc}}\nolimits(U)`$ and $`\mathop{\mathrm{soc}}\nolimits(U)\times D`$ span the same one-dimensional line, which is the restriction of the $`\varepsilon`$-multiple; and both vanish on socle pairs. The other $`F`$-complement is obtained by adding the socle map and has the same properties.

## Polar rank bound

The original fiber and $`F_{20}`$-module bounds, in the marked-rank source, make the nonfixed part $`B`$ of the $`W`$-shadow a copy of $`S^{b+1}`$, where $`S`$ is the unique nontrivial four-dimensional simple on restriction to $`F_{20}`$. Its intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$ has multiplicity $`c`$: $`W\cap Z=1`$, and the socle has no $`F_{20}`$-fixed part. Let $`B_0=B\cap\{X_S=0\}`$. It has multiplicity at least $`b`$, and its image $`T`$ in $`\mathop{\mathrm{top}}\nolimits(U^b)`$ has dimension at least $`b-c`$ over the multiplicity field $`\mathbb F_2`$.

Write $`C=C_0+\varepsilon C_1`$, with binary alternating matrices. The shadow of $`W`$ is polar-isotropic. On $`B_0`$, every socle graph correction to the polar lies in the $`\varepsilon`$-restriction line. Independence of the two $`D\times D`$ restrictions therefore gives $`C_0|_T=0`$. Since $`T`$ has codimension at most $`c`$, $`\mathop{\mathrm{rank}}\nolimits(C_0)\le2c`$. Congruence over $`R`$ splits off $`r\le c`$ unit hyperbolic pairs, leaving a free zero-residue summand of dimension $`b-2r`$. The same argument applies after the coordinate change; on that summand, the intersection of $`T`$ with the residue coordinate space has codimension at most $`c`$.

There the residue $`C_0`$ vanishes on every remaining coordinate, so all socle graph corrections vanish. Isotropy forces the residual binary $`C_1`$ to vanish on the intersection just described, hence its rank is at most $`2c`$. Splitting its alternating form gives at most $`c`$ $`\varepsilon`$-hyperbolic pairs. Thus $`C`$ has at most $`4c`$ nonzero-form coordinates. For clarity, a unit off-diagonal entry is scaled to 1; simultaneous row and column operations clear all its other incidences, splitting a hyperbolic pair. Repeat until every remaining entry is in εR, then use the ordinary binary alternating-form reduction to split the ε-pairs. These congruences are elementary changes in $`\mathop{\mathrm{GL}}\nolimits_b(R)`$; the zero residue and $`\varepsilon^2=0`$ ensure the remaining free radical has zero polar with all coordinates.

## Simultaneous row normalization

Retain every coefficient of both rows on the nonzero-form coordinates. Changes within the remaining free zero-form radical preserve the polar form. For $`J`$, the $`X`$-row and top-linear row are both binary, and a binary basis change puts both on at most two coordinates. For $`P_6`$, reduce the $`R`$-row to $`0`$, $`e_1`$, or $`\varepsilon e_1`$; in each case its stabilizer still contains all changes on the remaining residue coordinates. Those changes confine the binary top row to at most one further coordinate. If the free radical has fewer than two coordinates, retain all of them.

A preceding $`R`$-congruence can alter the top-linear row through quadratic diagonal terms; the proof does not assume a linear transformation law for it. After polar normalization it is again some binary row, and the final simultaneous reduction applies to that row. The $`X`$-row has the stated linear transformation law. Hence at most $`4c+2`$ coordinates support all of $`q`$ and $`\beta`$, proving (1) subject to the stated inputs.

Run from the repository root with Python 3.11 or later and assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_n_quadratic_support.py
```

The source and certificate have the exact-revision reviews below. The $`c\le3`$ input has its separately recorded reviews; neither a passing script nor this support bound proves an envelope classification.

Root read the new standalone certificate and its imported component interfaces, then ran it with Python 3.12.14. Both J and P₆ component and complement-restriction controls passed. This run supports the finite identities, not by itself the uniform normal-form proof.

## Independent review of the support reductions

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted both the quadratic-support and passive-group reductions, conditional on the pinned marked-rank, lifted-socle, Bruck-envelope and N-block/projectivity inputs. All checked the two polar rank bounds on the actual F20 shadow graph, simultaneous row normalization including the changed top-linear row, the central passive preimage, the same-block involution shear, and the H2/H1 argument using actual fixed H lifts. Each read the exact certificate and both imports, extracted all three from the committed tree, and independently ran the new certificate with pinned Python 3.12; the folder and small-order reviewers specified 3.12.14. Both J and P6 checks passed. Their acceptance covers the 14-block quadratic and 15-block group/involution bounds, not a classification or product decomposition of H, K or the folder, a fresh primary-source audit, or formal verification. It does not cover subsequent appended stabilizer deductions.

## Proposed finite covering family and affine equivalence

**Theorem with the separate scoped reviews below.** The earlier reviews of source the recorded source revision covered the support reduction; the reviews below cover this section and the new diagonal and automorphism assertions in the certificate. The following describes only the $`S_5`$-equivariant quadratic datum; it makes no assertion about equivalence of lifted groups, involutions, stabilizers or sections.

Choose the unique nonzero generator $`\psi:U\times U\to N`$ in the two-dimensional pair-map space satisfying $`\psi(u,u)=0`$ for every $`u`$. Its $`\varepsilon`$-multiple satisfies $`(\varepsilon\psi)(u,u)=\mathop{\mathrm{top}}\nolimits(u)`$. The extended verifier checks both identities on all 256 vectors. With this choice, encode $`q`$ by $`(C,r,\ell)`$: $`C=(C_{ik})`$ is the alternating $`U`$-pair matrix over $`R`$, $`r`$ is the $`X`$-to-$`U`$ row over $`R/(\varepsilon)`$ for $`J`$ and over $`R`$ for $`P_6`$, and $`\ell`$ is the binary row of $`U`$-diagonal top projections. The square restriction to $`X`$ is zero.

Use column coordinates for the $`b`$ copies of $`U`$: an $`S_5`$-module coordinate change $`A\in\mathop{\mathrm{GL}}\nolimits_b(R)`$ sends a new column $`u'`$ to the old column $`Au'`$. Write $`\overline a`$ for the residue of $`a\in R`$, and $`[\varepsilon]a`$ for its $`\varepsilon`$-coefficient. The transformed data are

```math
C'=A^TCA,\qquad r'=rA,\qquad
 \ell'_j=\sum_i\ell_i\overline{A_{ij}}+
 \sum_{i<k}[\varepsilon](C_{ik}A_{ij}A_{kj}). \tag{15}
```

For $`J`$, reduce $`rA`$ modulo $`\varepsilon`$. The last sum is the quadratic diagonal correction: evaluating $`q`$ on the $`j`$-th new summand gives it from $`\psi(u,u)=0`$ and $`(\varepsilon\psi)(u,u)=\mathop{\mathrm{top}}\nolimits(u)`$. Thus $`\ell`$ is not generally an ordinary covector under a change of coordinates.

The certificate also solves the $`S_5`$-endomorphism equations for $`X`$: $`\mathop{\mathrm{Aut}}\nolimits_{S_5}(J)=1`$, while $`\mathop{\mathrm{Aut}}\nolimits_{S_5}(P_6)=\{1,1+J_{\rm all}\}`$, where $`J_{\rm all}`$ is the all-ones map. On the $`P_6`$ cross-map space $`J_{\rm all}`$ acts as precomposition by $`\varepsilon`$, so the nontrivial automorphism multiplies $`r`$ by $`1+\varepsilon`$. The principal and $`N`$-blocks have no homomorphisms in either direction, and $`\mathop{\mathrm{Aut}}\nolimits_{S_5}(N)=1`$; thus these and (15) give all changes of the specified module coordinates.

The proof above gives the following explicit finite **covering family**, for every $`b`$; repetitions are intentional.

1. Choose $`0\le r_0,s_0\le3`$, $`2r_0+2s_0\le b`$, and set $`C=\mathop{\mathrm{diag}}\nolimits(J_2^{r_0},(\varepsilon J_2)^{s_0},0_m)`$, where $`m=b-2r_0-2s_0`$ and $`J_2=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)`$.
2. On the at most twelve nonzero-form coordinates retain arbitrary entries of $`r`$ and $`\ell`$.
3. On the $`m`$ zero-form coordinates, for $`J`$ take the pair of binary rows from $`(0,0),(e_1,0),(0,e_1),(e_1,e_1),(e_1,e_2)`$. For $`P_6`$, take the $`R`$-row as $`0,e_1,\varepsilon e_1`$. If it is zero, take the binary row as $`0`$ or $`e_1`$; otherwise allow any binary row supported on $`e_1,e_2`$. Omit a choice when a named coordinate does not exist.

These are covers because the two radical rows have the simultaneous normalization proved above; changes confined to the zero-form radical preserve $`C`$ and introduce no diagonal correction. The finite choices on active coordinates have not been quotiented, and this is not an irredundant orbit list or a stable-range classification.

For exact equivalence of two candidates at a **fixed** $`b`$, solve (15), optionally multiplying the $`P_6`$ row by $`1+\varepsilon`$. Equivalently, writing $`A=A_0+\varepsilon A_1`$ and $`C=C_0+\varepsilon C_1`$, require $`A_0\in\mathop{\mathrm{GL}}\nolimits_b(\mathbb F_2)`$ and

```math
A_0^TC_0A_0=C'_0,\qquad
 A_0^TC_1A_0+A_1^TC_0A_0+A_0^TC_0A_1=C'_1, \tag{16}
```

with the row equations in (15). This finite polynomial system permits all stabilizer transformations, including those mixing the named active coordinates with the unused radical. Comparing only the displayed active entries is not claimed sufficient. A compact closed-form list of the resulting stabilizer orbits, and any identification stable as $`b`$ grows, remain open.

## Independent review of quadratic equivalence

At exact source the recorded source revision, Independent checks an independent check and an independent check independently accepted the finite covering family and affine equivalence section, conditional on the preceding support theorem and stated module inputs. Both checked the diagonal correction, P6 automorphism action, radical-row representatives and necessity and sufficiency of the full equivalence equations. Both read the exact updated verifier and its two imports and ran `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_n_quadratic_support.py` using the pinned Python 3.12 runtime; the small-order reviewer specified 3.12.14 and extracted all three files from the exact commit. Both J and P6 checks passed. This accepts equivalence of the specified quadratic data, not equivalence of lifted groups or folders, an irredundant orbit list, a stable-range classification, a new primary-source audit or formal certification.

