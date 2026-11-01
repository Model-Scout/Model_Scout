---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
language:
- en
- es
- zh
- hi
- ar
- fr
- de
- ja
- ru
- pt
- ko
- it
- nl
- pl
- tr
- uk
- ro
- cs
- hu
- sv
- da
- fi
- th
- vi
- id
tags:
- automatic-speech-recognition
- streaming-asr
- cache-aware
- multilingual
- FastConformer
- RNNT
- litert
- tflite
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
library_name: litert
pipeline_tag: automatic-speech-recognition
---

# Nemotron-3.5-ASR-Streaming-Multilingual-0.6B — LiteRT (INT8)

Cache-aware **streaming** multilingual speech recognition. A 0.6 B
FastConformer-RNNT encoder with a 128-slot **language prompt**, exported to
**LiteRT (`.tflite`)** with channelwise **weight-only INT8** encoder weights.
Activations and compute remain FP32, making the compact encoder compatible with
the standard LiteRT CPU runtime without requiring an NNAPI, GPU or NPU
delegate. For best quality across all languages, use the
[FP16 build](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-FP16).

- **Architecture**: cache-aware FastConformer encoder (24 layers, 1024 hidden, 8× subsampling) + RNN-T decoder/joint
- **Streaming**: 320 ms chunk, 240 ms lookahead, left attention context 56, right context 3
- **Languages**: 100+ via the prompt dictionary (`languages.json`)
- **Audio**: 16 kHz mono, 128-bin log-mel front end

## Model

| | |
|---|---|
| Parameters | ~0.6 B |
| Format | LiteRT / TFLite (3-graph: encoder + decoder + joint) |
| Precision | INT8 weights / FP32 compute (encoder) + FP32 decoder/joint |
| Release revision | `v1.0.0` |
| Bundle size | ~687 MB |
| Sample rate | 16 kHz mono |
| Chunk / lookahead | 320 ms / 240 ms |

## Files

| File | Size | Description |
|---|---|---|
| `nemotron-multilingual-encoder.tflite` | ~594 MB | Cache-aware FastConformer encoder (weight-only INT8) |
| `nemotron-multilingual-decoder.tflite` | ~60 MB | RNN-T prediction network (FP32) |
| `nemotron-multilingual-joint.tflite` | ~38 MB | RNN-T joint network (FP32) |
| `io_map.json` | ~4 KB | 22-port I/O wiring (inputs, outputs, carried caches) |
| `config.json` | <1 KB | Model + streaming config (mel, chunk, cache sizes) |
| `languages.json` | ~2 KB | Locale → prompt-slot dictionary (128 slots) |
| `vocab.json` | ~230 KB | 13 087-token BPE vocabulary |
| `nemotron-multilingual-encoder_recipe.json` | <1 KB | Effective precision and graph-repair metadata |
| `speech_models_export.json` | <10 KB | Pinned source, checksums, tool versions and verified I/O |

## Runtime compatibility

The encoder uses LiteRT's hybrid path: weights are stored channelwise INT8
while activations, outputs and compute remain FP32. The original compact graph
incorrectly quantized one shared non-weight constant, selecting an invalid
integer `FULLY_CONNECTED` path. This release restores that constant to FP32 and
allows `allocate_tensors()` on the plain LiteRT CPU interpreter. A hardware
delegate is optional.

## Usage

```python
from ai_edge_litert.interpreter import Interpreter

enc = Interpreter(model_path="nemotron-multilingual-encoder.tflite")
enc.allocate_tensors()
# io_map.json describes the 22 ports: audio/mel input, language-prompt slot,
# carried encoder caches (attention / conv / pre-cache), and emitted features.
```

Production streaming, cache management and RNN-T greedy decoding are handled by
the **[speech-android](https://github.com/soniqo/speech-android)** SDK.

## Reproducibility

The compact graph is rebuilt from the pinned INT8 revision
`851781a85976d95e1967d33b8a60e3441199507c`; the exact FP32 non-weight
constant is restored from the structurally matching FP16 revision
`1503a9a1eb75b813b83ba65bf5e9fecea4a46091`. The accompanying
`speech_models_export.json` records both source and output SHA-256 checksums,
the guarded tensor repair, tool versions, and CPU-validated I/O signatures.

## Source

Converted from
**[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**
(NVIDIA NeMo) via ai-edge-torch. Licensed under the
[NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Related models

| Variant | Repo |
|---|---|
| ONNX · FP16 | [soniqo/…-ONNX-FP16](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-FP16) |
| ONNX · INT8 | [soniqo/…-ONNX-INT8](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-INT8) |
| LiteRT · FP16 | [soniqo/…-LiteRT-FP16](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-FP16) |
| LiteRT · INT8 (this) | `soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-INT8` |

## Links

- [speech-android](https://github.com/soniqo/speech-android) — Android SDK
- [speech-core](https://github.com/soniqo/speech-core) — on-device inference core (C++)
- [soniqo.audio](https://soniqo.audio) — website
- [blog](https://soniqo.audio/blog) — blog
