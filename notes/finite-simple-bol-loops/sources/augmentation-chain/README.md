# Reproducing the exponent-six augmentation chain

**Mira Cult**

The [proof of 0113](../../manuscripts/0113-infinite-augmentation-chain.md) builds a strictly nested sequence of finite simple proper left Bol loops. Its fixed input is the [published matrix bundle for 0112](../elementary-psl2-19/README.md). There is no new external dataset. Both programs use Python and NumPy and take the compressed base file as their argument. From this directory run:

```sh
python3 code/verify_psl2_19_infinite_chain.py ../elementary-psl2-19/evidence/psl2-19-explicit-matrix-input.json.zlib.b64
python3 code/independent_augmentation_physical_squares.py ../elementary-psl2-19/evidence/psl2-19-explicit-matrix-input.json.zlib.b64
```

The [author verifier](code/verify_psl2_19_infinite_chain.py) chooses the first available independent column and checks the bottom rank and all-cut iteration at the base and after three additions ([output](evidence/author.out)). The [independent verifier](code/independent_augmentation_physical_squares.py) chooses different, reproducible couplings, tests every one of the eight actual two-sign collision systems at each of four stages, and constructs a nonzero forbidden coupling with a tilted flat pair ([output](evidence/independent.out)). Neither program estimates the induction from a finite sample.

The [separate mathematical audit](evidence/chain-audit.txt) accepts the exact source revision `2c7ffe13a1f1af9f2ac38ee5dee8b417c076b466` on top of the reviewed base: the strictly increasing sequence, honest subloop embeddings, common exponent, faithful left groups and countably infinite locally finite simple union. The canonical proof source has SHA-256 `f0f8e560609c44ff40a665a87aca52c5d233d95618d1b619d8e38581f7ea85bd`. The original complete audit, separately pinned with SHA-256 `edb1498363f9f07e53db44502ae4d01c2990e754da1c23ab3bfc52eb2e6913a8`, is identified in the [manifest](manifest.json). This is independent AI mathematical review, not human refereeing or formal verification. It does not classify all loops, count all operations of a fixed order, or establish priority. Mira Cult directed the research; OpenAI models assisted with the construction and the separate audit. Exact model versions were not verified.
