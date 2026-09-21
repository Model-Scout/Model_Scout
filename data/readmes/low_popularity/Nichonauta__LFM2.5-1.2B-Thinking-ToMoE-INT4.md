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
base_model: Nichonauta/LFM2.5-1.2B-Thinking-ToMoE
tags:
- lfm2
- mixture-of-experts
- tomoe
- quantization
pipeline_tag: text-generation
library_name: transformers
---

# LFM2.5-1.2B-Thinking-ToMoE-INT4

Weight-only **INT4** quantization of the real ToMoE MoE — **[Nichonauta/LFM2.5-1.2B-Thinking-ToMoE](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE)** (derived from [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking)).

Unlike the GGUF companions (which are **dense-equivalents** because llama.cpp cannot represent the channel-MoE), this repository stores the **actual pruned MoE weights** quantized in safetensors format:

- `LinearINT4` replaces the MLP/attention/conv Linear layers (per-channel symmetric for INT8; per-group of 64 with zero-point for INT4), packed 2-nibbles-per-byte for INT4.
- The **routers, embeddings and norms stay fp32** (tiny and sensitive); weights dequantize lazily in the forward pass.
- Same custom model definition (`modeling_lfm2_moe_final.py`, `trust_remote_code`), plus the `quantization` flag in `config.json`.

## Metrics vs the fp32 MoE

| Metric | fp32 MoE | INT8 | INT4 |
|---|---|---|---|
| PPL wikitext-2 (raw, 1810 tok) | 504 | 504 | 504 |
| PPL chat-formatted (prompt+answer) | 712 | 709 | 723 |
| `model.safetensors` size | 4230 MB | 1015 MB | — |

The 1.2B MoE is robust to weight-only quantization: INT8 and INT4 are within measurement noise of the fp32 MoE (raw PPL identical, chat within ~1.5%).

## Usage (transformers, trust_remote_code)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT4",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
    attn_implementation="eager",
)
tokenizer = AutoTokenizer.from_pretrained("Nichonauta/LFM2.5-1.2B-Thinking-ToMoE-INT4")
```

The `quantization` field in `config.json` makes the custom modeling file build the quantized Linear layers automatically.

## Files

- `model.safetensors` — INT4 weights + fp32 scales/zero-points + fp32 routers/embeddings/buffers
- `modeling_lfm2_moe_final.py` — custom model definition with `LinearINT4` support (trust_remote_code)
- `config.json` — model configuration (`quantization: "int4"`, `auto_map`)
- `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja`, `generation_config.json`, `LICENSE`

## License

Derivative of LiquidAI/LFM2.5-1.2B-Thinking — released under the **LFM Open License v1.0** (see `LICENSE`).
