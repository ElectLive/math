# Verification and references

This is a computer-assisted mathematical proof, not a formalization. In a separate review, all seven lower-bound groups were run from their initial domains using the same exact implementation, and their ordered verdict digests matched. The construction was also rerun: 72 wall inequalities and 153 pair separations. The mathematical review checked the continuous enclosure, finite cover and live-branch arguments. Independent replay of the shared implementation is not an independent implementation of the geometry kernel; no external referee review is claimed.

The public replay includes only the 18-square theorem and its required sources and finite inputs. It makes no claim about other square counts, uniqueness, or having discovered the first layout of this side.

## References

- Erich Friedman, [*Packing Unit Squares in Squares: A Survey and New Results*](https://erich-friedman.github.io/papers/squares/squares.html), *Electronic Journal of Combinatorics*, Dynamic Survey 7. See Figure 7 and the table for the upper bound credited to Pertti Hämäläinen and other layouts with the same side.
- [The Squares Project: the 18-square ledger at a fixed historical revision](https://github.com/jlevy/squares/blob/1015fc175fa4e2c01f912d915d784100e36d3bab/packing/frontier/n-018.md), distinguishing the known construction from the lower bound recorded there.
- [Local source and runnable certificate](replay/README.md).
