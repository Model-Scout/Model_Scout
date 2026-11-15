---
library_name: transformers
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model:
  - nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16
base_model_relation: finetune
pipeline_tag: text-generation
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
  - no
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
  - nvidia
  - nemotron
  - nemotron-3.5
  - gemma4
  - heretic
  - abliteration
  - refusal-direction
  - abliterated
  - uncensored
---

# Nemotron-3.5-Bolt-E4B-Heretic

GGUF quants: [grumd0/Nemotron-3.5-Bolt-E4B-Heretic-GGUF](https://huggingface.co/grumd0/Nemotron-3.5-Bolt-E4B-Heretic-GGUF)

An abliterated variant of
[nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16),
made with [Heretic](https://github.com/p-e-w/heretic). The model uses Heretic's Arbitrary-Rank Ablation (ARA) modifier.

> [!WARNING]
> This is an **abliterated / uncensored** derivative. It has been optimized to
> reduce refusal behavior, so it may comply with requests that the base model
> refuses and may produce inaccurate, biased, or otherwise harmful content.
> Use it responsibly and in compliance with applicable laws and the licenses
> below. This is not an NVIDIA or Google product and comes with no warranty.

Refusals (none of these prompts were in the Heretic training set):

| Refusals | Base model | This model |
|:---|---:|---:|
| JailbreakBench Harmful | 89/100 | **3/100** |
| JailbreakBench Benign | 18/100 | **0/100** |
| XSTest Unsafe | 155/200 | **32/200** |
| KL divergence | 0 | **0.0859** |

KL divergence measured by Heretic on [harmless_alpaca](https://huggingface.co/datasets/mlabonne/harmless_alpaca).

| Parameter | Value |
|:---|---:|
| `start_layer_index` | 12 |
| `end_layer_index` | 27 |
| `preserve_good_behavior_weight` | 0.5232480534666997 |
| `steer_bad_behavior_weight` | 0.000237553833412742 |
| `overcorrect_relative_weight` | 0.748730444223033 |
| `neighbor_count` | 14 |

## License

The base model is released by NVIDIA under the
[OpenMDW License Agreement, version 1.1](https://openmdw.ai/license/1-1/),
and is post-trained from Google's
[gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it), which is
licensed under the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Attribution

- Base model: [NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) (NVIDIA Corporation)
- Upstream model: [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) (Google)
- Abliteration: [Heretic](https://github.com/p-e-w/heretic) (Philipp Emanuel Weidmann and contributors)
