---
license: gemma
base_model:
  - google/gemma-4-26B-A4B-it
  - huihui-ai/Huihui-gemma-4-26B-A4B-it-abliterated
  - Jiunsong/supergemma4-26b-abliterated-multimodal
tags:
  - gemma4
  - mlx
  - multimodal
  - image-text-to-text
  - abliterated
  - uncensored
  - quantized
  - 4-bit
  - apple-silicon
language:
  - en
  - ko
pipeline_tag: image-text-to-text
library_name: mlx
---

[Support ongoing open-source work: ko-fi.com/jiunsong](https://ko-fi.com/jiunsong)

# SuperGemma4-26B-Abliterated-Multimodal MLX 4bit

This is the lighter-weight MLX build of [Jiunsong/supergemma4-26b-abliterated-multimodal](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal).

It preserves multimodal behavior while reducing local storage and memory demand for Apple Silicon setups that want a smaller package.

## Important note on the Hugging Face size badge

If the Hub UI shows this repo as a smaller class such as `5B` or `8B`, that is a Hub-side auto-inference artifact from the exported MLX quantized config.

This repo is still a quantized release of the full `SuperGemma4-26B-Abliterated-Multimodal` line derived from the Gemma 4 `26B-A4B` multimodal family. The smaller badge does **not** mean the model was accidentally converted into a different 5B or 8B model.

## Why this variant

- Smaller MLX footprint for local use
- Keeps text + vision support
- Preserves the abliterated / low-refusal behavior of the main release
- Good option when you want better fit on-device without dropping multimodality
- Verified with both text-only and image-grounded prompts

## April 18 Stability Sync

- Synced this quantized child repo to the latest hardened parent chat template.
- Updated exact JSON-only formatting, long-context extraction, false-premise correction, and prompt-hygiene behavior.
- This refresh does not change the quantized weights themselves; it updates the serving template and release notes so downstream runtimes inherit the same behavior fixes.
- Parent validation snapshot after the refresh: capability audit `9 / 9`, reliability audit `20 / 20`.

## Validation

- Text check: returned `READY`
- Image check: returned `red` for a solid red test image
- Disk footprint: about `15 GB`

## Recommended use

Pick this version when you want a smaller MLX package and are willing to trade a bit of precision for a lighter local deployment.

## Quick start

```bash
python3 -m mlx_vlm.server \
  --model /absolute/path/to/supergemma4-26b-abliterated-multimodal-mlx-4bit \
  --host 127.0.0.1 \
  --port 8091
```

```python
from mlx_vlm import load

model, processor = load("/absolute/path/to/supergemma4-26b-abliterated-multimodal-mlx-4bit")
print("Loaded.")
```
