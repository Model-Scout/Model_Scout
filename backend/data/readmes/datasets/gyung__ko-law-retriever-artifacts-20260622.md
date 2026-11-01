---
license: other
tags:
  - korean
  - legal
  - retrieval
  - rag
  - evaluation
language:
  - ko
---

# Korean Legal Retriever Artifacts 2026-06-22

This public dataset repository stores large artifacts for `ko-law-retriever`
that are too large for GitHub's 100 MB file limit.

## Contents

- `ko_legal_source_rag/`: retriever SFT JSONL mixes and metadata.
- `ko_legal_retriever/ko_legal_fts_full.sqlite`: local SQLite FTS retrieval index.
- `evals/`: source-rag evaluation outputs.
- `reports/`: analysis JSON/Markdown reports and evidence-pack outputs.

## Scope

These files are for retrieval research and reproducibility. The retriever is
trained to emit JSON tool actions and select evidence; it is not a standalone
legal-advice model.

Before downstream redistribution, review the source terms for any statute,
precedent, ordinance, administrative-rule, or exam-derived text included in the
local corpus.
