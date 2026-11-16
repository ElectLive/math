# Five linear/unitary raw-F3 residuals

Mira Cult
This provisional work on [C0010](../../claims/0010.md) introduces no claim ID. For the reviewed [raw-F3 criterion](sd-raw-involution-count.md) at its recorded source revision, set n=|T|, a=|Aut(T)|, b=#{α∈Aut(T):α²=1}. It suffices to provide B≥b with B³+3aB<n² and n≥2²⁰. All five cases below pass; the new source deductions and application are not independently reviewed. The criterion remains conditional on its upstream folder, factor-action, cyclic semiregularity and CFSG-dependent inputs.

## Full-automorphism upper bound for four cases

Burness, *Fixed point ratios in actions of finite classical groups II*, Proposition 3.14, printed p. 8, https://seis.bristol.ac.uk/~tb13602/docs/fpr2.pdf, gives i₂(Aut(T))<2(1+q⁻¹)q^{N₂}, with N₂=dim(Gbar)−|Φ⁺|. For either PSL_d(q) or PSU_d(q), adjoint type A_{d−1} has dimension d²−1 and d(d−1)/2 positive roots, so N₂=(d²+d−2)/2. This is a bound on the **full** automorphism group, not merely the inner-diagonal subgroup. All four applications have d≥4 and q≥4 and are nonabelian simple; they avoid the small nonsimple unitary exception U₃(2). The earlier PSL₄(2) and PSU₄(2) exceptional identifications are not used in these four applications. Taking

    B=1+2(q+1)q^{(d²+d−2)/2−1}

therefore bounds b from above. It applies to PSL4(9), PSU4(7), PSU4(8) and PSU5(4). For unitary groups use n=q^{d(d−1)/2}∏_{i=2}^d(q^i−(−1)^i)/gcd(d,q+1) and a=2 f gcd(d,q+1)n, q=p^f; for PSL4(9), n=50759843097600 and a=16n. These group-order and outer-order formulas are in Kleidman–Liebeck, *The Subgroup Structure of the Finite Classical Groups* (1990), Tables 2.1.C–D and Theorems 2.1.3–2.1.4, pp. 16, 19, https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf. For PSL4(9), the bound B=860934421 suffices, so no detailed graph-field coset count is needed.

## PSL4(5)

The bound above fails here, so count all automorphism involutions. Put q=5, d=|GL4(q)|, P=d/(q−1), n=P/4 and a=2P. By the cited Kleidman–Liebeck theorem, Aut(T) is the union of PGL4(q) and its inverse-transpose graph coset. A nonidentity PGL involution is represented by A with A² scalar. The split ± eigenspace cases have counts d/(|GL1||GL3|) and d/(2|GL2|²), for dimensions 1+3 and 2+2. For nonsquare scalar, A may be rescaled to A²=νI with ν a fixed nonsquare; its projective centralizer is twice GL2(q²)/(q−1), since a conjugator may send A to −A. The third class has size d/(2|GL2(q²)|).

An element Aγ of the graph coset squares to 1 iff Aᵀ=±A. Invertible symmetric matrices form the two GL4-congruence orbits GL4/O4⁺ and GL4/O4⁻, while invertible alternating matrices form GL4/Sp4. Dividing by q−1 scalar representatives gives the graph-coset count

    d/(q−1)·(1/|O4⁺(q)|+1/|O4⁻(q)|+1/|Sp4(q)|).

The integer certificate below implements standard group-order formulas with divisibility checks, giving n=7254000000, a=58032000000, b=2366976. The exact integer inequality passes. This class calculation has not been independently reviewed.

The [integer certificate](../code/verify_sd_linear_unitary_final_five.py) checks the group-order divisions and all five strict inequalities. Run from the repository root:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_linear_unitary_final_five.py
```

The bundled Python 3.12.14 run passed all assertions.

The code checks only arithmetic; its inputs and the group theory need independent review. Together with the [refined linear/unitary bounds](sd-linear-unitary-refined-bounds.md) and [finite classical automorphism counts](sd-finite-classical-aut-counts.md), these cases leave PSU₄(3), treated by the appended common-class argument in the finite-count manuscript, among PSL_d(q) and PSU_d(q) with d≥4. The small PSL₄(2)≅A₈ and PSU₄(2)≅PSp₄(3) cases are handled separately by the [alternating-socle argument](sd-alternating-all-factors.md) and [finite common-class certificate](sd-finite-common-classes.md), respectively. This conclusion is conditional on the cited screening and finite-count inputs, and uses that separate common-class argument for PSU₄(3). Failure of a sufficient screen is not a possible-loop assertion.

## Source verification and limitations

automated reviewers a separate automated checker accepted this argument at its recorded source revision, conditional on Burness Proposition 3.14, Kleidman–Liebeck group data and the previously reviewed scalar/folder screens. The review confirmed that Burness bounds the full automorphism group, checked the split/nonsplit PGL and symmetric/alternating graph-coset counts for PSL4(5), and ran the pinned Python certificate. Together with the simultaneously reviewed finite classical counts/PSU4(3) argument and the earlier small A8/PSp4(3) cases, the cited routes cover every simple linear and unitary socle in the SD_k setting, k≥3. This is not a classification of arbitrary primitive Bol multiplication groups.
