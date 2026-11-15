---
license: apache-2.0
base_model:
  - FINAL-Bench/Darwin-27B-Opus
  - Qwen/Qwen3.5-27B
tags:
  - qwen3.5
  - korean
  - korean-sft
  - reasoning
  - thinking
  - ginigen-ai
  - rogue
  - k-ai
  - merge
language:
  - ko
  - en
  - ja
  - zh
  - multilingual
pipeline_tag: text-generation
library_name: transformers
---

# Rogue-27B-KR — Korean-Specialized High-Performance Reasoning Model

<p align="center">
  <img src="https://img.shields.io/badge/Korean_AI-Rogue--27B--KR-red?style=for-the-badge" alt="Rogue-27B-KR">
  <img src="https://img.shields.io/badge/K--AI_Leaderboard-2nd_Place-gold?style=for-the-badge" alt="K-AI 2nd">
  <img src="https://img.shields.io/badge/Base-Darwin--27B--Opus-blue?style=for-the-badge" alt="Base">
  <img src="https://img.shields.io/badge/License-Apache_2.0-green?style=for-the-badge" alt="License">
</p>

> **Qwen3.5 Hybrid Architecture | ~26B Params | Thinking Mode | 262K Context | BF16 | Apache 2.0**
> **Darwin-27B-Opus(Father) + Korean-SFT Qwen 27B(Mother) Merge + Korean SFT**

---

## K-AI Leaderboard — 2nd Place

> **K-AI Leaderboard** is operated by the Korean Ministry of Science and ICT (MSIT) / NIA, evaluating Korean AI language models across multiple benchmarks.

**Rogue-27B-KR achieved 2nd place** on the K-AI Leaderboard with an average score of **0.549**.

<p align="center">
  <img src="assets/l1.png" width="800" alt="K-AI Leaderboard Ranking">
</p>

| Metric | Score |
|---|---|
| **Average** | **0.549** |
| KMMLU-Pro | 0.658 |
| CLIcK | 0.794 |
| HLE(Ko) | 0.07 |
| MuSR(Ko) | 0.584 |
| Com2-main(Ko) | 0.646 |

<p align="center">
  <img src="assets/l2.png" width="800" alt="K-AI Leaderboard Charts">
</p>

---

## Model Overview

**Rogue-27B-KR** is a Korean-specialized high-performance reasoning model:

