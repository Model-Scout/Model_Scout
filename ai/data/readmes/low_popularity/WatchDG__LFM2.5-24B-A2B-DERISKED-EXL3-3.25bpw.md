---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16
pipeline_tag: text-generation
library_name: transformers
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
tags:
  - exl3
  - lfm2.5
  - lfm2
  - moe
  - quantized
  - 3.25bpw
  - blackfrost
---

# LFM2.5-24B-A2B-DERISKED-EXL3-3.25bpw

**EXL3-quantized derivative of [`Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16`](https://huggingface.co/Blackfrost-AI/LFM2.5-24B-A2B-DERISKED-BF16) at a 3.25 bpw budget.**

This is a third-party quantization of a third-party derivative. It is not endorsed by, or affiliated with, Liquid AI or Blackfrost-AI. The upstream model card remains the authoritative description of the model's intended behavior, capabilities and limitations — read it before deploying.

---

## At a glance

| Property | Value |
|---|---|
| Format | EXL3 (trellis, `mul1` codebook) |
| Target bitrate | **3.25 bpw** (final bitrate excluding head: 3.25) |
| Quantizer | exllamav3 **1.6.2** |
| Source precision | BF16 |
| On-disk size | **9.73 GiB** (2 safetensors shards) |
| Architecture | `Lfm2MoeForCausalLM` (`lfm2_moe`) |
| Layers | 40 (30 convolution + 10 grouped-query attention) |
| Experts per MoE block | 64, 4 routed per token |
| Hidden size / vocab | 2048 / 128000 |
| Native context | 131072 tokens |
| Tokenizer / template | inherited unchanged from the source checkpoint |

At ~9.73 GiB the weights fit a single 24 GB card with room for a full 128k context cache.

---

## Requirements

- **exllamav3 1.6.2 or newer** for inference. The extension is architecture- and version-sensitive; the weights carry `"version": "1.6.2"` in `quantization_config.json`.
- **GPU with ≥ 16 GB** for the full 131072-token context. Measured: 16.05 GiB total on an RTX 4090 (24 GB) with `cache_size: 131072` and Q8 KV cache.

Because only 10 of the 40 layers keep a KV cache (the other 30 are convolutional), a 128k context at Q8 costs about 1.3 GB rather than the ~17 GB a 40-layer attention model would need.

---

## Usage

### exllamav3

```python
from exllamav3 import Cache, CacheLayer_fp16, Config, Generator, Model, Tokenizer
import torch

path = "LFM2.5-24B-A2B-DERISKED-EXL3-3.25bpw"

config = Config.from_directory(path)
model = Model.from_config(config)

cache = Cache(model, max_num_tokens=131072, layer_type=CacheLayer_fp16,
              max_batch_size=1, recurrent_dtype=torch.half)

model.load(device="cuda:0")

tokenizer = Tokenizer.from_config(config)
gen = Generator(model, cache, tokenizer)

print(gen.generate("What is the capital of France? Answer in one word.",
                   max_new_tokens=400))
```

> The `Cache` must be constructed **before** `model.load()` — `load()` is what allocates its tensors. `Model.from_config()` is required; the bare `Model(config)` constructor does not build the module list.

### tabbyAPI

```yaml
model:
  model_dir: <container-dir>
  model_name: LFM2.5-24B-A2B-DERISKED-EXL3-3.25bpw
  cache_size: 131072
  cache_mode: Q8
  max_seq_len: 131072
```

`model_dir` is a **container** that tabbyAPI joins with `model_name`; if the checkpoint sits directly in `model_dir`, set `model_name: .` (pathlib folds it away).

---

## Files

| File | Purpose |
|---|---|
| `model-00001-of-00002.safetensors` | quantized weights (7.996 GiB) |
| `model-00002-of-00002.safetensors` | quantized weights (1.708 GiB) |
| `model.safetensors.index.json` | tensor → shard map |
| `quantization_config.json` | per-tensor EXL3 layout, bitrates, shapes |
| `config.json`, `generation_config.json` | model configuration |
| `tokenizer.json`, `tokenizer_config.json` | tokenizer |
| `chat_template.jinja` | chat template |
| `SHA256SUMS` | digests for all files above |
| `RELEASE_PROVENANCE.json` | quantization lineage |
| `LICENSE` | LFM Open License v1.0 |

Verify with:

```bash
sha256sum -c SHA256SUMS
```

---

## License

The parent model is distributed under the **LFM Open License v1.0**; see [`LICENSE`](LICENSE). That license includes commercial-use conditions, including thresholds at which separate permission may be required from Liquid AI.

**Quantization does not replace or relax the upstream license terms.** Users remain bound by the LFM Open License v1.0 and must review it against their intended use before deploying. No warranty is provided.