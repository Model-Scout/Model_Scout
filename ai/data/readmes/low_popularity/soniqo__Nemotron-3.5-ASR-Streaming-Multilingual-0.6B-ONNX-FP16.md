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
- onnx
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
library_name: onnxruntime
pipeline_tag: automatic-speech-recognition
---

# Nemotron-3.5-ASR-Streaming-Multilingual-0.6B — ONNX (FP16)

Cache-aware **streaming** multilingual speech recognition. A 0.6 B FastConformer-RNNT
encoder with a 128-slot **language prompt** (one slot per language/locale), exported to
ONNX in **FP16**. FP16 is lossless versus the FP32 source (identical WER/CER) at half the
download size, and is hardware-accelerated on GPU / NPU / Android-NNAPI.

- **Architecture**: cache-aware FastConformer encoder (24 layers, 1024 hidden, 8× subsampling) + RNN-T decoder/joint
- **Streaming**: 320 ms chunk, 240 ms lookahead, left attention context 56, right context 3
- **Languages**: 100+ via the prompt dictionary (`languages.json`); benchmarked on 6 below
- **Audio**: 16 kHz mono, 128-bin log-mel front end

## Model

| | |
|---|---|
| Parameters | ~0.6 B |
| Format | ONNX (external-data weights) |
| Precision | FP16 |
| Bundle size | ~1.25 GB |
| Sample rate | 16 kHz mono |
| Chunk / lookahead | 320 ms / 240 ms |

## Files

| File | Size | Description |
|---|---|---|
| `encoder.onnx` + `encoder.onnx.data` | ~1.18 GB | Cache-aware FastConformer encoder (FP16) |
| `decoder.onnx` + `decoder.onnx.data` | ~30 MB | RNN-T prediction network |
| `joint.onnx` + `joint.onnx.data` | ~19 MB | RNN-T joint network |
| `config.json` | <1 KB | Model + streaming config (mel, chunk, cache sizes) |
| `languages.json` | ~2 KB | Locale → prompt-slot dictionary (128 slots) |
| `vocab.json` | ~230 KB | 13 087-token BPE vocabulary |

## Performance

FLEURS test, 320 ms streaming, **CPU**, n=30 per language. FP16 is bit-equivalent to FP32.
For Japanese, **CER** is the meaningful metric (no word boundaries).

| Language | WER % | CER % |
|---|---|---|
| English (en-US) | 9.92 | 5.65 |
| German (de-DE) | 12.68 | 7.40 |
| French (fr-FR) | 15.93 | 6.02 |
| Arabic (ar-EG) | 14.02 | 3.74 |
| Hindi (hi-IN) | 7.37 | 4.46 |
| Japanese (ja-JP) | — | 16.28 |

Resource profile (8.4 s utterance, ONNX Runtime CPU): encoder ~87 ms/chunk (RTF ~0.27),
peak RSS ~3.4 GB. Note: ONNX Runtime up-converts FP16→FP32 on CPU (no native FP16 CPU
kernels), so FP16's runtime wins are realized on GPU / NPU / NNAPI — on CPU its benefit is
the smaller download. For lowest CPU latency/RAM, use the INT8 build.

## Usage

```python
import onnxruntime as ort

so = ort.SessionOptions()
enc = ort.InferenceSession("encoder.onnx", so, providers=["CPUExecutionProvider"])
dec = ort.InferenceSession("decoder.onnx", so, providers=["CPUExecutionProvider"])
joint = ort.InferenceSession("joint.onnx", so, providers=["CPUExecutionProvider"])

# Pick the language prompt slot from languages.json, e.g. "en-US" -> 0, "ja-JP" -> 10.
# Front end: 128-bin log-mel (n_fft=512, win=400, hop=160, preemph=0.97), 16 kHz mono.
# Streaming contract (per chunk): feed 320 ms of audio + the carried encoder caches
# (attention / conv / pre-cache), then run the RNN-T greedy loop over the 4 emitted frames.
# Port wiring for the encoder caches is described by config.json's "streaming" block.
```

Production streaming, cache management and RNN-T greedy decoding are handled by the
**[speech-android](https://github.com/soniqo/speech-android)** SDK.

## Source

Converted from **[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)**
(NVIDIA NeMo). Licensed under the
[NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).

## WebGPU / browser

The encoder emits its per-layer streaming-cache concatenation as a **tree of
≤6-input `Concat` nodes** (instead of one 24-input `Concat`), so no node exceeds
WebGPU's `maxStorageBuffersPerShaderStage` limit (8). This lets `onnxruntime-web`
run the encoder under the WebGPU execution provider — including Compatibility mode
and mobile GPUs that cap at 8 storage buffers per shader stage. The rewrite is
numerically identical to a standard graph (concatenation is associative) and has
no effect on CPU/NNAPI/CUDA runtimes. (INT8 is not WebGPU-compatible — its
`ConvInteger` op is unsupported there; use this FP16 build for the browser.)

## Related models

| Variant | Repo |
|---|---|
| ONNX · FP16 (this) | `soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-FP16` |
| ONNX · INT8 | [soniqo/…-ONNX-INT8](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-ONNX-INT8) |
| LiteRT · FP16 | [soniqo/…-LiteRT-FP16](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-FP16) |
| LiteRT · INT8 | [soniqo/…-LiteRT-INT8](https://huggingface.co/soniqo/Nemotron-3.5-ASR-Streaming-Multilingual-0.6B-LiteRT-INT8) |

## Links

- [speech-android](https://github.com/soniqo/speech-android) — Android SDK
- [speech-core](https://github.com/soniqo/speech-core) — on-device inference core (C++)
- [soniqo.audio](https://soniqo.audio) — website
- [blog](https://soniqo.audio/blog) — blog
