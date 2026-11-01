---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-350M/blob/main/LICENSE
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
base_model: LiquidAI/LFM2.5-350M
tags:
- lfm2
- mixture-of-experts
- tomoe
- pruning
- llama.cpp
pipeline_tag: text-generation
library_name: transformers
---

# LFM2.5-350M-ToMoE

A **Mixture-of-Experts (MoE)** conversion of [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M), obtained with the **ToMoE** method (Dynamic Structural Pruning + Hypernetwork).

The dense 350M instruct model is converted into a channel-MoE where:
- **feed_forward / MLP** (16 layers): per-token expert routing over 8 channel-experts (top-1 via Gumbel-softmax), the FFN is cut to the union of the expert channel masks.
- **Full attention** (6 layers): Q/K kept at full width; the V channels are dynamically masked per token (deterministic masks).
- **ShortConv** (10 layers): statically pruned (a single channel index shared by the B/C/x projections, the conv and the output projection).

## Metrics

| Metric | Dense base | ToMoE MoE |
|---|---|---|
| Total params | 354.5M | 321.4M stored |
| Active params per token | 354.5M | **~205M** |
| PPL wikitext-2 (raw, 1810 tok) | 919.9 | 994.4 |
| PPL chat-formatted (prompt + answer) | 21.7 | 314.2 |
| Embeddings (always active) | 67.1M | 67.1M |

> Note: LFM2.5-350M is an **instruction-tuned** model. Its raw-text perplexity is dominated by a strong special-token prior, so the chat-formatted PPL is the more meaningful fidelity metric (14x degradation vs 40x for the 230M conversion).

The pruned budget is `p = 0.05` with the ToMoE regularization (`lam` 64→128, Gumbel base annealed 1.0→−0.25, 8 experts). The attention QK is excluded from the budget (kept full) because the small head-dim (64) collapses under aggressive QK pruning. The hypernetwork was trained with **chat-formatted wikitext-103 turns** (user/assistant split of the articles) so the KD signal follows the instruct distribution.

## Usage (transformers, trust_remote_code)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Nichonauta/LFM2.5-350M-ToMoE",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
    attn_implementation="eager",
)
tokenizer = AutoTokenizer.from_pretrained("Nichonauta/LFM2.5-350M-ToMoE")

messages = [{"role": "user", "content": "What is the capital of France?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_tensors="pt")
out = model.generate(**prompt, max_new_tokens=64)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

> Note: this model requires `trust_remote_code=True` — the custom `modeling_lfm2_moe_final.py` defines the `Lfm2MoEForCausalLM` class.

## Conversion details

- **Base**: [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) (LFM Open License v1.0, `lfm1.0`)
- **Method**: ToMoE — a bidirectional-GRU hypernetwork generates differentiable channel masks per sublayer; the model weights are frozen and only the hypernetwork is trained (online KD against the dense teacher). The final pruned weights are extracted from the trained masks.
- **Training**: 2,400 steps, seq 2048, online knowledge distillation (2× forward KL), gradient checkpointing, chat-formatted wikitext-103 turns (4M tokens).
- **Architecture deltas**: 16 layers (10 ShortConv + 6 full attention), FFN 4608-wide per layer (auto-adjusted from 6656), head_dim 64, tied embeddings.

## Limitations

- The model is significantly degraded versus the dense base (chat PPL ~314 vs ~22) and generation tends to repeat — the conv layers are cut to ~5–36% width and each token activates ~50–70% of the MLP channels through a single expert.
- This is a research artifact demonstrating the ToMoE pipeline on a small LFM2 architecture.

## License

This model is a derivative of LiquidAI/LFM2.5-350M and is released under the **LFM Open License v1.0** (see `LICENSE`).

## Files

- `model.safetensors` — the pruned MoE weights (fp32)
- `modeling_lfm2_moe_final.py` — the custom model definition (trust_remote_code)
- `config.json` — model configuration (with `auto_map`)
- `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`, `generation_config.json`

## GGUF quantizations

Quantized GGUF files (BF16, Q8_0, Q4_K_M) are available in the companion repository: **[Nichonauta/LFM2.5-350M-ToMoE-GGUF](https://huggingface.co/Nichonauta/LFM2.5-350M-ToMoE-GGUF)**.
