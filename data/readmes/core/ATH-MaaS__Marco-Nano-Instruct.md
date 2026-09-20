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

# Marco-Nano-Instruct

**Marco-Nano-Instruct** is the post-trained variant of [Marco-Nano-Base](https://huggingface.co/AIDC-AI/Marco-Nano-Base), a highly sparse Mixture-of-Experts (MoE) multilingual language model from the [Marco-MoE](https://github.com/AIDC-AI/Marco-LLM) family, developed by Alibaba International Digital Commerce. It activates only **0.6B out of 8B total parameters** (7.5% activation ratio) per token. Despite its extreme sparsity, Marco-Nano-Instruct achieves the **best average performance** across English, multilingual general, and multilingual cultural benchmarks among all comparable instruct models up to 3.84B activated parameters.

## Model Description

Marco-Nano-Instruct shares the same architecture as [Marco-Nano-Base](https://huggingface.co/AIDC-AI/Marco-Nano-Base): a decoder-only Transformer with sparse MoE layers replacing standard FFN layers, upcycled from [Qwen3-0.6B-Base](https://huggingface.co/Qwen/Qwen3-0.6B-Base) using fine-grained sub-matrix splitting combined with Drop-Upcycling.

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

## Post-Training Details

Marco-Nano-Instruct is trained from [Marco-Nano-Base](https://huggingface.co/AIDC-AI/Marco-Nano-Base) using a two-stage post-training pipeline implemented with the SLIME framework:

### Stage 1: Supervised Fine-Tuning (SFT)

- **Duration:** ~24 hours on 64 GPUs
- **Steps:** ~4,000 (1 epoch)
- **Learning rate:** 1e-5 with cosine decay to 1e-6
- **Batch size:** 512, context length 8,192 tokens

**Data sources:**
1. **General instructions** — Dolci-Instruct dataset, augmented with Nemotron-Cascade-2 data
2. **Knowledge-intensive data** — Scientific prompts from Nemotron-Cascade-2, responses distilled from Gemini3-Flash
3. **Translation data** — Web-mined NLLB translation pairs, filtered and scored with [Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B) (top 10K per language)
4. **Multilingual & cultural data** — Wikidata-sourced content with Gemini3-Flash text synthesis for cultural concepts.

### Stage 2: On-Policy Distillation (OPD)

- **Duration:** ~110 hours on 64 GPUs
- **Steps:** ~2,900 total (2 responses sampled per prompt)
- **Learning rate:** 1e-6 (constant)

**Cascaded distillation:**
1. ~1,900 steps with Qwen3-30B-A3B-Instruct as teacher
2. ~1,000 steps with Qwen3-Next-80B-A3B-Instruct as stronger teacher

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

We compare Marco-Nano-Instruct against instruct models of comparable size: **Qwen3-1.7B-Instruct** (1.7B activated), **Qwen3-VL-2B-Instruct** (2B activated), **Ministral3-3B-Instruct** (3.84B activated), **LFM2-8B-A1B** (1.5B activated), and **Granite4-Tiny-Instruct** (1.47B activated). Marco-Nano-Instruct uses only **0.6B activated parameters** — the smallest among all baselines. Avg@8 accuracies are reported, except for GlobalMMLU and MMMLU where Acc@1 is reported.

### English

| Benchmark | Qwen3-1.7B | Qwen3-VL-2B | Ministral3-3B | LFM2-8B-A1B | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| MMLU _(Acc)_ | 62.4 | 62.1 | 69.8 | 72.1 | 50.8 | **73.2** |
| MMLU-Redux _(Acc)_ | 62.4 | 62.2 | 69.6 | 71.9 | 51.2 | **73.3** |
| MMLU-Pro _(Acc)_ | 35.2 | 38.3 | 49.5 | 49.5 | 25.3 | **54.5** |
| AGIEval _(Acc)_ | 39.6 | 33.0 | 44.7 | 45.2 | 30.7 | **49.8** |
| GPQA-Diamond _(Acc)_ | 27.5 | 21.0 | 31.6 | **31.9** | 28.3 | 22.2 |
| GSM8K _(EM)_ | 77.9 | 79.7 | 79.0 | 84.6 | 71.1 | **86.7** |
| MATH _(EM)_ | 70.6 | 73.7 | 70.2 | **82.6** | 53.4 | 79.6 |
| **Average** | 53.7 | 52.9 | 59.2 | 62.5 | 44.4 | **62.8** |

### Multilingual — General

| Benchmark | Qwen3-1.7B | Qwen3-VL-2B | Ministral3-3B | LFM2-8B-A1B | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| GlobalMMLU _(Acc)_ | 46.3 | 45.9 | 38.4 | 49.0 | 43.0 | **58.7** |
| MMMLU _(Acc)_ | 49.0 | 49.0 | 39.4 | 56.5 | 44.1 | **59.9** |
| MMLU-ProX-Lite _(Acc)_ | 28.6 | 30.3 | 26.7 | 33.8 | 22.1 | **43.2** |
| MGPQA _(Acc)_ | 25.3 | 22.3 | 18.8 | **27.2** | 25.9 | 21.6 |
| FLORES-200 En→Xx _(BLEU)_ | 12.7 | 15.3 | 8.3 | 14.9 | **22.5** | 22.3 |
| FLORES-200 Xx→En _(BLEU)_ | 28.2 | 28.6 | 18.9 | 20.1 | 30.4 | **31.1** |
| WMT24++ En→Xx _(BLEU)_ | 13.2 | 14.6 | 4.4 | 14.6 | **18.9** | 18.7 |
| WMT24++ Xx→En _(BLEU)_ | 26.4 | 26.2 | 8.3 | 17.9 | 25.1 | **27.3** |
| MGSM _(EM)_ | 63.6 | 67.6 | 47.0 | 56.5 | 55.3 | **76.5** |
| PolyMath _(EM)_ | 23.4 | 25.5 | 16.3 | 26.5 | 18.7 | **29.6** |
| **Average** | 31.7 | 32.5 | 22.7 | 31.7 | 30.6 | **38.9** |

### Multilingual — Cultural & Regional

| Benchmark | Qwen3-1.7B | Qwen3-VL-2B | Ministral3-3B | LFM2-8B-A1B | Granite4-Tiny | **Marco-Nano** |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| INCLUDE _(Acc)_ | 44.9 | 44.4 | 35.4 | 43.5 | 38.6 | **54.3** |
| Global-PIQA _(Acc)_ | 62.0 | 65.8 | 50.6 | 60.8 | 63.3 | **70.7** |
| CMMLU _(Acc)_ | 60.4 | **63.3** | 48.9 | 52.7 | 39.2 | 60.0 |
| C-Eval _(Acc)_ | 58.7 | **63.2** | 50.6 | 50.8 | 39.4 | 60.8 |
| ArabicMMLU _(Acc)_ | 48.8 | 46.9 | 22.7 | **56.5** | 43.4 | **56.5** |
| TurkishMMLU _(Acc)_ | 42.7 | 39.6 | 38.6 | 26.3 | 31.6 | **59.9** |
| GreekMMLU _(Acc)_ | 48.7 | 48.0 | 38.4 | 40.0 | 44.8 | **61.6** |
| KazakhMMLU _(Acc)_ | 46.0 | 47.1 | 41.4 | 39.6 | 39.6 | **56.3** |
| IndoMMLU _(Acc)_ | 48.8 | 49.3 | 35.2 | 41.1 | 37.2 | **56.3** |
| IndoCareer _(Acc)_ | 46.1 | 45.7 | 36.0 | 41.7 | 34.7 | **54.9** |
| IndoCulture _(Acc)_ | 45.8 | 47.7 | 37.2 | 45.9 | 42.8 | **59.1** |
| **Average** | 50.3 | 51.0 | 39.5 | 45.4 | 41.3 | **59.1** |

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "AIDC-AI/Marco-Nano-Instruct"
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
