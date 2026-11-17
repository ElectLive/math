# Symplectic subspaces, decompositions and actual factor stabilizers

**Conditionally proved scoped continuation; independently reviewed at exact source `899203054af332971f56c53557c6844e543f3288` as recorded below.** This
addresses `0323-finite-simple-non-moufang-bol-loops:C0010`, without allocating a
claim ID or closing that claim. The two geometric results below exclude every
loop in the specified actions. Their applications to simple proper Bol loops
add the explicitly cited full-group and actual-factor classification inputs.
They neither classify arbitrary symplectic actions nor identify loop operations
in the remaining cases.

## Inputs and notation

Use the loop and full multiplication group definitions in
[PROBLEM.md](../foundations/problem-contract.md#model-and-scope). The geometric input is
[C0008 Lemma 2.1(1)](../foundations/C0008.md), reviewed at
`06857e28349ca4529c31a9855ce12cfbb191c1b7`. In particular, if a nonempty
off-diagonal relation R on a transitive permutation domain is invariant under
a group containing Mlt(Q), then some actual translation sends every point x
to an R-related point. Indeed choose (e,a) in R, transporting a pair to e
if necessary. Right translation by y sends (e,a) to (y,L_a(y)). The relation
need not be a single orbital. We will contradict this consequence.

The [nondegenerate completion lemma](../primitive-completion/classical-nondegenerate-subspaces.md#completion-lemma),
reviewed at `698ce5f6d50e7186f205a63f4a2c413145775915`, embeds any subspace of
dimension at most two in a nondegenerate symplectic subspace of dimension at
most four, and then in any larger admissible even dimension. We use this
lemma without duplicating its proof. All symplectic spaces below have their
specified nondegenerate alternating form B. A semilinear similitude g has field
automorphism sigma and multiplier mu, so
B(gu,gv)=mu B(u,v)^sigma. Statements about its projective action do not depend
on the chosen scalar representative.

For the group applications put M=Mlt(Q), S=Soc(M), G=LMlt(Q), and I=M_e.
The reviewed C0008 reduction makes M almost simple, and simplicity makes I
maximal and core-free. Transitivity of G gives M=GI. The applications concern
the indicated **actual** I, not a replacement of either factor by a maximal
overgroup.

## Characteristic-two nondegenerate two-spaces

Let V have dimension 2m>=4 over F_q, with q even. Every semilinear symplectic
similitude g has a nondegenerate two-space U such that U intersects gU
nontrivially. Consequently no loop has full multiplication group contained
in this natural action on all nondegenerate two-spaces. Equivariant orthogonal
complementation gives the same exclusion for nondegenerate (2m-2)-spaces.

If B(v,gv) is nonzero for some v, take U=span(v,gv). Suppose instead that it
vanishes for all v. Polarization at u+c v gives

    c^sigma B(u,gv) + c B(v,gu) = 0

for every u,v,c. Setting c=1 identifies the two coefficients in characteristic
two. If sigma is nontrivial, choose c^sigma!=c; then B(u,gv)=0 for all u,v,
contradicting nondegeneracy and invertibility. Thus g is linear. The same
polarization says its B-adjoint satisfies g*=g. Since g*g=mu Id, we have
g^2=mu Id. Write mu=a^2 in F_q. Then (g-a Id)^2=0, and there is a nonzero
eigenvector v. Extend v to a nondegenerate two-space U; the vector gv=a v
belongs to U intersect gU.

Disjointness is an invariant nonempty relation on this action: any U has a
nondegenerate two-space in U-perp because dim(U-perp)>=2. The displacement
consequence above now proves the loop exclusion. This includes q=2. It does
not extend the element-level assertion to odd q: the nonsquare-multiplier
counterexample in the reviewed nondegenerate-subspace manuscript remains valid.

## Unordered equal orthogonal decompositions

Let V have dimension 4d, and let Omega be its unordered orthogonal
decompositions {U,W} into two nondegenerate 2d-spaces. Assume either d>=2,
over any finite field, or d=1 and q is even with q>=4. No loop has full
multiplication group contained in the natural semilinear symplectic-similitude
action on Omega.

Relate two decompositions when **all four** intersections between their
constituent spaces are zero. This off-diagonal relation R is invariant and
nonempty. To see nonemptiness, identify each of U,W with E^2 for
E=F_(q^d), carrying the form Tr_(E/F_q)(b_E), where
b_E(x,y)=x1 y2-x2 y1. Choose c in E other than 0,-1; the hypotheses ensure
such a choice. Let T=diag(c,1). Its graph E_T={(u,Tu)} has induced form

    Tr_(E/F_q)((1+c)b_E(u,v)),

which is nondegenerate by the nondegenerate finite-field trace pairing.
This is not multiplication of an F_q-valued form by c when c is outside F_q.
Define T* by B(Tu,w)=B(u,T*w). Then

    E_T-perp = {(-T*w,w): w in W}.

Both projections of E_T and E_T-perp are invertible, so {U,W} is R-related
to {E_T,E_T-perp}.

For d>=2, given any g choose v nonzero and a nondegenerate 2d-space U
containing v and gv using the completion lemma. Then gv is in U intersect gU.
For d=1 in the allowed even fields, use the two-space result above instead.
In either case D={U,U-perp} is not R-related to gD, irrespective of any swap
of its two constituents. No g displaces every decomposition into R, contrary
to the necessary translation. This proves the claim. The binary four-space
case and the odd-field four-space case are not asserted here.

## Recovering the actual point action from a product residual

The following elementary interface avoids an assumption about equality of
extension-field normalizers. Suppose S=Sp(V) in characteristic two, dim(V)>=6,
and J=(I intersect S)^(infinity) is characteristic in I intersect S. Suppose
V=U orthogonal-sum W is the direct sum of two inequivalent irreducible
F_q J-modules. Then U,W are exactly the minimal nonzero J-invariant subspaces.
Every semilinear normalizer of J permutes them. If their dimensions differ,
it fixes each one.

The classical automorphism description realizes Aut(S) by natural semilinear
symplectic similitudes in this dimension; the exceptional C2 graph case is
absent. Since I normalizes J, it lies in the proper M-stabilizer P of the
decomposition, or of U when the dimensions differ. Maximality gives I=P.
The symplectic group is transitive on the indicated subspaces or decompositions
by symplectic bases, so M/I is the entire natural domain used above. Notice
that N_M(J) can be smaller than P: an extension-field residual can retain
additional field structure. Only I<=N_M(J)<=P<M and maximality are needed.

Here X^(infinity) denotes the terminal derived subgroup, equivalently the
smallest normal subgroup with solvable quotient. For a normal product of
groups with solvable remaining quotient, this residual is the product of
their perfect residuals. If each factor acts irreducibly on its own summand
and trivially on the other, the two modules are inequivalent even when the
abstract factors are isomorphic.

There is a useful separate consequence in characteristic two, in natural
dimension at least six: **the actual I cannot preserve a nonzero proper
F_q-subspace**. If it preserves W and W is degenerate, it preserves the
nonzero totally isotropic space rad(W); otherwise W is nondegenerate.
Its containment in the respective proper geometric stabilizer, followed by
maximality in the original M, identifies a natural subspace action. The
nondegenerate actions are excluded by the two-space theorem above and the
reviewed completion argument at `698ce5f6d50e7186f205a63f4a2c413145775915`.
The isotropic actions, including points, use only
[C0009 Lemma 1.1(1) and Theorem 1.2(4), symplectic part](../foundations/C0009.md),
with their independent acceptance at
`71f7eae94a6d7ce43563047929bd0be7e8fe1285`. The local argument finds nonzero v
with B(v,gv)=0 by restriction of scalars and Chevalley--Warning; points then
contradict nonperpendicular displacement, while for k>=2 the totally isotropic
span(v,gv) extends to a k-space and contradicts disjoint displacement. This
does not invoke any other portion of the C0009 aggregate.

In particular, if a nontrivial normal subgroup J of I fixes a quadratic
refinement Q0 of B, then it fixes **exactly one**, unless the loop has already
been excluded. Otherwise the difference of two refinements is the square of
a nonzero J-invariant linear functional, corresponding via B to a nonzero
fixed vector. The proper fixed space C_V(J) is I-invariant and gives the
preceding contradiction. Here J is viewed as a nontrivial subgroup of S, so
C_V(J) cannot be all V. This alternative removes the need to identify a
particular irreducible tensor representation from an abstract factor label.

## Applications to the many-nonsolvable-factor symplectic list

Use Li--Xia, arXiv:1711.01090v2, Theorem 1.1(b), Table 1, with the correction
in Li--Wang--Xia arXiv:2106.03109v2, introduction footnote 2. The first two
rows have R.P with P<=2, not necessarily R.2. The missing Sp6(4) triple in
that footnote is retained as a separate obligation below. The table concerns
actual intersections with S and retains both orientations of M=GI.

**Row 1, actual I on the product side.** Here q=2^f,
S=Sp_(4ell)(q), ell=ab>=2, and I intersect S contains the normal natural
extension-field product Sp_(2a)(q^b) x Sp_(2a)(q^b), with solvable quotient.
Each nonsolvable factor's perfect residual acts irreducibly on its natural
2a-dimensional F_(q^b)-module, also on its restricted-scalar 2ell-dimensional
F_q-module. For the perfect symplectic groups this follows directly from
transitivity on nonzero vectors. The only nonsolvable nonperfect endpoint
is Sp4(2), whose A6 residual is transitive on the 15 nonzero vectors, using
the reviewed vector input at `1d64c9301e1fa3a8aae1a86c9a416d731cc419f8`.
Sp2(2) is solvable and cannot supply the required two nonsolvable factors.
The residual therefore recovers the two summands. The actual-action interface
and the equal-decomposition theorem exclude this orientation. This does not
silently replace an extension-field factor by Sp_(2ell)(q).

**Row 2, actual I on the G2-product side.** Here S=Sp_(12ell)(q),
and the two G2(q^ell) factors act on orthogonal restricted-scalar natural
6ell-spaces. Use their nonzero-vector transitivity, including the G2(2)'
endpoint, in the reviewed [G2 vector argument](g2-vector-parabolic-capacity.md)
at `4169b5a5219bf8872dcf8723a2dbea6e07ddb111`.
The same product-residual interface and equal-decomposition theorem apply.
Example 3.3's parenthetical repetition of G2(2^f) is a typographical mismatch;
its preceding wreath product, Table 1 and proof specify G2(2^(f ell)).

**Rows 3, 7 and 8, actual I on the unequal-product side.** These source
models have nondegenerate summands of dimensions 2 and dim(V)-2. The factors
are Sp2(4) and Sp_(4ell-2)(4) in row 3; a nonsolvable A<=Sp2(q) and Sp4(q)
in row 7, with q>=4; and Sp2(4) and Sp10(4) in row 8. The second factor is
perfect and irreducible. The perfect residual A^(infinity) in row 7 is
nontrivial and irreducible: a reducible subgroup of SL2(q) lies in a solvable
Borel, which cannot contain a nontrivial perfect subgroup. The other first
factors are perfect and irreducible as well. Thus the actual I fixes the
unique minimal invariant two-space, and maximality identifies the full
nondegenerate two-space action. The characteristic-two theorem excludes
these three orientations.

**Actual I on a minus-orthogonal side, natural rank at least three.** This
applies to rows 1,2,4,9 for q>=4. Write S=Sp_(2r)(q), r>=3. The actual
intersection has perfect residual J=Omega^minus_(2r)(q), with quotient of
order at most two, so I normalizes J. Let Q0 be its defining quadratic form
with polar B. The standard natural module of J has no nonzero invariant
linear functional: J is transitive on nonzero singular vectors; scalar
multiples with q>2 force a constant invariant value to be zero, and those
singular vectors span V. This is the same natural orthogonal-module input
as in the previously reviewed refinement normalizer arguments. Two quadratic
forms with polar B differ by the square of a linear functional, so Q0 is the
unique J-invariant refinement with that polar.

Normalize each projective semisimilarity to multiplier one, possible uniquely
in characteristic two. Transporting Q0 by a normalizer of J gives another
J-invariant refinement, hence Q0 itself. Conversely its stabilizer normalizes
J, the perfect residual of its orthogonal isometry group. Thus N_M(J) is
exactly the natural minus-refinement stabilizer. It is proper, since otherwise
the nontrivial proper J would be normal in S. Maximality identifies I with it.
The reviewed [minus-refinement exclusion](../primitive-completion/symplectic-refinement-all-fields.md)
at `13e21094894aed868a16d7859db036ca7cfc1a69` excludes the actual action.
That deduction is CFSG-dependent and assumes its stated earlier inputs.

## Source audit, scope and next obligation

The coordinator and contributor contributor 1 freshly inspected
Li--Xia v2 Theorem 1.1(b), all of Table 1, Example 3.2 and the row-1 part of
Lemma 5.4's proof; the contributor also inspected the product embeddings in
Examples 3.3,3.12,3.14 and the actual placements in Lemma 5.4's proof,
Row 2 (giving Table 1 rows 3 and 8) and Row 4 (giving Table 1 row 7).
These are classification inputs, not reconstructed
external proofs. LWX v2 introduction footnote 2 was freshly inspected by both.
The full natural automorphism input retains Kleidman--Liebeck (1990), §2.1,
Table 2.1.B p.15 and Theorems 2.1.3--2.1.4 p.16, with the primary inspections
recorded in [REFERENCES.md](../foundations/references.md). The small A6 and G2(2)' natural
module identifications retain the precise source-reported computations and
review limitations at their pins. The root checked both displacement proofs;
contributor 2 developed the two-space proof,
contributor 1 developed the decomposition proof and applications,
and contributor 3 performed a preliminary mathematical audit. These
development checks are not exact-revision acceptance.

The product applications above use those actual natural-model placements,
not merely the abstract isomorphism names in Table 1. They do not assert
that a displayed existence example by itself classifies all embeddings.
In the source's Lemma 4.2 reduction the original I still normalizes the
same (I intersect S)^(infinity), which is enough for the geometric interface.
**Maximality is used only in the original M.** It need not pass to the
intersection with a smaller normal almost-simple group; an attempted shortcut
using such transfer was rejected because of novelty maximal subgroups.

The scoped conclusions are uniform in their stated field and dimension
parameters. For row 1 with ell>=2 and row 2, both orientations are therefore
excluded when q>=4; at q=2 only the product-side orientation is established
here. Other opposite orientations in rows 3,7,8, tensor-product sides in
rows 4,5,9,10, rank-two exceptional graph actions (including row 6), and the
missing corrected Sp6(4) pair's precise common model remain separate. The
minus action at q=2 is outside the cited refinement theorem. No unqualified
Corollary 1.5 dispatch from arXiv:2402.18373v4 is used. Canonical groups
containing S and the remainder of the classical factorization classification
are also outside this argument. C0010 and the classification target stay open.

No numerical search or new executable is needed for this proof. Repository
integrity is checked separately with Python 3.12.14 and `python check.py`;
passing it is not mathematical verification.


## Independent exact-source review

GPT-6.1 Terra contributor 4, contributor 5 and
contributor 6 independently accepted exact source
`899203054af332971f56c53557c6844e543f3288`, conditional on the stated
displacement, completion, local isotropic-action, natural automorphism,
refinement and actual factor-model inputs. Each checked the characteristic-two
polarization and eigenvector cases, the trace-form graph and its adjoint
complement, the unordered all-four-intersections relation and dimension
boundaries, the intrinsic product-module normalizer, the invariant-subspace
and unique-refinement alternatives, and maximality only in the original M.
The applications retain their stated natural-model and small-module inputs.
contributor 4 freshly inspected Li--Xia v2 Table 1, Example 3.3,
Lemma 5.4 proof Rows 1--2 and LWX v2 correction footnote 2.
contributor 6 freshly inspected Table 1 rows 1--2 and
Example 3.3. The other primary-source inspections and small-module
computations were retained rather than reperformed; contributor 5
claimed no fresh primary-source audit. No new computation was needed or
claimed. These are independent model mathematical reviews, not formal GitHub
approvals or certification of the remaining factorization list or C0010.


## Any number of equal summands in characteristic two

**Continuation with independent mathematical review recorded below.** Let q be even, a≥1 and t≥3. On a 2at-dimensional nondegenerate alternating F_q-space V, let Ω be the full set of unordered orthogonal decompositions into t nondegenerate 2a-spaces. No loop has its full multiplication group contained in the natural semilinear symplectic-similitude action on Ω. Together with the reviewed two-summand result above, this covers every t≥2 in characteristic two except the binary four-space case already excluded from that earlier statement. This is an action theorem; identifying an arbitrary maximal subgroup with its decomposition stabilizer remains a separate source interface.

Relate two decompositions when every summand of the first has zero intersection with every summand of the second. This relation R is invariant and off the diagonal. Its nonemptiness has a uniform construction. Choose standard symplectic coordinates (e_i,f_i) with e_i,f_i in F_q^a, 1≤i≤t, so U_i is the i-th pair. Let J be the t-by-t all-ones matrix, with every matrix entry below tensored with I_a. The product

    g = [I 0; J I] [I J; 0 I] = [I J; J I+J²]

is symplectic because each factor is a shear with symmetric off-diagonal block. For target j different from source i, its local 2a-by-2a block is

    [0 I_a; I_a (t mod 2)I_a],

which is invertible. Given i,j, choose k distinct from both, possible for t≥3. Projection of gU_i onto U_k is injective, whereas U_j projects to zero there. Hence gU_i∩U_j=0 for all i,j, proving that R is nonempty over every even field, including F2.

For any semilinear symplectic similitude h, there is a nondegenerate 2a-space U with U∩hU nonzero. For a≥2, embed span(v,hv), v≠0, in U by the reviewed completion lemma above. For a=1, use the characteristic-two two-space theorem proved and reviewed above at `899203054af332971f56c53557c6844e543f3288`; its polarization argument includes nontrivial field automorphisms and scalar multipliers. Decompose U-perp into t−1 nondegenerate 2a-spaces. The resulting decomposition D is not R-related to hD. Thus no natural similitude sends every decomposition to an R-related decomposition, contradicting the original-loop displacement consequence of C0008 Lemma2.1(1) stated above. No factorization classification or projected loop is used. No new computation is needed.

Two independent mathematical reviewers, contributor 7 and contributor 8, accepted these local deductions at exact source `898445e11fd53478a1a84e4eeb00b98450424fe4`. Both checked the shears, the semilinear witness, displacement, the tensor refinement and maximality argument under the stated inputs. Both inspected Li–Xia v2 Example 3.13 and Lemma 6.2. The first also inspected Example 3.12 and the use in Lemma 6.7 Case 2(i). The example construction and external group and geometry inputs retain their stated qualifications. Neither reviewer performed a new computation or accepted the withdrawn global factorization argument.
