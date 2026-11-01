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

# LFM2.5-KO-SFT-Stage2-KoTSQA-Train-LFMChat-Raw

KoTSQA v2 train split converted to LFM chat JSONL. Test split is held out for evaluation.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0.
- Only the train split is converted to LFM chat JSONL.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- The test split is intentionally held out for Korean evidence-QA evaluation.
- Used to strengthen Korean table/document-grounded QA and false-premise correction behavior.

## Summary

| field | value |
|---|---:|
| kind | `raw_lfm_chat_jsonl` |
| sample count | n/a |
| token count | n/a |
| max sequence / sample length | n/a |
| uploaded size bytes | 2086221 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_plus_kotsqa.jsonl
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage2_plus_kotsqa.jsonl",
  "size_bytes": 2086221,
  "jsonl_files": [
    {
      "name": "kotsqa_v2_train.jsonl",
      "size_bytes": 2085953
    }
  ],
  "file_count": 2
}
```
