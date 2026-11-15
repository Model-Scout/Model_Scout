---
license: other
license_name: funasr-model-license
license_link: https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE
base_model:
- FunAudioLLM/SenseVoiceSmall
datasets:
- Bingsu/zeroth-korean
- google/fleurs
language:
- ko
- en
tags:
- litert
- tflite
- sensevoice
- asr
- quantized
- korean
- xnnpack
- fine-tuned
pipeline_tag: automatic-speech-recognition
---

# SenseVoice-Small Korean (Zeroth fine-tune) — fixed-shape LiteRT (TFLite) buckets, int8

[FunAudioLLM/SenseVoiceSmall](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)
(~234 M params, non-autoregressive SAN-M encoder + CTC), fine-tuned for one epoch on
Zeroth-Korean with an English share kept in the mix, then converted to LiteRT exactly like
[litert-community/SenseVoiceSmall](https://huggingface.co/litert-community/SenseVoiceSmall):
same buckets, same quantization, same tensor contract — it is a drop-in replacement.

**Read the comparison before choosing it.** The fine-tune is a trade, not a strict upgrade:

- **Better than stock:** short commands recorded in field noise (CER 0.269 → 0.222),
  the TTS short-command gate (0.204 → 0.185), FLEURS Korean (0.068 → 0.066) and FLEURS
  English (0.046 → 0.033).
- **Worse than stock:** quiet-room real recordings — **stock gets 12 / 13 exact, this model
  11 / 13** (CER 0.006 → 0.011). Over all 22 real recordings stock has **17 exact vs 16**;
  the lower pooled CER here (0.097 vs 0.114) comes from partial fixes on noisy clips that
  still do not become exact.
- If your audio is mostly quiet-room commands, use the stock conversion.

## Training

| | |
| --- | --- |
| Init | `FunAudioLLM/SenseVoiceSmall` (stock weights) |
| Korean | Zeroth-Korean train (OpenSLR 40, via `Bingsu/zeroth-korean`): 95 % = 21,150 utts / 49.1 h, `<\|ko\|>`, `<\|woitn\|>` |
| English | FLEURS `en_us` train: 2,602 utts / 7.5 h (all of it, ~11 % of the mix), `<\|en\|>`, `<\|withitn\|>` — forgetting guard |
| Dev | the other 5 % of Zeroth train: 1,113 utts / 2.6 h |
| Recipe | FunASR `train_ds.py` (the SenseVoice `finetune.sh` recipe), single GPU, full fine-tune |
| Optimizer | AdamW, lr **1e-5**, `warmuplr` with 500 warm-up steps, grad-clip 5, SpecAug as in the base config |
| Batch | token batching, 8,000 fbank frames (≈ 80 s of audio) per step, 2,690 steps / epoch |
| Length | utterances longer than ~20 s dropped by the loader (`max_source_length` 2000 frames) |
| Run | 2 epochs, checkpoints every half epoch; **released: end of epoch 1** (2,690 steps, ~18 min on one shared 24 GB GPU) |

Checkpoint selection: each half-epoch checkpoint was scored on the real recordings first
(quiet + noise, pooled CER), then FLEURS-ko. **Zeroth test was never used for selection**
(see caveats). FunASR's own "best" pick is unusable here — it ranks by an accuracy that this
CTC-only model reports as 0.

## Files

| File | Size | Window | `speech` input | Note |
| --- | ---: | --- | --- | --- |
| `sensevoice_small_3s_w8.tflite` / `_i8` | 231 MB | 3 s | `[1, 560, 50]` | short commands |
| `sensevoice_small_5s_w8.tflite` / `_i8` | 231 MB | 5 s | `[1, 560, 84]` | **voice commands, recommended** |
| `sensevoice_small_10s_w8.tflite` / `_i8` | 231 MB | 10 s | `[1, 560, 167]` | sentences |
| `sensevoice_small_30s_w8.tflite` / `_i8` | 231 MB | 30 s | `[1, 560, 500]` | dictation |
| `am.mvn` | 11 KB | | | CMVN (AddShift + Rescale, 560 each) — unchanged from upstream |
| `chn_jpn_yue_eng_ko_spectok.bpe.model` | 0.4 MB | | | SentencePiece, 25055 pieces — unchanged |
| `tokens.txt` | 0.3 MB | | | `id<TAB>piece`, same vocab, for runtimes without SentencePiece |
| `config.yaml` | | | | upstream config (front-end parameters), byte-identical |
| `SHA256SUMS` | | | | |

`w8` = `weight_only_wi8_afp32` (activations fp32), `i8` = `dynamic_wi8_afp32` (activations
quantized per call — faster, slightly worse in noise). Load only the bucket(s) you need —
every graph carries the full weights.

## REQUIRED integration notes (tensor contract)

Identical to the stock conversion. Bind inputs **by name** (signature `serving_default`;
the converter orders them alphabetically).

| Tensor | Shape | Type | Value |
| --- | --- | --- | --- |
| `speech` | `[1, 560, N]` | f32 | LFR+CMVN features, **feature-major** (transpose of the usual `[T, 560]`), zero-padded to N |
| `speech_lengths` | `[1]` | i32 | true number of LFR frames (≤ N) |
| `language` | `[1]` | i32 | query id: auto 0, zh 3, en 4, yue 7, ja 11, **ko 12**, nospeech 13 |
| `textnorm` | `[1]` | i32 | `withitn` 14 (punctuation + digits), `woitn` 15 |
| `ctc_logits` (out) | `[1, N+4, 25055]` | f32 | keep the first `speech_lengths + 4` rows |
| `encoder_out_lens` (out) | `[1]` | i32 | = `speech_lengths + 4` |

Padding is masked, not heard: pad the features of a shorter clip with zeros up to the bucket
and feed the true length. Feeding padded *audio* without the length wrecks the result.

Front end (must match exactly — this is funasr `WavFrontend`):

1. 16 kHz mono, waveform × 32768.
2. Kaldi fbank (`torchaudio.compliance.kaldi.fbank`): 80 mel bins, 25 ms window / 10 ms
   shift, Hamming, `snip_edges=True`, `energy_floor=0`, **dither 0** (funasr defaults to 1.0,
   which makes runs non-deterministic); Kaldi defaults otherwise (pre-emphasis 0.97, DC removal).
3. LFR m=7, n=6: prepend 3 copies of the first frame, stack 7 frames every 6, pad the tail
   with the last frame (→ 560-dim, 60 ms per frame, `ceil(T/6)` frames).
4. CMVN from `am.mvn`: `(x + shift) * scale`.

Decode: greedy CTC — argmax per row, collapse repeats, drop id 0 (blank), map ids through
`tokens.txt` (`▁` = space). The first four emitted tokens are tags
(`<|ko|>` `<|NEUTRAL|>` `<|Speech|>` `<|woitn|>`); strip `<|…|>`.

## ⚠️ Evaluation caveats — read before using the numbers

- **Zeroth test is not a held-out measure for this model.** Zeroth-Korean is speaker-disjoint
  but not sentence-disjoint: 456 of the 457 test sentences also occur in train, read by other
  speakers. This model trained on Zeroth train, so its Zeroth test CER is optimistic. It is
  reported, never used for selection.
- `gate40` is a 40-clip **TTS-synthesized** Korean short-command holdout. It is valid for
  **ranking only** (Spearman ρ = 1.00 against real recordings) and runs ~2.8× harsher than
  real audio in absolute CER.
- The real-recording sets are small: 13 quiet-room + 9 field-noise clips. One clip is
  8 (quiet) / 11 (noise) points of exact-match rate; read a one-clip difference as noise-level.
- References average 3.6 characters: one wrong syllable is CER 0.25–0.33.
- CER = Levenshtein on the string with spaces removed and punctuation stripped (what a
  command matcher sees), `woitn`, language forced to `ko` (FLEURS-en: forced to `en`).
- Every number below: dither 0, desktop x86-64 CPU, same scorer for every model.

## Comparison — PyTorch (funasr), all checkpoints

CER · exact count. **Bold** = released.

| Model | gate40 (40, TTS) | real quiet (13) | real noise (9) | real exact (22) | FLEURS-ko (64) | FLEURS-en (64) | Zeroth test (457, leaky) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| stock SenseVoiceSmall | 0.204 · 20 | **0.006 · 12** | 0.269 · 5 | **17** | 0.068 · 22 | 0.046 · 26 | 0.023 · 257 |
| lr 1e-5, 0.5 epoch | 0.204 · 20 | 0.011 · 11 | 0.222 · 5 | 16 | 0.068 · 21 | 0.035 · 26 | 0.022 · 261 |
| **lr 1e-5, 1.0 epoch** | **0.185 · 21** | **0.011 · 11** | **0.222 · 5** | **16** | **0.066 · 23** | **0.033 · 26** | **0.022 · 263** |
| lr 1e-5, 1.5 epochs | 0.192 · 20 | 0.011 · 11 | 0.241 · 5 | 16 | 0.067 · 23 | 0.032 · 27 | 0.021 · 265 |
| lr 1e-5, 2.0 epochs | 0.185 · 21 | 0.011 · 11 | 0.241 · 5 | 16 | 0.065 · 23 | 0.033 · 27 | 0.021 · 267 |
| lr 5e-5, 1 epoch | 0.183 · 23 | 0.011 · 11 | 0.370 · 4 | 15 | 0.070 · 20 | 0.032 · 28 | 0.020 · 269 |
| lr 5e-5, 2 epochs | 0.202 · 20 | 0.020 · 10 | 0.444 · 4 | 14 | 0.073 · 19 | 0.033 · 29 | 0.018 · 280 |
| lr 5e-5, 3 epochs | 0.179 · 21 | 0.020 · 10 | 0.333 · 4 | 14 | 0.077 · 20 | 0.032 · 29 | 0.018 · 299 |
| lr 5e-5, 4 epochs | 0.207 · 18 | 0.020 · 10 | 0.352 · 4 | 14 | 0.076 · 19 | 0.033 · 29 | 0.016 · 303 |

Pooled real-recording CER (22 clips): stock 0.114, released 0.097.

What the table says:

- **The higher learning rate drifts.** At 5e-5 the model moves toward read-speech sentences:
  Zeroth keeps improving (that set is leaky) while noisy real commands and FLEURS-ko get worse
  every epoch. At 1e-5 the real-recording numbers peak at one epoch — field-noise CER rises
  again at 1.5 and 2.0 epochs (0.222 → 0.241) — so epoch 1 is released.
- **Where stock wins, specifically:** the quiet-room clip that regresses is a 7 s sentence that
  loses syllables (`검토 중입니다` → `검토 입니다`); in noise, `음성 명령` comes out
  `운성명` (stock: `운성 명령`). Where the fine-tune wins: `볼륨 업` in noise
  (stock `거거볼륨 맛`, fine-tune `볼륨 맛`), `화면 꺼줘` and `이륙` on the TTS gate.
- English did not collapse; it improved, because FLEURS-en was in the mix.

## Validation of the conversion (desktop, Windows x86-64 CPU, LiteRT 2.1.6, XNNPACK, 4 threads)

| Set | n | PyTorch (funasr) | tflite fp32 | **w8** | i8 |
| --- | ---: | ---: | ---: | ---: | ---: |
| gate40 (TTS, ranking only) | 40 | 0.185 · 21 | 0.185 · 21 | **0.179 · 22** | 0.198 · 21 |
| real commands, quiet room | 13 | 0.011 · 11 | 0.011 · 11 | **0.011 · 11** | 0.011 · 11 |
| real commands, field noise | 9 | 0.222 · 5 | 0.222 · 5 | **0.222 · 5** | 0.241 · 5 |
| FLEURS ko dev | 64 | 0.066 · 23 | 0.066 · 23 | **0.066 · 21** | 0.066 · 23 |
| FLEURS en dev | 64 | 0.033 · 26 | 0.033 · 26 | **0.034 · 25** | 0.035 · 26 |
| Zeroth-Korean test (leaky) | 457 | 0.022 · 263 | 0.022 · 263 | 0.022 · 263 | 0.022 · 259 |

Stock conversion on the same protocol, for reference (fp32 / w8 / i8): real quiet 0.006 · 12
on all three; real noise 0.269 · 5 / 0.269 · 5 / 0.333 · 5; gate40 0.204 · 20 on all three.

- **Conversion parity**: fp32 tflite vs onnxruntime on the same features — max |Δlogit|
  3.3e-4 on the real recordings, 3.8e-3 on gate40, CTC argmax agreement 100 %. Against the
  PyTorch reference the fp32 tflite transcripts are **identical on all 647 clips**
  (w8: 605 / 647, i8: 578 / 647 — quantization flips borderline tokens, the table shows the cost).

Invoke latency per window (model only, p50; same graph shapes as the stock conversion, so
any difference from the stock card is machine load, not the model):

| Window | fp32 | w8 | i8 |
| --- | ---: | ---: | ---: |
| 3 s | 95 ms | 116 ms | 66 ms |
| 5 s | 109 ms | 137 ms | 83 ms |
| 10 s | 188 ms | 181 ms | 149 ms |
| 30 s | 821 ms | 782 ms | 560 ms |

XNNPACK delegated on every graph. Not yet measured on an Android device.

## Caveats

- One epoch on read speech is a mild domain shift: it helps noisy and sentence-style audio and
  costs a little on clean short commands. Evaluate on your own recordings before switching.
- Field noise is still the weak spot (5 / 9 exact, same as stock).
- Language forcing is soft: a few 1-syllable clips come out in kana even with `ko`, as with stock.

## License / attribution

Weights: fine-tuned from FunAudioLLM SenseVoiceSmall, under the
[FunASR model license](https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE).
Training data: [Zeroth-Korean](https://www.openslr.org/40/) (CC BY 4.0) and
[FLEURS](https://huggingface.co/datasets/google/fleurs) (CC BY 4.0).
Paper: [FunAudioLLM, arXiv 2407.04051](https://arxiv.org/abs/2407.04051).
