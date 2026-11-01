---
license: apache-2.0
base_model:
  - FINAL-Bench/Darwin-35B-A3B-Opus
tags:
  - llama-cpp
  - gguf
  - quantized
  - Q8_0
  - merge
  - evolutionary-merge
  - darwin
  - darwin-v5
  - reasoning
  - qwen3.5
  - qwen
  - moe
  - mixture-of-experts
  - claude-opus
  - distillation
  - multilingual
  - gpqa
  - open-source
  - apache-2.0
  - layer-wise-merge
  - coding-agent
  - tool-calling
  - long-context
  - 262k-context
language:
  - en
  - zh
  - ko
  - ja
  - de
  - fr
  - es
  - ru
  - ar
  - multilingual
pipeline_tag: text-generation
library_name: gguf
quantized_by: VIDRAFT
model-index:
  - name: Darwin-35B-A3B-Opus-Q8_0-GGUF
    results:
      - task:
          type: text-generation
          name: Graduate-Level Reasoning
        dataset:
          type: Idavidrein/gpqa
          name: GPQA Diamond
          config: gpqa_diamond
          split: train
        metrics:
          - type: accuracy
            value: 90.0
            name: Accuracy
            verified: false
      - task:
          type: text-generation
          name: Multilingual Knowledge
        dataset:
          type: openai/MMMLU
          name: MMMLU
        metrics:
          - type: accuracy
            value: 85.0
            name: Accuracy
            verified: false
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# Darwin-35B-A3B-Opus-Q8_0-GGUF

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Opus"><img src="https://img.shields.io/badge/🧬_Gen1-Darwin--4B--Opus-blue?style=for-the-badge" alt="Gen1"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-David"><img src="https://img.shields.io/badge/🧬_Gen2-Darwin--4B--David-blue?style=for-the-badge" alt="Gen2"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis"><img src="https://img.shields.io/badge/⭐_Gen3-Darwin--4B--Genesis-gold?style=for-the-badge" alt="Gen3"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--9B--Opus-blue?style=for-the-badge" alt="9B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-9B-Opus"><img src="https://img.shields.io/badge/🚀_Space-9B_Demo-purple?style=for-the-badge" alt="9B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--31B--Opus-blue?style=for-the-badge" alt="31B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-31B-Opus"><img src="https://img.shields.io/badge/🚀_Space-31B_Demo-purple?style=for-the-badge" alt="31B Space"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🧬_Model-Darwin--35B--A3B--Opus-blue?style=for-the-badge" alt="35B"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/Darwin-35B-A3B-Opus"><img src="https://img.shields.io/badge/🚀_Space-35B_Demo-purple?style=for-the-badge" alt="35B Space"></a>
  <a href="https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-Q8--Official-yellow?style=for-the-badge" alt="Q8 GGUF"></a>
  <a href="https://huggingface.co/bartowski/FINAL-Bench_Darwin-35B-A3B-Opus-GGUF"><img src="https://img.shields.io/badge/📦_GGUF-bartowski-yellow?style=for-the-badge" alt="bartowski GGUF"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/spaces/FINAL-Bench/Leaderboard"><img src="https://img.shields.io/badge/🏆_FINAL_Bench-Leaderboard-green?style=for-the-badge" alt="FINAL Bench"></a>
  <a href="https://huggingface.co/spaces/FINAL-Bench/all-bench-leaderboard"><img src="https://img.shields.io/badge/📊_ALL_Bench-Leaderboard-orange?style=for-the-badge" alt="ALL Bench"></a>
</p>

> Q8_0 GGUF of Darwin-35B-A3B-Opus | ~37GB (3 shards) | GPQA Diamond 90.0% | Near-lossless quality | MoE 35B (3B active) | 201 Languages | 262K Context | Apache 2.0

---

## About This Quantization

