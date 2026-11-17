# Symplectic point-parabolic residual as the actual stabilizer

Conditionally proved scoped continuation of [0323:C0010](../foundations/research-C0010.md), with exact-source independent reviews recorded below. Let Q be a finite simple **proper** left Bol loop, M=Mlt(Q) almost simple with nonabelian simple socle S=PSp_(2m)(q), m≥2, and let I=M_1 be its actual maximal stabilizer, assumed nonsolvable. Suppose that, in the natural symplectic model (up to an automorphism of S), I^(∞) is the projective image of the perfect residual of the stabilizer P1 of a totally isotropic one-space. Then this configuration is impossible, subject to the canonical full-group and classical-automorphism inputs and [the reviewed rank-three theorem C0017](../../claims/0017.md) at `e81276fa437c84fba95c8a7ba0bb7b3a9b82d99d`, conditional on CFSG and its specifically reviewed prerequisites. The result makes no assumption that the other actual factor has a unique nonsolvable composition factor, and uses neither a quotient loop nor a restriction on canonical G=LMlt(Q).

Use definitions in [PROBLEM.md](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45` and C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`.

## The actual characteristic radical

Put Y=I^(∞). Let p=char(Fq), and write U=O_p(P1) for the point radical. The source Guralnick–Li–Wang–Xia, arXiv:2402.18373v4, §8.4, displayed formula immediately before Example 8.14, printed p.55 (PDF p.54), explicitly gives

  P1[Sp_(2m)(q)]^(∞) = [q^(2m−1)]:Sp_(2m−2)(q)′.                 (1)

It distinguishes the Heisenberg radical for odd q from the abelian radical in characteristic 2, and includes the full U in both cases. For (m,q)=(3,2) it gives 2^5:A6; the source's smaller order-4 intersection there is with the opposite SL2(8) factor and does not reduce U. The projective scalar kernel has order gcd(2,q−1), coprime to p, so the radical survives faithfully.

For (m,q)=(2,3), P1 is solvable because its Levi quotient embeds in F3*×SL2(3); its perfect residual is trivial, incompatible with the stated nonsolvable residual. Sp4(2) is not simple; its derived A6 falls under the reviewed alternating/minimum-order exclusions and is not the asserted PSp4(2) socle. In every remaining permitted case the Levi residual in (1) has trivial p-core: it is a central quotient of a perfect symplectic group, except Sp4(2)'=A6, which is simple. The source's next blanket perfectness sentence must be read with the foregoing SL2(3) correction. Thus

  U = O_p(I^(∞)),

so U is characteristic in actual I. Its unipotent lifts are unique in the inverse image of U under the projective map, because that inverse image is U times a central p′ scalar group. The common fixed space of these lifts on the natural 2m-space is exactly the defining line ℓ: every point-radical element fixes ℓ, and the root elements move every vector outside ℓ. Hence the normalizer of U in S is exactly P1. In particular I∩S≤P1, and I normalizes this parabolic type intrinsically.

## The original action

The classical automorphism description gives natural projective semilinear symplectic similarities, except the characteristic-two rank-two graph/graph-field coset. These natural automorphisms preserve the two parabolic types. In Sp4 in characteristic two the exceptional graph map exchanges the two maximal parabolic classes; Burness–Gerhardt–Guralnick, *Topological generation of simple algebraic groups*, proof §5, printed p.53, states this exchange for the algebraic group. For finite q its standard root-group formulas exchange long and short root groups with parameters t or t²; both maps permute Fq, so the exchange restricts to the Fq-rational point and totally-isotropic-plane parabolics. This root-formula/rational-descent statement is a standard automorphism input and has not been independently rederived here; no assertion that an individual graph-field automorphism has order 2 is used. Since such an element cannot normalize P1, it cannot normalize Y: indeed U=O_p(Y) and N_S(U)=P1. Thus every element of I is natural semilinear and preserves ℓ. Since S is transitive on the original M/I, we have M=SI. All of M therefore lies in the natural semilinear subgroup; this is established before invoking its point action. Now I is contained in the proper M-stabilizer of ℓ, and maximality yields

  I=N_M(ℓ),   I∩S=P1.

Consequently the original coset action M/I is the natural projective-point action, with every actual outer element included. Equality I∩S=P1 follows from this maximality argument, not merely from containment of the radical.

This action has rank 3. Relative to ℓ, the two nontrivial P1-orbits consist of points in ℓ^⊥ other than ℓ, and points outside ℓ^⊥. Witt extension together with the line-scaling torus proves transitivity within each set. Semilinear symplectic similarities preserve orthogonality, so no larger actual I fuses them. C0017's independently reviewed rank-three theorem excludes every finite simple proper Bol loop in this action. No claim about the Moufang/Paige case is made.

Source scope: The geometric statement above is conditional only on the displayed exact actual residual. Guralnick–Li–Wang–Xia Theorem 8.1 and Table 10.8 row 1 use this residual in their classification when both actual factors have exactly one nonsolvable composition factor. Cases with multiple nonsolvable factors require their companion classification; this point-stabilizer deduction does not require or assert its exhaustiveness. The equality (1), finite graph descent, canonical primitive full-group interface and the rank-three theorem remain cited inputs, not reproved classification results. No new computation or review is claimed.


## Source inspection and remaining scope

The coordinator freshly inspected [Guralnick–Li–Wang–Xia, arXiv:2402.18373v4](https://arxiv.org/html/2402.18373v4), dated26 August2026, §8.4 at the displayed residual formula and Example8.14. The rank-two exchange is in Burness–Gerhardt–Guralnick, *Topological generation of simple algebraic groups*, version dated11 October2023, Theorem5.8 proof, printed p.53, [author PDF](https://seis.bristol.ac.uk/~tb13602/docs/bgg_classical_final.pdf), SHA256 `f9dafc7c5371271a4721a20f0bd81986b011cc917f16e203071c8684b9ea5d1c` downloaded2026-11-17. That passage was directly inspected. The rational root construction, complete automorphism description and CFSG-dependent rank-three theorem remain explicit inputs. This is one actual stabilizer orientation, not an exhaustive symplectic full-socle theorem. Independent reviews are recorded below.


## Independent review

GPT-6.1 Terra contributor 1, contributor 2 and contributor 3 independently accepted this scoped deduction at exact source `6c836d271832aa25cc0fcb120f31d8c4f1e2ebad`, conditional on its cited canonical, classification, finite-group and prior-review inputs. Each checked the actual characteristic full radical, small boundary cases, graph-type exclusion, maximality before identifying the original action, and the rank-three application. contributor 1 freshly inspected GLWX §8.4 and the BGG graph-exchange passage; the other reviewers retained those documented inspections. Finite graph descent and the classical automorphism description remain explicit standard inputs. No computation was needed. This excludes the stated actual stabilizer orientation, not every symplectic full action. These are scoped model reviews, not formal GitHub approval or a proof of C0010 in full.
