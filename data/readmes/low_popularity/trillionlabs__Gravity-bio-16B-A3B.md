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
  - biomedical
  - biology
  - midtraining
  - base
pipeline_tag: text-generation
base_model:
  - trillionlabs/Gravity-16B-A3B-Base
---

<p align="center">
  <img src="base-banner.png" alt="Gravity-bio-16B-A3B" width="100%">
</p>

# Gravity-bio-16B-A3B

**Gravity-bio-16B-A3B** is a biology-focus midtrained model derived from [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base). It uses the same sparse Mixture-of-Experts (MoE) architecture and tokenizer as Gravity-16B-A3B-Base, with additional midtraining for biological understanding on [TheBioCollection](https://huggingface.co/datasets/trillionlabs/TheBioCollection) corpus.


## Model Summary

| Property | Value |
|---|---|
| **Base Model** | [trillionlabs/Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) |
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
| **Context Length** | 8,192 tokens |
| **Vocabulary Size** | 151,552 |
| **Precision** | bf16 |
| **License** | Apache 2.0 |


## Architecture

Gravity-bio-16B-A3B uses the same Gravity-MoE architecture as Gravity-16B-A3B-Base. It follows a DeepSeek-style design ([DeepSeek-AI et al., 2024](https://arxiv.org/abs/2412.19437)) with the following key features:

- **Multi-head Latent Attention (MLA)**: Uses low-rank key-value compression (`kv_lora_rank=512`) for efficient KV cache usage, significantly reducing memory footprint during inference.
- **Mixture-of-Experts**: 64 routed experts with top-8 selection and 1 shared expert. The first layer uses a dense MLP, and all subsequent layers use the MoE structure.
- **Sigmoid Routing with Bias Correction**: Uses sigmoid-based scoring with auxiliary-free load balancing via `e_score_correction_bias`, avoiding the need for auxiliary loss terms during training.
- **Interleaved RoPE**: Rotary position embeddings with interleaved weight layout for efficiency.


## Tokenizer

Gravity-MoE uses a tokenizer initialized from [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) (vocabulary size: 151,552). Based on internal evaluations across multilingual corpora, we found this tokenizer to be more efficient in terms of fertility and compression ratio compared to alternatives, particularly for mixed English-Korean workloads.


## Evaluation Results on TheBioCollection-Eval

We compare Gravity-bio-16B-A3B with its base checkpoint, Gravity-16B-A3B-Base, on [TheBioCollection-Eval](https://huggingface.co/datasets/trillionlabs/TheBioCollection-Eval) under the same evaluation protocol.
Gravity-bio-16B-A3B more than doubles overall performance, with consistent gains across all domains.

| Domain | Task | Gravity-16B-A3B-Base | Gravity-bio-16B-A3B | Δ |
|---|---|---:|---:|---:|
| **Small molecules** | Molecule reconstruction/design | 0.200 | **0.522** | +0.322 |
|  | Forward synthesis | 0.213 | **0.619** | +0.406 |
|  | Molecular property recognition | 0.280 | **0.390** | +0.110 |
|  | *Domain average* | 0.223 | **0.513** | +0.290 |
| **Proteins** | Text-conditioned functional protein design | 0.243 | **0.522** | +0.279 |
|  | Binder design | 0.426 | **0.719** | +0.293 |
|  | Protein function prediction | 0.000 | **0.055** | +0.055 |
|  | *Domain average* | 0.223 | **0.432** | +0.209 |
| **Genomic sequences** | DNA regulatory/splice span localization | 0.134 | **0.516** | +0.382 |
|  | RNA family/anticodon span localization | 0.238 | **0.396** | +0.158 |
|  | *Domain average* | 0.175 | **0.468** | +0.293 |
| **Cells/pathways** | Cell type recognition | 0.470 | **0.580** | +0.110 |
|  | Hallmark program recognition | 0.520 | **0.750** | +0.230 |
|  | Perturbation response prediction | 0.015 | **0.498** | +0.483 |
|  | *Domain average* | 0.335 | **0.609** | +0.274 |
| **Overall** | *All domain average* | **0.239** | **0.506** | **+0.267** |


## Quickstart

### Installation

```python
pip install "transformers>=5.0" torch
```

### Using Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "trillionlabs/Gravity-bio-16B-A3B"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True,
)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)

prompt = "Synthesize a molecule that matches the given characteristics: The molecule appears as colorless crystals. Insoluble in water."
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7
)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```


## Limitations

- Gravity-bio-16B-A3B is not an instruction-tuned or safety-aligned assistant; its outputs may be inaccurate, biased, unsafe, or incomplete.
- Biological and biomedical responses should be independently verified, especially before any experimental, clinical, or decision-making use.
- This model is intended for research use and must not be treated as a substitute for professional scientific, medical, or regulatory judgment.


## Acknowledgements

This model was developed as part of a collaborative research initiative led by **Lunit** and **Trillion Labs**, with a focus on advancing foundation models for science and healthcare.

- **Lunit** — Project lead and medical AI research
- **Trillion Labs** — Model architecture, midtraining, and infrastructure
- **Aigen Science** — Biomedical AI and drug discovery research
- **SK Biopharmaceuticals** — AI-driven drug development and digital healthcare advisory
- **Kakao Healthcare** — Medical data standardization and platform support

We also thank the following participating institutions for their contributions: KAIST (Hyunjin Seo, Gyubok Lee, Yoonjae Choi, Taekyun Kim, Jong Chul Ye, Hyunwoo Kim, Seunghoon Hong), Korea University (Hyeon Hwang), Seoul National University (Yousung Jung), Rebellions, Standigm, NHIS Ilsan Hospital, Yongin Severance Hospital, Gangdong Kyung Hee University Hospital, Kyung Hee University Medical Center, Konyang University Hospital, Ewha Womans University Seoul Hospital, Keimyung University Dongsan Medical Center, Pusan National University Yangsan Hospital, and D-Circle.

This work was supported by the **AI Specialized Foundation Model Project** (인공지능 특화 파운데이션 모델 프로젝트), funded by the **Ministry of Science and ICT** (과학기술정보통신부, MSIT) and managed by the **National IT Industry Promotion Agency** (NIPA, 정보통신산업진흥원).


## License

This model is released under the Apache License 2.0.


## Citation

```
@misc{gravity-moe-2026,
    title={Gravity-bio-16B-A3B},
    author={{Trillion Labs}},
    year={2026},
    url={https://huggingface.co/trillionlabs/Gravity-bio-16B-A3B}
}
```


## Contact

- Website: [trillionlabs.co](https://trillionlabs.co/)
- Website: [lunit.io](https://www.lunit.io/)
