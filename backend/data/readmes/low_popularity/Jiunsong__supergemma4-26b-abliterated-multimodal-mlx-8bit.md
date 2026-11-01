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
  - 8-bit
  - apple-silicon
language:
  - en
  - ko
pipeline_tag: image-text-to-text
library_name: mlx
---

[Support ongoing open-source work: ko-fi.com/jiunsong](https://ko-fi.com/jiunsong)

# SuperGemma4-26B-Abliterated-Multimodal MLX 8bit

This is the recommended Apple Silicon local-default build of [Jiunsong/supergemma4-26b-abliterated-multimodal](https://huggingface.co/Jiunsong/supergemma4-26b-abliterated-multimodal).

It keeps the full text + vision behavior of the base release while giving you a practical MLX package that is ready to use on-device.

## Important note on the Hugging Face size badge

If the Hub UI shows this repo as a smaller class such as `5B` or `8B`, that is a Hub-side auto-inference artifact from the exported MLX quantized config.

This repo is still a quantized release of the full `SuperGemma4-26B-Abliterated-Multimodal` line derived from the Gemma 4 `26B-A4B` multimodal family. The smaller badge does **not** mean the model was accidentally converted into a different 5B or 8B model.

## Why this variant

- Best local-default choice on Apple Silicon
- Keeps multimodal support intact
- Strong low-refusal / abliterated behavior
- Quantized for a much smaller local footprint than the full model
- Verified with both text-only and image-grounded prompts

## April 18 Stability Sync

- Synced this quantized child repo to the latest hardened parent chat template.
- Updated exact JSON-only formatting, long-context extraction, false-premise correction, and prompt-hygiene behavior.
- This refresh does not change the quantized weights themselves; it updates the serving template and release notes so downstream runtimes inherit the same behavior fixes.
- Parent validation snapshot after the refresh: capability audit `9 / 9`, reliability audit `20 / 20`.

## Validation

- Text check: returned `READY`
- Image check: returned `red` for a solid red test image
- Disk footprint: about `26 GB`

## Recommended use

Use this build if you want the strongest local MLX version and have enough memory headroom. This is the variant configured as the preferred local runtime for our own Apple Silicon workflow.

## Quick start

```python
from mlx_vlm import load, generate

model, processor = load("/absolute/path/to/supergemma4-26b-abliterated-multimodal-mlx-8bit")

prompt = processor.apply_chat_template(
    [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the image briefly."},
                {"type": "image", "image": "/absolute/path/to/image.png"},
            ],
        }
    ],
    tokenize=False,
    add_generation_prompt=True,
)

out = generate(
    model,
    processor,
    prompt,
    image="/absolute/path/to/image.png",
    max_tokens=128,
    temperature=0.0,
    verbose=False,
)

print(out.text)
```

```bash
python3 -m mlx_vlm.server \
  --model /absolute/path/to/supergemma4-26b-abliterated-multimodal-mlx-8bit \
  --host 127.0.0.1 \
  --port 8091
```
