# Arithmetic count and isotope rigidity at the first odd two-prime degree

**Research proof; see the scope of verification.** [Verification and provenance](../VERIFICATION.md).

Let $`p,q`$ be distinct odd primes with $`p\mid q-1`$ and $`f=\mathrm{ord}_q(p)`$. At the proposed first order $`n=p^{1+\mathrm{lcm}(p,f)}q`$ the prior results give one standard loop unless $`f`$ is even and $`p\nmid f`$. In this exceptional range put $`Q=p^{f/2}`$. For each $`1\le s<f/2`$ put
```math
    e_s=\gcd(Q+1,p^s-1),\qquad
    D_s=p^{\gcd(f,2s)}-1,\qquad C_s=(Q+p^s-2)/2 .
```
Form the explicitly arithmetic subset
```math
 {\mathcal A}_s=\{\,j\bmod e_s:
          D_s\nmid (1+p^s)(C_s+(Q-1)j)\,\}
```
and the permutation $`\pi_s(j)=p j+(p-1)/2\bmod e_s`$. Then the exact number of isomorphism classes is
```math
                   p+1+\sum_{s=1}^{f/2-1}\left|\mathcal{A}_s / \langle\pi_s\rangle\right|.\qquad\mathrm{(1)}
```
There are no field-element searches or isomorphism tests in (1). If desired the summand is the integer
```math
 \frac1f\sum_{v=0}^{f-1}
       \ \sum_{j\in{\mathcal A}_s}
       \mathbf{1}_{\,e_s\mid (p^v-1)j+(p^v-1)/2},
```
since $`\pi_s^f=1`$. **Every loop at the first exponent is a G-loop**, i.e. isomorphic to each of its loop isotopes. So this also counts isotopy classes, not only based classes. For $`(3,61),(7,43),(3,193),(5,601)`$ the respective answers are $`8,12,11,20`$. No assertion is made about all larger orders or exact graph deletion radii.

## 1. Why isotopy gives no extra identifications

For any of the exceptional charts use the notation $`D,H,T,t`$ of 6247a009. We have $`H\cap C_D(t)=1`$: in the upper group $`J\cap C_X(t)`$ is trivial since $`J=B_2\rtimes P`$ and $`C_X(t)`$ is the diagonal $`q`$-axis. In $`N`$ the intersection is trivial since $`H\cap N`$ is the zero lift of a Lagrangian disjoint from $`U^+`$. Also $`|H|=|C_D(t)|=p^{d+1}q`$ and $`|D|=(p^{d+1}q)^2`$. Hence $`C_D(t)`$ acts regularly on the physical coset space $`D/H`$. It conjugates $`T`$ to itself. Moving the distinguished point while retaining $`T`$ therefore does not change the resulting based loop up to isomorphism.

