# Supported residual kernels and strict invariant cuts

Mira Cult

**Independently reviewed structural restrictions under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q for a finite odd nilpotent group Q acting faithfully by pure factor permutations. The original H0=H∩N splits into its full twisted A5 strips T and its correlated proper-coordinate residual R. H maps onto Q by the normal-maximal argument. We prove lower bounds on genuinely supported kernels of R, a resulting requirement that characters recur on other orbits, and strict bounds on actual residual projections across invariant cuts. These are necessary conditions, not a classification or construction.

The faithful-folder and strict normal-quotient inputs are C0001; actual marked classes use C0007. Full-strip/Goursat separation is [the orbit-tensor source](radical-free-a5-orbit-tensors.md). The original selected-class-square and support-parity interfaces are [the full-strip matching source](radical-free-a5-full-strip-matching.md). The local double-mark theorem is [the stable-orbit local source](radical-free-a5-stable-orbit-local.md); the projection-saturation theorem is [the residual saturation source](radical-free-a5-residual-saturation.md). The distinctions between actual support and projection, and between original quotients and quotient folders, are retained below.

## An actual supported kernel

Let A consist of all proper coordinates i whose H0 projection L_i is A4. Define the actual joint shadow W to be the image of R in ∏_{i∈A}(A4/V4)≅F3^A. Let χ_i∈W* be the nonzero coordinate character at i. Regard χ_i and −χ_i as one projective character class. Let U=O₂(R′).

For every proper subgroup L≤A5 the derived subgroup L′ is abelian; only L≅A4 has even-order L′, namely V4. Therefore R′, embedded coordinatewise in the product of such L′, is abelian, and U is an elementary abelian normal subgroup of R supported on A. Its projection to every coordinate in A is all V4, because R′ projects onto L_i′ and passage to Sylow-2 subgroups preserves that surjection. Conjugation of R on U factors through W, and on V4 at i is the irreducible two-dimensional F2-representation associated with the projective class {±χ_i}.

For I⊆A let r_I count the distinct projective classes appearing in I and nowhere in A−I. Since |W| is odd, F2[W] is semisimple. Each such private class gives a nonzero isotypic component of U, of dimension at least 2, and that component projects trivially to every coordinate outside I. Consequently

    dim_F2 {u∈U : u_i=1 for all i∉I} ≥ 2r_I.                 (1)

This is an actual supported kernel inside H0, not merely a projected rank. Different classes give nonisomorphic simple modules. A class shared with A−I provides no such guaranteed support.

Choose any actual selected N-class C, and write σ for its involutory permutation of Ω. Assume σ preserves I. Let c_I count σ-pairs inside I, and let z_I count σ-fixed coordinates in I at which C has the inactive identity mark. Then

    r_I ≤ c_I+z_I.                                             (2)

For suppose r_I>c_I+z_I. In the supported kernel (1), count elements with zero at each inactive fixed coordinate and matched zero/nonzero support on each σ-pair. These are precisely the support conditions used in the pinned actual-class square argument; all outside-I coordinates are automatically zero. Expanding the characteristic function mod 2 gives terms that impose at most one two-dimensional zero-coordinate condition per pair plus one per inactive fixed coordinate. The kernel dimension is greater than twice their number, so every expansion term has even cardinality. The matching count is even, yet contains the identity; it therefore contains a nonidentity u. Every nonidentity element of U is an involution, and the actual N-class square C² contains every N-involution with these support conditions, including simultaneous realizations. Thus 1≠u∈H0∩C², contradiction.

Now take I to be a τ-stable Q-orbit of n_I proper coordinates with H0 projection A4. Every σ induced by a selected outside element preserves I, because it differs from τ by Q. The pinned stable-proper local theorem makes every fixed local mark on I a double transposition, hence active. An involution on the odd-size orbit has f_I>0 fixed factors, so c_I=(n_I−f_I)/2 and (2) becomes

    r_I ≤ (n_I−f_I)/2.                                        (3)

If, additionally, the image of R in (A4/V4)^I has rank >n_I/ℓ for ℓ the least prime divisor of n_I, the transitive-character block argument shows the n_I coordinate projective classes are pairwise distinct. The joint W-classes are then distinct too, because the joint shadow maps onto its I-shadow and the coordinate forms on W are pullbacks of those on the I-shadow. The conclusion strengthens to recurrence of every one of the n_I classes outside I. Indeed, H normalizes R, and H0 acts trivially on W, so the induced action on W and its projective characters factors through Q. It carries the projective character of i to that of qi: the actual local conjugation takes one A4 projection to the other and induces the corresponding quotient isomorphism. Thus the n_I distinct classes on I form one transitive Q-orbit. Since A−I is Q-invariant, its occurring classes form a Q-invariant set; the subset of classes on I that are private is consequently either empty or all n_I. Inequality (3) rules out all n_I because f_I>0. Every class on I therefore also occurs outside I.

