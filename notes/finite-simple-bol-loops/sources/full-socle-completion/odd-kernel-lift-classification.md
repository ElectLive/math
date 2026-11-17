# Odd marked lifts: exact-cover assembly and pointed isomorphism

Independently reviewed finite-data parametrization for [0323:C0010](../foundations/research-C0010.md), the open residual classification frontier. Its interfaces are the canonical-folder and normal-subloop criterion C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, the scoped C0007 inversion input and C0011 prime-power exclusion at `932ead5db5f39045e2085caa6b062f6b981b2813`, the actual odd-layer fibers at `17e56bdfb16097218249f42f10e91adcb9f5a4b8`, and weighted fibers at `c9b83d37421da818e57ef69227bd04293862540d`. The exact-cover restriction uses the [odd-kernel stabilizer orbit theorem](odd-kernel-stabilizer-orbits.md) at `8c35369a08f93f123b7a86c9dd1e91ef0c5e3be3`, whose independent reviews are recorded at `21212030ea6260d216baf38ce84779c085253352`. The orbit/count part used here does not require that source's deeper Glauberman and Feit–Thompson argument; their exact locators and qualifications are in project `REFERENCES.md`. All groups are finite; no quotient loop is assumed. The result describes the branch admitting a nonzero τ-stable odd elementary normal subgroup; it does not bound its inputs or settle the unrestricted classification.

## Enumerating the extension and the marked classes

Choose a finite group L, an automorphism θ with θ²=1 (allow θ=1), a subgroup J≤L, an odd prime p and a nonzero finite Fp-module V for Ē=L⋊⟨t̄⟩, with t̄²=1 acting by θ on L and by σ on V. Also choose a J-invariant subspace W≤V. Enumerate normalized 2-cocycles F:Ē×Ē→V satisfying F(1,q)=F(q,1)=0, the usual cocycle identity, and F(t̄,t̄)=0. The multiplication `(v,q)(w,r)=(v+T_q w+F(q,r),qr)` builds E, with t=(0,t̄) an involution, G the inverse image of L, τ=conj_t on G and G/V=L. Every relevant extension with its distinguished involution occurs: choose a normalized section sending t̄ to t. Enumerating all cocycles may repeat isomorphic data; the pointed isomorphism test below removes repetition. The choices θ and the full Ē-action must be compatible, namely σT_lσ⁻¹=T_{θ(l)}.

Compute the Ē-conjugacy classes of involutions in Ē\L. For each class C and each outside double coset D=JxJ it meets, compute its J-conjugacy orbits in D. Discard C if it has more than one such orbit in any D. On the remaining classes form the 0–1 incidence matrix of classes against all outside J-double cosets. Choose an exact cover of the double cosets by class supports, requiring the class of t̄ and exactly one chosen class meeting each double coset. Let S be their union. For each chosen class and each double coset it meets, choose x in its unique J-orbit and set B=J∩x⁻¹Jx and `r_x=dim ker(1+T_x)`. Require the local equation

    [B:C_J(x)] p^{r_x} = [V:W].                              (0)

Conjugacy makes the test independent of the representative. To see necessity, the pinned odd-kernel source proves that in any actual folder `S∩xJ=x^B` and each outside J-double coset has exactly one selected J-orbit; all involution lifts of a selected x are selected, numbering p^{r_x}. Transversality above xJ gives (0). Equivalently, the selected classes provide an exact cover with these local weights. These are necessary prefilters, not by themselves sufficient: the affine collision, count, generation and core tests below remain mandatory. They do not assert that S is the full outside involution set or that t̄S is a quotient loop.

For fixed finite input, cocycles, involution classes, incidence covers, subspaces, cochains and all later tests are finite and effectively enumerable from multiplication tables. This is an exact parameterization, not a finite list uniform over all L, p and dimensions.

## Data and forced marks

Write π:E→Ē for the projection, regard V additively and let T_q be the given module action. Define `Λ` as the set of *all involutions* in `π⁻¹(S)` and `K=tΛ`. Every quotient involution has an involutory lift: its preimage over its order-two subgroup has odd normal Hall subgroup V. Its involutory lifts form one V-conjugacy orbit, namely `N_x λ_x`, where `λ_x` is any involutory lift and `N_x=ker(1+T_x)=im(1−T_x)`. Thus Λ is E-conjugacy invariant, contains t, and its projection is exactly S. Conversely, for an actual canonical folder its selected marks have precisely this form: conjugacy invariance forces each entire fiber, but not quotient involutions outside S. Set `r_x=dim N_x`; then `|K|=Σ_{x∈S}p^{r_x}`. The invariant involution set implies `1∈K`, `K⁻¹=K` and `kℓk∈K`.

