---
library_name: mlx
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
inference: false
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
tags:
- mistral-common
- mlx
- ministral
- ministral-3
- vision-language
- multimodal
- quantized
- edge
- 6-bit
- base-model
pipeline_tag: image-text-to-text
base_model: mistralai/Ministral-3-14B-Base-2512
---

# mlx-community/Ministral-3-14B-Base-2512-6bit

This is, **Ministral 3 14B Base 2512** is a vision-language model: a text backbone paired
with a vision encoder, supporting image understanding alongside text. This is
the **base pre-trained** checkpoint — not instruction- or chat-tuned. For
chat/instruction-following use cases, use the
[Instruct variant](https://huggingface.co/mlx-community/Ministral-3-14B-Instruct-2512-6bit)
instead; this base checkpoint is intended for custom post-training/fine-tuning.

> **Community note.** Structural check confirms the vision tower and
> multimodal projector were carried over intact (not dropped, which is a real
> failure mode for text-only conversion tools on vision-language models).
> Functional check confirms both text-only and image+text generation produce
> coherent output. Converted and verified by a single maintainer running
> local MLX tooling -- not independently reviewed by anyone else; please open
> a discussion if you hit anything unexpected.

This is an MLX conversion of [`mistralai/Ministral-3-14B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512),
converted with [mlx-vlm](https://github.com/Blaizzy/mlx-vlm). Refer to the
[original model card](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512) for the full
description, capabilities, and license terms.

## Heads up

- **Base model, not instruct-tuned** — expect raw completion behavior, not
  chat-following. Don't expect it to follow instructions well.
- **Vision retained at full precision** — only the language backbone is
  quantized; the vision tower and multimodal projector are untouched bf16,
  per mlx-vlm's standard policy of not quantizing multimodal modules.
- **Output size on disk: 12.68GB**

## Provenance

- Source: [`mistralai/Ministral-3-14B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512) (BF16)
- Language model layers: **6-bit** affine quantization, group_size=64
- Vision tower + multimodal projector: kept at full precision (not quantized)
- Blended average: **7.257 bits per weight** across all parameters

## Ministral 3 family

| Model | Type | mlx-community (4-bit) |
|---|---|---|
| Ministral 3 3B Base 2512 | Base pre-trained | [mlx-community/Ministral-3-3B-Base-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-3B-Base-2512-4bit) |
| Ministral 3 3B Instruct 2512 | Instruct post-trained | [mlx-community/Ministral-3-3B-Instruct-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-3B-Instruct-2512-4bit) |
| Ministral 3 3B Reasoning 2512 | Reasoning capable | [mlx-community/Ministral-3-3B-Reasoning-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-3B-Reasoning-2512-4bit) |
| Ministral 3 8B Base 2512 | Base pre-trained | [mlx-community/Ministral-3-8B-Base-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-8B-Base-2512-4bit) |
| Ministral 3 8B Instruct 2512 | Instruct post-trained | [mlx-community/Ministral-3-8B-Instruct-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-8B-Instruct-2512-4bit) |
| Ministral 3 8B Reasoning 2512 | Reasoning capable | [mlx-community/Ministral-3-8B-Reasoning-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-8B-Reasoning-2512-4bit) |
| Ministral 3 14B Base 2512 | Base pre-trained | [mlx-community/Ministral-3-14B-Base-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-14B-Base-2512-4bit) |
| Ministral 3 14B Instruct 2512 | Instruct post-trained | [mlx-community/Ministral-3-14B-Instruct-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-14B-Instruct-2512-4bit) |
| Ministral 3 14B Reasoning 2512 | Reasoning capable | [mlx-community/Ministral-3-14B-Reasoning-2512-4bit](https://huggingface.co/mlx-community/Ministral-3-14B-Reasoning-2512-4bit) |

## Use with mlx

```bash
pip install -U mlx-vlm
```

```bash
python -m mlx_vlm.generate --model mlx-community/Ministral-3-14B-Base-2512-6bit --max-tokens 100 --temperature 0.0 --prompt "Describe this image." --image <path_to_image>
```

For text-only prompts, omit `--image`.

## License

Apache 2.0 — see the [original model card](https://huggingface.co/mistralai/Ministral-3-14B-Base-2512) for
the full license text and any usage terms.
