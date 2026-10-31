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
- tokenized
---

# LFM2.5-KO-SFT-Stage2-Diverse-KoSWE-Reasoning-LFMChat-4K

Stage2 diverse Korean/SWE/reasoning prepared SFT arrays, LFM tokenizer.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Tokenized version of the Stage2 diverse KO/SWE/reasoning raw LFM chat mix.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Prepared with the LFM tokenizer and response-only labels for 4k full SFT.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 1467848 |
| token count | 1364349642 |
| max sequence / sample length | 4096 |
| uploaded size bytes | 5522278706 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning_4k
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning_4k",
  "size_bytes": 5522278706,
  "merge_stats.json": {
    "inputs": [
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/korean_domain_core",
        "samples": 219066,
        "tokens": 150707527
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/behavior_core",
        "samples": 289697,
        "tokens": 316932036
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/swe_zero",
        "samples": 53557,
        "tokens": 178477164
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/swe_glm_mix",
        "samples": 109560,
        "tokens": 244254758
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/swe_zero_30m",
        "samples": 8807,
        "tokens": 29320491
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/glm_reasoning",
        "samples": 56003,
        "tokens": 65777594
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/hf_extra_reasoning_agent_mm",
        "samples": 38292,
        "tokens": 99376915
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/agent_reasoning_25m",
        "samples": 8519,
        "tokens": 22061871
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/finance_50m",
        "samples": 108491,
        "tokens": 69608924
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/korean_legal_50m",
        "samples": 110575,
        "tokens": 81098603
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_diverse_ko_swe_reasoning.parts/text2sql_duckdb",
        "samples": 465281,
        "tokens": 106733759
      }
    ],
    "samples": 1467848,
    "tokens": 1364349642,
    "avg_sample_len": 929.489730544307,
    "max_sample_len": 4096,
    "epochs": 1
  },
  "file_count": 9
}
```
