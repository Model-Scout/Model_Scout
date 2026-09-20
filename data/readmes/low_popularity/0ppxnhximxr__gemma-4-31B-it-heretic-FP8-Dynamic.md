---
license: apache-2.0
language:
- en
- ko
- multilingual
library_name: transformers
pipeline_tag: image-text-to-text
base_model: coder3101/gemma-4-31B-it-heretic
base_model_relation: quantized
tags:
- gemma4
- gemma
- heretic
- abliterated
- uncensored
- decensored
- ara
- quantized
- fp8
- compressed-tensors
- llm-compressor
- w8a8
---

# gemma-4-31B-it-heretic-FP8-Dynamic

FP8 Dynamic quantized version of [coder3101/gemma-4-31B-it-heretic](https://huggingface.co/coder3101/gemma-4-31B-it-heretic),
which is itself a decensored variant of [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it)
created using [Heretic](https://github.com/p-e-w/heretic) v1.2.0 with the Arbitrary-Rank Ablation (ARA) method.

## Model Overview

- **Base model**: `coder3101/gemma-4-31B-it-heretic`
- **Original foundation**: `google/gemma-4-31B-it` (30.7B dense + 550M vision encoder)
- **Quantization scheme**: FP8_DYNAMIC (weights FP8 E4M3 per-channel, activations dynamic per-token)
- **Format**: `compressed-tensors`
- **Quantization tool**: [llm-compressor](https://github.com/vllm-project/llm-compressor)
- **Size**: ~34 GB (from ~63 GB BF16)

## Quantization Details

The language model Linear layers were quantized to FP8 (E4M3) while preserving
the following components in their original precision:

- `lm_head`
- Vision tower (`vision_tower.*`, `vision_model.*`)
- Multimodal projector (`multi_modal_projector.*`)
- Patch embedding (`patch_embedding.*`, `embed_vision.*`)

This preserves image understanding capabilities while reducing memory footprint
and accelerating language-generation throughput on hardware with FP8 support.

### Quantization Recipe

```python
from llmcompressor.modifiers.quantization import QuantizationModifier

recipe = QuantizationModifier(
    targets="Linear",
    scheme="FP8_DYNAMIC",
    ignore=[
        "lm_head",
        "re:.*vision_tower.*",
        "re:.*vision_model.*",
        "re:.*multi_modal_projector.*",
        "re:.*patch_embedding.*",
        "re:.*embed_vision.*",
    ],
)
```

## Usage with SGLang

Currently the most stable serving path for Gemma 4 is SGLang. vLLM has
known issues with Gemma 4's heterogeneous attention heads as of April 2026.

### Docker (recommended)

```bash
docker run -d --name sglang-gemma4 \
  --gpus all \
  --shm-size 32g \
  -v /path/to/model:/workspace/model \
  -p 30000:30000 \
  --ipc=host \
  lmsysorg/sglang:dev-cu13 \
  bash -c '
    pip install --no-cache-dir "git+https://github.com/huggingface/transformers.git@91b1ab1fdfa81a552644a92fbe3e8d88de40e167" &&
    exec python3 -m sglang.launch_server \
      --model-path /workspace/model \
      --attention-backend triton \
      --tp 1 \
      --reasoning-parser gemma4 \
      --tool-call-parser gemma4 \
      --mem-fraction-static 0.85 \
      --host 0.0.0.0 \
      --port 30000
  '
```

### Native (experimental)

```python
from transformers import AutoModelForImageTextToText, AutoProcessor

model = AutoModelForImageTextToText.from_pretrained(
    "YOUR_USERNAME/gemma-4-31B-it-heretic-FP8-Dynamic",
    dtype="auto",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(
    "YOUR_USERNAME/gemma-4-31B-it-heretic-FP8-Dynamic"
)
```

Requires `transformers >= 5.5.0` (Gemma 4 support) and `compressed-tensors`.

## Hardware Compatibility

| GPU | FP8 hardware support | Recommended |
|---|---|---|
| H100, H200 | Yes (E4M3) | ✅ Ideal |
| L40S, L40, RTX 6000 Ada | Yes | ✅ Good |
| RTX 4090 | Yes | ⚠️ Single card fits, TP=2 has PCIe overhead |
| RTX PRO 6000 Blackwell | Yes (DeepGemm fallback for ue8m0 scale) | ✅ Works with minor warnings |
| A100, A40, RTX 3090 | No (W8A16 Marlin fallback) | ⚠️ Memory savings only, no compute speedup |

## Benchmark

Measured on RTX PRO 6000 Blackwell 96GB (single GPU, TP=1, SGLang dev-cu13):

| Concurrent | Wall time | Median latency | Aggregate throughput |
|---|---|---|---|
| 1 | 0.93s | 0.93s | 24.6 tok/s |
| 3 | 6.25s | 2.17s | 34.4 tok/s |
| 6 | 6.16s | 6.16s | 108.3 tok/s |

VRAM usage: ~84 GB (weights 32 GB + KV cache 48 GB + overhead 4 GB) at 8K context length.

## Limitations

- Decensored (abliteration) may produce content the original Gemma 4 would refuse.
  Use responsibly and comply with applicable laws and regulations.
- Some refusal behaviors may still be present (7/100 refusal rate per Heretic's evaluation of the base model).
- KL divergence from original Gemma 4 31B: 0.3739 (from Heretic evaluation).
- FP8 quantization introduces negligible additional quality loss relative to the
  BF16 Heretic checkpoint (confirmed via native Transformers generation comparison).

## Acknowledgements

- [Google DeepMind](https://deepmind.google/models/gemma/) for the original Gemma 4 model
- [coder3101](https://huggingface.co/coder3101) for the Heretic ARA variant
- [p-e-w](https://github.com/p-e-w) for the [Heretic](https://github.com/p-e-w/heretic) abliteration tool
- [vLLM project](https://github.com/vllm-project/llm-compressor) for llm-compressor

## License

Apache 2.0 — inherited from the base model chain.