## Stabilizer cochains

For the selected J,W choose a normalized section `s:J→π⁻¹(J)∩G`, with `s(1)=1`, and define `f(j,k)∈V` by `s(j)s(k)=f(j,k)s(jk)`. Write `M=V/W`. Since W is J-invariant, `P=π⁻¹(J)∩G` satisfies `W◁P`. Subgroups `H≤P` with `H∩V=W` and image J correspond bijectively to complements of M in `P/W`: they are determined by functions `b:J→M` with `b(1)=0` and

    b(j)+T_j b(k)+f(j,k)+W = b(jk).                       (1)

Namely `H_b={v s(j): j∈J, v+W=b(j)}`. Solutions exist exactly when the restricted extension class vanishes in `H²(J,M)`; if nonempty they form an affine torsor for `Z¹(J,M)`. Conjugating H by `v∈V` changes `b(j)` by `(1−T_j)v+W`. These coboundaries act through M, including the possibility of a nontrivial kernel.

## Products and the forbidden affine arrangement

Since `K⁻¹K=Λ²` and Λ is E-invariant, K is collision-free for H and every conjugate of H exactly when `H∩Λ²={1}`. For `x,y∈S` write `j=xy∈L`. Only pairs with `j∈J` can meet H. Fix involution lifts `λ_x,λ_y` and put

    c_xy=λ_x λ_y s(j)⁻¹ ∈ V,   A_xy=N_x + T_x N_y ≤ V.   (2)

The entire product fiber is `(c_xy+A_xy)s(j)`. Therefore, for `x≠y`, there is a collision exactly when

    b(j) ∈ (c_xy+A_xy+W)/W.                               (3)

For `x=y`, use the same lift in both positions: `j=1`, `c_xx=0`, and `A_xx=N_x`. The diagonal condition is precisely `W∩N_x=0`. Its negation gives a nonidentity element of `H∩Λ²`; distinct quotient marks automatically give distinct lifted marks. No τ transport is missing here: these are product directions in Λ, rather than section-fiber directions in K.

For fixed x,y, (3) is empty or an affine subspace in the solution torsor of (1). It descends to an affine subset of the torsor under `H¹(J,M)`: for every v,

    (1−T_j)v = (1−T_x)v + T_x(1−T_y)v ∈ N_x+T_xN_y,

so every coboundary preserves (3). Equivalently, both full lift fibers are individually V-conjugacy invariant. Each forbidden set can have any codimension, be empty, or be the entire torsor; it need not be a hyperplane. Changing the chosen λ lifts changes c_xy within A_xy, so (3) is intrinsic. This cohomology quotient is valid for collision feasibility; it is not in general the loop-isomorphism quotient.

The exact folder-recognition conditions are: all diagonal tests; avoidance of all forbidden sets (3); and the scalar count

    Σ_{x∈S} p^{r_x} = [L:J] p^{dim V−dim W}.                (4)

The first two give injectivity of K into every G-conjugate coset space; (4) gives surjectivity. Conversely, an actual folder has all these properties. Also separately impose `Core_G(H_b)=1` and `<K>=G`; then the standard faithful generated folder interface gives the canonical loop. Generation is tested by subgroup closure in the constructed finite group. For a single minimal elementary layer in the even simple branch, the orbit theorem forces p to divide |J| and dim V≤2|L|. Thus all such layer data at fixed L, θ and J form a finite search, even without specifying a prime or dimension.

## Exact simplicity, Bruck and properness tests

For a faithful generated folder, C0001 gives the following test entirely in G: the loop is simple exactly when, for every normal subgroup `N◁G` with `H_b < H_b N < G`,

    |KN/N| > [G:H_b N].                                    (5)

One counts distinct products, not an assumed quotient loop. For an even-order simple loop with V nonzero, core-freeness gives `H_b<H_bV`, and `H_bV<G` since `[H_bV:H_b]` is odd. Thus (5) yields the scalar strict inequality `|KV/V|>[L:J]`. For simple proper loops in either parity the same conclusion follows using the separately pinned C0011 prime-power exclusion. Weighted fiber counting further gives `|KV/V|−[L:J]` a positive multiple of `p−1`, but it does not replace (5) for the other normal subgroups.

