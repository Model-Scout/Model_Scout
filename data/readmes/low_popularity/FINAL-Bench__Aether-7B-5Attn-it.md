---
license: apache-2.0
language:
- en
- ko
base_model: FINAL-Bench/Aether-7B-5Attn
datasets:
- HuggingFaceFW/fineweb-edu
- HuggingFaceTB/smollm-corpus
- HuggingFaceTB/finemath
- open-web-math/open-web-math
- OpenCoder-LLM/opc-fineweb-code-corpus
- HAERAE-HUB/KOREAN-WEBTEXT
- HAERAE-HUB/KOREAN-SyntheticText-1.5B
pipeline_tag: text-generation
library_name: transformers
tags:
- foundation-model
- sovereign-ai
- fully-open
- open-source
- mixture-of-experts
- moe
- heterogeneous-attention
- latin-square
- instruct
- sft
- fine-tuned
- korean
- vidraft
- aether
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Aether-7B-5Attn-it

## Update — 2026-07-20 (Korean instruction tuning v3)

This checkpoint has been refreshed with an expanded Korean instruction-tuning run.

| | |
|---|---|
| Training data | **14,865 samples** — Korean general instructions (12,000) + Korean exam-style reasoning (2,400) + model identity (465) |
| Method | LoRA (r16, alpha32) on q/k/v/o/gate/up/down projections, completion-only loss, entropy-gated weighting |
| Schedule | 1 epoch, LR 2e-4, merged back into the base weights |
| Language policy | Korean prompts are answered in Korean, English prompts in English (language-matched training data) |

### What changed

- **Korean responsiveness.** The previous checkpoint frequently returned empty completions for
  Korean prompts; this revision answers them.
- **Model identity.** The model now identifies itself as an AETHER model developed by **VIDRAFT**.
- **Language matching.** Korean in, Korean out; English in, English out.

### Known limitations

- **Factual accuracy in Korean history/knowledge remains weak.** The instruction mix was not
  large enough to reliably ground factual questions; verify factual claims before relying on them.
- **Repetition under greedy decoding.** Use sampling (e.g. `temperature=0.7`, `top_p=0.9`)
  rather than pure argmax decoding.
- This is a **7B-class MoE base with light instruction tuning**, not a fully aligned chat model.

<!-- AETHER-FAMILY-LINKS -->

