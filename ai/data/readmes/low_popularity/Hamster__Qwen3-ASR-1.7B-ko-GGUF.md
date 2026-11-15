---
license: apache-2.0
base_model: TeamUNIVA/qwen3_asr_1.7b_ko
base_model_relation: quantized
language:
- ko
- en
pipeline_tag: automatic-speech-recognition
tags:
- gguf
- llama.cpp
- mtmd
- qwen3-asr
- korean
- speech-recognition
---

# Qwen3-ASR-1.7B-ko — GGUF

GGUF conversion of [TeamUNIVA/qwen3_asr_1.7b_ko](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko),
a Korean fine-tune of [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)
(Apache 2.0), for use with [llama.cpp](https://github.com/ggml-org/llama.cpp)'s `mtmd`
audio front-end. Packaged for the [Milo](https://github.com/hamsterskywalker/Milo)
local voice-typing tool, where it is the `qwen3asr` engine's Korean model.

## Files

| File | Size | Purpose |
|------|-----:|---------|
| `Qwen3-ASR-1.7B-ko-Q8_0.gguf` | 2.1 GB | text model (Q8_0) |
| `mmproj-Qwen3-ASR-1.7B-ko-Q8_0.gguf` | 339 MB | audio encoder / projector (Q8_0) |

Both files are required; keep them in the same folder.

## Why this fine-tune

The upstream model card reports Korean CER 6.86% → **4.83%** over 8,383 reviewed
utterances (clova_call, common_voice_ko, fleurs_ko, ksponspeech, zeroth), with English
WER +0.27%p. On the seven showcase clips in that repository, this GGUF scores CER 0.7%
against 14.0% for the official `Qwen3-ASR-1.7B` Q8_0 GGUF and 12.9% for whisper
large-v3-turbo (q5_0) — note those clips were chosen by the fine-tune's authors.

## Usage

llama.cpp:

```
llama-mtmd-cli -m Qwen3-ASR-1.7B-ko-Q8_0.gguf --mmproj mmproj-Qwen3-ASR-1.7B-ko-Q8_0.gguf --audio clip.wav
```

Milo: Settings → STT engine "Qwen3-ASR" → model `Qwen3-ASR-1.7B-ko-Q8_0.gguf` → Download.

To force Korean, pre-fill the assistant turn with the model's own header
`language Korean<asr_text>`; Milo's helper does this when the language is set to `ko`.

## Conversion

Made with llama.cpp `convert_hf_to_gguf.py` (commit f3f1a8f, 2026-09-08), transformers 4.57.6:

```
python convert_hf_to_gguf.py qwen3_asr_1.7b_ko --outtype q8_0 --outfile Qwen3-ASR-1.7B-ko-Q8_0.gguf
python convert_hf_to_gguf.py qwen3_asr_1.7b_ko --mmproj --outtype q8_0 --outfile mmproj-Qwen3-ASR-1.7B-ko-Q8_0.gguf
```

No weights were changed; this is a straight quantised repackaging. All credit for the
model goes to TeamUNIVA and the Qwen team. License: Apache 2.0, as upstream.
