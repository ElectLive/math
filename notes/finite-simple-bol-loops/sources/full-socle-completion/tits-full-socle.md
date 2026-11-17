# The Tits group as a full multiplication socle

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md), independently reviewed at the exact source revision recorded below.

**Proposed theorem.** No finite simple proper left Bol loop Q has Soc(Mlt(Q))≅²F₄(2)′, under the canonical and finite-classification inputs below. Both actual factor orientations and the outer extension are covered. The nonsimple ²F₄(2) is its automorphism group, not a second simple socle.

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion at `932ead5db5f39045e2085caa6b062f6b981b2813`, the primitive almost-simple full-group result C0008 at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion/component obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. These are scoped dependencies, not aggregate claim promotions. Put S=²F₄(2)′ and A=Aut(S)=²F₄(2), of orders17971200 and35942400 respectively.

The finite inputs are the complete eight S-maximal conjugacy classes, the seven A-maximal classes, the group/table identifications and normal fusion from S to A in ATLAS/CTblLib. The [certificate](../code/verify_tits_full_sieve.g) pins GAP4.15.1/CTblLib1.3.11 and asserts the exact complete stored lists. It checks two statements:

1. For every pair of S-maximal classes B,C, the integer |S| does not divide 2|B||C|.
2. Every involution class of A lies in S.

The first is a necessary-order sieve, not a list of actual factorizations. The second is also explicitly stated in Aschbacher–Seitz1976 §18(18.6), printed p.75. The source authors inspected that primary statement and both online CTblLib maximal-list metadata pages; exact links and dataset-version limits are in [REFERENCES](../foundations/references.md). Correctness/completeness of the finite classifications and the actual normal fusion remain external inputs, not proved by arithmetic.

Let M=Mlt(Q), G=LMlt(Q) and I=M₁. Then S≤M≤A, I is core-free and M=GI. If S≤G, then G is S or A. For G=S, canonical τ is an involutory automorphism of S. Statement2 rules out an outer τ, so τ is inner, contrary to the pinned component obstruction. For G=A, restriction Aut(G)→Aut(S)=G is injective because S is characteristic and C_G(S)=1; inner automorphisms already supply every restriction. Thus every automorphism of G is inner, giving the same contradiction.

Otherwise G₀=G∩S and I₀=I∩S are proper subgroups of S. The second is proper because a nontrivial normal subgroup of M cannot be contained in its core-free point stabilizer. Choose maximal subgroups B,C containing G₀,I₀. With d=[M:S]∈{1,2} and e_G=[G:G₀], e_I=[I:I₀] dividing d, the actual factorization gives

    |S|=e_G e_I |G₀||I₀|/(d |G∩I|).

It follows that |S| divides2|G₀||I₀| and hence2|B||C|, contradicting Statement1. No factorization S=G₀I₀, solvability assumption or equality of actual factors with maximal overgroups is used. This proves the proposed full-socle exclusion.

The source authors read and ran the final certificate successfully under the pinned versions; its raw log remains outside Git. Repository integrity is checked separately with Python3.11+ and does not prove the theorem. Independent mathematical review is recorded below. The other remaining socle families and the classification of loop operations remain open.


## Independent exact-source review

Three independent automated-model agents accepted exact source `c0a78fff876603a8e2c2f4e269dd50ba8f01f693`: reviewer A, reviewer B, and reviewer C. Each read the actual-factor divisibility and inner-inversion arguments, extracted the certificate from that commit, and independently ran it successfully under GAP4.15.1/CTblLib1.3.11 with `--quitonbreak`. The paired-simple and rank-three reviewers freshly inspected Aschbacher–Seitz §18(18.6), p.75, and the online socle maximal-list metadata. The S5 reviewer attempted the publisher PDF but could not access it and did not freshly inspect those metadata pages; those source statements remained explicit inputs in that review. No reviewer claims to reproduce the external classifications, validate every inherited result anew, or give a formal GitHub approval. The reviewed source is available locally. Repository integrity separately passed115 tests under Python3.12.14. C0010 and the complete classification remain open.
