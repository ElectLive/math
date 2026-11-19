# Every central subgroup of every finite odd group as the nuclear translations inside LMlt

**Mira Cult**

For a loop $`Q`$ put $`R=\operatorname{Nuc}_r(Q)`$ and

```math
B_{\mathrm{in}}(Q)=\{r\in R: R_r\in D=\operatorname{LMlt}(Q)\}.
```

Always $`B_{\mathrm{in}}(Q)\le Z(R)`$: the nuclear right translations are exactly the permutation centralizer of $`D`$, the ones in $`D`$ are precisely $`Z(D)`$, and each such permutation centralizes the entire nuclear right translation group. Also $`|R|\mid |Q|`$ by its free right action.

**Classification of this intrinsic pair.** For every finite odd group $`R`$ and every specified subgroup $`B\le Z(R)`$, there is a finite simple non-Moufang left Bol G-loop of odd order with identified right nucleus $`R`$ and $`B_{\mathrm{in}}(Q)=B`$ **as a subgroup of that $`R`$**. No divisibility, direct-summand or elementary-abelian assumption on the inclusion is needed. The loop contains a finite simple centerless-left-multiplication base loop as a subloop. The base and larger loops have literally the same nuclear elements and multiplication, but the translations by the specified $`B`$ become native left-multiplication permutations only in the larger ambient loop. Thus the necessary central-subgroup condition is the only restriction on this pair, if the proof is verified. This does **not** classify the loops themselves or their minimum degrees. The case $`B=1`$ is the [separately frozen arbitrary-odd-nucleus construction](all-odd-groups.md); below $`B\ne1`$.

## 1. An integral module detecting every signed normal subgroup of the base

We use the transfer and the explicit graph factorization of that source, with its field prime chosen away from $`|R|`$. Here are the parameter changes and the needed extra assertion. Choose an odd prime $`p\nmid 3\cdot7 |R|`$ with $`p\bmod7\in\{2,4\}`$. For an elementary existence proof choose an even $`M`$ divisible by all excluded primes other than $`7`$ and satisfying $`M^2\equiv2\bmod7`$. Each prime divisor of $`M^2+7`$ is odd, different from $`7`$ and from the excluded primes, and is a quadratic residue mod $`7`$ by quadratic reciprocity $`(-7/q)=(q/7)`$. Not all its prime divisors can be $`1\bmod7`$, hence one is suitable.

Use $`k=\mathbb F_{p^3}`$, $`F_0=k^+\rtimes C_7`$, a seventh root scalar and primitive $`c\in k^\times`$. Replace the eleventh Frobenius in the preceding construction by the $`p`$th Frobenius $`a`$ (with $`z\mapsto z^p`$), use $`\theta=c a`$ on the additive group (and $`z\mapsto z^p`$), and $`a_2=\theta a\theta^{-1}`$. The proof still applies: $`\operatorname{ord}_7(p)=3`$; $`\theta^3`$ is a scalar of order $`p-1`$; $`a_2^i a^{-i}`$ for $`i=1,2`$ is a scalar of order $`p^2+p+1>7`$. Use the same two coordinatewise graph factors over the regular $`R`$-set $`\Omega`$; the auxiliary group is $`P=(F_0^\Omega\times F_0^\Omega)\rtimes(C_3\times R)`$. Choose an odd prime $`\ell\equiv1\bmod p`$, $`\ell\nmid |P|`$ (a divisor of $`\Phi_p(m)`$ for a multiple $`m`$ of $`2p|P|`$ works). The same two addressed trace covectors have $`49|R|`$ weights, span the dual and supply the faithful prime-field $`\ell`$-module $`V`$, with no condition on the primes of $`R`$. The arguments for the exact factors, all normal cuts and normalizers do not otherwise depend on $`p=11`$.

Write the resulting group and factors $`Y=W\rtimes(V\rtimes P)=K_f J_f`$, and write

```math
\bar D=Y^2,\quad \bar H_0=K_f\times J_f,\quad D=\langle d_y=(y,y^{-1})\rangle,\quad
 H_0=D\cap\bar H_0,\quad \tau=\text{swap}.
```

