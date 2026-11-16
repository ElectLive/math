# Uniform linear principal-module support for S₅ envelopes

**Scoped independent mathematical review recorded below.** Let \(m\ge0\) and let \(X\) be a finite-dimensional \(\mathbb F_2S_5\)-module with exactly \(m\) composition factors isomorphic to \(M\), all other composition factors trivial. Then \(X\cong X_0\oplus A\), with \(A\) a sign-only module and \(\dim X_0\le112m\). Here sign-only means that \(A_5\) acts trivially, so \(A\) is a direct sum of copies of the trivial module and the two-dimensional regular \(\mathbb F_2C_2\)-module \(R\).

Under the faithful Baer-envelope hypotheses in the S₅ radical analysis [dependency/context not reproduced in this update: `bruck-s5-radical.md`]—a finite simple exponent-2 right Bruck loop, elementary abelian \(V=O_2(G)\), and \(G/V\cong S_5\)—suppose the principal block of \(V\) has exactly \(m\) \(M\)-factors and its N-block is \(N^a\oplus U^b\), with \(U=N\otimes R\). The proposed consequences are

\[
 \dim V_{\mathrm{principal}}\le328m,\qquad a\le110m+1.
\]

These are linear bounds *in* \(m\), not a bound on \(m\), \(b\), or the total radical. They neither construct an envelope nor assert any splitting of its group extension. No permanent claim ID is allocated; this continues C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].

## Inputs

Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1, gives the absolutely irreducible \(\mathbb F_2S_5\)-modules \(\mathbf1,M,N\) of dimensions \(1,4,4\), and the restrictions to \(F=F_{20}\): \(M|_F\) and \(N|_F\) are isomorphic projective simple modules with endomorphism ring \(\mathbb F_2\). The projectivity of \(U\), separation of the \(N\)-block, and its decomposition as \(N^a\oplus U^b\) are in [bruck-s5-module-blocks.md](bruck-s5-module-blocks.md), reviewed by [model reviewer] at `dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499`. The finite calculation \(\operatorname{Ext}^1_{S_5}(M,M)=0\) is in the dimension-nine analysis [dependency/context not reproduced in this update: `bruck-s5-radical.md#dimension-nine-aggregate-review`], reviewed by the same reviewer at `168f7a4e4cef8e5b6824b58f9cbdaf0ba05f23ea`.

The invariant-functional obstruction used below is in bruck-s5-principal-envelope-bound.md [dependency/context not reproduced in this update: `bruck-s5-principal-envelope-bound.md#proposed-invariant-functional-obstruction`], reviewed at `6a563df3804682acb6bd4191fff2ac749cb0bd16`. The general envelope fiber counts and inequalities are recorded in bruck-s5-v6-fiber-bounds.md [dependency/context not reproduced in this update: `bruck-s5-v6-fiber-bounds.md#two-independent-capacity-inequalities`], with Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Lemmas 4.1 and 4.5, as source. The new arguments in this manuscript are not covered by those prior reviews.

## The projective cover of M

The group algebra \(\mathbb F_2S_5\) is symmetric, so its projective indecomposable modules are injective and each has isomorphic simple head and socle. Since the three simples are absolutely irreducible, the regular module decomposes as

\[
 \mathbb F_2S_5\cong P(\mathbf1)\oplus P(M)^4\oplus P(N)^4.
\]

The reviewed N-block construction gives \(U\) as an indecomposable projective with head \(N\), hence \(P(N)\cong U\) and \(\dim P(N)=8\). Every projective module restricts freely to a Sylow 2-subgroup of order 8, so each projective dimension is a positive multiple of 8. Taking dimensions gives

\[
 \dim P(\mathbf1)+4\dim P(M)=120-4\cdot8=88.
\]

Thus \(\dim P(M)\in\{8,16\}\). Dimension 8 is impossible: its head and socle would be copies of \(M\), leaving an extension of \(M\) by \(M\); the cited Ext vanishing would split it, contradicting indecomposability. Therefore \(\dim P(M)=16\) and \(\dim P(\mathbf1)=24\).

If \(Q^{S_5}=0\) and \(Q\) has \(m\) \(M\)-factors and otherwise trivial factors, then \(\operatorname{soc}Q\cong M^r\) for some \(r\le m\). Embed its socle in the injective module \(P(M)^r\) and extend this map to \(Q\). Every nonzero submodule of the finite-length module \(Q\) meets its socle, so the extended map has zero kernel. Thus

\[
 \dim Q\le16m.
\]

## Splitting off unsupported sign summands

