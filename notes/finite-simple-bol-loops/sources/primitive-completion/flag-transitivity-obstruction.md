# Transitive flag actions with type permutations

Mira Cult
**Status:** Scoped independent review recorded below. This is a bounded continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Its loop consequence uses C0008 Lemma 2.1. No classification of primitive almost-simple actions or identification of a full action normalizer is assumed or claimed.

## Abstract flag theorem

Let $`\Omega`$ be a finite set of flags, each consisting of one object of each of $`r\ge2`$ disjoint types. Let $`P`$ act on the objects, carrying flags to flags and globally permuting the types, and let $`P_0`$ be the type-preserving kernel. Assume:

1. A subgroup $`T\le P_0`$ is transitive on $`\Omega`$.
2. $`P_0`$ acts faithfully on the set of occurring objects of each type.
3. The graph on $`\Omega`$ whose edges join distinct flags differing in exactly one constituent is connected and has an edge.
4. For each pair of distinct types $`i,j`$, every occurring $`i`$-object is contained in flags with at least three different $`j`$-objects.

Then no element of $`P`$ sends every flag to a distinct adjacent flag. Consequently no loop on $`\Omega`$ has multiplication group contained in $`P`$.

*Proof.* Suppose first that $`g\in P_0`$ sends every flag to a distinct adjacent flag. In every flag exactly one constituent is moved. If two flags are adjacent, their common $`r-1`$ constituents have the same fixed statuses under $`g`$. Therefore their unique moved constituents have the same type: if a common constituent is moved it supplies that type for both; otherwise both moved constituents occupy the one differing type. Connectedness makes the moved type the same for every flag. Thus $`g`$ fixes every occurring object of another type, and hypothesis 2 gives $`g=1`$, a contradiction.

Now suppose $`g`$ induces a nonidentity permutation $`\pi`$ of the types. Let $`S`$ be its set of moved types and $`s=|S|\ge2`$. If a flag $`F`$ and $`gF`$ are adjacent, they share at least $`s-1`$ objects whose types lie in $`S`$. For each $`i\in S`$, let $`X_i(F)`$ be 1 if $`g`$ sends the type-$`i`$ constituent of $`F`$ to its type-$`\pi(i)`$ constituent, and 0 otherwise. Since a flag has exactly one object of each type, $`\sum_{i\in S}X_i(F)`$ counts precisely the shared objects of moved types. Thus it is at least $`s-1`$ for every flag.

Fix $`i\in S`$ and an occurring type-$`i`$ object $`v`$. Flag transitivity implies $`T_v`$ is transitive on flags containing $`v`$, and therefore on their occurring type-$`\pi(i)`$ constituents; all such constituents have the same number of completing flags. By hypothesis 4 there are at least three, and $`g(v)`$ selects at most one. Thus a uniformly random flag satisfies $`\mathbb E X_i\le1/3`$. Summing,

```math
\mathbb E\!\left[\sum_{i\in S}X_i\right]\le s/3<s-1,
```

contrary to the pointwise lower bound. This eliminates every possible type permutation.

For the loop consequence choose adjacent flags $`e,a`$, with $`e`$ the identity. C0008 Lemma 2.1 gives that the left translation $`L_a`$ sends every flag to a distinct member of the orbital of $`(e,a)`$, hence to an adjacent flag. That contradicts the first assertion. $`\square`$

## Conditional building corollary

Let $`\Delta`$ be a finite thick spherical building with a chamber-transitive type-preserving subgroup $`T`$. Let $`J`$ be a set of at least two types, and let $`\Omega_J`$ be the set of $`J`$-flags, obtained by restricting chambers to their constituents of types in $`J`$. Suppose $`P`$ is a group of building automorphisms containing $`T`$ and preserving $`J`$ setwise, and suppose its kernel $`P_0`$ on $`J`$ acts faithfully on the set of vertices of each type in $`J`$. Then no loop on $`\Omega_J`$ has multiplication group contained in the induced action of $`P`$.

Indeed, $`T`$ is transitive on $`J`$-flags. Any two chambers are joined by a gallery; restricting this gallery to $`J`$ and deleting repeated flags shows that the partial-flag adjacency graph is connected. It has an edge: vary any selected type in a chamber while fixing the other chamber vertices. Finally, for distinct selected types $`i,j`$ and any vertex of type $`i`$, take a chamber containing it and vary the $`j`$-vertex over the chambers containing the opposite $`j`$-panel. Thickness supplies at least three distinct $`j`$-vertices, all incident with the original $`i`$-vertex. Thus the abstract hypotheses hold.

For background on chambers, galleries and thickness, see Brent Everitt, *A (very short) introduction to buildings*, Expositiones Mathematicae **32** (2014), 221–247, [arXiv:1207.2266v3](https://arxiv.org/abs/1207.2266v3), §§3–5. The argument above uses only the displayed incidence and gallery properties; it does not use a classification of buildings.

If $`P_0`$ is almost simple with nonabelian simple socle $`T`$ and $`T`$ acts transitively and nontrivially on each selected vertex type, the required faithfulness follows: the kernel on a type is a normal subgroup of $`P_0`$; a nontrivial one contains $`T`$, which cannot act trivially there. This is a sufficient interface, not an assertion that an arbitrary almost-simple flag action meets it.

In particular, a type permutation acting transitively on $`J`$ is permitted by the abstract theorem; no proper invariant subset of types is required. This includes the **conditional** possibility of $`D_4`$ triality acting on its three outer types when the actual building action, chamber-transitive subgroup, faithfulness and full normalizer have been verified. The present manuscript does not make that case-specific identification or claim that the flag action is primitive.

## Review boundary

Independent review should check the expectation count, faithfulness hypothesis for the entire $`P_0`$ rather than only $`T`$, the partial-flag projection and thickness arguments, and the exact action interface for any named classical group. The rank-two incidence-graph proof in [flag-incidence-obstruction.md](flag-incidence-obstruction.md) has different hypotheses and does not require flag transitivity.

automated reviewers a separate automated checker accepted this manuscript at its recorded source revision under its displayed hypotheses, conditional on C0008 UOD for the loop consequence. The review checked type-preserving propagation, faithfulness of the entire type-preserving kernel, the uniform conditional distribution and expectation inequality, projected galleries and thickness, and the sufficient almost-simple faithfulness interface. Standard building incidence/gallery properties and the previously reviewed UOD are inputs. It does not classify full normalizers or primitive actions or identify the conditional D4 triality case. No computation or formal verification was used.
