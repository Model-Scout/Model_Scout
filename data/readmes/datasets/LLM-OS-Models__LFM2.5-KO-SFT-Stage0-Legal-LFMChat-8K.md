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

# LFM2.5-KO-SFT-Stage0-Legal-LFMChat-8K

Stage0 Korean legal warmup, LFM tokenizer, response-only SFT arrays.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Legal source-grounded SFT: `006_ko_legal_source_agent_sft_20260621.jsonl`.
- Legal RAG SFT: `007_ko_legal_rag_agent_sft_round15_v2.jsonl`.
- Bar-style JSON answer SFT: `008_current_law_bar_json_answer_sft_20260621.jsonl`.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- Warmup stage used to validate LFM tokenizer compatibility and response-only labels.
- Legal content is connected to Legalize-KR/law.go.kr style sources as documented in the CPT and SFT model cards.

## Summary

| field | value |
|---|---:|
| kind | `prepared_tokenized` |
| sample count | 8747 |
| token count | 35068923 |
| max sequence / sample length | 8192 |
| uploaded size bytes | 158463144 |

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
/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0_legal
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
  "path": "/home/work/.data/lfm2_ko_sft/prepared/lfm_chat/20260628_lfmchat_stage0_legal",
  "size_bytes": 158463144,
  "preprocess_stats.json": {
    "input_files": [
      "/home/work/.data/lfm2_ko_sft/prepared/jsonl_converted/legal_source_agent.sft.jsonl",
      "/home/work/.data/lfm2_ko_sft/prepared/jsonl_converted/legal_rag_round15.sft.jsonl",
      "/home/work/.data/lfm2_ko_sft/prepared/jsonl_converted/current_law_bar_json.sft.jsonl"
    ],
    "source_id": "legal_source_rag_bar_lfm_tokenizer",
    "rows": 8747,
    "kept_rows": 8747,
    "dropped_parse": 0,
    "dropped_empty_response": 0,
    "dropped_response_too_long": 0,
    "dedupe_dropped": 0,
    "truncated_rows": 1815,
    "max_original_len": 14052,
    "max_written_len": 8192,
    "target_tokens": 0,
    "max_seq_length": 8192,
    "tokenizer_vocab_size": 125017,
    "total_tokens": 35068923,
    "sample_count": 8747,
    "avg_sample_len": 4009.251514805076,
    "max_sample_len": 8192,
    "token_min": 10,
    "token_max": 124900,
    "max_token_id_seen": 124900
  },
  "file_count": 9
}
```
