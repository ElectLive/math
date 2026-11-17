# Weighted forest obstruction to faithful stable-factor action

**Mira Cult**

**Independently reviewed conditional theorem under pinned inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q, where Q is finite odd nilpotent acting faithfully by pure factor permutations. No regularity or common orbit degree is assumed. If there is any τ-stable Q-orbit, let Q0 be the kernel of Q on the union of all such orbits. We prove that its Sylow-5 subgroup has a nontrivial, quantitatively bounded index over its θ-fixed subgroup, where θ is the top automorphism induced by τ. Thus every odd nilpotent top of order coprime to 5 has only paired factor orbits, and a stable orbit or stable union carrying a faithful Q-action is impossible. The remaining nonfaithful 5-kernel branch is not excluded.

The exact inputs are the [original full-strip forest](radical-free-a5-strip-orbit-forest.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b71856a7191fb6cfbb7b00bfc6be3fae6c6f7a3), [positive orbit-tensor theorem](radical-free-a5-orbit-tensors.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/f86624c05f531304f76d6bc69aa0f0b1dc73759e), [actual selected-mark count and active-mark valuation bound](radical-free-a5-full-strip-matching.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/bff74f3fd03346aa30e761e01cb5e9546fb99cba), and [stable-proper local theorem](radical-free-a5-stable-orbit-local.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/bebeba638c0fd6e4a6d553f79e0c7e9fd7631f1d). The [5-free boundaries, marked-weight estimate and nonregular prime budgets](radical-free-a5-forest-prime-budget.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/765f6490a2ce914ee4da950b6a352a05882ec257) provide the preceding interfaces. H surjectivity and canonical inversion retain the C0001/C0007 source pins recorded there. All subgroups, projections and marks are the actual original ones.

## A weighted forest inequality

Let m be the number of original full strips, Np the number of proper coordinates, and e=(number of full coordinates)−2m. Every strip has size at least two, so e≥0. On the original strip-orbit forest, denote by N_J the cardinality of a full-coordinate Q-orbit J. An edge represents a τ-pair of full-coordinate orbits, hence the two degrees are equal; call their common degree N_edge. Marked half-edges carry the degree of their stable full orbit, while boundary half-edges carry the degree of their full orbit, equal to its proper τ-partner's degree.

Each forest component has a boundary half-edge whose proper partner is 5-free. Indeed take U to be all full-coordinate orbits of the component together with all proper partners of its boundary half-edges. It is a nonempty Q- and τ-stable union; every original full strip that meets U lies wholly in U and has size at least two. If every proper projection in U contained a 5-element, the positive tensor theorem would contradict the folder. Likewise, for every τ-pair of proper-coordinate orbits, at least one partner is 5-free: apply the tensor theorem to just that pair, on which no full strip occurs. Stable proper orbits are 5-free by the local theorem.

Root each tree at a vertex incident to one chosen 5-free boundary, of degree b. The number of original strips in the root vertex is at most b: every strip meets that boundary's full-coordinate orbit, and strips have disjoint supports. For every other vertex, its strip count is at most the degree N_edge of its incoming tree edge, by the same disjoint-support argument. Therefore

    m_component≤b+Σ_{edges in component} N_edge.

Its number of full coordinates is 2Σ_edges N_edge+Σ_stable N_i+Σ_boundary N_j, with the two sums over half-edges in that component. Thus

    e_component+2b−Σ_boundary N_j≥Σ_stable-full N_i.       (1)

Sum (1) over the forest. Let Z be the sum of the chosen boundary proper-orbit degrees, plus the degree of one 5-free proper orbit in each proper/proper τ-pair, plus the degrees of all stable proper orbits. These orbit sets are disjoint. The proper count Np is the sum of all boundary proper degrees, both partners of each proper/proper pair, and stable proper degrees. Since paired orbit degrees agree, the proper/proper terms cancel and (1) yields

    e+2Z−Np ≥ Σ_{all τ-stable Q-orbits i} N_i.             (2)

Write f=Σ_i f_i, the number of fixed coordinates for one selected top label, with f_i on each stable orbit. Let s,u,v count its stable-proper, even stable-full and odd stable-full fixed factors respectively. Put D=15^s·10^v·E with E the actual correlated optional fixed-mark weight, and k=[Q:C_Q(θ)]. The pinned exact count gives |R|=60^L/(kD), 2L=Np+e+f. Filtering the actual residual R through coordinate projections gives v5(R)≤Np−Z. Consequently

    e+f+2Z−Np≤2v5(kD).                                    (3)

By (2),

    Σ_i N_i + f ≤ 2v5(k)+2s+2v+2v5(E).                    (4)

Let a be the maximum selected subset size among the u optional even full fixed coordinates. If any τ-stable orbit exists, u≥1: otherwise E=1 and a=0, and the full active-mark bound v2(E)≥2s+v+2a forces s=v=0 as well, leaving no fixed factor on any odd-sized stable orbit. Moreover v2(E)≥2a. The actual family is a set of subsets, so

    E≤Σ_{j≤a} binom(u,j)15^j
      ≤4^a(19/4)^u <4^a 5^u.

