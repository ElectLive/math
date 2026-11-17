# Weighted Fourier constraints on odd-layer fibers

**Mira Cult**

**Independently reviewed necessary restrictions and an exact affine-partition test under pinned inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let `(G,H,K,τ)` be the faithful generated canonical folder of a finite simple nonassociative left Bol loop, and let `1<V<G` be a τ-stable elementary abelian normal p-subgroup of G, for an odd prime p. In the even-envelope branch with `O2(G)=1≠Rad(G)`, the reviewed odd-layer source below supplies such a characteristic layer. The quotient `G/V` may have even order, the extension may be nonsplit, and the ranks of the actual selected fibers may vary. No projected section is assumed to be a quotient folder, and no assertion is made that every quotient outside involution is selected.

The original faithful-folder and normal-subloop criterion is [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); the actual marked-set and inversion interface is [C0007](../../claims/0007.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The full actual fibers, their τ transport, and the strict normal-quotient comparison are in [odd elementary layers in even envelopes](odd-layers-in-even-envelopes.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/17e56bdfb16097218249f42f10e91adcb9f5a4b8). The reviewed odd-group affine-fiber and Fourier precedents are [the all-defect source](odd-elementary-layer-all-defects.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/d40369dfce8047eee1454295612b71468f11334b) and [the uniform-multiplicity source](odd-uniform-multiplicity-layers.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/39a493024a9ee0839852b60f389fe28d155701b9). Their full-inverted-set and constant-rank odd-group assumptions are not imported into the general-parity argument below. The prime-power exclusion used for strictness is the scoped [C0011](../../claims/0011.md) input at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813).

## Actual section labels and affine fibers

Put `L=G/V`, `J=HV/V`, `W=H∩V`, `d=dim_Fp V`, `w=dim_Fp W`, and `D=d−w`. Let `E=G⋊<t>` be the formal extension with `t` acting as τ, including the case τ=1. The actual outside marked set is `Λ=tK`. Write `barΛ` for its actual image in `E/V`, and `barK=KV/V=t barΛ` for the corresponding **section labels** in L. The following constructions use `barK` for cosets of J and use `barΛ` only for outside-conjugacy statements.

Fix a left coset `T=aJ⊆L`, choose a lift `s(a)∈G`, and put `W_a=s(a)Ws(a)⁻¹=ρ(a)W` and `X_a=V/W_a`. Its dimension is D. For each `l∈B_T=barK∩aJ`, choose an actual section lift `κ_l∈K` and an element `h_l∈H` with `l=a·π(h_l)`. The vector

    z_l=κ_l h_l⁻¹ s(a)⁻¹ mod W_a                              (1)

is the affine offset of that fiber in `X_a`. Let `barλ=t l∈barΛ`, and let `N_barλ` be the negative eigenspace on V of the action of any actual involutory lift of `barλ`. Its action is independent of the chosen lift because V is abelian. Put

    r_l=dim N_barλ,     D_l=(τ(N_barλ)+W_a)/W_a≤X_a.          (2)

By the pinned actual-fiber theorem, every involutory lift of an actual selected `barλ` is selected, and the corresponding K-fiber is an affine translate of `τ(N_barλ)`. Original transversality gives `τ(N_barλ)∩W_a=0`, so `dim D_l=r_l`; the affine sets `z_l+D_l`, for `l∈B_T`, are pairwise disjoint and cover `X_a`. In particular

    Σ_{l∈B_T} p^{r_l}=p^D.                                   (3)

The offsets depend on the chosen lifts and coset representative only through the affine fibers they specify. Different quotient cosets and different ranks are retained; no independent choice of offsets is assumed.

## Weighted Fourier balance

For `ν∈X_a*` and `z∈Fp`, define the actual weighted residue counts

    M_z(ν)=Σ_{l∈B_T : ν(D_l)=0, ν(z_l)=z} p^{r_l}.             (4)

For every nonzero ν, the p values `M_z(ν)` are equal. Conversely, for any specified family of affine fibers in `X_a` whose individual maps are injective, equality of these p values for every nonzero ν, together with the total-weight equation (3), is necessary and sufficient for those fibers to be pairwise disjoint and exhaustive.

To prove this, let F be the sum of the affine-fiber indicator functions. Its Fourier transform at ν, for a primitive p-th root ζ and either consistent sign convention, is

    Fhat(ν)=Σ_{l : ν(D_l)=0} p^{r_l} ζ^{ν(z_l)}.              (5)

