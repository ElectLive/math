# Candidate exclusion of primitive SD₃ left multiplication groups

**Mira Cult**

The A₅ counting argument has received scoped independent model review under the stated upstream hypotheses; the all-PSL₂(q) extension also has scoped independent review as recorded below. It is a manuscript-local attack on [C0010](../../claims/0010.md), using the [C0014](../../claims/0014.md) diagonal setup. It allocates no new claim ID and changes no claim status, and it assumes the exact canonical folder and inversion results noted below. Independent mathematical review is required.

## A₅ case

**Proposition (candidate).** No finite nonassociative left Bol loop has a primitive left multiplication group of simple diagonal type with socle $`B=T_1\times T_2\times T_3\cong A_5^3`$.

**Proof.** Put $`G=\mathop{\mathrm{LMlt}}\nolimits(Q)`$, $`H=G_1`$, $`K=\{L_x:x\in Q\}`$. Primitivity implies loop simplicity: a proper nontrivial normal subloop would give a nontrivial $`G`$-invariant partition by quotient fibres. The left nucleus is consequently trivial, by the canonical C0001 nucleus result; the C0007 inversion argument gives an involutory automorphism $`\tau`$ of $`G`$ with $`\tau(k)=k^{-1}`$ for $`k\in K`$. Use an external semidirect product $`\widetilde G=G\rtimes\langle t\rangle`$, with $`t^2=1`$ and $`tgt=\tau(g)`$, and put $`\Lambda=tK`$. The Bol folder identities give: $`\Lambda`$ consists of involutions, is invariant under conjugation by $`B`$, and $`\Lambda^2\cap H=\{1\}`$. In the SD₃ action we may identify the factors so that $`H\cap B=\Delta(T)`$, $`T=A_5`$, and $`|\Lambda|=[G:H]=|T|^2=3600`$.

The action of $`\Lambda`$ on $`B`$ by conjugation is injective. Indeed $`C=C_G(B)`$ is normal in the primitive group $`G`$, so if nontrivial it is transitive. Since $`B`$ is transitive, $`C`$ is semiregular: an element of $`C`$ fixing one point fixes every point. Thus $`C`$, if nontrivial, is regular. The centralizer in the symmetric group of a regular group is regular, so the transitive group $`B`$, which centralizes $`C`$, would also be regular. This contradicts $`B\cap H=\Delta(T)\ne1`$. Hence $`C_G(B)=1`$, and two elements of the coset $`tG`$ inducing the same automorphism on $`B`$ differ by an element of this trivial centralizer.

Write $`\mathcal I`$ for the unique $`T`$-class of 15 involutions of $`A_5`$. The primary ATLAS page cited below records $`\mathop{\mathrm{Aut}}\nolimits(A_5)=S_5`$; elementary cycle counting gives 25 involutions in $`S_5`$: ten transpositions and fifteen double transpositions. For each nonidentity involution $`\alpha\in\mathop{\mathrm{Aut}}\nolimits(T)`$, the set $`(\alpha^T)^2`$ contains $`\mathcal I`$. To see this, if $`\alpha`$ is a transposition choose two disjoint transpositions in its $`A_5`$-class; their product is a double transposition. If $`\alpha`$ is a double transposition choose two distinct nonidentity elements of a Klein four subgroup of $`A_5`$; their product is a double transposition. Since $`(\alpha^T)^2`$ is invariant under $`T`$-conjugacy, it contains all of $`\mathcal I`$.

Each $`\lambda\in\Lambda`$ induces either the identity or a transposition on the three simple factors. If it preserves all factors, write its restrictions $`(\alpha_1,\alpha_2,\alpha_3)`$, each of order at most two. The square $`(\lambda^B)^2`$ is the direct product $`\prod_i(\alpha_i^T)^2`$, viewed as a subset of $`B`$. If all three restrictions are nonidentity, then $`(v,v,v)\in(\lambda^B)^2\cap\Delta(T)`$ for any $`v\in\mathcal I`$, a contradiction. Thus at least one restriction is the identity. Among the 26 involutions-or-identity in $`S_5`$, at most

```math
26^3-25^3=3\cdot26^2-3\cdot26+1=1951
```

