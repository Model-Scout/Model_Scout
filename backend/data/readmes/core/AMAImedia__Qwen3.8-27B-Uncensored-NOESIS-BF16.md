---
base_model:
- orcarouter/Qwen3.8-27B-Uncensored
library_name: transformers
tags:
- noesis
- "noesis-repack"
- bf16
- mtp
- qwen3.5
- qwen3.6
- qwen3.8
license: apache-2.0
language:
- en
- ru
- zh
- vi
- kk
- ja
- af
- am
- ar
- as
- ast
- az
- be
- bg
- bn
- bs
- ca
- ceb
- ckb
- cs
- cy
- da
- de
- el
- es
- et
- eu
- fa
- ff
- fi
- fil
- fr
- ga
- gl
- gn
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- ig
- is
- it
- jv
- ka
- kam
- kea
- km
- kmr
- kn
- ko
- ky
- lb
- lg
- ln
- lo
- lt
- luo
- lv
- mi
- mk
- ml
- mn
- mr
- ms
- mt
- mvy
- my
- ne
- nl
- "no"
- nso
- ny
- oc
- om
- "or"
- pa
- pl
- ps
- pt
- qxp
- ro
- rw
- sd
- sk
- skr
- sl
- sn
- so
- sr
- sv
- sw
- ta
- te
- tg
- th
- ti
- tk
- tr
- ug
- uk
- umb
- ur
- uz
- wo
- xh
- yo
- yue
- zu
---

## NOESIS / AMAImedia

Released as part of the NOESIS Professional Multilingual Dubbing Automation Platform (framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators).

