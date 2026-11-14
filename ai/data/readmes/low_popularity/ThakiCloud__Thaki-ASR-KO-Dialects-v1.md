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
tags:
- speech
- asr
- korean
- dialect
- qwen3-asr
- jeju
---

# Thaki-ASR-KO-Dialects-v1

**Qwen3-ASR-1.7B fine-tuned on five Korean regional dialects (Gangwon, Gyeongsang, Jeolla, Jeju, Chungcheong), with standard Korean kept intact.**
Pooled character error rate on sealed dialect test sets drops from 13.52% to **10.81%** (relative −20.1%); every region improves; Zeroth-Korean (standard read speech) moves from 3.83% to 3.66%.

🇰🇷 한국어 카드: [MODEL_CARD.ko.md](./MODEL_CARD.ko.md)

| | |
|---|---|
| Base | `Qwen/Qwen3-ASR-1.7B` (Apache-2.0) |
| Method | Full-parameter fine-tune including the audio encoder, FP32 master weights, 1 epoch |
| Training speech | 289.6 h of AI Hub Korean dialect speech (5 regions, ≤60 h each) + Zeroth-Korean train (19,233 utterances) |
| Release format | single checkpoint (bf16-loadable), weights + tokenizer/processor configs only |
| Evaluation | pre-registered gates (GD1 pooled dialect CER −15% with no regional regression, GD2 Zeroth ≤ base + 0.3 pp), both passed |
| License | Apache-2.0 for the weights; **no AI Hub audio or transcripts are included** (see §6) |

> ⚠️ This is a **research-gate release**, not a production-validated model. It was evaluated on clean, single-channel AI Hub recordings with a female-skewed speaker pool. Noisy or far-field audio, male speakers, children, and non-Korean languages were **not** evaluated (§5).

## 0. Quick start

The checkpoint is a drop-in replacement for `Qwen/Qwen3-ASR-1.7B`. Use the official `qwen-asr` package.

```bash
pip install -U qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "ThakiCloud/Thaki-ASR-KO-Dialects-v1",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    max_inference_batch_size=16,
    max_new_tokens=256,
)

# audio: a local path / URL to a 16 kHz mono WAV, or a (numpy array, sample_rate) tuple
results = model.transcribe(audio="jeju_sample.wav", language="Korean")
print(results[0].text)
```

Decoding used for every number on this card: greedy (`do_sample=False`), `language="Korean"` forced, `max_new_tokens=256`, bf16 inference on one H100. The model also accepts the base model's other 51 languages, but we did not evaluate them (§5).

Transcription conventions follow the training labels: AI Hub dialect transcripts (spoken form, no punctuation normalisation) and Zeroth-Korean (numbers written out in Korean, e.g. 이천 십 일 년). Expect Korean-numeral output more often than the base model.

## 1. What changed, and what did not

Numbers below are **our own measurements** of the base model and this checkpoint, same sealed sets, same decoding, same hardware (1× H100 NVL, dev cluster), 2 repetitions each (greedy decoding is deterministic here: both repetitions produced identical character-level output, so no spread is shown).

### 1.1 Dialect test sets (sealed before training)

| Region | n utts | Base CER | **v1 CER** | Rel. change |
|---|---|---|---|---|
| Gangwon (강원) | 300 | 10.62% | **8.29%** | −21.9% |
| Gyeongsang (경상) | 300 | 5.94% | **4.97%** | −16.4% |
| Jeolla (전라) | 300 | 13.43% | **11.94%** | −11.1% |
| Jeju (제주) | 300 | 31.55% | **23.62%** | −25.1% |
| Chungcheong (충청) | 195 | 8.51% | **6.63%** | −22.1% |
| **Pooled (1,395 utts / 25,332 ref chars)** | 1,395 | **13.52%** | **10.81%** | **−20.1%** |
| Utterance-weighted mean of the five regional CERs | 1,395 | 14.42% | 11.43% | −20.7% |

**How the pooled number is computed.** The pre-registered gate (GD1) defines the aggregate CER as *total substituted + deleted + inserted characters ÷ total reference characters* across the five regional sets (3,425 / 25,332 for the base, 2,738 / 25,332 for v1). This weights regions by their reference-character count, not by utterance count, which is why it differs from the utterance-weighted mean of the regional CERs shown in the last row. Both are reported; the gate was judged on the pooled figure.

Jeolla improved the least (−11.1%); it is the only region whose single-region improvement would not have met a 15% bar on its own. The gate as registered asks for a pooled −15% **and** no regional regression, which v1 meets.

### 1.2 Dialectal vs. standard-form utterances

