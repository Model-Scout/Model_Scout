---
license: gemma
license_link: https://ai.google.dev/gemma/terms
library_name: litert-lm
base_model:
  - google/gemma-4-E2B-it
base_model_relation: finetune
pipeline_tag: image-text-to-text
tags:
  - gemma
  - gemma-4
  - litert-lm
  - on-device
  - lora
  - korean
  - audio
  - vision
  - mobile
language:
  - ko
  - en
---

# Gemma 4 E2B — Korean audio LoRA (LiteRT-LM `.litertlm`, on-device deploy artifact)

On-device Gemma 4 E2B-it with a Korean-audio LoRA grafted into the
LiteRT-LM `.litertlm` bundle. Built for the **[Gilbeot][gilbeot] (길벗)**
project — a Korean walking-guide app for blind and elderly users —
submitted to the Kaggle Gemma 4 Good Hackathon (May 2026).

[gilbeot]: https://github.com/psymon-dev/gilbeot-public

## What is this

This is a **Model Derivative** of [`google/gemma-4-E2B-it`][base], packaged
as a single 2.6 GB LiteRT-LM `.litertlm` file ready for on-device
inference on Android via the [`flutter_gemma`][fg] plugin (or any
LiteRT-LM runtime). The base model is multimodal (text + vision + audio);
this derivative bakes in a Korean-audio LoRA that lowers on-device
Korean STT CER from ~13 % (INT4-quantized base) to ~5 % on our
134-utterance Korean held-out evaluation set.

[base]: https://huggingface.co/google/gemma-4-E2B-it
[fg]: https://github.com/DenisovAV/flutter_gemma

| Metric (134-utterance Korean STT eval, S10e CPU, device-side measurement) | Value |
|---|---|
| Base `litert-community/gemma-4-E2B-it-litert-lm` CER (no LoRA) | 13.14 % |
| **This model (graft + alpha-8 LM sidecar) CER** | **5.00 %** |
| Improvement vs device base | **~2.6 × reduction (−62 % relative)** |

For reference, the upstream HF Gemma 4 E2B-it at full precision
(no quantization) measured on the same eval set hits CER ~3.06 %
with the audio LoRA applied at HF level — the on-device 5.00 %
above is the deployable INT4 packaging of that adapter.

The accompanying alpha-8 LM-side LoRA sidecar (`~50 MB`) is bundled
inside the Gilbeot APK itself (`assets/lora/`) and applied at runtime
via the patched [`flutter_gemma`][fg] fork's `SetScopedLoraFile` path.
This repository carries the graft `.litertlm` only.

## Modifications (per Gemma Terms of Use § 3.1(3))

This file has been **modified** from the upstream `google/gemma-4-E2B-it`
in the following ways:

1. **Audio encoder LoRA graft** (`audio_encoder_hw.tflite` section):
   per-row dequantize → add LoRA delta → re-quantize on the same INT4
   grid. Computed against a PEFT LoRA fine-tuned with Unsloth FastModel
   on a **50-hour speaker-stratified subset** of AI-Hub's
   "[명령어 음성(노인남녀)](https://aihub.or.kr/)" (Command Speech —
   Elderly Men and Women) dataset — 45,823 utterances, 138 Korean
   elderly speakers (60+), 4 regional dialects, AI-assistant
   command-style + unstructured commands, recorded on smartphones in
   home environments at 48 kHz (resampled to 16 kHz mono for training).
   This audio-encoder graft is the decisive contribution
   (~39 % relative CER improvement on top of base + sidecar).

2. **LM-side LoRA graft** (`prefill_decode.tflite` section):
   same dequantize → add → re-quantize approach on attention + MLP
   blocks. Empirically contributes ~0.16 %p CER on top of (1); kept
   for compatibility with the production deployment pipeline.

3. **No changes** to: tokenizer, vocabulary, vision encoder
   (`vision_encoder.tflite`), MTP drafter (`mtp_drafter.tflite`),
   per-layer embedder, runtime ABI, or any other section.

The patcher source (`tools/patch_gemma4_lora_requant.py`) and the
full saga of getting this through an unsupported toolchain (Google's
official Gemma 4 audio LoRA `.litertlm` exporter is not public at
submission time) are documented in the [Gilbeot public repo][gilbeot]
under `docs/dev_log_highlights.md`.

## License & notices

