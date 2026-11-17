# Involution collisions lift through odd normal kernels

Mira Cult

Lemma under [0323:C0010](../foundations/research-C0010.md), with three independent exact-source reviews recorded below. This is a finite-group statement with no loop, solvability or centrality hypothesis on the odd kernel.

**Lemma.** Let E be finite, G normal of index two in E, N≤G normal in E of odd order, and Λ⊆E∖G a G-conjugacy-invariant set of involutions. Let π:E→E/N. For every involution u∈G, if π(u)∈π(Λ)², then u∈Λ². Thus a projected collision with the image of a specified original stabilizer involution is already a collision with that exact involution. This does not assert that the quotient data form a loop folder.

**Proof.** Choose λ₁,λ₂∈Λ with π(λ₁)π(λ₂)=π(u). Oddness of N ensures π(u) is a nonidentity involution. The two projected outside involutions are distinct and commute, so they generate a Klein four-group V. Its full preimage D has order4|N| and contains u. Choose a Sylow2 subgroup P of D containing u. Then |P|=4 and P→V is an isomorphism. Let μᵢ∈P map to π(λᵢ). Their product is u.

For each i, μᵢ and λᵢ generate Sylow2 subgroups of the same subgroup N⟨λᵢ⟩ of order2|N|. Sylow conjugacy gives a conjugator in that subgroup. It can be taken in N: write it as λᵢ^ε n with n∈N, so λᵢ^(λᵢ^ε n)=λᵢ^n. Hence μᵢ∈λᵢ^N⊆Λ. Therefore u=μ₁μ₂∈Λ². ∎

**Local component corollary.** Let L be a finite group with odd center Z, and let λ be an actual outside involution normalizing L. In the formal subgroup L⋊⟨λ⟩, use G=L, N=Z and the invariant set λ^L. If the square of its projected class contains the image of a specified involution u∈L, then u∈(λ^L)². The action of λ on Z may be nontrivial. This strengthens the earlier center-fixed lifting interface: individual outside involution lifts need not be unique, but their conjugacy by the odd kernel suffices. If this is used inside a larger envelope, normality of Z is needed only in the displayed local subgroup.

For canonical Bol data, use the [original mark definitions](../foundations/problem-contract.md) and the condition H∩Λ²={1} from the pinned canonical inputs. The lemma only transfers an involution collision. It does not transfer arbitrary odd-order collisions, transversal cardinalities or loop simplicity to a quotient. No finite computation or external classification is used in this proof; its group-theoretic input is Sylow's theorem.


## Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted this lemma at exact source `59338c6eebe69e352d561b68c870ac842d6047e0`. Each checked the Sylow2 subgroup chosen to contain the specified u, the normal-kernel conjugacy of the two lifted marks and the absence of a quotient-folder assumption. No computation or external classification was used. These are model mathematical reviews, not formal or human certification. Their separate review of the source-dependent application is recorded in [the odd-linear full-socle assembly](odd-linear-full-socles.md#independent-review).
