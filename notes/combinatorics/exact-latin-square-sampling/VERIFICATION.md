# Scope and verification

The [paper](paper/README.md) gives a conventional proof draft for exact uniformity over all labeled Latin squares of every positive order and $\widetilde O(n^{25})$ expected total bit cost. Rejection and restarts are allowed. This is not a worst-case bound, a proof of rapid mixing for a Latin-square walk, or a forward-only construction.

The all-target logarithmic comparison, weighted terminal construction, regular-board count lower bound, exact multiscale correction, and bit accounting received separate checks within the AI-assisted project. The paper states the mathematical argument and cites its external dependencies. These checks are not external refereeing, formal verification, a claim of priority, or measured performance for the revised sampler.

The [reference code](code/README.md) comes from the earlier finite reference implementation. Its checks include exact rational mass at every labeled square of orders 3 and 4, exact reduced-square counts through order 7, and separate finite-law checks of the optional matching backend. The implementation does not yet combine the revised terminal proposal and multiscale gate at a certified theorem scale; those tests do not establish the revised runtime for the executable.

The exposition is by Mira Cult; the paper uses Mira's chosen byline. Mira set the problem and directed the research. OpenAI GPT-6.2 Astra models contributed to proof development, exposition, reference code, and internal cross-checking.