Use the finite simple base $`Q_0=D/H_0`$. Its right nucleus is identified with $`R`$ by the actual marks $`d_r`$, $`r`$ a pure group element. The subgroups $`K_f,J_f`$ are *both normalized* by every such pure $`r`$: it normalizes $`S`$ and belongs to $`T`$ on the two auxiliary graph sides. Hence $`d_r`$ normalizes both $`\bar H_0`$ and $`H_0`$. These representatives give all $`N_D(H_0)/H_0`$, with $`d_rH_0\,d_sH_0=d_{rs}H_0`$ in that quotient, as well as genuine native multiplication. $`D`$ is centerless.

We construct, for the additive coefficient ring $`S_B=\prod\mathbb Z/b_i`$ with additive group identified with $`B`$ (each $`b_i`$ a prime power), a finite free $`S_B`$-module $`M`$ with $`Y`$-action preserving a perfect symmetric form, such that

```math
[A,M]=M \quad\text{for every }1\ne A\triangleleft Y.
                  \tag{2}
```

Here brackets denote the subgroup spanned by action differences, not the assertion that a single element has invertible difference on all of $`M`$.

In the coefficient group write $`P=N_0\rtimes L`$ with $`N_0=(k^+\times k^+)^\Omega`$ and $`L=(C_7\times C_7)^\Omega\rtimes(C_3\times R)`$. To deal correctly with the inner coefficient conjugations in $`Y`$, **untwist the coordinates**: send $`(w,(v,h))`$ to $`(f,(v,h))`$ in $`P^V\rtimes(V\rtimes P)`$ with pure affine permutation of the $`V`$-sites, where $`f(x)=w(x)h`$. This is a true homomorphism: multiplications of these new coordinate functions include the factor $`h`$ exactly where the conjugation $`h w' h^{-1}`$ occurred in the old law. The signed balance condition here is $`\prod_x\bar f(x)=\bar h^{|V|}`$ in $`P_{\mathrm{ab}}`$. Because $`N_0\le P'`$, this permits the split expression $`Y=N_*\rtimes L_*`$, $`N_*=N_0^V`$, with $`L_*`$ the same condition on $`L`$-valued $`f`$ together with the full affine coordinate. It acts faithfully on $`N_*`$: any nonidentity affine permutation moves a site, and at fixed sites the local $`L`$-action is faithful as checked for the base.

Each nonzero $`Y`$-normal subgroup $`A`$ meets $`N_*`$ nontrivially, since otherwise it centralizes $`N_*`$ and lies in $`C_Y(N_*)=N_*`$. Pick a nonzero component of $`A\cap N_*`$ at one field summand (one $`V`$-site, one $`\Omega`$-address, one wing). There is an independent scalar seven there in $`L_*`$: this local seven is in $`P'`$, so its single-site word is balanced. Its difference isolates a nonzero vector in that summand, whose orbit spans the whole summand over $`\mathbb F_p`$. Pure translations move the $`V`$-site freely, and an arbitrary element of $`R`$ can act at a selected site with a balancing inverse at another. Thus $`A`$ contains the entire sum of these field summands over *all* sites and addresses of at least one wing.

Let $`\Lambda`$ be the set of actual $`\mathbb F_p`$-valued weights of $`N_*`$ supported on one site and one address there with the two nonzero trace forms $`\operatorname{Tr}(x)`$ and $`\operatorname{Tr}(c^{-1}y)`$ independently shifted by seventh roots. All $`49|R||V|`$ such weights are preserved as a set by $`L_*`$ via the dual action, using the Frobenius adjunction above. On each weight take a copy of $`E_0=\ker(\sum:S_B^p\to S_B)`$, with coordinate-cycle $`z`$. Its ordinary dot product is perfect because the constant line splits orthogonally ($`p`$ a unit on $`B`$). For every $`j\ne0\bmod p`$, $`z^j-1`$ has no nonzero kernel on $`E_0`$ and hence is invertible. Define $`M=\bigoplus_{\lambda\in\Lambda}E_0`$; $`N_*`$ acts on the $`\lambda`$ term by $`z^{\lambda(n)}`$ and $`L_*`$ permutes the terms by its actual weight action, so this is a representation by isometries. For every nonzero $`A`$ as above, on *each* weight choose a vector in its included full wing giving a nonzero exponent; acting on an input supported at that weight fills it by differences. This proves (2) even when the coefficient group is not elementary or has several primary components.

