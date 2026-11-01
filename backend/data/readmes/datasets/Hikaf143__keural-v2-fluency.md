---
license: other
language:
- ko
- en
task_categories:
- text-generation
---

<div align="center">

# Keural-v2 Fluency: A Curated Korean–English Conversational Corpus for LLM Fine-Tuning

</div>

<p align="center">
  <a href="#1-introduction">Introduction</a> |
  <a href="#2-dataset-composition">Dataset Composition</a> (<a href="#23-source-revisions">Revisions</a>) |
  <a href="#3-data-collection--processing-methodology">Methodology</a> |
  <a href="#4-license-and-attribution">License</a> |
  <a href="#5-known-limitations">Limitations</a>
</p>

**Status: Private staging — not yet cleared for public release (pending §4 evaluation and second-party license audit).**

## 1. Introduction

Keural-v2 Fluency is the "Area 1" component of the Keural-v2 Korean SFT training corpus, purpose-built for [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) fine-tuning. While the broader Keural-v2 program targets specialized capabilities such as tool-calling and chain-of-thought reasoning, this dataset addresses a distinct and easily-overlooked objective: preserving and improving the model's raw *conversational fluency* — the ability to produce natural, idiomatic Korean, without the "translationese" artifacts that plague machine-translated instruction data — while simultaneously guarding against degradation of the model's existing English conversational ability during Korean-focused fine-tuning.

To meet this goal without introducing the licensing and quality risks documented throughout this project's data-collection process (see §4 below), every candidate source was screened not only at the level of its top-level license tag, but down to its actual composition: several well-known, seemingly clean Korean instruction datasets were rejected after tracing their construction tables back to non-commercial, unlicensed, or machine-translated upstream components. The dataset below reflects only sources that survived this audit intact.

The corpus totals **300,000 examples**, split 80/20 between Korean (240,000) and English (60,000), matching the project's overall fluency-objective ratio.

## 2. Dataset Composition

### 2.1 Korean Slice (240,000 examples, 80% of Area 1)

<div align="center">

| Source | Examples | License | Provenance |
|:---|---:|:---:|:---|
| `mkd-chanwoo/keural-conversation-ko` (raw) | 141,671 | CC BY 4.0 | Generated end-to-end by Gemma-4-26B-A4B-it (open-weight); no external seed dataset |
| `IkJun1/korean-qa-dataset` | 47,115 | MIT | Undisclosed LLM |
| `coastral/korean-writing-style-instruct` | 27,313 | Apache-2.0 | Synthesized via the Glaive platform (generation model unconfirmed) |
| `CarrotAI/ko-instruction-dataset` | 6,435 | Apache-2.0 | WizardLM-2-8x22B (open-weight, Evol-Instruct) |
| `beomi/KoAlpaca-RealQA` | 17,466 | CC BY-SA 4.0 | Authentic user questions with GPT-4o-generated answers |

</div>

`jojo0217/korean_rlhf_dataset` was evaluated as a candidate primary source but excluded after its construction table revealed that 91% of its rows trace to non-commercially-licensed (Stanford Alpaca, CC BY-NC 4.0), unlicensed (KoAlpaca v1.1), or machine-translated (Dolly-ko, OpenAssistant-ko) upstream content — none of which is curable by downstream rewriting.

### 2.2 English Balance Slice (60,000 examples, 20% of Area 1)

<div align="center">

| Source | Examples | License | Provenance |
|:---|---:|:---:|:---|
| `databricks/databricks-dolly-15k` | 15,011 | CC BY-SA 3.0 | Human-written by Databricks employees; no generative AI involved |
| `OpenAssistant/oasst2` | 36,594 | Apache-2.0 | Human crowdsourced (`synthetic` field verified 0/128,575) |
| Taskmaster-1 / Taskmaster-2 / Taskmaster-3 / MultiWOZ 2.2 (combined) | 8,395 | CC BY 4.0 / Apache-2.0 | Zero LLM involvement — hand-written by crowdworkers and academic research teams (2019–2020), pre-dating usable chat LLMs entirely |

</div>

This slice was deliberately restricted to human-authored data. Given how much of the rest of the Keural-v2 corpus is necessarily LLM-synthesized, the English balance slice is held to a stricter standard specifically to avoid compounding synthetic-data risk in the one category whose only job is to preserve an already-solid baseline capability.

### 2.3 Source Revisions

Exact commit/revision pinned at download time (2026-08-06), for reproducibility and future re-verification:

<div align="center">

| Source | Revision |
|:---|:---|
| `mkd-chanwoo/keural-conversation-ko` | `fcb975654651d55ff1a642455d620045b6d3f741` |
| `IkJun1/korean-qa-dataset` | `e1f177a7497cf4e55e54d86101c6c522345441d2` |
| `coastral/korean-writing-style-instruct` | `9f31462314f07847534fd13f7406c330ab15d156` |
| `CarrotAI/ko-instruction-dataset` | `5c0e2c0180b50400e401dd0b296043f18fc6cb3f` |
| `beomi/KoAlpaca-RealQA` | `a7df38a0b2cc187b72b40330af81e7b9f28dd95b` |
| `databricks/databricks-dolly-15k` | `bdd27f4d94b9c1f951818a7da7fd7aeea5dbff1a` |
| `OpenAssistant/oasst2` | `179dd21fc55192153d94adb0e0ce8f69e222bf75` |
| Taskmaster-1 / 2 / 3, MultiWOZ 2.2 | Fetched directly from `github.com/google-research-datasets/Taskmaster` and `github.com/budzianowski/multiwoz` (`master` branch, 2026-08-06) — these are legacy loading-script-only HF repos with no data-bearing revision of their own, so the upstream GitHub source is the canonical reference |

