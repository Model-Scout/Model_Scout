---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
language:
  - zh
  - en
  - ja
  - ko
  - es
  - fr
  - de
tags:
  - litert
  - tflite
  - automatic-speech-recognition
  - streaming-asr
  - FastConformer
  - RNNT
  - q4
  - quantization-aware-training
pipeline_tag: automatic-speech-recognition
library_name: litert
---

# Nemotron-3.5-ASR-Streaming-0.6B — LiteRT q4-mix

On-device (Android) LiteRT port of
[nvidia/nemotron-3.5-asr-streaming-0.6b](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b)
(0.6B FastConformer-RNNT, multilingual streaming ASR). **q4-mix**: INT4 encoder
(83% of the weights) + fp16 decoder/joint, near-lossless via quantization-aware
training. Bundle **663 MB**.

Port, export scripts, runner, and the VoxSum integration note:
https://github.com/vieenrose/LiteRT/tree/nemotron/litert/samples/asr/nemotron

## Files

| file | role | precision | size |
|---|---|---|---|
| `nemotron_encoder_q4.tflite` | FastConformer encoder | INT4 FC (blockwise-128, QAT) + fp32 convs | 569 MB |
| `nemotron_prompt_fuse_fp32.tflite` | 128-slot language-prompt fusion | fp32 | 17 MB |
| `nemotron_decoder_fp16.tflite` | RNN-T prediction net (2-layer LSTM) | fp16 | 29 MB |
| `nemotron_joint_fp16.tflite` | RNN-T joint (→ vocab 13088) | fp16 | 17 MB |
| `tokenizer.json` / `tokenizer_config.json` | ParakeetTokenizer (SentencePiece BPE) | — | — |
| `processor_config.json` | mel front-end + `prompt_dictionary` (128 slots) | — | — |
| `config.json` | model config | — | — |

## Graph flow (RNN-T greedy, batch-1)

```
mel[1,T,128] --encoder_q4--> hidden[1,T',1024]
hidden + one_hot(lang)[1,128] --prompt_fuse--> fused[1,T',1024]
for t in T':  loop: logits = joint(fused[:,t], dec_out); k=argmax; if k==BLANK(13087) next
              else emit k; dec_out,h,c = decoder(k, h, c)
```

Front end: 128-bin log-mel, `n_fft=512 hop=160 win=400 preemph=0.97`, **raw
log-mel, no per-feature norm**, 16 kHz mono. Language slots from
`processor_config.json` (`en-US`=0, `zh-CN`=4, `ja-JP`=10, …).

**zh-TW**: this base build's zh-TW slot is untrained (~100% CER) — decode with
`zh-CN` + OpenCC `s2t`, or use the **fine-tuned** variant
[Luigi/nemotron-asr-litert-zhtw](https://huggingface.co/Luigi/nemotron-asr-litert-zhtw)
(Common Voice zh-TW **13.20 CER** vs ~38 here; other languages unaffected).

## Accuracy

ASCEND zh, CER, n=100:

| build | zh-CN CER |
|---|---|
| fp32 `model.generate` (reference) | 15.61% |
| **this q4-mix LiteRT** | **16.32%** (+0.7, near-lossless) |

The encoder is quantized to INT4 via a label-based RNN-T QAT (STE fake-quant on
the FC weights, FP self-distillation pseudo-labels) whose grid is pre-baked into
the export. decoder/joint/prompt stay ≥fp16 (INT4 there collapses the RNN-T →
435% WER).

## Runtime note (important)

The INT4 encoder uses dynamic-range INT4 `FULLY_CONNECTED` — the classic TFLite
`Interpreter` reference CPU kernel **cannot allocate it**. Run it through the
**LiteRT-Next `CompiledModel`** runtime (Android NNAPI / XNNPACK-QD8, or the
`com.google.ai.edge.litert:litert` AAR); set the CPU thread count explicitly.

## Provenance

Base: nvidia/nemotron-3.5-asr-streaming-0.6b (NVIDIA Open Model License). The QAT
of the INT4 encoder is the only trained change (no language change, "as original
as possible"); everything else is numerics-preserving conversion.
