# Actual algebra groups in one principal isotope of a simple exponent-six projective loop

**Mira Cult · Provisional research.** The author proofs below have not been independently reviewed.

The direct calculation below is distinct from the group inclusion in [the noncommutative radical theorem](noncommutative-radicals.md), on which existence of the ambient finite simple exponent-six host depends. Neither claim has completed independent review. The [earlier class-two native host](../proofs/native-subloops.md) only concerns the class and exponent stated there; the [odd right-nucleus construction](../../right-nuclei/proofs/all-odd-groups.md) already realizes finite odd groups as subloops without this specific projective/exponent-six-isotopy constraint.

**Theorem.** For every finite-dimensional nilpotent associative ternary algebra $`R`$ there is a finite simple non-Moufang left Bol loop $`Q`$ of exponent six and a genuine involution $`k\in Q`$ for which the **single** principal isotope

```math
x\circ y=x\cdot(k\cdot y)
 \tag{1}
```

is also a finite simple non-Moufang left Bol loop, has exactly the same permutation left multiplication group as $`Q`$, and contains the algebra group $`1+R`$ under its **own multiplication**. The common faithful left group modulo its whole solvable radical is $`\mathrm{PSL}_2(19)`$. The construction is simultaneous for a finite list of algebras by taking their direct sum. In particular every finite $`3`$-group occurs as a native subloop of a finite simple proper loop *isotopic by an involution to an exponent-six simple loop with this fixed quotient*. This does not say those arbitrary $`3`$-groups embed in the original exponent-six loop, nor turn an embedded subgroup of its left group automatically into a native subloop.

## The multiplication, not just a faithful action

Take $`V=R\oplus R\oplus S`$ with cross-products zero, where $`S=Fa\oplus Fb`$ has $`a^2=b`$, $`a b=b^2=0`$. Use the algebra automorphism $`\sigma(r,s,v)=(s,r,\sigma_0 v)`$, $`\sigma_0a=-a`$, $`\sigma_0b=b`$. Apply the [noncommutative local-algebra theorem, §3](noncommutative-radicals.md#3-native-two-sheets-for-noncommuting-local-units) to the entire two-sheet law on $`V`$, embedded with **all** native left products in one finite simple proper $`Q`$. Here $`k=(1,0)`$ is the genuine involution interchanging the sheets and applying $`\sigma`$. Left alternativity gives $`L_k^2=1`$ in $`Q`$. Thus (1) is the principal isotope with parameters $`k`$ and the old identity $`1`$, and its identity is $`k`$.

Since the small two sheets are closed under (1), evaluate the product of two old odd points there. On their $`V`$ coordinates it is **exactly**

```math
u\diamond v=u+(1+u)(1+\sigma u)^{-1}v.
```

Take $`u=(x,0,0)`$ and $`v=(y,0,0)`$. Its scalar on the first copy of $`R`$ is $`1+x`$, on the second $`(1+x)^{-1}`$, and it multiplies only on the left. Thus the first coordinate of $`u\diamond v`$ is $`x+y+xy`$, and the others vanish. Consequently $`1+x\mapsto (1,(x,0,0))`$ is a native group embedding of the *original* algebra group, not its opposite or associated graded group. Its inverses and both divisions agree: it is closed with the law $`1+(x+y+xy)=(1+x)(1+y)`$, contains the new identity, and divisions in a loop are unique.

## Properties of the actual isotope

Writing $`K=\{L_x:x\in Q\}`$ and $`c=L_k=c^{-1}`$, its left translations are precisely $`Kc`$. The word $`(a c)(b c)(a c)=(a(cbc)a)c`$ lies in $`Kc`$ by the original Bol sandwiches. Left translations are sharply indexed by their value at the new identity $`k`$, so this is the left Bol law of the new loop. Its group is literally unchanged: $`L'_1=c`$ and $`L_x=L'_x c`$. Simplicity is unchanged as well: (1) is a polynomial with parameter $`k`$ in the old multiplication, and the reverse polynomial is $`x\cdot y=x\circ(1\circ y)`$ since $`1\circ y=k\cdot y`$. Equivalences compatible with the loop operations are therefore the same. For precision the divisions are interdefinable too: the right equation $`X\circ b=a`$ is the old right equation $`X\cdot(kb)=a`$, and the left equation $`b\circ X=a`$ is solved by $`X=k(b\backslash a)`$; in reverse the fixed translation $`1\circ(-)`$ is itself involutive. Hence a nontrivial proper loop quotient could not appear by the isotope.

The scalar algebra $`S`$ merely ensures an explicit non-Moufang witness in the isotope irrespective of $`R`$. Its original two-sheet loop, in coordinates $`(e,v,z)`$ with $`v,z\in F`$, is $`(e,v,z)(f,w,t)=(e\oplus f,v+(-1)^e w,z+t+evw)`$. In the isotope use coordinates $`(e,v,z)\mapsto(1\oplus e,-v,z)`$; direct substitution gives the same dihedral first coordinates and central cochain $`(e-1)vw`$. Taking $`X=(0,1,0)`$ and $`Y=(1,0,0)`$ in these *new* labels gives $`(X\circ Y)\circ X`$ vs. $`X\circ(Y\circ X)`$ with unequal central coordinates (respectively $`0`$ and $`1`$ in $`F`$). The isotope is not flexible, hence not Moufang. The witness is independent of a classification of simple Moufang loops or an appeal to a general isotopy theorem.

If $`r=\dim R`$, the algebra used for the ambient construction has dimension $`2r+2`$, so (2) of that theorem gives host order at most $`20\cdot3^{218+80r}`$, polynomial in $`|1+R|`$. For an arbitrary finite $`3`$-group $`H`$, use a faithful unitriangular representation of $`H`$ in $`1+R`$, for $`R`$ the strictly upper triangular matrices of dimension $`m\times m`$; $`m=|H|`$ suffices by the invariant-flag argument of the [radical proof, §4](noncommutative-radicals.md#4-explicit-universal-radical-consequence). A fixed $`m`$ gives one actual host for all subgroups of $`\mathrm{UT}_m(3)`$. No polynomial bound in $`|H|`$ is asserted when the representing algebra is not controlled in those terms.

**Unbounded native exponent change.** For each $`s\ge2`$, take $`R=tF[t]/(t^{3^{s-1}+1})`$. The genuine old odd point corresponding to $`1+t`$ in the new native group has order $`3^s`$, since $`(1+t)^{3^j}=1+t^{3^j}`$. The original simple loop has exponent exactly six. Thus a *single principal isotope at an involution* produces unbounded native element orders and unbounded exponent ratios within an otherwise fixed projective quotient. The isotope need not have exponent six, and is certainly not isomorphic to the original for these $`s`$.

[Overview and reproducible checks](README.md)
