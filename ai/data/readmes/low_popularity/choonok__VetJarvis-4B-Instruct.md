---
license: other
license_name: vetjarvis-model-license-1.0-nc
license_link: LICENSE
language:
- ko
- en
base_model:
- choonok/VetJarvis-4B-Base
- Qwen/Qwen3.5-4B
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
tags:
- veterinary
- companion-animal
- canine
- feline
- medical
- domain-specific
- qwen3.5
- not-a-medical-device
---

# VetJarvis-4B-Instruct

**언어 / Language**: [🇰🇷 한국어](README_ko.md) · [🇺🇸 English](README.md)


## 🆕 업데이트

- **VetJarvis 1.1** 버전이 업데이트되었습니다. 사후학습(Post-training) 파이프라인 개선을 통해 **Reasoning 성능**이 한층 강화되었습니다.
- **`thinking` 모드** 활성화 시, **GPT-5.4-mini(no thinking)에 근접한 성능**을 제공합니다.
- 자세한 내용은 VetJarvis-1.1 모델카드를 참고해 주세요 → [choonok/VetJarvis-1.1-4B-Instruct](https://huggingface.co/choonok/VetJarvis-1.1-4B-Instruct)
---
## 🆕 Update

- **VetJarvis 1.1** has been released — featuring significantly enhanced **reasoning performance** through an improved post-training pipeline.
- With **`thinking` mode** enabled, VetJarvis 1.1 delivers **GPT-5.4-mini-class performance**.
- For details, please refer to the new repository → [choonok/VetJarvis-1.1-4B-Instruct](https://huggingface.co/choonok/VetJarvis-1.1-4B-Instruct)


## 1. Model Introduction

**VetJarvis-4B-Instruct**, a 4-billion-parameter domain-specific large language model (LLM) developed by CHOONOK COMPANY, is designed for companion animal(canine and feline) veterinary knowledge, education, and responsible AI research.

CHOONOK COMPANY, a Korea-based company, releases VetJarvis-4B-Instruct as a contribution to the veterinary research and education community, with the goal of supporting safe and responsible advancement of veterinary AI technologies.

- Research & education: freely available, no approval needed.
- Beyond research: we welcome broader use - including industry applications -
  > through a lightweight safety review, not a commercial gate.
- Clinical use: not permitted. VetJarvis is not a medical device and should not replace professional veterinary judgment.

We want this model to be genuinely useful - to researchers, educators, and eventually the broader veterinary ecosystem - while ensuring that its use remains responsible and expert-guided.

## 2. Model Configuration

### Overview

- **Model Name**: VetJarvis-4B-Instruct
- **Base Model**: choonok/VetJarvis-4B-Base
- **Architecture**: Qwen3_5ForConditionalGeneration
- **Number of Parameters**: 4.2B (Language Model) + ~62M (MTP)
- **Context Length**: 8,192 tokens (SFT); 4,096 tokens (CPT stage)
- **Training Hardware**: NVIDIA B200 192GB × 4 (single node)
- **Training Framework**: NVIDIA Megatron-Bridge
- **Knowledge Cutoff**: Apr 2026
- **Domain**: Veterinary medicine
- **Language**: Korean, English

### Training Pipeline

- **Stage 1**: Continual Pre-Training (CPT) --- Qwen/Qwen3.5-4B → VetJarvis-4B-Base
- **Stage 2**: Supervised Fine-Tuning (SFT) --- VetJarvis-4B-Base → VetJarvis-4B-Instruct
- **MTP**: Jointly trained during both CPT and SFT stages

### Training Data

- VetJarvis-4B-Instruct was trained using veterinary reference materials and real-world clinical data. All clinical records were **fully de-identified** prior to use, with personal information of both animal guardians and veterinary personnel removed in accordance with data protection standards. General-domain Korean/English documents were also included to preserve the base model's general reasoning capabilities.
- **Total Training Tokens**: ~8.5B tokens

### Training Hyperparameters

| Item | Value |
|---|---|
| **Framework** | [NVIDIA Megatron-Bridge](https://github.com/NVIDIA/Megatron-Bridge) |
| **Objective** | Next-token prediction (causal LM) |
| **Precision** | BF16 mixed (FP32 master params + grads + Adam m/v) |
| **Optimizer** | Distributed Fused AdamW |
| **LR Schedule** | Cosine annealing |
| **Max LR** | 2e-5 |
| **Min LR** | 5e-6 |
| **LR Warmup** | 5% (≈ 863 iters) |
| **Global Batch Size** | 120 samples |
| **Micro Batch Size** | 3 |
| **Sequence Length** | 4,096 |
| **Tokens per Step** | 491,520 |
| **Training Iterations** | **17,264** |
| **RNG Seed** | 42 |

### Parallelism & Sharding

| Item | Value |
|---|---|
| **Tensor Parallel (TP)** | 1 |
| **Pipeline Parallel (PP)** | 1 |
| **Data Parallel (DP)** | 4 |
| **Context Parallel (CP)** | 1 |
| **Sequence Parallel** | False |
| **Optimizer Sharding** | ZeRO-1 (`data_parallel_sharding_strategy=optim`) |
| **Gradient Accumulation Fusion** | True |
| **Cross-Entropy Loss Fusion** | True (native impl) |
| **Attention Backend** | Flash-Attention |
| **Activation Recomputation** | None |

### Hardware & Compute

| Item | Value |
|---|---|
| **GPU** | NVIDIA **B200 192GB × 4** (Blackwell) |
| **Node** | Single-node (NVLink 5th gen) |
| **CPU** | 96 cores |
| **System RAM** | 944 GB |
| **CUDA Cores per GPU** | 18,944 |

### Compute & Throughput

| Item | Value |
|---|---|
| **Wall-clock Training Time** | ~28.65 hours (≈ 29h) |
| **Total GPU-hours (measured)** | **114.6 B200 GPU-hour** (28.65h × 4 GPU) |
| **Total FLOPs (estimated)** | ~**2.04 × 10²⁰ FLOPs** (6ND: N=4B, D=8.49B) |
| **Per-GPU Throughput (avg)** | ~494 TFLOP/s (BF16) |
| **Model FLOPs Utilization (MFU)** | ~22% |
| **A100 Equivalent GPU-hour** | ~454 A100 GPU-hour (BF16 312 TFLOP/s, MFU 40% assumed) |

## 3. Quickstart

### Serving VetJarvis-4B-Instruct

VetJarvis-4B-Instruct is a text-only LLM based on Qwen3.5-4B, and can be served in BF16 using a variety of frameworks including Hugging Face Transformers and vLLM.

### Hugging Face Transformers

Qwen3.5 architecture is natively supported from `transformers>=5.5`.

```bash
pip install -U "transformers>=5.5" accelerate torch flash-attn
```

```python
import torch
from transformers import AutoTokenizer, Qwen3_5ForConditionalGeneration

MODEL = "choonok/VetJarvis-4B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = Qwen3_5ForConditionalGeneration.from_pretrained(
    MODEL,
    dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="flash_attention_2",
)
model.eval()

messages = [
    {
        "role": "system",
        "content": "You are 'VetJarvis', a veterinarian-only AI assistant developed by CHOONOK COMPANY.",
    },
    {"role": "user", "content": "Please tell me the metronidazole protocol."},
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)

inputs = tokenizer(text, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=4096,
        temperature=0.8,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

print(tokenizer.decode(
    outputs[0][inputs.input_ids.shape[-1]:],
    skip_special_tokens=True,
))
```

On Blackwell GPUs (RTX 5090 / B200), a compatible build of flash-attn ≥ 2.7 is required. If you encounter build or compatibility issues, fall back to `attn_implementation="sdpa"`.

### vLLM

Recommended for production or high-throughput use cases. `vllm>=0.18` supports the Qwen3.5 architecture, and the jointly trained MTP layer can be used for speculative decoding to improve throughput.

```bash
pip install "vllm>=0.18"
```

Launch an OpenAI-compatible server:

```bash
vllm serve choonok/VetJarvis-4B-Instruct \
    --served-model-name VetJarvis-4B-Instruct \
    --port 8000 \
    --max-model-len 8192 \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.85 \
    --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}'
```

Example:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

response = client.chat.completions.create(
    model="VetJarvis-4B-Instruct",
    messages=[
        {
            "role": "system",
            "content": "You are 'VetJarvis', a veterinarian-only AI assistant developed by CHOONOK COMPANY.",
        },
        {
            "role": "user",
            "content": "Please tell me the metronidazole protocol.",
        },
    ],
    max_tokens=4096,
    temperature=0.8,
    top_p=0.9,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": False},
    },
)

print(response.choices[0].message.content)
```

### Recommended Parameters

| Parameter | Value |
|---|---|
| **Temperature** | 0.8 |
| **Top-p** | 0.9 |
| **max_new_tokens** | 4,096 |
| **enable_thinking** | `False` (default) |
| **Context length** | ≤ 262,144 tokens |

## 4. Evaluation Results

### Main Benchmarks

To ensure the transparency and reproducibility of the evaluation, the benchmark for this model utilizes data from the 73rd to 77th (2022–2026) Japanese Veterinary National Examination, currently the only veterinary licensing exam globally that officially publishes its past questions. We constructed an evaluation subset (n=132) by filtering for questions directly related to small animal (canine and feline) clinical practice from Theory Exam A/B. For multiple-answer (all-correct) questions, the original grading criteria of the examining body were strictly observed.

The comparison targets include, in addition to our VetJarvis model, GPT-5-mini (reasoning effort: minimal/medium), Qwen3.5-4B (base model), Gemma-4-E2B / E4B-it, and EXAONE-3.5-7.8B-Instruct.

**Figure 1. Parameter size vs accuracy**

![](media/image1.png)

Figure 1 compares **mean accuracy against parameter count (log scale)** on the small-animal clinical subset (n=132) of the Japanese Veterinary National Examination benchmark. The x-axis denotes model parameter count (1B–10B+, log scale), the y-axis denotes mean accuracy (%), and error bars indicate per-exam variance.

- The **VetJarvis-4B** family reaches **77.88%** (standard) and **81.67%** (think mode) at the 4B scale, outperforming similarly sized open local models Qwen3.5-4B (62.58%) and Gemma-E4B (56.97%, effective 4.5B) by more than 15–25 percentage points.
- It also exceeds EXAONE-3.5-7.8B (47.58%)—a model 1.7–2× its size—by over 30 percentage points, clearly departing from the **local-model trend** line.
- Compared to closed models, the gap versus **GPT-5.4-mini (86.82%)** and **GPT-5.4-mini · think (93.94%)** is only about 5–9 percentage points, suggesting that VetJarvis-4B approaches a comparable performance envelope despite the 2×+ difference in parameter scale.

In short, VetJarvis-4B clearly demonstrates the value of **veterinary-domain-specialized training** relative to open local models at the same parameter scale, and enabling think mode yields additional accuracy gains.

**Figure 2. Parameter size vs accuracy**

![](media/image_re_2.png)

Figure 2 presents the same evaluation as Figure 1 in a **detailed table ranked by accuracy across eight models**, reporting **per-session accuracy** for the 73rd–77th Japanese Veterinary National Exams, **mean accuracy**, **standard deviation (σ)**, **min–max range**, and **gap versus GPT-5.4-mini (think mode)** (Δ vs GPT-5.4-mini-think).

- The top two ranks are taken by the closed models **GPT-5.4-mini (medium thinking) at 93.94%** and **GPT-5.4-mini (no thinking) at 86.82%**.
- **VetJarvis-4B-THINK-IT (thinking ON) at 81.67%** ranks 3rd overall, and **thinking OFF at 77.88%** ranks 4th, with gaps to GPT-5.4-mini (think) of **-12.27 pp** and **-16.06 pp** respectively.
- Against the same 4B-scale **Qwen3.5-4B (62.58%)**, VetJarvis-4B leads by **+19.09 pp** (think ON) and **+15.30 pp** (think OFF).
- Other open local models trail by wide margins relative to GPT-5.4-mini (think): **Gemma-3n-E4B-it 56.97% (-36.97 pp)**, **EXAONE-3.5-7.8B 47.58% (-46.36 pp)**, and **Gemma-3n-E2B-it 43.18% (-50.76 pp)**.
- The per-session standard deviation (σ) of VetJarvis-4B (1.73–2.17) is comparable to GPT-5.4-mini (no thinking, 1.98), indicating that **stability across exam sessions** is on par with closed models.

In summary, VetJarvis-4B records **the highest accuracy among 4B-parameter open local models**, narrowing the gap to leading closed models to a 10–16 pp range and reaffirming the practical effectiveness of **veterinary-domain-specialized training**.

### Summary

> The VetJarvis-4B-Instruct model consistently outperforms comparable open local models (Qwen3.5-4B, Gemma-4-E4B, EXAONE-3.5-7.8B) across hematology/oncology (98%), orthopedics (89%), endocrinology (88%), infectious diseases/zoonoses (78%), and respiratory (74%) domains, with margins ranging from 5 to 55 percentage points. It shows particular strength in histopathological classification, differential diagnosis of non-erosive arthritis, judgment on procedural indications (e.g., lobectomy for lung lobe torsion), and clinical decision-making that incorporates regional epidemiological data (such as the current status of feline-to-human zoonoses in Japan).

## 5. Limitation & License

### Limitations

> **Not a Medical Device** : This model is not a medical device evaluated or approved by any regulatory authority.
>
> **Prohibition of Clinical Use** : The model's outputs cannot replace clinical decision-making, such as diagnosis, prescription, or treatment for actual animal patients, and direct use for such purposes is strictly prohibited.
>
> **Hallucination** : Due to the technical nature of generative AI, the model may produce factually incorrect or veterinary-inaccurate information (hallucinations). Blind trust in the model's outputs is dangerous, and cross-verification by veterinary professionals is essential.
>
> **Knowledge Cutoff Limitations**: As this model was trained on data up to a specific point in time (Knowledge Cutoff), it may not reflect the latest veterinary research papers, new drug information, or developments published thereafter.
>
> **Disclaimer of Liability**: CHOONOK COMPANY assumes no legal liability for any decisions made by the licensee utilizing the model's outputs, nor for any direct or indirect damages resulting from such use.

### License

> **Applicable License**: This model is governed by the CHOONOK COMPANY VetJarvis Model License Agreement 1.0 - NC.
>
> **Non-Commercial Research & Education Only**: Commercial use for revenue generation is prohibited; use is permitted solely for veterinary academic research, education, and technical evaluation.
>
> **Approval Process**: For uses beyond the Permitted Use, users must obtain prior written approval from CHOONOK COMPANY based on a 'safety and appropriateness review' rather than commercial criteria.
>
> **Detailed Terms**: Users must fully read and understand the complete text of the [LICENSE](./LICENSE) before use.

## 6. Contact

- **Email**: admin@choonokcompany.com
