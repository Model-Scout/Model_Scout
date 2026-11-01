---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE
language:
- en
- zh
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fr
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- ka
- kk
- km
- kn
- ko
- lt
- lv
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- "no"
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- uz
- vi
tags:
- qwen
- qwen3.5
- prism
- moe
- multimodal
- vision
- hybrid-attention
- gguf
- finetuned
base_model:
- Qwen/Qwen3.5-122B-A10B
base_model_relation: finetune
pipeline_tag: image-text-to-text
library_name: llama.cpp
quantized_by: Ex0bit
---

[![Parameters](https://img.shields.io/badge/Parameters-122B_(10B_Active)-blue)]()
[![Format](https://img.shields.io/badge/Format-GGUF-red)]()
[![Quant](https://img.shields.io/badge/Quant-PRISM_Dynamic_(4.06_BPW)-yellow)]()
[![Multimodal](https://img.shields.io/badge/Multimodal-Vision%20%2B%20Text-purple)]()

---

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/63adf1fa42fd3b8dbaeb0c92/ErhMZ5g6hiB4AIya6peif.png" width="400"/>
</p>

---

<div align="center">

### Get PRISM-PRO Models on Day-0 & Support Our Research & Development efforts

[**PRISM-LITE Version**](https://hf.co/Ex0bit/Qwen3.5-122B-A10B-PRISM-LITE-GGUF/) | [**PRISM VIP Memberships**](https://ko-fi.com/summary/6bae206c-a751-4868-8dc7-f531afd1fb4c) | [**Ko-fi**](https://ko-fi.com/Ex0bit) | [**Direct Model Purchase**](https://ko-fi.com/s/741ff3bad9)  

</div>

---

# Qwen3.5-122B-A10B-PRISM-PRO-GGUF

GGUF quantized versions of [Qwen3.5-122B-A10B-PRISM-PRO](https://huggingface.co/Ex0bit/Qwen3.5-122B-A10B-PRISM-PRO) -- an unrestricted PRISM Production model with full over-refusal and bias mechanisms completely removed using our State of the Art **PRISM pipeline** (**P**rojected **R**efusal **I**solation via **S**ubspace **M**odification).

---

<div align="center">

If you find PRISM models useful, please consider supporting development:

[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20PRISM-ff5e5b?logo=ko-fi&logoColor=white)](https://ko-fi.com/Ex0bit)

</div>

---

## Available Quantizations

| Quantization | Size | BPW | Description |
|---|---|---|---|
| **[Dynamic](Dynamic/)** | 57.7 GB | 4.06 | PRISM Dynamic -- forensic per-block quantization with 5-tier `ffn_down_exps` allocation |

### PRISM Dynamic Quantization

This is not a standard uniform quantization. PRISM Dynamic uses **forensic per-block analysis** derived from comprehensive KLD sensitivity scoring to assign optimal quantization types to each tensor block individually:

- **Critical blocks** (convergence + exit layers): Q6_K (6.6 BPW)
- **High-impact blocks** (entry zone): Q5_K_M (5.5 BPW)
- **Standard blocks** (bulk processing): Q4_K_M (4.8 BPW)
- **Low-sensitivity blocks**: IQ4_XS (4.25 BPW)
- **Cold blocks** (lowest sensitivity): IQ3_XXS (3.06 BPW)

All attention tensors are preserved at Q8_0. All norms and routing weights are kept at F32. The imatrix used for information-sensitive quantization types is included.

### Included Files

```
Dynamic/
  Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf   -- Dynamic quant (57.7 GB)
  mmproj-Qwen3.5-122B-A10B-PRISM-PRO.gguf     -- Vision encoder (871 MB)
  imatrix.dat                                   -- Importance matrix (342 MB)
```

---

## Model Highlights

- **PRISM Ablation** -- State-of-the-art technique that removes over-refusal behaviors while preserving model capabilities.
- **122B Hybrid MoE Architecture** -- 122 billion total parameters with 10 billion active per token across 256 routed experts + 1 shared expert per layer.
- **Hybrid Attention** -- Novel GatedDeltaNet linear attention (36 layers) combined with full attention (12 layers) for efficient long-context processing.
- **Native Multimodal** -- Vision encoder included as `mmproj` GGUF for seamless image and video understanding.
- **262K Full Context Window** -- Native 262,144 token context length.
- **Dual Modes** -- Supports both Thinking (deep reasoning) and Instant (direct response) modes.

---

## Usage

### llama.cpp (Recommended)

```bash
# Text-only inference
./llama-cli \
  -m Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf \
  -p "Hello! Tell me about quantum computing." \
  -n 2048 -ngl 999 --temp 0.7

# With vision (multimodal)
./llama-mtmd-cli \
  -m Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf \
  --mmproj mmproj-Qwen3.5-122B-A10B-PRISM-PRO.gguf \
  --image photo.jpg \
  -p "Describe this image in detail." \
  -n 2048 -ngl 999

# Server mode
./llama-server \
  -m Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf \
  --mmproj mmproj-Qwen3.5-122B-A10B-PRISM-PRO.gguf \
  -ngl 999 --port 8080
```

### koboldcpp

```bash
koboldcpp \
  --model Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf \
  --mmproj mmproj-Qwen3.5-122B-A10B-PRISM-PRO.gguf \
  --gpulayers 999 \
  --contextsize 8192
```

### Ollama

```bash
# Create a Modelfile
cat > Modelfile << 'EOF'
FROM ./Qwen3.5-122B-A10B-PRISM-PRO-Dynamic.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.95
PARAMETER top_k 20
EOF

ollama create prism-pro -f Modelfile
ollama run prism-pro
```

---

## Hardware Requirements

| Setup | VRAM Required | Notes |
|---|---|---|
| **Dynamic (GPU only)** | ~60 GB | Fits on 1x A100 80GB or 1x H100 80GB |
| **Dynamic (GPU + CPU offload)** | 48+ GB GPU + RAM | Offload some layers to CPU |
| **Dynamic (CPU only)** | 64+ GB RAM | Slower but functional |

---

## Benchmarks

| Benchmark | Qwen3.5-122B-A10B | GPT-5-mini | Qwen3-235B-A22B |
|---|---|---|---|
| MMLU-Pro | **86.7** | 83.7 | 84.4 |
| MMLU-Redux | **94.0** | 93.7 | 93.8 |
| GPQA Diamond | **86.6** | 82.8 | 81.1 |
| HMMT Feb 25 | **91.4** | 89.2 | 85.1 |
| SWE-bench Verified | **72.0** | **72.0** | -- |
| LiveCodeBench v6 | 78.9 | **80.5** | 75.1 |
| MMMU | **83.9** | 79.0 | 80.6 |
| VideoMME (w/ sub) | **87.3** | 83.5 | 83.8 |

> **Note:** Benchmark results are from the base Qwen3.5-122B-A10B model.

---

## License

Based on [Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) by the Qwen Team (Alibaba Group). Licensed under [Apache 2.0](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/main/LICENSE).

---

## Acknowledgments

Based on **Qwen3.5-122B-A10B** by the Qwen Team. GGUF conversion and quantization by [Ex0bit](https://huggingface.co/Ex0bit). See the [Qwen3.5 blog post](https://qwen.ai/blog?id=qwen3.5) for architecture details.

---

## Citation

```bibtex
@misc{qwen35prismpro_gguf,
    title  = {Qwen3.5-122B-A10B-PRISM-PRO-GGUF},
    author = {Ex0bit},
    month  = {February},
    year   = {2026}
}
```
