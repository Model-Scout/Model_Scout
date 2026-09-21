---
license: apache-2.0
language:
- en
- zh
- ar
- de
- es
- fr
- ko
- ja
- pt
- tr
- id
- it
- nl
- pl
- ru
- vi
- th
- he
- uk
- ms
- bn
- cs
- ur
- kk
- el
- ro
- hu
- ne
- az
library_name: transformers
tags:
- moe
- mixture-of-experts
- multilingual
- upcycling
datasets:
- nvidia/Nemotron-CC-v2
- nvidia/Nemotron-Pretraining-SFT-v1
- nvidia/Nemotron-Pretraining-Specialized-v1
- nvidia/Nemotron-CC-v2.1
- allenai/dolmino-mix-1124
- nvidia/Nemotron-CC-Math-v1
- nvidia/OpenMathInstruct-2
- HuggingFaceTB/finemath
- LLM360/MegaMath
- open-thoughts/OpenThoughts3-1.2M
- opencsg/Fineweb-Edu-Chinese-V2.1
- HuggingFaceFW/fineweb-2
- allenai/dolma3_dolmino_mix-100B-1125
---

# Marco-Mini-Base

**Marco-Mini-Base** is a compact, highly sparse Mixture-of-Experts (MoE) multilingual language model from the [Marco-MoE](https://github.com/AIDC-AI/Marco-LLM) family, developed by Alibaba International Digital Commerce. It activates only **0.86B out of 17.3B total parameters** (5% activation ratio) per token, matching or surpassing dense models with up to 4B parameters on English and multilingual benchmarks across 29 languages — while using **5.5x fewer training FLOPs** than Qwen3-4B.

## Model Description

Marco-Mini is built on a decoder-only Transformer architecture with sparse MoE layers replacing standard FFN layers. It is upcycled from [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) using a fine-grained sub-matrix splitting strategy combined with Drop-Upcycling to promote expert diversification.

| Configuration | Value |
|:---|:---:|
| Total Parameters | 17.3B |
| Activated Parameters | 0.86B |
| Activation Ratio | 5% |
| Num Layers | 28 |
| Model Dimension | 1024 |
| FFN Intermediate Dimension | 3072 |
| Q-Heads | 16 |
| KV-Heads | 8 |
| Head Dimension | 128 |
| Expert Dimension | 768 |
| Total Experts | 256 |
| Activated Experts | 8 |
| Tie Embeddings | True |
| Training FLOPs | $1.56 \times 10^{23}$ |

## Training Details

Marco-Mini was pre-trained on **5.1 trillion tokens** using a four-stage curriculum:

1. **Stage 1 (0 - 2.4T tokens): Foundational Training** — High-quality English data (Nemotron-CC-v2), reasoning and instruction data, and multilingual web/QA data for 19 languages.
2. **Stage 2 (2.4T - 4.1T tokens): Optimization & Upsampling** — Upsampled reasoning corpora, downsampled English web data, and upsampled Chinese data with learning rate decay.
3. **Stage 3 (4.1T - 4.6T tokens): Language Expansion** — Added 9 new languages (Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani) and upsampled medium-resource languages.
4. **Stage 4 (4.6T - 5.1T tokens): Synthetic Data Integration** — Curated multilingual synthetic data including cultural content (Fineweb2-Culture) and synthetic regional MCQs.

## Supported Languages

English, Chinese, Arabic, German, Spanish, French, Korean, Japanese, Portuguese, Turkish, Indonesian, Italian, Dutch, Polish, Russian, Vietnamese, Thai, Hebrew, Ukrainian, Malay, Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani

## Evaluation

We compare Marco-Mini against strong baselines: **Qwen3-4B** (4B activated), **Trinity Mini** (3.85B activated), **Gemma3-4B** (4B activated), **SmolLM3-3B** (3B activated), **Llama3.2-3B** (3B activated), and **Tiny-Aya-3.35B** (3.35B activated). Marco-Mini uses only **0.86B activated parameters** — far fewer than all baselines.

### English

| Benchmark | # Shots | Llama3.2-3B | SmolLM3-3B | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | Trinity Mini | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MMLU _(Acc)_ | 5-shot | 57.6 | 62.6 | 61.1 | 58.6 | **75.2** | 71.4 | 72.8 |
| MMLU-Redux _(Acc)_ | 0-shot | 56.9 | 58.4 | 57.7 | 51.7 | **71.3** | 68.2 | 68.8 |
| MMLU-Pro _(Acc)_ | 5-shot | 26.0 | 35.1 | 28.8 | 26.9 | **45.9** | 41.3 | 45.3 |
| AGIEval _(Acc)_ | 0-shot | 31.2 | 34.5 | 32.6 | 29.0 | **44.0** | 39.7 | 41.9 |
| BBH _(EM)_ | 3-shot | 47.1 | 60.0 | 52.2 | 46.8 | **72.3** | 57.6 | 65.1 |
| ARC-Easy _(Acc)_ | 0-shot | 71.8 | 78.5 | **82.6** | 76.5 | 75.0 | 80.6 | 82.4 |
| ARC-Challenge _(Acc)_ | 0-shot | 46.0 | 52.6 | 54.1 | 47.4 | 49.9 | **57.8** | 56.3 |
| HellaSwag _(Acc)_ | 0-shot | 75.6 | 76.1 | 76.7 | 71.0 | 74.4 | **82.8** | 77.4 |
| WinoGrande _(Acc)_ | 0-shot | 58.6 | 58.9 | **61.4** | 56.6 | 59.6 | 60.8 | 57.7 |
| BoolQ _(Acc)_ | 0-shot | 75.2 | **79.3** | 76.6 | 74.6 | 74.2 | 72.5 | 74.2 |
| CommonsenseQA _(Acc)_ | 0-shot | 60.4 | 55.4 | 61.1 | 60.4 | 52.9 | 57.7 | **61.5** |
| OpenBookQA _(Acc)_ | 0-shot | 42.2 | 40.4 | 42.6 | 40.4 | 42.6 | **44.8** | 44.6 |
| PIQA _(Acc)_ | 0-shot | 78.2 | 79.1 | 80.3 | 76.9 | 77.4 | 71.7 | **81.1** |
| SIQA _(Acc)_ | 0-shot | 51.0 | 49.8 | 50.4 | 49.9 | **53.0** | 52.5 | 49.4 |
| GSM8K _(EM)_ | 5-shot | 27.3 | 67.4 | 39.3 | 58.0 | **81.7** | 57.5 | 76.4 |
| **Average** | - | 53.7 | 59.2 | 57.2 | 55.5 | 63.3 | 61.1 | **63.7** |

### Multilingual — General

| Benchmark | # Shots | Llama3.2-3B | SmolLM3-3B | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | Trinity Mini | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| GlobalMMLU _(Acc)_ | 5-shot | 43.2 | 46.7 | 50.8 | 50.0 | 61.6 | 52.6 | **64.2** |
| MMMLU _(Acc)_ | 0-shot | 44.0 | 47.3 | 47.4 | 44.5 | 59.3 | 50.9 | **62.0** |
| MMLU-ProX-Lite _(Acc)_ | 5-shot | 22.4 | 28.3 | 24.3 | 24.3 | 38.5 | 32.2 | **39.2** |
| BELEBELE _(Acc)_ | 0-shot | 60.1 | 54.3 | 65.7 | 65.4 | **81.5** | 67.6 | 79.8 |
| mHellaSwag _(Acc_norm)_ | 0-shot | 49.0 | 49.6 | 55.2 | 53.5 | 53.2 | 51.5 | **58.6** |
| mARC-Challenge _(Acc_norm)_ | 0-shot | 34.2 | 36.1 | 41.5 | 37.2 | 42.5 | 37.5 | **45.4** |
| FLORES-200 En→Xx _(BLEU)_ | 5-shot | 23.5 | 19.7 | 32.1 | 30.2 | 25.4 | 13.7 | **32.3** |
| FLORES-200 Xx→En _(BLEU)_ | 5-shot | 34.6 | 30.3 | 39.7 | 37.3 | 36.8 | 24.1 | **40.1** |
| WMT24++ En→Xx _(BLEU)_ | 5-shot | 16.4 | 17.8 | 27.7 | 26.1 | 23.9 | 7.5 | **28.1** |
| WMT24++ Xx→En _(BLEU)_ | 5-shot | 28.9 | 27.4 | 34.0 | 32.7 | 32.9 | 10.6 | **34.4** |
| MGSM _(EM)_ | 8-shot | 22.4 | 50.8 | 36.6 | 38.4 | **76.0** | 57.2 | 75.6 |
| **Average** | - | 34.4 | 37.1 | 41.4 | 39.9 | 48.3 | 36.9 | **50.9** |

### Multilingual — Cultural & Regional

| Benchmark | # Shots | Llama3.2-3B | SmolLM3-3B | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | Trinity Mini | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| INCLUDE _(Acc)_ | 5-shot | 45.5 | 46.2 | 52.6 | 53.9 | 61.4 | 51.9 | **61.7** |
| Global-PIQA _(Acc_norm)_ | 0-shot | 62.2 | 60.9 | 69.4 | 67.9 | 65.4 | 57.2 | **72.3** |
| CMMLU _(Acc)_ | 5-shot | 44.1 | 50.1 | 50.2 | 58.8 | **76.2** | 58.6 | 68.0 |
| C-Eval _(Acc)_ | 5-shot | 43.1 | 47.9 | 48.5 | 57.6 | **76.6** | 57.1 | 66.0 |
| ArabicMMLU _(Acc)_ | 3-shot | 48.9 | 60.6 | 61.6 | 63.2 | 67.0 | 57.1 | **67.1** |
| TurkishMMLU _(Acc)_ | 5-shot | 36.7 | 28.4 | 43.7 | 45.2 | 60.6 | 43.0 | **62.7** |
| GreekMMLU _(Acc)_ | 5-shot | 56.4 | 64.0 | 63.4 | 66.3 | 69.4 | 59.7 | **70.3** |
| KazakhMMLU _(Acc)_ | 5-shot | 44.7 | 47.4 | 52.1 | 47.1 | 62.3 | 49.6 | **62.6** |
| IndoMMLU _(Acc)_ | 0-shot | 47.0 | 43.7 | 48.5 | 52.0 | **60.1** | 51.0 | 59.9 |
| IndoCareer _(Acc)_ | 3-shot | 48.6 | 47.7 | 53.4 | 56.6 | **61.5** | 55.2 | **61.5** |
| IndoCulture _(Acc)_ | 0-shot | 50.1 | 44.5 | 59.1 | 58.5 | 61.1 | 57.6 | **62.3** |
| **Average** | - | 47.9 | 49.2 | 54.8 | 57.0 | **65.6** | 54.4 | 65.0 |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "AIDC-AI/Marco-Mini-Base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

input_text = "The capital of France is"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Citation

```bibtex
@article{marco-moe,
  title={Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling},
  author={Fan Jiang, Yu Zhao, Chenyang Lyu, Tianqi Shi, Yichao Du, Feihu Jiang, Longyue Wang and Weihua Luo},
  year={2026}
}
```

## License

This model is released under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