</div>

## 3. Data Collection & Processing Methodology

1. Each source was downloaded from its canonical location and exact-match deduplicated internally on its primary text field.
2. Large, synthesis-heavy sources (`keural-conversation-ko`, `IkJun1/korean-qa-dataset`) were capped prior to pooling to prevent any single source from dominating the mix, preserving topical and stylistic diversity.
3. All Korean-slice sources were pooled and cross-source deduplicated, then randomly sampled (`seed=42`) down to the 240,000-example target.
4. `OpenAssistant/oasst2` conversations were reconstructed by walking each valid English, non-deleted assistant reply back through its `parent_id` ancestry (rather than treating messages as independent rows), preserving genuine multi-turn structure; threads were capped at 8 turns.
5. The English-slice supplementary sources (Taskmaster/MultiWOZ) were pooled with a per-source cap of 4,000, cross-deduplicated, and randomly sampled to close the exact gap remaining after Dolly and oasst2.
6. Every record retains a `_source` and `_license` field; share-alike sources additionally carry `_share_alike: true` for downstream compliance tracking.

Final-format encoding (e.g., DeepSeek-V4-Flash-0731's native `<｜User｜>`/`<｜Assistant｜>`/`<think>` scheme) has intentionally **not** been applied at this stage — all records remain in structured `role`/`content`-style fields so that the correct target-model encoding can be applied uniformly across all five Keural-v2 data areas once collection is complete.

## 4. License and Attribution

This is a mixed-license dataset. Each record carries its own `_source` and `_license` field; verify the applicable license before any commercial use of a given slice.

<div align="center">

| License | Sources |
|:---:|:---|
| CC BY 4.0 | `keural-conversation-ko`, Taskmaster-1, Taskmaster-2, Taskmaster-3 |
| MIT | `IkJun1/korean-qa-dataset` |
| Apache-2.0 | `coastral/korean-writing-style-instruct`, `CarrotAI/ko-instruction-dataset`, `OpenAssistant/oasst2`, MultiWOZ 2.2 |
| CC BY-SA 4.0 (share-alike) | `beomi/KoAlpaca-RealQA` |
| CC BY-SA 3.0 (share-alike) | `databricks/databricks-dolly-15k` |

</div>

**Share-alike notice.** Rows derived from `beomi/KoAlpaca-RealQA` and `databricks/databricks-dolly-15k` carry `_share_alike: true`. Any redistribution or relicensing of this slice must satisfy CC BY-SA's attribution and same-license-propagation terms.

**Gemma "Model Derivative" notice.** Rows derived from `keural-conversation-ko` — the largest single component of the Korean slice — were generated by Google's Gemma (`gemma-4-26B-A4B-it`). Under Section 3.1 of the Gemma Terms of Use, a model fine-tuned on Gemma-generated synthetic outputs is itself considered a Gemma "Model Derivative." **Anyone distributing a model fine-tuned on this dataset must**: (1) include a notice stating "Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms," and (2) incorporate the Gemma Prohibited Use Policy into that model's own terms of use. This obligation is purely a downstream distribution/notice requirement — Google claims no ownership rights over Gemma-generated Outputs, so the dataset itself carries no copyright encumbrance.

This dataset inherits the licenses of its 13 upstream sources as listed above (Apache-2.0 / MIT / CC BY 4.0 / CC BY-SA 3.0 / CC BY-SA 4.0), mixed and processed in accordance with each source's attribution and share-alike terms. **"Keural-v2 Fluency" is a dataset made by MKD.**

## 5. Known Limitations

- The generation models behind `IkJun1/korean-qa-dataset` and `coastral/korean-writing-style-instruct` are undisclosed by their original authors. This does not constitute a license violation (per the same disclosure standard already applied to `glaiveai/glaive-function-calling-v2` in Area 2 of this project), but independent native-speaker quality review is recommended before final release.
- The Taskmaster/MultiWOZ portion of the English slice consists of task-oriented (booking/reservation/inquiry) dialogue, a narrower register than Dolly/oasst2's open-domain conversation.
- This dataset represents 300,000 of the project's overall 500,000-example target across five capability areas.
- Target-model-specific chat-template encoding has not yet been applied (see §3); this happens in a unified pass across all five areas once collection is complete.



## 6. MKD Ownership Notice / 주식회사 MKD 소유권 고지

**"Keural-v2 Fluency"는 주식회사 MKD(MKD Inc.)가 제작한 데이터셋입니다.** 위 §3에서 설명한 수집 및 처리 작업(출처 심사, 중복 제거, 소스별 상한 설정, 교차 소스 샘플링, OpenAssistant 멀티턴 재구성)은 주식회사 MKD가 수행했으며, 원본 데이터는 위 §4에 명시된 각 원 저작자의 라이선스를 그대로 따릅니다.

**"Keural-v2 Fluency" is a dataset produced by MKD Inc. (주식회사 MKD).** The collection and processing work described in §3 above (source screening, deduplication, per-source capping, cross-source sampling, and OpenAssistant multi-turn reconstruction) was performed by MKD Inc.; underlying source data remains governed by the licenses of its original publishers as listed in §4.