For every nontrivial $`\tau`$-stable normal $`I\triangleleft D`$, its pure subgroup $`\{y:(y,1)\in I\}`$ is a nontrivial normal subgroup of $`Y`$. Indeed if it were zero the first projection would centralize $`Y'`$ by commutators with $`Y'\times1`$. But $`C_Y(Y')=1`$: an affine component moving a site fails to centralize $`W\le Y'`$, and an element of $`W`$ centralizing $`Y'`$ is trivial by translated constants and $`Z(P)\cap P'=1`$ as in the base proof. Swap then also kills the second projection. Consequently (2) detects every such $`I`$ on a pure coordinate. This is the main reason an arbitrary faithful module, or a group algebra in bad characteristic, is not substituted here.

## 2. Symplectic central insertion and genuine marked squares

Put $`L_B=S_B^2\otimes M\otimes M`$, all tensors over $`S_B`$. Take on $`S_B^2`$ the perfect alternating determinant form $`j`$. Use on $`L_B`$ the perfect alternating form

```math
\beta(s\otimes m\otimes n,s'\otimes m'\otimes n')
       = j(s,s')\,\langle m,n'\rangle\,\langle n,m'\rangle .
```

Let $`(y_1,y_2)\in\bar D`$ act by the separate tensor actions of $`y_1,y_2`$ on $`M,M`$. This form is twisted invariant: $`\beta(gx,\tau(g)y)=\beta(x,y)`$; alternation follows from the skew first factor and symmetric flip pairing. Take $`U=L_0\oplus L_1=L_B\oplus L_B`$, with the indicated representation on $`L_0`$, its $`\tau`$-twist on $`L_1`$, and $`\tau`$ interchanging the two halves. The form $`\omega((x,y),(x',y'))=\beta(x,y')+\beta(y,x')`$ is perfect alternating, symplectic under the whole extension $`\bar D\rtimes\langle\tau\rangle`$, and the halves are complementary Lagrangians. By (2), for every $`1\ne I\triangleleft D`$ stable under $`\tau`$, $`[I,U]=U`$: the nontrivial pure coordinate subgroup fills the active tensor factor in each $`L_j`$, and inputs may be chosen separately in each half. In particular the action of $`D`$ on $`U`$ is faithful (its kernel is a signed normal). Form the Heisenberg group $`N=U\times B`$, product $`(u,z)(u',z')=(u+u',z+z'+\omega(u,u')/2)`$; $`N'=Z(N)=B`$, since the form is perfect and takes values spanning $`S_B`$. All actions fix $`B`$. Put $`D'=N\rtimes D`$.

Enlarge the old stabilizer to $`J=H_0\{d_b:b\in B\}\le N_D(H_0)`$. This really is a subgroup with $`J/H_0=B`$: $`B\le Z(R)`$ is abelian and these marks form an actual subgroup, with trivial intersection with $`H_0`$. Let $`\psi:J\to B`$ be this quotient map in the prescribed identification. Use the **coupled** point stabilizer

```math
H'=\{(x,\psi(j))j : x\in L_0,\ j\in J\}.
```

It is a subgroup since $`J`$ preserves $`L_0`$, which is isotropic, and fixes the central phases. Thus $`H'\cap N=L_0`$ on its zero sheet and $`H'\cap D=H_0`$. The number of its elements is $`|L_B||B||H_0|=|C_{D'}(\tau)|`$. Set $`\mathcal C=\tau^{D'}`$ in $`D'\rtimes\langle\tau\rangle`$; all outside involutions are here by Sylow conjugacy. The proposed mark set $`\mathcal K=\mathcal C\tau`$ is the whole $`\tau`$-inverted set.

