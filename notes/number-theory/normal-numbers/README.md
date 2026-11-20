# Normal numbers and digit expansions

This workspace studies the digits of fixed real numbers and what changes when we read the same number in different bases.

## Joint digit switches in coprime bases

A **switch** is an adjacent pair of unequal digits within one expansion. For example, `10011` has two switches. Count the switches separately in the first $N$ fractional digits in base 2 and in base 3, then add the counts.

For every irrational real number, the combined count is at least a positive constant times $\log N\log\log N$ for every sufficiently large $N$. The constant is independent of the number; the cutoff may depend on it. The same result holds for any fixed pair of coprime integer bases.

**[Read the theorem and full proof](0001-joint-digit-switches.md).** The proof analyzes sparse windows in the two expansions and uses the quantitative Subspace Theorem to bound how often such windows can occur.

## What remains open

This bound does not choose a base in which the switches are frequent, prove positive switch density, or prove normality of any particular irrational number. Natural next questions are whether the joint lower bound can be increased and what fails when the bases share a prime factor.

For a separate construction that *builds* normal digit streams, see [Normal dovetails from analytic functions](../normal-dovetails/README.md).
