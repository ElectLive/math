# Fixed-plane and socle incidence in the two-N shadow

**Mira Cult**

**Theorem with the scoped independent reviews below.** This is a bounded continuation of [0323:C0010](../../claims/0010.md). It studies only the stated two-N, marked-rank-two Bruck-envelope branch. It does not classify Bruck loops, establish an original transversal, or assert that any shadow counted below lifts to an envelope.

Let `(G,H,K,τ)` be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Assume `P=O₂(G)` has class at most two and exponent at most four, `Z=Φ(P)≅N²` is central in P, `V=P/Z≅P6⊕U^b` as an `S5=G/P` module, and H maps onto `F=F20`. Let `W=H∩P`, and let `B` be its image in V. Assume the actual marked map at a selected transposition has rank `r=2`. Let `c` be the multiplicity of `N|F` in the pure intersection `B∩soc(U^b)`. The reviewed inputs below give `c≤1`, the full F-fixed plane of P6 inside B, and `β(1,V)≠0`, where `β` is the polar of the P square map and `1` is the constant vector in P6.

**Claim.** Under these hypotheses, `c=1`, the map `β(1,−):V→N²` has image one copy of N, and the U-top image of B has multiplicity dimension `b−1`. If `A:F2^b→F2²` is the corresponding rank-one top-multiplicity matrix, `T=ker A`, and `z⊗N` is the pure U-socle intersection, then `z∈T`. For `b=3` this leaves at most 1,344 F-submodule shadows before the remaining quadratic, actual-lift and transversal tests.

The module definitions and block separation are in [bruck-s5-module-blocks](bruck-s5-module-blocks.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499); the actual fixed-plane and nonzero-polar inputs are in [bruck-n-affine-fiber-parity](bruck-n-affine-fiber-parity.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3c3cafff03f9e9d79640b68f03883c22e57210d6) and its cited fixed-vector/core sources; and `c≤1` at `a=2,r=2` is the scoped bound in [bruck-n-nonsplit-extension-lifts](bruck-n-nonsplit-extension-lifts.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff). These inputs retain their own hypotheses and review scopes; no new exact-source review of the present claim is asserted.

## Rank one and the one-dimensional socle intersection

The F-fixed part of B is the full two-dimensional fixed plane of P6, and its nonfixed part `B_S` has multiplicity dimension `b+1` over the projective simple F-module `S=N|F`. Since `1` is S5-fixed, `β(1,−):V→N²` is S5-equivariant. The reviewed module facts give `Hom_S5(P6,N)=0` and `Hom_S5(U,N)=F2·top`, so this nonzero map is represented on the U-top multiplicities by a nonzero `2×b` binary matrix A.

The kernel of the U-top projection on `B_S` lies in the sum of the one-dimensional P6_S multiplicity and the U-socle multiplicity space. Its intersection with the latter has dimension `c≤1`, so this kernel has dimension at most two. Hence the top image of `B_S` has dimension at least `b−1`. The actual W shadow is polar-isotropic and contains `1`, so its top image is contained in `ker A`. Since A is nonzero, its kernel has dimension at most `b−1`. Equality holds throughout: `rank A=1`, the top image equals `T=ker A`, the projection kernel has dimension two, and its pure-socle intersection has dimension `c=1`. This uses the actual shadow and requires no splitting of G or of its quotient by P.

## The P6–U cross identity

Let `D=F∩A5≅D10`, let `f=e_F` be the point vector in the six-point permutation module `P6=F2[S5/F]`, and write `1` for the sum of its six point vectors. Use the standard two-copy model `U=N⊗F2[S5/A5]`: on restriction to A5 it is `N⊕N`, and an odd element of F acts on N and interchanges the two copies. Identify the top quotient with N by `(x,y)↦x+y` and the socle with N by `x↦(x,x)`.

For every S5-equivariant bilinear map `γ:P6×U→N` and every `u∈U`,

    γ(f, soc(top u)) = γ(1,u).                                  (1)

Here the socle embedding and top quotient are the synchronized maps just defined. In particular `γ(1,−)` vanishes on the socle.

To prove (1), let `φ(u)=γ(f,u)`. It is F-equivariant. A 5-cycle `r∈D` acts irreducibly on the even-weight natural five-point module N because `Φ5` is irreducible over F2, so its endomorphism centralizer is F16. The D-involution sends r to its inverse, whose action on F16 is the square of Frobenius; therefore `End_D(N)=F4`. Let the restriction of φ to the first A5-copy of N be `a∈F4`. An odd 4-cycle of F conjugates r to r² and interchanges the two copies, so its second-copy coefficient is `a²`. Thus

    φ(x,0)=a x,  φ(0,x)=a² x,  φ(x,x)=(a+a²)x.                 (2)

Choose six even coset representatives for `S5/F≅A5/D`. Equivariance gives

    γ(1,(x,0)) = (Tr_D^{A5} a)x.                               (3)

