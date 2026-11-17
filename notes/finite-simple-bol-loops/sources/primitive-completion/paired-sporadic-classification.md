# Paired canonical groups with a sporadic simple factor

**Mira Cult**

**Independently reviewed scoped classification**, continuing [0323:C0010](../../claims/0010.md). Let T be any of the26 sporadic finite simple groups. For finite simple nonassociative left Bol loops with entire faithful canonical left multiplication group T² and canonical inversion swapping its factors, every stabilizer is a product from an exact factorization of T. The numbers of loop-isomorphism classes are

| T | Classes |
|---|---:|
| M11 | 2 |
| M12 | 4 |
| M23 | 3 |
| M24 | 10 |
| Every other sporadic T | 0 |

These loops are proper, and their order is |T|. The conclusion is conditional on the precise factorization and subgroup-class inputs below. No ambivalence assumption, Rota–Baxter classification, or inference about other canonical groups or all loops of these orders is used.

The canonical paired-folder interface and its Goursat/isomorphism theorem are [the paired source](../factor-permutation/radical-free-paired-simple-envelopes.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff), sharpened at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e898d8a00b1fc97431ad8092b4e51b9217650187). They retain C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), the scoped C0007 inversion input at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), and the CFSG/FGS dependency recorded there. The explicit external source is Michael Giudici's 8February2006 preprint *Factorisations of sporadic simple groups*, Theorem1.1/Tables1–3 and Theorem1.3/Table5, with the indicated §3 class analysis. The [source record](../foundations/references.md#paired-sporadic-classification-sources) pins the inspected version and ATLAS class inputs. Those classification proofs and their computational ingredients are cited inputs, not independently reproved here.

## Product stabilizers are forced

Write the actual proper projections of H as A,B<T. The paired theorem gives T=AB, a common quotient C of A and B, and

    |H|=|T|=|A||B|/|C|,       |C|=|A∩B|.                 (1)

If A is simple, a nontrivial quotient C must be A itself. Equation(1) would then give |H|=|B|<|T|, impossible. Thus a simple projection forces C=1. The same holds for B. Exact factorizations also force C=1 directly.

Giudici's Theorem1.1 covers actual factors, including nonmaximal subgroups. Its tables leave only two nonexact rows with neither factor simple. In the M11 row the factors are 11:5 and M10, with intersection order5; M10 has a normal simple A6 of index2, so cannot have a quotient of order5. In the Held row the factors are Sp4(4).2 and 7²:SL2(7), with intersection order8; Sp4(4).2 has normal simple Sp4(4) of index2, so cannot have a quotient of order8. For either quotient obstruction, any map onto the specified group must kill the much larger simple normal subgroup, leaving an image of order at most2. The simple-index-two structures are the named subgroup inputs in the cited tables; Sp4(4) is nonabelian simple and M10 is the standard A6.2 group.

The compact M12 and M24 table rows allow all transitive partners but have a simple M11 or M23 factor, so their compressed presentation leaves no nonproduct case untested. Every other listed row is exact or has a simple factor. This proves C=1 in every possible folder, hence H=A×B and T=AB is exact.

Conversely every listed exact factorization supplies a paired folder. To check the collision condition without ambivalence, the action of A on T/B is regular, so A∩gBg⁻¹=1 for every g∈T. As B is inverse-closed, no nonidentity pair in A×B has conjugate-inverse coordinates. The paired theorem gives the faithful simple proper loop and its canonical group T². No quotient-folder construction is used.

## Embedded factor pairs and isomorphism

The paired theorem identifies isomorphism with simultaneous Aut(T), allowing interchange of the factors. Relative position contributes no extra choice once the two T-conjugacy classes of an exact factor pair are fixed. Indeed, after fixing A, write B′=gBg⁻¹ and g=ab using T=AB. Then B′=aBa⁻¹, and conjugation by a fixes A. Thus inner orbits of embedded factor pairs are determined by their two subgroup classes. Outer automorphisms act on the two classes simultaneously. The factor types in the rows below distinguish the two endpoints, so factor interchange does not identify different rows or multiplicities.

Giudici's exact-factorization list gives the representative types in the following table. Class multiplicities refer to embedded subgroups, not just abstract groups; in the M24 row R runs over the eight regular-subgroup classes in the natural24-point action.

| T | Exact factor pairs, with the identifications explained below |
|---|---|
| M11 | (C11,M10), (11:5,M9.2) |
| M12 | (M11,A4), (M11,D12), (M11,C6×C2), (PSL2(11),M9.2) |
| M23 | (M22,C23), (PΣL3(4),23:11), (2⁴:A7,23:11) |
| M24 | (M23,R): eight classes; (PSL2(23),PΣL3(4)); (PSL2(23),2⁴:A7) |

