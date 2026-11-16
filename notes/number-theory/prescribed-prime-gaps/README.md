# Prescribed endpoints in prime-gap coverings

**Mira Cult · 16 November 2026**

For every sufficiently large even integer $g$, there is a congruence class
whose two endpoints differ by exactly $g$, remain coprime to the covering
modulus, and have every intermediate integer forced composite. The modulus is
subexponential in $g$:

```math
\log M=(8+o(1))g\frac{\log\log\log g}{\log\log g}=o(g).
```

The proof preserves an arbitrary even difference, including differences with
large prime factors. It uses only the prime number theorem, Mertens' product
theorem, Brun–Titchmarsh and elementary congruence arguments.

**The endpoint-primality step remains open.** This note does not prove that
every even integer occurs as a consecutive-prime gap, or a new infinite family
of specified prime gaps. Its uniform theorem concerns complete coverings and
consecutive reduced residues. No historical priority is claimed.

## Results and proofs

| Result | Exact scope | Canonical proof |
|---|---|---|
| Prescribed endpoint cover | For all sufficiently large even $g$, a complete interior cover modulo $M=\prod_{p\le y}p$, with $y=8(g+1)\log_3(g+1)/\log_2(g+1)$, preserving both endpoints | [Theorem C-SUB](cover.md#the-covering-theorem) |
| Uniform primorial gap prefix | For every fixed $c<1/8$, all even $g\le c p\log_2p/\log_3p$ occur between consecutive integers coprime to $p\#$, for every sufficiently large prime $p$ | [Corollary C-RESIDUES](cover.md#a-uniform-interval-of-gaps-between-reduced-residues) |
| Erdős's existence question | The smallest missing even gap tends to infinity exactly when every even prime gap occurs at least once | [Proposition R1](first-occurrence.md) |
| Erdős's stronger rate | Assuming every gap occurs, $r(x)/\log x\to\infty$ is equivalent to a subexponential first-occurrence bound, in prime index or prime location | [Proposition R2](first-occurrence.md) |
| Finite prime-gap bridge | Exact occurrences of every even gap through 180, with prime endpoints and proper divisors for every interior number | [Certificates](evidence/gaps-through-180.json) and [verifier](code/gap_certificates.py) |

The complete proofs are self-contained apart from their explicitly cited
classical analytic inputs. The asymptotic covering threshold is not numerical.
The first-occurrence note separates a location bound from an index bound and
states the unproved two-form input that would connect the cover to either
Erdős question.

## Why the cover is smaller

Translate the protected offsets to $1,g+1$. Most medium-prime residue classes
can then be set to zero. Omit medium primes dividing the right endpoint, and
bound the survivors arising from these exceptional factors uniformly by a
Rankin sum. Choose nonzero classes at the small primes; surviving large prime
cofactors can then be counted by Brun–Titchmarsh in reduced residue classes.
The remaining reserve primes remove every interior survivor while avoiding
both endpoints. The cleanup budget gives the displayed modulus.

This is a quantitative variant of established Erdős–Rankin and protected-tuple
constructions. [The comparison](cover.md#comparison-for-this-corollary)
distinguishes it from Holt–Rudd's fixed-gap primorial theorem and Ziller's
explicit $N_{\min}(k)\ge2k$ bound. The new growing-range bound exceeds that
identified baseline; a complete external priority assessment is still open.

## Reproduce the finite certificates

From this directory, with Python 3.12 and no third-party packages:

```sh
python code/gap_certificates.py verify evidence/gaps-through-180.json
python -O code/gap_certificates.py verify evidence/gaps-through-180.json
```

Both modes verify 90 gaps, 180 prime endpoints by exact trial division, and
8,100 proper interior divisors. The largest endpoint is 83,751,287. Recorded
generator indices are metadata, not certified minimal first-occurrence indices.
The finite certificate does not establish any infinite family.

## What remains to prove

For a cover $a\pmod M$, prove that the two particular forms $Mt+a$ and
$Mt+a+g$ are simultaneously prime. Admissibility is established; simultaneous
primality is not. A polynomial bound in $M$ for the first such pair would,
combined with the subexponential modulus and a finite bridge, imply the
stronger Erdős rate. That quantitative two-form assertion is unproved and is
not ordinary Linnik's theorem or a consequence supplied by qualitative Dickson.

## Review and sources

[Verification](VERIFICATION.md) records the exact source revision, independent
model-review scope and executable checks. This is a conventional mathematical
research note, not a formalization or externally refereed paper.

The motivating questions are [Erdős problem 853](https://www.erdosproblems.com/853),
with its [official history](https://www.erdosproblems.com/history/853). Primary
covering and sieve references appear beside their use in the full proof.