The total-weight equation is the zero-frequency condition. At nonzero ν, (5) vanishes exactly when all coefficients `M_z(ν)` agree: the only rational linear relation among `1,ζ,…,ζ^(p−1)` is their sum. Thus the displayed conditions are equivalent by Fourier inversion to `F=1`. Since F has nonnegative integer values, this is exactly disjoint exhaustive coverage. The test concerns the affine partition over one original quotient coset; it does not supply independent stabilizer cochains or assert that a quotient is a loop.

For every nonzero ν, either no selected direction is annihilated by ν, or at least p selected directions are annihilated, with positive weighted mass at every residue. If exactly p selected directions are annihilated, their ranks are equal and their ν-offsets exhaust Fp. These are actual selected-fiber restrictions, including when the quotient has even order.

## Multiplicity and minimum-rank consequences

Let `m_T=|B_T|`. Reducing (3) modulo `p−1` gives

    m_T ≡ 1 (mod p−1).                                        (6)

Hence `m_T=1` or `m_T≥p`. If `m_T=p`, all p fibers have rank `D−1` and are the p parallel affine hyperplanes of one pencil. Indeed, if there is more than one fiber each is proper and has at most `p^(D−1)` points; equality in (3) makes every one a hyperplane. Distinct affine hyperplanes of different directions intersect, so disjointness makes them parallel.

Corefreeness and `V≠1` imply `V⊄H`. If `HV=G`, then `[G:H]=[V:W]` is a prime power, contrary to C0011. Thus `H<HV<G`, and the original normal-subloop criterion gives `|KV/V|>[L:J]`. Every quotient J-coset contains at least one section label, so (6) yields

    |KV/V|−[L:J] is a positive multiple of p−1.               (7)

In particular the excess is at least `p−1`. If it is exactly `p−1`, exactly one quotient coset has p selected section labels; its fibers form the hyperplane pencil above, and every other coset has one selected label.

Let `r_min` be the minimum of `r_l` over the actual selected quotient labels. It satisfies `r_min<D`: otherwise all selected fibers would fill their coset fibers, giving exactly one label per quotient coset and contradicting strictness. In every quotient coset, the number of labels of rank `r_min` is divisible by p. Divide (3) by `p^r_min` and reduce modulo p; higher-rank terms vanish. Summing over cosets shows that the total number of actual projected selected marks of minimum rank is divisible by p.

Rank is invariant under L-conjugacy on `barΛ`, because V is normal. Therefore, if the actual projected selected marks of minimum rank form one L-conjugacy class, its class size is divisible by p. This does not assert that every outside involution of `E/V` is selected.

If the **entire actual** `barΛ` is one L-conjugacy class, it is the class of `bar t`, and all selected ranks equal `r0=dim V_−(τ)`. Put `δ=D−r0`. The strict comparison gives `δ≥1`, and (3) gives exactly `p^δ` selected labels in every J-coset. Counting the class in two ways gives

    |barΛ|=[L:J]p^δ=[L:C_L(bar t)],
    |J|=p^δ·|C_L(bar t)|.                                    (8)

In particular p divides `|J|`. Thus a p-free projected stabilizer is impossible under this single-actual-class hypothesis, even with an even quotient or nonsplit extension.

## Scope and control

Variable ranks cannot be discarded on affine-partition grounds alone. In `F3²`, two parallel affine lines and the three points on the remaining parallel line partition the plane with fiber ranks `(1,1,0,0,0)`. This is an affine-partition control, not a constructed Bol folder.

The weighted balance compresses the actual affine-fiber condition but does not classify the selected quotient marks, establish a quotient folder, or prove generation, simplicity or isomorphism of prospective lifts. Those global cochain and original normal-subgroup obligations remain separate. No computation is claimed; C0010 and the unrestricted classification remain partial.

## Independent mathematical review

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete source at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c9b83d37421da818e57ef69227bd04293862540d), conditional on its pinned original-folder, actual-fiber and prime-power-exclusion inputs. They checked the actual τ-transport and offsets, variable-rank Fourier inversion, strict quotient comparison, multiplicity congruence and hyperplane pencil, minimum-rank divisibility and single-actual-class centralizer formula. No new computation, fresh primary-source audit or independent reproof of all upstream results was performed. These are model mathematical reviews, not human/formal certification or GitHub approval.
