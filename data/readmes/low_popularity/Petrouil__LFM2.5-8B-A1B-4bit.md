---
library_name: transformers
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
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
pipeline_tag: text-generation
tags:
  - liquid
  - lfm2.5
  - edge
  - conversational
  - moe
  - bitsandbytes
  - 4bit
  - nf4
base_model: LiquidAI/LFM2.5-8B-A1B
arxiv: 2511.23404
model-index:
  - name: LFM2.5-8B-A1B (4-bit NF4)
    results:
      - task:
          type: instruction-following
        dataset:
          type: IFEval
          name: IFEval
        metrics:
          - type: accuracy
            value: 91.84
      - task:
          type: instruction-following
        dataset:
          type: IFBench
          name: IFBench
        metrics:
          - type: accuracy
            value: 56.47
      - task:
          type: instruction-following
        dataset:
          type: Multi-IF
          name: Multi-IF
        metrics:
          - type: accuracy
            value: 79.93
      - task:
          type: math
        dataset:
          type: MATH-500
          name: MATH-500
        metrics:
          - type: accuracy
            value: 88.76
      - task:
          type: math
        dataset:
          type: AIME-2025
          name: AIME 2025
        metrics:
          - type: accuracy
            value: 42.53
      - task:
          type: tool-calling
        dataset:
          type: BFCL-v3
          name: BFCL v3
        metrics:
          - type: accuracy
            value: 64.36
      - task:
          type: tool-calling
        dataset:
          type: BFCL-v4
          name: BFCL v4
        metrics:
          - type: accuracy
            value: 48.50
widget:
  - text: "Hi, what can you help me with?"
  - text: "What is 84 * 3 / 2?"
  - text: "Tell me an interesting fact about the universe!"
  - text: "Explain quantum computing in simple terms."
---

# LFM2.5-8B-A1B (4-bit NF4 Quantized)

This is a **bitsandbytes 4-bit NF4** quantized version of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B), an 8.3B-parameter Mixture-of-Experts model with 1.5B active parameters and a 128K-token context window.

- **Disk size**: 4.4 GB (model) + 125 MB (expert quant state)
- **VRAM at inference**: ~5 GB
- **Compute dtype**: bfloat16

## Architecture

| Property | Value |
|---|---|
| Parameters | 8.3B total / 1.5B active |
| Layers | 24 (alternating conv-L + full attention) |
| Experts | 32, top-4 per token |
| MoE intermediate | 1792 per expert |
| Hidden size | 2048 |
| Attention heads | 32 (8 KV heads) |
| Context length | 128K tokens |
| Position encoding | RoPE (θ = 5,000,000) |
| Vocabulary | 128K tokens |
| Tie embeddings | True |

The model uses a hybrid architecture: 19 conv-L layers (liquid neural network cells with an internal cache of 3) and 5 full-attention layers, arranged in a repeating pattern.

## Quantization

Quantized with **bitsandbytes NF4** using double quantization and bf16 compute dtype:

- **Non-expert weights** (`q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`, `embed_tokens`, `norm`, `router`): loaded natively as `Linear4bit` / `Params4bit` by `from_pretrained`
- **Expert weights** (`experts.gate_up_proj`, `experts.down_proj`): stored as raw uint8 `Parameter` with a companion `expert_quant_state.pt` file containing the per-weight `QuantState` needed for dequantization

