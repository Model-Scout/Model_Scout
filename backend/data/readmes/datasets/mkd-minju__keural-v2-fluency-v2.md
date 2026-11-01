---
license: other
language:
- ko
- en
task_categories:
- text-generation
---

<div align="center">

# Keural-v2 Fluency (v2): A Curated Korean–English Conversational Corpus for LLM Fine-Tuning

</div>

<p align="center">
  <a href="#1-introduction">Introduction</a> |
  <a href="#2-dataset-composition">Dataset Composition</a> |
  <a href="#3-data-collection--processing-methodology">Methodology</a> |
  <a href="#4-license-and-attribution">License</a> |
  <a href="#5-known-limitations">Limitations</a>
</p>

**Status: Private staging — full §3 processing pipeline complete (dedup → PII removal → Korean-purity filter → length check → ratio measurement → train/val/test split → schema normalization → target-model encoding). Pending §4 quantitative/qualitative evaluation and second-party license audit before any public release.**

## 1. Introduction

Keural-v2 Fluency is the "Area 1" component of the Keural-v2 Korean SFT training corpus, purpose-built for [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) fine-tuning. It preserves and improves the model's raw *conversational fluency* — natural, idiomatic Korean without "translationese" artifacts — while guarding against degradation of existing English conversational ability during Korean-focused fine-tuning.

This **v2** release supersedes the earlier v1 staging snapshot: a full re-audit of the processing pipeline (2026-08-10) found and corrected several defects described in §3 and §5 below. The corpus now totals **290,636 examples** (235,213 Korean / 55,423 English, ≈80.9%/19.1%, close to the ~80/20 target), each pre-encoded into DeepSeek-V4-Flash-0731's native training text format and split into train/val/test.

## 2. Dataset Composition

Sources are unchanged from v1 (see the original collection-time README for full per-source license/provenance/revision tables: `mkd-chanwoo/keural-conversation-ko`, `IkJun1/korean-qa-dataset`, `coastral/korean-writing-style-instruct`, `CarrotAI/ko-instruction-dataset`, `beomi/KoAlpaca-RealQA` for Korean; `databricks/databricks-dolly-15k`, `OpenAssistant/oasst2`, Taskmaster-1/2/3, MultiWOZ 2.2 for English). What changed in v2 is the **processing**, not the source list.

## 3. Data Collection & Processing Methodology

Full §3 pipeline applied and re-verified end-to-end (2026-08-10):

1. **Deduplication**: exact + near-duplicate (MinHash/LSH) removal, both intra-source and cross-source. 300,000 → 295,121 rows.
2. **PII removal**: regex-based masking (email/phone/card/RRN/IP) — but a full-instance audit found the naive first pass had a **high false-positive rate specific to this category**: IP-pattern matches were almost entirely coding/networking Q&A content (ping examples, router default-IP guides, Flask/Docker configs — none real personal IPs), and several CARD matches were plain numeric content (binary/hex conversions) with no "card" context. These patterns were disabled/gated (IP disabled entirely for this category; CARD applied only when "card"/"credit" appears in the same turn; RRN disabled for Korean since all matches were corporate registration numbers, not personal IDs — a different legal category entirely). Genuine email/phone matches were retained.
3. **Korean purity filter**: `lang:"ko"` rows checked for unexplained Hanja contamination — 4,470 rows removed.
4. **Length/tokenizer check**: real DeepSeek-V4-Flash-0731 tokenizer used. 5 Korean rows were found to be a **degenerate generation-repetition bug** from `IkJun1/korean-qa-dataset` (the same sentence repeated verbatim until ~74,500 characters) and removed — not truncated, since truncation would leave the repetition pattern intact.
5. **Category/language ratio**: measured directly (not assumed) — 80.9% ko / 19.1% en, accepted as within tolerance of the ~80/20 target.
6. **Train/val/test split**: performed with cross-split deduplication (0 leakage confirmed).
7. **Schema normalization**: all heterogeneous collection-time formats (flat instruction/response fields, ShareGPT-style, OpenAI-style) unified into `schema/korean_sft_schema.md`'s common Turn structure.
8. **Target-model encoding**: DeepSeek's official `encode_messages()` implementation is **not available** in the public `deepseek-ai/DeepSeek-V4-Flash-0731` HF repo (no `chat_template`, no custom code). Encoding was reimplemented from the tokenizer's own `added_tokens` (confirmed real, registered tokens: `<｜User｜>`, `<｜Assistant｜>`, `<|EOT|>`; fluency has no reasoning/tool-call content so `<think>` is unused here). During this step, two further defects were caught and fixed: (a) `coastral`'s Vicuna-style `role: "gpt"` turns were not being mapped to `assistant` (encoder was raising on unrecognized roles rather than silently mis-encoding); (b) 1,912 Taskmaster1/2/3 dialogues ended on a trailing user utterance with no assistant reply to predict — these were trimmed to end on the last assistant turn, and 10 dialogues that had *no* assistant-preceding user turn at all (a loader artifact) were dropped entirely.

Post-encoding, the full token-length check was re-run across all 6 splits: 0 rows over the 32,768-token threshold.

## 4. License and Attribution

Unchanged from v1 — see the original README for the full per-source license table and the Gemma "Model Derivative" notice applicable to `keural-conversation-ko`-derived rows.

**"Keural-v2 Fluency" is a dataset produced by 주식회사 MKD (MKD Inc.).** The processing pipeline (deduplication, PII removal, filtering, splitting, and target-model encoding) described in §3 was performed by MKD Inc.; underlying source data retains the licenses of its original upstream publishers as listed above.

## 5. Known Limitations

- The DeepSeek-V4-Flash-0731 encoding used here is a **reimplementation**, not the vendor's official `encode_messages()` (which is not published). It was built from tokenizer-confirmed special tokens, but has not been validated against the vendor's actual reference implementation.
- Not yet evaluated per §4 (row/token distributions, diversity, contamination check against eval benchmarks) — pending before any public release.
- Represents 290,636 of the project's overall ~500,000-example target across six capability areas.
