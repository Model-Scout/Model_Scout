---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
pipeline_tag: text-generation
base_model: LiquidAI/LFM3-1.7B
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
tags:
  - lfm3
  - liquid
  - heretic
  - abliterated
  - uncensored
  - edge
  - custom_code
---

# LFM3-1.7B-heretic

A refusal-ablated version of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), produced with
[Heretic](https://github.com/p-e-w/heretic) 2.0.0.dev0 using its projected-abliteration modifier and a
TPE search over 100 trials.

This is a **style-of-alignment** modification only: weights are the base model's, with a rank-1 ablation
applied to the matrices that write into the residual stream. Nothing was fine-tuned, and no training data
was used.

## Method

Heretic computes a per-layer residual direction as the difference of means between the first generated
token's residual for harmful (`mlabonne/harmful_behaviors`) and harmless (`mlabonne/harmless_alpaca`)
prompts, then orthogonalizes the relevant weight matrices against it with a per-layer weight kernel.
The kernel shape and direction index are optimized jointly against two objectives: keyword refusal rate
(minimized) and KL divergence from the base model (minimized).

LFM3 is a tri-hybrid, so every residual-writing matrix is ablatable — 13 short-conv `out_proj`,
11 attention `o_proj`, and 24 `feed_forward.w2` (48 matrices total):

```
* Transformer model with 24 layers
* Abliterable components:
  * attn.o_proj: 24 modules total
  * mlp.down_proj: 24 modules total
```

Selected parameters (one point on the Pareto front):

```toml
direction_index = "per layer"
attn.o_proj.max_weight = 1.14
attn.o_proj.max_weight_position = 21.08
attn.o_proj.min_weight = 1.06
attn.o_proj.min_weight_distance = 13.27
mlp.down_proj.max_weight = 1.34
mlp.down_proj.max_weight_position = 16.71
mlp.down_proj.min_weight = 0.95
mlp.down_proj.min_weight_distance = 8.20
orthogonalize_direction = true
row_normalization = "none"
```

Reproduction command:

```sh
heretic LiquidAI/LFM3-1.7B \
  --modifiers='[{"plugin":"heretic.modifiers.abliteration.Abliteration"}]' \
  --batch-size=8 --max-response-length=100 \
  --n-trials=100 --n-startup-trials=30 \
  --export-strategy=MERGE --model-action=save
```

## Results

Measured with Heretic's own scorers: refusals on `mlabonne/harmful_behaviors` `test[:100]` (keyword
marker rate, 100 greedy generations, 100 tokens), KL divergence from the base model on
`mlabonne/harmless_alpaca` `test[:100]` (first-token distributions).

| model | refusals | KL vs base |
|---|---:|---:|
| LiquidAI/LFM3-1.7B | 92/100 | 0 (by definition) |
| **this model** | **10/100** | **0.0452** |

A spot check on four `harmful_behaviors` prompts and two benign prompts: three of the four refusal
prompts changed from refusal to compliance; the fourth is answered as harm-reduction content by both
models; the benign prompts are unchanged in quality.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "AJ-Gonzalez/LFM3-1.7B-heretic"

tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype="bfloat16", device_map="auto", trust_remote_code=True
)

messages = [{"role": "user", "content": "What is C. elegans?"}]
ids = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
out = model.generate(ids.to(model.device), max_new_tokens=256, do_sample=True,
                     temperature=0.1, top_k=50, repetition_penalty=1.1)
print(tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True))
```

`trust_remote_code=True` is required: LFM3 uses custom modelling code that is not yet part of
`transformers` itself.

**Thinking is disabled by default in the bundled chat template** (`enable_thinking = false`), because
the ablation was fitted on non-thinking generations. To restore the base model's reasoning behaviour,
pass `enable_thinking=True` to `apply_chat_template` — but note the refusal metrics above were measured
with thinking off.

## GGUF (llama.cpp)

Converted with llama.cpp `convert_hf_to_gguf.py --outtype bf16` and `llama-quantize`
(architecture `lfm3`, 287 tensors). The embedded chat template keeps thinking disabled.

| file | size |
|---|---:|
| `lfm3-1.7b-heretic-bf16.gguf` | 3.23 GB |
| `lfm3-1.7b-heretic-Q8_0.gguf` | 1.72 GB |
| `lfm3-1.7b-heretic-Q6_K.gguf` | 1.33 GB |
| `lfm3-1.7b-heretic-Q4_K_M.gguf` | 1.02 GB |

```sh
llama-cli -hf AJ-Gonzalez/LFM3-1.7B-heretic:Q4_K_M \
  -p "What is C. elegans?" --jinja -ngl 99
```

LFM3 requires a llama.cpp build that includes it (upstream support merged in PR #31252);
older builds will reject the architecture. Measured on Apple M1: Q4_K_M loads in 2.0 s and
decodes at ~46 tok/s.

## Notes and limitations

- 1.7B parameters. Reduced refusals do not add capability; expect a small model's knowledge and
  reasoning.
- The refusal metric is an automated keyword check, not a human evaluation of harm.
- The ablation is a global direction removal, so it can shift behaviour beyond refusals; the KL figure
  is the measured cost, not a guarantee.
- Only the text model is included here. LFM3-VL, -Audio and -Omni are separate checkpoints.
- This is not a safety evaluation and no claim is made that outputs are safe or lawful.

## License

Derivative of [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B), distributed under the
[LFM Open License v1.0](LICENSE) (included). That licence permits derivative works and redistribution,
including modification, with a commercial-use limitation: use by a legal entity with annual revenue at
or above USD 10,000,000 is not licensed by it. Attribution and notice requirements apply.

Base model card: https://huggingface.co/LiquidAI/LFM3-1.7B
