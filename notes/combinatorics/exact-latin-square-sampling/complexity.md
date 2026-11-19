# Expected bit complexity

The [paper](paper/README.md) proves **$\widetilde O(n^{25})$ expected total bit work** for exact uniform generation of a labeled order-$n$ Latin square. The tilde hides fixed powers of $\log(2n)$. The bound includes preprocessing, rational arithmetic, random bits, and failures and restarts.

| Step | Bound and scope |
| --- | --- |
| One exact uniform perfect matching | $\widetilde O(n^{21})$ expected bit work on boards of side at most $n$, using the [finite rational matching subroutine](pm-bit-clock.md) derived from Göbel, Liu, Manurangsi and Pappik. |
| One decorated forward or reverse gate | $\widetilde O(n^4)$ matching draws. Binary conditioning reduces the cost of each inverse-probability probe. Bounded weighted fills use ordinary uniform matching draws and exact rational rejection. |
| Other work | $\widetilde O(n^{24})$ suffices for the remaining bookkeeping, including the finite cubic block calculation and calibration. |
| Number of gate uses | The counting lower bound makes the threshold comparable to the number of squares. Multiscale flattening then adds logarithmic factors, not a further power of $n$. |

Thus the leading bound is the matching-call budget times the matching bit cost. This is not a claim of an optimal exponent, a worst-case guarantee, or a measured scaling law. The [runnable reference](code/README.md) has its own, different cost. It does not implement the revised sampler end to end.
