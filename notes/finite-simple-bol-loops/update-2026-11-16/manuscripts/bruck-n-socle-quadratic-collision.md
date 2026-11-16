# A quadratic marked collision on two socle copies

**Theorem with scoped independent reviews, continuing of 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`].** In the faithful simple nonassociative Bruck-envelope setting of the N-Frattini marked-rank theorem [dependency/context not reproduced in this update: `bruck-n-frattini-marked-rank.md`], assume \(G/P\cong S_5\), \(P\) has class at most two and exponent at most four, \(Z=\Phi(P)\cong N\), and
\[
 V=P/Z\cong X\oplus U^b,\qquad X\in\{J,P_6\}.
\]
Let \(W=H\cap P\), and let \(c\) be the \(N|_{F_{20}}\)-multiplicity of the intersection of its shadow with \(\operatorname{soc}(U^b)\). Then the bound is
\[
 c\le1.                                                             \tag{1}
\]
Subject also to the exceptional J normal form [dependency/context not reproduced in this update: `bruck-j-exceptional-normal-form.md`] at exact source `5325d80926fe96073e800134e60fe9902f15bcce` and its separately recorded independent reviews, this excludes the entire \(X=J\) branch of the displayed N-Frattini hypotheses. It does not exclude \(P_6\) or classify the remaining Bruck envelopes.

The marked identity and its \(d=0\) consequence are from the marked-rank source [dependency/context not reproduced in this update: `bruck-n-frattini-marked-rank.md`], reviewed at `123933cc594b601dd317d62b333a949d20431d35`. Its lifted-socle discrepancy is reviewed at `ceb13792291dc825dc9dc4f1cfeaf6a190deba6e`. The mandatory \(\dim W=4b+5\), and the \(J\)-to-\(U\) cross-map description, are in the central-socle obstruction [dependency/context not reproduced in this update: `bruck-n-central-socle-obstruction.md`] at `bf11794257554b943a1b26ca15acd861f9faaa7f`; the reviewed block and component interfaces cited there remain dependencies. The present quadratic collision has the scoped exact-source reviews below.

## Fixed socle vectors and marked variation

Assume for contradiction that \(c\ge2\). The \(F_{20}\)-submodule of \(\operatorname{soc}(U^b)\cong N^b\) in the \(W\)-shadow is an \(S_5\)-submodule, because \(\operatorname{End}_{F_{20}}(N)=\mathbb F_2\). Choose \(T\cong N^2\) inside that intersection. Let \(E_T\le P\) be its full preimage. The reviewed component calculation gives \(q|_T=0\), including its pair terms, so \(E_T\) is elementary abelian. We do not assume that \(E_T\) centralizes \(P\).

Fix a selected marked involution \(\lambda\) over a transposition \(t\), and put
\[
 I=(1+t)Z,\qquad C=C_T(t),\qquad R=(1+t)T.
\]
The transposition rank on \(N\) is one, so \(\dim I=1\), \(\dim C=6\), and \(\dim R=2\). The reviewed marked-rank table and \(\dim W=4b+5\) give \(\ell_\lambda=0\) on all of \(C_V(t)\). Also \(C\subseteq(1+t)V\), since \(U|_{\langle t\rangle}\) is free.

For all \(m\in C\),
\[
 \beta(m,C_V(t))\subseteq I.                                      \tag{2}
\]
Indeed, for \(X=P_6\), both \(P_6\) and \(U\) restrict freely to \(\langle t\rangle\), so \(C_V(t)=(1+t)V\). For \(X=J\), the \(U\)-fixed part is again \((1+t)U^b\), and the unique \(J\)-to-\(U\) cross-map annihilates the \(U\)-socle. In either case, if \(tm=m\), equivariance gives
\[
 \beta(m,(1+t)v)=(1+t)\beta(m,v)\in I.
\]

## The actual discrepancy

For each \(m\in C\), let \(w_m\in W\cap E_T\) be its unique lift, and choose \(p_m\in P\) whose shadow \(v_m\in V\) satisfies \((1+t)v_m=m\). The elements \(w_m\) depend linearly on \(m\), because \(W\) is elementary and \(W\cap Z=1\). Define the marked displacement
\[
 D(p)=p^{-1}\lambda(p),\qquad
 \Delta(m)=w_mD(p_m)+I\in Z/I.                                    \tag{3}
\]
The product \(w_mD(p_m)\) lies in \(Z\), since both factors have shadow \(m\); the formula is computed in the elementary group \(E_T\).

The value in (3) is independent of the choice of \(p_m\). If \(p_m\) is replaced by \(p_mq\), then the shadow of \(q\) is \(t\)-fixed. The class-two identity
\[
 D(pq)=D(p)D(q)[D(p),q]                                          \tag{4}
\]
shows that the change lies in \(I\): \(D(q)\in I\) because \(\ell_\lambda=0\), and the commutator has value \(\beta(m,\overline q)\in I\) by (2). Changing a central lift is included in this argument.

For \(m,n\in C\), choose shadows \(v_m,v_n\) as above. Since \(E_T\) and \(W\cap E_T\) are elementary, (4) gives
\[
 \Delta(m+n)+\Delta(m)+\Delta(n)
   =\beta(m,v_n)\pmod I.                                         \tag{5}
\]
The right side is independent of \(v_n\) by (2), and is bilinear in \(m,n\). It is alternating: its diagonal is \(\beta(v_m,tv_m)\pmod I=0\) by the reviewed \(d=0\) identity. It is symmetric because the sum with its transpose is \((1+t)\beta(v_m,v_n)+\beta(m,n)\), which is zero modulo \(I\); here \(\beta(T,T)=0\). Thus \(\Delta:C\to Z/I\) is a quadratic map.

## Scalarization forces a collision

On \(R\), choose the preimages \(p_m\) inside \(E_T\). The restriction \(\Delta|_R\) is the linear discrepancy map of the reviewed lifted-socle argument. It is injective: if a nonzero \(m\in R\) mapped to zero, adjusting by \(I=(1+\lambda)Z\) would put the nonidentity \(w_m\) in \(W\cap(1+\lambda)E_T\), contrary to \(H\cap\Lambda^2=1\). Let \(A=\Delta(R)\); it has dimension two in the three-dimensional space \(Z/I\).

The polar in (5) vanishes on \(R\times C\). If \(m=(1+t)a\) with \(a\in T\), then
\[
 \beta(m,v_n)=\beta(a,(1+t)v_n)\pmod I
 =\beta(a,n)=0,
\]
using equivariance and \(\beta(T,T)=0\). Therefore projection of \(\Delta\) to \((Z/I)/A\cong\mathbb F_2\) is constant on \(R\)-cosets and induces a scalar quadratic
\[
 Q:C/R\longrightarrow\mathbb F_2,\qquad \dim(C/R)=4.             \tag{6}
\]
Every scalar quadratic on an \(\mathbb F_2\)-space of dimension at least three has a nonzero zero. For if it took value one on every nonzero vector, three independent vectors and their pair sums would force all three mutual polar values to be one, while their triple sum would have value zero.

Choose \(m\notin R\) with \(Q(m+R)=0\). Then \(\Delta(m)\in A\), so there is \(r\in R\) with \(\Delta(r)=\Delta(m)\). The polar vanishes on \(R\times C\), hence \(\Delta(m+r)=0\), while \(m+r\ne0\). In (3), this says \(w_{m+r}D(p_{m+r})\in I\). Since \(\lambda\) acts as \(t\) on \(Z\), choose \(z\in Z\) with \(D(z)\) equal to that element. Equation (4) and centrality of \(Z\) give
\[
 D(p_{m+r}z)=w_{m+r}\ne1.
\]
The latter is the product of \(\lambda\) with a \(P\)-conjugate of \(\lambda\), hence lies in \(\Lambda^2\cap H\), contradicting the original folder transversality. This proves (1).

## Consequence for the J branch

The reviewed \(J,C_0=0\) exclusion and whole-\(J\)-in-shadow exclusion, together with the separately reviewed exceptional normal form at `5325d80926fe96073e800134e60fe9902f15bcce`, leave only a shadow whose pure socle intersection is \(N^2\): it is the sum of the first two active socles, while the third socle occurs only in the mixed graph. Thus the remaining \(J\) case has \(c=2\), contrary to (1). Conditional on the cited inputs and this new collision, no displayed \(N\)-Frattini envelope with \(X=J\) exists.

The argument is entirely in the original group and uses no projected quotient folder, orbit census, or temporary computation. Its choice-independence and class-two quadratic calculation have the scoped exact-source reviews below.

## Independent review

At exact source `c4154e4d8cfbe1485491f6ec0b57567f8a18e396`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the full collision proof and its J-branch consequence, conditional on the pinned marked-rank, module/component, actual-lift, canonical-folder and exceptional-normal-form inputs. All checked independence under arbitrary noncommuting lift changes, the displacement product formula and alternating polar, the actual discrepancy image on R and its polar radical, the four-dimensional scalar quadratic, and the final R and central-I adjustments producing an original marked collision. No new computation was required. Their scope is c at most one for J and P6 and exclusion of the displayed J branch, not the still-separate P6 deduction or unrestricted Bruck envelopes.
