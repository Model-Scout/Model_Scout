---
language:
- en
- zh
- ko
- ja
license: apache-2.0
base_model: Jackrong/Qwopus3.6-27B-v2
tags:
- qwen3.5
- qwen3.6
- qwopus
- reasoning
- quantized
- nvfp4
- fp8
- compressed-tensors
- multi-token-prediction
pipeline_tag: text-generation
library_name: transformers
quantized_by: mconcat
---

# Qwopus3.6-27B-v2-NVFP4

Mixed-precision (NVFP4 + FP8 + BF16) quantization of [Jackrong/Qwopus3.6-27B-v2](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2), a Claude Opus reasoning-distilled fine-tune of Qwen 3.6 27B.

The hybrid DeltaNet + softmax attention architecture is preserved, the 1-layer MTP head is included as a BF16 sidecar for speculative decoding, and the multimodal processor metadata is kept intact.

## Quick start

Requires **vLLM ≥ 0.21.0** and a Blackwell-class GPU (SM 10.0+) for native NVFP4 W4A4 inference:

```bash
vllm serve mconcat/Qwopus3.6-27B-v2-NVFP4 \
  --tensor-parallel-size 1 \
  --max-model-len 16384 \
  --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' \
  --tool-call-parser qwen3_coder \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --trust-remote-code
```

## Benchmarks

Evaluated with [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) on a single NVIDIA B300 SXM6, 100 samples per task, 0-shot CoT, `max_gen_toks=4096`:

| Task | Qwen 3.6 27B (base) | Qwopus 3.6 v2 (source BF16) | **This (NVFP4)** |
|---|---:|---:|---:|
| GSM8K (flexible-extract) | 65.0% | 87.0% | **87.0%** |
| ARC-Challenge (acc) | 50.0% | 50.0% | **53.0%** |
| TruthfulQA-MC2 | 55.1% | 59.3% | **58.7%** |
| IFEval (inst_level_strict) | 40.5% | 42.3% | **41.7%** |

Accuracy is preserved versus the BF16 source — the GSM8K score is identical to the source and the other tasks match within standard error.

## Throughput

Measured on a single NVIDIA B300 SXM6 with vLLM 0.21.0 and `torch.compile` enabled:

| Setup | Throughput | Speedup |
|---|---:|---:|
| Batch = 1, no MTP | 121 tok/s | 1.00× |
| Batch = 1, MTP `num_speculative_tokens = 3` | **274 tok/s** | **2.26×** |
| Batch = 8 continuous batching, no MTP | 1054 tok/s | — |

Self-test of tool calling with `--tool-call-parser qwen3_coder`: passes (model emits well-formed `<tool_call>...</tool_call>` syntax that the parser extracts correctly).

## Quantization

| Precision | Modules |
|---|---|
| **NVFP4 W4A4** (group_size = 16) | `o_proj`, MLP `gate_proj`, MLP `up_proj` |
| **FP8 W8A8 dynamic** (per-channel weight, per-token activation) | `q_proj`, `k_proj`, `v_proj`, MLP `down_proj`, DeltaNet `in_proj_qkv`, `in_proj_z`, `out_proj` |
| **BF16** | `lm_head`, `embed_tokens`, norms, DeltaNet small projections (`in_proj_a`, `in_proj_b`), vision tower, multimodal projector, 1-layer MTP head |

Calibration data: 1024 self-generated reasoning traces from the BF16 source model (256 prompts × 4 generations) spanning math, code, logic, analysis, creative writing, general knowledge, tool calling, and Korean. Generated at temperature=1.0, top_p=0.95.

## Files

| File | Size | Purpose |
|---|---:|---|
| `model.safetensors` | 25.2 GB | Main quantized weights |
| `model.mtp.safetensors` | 849 MB | MTP head (BF16 sidecar) |
| `config.json` + tokenizer + processor configs | <100 MB | Standard metadata |

Total checkpoint size: **~26 GB** (down from ~54 GB BF16 source).

## License

Apache 2.0 (inherited from the base model).