Here D12 has order12 and the dotted subgroup names follow Giudici's fixed representations. The table supplies embedded factors through that source; it does not identify distinct subgroup classes merely because their abstract types agree.

For M11 and M23, ATLAS gives trivial outer automorphism groups and one maximal subgroup class for each relevant noncyclic factor. Sylow conjugacy gives a single class for C11 or C23, and their normalizers give 11:5 or23:11. The pair-orbit argument therefore gives exactly two and three classes, respectively.

For M12, Giudici §3 gives two M11 classes, and for each M11 exactly three regular partner classes of distinct types A4,D12,C6×C2. In the Aut(M12) discussion, printed p.6, the source states that M11 and M9.2 are self-normalizing in Aut(M12). Since Out(M12) has order2, neither subgroup's M12-conjugacy class can be fixed by the outer automorphism: otherwise composing that automorphism with an inner one would normalize the subgroup. Therefore the two M11 classes are exchanged, leaving three pair-orbits, one for each partner type. The source's Table5 gives two M9.2 classes in the PSL2(11) row, while ATLAS gives one PSL2(11) maximal class. The same self-normalizer argument exchanges the two M9.2 classes, giving one more pair-orbit. This proves the total4. The separate GAP certificate below corroborates this last fusion and is not needed to replace the stated source assertion.

For M24, Out(M24)=1 and ATLAS gives one M23 and one PSL2(23) maximal class. Giudici §3, printed p.7, reports exactly eight regular-subgroup conjugacy classes in the24-point action. Its Table5 distinguishes three S4 classes and two classes of the group named B24 there, in addition to three other types. These give eight different M23 pair-orbits; collapsing repeated abstract types would give a wrong count.

The two additional factor types each have one embedded class. Giudici's M24 analysis, printed p.7, puts every relevant PΣL3(4) factor inside an M23: this includes the alternatives obtained within M22.2 and within PSL3(4).S3. It identifies every relevant 2⁴:A7 factor as an incident octad–point stabilizer, hence inside the point stabilizer M23; the factors obtained initially from an M23 are already so contained. ATLAS gives one M24-class of M23 and one M23-class each of its maximal PΣL3(4) and2⁴:A7 subgroups. Conjugating first the M23 overgroup and then within it proves uniqueness for each partner. Together with the unique PSL2(23) class, the pair-orbit argument gives one class from each row, and hence total10.

Giudici's Theorem1.3/Table5 has no exact factorizations for the other sporadic simple groups. Combined with the product-stabilizer theorem, this completes the displayed zero rows. Almost simple extensions such as Aut(M12) in the source table are outside the present T² scope.

## Reproducible supplementary fusion check

Run `gap -q -b problems/0323-finite-simple-non-moufang-bol-loops/code/verify_m12_outer_fusion.g` with GAP4.15.1. The [certificate](../code/verify_m12_outer_fusion.g) uses the pinned runtime's MathieuGroup(12), subgroup conjugacy and automorphism algorithms. It checks order95040 and simplicity,147 subgroup classes, exactly two classes of order144, automorphism order190080 with inner subgroup order95040, and interchange of the two order144 classes by a non-inner automorphism. Its identification of these classes with the M9.2 rows uses the primary factorization source. It needs no SmallGroups identifiers, external files or network.

The project read and ran this certificate successfully. This finite check corroborates the specific fusion; it does not independently reproduce Giudici's three or eight regular-subgroup class computations, the other factorization classifications or the proof of their completeness. The project and preliminary reviewers inspected the cited primary table and ATLAS statements. The independent exact-source reviews of this assembly and certificate are recorded below. No formal verification or unrestricted Bol classification is claimed.


## Independent exact-source review

reviewers contributor 1, contributor 2, and contributor 3 independently accepted the complete manuscript, relevant source entries and certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/22595b4b84618e067e7dc2ddcffcccbcb162730f), conditional on the pinned paired-folder/FGS and Giudici/ATLAS classification inputs. Each checked the actual-factor exhaustion, both nonexact nonsimple projection obstructions, relative pair-conjugacy argument, all four orbit counts and the zero cases without an ambivalence assumption. Each read and extracted the committed verifier and independently reran it under GAP4.15.1; all assertions passed.

All three inspected Giudici's versioned primary text, including the M12 self-normalizer and M24 containment/class-count statements. The paired-simple and strip-forest reviewers inspected all four cited ATLAS maximal lists and outer automorphism headers; the C9 reviewer inspected the M11/M23/M24 lists and checked the M12 fusion computationally. None independently reproduced Giudici's full factorization classification, its reported three/eight regular-subgroup enumerations, ATLAS class-list completeness or GAP algorithms. These are model mathematical/source/code reviews of the exact canonical T² branch, not human/formal certification or GitHub approval, and not an unrestricted sporadic-envelope classification.
