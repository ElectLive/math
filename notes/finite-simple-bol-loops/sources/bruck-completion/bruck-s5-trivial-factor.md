# Candidate trivial-factor obstruction for S₅ envelopes

**Mira Cult**

**Scoped independent mathematical review recorded below.** Let $`(G,H,K)`$ be the faithful Baer envelope of a finite simple exponent-2 right Bruck loop. Suppose $`V=O_2(G)`$ is elementary abelian and $`G/V\cong S_5`$. Then the $`\mathbb F_2S_5`$-module $`V`$ has a trivial composition factor.

This manuscript continues [C0010](../../claims/0010.md), allocates no claim ID, and uses the stabilizer, section and fiber facts from [bruck-s5-radical.md](bruck-s5-radical.md). The proposed conclusion concerns the stated elementary-abelian radical and does not classify its extensions or the loops.

## Dependencies

Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1, lists the simple $`\mathbb F_2S_5`$-modules $`\mathbf1,M,N`$, describes their actions and shows both four-dimensional modules restrict to the same projective irreducible $`F_{20}`$-module. The [dimension-nine radical argument](bruck-s5-radical.md) records a scoped independent review at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/168f7a4e4cef8e5b6824b58f9cbdaf0ba05f23ea) of the finite calculations $`H^1(S_5,M\otimes M)=0`$ and $`H^2(S_5,M)=0`$, and of the relevant module identifications. The [radical-bound argument](bruck-s5-radical.md) supplies the separately reviewed $`H^2(S_5,N)=0`$. The [N-block manuscript](bruck-s5-module-blocks.md) records a scoped independent review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499) of separation of the $`N`$-block from the $`\{\mathbf1,M\}`$-block, the decomposition of an $`N`$-only module as $`N^a\oplus U^b`$, and projectivity of $`U=N\otimes\mathbb F_2C_2`$. The reviews are separate; none reviewed the new deduction below.

## Proposed proof

Suppose $`V`$ has no trivial composition factor. By the N-block decomposition and $`\mathop{\mathrm{Ext}}\nolimits^1_{S_5}(M,M)\cong H^1(S_5,M\otimes M)=0`$, induction on a composition series gives

```math
V\cong M^c\oplus N^a\oplus U^b.
```

Here $`M`$ is self-dual, and $`U\cong\mathop{\mathrm{Ind}}\nolimits_{A_5}^{S_5}(N|_{A_5})`$ is projective. The cited vanishings and additivity give $`H^2(S_5,V)=0`$, so $`G=V\rtimes S_5`$.

Write $`W=H\cap V`$. All $`F_{20}=\pi(H)`$ composition factors of $`V`$ are the same projective irreducible 4-dimensional module. The quotient $`V/W`$ is therefore projective: its composition series splits because each simple factor is projective. Thus $`H^1(F_{20},V/W)=0`$. The subgroup $`H/W`$ is a complement to $`V/W`$ in the preimage of $`F_{20}`$ modulo $`W`$; conjugating by $`V`$ makes it the standard complement. Hence we may assume $`H=W\rtimes F_{20}`$.

Let $`t`$ be a transposition and $`T=\langle t\rangle`$. The restriction $`M|_T`$ is free: its dimension is 4 and $`\mathop{\mathrm{rank}}\nolimits(1+t)=2`$. The module $`U|_T`$ is free because $`t`$ swaps its two four-dimensional summands. Thus

```math
H^1(T,V)\cong H^1(T,N)^a\cong(\mathbb F_2^2)^a.
```

For $`t=(12)`$, a vector of the even-weight five-point module $`N`$ fixed by $`t`$ has equal first two coordinates. Modulo $`(1+t)N=\langle e_1+e_2\rangle`$, it is identified with an even-weight triple on the other three points. The $`S_3`$ factor in $`C_{S_5}(t)=T\times S_3`$ acts on that 2-dimensional space as $`GL_2(\mathbb F_2)`$, diagonally on the $`a`$ copies. A tuple spanning one line has orbit size 3, a tuple spanning the whole plane has orbit size 6, and zero is the only fixed tuple. This includes $`a=0`$, when the space is zero.

In the split group every involution above $`t`$ is a translate of the pure involution $`t`$ by a vector fixed by $`t`$. Its $`V`$-conjugacy class is determined by its cohomology class in $`H^1(T,V)`$ and has size $`2^r`$, where $`r=\mathop{\mathrm{rank}}\nolimits(1+t)`$. The $`K`$-fiber is conjugacy invariant; the $`S_3`$-orbits above therefore partition the selected $`V`$-classes. The envelope fiber count gives

```math
|K\cap tV|=2^{d-w-1},\qquad q=2^{d-w-1-r},
```

where $`q`$ is the number of selected $`V`$-orbits. It is an integer. Modulo 3, a union of the displayed $`S_3`$-orbits has size 0 if it omits zero and 1 if it contains zero. If the exponent of 2 in $`q`$ is odd, $`q\equiv2\pmod3`$, impossible. If it is even, $`q\equiv1\pmod3`$, so the zero class is selected. In the chosen splitting, that class contains the pure transposition $`t`$. Conjugacy then puts every pure transposition in $`K`$. Two disjoint pure transpositions multiply to a double transposition in $`F_{20}\le H`$, contradicting the transversal property.

This proves the proposed obstruction, conditional on the cited inputs and independent review. In particular, the argument does not infer that $`W\cap(1+t)V=0`$ forces $`W`$ to be $`S_5`$-invariant. Nagy's construction in arXiv:0709.4544v1, Lemmas 4.2–4.3 and Theorem 5.2, uses a nonsplit $`N`$-block and has a trivial composition factor, so it is compatible with this obstruction.

## Scoped independent review

reviewer contributor 1 accepted the trivial-factor obstruction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), under the displayed envelope hypotheses and cited reviewed inputs. The review checked the M-only semisimplicity and block decomposition, H² vanishings, F20 normalization, free restrictions of M and U, S3 orbit lengths and the mod-3 forced pure-transposition collision. The conclusion requires a trivial composition factor; it does not remove any sign-only summand from an envelope. This is independent model review, not human or formal certification.