factor-preserving automorphisms satisfy this requirement.

Now suppose $`\lambda`$ swaps the first two factors and fixes the third. For an arbitrary isomorphism $`\theta:T_1\to T_2`$ and an involutory automorphism $`\alpha`$ on the third factor, its action is

```math
\phi(x_1,x_2,x_3)=(\theta^{-1}(x_2),\theta(x_1),\alpha(x_3)).
```

For $`b,c\in B`$, the product of the two conjugates of $`\lambda`$ equals

```math
(b\lambda b^{-1})(c\lambda c^{-1})=b\,\phi(b^{-1}c)\,c^{-1}.
```

Assume $`\alpha\ne1`$. Choose $`v\in\mathcal I`$ and $`g\in T`$ such that $`g^{-1}\theta(v)g=v`$; this is possible because $`\theta(v)`$ belongs to the unique involution class. Take $`b=(1,g^{-1},b_3)`$ and $`c=(v,g^{-1},c_3)`$. The first two coordinates of the displayed product are $`(v,g^{-1}\theta(v)g)=(v,v)`$. Independently choose $`b_3,c_3`$ so that the third coordinate $`b_3\alpha(b_3^{-1}c_3)c_3^{-1}`$ is $`v`$, possible since $`v\in(\alpha^T)^2`$. Thus $`(v,v,v)\in\Lambda^2\cap H`$, contradiction. Consequently $`\alpha=1`$. For each of the three possible transposed factor pairs, the swap is specified by at most $`|\mathop{\mathrm{Aut}}\nolimits(T)|=120`$ choices of $`\theta`$, so there are at most 360 such actions.

Injectivity now gives $`|\Lambda|\le1951+360=2311<3600`$, contradiction. ∎

## Candidate generalization: one involution class

Let $`T`$ be a finite nonabelian simple group with a single class $`\mathcal I`$ of involutions. Suppose, for every nonidentity involutory $`\alpha\in\mathop{\mathrm{Aut}}\nolimits(T)`$, that $`\mathcal I\subseteq(\alpha^T)^2`$. The identical argument yields the necessary condition

```math
|T|^2\le 3(i+1)^2-3(i+1)+1+3|\mathop{\mathrm{Aut}}\nolimits(T)|,
```

where $`i`$ is the number of involutions in $`\mathop{\mathrm{Aut}}\nolimits(T)`$. C0014 §3 proposes a proof of the stated square-class property using Glauberman's $`Z^*`$-theorem; this invocation and the generalization have not been independently reviewed here. The A₅ proof above uses elementary cycle calculations instead.

## Candidate extension: all PSL₂(q)

**Proposition (candidate, conditional on the cited repository results).** Let $`q=p^f\ge4`$ be a prime power and $`T=\mathop{\mathrm{PSL}}\nolimits_2(q)`$. There is no finite nonassociative left Bol loop whose left multiplication group is primitive of simple diagonal type with socle $`T^3`$, assuming the nucleus-normality, inverting-automorphism and Bol-folder statements used in the A₅ argument above. This is an exclusion for one primitive type and family, not a classification of finite simple Bol loops.

The following square-class lemma supplies the hypothesis in the preceding general counting argument.

**Lemma.** Let $`T`$ be a finite nonabelian simple group with a single conjugacy class $`\mathcal I`$ of involutions. For every nonidentity involution $`\alpha\in\mathop{\mathrm{Aut}}\nolimits(T)`$, one has $`\mathcal I\subseteq(\alpha^T)^2`$, where products are taken in $`\mathop{\mathrm{Aut}}\nolimits(T)`$, identifying $`T`$ with its inner automorphism group.

**Proof.** Put $`M=\langle T,\alpha\rangle`$. If $`N=O_{2'}(M)`$, then $`N\cap T=1`$: it is normal in the nonabelian simple group $`T`$, which has even order (or use that an odd-order group is solvable). Hence $`[N,T]\le N\cap T=1`$. As the centralizer of the inner automorphism group in $`\mathop{\mathrm{Aut}}\nolimits(T)`$ is trivial, $`N=1`$. Likewise $`Z(M)=1`$, so $`Z^*(M)=1`$.

