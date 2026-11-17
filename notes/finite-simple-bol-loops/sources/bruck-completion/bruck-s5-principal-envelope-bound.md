# Candidate principal-block bound for S₅ envelopes

**Mira Cult**

**Scoped independent mathematical review recorded below.** Let $`(G,H,K)`$ be the faithful Baer envelope of a finite simple exponent-2 right Bruck loop, with elementary abelian $`V=O_2(G)`$ and $`G/V\cong S_5`$. If $`V`$ has exactly one composition factor $`M`$, then its $`\{\mathbf1,M\}`$-block has dimension at most 19. No bound on the $`N`$-block or total radical dimension is asserted, and this is not an existence or classification theorem.

This continues [C0010](../../claims/0010.md) and allocates no new claim ID. It uses the envelope conventions and restrictions in [bruck-s5-radical.md](bruck-s5-radical.md); the N/principal block decomposition and its scoped review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499) in [bruck-s5-module-blocks.md](bruck-s5-module-blocks.md); and the one-$`M`$ module bounds reviewed at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9) in [bruck-s5-principal-one-m.md](bruck-s5-principal-one-m.md). Those reviews do not certify the new envelope deduction below.

## Proposed invariant-functional obstruction

Put $`W=H\cap V`$, with $`\pi(H)=F_{20}`$. The restriction map

```math
\mathop{\mathrm{Hom}}\nolimits_{S_5}(V,\mathbf1)\longrightarrow
\mathop{\mathrm{Hom}}\nolimits_{F_{20}}(W,\mathbf1)
```

is injective. For suppose a nonzero invariant functional $`\lambda:V\to\mathbf1`$ vanishes on $`W`$. The subgroup $`L=\ker\lambda`$ is normal in $`G`$, and $`G/L`$ is a central $`C_2`$-extension of $`S_5`$. Since $`H\cap L=W`$, the image $`H/W`$ complements its kernel over $`F_{20}`$. A transposition section involution remains an involution in $`G/L`$, so restriction of its extension class to a transposition subgroup also vanishes.

These two restrictions jointly detect $`H^2(S_5,\mathbf1)`$. Specifically, Akita–Kawasaki–Satoh, [*Presentations of Schur covers of braid groups*](https://doi.org/10.1515/jgth-2023-0014), *J. Group Theory* **27** (2024), §2.1 and Theorem 2.2, give the two-dimensional central-extension space and spin presentation; Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 3.1, gives an order-eight lift of the $`C_4`$ in $`F_{20}`$. The sign-square class restricts nontrivially to a transposition and trivially to $`C_4`$, while the spin class with involutory transposition lifts restricts nontrivially to $`C_4`$. This detection was used in the reviewed radical argument at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/65c54aff108cc70208bf6f7271b1e5cf6a0a76bc) and in the one-factor obstruction at [the source revision](https://github.com/Mira-Cult/math-wip/commit/71f7eae94a6d7ce43563047929bd0be7e8fe1285) as recorded there. Thus $`G/L\cong C_2\times S_5`$.

A projection to the kernel $`C_2`$ is nonzero on $`V/L`$. Its restriction to $`H/W\cong F_{20}`$ is either zero or the sign character; adding sign if necessary makes it vanish on $`H`$ while retaining its nonzero kernel restriction. Because $`K`$ generates $`G`$, its restriction to $`K`$ is nontrivial. It is a loop homomorphism to $`C_2`$, since a product of section representatives differs from the representative of the loop product by an element of $`H`$. The loop has order $`6\cdot2^{d-w}\ge6`$, so this is a proper nontrivial quotient, contradicting simplicity. The argument does not assume that a module summand splits as a subgroup of $`G`$.

## Bounding the principal block

Assume there is exactly one $`M`$ factor. The cited module results give an $`S_5`$-decomposition

```math
V=X_0\oplus A\oplus Y,\qquad
A\cong\mathbf1^a\oplus R^b,
```

where $`X_0`$ is the indecomposable principal-block summand containing $`M`$, $`R`$ is the 2-dimensional regular sign module, and $`Y`$ is the $`N`$-block. Put $`m_0=\dim C_{X_0}(P)=\dim X_0-4`$, for $`P\cong C_5`$ normal in $`F_{20}`$, and $`h_0=\dim\mathop{\mathrm{Hom}}\nolimits_{S_5}(X_0,\mathbf1)`$. The equality for $`m_0`$ follows from semisimplicity of $`P`$ and the single nontrivial 4-dimensional $`P`$-factor. The N-block has no $`P`$-fixed vectors.

The subspace $`W\cap A`$ is $`F_{20}`$-invariant and hence $`S_5`$-invariant, because both groups act on $`A`$ through the same sign quotient. Core-freeness gives $`W\cap A=0`$. The $`P`$-idempotent splits $`W`$, and projection embeds $`W^P`$ into $`C_{X_0}(P)`$: a vector in the kernel lies in $`W\cap A`$, since $`C_Y(P)=0`$. Thus $`\dim W^P\le m_0`$. Invariant functionals on $`X_0\oplus A`$ vanish on $`[P,W]`$, so the proposed injectivity gives

```math
h_0+a+b\le\dim W^P\le m_0.
```

Consequently

```math
\dim(X_0\oplus A)\le\dim X_0+2(m_0-h_0)
=3\dim X_0-8-2h_0.
```


Apply the maximal sign-submodule and support calculation of [bruck-s5-principal-one-m.md](bruck-s5-principal-one-m.md) to the indecomposable $`X_0`$ itself: its split-off sign summand must be zero. Write its supported extension as

```math
0\longrightarrow \mathbf1^\alpha\oplus R^\beta
\longrightarrow X_0\longrightarrow Q\longrightarrow0.
```

For $`Q=M,J,V_6`$, the reviewed support ranges are respectively
$`\alpha\le1,2,1`$, with $`\beta\le2`$ in every case; the corresponding dimensions of $`\mathop{\mathrm{Ext}}\nolimits^1(Q,\mathbf1)`$ are $`e_1=1,2,1`$, and $`h_Q=\dim\mathop{\mathrm{Hom}}\nolimits_{S_5}(Q,\mathbf1)`$ is $`0,1,1`$. Applying $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(-,\mathbf1)`$ to the extension gives

```math
h_0\ge \max\{h_Q,\ h_Q+\alpha+\beta-e_1\},
```

because $`\dim\mathop{\mathrm{Hom}}\nolimits_{S_5}(\mathbf1^\alpha\oplus R^\beta,\mathbf1)=\alpha+\beta`$. Substitution in $`3\dim X_0-8-2h_0`$, using $`\dim X_0=\dim Q+\alpha+2\beta`$, gives maxima 15, 19 and 19 for $`Q=M,J,V_6`$, respectively. Thus the principal block has dimension at most 19. The pushout argument, Hom–Ext refinement and bound have the scoped review below; the bound is not claimed sharp. The later [indecomposable filter](bruck-s5-principal-indecomposables.md) sharpens it to 14 under the same envelope hypotheses.

## Scoped independent review

reviewer contributor 1 accepted the invariant-functional obstruction and principal-block bound 19 at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6a563df3804682acb6bd4191fff2ac749cb0bd16), conditional on the recorded prior inputs. The review checked the central pushout and jointly detected restrictions, sign-adjusted proper loop quotient, P-idempotent projection and core-freeness, restriction injectivity, and the Hom–Ext refinement giving maxima 15, 19 and 19. This bounds only the principal block under the exactly-one-M hypothesis; the N-block and total radical remain unbounded. No unrestricted envelope classification or formal verification follows.
