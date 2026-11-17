# Paired-orbit support without top surjectivity

**Mira Cult**

**Independently reviewed necessary restrictions under pinned inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let `(G,H,K,τ)` be the faithful generated canonical folder of a finite simple nonassociative left Bol loop, with `G=N⋊Q`, `N=A5^Ω`, and `Q` a finite odd group acting faithfully by pure factor permutations. Assume τ exchanges every Q-orbit on Ω with a distinct Q-orbit. Put `H0=H∩N` and `H_Q=HN/N≤Q`. We do **not** assume `H_Q=Q`, that Q normalizes H0, or independence of proper-coordinate projections.

The faithful-folder, original transversal and normal-subloop interfaces are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); canonical inversion and invariance of the actual outside marked set `Λ=τK` are [C0007](../../claims/0007.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The A5 subgroup and character calculations used below are in [the stable-orbit local source](radical-free-a5-stable-orbit-local.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/bebeba638c0fd6e4a6d553f79e0c7e9fd7631f1d); the actual selected-class square and zero-indicator parity interface are in [the full-strip matching source](radical-free-a5-full-strip-matching.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/bff74f3fd03346aa30e761e01cb5e9546fb99cba). These inputs retain their own hypotheses and review scopes. The arguments below use actual stabilizers and selected classes in the original folder; no quotient folder is asserted.

## A pure proper orbit pair has both local types

Let `O,O'` be τ-exchanged Q-orbits and suppose the H0 projection `L_i=pr_i(H0)` is proper for every `i∈O∪O'`. Let `H_i` be the actual H-stabilizer of factor i, and let `J_i≤A5` be its local image. Then `O∪O'` contains at least one coordinate with `J_i=A4` and at least one coordinate with `J_i=C5` or `D10`. The two coordinates need not lie in different Q-orbits.

Every `J_i` is proper. Indeed `L_i` is normal in `J_i`; if `L_i` is nontrivial, simplicity of A5 rules out `J_i=A5`. If `L_i=1`, the local image is a quotient of `H_i/H0`, hence has odd order, and is again proper.

Let ψ be the degree-five S5 extension in the pinned local source. Among proper A5 subgroups, ψ has no fixed vector exactly on A4. Suppose no `J_i` on `U=O∪O'` is A4. Put ψ on every factor in U and the trivial representation elsewhere. This is an irreducible N-module, and U is Q- and τ-stable, so it has the natural action of `G⋊<τ>`. The action of H on U may have several orbits. On each actual H-orbit choose a representative i and a nonzero `J_i`-fixed vector; transport it to the other factors in that H-orbit. The actual point stabilizer fixes the initial vector, so the transport is well defined. Their tensor product is a nonzero H-fixed vector. This construction does not require the proper-coordinate residual to split.

Every `λ∈Λ` induces on factors a permutation in `Qτ`, and therefore exchanges O and O'. Its restriction to U has only transpositions. Each transposed pair contributes trace 5 in the tensor representation, so `Tr(λ)>0`. The actual marked set is N-conjugacy invariant; its sum acts as a scalar on the irreducible N-module. The positive trace makes that scalar nonzero. The original transversal identity `(Σ_K k)(Σ_H h)=Σ_G g` then says this scalar annihilates the nonzero H-fixed vector, a contradiction. Thus some `J_i=A4`.

If no `J_i` contains an element of order five, its natural action on five points is intransitive. Hence it fixes a nonzero vector in the deleted four-dimensional S5 module χ. Repeat the same transport independently on each actual H-orbit, now with χ on U. Every selected outside involution again has only transposed factor pairs on U, each contributing trace 4, and the same marked-class-sum contradiction follows. Thus some `J_i` contains 5. The proper A5 subgroups containing 5 are C5 and D10, proving the assertion. In particular, this argument does not identify which ambient Q-orbit contains either local type.

## A Sylow-2 information set for every selected class

Write `|Ω|=2n`, let θ be the automorphism induced by τ on Q, and put `k=[Q:C_Q(θ)]` and `t=[Q:H_Q]`. Since Q is odd, its outside involutions form one Q-conjugacy class. Every selected outside top label has one N-conjugacy class of lifts: its factor permutation has no fixed coordinate and hence consists of n transposed pairs. As `Λ` is G-conjugacy invariant and contains τ,

    |K|=|Λ|=k·60^n,       |H0|=60^n t/k.                        (1)

Both k and t are odd. Let P be a Sylow-2 subgroup of the actual H0. Its order is `2^(2n)`. Each coordinate projection of P is contained in a Sylow-2 subgroup V4 of A5, so P itself is an elementary abelian group of dimension `2n` over F2.

Fix **any actual selected N-class** `C⊆Λ`, and let `(i,j)` range over its n transposed factor pairs. The square C² contains every N-involution with matching zero/nonzero support on each pair; the realizations on different pairs occur simultaneously by independent N-conjugation. Since `H∩Λ²=1`, the identity is the only element of P with that support pattern. For p∈P let `e_i(p)` be 1 when its i-th coordinate is identity and 0 otherwise. The pair-matching indicator over F2 is `1+e_i+e_j`. Thus, modulo two, the matching count is

    Σ_{p∈P} ∏_{(i,j)}(1+e_i(p)+e_j(p)) = 1.                  (2)

An expansion term selects at most one coordinate from each pair. Its contribution is the size of the kernel of the projection of P to the selected coordinates. This size is odd exactly when the projection is injective. Equation (2) therefore gives at least one injective selection.

Each selected coordinate has image dimension at most two. Since `dim P=2n`, an injective selection must contain exactly one coordinate from every pair and every selected coordinate image must have dimension two. Its joint projection is consequently an isomorphism

    P ≅ ∏_{selected i} pr_i(P) ≅ V4^n.                          (3)

In particular, every pair of this actual selected class has at least one coordinate whose H0 projection contains V4. The only possibilities for that H0 projection are V4, A4 or A5. The argument applies to every selected class separately; it does not assert that their information sets coincide or that P's proper-coordinate images are independent.

Suppose an original full A5 strip of H0 is a singleton at coordinate i. Its independent V4 Sylow factor in P lies in the kernel of any selected-coordinate projection that omits i. Hence i belongs to every injective selection in (3). In particular, no selected factor pair can contain two singleton full strips.

A singleton strip can occur only in a Q-orbit on which H_Q is intransitive. Indeed H normalizes H0 and transports the singleton through its H_Q-orbit. If that were the entire Q-orbit, the product of the corresponding individual A5 factors would be a nontrivial G-normal subgroup contained in H, contrary to corefreeness. The transport here is by H_Q, not by an assumed Q-action on H0.

## Scope and next obligation

The proper-pair argument does not classify mixed full/proper Q-orbit pairs, and the Sylow-2 information set does not prove `H_Q=Q` or supply a compatible global choice for all selected classes. These are analytic necessary conditions under the pinned inputs; no computation is used; independent exact-source review is recorded below. The next obligation is to combine the actual H_Q-orbits and their singleton/full-strip incidence with the original normal-subloop criterion, without assuming ambient Q preserves H0. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete nonsurjective paired-support manuscript at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/82c3b17fc6f25e1a0dc6b0096219ad0efad5a41d), conditional on its pinned inputs. They checked proper actual local subgroups and fixed-vector transport on H-orbits, selected-mark traces and full top/marked cardinalities, the mod-2 expansion and per-class Sylow-2 information set, and singleton/core-freeness consequences. They did not independently reprove every upstream input, run computations or conduct a fresh primary-source audit. These are model mathematical reviews, not human/formal certification or GitHub approval. These are scoped restrictions; they do not classify the general nonsurjective model.
