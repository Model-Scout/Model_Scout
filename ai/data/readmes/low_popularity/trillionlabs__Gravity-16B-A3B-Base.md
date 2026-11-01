---
license: apache-2.0
language:
  - en
  - ko
library_name: transformers
tags:
  - moe
  - mixture-of-experts
  - gravity
  - trillion-labs
  - pretrained
  - base
pipeline_tag: text-generation
base_model: []
---

<p align="center">
  <img src="base-banner.png" alt="Gravity-16B-A3B-Base" width="100%">
</p>

# Gravity-16B-A3B-Base

**Gravity-16B-A3B-Base** is a pretrained language model trained from scratch (from random weights) by [Trillion Labs](https://trillionlabs.co), [Lunit](https://www.lunit.io) Consortium. Built on a sparse Mixture-of-Experts (MoE) architecture, it features 16.24B total parameters with 3.16B active parameters per token. The model was pretrained on approximately 5.5 trillion tokens with a strong emphasis on STEM and medical domains. This model has been further extended by Lunit Consortium into an [L1-16B-A3B](https://huggingface.co/learning-unit/L1-16B-A3B), a more specialized model for the medical domain. 

## Model Summary

| Property | Value |
|---|---|
| **Total Parameters** | 16.24B |
| **Active Parameters** | 3.16B |
| **Architecture** | GravityMoE |
| **Number of Layers** | 28 |
| **Hidden Size** | 2048 |
| **Attention Heads** | 16 |
| **KV Heads** | 16 |
| **Routed Experts** | 64 |
| **Shared Experts** | 1 |
| **Experts per Token** | 8 |
| **MoE Intermediate Size** | 1408 |
| **Context Length** | 32,768 tokens |
| **Vocabulary Size** | 151,552 |
| **Precision** | bf16 |
| **License** | Apache 2.0 |

## Architecture

Gravity-16B-A3B-Base is pretrained from scratch using a DeepSeek-like architecture ([DeepSeek-AI et al., 2024](https://arxiv.org/abs/2412.19437)), which demonstrates strong performance at this scale and whose original results serve as a reference for comparison. This is the same architectural family adopted by [Moonlight](https://huggingface.co/moonshotai/Moonlight-16B-A3B) ([Liu et al., 2025](https://arxiv.org/abs/2502.16982)). Key architectural features include:

- **Multi-head Latent Attention (MLA)**: Uses low-rank key-value compression (`kv_lora_rank=512`) for efficient KV cache usage, significantly reducing memory footprint during inference.
- **Mixture-of-Experts**: 64 routed experts with top-8 selection and 1 shared expert. The first layer uses a dense MLP, and all subsequent layers use the MoE structure.
- **Sigmoid Routing with Bias Correction**: Uses sigmoid-based scoring with auxiliary-free load balancing via `e_score_correction_bias`, avoiding the need for auxiliary loss terms during training.
- **Interleaved RoPE**: Rotary position embeddings with interleaved weight layout for efficiency.

### Comparison with Similar Models

While the overall architecture is similar, Gravity-16B-A3B-Base differs in the design choices:

| Parameter | Gravity-16B-A3B-Base | DeepSeek-V3-Small | Moonlight-16B-A3B |
|---|---|---|---|
| **Tokenizer** | GLM-4.5 (vocab: 151,552) | DeepSeek (vocab: 129,280) | Custom (vocab: 163,840) |
| **Layers** | 28 | 27 | 27 |
| **Dense Intermediate Size** | 8,192 | 11,264 | 11,264 |
| **Shared Experts** | 1 | 2 | 2 |
| **Experts per Token** | 8 | 8 | 6 |
| **Context Length** | 32,768 | 4,096 | 8,192 |
| **RoPE Base Frequency** | 1,000,000 | 10,000 | 50,000 |

### Tokenizer

Gravity-MoE uses a tokenizer initialized from [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) (vocabulary size: 151,552). Based on internal evaluations across multilingual corpora, we found this tokenizer to be more efficient in terms of fertility and compression ratio compared to alternatives, particularly for mixed English-Korean workloads.

## Evaluation Results

All evaluations are conducted on the base pretrained model without any instruction tuning or post-training.

| Category | Benchmark | Description | Metric | Score |
|---|---|---|---|---|
| **General Knowledge** | MMLU (5-shot) | Massive Multitask Language Understanding across 57 subjects | acc | 73.0 |
| | Global MMLU (EN) | Multilingual MMLU — English | acc | 73.5 |
| | Global MMLU (KO) | Multilingual MMLU — Korean | acc | 65.8 |
| **Reasoning** | GPQA Main | Graduate-level science QA (physics, chemistry, biology) | acc | 38.4 |
| | ARC-Challenge | Grade-school science questions, challenge set | acc_norm | 56.8 |
| | HellaSwag | Commonsense natural language inference | acc_norm | 77.9 |
| **Math** | GSM8K | Grade-school math word problems | exact_match | 71.3 |
| **Code** | HumanEval+ | Python function synthesis with augmented tests | pass@1 | 31.7 |
| | MBPP+ | Mostly basic Python programs with augmented tests | pass@1 | 73.3 |
| **Medical** | MedQA (4 options) | US Medical Licensing Exam-style questions | acc | 63.4 |
| **Reading Comprehension** | CoQA | Conversational question answering over passages | F1 | 77.5 |

## Quickstart

### Installation

```bash
pip install "transformers>=5.0" torch
```

### Using Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "trillionlabs/Gravity-16B-A3B-Base"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

input_ids = tokenizer("The theory of relativity states that", return_tensors="pt").input_ids.to(model.device)
output = model.generate(input_ids, max_new_tokens=128, do_sample=True, temperature=0.7)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Limitations

- This is a base pretrained model without instruction tuning or safety alignment. It may generate factually incorrect, biased, or harmful content.
- Performance may degrade on languages not well-represented in the training data.
- The model has a maximum context length of 32,768 tokens.

## Acknowledgements

This model was developed as part of a collaborative research initiative led by **Lunit** and **Trillion Labs**, with a focus on advancing foundation models for science and healthcare.

- **Lunit** — Project lead and medical AI research
- **Trillion Labs** — Model architecture, pretraining, and infrastructure
- **Aigen Science** — Biomedical AI and drug discovery research
- **SK Biopharmaceuticals** — AI-driven drug development and digital healthcare advisory
- **Kakao Healthcare** — Medical data standardization and platform support

We also thank the following participating institutions for their contributions: KAIST (Yoonjae Choi, Taekyun Kim, Jong Chul Ye, Hyunwoo Kim, Seunghoon Hong), Seoul National University (Yousung Jung), Rebellions, Standigm, NHIS Ilsan Hospital, Yongin Severance Hospital, Gangdong Kyung Hee University Hospital, Kyung Hee University Medical Center, Korea University, Konyang University Hospital, Ewha Womans University Seoul Hospital, Keimyung University Dongsan Medical Center, Pusan National University Yangsan Hospital, and D-Circle.

This work was supported by the **AI Specialized Foundation Model Project** (인공지능 특화 파운데이션 모델 프로젝트), funded by the **Ministry of Science and ICT** (과학기술정보통신부, MSIT) and managed by the **National IT Industry Promotion Agency** (NIPA, 정보통신산업진흥원).

## License

This model is released under the [Apache 2.0 License](LICENSE).

## Citation

```bibtex
@misc{gravity-trillionlabs,
      title={Gravity-16B-3AB}, 
      author={Trillion Labs},
      year={2026},
}
```

## Contact

- Website: [trillionlabs.co](https://trillionlabs.co)
