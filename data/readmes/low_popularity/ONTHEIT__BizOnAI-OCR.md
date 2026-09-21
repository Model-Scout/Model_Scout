---
language:
- ko
- en
tags:
- ocr
- document-understanding
- korean
- vlm
- vision-language
license: openrail
base_model: Qwen/Qwen3-VL-8B-Instruct
pipeline_tag: image-text-to-text
library_name: transformers
---

# BizOnAI-OCR

A **Korean-optimized** OCR model for industrial document processing developed by [ONTHEIT](http://www.ontheit.com/).

Built on [Qwen3-VL-8B](https://github.com/QwenLM/Qwen3-VL), BizOnAI-OCR is tuned for real-world Korean documents — contracts, medical records, financial forms, government paperwork, and more. It handles Korean-specific layouts, mixed Korean/English/Chinese text, decorative spacing, vertical tables, and complex forms that trip up general-purpose OCR models.

## Highlights

- **Korean-first**: fine-tuned on Korean industrial documents
- **Bilingual**: remains competitive on English OCR benchmarks
- **Markdown output**: structured output with tables, headings, and formatting preserved
- **vLLM-ready**: served efficiently via vLLM (OpenAI-compatible API) or plain `transformers`

## Benchmark Results

### KDoc-OCRBench (Korean)

Evaluated on [KDoc-OCRBench](https://huggingface.co/datasets/ONTHEIT/KDoc-OCRBench) — 14,738 unit-test-style assertions across 804 Korean industrial PDFs.

| Model | Baseline | Header/Footer | Long Text | Table | **Overall** |
|-------|---------:|--------------:|----------:|------:|------------:|
| **BizOnAI-OCR** | 98.1 | 88.8 | 77.0 | 68.0 | **83.0** |
| olmOCR v0.2.0 | 99.9 | 88.5 | 73.7 | 53.4 | 78.9 |
| PaddleOCR-VL | 100.0 | 90.5 | 65.7 | 57.6 | 78.4 |
| DeepSeek OCR | 99.8 | 88.3 | 66.0 | 53.1 | 76.8 |
| GLM OCR | 99.9 | 96.3 | 41.8 | 31.0 | 67.2 |

### olmOCR-bench (English)

Evaluated on [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) by Allen AI.

| Model | ArXiv | Old Scans Math | Tables | Old Scans | Headers & Footers | Multi Column | Long Tiny Text | Base | Overall |
|-------|------:|---------------:|-------:|----------:|------------------:|-------------:|---------------:|-----:|--------:|
| **BizOnAI-OCR** | 84.0 | 74.2 | 89.7 | 47.3 | 92.4 | 80.2 | 92.5 | 98.7 | 82.4 |
| PaddleOCR-VL | 85.7 | 71.0 | 84.1 | 37.8 | 97.0 | 79.9 | 85.7 | 98.5 | 80.0 |
| olmOCR v0.2.0 | 78.8 | 77.5 | 71.9 | 45.4 | 94.2 | 78.6 | 81.4 | 99.8 | 78.5 |
| DeepSeek OCR | 77.2 | 73.6 | 80.2 | 33.3 | 96.1 | 66.4 | 79.4 | 99.8 | 75.7 |

## Quick Start

Full installation instructions, CLI tools, and the benchmark pipeline are in the [GitHub repository](https://github.com/ONTHEIT-AI/BizOnAI-OCR).

### Serve with vLLM (recommended)

```bash
python -m vllm.entrypoints.openai.api_server \
    --model ONTHEIT/BizOnAI-OCR \
    --port 8000 \
    --dtype bfloat16 \
    --max-model-len 16384 \
    --trust-remote-code \
    --served-model-name bizonai-ocr
```

### Python CLI

```bash
git clone https://github.com/ONTHEIT-AI/BizOnAI-OCR.git
cd BizOnAI-OCR && uv venv && source .venv/bin/activate
uv pip install -e .
bizonai-ocr input.pdf ./output
```

## Tested Environment

Python 3.12, vllm==0.11.0, transformers==4.57.6, torch==2.8.0+cu128 (CUDA 12.8)

## Credits

- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) by Alibaba
- [olmocr](https://github.com/allenai/olmocr) by Allen AI
- [olmOCR-bench](https://huggingface.co/datasets/allenai/olmOCR-bench) by Allen AI
- [vLLM](https://github.com/vllm-project/vllm)

## License

This repository is released under the Apache2.0 and OpenRAIL. See the [LICENSE](https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/main/LICENSE) file for details.