Each test set was split by whether the AI Hub transcript marks the utterance as containing dialectal forms (`dialectal`) or not (`standard`). This separates *Jeju language* from *standard Korean spoken by Jeju residents*. Splits with fewer than 20 utterances were not evaluated; splits under n = 150 are reported but were **not** gate criteria.

| Split | n | Base CER | **v1 CER** | Rel. change |
|---|---|---|---|---|
| Jeju · dialectal (제주어) | 134 | 39.07% | **28.44%** | −27.2% |
| Jeju · standard | 166 | 24.15% | **18.88%** | −21.8% |
| Gangwon · dialectal | 63 | 11.71% | 10.69% | −8.7% |
| Gangwon · standard | 237 | 10.31% | **7.62%** | −26.1% |
| Gyeongsang · standard | 293 | 5.87% | **4.74%** | −19.2% |
| Jeolla · dialectal | 27 | 16.88% | 11.56% | −31.5% |
| Jeolla · standard | 273 | 13.04% | 11.98% | −8.1% |
| Chungcheong · dialectal | 51 | 11.66% | 8.33% | −28.6% |
| Chungcheong · standard | 144 | 7.43% | **6.05%** | −18.6% |

Read the small splits (Jeolla dialectal n = 27, Chungcheong dialectal n = 51, Gangwon dialectal n = 63) as direction only. One utterance in the Jeolla dialectal split is roughly 3.7 percentage points of its CER.

### 1.3 Standard Korean guardrail

| Set | n | Base CER | **v1 CER** | Gate |
|---|---|---|---|---|
| Zeroth-Korean test (sealed 200-utterance sample) | 200 | 3.83% | **3.66%** | ≤ 4.13% → pass |

The standard-Korean guardrail only says "did not get worse on read speech". It does not claim a general Korean ASR improvement.

### 1.4 Latency

Architecture and parameter count are unchanged from the base model, so throughput is the same. On the evaluation run (1× H100 NVL, bf16, batch 1): median latency 0.39–0.61 s per 3–8 s utterance, real-time factor 0.11–0.14.

## 2. Training data

| Source | Regions / split | Hours | Utterances | Speakers | Licence to us |
|---|---|---|---|---|---|
| AI-Hub **한국어 방언 발화(강원도)** (dataSetSn 118) | Gangwon | 49.6 | 47,790 | 171 | AI Hub terms |
| AI-Hub **한국어 방언 발화(경상도)** (dataSetSn 119) | Gyeongsang | 60.0 | 50,172 | 370 | AI Hub terms |
| AI-Hub **한국어 방언 발화(전라도)** (dataSetSn 120) | Jeolla | 60.0 | 49,499 | 334 | AI Hub terms |
| AI-Hub **한국어 방언 발화(제주도)** (dataSetSn 121) | Jeju | 60.0 | 68,101 | 530 | AI Hub terms |
| AI-Hub **한국어 방언 발화(충청도)** (dataSetSn 122) | Chungcheong | 60.0 | 40,342 | 177 | AI Hub terms |
| Zeroth-Korean (`Bingsu/zeroth-korean`, CC BY 4.0) | train split | — | 19,233 | — | CC BY 4.0 |

- Dialect hours were capped at 60 h per region (Gangwon has less available). Within a region, whole recording sessions were sampled so that test speakers never appear in training.
- **Leak filtering**: 0 training utterances share audio with any test set; 4,750 training utterances whose transcript exactly matched a test reference were dropped. Final training set: 273,217 utterances; 200 held-out utterances for training-time eval loss.
- **Speaker skew**: 78–89% of dialect training utterances per region are from female speakers (Gangwon 81%, Gyeongsang 86%, Jeolla 89%, Jeju 78%, Chungcheong 83%), and speakers in their twenties dominate. The sealed test sets have the same skew (Chungcheong test is 100% female). Male and older-speaker performance is therefore under-measured.
- The Zeroth-Korean **test** split and the five sealed dialect test sets were never used for training or model selection.

## 3. Training recipe

| | |
|---|---|
| Objective | Standard Qwen3-ASR SFT (`language Korean<asr_text>` prefix + transcript), audio encoder **not** frozen |
| Precision | FP32 master weights and optimizer (bf16 inference is fine) |
| Optimiser / schedule | AdamW, lr 2e-5, linear decay, 1 epoch |
| Batch | 4 per device × 32 gradient accumulation = 128 effective |
| Steps | 2,135 (one pass over 273,217 utterances) |
| Hardware / cost | 1× NVIDIA H100 NVL, 8.27 GPU-hours end to end (data staging included) |
| Held-out eval loss | 0.615 → 0.474 |
| Checkpointing | every 200 steps to object storage with hash verification; this release is the final step-2135 checkpoint |