Q8_0 GGUF of [`FINAL-Bench/Darwin-35B-A3B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus).

| | Original (BF16) | This Model (Q8_0 GGUF) |
|---|---|---|
| Format | SafeTensors | GGUF |
| Size | 65.5 GB | ~37 GB (3 shards) |
| Quality | Baseline | Near-lossless (~99.9% of BF16) |
| VRAM Required | 65+ GB | ~37 GB |
| Runs on | H100, A100 80GB | A100 40GB, Mac 64GB, 2x RTX 4090 |
| Framework | Transformers, vLLM, SGLang | llama.cpp, Ollama, LM Studio |

---

## Files

| File | Size | Description |
|---|---|---|
| `darwin-35b-a3b-opus-q8_0-00001-of-00003.gguf` | ~13.6 GB | Shard 1 of 3 |
| `darwin-35b-a3b-opus-q8_0-00002-of-00003.gguf` | ~12.5 GB | Shard 2 of 3 |
| `darwin-35b-a3b-opus-q8_0-00003-of-00003.gguf` | ~10.7 GB | Shard 3 of 3 |
| Total | ~36.8 GB | All 3 shards required |

> Download all 3 shard files. llama.cpp and Ollama will automatically load them together.

---

## Hardware Requirements

| Setup | Memory | Status |
|---|---|---|
| NVIDIA A100 40GB | 40 GB VRAM | Fits |
| NVIDIA A100 80GB | 80 GB VRAM | Comfortable |
| NVIDIA H100 93GB | 93 GB VRAM | Comfortable |
| 2x RTX 4090 (24GB each) | 48 GB VRAM | With tensor parallel |
| Mac Studio M2/M3 Ultra 64GB | 64 GB Unified | Fits |
| Mac M3 Max 48GB | 48 GB Unified | Fits |
| Single RTX 4090 24GB | 24 GB VRAM | Insufficient (use Q4_K_M) |

> As a MoE model, only 3B parameters are active per token. Inference is fast despite the 37GB model size.

---

## Usage

### llama.cpp (CLI)

```bash
llama-cli \
  --hf-repo FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF \
  --hf-file darwin-35b-a3b-opus-q8_0-00001-of-00003.gguf \
  -p "The meaning to life and the universe is" \
  -n 512 -ngl 99
```

### llama.cpp (Server)

```bash
llama-server \
  --hf-repo FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF \
  --hf-file darwin-35b-a3b-opus-q8_0-00001-of-00003.gguf \
  -c 32768 -ngl 99
```

### Ollama

```bash
echo 'FROM ./darwin-35b-a3b-opus-q8_0-00001-of-00003.gguf' > Modelfile
ollama create darwin-opus -f Modelfile
ollama run darwin-opus
```

### LM Studio

1. Download all 3 `.gguf` shard files
2. Place them in the same folder
3. Open LM Studio, load the first shard
4. LM Studio auto-detects and loads all shards

### MoE Expert Offload (Limited VRAM)

```bash
llama-cli \
  --hf-repo FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF \
  --hf-file darwin-35b-a3b-opus-q8_0-00001-of-00003.gguf \
  -ot ".ffn_.*_exps.=CPU" \
  -ngl 99 -c 32768
```

---

## Benchmark Results (Original Model)

Q8_0 preserves near-identical performance to BF16.

GPQA Diamond (198 Questions, Graduate-Level Reasoning)

| Model | Accuracy |
|---|---|
| Darwin-35B-A3B-Opus | 90.0% |
| Mother (Jackrong Claude 4.6 Opus Distilled) | 85.0% |
| Father (Qwen3.5-35B-A3B Official) | 84.2% |

MMMLU (Multilingual Knowledge, 29 Languages)

| Model | Accuracy |
|---|---|
| Darwin-35B-A3B-Opus | 85.0% |
| Father (Qwen3.5-35B-A3B Official) | 85.2% |

---

## How Darwin Was Created

Darwin-35B-A3B-Opus was created using Darwin V5, a diagnostic-guided evolutionary merge engine built on [mergekit](https://github.com/arcee-ai/mergekit).

Both parent models share the identical Qwen3.5-35B-A3B architecture. The Mother is a LoRA SFT on the same base — not a different architecture.

Darwin V5 adds three phases over standard mergekit evolve:
1. Pre-merge parent profiling (40 layers x 256 experts: activation frequency, routing entropy, probe cosine distance)
2. Evolution with diagnostic-informed initial population and constrained search space
3. Post-merge child validation (layer-by-layer comparison against both parents)

Key diagnostic finding: Mother had 50-65% dead experts (activation < 5%) from text-only LoRA SFT. Darwin compensated by reducing Mother density and using Father's living experts to fill inactive slots.

Merge configuration:
```yaml
# Method: DARE-TIES via mergekit
L0-L37:  t=0.5988 (Mother 60%) — router from Mother
L38:     t=0.9000 (Mother 90%) — reasoning core (peak probe cosine distance)
L39:     t=0.5336 (Father 47%) — router from Father (output routing)
```

For full technical details, diagnostics, and health check results, see the [original model card](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus).

---

## Other Quantizations

| Quantization | Size | Quality | Use Case |
|---|---|---|---|
| Q8_0 (this) | ~37 GB | Near-lossless | Maximum quality |
| Q4_K_M (coming soon) | ~20 GB | Good | RTX 4090, Mac 32GB |

---

## Model Specifications

| | |
|---|---|
| Base Model | [FINAL-Bench/Darwin-35B-A3B-Opus](https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus) |
| Architecture | Qwen3.5 MoE (Gated DeltaNet + MoE) |
| Total Parameters | 35B |
| Active Parameters | 3B per forward pass |
| Experts | 256 (8 routed + 1 shared active) |
| Context Length | 262,144 native |
| Languages | 201 |
| Quantization | Q8_0 (8-bit integer) |
| GGUF Shards | 3 files |
| License | Apache 2.0 |
| Quantized by | VIDRAFT via llama.cpp |

---

## Acknowledgements

- Korean Government — GPU Support Program research grant
- [Qwen Team](https://huggingface.co/Qwen) — Qwen3.5-35B-A3B base architecture
- [Jackrong](https://huggingface.co/Jackrong) — Claude 4.6 Opus Reasoning Distilled model
- [mergekit](https://github.com/arcee-ai/mergekit) — Merge backend infrastructure
- [llama.cpp](https://github.com/ggml-org/llama.cpp) — GGUF conversion and quantization

---

## Citation

```bibtex
@misc{vidraft_darwin_35b_opus_gguf,
  title        = {Darwin-35B-A3B-Opus-Q8_0-GGUF},
  author       = {VIDRAFT},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/FINAL-Bench/Darwin-35B-A3B-Opus-Q8-GGUF}}
}
```

This model is introduced in [Darwin Family](https://arxiv.org/abs/2605.14386).