One must also allow changing the distinguished row of the square. Normalizing at row $`a\in T`$ gives left translations $`T a^{-1}`$ on the original symbol space, followed by a choice of base point. There is $`b\in T`$ with $`b^2=a`$, by odd-order power closure. The equality $`bTb=T`$ follows from sandwich closure in both directions; hence $`Ta^{-1}=bTb^{-1}`$. Conjugating this normalized family back by $`b`$ merely changes the choice of point, already handled. All loop isotopes arise by such row normalization and point choice up to common relabeling. The standard abelian-core class is also a G-loop by [Nagy, *A class of simple proper Bol loops*, Proposition 3.2](https://arxiv.org/pdf/math/0703919), since its known construction is the actual faithful exact-factorization folder. This argument makes no assertion that different based classes with abstractly isomorphic left multiplication groups are necessarily isotopic.

## 2. Reduce the multiplicity-two charts

Let $`K=\mathbb F_{p^f}`$, $`\bar x=x^Q`$, and write $`S=\langle\alpha,p\bmod q\rangle`$. In the previous chart each label is $`a_i=\alpha^{r_i}p^{s_i}`$. The signed involution $`t`$ requires the multiset of the two labels to be invariant under
```math
                    (r,s)\longmapsto(r,-s).
```
The simultaneous axis relabeling of the chart by $`\alpha^u p^v`$ changes every $`r_i`$ by **the same** $`-2u`$ and no $`s_i`$; it also permutes the two coordinate names where applicable. This follows by checking $`F b_1=(b_1')^{\alpha^u p^v}F`$ at its target site $`j+u`$. The row-stabilizer's distinguished axis is preserved, so no further automorphism interchanges the two $`s`$ orientations after they have been assigned to their actual labels. Rescale the central coordinate first so that $`\lambda=1`$: replacing $`\omega`$ by $`\omega/\lambda`$ and taking multiplier $`1/\lambda`$ is literally the chart equivalence. Subsequent equivalences therefore have multiplier one.

Write $`H(x,y)=x^T M\bar y`$ for the skew-Hermitian form on the multiplicity space (not the group stabilizer in this calculation). Site permutations introduce no signs. Prime-field trace isometry of a semilinear component with Frobenius $`\sigma`$ entails the corresponding form identity with values conjugated by $`\sigma`$, by varying the first input over $`K`$ and applying trace duality.

**Both labels fixed under the displayed involution.** A label with $`s=f/2`$ cannot occur. On its multiplicity block the site reversal has a common shift and the coefficient action $`T_0`$ is involutive and semilinear for field conjugation, with $`H(T_0x,T_0y)=\overline{H(x,y)}`$. Hence $`H(T_0x,x)=\overline{H(x,T_0x)}`$ and also its negative, so $`H(x,T_0x)=0`$. On a distinct-label single coordinate this contradicts nondegeneracy. If both labels are equal in this case, take $`x`$ spanning the isotropic chart line. Transversality requires $`x,T_0x`$ be independent, and both are isotropic; their cross-value zero would make the form degenerate. Thus only $`s_1=s_2=0`$ survives.

For distinct labels the coefficient of $`t`$ on each coordinate is a scalar $`\varepsilon_i=\pm1`$ (its square is one). The form has diagonal entries only, each nonzero with $`\bar c_i=-c_i`$. The isotropic chart line therefore has both coordinates nonzero. Rescaling coordinates makes it $`K(1,1)`$, with $`M=\mathrm{diag}(c,-c)`$. After this normalization the remaining common scalar rescales $`c`$ by an arbitrary norm $`K^\times\to\mathbb F_Q^\times`$, so all nonzero such $`c`$ are equivalent. The intersection with $`tL`$ is zero exactly when $`\varepsilon_1\ne\varepsilon_2`$: the two site reversals yield the equation that a sequence equals $`\varepsilon_1\varepsilon_2`$ times its translate. A nonzero constant sequence works for equal signs; for opposite signs iterating an odd number $`p`$ of times forces zero. Normalize the **plus** label to $`r=0`$. Its minus partner has any $`r\in\mathbb F_p^\times`$. These $`p-1`$ based classes are different: after matching plus to plus, only a common $`r`$-shift is allowed, and Frobenius fixes the signs. A coordinate name-swap does not change which physical label has the positive eigenvalue.

For two equal labels normalize them both to $`r=0`$. The multiplicity involution $`T_0`$ is now $`K`$-linear; its chart line and its image under $`T_0`$ must differ. For a generator $`v`$ of the line use basis $`(v,T_0v)`$. Both vectors are isotropic, their cross-value $`c\ne0`$ satisfies $`c=-\bar c`$ by invariance and skew-Hermitian symmetry, and the action is the literal swap. A common scalar norm again removes $`c`$. This gives exactly **one** repeated-label exceptional class. Together with the standard class and distinct-label fixed pairs, the subtotal is $`p+1`$.

## 3. The transposed-label cases and cyclic arithmetic

The other possibility has $`s_2=-s_1\ne s_1`$. Fix once and for all the representative $`s`$ of $`\{s,-s\}`$ in $`1,\ldots,f/2-1`$. The two labels have the same $`r`$, normalized to zero by a site shift, and are now in the fixed order $`p^s,p^{-s}`$. Residual chart equivalences have only simultaneous axis factor $`p^v`$ with no site shift; they cannot exchange the two **fixed numerical** labels. Write $`\sigma(x)=x^{p^s}`$. As for distinct labels, normalize the chart line to $`K(1,1)`$ and the matrix to $`\mathrm{diag}(k,-k)`$ with $`\bar k=-k`$. The shared site reversal is $`j\mapsto-j`$. Its action on a two-vector is
```math
                (x,y)\longmapsto
                (c\, y^\sigma,\ (c^{-1})^{\sigma^{-1}}x^{\sigma^{-1}}).
```
The second coefficient is forced by $`t^2=1`$. These maps preserve the trace form exactly when
```math
                            c\bar c=-k^\sigma/k.                        \qquad\mathrm{(2)}
```
For example the second-coordinate contribution, mapped to the first, transforms trace of $`k c\bar c (x\bar y)^\sigma`$ into trace of $`-k x\bar y`$; trace duality gives (2). The first-to-second equation is its involutory counterpart. The common line is transverse to its image iff there is no nonzero $`x\in K`$ with $`c x^\sigma=(c^{-1})^{\sigma^{-1}}x^{\sigma^{-1}}`$; this is equivalent to
```math
                         x^{p^{2s}-1}=c^{-(1+p^s)}.                     \qquad\mathrm{(3)}
```
The site reversal does not couple these tests between sites, since independent scalars on all sites of the chart line are allowed.

The only remaining coordinate transformation sends both coordinates to $`w x^{p^v}`$ for one common $`w\in K^\times`$. The common scalar is forced by preservation of the diagonal line once the distinct labels are fixed. It sends $`c`$ to $`w c^{p^v}/w^\sigma`$ and $`k`$ to $`k^{p^v}/(w\bar w)`$. Choose a generator $`g`$ of $`K^\times`$, of order $`M=Q^2-1`$, and normalize $`k=k_0=g^{(Q+1)/2}`$. This is anti-fixed since $`k_0^{Q-1}=-1`$; all anti-fixed $`k`$ are obtained by common norms, also when $`p\mid f`$. No normalization of the scalar $`\lambda=1`$ is lost.

Putting $`c=g^C`$, equation (2) is precisely
```math
               C=C_s+(Q-1)j\pmod M,\qquad j\bmod Q+1.
```
With no Frobenius change, the residual $`w`$ has norm one, so its exponent is a multiple of $`Q-1`$. Its action on $`j`$ is addition by a multiple of $`1-p^s`$, giving just $`j\bmod e_s`$. Condition (3) on this cyclic group of size $`M`$ is **solvable** iff $`D_s\mid(1+p^s)C`$. Its negation is exactly the displayed definition of $`\mathcal A_s`$ (independent of representative by the actual norm-one gauges).

For the $`p`$-Frobenius change, choose $`w=g^{(p-1)/2}`$ to restore $`k_0`$ because $`w\bar w=k_0^{p-1}`$. The resulting $`C'`$ is $`p C+(1-p^s)(p-1)/2`$, hence $`j'=p j+(p-1)/2\bmod e_s`$. All other restoring scalars differ by a norm-one factor already quotiented. This exhausts the full marked equivalence for this unordered label type and yields precisely its summand in (1). Different $`s`$ types cannot be identified by the allowed common $`r`$-shifts or label-preserving Frobenius maps. Together with Section 2 this proves the count, conditional only in the stated upstream sense.
