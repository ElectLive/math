# A class-two J-shadow and N-Frattini exclusion

**Mira Cult**

**Scoped exclusion with independent proof/code reviews below.** Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Put $`P=O_2(G)`$, and suppose $`G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, and


```math
P/\Phi(P)\cong J,\qquad \Phi(P)\cong N
```


as $`\mathbb F_2S_5`$-modules, where $`J=\mathbb F_2^6/\langle\mathbf1\rangle`$ for the six-point action and $`N`$ is the even subspace of the five-point permutation module. In particular the latter assumption says $`\Phi(P)`$ is elementary abelian and central in $`P`$; no centrality in $`G`$, splitting of $`G`$ over $`P`$, or exponent-two loop assumption is made. The conclusion is that no such envelope exists, under the cited envelope inputs. This is a bounded continuation of [C0010](../../claims/0010.md), with no new ID.

The envelope inputs are Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5: $`HP/P=F_{20}`$, the canonical inversion $`\tau`$ fixes $`H`$ pointwise, $`P=(H\cap P)(K\cap P)`$, and the original section fiber over each transposition has size $`|P:H\cap P|/2`$. See [the Frattini-shadow source](bruck-frattini-shadow.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9009bb98c97148e7cf250344f714528b1620b0a9), and [the all-radical constraints](bruck-all-radical-constraints.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6b719ad3026522f93cd9e0e027ae4027f6ee12df). Nagy, [arXiv:0709.4544v1](https://arxiv.org/abs/0709.4544v1), §4, Lemma 4.1, supplies the simple-module identifications and irreducibility on $`F_{20}`$. The argument below and its finite control have the separate exact-source reviews recorded at the end.

Let $`W=H\cap P`$, $`V=P/\Phi(P)`$, and $`Z=\Phi(P)`$. Because $`P=W(K\cap P)`$, $`\tau`$ fixes $`W`$, and $`\tau`$ inverts $`K`$, it fixes $`V`$ pointwise. It also fixes $`Z`$ pointwise: for $`x\in P`$, write $`\tau(x)=xz`$ with $`z\in Z`$. Since $`Z`$ is central elementary abelian, $`\tau(x^2)=(xz)^2=x^2`$. The squares generate $`\Phi(P)`$, because commutators are polarizations of squares in this class-two group. Thus no assumption that $`\tau=1`$ on $`P`$ is used.

The subgroup $`W\cap Z`$ is $`F_{20}`$-invariant. Since $`N|F_{20}`$ is irreducible, it is either zero or all $`Z`$; the latter would put the nontrivial normal subgroup $`Z`$ in $`H`$, contrary to corefreeness. Hence $`W\cap Z=1`$, and $`W`$ injects into $`V`$. The restriction $`J|F_{20}=\mathbf1\oplus S`$, where $`S`$ is the four-dimensional irreducible, so $`w=\dim W`$ is one of $`0,1,4,5`$. The unique $`S`$-submodule is $`M=\mathbb F_2^{6,\mathrm{even}}/\langle\mathbf1\rangle\le J`$.

Fix a transposition $`t`$ and any lift $`g\in G`$. The equation $`\tau(k)k=1`$ for section elements $`k`$ above $`t`$ gives an affine equation $`(1+t)v=c`$ for their shadows $`v\in V`$. The rank of $`1+t`$ on $`J`$ is 2, so there are at most $`2^3`$ possible shadows. For two lifts with the same shadow, their difference is $`z\in Z`$; because $`\tau`$ fixes $`Z`$, their inversion equations differ by $`(1+t)z`$. The rank on $`N`$ is 1, so each shadow has at most $`|C_Z(t)|=2^3`$ solutions. Therefore $`|K_t|\le2^6`$. The original fiber formula gives


```math
|K_t|=|P:W|/2=2^{8-w},
```


because $`|P|=2^9`$. Thus $`w\ge2`$, so $`w\in\{4,5\}`$ and the $`W`$-shadow contains $`M`$.

The square in $`P`$ defines a quadratic map $`q:V\to Z`$, with polarization $`b(v,v')=[\widetilde v,\widetilde v']`$. It is well-defined because $`Z`$ is central elementary, and is $`S_5`$-equivariant: an inner automorphism by an element of $`P`$ acts trivially on both $`V`$ and $`Z`$, so no group-extension splitting is needed. It is nonzero, since its values generate $`Z=\Phi(P)`$.

The standalone [verifier](../code/verify_bruck_j_n_quadratic.py) uses the paired generators


```math
c_5=(1,0,2,3,4),\quad d_5=(0,2,3,4,1),\qquad
 c_6=(1,0,3,2,5,4),\quad d_6=(0,2,3,4,1,5),
```


with entries denoting images of zero-based points. It checks that the paired actions form a faithful group of order 120, constructs a five-cycle normalizer $`F_{20}`$, verifies $`N|F_{20}`$ is irreducible, and checks the two transposition ranks. In the quotient basis for $`J`$, it solves all 60 coefficient variables for equivariant quadratic maps $`J\to N`$, with equations evaluated on the five basis vectors and ten pair sums. The solution space has dimension one. For its nonzero map, the image of the polar form on $`M\times M`$ has rank four, hence is all $`N`$. The verifier also checks equivariance on all 32 vectors and all 120 group elements.

But for any two elements of $`W`$, their commutator belongs to $`W\cap Z=1`$. Thus $`b`$ vanishes on the $`W`$-shadow, which contains $`M`$, contradicting the computed polar rank. This excludes the stated module pair conditional on the cited source inputs and the finite calculation reviewed below. It does not prove $`\Phi(O_2(G))\le Z(G)`$ in general or classify other radical extensions.

From the repository root, with Python 3.11+ and assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_j_n_quadratic.py
```

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/2a25b81e3efe5bdd8a3923e27c94aef16a559094), reviewers contributor 1 and contributor 2 independently accepted the complete proof and standalone certificate under the specified Baumeister–Stein envelope/fiber and earlier module inputs. Each checked both layer actions of τ without splitness, the F20 submodule possibilities, the affine inversion-fiber bound, and the quadratic-square contradiction. Each read and ran the exact certificate with Python 3.12.14: paired group order 120, F20 order 20, transposition ranks 2 and 1, quadratic-map dimension 1 and polar rank 4. Their code reviews checked all 60 coefficient variables, the complete basis/pair constraints, the nullspace and full 120×32 equivariance. No fresh external primary-source audit or classification of other radicals was performed. The earlier precommit review was provisional; these are the exact-source proof/code reviews.
