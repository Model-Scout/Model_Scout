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

# LFM2.5-KO-SFT-Stage1-Finance-Text2SQL-LFMChat-4K

Stage1 4k finance/Text2SQL prepared SFT arrays.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Finance/accounting SFT: `finance_bcai_hrm` prepared split.
- Structured Text2SQL/code-like reasoning: `text2sql_core` prepared split.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Main 4k SFT stage for Korean finance/accounting explanations and SQL-style exact structured outputs.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 2302304 |
| token count | 1285864494 |
| max sequence / sample length | 3741 |
| uploaded size bytes | 5235038981 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql_4k_finance_text2sql
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql_4k_finance_text2sql",
  "size_bytes": 5235038981,
  "merge_stats.json": {
    "inputs": [
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql.parts/finance_bcai_hrm",
        "samples": 1861521,
        "tokens": 1188434718
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql.parts/text2sql_core",
        "samples": 440783,
        "tokens": 97429776
      }
    ],
    "samples": 2302304,
    "tokens": 1285864494,
    "avg_sample_len": 558.5120357693858,
    "max_sample_len": 3741,
    "epochs": 1
  },
  "file_count": 9
}
```
