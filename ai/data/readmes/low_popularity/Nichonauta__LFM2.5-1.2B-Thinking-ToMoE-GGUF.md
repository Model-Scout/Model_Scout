---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking/blob/main/LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
base_model: Nichonauta/LFM2.5-1.2B-Thinking-ToMoE
tags:
- lfm2
- mixture-of-experts
- tomoe
- gguf
- llama.cpp
- reasoning
pipeline_tag: text-generation
---

# LFM2.5-1.2B-Thinking-ToMoE-GGUF

GGUF quantizations of **[Nichonauta/LFM2.5-1.2B-Thinking-ToMoE](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE)** — the ToMoE Mixture-of-Experts conversion of [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking).

## Files

| File | Quantization | Size | BPW |
|---|---|---|---|
| `LFM2.5-1.2B-Thinking-ToMoE-BF16.gguf` | BF16 | 2343 MB | 16.0 |
| `LFM2.5-1.2B-Thinking-ToMoE-Q8_0.gguf` | Q8_0 | 1186 MB | 8.50 |
| `LFM2.5-1.2B-Thinking-ToMoE-Q4_K_M.gguf` | Q4_K_M | **695 MB** | 4.98 |

The Q4_K_M version runs **under 1 GB** of storage — matching the "on-device under 1 GB" goal of the original model.

## Important note about the conversion

The ToMoE channel-MoE experts and the per-token dynamic V masks have **no native representation in llama.cpp**'s LFM2 architecture. To produce a runnable GGUF, the pruned model was rebuilt as a **dense-equivalent**:

- The cut conv layers were restored to their full width using the original dense weights (the conv weights were never modified by ToMoE — only masked at runtime).
- The MLP union cut (~99% of the FFN was already preserved) was restored to the full FFN.
- The attention Q/K were already full-width in the pruned model.

As a result, the GGUF behaves like the dense base model rather than the pruned MoE (including the native `<think>` reasoning behavior of LFM2.5-Thinking). For the actual MoE behavior, use the safetensors version with `trust_remote_code`.

## Usage (llama.cpp, CUDA)

```bash
llama-server.exe ^
  --model LFM2.5-1.2B-Thinking-ToMoE-Q4_K_M.gguf ^
  --gpu-layers all ^
  --ctx-size 32768 ^
  --temp 0.05 ^
  --top-k 50 ^
  --repeat-penalty 1.05 ^
  --alias LFM2.5-1.2B-Thinking-ToMoE
```

Or with `llama-cli` (single turn, shows the thinking block):

```bash
llama-cli.exe -m LFM2.5-1.2B-Thinking-ToMoE-Q4_K_M.gguf -ngl 99 -p "What is the capital of France?" -n 90
```

Measured on an RTX 3060 (CUDA 13.3 build, llama.cpp b10603): **~302 t/s** generation for Q4_K_M, ~212 t/s for Q8_0, ~125 t/s for BF16. The official generation parameters of the base model (temperature 0.05, top_k 50, repetition_penalty 1.05) are recommended.

## Base model

- **MoE source**: [Nichonauta/LFM2.5-1.2B-Thinking-ToMoE](https://huggingface.co/Nichonauta/LFM2.5-1.2B-Thinking-ToMoE)
- **Dense base**: [LiquidAI/LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) (LFM Open License v1.0)

## License

Derivative of LiquidAI/LFM2.5-1.2B-Thinking — released under the **LFM Open License v1.0** (see `LICENSE`).
