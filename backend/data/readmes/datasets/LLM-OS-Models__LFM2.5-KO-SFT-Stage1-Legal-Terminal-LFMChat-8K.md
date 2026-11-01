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

# LFM2.5-KO-SFT-Stage1-Legal-Terminal-LFMChat-8K

Stage1 8k Korean legal/terminal/tool-use prepared SFT arrays.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Korean legal task corpus: `korean_legal_tasks` prepared split.
- Terminal/tool behavior: `terminal_toolbench` prepared split, derived from LFM2.5 Terminal ToolBench style conversations.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- 8k context is used to preserve longer legal and terminal/tool traces.
- This stage is full-parameter SFT, not LoRA.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 1600835 |
| token count | 1658848754 |
| max sequence / sample length | 8192 |
| uploaded size bytes | 6704529018 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql_8k_legal_terminal
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql_8k_legal_terminal",
  "size_bytes": 6704529018,
  "merge_stats.json": {
    "inputs": [
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql.parts/korean_legal_tasks",
        "samples": 1383340,
        "tokens": 1055974455
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage1_ko_finance_terminal_text2sql.parts/terminal_toolbench",
        "samples": 217495,
        "tokens": 602874299
      }
    ],
    "samples": 1600835,
    "tokens": 1658848754,
    "avg_sample_len": 1036.2396836650873,
    "max_sample_len": 8192,
    "epochs": 1
  },
  "file_count": 9
}
```
