# Six-point shadow with semisimple Frattini module

**Mira Cult**

**Scoped theorem with exact-source proof/code reviews below.** Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Assume $`G/P\cong S_5`$, where $`P=O_2(G)`$ has class at most two and exponent at most four. Suppose $`V=P/\Phi(P)`$ is the six-point permutation module $`P_6=\mathbb F_2^6`$, and $`Z=\Phi(P)`$ is elementary abelian, central in $`P`$, and semisimple as an $`S_5`$-module. The conclusion is that **$`Z\le Z(G)`$**. No splitting of $`G`$ over $`P`$, exponent-two loop assumption, or quotient-folder assumption is made. This continues [C0010](../../claims/0010.md), without a new permanent ID.

Use the envelope and original-fiber inputs from Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, in the form recorded in [the Frattini-shadow manuscript](bruck-frattini-shadow.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9009bb98c97148e7cf250344f714528b1620b0a9) and [the all-radical constraints](bruck-all-radical-constraints.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6b719ad3026522f93cd9e0e027ae4027f6ee12df). The related J-shadow/N-Frattini result and its module interfaces are reviewed in [bruck-j-n-frattini-exclusion.md](bruck-j-n-frattini-exclusion.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/2a25b81e3efe5bdd8a3923e27c94aef16a559094). These are input reviews; the new deduction and verifier have the separate exact-source reviews below.

Write $`W=H\cap P`$, $`T=W\cap Z`$, and $`U=WZ/Z\le V`$. The source gives $`P=W(K\cap P)`$, $`HP/P=F=F_{20}`$, and canonical inversion $`\tau`$ fixing $`H`$ pointwise. It follows that $`\tau`$ fixes $`V`$ pointwise. It fixes $`Z`$ as well: if $`\tau(x)=xz`$, with $`z\in Z`$, then $`\tau(x^2)=(xz)^2=x^2`$, and the squares generate $`\Phi(P)`$, since commutators are their polarizations. The square defines an $`S_5`$-equivariant quadratic map $`q:V\to Z`$ whose values generate $`Z`$, with polarization $`b(v,v')=[\widetilde v,\widetilde v']`$. This equivariance does not require a split extension, since $`P`$ acts trivially on $`V`$ and $`Z`$.

