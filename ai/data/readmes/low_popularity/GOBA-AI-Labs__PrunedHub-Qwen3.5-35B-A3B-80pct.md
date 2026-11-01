---
license: apache-2.0
library_name: gguf
base_model: Qwen/Qwen3.5-35B-A3B
tags:
  - moe
  - mixture-of-experts
  - pruned
  - expert-pruning
  - gguf
  - qwen3.5
  - deltanet
  - language-aware-pruning
  - q3_k_m
model_name: PrunedHub Qwen3.5-35B-A3B 80%
pipeline_tag: text-generation
language:
  - en
  - ja
  - zh
  - ko
  - fr
  - de
  - es
datasets:
  - openai/MMMLU
model_type: qwen35moe
quantized_by: GOBA-AI-Labs
---

# PrunedHub Qwen3.5-35B-A3B 80%: Expert Pruning for 24GB Mac

**13.67 GB** | 204/256 experts | Q3_K_M | **MMLU -1pp, GSM8K equal** | Full GPU-resident on 24GB Mac | GGUF | Apache 2.0

A pruned variant of [Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) that **fits entirely in GPU memory on a 24GB Mac** while preserving near-original quality. The official Q4_K_M (21.2 GB) requires swap; this model runs fully GPU-resident.

## Highlights

- **13.67 GB**: full GPU-resident on 24GB Apple Silicon (no swap, no SSD streaming)
- **19% smaller** than original Q3_K_M (16.80 GB), **36% smaller** than Q4_K_M (21.2 GB)
- **MMLU 80%** (-1pp from original 81%) -- near-lossless knowledge
- **GSM8K 82%** (equal to original) -- math reasoning fully preserved
- **LiveCodeBench Easy 83.1%** (142 problems, contamination-free) -- strong code generation
- **DeltaNet hybrid architecture** (75% Gated DeltaNet + 25% Full Attention)
- Compatible with **llama.cpp** (build 8140+)

## Benchmark Results

| Benchmark | Original Q3_K_M (16.80 GB) | This Model (13.67 GB) | Delta |
|-----------|---------------------------|----------------------|-------|
| **MMLU** (0-shot, 100Q, no-think) | 81% | **80%** | **-1 pp** |
| **GSM8K** (0-shot, 50Q, no-think) | 82% | **82%** | **0 pp** |
| **LCB Easy** (142Q, no-think) | 93.0% | **83.1%** | -9.9 pp |
| **HumanEval** (50Q) | 50% | 38% | -12 pp |
| **JA Quality** (20Q) | 100% | 85% | -15 pp |
| File size | 16.80 GB | **13.67 GB** | **-18.6%** |

> Note: LiveCodeBench Easy (142 competitive programming problems from LeetCode/AtCoder/Codeforces, 2024+) is the primary code benchmark. HumanEval 50Q is unreliable at this sample size -- LCB and HumanEval gave opposite conclusions for model comparisons in our testing.

## Why Not MxMoE?

We also tested Weight-80% + MxMoE (mixed quantization, 12.69 GB) but found it **damages code quality**:

| Model | Size | MMLU | LCB Easy |
|-------|------|------|----------|
| **This model (Weight-80%)** | **13.67 GB** | **80%** | **83.1%** |
| Weight-80% + MxMoE | 12.69 GB | 78% | 77.5% |

The extra 1 GB savings is not worth -5.6pp on code generation.

## Model Details

| Property | Value |
|----------|-------|
| Base model | [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) |
| Total parameters | ~35B (3B active per token) |
| Architecture | Gated DeltaNet (75%) + Full Attention (25%) with Sparse MoE |
| Layers | 40 (30 DeltaNet + 10 Full Attention) |
| Experts per layer | **204** (pruned from 256) |
| Routing | Top-8, softmax |
| Expert FFN dim | 512 (SwiGLU) |
| Shared expert | 1 per layer (FFN dim 512) |
| Hidden size | 2048 |
| Attention heads | 16 (2 KV heads, GQA) |
| Context length | 262K tokens |
| Quantization | Q3_K_M (Unsloth imatrix) |
| Pruning | Weight-based importance, 80% expert retention |
| File size | **13.67 GB** (12.73 GiB) |
| License | Apache 2.0 |

## How to Use

### With llama.cpp (recommended)

Requires llama.cpp **build 8140+** for Qwen3.5 DeltaNet support.

```bash
llama-server \
  -m PrunedHub-Qwen3.5-35B-A3B-80pct-Q3_K_M.gguf \
  --port 8090 \
  -ngl 99 \
  -c 4096
```

### With OpenAI-compatible API

Once `llama-server` is running:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8090/v1", api_key="none")

response = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "Write a Python function to find the longest palindromic substring."}],
    max_tokens=1024,
    temperature=0.7,
)
print(response.choices[0].message.content)
```

### Requirements

- **[llama.cpp](https://github.com/ggerganov/llama.cpp)** build 8140+ (for Qwen3.5 / DeltaNet support)
- **24 GB RAM** for full GPU-resident inference (model uses ~13.7 GB; rest for KV cache)
- Apple Silicon (Metal) recommended; CUDA also supported

## Compression Methodology

### Weight-Based Expert Pruning (80% Keep)

Each expert is scored using weight magnitude importance -- the L2 norm of the expert's FFN weight matrices:

```
importance(layer, expert) = ||gate_weight||_F + ||up_weight||_F + ||down_weight||_F
```

The bottom 20% of experts per layer are removed (256 -> 204 experts/layer). Weight-based scoring outperformed activation-based calibration for this model:

| Method | MMLU | GSM8K | Notes |
|--------|------|-------|-------|
| **Weight-based (this model)** | **80%** | **82%** | Weight magnitude captures full training data |
| Activation calibration | 78% | 78% | 55 prompts insufficient for 256 experts |
| Union (weight + activation) | 78% | 80% | No improvement over weight-only |

### Why Weight-Based Wins for 256 Experts

With 256 experts per layer, activation-based calibration (55 prompts x 32 tokens) cannot adequately cover all experts. Weight magnitude, which encodes information from the full training data, provides a more reliable importance signal. This is consistent with findings that weight-based pruning dominates for high expert-count models.

### Size Breakdown

```
Original Q4_K_M:      21.20 GB (256 experts x 40 layers)
Original Q3_K_M:      16.80 GB (256 experts x 40 layers)
After 80% pruning:    13.67 GB (204 experts x 40 layers, Q3_K_M)
Total reduction:      -18.6% (from Q3_K_M), -35.5% (from Q4_K_M)
```

## Pruning Curve (Qwen3.5-35B-A3B)

| Keep % | Experts/Layer | MMLU | Notes |
|--------|---------------|------|-------|
| 100% (original Q3_K_M) | 256 | 81% | Baseline |
| 90% | 230 | 79% | Minor loss |
| **80% (this model)** | **204** | **80%** | **Best tradeoff** |
| 70% | 179 | ~65% | Quality cliff |

## Qwen3.5-35B-A3B vs Qwen3.5-27B (Dense)

The Dense 27B model outperforms the MoE 35B-A3B on many benchmarks, but at 9x inference cost:

| Metric | 35B-A3B (MoE) | 27B (Dense) |
|--------|---------------|-------------|
| MMLU-Pro | 85.3 | 86.1 |
| LiveCodeBench v6 | 74.6 | **80.7** |
| Active params | **3B** | 27B |
| Inference cost | **1x** | **9x** |

MoE's value is cost efficiency: 3B active parameters achieve 85-93% of the Dense 27B's quality. And only MoE models can be further compressed via expert pruning.

## Limitations

- **Japanese quality**: -15pp (100% -> 85%) due to pruning of some language-specialized experts. Expert Tuning could recover this
- **Code generation**: -9.9pp on LiveCodeBench Easy. Trade-off for 19% size reduction
- **No post-pruning training**: Pruned without fine-tuning. Quality could be improved with expert tuning
- **llama.cpp 8140+ required**: Older builds do not support Qwen3.5 / DeltaNet architecture

## Related Models

| Model | Size | MMLU | Notes |
|-------|------|------|-------|
| [PrunedHub-GPT-OSS-20B-28x](https://huggingface.co/GOBA-AI-Labs/PrunedHub-GPT-OSS-20B-28x) | 10.4 GB | 78% | Lossless pruning, GPU-resident on 16GB |
| [PrunedHub-Qwen3-30B-A3B-EN-MxMoE](https://huggingface.co/GOBA-AI-Labs/PrunedHub-Qwen3-30B-A3B-EN-80pct-MxMoE) | 13.5 GB | 70% | EN-optimized, mixed quantization |
| [PrunedHub-Qwen3-30B-A3B-JP-MxMoE](https://huggingface.co/GOBA-AI-Labs/PrunedHub-Qwen3-30B-A3B-JP-80pct-MxMoE) | 13.5 GB | 73% | JP-optimized, mixed quantization |
| **This model** | **13.67 GB** | **80%** | **Qwen3.5, best quality-per-GB** |

## Citation

```bibtex
@misc{goba2026qwen35prune,
  title   = {Weight-Based Expert Pruning for Qwen3.5-35B-A3B},
  author  = {GOBA-AI-Labs},
  year    = {2026},
  url     = {https://huggingface.co/GOBA-AI-Labs/PrunedHub-Qwen3.5-35B-A3B-80pct},
  note    = {80\% expert retention achieves 19\% size reduction with MMLU -1pp on 256-expert DeltaNet MoE}
}
```

## Acknowledgments

- [Qwen Team](https://huggingface.co/Qwen) for releasing Qwen3.5-35B-A3B under Apache 2.0
- [Unsloth](https://github.com/unslothai/unsloth) for the Q3_K_M quantization with imatrix
- [llama.cpp](https://github.com/ggerganov/llama.cpp) for DeltaNet support and GGUF format

## License

This model inherits the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) from the base model ([Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B)).