This relative transfer lies in `End_A5(N)=F2`. It kills 1 because `[A5:D]=6`. For `a=r+r⁻¹`, its transfer is the sum of one A5 conjugacy class of twelve 5-cycles: each of the six Sylow-five subgroups supplies its pair `r_g,r_g⁻¹`. On the natural five-point permutation module, none of these 5-cycles fixes a point, and exactly three send any chosen point to any other chosen point. Over F2 this class-sum matrix is `J+I`. It acts as I on the even-weight submodule N because J vanishes there. The transfer is therefore the nonzero F2-linear map `F4→F2` killing 1, namely `a↦a+a²`. Applying this also to `a²` proves (1) and the asserted vanishing on the socle. This argument is elementary and uses neither a finite basis enumeration nor a marked-map condition.

## Incidence and the b=3 count

Apply (1) separately to each of the two N components of the actual polar and each U summand. Since B contains both f and the pure socle line `z⊗N` and is polar-isotropic, `β(f,z⊗N)=0`. Equation (1) identifies this with the action of A on z, so `A z=0`, i.e. `z∈T`.

For `b=3`, in the F20 multiplicity space `P6_S⊕soc(U³)⊕top(U³)`, there are 7 choices for the two-dimensional top plane T, then 3 choices for the pure socle line `z≤T`. The other kernel generator is `x+v` with x the nonzero P6_S coordinate and v taken modulo z, giving 4 choices. Finally, the graph from T to the two-dimensional quotient of `P6_S⊕soc(U³)` by this kernel has `2⁴=16` choices. The fixed part is the full F-fixed plane. Thus at most `7·3·4·16=1,344` shadows remain.

These are submodules in a chosen synchronized F20 multiplicity model, not isomorphism classes. They may fail the rest of `q|B=0`, the actual marked-rank condition, corefreeness, compatible τ/H lifts, the selected-class collision test or the radical transversal condition. Module automorphisms can simplify some graph parameters while TRANSPORTING the entire quadratic datum, but they need not preserve a fixed q; no such fixed-q gauge is assumed here. The reduction leaves C0010 and the two-N envelope problem open.


## Independent mathematical review

reviewers contributor 1, contributor 2 and contributor 3 independently accepted this complete manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e01de6619af5ace529ef8469a36d4808512f7061), conditional on its pinned module, fixed-plane, nonzero-polar, marked-rank and socle-bound inputs. They checked the rank-one/c=1 dimension squeeze, the unrestricted P6–U cross identity via the F4 centralizer and explicit A5/D10 transfer, z∈ker A, and the 1,344-shadow count. They did not reprove all upstream inputs, audit fresh primary sources, or claim an actual lift or transversal. This proof is analytic; no new computation establishes the result. These are model mathematical reviews, not formal GitHub approvals or human/formal certification. The separate stable121 review at the same commit has a different outcome and scope, recorded in its own manuscript.


## Two transported shadow forms

**Independently reviewed continuation at the source below.** Under the same actual-envelope hypotheses and the now-reviewed incidence conclusion, only two transported shadow forms remain for b≥3, and the b=3 candidate count is at most 1,008.

Let E=F2^b, let T=ker A and let x be the P6_S multiplicity coordinate. The kernel of the top projection is span{x+v,z}, with v defined modulo z and 0≠z∈T. All multiplicity spans represent copies of S=N|F.

For every b, an S5-equivariant automorphism 1+εM of U^b, for arbitrary M∈End_F2(E), fixes the top quotient and adds M(k) to the socle component of a lift of top coordinate k; it fixes the socle and P6. Write the top graph of B_S modulo span{x+v,z}. Subtract any x-component of a lift using x+v, which does not change its top coordinate. Then its remaining socle component is a linear map T→E/<z>. Choose a linear lift T→E and extend it to M:E→E. The shear 1+εM eliminates that graph. It is invertible, with inverse itself. Thus after transporting the entire square map, polar form and envelope structure along this module isomorphism, B_S=span{x+v,z,top T}. No assertion is made that the shear preserves the original fixed quadratic map.

GL(E) acts transitively on flags <z>⊂T of these dimensions, and its flag stabilizer is transitive on each of the three possibilities v∈<z>, v∈T\<z>, and v∈E\T. The generator x+v is defined modulo z, so the first case is v=0. The middle case exists for b≥3, the outside case for b≥2. These give a cover by transported models; no claim is made that the last two are inequivalent under the full automorphism group or after changing the full quadratic datum.

The case v=0 cannot occur in an actual envelope. Since the fixed plane is present, x supplies all P6. The shear-normalized B also contains the U-submodule with socle z and top z because z∈T; hence B contains P6⊕U_z as an S5-submodule. It has transposition rank 3+4=7. This contradicts the rank bound ≤3a=6 for S5-stable submodules of the actual shadow when Z≅N², reviewed in `bruck-two-n-two-u-exclusion.md`, Actual stable-shadow rank bound, exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/a1f42ac3a21ce22edef96845f6cdf379511b2a51). Applying the shear transports the entire envelope data, so the actual-shadow bound remains applicable. Equivalently, the same source's lift argument proves the inclusion even before normalizing the top graph.

For b=3, the pre-incidence count is 7 choices T, 3 choices <z>≤T, 4 choices v mod z and 16 top graphs: 1,344. The excluded class v mod z=0 comprises 7·3·1·16=336 distinct shadows, leaving at most 1,008. These are actual subspaces in the chosen synchronized model, not orbit classes or proven realizable shadows. Further quadratic, core, marked and transversal conditions remain.


