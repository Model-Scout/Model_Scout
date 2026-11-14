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
- awq
- int4
- multi-token-prediction
pipeline_tag: text-generation
library_name: transformers
quantized_by: mconcat
---

# Qwopus3.6-27B-v2-AWQ-4bit

AutoAWQ-format INT4 (W4A16) quantization of [Jackrong/Qwopus3.6-27B-v2](https://huggingface.co/Jackrong/Qwopus3.6-27B-v2), a Claude Opus reasoning-distilled fine-tune of Qwen 3.6 27B.

The hybrid DeltaNet + softmax attention architecture is preserved, the 1-layer MTP head is included for speculative decoding, and the multimodal processor metadata is kept intact. APEX-style edge protection keeps the first and last layers in BF16 for quality.

## Quick start

Requires **vLLM ≥ 0.21.0**:

```bash
vllm serve mconcat/Qwopus3.6-27B-v2-AWQ-4bit \
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

| Task | Qwen 3.6 27B (base) | Qwopus 3.6 v2 (source BF16) | **This (AWQ-4bit)** |
|---|---:|---:|---:|
| GSM8K (flexible-extract) | 65.0% | 87.0% | **85.0%** |
| ARC-Challenge (acc_norm) | 46.0% | 45.0% | **47.0%** |
| TruthfulQA-MC2 | 55.1% | 59.3% | **59.3%** |
| IFEval (inst_level_strict) | 40.5% | 42.3% | **42.9%** |

Quantization preserves accuracy within standard error of the BF16 source on every task, and matches the source on TruthfulQA. The Claude Opus reasoning gain over the Qwen 3.6 base (+20 pp on GSM8K) is retained.

## Throughput

Measured on a single NVIDIA B300 SXM6 with vLLM 0.21.0 and `torch.compile` enabled:

| Setup | Throughput | Speedup |
|---|---:|---:|
| Batch = 1, no MTP | 115 tok/s | 1.00× |
| Batch = 1, MTP `num_speculative_tokens = 3` | **251 tok/s** | **2.19×** |
| Batch = 8 continuous batching, no MTP | 880 tok/s | — |

MTP speculative decoding hits an **Avg Draft acceptance rate of ~77 %** (per-position: 0.92 / 0.79 / 0.65) with a mean acceptance length of ~3.3, measured on a mixed reasoning + code prompt set at greedy decoding.

Self-test of tool calling with `--tool-call-parser qwen3_coder`: passes (model emits well-formed `<tool_call>...</tool_call>` syntax).

## Quantization

| Precision | Modules |
|---|---|
| **INT4 asymmetric, group_size = 128** | `q_proj`, `k_proj`, `v_proj`, MLP `gate_proj`, MLP `up_proj`, DeltaNet `in_proj_qkv`, `in_proj_z` |
| **BF16** | `o_proj`, MLP `down_proj`, `lm_head`, `embed_tokens`, norms, DeltaNet small projections (`in_proj_a`, `in_proj_b`), DeltaNet `out_proj`, vision tower, multimodal projector, 1-layer MTP head, **first 5 and last 5 transformer layers (APEX edge protection)** |

The AWQ skip list also names every `mtp.*` linear module explicitly so the MTP draft head stays unquantized — previous revisions of this checkpoint omitted those entries, which caused vLLM to build the MTP head with AWQ-packed parameters and produced 0 % draft acceptance.

Tuned with [AutoRound](https://github.com/intel/auto-round) on 1024 self-generated reasoning traces (200 iterations per block, batch_size=1).

Calibration data: 1024 self-generated traces from the BF16 source model (256 prompts × 4 generations) covering math, code, logic, analysis, creative writing, general knowledge, tool calling, and Korean.

## Files

| File | Size | Purpose |
|---|---:|---|
| `model-*.safetensors` (13 shards) | ~25 GB | Main quantized weights |
| `model_extra_tensors.safetensors` | ~1 GB | MTP head + edge-protected layers (BF16) |
| `quantization_config.json` | <1 KB | AWQ config (`quant_method=awq`, `bits=4`, `group_size=128`, `zero_point=true`) with BF16 MTP skip entries |
| `config.json` + tokenizer + processor configs | <100 MB | Standard metadata |

Total checkpoint size: **~26 GB** (down from ~54 GB BF16 source).

## License

Apache 2.0 (inherited from the base model).