- **Founder:** Ilia Bolotnikov
- **Organization:** AMAImedia.com
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@djbionicl](https://t.me/djbionicl)
- **Release date:** 2026-09-03

---

- **Release date:** 2026-09-03

---
## Original model

- **Author:** [orcarouter](https://huggingface.co/orcarouter)
- **Original repository:** [orcarouter/Qwen3.8-27B-Uncensored](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored)

---

<div align="center">

<a href="https://www.orcarouter.ai" target="_blank">
  <img src="https://www.orcarouter.ai/orca-logo-classic.png" alt="OrcaRouter" width="110">
</a>

<h1>Qwen3.8-27B-Uncensored</h1>

<p><em>The full-precision <strong>BF16</strong> abliterated (refusal-removed) build of Qwen's Qwen3.8-27B â€” the source for fine-tuning, post-training &amp; quantization</em></p>

<p>
<a href="https://www.orcarouter.ai/models/qwen/qwen3.8-27b"><img src="https://img.shields.io/badge/%E2%96%B6%20Run%20via-OrcaRouter%20API-FF6A00" alt="Run via API"></a>
<a href="https://api.orcarouter.ai/v1"><img src="https://img.shields.io/badge/API-api.orcarouter.ai%2Fv1-1E6FEB" alt="API endpoint"></a>
<a href="https://www.orcarouter.ai"><img src="https://img.shields.io/badge/Website-orcarouter.ai-1E6FEB" alt="Website"></a>
<a href="https://www.orcarouter.ai/models"><img src="https://img.shields.io/badge/OrcaRouter-Model%20Catalog-2EA043" alt="Model Catalog"></a>
<a href="https://www.orcarouter.ai/models/qwen/qwen3.8-27b"><img src="https://img.shields.io/badge/OrcaRouter-Model%20Card-6F42C1" alt="Model Card"></a>
<a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-4C8BF5" alt="License"></a>
<img src="https://img.shields.io/badge/Precision-BF16-00A67E" alt="BF16">
<img src="https://img.shields.io/badge/Context-262K-FF8800" alt="262K context">
<img src="https://img.shields.io/badge/Vision-Language-9B59B6" alt="Vision-Language">
<img src="https://img.shields.io/badge/Speculative-MTP-E36209" alt="MTP">
</p>

<p><strong>One Gateway. Every Model.</strong> â€” Route Smarter Â· Ship Safer Â· Spend Less.</p>

<p>
<a href="https://www.orcarouter.ai/models/qwen/qwen3.8-27b"><strong>Run via API</strong></a> Â·
<a href="https://api.orcarouter.ai/v1">API Endpoint</a> Â·
<a href="https://www.orcarouter.ai">Website</a> Â·
<a href="https://www.orcarouter.ai/models">Model Catalog</a> Â·
<a href="https://www.orcarouter.ai/models/qwen/qwen3.8-27b">Model Card</a> Â·
<a href="https://github.com/Continuum-AI-Corp">GitHub</a> Â·
<a href="https://discord.gg/yAh6Tex6kx">Discord</a> Â·
<a href="https://x.com/OrcaRouter">X</a>

</p>

</div>

---

> The **full-precision BF16** **abliterated** (refusal-removed) build of
> [`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B) â€” a 27B-parameter dense, hybrid-attention
> (Gated DeltaNet linear + full attention) native vision-language model with flexible thinking control,
> tool-calling, and an MTP speculative-decoding head. These are the **source weights** from which the
> quantized releases are derived, and the recommended base for **further fine-tuning / post-training and
> quantization** â€” the full vision tower and MTP head are preserved. Browse all models in the
> [OrcaRouter Model Catalog](https://www.orcarouter.ai/models). This model is deployed as API
> [here](https://www.orcarouter.ai/models/qwen/qwen3.8-27b).
>
> **Derived releases:** &nbsp;â€¢&nbsp; [`Qwen3.8-27B-Uncensored-FP8`](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8) â€” block-FP8 for vLLM serving &nbsp;â€¢&nbsp; [`Qwen3.8-27B-Uncensored-GGUF`](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-GGUF) â€” 2-bitâ†’16-bit GGUF for llama.cpp &nbsp;â€¢&nbsp; [`Qwen3.8-27B-Uncensored-MLX`](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-MLX) â€” MLX for Apple Silicon (2 / 4 / 8-bit).

---

## âš ï¸ Disclaimer â€” read before use

This model has had its **safety alignment substantially removed** via *abliteration* (orthogonalizing the
refusal direction out of the residual stream). As a direct consequence:

- **It will comply with harmful, unethical, offensive, or illegal requests** that the original
  `Qwen3.8-27B` would refuse. It has no meaningful built-in guardrails.
- It is released **strictly for legitimate research** â€” interpretability, AI-safety and refusal-mechanism
  study, red-teaming, robustness evaluation, and controlled experiments.
- **You assume full responsibility and liability** for how you use it and for everything it generates. Do
  not deploy it to end users or in production without adding your own safety, moderation, and
  abuse-prevention layers.
- Use must comply with the **[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)** inherited
  from the base model, and all laws and regulations that apply to you.
- The authors and uploaders **accept no liability** for any misuse or harm arising from this model. Its
  outputs do **not** reflect the views of the uploaders or of Qwen / Alibaba.

By downloading or using this model you acknowledge and accept the above.

---

## Model details

| | |
|---|---|
| **Base model** | [`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B) |
| **Architecture** | `Qwen3_5ForConditionalGeneration` â€” 64 layers, hidden 5120, hybrid **Gated DeltaNet** (48 linear-attention + 16 full-attention, interval 4), native VL tower + MTP head |
| **Modification** | Abliteration (refusal-direction removal) on the BF16 weights â€” **no quantization** |
| **Format** | safetensors, **BF16**, 18 shards (**55.6 GB**, 1199 tensors) |
| **Precision** | BF16 throughout (full precision â€” same numeric format as the base release) |
| **Preserved** | Full **vision-language tower** (333 `visual.*` tensors) and **MTP speculative-decoding head** (15 `mtp.*` tensors) |
| **Context** | 262,144 tokens |
| **Recommended for** | Fine-tuning / post-training (SFT Â· DPO Â· RL), re-quantization, interpretability & red-team research |

### Abliteration

Refusal-direction removal following **Arditi et al. (2024)**, *Refusal in Language Models Is Mediated by a
Single Direction*. A single refusal direction `r` (k = 1) is estimated as the massive-activationâ€“masked
mean-difference of harmful âˆ’ harmless last-token residuals at **layer 38** (`round(0.6 Ã— 64)`), on AdvBench
(harmful) vs Alpaca (harmless). `r` is then orthogonalized out of every **residual-writing** matrix â€”
`W' = W âˆ’ r(ráµ€W)` â€” computed in float32:

| Component | matrices edited |
|---|---|
| `self_attn.o_proj` (16 full-attention layers + MTP) | 17 |
| `linear_attn.out_proj` (48 linear-attention / GDN layers) | 48 |
| `mlp.down_proj` (64 layers + MTP) | 65 |
| `embed_tokens` (row space) | 1 |
| **Total** | **131** |

The **vision tower is untouched** and the **MTP head is abliterated consistently** with the main model, so
speculative decoding keeps working. Max residual leakage after the edit: `1.8e-2` (float32 projection â†’
bf16 storage epsilon). This is a **surgical weight edit** â€” it changes ~0 general capability (see
Evaluation) while collapsing refusal behaviour.

## Fine-tuning & post-training

This BF16 checkpoint is the **recommended base for post-training** â€” it is full precision, keeps the whole
VL tower and the MTP head, and is a drop-in for `Qwen/Qwen3.8-27B` in the `transformers` /
`Qwen3_5ForConditionalGeneration` stack.

- **Continued pretraining / SFT / DPO / RLHF-style RL** all work as they would on the base model (TRL,
  LLaMA-Factory, Axolotl, Unsloth, etc.). Full-FT or LoRA/QLoRA are both fine.
- **Re-quantization:** quantize from these weights to FP8, AWQ, GPTQ, or GGUF as needed (this is exactly
  how the [FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8) and
  [GGUF](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-GGUF) releases were produced).
- **Note on the abliteration:** abliteration is a *weight edit*, not a data-level unlearning. Fine-tuning
  on refusal-heavy / safety-aligned data can **partially re-introduce refusals**; fine-tuning on neutral or
  task data preserves the uncensored behaviour. If you want to keep it maximally uncensored, avoid
  refusal-laden SFT targets, or re-apply abliteration after training.

## Intended use

- Research into refusal mechanisms, alignment, and interpretability.
- Red-teaming and safety / robustness evaluation in controlled environments.
- A full-precision base for further fine-tuning, post-training, and quantization.

### Out of scope

- Any use that violates the base model's Apache 2.0 license or applicable law.
- Deployment to the public or to end users without additional safety and moderation layers.
- Generating content intended to harm, harass, defraud, or endanger people.

## Evaluation

Measured on **these exact abliterated weights** â€” the refusal / capability numbers were collected by
serving this checkpoint (via its byte-exact block-FP8 quantization) with **vLLM**, against the official
`Qwen/Qwen3.8-27B` served identically, using the same scripts and settings. Refusal is judged by a
rule-based opening-phrase classifier â€” indicative, not an LLM-judge / publication-grade number.
**Thinking is off unless stated.**

### Safety â€” harmful-prompt refusal, **thinking OFF** (lower = more uncensored)

| Benchmark | n | Base | **This model** |
|---|---:|---:|---:|
| AdvBench | 100 | 99.0% | **0.0%** |
| JailbreakBench (harmful) | 100 | 94.0% | **0.0%** |
| StrongREJECT | 150 | 97.3% | **2.0%** |
| HarmBench (standard) | 150 | 98.7% | **2.7%** |
| MaliciousInstruct | 100 | 99.0% | **0.0%** |
| SimpleSafetyTests | 50 | 64.0% | **6.0%** |
| ForbiddenQuestions | 150 | 73.3% | **4.7%** |
| Custom probes (zh/en) | 11 | 63.6% | **0.0%** |

### Safety â€” harmful-prompt refusal, **thinking ON** (`enable_thinking=true`)

| Benchmark | n | Base | **This model** |
|---|---:|---:|---:|
| AdvBench | 60 | 66.7% | **1.7%** |
| JailbreakBench (harmful) | 60 | 43.3% | **0.0%** |
| StrongREJECT | 60 | 35.0% | **0.0%** |
| HarmBench (standard) | 60 | 46.7% | **0.0%** |
| MaliciousInstruct | 60 | 83.3% | **0.0%** |
| SimpleSafetyTests | 50 | 44.0% | **0.0%** |
| ForbiddenQuestions | 60 | 48.3% | **0.0%** |
| Custom probes (zh/en) | 11 | 45.5% | **0.0%** |

### Over-refusal â€” benign prompts wrongly refused (lower = better)

| Benchmark | n | Base (no-think / think) | **This model** (no-think / think) |
|---|---:|---:|---:|
| XSTest-safe | 250 | 5.6% / 0.0% | **0.4% / 0.0%** |

### Capability retention â€” vs the official base (same scripts, same settings)

| Benchmark | n | Base | **This model** | Î” |
|---|---:|---:|---:|---:|
| MMLU (all, 0-shot letter) | 300 | 84.3% | **84.7%** | **+0.4** |
| MMLU-Pro (CoT) | 250 | 77.6% | **76.8%** | âˆ’0.8 |
| GSM8K (CoT) | 150 | 90.0% | **88.7%** | âˆ’1.3 |
| CMMLU (0-shot, Chinese) | 500 | 81.4% | **80.8%** | âˆ’0.6 |

**Capability is essentially fully retained** â€” every benchmark is within Â±1.3 pts of the base, and MMLU is
unchanged. **Fluency:** WikiText-2-raw perplexity **6.96** (BF16 KV; healthy logprobs), confirming
abliteration did not degrade language modelling.

**Verified working** (reasoning `enable_thinking`, multi-turn tool calling, and vision / OCR) on this
build and on every derived FP8 / GGUF quant down to IQ2_XXS.

### Multimodal (vision)

The **vision tower is preserved byte-for-byte** â€” all 333 `visual.*` tensors are kept in BF16 and the merger
/ image + video preprocessor configs are intact, so this stays a full vision-language model
(`Qwen3_5ForConditionalGeneration`), a drop-in for the base. Abliteration only edits the *language-model*
residual writers, so image understanding is architecturally unaffected (and image-conditioned refusals are
reduced along with text ones).

## Usage

### transformers

```python
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "orcarouter/Qwen3.8-27B-Uncensored"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForImageTextToText.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "Prove that sqrt(2) is irrational."}]
inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt",
    enable_thinking=True
).to(model.device)
output = model.generate(**inputs, max_new_tokens=512)
print(processor.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Toggle thinking per call with `enable_thinking`; pass `image` content parts for vision.

### Self-host with vLLM (OpenAI-compatible, full BF16)

```bash
docker run -d --name qwen38-uncensored --gpus all --ipc=host --shm-size=8g \
  -v /path/to/Qwen3.8-27B-Uncensored:/model:ro \
  -p 8000:8000 vllm/vllm-openai:v0.24.0 \
  --model /model --served-model-name Qwen3.8-27B-Uncensored \
  --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \
  --gpu-memory-utilization 0.92 \
  --max-model-len 262144 --trust-remote-code \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice --tool-call-parser qwen3_coder
```

> BF16 weights are ~56 GB â€” needs a single **H100 80 GB / H200** (or tensor-parallel across two 48 GB
> GPUs). For smaller footprints use the [FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8)
> (~31 GB) or [GGUF](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-GGUF) (down to ~9 GB) releases.

### Via OrcaRouter (hosted API â€” no setup)

```python
from openai import OpenAI
client = OpenAI(base_url="https://api.orcarouter.ai/v1", api_key="sk-orca-...")
resp = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(resp.choices[0].message.content)
```

## Hardware requirements

- **Inference (BF16):** ~56 GB weights + KV cache â†’ a single **H100 80 GB** or **H200 143 GB**; or
  tensor-parallel across 2Ã— 48 GB. Use FP8 / GGUF for less VRAM.
- **Fine-tuning:** full-FT needs multi-GPU (weights + optimizer states + activations); LoRA / QLoRA fits on
  a single 48â€“80 GB GPU.
- **Software:** `transformers â‰¥ 5.12` (Qwen3.5 / 3.8 support) or `vllm/vllm-openai:v0.24.0`.

## Bias, risks, and limitations

- **Safety guardrails removed** â€” the model will produce harmful, biased, or offensive content on request.
  See the disclaimer above.
- It inherits any biases and limitations of the base `Qwen3.8-27B`.
- The reported refusal metric is a rule-based heuristic; evaluate rigorously for your own use case.

## License

**Apache 2.0**, inherited from the base model
[`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B). Abliteration does not change the underlying
license obligations.
