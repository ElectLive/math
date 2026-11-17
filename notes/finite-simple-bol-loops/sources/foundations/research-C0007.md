+++
id = "0323-finite-simple-non-moufang-bol-loops:C0007"
title = "Twisted Involution Obstruction Theory and Infinite Non-Abelian Simple and Almost-Simple LMlt(Q) Exclusions"
status = "proved"
allocation_owner = "swarm-0323"
depends_on = ["0323-finite-simple-non-moufang-bol-loops:C0001"]
assumptions = []
proof = "problems/0323-finite-simple-non-moufang-bol-loops/proofs/C0007.md"
evidence = [
  { kind = "computation", path = "problems/0323-finite-simple-non-moufang-bol-loops/code/test_lmlt_exclusions.py" },
  { kind = "computation", path = "problems/0323-finite-simple-non-moufang-bol-loops/evidence/computational_census.md" },
]
refuted_by = []
references = [
  "https://dml.cz/handle/10338.dmlcz/119721 | G. P. Nagy, CMUC 49(2) (2008), Problem 2",
  "https://doi.org/10.4153/CMB-1967-048-9 | J. D. Dixon, The maximum order of the group of a tournament, Canad. Math. Bull. 10(4) (1967), 503–505, Theorems 1 and 1′",
  "https://doi.org/10.1112/blms/12.4.303 | C. E. Praeger and J. Saxl, Bull. London Math. Soc. 12(4) (1980), Theorem 1",
  "https://doi.org/10.1007/BF01443417 | A. Bochert, Math. Ann. 33(4) (1889), 584-590",
]
review = { status = "unreviewed" }
+++

Mira Cult

## Statement

1. **Twisted involution obstruction theory**: For any left Bol loop $`Q`$ with $`N_\lambda(Q) = \{1\}`$ (in particular every simple proper left Bol loop) and faithful folder $`(G, H, K)`$, there is a unique involutory $`\tau \in \mathop{\mathrm{Aut}}\nolimits(G)`$ inverting $`K`$ ($`\tau(k) = k^{-1}`$ for all $`k \in K`$). In $`\widetilde{G} = G \rtimes \langle \tau \rangle`$, $`\Lambda = \tau K`$ is a union of $`\widetilde{G}`$-conjugacy classes of involutions in $`\tau G`$ containing $`\tau^{\widetilde{G}}`$ with $`H \cap \Lambda^2 = \{1\}`$, cannot lie in a single coset of any index-$`2`$ subgroup $`G_+ \trianglelefteq G`$, and cannot be a single class $`\tau^{\widetilde{G}}`$ whenever $`G`$ has a unique involution class and $`|C_G(\tau)|`$ is even ($`|H| \ge 2`$).
2. **Infinite Lie-type `LMlt` exclusions**: No finite simple proper left Bol loop $`Q`$ satisfies $`\mathop{\mathrm{LMlt}}\nolimits(Q) \cong G`$ for:
   - $`G = \mathop{\mathrm{PSL}}\nolimits_2(q)`$ or $`G = \mathop{\mathrm{PGL}}\nolimits_2(q)`$ for **all** prime powers $`q \ge 4`$;
   - $`G = \mathop{\mathrm{PSL}}\nolimits_3(p)`$ for **all** primes $`p \ge 2`$;
   - $`G = \mathop{\mathrm{PSU}}\nolimits_3(p)`$ for **all** odd primes $`p \ge 3`$, and $`G = \mathop{\mathrm{PSU}}\nolimits_3(2^{2^s})`$ for **all** $`s \ge 1`$.
3. **Universal alternating and symmetric `LMlt` exclusion**: No finite simple proper left Bol loop $`Q`$ satisfies $`\mathop{\mathrm{LMlt}}\nolimits(Q) \cong A_m`$ or $`\mathop{\mathrm{LMlt}}\nolimits(Q) \cong S_m`$ for **any** integer $`m \ge 5`$.

## Hypotheses

Left Bol loops with $`N_\lambda(Q) = \{1\}`$ in (1); finite simple proper left Bol loops in (2)–(3). All three parts are completely CFSG-free (and do not rely on Loginov's flawed 2007 algebraic-group argument).

## Proof

Complete proofs of Theorems 1.1, 2.1, and 3.1 are given in [C0007.md](C0007.md): $`\Xi_K(G) \subseteq \{L_a : a \in N_\lambda(Q)\} = \{1\}`$ yields $`\tau \in \mathop{\mathrm{Aut}}\nolimits(G)`$; Lang–Steinberg on connected $`\mathbf{SL}_2`$ and $`\mathbf{K} = \{X \in \mathbf{SL}_3 : X^T X = I_3\}`$ ($`\mathbf{SO}_3`$ for odd $`p`$, $`\mathbf{SL}_2`$ for $`q = 2^{2^s}`$) plus the Master Single-Class Lemma exclude the Lie-type families; and for $`A_m, S_m`$, cycle-product lemmas $`C_{2r}, C_{(3)} \subseteq C_k^2`$ combine with Dixon's odd-order bound ($`k_{\max} \ge \lfloor m/4 \rfloor`$), Praeger–Saxl + Bohr–Mollerup simplex convexity ($`1 \le k_{\max} < \lfloor m/4 \rfloor`$, $`m \ge 42`$), and Sylow-$`2`$ / Jordan–Bochert caps ($`5 \le m \le 41`$).

## Evidence

Deterministic `< 0.1s` finite-range and small-group verification is implemented in [test_lmlt_exclusions.py](../code/test_lmlt_exclusions.py) (`TestLMltExclusions`, also wired into `test_bol_engine.py`), checking $`m \in \{5, 6, 7, 8\}`$, the full $`\mathop{\mathrm{Aut}}\nolimits(A_6) = \mathop{\mathrm{P\Gamma L}}\nolimits_2(9)`$ lattice, $`m = 9`$ Regime I, $`R(10), R(11) < 1`$, simplex base cases $`42 \le m \le 45`$, all $`208`$ Regime II hits across $`9 \le m \le 41`$, $`\mathop{\mathrm{PSL}}\nolimits_2(7), \mathop{\mathrm{PGL}}\nolimits_2(7), \mathop{\mathrm{PSL}}\nolimits_2(8)`$, and $`|C_{\mathop{\mathrm{SU}}\nolimits_3(4)}(\phi_0)| = 60`$; extended exclusions up to $`|G| = 190{,}080`$ are documented in [computational_census.md](computational-census.md).

## References

- [REFERENCES.md](references.md): Nagy `CMUC 2008` Problem 2, Dixon (1967), Praeger–Saxl (1980), Jordan (1873) / Wielandt (1964), Bochert (1889) / Dixon–Mortimer (1996), and source-limit note on Loginov (2007).


## Scoped alternating review

The m≥7 arbitrary-stabilizer argument of Theorem3.1 has three independent mathematical/code acceptances at exact source `b03fdd414954bf1fc12186e13c8e3da404e87f95`; the separately reviewed all-PSL2 theorem supplies m=5,6 including every A6 overgroup. The [C0010 assembly and exact review record](../odd-completion/nonbruck-almost-simple-radical-bridge.md#independent-review-of-the-alternating-canonical-assembly) owns the inspected source versions, arithmetic commands and limitations. This scoped acceptance does not certify Theorem2.1 or change C0007's aggregate review status.
