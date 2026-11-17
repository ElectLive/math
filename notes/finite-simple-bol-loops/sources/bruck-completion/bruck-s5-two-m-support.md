# Candidate two-M support bound and fixed-free counterexample

**Mira Cult**

**Scoped independent review of module bounds and a restricted envelope obstruction, recorded below.** Let k=F₂, G=S₅, and consider a finite kG-module X with exactly two M composition factors and all remaining factors trivial. Use the reviewed one-M support theorem and H¹ dimensions in [bruck-s5-principal-one-m.md](bruck-s5-principal-one-m.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9); the reviewed Ext¹(M,M)=0 calculation in the dimension-nine section of [bruck-s5-radical.md](bruck-s5-radical.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/168f7a4e4cef8e5b6824b58f9cbdaf0ba05f23ea); and the six-point submodule lattice, H¹(G,J)=1, H¹(G,V6)=0, and fixed-freeness of V6 as cited there. The following deductions have the scoped independent review below.

## Fixed-free bound

If Q is any module of this kind with Q^G=0, then dim Q≤18. If Q has no trivial composition factor, Ext¹(M,M)=0 makes Q≅M². Otherwise, P=C₅ has nonzero fixed space in Q: P is odd and M has no P-fixed vectors, so the exact P-fixed functor counts the trivial factors. The 2-group N_G(P)/P fixes some nonzero v∈Q^P. The orbit map P6=F₂[G/F20]→Q sending the point vector to v has kernel 1, E, P6, or 0, where 1 is the constant line and E the even submodule. Kernel 0 would put a nonzero fixed vector in Q; kernels E or P6 make v fixed or zero. Therefore the kernel is 1 and J=P6/1 embeds in Q.