### Independent review of the two-form reduction

contributor 1, contributor 2 and contributor 3 independently accepted the preceding two-form section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8aa8130e5f07aa490f3d32a0fa8692c9e5bdd266), conditional on the pinned module, incidence and actual stable-shadow rank inputs. They checked that the shear transports the entire quadratic/envelope data, the flag cases give a cover, the pure-P6 case has rank 7>6, and removing its 336 shadows leaves at most 1,008. No new computation or external-source audit was claimed. This review does not cover the subsequent one-form strengthening until separately recorded.

## One transported shadow form

**Independently reviewed continuation at the exact source below.** In the preceding setting, the surviving shadow has a single normal form when the entire quadratic datum is transported along the indicated module automorphisms. Write `E=F2^b`, `T=ker A`, and choose the synchronized F20 nonfixed coordinates `x` in P6, `soc(E)` and `top(E)`. The preceding incidence gives `0≠z∈T`, and the top-projection kernel of `B_S` is `span{x+soc(v),soc(z)}`, with v defined modulo z.

An S5-equivariant automorphism `1+εM` of `U^b`, with arbitrary binary matrix M, fixes the top and socle and adds M applied to a top coordinate in the socle. First eliminate any x component of the top graph using the kernel generator `x+soc(v)`, and then choose M to eliminate its remaining socle graph. Thus, after transporting q, its polar and the entire envelope data, `B_S=span{x+soc(v),soc(z),top(T)}`. This is a transport of data, not an assertion that the automorphism preserves a previously fixed q.

We show that `v∈T`. The full scalar P6–U cross-map space has dimension two, and the two maps whose restrictions are computed in [bruck-n-p6-one-u-exclusion](bruck-n-p6-one-u-exclusion.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1a8a1eddcdfaeb5fab6f3e7682a37c5597a3b522) span it: that source computes two independent maps in the d=0 subspace, while the full dimension is two in [the component source](bruck-n-frattini-quadratic-support.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b40066d01085772606b1d1160d58c033b8ba3302). Both vanish on `P6_S×soc(U)`. The same component source proves that every U–U pair polar vanishes on two socles. The polar of a single U summand is also an S5-equivariant bilinear map `U×U→N`, so it belongs to the same full two-dimensional pair-map space and vanishes on two socle vectors. Consequently, on the mixed copy `x+soc(v)` the polar is exactly that of the P6 restriction.

The unique nonzero scalar equivariant quadratic map on P6 has nonzero polar on `P6_S`. Here is an elementary proof. Identify P6 with the six-point permutation module, let f be its F-fixed point, and let `P6_S` be the even-weight subspace on the other five points. If the polar β vanished there, S5-transitivity would give the same vanishing on every such five-point even subspace. For distinct i,j,k choose a point outside the triple; then `β(e_i+e_j,e_i+e_k)=0`. These identities imply β vanishes on `J×J`, where J is the full augmentation kernel. Thus for `u∈J`, the value `β(e_i,u)` is independent of i and defines an S5-map `J→N`. It is zero by the reviewed principal/N block separation in [bruck-s5-module-blocks](bruck-s5-module-blocks.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499). Hence β is zero on all of P6. The quadratic map would then be linear and hence an S5-map `P6→N`, also zero by block separation, a contradiction.

Since the actual shadow is polar-isotropic, each scalar central component has zero P6 quadratic coefficient. In particular `β(f,x)=0`. The cross identity (1) gives `β(f,soc(v))=A v`, so isotropy of `f` and `x+soc(v)` forces `A v=0`, as claimed.

If `v∈<z>`, replace the mixed generator by x. The normalized shadow then contains the S5-submodule `P6⊕U_z`, since `z∈T`; a transposition has rank `3+4=7` on it. This contradicts the actual stable-shadow rank bound `3a=6` for `Z≅N²` in [bruck-two-n-two-u-exclusion](bruck-two-n-two-u-exclusion.md), independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/a1f42ac3a21ce22edef96845f6cdf379511b2a51). Hence `v∈T\<z>`, so necessarily `b≥3`. A binary change of U multiplicity coordinates puts `T=e1⊥`, `z=e2` and `v=e3`. This proves a single covering form under transport; it does not assert a fixed-q gauge or classify lifts.

For `b=3`, the earlier count has 7 choices of T, 3 of z, 4 of v modulo z and 16 top graphs. The condition `v∈T\<z>` leaves one choice modulo z, hence at most `7·3·1·16=336` candidate shadows in the chosen synchronized model. They remain subject to all the quadratic, lift and original-transversal conditions listed above.


### Independent review of the one-form reduction

contributor 1, contributor 2 and contributor 3 independently accepted the preceding one-form section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/243974128b27510c9783d871d5e3be31e4a016b8). They checked the full-space cross and socle-pair restrictions, the elementary augmentation-kernel/block argument for the P6 polar, the deduction v∈T, the rank exclusion of v∈⟨z⟩ and the 336-shadow count. Acceptance is conditional on the precise module and actual-shadow inputs cited there; no upstream certificate reproof, new computation or fresh primary-source audit was claimed. These are model mathematical reviews, not fixed-q equivalence classifications, existence proofs or formal GitHub approvals. The later seven-block theorem has its own review obligation.

