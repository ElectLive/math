# Candidate exceptional-family raw involution bounds

**Mira Cult**

This manuscript-local result, with scoped independent review below, concerns [C0010](../../claims/0010.md) treats simple T in the families G₂(q), q≥3; ³D₄(q), q≥2; and ²F₄(Q), Q=2^f≥8 with f odd. Subject to the [raw-F₃ SD criterion](sd-raw-involution-count.md) and its primitive-folder and inversion dependencies, it excludes primitive SD_k left multiplication groups with socle T^k for every k≥3. No common involution class is assumed. These checks do not cover the Tits group or assert a census of simple groups.

Put n=|T|, t=|Out(T)|, a=tn, and b=|{x∈Aut(T):x²=1}|. Fulman–Guralnick, [*Bounds on the number and sizes of conjugacy classes in finite Chevalley groups with applications to derangements*](https://doi.org/10.1090/S0002-9947-2012-05427-4), Trans. AMS 364 (2012), Lemma 2.1(1)–(2), p.3027 and Table 1, p.3049, give k(Aut T)≤t k(T) and the simple-group class bounds below. The Frobenius–Schur identity and Cauchy–Schwarz give b²≤a k(Aut T). It suffices to show n≥2²⁰ and b³+3ab<n². All conclusions depend on the cited group data and upstream criterion, and need independent review.

## G₂

Write q=p^f. The group order is n=q⁶(q⁶−1)(q²−1); see Wilson, [*The finite simple groups*](https://citeseerx.ist.psu.edu/document?doi=a45a9da3e6de88f7f27c1178314903190b4486b4&repid=rep1&type=pdf), §4.2, equations (4.9) and (4.12). [Lucchini–Marion–Tracey](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/147250970/LUCCHINI_et_al_2020_Forum_of_Mathematics_Sigma.pdf), Proposition 3.11 and Table 2, give t=f except t=2f in characteristic 3. Thus t≤2log₂q. Table 1 of Fulman–Guralnick gives k(T)≤q²+2q+9≤4q². Therefore b≤2tq√n, while n>q¹⁴/2, and

    (b³+3ab)/n² < 96(log₂q)³/q⁴ + 36(log₂q)²/q⁶.

Both summands decrease for q≥16, and their sum at 16 is below one. For q∈{3,4,5,7,8,9,11,13}, the [integer certificate](../code/verify_sd_exceptional_class_bounds.py) takes K=t(q²+2q+9), B=ceil√(aK), and verifies B³+3aB<n². The size threshold holds throughout. G₂(2) is nonsimple; its derived group is handled separately.

## Triality ³D₄

Wilson, *The finite simple groups*, §4.8.2–3, printed p. 138, equation (4.77), gives n=q¹²(q⁸+q⁴+1)(q⁶−1)(q²−1), simplicity, and t=3f. Table 1 of Fulman–Guralnick gives k(T)≤q⁴+q³+q²+q+6<2q⁴ for q≥3. Hence b<√2 tq²√n, n>q²⁸/2, and, using t=3f≤3q,

    (b³+3ab)/n² < 4t³/q⁸+6t²/q¹² ≤ 108/q⁵+54/q¹⁰ < 1.

The last expression decreases and is below one at q=3. For q=2 the certificate uses t=3 and K=108 and proves the exact integer inequality. All these n exceed 2²⁰. Here q denotes the conventional ³D₄(q) parameter, with underlying field of order q³; the proof uses the explicit simple-group class bound rather than an almost-simple twisted q/r convention.

## Large Ree ²F₄

Wilson, [*A simple construction of the Ree groups of type ²F₄*](https://webspace.maths.qmul.ac.uk/r.a.wilson/pubs_files/ReeF4alg.pdf), Theorems 1–2, gives n=Q¹²(Q⁶+1)(Q⁴−1)(Q³+1)(Q−1) and simplicity. Himstedt–Huang, [*Character table of a Borel subgroup of the Ree groups ²F₄(q²)*](https://doi.org/10.1112/S1461157000000012), §6, state Aut(T)=T⋊C_f; their q² is our Q. Fulman–Guralnick Table 1 gives k(T)≤Q²+4Q+17<2Q². Hence b<√2 fQ√n, and n>Q²⁶/2. Since f≤Q,

    (b³+3ab)/n² < 4/Q⁷+6/Q¹⁰ < 1.

The last inequality holds already at Q=8 and decreases thereafter; n≥2²⁰. This uses the explicit simple-group class bound and Gallagher's inequality, without identifying the field/rank convention for the general almost-simple bound.

Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_exceptional_class_bounds.py` from the repository root. The script checks finite integer cases and rational endpoints; it does not certify the group data, asymptotic derivations, or the upstream criterion.

## Scoped independent review

reviewer contributor 1 accepted the exceptional-family estimates at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6a563df3804682acb6bd4191fff2ac749cb0bd16), conditional on the stated raw criterion, folder inputs and cited group data. The review checked FG class bounds, outer automorphism data, inequalities and endpoints, and independently ran the Python 3.12.14 certificate. After an initial access failure, the reviewer verified the cited Wilson PDF (SHA-256 `4d1f7cb4cc86e726b7d0a8d671dcb3532f22233d5ce1adc07f5d0779d66614eb`) and directly checked printed p. 138, equation (4.77) and §4.8.3 for the triality order, simplicity and field automorphisms. Himstedt–Huang §6 was directly checked; the DOI above corrects an erroneous older PDF footer. This source-link correction does not change the reviewed mathematics. No global simple-group census or unrestricted loop classification follows.
