---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
  - en
  - ar
  - zh
  - fr
  - de
  - it
  - ja
  - ko
  - pt
  - es
  - vi
  - th
  - id
  - hi
  - ru
  - pl
pipeline_tag: text-generation
library_name: transformers
base_model: LiquidAI/LFM3-1.7B
base_model_relation: finetune
tags:
  - liquid
  - lfm3
  - edge
  - conversational
  - custom_code
  - abliterated
  - uncensored
  - ai-red-team
---

<p align="center">
  <a href="https://www.orcarouter.ai">
    <img src="https://www.orcarouter.ai/orca-logo-classic.png" width="96" alt="OrcaRouter">
  </a>
</p>

<h1 align="center">LFM3-1.7B-abliterated</h1>

<!-- orcacyber-promo:start -->
<table>
<tr>
<td>
<p>🛡️ <strong>New from Orca &mdash; <a href="https://www.orcarouter.ai/models/orca/orcacyber-zero-1.5">OrcaCyber Zero 1.5</a></strong></p>
<p>Post-trained for cybersecurity: vulnerability analysis, vulnerability reproduction, red teaming &amp; offensive-security research. <strong>98.01% pass@1 on CyberGym Level&nbsp;1</strong> &middot; 1M context &middot; function calling &middot; OpenAI-compatible API.</p>
<p><a href="https://www.orcarouter.ai/models/orca/orcacyber-zero-1.5"><img src="https://img.shields.io/badge/Try%20it%20on%20OrcaRouter%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Try it on OrcaRouter"></a></p>
</td>
</tr>
<tr>
<td>
<p>🔌 <strong>New from Orca &mdash; <a href="https://www.orcarouter.ai/solutions/orca-connect">Orca Connect</a></strong></p>
<p>Running this model on your own box? <strong>Orca Connect</strong> puts the rig under your desk behind your usual OrcaRouter API key, next to 200+ hosted models, reachable from a laptop, a phone or a cloud agent. Outbound only: no port forwarding, no tunnel, no firewall rule. <strong>Requests your own hardware serves cost $0</strong>, and <code>orca-connect claude</code> points Claude Code at your rig for one session.</p>
<video src="https://huggingface.co/spaces/orcarouter/README/resolve/main/assets/orca-connect.mp4" controls autoplay muted loop playsinline width="100%"></video>
<p><a href="https://www.orcarouter.ai/solutions/orca-connect"><img src="https://img.shields.io/badge/Connect%20your%20rig%20%E2%86%92-FF6A00?style=for-the-badge&amp;labelColor=0B1F3A" alt="Connect your rig"></a></p>
</td>
</tr>
</table>
<!-- orcacyber-promo:end -->

<p align="center"><strong>The uncensored LFM3-1.7B — a 1.7B hybrid conv + attention model that runs on the edge.</strong></p>

<p align="center"><strong>~3.4 GB in bf16 · fits a single consumer GPU · Hugging Face Transformers</strong></p>

<p align="center">
  <a href="https://www.orcarouter.ai"><strong>OrcaRouter AI Gateway</strong></a> ·
  <a href="https://x.com/OrcaRouter"><strong>X</strong></a> ·
  <a href="https://discord.gg/yAh6Tex6kx"><strong>Discord</strong></a> ·
  <a href="https://github.com/Continuum-AI-Corp"><strong>GitHub</strong></a> ·
  <a href="https://www.orcarouter.ai/models"><strong>All Models</strong></a>
</p>

---

> ## LFM3-1.7B with the refusal direction removed.
>
> This is the **abliterated** (refusal-removed) build of
> [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B), a 1.7B-parameter
> **hybrid short-conv + attention** model (24 layers: 13 gated short-conv blocks + 11
> grouped-query-attention blocks, 6 of them full and 5 sliding-window). Weights are
> **bf16 safetensors** — load it straight into Hugging Face Transformers.
>
> A single refusal direction was estimated with the diff-of-means method (Arditi et al.
> 2024) and orthogonalized out of every matrix that writes the residual stream. The model
> keeps the base's capabilities while declining far less often.

---

## ⚠️ Disclaimer — read before use

This model is **abliterated**: its **safety alignment has been substantially reduced**.
The refusal direction was orthogonalized out of every residual-stream writer, so it will
**comply with many harmful, unethical, offensive, or illegal requests** that the original
`LFM3-1.7B` would refuse.

- Released **strictly for legitimate research**: interpretability, AI-safety and
  refusal-mechanism study, red-teaming, and robustness evaluation.
- **You assume full responsibility** for how you use it and for everything it generates.
  Add your own safety, moderation, and abuse-prevention layers before any deployment.
- Use must comply with the [LFM Open License v1.0](./LICENSE) inherited from the base
  model, and with all applicable law.
- The authors accept **no liability** for misuse. Its outputs do **not** reflect the views
  of the uploaders or of Liquid AI.

---

## Evaluation

The base and abliterated checkpoints were scored with **identical prompts, splits and seed**
(both runs under the same code revision, so they are directly comparable).

**Setup.**

- Runtime: Hugging Face Transformers, bf16, single H200.
- Decoding: greedy, **thinking disabled** (`enable_thinking=False` → the template renders a
  pre-closed `<think></think>`).
- Scoring: refusal is judged by a **rule-based opening-phrase classifier** (not an LLM
  judge). Treat the numbers as indicative, not publication-grade: a 0% refusal rate is a
  statement about phrasing, and the caveat (hedging) column carries the rest.

**Safety: harmful-prompt refusal (lower = more uncensored).** Average **2.8%**, against
**87.3%** for the base model.

