---
license: apache-2.0
base_model: mlx-community/Qwen3.6-35B-A3B-8bit
library_name: mlx
pipeline_tag: text-generation
language:
- ko
- en
tags:
- mlx
- qwen3.6
- qwen3_5_moe
- mixture-of-experts
- reap
- expert-pruning
- korean
- 8-bit
datasets:
- eouya2/KGuard-Korean-MoE-Calibration-v1
---

# Qwen3.6-35B-A3B K-Guard REAP 12.5% — MLX 8-bit

> Korean model card: [README_ko.md](./README_ko.md)

This is a Korean-oriented, expert-pruned MLX release of
[`mlx-community/Qwen3.6-35B-A3B-8bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-8bit).
It applies REAP-style router-weighted expert activation pruning to the routed
MoE experts while keeping the upstream 8-bit MLX format, top-8 routing, shared
experts, tokenizer, chat template, and non-MoE components intact.

In this release, **K-Guard** is the name of the Korean-centered calibration
profile used to collect routing and activation statistics before pruning.
There is no fine-tuning or weight retraining..

## Model summary

| Property | Value |
|---|---:|
| Base checkpoint | `mlx-community/Qwen3.6-35B-A3B-8bit` |
| Architecture | Qwen3.6 MoE (`qwen3_5_moe`) |
| MoE layers | 40 |
| Routed experts per layer | **224**, reduced from 256 |
| Experts removed per layer | 32 / 256 (**12.5%**) |
| Active routed experts per token | 8, unchanged |
| Shared expert | Preserved |
| Quantization | MLX affine 8-bit, group size 64 |
| Local checkpoint size | approximately **31.17 GiB** |
| Training after pruning | None |

## Calibration and expert selection

Expert importance was observed on a deterministic Korean-centered mixture of
24,576 sequences:

- 8,192 general Korean instruction and reasoning records
- 8,192 Korean-English paired records
- 4,096 general capability replay records
- 4,096 Qwen3.6 text and reasoning records

The observer covered all 40 MoE layers with a maximum sequence length of 8,192
tokens and seed 17. For every layer, routed experts were ranked using
router-weighted activation statistics; the 224 highest-ranked experts were
retained, the router rows were sliced to the same indices, and top-8 routing
was preserved.

The calibration file and the complete per-layer/per-expert observation CSV are
published in
[`eouya2/KGuard-Korean-MoE-Calibration-v1`](https://huggingface.co/datasets/eouya2/KGuard-Korean-MoE-Calibration-v1).

## Evaluation snapshot

The following scores use the same deterministic evaluation subsets and prompts
for the base and pruned checkpoints.

| Benchmark | Base 8-bit | This model |
|---|---:|---:|
| KMMLU | 66.4 | **64.5** |
| MMLU-Pro | 64.3 | **61.3** |
| GSM8K | 96.7 | **95.7** |
| HumanEval+ pass@1 | 90.9 | **92.1** |
| Academic 10-benchmark macro | 81.2 | **80.5** |

KMMLU, MMLU-Pro, and GSM8K use 512-item deterministic subsets. HumanEval+
uses the complete 164-task EvalPlus set. These results are intended for paired
comparison under the reported local protocols rather than as direct official
leaderboard submissions.

## Use with MLX

Install MLX LM:

```bash
pip install -U mlx-lm
```

Generate from the command line:

```bash
mlx_lm.generate \
  --model eouya2/Qwen3.6-35B-A3B-KGuard-REAP12.5-8bit-MLX \
  --prompt "한국어로 mixture-of-experts 모델을 간단히 설명해 주세요." \
  --max-tokens 256 \
  --temperature 0.0
```

Or use Python:

```python
from mlx_lm import generate, load

model_id = "eouya2/Qwen3.6-35B-A3B-KGuard-REAP12.5-8bit-MLX"
model, tokenizer = load(model_id)

messages = [{"role": "user", "content": "한국어로 자기소개를 해 주세요."}]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

print(generate(model, tokenizer, prompt=prompt, max_tokens=256))
```

Serve an OpenAI-compatible endpoint:

```bash
mlx_lm.server --model eouya2/Qwen3.6-35B-A3B-KGuard-REAP12.5-8bit-MLX
```

## Intended use

This checkpoint is suitable for local Apple Silicon experimentation, Korean
and bilingual generation, MoE pruning research, and memory-conscious inference
where a modest reduction in routed-expert capacity is useful. As with the base
model, application-specific safety and quality evaluation is recommended
before deployment.

## References and acknowledgements

- Base model: [`Qwen/Qwen3.6-35B-A3B`](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- MLX 8-bit conversion: [`mlx-community/Qwen3.6-35B-A3B-8bit`](https://huggingface.co/mlx-community/Qwen3.6-35B-A3B-8bit)
- REAP paper: [REAP the Experts: Why Pruning Prevails for One-Shot MoE Compression](https://huggingface.co/papers/2510.13999)
- MLX pruning implementation: [`egesabanci/reap-mlx`](https://github.com/egesabanci/reap-mlx)

## License

The model follows the Apache 2.0 license of the upstream Qwen release. The
companion synthetic calibration data is released separately under CC BY 4.0.
