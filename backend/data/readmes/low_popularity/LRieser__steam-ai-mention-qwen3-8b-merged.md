---
language:
- en
- zh
- ru
- it
- de
- fr
- pt
- es
- pl
- tr
- ko
- cs
- ja
- nl
- sv
- uk
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-8B
tags:
- steam
- game-reviews
- generative-ai
- ai-disclosure
- multilingual
- qwen3
- json-output
- merged
model-index:
- name: steam-ai-mention-qwen3-8b-merged
  results:
  - task:
      type: text-classification
      name: Generative-AI mention detection in Steam reviews
    dataset:
      name: Steam AI-mention gold labels v1.3, held-out test split
      type: steam-ai-mention-gold-v1-3
    metrics:
    - type: f1
      name: Macro-F1 (keyword-matched stratum, n=720)
      value: 0.953
    - type: precision
      name: Positive-class precision
      value: 0.959
    - type: recall
      name: Positive-class recall
      value: 0.912
---

# Steam AI-mention classifier (Qwen3-8B, merged bf16)

[Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) fine-tuned to
classify Steam game reviews: given the review and its game context, it
answers whether the review discusses generative AI used to produce the
game's content (art, voice, music, writing, code, translation). The answer
is a JSON object. Trained on 19,152 Steam reviews labeled by a large
language model. Multilingual.

These are the full bf16 weights (about 16 GB) with the LoRA adapter from
[LRieser/steam-ai-mention-qwen3-8b-lora](https://huggingface.co/LRieser/steam-ai-mention-qwen3-8b-lora)
merged in. No base model download is needed and the weights load directly
into vLLM.

## Output

```json
{"mentions_genai": true, "confidence": "high", "reasoning": "Calls the portraits 'AI slop'."}
```

| Field | Values |
|---|---|
| `mentions_genai` | `true` if the review discusses generative AI in the game's production, else `false` |
| `confidence` | `"low"`, `"medium"`, `"high"` |
| `reasoning` | one or two sentences quoting the decisive phrase |

`true` covers explicit terms ("AI art", "AI-generated", "AI slop"), tool and
vendor names, their equivalents in other languages, reactions to a
developer's AI disclosure, and speculative claims when the context supports
a genuine suspicion. `false` covers gameplay AI (enemy or NPC behaviour),
procedural generation, the reviewer's own use of AI tools, and rhetorical
comparisons ("an AI could have written this"). The full rubric is the
system prompt in [`prompt_system.md`](prompt_system.md).

## Usage

The model expects the system prompt from `prompt_system.md` and a user
message in the format of [`prompt_user_template.md`](prompt_user_template.md)
(game name, genres, tags, release date, the developer's AI disclosure if
any, review date, language, recommendation, and the review text). Both files
are in this repository.

```python
import json
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "LRieser/steam-ai-mention-qwen3-8b-merged"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype=torch.bfloat16, device_map="auto").eval()

system_prompt = open(hf_hub_download(repo, "prompt_system.md"), encoding="utf-8").read()

user_message = """=== GAME ===
name: Example Quest
genres: RPG, Indie
top_tags: Pixel Graphics, Story Rich, 2D
release_date: 2024-09-12
early_access: False

=== DISCLOSURE ===
  flag: no

=== REVIEW ===
written_on: 2025-03-02
regime: post_mandate_2024  (computed from effective date = max(written, edited))
language: english
voted_up: False
text: |
The portraits are AI slop, every face has that same plastic look."""

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}]
inputs = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, max_new_tokens=128, do_sample=False)
result = json.loads(tok.decode(out[0, inputs.shape[1]:], skip_special_tokens=True))
result["mentions_genai"]  # True
```

For corpus-scale inference serve the weights with vLLM (about 11 reviews per
second on an RTX 4090, against about one per second with plain `generate()`):

```bash
vllm serve LRieser/steam-ai-mention-qwen3-8b-merged --dtype bfloat16
```

## Training

- Base model: `Qwen/Qwen3-8B`.
- Method: QLoRA with DoRA (`use_dora=True`), rank 16, alpha 32, dropout 0,
  on `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`,
  `down_proj`. NF4-quantised base, bf16 compute. The adapter was then merged
  into the bf16 base weights.
- Data: 19,152 Steam reviews, 4,585 positive. Two sampling strata: reviews
  matching a multilingual generative-AI keyword list (14,379) and a uniform
  random sample of reviews (4,773). Labels were produced by DeepSeek V4-Pro
  in thinking mode under the rubric in `prompt_system.md`, after a
  250-review audit that refined the rubric. Twenty languages; the largest
  are English (55%), Simplified Chinese (12%), Russian (10%), Italian (6%),
  and German (4%).
- Optimisation: paged AdamW 8-bit, learning rate 2e-4, cosine schedule,
  warmup ratio 0.05, weight decay 0.01, gradient clipping 1.0, batch size 1
  with gradient accumulation 4, gradient checkpointing, maximum sequence
  length 4096. Loss on the assistant JSON only.
- Schedule: 2 epochs (7,662 steps); the merged checkpoint is the one with
  the lowest validation loss (0.295). Final token accuracy 93.9%.

![train_loss.png](train_loss.png)
![eval_metric.png](eval_metric.png)

## Evaluation

Held-out test split of 960 reviews (seed 42), never used in training, scored
with these weights under vLLM. The keyword-matched stratum (n=720) contains
almost all positives; the random stratum (n=240) checks for false positives
on ordinary reviews.

| Metric | Value |
|---|---|
| Macro-F1, keyword-matched stratum | 0.953 |
| Positive-class precision / recall / F1 | 0.959 / 0.912 / 0.935 |
| Macro-F1, English / non-English | 0.968 / 0.940 |
| False positives, random stratum (n=240) | 0 |
| Throughput (RTX 4090, vLLM bf16) | about 11 reviews/s |

The companion encoder
([LRieser/steam-ai-mention-mmbert-base](https://huggingface.co/LRieser/steam-ai-mention-mmbert-base))
reaches macro-F1 0.925 on the same split at about 430 reviews per second.

## Citation

```bibtex
@misc{rieser2026steamaimentionqwen3merged,
  author    = {Rieser, Lars and Ohlrogge, Fynn and Joshi, Anant and Sethi, Navneet},
  title     = {Steam AI-mention classifier (Qwen3-8B, merged)},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/LRieser/steam-ai-mention-qwen3-8b-merged}
}
```