## Seven-block quadratic and actual-envelope reduction

**Theorem with the scoped independent reviews below.** Under the preceding hypotheses and using the independently reviewed one-shadow reduction, transport the data so that `T=<e2,...,eb>`, `z=e2`, `v=e3`, and the shadow has the displayed one-form. For one scalar central component, the space of equivariant quadratic maps vanishing on this shadow has dimension `2b+2`; prescribing its coefficient in `β(1,−)` leaves dimension `2b+1`. The two-component quadratic datum is supported on P6 and at most seven U blocks. Moreover the actual group, inversion and stabilizer admit

    G=G0⋉Y,  P=P0×Y,  τ(G0)=G0,  τ|Y=1,
    H=(H∩G0)⋉D_Y,

where `Y≅U^s`, `P0/Z≅P6⊕U^a` with `a≤7`, and `D_Y` is the standard F20-simple top complement in Y. In particular `|G0|≤120·2^70`. The original marked section K is retained in G; no splitting of K or solution of its transversality and simplicity tests is asserted.

The full component dimensions and U–U restriction identities used below are those of [the quadratic-support source](bruck-n-frattini-quadratic-support.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/b40066d01085772606b1d1160d58c033b8ba3302); the P6 cross restrictions are those of [the one-U source](bruck-n-p6-one-u-exclusion.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1a8a1eddcdfaeb5fab6f3e7682a37c5597a3b522). The actual passive transport interfaces are in [the multiple-N source](bruck-multiple-n-frattini.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/39a493024a9ee0839852b60f389fe28d155701b9) and [the section source](bruck-n-frattini-sections.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ced6706720b08adb94f4497534b2208f5c1a3d51). These are inputs, not reviews of this new theorem.

### Restriction to the top complement

The unrestricted scalar quadratic space `Q(U,N)` has dimension two, and its restriction to the synchronized F20-simple complement D to the socle is injective. To see this without a new finite enumeration, write `U=N⊕N` on restriction to A5, with odd elements acting naturally on N and swapping copies. For the even-weight subspace `N≤F2^5`, define

    B(x,y)=x*y+(x·y)1,
    qlin(x,y)=x+y,       qnonlin(x,y)=B(x,y),

where `*` is coordinatewise product. These are equivariant quadratic maps U→N. They are independent because `qnonlin(x,x)=x` whereas `qlin(x,x)=0`, and hence form a basis by the reviewed dimension calculation.

Choose `r=(01234)` and `ω=r+r⁻¹`. The D10 centralizer on N is F4 and `ω²+ω+1=0`. The graph `D={(x,ωx):x∈N}` is F20-stable: an odd normalizing 4-cycle swaps copies and conjugates ω to `ω²=ω⁻¹`. The other synchronized complement is obtained by swapping copies. For `x=e0+e1`, `y=e0+e2`,

    ωx=e0+e1+e2+e4,  ωy=e3+e4,
    B(x,ωy)+B(y,ωx)=y≠0.

Thus qnonlin has nonzero polar on D, while qlin restricts to the nonzero linear map `1+ω`. Their restrictions are independent.

### Quadratic components and support

Fix one scalar central projection. Its P6 component vanishes by the preceding polar argument. The shadow contains `D⊗T`; hence injectivity of `Q(U,N)→Q(D,N)` kills both square coefficients on each `Ui`, `i≥2`. The full two-dimensional U–U pair space restricts injectively to `D×D`, so polar isotropy kills both pair coefficients for each `Ui,Uj` with `i,j≥2`.

For `i≥2`, isotropy of `x+soc(v)` against `D_i` now reduces to the P6–Ui cross term, because `v∈T` and all squares and pair terms on T vanish. In the reviewed cross basis `β0,β1`, only β1 has nonzero `P6_S×D` restriction, so its coefficient is zero. Isotropy of the fixed point f against `D_i` kills the β0 coefficient: `β0(f,D_i)` is the top identification and `β1(f,D_i)=0`. Thus the only possible scalar coefficients are two U1 squares, two P6–U1 crosses, and two U1–Ui pairs for each `i≥2`. Conversely each of these terms vanishes on the displayed shadow, giving dimension `2+2+2(b−1)=2b+2`. The `β(1,−)` value on U1 fixes one independent P6–U1 coefficient, leaving `2b+1` parameters.

For the two central components, the remaining U1–T pairs give four binary rows on T. Choose a subspace L of T containing z and v and mapping onto the joint row image; `dim L≤6`. Choose a complement `T0≤T` contained in all four kernels. After the binary multiplicity change `T=L⊕T0`, all terms involving U(T0) vanish. No diagonal correction is introduced inside T, since the entire quadratic restriction and pair polar there are already zero. Consequently q and its polar are supported on the outside coordinate U1 and at most six coordinates in L. The change transports the full datum; it is not a fixed-q automorphism.

### Actual passive group and stabilizer

Let Y denote the passive U-summand, `D_Y` its literal top complement in the shadow, and `P0` the full preimage of the active shadow plus Z. The full preimage of Y in P is elementary abelian and central in P, because q vanishes on Y and its polar with V is zero. As an S5-module it is an extension of Y by Z; projectivity of U gives an S5-equivariant complement `Y0≅Y`.

