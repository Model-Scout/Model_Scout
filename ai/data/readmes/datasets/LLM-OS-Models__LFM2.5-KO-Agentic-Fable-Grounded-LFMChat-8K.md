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

# LFM2.5-KO-Agentic-Fable-Grounded-LFMChat-8K

Agentic/Fable grounded 8k prepared response-only SFT arrays.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Tokenized response-only 8k version of the Agentic/Fable grounded LFM chat raw dataset.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Target model repo: `LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT`.
- Stage3 is intentionally separated from the main Stage2 SFT model line.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 3943 |
| token count | 7124298 |
| max sequence / sample length | 8192 |
| uploaded size bytes | 46530552 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded_8k
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded_8k",
  "size_bytes": 46530552,
  "merge_stats.json": {
    "inputs": [
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded.parts/fable5_helio_agentic",
        "samples": 3937,
        "tokens": 7115910
      },
      {
        "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260630_lfmchat_agentic_fable_grounded.parts/local_grounding_logs_docs",
        "samples": 6,
        "tokens": 8388
      }
    ],
    "samples": 3943,
    "tokens": 7124298,
    "avg_sample_len": 1806.8217093583567,
    "max_sample_len": 8192,
    "epochs": 1
  },
  "file_count": 9
}
```
