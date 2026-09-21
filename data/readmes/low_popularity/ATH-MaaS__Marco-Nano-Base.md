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

# Marco-Nano-Base

**Marco-Nano-Base** is a compact, highly sparse Mixture-of-Experts (MoE) multilingual language model from the [Marco-MoE](https://github.com/AIDC-AI/Marco-LLM) family, developed by Alibaba International Digital Commerce. It activates only **0.6B out of 8B total parameters** (7.5% activation ratio) per token, achieving strong English and multilingual performance across 29 languages while requiring significantly less compute than comparable dense models.

## Model Description

Marco-Nano is built on a decoder-only Transformer architecture with sparse MoE layers replacing standard FFN layers. It is upcycled from [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) using a fine-grained sub-matrix splitting strategy combined with Drop-Upcycling to promote expert diversification.

| Configuration | Value |
|:---|:---:|
| Total Parameters | 8B |
| Activated Parameters | 0.6B |
| Activation Ratio | 7.5% |
| Num Layers | 28 |
| Model Dimension | 1024 |
| FFN Intermediate Dimension | 3072 |
| Q-Heads | 16 |
| KV-Heads | 8 |
| Head Dimension | 128 |
| Expert Dimension | 384 |
| Total Experts | 232 |
| Activated Experts | 8 |
| Tie Embeddings | True |
| Training FLOPs | $1.40 \times 10^{23}$ |

## Training Details

Marco-Nano was pre-trained on **5.1 trillion tokens** using a four-stage curriculum:

1. **Stage 1 (0 - 2.4T tokens): Foundational Training** — High-quality English data (Nemotron-CC-v2), reasoning and instruction data, and multilingual web/QA data for 19 languages.
2. **Stage 2 (2.4T - 4.1T tokens): Optimization & Upsampling** — Upsampled reasoning corpora, downsampled English web data, and upsampled Chinese data with learning rate decay.
3. **Stage 3 (4.1T - 4.6T tokens): Language Expansion** — Added 9 new languages (Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani) and upsampled medium-resource languages.
4. **Stage 4 (4.6T - 5.1T tokens): Synthetic Data Integration** — Curated multilingual synthetic data including cultural content (Fineweb2-Culture) and synthetic regional MCQs.

## Supported Languages

English, Chinese, Arabic, German, Spanish, French, Korean, Japanese, Portuguese, Turkish, Indonesian, Italian, Dutch, Polish, Russian, Vietnamese, Thai, Hebrew, Ukrainian, Malay, Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani

## Evaluation

We compare Marco-Nano against size-matched baselines: **Qwen3-1.7B** (1.7B activated), **Trinity Nano** (1.09B activated), and **Granite4-Tiny** (1.47B activated). Marco-Nano uses only **0.6B activated parameters** — the smallest among all baselines.

### English

| Benchmark | # Shots | Qwen3-1.7B | Trinity Nano | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|
| MMLU _(Acc)_ | 5-shot | 65.1 | 64.7 | **69.1** | 64.7 |
| MMLU-Redux _(Acc)_ | 0-shot | 61.2 | 60.1 | **65.8** | 62.9 |
| MMLU-Pro _(Acc)_ | 5-shot | 33.2 | 32.0 | 32.1 | **35.9** |
| AGIEval _(Acc)_ | 0-shot | 35.9 | 31.4 | 36.1 | **38.4** |
| BBH _(EM)_ | 3-shot | 54.5 | 49.3 | **59.9** | 53.5 |
| ARC-Easy _(Acc)_ | 0-shot | 69.3 | 77.9 | **78.5** | 75.3 |
| ARC-Challenge _(Acc)_ | 0-shot | 42.8 | **53.5** | 52.3 | 49.4 |
| HellaSwag _(Acc)_ | 0-shot | 66.6 | 77.4 | **77.9** | 69.2 |
| WinoGrande _(Acc)_ | 0-shot | 57.1 | 57.1 | **58.6** | 53.4 |
| BoolQ _(Acc)_ | 0-shot | **74.6** | 71.5 | 63.5 | 71.2 |
| CommonsenseQA _(Acc)_ | 0-shot | 49.5 | 54.1 | **55.9** | 55.7 |
| OpenBookQA _(Acc)_ | 0-shot | 36.4 | 42.0 | **43.6** | 39.4 |
| PIQA _(Acc)_ | 0-shot | 75.5 | 69.6 | **80.6** | 76.5 |
| SIQA _(Acc)_ | 0-shot | 47.8 | 52.7 | **53.0** | 46.0 |
| GSM8K _(EM)_ | 5-shot | 69.1 | 57.8 | **70.7** | 69.7 |
| **Average** | - | 55.9 | 56.7 | **59.8** | 57.5 |

### Multilingual — General

| Benchmark | # Shots | Qwen3-1.7B | Trinity Nano | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|
| GlobalMMLU _(Acc)_ | 5-shot | 49.6 | 43.6 | **54.8** | 52.2 |
| MMMLU _(Acc)_ | 0-shot | 48.6 | 41.2 | 52.3 | **52.6** |
| MMLU-ProX-Lite _(Acc)_ | 5-shot | 27.2 | 20.3 | **30.1** | 28.9 |
| BELEBELE _(Acc)_ | 0-shot | 67.5 | 54.5 | 61.2 | **73.8** |
| mHellaSwag _(Acc_norm)_ | 0-shot | 43.9 | 42.5 | **53.2** | 48.8 |
| mARC-Challenge _(Acc_norm)_ | 0-shot | 34.7 | 30.9 | **39.9** | 36.9 |
| FLORES-200 En→Xx _(BLEU)_ | 5-shot | 18.6 | 15.1 | **25.4** | 24.7 |
| FLORES-200 Xx→En _(BLEU)_ | 5-shot | 31.5 | 31.1 | **36.7** | 33.6 |
| WMT24++ En→Xx _(BLEU)_ | 5-shot | 18.3 | 15.0 | **21.9** | 20.7 |
| WMT24++ Xx→En _(BLEU)_ | 5-shot | 28.3 | 28.0 | **30.7** | 28.1 |
| MGSM _(EM)_ | 8-shot | 58.8 | 40.6 | 56.7 | **65.3** |
| **Average** | - | 38.8 | 33.0 | 42.1 | **42.3** |

### Multilingual — Cultural & Regional

| Benchmark | # Shots | Qwen3-1.7B | Trinity Nano | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|
| INCLUDE _(Acc)_ | 5-shot | 51.2 | 43.9 | 52.1 | **53.2** |
| Global-PIQA _(Acc_norm)_ | 0-shot | 60.3 | 52.3 | 64.0 | **64.3** |
| CMMLU _(Acc)_ | 5-shot | **66.1** | 49.6 | 53.5 | 55.5 |
| C-Eval _(Acc)_ | 5-shot | **65.1** | 47.6 | 50.9 | 56.0 |
| ArabicMMLU _(Acc)_ | 3-shot | 57.6 | 44.0 | **60.5** | 55.8 |
| TurkishMMLU _(Acc)_ | 5-shot | 47.9 | 29.6 | 41.8 | **48.9** |
| GreekMMLU _(Acc)_ | 5-shot | 58.1 | 52.2 | 62.3 | **64.1** |
| KazakhMMLU _(Acc)_ | 5-shot | 52.1 | 43.1 | 52.6 | **53.1** |
| IndoMMLU _(Acc)_ | 0-shot | **51.0** | 41.5 | 49.0 | **51.0** |
| IndoCareer _(Acc)_ | 3-shot | **53.9** | 46.7 | 53.0 | 52.1 |
| IndoCulture _(Acc)_ | 0-shot | 51.6 | 49.8 | 51.3 | **57.4** |
| **Average** | - | **55.9** | 45.5 | 53.7 | 55.6 |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "AIDC-AI/Marco-Nano-Base"
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