Nagy, [arXiv:0709.4544v1](https://arxiv.org/abs/0709.4544v1), Lemma 4.1, gives the binary simple modules $`\mathbf1,M,N`$, with $`M,N`$ four-dimensional and restricting to the same absolutely irreducible projective $`F`$-module $`S`$. Write


```math
Z=\mathbf1^c\oplus M^a\oplus N^b. \tag{1}
```


The [standalone verifier](../code/verify_bruck_p6_frattini.py) computes that the spaces of equivariant quadratic maps $`P_6\to M`$ and $`P_6\to N`$ each have dimension one. Since the values of $`q`$ generate $`Z`$, this forces $`a,b\le1`$: the images in multiple copies of either simple lie in one diagonal copy. Thus it is enough to exclude the cases $`a+b>0`$ with $`a,b\in\{0,1\}`$, allowing arbitrary $`c`$.

The subspace $`T`$ is $`F`$-invariant and contains no nonzero $`S_5`$-submodule by corefreeness. The trivial part is its $`C_5`$-fixed part and hence vanishes: any such vector lies in $`\mathbf1^c`$, which is central in $`G`$. Every $`F`$-submodule of the pure $`M`$ or $`N`$ component is $`S_5`$-invariant, so $`T`$ meets each pure component trivially. If $`a+b=1`$, this gives $`T=0`$. If $`a=b=1`$, then $`T`$ is either zero or the four-dimensional graph of the unique nonzero $`F`$-intertwiner $`M\to N`$.

Let $`w=\log_2|W|`$, $`d=\dim V=6`$, and let $`\rho_V,\rho_Z`$ be the ranks of $`1+t`$ for a transposition $`t`$. Because $`\tau`$ fixes $`V,Z`$, the inversion equation on the fiber over $`t`$ has at most $`2^{d-\rho_V}`$ possible shadows, with at most $`2^{\dim Z-\rho_Z}`$ lifts for each. Comparing with the original fiber count $`|P:W|/2`$ gives


```math
w\ge \rho_V+\rho_Z-1. \tag{2}
```


This holds for arbitrary lifts and a nonsplit $`G`$. The verifier checks $`\rho_V=3`$, $`\rho_M=2`$, $`\rho_N=1`$. As an $`F`$-module, $`V=\mathbf1^2\oplus S`$; its unique $`S`$-submodule is the even-sum space on the five-point $`F`$-orbit.

If $`a+b=1`$, then $`T=0`$, so $`W`$ injects into $`V`$. Equation (2) gives $`\dim W\ge3`$, forcing its shadow to contain $`S`$. But $`q(U)\subseteq T=0`$, while the verifier finds that the unique nonzero quadratic map to either $`M`$ or $`N`$ takes values spanning the target on $`S`$. This is a contradiction.

Suppose $`a=b=1`$. Then (2) gives $`w\ge5`$. The verifier checks that on $`S`$ the polar form of the unique map to $`M`$ is zero, while that of the unique map to $`N`$ has rank four. Since $`b(U,U)\subseteq T`$, $`U`$ cannot contain $`S`$: neither zero nor the mixed graph contains a nonzero pure $`N`$-vector. Thus $`U\le V^F=\mathbf1^2`$. If $`T=0`$, then $`w=\dim U\le2`$, a contradiction. Consequently $`\dim T=4`$ and $`w=5`$ or $`6`$.

For $`w=5`$, the original transposition fiber has size $`2^{8+c}`$, exactly the maximum number of solutions to $`\tau(k)k=1`$: there are at most $`2^3`$ shadows and $`2^{5+c}`$ lifts per shadow. Thus the whole inversion-solution fiber is selected. The verifier finds $`\dim(T\cap C_Z(t))=1`$. Multiplication by a nonzero element of this intersection preserves inversion, but it is an element of $`H`$, creating a transversal collision. Hence $`w\ne5`$.

For $`w=6`$, $`U=V^F`$. Define


```math
f:V\to Z,\qquad f(v)=\tau(p)p^{-1}\quad(p\Phi(P)=v).
```


It is well-defined and linear because $`\tau`$ fixes $`V,Z`$ and $`Z`$ is central. It is $`F`$-equivariant because $`\tau`$ fixes the actual $`H`$-lifts of $`F`$, and $`f(U)=0`$ because $`\tau`$ fixes $`W`$. For an element of $`K\cap P`$, inversion requires $`q(v)=f(v)`$. Project this equation to $`M\oplus N`$. The restriction $`q_M|S`$ is an $`F`$-linear isomorphism, and each of $`\mathop{\mathrm{Hom}}\nolimits_F(S,M)`$, $`\mathop{\mathrm{Hom}}\nolimits_F(S,N)`$ is one-dimensional. Thus the two projected components of $`f`$ have exactly four choices. The verifier evaluates the projected inversion equation on all 64 vectors, including cross-polar terms with $`U`$, and obtains solution counts $`14,4,4,14`$. Therefore at most 14 shadows can occur in $`K\cap P`$.

For each shadow, transversality allows at most $`|Z:T|=2^{4+c}`$ section elements. Consequently


```math
|K\cap P|\le14\cdot2^{4+c}<2^{8+c}=|P:W|,
```


contradicting $`P=W(K\cap P)`$ and the section property. This completes the exclusion of all $`a+b>0`$, so the semisimple $`Z`$ is trivial as an $`S_5`$-module and is central in $`G`$. The argument establishes neither centrality without these hypotheses nor existence of the remaining central cases.

The verifier uses the synchronized five- and six-point generators from the J/N control, checks the faithful group of order 120, constructs $`F_{20}`$, checks its simple submodules and the transposition ranks, solves both 84-variable quadratic systems, computes the mixed graph and evaluates all four residual cases. Run from the repository root with Python 3.11+ and assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_p6_frattini.py
```

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/54aec585a4311d67571500965fbf63d42b1a7e99), reviewers contributor 1 and contributor 2 independently accepted the entire proof and standalone certificate, conditional on the cited original-envelope/fiber and module inputs. Both checked the complete semisimple multiplicity reduction with arbitrary c, the allowed intersections T, the nonsplit inversion-fiber bounds, pure cases, mixed w=5 saturation and w=6 equivariant shear argument. Both read and ran the pinned code using Python 3.12.14, checking the exhaustive 84-variable systems, unique mixed graph, full vector/group equivariance and residual counts 14,4,4,14. No fresh primary-source audit, quotient-folder assumption, formal verification or centrality assertion outside the stated hypotheses is part of these reviews.
