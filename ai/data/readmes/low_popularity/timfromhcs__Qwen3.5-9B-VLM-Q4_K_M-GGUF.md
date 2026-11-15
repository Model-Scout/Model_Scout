---
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
  - th
  - vi
  - id
license: apache-2.0
library_name: llama.cpp
tags:
  - gguf
  - vlm
  - vision
  - multimodal
  - qwen3.5
  - quantized
  - llama-cpp
  - on-device
  - ios
  - mobile
base_model: Qwen/Qwen3.5-9B
pipeline_tag: image-text-to-text
quantized_by: jc-builds
model_type: qwen3
---

# Qwen3.5-9B VLM Q4_K_M GGUF

> **Ready-to-run Vision Language Model** — bundled Q4\_K\_M quantization + multimodal projector for immediate VLM inference with llama.cpp.

## Overview

This repository provides a **complete, self-contained VLM package** for [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) in GGUF format. Unlike text-only GGUF repos, this includes the **multimodal projector (mmproj)** required for vision capabilities — no need to hunt for separate files.

| File | Description | Size |
|------|-------------|------|
| `Qwen3.5-9B-Q4_K_M.gguf` | Main model weights (4-bit quantized) | ~6.0 GB |
| `mmproj-F16.gguf` | Vision encoder projection (FP16) | ~918 MB |

**Total VRAM/RAM required:** ~7–8 GB for full VLM inference

## Key Features

- **Natively Multimodal** — Qwen3.5 uses early fusion architecture where vision and language are jointly trained from the ground up, not bolted on as an afterthought
- **Outperforms Qwen3-VL** — Cross-generational improvements across visual understanding, reasoning, coding, and agent benchmarks
- **262K Context Length** — Native 262,144 token context window, extensible to 1M+ tokens
- **201 Languages** — Broad multilingual support including CJK, European, Arabic, Southeast Asian, and more
- **Efficient Quantization** — Q4\_K\_M provides an excellent balance of quality and size, retaining strong performance while fitting in ~6 GB

## Architecture

Qwen3.5 represents a paradigm shift from the separate "LLM + Vision Encoder" approach (used by Qwen3-VL, LLaVA, etc.) to a **unified early-fusion architecture**:

```
Image → Vision Encoder → Multimodal Projector (mmproj) ─┐
                                                         ├→ Unified Transformer → Output
Text → Token Embedding ─────────────────────────────────┘
```

The vision encoder processes images into visual tokens that are projected into the same embedding space as text tokens via the `mmproj` file, enabling seamless multimodal reasoning within a single transformer.

## Quickstart

### Prerequisites

- [llama.cpp](https://github.com/ggml-org/llama.cpp) (built from source or pre-built binaries)
- ~8 GB available RAM/VRAM

### Download

```bash
# Download both files
huggingface-cli download jc-builds/Qwen3.5-9B-VLM-Q4_K_M-GGUF \
  --local-dir Qwen3.5-9B-VLM-Q4_K_M-GGUF
```

### Run with llama.cpp CLI

```bash
# Image understanding
./llama-cli \
  --model Qwen3.5-9B-VLM-Q4_K_M-GGUF/Qwen3.5-9B-Q4_K_M.gguf \
  --mmproj Qwen3.5-9B-VLM-Q4_K_M-GGUF/mmproj-F16.gguf \
  --image your_image.jpg \
  -p "Describe what you see in this image in detail." \
  --temp 0.7 --top-p 0.9 \
  -n 512

# Text-only mode (omit --mmproj and --image)
./llama-cli \
  --model Qwen3.5-9B-VLM-Q4_K_M-GGUF/Qwen3.5-9B-Q4_K_M.gguf \
  -p "Explain quantum entanglement simply." \
  --temp 0.7 \
  -n 512
```

### Run with llama.cpp Server

```bash
./llama-server \
  --model Qwen3.5-9B-VLM-Q4_K_M-GGUF/Qwen3.5-9B-Q4_K_M.gguf \
  --mmproj Qwen3.5-9B-VLM-Q4_K_M-GGUF/mmproj-F16.gguf \
  --port 8080
```

Then send requests with images via the OpenAI-compatible API:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-9b-vlm",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
        ]
      }
    ]
  }'
