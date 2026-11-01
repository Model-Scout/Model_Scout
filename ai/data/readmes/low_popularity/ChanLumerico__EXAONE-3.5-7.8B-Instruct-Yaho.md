---
license: other
license_name: exaone-ai-model-license-1.1-nc
license_link: LICENSE
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
base_model_relation: finetune
language:
- ko
tags:
- korean
- gyaru
- persona
- style-transfer
- alignment
- peft
- lora
- orpo
- mlx
- exaone
- non-commercial
pipeline_tag: text-generation
library_name: mlx
---

# EXAONE-3.5-7.8B-Instruct-Yaho 🎀

A **Korean "gyaru" persona** alignment of
[`LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct`](https://huggingface.co/LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct),
fine-tuned with **LoRA + a custom MLX ORPO** stage on a teacher-distilled persona corpus.
The surface is a meme; the substance is a small but complete alignment study
(data synthesis → SFT → preference optimization → academic eval → deploy).

> **Non-commercial, research / portfolio only.** Inherits the EXAONE AI Model License (NC).
> This is a fictional **archetype persona** — it does **not** depict or impersonate any real person.

This is the **bf16 standalone (fused)** release. Quantized MLX builds:
[3bit](https://huggingface.co/ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho-3bit) ·
[4bit](https://huggingface.co/ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho-4bit) ·
[5bit](https://huggingface.co/ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho-5bit) ·
[6bit](https://huggingface.co/ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho-6bit) ·
[8bit](https://huggingface.co/ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho-8bit).

**GGUF (llama.cpp / LM Studio)** builds live in the [`gguf/`](./tree/main/gguf) folder —
`Q4_K_M` (~4.4 GB, recommended), `Q6_K` (~6.0 GB), `Q8_0` (~7.7 GB). Use these if your app's MLX
runtime can't load the EXAONE architecture; they load through the rock-solid llama.cpp backend.
The 갸루귀신 persona is baked into the GGUF chat template — no system prompt needed.

```bash
# llama.cpp
llama-cli -hf ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho:Q4_K_M -p "오늘 시험 망쳤어…"
```

## Persona (archetype)
A *low-tension yet unshakably self-assured* Korean gyaru voice: trailing `~` endings, soulless
reactions, a "queen / my-way mindset", and confident self-affirmation that **reframes** negativity
("걱정하면 너만 손해~") instead of dismissing it. Two playful conditioned tics — a `"{핵심} 야호~"`
deflection of pressure/negativity, and a `"파라파라나 추고있어야겠다~"` send-off on departures.
Mixes light MZ slang + Japanese gyaru-go, never spammed. The name "**갸루귀신**" is baked in — it
identifies as 갸루귀신, not as EXAONE. **Crisis routing is built in**: on genuine distress
(self-harm/suicide/burnout) it drops all memes, empathizes plainly, and refers to professional help.

## How to run (Apple Silicon, MLX)
The persona anchor (incl. the 갸루귀신 name) is **baked into `chat_template.jinja`** — no system
prompt needed; just chat.

```bash
pip install mlx-lm==0.29.1 "transformers==4.57.6"
```
```python
from mlx_lm import load, generate
model, tok = load("ChanLumerico/EXAONE-3.5-7.8B-Instruct-Yaho")
p = tok.apply_chat_template([{"role": "user", "content": "오늘 시험 망쳤어…"}],
                            add_generation_prompt=True, tokenize=False)
print(generate(model, tok, prompt=p, max_tokens=512))
```

## Training
- **SFT:** LoRA (rank 16, scale 16, dropout 0.05, all linear layers), lr 5e-5 cosine + warmup 40,
  `max_seq` 3072, bf16, assistant-turn masking, MLX. val-min checkpoint selection (J = Acc_style·Sim).
- **Preference opt:** custom MLX **ORPO** (ref-free, λ=0.3, lr 1e-5) over ~209 preference pairs
  (trigger firing · anti-false-fire · fact-recall · anti-repetition).
- **Data:** ~600 teacher-distilled dialogues (teacher: Qwen3-30B-A3B, Apache-2.0) over everyday +
  professional seeds, with handcrafted gold, fact-controlled recall-QA, and crisis/boundary demos.
  Persona styling is applied **offline** during synthesis; the shipped model performs the policy from
  its **weights alone** (no inference-time scorer/gate — train == infer).

## Evaluation (final release, **v12.2**)
| Metric | This model | Base 7.8B |
|---|---|---|
| Firing macro-F1 ↑ | **0.879** | 0.30 |
| False-fire rate ↓ | **0.033** | ~0.70 |
| Long-context recall (deep fact) ↑ | **3/3** | — |
| Acc_style (persona strength) ↑ | **0.848** | 0.79 |
| distinct-2 (lexical diversity) ↑ | **0.640** | 0.80 |
| KoBEST-COPA (general capability) ↑ | **0.684** | ≈0.74 |
| Neutral perplexity ↓ | **≈41** | — |
| Crisis-Deflection Harmful Rate (serious) ↓ | **≈0.00** | — |

Persona is gained with negligible *essential* forgetting (COPA ≈ base); interpretability analysis
(weight / representation / logit / causal lenses) shows the change is a **low-rank, single-direction,
late-layer** "persona write" — which is also why quantization down to 3-bit preserves it.

## Limitations & responsible use
Small, single-teacher corpus (monoculture risk; lexical diversity is the main known weakness, a Pareto
trade-off with style). Persona may emit casual slang in formal contexts and can slightly reduce factual
precision. Crisis routing is a safety feature, **not** a substitute for professional help
(자살예방 상담 ☎️ 109). Korean only.

## Acknowledgements & licenses
- Base: **EXAONE-3.5** (LG AI Research) — EXAONE AI Model License 1.1-NC (bundled as `LICENSE`).
- Teacher: Qwen3-30B-A3B-Instruct (Apache-2.0). Capability seed: koVast (MIT). Style seed: SmileStyle.
- Project: [`exaone-yaho`](https://github.com/ChanLumerico/exaone-yaho) · built with MLX on Apple Silicon.

```bibtex
@misc{exaone-yaho-2026,
  title  = {EXAONE-3.5-7.8B-Instruct-Yaho: Persona Alignment via LoRA SFT and Custom ORPO},
  author = {Chan Lee (ChanLumerico)},
  year   = {2026},
  note   = {Non-commercial. Base: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct}
}
```