For two actual signs projecting to involutions $`a,b'`$ in $`D\tau`$, each lift has zero central phase and an actual negative vector for its projected involution: the square is zero precisely under these conditions since $`2`$ is invertible. In their product the vector summands are anti-fixed by $`a`$ and $`c=a b' a`$, respectively. If the sum lies in $`L_0`$, for a common $`y\in L_1`$ they are $`ay-y`$ and $`-cy+y`$: each sign swaps the two Lagrangians, so a negative vector is fixed by its second half. The central carry is zero, since $`\omega(sy,y)=0`$ for every symplectic involution $`s`$ (apply it to both arguments and use alternation), and same-half pairings vanish. Thus a marked product in $`H'`$ must project to $`\ker\psi=H_0`$. The old folder excludes every nonidentity signed product there. At identity projection the two negative spaces are the same and contain no nonzero vector in $`L_0`$, so the product itself is identity. This proves $`H'\cap\mathcal C^2=1`$, hence all conjugate stabilizers avoid the difference set $`\mathcal K^{-1}\mathcal K`$. The matching size makes $`\mathcal K`$ sharply transitive; sandwich closure gives the left Bol operation.

These are the true faithful generating permutations. The generated even marks form a normal subgroup of $`D'`$ (the even part of the normal sign-class-generated group), contain the pure base marks and therefore $`D`$, and their commutators with $`N`$ cover $`N/B=U`$. Their intersection with $`N`$ then contains $`B=[N,N]`$ since $`B`$ is central, hence contains all of $`N`$. Any normal subgroup inside $`H'`$ meeting $`N`$ nontrivially would have a nonzero zero-sheet vector in $`L_0`$; some commutator with $`N`$ would be nonzero in $`B`$, whereas $`H'\cap B=1`$. A normal subgroup in $`H'`$ disjoint from $`N`$ centralizes $`N`$ and has trivial top by faithfulness on $`U`$. Thus $`D'=\operatorname{LMlt}(Q')`$. Its center is $`B`$ since $`D`$ is centerless and $`Z(N)=B`$. Also the map $`dH_0\mapsto dH'`$ embeds $`Q_0`$ as an actual subloop: its marks are the same pure group elements, their products differ from the unique old product marks by elements of $`H_0\le H'`$, and $`H'\cap D=H_0`$. The degree increases by exactly $`|L_B|`$.

## 3. Simplicity, the nuclear pair, and all isotopes

Use the [odd complete-inverted strict-cut criterion](../../extraspecial-cores/signed-cut-test.md) on the just-established faithful group. For a nontrivial signed normal $`C\le N`$, put $`B_0=C\cap B`$ and let $`A`$ be the image in $`U`$. If $`A\ne0`$, some commutator with $`N`$ is nonzero in $`B_0`$ by perfectness. If $`A=0`$, then $`B_0=C\ne1`$. For fixed image in $`A^\tau`$ every lift in $`C`$ is fixed: writing $`\tau(x)=xz`$ with $`z\in B_0`$ gives $`z^2=1`$ since $`\tau`$ fixes $`B_0`$. Moreover $`a\mapsto a+\tau a`$ injects $`A\cap L_0`$ into $`A^\tau`$. Therefore

```math
|C_C(\tau)|=|B_0|\,|A^\tau|>|A\cap L_0|\ge |C\cap H'|.
```

Here $`H'\cap N`$ has no nonzero phase. No splitting of any mixed normal subgroup is needed. If $`C`$ projects onto $`1\ne I\triangleleft D`$, then $`[I,U]=U`$ implies $`C\cap N`$ surjects to $`U`$ by commutating arbitrary lifts with $`N`$, so contains $`N`$ by $`N'=B`$. For proper $`C`$ we now have proper $`I`$, and

```math
\frac{|C_C(\tau)|}{|C\cap H'|}
   =\frac{|B||C_I(\tau)|}{|J\cap I|}>1,
 \qquad |J\cap I|\le |B||H_0\cap I|.
```

The base has the strict inequality for every such $`I`$ by its original simplicity. This covers every signed normal; the constructed loop is simple. The base already embeds as a non-Moufang subloop.

For the normalizer, $`H'\cap N=L_0`$ on the zero sheet. Since $`D`$ preserves $`L_0`$, a normalizing element $`n d`$ must have $`n\in L_0\times B`$ by nondegeneracy of the pairing against $`L_0`$; every such $`n`$ does normalize $`H'`$ since all phase contributions on $`L_0`$ vanish. A pure $`d\in D`$ normalizes $`H'`$ iff it normalizes $`J`$ and fixes $`\psi`$, hence it normalizes $`H_0=\ker\psi`$. Conversely each $`d\in N_D(H_0)`$ preserves the inverse image $`J`$ of the specified subgroup $`B`$ and fixes $`\psi`$ because its action on $`N_D(H_0)/H_0=R`$ is inner and $`B\le Z(R)`$. Consequently

