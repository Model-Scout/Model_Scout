---
license: apache-2.0
base_model: mkd-hossain/Keural-Nova-v1.2-experimental
language: [ko, en]
pipeline_tag: text-generation
library_name: transformers
tags: [keural, keural-nova, mkd, nvfp4, fp4, quantized, compressed-tensors, vllm, blackwell, moe, qwen3]
---

# Keural Nova v1.2 — NVFP4 (experimental)

**NVFP4 (4-bit) quantization of [Keural Nova v1.2](https://huggingface.co/mkd-hossain/Keural-Nova-v1.2-experimental)**,
by **[MKD](https://mkd.kr)**, for high-throughput serving on **NVIDIA Blackwell** GPUs via **vLLM**.

- **67 GB (bf16) → 21.9 GB (NVFP4)** — ~3× smaller.
- Recipe replicates `RedHatAI/Qwen3.6-35B-A3B-NVFP4`: **NVFP4 4-bit weights + activations** on the
  language model; **vision tower, `lm_head`, and MTP kept in high precision** for accuracy.
- Format: **`compressed-tensors` / `nvfp4-pack-quantized`** → served directly by vLLM.

## ⚠️ Hardware
FP4 tensor cores exist only on **Blackwell (B200 / GB200 / RTX 50xx)**. Serve there for the
speed/memory benefit. (Hopper/H200 lack FP4 kernels — this checkpoint is *produced* on H200 but
*runs accelerated* on Blackwell.)

## Serving (vLLM on Blackwell)
```bash
vllm serve mkd-hossain/Keural-Nova-v1.2-experimental-NVFP4 \
  --served-model-name Keural-Nova-v1.2 \
  --tensor-parallel-size 2 \
  --max-model-len 262144 \
  --tool-call-parser qwen3_xml --enable-auto-tool-choice
```
- **Non-thinking default** (the fixed chat template ships here); tool calls are **Qwen XML**.
- **Serve native 256K** for agent/tool workloads (YaRN 1M only for genuine >256K requests).
- Multimodal (vision) works — the vision tower is kept high-precision.

## Quantization details
- **Tool:** `llm-compressor` (compressed-tensors), NVFP4 scheme.
- **Calibration:** 512 samples from the Keural Nova v1.2 SFT mix (Korean/English/code/tool-use), seq-len 2048.
- **Coverage:** 31,070 linear layers quantized (incl. **30,880 MoE experts** + attention + Gated-DeltaNet
  linear-attention); **vision blocks + `lm_head` + MTP excluded** (bf16).
- **Group scheme:** weights 4-bit float / activations 4-bit float, per-block FP8 scales (NVFP4).

## Accuracy
NVFP4 typically costs ~1–2% vs bf16 — the same small delta as the public
`nvidia`/`RedHatAI` NVFP4 Qwen3.6-A3B checkpoints. **Validate on your Blackwell** against the
bf16 base ([Keural-Nova-v1.2-experimental](https://huggingface.co/mkd-hossain/Keural-Nova-v1.2-experimental))
on your workload (tool-calling, Korean, code) before production.

## License & attribution
Apache-2.0, inheriting the base **Qwen/Qwen3.6-35B-A3B** license. Quantization recipe after
`RedHatAI/Qwen3.6-35B-A3B-NVFP4`. "Keural Nova" is a model by MKD.
