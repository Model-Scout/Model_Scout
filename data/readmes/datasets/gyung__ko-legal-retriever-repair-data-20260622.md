---
license: other
tags:
  - korean
  - legal
  - retrieval
  - tool-use
  - sft
language:
  - ko
---

# Korean Legal Retriever Repair Data 2026-06-22

This dataset bundle contains SFT rows for Korean legal retrieval tool use.

The rows are intended to train a model to emit JSON tool actions, not to generate final legal answers.

## Included Local Files

- `lfm_retriever_v9_hardcase_mix_20260622.jsonl`
- `lfm_retriever_v10_source_rag_hardcases_20260622.jsonl`
- `lfm_retriever_v10_source_repair_mix_20260622.jsonl`
- `lfm_retriever_v11_strict_action_hardcases_20260622.jsonl`
- `lfm_retriever_v11_strict_action_mix_20260622.jsonl`
- `lfm_retriever_v12_extended_tools_sft_20260622.jsonl`
- `lfm_retriever_v12_extended_tools_mix_20260622.jsonl`
- matching `.meta.json` files

Local source directory:

```text
/home/work/.data/harness1/ko_legal_source_rag
```

## Download

```bash
hf download gyung/ko-legal-retriever-repair-data-20260622 \
  --repo-type dataset \
  --local-dir ko-legal-retriever-repair-data-20260622
```

Large reproducibility artifacts that do not fit in GitHub are published in:

```bash
hf download gyung/ko-law-retriever-artifacts-20260622 \
  --repo-type dataset \
  --local-dir ko-law-retriever-artifacts-20260622
```

## Schema

Each JSONL row contains:

- `messages`: chat messages ending with a target assistant JSON action.
- `target_tool`: one of the retrieval or official-source tools listed below.
- `query_id`
- `query`
- `gold_doc_ids`
- `answer_doc_ids`
- `source`

## Tool Actions

```json
{"tool":"fan_out_search","queries":["검색어 1","검색어 2"]}
{"tool":"review_docs","doc_ids":["doc_id"]}
{"tool":"curate","add_ids":["doc_id"]}
{"tool":"verify","doc_ids":["doc_id"],"claim":"검증할 법률 명제"}
{"tool":"end_search","reasoning":"필요한 근거 문서를 검색, 검토, curate, 검증했다."}
```

Extended official-source actions in v12:

```json
{"tool":"law_search","query":"민법 제126조","search_body":false,"display":10}
{"tool":"law_fetch","law_id":"001706","law_name":"민법","article_no":"126"}
{"tool":"precedent_search","query":"표현대리 정당한 이유 대법원","search_body":true,"display":10}
{"tool":"precedent_fetch","precedent_id":"228541","case_name":"손해배상"}
{"tool":"google_legal_search","query":"site:law.go.kr 민법 제126조 표현대리 판례","display":10}
```

Official data-source functions are implemented locally in:

```text
harness-1/tools/ko_law_openapi_tools.py
```

## Release Notes

This public dataset may include snippets from Korean legal corpora. Before downstream redistribution, review source licenses and any restrictions for statute, precedent, ordinance, administrative-rule, exam-derived, or web-derived text.

## Evaluation

See:

```text
harness-1/docs/KO_LEGAL_RETRIEVER_TOTAL_SUMMARY_20260622.ko.md
harness-1/docs/KO_LEGAL_RETRIEVER_ONLY_STATUS_20260622.ko.md
```