Choose a Sylow 2-subgroup $`S`$ of $`M`$ containing $`\alpha`$. Glauberman's $`Z^*`$-theorem, for example the consequence of Theorem 4 cited below, gives a distinct $`M`$-conjugate $`\beta\in S`$ of $`\alpha`$. Since $`M=T\langle\alpha\rangle`$, the $`M`$- and $`T`$-conjugacy classes of $`\alpha`$ coincide. Set $`r=\alpha\beta`$; its order is $`2^e`$ for some $`e\ge1`$, since $`r\in S`$ and $`\alpha\ne\beta`$. Both $`\alpha`$ and $`\beta`$ invert $`r`$. For every integer $`k\ge0`$, the involution $`\alpha r^k`$ is a conjugate in $`\langle\alpha,\beta\rangle`$ of $`\alpha`$ when $`k`$ is even and of $`\beta`$ when $`k`$ is odd: explicitly $`\alpha r^{2m}=r^{-m}\alpha r^m`$, and $`\alpha r^{2m+1}=r^{-m}\beta r^m`$. Both lie in $`\alpha^T`$. Thus $`r^k=\alpha(\alpha r^k)\in(\alpha^T)^2`$. In particular $`r^{2^{e-1}}`$ is an involution in this square. The square lies in $`T`$, because $`M/T`$ has order at most two. It is invariant under $`T`$-conjugation, so it contains the entire unique class $`\mathcal I`$. ∎

For $`T=\mathop{\mathrm{PSL}}\nolimits_2(q)`$, let $`d=(2,q-1)`$, $`n=|T|=q(q^2-1)/d`$, and let $`i`$ be the number of involutions in $`\mathop{\mathrm{Aut}}\nolimits(T)`$. The standard group facts in Guralnick–Zieve, Appendix, give a unique involution class in $`T`$, and

```math
\mathop{\mathrm{Aut}}\nolimits(T)=\mathop{\mathrm{P\Gamma L}}\nolimits_2(q),\qquad |\mathop{\mathrm{Aut}}\nolimits(T)|=dfn.
```

Its Lemma A.3 gives $`q^2-(2-d)`$ involutions in $`\mathop{\mathrm{PGL}}\nolimits_2(q)`$. If $`f`$ is odd, these are all the involutions in $`\mathop{\mathrm{Aut}}\nolimits(T)`$. If $`f`$ is even, put $`s=p^{f/2}=\sqrt q`$. The only nonidentity field projection of an involution is $`\sigma:x\mapsto x^s`$. Every involution in $`\mathop{\mathrm{PGL}}\nolimits_2(q)\sigma`$ is conjugate to $`\sigma`$ by $`\mathop{\mathrm{PGL}}\nolimits_2(q)`$. Indeed, write one as $`[A]\sigma`$. Its square being projectively trivial says $`A\sigma(A)=cI`$. Associativity gives $`\sigma(c)=c`$, and the norm $`\mathbb F_q^*\to\mathbb F_s^*`$ is onto, so rescaling $`A`$ makes $`A\sigma(A)=I`$. Matrix Hilbert 90 gives $`A=B\sigma(B)^{-1}`$, as required. The projective centralizer of $`\sigma`$ is $`\mathop{\mathrm{PGL}}\nolimits_2(s)`$: if $`\sigma(B)=aB`$, then $`a\sigma(a)=1`$, and scalar Hilbert 90 rescales $`B`$ to a matrix fixed by $`\sigma`$. Hence the number in that coset is

```math
\frac{|\mathop{\mathrm{PGL}}\nolimits_2(q)|}{|\mathop{\mathrm{PGL}}\nolimits_2(s)|}=s(s^2+1).
```

Consequently the exact count is

```math
i=q^2-(2-d)+\begin{cases}0,&f\text{ odd},\\ s(s^2+1),&f\text{ even}.\end{cases}
```

The conjugacy statement also follows from the explicitly stated Lang-theorem consequence in Guralnick–Zieve, Appendix, immediately after Lemma A.5.

By the lemma and the general counting argument above, the assumed folder would require

```math
n^2\le 3(i+1)^2-3(i+1)+1+3dfn. \tag{*}
```