The actual W lifts of `D_Y` are the graph of an F20-map `D_Y→Z`. Each such map extends to an S5-map `Y→Z`: both relevant scalar Hom spaces are one-dimensional, and restriction of the top map to D is nonzero. Adjusting the S5 complement by this map makes `D_Y≤W` literal. The original Bruck factorization shows τ fixes V, and the class-two central elementary Z is generated by squares, so τ fixes Z as well; the explicit multiple-N proof is reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6fe18de73836f5babe8bff5be255ff80fc864fb7). On the central elementary preimage, τ is an S5-equivariant shear `Y→Z`. Since τ fixes W and Z pointwise, that shear vanishes on `D_Y`; every such S5-map factors through top, on which D maps isomorphically. Therefore τ fixes Y0 pointwise.

Now `P=P0×Y0`, and P0 is τ-stable because τ fixes V and Z. The quotient `G/P0` is an extension of S5 by Y0. Projectivity gives `H²(S5,Y0)=0`, so choose a complement to Y0 there and let G0 be its inverse image. Then `G=G0⋉Y0` and `P0≤G0`. Because the normalized shadow is the literal direct sum of its active part and `D_Y`, and `W∩Z=1`, one has `W=(W∩P0)×D_Y`. The remaining passive component of H gives a cocycle `F20→Y0/D_Y`. The latter is projective as an F20-module, so its first cohomology vanishes. Conjugation by a suitable element of Y0 removes that cocycle; this conjugation is τ-fixed. Thus `H=(H∩G0)⋉D_Y`.

Finally τ preserves P0 and fixes Y0. Its deviation from preserving G0 is an S5-cocycle into Y0. Projectivity gives `H¹(S5,Y0)=0`, so this cocycle is principal. It vanishes on F20 because τ fixes H pointwise and H has the displayed form; its principal vector is therefore F20-fixed. Since `Y0^F20=0`, that vector is zero and τ preserves G0. Renaming Y0 as Y gives the stated splitting. The active radical has order at most `2^(6+8·7+8)`, and its quotient is S5, giving `|G0|≤120·2^70`. The original section remains in G and still requires its actual marked-fiber, collision, generation and normal-subloop tests.


### Independent review of the seven-block theorem

contributor 1, contributor 2 and contributor 3 independently accepted the complete seven-block section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/c65bc6cc519bb066f52508a1fd1d447de5fbddf1). They checked the elementary ω-graph calculation, exact scalar dimensions, four-row compression retaining z and v, actual passive complement and W-graph adjustment, τ-shear vanishing, the G/P0 and H cohomological normalizations, τ-stability of G0 and the bound 120·2^70. Acceptance retains the pinned component, one-shadow, projectivity and actual Bruck-envelope hypotheses. No new computation, independent reproof of all upstream inputs or fresh primary-source audit was claimed. The original K remains unsplit; these model reviews are not a section classification or formal GitHub approvals.

## Eight layer-trivial, H-fixing automorphisms

**Theorem with the scoped independent reviews below.** Under the actual-group hypotheses and the independently reviewed one-shadow and component reductions above, the automorphisms of G that fix H pointwise and induce the identity on `G/P`, `V=P/Z` and Z form an elementary abelian group of order eight. The identity is included. This does not assert that any candidate inverts an admissible marked section K.

For such an automorphism θ, define its P-shear `δ:V→Z` by `θ(p)=pδ(pZ)`. It is linear, and `δ(B)=0` because θ fixes W and Z. For `g∈S5`, choose a lift `g̃∈G` and put `a(g)=θ(g̃)g̃⁻¹Z`. As in the reviewed relative-cohomology and defect calculation in [the multiple-N source](bruck-multiple-n-frattini.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/39a493024a9ee0839852b60f389fe28d155701b9), a is a well-defined cocycle, zero on F, and has the form `a(g)=(1+g)v0` for `v0∈V^F`. Its proof uses the layer-trivial and H-fixing assumptions, not `θ²=1`. The exact defect identity makes `δ0=δ+β(v0,−)` S5-equivariant. Since `V^F=P6^F=<f,1>` and 1 is S5-fixed, choose `v0=αf`, `α∈F2`.

The reviewed block and Hom calculation in [the module-block source](bruck-s5-module-blocks.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499) says `δ0` kills P6 and is a row of top maps on the U summands. The preceding quadratic reduction gives `β(P6,P6)=0` and `β(f,U(T))=0`. Since `D⊗T≤B`, both δ and `β(f,−)` vanish there, and the top projection maps D isomorphically to N. Thus the top rows of δ0 vanish on T. Every θ therefore has

    a(g)=α(1+g)f,       δ=αβ(f,−)+ℓ,

where `ℓ∈Hom_S5(V,Z)` is supported on the U1 top and has two binary coefficients. These are necessary identities; no change of θ is made.