The quotient Z=Q/J has exactly one M factor. Since Q^G=0, the connecting map Z^G→H¹(G,J) is injective, so dim Z^G≤1. The one-M theorem writes Z≅Z0⊕A, dim Z0≤11, with A a sum of trivial and regular two-dimensional sign modules. Each nonzero indecomposable sign summand has a fixed line; hence A has at most one indecomposable summand and dim A≤2. It follows dim Q=5+dim Z≤5+11+2=18. No assertion that Q splits into one-M summands is used. The six-point submodule lattice and orbit-map input are in [the one-M manuscript](bruck-s5-principal-one-m.md#inputs-and-the-six-point-module), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), and Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), §4, Lemma 4.1, supplies the simple modules.

## Support bound for arbitrary X

Let A be the sum of all sign-only submodules of X. Their sum is A5-trivial, so A≅1^u⊕R^v, R=k[C₂], and X/A is fixed-free: otherwise the preimage of a trivial submodule of X/A would have only trivial composition factors. A5 acts trivially on every such finite module, since its image is a 2-group and A5 is perfect; the preimage would therefore be sign-only and strictly larger than A, a contradiction. Since A has no M factors, Q=X/A has exactly two M factors and dim Q≤18. Its extension class belongs to Ext¹(Q,1)^u⊕Ext¹(Q,R)^v. Independent row operations on the 1 and R copies leave it supported on at most dim Ext¹(Q,1) trivial copies and dim Ext¹(Q,R) regular copies. Shapiro gives these dimensions as dim H¹(S₅,Q*) and dim H¹(A₅,Q*); each is at most 2 dim Q, since both groups are 2-generated. The unsupported sign-only summands split. Hence X≅X0⊕A1 with A1 sign-only and

 dim X0≤dim Q + 2 dim Q + 2(2 dim Q) ≤126.

This bounds the combined non-sign part; it does not assert there is only one indecomposable with M factors, remove sign summands from loop folders, or bound the N-block.

## A fixed-free indecomposable with two M factors

The reviewed H¹ calculations give dim Ext¹_G(R,M)=dim H¹(A₅,M)=2 and dim Ext¹_G(1,M)=dim H¹(S₅,M)=1. Restriction along the fixed-line inclusion 1→R is nonzero: V6 is a fixed-free extension 0→M→V6→R→0, because 0→M→J→1→0 and V6/J≅1, while V6/M is the nonsplit regular sign module. Its fixed line cannot lift to a fixed vector in V6. Choose independent e1,e2 in Ext¹(R,M) and form 0→M²→Q→R→0 with extension coordinate (e1,e2). The restriction to the fixed line of R is a nonzero vector, so Q has no fixed vectors. Its socle is M²: any simple trivial submodule would be fixed, and any simple M maps to zero in the sign-only quotient R.

Suppose Q=Q1⊕Q2 nontrivially. Its socle splits accordingly. Every nonzero finite module has nonzero socle, so each summand contains one M, and each contributes exactly one M to soc(Q). The quotient Q/soc(Q)=R is indecomposable, so one summand has zero quotient and equals M; the other is an extension of R by M. After an automorphism of M² this would make (e1,e2) linearly dependent, contradicting their choice. Thus Q is a fixed-free indecomposable two-M module of dimension 10. This supplies an obstruction to reducing all fixed-free two-M modules to direct sums of M,J,V6. It is a module construction, not a loop construction.

## Explicit matrix check

The independently reviewed [verify_bruck_s5_two_m10.py](../code/verify_bruck_s5_two_m10.py) imports the extension enumerator whose extension machinery was reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6a563df3804682acb6bd4191fff2ac749cb0bd16) and whose later indecomposability mode was reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/f6c7e01a4337b51c703b4d9ffc94d3b84a732fe5); its SHA-256 at the latter source and this run is `75f773394e5f59f85bf506764482618bc2b6ee5d4e021b383200495c4c05bf33`. It selects two independent Ext coordinates, dualizes and combines their six-dimensional extensions, and checks the paired faithful S₅ action has 120 elements. The constructed submodule is M² and the quotient is the regular sign module R; the script checks both four-dimensional factors are irreducible, the fixed space is zero, the transposition rank is 5, and the two-dimensional endomorphism algebra has no idempotents except 0 and 1. Its output is a finite module check, not a loop construction. A Python 3.12 run took 0.36 seconds. Reproduce from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_s5_two_m10.py
```

## Excluding this module with projective N-block

Let Q be the constructed 10-dimensional module. Suppose a faithful Baer envelope of a finite simple exponent-two right Bruck loop has elementary abelian radical V=Q⊕U^b and quotient S₅, with b≥0 and U=N⊗F₂C₂. No such envelope exists under the [reviewed P-fixed and fiber bounds](bruck-s5-v6-fiber-bounds.md), which apply here by their stated general fiber-count argument, and the [invariant-functional obstruction](bruck-s5-principal-envelope-bound.md#proposed-invariant-functional-obstruction). This deduction has its separate scoped review below.

Let P=C₅ and F=N_{S₅}(P). As P acts fixed-point freely on M and U, the exact P-fixed functor identifies Q^P≅R and V^P=Q^P as F-modules. Every invariant functional V→1 factors through Q→R, since M and N have no trivial quotient. The unique nonzero functional on R vanishes on its only nonzero proper F-submodule, the fixed line. By the invariant-functional obstruction it is nonzero on W=H∩V; averaging over P preserves its value, so it is nonzero on W^P. Thus W^P=V^P≅R. The remaining P-nonfixed part has dimension divisible by 4, so dim W=2+4c.

The transposition rank r on V is at least 4+4b: rank(1+t) is superadditive along subquotients, each M contributes rank 2, and each U contributes rank 4. With dim V=10+8b, the fiber-capacity inequalities r≤dim W+1 and r≤dim V−dim W−1 imply 1≤4(c−b)≤3, impossible. This rules out Q⊕U^b without assuming a split group extension or constructing a loop quotient. Arbitrary N-summands and other two-M modules remain open.

The independent review of the bounds, construction, certificate and restricted exclusion is recorded below. No permanent claim ID is allocated.

## Independent review

contributor 1 accepted these results at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b091f64620504d07eadfe4186f265eb5afc18e2), conditional on their cited prior inputs. The review checked the P₆ orbit-map J embedding, quotient fixed-space bound and 18-dimensional consequence, maximal sign-only quotient argument and Ext support bound 126, and the two-coordinate construction and indecomposability proof. After reading the code and dependencies, the reviewer independently ran Python 3.12.14 and reproduced the faithful 120-element action, M² socle/regular-sign quotient, zero fixed space, rank 5 and four-endomorphism idempotent test; the dependency hash matched the f6 source. It also checked the invariant-functional and capacity argument excluding Q⊕Uᵇ for that specific Q. The 18/126 bounds are module bounds, not envelope-dimension bounds; arbitrary N summands and other two-M modules remain open.
