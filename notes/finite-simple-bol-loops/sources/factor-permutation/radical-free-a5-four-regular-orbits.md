# Exclusion of one four-regular-orbit pattern

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). The faithful-folder and inversion interfaces are C0001 and C0007. The original full-strip splitting and positive tensor interface in [the orbit-tensor source](radical-free-a5-orbit-tensors.md) are pinned; [the actual stable-proper local theorem](radical-free-a5-stable-orbit-local.md) is pinned; and [the actual marked-class count and active fixed-mark valuation restriction](radical-free-a5-full-strip-matching.md) are pinned. The present argument assumes those interfaces and preserves their scope. It asserts no general four-orbit or classification result.

Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=A5^Ω and G=A5^Ω⋊Q for a nontrivial finite odd nilpotent top Q of order n acting faithfully by pure factor permutations. Put H0=H∩A5^Ω. Assume exactly four Q-regular factor orbits: a τ-stable full-projection orbit A, a τ-stable proper-projection orbit B, and τ-exchanged full/proper orbits C,D. Assume the original full strips are exactly n two-coordinate strips, each joining A to C. Then no such folder exists.

The nilpotent normal-maximal argument gives H→Q onto. Let θ be τ's automorphism of Q, t=|C_Q(θ)| and k=n/t. Since K generates G and τ inverts each element of K, θ acts by inversion on Q_ab. A τ-stable regular Q-orbit contains a τ-fixed factor: its size is odd. Choosing such a factor as origin identifies τ's action with θ, so there are exactly t fixed factors in each stable orbit. The exchanged orbits have no fixed factors. All selected outside top involutions are Q-conjugate, so these counts apply to each selected N-class.

The actual stabilizer of each B-coordinate is H0, as the Q-action there is regular. The pinned local theorem thus makes its H0 projection A4, and every selected fixed mark on B is a double. Local parity is constant on A. If it is odd, all t fixed marks on A are transpositions; the marked weight is Δ=15^t 10^t, whereas the fixed-mark restriction requires v2(Δ)≥2(2t), impossible. Hence A has even parity. Its t fixed marks are identities or doubles. Let S be the actual nonempty selected family of subsets, E=Σ_{S}15^|S|, and a=max |S|. Then Δ=15^t E, E≤16^t, and the fixed-mark restriction gives v2(E)≥2t+2a. Since t>0, a=0 would give E=1, a contradiction; hence a≥1.

The n independent full strips contribute 60^n to |H0|. The class-size formula therefore gives the actual proper-coordinate residual R the order

    |R| = 60^n 4^t/(kE).

It follows that v2(|R|)=2n+2t−v2(E)<2n. The desired contradiction will be v2(|R|)≥2n.

We have k≥3: in the nonabelian case k≥9 by the argument below, while in the abelian case θ=inversion gives k=n≥3. Since 5^k>16k for all integers k≥3, 5^n=5^(kt)>(16k)^t≥k16^t≥kE. Consequently v5(kE)<n and 5 divides |R|. The B projections are A4 and contribute no 5. Thus some D-coordinate projection has order divisible by 5; Q-transitivity on D forces all of them to do so. Each proper A5 subgroup containing 5 is C5 or D10. The residual is therefore contained in A4^n×D10^n, allowing C5 as a subgroup of D10 independently at each coordinate.

Let W be the image of R in (A4/V4)^B=C3^n. The kernel of this projection lies in V4^n×D10^n and has order prime to 3, so

    d=dim_F3 W=v3(|R|)=n−v3(k)−v3(E).

The original H normalizes R and acts transitively on B. Apply the companion [actual residual saturation lemma](radical-free-a5-residual-saturation.md) from this source revision to that orbit. If d>n/ℓ, where ℓ is the least prime divisor of n, the image of O₂(R′) on B is V4^n and hence v2(|R|)≥2n. This contradicts the strict 2-part bound above. The saturation conclusion is a full projection and a dimension lower bound; it does not replace R by independent coordinates or assert a coordinate subgroup is contained in R.

It remains to prove d>n/ℓ. If Q is abelian then θ=inversion, t=1 and k=n. Here a≥1 and v2(E)≥4, while E≤16, so E=16. Thus d=n−v3(n)>n/ℓ for every odd n≥3. Indeed v3(n)≤n/3 and n−n/3>n/ℓ.

If Q is nonabelian, finite nilpotence implies Q_ab is noncyclic and has order at least 9. Since θ acts by inversion on the odd group Q_ab, C_Q(θ) maps trivially to Q_ab and is contained in Q′. Hence k≥|Q_ab|≥9. For odd k≥9, 3^(2k/3)>16k; at k=9 the left side is 729>144; as k increases by 2, the left-to-right ratio is multiplied by 3^(4/3)k/(k+2)>1. Thus 3^(2kt/3)>k16^t≥kE, and

    d ≥ n−log_3(kE) > n/3 ≥ n/ℓ.

This establishes the contradiction for every nontrivial odd nilpotent Q in the stated four-orbit model, conditional on the pinned interfaces. It does not assume independence of the proper-coordinate residual and does not address other orbit/strip patterns. No new computation is used. The next obligation is to extend the module bound to nonregular actions and to additional orbit/strip patterns; this theorem does not establish that every stable orbit is impossible. The unrestricted classification remains open.