They are also realized uniquely for the fixed ordinary pair `(G,H)`. Let w be the unique element of W over f. The injection `W→B` and F-fixedness of f imply `w∈Z(H)`, and W is elementary, so `w²=1`. For each of the four allowed maps ℓ, regard its composite with `P→V` as an invariant homomorphism `P→Z`. Because P centralizes Z, inflation–restriction for `1→P→G→S5→1` and the vanishings `H¹(S5,Z)=H²(S5,Z)=0` proved in [the nonsplit-extension source](bruck-n-nonsplit-extension-lifts.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff) extend it to a derivation `D:G→Z`, uniquely up to a principal derivation. Since ℓ vanishes on B, `D|H` vanishes on W and descends to an F-derivation. The F-module Z is projective, so `H¹(F,Z)=0`; subtracting a principal derivation normalizes D to vanish on H. This normalized D is unique: a principal difference vanishing on H has its defining vector in `Z^F=0`.

Because D kills Z, `ηℓ(g)=D(g)g` is an automorphism of square one. It fixes H and induces the identity on the three layers. The normalized derivations add, so the four maps η form an elementary abelian subgroup. They fix w, hence commute with `Inn(w)`. The latter is an involution fixing H, with quotient cocycle `(1+g)f` and P-shear `β(f,−)`. Consequently the eight automorphisms `Inn(w)^α ηℓ` are distinct and form `C2^3`; the zero choices give the identity.

Conversely, match any θ with the automorphism having its α and ℓ above. Their quotient fixes P pointwise, and equality of their cocycles a makes its displacement modulo Z zero. Its displacement is therefore an S5-derivation into Z, rather than merely into the potentially larger center of P. It vanishes on F because both automorphisms fix H. The vanishing of `H¹(S5,Z)` makes it principal, and `Z^F=0` makes it zero. Thus the eight listed automorphisms exhaust the layer-trivial, H-fixing group, without assuming in advance that θ has square one. Actual extension data and the condition that a candidate invert the original section K remain part of the original folder problem.


### Independent review of the eight-automorphism theorem

contributor 1, contributor 2 and contributor 3 independently accepted the complete eight-automorphism section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/47f3e2296802dc397bb301318a1000eecfe0610b). They checked necessity for arbitrary layer-trivial H-fixing automorphisms without assuming square one, the relative defect formula, existence and unique H-normalization of the four derivations, the H-central lift of f, distinctness and commutation, and completeness after matching both the quotient cocycle and the P-shear. They retained the pinned one-shadow, component and cohomology inputs without claiming a fresh source audit or complete upstream reproof. No computation was used. The theorem concerns a fixed ordinary pair G,H and does not establish inversion of K or a loop classification; these are model reviews, not formal GitHub approvals.

## Finite cover of the quadratic data

**Continuation with the scoped independent reviews below.** Under the independently reviewed one-shadow and seven-block reductions, fix the ordered independent vectors `z,v∈T`, the synchronized coordinates, bases of the two scalar U1–Ui pair-map spaces and a basis of the two central N components. The four binary pair rows form a linear map `F:T→C=F2^4`. Put `W_F=im F`, `a=Fz`, `b=Fv`, `d=dim W_F`, `r=dim<a,b>`, and `n=dim T`.

For the restricted action of `GL(T)` fixing z and v pointwise, two such maps lie in the same orbit exactly when their triples `(W_F,a,b)` agree. A triple occurs exactly when `a,b∈W_F` and

    n≥d+2−r.                                                    (4)

Indeed `ker F` contains the `(2−r)`-dimensional kernel of `F|<z,v>`, so (4) is necessary. Conversely, choose vectors in `<z,v>` mapping to a basis of `<a,b>`, together with a basis of the prescribed kernel inside `<z,v>`. Lift a basis of a complement of `<a,b>` in `W_F`, and extend the prescribed kernel basis to a basis of `ker F`. These choices form a basis of T. Matching such bases for two maps with the same triple gives an isomorphism fixing z and v pointwise and intertwining the maps. The same construction realizes every triple satisfying (4).

The construction has a representative with active T-dimension `d+2−r≤6`; any additional T coordinates lie in `ker F` and are passive. Keeping U1 gives the seven-block cover above. The remaining finite data are the scalar U1-square and P6–U1 cross coefficients for the two central components, subject to the stated nonzero rank-one `β(1,−)` condition. A change of basis in the central multiplicity space normalizes its U1 value to `(1,0)`. This leaves four U1-square bits and two P6–U1 cross bits, hence 64 local choices.

There are `1,15,35,15,1` subspaces of `F2^4` in dimensions `0,1,2,3,4`. Summing `2^(2d)` choices of `(a,b)` for each d gives

    1+15·4+35·16+15·64+256=1837

triples `(W_F,a,b)`. Thus at most `1837·64=117568` active quadratic records form a finite cover, before the Frattini, marked-rank, core, lift and original-section tests. For fixed n retain only records satisfying (4); the excess over the active dimension gives the prescribed passive multiplicity. Repetitions under other coordinate changes are intentional.

This is an exact orbit criterion only for the stated `GL(T)_{z,v}` action on the four-row map. Neither these records nor their remaining coefficient choices are asserted to be full quadratic-data or `G,H,K` isomorphism classes, realizable envelopes, or loop isomorphism classes. The actual involution, original marked section and simplicity conditions remain necessary.

## Proposed ordinary extension and stabilizer cover

