# Research workflow for humans and AI agents

Use this workflow with any one branch of the classification. It mirrors the useful structure of the research process without requiring private chat history. It is guidance, not an automatic acceptance process.

## 1. Freeze and understand the starting point

Record the public repository commit, exact statement and manuscript section. Read its definitions and dependencies, not just the catalogue. Write down the group model, inversion, stabilizer, selected translations, loop equivalence and quantifiers. Distinguish a subgroup construction from an actual loop construction.

Mark each input:
- published theorem with exact locator;
- project proof with exact revision and scope;
- unreviewed proposed lemma;
- finite computation and its input;
- unavailable or incomplete dependency.

Do not treat missing imports as established facts. Consult [coverage](COVERAGE_AUDIT.md) and [SD dependencies](SD_DEPENDENCIES.md).

## 2. Choose a decisive question

Use [current results](RESULTS.md) and [open problems](OPEN_PROBLEMS.md). State what would count as progress before computing. Examples:
- prove the converse of an existing construction;
- show an admissible family covers a named residual case;
- recover a parameter invariant from the unmarked loop;
- exhibit an actual counterexample to a proposed boundedness statement;
- resolve one exact cohomological or section compatibility obstruction.

Do not equate a group extension, a quotient shadow or a numerical solution with an admissible simple Bol loop.

## 3. Alternate breadth with depth

Briefly compare several materially different approaches and test easy obstructions. Then pursue the strongest deeply. If it fails, isolate the missing lemma or counterexample and change approach rather than accumulating equivalent reformulations. Keep useful failed attempts so another researcher does not repeat them.

For experiments, choose the smallest cases that can falsify the conjecture. Preserve all correlations and actual marked data. A success on small cases motivates a conjecture; it does not establish exhaustion.

## 4. Separate the four mathematical obligations

For a family, report separately:
1. admissibility and sound construction;
2. simplicity and properness;
3. exhaustion within an explicitly named scope;
4. exact isomorphism criterion, and isotopy only if separately investigated.

State parameter overlaps and exceptional cases. Never silently strengthen “entire canonical group is G” to “some composition factor is G,” or remove a paired-inversion hypothesis.

## 5. Produce a reusable packet

A suggested layout is:

```text
statement.md       exact theorem/conjecture and scope
proof.md           argument and dependency list
examples.md        minimal positive and negative controls
code/              source and exact input data, if needed
reproduce.md       versions, commands, outputs and expected checks
review.md          independent review of a fixed revision
next.md            unresolved obligations and promising next attack
```

Do not add empty scaffolding for its own sake. One readable document can contain all seven sections. Existing manuscripts may retain their established layout.

A dependency entry should state the theorem actually used, source/section, required hypotheses, and whether it is publicly available. Attach source-data hashes to finite certificates. Record which scripts were actually rerun, not merely copied.

## 6. Review and integrate

Seek a separate review of a pinned revision. A reviewer should try to break the proof: hidden independence assumptions, lost multiplicities, incorrect quotients, insufficient isomorphism groups and extrapolation from finite checks are recurring risks here. Record objections, repairs and unresolved qualifications.

After repair, update the catalogue and open task only as far as the result warrants. Preserve old snapshots and explain supersession. Independent AI review is not human refereeing or formal verification; historical novelty is a separate question.

## A compact handoff template

> **Question and scope:**  
> **Source revision and exact starting result:**  
> **What is newly established:**  
> **Proof/dependency links:**  
> **Computations actually run:**  
> **Known gaps or failed routes:**  
> **Review scope:**  
> **Next decisive target:**

This makes a task restartable by another human or model. A summary without accessible mathematical inputs is a progress report, not a complete handoff.
