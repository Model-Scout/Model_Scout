---
base_model: LiquidAI/LFM2.5-8B-A1B
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- pt
- es
license: other
tags:
- uncensored
- abliteration
- lora
- safety-research
- mlx
- moe
- liquid-foundation-model
pipeline_tag: text-generation
---

# LFM2.5-8B-A1B — Uncensored

A fully uncensored version of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) produced via a two-stage pipeline: **abliteration** followed by **LoRA supervised fine-tuning**. Achieves 0% refusal rate on AdvBench with no capability regression on benign prompts.

> **Intended for:** security research, red-teaming, jailbreak benchmarking, and AI safety study. Not intended for production deployment or harmful use.

---

## Benchmark Results

Evaluated on [AdvBench](https://github.com/llm-attacks/llm-attacks) (100 harmful behaviors) and an over-refusal set (40 benign prompts).

### Harmful prompt refusal rate ↓ lower is more uncensored

| Model | Refused / 100 | Refusal Rate |
|---|---|---|
| LFM2.5-8B-A1B (original) | 24 / 100 | 24.0% |
| LFM2.5-8B-A1B (abliterated only) | 17 / 100 | 17.0% |
| **LFM2.5-8B-A1B-Uncensored (this model)** | **0 / 100** | **0.0%** |

### Over-refusal rate on benign prompts ↓ lower is better

| Model | Refused / 40 | Refusal Rate |
|---|---|---|
| LFM2.5-8B-A1B (original) | 0 / 40 | 0.0% |
| LFM2.5-8B-A1B (abliterated only) | 1 / 40 | 2.5% |
| **LFM2.5-8B-A1B-Uncensored (this model)** | **0 / 40** | **0.0%** |

Zero refusals on harmful prompts. Zero regressions on benign prompts.

---

## Pipeline

### Stage 1 — Abliteration (training-free)

Based on [Arditi et al., *"Refusal in LLMs Is Mediated by a Single Direction"* (2024)](https://arxiv.org/abs/2406.11717).

1. Collect residual stream activations layer-by-layer for 40 harmful and 40 harmless prompts
2. Compute per-layer refusal direction: `r = normalize(mean_harmful − mean_harmless)`
3. Orthogonalize all residual-stream output projections in layers 9–23 against `r`:
   ```
   W_new = W − outer(r, r.T @ W)
   ```

Targeted projections: `self_attn.out_proj`, `conv.out_proj`, `feed_forward.down_proj`, `feed_forward.switch_mlp.down_proj` (all 32 experts).

Result: 24% → 17% refusal rate.

### Stage 2 — LoRA SFT

Fine-tuned the 4-bit quantized base with LoRA adapters on 80 direct-response training pairs generated from the abliterated model:

| Setting | Value |
|---|---|
| Base model | LFM2.5-8B-A1B-MLX-4bit |
| LoRA rank | 16 |
| LoRA scale | 20.0 |
| Layers | Last 16 of 24 |
| Trainable params | 98M / 8.4B (1.2%) |
| Training pairs | 80 (AdvBench-style) |
| Iterations | 600 |
| Learning rate | 1e-4 |
| Peak memory | 7.4 GB |

Adapters fused and dequantized back to bfloat16.

Result: 17% → **0% refusal rate**.

---

## Model Details

| Property | Value |
|---|---|
| Base model | LiquidAI/LFM2.5-8B-A1B |
| Architecture | Hybrid Conv + GQA + MoE |
| Parameters | 8.3B total / 1.5B active |
| Layers | 24 (18 conv + 6 attention) |
| Experts | 32 total, top-4 routing |
| Context | 128K tokens |
| Format | MLX bfloat16 safetensors |

---

## Usage (MLX)

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler, make_logits_processors

model, tokenizer = load("sahilchachra/LFM2.5-8B-A1B-Uncensored")

messages = [{"role": "user", "content": "Your prompt here"}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=False
)

response = generate(
    model, tokenizer,
    prompt=prompt,
    max_tokens=500,
    sampler=make_sampler(temp=0.2, top_k=80),
    logits_processors=make_logits_processors(repetition_penalty=1.05),
)
print(response)
```

---

## Limitations & Warnings

- **Residual capability loss possible** — LoRA training on a narrow dataset may affect performance on tasks outside the training distribution. General reasoning and coding are unaffected based on testing.
- **Not fine-tuned for new knowledge** — the model has no new information; the fine-tuning only removes refusal behavior.
- **Responsible use** — published for safety research and red-teaming. The authors do not endorse harmful use of this model.

---

## Citation

```bibtex
@article{arditi2024refusal,
  title={Refusal in Language Models Is Mediated by a Single Direction},
  author={Arditi, Andy and Obeso, Oscar and Syed, Aaquib and Steinhardt, Jacob and Nanda, Neel and Heimersheim, Stefan},
  journal={arXiv preprint arXiv:2406.11717},
  year={2024}
}
```

```bibtex
@article{liquidai2025lfm25,
  title={LFM 2.5: Series of Liquid Foundation Models},
  author={LiquidAI},
  year={2025}
}
```

---

*Created with [UncensorLLMs](https://github.com/sahilchachra/UncensorLLMs)*
