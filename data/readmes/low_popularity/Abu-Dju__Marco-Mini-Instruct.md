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
- on-policy distillation
datasets:
- allenai/Dolci-Instruct-SFT
- nvidia/Nemotron-Cascade-2-SFT-Data
- nvidia/Nemotron-RL-instruction_following
- nvidia/Nemotron-RL-instruction_following-structured_outputs
- nvidia/Nemotron-RL-ReasoningGym-v1
- nvidia/Nemotron-RL-knowledge-mcqa
- nvidia/Nemotron-Cascade-RL-RLHF
- BytedTsinghua-SIA/DAPO-Math-17k
- Skywork/Skywork-OR1-RL-Data
- nvidia/Nemotron-SFT-Multilingual-v1
---

# Marco-Mini-Instruct

**Marco-Mini-Instruct** is the instruction-tuned variant of [Marco-Mini-Base](https://huggingface.co/AIDC-AI/Marco-Mini-Base), a highly sparse Mixture-of-Experts (MoE) multilingual language model from the [Marco-MoE](https://github.com/AIDC-AI/Marco-LLM) family, developed by Alibaba International Digital Commerce. It activates only **0.86B out of 17.3B total parameters** (5% activation ratio) per token. Marco-Mini-Instruct achieves the **best average performance** across English, multilingual general, and multilingual cultural benchmarks when compared against instruct models with up to 12B activated parameters, including Qwen3-4B-Instruct, Ministral3-8B-Instruct, Gemma3-12B-Instruct, LFM2-24B-A2B, and Granite4-Small-Instruct.

## Model Description

Marco-Mini-Instruct shares the same architecture as [Marco-Mini-Base](https://huggingface.co/AIDC-AI/Marco-Mini-Base): a decoder-only Transformer with sparse MoE layers replacing standard FFN layers, upcycled from [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) using fine-grained sub-matrix splitting combined with Drop-Upcycling.

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

## Post-Training Details

Marco-Mini-Instruct is trained from [Marco-Mini-Base](https://huggingface.co/AIDC-AI/Marco-Mini-Base) using a two-stage post-training pipeline implemented with the SLIME framework:

### Stage 1: Supervised Fine-Tuning (SFT)

- **Duration:** ~24 hours on 64 GPUs
- **Steps:** ~4,000 (1 epoch)
- **Learning rate:** 1e-5 with cosine decay to 1e-6
- **Batch size:** 512, context length 8,192 tokens

**Data sources:**
1. **General instructions** — Dolci-Instruct dataset, augmented with Nemotron-Cascade-2 data
2. **Knowledge-intensive data** — Scientific prompts from Nemotron-Cascade-2, responses distilled from Gemini3-Flash
3. **Translation data** — Web-mined NLLB translation pairs, filtered and scored with Qwen3-Embedding-8B (top 10K per language)
4. **Multilingual & cultural data** — Wikidata-sourced content with Gemini3-Flash text synthesis for cultural concepts.

### Stage 2: On-Policy Distillation (OPD)

- **Duration:** ~110 hours on 64 GPUs
- **Steps:** ~3,800 total (2 responses sampled per prompt)
- **Learning rate:** 1e-6 (constant)

**Cascaded distillation:**
1. ~1,900 steps with Qwen3-30B-A3B-Instruct as teacher
2. ~1,900 steps with Qwen3-Next-80B-A3B-Instruct as stronger teacher

**OPD data mixture:**

| Category | Datasets | Ratio |
|:---|:---|:---:|
| Instruction Following | Nemotron-RL-instruction-following + structured outputs | 25% |
| Knowledge & Reasoning | Nemotron-RL-ReasoningGym-v1 + knowledge-mcqa | 25% |
| Alignment | Nemotron-Cascade-RL-RLHF | 10% |
| Math | DAPO-Math-17k + Skywork-OR1-RL-Data | 10% |
| Multilingual | Translation + Cultural + Nemotron-SFT-Multilingual-v1 | 30% |

## Supported Languages

English, Chinese, Arabic, German, Spanish, French, Korean, Japanese, Portuguese, Turkish, Indonesian, Italian, Dutch, Polish, Russian, Vietnamese, Thai, Hebrew, Ukrainian, Malay, Bengali, Czech, Urdu, Kazakh, Greek, Romanian, Hungarian, Nepali, Azerbaijani

## Evaluation

We compare Marco-Mini-Instruct against strong instruct baselines: **Qwen3-4B-Instruct** (4B activated), **Ministral3-8B-Instruct** (8.8B activated), **Gemma3-12B-Instruct** (12B activated), **Granite4-Small-Instruct** (9B activated), and **LFM2-24B-A2B** (2B activated). Marco-Mini-Instruct uses only **0.86B activated parameters**. Avg@8 accuracies are reported, except for GlobalMMLU and MMMLU where Acc@1 is reported.

### English

| Benchmark | Qwen3-4B | Ministral3-8B | Gemma3-12B | Granite4-Small | LFM2-24B-A2B | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| MMLU _(Acc)_ | 80.8 | 79.8 | 76.2 | 76.7 | 74.9 | **83.4** |
| MMLU-Redux _(Acc)_ | 80.9 | 79.9 | 76.2 | 76.7 | 74.9 | **83.5** |
| MMLU-Pro _(Acc)_ | 66.9 | 63.9 | 55.8 | 57.1 | 57.6 | **70.7** |
| AGIEval _(Acc)_ | 51.7 | 52.4 | 43.6 | 44.7 | 49.0 | **55.4** |
| GPQA-Diamond _(Acc)_ | **50.8** | 44.8 | 35.2 | 38.6 | 39.7 | 50.3 |
| GSM8K _(EM)_ | 88.6 | 89.5 | 89.7 | 83.9 | 87.2 | **93.1** |
| MATH _(EM)_ | **93.4** | 86.2 | 83.8 | 75.7 | 83.9 | 91.8 |
| **Average** | 73.3 | 70.9 | 65.8 | 64.8 | 66.7 | **75.5** |

### Multilingual — General

| Benchmark | Qwen3-4B | Ministral3-8B | Gemma3-12B | Granite4-Small | LFM2-24B-A2B | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| GlobalMMLU _(Acc)_ | 70.2 | 55.4 | 69.2 | 67.4 | 57.0 | **73.3** |
| MMMLU _(Acc)_ | 71.3 | 56.4 | 69.4 | 68.1 | 62.3 | **73.7** |
| MMLU-ProX-Lite _(Acc)_ | 58.3 | 43.3 | 51.3 | 51.6 | 43.3 | **61.2** |
| MGPQA _(Acc)_ | 41.0 | 30.5 | 32.8 | 35.0 | 32.7 | **41.8** |
| FLORES-200 En→Xx _(BLEU)_ | 22.1 | 17.5 | **35.6** | 31.9 | 19.2 | 30.6 |
| FLORES-200 Xx→En _(BLEU)_ | 33.5 | 31.0 | **40.3** | 32.2 | 22.7 | 36.8 |
| WMT24++ En→Xx _(BLEU)_ | 20.9 | 14.4 | **32.1** | 26.6 | 16.0 | 26.8 |
| WMT24++ Xx→En _(BLEU)_ | 29.9 | 24.2 | **35.5** | 27.5 | 18.8 | 31.3 |
| MGSM _(EM)_ | 84.4 | 68.7 | 84.0 | 75.7 | 67.8 | **87.4** |
| PolyMath _(EM)_ | **47.2** | 26.4 | 35.5 | 28.9 | 29.3 | 44.7 |
| **Average** | 47.9 | 36.8 | 48.6 | 44.5 | 36.9 | **50.8** |

### Multilingual — Cultural & Regional

| Benchmark | Qwen3-4B | Ministral3-8B | Gemma3-12B | Granite4-Small | LFM2-24B-A2B | **Marco-Mini** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| INCLUDE _(Acc)_ | 63.8 | 50.7 | 65.0 | 60.3 | 49.1 | **65.6** |
| Global-PIQA _(Acc)_ | 79.6 | 61.3 | 82.2 | 80.2 | 69.0 | **84.2** |
| CMMLU _(Acc)_ | **78.6** | 67.4 | 60.8 | 59.6 | 56.7 | 75.3 |
| C-Eval _(Acc)_ | **80.4** | 68.0 | 59.7 | 59.4 | 56.7 | 75.4 |
| ArabicMMLU _(Acc)_ | 66.0 | 41.4 | **70.1** | 66.3 | 61.3 | 67.8 |
| TurkishMMLU _(Acc)_ | 71.6 | 48.2 | 64.4 | 57.9 | 33.4 | **74.7** |
| GreekMMLU _(Acc)_ | 68.6 | 49.5 | **77.7** | 71.7 | 44.7 | 72.5 |
| KazakhMMLU _(Acc)_ | 66.6 | 59.1 | 66.8 | 63.5 | 47.6 | **68.8** |
| IndoMMLU _(Acc)_ | 64.4 | 52.4 | 65.3 | 59.6 | 42.7 | **65.7** |
| IndoCareer _(Acc)_ | 62.2 | 53.4 | 63.2 | 56.3 | 43.7 | **64.4** |
| IndoCulture _(Acc)_ | 58.7 | 47.8 | **69.6** | 59.3 | 44.2 | 67.1 |
| **Average** | 69.1 | 54.5 | 67.7 | 63.1 | 49.9 | **71.0** |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "AIDC-AI/Marco-Mini-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

messages = [
    {"role": "user", "content": "What is the capital of France?"}
]
inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to(model.device)
outputs = model.generate(inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True))
```

**Note**: vLLM is the recommended engine for deployment, as SGLang currently lacks support for MoE models with tied embeddings (see [PR #20127](https://github.com/sgl-project/sglang/pull/20127)). If SGLang is required for your workflow, please use the specific build at commit e5f48b32abff027d859a43b7d5ba3aece04471c7.

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