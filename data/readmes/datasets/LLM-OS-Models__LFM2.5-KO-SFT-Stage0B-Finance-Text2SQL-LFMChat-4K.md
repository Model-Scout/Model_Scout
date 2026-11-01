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

# LFM2.5-KO-SFT-Stage0B-Finance-Text2SQL-LFMChat-4K

Stage0b finance/Text2SQL/legal fast mix, LFM tokenizer.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Korean finance/accounting instruction data sampled from the BCAI finance family used locally.
- Text2SQL clean DuckDB-style structured reasoning data.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Fast full-SFT smoke stage for finance/Text2SQL behavior and 8-GPU DDP stability.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 280000 |
| token count | 58090087 |
| max sequence / sample length | 1846 |
| uploaded size bytes | 259227543 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0b_fast_mix_4k_finance_text2sql
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0b_fast_mix_4k_finance_text2sql",
  "size_bytes": 259227543,
  "merge_stats.json": {
    "inputs": [
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0b_fast_mix.parts/finance_bcai_120k",
        "samples": 120000,
        "tokens": 36119985
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0b_fast_mix.parts/text2sql_160k",
        "samples": 160000,
        "tokens": 21970102
      }
    ],
    "samples": 280000,
    "tokens": 58090087,
    "avg_sample_len": 207.46459642857144,
    "max_sample_len": 1846,
    "epochs": 1
  },
  "file_count": 9
}
```
