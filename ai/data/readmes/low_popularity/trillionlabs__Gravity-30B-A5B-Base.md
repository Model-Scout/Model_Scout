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
---

<p align="center">
  <img src="base-banner.png" alt="Gravity-30B-A5B-Base" width="100%">
</p>

# Gravity-30B-A5B-Base

**Gravity-30B-A5B-Base** is a pretrained sparse Mixture-of-Experts (MoE) language model by [Trillion Labs](https://trillionlabs.co) and the [Lunit](https://www.lunit.io) Consortium. It features 29.56B total parameters with 5.34B active parameters per token and a native 128K context window.

The model grows [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) from 28 to 52 layers with **LLaMA-Pro-style block expansion** ([Wu et al., 2024](https://arxiv.org/abs/2401.02415)): new transformer blocks are interleaved into the existing stack, and the expanded network is then continually pretrained on a STEM-, code- and Korean-heavy mixture, followed by long-context extension to 131,072 tokens.

The checkpoint uses the GravityMoE architecture, whose modeling code inherits directly from the DeepSeek-V3 implementation in `transformers`; the weight layout, routing fields and attention are exactly DeepSeek-V3. Load it with `trust_remote_code=True`.

## Model Summary

| Property | Value |
|---|---|
| **Total Parameters** | 29.56B |
| **Active Parameters** | 5.34B |
| **Architecture** | GravityMoE (DeepSeek-V3-compatible: MLA + sparse MoE) |
| **Number of Layers** | 52 (2 dense + 50 MoE) |
| **Hidden Size** | 2048 |
| **Attention Heads** | 16 |
| **KV Heads** | 16 |
| **Routed Experts** | 64 |
| **Shared Experts** | 1 |
| **Experts per Token** | 8 |
| **MoE Intermediate Size** | 1408 |
| **Context Length** | 131,072 tokens |
| **Vocabulary Size** | 151,552 |
| **Precision** | bf16 |
| **License** | Apache 2.0 |

## Architecture

Gravity-30B-A5B-Base uses a DeepSeek-V3-style architecture ([DeepSeek-AI et al., 2024](https://arxiv.org/abs/2412.19437)), the same family as [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) and [Moonlight](https://huggingface.co/moonshotai/Moonlight-16B-A3B). Key features:

- **Multi-head Latent Attention (MLA)**: low-rank key-value compression (`kv_lora_rank=512`, `qk_nope_head_dim=128`, `qk_rope_head_dim=64`, `v_head_dim=128`) for a compact KV cache.
- **Mixture-of-Experts**: 64 routed experts with top-8 selection plus 1 shared expert. The first two layers use a dense MLP (`first_k_dense_replace=2`); all subsequent layers are MoE.
- **Sigmoid Routing with Bias Correction**: sigmoid scoring with auxiliary-loss-free load balancing via `e_score_correction_bias` (`topk_method=noaux_tc`, `routed_scaling_factor=2.446`).
- **Interleaved RoPE**: rotary embeddings with `rope_theta=1,000,000`, no scaling.

### Comparison with Gravity-16B-A3B-Base

| Parameter | Gravity-30B-A5B-Base | Gravity-16B-A3B-Base |
|---|---|---|
| **Layers** | 52 | 28 |
| **Dense Layers** | 2 | 1 |
| **Total / Active Params** | 29.56B / 5.34B | 16.24B / 3.16B |
| **Context Length** | 131,072 | 32,768 |
| **HF Architecture** | `GravityMoEForCausalLM` | `GravityMoEForCausalLM` |
| **Tokenizer** | GLM-4.5 (151,552) | GLM-4.5 (151,552) |

### Tokenizer

The tokenizer is initialized from [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) (vocabulary size 151,552). Internal evaluations across multilingual corpora found it more efficient in fertility and compression ratio than alternatives, especially for mixed English-Korean text. For the base model, `eos_token` is `<|endoftext|>`.

## Training

1. **Block Expansion (LLaMA-Pro style)** — Initialized from Gravity-16B-A3B-Base by stacking additional transformer blocks into the existing layer stack (28 → 52 layers), then warmed up at 4K context.
2. **Continued Pretraining / Annealing** — 32K context on a high-quality mixture emphasizing STEM, code, mathematics, medical literature and Korean web/text corpora.
3. **Long-Context Extension** — 128K context training on a long-document mixture (`rope_theta=1e6`, no RoPE scaling).

## Quickstart

### Installation

```bash
pip install "transformers>=4.57" torch
```

### Using Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "trillionlabs/Gravity-30B-A5B-Base"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="auto",
)

input_ids = tokenizer("The theory of relativity states that", return_tensors="pt").input_ids.to(model.device)
output = model.generate(input_ids, max_new_tokens=128, do_sample=True, temperature=0.7)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Deployment

> **Note:** We are working on upstreaming native GravityMoE support to [SGLang](https://github.com/sgl-project/sglang). Until the PR is merged, please use the fork below. Internally the model is DeepSeek-V3-compatible, so the fork only registers the `GravityMoEForCausalLM` name onto SGLang's DeepSeek-V3 implementation.

### SGLang

Install SGLang from the [sglang-gravity](https://github.com/trillion-labs/sglang-gravity) fork (based on SGLang v0.5.19):

```bash
pip install "sglang[all] @ git+https://github.com/trillion-labs/sglang-gravity.git#subdirectory=python"
```

Launch the server:

```bash
python3 -m sglang.launch_server \
    --model-path trillionlabs/Gravity-30B-A5B-Base \
    --host 0.0.0.0 --port 30000 \
    --tp 4 --context-length 131072 \
    --trust-remote-code --dtype bfloat16
```

## Limitations

- This is a base pretrained model without instruction tuning or safety alignment. It may generate factually incorrect, biased, or harmful content.
- Performance may degrade on languages not well-represented in the training data.

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
@misc{gravity-30b-base-2026,
    title={Gravity-30B-A5B-Base},
    author={Trillion Labs},
    year={2026},
    url={https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base}
}
```

## Contact

- Website: [trillionlabs.co](https://trillionlabs.co)
- Website: [lunit.io](https://www.lunit.io)
