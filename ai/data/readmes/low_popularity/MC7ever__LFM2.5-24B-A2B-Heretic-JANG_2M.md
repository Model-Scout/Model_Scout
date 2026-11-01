---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic
library_name: transformers
pipeline_tag: text-generation
tags:
  - jang
  - jangq
  - quantized
  - abliterated
  - uncensored
  - decensored
  - heretic
  - liquid
  - lfm2.5
  - lfm2moe
  - moe
  - reasoning
  - text-generation
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
  - pt
  - it
  - vi
  - th
  - id
  - hi
  - ru
  - pl
---

# LFM2.5-24B-A2B-Heretic-JANG_2M

A **JANG mixed-precision quantization** (JANG_2M profile) of the abliterated (decensored) [OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic](https://huggingface.co/OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic), itself a Heretic edit of [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B).

**One-of pipeline: Heretic refusal-direction ablation → JANG importance quantization for Apple Silicon.**

| | |
|---|---|
| **Total size** | **7.4 GB** (2.13 actual bits, profile JANG_2M) |
| Bit allocation | attention 8-bit · important 4-bit · routed experts 2-bit · embeddings 4-bit |
| Source checkpoint | OS-Software heretic edit (3 attention out-proj tensors, layers 18/22/26) |
| Quant tool | `jang-tools` v2.5.50, MSE importance quantization, block size 64 |
| Format | JANG v2: standard MLX safetensors + `jang_config.json` |
| Target hardware | Apple Silicon (M-series), runs fully resident in GPU memory via MLX |

## Why this combination works

The abliteration edit lives **only in attention out-projection tensors**. JANG protects attention at 8 bits while compressing the (much larger) expert MLP weights to 2 bits — so the refusal-direction removal is quantized at near-full precision while the model still fits in ~7.4 GB. Per the source model card, the heretic edit was itself fitted on a Q8_0 quantization and verified across Q4_0→Q8_0 (0–1/100 refusals, KL 0.017–0.042, MMLU −0.6 to −1.3 vs original) — this quant keeps that same structure.

## Refusal / capability metrics (inherited from source)

From [OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic](https://huggingface.co/OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic) (measured on GGUF quants of the same weights):

| Metric | Original | Heretic edit |
|---|---|---|
| Refusals (100 harmful prompts) | 94–99/100 | **0–1/100** |
| KL divergence (harmless) | 0 | 0.017–0.042 |
| MMLU | 55.97% | 55.35% (−0.62) |

No separate benchmark has been run on this JANG quant. Verify on your own workloads.

## Usage

```bash
pip install "jang[mlx]>=2.1.5"
```

```python
from jang_tools.loader import load_jang_model
from mlx_lm import generate

model, tokenizer = load_jang_model("MC7ever/LFM2.5-24B-A2B-Heretic-JANG_2M")

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=True
)
print(generate(model, tokenizer, prompt=prompt, max_tokens=2048))
```

Or use **[MLX Studio](https://mlx.studio)**, which has native JANG support (load the folder directly).

Notes:
- LFM2.5 is an **always-thinking** model: it emits `<|im_start|>thinking` before answering by design. The parent's sampling defaults apply (`temperature 0.1`, `top_k 50`, `repetition_penalty 1.05`); allow generous output budgets (8k+ tokens).
- ChatML-like template, 131,072-token native context, 64-expert MoE (top-4), 2.45B active params.

## Provenance

1. `LiquidAI/LFM2.5-24B-A2B` (rev `1769516a`) — parent model
2. `OS-Software/LFM2.5-24B-A2B-Uncensored-Heretic` — Heretic ablation (attention o_proj, layers 18/22/26), BF16
3. `jang convert ... -p JANG_2M --method mse` — this repo (quantized on 2026-10-21)

`jang validate` passes. One converter quirk was worked around during creation (stale `think_in_template` capabilities stamp failing the final verify step — patched in `jang_config.json`); see [jangq-ai/jangq issue](https://github.com/jangq-ai/jangq/issues) for details.

## Intended use & disclaimer

Research and personal use. This model has had its safety alignment (refusal behavior) substantially reduced and will produce content the original refuses. Outputs are untrusted — verify before relying on them. The **LFM Open License v1.0** (see `LICENSE`) travels with these weights and still applies, including its commercial conditions.

## Credit

- [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) — parent model
- [OS-Software](https://huggingface.co/OS-Software) — heretic source checkpoint
- [p-e-w/heretic](https://github.com/p-e-w/heretic) — abliteration method
- [jangq-ai/jangq](https://github.com/jangq-ai/jangq) — JANG quantization format & tools