**Continuation with the scoped independent reviews below.** Under the group and module hypotheses of [the nonsplit extension source](bruck-n-nonsplit-extension-lifts.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff), fix the identifications of `Q=S5`, `V=P/Z`, and `Z`, their specified Q-actions, the equivariant square map `q:V→Z`, and a class `e∈H²(Q,V)`. The ordinary extensions realizing these data are isomorphic by an isomorphism inducing the identity on Q, V and Z. This does not classify an inversion, a marked section, or loops. In particular, changing these identifications or transporting q may introduce additional equivalences that are not counted here.

Indeed the ordered-basis presentation in the cited source identifies P from the fixed square map. Align the quotient factor sets by a V-valued one-cochain and adjust their lifts to P. The cited realization proof gives a genuine action `α:Q→Aut(P)` inducing the fixed layer actions; each crossed action has the form `d_f(g)α_g`, with `f(g)∈M=Hom(V,Z)`. Once the two systems use the same V-valued cocycle representing e, their difference is an M-valued 1-cocycle. Since `H¹(Q,M)=0`, a shear of P aligns their crossed actions. The remaining difference of their factor sets is a Z-valued 2-cocycle, removed by `H²(Q,Z)=0`. Thus no additional outer-action parameter survives these fixed-layer identifications. Both vanishing statements and the crossed-system conventions are those proved in the cited realization source.

Now fix an F-submodule `B≤V` satisfying the hypotheses of the automatic stabilizer-lift theorem in [the same source](bruck-n-nonsplit-extension-lifts.md#proposed-automatic-stabilizer-lift), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1818e2c44bee176638f1212fd8b36c6a8a92e5ba): `q|B=0` and B contains the full F-fixed plane of P6. Write `F=F20`. The possible subgroups `Hbar≤G/Z` above F with `Hbar∩V=B` are P-conjugate. For their images modulo B are complements to `V/B` in the corresponding extension, and `H¹(F,V/B)=0` because `V/B` is F-projective. Fix one Hbar. Complements to Z in its full preimage, modulo Z-conjugacy, form a torsor for `H¹(Hbar,Z)`. The inflation–restriction sequence for B normal in Hbar, together with `H¹(F,Z)=H²(F,Z)=0` and trivial B-action on Z, identifies this group with `Hom_F(B,Z)`. The automatic-lift theorem supplies existence.

In the normalized rank-two shadow of the one-form theorem above, `V/B` is a sum of copies of the nontrivial F-simple module S, so `(V/B)^F=0`. If an element of P preserves the fixed Hbar, its image in V/B is F-fixed and hence zero. Its image in V lies in B, and multiplication by an element of H representing that image leaves an element of Z. Thus P-conjugacy causes no further identifications in this fixed-Hbar torsor.

Every `δ∈Hom_Q(V,Z)` gives a central derivation automorphism of G. Indeed, inflation–restriction and `H²(Q,Z)=0` extend the composite `P→V→Z` to a derivation `G→Z`; it kills Z and hence defines an automorphism fixing Q, V and Z. Its action on the fixed-shadow torsor is translation by `δ|B`. The cited module-block input at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499) gives `B|F≅1²⊕S^(b+1)`, `Z|F≅S²`, and `End_F(S)=F2`. Hence `dim Hom_F(B,Z)=2(b+1)`. Every Q-map `V→Z` is a pair of rows of U-top maps, and the U-top image of B has dimension `b−1`; the restriction image consequently has dimension `2(b−1)`. Thus the quotient torsor by these central derivation automorphisms has dimension four. After the stated normalizations it supplies **at most 16 representatives** for ordinary stabilizer lifts.

This is a cover, not a count of isomorphism classes. Other layer-trivial automorphisms may have nonzero quotient cocycles in `H¹(Q,V)`, and automorphisms preserving the complete q and e data may fuse representatives further. No assertion is made here that the representatives admit τ, an original marked section, or a simple Bruck loop.

### Independent review of the finite and ordinary covers

contributor 1, contributor 2 and contributor 3 independently accepted the two preceding sections at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/22db023526be99e25f93bd9f5643104c153b29f0), conditional on their pinned inputs. Their mathematical reviews covered the restricted row-map orbit criterion and realization inequality, the 1,837 triples and 64 local choices, ordinary extension uniqueness via the two cohomology vanishings, quotient-stabilizer normalization, the central-lift torsor and its four-dimensional quotient. They retain the distinction between covers and full isomorphism classifications. No new computation or source audit was needed, and no section existence or global classification was accepted. These are model reviews, not formal GitHub approvals.

## Four inner automorphisms and two remaining cosets

**Continuation with scoped independent reviews below.** In the normalized branch of the eight-automorphism theorem, let `w_f,w_1` be the unique W-lifts of the F-fixed vectors f and 1. Then

    C_G(H)=<w_f,w_1>≅C2²,
    η_(A top_U1)=Inn(w_1),

where the central row A is normalized to `(1,0)`. Consequently exactly four of the eight compatible automorphisms are inner, and there are two cosets modulo them. This is a statement about automorphisms of a fixed ordinary pair, not about loop or folder isomorphism classes.

