#!/usr/bin/env python3
"""Command-line exact labeled-square sampler. Run with -h for help."""
import argparse
import json
import random

from exact_core import ReducedSpace, sample_latin


def main(argv=None):
    p = argparse.ArgumentParser(description="Draw exactly uniform labeled Latin squares (0-based labels by default).")
    p.add_argument("n", type=int, help="positive Latin-square order")
    p.add_argument("--samples", type=int, default=1, help="number of independent draws; one JSON square per line")
    p.add_argument("--method", choices=("auto", "reduced", "rejection", "decorated", "huber"), default="auto",
                   help="auto: reduced unranking up to order 7, row rejection thereafter; decorated/huber: three-family finite reference")
    p.add_argument("--seed", type=int, default=None, help="deterministic test PRNG only; omit for system randomness")
    p.add_argument("--one-based", action="store_true", help="display symbols as 1,...,n instead of 0,...,n-1")
    p.add_argument("--counts", action="store_true", help="compute reduced and labeled counts instead of sampling")
    p.add_argument("--rank", type=int, help="unrank one labeled square deterministically, using reduced-square DP")
    a = p.parse_args(argv)
    if a.n < 1 or a.samples < 1:
        p.error("n and --samples must be positive")
    if a.counts and a.rank is not None:
        p.error("--counts and --rank are mutually exclusive")
    if a.rank is not None and (a.samples != 1 or a.rank < 0):
        p.error("--rank requires a nonnegative rank and --samples 1")
    if a.counts:
        s = ReducedSpace(a.n)
        print(json.dumps({"order": a.n, "reduced": s.reduced_count, "labeled": s.labeled_count}))
        return
    rng = random.Random(a.seed) if a.seed is not None else None
    small = a.method == "reduced" or (a.method == "auto" and a.n <= 7)
    space = ReducedSpace(a.n) if small or a.rank is not None else None
    for _ in range(a.samples):
        if a.rank is not None:
            if a.rank >= space.labeled_count:
                p.error("rank must be smaller than the labeled square count")
            out = space.unrank(a.rank)
        elif space is not None:
            out = space.sample(rng)
        elif a.method in ("decorated","huber"):
            from decorated import sample_decorated, sample_huber
            out = (sample_decorated if a.method=="decorated" else sample_huber)(a.n,rng)
        else:
            out = sample_latin(a.n, rng, method="rejection")
        if a.one_based:
            out = [[x+1 for x in row] for row in out]
        print(json.dumps(out, separators=(",", ":")))


if __name__ == "__main__":
    main()
