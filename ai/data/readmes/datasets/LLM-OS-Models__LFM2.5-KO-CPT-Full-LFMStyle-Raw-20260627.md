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

# LFM2.5-KO-CPT-Full-LFMStyle-Raw-20260627

Full Korean CPT mix converted to LFM-style text JSONL, about 4B-token training source.

This dataset is part of the `LFM2.5-8B-A1B-KO-SFT` / Agentic SFT workflow.

- Main SFT model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-SFT
- CPT base model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-CPT-FULL
- Agentic follow-up model: https://huggingface.co/LLM-OS-Models/LFM2.5-8B-A1B-KO-Agentic-SFT
- SFT GitHub: https://github.com/gyunggyung/LFM25-KO-SFT
- CPT GitHub: https://github.com/gyunggyung/LFM25-KO-CPT

## Source Attribution

- Korean Wiki/general knowledge: `kowiki_raw_full_20260524`.
- Korean finance/accounting text and instruction data: `bcai_finance_kor_hrm_20260524`, `BCAI-Finance-Kor-1862K`.
- Korean legal raw/task/RAG/bar-answer sources: `korean_legal_raw_full_20260523`, `korean_legal_tasks_full_20260524`, `korean_admrule_precedent_raw_full_20260524`, `ko_legal_source_agent_sft_20260621`, `ko_legal_rag_agent_sft_round15_v2`, `current_law_bar_json_answer_sft_20260621`.
- Terminal/tool-use traces: `lfm25_terminal_toolbench_hrm_turns_v1`.

Additional public references:

- Liquid LFM base model: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B
- Liquid chat template docs: https://docs.liquid.ai/lfm/key-concepts/chat-template
- Liquid tool-use docs: https://docs.liquid.ai/lfm/key-concepts/tool-use
- Legalize-KR organization: https://github.com/legalize-kr
- KoTSQA v2.0: https://huggingface.co/datasets/etri-lirs/KoTSQA-v.2.0
- Korean dataset index reviewed for candidates: https://github.com/gyunggyung/LLM-Ko-Datasets

## Notes

- This is the full CPT source after LFM-style wrapping. It is intended for continued pretraining/mid-training, not final chat SFT.
- Legal-domain attribution includes the public Legalize-KR ecosystem and the Korean law source ecosystem documented in the model card.

## Summary

| field | value |
|---|---:|
| kind | `raw_lfm_chat_jsonl` |
| sample count | n/a |
| token count | n/a |
| max sequence / sample length | n/a |
| uploaded size bytes | 20539721507 |

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
/home/work/.data/lfm2_ko_cpt/datasets/ko_cpt_mix_full_lfmstyle_20260627.jsonl
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
  "path": "/home/work/.data/lfm2_ko_cpt/datasets/ko_cpt_mix_full_lfmstyle_20260627.jsonl",
  "size_bytes": 20539721507,
  "file_count": 1,
  "file_name": "ko_cpt_mix_full_lfmstyle_20260627.jsonl"
}
```
