---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model: orcarouter/LFM3-1.7B-abliterated
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
tags:
- gguf
- lfm3
- llama.cpp
- abliterated
- quantized
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
---

# LFM3-1.7B-abliterated GGUF

GGUF files of [orcarouter/LFM3-1.7B-abliterated](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated) for llama.cpp.

Nothing here was trained or abliterated. The BF16 file is a format conversion of that repo's safetensors. Q8_0 and Q4_K_M are standard llama.cpp quants of that BF16 file. They are not the Liquid AI QAD Q4_0 quant.

## Credit

- Liquid AI made [LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) and the LFM Open License v1.0 in `LICENSE`.
- OrcaRouter published the abliterated weights at [orcarouter/LFM3-1.7B-abliterated](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated).
- [llama.cpp](https://github.com/ggml-org/llama.cpp) b12040, commit `00ef13664`, did the safetensors to GGUF conversion and the quants. LFM3 needs llama.cpp b11960 (v0.8.0) or newer.

## What changed

The safetensors were converted to GGUF. Q8_0 and Q4_K_M were quantized from that BF16 GGUF. No tensor was finetuned.

## Files

| File | Quant |
| --- | --- |
| `LFM3-1.7B-abliterated-BF16.gguf` | BF16. Same values as the source safetensors. |
| `LFM3-1.7B-abliterated-Q8_0.gguf` | Q8_0 |
| `LFM3-1.7B-abliterated-Q4_K_M.gguf` | Q4_K_M |

Context length is 262144. The source chat template is stored in the GGUF, including tool calls.

## Run

```bash
llama-cli -m LFM3-1.7B-abliterated-Q4_K_M.gguf -c 131072 --jinja --temp 0.1 --top-k 50 --repeat-penalty 1.1
```

Those sampler values come from the source model card. Use a context size that fits the GPU. The weights were trained for 262144 tokens.