- **Father**: [FINAL-Bench/Darwin-27B-Opus](https://huggingface.co/FINAL-Bench/Darwin-27B-Opus) — Evolutionary merge model based on Qwen3.5-27B (inheriting Claude 4.6 Opus reasoning patterns)
- **Mother**: Korean-specialized SFT applied Qwen 27B variant
- **Rogue**: Merged both parents + additional Korean SFT

Combines Darwin's powerful reasoning with the mother model's Korean expressiveness, greatly enhancing Korean intelligence across culture, language, law, history, and more.

### Key Features

- **K-AI Leaderboard 2nd Place** — Top-tier Korean AI performance verified by government evaluation
- **Strong reasoning** — Chain-of-Thought inherited from Darwin-27B-Opus
- **Enhanced Korean cultural intelligence** — +6%p improvement on CLIcK benchmark (0.794)
- **262K context** — Ultra-long Korean document processing
- **Thinking mode** — Step-by-step reasoning via `<think>` tags
- **BF16 format** — Memory-efficient (~48GB), optimized for modern GPUs
- **Apache 2.0** — Free for commercial use

---

## Benchmark Results

### CLIcK (Cultural and Linguistic Intelligence in Korean)

200 questions, 0-shot evaluation:

| Model | CLIcK (Overall) | Culture | Language |
|---|---|---|---|
| Qwen3.5-27B (base) | 69.52% | 71.84% | 64.66% |
| Darwin-27B-Opus | 70.19% | 72.91% | 64.47% |
| **Rogue-27B-KR** | **75.59%** | **77.85%** | **70.86%** |

> **+6.07%p** over Qwen3.5-27B, **+5.40%p** over Darwin-27B-Opus

### Category Details

| Category | Qwen3.5-27B | Darwin-27B-Opus | **Rogue-27B-KR** |
|---|---|---|---|
| Economy | 93.22% | 93.22% | **94.92%** |
| Geography | 70.23% | 70.23% | **75.57%** |
| History | 47.00% | 47.00% | **53.50%** |
| K-pop | 92.68% | 97.56% | 92.68% |
| Law | 59.50% | 60.00% | **69.50%** |
| Politics | 80.95% | 82.14% | **85.71%** |
| Society | 87.00% | 89.00% | **90.00%** |
| Tradition | 81.50% | 82.50% | **88.50%** |
| Function Words | 68.18% | 67.42% | **75.00%** |
| Grammar | 44.50% | 44.50% | **53.00%** |
| Text | 82.50% | 82.50% | **86.00%** |

---

## Model Specifications

| Property | Value |
|---|---|
| **Architecture** | Qwen3.5 (GatedDeltaNet Hybrid Attention, 64-layer) |
| **Parameters** | ~26B (text-only, no vision encoder) |
| **Hidden Size** | 5120 |
| **Intermediate Size** | 16384 |
| **Layers** | 64 |
| **Attention Heads** | 24 (GQA, KV Heads: 4) |
| **Context Length** | 262,144 tokens (1M with YaRN) |
| **Precision** | **BF16** (~48GB) |
| **Vocab Size** | 248,320 |
| **Thinking** | Supported (`<think>` tags) |
| **Languages** | Korean, English, Japanese, Chinese + 201 languages |
| **License** | Apache 2.0 |

---

## VRAM Requirements

| Setup | VRAM | Notes |
|---|---|---|
| BF16 (native) | ~48 GB | Single H100/B200 or 2x A100 |
| 4-bit quantized | ~14 GB | Single RTX 4090 |
| 8-bit quantized | ~26 GB | Single A6000 |

---

## Usage

> **Requirements**: `transformers >= 4.57.0` (Qwen3.5 support). Latest recommended:
> `pip install -U transformers`

### Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("ginigen-ai/Rogue-27B-KR")
model = AutoModelForCausalLM.from_pretrained(
    "ginigen-ai/Rogue-27B-KR",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [{"role": "user", "content": "Explain traditional Korean wedding ceremonies."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=4096, do_sample=False)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### vLLM

```bash
vllm serve ginigen-ai/Rogue-27B-KR \
    --enforce-eager \
    --max-model-len 32768 \
    --dtype bfloat16
```

### SGLang

```bash
python -m sglang.launch_server \
    --model-path ginigen-ai/Rogue-27B-KR \
    --tp 1 \
    --mem-fraction-static 0.90 \
    --context-length 32768 \
    --dtype bfloat16 \
    --reasoning-parser qwen3
```

---

## Training Info

| Item | Details |
|---|---|
| **Father model** | [FINAL-Bench/Darwin-27B-Opus](https://huggingface.co/FINAL-Bench/Darwin-27B-Opus) — Reasoning |
| **Mother model** | Korean-SFT Qwen 27B variant — Korean expressiveness |
| **Merge** | Weight merge (intermediate_size 16384 adopted) |
| **Additional SFT** | Korean-specialized Supervised Fine-Tuning |
| **Developer** | [GinigenAI](https://huggingface.co/ginigen-ai) |

### Lineage

```
Qwen/Qwen3.5-27B (Apache 2.0)
+-- FINAL-Bench/Darwin-27B-Opus (evolutionary merge)  <- Father
|
+-- Korean-SFT Qwen 27B (Korean specialization)       <- Mother
        |
    [Merge: Father + Mother]
        |
    [Additional Korean SFT]
        |
    ginigen-ai/Rogue-27B-KR (this model, BF16)
```

---

## Citation

```bibtex
@misc{ginigen_rogue_27b_kr_2026,
  title        = {Rogue-27B-KR: Korean-Specialized High-Performance Reasoning Model},
  author       = {GinigenAI},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ginigen-ai/Rogue-27B-KR}}
}
```

---

## Acknowledgements

- [VIDRAFT](https://huggingface.co/FINAL-Bench) — Darwin-27B-Opus base model
- [Qwen Team](https://huggingface.co/Qwen) — Qwen3.5 architecture
- Korean Ministry of Science and ICT / NIA — K-AI Leaderboard

---

*Built by GinigenAI for the Korean AI community*

## 학습 데이터셋

본 모델은 **AI Hub**(과학기술정보통신부·NIA 구축) 공개 한국어 말뭉치로 파인튜닝되었습니다.

✅ [전문 의학지식 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71874)
✅ [한국어 생성 기반 상식추론 데이터셋](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=459)
✅ [금융·법률 문서 기계독해 데이터](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71610)
✅ [국가기록물 초거대 AI 학습 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71788)
✅ [대규모 구매도서 기반 한국어 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=653)
✅ [멀티세션·대화 관련 말뭉치 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=511&topMenu=100&aihubDataSe=dataPckage&dataPckageSn=1)
✅ [한국어 대화 데이터셋](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=272)
