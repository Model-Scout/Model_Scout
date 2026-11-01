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

# LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-Raw

Fable5/Helio Korean agentic traces and local grounded document/log examples converted to LFM chat JSONL.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Local Fable5 Korean traces: `fable_distillation/datasets_ko/fable5_ko_sft_20260624.jsonl`.
- Local Helio Korean reasoning traces: `fable_distillation/datasets_ko/helio_ko_sft_20260628.jsonl`.
- Grounded examples generated from this project's README, runbook, train logs, git-push failure patterns, and vLLM/agent harness docs.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- This is a separate Stage3 Agentic/Fable follow-up dataset, not part of the main Stage2 KO-SFT release.
- The goal is command-following, log inspection, evidence-grounded diagnosis, and terminal/tool style behavior.

## Summary

| field | value |
|---|---:|
| kind | `raw_lfm_chat_jsonl` |
| sample count | n/a |
| token count | n/a |
| max sequence / sample length | n/a |
| uploaded size bytes | 38473643 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded.jsonl
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded.jsonl",
  "size_bytes": 38473643,
  "jsonl_files": [
    {
      "name": "fable5_helio_agentic.jsonl",
      "size_bytes": 38446004
    },
    {
      "name": "local_grounding_logs_docs.jsonl",
      "size_bytes": 27215
    }
  ],
  "file_count": 3
}
```
