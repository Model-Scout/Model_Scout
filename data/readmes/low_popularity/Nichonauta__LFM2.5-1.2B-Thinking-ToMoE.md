---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking/blob/main/LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
base_model: LiquidAI/LFM2.5-1.2B-Thinking
tags:
- lfm2
- mixture-of-experts
- tomoe
- pruning
- reasoning
pipeline_tag: text-generation
library_name: transformers
---

# LFM2.5-1.2B-Thinking-ToMoE

A **Mixture-of-Experts (MoE)** conversion of [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking), obtained with the **ToMoE** method (Dynamic Structural Pruning + Hypernetwork).

The dense 1.17B reasoning model is converted into a channel-MoE where:
- **feed_forward / MLP** (16 layers): per-token expert routing over 8 channel-experts (top-1 via Gumbel-softmax), the FFN is cut to the union of the expert channel masks.
- **Full attention** (6 layers): Q/K kept at full width; the V channels are dynamically masked per token (deterministic masks).
- **ShortConv** (10 layers): statically pruned (a single channel index shared by the B/C/x projections, the conv and the output projection).

## Metrics

| Metric | Dense base | ToMoE MoE |
|---|---|---|
| Total params | 1170.3M | 1031.9M stored |
| Active params per token | 1170.3M | **~700M** (est.) |
| PPL wikitext-2 (raw, 1810 tok) | 16.9 | 504.3 |
| PPL chat-formatted (prompt + answer) | 71.1 | 711.7 |
| Embeddings (always active) | 134.2M | 134.2M |

The pruned budget is `p = 0.05` with the ToMoE regularization (`lam` 64→128, Gumbel base annealed 1.0→−0.25, 8 experts), trained 2,400 steps at seq 2048 with online KD against the dense teacher on wikitext-103 (4M tokens, raw text). The attention QK is excluded from the budget (kept full) because the small head-dim (64) collapses under aggressive QK pruning.

> Notes:
> - LFM2.5-1.2B-Thinking is a **reasoning (RL) model**: its native output format includes a `<think>` block before the answer. Unlike the 350M instruct model, its raw-text distribution is NOT degenerate (raw PPL 16.9 — the RL training preserved base-LM quality), so raw-text KD works well for this conversion.
> - The MoE keeps the whole base distribution (it can still emit `<think>` blocks) but is strongly degraded: raw PPL ~30x and chat PPL ~10x worse than the dense base. Generation repeats — this is the known structural limit of the ToMoE conversion on LFM2.

## Usage (transformers, trust_remote_code)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Nichonauta/LFM2.5-1.2B-Thinking-ToMoE",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
    attn_implementation="eager",
)
tokenizer = AutoTokenizer.from_pretrained("Nichonauta/LFM2.5-1.2B-Thinking-ToMoE")

messages = [{"role": "user", "content": "What is the capital of France?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_tensors="pt")
out = model.generate(**prompt, max_new_tokens=64)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

> Note: this model requires `trust_remote_code=True` — the custom `modeling_lfm2_moe_final.py` defines the `Lfm2MoEForCausalLM` class.

## Conversion details

- **Base**: [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) (LFM Open License v1.0, `lfm1.0`)
- **Method**: ToMoE — a bidirectional-GRU hypernetwork generates differentiable channel masks per sublayer; the model weights are frozen and only the hypernetwork is trained (online KD against the dense teacher). The final pruned weights are extracted from the trained masks.
- **Training**: 2,400 steps, seq 2048, online knowledge distillation (2× forward KL), gradient checkpointing, wikitext-103 (4M tokens).
- **Architecture deltas**: 16 layers (10 ShortConv + 6 full attention), FFN 8192-wide per layer (auto-adjusted from 12288), hidden 2048, head_dim 64, tied embeddings.

## Limitations

- The model is significantly degraded versus the dense base (chat PPL ~712 vs ~71; raw ~504 vs ~17) and generation tends to repeat — the conv layers are cut to ~5–40% width and each token activates ~50–70% of the MLP channels through a single expert.
- This is a research artifact demonstrating the ToMoE pipeline on a mid-size LFM2 architecture; it is NOT a usable chat assistant.

## License

This model is a derivative of LiquidAI/LFM2.5-1.2B-Thinking and is released under the **LFM Open License v1.0** (see `LICENSE`).

## Files

- `model.safetensors` — the pruned MoE weights (fp32)
- `modeling_lfm2_moe_final.py` — the custom model definition (trust_remote_code)
- `config.json` — model configuration (with `auto_map`)
- `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`, `generation_config.json`

## Related repositories

- **GGUF (dense-equivalent)**: [Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-GGUF](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-GGUF)
- **Weight-only quantizations of the real MoE**: [Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT8](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT8) and [Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT4](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT4)