Since coprime 4^a and 5^v5(E) both divide E, v5(E)<u. Substituting f=s+u+v into (4) now yields the strict global fixed-deficit inequality

    Σ_i (N_i−f_i)<2v5(k).                                 (5)

This inequality itself requires no faithful stable action. Each N_i−f_i is even, so v5(k)≥1+Σ_i(N_i−f_i)/2. In particular 5 divides k and |Q|: the stable branch is excluded for every odd nilpotent 5-free top, regardless of regularity or faithfulness of the stable union.

## The kernel of the stable-orbit action

Assume for contradiction that Q acts faithfully on the union of the stable orbits. Because each stable Q-orbit has odd size and is preserved by the involution τ, it has a τ-fixed point. Identify it as Q/L with a θ-stable point stabilizer L, where θ is the automorphism induced by τ on Q. The generated folder has θ acting by inversion on Qab. If qL is τ-fixed then q⁻¹θ(q)∈L, and because squaring is invertible in the odd-order abelian group Qab, q∈LQ′. Finite nilpotence gives Q′≤Φ(Q). Thus for every nontrivial orbit, L<Q entails [Q:LQ′]≥3, and

    f_i≤[LQ′:L]=N_i/[Q:LQ′]≤N_i/3.                       (6)

A singleton has N_i=f_i=1. Faithfulness embeds Q in the product ∏_i Sym(N_i), so Legendre's formula gives

    v5(k)≤v5(|Q|)≤Σ_i v5(N_i!)≤Σ_i (N_i−1)/4.             (7)

If a nontrivial stable orbit exists, (6) and (7) imply 2v5(k)≤Σ_i(N_i−1)/2<Σ_i(N_i−f_i), contradicting (5). If all stable orbits are singletons, faithful action forces Q=1, so (5) reads 0<0, also impossible. Hence the stable-orbit union is not faithful. More precisely let Q0 be its action kernel and put δ=Σ_i(N_i−f_i). From (5) and parity, v5(k)≥δ/2+1. Since Q/Q0 embeds in ∏Sym(N_i),

    v5(|Q0|)≥δ/2+1−Σ_i v5(N_i!).

The right side is positive: each nontrivial stable orbit satisfies v5(N_i!)≤(N_i−1)/4<(N_i−f_i)/2, and singleton terms are zero. Therefore Q0 contains a nontrivial 5-subgroup, a stronger conclusion than nonfaithfulness.

## A nontrivial inverted index in the 5-kernel

The same lower bound controls the part of the 5-kernel moved by θ. Let Q5=O5(Q0), and write Qbar=Q/Q0, θbar for the induced involution, and kbar=[Qbar:C_Qbar(θbar)]. The kernel Q0 is θ-stable because the stable-orbit union is τ-invariant. The fixed-point map C_Q(θ)→C_Qbar(θbar) is surjective. To see this, if qQ0 is fixed, the two involutions τ and q⁻¹τq belong to Q0⋊⟨τ⟩. They are Sylow-2 subgroups there and are conjugate by an element of Q0. Consequently the coset qQ0 has a representative centralizing τ. This proof uses the formal semidirect product, including when θ acts trivially. Its fixed-point kernel is C_Q0(θ), so

    k=[Q0:C_Q0(θ)]·kbar.

Nilpotence makes Q0 a direct product of its characteristic Sylow subgroups, all preserved by θ. Hence the 5-part of the first index is exactly [Q5:C_Q5(θ)]. Since the faithful stable-union action of Qbar gives v5(kbar)≤Σ_i v5(N_i!), the bound sharpens to

    log_5 [Q5:C_Q5(θ)]
        ≥ δ/2+1−Σ_i v5(N_i!) > 0.

In particular θ cannot fix the entire required 5-kernel pointwise. This concerns a normal subgroup of the permutation top Q; it does not assert that this top subgroup is normal in G without adding the appropriate socle factors.

## Evidence and remaining obligation

This is an analytic proof with no computation; independent review of the complete exact source is recorded below. The remaining stable-orbit branch requires a nontrivial normal 5-subgroup of Q acting trivially on every stable orbit and faithfully on the union of the paired orbits. The theorem does not show that its action on any one paired orbit is faithful, nor that its original residual lifts independently. The next obligation is to combine actual normal-quotient cuts and non-involution class-square collisions with this kernel restriction. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.

## Independent mathematical review

reviewers contributor 1, contributor 2, contributor 3, and contributor 4 independently accepted the complete source at exact revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/6e991d408de0e914a06c07f8069396ae895749af), conditional on its pinned original-folder, tensor, strip-forest, local-mark and actual selected-weight inputs. They checked rooting weighted trees at chosen 5-free boundaries, disjoint coordinate accounting and the actual residual valuation; the strict fixed-deficit inequality; the fixed-coset containment and nilpotent Frattini bound; factorial estimates including singleton cases; and the centralizer-lifting/index factorization that gives the nontrivial θ-moved 5-kernel. The conclusion concerns a normal subgroup of Q, with no unsupported claim that it alone is normal in G. No computation or fresh independent audit of the pinned inputs was performed. These are model mathematical reviews, not human or formal certification or GitHub approval. The nonfaithful 5-kernel and paired-orbit classifications remain open.