We show the reverse strict inequality. For $`q\ge8`$, $`i+1\le(5/3)q^2`$: if $`f`$ is even this follows from $`\sqrt q(q+1)+1\le(2/3)q^2`$, and if $`f`$ is odd it is immediate. Also $`f\le q`$, $`d\le2`$, and $`n\ge q(q^2-1)/2`$. Therefore the right side of (*) is strictly below

```math
\frac{25}{3}q^4+6qn<n^2.
```

For the last inequality, use $`n-6q\ge q(q^2-13)/2>0`$ and

```math
n(n-6q)\ge\frac{q^2(q^2-1)(q^2-13)}4>\frac{25}{3}q^4,
```

where $`(q^2-1)(q^2-13)>100q^2/3`$ for $`q\ge8`$. The remaining prime powers $`4\le q<8`$ are $`4,5,7`$: for $`q=4,5`$, $`(n,i,|\mathop{\mathrm{Aut}}\nolimits(T)|)=(60,25,120)`$ and the right side of (*) is $`2311<3600=n^2`$; for $`q=7`$, $`(n,i,|\mathop{\mathrm{Aut}}\nolimits(T)|)=(168,49,336)`$, giving $`8359<28224=n^2`$. This contradicts (*). ∎

**Source and review notes.**

- George Glauberman, “Central Elements in Core-Free Groups,” *Journal of Algebra* **4** (1966), 403–420, Theorem 4, p. 403, https://doi.org/10.1016/0021-8693(66)90030-5. The accessible publisher PDF states Theorem 4 explicitly; its conclusion gives a distinct conjugate in the same Sylow 2-subgroup. This is the source of the distinct-conjugate consequence used above.
- Robert M. Guralnick and Michael E. Zieve, “Polynomials with PSL(2) monodromy,” *Annals of Mathematics* **172** (2010), 1315–1359, Appendix, Lemma A.3 and the automorphism discussion immediately before Lemma A.5 and the Lang-theorem discussion immediately after Lemma A.5, https://doi.org/10.4007/annals.2010.172.1315, https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf. These state the involution counts and conjugacy, the automorphism group, and the field-coset conjugacy, respectively.
- Donald L. White, “Character degrees of extensions of PSL₂(q) and SL₂(q),” *Journal of Group Theory* **16** (2013), 1–33, §2, https://doi.org/10.1515/jgt-2012-0026, is a published alternative source for the automorphism structure.
- This argument has received scoped independent review at the source recorded below. It relies on the manuscript's general counting argument and upstream repository results, which this draft does not reprove. It allocates no claim ID.

## Exact repository dependencies

The canonical nucleus, inversion and folder results invoked above are C0001 Theorems 1.4–1.5 and 2.2 and C0007 Theorem 1.1. The initial source examined was [the source revision](https://github.com/Mira-Cult/math-wip/commit/79b70a50b19bc728b349a2a6ed2bd958391e8b6e); the scoped review below applies only to its stated source and scope. The A₅ automorphism structure is recorded on the [ATLAS A₅ page](https://brauer.maths.qmul.ac.uk/Atlas/alt/A5/); the involution counts are also derived directly above.

## Scoped independent review

reviewer contributor 1 examined exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/66d1f655f5e8f57a04ec82a851113f2d1f1ee386) and accepted the A₅ counting argument conditional on the invoked nucleus-normality and inversion results in C0001 and C0007. Scope: centralizer and injectivity, both factor-action cases, swap-product calculation, and the count 2311 < 3600. The reviewer did not independently audit those upstream results or the general PSL₂ source premises. This is not claim-wide review of C0014, nor a classification result.

reviewer contributor 2 accepted the all-PSL₂(q) extension at exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/65c54aff108cc70208bf6f7271b1e5cf6a0a76bc), conditional on the invoked C0001/C0007 results. Scope: the square-class lemma, field-coset Hilbert 90 count, SD₃ counting cases and all parameter inequalities. The reviewer directly inspected Guralnick–Zieve Lemma A.3; the full Glauberman publisher text was inaccessible to that reviewer, who corroborated the standard isolated-involution consequence. The producer separately inspected the publisher’s Theorem 4 statement. No claim-wide upstream review is implied.