```

### Use with iOS / On-Device (llama.cpp Swift bindings)

This model is optimized for on-device inference. Load both files in your llama.cpp-based iOS app:

```swift
// Load main model
let modelParams = llama_model_default_params()
let model = llama_model_load_from_file("Qwen3.5-9B-Q4_K_M.gguf", modelParams)

// Load vision projector
let clipModel = clip_model_load("mmproj-F16.gguf", /* verbosity */ 1)
```

## Quantization Details

| Property | Value |
|----------|-------|
| **Method** | Q4\_K\_M (4-bit, mixed precision) |
| **Base Model** | [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) |
| **Parameters** | 9.6B (dense) |
| **Vision Projector** | FP16 (full precision for visual quality) |
| **GQA Groups** | 4 |
| **Context Length** | 262,144 tokens |
| **Vocabulary** | 200K+ tokens |

Q4\_K\_M uses a mixed quantization strategy where more important layers retain higher precision, providing a strong quality-to-size ratio. The vision projector is kept at FP16 to preserve visual understanding fidelity.

## Compatibility

| Backend | Text | Vision | Notes |
|---------|:----:|:------:|-------|
| **llama.cpp** (CLI/Server) | Yes | Yes | Full support with `--mmproj` flag |
| **llama.cpp** (Swift/iOS) | Yes | Yes | Load both model + clip files |
| **LM Studio** | Yes | Partial | Check for mmproj support |
| **Ollama** | Yes | No | Does not support separate mmproj files yet |
| **KoboldCpp** | Yes | Yes | Supports `--mmproj` flag |

## Benchmarks

Qwen3.5-9B delivers exceptional performance across vision, text, and reasoning tasks — often matching or exceeding models many times its size.

> Note: Quantization to Q4\_K\_M typically results in minimal degradation (~1-2%) compared to FP16 for models of this size. All scores below are from the FP16 base model.

### Vision & Multimodal Performance

<p align="center">
  <img src="assets/vision_benchmarks.svg" width="100%" alt="Vision benchmark comparison"/>
</p>

<details>
<summary><b>Full Vision Benchmark Table</b> (click to expand)</summary>

| Benchmark | Qwen3.5-9B | GPT-5-Nano | Gemini 2.5 Flash | Qwen3-VL-30B |
|-----------|:----------:|:----------:|:----------------:|:------------:|
| **STEM & Puzzle** | | | | |
| MMMU | **78.4** | 75.8 | 73.4 | 76.0 |
| MMMU-Pro | **70.1** | 57.2 | 59.7 | 63.0 |
| MathVision | **78.9** | 62.2 | 52.1 | 65.7 |
| MathVista (mini) | **85.7** | 71.5 | 72.8 | 81.9 |
| We-Math | **75.2** | 62.5 | 32.1 | 70.0 |
| DynaMath | **83.6** | 78.0 | 69.9 | 80.1 |
| VLMs Are Blind | **93.7** | 66.7 | 68.4 | 72.5 |
| **General VQA** | | | | |
| RealWorldQA | **80.3** | 71.8 | 72.2 | 77.4 |
| MMStar | **79.7** | 68.6 | 69.1 | 75.5 |
| MMBench EN v1.1 | **90.1** | 80.3 | 82.7 | 88.9 |
| HallusionBench | **69.3** | 58.4 | 64.5 | 66.0 |
| **OCR & Documents** | | | | |
| OmniDocBench 1.5 | **87.7** | 55.9 | 79.4 | 86.8 |
| CharXiv (RQ) | **73.0** | 50.1 | 56.1 | 56.6 |
| MMLongBench-Doc | **57.7** | 31.8 | 46.5 | 47.4 |
| CC-OCR | **79.3** | 58.9 | 72.9 | 77.8 |
| AI2D | **90.2** | 81.9 | 85.7 | 86.9 |
| OCRBench | **89.2** | 75.3 | 82.5 | 83.9 |
| **Spatial Intelligence** | | | | |
| CountBench | **97.2** | 80.0 | 79.2 | 90.0 |
| EmbSpatialBench | **83.0** | 74.2 | 66.1 | 80.6 |
| RefSpatialBench | **58.5** | 12.6 | 11.2 | 54.2 |
| LingoQA | **80.4** | 57.0 | 17.8 | 62.0 |
| **Video Understanding** | | | | |
| VideoMME (w/ sub) | **84.5** | 71.7 | 74.6 | 79.9 |
| VideoMME (w/o sub) | **78.4** | 66.2 | 72.7 | 73.3 |
| VideoMMMU | **78.9** | 63.0 | 69.2 | 75.0 |
| MLVU | **84.4** | 69.2 | 78.5 | 78.9 |
| MMVU | **67.8** | 63.1 | 65.3 | 66.1 |
| **Visual Agent** | | | | |
| ScreenSpot Pro | **65.2** | — | — | 60.5 |
| OSWorld | **41.8** | — | — | 30.6 |
| AndroidWorld | 57.8 | — | — | 55.0 |
| **Medical VQA** | | | | |
| SLAKE | **79.0** | 57.0 | 65.0 | 68.8 |
| PMC-VQA | **57.9** | 37.8 | 48.8 | 51.5 |
| MedXpertQA-MM | **49.9** | 26.7 | 35.3 | 35.5 |

</details>

### Capability Radar

<p align="center">
  <img src="assets/radar_chart.svg" width="520" alt="Capability radar chart"/>
</p>

### Text & Reasoning Performance

<p align="center">
  <img src="assets/text_benchmarks.svg" width="100%" alt="Text benchmark comparison"/>
</p>

<details>
<summary><b>Full Text Benchmark Table</b> (click to expand)</summary>

| Benchmark | Qwen3.5-9B | GPT-OSS-120B | Qwen3-30B-A3B |
|-----------|:----------:|:------------:|:-------------:|
| **Knowledge & STEM** | | | |
| MMLU-Pro | **82.5** | 80.8 | 80.9 |
| MMLU-Redux | **91.1** | 91.0 | 91.4 |
| GPQA Diamond | **81.7** | 80.1 | 73.4 |
| SuperGPQA | **58.2** | 54.6 | 56.8 |
| C-Eval | **88.2** | 76.2 | 87.4 |
| **Instruction Following** | | | |
| IFEval | **91.5** | 88.9 | 88.9 |
| IFBench | 64.5 | **69.0** | 51.5 |
| MultiChallenge | **54.5** | 45.3 | 46.5 |
| **Reasoning & Math** | | | |
| HMMT Feb '25 | 83.2 | **90.0** | 63.1 |
| HMMT Nov '25 | 82.9 | **90.0** | 73.8 |
| LiveCodeBench v6 | 65.6 | **82.7** | 66.0 |
| OJBench | 29.2 | **41.5** | 25.1 |
| **Long Context** | | | |
| LongBench v2 | **55.2** | 48.2 | 44.8 |
| AA-LCR | **63.0** | 50.7 | 49.0 |
| **Agent & Tool Use** | | | |
| BFCL-V4 | **66.1** | — | 42.4 |
| TAU2-Bench | **79.1** | — | 41.9 |
| VITA-Bench | **29.8** | — | 14.1 |
| **Multilingual** | | | |
| MMMLU | **81.2** | 78.2 | 78.4 |
| MMLU-ProX | **76.3** | 74.5 | 69.1 |
| NOVA-63 | **55.9** | 51.1 | 52.5 |
| INCLUDE | **75.6** | 74.0 | 74.4 |
| WMT24++ | 72.6 | **74.4** | 69.3 |

</details>

## Credits & Acknowledgments

- **Base Model:** [Qwen Team, Alibaba Cloud](https://huggingface.co/Qwen/Qwen3.5-9B)
- **mmproj Extraction:** Derived from [unsloth/Qwen3.5-9B-GGUF](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF)
- **Quantization Format:** [GGML / llama.cpp](https://github.com/ggml-org/llama.cpp)

## License

This model is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0), consistent with the base Qwen3.5-9B model.

## Citation

```bibtex
@article{qwen3.5,
  title={Qwen3.5 Technical Report},
  author={Qwen Team},
  year={2025},
  url={https://qwen.ai/blog?id=qwen3.5}
}
```

---

<p align="center">
  <i>Packaged by <a href="https://huggingface.co/jc-builds">jc-builds</a> for easy on-device VLM deployment.</i>
</p>