The loop is Bruck exactly when `τ(H_b)=H_b`: in one direction τ induces inversion on the coset loop; in the other, the automorphic inverse property induces an automorphism of the canonical group carrying `L_x` to `L_{x⁻¹}`, which is τ because K generates G. This is an exact algebraic test. If `θ=τ̄|L`, `σ=τ|V`, the scalar cochain version requires `θ(J)=J`, `σ(W)=W`, and, with `τ(s(j))=q(j)s(θj)`,

    b(θj)=σ b(j)+q(j)+W  for every j∈J.                   (6)

For an explicit non-Moufang test, define `a*b` as the unique element of `K∩abH_b`. Count triples `(a,b,c)∈K³` on which `(a*b)*(c*a)=(a*(b*c))*a` fails. The loop is non-Moufang exactly when this nonnegative integer is positive. In particular neither non-Bruckness nor any marked-fiber scalar count alone establishes non-Moufangness.

## Exact pointed isomorphisms

For two such datasets (possibly with different groups), a pointed isomorphism means a loop isomorphism carrying the chosen layer V onto V′. Canonical-folder uniqueness makes it equivalent to a group isomorphism `α:G→G′` carrying `(H_b,K,V)` to `(H′_{b′},K′,V′)` and commuting with τ. Equivalently it extends uniquely to `E→E′` carrying `t` to `t′`, V to V′, and Λ to Λ′. Therefore its induced isomorphism `β:Ē→Ē′` sends L to L′, `t̄` to `t̄′`, J to J′, and S to S′; its restriction `A:V→V′` is a compatible module isomorphism and sends W to W′.

To display all extension automorphisms, choose normalized sections `r:Ē→E`, `r′:Ē′→E′` with `r(t̄)=t`, `r′(t̄′)=t′`, and whose restrictions to J,J′ are the stabilizer sections. Write their factor sets as `F(q,r)` and `F′(q′,r′)`. An extension isomorphism is uniquely

    v r(q) ↦ (A(v)+u(q)) r′(βq),

where `u:Ē→V′`, `u(1)=u(t̄)=0`, A intertwines the actions, and for all q,r

    A F(q,r)+u(qr)=u(q)+T′_{βq}u(r)+F′(βq,βr).          (7)

The notation on the right means a V′ element multiplying the chosen section. In addition the stabilizer must satisfy

    b′(βj)=A b(j)+u(j)+W′   (j∈J).                       (8)

Conversely, all these conditions yield a pointed loop isomorphism: β carries S to S′ and the complete involution lifts then carry Λ to Λ′. For fixed compatible A,β, if one solution u to (7) with u(t̄)=0 exists, all such u form a torsor for `Z¹(Ē,V′)` with the β-twisted action, restricted by `z(t̄)=0`. In particular extension automorphisms fixing t and inducing the identity on both Ē and V are exactly `Z¹(Ē,V)` with `z(t̄)=0`; their effect on b is `b(j)↦b(j)+z(j)+W`. General pointed isomorphism orbits include these automorphisms and every residual compatible pair (A,β) for which (7) is solvable.

Coboundaries from arbitrary V-conjugation do not automatically lie in this automorphism group: conjugation by v fixes t only when v∈C_V(t). Thus replacing the actual cochain b by its H¹ class generally loses isomorphism information even though the forbidden arrangement descends. For a family of groups, pointed orbits become ordinary loop-isomorphism classes if the chosen V is specified functorially across the entire family: every relevant group isomorphism must carry the chosen V to the chosen V′. A fixed characteristic V in one fixed G suffices for comparisons among data with that same G and that same V. Merely choosing some characteristic layer independently in each of two different groups does not ensure that an isomorphism maps one choice to the other. In general, to obtain ordinary loop-isomorphism classes, compare across all chosen layers and identify datasets whenever an isomorphism of their unpointed canonical folders exists; equivalently allow pointed comparisons after moving the layer on one side. The pointed classification alone does not settle that orbit problem.

## Independent mathematical review

GPT-6.1 Terra reviewers contributor 1 and contributor 2 independently accepted this assembly at `e8644c4779fe3ad9cc03c69f97d2ac8071a95a05`. Both examined the normalized extensions, local orbit and complete-lift conditions, affine collisions, folder and simplicity tests and pointed isomorphisms. The former explicitly checked the finiteness conclusion for a minimal layer in the even simple branch. These model mathematical reviews retain the canonical-folder, inversion, prime-power and stabilizer-orbit inputs. Neither reviewer performed finite computations or an independent audit of all the imported theorems.
