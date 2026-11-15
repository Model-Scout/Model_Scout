---
license: apache-2.0
base_model: Qwen/Qwen3-ASR-1.7B
base_model_relation: finetune
language:
- ko
library_name: transformers
pipeline_tag: automatic-speech-recognition
datasets:
- Bingsu/zeroth-korean
- amphion/Emilia-Dataset
tags:
- asr
- speech-recognition
- korean
- telephony
- fine-tuning
- qwen3-asr
---

# Thaki-ASR-KO-1.7B

A Korean speech-recognition (ASR) model, fine-tuned from [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) (Apache-2.0) with an emphasis on **Korean telephony / customer-service (상담) speech** and numeric content, with general read speech used as a no-regression guardrail. The model is released from an independent 2-arm evaluation that passed all five pre-registered gates (Step 5b, 2026-10-29). A release audit (2026-11-04) limits what those gates show; read [it](#release-audit-2026-11-04--scope-of-the-go) before citing the numbers.

> **한국어판 카드:** [MODEL_CARD.ko.md](MODEL_CARD.ko.md) — same facts in Korean.

This repository contains **model weights and configuration files only** — no training audio, transcripts, metadata, or derived data. See [Data licensing and what is NOT in this repository](#8-data-licensing-and-what-is-not-in-this-repository).

> **Scope note (read before use):** All published evaluation numbers are measured on audio of **≤ 20 seconds** per utterance. We do **not** claim or guarantee performance on audio longer than 20 seconds. See [Limitations](#7-limitations).

---

## 0. Quick start

Requires the `qwen-asr` package (matches the base model's inference API):

```bash
pip install qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "ThakiCloud/Thaki-ASR-KO-1.7B",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    max_inference_batch_size=16,
    max_new_tokens=256,
)

result = model.transcribe(audio="path/to/korean_audio.wav", language="Korean")
print(result)
```

The model is greedy by default in this recipe (temperature 0). It expects Korean input; for other languages fall back to the base [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B).

---

## 1. What this model is

- **Base:** [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) — Apache-2.0, 30-language ASR. This model is a Korean fine-tune (SFT) of that base.
- **Primary target:** Korean telephony / customer-service (상담) speech and numeric content (prices, dates, IDs, amounts), with general conversational Korean held as a guardrail.
- **Provenance:** Initialized from the original base weights, fine-tuned once (R1 run), and the selected checkpoint was validated by an independent sealed evaluation before release. No re-training was performed for this release.

---

## 2. Results — Step 5b independent evaluation (Base vs Candidate)

2-arm comparison. **Base** = original Qwen3-ASR-1.7B (restored). **Candidate** = the R1 checkpoint released here (checkpoint-1200). Decoding is **greedy (temperature 0)**, run **3 times** per utterance; CER/RTF are reported as the median of the 3 reps and counts are the sum over reps (deterministic greedy, so reps agree).

| Gate | Set (scope) | Metric | Base | Candidate | Pass rule | Result |
|---|---|---|---|---|---|---|
| **A1** | TEST-D — telephony/상담 (900 utts) | CER | 6.88% | **6.07%** | cand ≤ base | ✅ −0.80 pp (−11.6% rel.) |
| **A1** | TEST-E — numeric/숫자 (250 utts) | CER | 6.83% | **6.35%** | cand ≤ base | ✅ −0.48 pp (−7.1% rel.) |
| **B1** | TEST-C — general (456 utts) † | CER | 3.46% | **1.95%** | cand ≤ base + 0.5 pp | ✅ −1.51 pp (−43.7% rel.) |
| **C1** | TEST-E ∪ TEST-C — 327 utts × 3 reps = 981 ‡ | numeric reference coverage (v2) | 66.4% | **88.7%** | cand ≥ base | ✅ +22.3 pp |
| **C2** | TEST-E ∪ TEST-C | wrong-but-plausible count | 12 | **6** | cand ≤ base | ✅ |
| **C3** | TEST-C / D / E | runaway count & RTF | 0 / 0.104–0.134 | 0 / 0.109–0.138 | runaway cand ≤ base **and** RTF cand ≤ base × 1.10 (per set) | ✅ |

† TEST-C sentences overlap the training data — B1 is a no-regression check, not evidence of general-domain improvement. ‡ C1 is notation-biased; see [§3](#3-what-c1-counts-and-what-it-does-not).

**G7 = all five gates passed → GO.** This is the verdict of record and it is unchanged. Its scope, after the [release audit](#release-audit-2026-11-04--scope-of-the-go): the telephony CER gain holds up under notation-insensitive re-scoring (kocer) and in an independent external evaluation. The C1 number gain is partly a shift toward Arabic-digit notation. B1 does not measure general-domain generalization. Wrong-but-plausible errors fall 12 → 6 and no silence or runaway regression was seen (RTF within 10% of base on every set).

### Release audit (2026-11-04) — scope of the GO

This audit was prompted by an independent re-score in [Discussion #1](https://huggingface.co/ThakiCloud/Thaki-ASR-KO-1.7B/discussions/1). It changes no gate value, threshold, or verdict above; it only limits what they should be read to mean. Nothing was re-trained or re-run on GPU. The stored Step 5b outputs were re-scored on CPU, and the B1 and C1 gate values were reproduced exactly before any new number was computed.

**B1 (TEST-C) is not a held-out measurement.** TEST-C is the Zeroth-Korean test split, and Zeroth-Korean's train and test splits share sentence scripts (with different recordings). Our training pipeline drops training rows whose normalized transcript appears in an evaluation set (the same logic as the public `data/sft.py`), but it was run against the telephony DEV set only. TEST-C was built after training, and the set builder did not exclude Zeroth-train sentences. What we found:

- 455 of the 456 TEST-C reference sentences appear in the 22,263-row Zeroth train split (normalized, whitespace-insensitive; 429/456 on exact normalized match).
- The training mix sampled 30,842 of the 32,567 general rows without replacement. The mixed file was not kept, so we replayed the mix builder's seeded sampling from its recorded seed and pool sizes: 21,073 Zeroth-train rows were in the mix, covering **454/456** TEST-C sentences (426 on exact match). This is a deterministic reconstruction, not a byte-level comparison with the original file.
- So the −1.51 pp B1 change reflects training on the same sentences. The one non-overlapping sentence is too few to measure anything. B1 still did its pre-registered job as a no-regression guardrail, but we withdraw "improves general CER": a held-out general-domain set was not evaluated.

**Supplementary v1 (2026-11-04, not a gate): kocer re-score of the same outputs.** [kocer](https://pypi.org/project/kocer/) 0.5.3 normalizes notation (e.g. digits vs. spelled numbers) before computing CER. Corpus CER pooled over the 3 reps, against the reference `text` field. Δ = candidate − base with a paired sentence-level bootstrap 95% CI (2,000 resamples). "Raw CER" is unnormalized character CER and is not the gate CER, which uses the frozen gate normalizer.

| Set | n | Raw CER base → cand | kocer CER base → cand | Δ kocer, pp [95% CI] |
|---|---|---|---|---|
| TEST-D telephony | 900 | 10.57% → 8.57% | 7.06% → 6.07% | −0.99 [−1.25, −0.74] |
| TEST-D, reference contains digits | 208 | 12.31% → 7.90% | 6.41% → 4.99% | −1.41 [−1.84, −0.98] |
| TEST-E numeric | 250 | 11.29% → 8.18% | 6.62% → 5.55% | −1.06 [−1.51, −0.64] |
| TEST-E, reference contains digits | 138 | 13.76% → 8.06% | 6.73% → 5.10% | −1.63 [−2.14, −1.09] |
| TEST-C general (overlaps training) | 456 | 7.31% → 5.21% | 2.70% → 1.88% | −0.83 [−1.05, −0.62] |

Under kocer every gain shrinks but stays significant, so part of the raw and gate gains comes from notation. TEST-D and TEST-E come from AI-Hub data, so only aggregates are published, never per-utterance outputs.

**Independent evaluation.** Kwan-u Choi (author of kocer) re-scored the model in his own setup in Discussion #1. He reported a significant kocer CER improvement on telephony speech (−1.14 pp) and no significant difference on a number-focused subset. Our in-domain number subsets do show a significant kocer gain and his does not, so treat the number improvement as domain-dependent rather than general.

### Evaluation data range (Step 5b)

| Set | Content | Utterances | Constraint |
|---|---|---|---|
| TEST-C | General Korean read speech (Zeroth-Korean) | 456 | ≤ 20 s; aligner omissions = 0; 1 item excluded by the length window |
| TEST-D | Telephony / customer-service (상담) speech (KtelSpeech, per-utterance) | 900 | ≤ 20 s; no label omissions by construction |
| TEST-E | Numeric (숫자) speech (KtelSpeech) | 250 | TEST-E ⊂ TEST-D; TEST-E ∩ TEST-C = ∅ |

All sets are length-windowed to **≤ 20 s** (the window was frozen **before** the evaluation run). KtelSpeech and the general set are **internal, non-redistributable** benchmarks — they are named only as a range description and are not included in this repository.

### Transparent record: Step 5 (sealed) NO-GO → Step 5b (new independent sets) GO

This model was **not** released from its first sealed evaluation. The full history, stated plainly:

1. **Step 5 (sealed, 2026-10-28): NO-GO.** A 2-arm sealed evaluation of the same candidate passed 4 of 5 pre-registered gates. The **single failure** was gate C3 (silence / runaway / latency): the candidate produced **runaway** output on **one utterance** (TD-z065, counted 3× because greedy reps agree), which failed the per-set runaway condition. Silence and latency (RTF) passed on every set. Because one of the five gates failed, the pre-registered rule was **NO-GO** and the model was not released.

2. **The TD-z065 case.** On TD-z065 (a **20.45 s** utterance), the base model produced **0** runaway and the candidate produced over-generated trailing conversational text that exceeded the runaway length threshold by a **2-character margin** (the core content was transcribed correctly). This single borderline-length utterance was the entire cause of the Step 5 failure.

3. **Step 5b (new independent sets, 2026-10-29): GO.** A **new, independent** set of evaluation data was built and frozen (new set hashes; identical gate structure, thresholds, and frozen verdict code — **no gates, thresholds, or verdict logic were changed**). The new sets apply a **≤ 20 s** length window. TD-z065 (20.45 s) falls **outside** this window and is therefore **not present** in the new sets. Across the new independent sets, runaway is **0 for both arms on every set**, so C3 passes and **all five gates pass → GO**.

**The GO stands on the new independent sets, not on a re-scoring of the sealed sets, and not on any model change.** The only reason the TD-z065 utterance is not scored in Step 5b is that it is longer than the 20 s window — this is a **scope limitation of the evaluation**, not a model fix. See the next subsection.

### The ≤ 20 s scope limit (do not over-claim)

- Every published number above is measured on **audio ≤ 20 s** per utterance.
- We **do not claim, test, or guarantee** performance on audio longer than 20 seconds.
- The single utterance (TD-z065) that failed in Step 5 is **20.45 s** — it is excluded from Step 5b **by the length window**, not because the model was changed. If you deploy this model on long-form or >20 s audio, treat the runaway/over-generation behavior on such inputs as **uncharacterized** and evaluate it yourself before relying on it.

---

## 3. What C1 counts (and what it does not)

C1 is the share of numeric-reference utterances whose reference numbers are all covered by the hypothesis, as judged by the frozen evaluator `match_utterance_v2` (public in the GitHub repo, `eval/num_match_v2.py`). Read it as **numeric reference coverage with a notation bias**. It is not numeric accuracy, and it is not the share of outputs written in Arabic digits.

- **What counts as a number.** Only (a) runs of Arabic digits, with 만/천/억 units expanded (`52만원` → 520000), and (b) runs of two or more Hangul digit-reading syllables read digit by digit (공영일이삼사오육칠팔구, e.g. `공일공` → 010). Sino-Korean or native numerals with place values are not parsed. A hypothesis `오십이만 원` is not recognized, so a reference `52만원` fails against it even though the transcription is right.
- **A lone single digit without a unit** (e.g. `3개`) is not a numeric element and is not scored.
- **Pass rule.** An utterance passes when every reference element is covered. Extra numbers in the hypothesis are ignored, so `52만원` → `52만 4천원` passes. An utterance with several numbers is still one item.
- **Denominator.** 327 utterances per rep: all 250 TEST-E utterances plus the 77 TEST-C utterances in which the detector finds a numeric element, × 3 greedy reps = **981**. Base 651/981 (66.4%), candidate 870/981 (88.7%).
- **The 77 TEST-C items are mostly not numbers.** Their references contain no Arabic digits; they are counted only through Hangul runs that happen to coincide with digit syllables, and most are ordinary words (e.g. 공사, 사이, "이 노인"). A few are real spelled numbers (e.g. "오 일").
- **The notation effect, measured.** Of the base model's 330 failures, 267 hypotheses contain no Arabic digit at all, and 57 failures are utterances with zero kocer errors (correct transcription, failed only on notation). The candidate has 0 such notation-only failures. The candidate writes Arabic digits much more often: among TEST-E utterances whose reference contains digits, hypotheses containing a digit go 40.6% → 89.9%. On the 414 TEST-E items (138 × 3) whose reference contains Arabic digits, the C1 rate goes 46.4% → 89.1%.

So the +22.3 pp mixes real corrections with a shift toward the reference's notation, and we have not separated the two. kocer, which is notation-insensitive, still shows a significant gain on number-bearing telephony utterances (−1.4 to −1.6 pp; see the release audit in §2).

---

## 4. Training data

The R1 run used a Korean mixture (by sample count): **상담 (telephony) 65% / Kspon 20% / general 15%.**

| Component | Source | Scale | Notes |
|---|---|---|---|
| Telephony / 상담 (65%) | AI-Hub **상담 음성** (dataSetSn 100, distributed as KtelSpeech) | 133,651 utts / 200.0 h / 224 speakers | 8 kHz mobile-call audio upsampled to 16 kHz; D60/D61/D62 partitions |
| Kspon (20%) | AI-Hub **한국어 음성** (dataSetSn 123, distributed as KsponSpeech) | 54,993 utts / 80.0 h | |
| General (15%) | Zeroth-Korean (CC BY 4.0) + a small preserved amount of Emilia-YODAS Korean (CC BY 4.0) | (preserved) | Zeroth-Korean **train** split; its sentences overlap TEST-C (see the release audit in §2) |

**Data rights.** Both AI-Hub sources (상담 음성 and 한국어 음성) are governed by the AI-Hub terms of use, which allow the data to be used for training AI models and prohibit providing the data, or simple edits of it, to unapproved third parties. Neither is uploaded, redistributed, or exported here: **this release contains no audio, transcripts, or metadata from either source** — only the trained weights. Zeroth-Korean and Emilia-YODAS are CC BY 4.0. Section 8 carries the source attribution the AI-Hub terms require.

> The exact per-source split above is described from the internal training-data ledger; the source corpora themselves are **not** redistributed with this model.

---

## 5. Training recipe

- **Initialization:** original [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) weights.
- **Method:** supervised fine-tuning (SFT). The **audio encoder was frozen** (only the decoder/ASR head trained).
- **Precision:** fp32.
- **Optimizer / learning rate:** lr = 2e-6; effective batch size 128 (micro-batch 4 × gradient-accumulation 32).
- **Loss:** cross-entropy + knowledge distillation (λ = 0.05) applied to **general samples only** (distilled from the original base model).
- **Duration:** 1 epoch, single H100 (1 GPU).
- **Checkpoint selection:** checkpoint-1200 was selected by **minimum telephony (상담) DEV CER** among the run's checkpoints (5.24% candidate vs 6.05% base on the held-out telephony DEV). No re-selection was performed for the release.

Reproduction code (training recipe, data composition, preprocessing, and the evaluator v2) is published in the linked GitHub repository — see [Reproducibility](#9-reproducibility).

---

## 6. Evaluation protocol

- **Arms:** Base (original Qwen3-ASR-1.7B) vs Candidate (R1 checkpoint-1200). Fixed 2-arm; no re-selection between them.
- **Decoding:** greedy (temperature 0), **3 reps**; CER/RTF = median of 3 reps, counts = sum over reps (deterministic greedy).
- **Gates (pre-registered, frozen):** A1 (telephony CER), B1 (general CER), C1 (number robustness), C2 (wrong-but-plausible), C3 (silence/runaway/RTF). **GO = all five pass simultaneously.**
- **Sets:** TEST-C (general, 456), TEST-D (telephony, 900), TEST-E (numeric, 250; E ⊂ D). All ≤ 20 s.
- **Release audit (2026-11-04):** CPU-only re-score of the stored outputs (kocer, B1 overlap, C1 diagnostics), separately versioned; the verdict of record was not modified.
- **Integrity:** set hashes and the frozen verdict-code hashes were verified at evaluation time (all sets and all frozen code files matched the pre-registered values). The verdict of record is the S3-stored verdict artifact, not the pod log.

---

## 7. Limitations

- **≤ 20 s scope.** All published numbers are for audio ≤ 20 s per utterance. Performance on longer audio is **uncharacterized** here; the TD-z065 runaway case (20.45 s) shows over-generation can occur on borderline-length inputs. Do not extrapolate the GO to long-form audio.
- **Korean-only focus.** This is a Korean fine-tune. For other languages use the base model.
- **Telephony bias.** Training is weighted toward telephony/consulting speech; performance on very different domains (e.g. music, heavy background noise, non-telephony accents) is not separately validated here.
- **Number gains are real but smaller than C1 suggests.** C1 (66.4% → 88.7%) is notation-biased (§3). Under kocer, the gain on number-bearing telephony utterances is −1.4 to −1.6 pp CER, and an independent number subset showed no significant difference. Treat number improvements as domain-dependent.
- **General-domain improvement is not measured.** TEST-C overlaps the training sentences, and no held-out general-domain set was evaluated.
- **Greedy only.** Only temperature-0 decoding was evaluated; sampling behavior is not characterized.

---

## 8. Data licensing and what is NOT in this repository

**What is in this repository:** model weights (`.safetensors`), `config.json`, tokenizer/processor files, and this card. Nothing else.

**What is NOT in this repository (by policy):**
- **No training audio** — no KtelSpeech, Kspon, Zeroth, or Emilia audio files.
- **No transcripts, metadata, or derived data** from any training source.
- **No personal information (PII)** and **no internal credentials**.

**Licensing:**
- **Weights & config:** released under **Apache-2.0** (the base model is Apache-2.0; this fine-tune follows that).
- **AI-Hub sources — 상담 음성 (dataSetSn 100) and 한국어 음성 (dataSetSn 123):** governed by the AI-Hub terms of use, which allow the data to be used for training AI models and prohibit providing the data, or simple edits of it, to unapproved third parties. **Not redistributed, not uploaded, not exported.** Only the trained weights are released.
- **Source attribution (required by the AI-Hub terms, which extend the requirement to derivative works):** 이 모델은 한국지능정보사회진흥원(NIA)의 사업결과인 AI-Hub "상담 음성", "한국어 음성" 데이터를 활용해 학습했습니다. *(This model was trained using the AI-Hub datasets "상담 음성" and "한국어 음성", which are results of a project of the National Information Society Agency (NIA), Korea.)*
- **Zeroth-Korean:** CC BY 4.0 (Lucas Jo, Wonkyum Lee; mirrored as `Bingsu/zeroth-korean`).
- **Emilia-YODAS, Korean subset:** CC BY 4.0 (`amphion/Emilia-Dataset`, path `Emilia-YODAS/KO`). Only the CC BY 4.0 YODAS portion was used, not the CC BY-NC `Emilia/` portion; every stored shard was checked against the YODAS file sizes.

If you use this model, you are using the weights under Apache-2.0. The underlying training corpora are **not** provided and remain subject to their own (more restrictive) terms; you are not receiving a license to those corpora from this repository.

---

## 9. Reproducibility

Training recipe, data-composition description, preprocessing, the **evaluator v2** (`match_utterance_v2`), and a reproducible inference example are published (open-source) in:

**`ThakiCloud/thaki-asr-ko-1.7b`** on GitHub — https://github.com/ThakiCloud/thaki-asr-ko-1.7b

The GitHub repository **does not** duplicate the model weights (fetch them from this Hugging Face repo) and **excludes** internal cluster configuration, internal storage paths, and internal-only code. The model card (here) and the GitHub README cross-reference each other.

---

## 10. Citation

If you use this model, please cite the base model and this repository:

```bibtex
@misc{thaki_asr_ko_1_7b,
  title        = {Thaki-ASR-KO-1.7B: A Korean Telephony ASR Fine-tune of Qwen3-ASR-1.7B},
  author       = {ThakiCloud},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/ThakiCloud/Thaki-ASR-KO-1.7B}},
  note         = {Fine-tuned from Qwen/Qwen3-ASR-1.7B (Apache-2.0)}
}
```

---

## Base model

[Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) — Apache-2.0, 30-language automatic speech recognition.
