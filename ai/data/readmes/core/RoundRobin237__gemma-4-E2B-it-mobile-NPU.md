---
license: apache-2.0
base_model: google/gemma-4-E2B-it
base_model_relation: quantized
language: [en, ko]
tags: [gemma4, executorch, qualcomm, qnn, sm8450, hexagon, android, text-generation, experimental]
---

# gemma-4-E2B-it-mobile-NPU

Community text-only conversion of [Google Gemma 4 E2B Instruct](https://huggingface.co/google/gemma-4-E2B-it)
for **PyTorch ExecuTorch with the Qualcomm QNN HTP backend**. The model runs locally
on the Snapdragon 8 Gen 1 / SM8450 NPU, with portable CPU token-embedding kernels.
The original model was not fine-tuned.

## Compatible engine

- Engine Git: [pytorch/executorch](https://github.com/pytorch/executorch).
- Tested revision: [`ca56e1ffdba1c902d9202021d7297982d3501439`](https://github.com/pytorch/executorch/tree/ca56e1ffdba1c902d9202021d7297982d3501439).
- Backend: [ExecuTorch Qualcomm QNN](https://github.com/pytorch/executorch/tree/ca56e1ffdba1c902d9202021d7297982d3501439/backends/qualcomm).
- Runner: [Gemma-capable qnn_llama_runner](https://github.com/pytorch/executorch/tree/ca56e1ffdba1c902d9202021d7297982d3501439/examples/qualcomm/oss_scripts/llama).
- QNN SDK/runtime version: **2.37.0.250724**; target **SM8450 / Hexagon v69**.

Use an Android ARM64 Gemma-capable ExecuTorch runner built with the matching
Qualcomm backend/runtime and portable quantized embedding support. The older
Qwen-only runner is incompatible. The PTE cannot be loaded as GGUF in llama.cpp.
Runtime binaries are obtained separately under their licenses; none are bundled here.
Other Snapdragon targets and Exynos have not been validated.

## Model files and configuration

| Item | Value |
|---|---|
| Weights | `gemma4-e2b-v69-mixed4b32-ffn-all-tail8w8-kv16-quality-2k-shard11.pte` |
| Bytes | 3,361,616,512 (approximately 3.36 GB) |
| SHA-256 | `38faf5d2337d9fb2b75b2ddca0fb3c63d916b2795c55bff6a1b6b92c027e8c7b` |
| Context | Fixed **2,048 tokens**, input and output combined |
| Decoder quantization | Mixed W4 block32 / W8, A16, KV16 |
| CPU embeddings | Q4, group size 32 |
| QNN delegates | 12 |
| Source revision | `3e22461f65e89153144f8adb70e3b8c2cc9845a7` |

FFN gate/up/down projections primarily use W4; the final eight cross-decoder
FFN down projections remain W8. Other decoder projections, including attention
and the output head, remain W8. The attention MatMul right-hand input is requantized
to eight bits for v69 compatibility. Full recipe metadata is in `quantization.json`.
The JSON tokenizer is for the ExecuTorch runner. The optional GGUF vocabulary
contains no model tensors and can be used for tokenization/chat templating.
Vision, audio, and MTP are not included. Increasing a runtime context setting
does not extend the compiled 2K model.

## Samsung Galaxy S22 Ultra benchmark

Test device: **SM-S908N, Snapdragon 8 Gen 1 / SM8450, 12 GB RAM**, real Hexagon v69 execution.
Three Korean Java-generation requests used greedy decoding (`temperature=0`).

| Request | Native decode tokens/second | Code execution result |
|---|---:|---|
| Basic diamond | 6.78 | Compiled; diamond logic incorrect |
| Scanner diamond | 6.52 | Passed inputs 1, 2, 3, 5, 7 |
| Sum 1 through 20 | 6.45 | Correct result: 210 |

Observed decode throughput was approximately **6.5–6.8 tokens/second**.
These are native decode rates, excluding model loading and prompt processing,
and do not describe end-to-end response latency or guaranteed sustained performance.
Raw token counts, native timing values, and total request wall times are in `benchmark.json`.
A separate request with **1,299 input tokens** verified execution beyond 1K.

All three Java answers compiled, but functional checks passed **2/3**. The basic
diamond answer printed only one star per row. The same model's Q4_K_M GGUF
baseline generated a functioning diamond for that request. General GGUF-equivalent
quality has not been established, and the failed check is retained in the benchmark.
No phone CPU/GPU engine speed comparison or broad multilingual evaluation was performed.

## License

Original model: Apache-2.0 (`LICENSE`). ExecuTorch: BSD-3-Clause (`ExecuTorch-LICENSE.txt`).
Qualcomm SDK/runtime remains subject to Qualcomm's separate terms. See `NOTICE`.
