---
license: mit
pipeline_tag: automatic-speech-recognition
base_model:
- microsoft/VibeVoice-ASR-BitNet
language:
- en
- zh
- fr
- it
- ko
- pt
- vi
library_name: ggml
base_model_relation: quantized
tags:
- thox
- asr
- quantization
- cpu-inference
- gguf
- bitnet
- multilingual
- thoxos
- meshstack
- thoxspeech
- local-first
---
<div align="center">

<img src="hero-family.png" alt="The THOX four-device family" width="100%">

<h1>ThoxSpeech-ASR-BitNet</h1>

**CPU Multilingual Speech Recognition (Redistribution) — a verbatim redistribution of a third-party multilingual automatic speech recognition model, mirrored here for CPU-only on-device transcription in the THOX stack**

**Multilingual ASR, CPU-only · 1.58 GB total (I8_S tokenizer 0.65 GB + I2_S / Q6_K decoder 0.92 GB) · Verbatim upstream redistribution**

</div>

| ![License](https://img.shields.io/badge/License-MIT-05A451) | ![Params](https://img.shields.io/badge/Params-1.58_GB_total-05A451) | ![Base](https://img.shields.io/badge/Base-VibeVoice--ASR--BitNet-05A451) | ![Access](https://img.shields.io/badge/Access-Public-05A451) |
|---|---|---|---|



> **Your AI. Your Data. Your Rules.™**

> **Status: VERBATIM REDISTRIBUTION.** THOX did not retrain or re-quantize this model; it is mirrored here for CPU-only on-device transcription in the THOX stack, under the upstream MIT license, with credit to the upstream authors (see License).

## Summary

ThoxSpeech-ASR-BitNet is a verbatim redistribution of a third-party multilingual automatic speech recognition model, mirrored here for CPU-only on-device transcription in the THOX stack. **THOX did not retrain or re-quantize it**; credit for the model belongs upstream (see License). Total size 1.58 GB: an I8_S acoustic tokenizer (0.65 GB) plus an I2_S / Q6_K language-model decoder (0.92 GB), in a two-stage architecture.


## Highlights

- ThoxSpeech-ASR-BitNet is a verbatim redistribution of a third-party multilingual automatic speech recognition model, mirrored here for CPU-only on-device transcription in the THOX stack.
- ```bash hf download Thox-ai/ThoxSpeech-ASR-BitNet --local-dir ./ThoxSpeech-ASR-BitNet # run with the VibeVoice / BitNet ggml ASR runtime (CPU) ``` Ollama and LM Studio do not support these files; the ternary and non-standard GGUF types need the dedicated ggml ASR runtime.

## Specifications

| | |
|---|---|
| Base model | microsoft/VibeVoice-ASR-BitNet |
| Parameters | See card body |
| Formats | GGUF: thoxspeech-lm-i2_s-embed-q6_k.gguf, thoxspeech-vae-encoder-i8_s.gguf |
| License | MIT. This repo is a mirror of an upstream MIT-licensed model (© Microsoft Corporation); the MIT notice carries forward and THOX claims no authorship of the weights. See the license text for terms. |
| This repository contains | GGUF build(s) in this repo: thoxspeech-lm-i2_s-embed-q6_k.gguf, thoxspeech-vae-encoder-i8_s.gguf |

## Files

| File | Size | SHA-256 |
|---|---:|---|
| `thoxspeech-lm-i2_s-embed-q6_k.gguf` | 992,877,600 B | `fbe273d8dc2f2433bb25f849e19d77ea65aaa2188d12c20cee987ab6f321e002` |
| `thoxspeech-vae-encoder-i8_s.gguf` | 703,080,064 B | `4941c82608c253ec066b5cc74d3dd11a5c8fef96cccbc5b87359ef0fe4338df6` |
| `THIRD_PARTY_NOTICES.md` / `NOTICE` / `.gitattributes` | — | Supporting files (see repo) |


## Run it

```bash
hf download Thox-ai/ThoxSpeech-ASR-BitNet --local-dir ./ThoxSpeech-ASR-BitNet
# run with the VibeVoice / BitNet ggml ASR runtime (CPU)
```

Ollama and LM Studio do not support these files; the ternary and non-standard GGUF types need the dedicated ggml ASR runtime.


## Platforms

| Platform / device | Run path |
|---|---|
| Hugging Face | Download the builds listed under Files from this repo (see Run it) |
## Intended use

- Multilingual automatic speech recognition on CPU: research and on-device transcription.
- Out of scope: medical, legal, financial, safety-critical, or other high-stakes decisions without human review; unattended control of physical devices without a confirmation step.

## Training data and procedure

THOX fine-tune of `microsoft/VibeVoice-ASR-BitNet`. The corpus and procedure are described in this card as published at release (see Summary and Evaluation); no training beyond what this card describes is claimed for this repository.

## Evaluation

Word error rate around 2.41 on LibriSpeech-clean in THOX's internal testing. Accuracy degrades on far-field and overlapping speech. No THOX GATE49 result applies (speech model).

## Limitations

- Transcription errors are expected on noisy, far-field, or overlapping speech; verify important transcripts.
- THOX makes no quality claim beyond the measurement above; the model is redistributed as published upstream.
- Behaviour and bias reflect the upstream training data.

## License

MIT. This repo is a mirror of an upstream MIT-licensed model (© Microsoft Corporation); the MIT notice carries forward and THOX claims no authorship of the weights. See the license text for terms.

THOX.ai — Your AI. Your Data. Your Rules.™

## Provenance

Published by THOX.ai as `Thox-ai/ThoxSpeech-ASR-BitNet`. Upstream base: `microsoft/VibeVoice-ASR-BitNet`. This card was conformed to THOX Model Card Standard v1.0 on 2026-10-31 (frontmatter, tags, header, files, and section structure); the technical content is as published at release.

## Citation

```bibtex
@misc{thoxai2026thoxspeechasrbitnet,
      title={ThoxSpeech-ASR-BitNet},
      author={THOX.ai},
      year={2026},
      url={https://huggingface.co/Thox-ai/ThoxSpeech-ASR-BitNet}
}
```