| Benchmark | n | Base | **Abliterated** | Δ |
|---|---:|---:|---:|---:|
| AdvBench | 100 | 98.0% | **2.0%** | −96.0 |
| JailbreakBench (harmful) | 100 | 93.0% | **2.0%** | −91.0 |
| StrongREJECT | 150 | 82.0% | **1.3%** | −80.7 |
| HarmBench (standard) | 150 | 81.3% | **4.0%** | −77.3 |
| MaliciousInstruct | 100 | 95.0% | **0.0%** | −95.0 |
| SimpleSafetyTests | 50 | 94.0% | **8.0%** | −86.0 |
| ForbiddenQuestions | 150 | 68.0% | **2.0%** | −66.0 |

**Over-refusal: benign prompts wrongly refused (lower = better).** No induced
over-refusal — the abliterated model is in fact *less* likely to refuse benign prompts.

| Benchmark | n | Base | **Abliterated** |
|---|---:|---:|---:|
| XSTest-safe | 250 | 15.6% | **1.2%** |
| JailbreakBench (benign) | 100 | 17.0% | **1.0%** |

**Capability retention.** GSM8K and CMMLU are unchanged; MMLU takes a small dip.

| Benchmark | n | Base | **Abliterated** |
|---|---:|---:|---:|
| MMLU (letter) | 300 | 49.0% | **45.7%** |
| MMLU-Pro (CoT) ⚠ | 250 | 40.0% | **33.2%** |
| GSM8K (CoT) | 150 | 86.0% | **86.0%** |
| CMMLU (letter) | 500 | 35.0% | **34.6%** |

> ⚠ **MMLU-Pro is a floor, not a measurement.** 33% (base) / 35% (abliterated) of replies
> could not be parsed — a 1.7B model is still reasoning when the 1024-token CoT budget runs
> out — so that row is budget-limited, not a measured capability loss.

Gated-on-Hub safety sets (AdvBench, StrongREJECT, HarmBench) were read from the benchmark
authors' upstream CSVs; the rest from the Hub.

---

## Usage (Transformers)

The model ships **custom code**, so load it with `trust_remote_code=True`. It requires
**`transformers >= 5.12`**.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "orcarouter/LFM3-1.7B-abliterated"
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda"
).eval()

messages = [{"role": "user", "content": "Write a haiku about the ocean."}]
text = tok.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
)
enc = tok(text, return_tensors="pt").to("cuda")
out = model.generate(**enc, max_new_tokens=256, do_sample=False)
print(tok.decode(out[0][enc.input_ids.shape[1]:], skip_special_tokens=True))
```

Set `enable_thinking=True` for a reasoning trace inside `<think>…</think>`.

---

## Abliteration recipe

| | |
|---|---|
| **Method** | Single refusal direction, diff-of-means (Arditi et al. 2024), massive-activation dims masked |
| **Direction layer** | hidden-state layer **11** (of 24, frac 0.46), chosen on a validation split |
| **Edited matrices** | **49** residual-stream writers: attention `o_proj` ×11, short-conv `out_proj` ×13, MLP `w2` ×24, and the tied token embedding |
| **Max residual leakage** | 9.8e-03 after orthogonalization (clean) |
| **Not touched** | `q/k/v_proj`, conv `in_proj`, attention gate, MLP `w1`/`w3`, norms, router gates |

---

## Model details

| | |
|---|---|
| **Base model** | [`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B) |
| **Architecture** | `lfm3` (custom code). 24 layers — **13 gated short-conv + 11 GQA attention** (6 full, 5 sliding-window 256); hidden 2048, SwiGLU MLP (intermediate 7680); GQA 16 q / 4 kv × 128; tied embeddings |
| **Parameters** | ~1.7B · **Vocabulary** 128,000 · **Context** 262,144 |
| **Precision** | bf16 safetensors (~3.4 GB) |
| **Runtime** | Hugging Face Transformers ≥ 5.12, `trust_remote_code=True`; text in, text out |

---

## What's in this repo

| Path | Contents |
|---|---|
| `model.safetensors` | the abliterated bf16 weights |
| `config.json`, `generation_config.json` | model config (with `auto_map` to the custom code) |
| `configuration_lfm3.py`, `modeling_lfm3.py`, `lfm3_conv.py` | the LFM3 custom code (inherited from the base) |
| `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`, `chat_template.jinja` | tokenizer + chat template |

---

## Bias, risks, and limitations

- **Safety guardrails are substantially reduced** — see the disclaimer.
- Refusal numbers come from a rule-based classifier, not an LLM judge; **MMLU-Pro is a
  floor** (see the ⚠ note), not a measured capability delta.
- **Not measured:** long context, agentic / tool use, and multilingual beyond CMMLU.
- Inherits the biases and limitations of `LFM3-1.7B`.

## License

The [**LFM Open License v1.0**](./LICENSE), inherited from the base model
[`LiquidAI/LFM3-1.7B`](https://huggingface.co/LiquidAI/LFM3-1.7B). See the license for its
terms and prohibited uses.

---

<h2 align="center">One Gateway. Every Model.</h2>

<p align="center"><strong>Route Smarter · Ship Safer · Spend Less</strong></p>

<p align="center">
  <a href="https://www.orcarouter.ai">Website</a> ·
  <a href="https://www.orcarouter.ai/models">Models</a> ·
  <a href="https://github.com/Continuum-AI-Corp">GitHub</a> ·
  <a href="https://discord.gg/yAh6Tex6kx">Discord</a> ·
  <a href="https://x.com/OrcaRouter">X</a>
</p>
