---
library_name: gguf
license: other
license_name: openmdw-1.1
license_link: https://openmdw.ai/license/1-1/
base_model:
  - grumd0/Nemotron-3.5-Bolt-E4B-Heretic
base_model_relation: quantized
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
  - gguf
  - llama.cpp
  - nvidia
  - nemotron
  - nemotron-3.5
  - gemma4
  - heretic
  - abliteration
  - refusal-direction
  - abliterated
  - uncensored
  - quantized
---

# Nemotron-3.5-Bolt-E4B-Heretic-GGUF

BF16 safetensors: [grumd0/Nemotron-3.5-Bolt-E4B-Heretic](https://huggingface.co/grumd0/Nemotron-3.5-Bolt-E4B-Heretic)

GGUF of an abliterated variant of
[nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16),
made with [Heretic](https://github.com/p-e-w/heretic) and converted with
[llama.cpp](https://github.com/ggml-org/llama.cpp). The model uses Heretic's Arbitrary-Rank Ablation (ARA) modifier.

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

## Quantization quality

KL divergence of each file from this model's BF16 weights (quantization error) and from
NVIDIA's BF16 base model (abliteration plus quantization), measured with llama.cpp's
`llama-perplexity --kl-divergence` on 100 × 512 tokens of wikitext-2 (test).

| File | Size | KLD vs Heretic BF16 | Same top token | KLD vs NVIDIA BF16 | Same top token |
|:---|---:|---:|---:|---:|---:|
| BF16 | 14.94 GB | 0 | 100% | 0.0969 | 87.95% |
| UD-Q8_K_XL | 8.13 GB | 0.0045 | 97.45% | 0.1007 | 87.85% |
| Q8_0 | 7.97 GB | 0.0077 | 96.59% | 0.1025 | 87.68% |
| UD-Q6_K_XL | 7.23 GB | 0.0079 | 96.58% | 0.1035 | 87.66% |
| ~~Q6_K~~ *(removed)* | ~~6.17 GB~~ | ~~0.0333~~ | ~~92.78%~~ | ~~0.1237~~ | ~~86.38%~~ |
| UD-Q5_K_XL | 5.80 GB | 0.0154 | 95.25% | 0.1070 | 87.53% |
| ~~Q4_K_M~~ *(removed)* | ~~5.30 GB~~ | ~~0.3685~~ | ~~77.18%~~ | ~~0.4480~~ | ~~75.37%~~ |
| UD-Q4_K_XL | 5.03 GB | 0.0416 | 91.93% | 0.1307 | 86.27% |
| UD-Q3_K_XL | 4.20 GB | 0.1283 | 86.25% | 0.2113 | 82.61% |
| UD-Q2_K_XL | 3.72 GB | 0.3669 | 77.30% | 0.4401 | 75.15% |

Q6_K and Q4_K_M were made without an importance matrix and were removed from this repository
after measuring worse than the smaller UD-Q5_K_XL and UD-Q4_K_XL.

The `UD-*_K_XL` files use the same per-tensor quantization types and importance matrix as
Unsloth's dynamic quants of the base model,
[unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF).

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
- GGUF conversion and quantization: [llama.cpp](https://github.com/ggml-org/llama.cpp)
- `UD-*_K_XL` quantization recipes and importance matrix: [Unsloth](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF)