Choose one outside A4-coordinate whose character belongs to this Q-orbit, and let J be its Q-orbit. Its character image is exactly the entire n_I-element character orbit. Equivariance gives a Q-map J→I's character orbit, so n_I divides |J|. In particular, if n_I is maximal among A4-coordinate Q-orbit sizes, then |J|=n_I and the coordinate characters on J are also pairwise distinct. Thus any such saturated stable A4 orbit of maximal size has another A4 orbit of the same size with exactly the same projective character image. J need not be τ-stable, and no independence of their actual residual coordinates is asserted. This is an actual cross-orbit coupling requirement; it applies without identifying a four-orbit subconfiguration. For n_I=1 the pairwise-distinct conclusion is automatic.

All projections and kernels here are of the original R. The conclusion does not assert that a projective class shared with another orbit gives independent elements or that a surviving support pattern defines a folder. A next step is to combine (3) with the full-strip incidence graph and the strict normal-quotient cut inequalities to force an impossible supply of repeated classes.

## Strict original-folder cut inequalities

Let V be any nonempty proper subset of Ω that is a union of Q-orbits and is τ-stable. Let N_complement be the product of factors outside V. It is a nontrivial normal subgroup of G preserved by τ.

Let m_V be the number of original full strips meeting V, and R_V the image of R on the proper coordinates in V. Let σ be the factor permutation of a selected outside element above any one selected top label. Let c_V be its number of two-cycles in V and f_V its number of fixed coordinates there. Let D_V be the sum, over DISTINCT restrictions to the fixed coordinates in V of actual selected N-classes above that top label, of the product of the corresponding fixed local class sizes. Thus projected mark patterns are deduplicated; no independence is assumed. All selected top labels are Q-conjugate, and Q preserves V, so their restricted class sizes and D_V agree. There are k=[Q:C_Q(θ)] such labels, where θ is the automorphism induced by τ on Q.

Then

    |R_V| > 60^(c_V+f_V−m_V)/(k D_V).                         (4)

The inequality is strict for every such cut, including when H N_complement=G.

Proof. Project the actual marked set to G/N_complement. Distinct top labels remain distinct, and within each label the projected N_V-class of each restricted mark pattern has size 60^c_V times its fixed local weight. Thus |K N_complement/N_complement|=k·60^c_V D_V. The projected H0 has order 60^m_V |R_V|: even a strip only partly meeting V projects isomorphically to a full A5 strip, while the proper residual projects independently of those full strips. Since H maps onto Q, [G:H N_complement]=60^|V|/(60^m_V |R_V|). The image of the original transversal K meets every projected H-coset, giving the non-strict version of (4). If H N_complement<G, it strictly contains H: otherwise N_complement≤H contradicts corefreeness. Equality of the transversal image with the index would, by the pinned C0001 criterion, give a nontrivial proper normal subloop, contrary to simplicity. A proper coordinate in V guarantees H N_complement<G because its local H0 projection is proper. If H N_complement=G, the index is 1, while the image of K contains the identity and generates the nontrivial group G/N_complement; its size is therefore greater than 1. No folder property is asserted for the quotient image.

If the proper coordinates in V have local projection orders r_i, then |R_V|≤∏r_i, with the actual projected subgroup often substantially smaller. In particular, for every such cut,

    ∏_{proper i in V} r_i > 60^(c_V+f_V−m_V)/(k D_V).         (5)

The same inequalities hold with any sharper bound on the actual R_V; they apply to arbitrary Q- and τ-invariant cuts, including cuts that split full strips. Unlike the paired-envelope forest, fixed-factor weights and the top-label factor k remain, and m_V counts every strip meeting the cut. Therefore (5) alone is not a forest theorem and does not force a four-orbit configuration.

If one selects V as a union of connected components of the graph generated by Q-permutation edges, τ-pair edges, and edges joining all coordinates in each full strip, then no full strip crosses V. This removes strip-crossing ambiguity, but connected components can contain many Q-orbits and the actual R_V and mark restrictions can still be correlated across components. A component need not reproduce the four-regular-orbit hypothesis.

A concrete subgroup-level obstruction to summing saturation budgets is R={(x,x):x∈A4³}≤A4³×A4³, with Q=C3 rotating both rows. Each regular row has full A4 projections, rank-3 C3 shadow and full projected V4³, but v2(|R|)=6, not 12. It is only subgroup data: no folder, class-size or transversality realization is asserted. It shows why separate row-projection saturation does not supply disjoint support or a sum of their 2-ranks.


## Evidence and remaining obligation

These are analytic arguments with no computation. Independent review of this complete exact source is recorded below. The supported-kernel lemma avoids the false inference that separate full projections have disjoint support. The cut formula keeps distinct restricted mark patterns and original crossing strips; it does not assert that their projected data define a Bol folder. The next obligation is to combine character recurrence, supported-kernel bounds and strict cuts to control general stable-full orbit configurations, without assuming that a component has a previously classified four-orbit form. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned folder, strip, actual marked-square, local-mark and residual-saturation inputs. They checked the actual joint shadow and private isotypic components, the supported-kernel parity bound, the transitive all-or-none recurrence argument and outside-orbit divisibility, and the strict cut formula with deduplicated restricted marks and crossing strips. They also checked strictness when the projected stabilizer is the whole quotient using generation by K. No computation or fresh upstream-source audit was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval. The statements remain necessary conditions; they neither assert independent residual factors nor a quotient folder or exhaustive orbit classification.