```math
N_{D'}(H')/H'
 \ \cong\ (B\times R)/\{(b,b):b\in B\}
 \ \xrightarrow{\ [(z,r)]\mapsto z^{-1}r\ }\ R .
```

In particular all the original actual marks $`d_r`$ remain nuclear, with their original operation by the embedding; they exhaust the new nucleus. For $`b\in B`$ the product $`(0,b)d_b`$ belongs to $`H'`$ and $`d_b H'=(-b)H'`$. The nuclear right translation represented by this normalizing point acts by right coset multiplication by $`d_b`$, hence by the same permutation as the *left* action of the central phase $`-b`$. Conversely every nuclear right translation lying in $`D'`$ lies in its center $`B`$. This identifies the original prescribed subgroup pointwise up to the exhibited inverse map on the phase labels, without changing its specified inclusion in $`R`$.

Finally we must prove the G-loop property, not inherit it from a general extension. Extend to $`\bar D'=N\rtimes Y^2`$ and $`\bar J=\bar H_0\{d_b:b\in B\}`$, with quotient map $`\bar\psi:\bar J\to B`$ extending $`\psi`$. Use $`\bar H'=\{(x,\bar\psi(j))j:x\in L_0,\ j\in\bar J\}`$. This is legitimate in the pure-coordinate ambient actions already defined; $`D'\triangleleft\bar D'`$, $`\bar H'\cap D'=H'`$, and the two coset degrees agree, so $`\bar D'`$ acts on the same points. The full diagonal $`\Delta Y`$ was regular on $`\bar D/\bar H_0`$ since $`K_f\cap J_f=1`$ and $`|Y|`$ equals that degree. Thus $`|\bar J\cap\Delta Y|=|B|`$ by $`\bar D=\Delta Y\,\bar H_0`$. The full fixed group of $`\tau`$ in $`\bar D'`$ has size $`|L_B||B||Y|`$. Its intersection with $`\bar H'`$ has size $`|B|`$: the fixed vector diagonal meets $`L_0`$ only at zero, and over each diagonal $`j\in\bar J`$ there is exactly its prescribed central phase. The fixed group is therefore transitive on all $`|L_B||Y|`$ loop points, and it conjugates the true $`\mathcal K`$ to itself since it centralizes the sign and preserves $`D'`$. For each $`a\in\mathcal K`$ take $`x\in\langle a\rangle`$ with $`x^2=a^{-1}`$; choose fixed-group $`s`$ with $`xs`$ stabilizing the native identity point. Its conjugation takes $`\mathcal K`$ onto $`x\mathcal K x^{-1}=x^2\mathcal K=a^{-1}\mathcal K`$ by sandwich closure and inversion. This is exactly [Nagy's G-loop criterion, Lemma 2.3](https://arxiv.org/pdf/math/0703919). Replacing the full fixed group by the diagonal of the generated group without checking transitivity would not be justified.

**Checks and boundaries.** [Independent-of-the-proof finite-mechanism script](../code/verify_central_nuclear_insertion.py), [stdout](../checks/central-nuclear-insertion.out): real two-wing $`C_7:C_3`$ permutation tensors over $`\mathbb Z/9`$; all 441 projected signed pairs and 386 off-Lagrangian nonzero phases; all 59,049 actual quotient products for a nonabelian order-81 target whose central $`C_3=3C_9`$ is nonsummand; all 36 swap-stable images in a small symplectic kernel; and true diagonal/stabilizer intersections on the independent Nagy 1053 folder (the latter is only an orbit-mechanism test). No fully enumerated large loop table, no priority, and no independent signoff yet on this extension or its universal input. The abelian-specific phase, mixed and two-sheet mechanisms have separate narrower records; this proof does not retroactively review them.

[Review and replication](../verification.md) · [Right nuclei](../README.md)
