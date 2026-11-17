# Correction to the alternating solvable-factor inventory

**Conditionally proved correction for 0323-finite-simple-non-moufang-bol-loops:C0010;
exact-source independent reviews are recorded below.** This repairs an external-source omission in the
[full-action bridge](../odd-completion/nonbruck-almost-simple-radical-bridge.md), rather than
changing a historical review's scope. Let Q be a finite simple proper left Bol
loop, M=Mlt(Q), G=LMlt(Q), I=M₁ and H=G∩I. Retain the reviewed canonical and
primitive almost-simple inputs C0001/C0008, and C0017's rank-three exclusion at
`e81276fa437c84fba95c8a7ba0bb7b3a9b82d99d`. Thus M=GI and I is maximal and
core-free. We exclude both actual orientations of each of the two additional
factorizations below. The conclusion is conditional on those inputs and the
explicit finite subgroup-classification and algorithm inputs here.

## The missing cases and their effect

Guralnick–Li–Wang–Xia, [arXiv:2402.18373v4](https://arxiv.org/html/2402.18373v4),
26 August 2026, §2.2(V), printed p.5, corrects Li–Xia arXiv:1408.0350v3
Proposition 4.3 by adding the triples

    (S9, S4 × AGL1(5), PΓL2(8)),
    (A9, (A4 × D10).2, PΓL2(8)).

Here the solvable factor preserves the indicated four-plus-five partition in
the natural nine-point representation. The natural degree nine is not the
degree of the putative loop action. Common ambient automorphisms and independent
factor conjugations preserve the arguments below.

The previously reviewed alternating reduction at
`4922123613711b1884764a672d0091afabd5d991`, solvable-G full-action assembly at
`7f456116c2e6ca420c7c15c789c96ee105050c1b`, and reversed solvable-I reduction at
`030ebb1d681efd8b12139efc7d0e3d4bdc9173ce` used the older list as exhaustive.
Those reviews did not examine these omitted cases. This is a genuine gap in
that source interface, even though the conclusions survive the additional
case analysis proposed here. Uses of those reductions now require this repair
as well as their retained historical inputs. In particular the same correction
must accompany downstream full-socle assemblies, including the alternating,
linear and unitary assemblies. No earlier review is retrospectively enlarged.

## Actual stabilizer equal to the solvable factor

For M=S9 the displayed factor has order 480 and is properly contained in the
four-subset stabilizer S4×S5 of order 2880. For M=A9 its intersection has order
240 and is properly contained in (S4×S5)∩A9 of order 1440. Thus neither factor
can be the actual maximal stabilizer I. This also covers any smaller permitted subgroup of that factor. The following
argument additionally excludes a **solvable overgroup** of either displayed
factor as actual I, so no ambiguity about enlarging a source factor is needed.

Every solvable subgroup J≤S9 containing a 5-cycle preserves its five-point
support. Indeed its orbit Δ containing that support has size d between 5 and 9.
If d>5, the induced solvable group on Δ is transitive and primitive: in an
imprimitive action of any of these degrees, both block size and block count are
less than five, so an element of order five fixes every point. A faithful
solvable primitive group has an elementary abelian regular minimal normal
subgroup N. To recall the short argument, minimal normality and solvability make
N elementary abelian, primitivity makes N transitive, and abelian transitivity
makes all point stabilizers equal and hence trivial by faithfulness. Thus d is
a prime power and the group embeds in AGL_e(p), d=p^e. For d=6 this is
impossible; for d=7,8,9 the affine group orders are respectively 42,1344,432,
none divisible by five. This contradiction proves d=5. In particular every
solvable overgroup of the displayed factor lies in its proper four-subset
stabilizer. Such a subgroup cannot be maximal in M unless equal to that full
stabilizer, which is nonsolvable (it contains A5).

## Actual stabilizer PΓL2(8)

In its natural nine-point representation L=PSL2(8) lies in A9: the sign map on
the nonabelian simple L is trivial. Its extension PΓL2(8)/L has order three, so
the entire extension also lies in A9. If I equals this factor and M=S9, the strict containment
I<A9<S9 contradicts maximality. More generally no proper core-free maximal
stabilizer in S9 can contain this factor J: the certificate below shows J
maximal in A9 and N_S9(J)=J. For an overgroup I containing J, I∩A9 is either J
or A9. In the first case J is normal in I and hence I≤N_S9(J)=J. In the second
case I contains the socle and is not core-free. For M=A9, maximality of J
likewise forces every proper overgroup to equal J. Thus enlarging the
nonsolvable source factor cannot introduce a missing actual stabilizer.

For M=A9, the original loop action is the action on the 120 cosets of I. The
[finite certificate](../code/verify_a9_factor_correction.g) constructs
L=PSL(2,8) in GAP's natural degree-nine representation and I=N_A9(L). It checks
|L|=504, |I|=1512, I′=L, maximality of I in A9,
N_S9(L)=N_S9(I)=I, and a faithful coset action with subdegrees **1,56,63**.
Consequently this action has rank three and C0017 excludes the proper Bol loop.

There are **two**, not one, A9-conjugacy classes of maximal PΓL2(8) subgroups.
The complete two-class datum is an explicit external input from Thomas Breuer,
[CTblLibXpls Chapter 11, §11.5-1](https://www.math.rwth-aachen.de/homes/sam/ctbllib/doc2/chap11_mj.html),
the paragraph after the odd-degree alternating-group table. Since N_S9(I)≤A9,
the S9-conjugacy class of our representative splits into two A9 classes. These
are both source-listed possibilities. Conjugation by an odd permutation is an
automorphism of A9 and transports the coset action and its subdegrees, so the
same rank calculation covers both. The proof does not silently replace two
embeddings by a unique A9 class or assume completeness from one enumeration.

## Restored interface and evidence boundary

The omitted triples therefore add no surviving action for proper simple Bol
loops. Combined with the older reviewed cases, the corrected solvable-G
reduction still forces the natural alternating/symmetric action, and the
corrected solvable-I reduction still forces S≤G. The natural-action loop
operations and the socle-containing case remain open. The old solvable-G
statement allowed nonassociative Moufang loops as well; solvable G is already
incompatible with the reviewed Paige full-group input, so restricting this
repair to the proper case loses no case of that assembly.

One reviewer of the initial source requested the explicit overgroup argument
above before accepting restoration of the arbitrary solvable-I reduction. The
initial case-by-case calculation did not state it; the present version includes
both solvable and nonsolvable overgroups and requires review at its new exact
revision. The other three deductions in that source checkpoint are unchanged.

The coordinator freshly inspected the cited corrigendum and the two-class
paragraph. The source's corrected completeness and GAP's exact natural-group,
normalizer, maximality and coset algorithms remain inputs. The certificate is
finite evidence for these concrete groups; it neither verifies a general
factorization theorem nor proves C0017. Run from the repository root with the
pinned GAP 4.15.1:

    gap --quitonbreak -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_a9_factor_correction.g

No canonical definitions or permanent claim IDs are changed. The repaired source interface has the exact-source independent reviews
recorded below.


## Independent review of the corrected interface

GPT-6.1 Terra contributor 1, contributor 2 and contributor 3 independently accepted the final correction at exact source `fbc63aab2c35d93038789802c01d0c04fad82a3b`, conditional on the cited corrected factor classification, two-class completeness, canonical and rank-three inputs and the exact finite algorithms. All checked the explicit solvable-overgroup five-cycle lemma, its elementary affine primitive-group argument and three orders, the nonsolvable-overgroup normalizer argument, both A9 classes and restoration of the affected reductions.

All three independently read, extracted and ran the unchanged GAP certificate at `6c836d271832aa25cc0fcb120f31d8c4f1e2ebad` with GAP4.15.1; its normalizer, primitivity, subdegree and overgroup-order assertions passed. They did not rerun unchanged code for the final prose repair. contributor 1 and contributor 3 freshly inspected GLWX §2.2(V) and the CTblLibXpls two-class paragraph; contributor 2 retained those stated source inputs. The first and third reviewers initially accepted the earlier case analysis; contributor 2 requested explicit coverage of strictly enlarged solvable stabilizers. Its final acceptance covers the added argument resolving that concern, rather than treating its earlier partial acceptance as complete. All historical source/review pins retain their scopes. These are model mathematical/code reviews, not formal GitHub approvals. C0010 remains open.
