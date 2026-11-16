# An actual-lift residual for two N Frattini factors

**Independently reviewed under the pinned inputs**, continuing 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`]. Let (G,H,K) be the original faithful canonical envelope of a finite simple nonassociative Bruck loop, with G/P≅S5, P=O₂(G) class at most two and exponent at most four, Z=Φ(P)≅N² central in P, and V=P/Z≅P6⊕U^b. Suppose the marked rank is r=2. The [affine-fiber parity theorem](bruck-n-affine-fiber-parity.md) at `3c3cafff03f9e9d79640b68f03883c22e57210d6` then gives exactly one actual selected P-conjugacy orbit over each quotient transposition. The original marked-set and radical-action inputs are those of that source and [the multiple-N source](bruck-multiple-n-frattini.md) at `1d4b306b5e94e1b2c0fb0a85809e374bca0f4327`; the compatible module matrices and projectivity are in [the N-block source](bruck-s5-module-blocks.md) at `dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499`. The actual nonsplit realization and its limits are in [the nonsplit-extension source](bruck-n-nonsplit-extension-lifts.md) at `4c93742a59ccdd786f23598f0374f674c6f75fff`; the split case is separately excluded in [the split-extension source](bruck-n-split-extension-exclusion.md) at `a1f42ac3a21ce22edef96845f6cdf379511b2a51`. Their reviews retain their original scopes; the new residual analysis has separate reviews recorded below.

Fix disjoint quotient transpositions t₁,t₂ such that d=t₁t₂∈F20, actual selected outside marks λ₁,λ₂, and an actual h∈H above d. Let W=H∩P, B=WZ/Z≤V and J=(1+t₁)Z+(1+t₂)Z≤Z. The quotient Z/J has dimension four: in each deleted-five N, the two transposition-image lines are independent. This is a computation in the pinned standard N module. No quotient folder, split extension, or existence of a shadow solution is assumed. The group quotient G/Z is used only for its actual actions and coordinates.

## Coordinates and the actual affine equation

Choose a basis e_i of V and lifts in P. Write the group law on P as

 (v,z)(w,u)=(v+w,z+u+f(v,w)),
 f(v,w)=Σ_i v_i w_i q(e_i)+Σ_{i<j}v_i w_j β(e_i,e_j),       (1)

where q(v)=f(v,v) and β(v,w)=f(v,w)+f(w,v). This ordered-generator cocycle is bilinear and works for every actual class-two exponent-four P with the prescribed q. Let T_i be t_i acting on V and Z, Δ_i=1+T_i. Conjugation by λ_i on P necessarily has the form

 α_i(v,z)=(T_i v,T_i z+a_i(v)),                            (2)

with a_i(0)=0 and polar

 a_i(v+w)+a_i(v)+a_i(w)
    = E_i(v,w):=f(T_i v,T_i w)+T_i f(v,w).                 (3)

The right side is symmetric bilinear because α_i preserves q. Its equality with the polar is forced by the group automorphism law. The linear coefficients of a_i, which encode actual marked-action/extension choices, are deliberately not specified.

Let g₀=λ₁λ₂h⁻¹=(c,z₀)∈P. For p=(x,z), define D_i(p)=pα_i(p⁻¹), so λ_i^p=D_i(p)λ_i. Its shadow is Δ_i x and its central coordinate is

 (1+T_i)z+d_i(x),
 d_i(x)=a_i(x)+T_i q(x)+f(x,T_i x).                        (4)

Put C(x,y)=Δ₁x+T₁Δ₂y and let [·] denote projection to V/B. A necessary and sufficient shadow equation for λ₁^p λ₂^q h⁻¹ to have W-shadow is

 [C(x,y)]=[c].                                               (5)

If (5) is inconsistent, A=∅ and this pair's F is not defined. If it has one solution, all solutions form its affine translate A of

 V₀=ker( V⊕V → V/B, (x,y)↦[C(x,y)] ).                       (6)

The actual-lift lemma in the multiple-N source gives W∩Z=1 (its proof is independently reviewed at `6fe18de73836f5babe8bff5be255ff80fc864fb7`), so there is a unique w(s)∈W for each s∈B. Write w(s)=(s,ω(s)); then q(s)=0 and W's multiplication gives

 ω(s+s′)+ω(s)+ω(s′)=f(s,s′)   (s,s′∈B).                   (7)

Thus f|B is symmetric and ω has the displayed polar. These statements use the actual W lift. No extension of ω to all V is assumed.

For a solution (x,y), central parts z of p and u of q change the product by (1+T₁)z+T₁(1+T₂)u; this has span J. Using (1)–(4), the central coordinate of λ₁^p λ₂^q h⁻¹ w(c+C(x,y))⁻¹ modulo J is

 F(x,y)= d₁(x)+T₁d₂(y)+a₁(Δ₂y)
       +f(Δ₁x,T₁Δ₂y)+f(C(x,y),c)+z₀+ω(c+C(x,y)) mod J.  (8)

Here c+C(x,y) belongs to B by (5), and f(s,s)=q(s)=0 makes the final multiplication by w(s)⁻¹ introduce no extra central term. Equation (8) is an actual-lift expression: changing p,q's central coordinates adjusts exactly J, so F=0 is equivalent to the desired H-collision for that pair, provided the shadow equation is solvable.

## The homogeneous polar and rank matrix

Define D_i(v,w) as the polar of d_i. From (3) and (4),

 D_i(v,w)=E_i(v,w)+T_iβ(v,w)+f(v,T_i w)+f(w,T_i v).      (9)

For k=(x,y), k′=(x′,y′) in V₀, set C_k=C(x,y). The polar B_F of (8), computed about any actual solution of (5), is

 B_F(k,k′) = D₁(x,x′)+T₁D₂(y,y′)
   +E₁(Δ₂y,Δ₂y′)
   +f(Δ₁x,T₁Δ₂y′)+f(Δ₁x′,T₁Δ₂y)
   +f(C_k,C_{k′})  mod J.                                  (10)

The final term uses (7), since C_k,C_{k′}∈B. The z₀, c, the linear terms of a_i and the linear choices in ω disappear on polarization. Formula (10) is bilinear and alternating on V₀, as it must be. Although f changes with the ordered section, the intrinsic polar in Z/J is invariant after the corresponding coordinate identification; the displayed formula makes the section choice explicit rather than assuming individual terms are invariant.

To compute all 15 scalar ranks, choose an F₂-basis k₁,…,k_d of V₀ by row reduction of (6), and a basis of Z/J by row reduction of the known transposition matrices. Evaluate (10) on each pair (k_i,k_j). For each nonzero χ∈(Z/J)* form the binary d×d alternating matrix Mχ with entries χ(B_F(k_i,k_j)); its ordinary binary rank is exactly the scalar polar rank in the Fourier test below. Thus the matrix input consists only of q's invariant component coefficients, B's graph/basis, and the explicit S5 matrices. The affine solution vector, crossed-system lifts, a_i linear parts, z₀ and the actual W section are required only later to compute F's affine values and Arf signs. If every one of the 15 ranks is at least 8, the Fourier estimate below forces an actual collision whenever (5) is solvable.

The full-S5 identities and Fourier test below do not by themselves prove that (5) is consistent, eliminate the low-rank pencils, or determine the affine coefficients and Arf signs.


## Full-S5 coupling of the actual selected orbits

Since the marked set Λ is invariant under G and under the formal inversion involution, it is invariant under conjugation by each λ_i. For disjoint t₁,t₂, λ₁λ₂λ₁ lies above t₂ and is an actual selected mark. The unique selected P-orbit above t₂ therefore gives p∈P with
\[
 \lambda_1\lambda_2\lambda_1=p\lambda_2p^{-1},\qquad
 (\lambda_1\lambda_2)^2=p\lambda_2p^{-1}\lambda_2. \tag{11}
\]
By exchanging the two marks, the inverse of this commutator is a displacement of λ₁; displacement sets of an involution are inverse-closed, so the same holds for the commutator. Its shadow lies in \((1+t_1)V\cap(1+t_2)V\). In the six-point model the Klein group generated by the disjoint transpositions has point orbits of sizes two and four; on each U it has two regular summands. Hence this intersection has dimension \(2+2b\). In particular its two-point-orbit contribution must not be discarded as though the intersection were only \((1+t_1)(1+t_2)V\).

For adjacent transpositions t,u, the marks λ_t λ_u λ_t and λ_u λ_t λ_u lie over the same transposition tut and are in the same unique selected P-orbit. Thus for some p∈P,
\[
 (\lambda_t\lambda_u)^3=p\mu p^{-1}\mu,
 \qquad \mu=\lambda_u\lambda_t\lambda_u. \tag{12}
\]
The disjoint and braid identities hold simultaneously for every actual choice of representatives. They constrain actual central and affine data; neither is an assertion that arbitrary shadow coincidences lift, nor that the selected marks themselves satisfy the Coxeter relations.

## Fourier criterion for an actual residual

If (5) is inconsistent there is no collision for this chosen pair, and no residual F is defined. Suppose it is consistent, so A is an affine space with translation kernel V₀ of dimension d, and put Q=Z/J≅F₂⁴. For a nonzero χ∈Q*, let rχ be the binary rank of χ∘B_F. For any y∈Q, Fourier inversion gives
\[
 16|F^{-1}(y)|=2^d+\sum_{\chi\ne0}(-1)^{\chi(y)}
  \sum_{x\in A}(-1)^{\chi(F(x))}. \tag{13}
\]
A binary quadratic function with polar rank r has signed sum either zero, if its affine-linear part is nonzero on the polar radical, or of magnitude \(2^{d-r/2}\). Thus if all fifteen rχ are at least eight, every y occurs: the absolute total error is at most \(15\cdot2^{d-4}<2^d\). In particular 0 occurs and the original pair collides. Consequently any actual zero-free residual has a nonzero scalar polar of rank at most six. With the actual affine coefficients in hand, radical restrictions and Arf signs compute all fifteen sums and decide collision without enumerating every point of A.

This is an exact test and necessary rank obstruction, not an exclusion. It is not proved that the shadow equation is solvable, that (11)–(12) eliminate every low-rank pencil, or that an actual compatible zero-free assignment exists. The nonlinear crossed-system coefficients, the original stabilizer and marked section, and simplicity remain to be handled; a shadow-only model does not establish any of those objects.


## Reproducible formula control

The standalone [group-word control](../code/verify_bruck_residual_polar.py) uses Python 3.11+ with assertions enabled. It constructs a class-two group of order 32 and two commuting involutory automorphisms, checks the automorphism laws, and compares (8) with 64 direct group-word evaluations at a nonzero affine shadow offset. It then compares (10) with all 4096 ordered kernel pairs. The actual group product supplies the first comparison; it is not merely a comparison of two expansions of (8). The toy group is not an S₅ envelope or a Bol folder, and the test establishes neither the general formulas nor existence/nonexistence of the research branch. The coordinator read and ran the script with Python 3.12.14; all assertions passed. Independent proof/code reviews are recorded below.


## Independent mathematical and code review

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted exact source `6f17ba6210a02e02707d49f0a47fb89de46dfffa`, conditional on the cited actual-mark, module and stabilizer-lift inputs. Each checked the actual affine residual, its homogeneous polar, selected-orbit group identities and Fourier cutoff, and independently ran the committed standalone control with Python 3.12.14: all 64 direct group-word and 4096 polar comparisons passed. A subsequent editorial correction replaces the accidentally reused kernel name K in the basis instruction with V₀, as already defined in (6). These model reviews establish neither shadow solvability nor a classification of the remaining low-rank affine pencils, and the toy calculation is not an S₅ envelope or existence/nonexistence result.


## The affine cokernel obstruction and crossed-system gauges

Independently reviewed progress on 0323:C0010 under the pinned inputs. Retain the actual faithful simple Bruck-envelope hypotheses of [the nonsplit source](bruck-n-nonsplit-extension-lifts.md), especially Z=Φ(P)=N², V=P/Z=P6⊕U^b, and the unique selected P-orbit over each transposition in the r=2 branch. Use the actual residual and polar formulas above, independently reviewed at `6f17ba6210a02e02707d49f0a47fb89de46dfffa`. No shadow datum is asserted to lift, and no quotient is assumed to be a loop.

### Exact affine-span obstruction

For a disjoint pair whose shadow equation is solvable, let A=k0+V₀ be its actual affine solution space, Q=Z/J≅F₂⁴ and F:A→Q the actual residual. Let M_F≤Q be the linear span of all polar values B_F(k,k′), k,k′∈V₀. Then

 L_F:V₀→Q/M_F,     k↦F(k0+k)+F(k0) mod M_F

is linear. Its definition does not depend on k0: changing the affine basepoint changes the derivative only by a polar value. There is an intrinsic element

 o(F)=[F(k0)] ∈ (Q/M_F)/im L_F.                            (1)

It is independent of k0, and F(A) avoids 0 whenever o(F)≠0. Conversely, o(F)=0 is necessary but not sufficient for collision: it solves exactly the linear quotient equation, after which the remaining M_F-valued quadratic system can still omit zero. Thus the precise remaining affine question is whether full crossed-system, τ, H and selected-orbit relations force o(F)=0 for at least one admissible disjoint pair. This is a cokernel obstruction associated to the actual collision map; no identification with a standard group-cohomology class is asserted.

For instance, if dim M_F=2, the linear quotient has dimension two. This conditional observation does not assert that such data arise from an actual envelope.

### Dependence on actual action and stabilizer coefficients

Fix q, the chosen ordered P-coordinates, B and the affine shadow offset c. For the marked action α_i(v,z)=(T_i v,T_i z+a_i(v)), equation (3) of the reviewed residual above says the polar of a_i is fixed by q and T_i. Thus the difference between two such possible action-coordinate functions is an F₂-linear map L_i:V→Z. If both α_i are involutions, necessarily

 L_i T_i = T_i L_i.                                          (2)

Likewise two elementary W sections over the same B differ by a linear map ℓ:B→Z. If their g0=λ1λ2 h⁻¹ central coordinates differ by z∈Z while c is fixed, direct subtraction of residual formula (8) above gives

 ΔF(x,y) = L₁(x+Δ₂y)+T₁L₂(y)+ℓ(c+C(x,y))+z mod J.        (3)

Here C(x,y)=Δ₁x+T₁Δ₂y. Formula (3) is affine-linear on A, so it changes neither B_F nor M_F. It is an explicit interface for the remaining crossed-system freedom: the linear parts of the actual marked actions, the actual stabilizer graph and the central product coordinate control exactly the affine quotient data. However arbitrary choices of L₁,L₂,ℓ,z satisfying (2) need not arise from a single S5 extension, canonical τ, one actual subgroup H and the globally selected marked orbit. Determining the image of those full compatibility equations in the cokernel of (1), rather than assuming it vanishes, is the unresolved step.

Equations (1)–(3) reduce the question for each fixed q,B and solvable c to finite linear algebra once the actual compatible coefficients have been supplied: row-reduce the reviewed polar to obtain M_F, evaluate (8) at k0 and at k0+k_i for a kernel basis, and solve

 F(k0)+Σ_i x_i [F(k0+k_i)+F(k0)] ∈ M_F.                  (4)

If (4) is inconsistent, the actual selected disjoint fibers do not collide. If it is consistent, one still evaluates the residual quadratic system in M_F; Fourier/Arf computation decides it. Variation in the full crossed-system unknowns and the unknown x_i makes the joint existence problem generally bilinear; this note does not falsely call the whole family a single linear cohomology computation.

### Ordinary group-extension uniqueness at fixed q and quotient class

The realization in [the nonsplit source](bruck-n-nonsplit-extension-lifts.md), independently reviewed at `4c93742a59ccdd786f23598f0374f674c6f75fff`, constructs each e∈H²(S5,V) from M=Hom(V,Z), with H¹(S5,M)=H²(S5,M)=0 and H²(S5,Z)=H³(S5,Z)=0. These vanishings also give the following proposed uniqueness refinement. Fix the S5-actions on V,Z and q, and fix e. Up to an extension isomorphism inducing identity on V,Z,S5 (and possibly a central automorphism of P), at most one group G realizes those data.

Indeed choose a common representative V-valued cocycle for e by changing quotient sections. Any two choices of lifted S5 actions inducing the same actions on V,Z differ by a normalized M-valued 1-cochain. Their crossed-action equations with the same V-valued factor set make its coboundary zero. Since H¹(S5,M)=0, this 1-cocycle is a coboundary and one central automorphism of P aligns the two action systems. Their P-valued factor sets now differ by a Z-valued normalized 2-cocycle; H²(S5,Z)=0 makes it a coboundary and a central section change aligns them. The source's H²(S5,M)=0 and H³(S5,Z)=0 provide existence. This is a statement about ordinary groups/extensions only. It does not identify τ, W,H, marked orbits or their original transversal sections, and the compatibility of (3) with all those choices remains open.

Both this uniqueness deduction and the actual affine obstruction have the scoped independent reviews below. Their exact relevance may be superseded by a stronger full-S5 collision or by a realizable nonzero-o assignment; neither is currently known.

### The reviewed stabilizer torsor narrows ℓ

The [automatic stabilizer-lift section](bruck-n-nonsplit-extension-lifts.md#proposed-automatic-stabilizer-lift), accepted at `1818e2c44bee176638f1212fd8b36c6a8a92e5ba`, applies when B is F-stable, q-singular and contains the full fixed P6-plane. Since V/B is F-projective, H¹(F,V/B)=0; hence its subgroup Hbar≤G/Z over F with kernel B is unique up to V-conjugacy. For a fixed Hbar, the actual complements H to Z form, up to Z-conjugacy, a torsor under Hom_F(B,Z). Therefore, once Hbar and one reference complement are aligned, the variations ℓ in (3) that come from stabilizer lifts are F-equivariant, rather than arbitrary elements of Hom(B,Z). This is an additional genuine linear restriction on the affine parameters. The torsor's existence and parametrization do not prove H corefree or τ-fixed, or produce any original section; those remain constraints on the allowed torsor points and on the marked maps L_i,z. This paragraph is a deduction from the reviewed stabilizer source; its use with (1)–(4) has the scoped independent reviews below.


### Independent review of the affine cokernel and crossed-system gauges

GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted this appended section at exact source `dd2f0fc5c4db866f93afe898d3a9a25382774489`, conditional on its pinned structural, source and cohomological inputs where applicable. They checked basepoint independence, the one-way zero obstruction, actual affine variation, ordinary extension uniqueness at fixed q and quotient class without assuming Z(P)=Z, and the stabilizer-torsor restriction. No new computation or fresh primary-source audit was performed. These are model mathematical reviews, not human or formal certification. The stated restrictions and unresolved reconstruction conditions remain: these deductions do not complete the unrestricted classification.
