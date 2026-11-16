# Exact elementary-layer lifting at arbitrary defect

**Theorem with scoped independent reviews**, continuing 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`]. It extends the exact defect-one theorem at `7171a4e11376839d09b2a76544fed0c941b2507e` in [odd-elementary-layer-obstructions](../../packet/manuscripts/odd-elementary-layer-obstructions.md) [earlier public snapshot]. The finite odd group quotient need not define a loop, and its extension need not split. This is an exact recognition and gluing criterion for a chosen elementary normal layer, not an odd Bol classification.

Let p be odd, V a finite Fp-space, L a finite odd group, θ an involution of L, S²=1 on V, and ρ:L→GL(V) with Sρ(l)=ρ(θl)S. Give normalized c:L²→V and η:L→V satisfying the identities below. They define G=V×_c L and τ(vs(l))=(Sv+η(l))s(θl), and every chosen extension and τ-preserved elementary layer arises this way. Choose J≤L, a J-submodule W≤V, and set δ=dim V_+−dim W≥1, n_−=dim V_−. The full identities, with all maps normalized at 1, are

 c(l,m)+c(lm,n)=ρ(l)c(m,n)+c(l,mn),
 S c(l,m)+η(lm)=η(l)+ρ(θl)η(m)+c(θl,θm),
 Sη(l)+η(θl)=0.

A subgroup H projecting to J with kernel W is specified by one normalized global f:J→V/W satisfying f(jk)=f(j)+ρ(j)f(k)+c(j,k) mod W. Existence is the vanishing of the restricted extension class in H²(J,V/W); its solutions form a Z¹(J,V/W)-torsor.

For Kbar={l∈L:θ(l)=l⁻¹}, solve (1+ρ(l)S)v_l=−ρ(l)η(l)−c(l,θl) for one v_l, and put N_l=ker(1+ρ(l)S). Coprime involution lifting gives a solution for each l and dim N_l=n_−. This is the complete actual inverted fiber v_l+N_l, not a choice of quotient section.

For each left coset T=aJ let B_T=Kbar∩aJ. For l=aj∈B_T set W_a=ρ(a)W and let

 a_T(l)=v_l−c(a,j)−ρ(a)f(j) ∈ V/W_a,
 D_T(l)=(N_l+W_a)/W_a.

Then K={g∈G:τ(g)=g⁻¹} is a transversal to H and every conjugate of H if and only if all of the following hold for each T:

(i) |B_T|=p^δ;
(ii) N_l∩W_a=0 for each l∈B_T;
(iii) for distinct l,m∈B_T, a_T(l)−a_T(m)∉D_T(l)+D_T(m).

The quotient V/W_a has dimension n_−+δ. Under (ii), every affine fiber a_T(l)+D_T(l) has exactly p^n_− elements; (iii) is exactly pairwise disjointness. Thus (i)–(iii) make their union the whole quotient. Conversely, actual transversality supplies injectivity and disjointness of those affine fibers and coverage; the constant fiber dimension then forces exactly p^δ of them. As in the defect-one proof, all outside involutions in the finite odd extension are conjugate, so K⁻¹K is G-conjugacy-invariant and transversality to H implies it for all conjugates. This use of the odd-folder input is essential.

The directions need not be parallel for δ>1. For a fixed pair, write

 A_{T,l,m}=ann(W_a+N_l+N_m) ≤ V*.

The data are impossible if this annihilator is zero. Otherwise the forbidden set of f is the affine solution set of the simultaneous linear equations ν(a_T(l)−a_T(m))=0 for all ν∈A_{T,l,m}. These equations are well-defined for f(j)∈V/W, and their right-hand sides include the actual cocycle and chosen inverted-fiber offsets. The exact set of admissible global stabilizer cochains is the complement of the union of these affine subspaces in the solution space of the displayed stabilizer-cochain equation, simultaneously for all T and pairs. They can have codimension greater than one, can be empty or the entire solution space, and cannot generally be replaced by a hyperplane arrangement. The quotient-fiber feasibility checks (i)–(ii) are independent of f.

Changing the section by s′(l)=b(l)s(l) gives the actual gauge laws

 c′(l,m)=c(l,m)+b(l)+ρ(l)b(m)−b(lm),
 η′(l)=η(l)+Sb(l)−b(θl),
 f′(j)=f(j)−b(j) mod W,    v′_l=v_l−b(l).

Every a_T(l) shifts by the same −b(a), and each N_l remains unchanged, so (iii) and the full criterion are section-independent. Inverted-fiber basepoints can be changed by N_l without changing any affine fiber. Coset representatives a change the same fibers under the canonical identification.

## Exact isomorphism with a marked layer

For two such data sets, an isomorphism of extensions intertwining τ and sending H to H′ and V onto the chosen V′ is equivalent to maps γ:L→L′, α:V→V′ and u:L→V′, where both nonzero layers are over the same odd prime p, γ is a group isomorphism, α is a linear isomorphism, u(1)=0, and

 γθ=θ′γ, αS=S′α, α ρ(l)=ρ′(γl) α,
 α c(l,m)+u(lm)=u(l)+ρ′(γl)u(m)+c′(γl,γm),
 α η(l)+u(θl)=S′u(l)+η′(γl),
 γ(J)=J′, α(W)=W′,
 α f(j)+u(j)=f′(γj) mod W′.

The map is vs(l)↦α(v)+u(l) times s′(γl). These identities are both necessary and sufficient by multiplication and τ compatibility. For faithful generating canonical folders it automatically maps the full inverted set K to K′ and hence yields the corresponding pointed loop isomorphism; conversely every loop isomorphism carrying the selected layer to the selected layer induces such data. If the layer is not characteristic, unmarked loop isomorphism may identify different chosen layers, which this marked criterion deliberately does not quotient out.

## Independent envelope and normal tests

Core_G(H)=1 and ⟨K⟩=G remain independent. Generation has the reviewed finite linear reduction: require Kbar to generate L and take the L-submodule of V generated by all N_l and all relator residues from a presentation on symbols for every l∈Kbar; it must equal V. For a finite faithful generating left Bol folder of odd G satisfying the full-inverted-set and centralizer-ratio inputs, the independently reviewed strict-defect theorem in [odd-folder-radicals](odd-folder-radicals.md#candidate-simplicity-criterion-using-τ-stable-normal-subgroups), at `65a3e58df517df59656ab948ac9d122208f62c4a`, says simplicity is equivalent to |H∩N|<|C_N(τ)| for every nontrivial proper τ-stable normal N◁G; no normal quotient is presumed to be a loop. The all-defect result does not bound L or δ and does not itself enumerate isomorphism types. Even at fixed data, exponentially many pair constraints may occur, but each is explicit linear algebra over Fp; stabilizer cochains are global, so the complexity is not an independent per-coset enumeration.

## Independent review

At exact source `d40369dfce8047eee1454295612b71468f11334b`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the complete arbitrary-positive-defect criterion and marked-layer isomorphism equations, conditional on the cited odd-folder, generation and strict-defect inputs. All checked the nonsplit extension/involution formulas, complete inverted fibers, transported stabilizer and global cochain, both directions of affine partition coverage, all-conjugate propagation, annihilator formulation, gauge and basepoint invariance, and the invertible layer/quotient/cochain isomorphism identities. No computation or fresh primary-source audit was required. Faithfulness, generation and simplicity remain separate tests; the reviews do not bound layers or classify all odd envelopes.
