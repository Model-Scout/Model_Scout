---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-350M/blob/main/LICENSE
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
base_model: Nichonauta/LFM2.5-350M-ToMoE
tags:
- lfm2
- mixture-of-experts
- tomoe
- gguf
- llama.cpp
pipeline_tag: text-generation
---

# LFM2.5-350M-ToMoE-GGUF

GGUF quantizations of **[Nichonauta/LFM2.5-350M-ToMoE](https://huggingface.co/Nichonauta/LFM2.5-350M-ToMoE)** — the ToMoE Mixture-of-Experts conversion of [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M).

## Files

| File | Quantization | Size | BPW |
|---|---|---|---|
| `LFM2.5-350M-ToMoE-BF16.gguf` | BF16 | 678 MB | 16.0 |
| `LFM2.5-350M-ToMoE-Q8_0.gguf` | Q8_0 | 362 MB | 8.50 |
| `LFM2.5-350M-ToMoE-Q4_K_M.gguf` | Q4_K_M | 219 MB | 5.12 |

## Important note about the conversion

The ToMoE channel-MoE experts and the per-token dynamic V masks have **no native representation in llama.cpp**'s LFM2 architecture. To produce a runnable GGUF, the pruned model was rebuilt as a **dense-equivalent**:

- The cut conv layers were restored to their full width using the original dense weights (the conv weights were never modified by ToMoE — only masked at runtime).
- The MLP union cut (~99% of the FFN was already preserved) was restored to the full FFN.
- The attention Q/K were already full-width in the pruned model.

As a result, the GGUF behaves like the dense base model rather than the pruned MoE. For the actual MoE behavior, use the safetensors version with `trust_remote_code`.

## Usage (llama.cpp, CUDA)

```bash
llama-server.exe ^
  --model LFM2.5-350M-ToMoE-Q4_K_M.gguf ^
  --gpu-layers all ^
  --ctx-size 32768 ^
  --alias LFM2.5-350M-ToMoE
```

Or with `llama-cli`:

```bash
llama-cli.exe -m LFM2.5-350M-ToMoE-Q4_K_M.gguf -ngl 99 -p "The capital of France is" -n 30
```

Measured on an RTX 3060 (CUDA 13.3 build, llama.cpp b10603): ~470 t/s generation for Q4_K_M, ~370 t/s for Q8_0, ~270 t/s for BF16.

## Base model

- **MoE source**: [Nichonauta/LFM2.5-350M-ToMoE](https://huggingface.co/Nichonauta/LFM2.5-350M-ToMoE)
- **Dense base**: [LiquidAI/LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) (LFM Open License v1.0)

## License

Derivative of LiquidAI/LFM2.5-350M — released under the **LFM Open License v1.0** (see `LICENSE`).
