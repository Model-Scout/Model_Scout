---
license: other
license_name: apache-2.0-and-mit
license_link: https://huggingface.co/leuconoe/whisper-acft-ko#license--attribution
base_model:
- openai/whisper-tiny
- openai/whisper-base
- openai/whisper-medium
- openai/whisper-large-v3-turbo
datasets:
- google/fleurs
language:
- ko
- en
tags:
- litert
- tflite
- whisper
- asr
- quantized
- korean
- acft
pipeline_tag: automatic-speech-recognition
---

# Whisper ACFT-KO — Korean audio-context fine-tuned short-window TFLite (LiteRT)

Korean **audio-context fine-tuned (ACFT-KO)** Whisper models, exported as fixed short-window TFLite (LiteRT) graphs with encode/decode-split signatures. Four model sizes (tiny / base / medium / large-v3-turbo), three window lengths each (5 s / 10 s / 30 s), all dynamic-range int8 quantized ("drq").

Trained and exported by the [LiteRT-LM-Unity](https://github.com/Leuconoe/LiteRT-LM-Unity) project for on-device Korean voice commands.

## What ACFT-KO is

Audio-context fine-tuning per the method of [futo-org/whisper-acft](https://github.com/futo-org/whisper-acft) (method citation): Whisper is fine-tuned to tolerate a shortened encoder audio context, so short clips can be transcribed without padding to 30 s — cutting encoder cost by up to ~6-12x for voice-command use. Stock Whisper is trained for the 30 s window, so simply truncating the audio context puts it out of distribution (short-Korean CER 1.07-24.9 across sizes at a 5 s context); ACFT restores usable output at the short context.

These weights are **not** futo's checkpoints — they were trained from the stock openai checkpoints ([whisper-tiny](https://huggingface.co/openai/whisper-tiny), [whisper-base](https://huggingface.co/openai/whisper-base), [whisper-medium](https://huggingface.co/openai/whisper-medium), [whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)) by this project with a Korean-focused data mix.

## Training

- **Data**: zeroth-korean ([OpenSLR SLR40](https://openslr.org/40/), CC-BY-4.0) 70 % + [google/fleurs](https://huggingface.co/datasets/google/fleurs) `en_us` (CC-BY-4.0) 30 %, with short-utterance augmentation (short clips oversampled/cropped to match the voice-command regime).
- **Objective**: MSE self-distillation on decoder hidden states — teacher = the same checkpoint at full 30 s context; student sees per-batch sampled audio contexts with a floor of n_audio_ctx = 250 (the fixed 5 s deployment window).
- lr 1e-6, early stopping on a Korean-short + FLEURS composite CER gate. All four models passed their training gates. **The Korean-short bucket of that gate is TTS-synthesized** — it ranks tiers correctly but is not an absolute quality measure, and passing it did not make every tier usable (see "Evaluation caveats & tier guidance").

## Files

Converter-time dynamic-range quantization (int8 weights, fp32 activations — `tf.lite.Optimize.DEFAULT`).

| File | Size | Window | Encode input | Vocab |
| --- | ---: | --- | --- | ---: |
| `whisper_tiny_acft_ko_5s_drq.tflite` | 59 MB | 5 s | `[1, 80, 500]` | 51865 |
| `whisper_tiny_acft_ko_10s_drq.tflite` | 59 MB | 10 s | `[1, 80, 1000]` | 51865 |
| `whisper_tiny_acft_ko_30s_drq.tflite` | 61 MB | 30 s | `[1, 80, 3000]` | 51865 |
| `whisper_base_acft_ko_5s_drq.tflite` | 101 MB | 5 s | `[1, 80, 500]` | 51865 |
| `whisper_base_acft_ko_10s_drq.tflite` | 101 MB | 10 s | `[1, 80, 1000]` | 51865 |
| `whisper_base_acft_ko_30s_drq.tflite` | 103 MB | 30 s | `[1, 80, 3000]` | 51865 |
| `whisper_medium_acft_ko_5s_drq.tflite` | 827 MB | 5 s | `[1, 80, 500]` | 51865 |
| `whisper_medium_acft_ko_10s_drq.tflite` | 828 MB | 10 s | `[1, 80, 1000]` | 51865 |
| `whisper_medium_acft_ko_30s_drq.tflite` | 832 MB | 30 s | `[1, 80, 3000]` | 51865 |
| `whisper_large_v3_turbo_acft_ko_5s_drq.tflite` | 883 MB | 5 s | `[1, 128, 500]` | 51866 |
| `whisper_large_v3_turbo_acft_ko_10s_drq.tflite` | 884 MB | 10 s | `[1, 128, 1000]` | 51866 |
| `whisper_large_v3_turbo_acft_ko_30s_drq.tflite` | 889 MB | 30 s | `[1, 128, 3000]` | 51866 |

Tokenizers are unchanged from the base models — use `tokenizer.json` from the corresponding openai checkpoint (tiny/base/medium: vocab 51865, 80 mel bins; large-v3-turbo: vocab 51866, **128 mel bins**, `<|transcribe|>` = 50360, `<|notimestamps|>` = 50364).

## REQUIRED integration note

These are **fixed short-window graphs**, not 30 s graphs. The encode signature input is `[1, n_mels, frames]` with frames = 500 / 1000 / 3000 for the 5 s / 10 s / 30 s files. The runtime must **size the mel window from the encode signature's input shape** (compute/pad the log-mel to exactly that frame count) instead of assuming 3000 frames. Also note the decode signature input order of these exports is `(mask, audio, tokens)` — opposite of the stock litert-community exports — so bind decode tensors by shape/name rather than position. Reference implementation: the take6 JNI bridge in [LiteRT-LM-Unity](https://github.com/Leuconoe/LiteRT-LM-Unity), which auto-detects 500/1000/3000-frame windows from the signature on one code path.

The decoder is a fixed-length full re-run per step (no KV cache), matching the litert-community whisper-tiny/base graph interface.

## ⚠️ Evaluation caveats & tier guidance — read before using the numbers below

A 2026-07-26 methodology audit (inference-only re-evaluation of the checkpoints, 7 checkpoints × 7 eval buckets) re-scored these models on **real human recordings** instead of the synthesized gate set. Three things you need to know:

**1. `tiny` is NOT recommended for Korean voice commands.** Real-recorded-command CER **0.896**; on device it got **1/4 commands exact** and was rejected for deployment. The published gate number for tiny (0.457) reads as "workable small tier" and it is not one. Root cause: this tier was distilled from the **stock** `openai/whisper-tiny` checkpoint, so it is effectively an English model with fragile Korean — its real-recorded **English** CER is 0.031 (the best in the whole lineup) against 0.896 on Korean commands. Use `tiny` only for English/near-English short-window work, or pick **base** (fast path) / **large-v3-turbo** (accuracy path) for Korean commands.

**2. The training gate is a TTS-synthesized bucket. It ranks models correctly; it does not give absolute quality.** The gate is 40 edge-tts synthesized short-command clips (0.46–1.43 s). Against the real recordings its **ranking is validated** — Spearman ρ = **1.000**, Pearson r = 0.992 across 7 checkpoints — so model-to-model comparisons made with it are trustworthy. Its **absolute level is not calibrated**: for a strong un-finetuned base it is ~2.8× harsher than real audio, and for this tiny tier it is *optimistic* (TTS 0.728 vs real 0.896 when both are measured at full context). Do not read a gate CER as an "is this shippable" threshold.

**3. Punctuation sensitivity — the gate references average 3.6 characters.** On such short references a single trailing period is **+0.25 to +0.50 CER**. In the audited comparisons, **33–79 % of the measured CER "regression" between checkpoints was trailing punctuation alone**, and a typical voice-command matcher (including the reference implementation's) ignores punctuation and spacing entirely. Treat any absolute CER from a short-command bucket as an upper bound on product-relevant error, and score punctuation-stripped as well.

Context note for honesty about the tiny numbers: the published **0.457** was measured at the 5 s deployment context on 24 of the 40 gate clips, while the audit re-measured the same checkpoint at full 1500-frame context (TTS-40 **0.728**, real recorded commands **0.896**, real spontaneous short Korean **0.937**). So 0.457 → 0.896 is *not* a like-for-like delta — part of the gap is the context/subset difference. What is unambiguous is that every measurement of this tier on **real** Korean audio (either context, desktop or device) lands outside the range we would deploy for Korean voice commands. Only the tiny tier was re-measured on real recordings by the audit; base / medium / large-v3-turbo rest on their device results below and are unaffected by this correction.

## Validation

### Training gate — TTS-synthesized short-command eval (desktop, 5 s context) — **ranking-valid, not an absolute quality number**

Eval bucket = a 40-clip **edge-tts synthesized** short-command holdout (0.46–1.43 s, mean reference 3.6 characters); the gate scored 24 of the 40 clips (per-bucket SEM ≈ 0.05). CER vs punctuation-normalized references, greedy decode. "Stock" = the unmodified openai checkpoint evaluated at the same truncated 5 s audio context. Read the columns as an **ordering** of the tiers, not as expected real-world CER (see caveats above):

| Model @ 5 s ctx | Short-Korean CER, TTS gate (stock → ACFT-KO) | FLEURS ko CER | FLEURS en CER |
| --- | --- | --- | --- |
| tiny | 1.071 → **0.457** | 0.803 → 0.218 | 2.540 → 0.066 |
| base | 1.790 → **0.305** | 0.349 → 0.152 | 1.399 → 0.048 |
| medium | 1.194 → **0.208** | 0.495 → 0.090 | 2.006 → 0.033 |
| large-v3-turbo | 24.863 → **0.182** | 0.111 → 0.065 | 0.389 → 0.030 |

### The same tiers against real audio

"Real-recorded command CER" = 2026-07-26 audit, checkpoint at full context on human recordings of the target commands. "Device" = these 5 s TFLite exports on a Snapdragon 865 (five device test cycles). Where the audit did not measure a tier, the device column is the real-audio evidence for it:

| Tier | TTS gate CER (ranking) | Real-recorded command CER | Device (5 s export) | Guidance |
| --- | ---: | ---: | --- | --- |
| tiny | 0.457 | **0.896** | **1/4 exact — rejected** | **not recommended for Korean voice commands** |
| base | 0.305 | not measured | 4/5 exact, 0.7–0.8 s E2E | recommended default (fast path) |
| medium | 0.208 | not measured | 4/5 exact (`음량 증가` → `음향증가`) | no deployment role of its own |
| large-v3-turbo | 0.182 | not measured | **5/5 exact incl. the quiet take** | recommended accuracy path |

### On device (Snapdragon 865, arm64 CPU, LiteRT, fresh process incl. model compile)

Korean voice-command clips + one 3.8 s Korean report sentence:

| Variant | Command clips exact | E2E per command clip | Note |
| --- | --- | --- | --- |
| base 5s | **all normal-volume commands exact** (4/5; miss = very quiet take) | **0.7–0.8 s** | recommended default voice-command tier; ~3.5x faster than stock base-30s i8 on the same device |
| large-v3-turbo 5s | **5/5 exact incl. the very quiet take** | ~4.0 s cold / ~1.9 s warm | the only model across five device test cycles to read every clip; keeps digits (`2025년`) |
| medium 5s | 4/5 (`음량 증가` → `음향증가` flip on device) | 4.8–5.3 s | slower and less accurate than turbo-5s on device — no deployment role of its own |
| tiny 5s | 1/4 — **not recommended** | ~0.5 s | model-capacity failure, same as stock tiny; independently confirmed off-device (real-recorded-command CER 0.896) |

Desktop rebench of the exports (7-clip Korean/English matrix): medium-5s and turbo-5s/10s all-Korean-exact including the quiet take; per-window mean CER medium 0.039, turbo 0.031 (best of the queue).

## Caveats

- The 5 s graph hard-truncates longer audio — use the 10 s/30 s variants for dictation/longer clips.
- **tiny is NOT recommended for Korean voice commands** — real-recorded-command CER **0.896**, device **1/4 exact** (rejected for deployment). Its TTS gate number (0.457) overstates its Korean ability; it was distilled from the stock English-leaning checkpoint (real-recorded English CER 0.031). Published for completeness / English-leaning small targets. Use base (fast path) or large-v3-turbo (accuracy path) for Korean.
- **The training-gate CERs are TTS-synthesized and ranking-valid only** — see "Evaluation caveats & tier guidance" above. Never quote them as absolute Korean quality, and note that on ~3.6-character references a single trailing period is +0.25–0.50 CER while most command matchers ignore punctuation.
- Sub-1.2 s very-quiet clips remain AGC-dependent (capture-side loudness normalization recommended) on the smaller models; large-v3-turbo-5s handles the quiet gate take.
- 10 s/30 s medium variants regress one command clip (`음량` → `음향`); 30 s turbo drops one word on one clip vs its 5 s/10 s windows. Pick the window that matches your audio length rather than defaulting to 30 s.

## License / attribution

- **tiny / base / medium** files: **Apache-2.0** (matching the upstream openai/whisper-tiny/base/medium releases).
- **large-v3-turbo** files: **MIT** (matching upstream openai/whisper-large-v3-turbo).
- Method: [futo-org/whisper-acft](https://github.com/futo-org/whisper-acft) (audio-context fine-tuning).
- Training data attribution:
  - Zeroth-Korean corpus (Lucas Jo & Wonkyum Lee, Atlas Guide) — [OpenSLR SLR40](https://openslr.org/40/), CC-BY-4.0.
  - FLEURS (Google) — [google/fleurs](https://huggingface.co/datasets/google/fleurs), CC-BY-4.0.

Produced by [LiteRT-LM-Unity](https://github.com/Leuconoe/LiteRT-LM-Unity).
