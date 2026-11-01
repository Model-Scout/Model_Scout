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

# LFM2.5-KO-SFT-Stage2-Diverse-KoSWE-Reasoning-LFMChat-Raw

Stage2 raw LFM chat JSONL shards: Korean domain, behavior, SWE/coding, reasoning, finance, legal, Text2SQL.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Korean domain core.
- Behavior core covering terminal/tool/SWE/reasoning/legal/finance patterns.
- SWE/coding sources: `swe_zero`, `swe_glm_mix`, compact SWE supplement.
- Reasoning/agent sources: GLM reasoning, HF extra reasoning/agent mix, compact agent-reasoning supplement.
- Compact finance/legal reinforcement and Text2SQL DuckDB data.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Raw LFM chat JSONL for Stage2 before tokenization.
- CPT-style raw corpora such as Korean Wiki and raw statutes are intentionally excluded from this SFT stage.

## Summary

| field | value |
|---|---:|
| kind | `raw_lfm_chat_jsonl` |
| sample count | n/a |
| token count | n/a |
| max sequence / sample length | n/a |
| uploaded size bytes | 5607408357 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.jsonl
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.jsonl",
  "size_bytes": 5607408357,
  "jsonl_files": [
    {
      "name": "agent_reasoning_25m.jsonl",
      "size_bytes": 94601210
    },
    {
      "name": "behavior_core.jsonl",
      "size_bytes": 1319724616
    },
    {
      "name": "finance_50m.jsonl",
      "size_bytes": 325143039
    },
    {
      "name": "glm_reasoning.jsonl",
      "size_bytes": 281229435
    },
    {
      "name": "hf_extra_reasoning_agent_mm.jsonl",
      "size_bytes": 425776347
    },
    {
      "name": "korean_domain_core.jsonl",
      "size_bytes": 635356361
    },
    {
      "name": "korean_legal_50m.jsonl",
      "size_bytes": 309121598
    },
    {
      "name": "swe_glm_mix.jsonl",
      "size_bytes": 968054909
    },
    {
      "name": "swe_zero.jsonl",
      "size_bytes": 686754913
    },
    {
      "name": "swe_zero_30m.jsonl",
      "size_bytes": 112607969
    },
    {
      "name": "text2sql_duckdb.jsonl",
      "size_bytes": 449032124
    }
  ],
  "file_count": 22
}
```
