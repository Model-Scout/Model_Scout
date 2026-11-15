---
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
library_name: mlx
pipeline_tag: image-text-to-text
base_model: nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
base_model_relation: quantized
language:
- en
- ar
- bg
- cs
- da
- de
- el
- es
- et
- fi
- fr
- hi
- hr
- hu
- id
- it
- ja
- ko
- lt
- lv
- nl
- "no"
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- th
- tr
- uk
- vi
- zh
tags:
- mlx
- optiq
- quantized
- mixed-precision
- 4bit
- 8bit
- nemotron
- gemma-4
- vision-language-model
- image-text-to-text
- apple-silicon
---

# mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit

> **Built with [mlx-optiq](https://mlx-optiq.com)**, the MLX-native toolkit to quantize, fine-tune, and serve LLMs locally on Apple Silicon, no PyTorch and no cloud. [Try the Lab](https://mlx-optiq.com/docs/lab/) · [All OptiQ quants](https://mlx-optiq.com/models) · [Docs](https://mlx-optiq.com/docs/)

**NVIDIA's Nemotron 3.5 Bolt, quantized for a Mac.** A mixed-precision MLX quant of [nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16), built on the Gemma-4 E4B architecture. 7.5 GB on disk, down from 16 GB bf16. See the [original card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) for what the model is trained to do and how NVIDIA evaluates it.

OptiQ quantizes the language tower to mixed 4/8-bit and keeps the vision tower at bf16 in a sidecar, so one checkpoint does both text and images.

## What it is

| Property | Value |
|---|---|
| Base | nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16 (Gemma-4 E4B architecture) |
| Language tower | per-layer 4/8-bit: 124 layers at 4-bit, 221 at 8-bit (345 total) |
| Vision tower | bf16, kept in `optiq_vision.safetensors` |
| On disk | 6.53 GB language + 0.96 GB vision |
| Group size | 64 |
| Context | 65,536 tokens |
| KV cache | `kv_config.json` included (mixed-precision KV for `optiq serve`) |

Following `llama.cpp`'s naming for mixed quants, the "4bit" label denotes the predominant precision, not the weighted average.

## How the bit-widths were chosen

The per-layer allocation was not measured on this model. It was transferred from [mlx-community/gemma-4-e4b-it-OptiQ-4bit](https://huggingface.co/mlx-community/gemma-4-e4b-it-OptiQ-4bit), whose allocation came from a KL-divergence sensitivity sweep over a [six-domain calibration mix](https://mlx-optiq.com/blog/calibration-mix). The two language towers share an architecture exactly, and all **345 tensors matched with none unmatched**.

## Checked after conversion

Run through this quant and its bf16 parent on Apple Silicon with greedy decoding and thinking off:

| Prompt | This quant | bf16 parent |
|---|---|---|
| 240 km in 3 h, average speed with steps | 80 km/h, same four steps | 80 km/h |
| Capital of Australia, and why not Sydney | Canberra, a compromise between Sydney and Melbourne | same answer, word for word |
| `is_palindrome(s)` ignoring case and non-alphanumerics | correct function | correct function |
| Call `get_weather` for Paris, JSON only | `{"tool_name": "get_weather", "params": {"city": "Paris"}}` | identical |

Image input: shown a red rectangle, a blue circle and the number 42, it answered "The image displays a red square, a blue circle, and the number 42 below them on a white background."

## Serve it with the assistant drafter

Google's Gemma-4 E4B assistant drafter shares this model's tokenizer and architecture, and speeds it up roughly 2x. Measured on a 24 GB M4, batch 1, greedy, thinking off, best of three runs each:

| Workload | Plain | `--drafter` (assistant) | `--ngram-draft 16` |
|---|---|---|---|
| Code generation | 26.6 tok/s | **57.9 tok/s (2.17x)** | 27.0 tok/s (1.02x) |
| Math, step by step | 26.5 tok/s | **60.8 tok/s (2.29x)** | 28.8 tok/s (1.09x) |
| Prose | 26.6 tok/s | **45.4 tok/s (1.70x)** | 26.4 tok/s (0.99x) |
| Edit (rename an identifier across a file, return it) | 26.3 tok/s | 62.6 tok/s (2.38x) | **93.6 tok/s (3.56x)** |

```bash
pip install mlx-optiq
optiq serve --model mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit \
            --drafter mlx-community/gemma-4-e4b-it-assistant-bf16
```

The drafter's guesses were accepted 74% of the time on code and 45% on prose, even though it was trained for the base Gemma rather than this fine-tune. Every token is still verified by the model itself: code, math and the edit came out identical to plain decoding; the prose run took a different word at one position where the model's top two choices were within bf16 rounding of each other. For edits that copy the prompt back, `--ngram-draft 16` is faster still.

## Use it

```bash
pip install mlx-optiq
# chat, images, and every app that talks to optiq serve
optiq serve --model mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit
optiq lab --model mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit
```

Text only, with stock mlx-lm:

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit")
messages = [{"role": "user", "content": "What is 17 multiplied by 23?"}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
print(generate(model, tokenizer, prompt=prompt, max_tokens=400))
```

Thinking is on by default under mlx-lm and `optiq serve`: the model writes a thought channel before the answer. Pass `enable_thinking=False` to `apply_chat_template` to turn it off; through `optiq serve`, send `"reasoning_effort": "none"` or `"chat_template_kwargs": {"enable_thinking": false}`. NVIDIA recommends temperature 1.0 and top-p 0.95 in both modes.

See the [Gemma-4 family guide](https://mlx-optiq.com/docs/gemma-4) for family-specific notes.