The expert weights require explicit `QuantState` restoration after loading. See [Usage](#usage) below.

## Usage

This model requires [Unsloth](https://github.com/unslothai/unsloth) for the MoE inference forward path. The expert 4-bit weights must be patched after `from_pretrained`.

### Installation

```bash
pip install unsloth bitsandbytes transformers safetensors
```

### Load

```python
from unsloth import FastLanguageModel
from bitsandbytes.nn import Params4bit as BnbParams4bit
from safetensors import safe_open
from pathlib import Path
import torch

cache_path = "models/lfm2.5-8b-4bit-hf"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=cache_path,
    max_seq_length=2048,
    load_in_4bit=True,
    device_map=0,
)

# Restore expert quant states
qs_path = Path(cache_path) / "expert_quant_state.pt"
st_path = Path(cache_path) / "model.safetensors"
quant_states = torch.load(str(qs_path), weights_only=False)
device = next(model.parameters()).device

# Move quant state tensors to GPU once
for name, qs in quant_states.items():
    qs.absmax = qs.absmax.to(device, non_blocking=True)
    qs.code = qs.code.to(device, non_blocking=True)
    if qs.nested:
        if qs.offset is not None:
            qs.offset = qs.offset.to(device, non_blocking=True)
        if hasattr(qs.state2, "absmax") and qs.state2.absmax is not None:
            qs.state2.absmax = qs.state2.absmax.to(device, non_blocking=True)
        if hasattr(qs.state2, "code") and qs.state2.code is not None:
            qs.state2.code = qs.state2.code.to(device, non_blocking=True)

with safe_open(str(st_path), framework="pt", device="cpu") as f:
    for name, param in model.named_parameters():
        if name not in quant_states or "experts" not in name:
            continue
        original_data = f.get_tensor(name)
        new_param = BnbParams4bit(
            data=param.data,
            requires_grad=False,
            quant_state=quant_states[name],
            blocksize=64,
            compress_statistics=True,
            quant_type="nf4",
            bnb_quantized=True,
        )
        new_param.data.copy_(original_data.to(new_param.device))
        parts = name.split(".")
        parent = model
        for p in parts[:-1]:
            parent = getattr(parent, p)
        setattr(parent, parts[-1], new_param)

model.config.use_cache = True
model.eval()
torch.cuda.empty_cache()
```

### Generate

```python
@torch.inference_mode()
def generate(prompt: str, max_new_tokens: int = 128, temperature: float = 0.7):
    messages = [{"role": "user", "content": prompt}]
    inputs = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
    ).to(model.device)
    attention_mask = torch.ones_like(inputs)
    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,
        max_new_tokens=max_new_tokens,
        max_length=inputs.shape[1] + max_new_tokens,
        temperature=temperature,
        do_sample=temperature > 0,
        pad_token_id=tokenizer.eos_token_id,
    )
    return tokenizer.decode(outputs[0][inputs.shape[1]:], skip_special_tokens=True).strip()

print(generate("What is 2+2?"))
```

## Benchmarks

Benchmark scores from the original [LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) model card. Quantization to 4-bit NF4 should preserve these scores near-identically.

| Benchmark | Score |
|---|---|
| IFEval | 91.84 |
| IFBench | 56.47 |
| Multi-IF | 79.93 |
| MATH-500 | 88.76 |
| AIME 2025 | 42.53 |
| BFCL v3 | 64.36 |
| BFCL v4 | 48.50 |
| Tau² Telecom | 88.07 |
| Tau² Retail | 39.82 |
| AA-Omniscience Index | -24.70 |
| AA-Omniscience Accuracy | 8.67 |
| AA-Omniscience Non-Hallucination | 63.47 |

## Caveats

- **Unsloth required**: the MoE forward pass uses `unsloth_zoo`'s MoE utilities. Loading without Unsloth will produce incorrect outputs for MoE layers.
- **Two-step load**: expert weights need explicit `QuantState` restoration (see above). A future `bitsandbytes` release with native `Experts4bit` support will eliminate this step.
- **Expert quant state**: the `expert_quant_state.pt` file (125 MB) is required. Without it, expert weights are un-dequantizable raw uint8 tensors.

## Citation

```bibtex
@article{liquidAI20268BA1B,
  author  = {Liquid AI},
  title   = {LFM2.5-8B-A1B: Personal Assistant On Your Laptop},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-8b-a1b},
}
```

```bibtex
@misc{liquidAI2025LFM2,
  title  = {LFM2 Technical Report},
  author = {Liquid AI},
  year   = {2025},
  eprint = {2511.23404},
  archivePrefix = {arXiv},
}
```

## License

This quantized distribution inherits the [LFM 1.0 License](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE) from the original model.