This model is distributed under and subject to the **[Gemma Terms of
Use](https://ai.google.dev/gemma/terms)** and the **[Gemma Prohibited
Use Policy](https://ai.google.dev/gemma/prohibited_use_policy)**.

**NOTICE** (per Gemma Terms of Use § 3.1(4)):
> Gemma is provided under and subject to the Gemma Terms of Use found
> at ai.google.dev/gemma/terms

By downloading or using this model you agree to the Gemma Terms of
Use and the Gemma Prohibited Use Policy, and you agree to pass these
restrictions through to any further recipients of this model or its
derivatives (per § 3.1(1) and § 3.1(2)).

A copy of the Gemma Terms of Use notice and the Gemma Prohibited Use
Policy reference is included in this repository's [`LICENSE`](LICENSE)
file.

## Prohibited use

Per [Google's Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy),
you may not use, nor allow others to use, this model or its derivatives
to perform or facilitate dangerous, illegal, or malicious activities;
to generate content that misleads, defames, or harasses; to infringe
the rights of individuals or entities; or to attempt to override or
bypass safety mechanisms. The authoritative current version of the
policy is the live page at the link above — please review it before
use.

## Usage

### From a Flutter app (`flutter_gemma`)

```dart
final installation = await FlutterGemma.installModel(
  modelType: ModelType.gemma4,
  fileType: ModelFileType.litertlm,
)
  .fromNetwork(
    'https://huggingface.co/psymon/gemma-4-E2B-it-korean-audio-litertlm/'
    'resolve/main/gemma-4-E2B-it.litertlm',
  )
  .withProgress((p) => print('download $p%'))
  .install();
```

The downloaded `.litertlm` lands in the app-private directory and is
removed automatically when the user uninstalls the app (standard
Android private-data semantics — no orphaned files in
`/data/local/tmp/`).

To get the production CER 5%, also attach the alpha-8 LM-side LoRA
sidecar — the [Gilbeot APK][gilbeot] bundles it as an asset and
extracts it on first launch; alternatively `withLoraFromNetwork(...)`
can pull it from a separate URL.

### Verified deployment

- Android arm64 only (LiteRT-LM `.litertlm` is arm64-v8a)
- Tested on: **Galaxy S23** (Adreno 740, GPU backend, MTP on:
  ~13s / vision photo at warm cache) and **Galaxy S10e** (Exynos
  9820 / Mali-G76, CPU backend, MTP off: ~48s / vision photo)
- Requires `flutter_gemma` 0.14.5 or compatible LiteRT-LM runtime

## Training & deployment recipe (reproducibility)

| Stage | Tool / artifact |
|---|---|
| Data | **AI-Hub "명령어 음성(노인남녀)"** (Command Speech — Elderly Men and Women), https://aihub.or.kr — 125.7 h / 138 elderly Korean speakers / 4 dialects raw |
| Train subset | 50 h speaker-stratified (45,823 utterances → 43,431 after quality filter) + 2,291 utt (~2.5 h) speaker-stratified validation hold-out |
| Fine-tune | **Unsloth FastModel** + bitsandbytes 4-bit + PEFT, rank-8 LoRA on attention + MLP, alpha-8, 2 epochs |
| Adapter (HF level) | `outputs/gemma4_audio_v2/lora/adapter_model.safetensors` — CER 3.06 % on 134-sample held-out elderly Korean eval (speaker-disjoint from training set) |
| Graft into `.litertlm` | `tools/patch_gemma4_lora_requant.py` in [Gilbeot public repo][gilbeot] — dequantize, add LoRA delta, re-quantize on the same INT4 grid |
| Runtime LM-side sidecar | `gemma4_full_lm_lora_atten_mlp_alpha8.bin` (~50 MB, attached via `SetScopedLoraFile`) — bundled in the Gilbeot APK, **not in this repo** |
| Final on-device CER | **5.00 %** (134-utterance Korean held-out, S10e CPU) |

Unsloth was used specifically because vanilla PEFT 0.19 silently
skips Gemma 4's `Gemma4ClippableLinear` audio-side custom layer
(loss decreases but adapter has no effect on audio outputs).
Unsloth's FastModel correctly wraps that layer.

## Acknowledgments

- Google DeepMind for [Gemma 4 E2B][base] and the LiteRT-LM runtime
- `litert-community` for [`gemma-4-E2B-it-litert-lm`][litcomm] (the
  ungated LiteRT-LM packaging this derivative is based on)
- [DenisovAV][denisovav] for the [`flutter_gemma`][fg] package and
  the prebuilt `libLiteRtLm.so` used in Gilbeot
- [Unsloth][unsloth] for FastModel and the Gemma 4 audio fine-tune
  support
- **AI-Hub** (한국지능정보사회진흥원 / NIA) for the publicly
  released "명령어 음성(노인남녀)" (Command Speech — Elderly Men
  and Women) dataset used for the LoRA training

[litcomm]: https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm
[denisovav]: https://github.com/DenisovAV
[unsloth]: https://github.com/unslothai/unsloth

## Citation / contact

Submitted as part of the **Gilbeot** project to the Kaggle Gemma 4
Good Hackathon, May 2026. Source code, dev log highlights, patcher,
and the production Android APK at:

→ <https://github.com/psymon-ai/gilbeot-public>

For issues with this model file specifically (graft regressions,
LoRA mismatch reports, etc.), please open an issue on the Gilbeot
repo and tag it `[hf-model]`.

## Attribution

  Built with [Gemma 4 E2B](https://huggingface.co/google/gemma-4-e2b-it).
  A rank-8 LoRA was fine-tuned with Unsloth + PEFT + bitsandbytes 4-bit on
  AI Hub's *Command Speech (Elderly Male/Female)* dataset (~45,823
  utterances / ~50 h), then grafted into the LiteRT-LM `.litertlm` bundle
  via a same-grid requant patcher (source:
  [psymon-ai/gilbeot-public/tools](https://github.com/psymon-ai/gilbeot-public/tree/master/tools)).
  Korean STT improves from 13.14 % → 5.00 % CER on a 134-utterance Korean
  held-out set.

  _Gemma is a trademark of Google LLC._