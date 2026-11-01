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
- da
- sv
- "no"
- ca
- gl
- cy
- ga
- eu
- hr
- lv
- lt
- sk
- sl
- et
- fi
- sr
- bg
- fa
- mt
- hi
- mr
- gu
- pa
- ta
- te
- tl
- jv
- km
- lo
- my
- am
- sw
- yo
- ig
- zu
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

# Marco-Mini-Global-Base

**Marco-Mini-Global-Base** is an extended variant of [Marco-Mini-Base](https://huggingface.co/AIDC-AI/Marco-Mini-Base) that scales linguistic coverage from 29 to **64 languages**. It is a highly sparse Mixture-of-Experts (MoE) multilingual language model from the [Marco-MoE](https://github.com/AIDC-AI/Marco-LLM) family, developed by Alibaba International Digital Commerce. It activates only **0.86B out of 17.3B total parameters** (5% activation ratio) per token while supporting 64 languages — demonstrating that the MoE architecture enables scalable language expansion without the interference typical of dense models.

## Model Description

Marco-Mini-Global shares the same architecture as Marco-Mini-Base: a decoder-only Transformer with sparse MoE layers replacing standard FFN layers, upcycled from [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) using fine-grained sub-matrix splitting combined with Drop-Upcycling.

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
| Training FLOPs | $1.584 \times 10^{23}$ |

## Training Details

Marco-Mini-Global-Base branches from the Stage-2 checkpoint of Marco-Mini-Base and recalibrates the data mixtures in Stages 3 and 4 to integrate pre-training corpora for 35 newly introduced languages. In total it was trained on 5.5T tokens.

The four-stage curriculum follows the same structure as Marco-Mini-Base:

1. **Stage 1 (0 - 2.4T tokens): Foundational Training** — High-quality English data (Nemotron-CC-v2), reasoning and instruction data, and multilingual web/QA data for 19 languages.
2. **Stage 2 (2.4T - 4.1T tokens): Optimization & Upsampling** — Upsampled reasoning corpora, downsampled English web data, and upsampled Chinese data with learning rate decay.
3. **Stage 3 (4.1T - 5T tokens): Language Expansion** — Recalibrated data mixtures to integrate 35 new languages alongside the original 29.
4. **Stage 4 (5T - 5.5T tokens): Synthetic Data Integration** — Curated multilingual synthetic data including cultural content and synthetic regional MCQs for all 64 languages.

## Supported Languages

**Original 29 languages:** English, Chinese, Arabic, German, Spanish, French, Korean, Japanese, Portuguese, Turkish, Indonesian, Italian, Dutch, Polish, Russian, Vietnamese, Thai, Hebrew, Ukrainian, Malay, Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani

**35 newly introduced languages:** Danish, Swedish, Norwegian, Catalan, Galician, Welsh, Irish, Basque, Croatian, Latvian, Lithuanian, Slovak, Slovenian, Estonian, Finnish, Serbian, Bulgarian, Persian, Maltese, Hindi, Marathi, Gujarati, Punjabi, Tamil, Telugu, Tagalog, Javanese, Khmer, Lao, Burmese, Amharic, Swahili, Yoruba, Igbo, Zulu

## Evaluation

We compare Marco-Mini-Global-Base against strong multilingual baselines: **Gemma3-4B** (4B activated), **Tiny-Aya-3.35B** (3.35B activated), and **Qwen3-4B** (4B activated). All benchmarks are evaluated across the full 64-language set. Marco-Mini-Global uses only **0.86B activated parameters** while preserving robust English proficiency (63.6 vs. 63.7 for the 29-language Marco-Mini) and increasing the multilingual advantage over Qwen3-4B from +2.6% to +3.6%.

### English

| Benchmark | # Shots | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | **Marco-Mini-Global** |
|:---|:---:|:---:|:---:|:---:|:---:|
| MMLU _(Acc)_ | 5-shot | 61.1 | 58.6 | **75.2** | 72.9 |
| MMLU-Redux _(Acc)_ | 0-shot | 57.7 | 51.7 | **71.3** | 68.9 |
| MMLU-Pro _(Acc)_ | 5-shot | 28.8 | 26.9 | **45.9** | 44.5 |
| AGIEval _(Acc)_ | 0-shot | 32.6 | 29.0 | **44.0** | 41.0 |
| BBH _(EM)_ | 3-shot | 52.2 | 46.8 | **72.3** | 65.0 |
| ARC-Easy _(Acc)_ | 0-shot | **82.6** | 76.5 | 75.0 | 82.4 |
| ARC-Challenge _(Acc)_ | 0-shot | 54.1 | 47.4 | 49.9 | **57.0** |
| HellaSwag _(Acc)_ | 0-shot | 76.7 | 71.0 | 74.4 | **77.2** |
| WinoGrande _(Acc)_ | 0-shot | **61.4** | 56.6 | 59.6 | 58.3 |
| BoolQ _(Acc)_ | 0-shot | **76.6** | 74.6 | 74.2 | 75.6 |
| CommonsenseQA _(Acc)_ | 0-shot | 61.1 | 60.4 | 52.9 | **61.2** |
| OpenBookQA _(Acc)_ | 0-shot | 42.6 | 40.4 | 42.6 | **45.0** |
| PIQA _(Acc)_ | 0-shot | 80.3 | 76.9 | 77.4 | **80.7** |
| SIQA _(Acc)_ | 0-shot | 50.4 | 49.9 | **53.0** | 48.4 |
| GSM8K _(EM)_ | 5-shot | 39.3 | 58.0 | **81.7** | 76.4 |
| **Average** | - | 57.2 | 55.5 | 63.3 | **63.6** |

### Multilingual — General

| Benchmark | # Shots | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | **Marco-Mini-Global** |
|:---|:---:|:---:|:---:|:---:|:---:|
| GlobalMMLU _(Acc)_ | 5-shot | 49.1 | 48.4 | 57.8 | **60.9** |
| MMMLU _(Acc)_ | 0-shot | 45.0 | 42.8 | 54.8 | **58.2** |
| MMLU-ProX-Lite _(Acc)_ | 5-shot | 23.3 | 23.5 | 35.6 | **36.2** |
| BELEBELE _(Acc)_ | 0-shot | 62.3 | 62.5 | 74.0 | **76.0** |
| mHellaSwag _(Acc_norm)_ | 0-shot | 51.9 | 50.3 | 48.5 | **54.4** |
| mARC-Challenge _(Acc_norm)_ | 0-shot | 39.3 | 35.7 | 39.3 | **41.2** |
| FLORES-200 En→Xx _(BLEU)_ | 5-shot | 27.9 | 25.6 | 25.8 | **29.5** |
| FLORES-200 Xx→En _(BLEU)_ | 5-shot | 39.2 | 37.2 | 33.4 | **40.2** |
| WMT24++ En→Xx _(BLEU)_ | 5-shot | **26.0** | 24.4 | 19.6 | **26.0** |
| WMT24++ Xx→En _(BLEU)_ | 5-shot | 34.4 | 32.9 | 31.2 | **34.5** |
| MGSM _(EM)_ | 8-shot | 35.7 | 36.6 | 69.1 | **71.7** |
| **Average** | - | 39.5 | 37.3 | 44.5 | **48.1** |

### Multilingual — Cultural & Regional

| Benchmark | # Shots | Gemma3-4B | Tiny-Aya-3.35B | Qwen3-4B | **Marco-Mini-Global** |
|:---|:---:|:---:|:---:|:---:|:---:|
| INCLUDE _(Acc)_ | 5-shot | 52.3 | 53.5 | 60.0 | **61.1** |
| Global-PIQA _(Acc_norm)_ | 0-shot | 67.8 | 66.7 | 61.8 | **70.2** |
| CMMLU _(Acc)_ | 5-shot | 50.2 | 58.8 | **76.2** | 67.9 |
| C-Eval _(Acc)_ | 5-shot | 48.5 | 57.6 | **76.6** | 66.2 |
| ArabicMMLU _(Acc)_ | 3-shot | 61.6 | 63.2 | **67.0** | 66.6 |
| TurkishMMLU _(Acc)_ | 5-shot | 43.7 | 45.2 | 60.6 | **63.1** |
| GreekMMLU _(Acc)_ | 5-shot | 63.4 | 66.3 | 69.4 | **70.4** |
| KazakhMMLU _(Acc)_ | 5-shot | 52.1 | 47.1 | **62.3** | 61.8 |
| IndoMMLU _(Acc)_ | 0-shot | 48.5 | 52.0 | **60.1** | 59.5 |
| IndoCareer _(Acc)_ | 3-shot | 53.4 | 56.6 | 61.5 | **61.8** |
| IndoCulture _(Acc)_ | 0-shot | 59.1 | 58.5 | 61.1 | **62.5** |
| **Average** | - | 54.6 | 56.9 | **65.1** | 64.7 |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "AIDC-AI/Marco-Mini-Global-Base"
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