**Aether family** — [![5Attn Base](https://img.shields.io/badge/%F0%9F%A7%AC_Aether--7B--5Attn-Fully_Open-green)](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) [![7Attn Base](https://img.shields.io/badge/%F0%9F%A7%A9_Aether--7B--7Attn--base-Open_Weights-teal)](https://huggingface.co/FINAL-Bench/Aether-7B-7Attn-base) [![11Attn](https://img.shields.io/badge/%F0%9F%94%9F_Aether--6B--11Attn-Open_Weights-purple)](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn) [![Checkpoints](https://img.shields.io/badge/%F0%9F%97%82%EF%B8%8F_Checkpoints-Intermediate-lightgrey)](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints) [![Demo](https://img.shields.io/badge/%F0%9F%9A%80_Demo-Aether_Sovereign_AI-orange)](https://huggingface.co/spaces/FINAL-Bench/Aether-Sovereign-AI) [![Blog](https://img.shields.io/badge/%F0%9F%93%9D_Blog-Open_Source_LLM-yellow)](https://huggingface.co/blog/FINAL-Bench/opensource-llm) [![Collection](https://img.shields.io/badge/%F0%9F%93%9A_Collection-Aether_Foundation-blue)](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)

<!-- /AETHER-FAMILY-LINKS -->

### Which Aether model should I use?

| Model | What it is | Pick it if |
|---|---|---|
| [**Aether-7B-5Attn**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) | 6.59B MoE base. **Fully open** - weights + data recipe + training code + all 162k-step logs + checkpoints | You want to audit, verify or rebuild a foundation model end to end |
| [**Aether-7B-5Attn-it**](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn-it) | The same model, instruction-tuned | You want it to answer rather than continue text |
| [**AETHER-7B-7Attn-base**](https://huggingface.co/FINAL-Bench/AETHER-7B-7Attn-base) | Same 49-layer architecture, a different checkpoint. Open weights | You want a second run of this architecture to compare against |
| [**Aether-6B-11Attn-base**](https://huggingface.co/FINAL-Bench/Aether-6B-11Attn-base) | 121 layers, **11 sequence-mixing mechanisms** in one network - attention, Mamba-2, Hyena, GDN, MLA - on an 11x11 Latin square | You research heterogeneous sequence mixing. It is a mid-training research artifact |

All four load the same way:

```python
AutoModelForCausalLM.from_pretrained(MODEL, trust_remote_code=True, dtype=torch.bfloat16)
```


![Aether-7B-5Attn](aether_hero.png)

[![Blog](https://img.shields.io/badge/%F0%9F%A4%97%20Blog-Read%20the%20Aether%20story-FFD21E)](https://huggingface.co/blog/FINAL-Bench/opensource-llm)



> 📚 **Part of the [Aether Foundation Model collection](https://huggingface.co/collections/FINAL-Bench/aether-foundation-model)** — base, instruction-tuned, and checkpoints in one place.

> 🧩 **Intermediate checkpoints** (110k · 115k · 162k) are released as a dataset: [Aether-7B-5Attn-checkpoints](https://huggingface.co/datasets/FINAL-Bench/Aether-7B-5Attn-checkpoints).
**Instruction-tuned (SFT) version of the fully-open [Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn) base model.** Post-trained for multiple-choice / benchmark-style answering. 6.59B MoE (~2.98B active), 49 layers on a 7×7 Latin square. **Apache-2.0.**

## Learning rate chosen by held-out accuracy, not loss

Full-parameter SFT was run at three learning rates (2e-6 / 6e-6 / 2e-5). The final checkpoint was selected by **held-out benchmark accuracy, not training loss** — for small models a high LR lowers training loss while degrading real capability, so loss is the wrong selector.

| LR | K-AI 4 avg | Note |
|----|-----------|------|
| 2e-6 | 29.7% | Under-fit (weak on some subjects) |
| **6e-6 (selected)** | **34.9%** | Best & balanced, no degradation |
| 2e-5 | 32.3% | One subject collapsed (format-degradation sign) |

## Held-out results (selected checkpoint, 6e-6)

- **GPQA-Diamond (198):** 25.3%
- **K-AI 4 average (195):** **34.9%**
  - musr_ko 26.5% · com2_main_ko 50.0% · click 32.0% · kommlu_pro 30.4%
- **vs base (before SFT):** base 26.7% → **34.9% (+8.2pp)** — same held-out set, same harness.

*All evaluations use held-out sets not seen in training. SFT was performed on MMLU-auxiliary (multiple-choice format), which does not overlap with the evaluation subjects (GPQA / K-AI).*

## Pretraining data mix (inherited from base)

| Domain | Share |
|--------|-------|
| Math (finemath + open-web-math) | 37.8% |
| Korean (webtext + synth) | 21.6% |
| English web & synthetic (fineweb-edu + cosmopedia) | 21.6% |
| Code (opc) | 13.5% |
| phase15 pre-blend | 5.4% |

*This is the **base pretraining** mix. This model's post-training (SFT) data is MMLU-auxiliary.*

## Architecture (inherited from base)

Identical to Aether-7B-5Attn base: 49 layers placed on a **7×7 Latin square** with heterogeneous attention (7 labels / 5 distinct mechanisms) and a 25-expert MoE (top-7 + 1 shared). Full structural detail and the diagram are in the base card, §3.2:
[FINAL-Bench/Aether-7B-5Attn](https://huggingface.co/FINAL-Bench/Aether-7B-5Attn).

## Open-source fully-open LLMs — 6-country comparison

![Open-source LLM comparison](opensource_llm_comparison.png)

*Relative to the base Aether. Among six sovereign fully-open models, VIDRAFT is the only single AI startup, and Aether has the most attention types (5) in a Latin-square layout.*

## Running the model

### 1. Loading

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL = "FINAL-Bench/Aether-7B-5Attn-it"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(
    MODEL, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda"
).eval()
```

`trust_remote_code=True` is required: this is a custom architecture (`aether_v2_7way`),
and the modeling code ships in this repository. Loading needs roughly **14 GB of VRAM**
in bfloat16.

> The module files also remain under `aether_pkg/` for anyone who was importing them
> directly; the copies at the repository root are what `trust_remote_code` resolves.

### 2. `use_cache=False` is mandatory

This architecture ships **no KV cache**. Leaving `use_cache` enabled raises an
`IndexError` from the standard cache path. Set it on the config *and* keep it off
in `generate()`.

### 3. Generation is slow — plan for it

With no KV cache, every new token re-runs the full forward pass, so decoding is
**O(n²)** in sequence length. Measured throughput:

| Hardware | Throughput |
|---|---|
| NVIDIA T4 (16 GB) | **~1.5 tokens/s** — 64 tokens takes about 40 s |
| NVIDIA B200 | ~7 tokens/s |

Keep `max_new_tokens` small. This is a property of the released architecture, not a
configuration problem.

```python
# REQUIRED: this checkpoint was trained with attention_mask=None. generate() builds a
# mask automatically, which puts the model off-distribution and degenerates the output
# (you get things like "국가의 수도는 국가의 수도입니다..." instead of an answer).
# Drop the mask before it reaches the model:
_forward = model.forward
def _forward_without_mask(*a, **kw):
    kw.pop("attention_mask", None)
    return _forward(*a, **kw)
model.forward = _forward_without_mask

out = model.generate(
    tok(prompt, return_tensors="pt").input_ids.to("cuda"),
    max_new_tokens=64, do_sample=False, use_cache=False,
    pad_token_id=tok.eos_token_id,
)
print(tok.decode(out[0], skip_special_tokens=True))
```

### Why the mask has to go

Measured on 2026-07-20, same prompt, greedy decoding, only the mask varied:

| attention_mask | Output for `너는 누구야?` |
|---|---|
| **absent** | *저는 비드래프트(VIDRAFT)의 AETHER 모델입니다. 7종의 서로 다른 어텐션 메커니즘을…* |
| present (generate default) | *비드래프트(VIDRAFT)의 한국어입니다. 비드래프트는 비드래프트의…* (degenerate) |

This is a property of how the checkpoint was tuned, not a bug in `generate()`.
Greedy decoding is also recommended — sampling drifts off-distribution on this checkpoint.

### 4. Prompt format

Instruction tuning used a plain format — the instruction, a blank line, then the
response. The bundled `chat_template.jinja` reproduces exactly this, so
`apply_chat_template` and the raw form below are equivalent:

```python
prompt = "대한민국의 수도는 어디인가요?" + "\n\n"
```

### 5. Quality caveats — please read before use

Instruction tuning here is **light**: 14,865 samples for a single epoch. Measured
consequences, stated plainly:

- **Sensitive to prompt format and decoding settings.** Outputs degrade sharply
  once you move away from the trained format. Greedy decoding on the format above
  is the only configuration we validated.
- **Factual accuracy in Korean history and general knowledge is weak.** The model
  produces fluent but confidently wrong statements. Verify anything factual.
- **Benchmark:** on a held-out 4-subject Korean set (CLIcK / KMMLU / MuSR / Com2,
  80 items, no train overlap) this revision scores **31.2%** against **33.8%** for
  the previous one — within noise of each other and near the 25% random baseline.
- Treat this as a **lightly instruction-tuned research checkpoint**, not a
  production assistant.
## Contact
VIDRAFT (주식회사 비드래프트) · arxivgpt@gmail.com · License: Apache-2.0
