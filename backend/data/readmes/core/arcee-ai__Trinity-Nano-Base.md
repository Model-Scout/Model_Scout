---
license: other
language:
- en
- es
- fr
- de
- it
- pt
- ru
- ar
- hi
- ko
- zh
library_name: transformers
base_model:
- arcee-ai/Trinity-Nano-Base-Pre-Anneal
license_link: LICENSE
license_name: openmdw-1.1
---
<div align="center">
  <picture>
    <img
      src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/i-v1KyAMOW_mgVGeic9WJ.png"
      alt="Arcee Trinity Mini"
      style="max-width: 100%; height: auto;"
    >
  </picture>
</div>

# Trinity Nano Base

Trinity Nano is an Arcee AI 6B MoE model with 1B active parameters. It is the small-sized model in our new Trinity family, a series of open-weight models for enterprise and tinkerers alike.

This base model *pre* fine tuning, and so is not suitable for chatting, and should be trained for your specific domain before use.

Trinity Nano is trained on 10T tokens gathered and curated through a key partnership with [Datology](https://www.datologyai.com/), building upon the excellent dataset we used on [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) with additional math and code.

Training was performed on a cluster of 512 H200 GPUs powered by [Prime Intellect](https://www.primeintellect.ai/) using HSDP parallelism.

More details, including key architecture decisions, can be found on our blog [here](https://www.arcee.ai/blog/the-trinity-manifesto)

***

## Model Details

* **Model Architecture:** AfmoeForCausalLM
* **Parameters:** 6B, 1B active
* **Experts:** 128 total, 8 active, 1 shared
* **Context length:** 128k
* **Training Tokens:** 10T
* **License:** [OpenMDW-1.1](https://huggingface.co/arcee-ai/Trinity-Nano-Base#license)

## Benchmarks

### 🔢 Math & Reasoning
| Benchmark | Score |
|-----------|-------|
| GSM8K | 58.4% |
| Minerva Math 500 | 36.0% |
| DROP (0-shot) | 4.5% |
| DROP (5-shot) | 63.6% |

### 💻 Code Generation
| Benchmark | Pass@1 | Pass@10 |
|-----------|--------|---------|
| HumanEval (3-shot, bpb) | 36.3% (bpb) | - |
| HumanEval+ (temp 0.8) | 31.7% | - |
| MBPP+ | 44.7% | - |

### 🧠 Knowledge & Reasoning
| Benchmark | 5-shot | 0-shot |
|-----------|---------|--------|
| ARC-Challenge | 84.0% | 78.2% |
| ARC-Easy | 94.8% | 91.2% |
| CommonsenseQA | 74.9% | 62.7% |
| OpenBookQA | 82.2% | 75.2% |
| WinoGrande | 72.8% | 68.0% |
| MMLU | 67.7% | 64.2% |
| MMLU Pro | 35.8% | 27.7% |
| AGI Eval (English) | 51.8% | - |
| BBH (CoT) | 50.4% | 7.6% |

### 📘 Understanding & QA
| Benchmark | Score |
|-----------|-------|
| BoolQ (5-shot) | 84.3% |
| HellaSwag (5-shot) | 77.4% |
| PIQA (5-shot) | 82.2% |
| SciQ (5-shot) | 93.2% |
| Social IQA (5-shot) | 73.0% |

<div align="center">
  <picture>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/6435718aaaef013d1aec3b8b/sSVjGNHfrJKmQ6w8I18ek.png" style="background-color:ghostwhite;padding:5px;" width="17%" alt="Powered by Datology">
  </picture>
</div>

## License

Trinity-Mini-Base is released under the OpenMDW-1.1 license.