---
license: other
language:
- ko
- en
tags:
- lfm
- korean
- sft
- lfm-chat
- jsonl
---

# LFM2.5-KO-CPT-Full-LFMStyle-Shards-20260627

Source-separated LFM-style CPT shards: Korean Wiki, finance, legal raw/tasks/RAG/bar answers, and terminal ToolBench.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Source-separated CPT shards for Korean Wiki, Korean finance, Korean legal raw/task/RAG/bar-answer data, and terminal/tool-use traces.
- Shard filenames are preserved under `data/` so consumers can inspect or reweight domains independently.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Use this repo when you need source-level filtering, deduplication, or domain-ratio reconstruction.
- This is the best public artifact for auditing which CPT source files entered the KO-CPT run.

## Summary

| field | value |
|---|---:|
| kind | `raw_lfm_chat_jsonl` |
| sample count | n/a |
| token count | n/a |
| max sequence / sample length | n/a |
| uploaded size bytes | 26204095030 |

## Format

- `raw_lfm_chat_jsonl`: JSONL rows with a `text` field containing LFM ChatML-like conversation text.
- `prepared_tokenized`: NumPy response-only SFT arrays built with the LFM tokenizer:
  - `tokens.npy`
  - `epoch_0/inst_start.npy`
  - `epoch_0/inst_len.npy`
  - `epoch_0/resp_start.npy`
  - `epoch_0/resp_len.npy`
  - `tokenizer.json`

## Local Source Path

```text
/home/work/.data/lfm2_ko_cpt/datasets/shards_full_lfmstyle_20260627
```

## License And Usage Notes

This release republishes preprocessing artifacts used for the LFM2.5 Korean CPT/SFT
workflow. Source components come from multiple public or locally prepared
datasets, so downstream users should verify each upstream source license before
redistribution or commercial use. Legal and finance examples are for model
training/evaluation only and are not legal, financial, or investment advice.

## Stats

```json
{
  "path": "/home/work/.data/lfm2_ko_cpt/datasets/shards_full_lfmstyle_20260627",
  "size_bytes": 26204095030,
  "jsonl_files": [
    {
      "name": "000_kowiki_raw_full_20260524.jsonl",
      "size_bytes": 2055390454
    },
    {
      "name": "001_bcai_finance_kor_hrm_20260524.jsonl",
      "size_bytes": 5677401098
    },
    {
      "name": "002_BCAI-Finance-Kor-1862K.jsonl",
      "size_bytes": 5664370381
    },
    {
      "name": "003_korean_legal_raw_full_20260523.jsonl",
      "size_bytes": 1801038575
    },
    {
      "name": "004_korean_legal_tasks_full_20260524.jsonl",
      "size_bytes": 4130351212
    },
    {
      "name": "005_korean_admrule_precedent_raw_full_20260524.jsonl",
      "size_bytes": 1682358397
    },
    {
      "name": "006_ko_legal_source_agent_sft_20260621.jsonl",
      "size_bytes": 123458032
    },
    {
      "name": "007_ko_legal_rag_agent_sft_round15_v2.jsonl",
      "size_bytes": 14971282
    },
    {
      "name": "008_current_law_bar_json_answer_sft_20260621.jsonl",
      "size_bytes": 8900012
    },
    {
      "name": "009_lfm25_terminal_toolbench_hrm_turns_v1.jsonl",
      "size_bytes": 5045852445
    }
  ],
  "file_count": 20
}
```
