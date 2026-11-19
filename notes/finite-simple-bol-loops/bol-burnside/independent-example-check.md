# An independent check of the two-generator example

A separate AI mathematical review accepted the [explicit construction](two-generators.md) for every odd prime. It checked the actual loop operations, two-generator assertion, quotient and residual-finiteness arguments, and the distinction between translation sides. It did not assess priority or the separate positive translation-group theorem.

## Recover the Bol identity in the actual action

Use the affine maps

```math
s(i,h,k):(j,v)\longmapsto(j+i,v+h+jk).
```

The native translations are exactly the displayed section with $`(1+it)k=2th`$$. Each $`1+it`$$ is invertible in the stated ring, which gives both loop division laws. Compose three genuine transformations, using the first again at the end. If the two inputs have triples $`(i,h,k)`$$ and $`(j,u,v)`$$, their sandwich is

```math
(2i+j,\,2h+u+(i+j)k+iv,\,2k+v).
```

Multiplying the new middle entry by $`2t`$$ and substituting the two input relations gives $`(1+(2i+j)t)(2k+v)`$$. Thus the sandwich belongs to the section, and its value at zero identifies the actual left translation. Iterating one affine map $`p`$$ times gives zero increment because $`p`$$ and $`\binom p2`$$ vanish in characteristic $`p`$$.

The review independently traced three native multiplications from a base-zero point to another base-zero point: their multiplier can be *any* $`(1+ht)/(1+it)`$$. Addition and these multipliers give every allowed numerator and inverse denominator. Reductions at irreducibles separate unequal coordinates. This proves residual finiteness for the example, not for the free loop. For the opposite-hand word, finite order on the free loop would imply finite order downstairs, contradicted by the rational multiplier.

## A different family of finite tests

Instead of irreducible field reductions, reduce modulo $`t^d`$$. These quotients also separate the infinite loop: each nonzero numerator has finite vanishing order at zero, and every denominator is a unit there. The wrong-hand product in the construction acts on the whole fiber $`i`$$ by

```math
\lambda_i=1-\frac{2t^2}{(1+it)(1+(i+1)t)}.
```

The first nonzero term of $`\lambda_i-1`$$ has degree two. In characteristic $`p`$$, raising to $`p^h`$$ multiplies that first degree by $`p^h`$$. Thus the exact order of the permutation on the **whole** truncated loop is the least $`p^h`$$ for which $`2p^h\ge d`$$; the point with second coordinate 1 attains it. At $`d=2`$$ these truncated-ring quotients are actually associative; the degree-two **field** quotients in the proof are not. The [independent program](code/check_native_t_adic_burnside.py) tests both, builds ordinary multiplication tables, and follows actual point orbits, including periods 81, 125 and 343. [Review and reproduction scope](verification.md).
