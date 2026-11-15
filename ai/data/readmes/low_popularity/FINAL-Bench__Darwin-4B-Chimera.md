---
license: gemma
tags:
  - chimera
  - darwin
  - vidraft
  - korean
  - kmmlu
  - reasoning
pipeline_tag: text-generation
language:
  - ko
  - en
library_name: transformers
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-4B-Chimera

**A 4B Korean-reasoning model built with VIDRAFT's Chimera technology.**

Most models get better by getting bigger. This one got better by **combining** — and then refining itself.

---

## Why Chimera matters

Merging models usually means losing something. Average two networks and you get a compromise: each parent's edge is blunted, and the child is worse than both at what each did best. That is why "model merging" has a reputation as a cheap trick.

Chimera is built on the opposite premise.

### 1. The parents survive intact
Chimera fuses components from models of **different families and different strengths** while preserving what each parent knew. Knowledge is carried over, not averaged away. What you merge in is what you keep.

### 2. The result cannot be reduced to any single parent
A Chimera individual is not "model A with a bit of B." It sits at a point in model space that **no parent reaches alone**, and it cannot be recovered from any one of them. That non-reducibility is the entire point — it is what makes a lineage an asset rather than a re-skin.

### 3. No additional pretraining
A new generation is a **fusion plus an evaluation**, not a training run measured in GPU-months. Iteration collapses from months to days — which means the space of viable combinations actually gets explored instead of theorized about.

### 4. It compounds
Chimera individuals become parents. Strengths accumulate across generations: parent → child → grandchild. Capability is **grown**, not purchased.

### 5. It answers the real constraint
Frontier capability is gated by capital: tens of thousands of GPUs, months of training, hundreds of millions of dollars. Chimera attacks that gate directly — **structural evolution instead of brute-force scale**. It is how a small team competes on method rather than on budget.

---

## What that buys you at 4B

This model is a late-generation Chimera individual, refined further by VIDRAFT's own reinforcement fine-tuning pipeline.

**KMMLU · 6 subjects · 240 held-out items · greedy decoding**

| Model | KMMLU | Δ |
|---|---|---|
| Chimera 4B baseline | 42.9% | — |
| **Darwin-4B-Chimera** | **48.3%** | **+5.4pp** |

**+5.4pp on Korean knowledge reasoning with zero parameter growth** — 4.02B before, 4.02B after. The gain came from what the model learned from itself, not from more weights. Same architecture, same size, same inference cost: strictly better.

That matters because 4B is the size that actually ships. It runs on a single consumer GPU, on-premise, inside an air-gapped network — the places where frontier APIs cannot go.

---

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

mid = "FINAL-Bench/Darwin-4B-Chimera"
tok = AutoTokenizer.from_pretrained(mid)
model = AutoModelForCausalLM.from_pretrained(mid, torch_dtype="auto", device_map="auto")

msgs = [{"role": "user", "content": "한국의 삼권분립을 간단히 설명해줘."}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=512, do_sample=False)
print(tok.decode(out[0][ids.shape[-1]:], skip_special_tokens=True))
```

---

## What is open, and what is not

The **weights are open** and the **numbers are stated with the exact evaluation setup**, so anyone can reproduce the result above rather than take our word for it.

The internal design of Chimera fusion and of the refinement pipeline — component selection, data selection criteria, training configuration, routing — is **VIDRAFT proprietary**.

> **Results are open. The recipe is not.**

---

## Links

- **Darwin family** — https://huggingface.co/collections/FINAL-Bench/darwin-family
- **Method paper (evolutionary merging)** — arXiv [2605.14386](https://huggingface.co/papers/2605.14386)
- **VIDRAFT** — https://vidraft.net

## License

`gemma` — the Chimera lineage includes Gemma-derived components, so the Gemma license applies. Review the [Gemma Terms of Use](https://ai.google.dev/gemma/terms) before use.

## Learn more
- How model merging and cross-breeding work: [Can you make an AI model smarter without training?](https://vidraft.net/insights/model-merging-without-training.html)
