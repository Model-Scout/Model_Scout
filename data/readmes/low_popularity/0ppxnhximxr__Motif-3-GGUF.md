---
library_name: gguf
pipeline_tag: text-generation
language:
- en
- ko
tags:
- motif
- motif-3
- gguf
- llama.cpp
- quantized
- mixture-of-experts
- moe
- multilingual
license: mit
base_model: Motif-Technologies/Motif-3
base_model_relation: quantized
---

# Motif-3 GGUF

GGUF quantizations of the official [Motif-Technologies/Motif-3](https://huggingface.co/Motif-Technologies/Motif-3) checkpoint for the Motif-3-enabled llama.cpp runtime.

These files were converted **directly from the official BF16 weights** at source revision `1695f5aa6d97cccc8623a03f93c9c7d5fbb14d45`. They are not requantizations of an FP8 or another reduced-precision checkpoint.

Motif-3 is a 314B-total / 13.2B-active decoder-only MoE model. The upstream model card and MIT license remain the authoritative sources for architecture details, intended use, and limitations.

## Files and BF16-relative fidelity

Each variant is split into 14 GGUF shards. Download all shards for one variant and pass only its `00001-of-00014.gguf` file to llama.cpp; the remaining shards are discovered automatically.

| Variant | Size (GB) | Size (GiB) | Global cosine vs. BF16 | Cosine retained | Relative RMSE |
|:--|--:|--:|--:|--:|--:|
| Q8_0 | 338.186 | 314.960 | 0.99998562 | 99.9986% | 0.005362 |
| Q6_K | 262.881 | 244.827 | 0.99984197 | 99.9842% | 0.017779 |
| Q5_K_M | 228.151 | 212.482 | 0.99938693 | 99.9387% | 0.035013 |
| Q4_K_M | 195.465 | 182.041 | 0.99764785 | 99.7648% | 0.068587 |
| Q3_K_M | 155.723 | 145.029 | 0.99002836 | 99.0028% | 0.141684 |
| Q2_K | 120.750 | 112.458 | 0.96210594 | 96.2106% | 0.279441 |

Q8_0 provides the closest weight reconstruction. Q6_K and Q5_K_M are the practical high-fidelity choices when their memory footprint is acceptable. Lower-bit variants trade progressively more reconstruction precision for capacity.

### Fidelity methodology

The comparison uses deterministic, evenly spaced, complete GGML rows sampled from every tensor changed from BF16 by quantization: 2 rows from each of 314 quantized tensors, or 2,030,592 scalar values per variant. Quantized rows are reconstructed with the reference dequantizers in the same llama.cpp GGUF implementation and compared directly with the corresponding official-source BF16 rows. Global cosine is accumulated over all sampled values; relative RMSE is `||BF16 - dequantized||₂ / ||BF16||₂`.

These are weight-reconstruction measurements, not task benchmark scores. The reproducible measurement script is included as `compare_cosine.py`.

## Mixed precision details

The label describes the target type for the large quantizable tensors, not a promise that every tensor uses that type. The Motif-3 converter deliberately preserves sensitive GDLA attention tensors in BF16 and control/norm tensors in F32. Each variant contains 2,162 tensors in total:

- 424 BF16 tensors
- 1,424 F32 tensors
- 314 quantized tensors

The current Motif-3 GGUF converter covers the main causal model but does not export the upstream MTP auxiliary head. Consequently, the upstream self-speculative MTP path is not available in these GGUF files.

## Runtime requirement

Motif-3 support is not yet part of ordinary llama.cpp releases used for this conversion. Use the Motif3 branch at the pinned commit below and apply the included tokenizer patch. The patch adds the exact Motif-3 pre-tokenizer and was checked to apply cleanly to that commit.

```bash
git clone --branch Motif3 https://github.com/timkhronos/llama.cpp.git
cd llama.cpp
git checkout 7a56c974b46ec26b4db2967d02481f1fc8c6a17e

curl -L -o llama.cpp-motif3-tokenizer.patch \
  https://huggingface.co/0ppxnhximxr/Motif-3-GGUF/resolve/main/llama.cpp-motif3-tokenizer.patch
git apply llama.cpp-motif3-tokenizer.patch

cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CUDA_ARCHITECTURES=90
cmake --build build --config Release -j
```

Example server command for a multi-GPU machine:

```bash
./build/bin/llama-server \
  -m /path/to/Motif-3-Q5_K_M-00001-of-00014.gguf \
  --split-mode layer \
  --gpu-layers auto \
  --fit on \
  --fit-target 4096 \
  --flash-attn off \
  --cache-type-k f16 \
  --cache-type-v f16 \
  -c 4096 \
  --host 0.0.0.0 \
  --port 8080
```

`--fit on` lets llama.cpp leave layers in system memory when the model plus runtime buffers do not fit fully in aggregate VRAM. Q8_0 was loaded and served on the four-H100 system below with automatic host offload.

## Quantization environment

| Component | Environment |
|:--|:--|
| GPUs | 4 × NVIDIA H100 80GB HBM3 |
| GPU driver | 580.178.04 |
| CUDA toolkit | 13.0 (`nvcc` 13.0.88) |
| CPU | Intel Xeon Platinum 8480+, 52 cores / 104 threads |
| System memory | 885 GiB |
| Kernel | Linux 6.8.0-1046-nvidia |
| llama.cpp Motif3 base | `7a56c974b46ec26b4db2967d02481f1fc8c6a17e` |
| Source model revision | `1695f5aa6d97cccc8623a03f93c9c7d5fbb14d45` |
| Transfer path | Hugging Face Xet high-performance mode |

The BF16-to-GGUF conversion and CPU quantization used local NVMe storage and high parallel CPU utilization. CUDA was used for the runtime build and inference validation; standard llama.cpp GGUF quantization itself is CPU-side.

## Attribution and license

The model architecture and original weights are by [Motif Technologies](https://huggingface.co/Motif-Technologies). The source model is distributed under the MIT license. This repository contains format-converted and quantized derivatives under the same license terms; consult the upstream repository for complete model documentation.
