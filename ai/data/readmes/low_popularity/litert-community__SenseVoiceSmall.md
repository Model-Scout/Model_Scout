---
license: other
license_name: funasr-model-license
license_link: https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE
base_model:
- FunAudioLLM/SenseVoiceSmall
language:
- ko
- en
- zh
- ja
- yue
tags:
- litert
- tflite
- sensevoice
- asr
- quantized
- korean
- xnnpack
pipeline_tag: automatic-speech-recognition
---

# SenseVoice-Small — fixed-shape LiteRT (TFLite) buckets, int8

[FunAudioLLM/SenseVoiceSmall](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)
(~234 M params, non-autoregressive SAN-M encoder + CTC) converted to LiteRT for
on-device use, unchanged weights. One forward pass per utterance — no decoder loop.

## What is different from the upstream ONNX

- **Static shapes, one graph per window** (3 / 5 / 10 / 30 s). A dynamic-shape graph keeps
  the XNNPACK delegate from attaching on LiteRT; these graphs run 10× (fp32) to 25× (i8)
  faster with XNNPACK than on the built-in kernels.
- **Padding is masked, not heard.** `speech_lengths` stays a graph input: pad the features
  of a shorter clip with zeros up to the bucket and feed the true length. Measured: padded +
  true length is bit-identical to the unpadded graph (max |Δlogit| 0.0000). Feeding padded
  *audio* without the length instead wrecks it (real-command CER 0.009 → 0.44 at a 5 s pad).
- **Weights int8.** `w8` = `weight_only_wi8_afp32` (activations fp32), `i8` =
  `dynamic_wi8_afp32` (activations quantized per call — faster, slightly worse in noise).

## Files

| File | Size | Window | `speech` input | Note |
| --- | ---: | --- | --- | --- |
| `sensevoice_small_3s_w8.tflite` / `_i8` | 231 MB | 3 s | `[1, 560, 50]` | short commands |
| `sensevoice_small_5s_w8.tflite` / `_i8` | 231 MB | 5 s | `[1, 560, 84]` | **voice commands, recommended** |
| `sensevoice_small_10s_w8.tflite` / `_i8` | 231 MB | 10 s | `[1, 560, 167]` | sentences |
| `sensevoice_small_30s_w8.tflite` / `_i8` | 231 MB | 30 s | `[1, 560, 500]` | dictation |
| `am.mvn` | 11 KB | | | CMVN (AddShift + Rescale, 560 each) |
| `chn_jpn_yue_eng_ko_spectok.bpe.model` | 0.4 MB | | | SentencePiece, 25055 pieces |
| `tokens.txt` | 0.3 MB | | | `id<TAB>piece`, same vocab, for runtimes without SentencePiece |
| `config.yaml` | | | | upstream config (front-end parameters) |
| `SHA256SUMS` | | | | |

Load only the bucket(s) you need — every graph carries the full weights.

## REQUIRED integration notes (tensor contract)

Bind inputs **by name** (signature `serving_default`; the converter orders them alphabetically).

| Tensor | Shape | Type | Value |
| --- | --- | --- | --- |
| `speech` | `[1, 560, N]` | f32 | LFR+CMVN features, **feature-major** (transpose of the usual `[T, 560]`), zero-padded to N |
| `speech_lengths` | `[1]` | i32 | true number of LFR frames (≤ N) |
| `language` | `[1]` | i32 | query id: auto 0, zh 3, en 4, yue 7, ja 11, **ko 12**, nospeech 13 |
| `textnorm` | `[1]` | i32 | `withitn` 14 (punctuation + digits), `woitn` 15 |
| `ctc_logits` (out) | `[1, N+4, 25055]` | f32 | keep the first `speech_lengths + 4` rows |
| `encoder_out_lens` (out) | `[1]` | i32 | = `speech_lengths + 4` |

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

- `gate40` is the 40-clip **TTS-synthesized** Korean short-command holdout used to rank this
  project's Whisper ACFT tiers. It is valid for **ranking only** (Spearman ρ = 1.00 against
  real recordings) and runs ~2.8× harsher than real audio in absolute CER.
- References average 3.6 characters: one wrong syllable is CER 0.25–0.33.
- Zeroth-Korean test sentences also appear in Zeroth train (456 / 457), and SenseVoice's
  training data is undisclosed — treat the Zeroth number as optimistic.
- CER = Levenshtein on the string with spaces removed and punctuation stripped (what a
  command matcher sees), `woitn`, language forced to `ko`.

## Validation (desktop, Windows x86-64 CPU, LiteRT 2.1.6, XNNPACK, 4 threads)

| Set | n | PyTorch (funasr, CUDA) | tflite fp32 | **w8** | i8 |
| --- | ---: | ---: | ---: | ---: | ---: |
| gate40 (TTS, ranking only) | 40 | 0.169 · 21 exact | 0.204 · 20 | 0.204 · 20 | 0.204 · 20 |
| real commands, quiet room | 13 | 0.009 · 11 | 0.006 · 12 | **0.006 · 12** | 0.006 · 12 |
| real commands, field noise | 9 | 0.296 · 4 | 0.269 · 5 | **0.269 · 5** | 0.333 · 5 |
| Zeroth-Korean test (see caveat) | 457 | 0.024 | 0.023 | 0.023 | 0.024 |
| FLEURS ko dev | 64 | 0.071 | 0.068 | 0.068 | 0.068 |

- **Conversion parity**: fp32 tflite vs onnxruntime on the same features — max |Δlogit|
  ≤ 3.6e-4 on commands, 0.029 on 20 s sentences, CTC argmax agreement 100 %, transcripts
  identical on all 583 clips. The PyTorch column differs only by CUDA-vs-CPU numerics
  flipping borderline tokens (e.g. `확대` → kana in both, on different clips).
- **Against Whisper ACFT-KO** on the same gate, same protocol (first 24 clips, punctuation
  kept): SenseVoice-Small 0.198 (PyTorch) / 0.247 (tflite) vs turbo-acft 0.182, medium
  0.208, base 0.305, tiny 0.457 — between turbo and base, at a quarter of turbo's size.

Invoke latency per window (model only, p50):

| Window | fp32 | w8 | i8 |
| --- | ---: | ---: | ---: |
| 3 s | 128 ms | 134 ms | 98 ms |
| 5 s | 145 ms | 172 ms | 121 ms |
| 10 s | 290 ms | 286 ms | 211 ms |
| 30 s | 827 ms | 815 ms | 691 ms |

Not yet measured on an Android device.

## Caveats

- Stock weights. Two Korean fine-tunes were measured and lost to stock on every set
  (an EDIE fine-tune: Zeroth CER 0.48; an in-house Zeroth fine-tune: real-command CER 0.020 vs 0.009).
- Field noise is the weak spot (fan/wind/vehicle recordings: 5 / 9 exact).
- Language forcing is soft: a few 1-syllable clips come out in kana even with `ko`.

## License / attribution

Weights: FunAudioLLM SenseVoiceSmall, under the
[FunASR model license](https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE).
Conversion only — no weights were changed. Paper: [FunAudioLLM, arXiv 2407.04051](https://arxiv.org/abs/2407.04051).