An earlier run with the audio encoder frozen (same data, bf16) improved Jeju by only 9% relative, so for dialect adaptation the encoder update appears to matter. An earlier run with 10 h per region (full fine-tune) reached a pooled −11.2% and did not pass the gate; the 60 h cap did.

## 4. Evaluation protocol

- **Pre-registered gates** (frozen before training, with a self-test on earlier failed runs): GD1 pooled dialect CER relative change ≤ −15% **and** no region (n ≥ 150) worse than base; GD2 Zeroth test CER ≤ base + 0.3 pp. Verdict: **both passed**.
- Sealed sets: per region 300 utterances (Chungcheong 195) drawn from recording sessions excluded from training; Zeroth test 200 utterances sampled once and frozen.
- Scoring: character error rate after Unicode NFC normalisation, whitespace collapsing and punctuation removal; the same scorer was used for base and candidate. Numerals are **not** normalised in the headline numbers (a numeral-normalised CER is in the ledger and differs by < 0.1 pp).
- Two repetitions per set; greedy decoding produced identical outputs, so the measurement-noise band used by the gate was 0.

Raw per-utterance hypotheses and the gate verdict file are kept in our internal ledger; the numbers on this card are copied from it without rounding beyond two decimals.

## 5. Limitations and what we did not measure

- **Not production-validated.** Clean studio-style AI Hub audio only. No noise, far-field, telephone, or overlapping-speech evaluation.
- **Female and young speakers dominate** both training and test. Treat male, child and elderly-speaker accuracy as unknown.
- **Other languages were not evaluated.** The base model supports 52 languages. In a separate Korean-only fine-tune of the same base we observed Japanese CER nearly doubling, so do **not** assume multilingual ability is preserved here. Use the base model for non-Korean audio.
- **Jeolla gains are modest** (−11.1%) and the Jeolla dialectal split is tiny (n = 27).
- **Jeju remains hard**: 23.6% CER overall and 28.4% on dialectal utterances. This is a large improvement, not a solved problem.
- Transcription style follows AI Hub / Zeroth conventions (spoken forms, Korean numerals); downstream text normalisation may be needed.
- No timestamp / forced-alignment evaluation was done (the base model's aligner should still work, untested).

## 6. Data licensing and what is (not) in this repository

- This repository contains **model weights and configuration files only**. No AI Hub audio, transcripts, metadata, or derived data files are included, in line with the AI-Hub terms of use, which allow the data to be used for training AI models and prohibit providing the data, or simple edits of it, to unapproved third parties.
- Source attribution (required by the AI-Hub terms, which extend the requirement to derivative works): 이 모델은 한국지능정보사회진흥원(NIA)의 사업결과인 AI-Hub "한국어 방언 발화(강원도)", "한국어 방언 발화(경상도)", "한국어 방언 발화(전라도)", "한국어 방언 발화(제주도)", "한국어 방언 발화(충청도)" 데이터를 활용해 학습했습니다. *(This model was trained using the AI-Hub datasets "한국어 방언 발화" for Gangwon, Gyeongsang, Jeolla, Jeju and Chungcheong, which are results of a project of the National Information Society Agency (NIA), Korea.)*
- Zeroth-Korean is CC BY 4.0 (Lucas Jo, Wonkyum Lee; mirrored as `Bingsu/zeroth-korean`).
- Base model `Qwen/Qwen3-ASR-1.7B` is Apache-2.0. The fine-tuned weights are released under Apache-2.0.

## 7. Reproducibility

- Base checkpoint: `Qwen/Qwen3-ASR-1.7B` (Hugging Face, Apache-2.0).
- Training: official `qwen-asr` SFT recipe, hyperparameters in §3, `transformers 4.57.6`, `torch 2.9.0+cu130`, `flash-attn 2.8.3`.
- Evaluation: greedy decoding, `language="Korean"`, scorer as in §4. The sealed dialect test sets are AI Hub-derived and cannot be redistributed; the Zeroth test sample can be reconstructed from `Bingsu/zeroth-korean` test split (first 200 utterances after our deterministic ordering are listed in the ledger on request).
- File integrity: SHA-256 of every uploaded file was verified against the training job's manifest before and after upload (see the upload commit message / ledger).

## 8. Citation

```bibtex
@misc{thakicloud2026thakiasrdialects,
  title  = {Thaki-ASR-KO-Dialects-v1: Qwen3-ASR-1.7B fine-tuned on five Korean regional dialects},
  author = {ThakiCloud},
  year   = {2026},
  url    = {https://huggingface.co/ThakiCloud/Thaki-ASR-KO-Dialects-v1}
}
```

Base model: Qwen Team, *Qwen3-ASR Technical Report* (arXiv:2601.21337).
