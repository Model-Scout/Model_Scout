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

# Nemotron-3.5-ASR-Streaming-Multilingual-0.6B — LiteRT (FP16)

Cache-aware **streaming** multilingual speech recognition. A 0.6 B FastConformer-RNNT
encoder with a 128-slot **language prompt**, exported to **LiteRT (`.tflite`)** in **FP16**
for on-device Android inference (GPU / NNAPI / XNNPACK). FP16 is near-lossless versus the
FP32 source at half the size.

- **Architecture**: cache-aware FastConformer encoder (24 layers, 1024 hidden, 8× subsampling) + RNN-T decoder/joint
- **Streaming**: 320 ms chunk, 240 ms lookahead, left attention context 56, right context 3
- **Languages**: 100+ via the prompt dictionary (`languages.json`); benchmarked on 6 below
- **Audio**: 16 kHz mono, 128-bin log-mel front end

## Model

| | |
|---|---|
| Parameters | ~0.6 B |
| Format | LiteRT / TFLite (3-graph: encoder + decoder + joint) |
| Precision | FP16 (FLOAT_CASTING) |
| Bundle size | ~1.22 GB |
| Sample rate | 16 kHz mono |
| Chunk / lookahead | 320 ms / 240 ms |

## Files

| File | Size | Description |
|---|---|---|
| `nemotron-multilingual-encoder.tflite` | ~1.17 GB | Cache-aware FastConformer encoder (FP16) |
| `nemotron-multilingual-decoder.tflite` | ~30 MB | RNN-T prediction network |
| `nemotron-multilingual-joint.tflite` | ~19 MB | RNN-T joint network |
| `io_map.json` | ~4 KB | 22-port I/O wiring (inputs, outputs, carried caches) |
| `config.json` | <1 KB | Model + streaming config (mel, chunk, cache sizes) |
| `languages.json` | ~2 KB | Locale → prompt-slot dictionary (128 slots) |
| `vocab.json` | ~230 KB | 13 087-token BPE vocabulary |
| `*_recipe.json` | <1 KB | ai_edge_quantizer FP16 recipe per graph |

## Performance

FLEURS test, 320 ms streaming, **CPU**, n=30 per language. LiteRT FP16 matches ONNX FP16
within small-n variance (confirms the export is near-lossless). Japanese uses **CER**.

| Language | WER % | CER % |
|---|---|---|
| English (en-US) | 10.23 | 6.10 |
| German (de-DE) | 12.39 | 7.29 |
| French (fr-FR) | 15.93 | 6.00 |
| Arabic (ar-EG) | 14.02 | 3.74 |
| Hindi (hi-IN) | 7.37 | 4.46 |
| Japanese (ja-JP) | — | 16.34 |

On Android, run FP16 through the GPU or NNAPI delegate for hardware-accelerated half-precision
inference.

## Usage

```python
from ai_edge_litert.interpreter import Interpreter

enc = Interpreter(model_path="nemotron-multilingual-encoder.tflite")
enc.allocate_tensors()
# io_map.json describes the 22 ports: audio/mel input, the language-prompt slot,
# the carried encoder caches (attention / conv / pre-cache), and the emitted features.
# Per 320 ms chunk: set inputs + carried caches, invoke(), then drive the RNN-T
# decoder/joint greedy loop over the 4 emitted frames; carry caches into the next chunk.
```

Production streaming, delegate selection, cache management and RNN-T greedy decoding are
handled by the **[speech-android](https://github.com/soniqo/speech-android)** SDK.

## Source

Converted from **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**
(NVIDIA NeMo) via ai-edge-torch. Licensed under the
[NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## Related models

| Variant | Repo |
|---|---|
| ONNX · FP16 | [soniqo/…-ONNX-FP16](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-FP16) |
| ONNX · INT8 | [soniqo/…-ONNX-INT8](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-INT8) |
| LiteRT · FP16 (this) | `soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-FP16` |
| LiteRT · INT8 | [soniqo/…-LiteRT-INT8](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-INT8) |

## Links

- [speech-android](https://github.com/soniqo/speech-android) — Android SDK
- [speech-core](https://github.com/soniqo/speech-core) — on-device inference core (C++)
- [soniqo.audio](https://soniqo.audio) — website
- [blog](https://soniqo.audio/blog) — blog