Let \(A_{\max}\) be the sum of all submodules of \(X\) whose composition factors are trivial. Each such submodule is \(A_5\)-trivial: its group image is a 2-group and \(A_5\) is perfect. Their sum is therefore also \(A_5\)-trivial, so \(A_{\max}\cong\mathbf1^u\oplus R^v\). The quotient \(Q=X/A_{\max}\) is fixed-free: otherwise the preimage of a fixed line would have only trivial composition factors, hence would be sign-only and strictly larger than \(A_{\max}\). It has the same \(m\) \(M\)-factors, so \(\dim Q\le16m\).

The extension class of \(0\to A_{\max}\to X\to Q\to0\) is a tuple in

\[
 \operatorname{Ext}^1(Q,\mathbf1)^u\oplus\operatorname{Ext}^1(Q,R)^v.
\]

Independent invertible row operations among the trivial copies and among the \(R\)-copies support these tuples on at most \(e_1=\dim\operatorname{Ext}^1(Q,\mathbf1)\) and \(e_R=\dim\operatorname{Ext}^1(Q,R)\) copies respectively; the remaining sign-only summands split. By Shapiro, since \(R\cong\operatorname{Ind}_{A_5}^{S_5}\mathbf1\),

\[
 e_1=\dim H^1(S_5,Q^*),\qquad e_R=\dim H^1(A_5,Q^*).
\]

Both \(S_5\) and \(A_5\) are two-generated, so each cocycle space has dimension at most \(2\dim Q\), and so do the corresponding cohomology spaces. The supported summand \(X_0\) therefore satisfies

\[
 \dim X_0\le\dim Q+e_1+2e_R\le7\dim Q\le112m.
\]

This decomposition is a module statement. It does not remove the sign summand from an envelope or assert that \(X_0\) is indecomposable.

## Consequences for an envelope

Write \(V=X_0\oplus A\oplus Y\), where \(A=\mathbf1^u\oplus R^v\), \(Y=N^a\oplus U^b\), and \(d_0=\dim X_0\). Let \(W=H\cap V\), \(P\cong C_5\), and \(F=N_{S_5}(P)\). The intersection \(W\cap A\) is \(F\)-invariant and hence \(S_5\)-invariant because the two actions on \(A\) have the same sign image; core-freeness gives \(W\cap A=0\). Also \(Y^P=0\). Thus projection embeds \(W^P\) in \(X_0^P\). P-averaging is exact, so \(\dim X_0^P=d_0-4m\).

Put \(h_0=\dim\operatorname{Hom}_{S_5}(X_0,\mathbf1)\). The cited invariant-functional obstruction, followed by P-averaging, gives

\[
 h_0+u+v\le \dim W^P\le d_0-4m.
\]

Consequently

\[
 \dim V_{\mathrm{principal}}=d_0+u+2v
 \le 3d_0-8m-2h_0\le328m.
\]

For the N-block, \(\operatorname{soc}Y=N^{a+b}\). Every \(F\)-submodule of this socle is \(S_5\)-invariant: the common irreducible \(N|_F\) has endomorphism ring \(\mathbb F_2\), and its multiplicity subspaces define the same \(S_5\)-submodules. Hence \(W\cap\operatorname{soc}Y=0\). Let \(\dim[P,W]=4c\). Projection from \([P,W]\) to the P-nonfixed part of \(V/\operatorname{soc}Y\) is injective; the latter has \(m+b\) copies of the unique projective simple \(F\)-module. Thus \(c\le m+b\).

For a transposition \(t\), put \(\rho=\operatorname{rank}(1+t|X_0)\). Rank is superadditive on subquotients and each \(M\) has rank 2, so \(\rho\ge2m\). The full transposition rank is \(r=\rho+v+a+4b\). The cited fiber count gives \(r\le\dim W+1=\dim W^P+4c+1\), and therefore

\[
 a\le\dim W^P+4m+1-\rho-v
 \le d_0-2m+1-v\le110m+1.
\]

These deductions use the N-block only as a module and use no quotient by it as a loop. They leave the possible number of \(M\)-factors and the projective multiplicity \(b\) open.

## Independent review

GPT-6.1 Terra reviewer [model reviewer] accepted this argument at exact source `32b5918c4b3fa3b2686185006b80d41b1ece76aa`, conditional on the cited prior Ext, block and envelope inputs. The review checked the symmetric-algebra projective-cover dimensions, socle embedding in an injective hull, maximal sign-only quotient and Ext-row support, including m=0. It checked the invariant-functional injection, P-fixed projection and core-free socle argument for the envelope bounds, with no quotient-loop assumption. Neither m nor U multiplicity nor total radical dimension is bounded; this is a structural support result, not an envelope classification. No computation or formal verification was used.