To prove the centralizer statement, its image in S5 centralizes F20. The centralizer of a five-cycle in S5 is its C5, and the order-four complement acts faithfully on that C5, so `C_S5(F20)=1`. Thus `C_G(H)≤P`. The shadow of an element centralizing H lies in `V^F=<f,1>`. Its unique W-lift centralizes H: conjugation preserves W and its shadow, and `W∩Z=1`. Dividing by that lift leaves an element of `Z^F=0`. Hence the displayed centralizer is exact. W is elementary, so its four elements are involutions or identity.

Conjugation by w_1 has quotient displacement `(1+g)1=0` and P-shear `β(1,−)=A top_U1`. The uniqueness part of the reviewed eight-automorphism theorem identifies it with the indicated normalized derivation automorphism. Conjugation by w_f has nonzero quotient displacement `(1+g)f`, while conjugation by w_1 has nonzero P-shear. They are distinct commuting involutions, giving four distinct inner automorphisms. Every inner automorphism fixing H is induced by an element of `C_G(H)`, proving exhaustion. Representatives for the two cosets can therefore be chosen as identity and the second-central top derivation. No existence of an inverted admissible section is inferred.

## A uniform radical-factorization prefilter

**Continuation with scoped independent reviews below.** Retain the one-shadow, seven-block and exact-eight inputs at their reviewed revisions above. Write `R=P6⊕U(T)`, so `V=U1⊕R`, `B≤R`, `q|R=0` and `β(R,R)=0`. Each of the eight compatible automorphisms has P-shear `δ=αβ(f,−)+ℓ`, where ℓ is supported on top U1. Thus `δ|R=0`.

The necessary original radical-factorization condition from [the multiple-N source](bruck-multiple-n-frattini.md#radical-fiber-and-a-relative-cohomology-correction), exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/39a493024a9ee0839852b60f389fe28d155701b9), is `q(v)+δ(v)∈β(v,B)` for every v in V. It is equivalent to the following two tests for every u in the 256-element module U1:

    β(u,R)=β(u,B),     q(u)+δ(u)∈β(u,B).                 (5)

Indeed, for v=u+r, `β(v,B)=β(u,B)` and `q(v)+δ(v)=q(u)+δ(u)+β(u,r)`. Taking r=0 proves the second necessity, and subtracting it for all r proves the first. Conversely the two assertions imply the condition for every r. This equivalence is only for the necessary radical-factorization condition, not for an actual folder.

Both tests are F20-equivariant, so one representative from each orbit on U1 suffices. There are exactly 19 orbits. On `U1|F≅S²`, the identity fixes 256 vectors, the four nonidentity C5 elements fix one each, the five involutions fix 16 each, and the ten order-four elements fix four each. These fixed-space dimensions follow from the cycle types `2²1` and `41` on the even-weight natural five-point module S. Burnside gives `(256+4+5·16+10·4)/20=19`. Passive blocks contribute zero to the quadratic and polar expressions, so (5) depends only on the finite active record, not on passive multiplicity or central H-lift parameters.

The α-term lies in `β(u,B)` since f is in B; the first top-shear bit also lies there since `β(1,u)=A top(u)` and 1 is in B. Thus the tests are independent of these two bits for every quadratic record. Adding the linear second-central top map to q exchanges the remaining two tests without changing the polar. This yields equal counts only on parameter sets closed under that change. It need not preserve the condition `Φ(P)=N²`, because it can send the second scalar component from top to zero.

For b=3, the [standalone certificate](../code/verify_bruck_b3_radical_prefilter.py) reconstructs the seven-dimensional scalar coefficient space from committed component solvers, checks the zero restrictions used above, constructs the 19 actual F20 orbits, and implements (5) using explicit subspace sets. With labels `α+2ℓ0+4ℓ1`, its marked-rank-two population has 12,288 ordered quadratic pairs. Requiring independent scalar quadratic components, hence the full two-copy Frattini image, leaves 12,224 pairs. Of these, 9,720 pass every label, four pass only labels 0–3, 68 pass only labels 4–7, and 2,432 pass none. Thus each label 0–3 has 9,724 survivors and each label 4–7 has 9,788. These are necessary-test survivors in fixed coordinates, not isomorphism classes, admissible sections or proven loops. The project, producer and three independent reviewers ran the Python 3.12.14 certificate successfully; exact-source review is recorded below. The earlier temporary C++ test independently checked all 256 vectors and reproduced the unfiltered counts, but temporary sources are not the canonical evidence.


### Independent review of the inner and radical reductions

contributor 1, contributor 2 and contributor 4 independently accepted both preceding deductions at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/a30da29fcf9655735429b5fb3064302e0c333381), conditional on the pinned one-shadow, component, eight-automorphism and radical-factorization inputs. They checked the exact H-centralizer, identification of the first top derivation as inner, the four/two count, the all-b equivalence (5), the 19-orbit argument, label independence, and the full-Frattini filter caveat. Each extracted the exact committed code directory, read and ran `verify_bruck_b3_radical_prefilter.py` with Python 3.12.14, and reproduced the reported populations and survivor masks. These counts remain necessary filters, not sections or isomorphism classes. Their separate ordinary-lift and inner-twist collision reviews are recorded in the phase manuscript. No reviewer claimed a fresh upstream source audit, a loop construction or formal GitHub approval.
