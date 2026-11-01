---
license: apache-2.0
language:
- en
- zh
- ja
- ko
- fr
- de
- es
- pt
- ru
- ar
- th
- vi
tags:
- qwen3_5_moe
- autoround
- gptq
- int4
- quantization
- uncensored
- heretic
- abliterated
- moe
- code
- reasoning
- vision
base_model: trohrbaugh/Qwen3.5-397B-A17B-heretic
pipeline_tag: text-generation
---

# Qwen3.5-397B-A17B-heretic-int4-AutoRound

**The first INT4 AutoRound quantization of the Heretic (uncensored) Qwen3.5-397B — the largest open-source abliterated model.**

A 4-bit symmetric quantization of [trohrbaugh/Qwen3.5-397B-A17B-heretic](https://huggingface.co/trohrbaugh/Qwen3.5-397B-A17B-heretic), generated using [Intel AutoRound](https://github.com/intel/auto-round) v0.12.0. The original multimodal architecture (`Qwen3_5MoeForConditionalGeneration`) is fully preserved — text, vision, video, and reasoning all work.

| | |
|---|---|
| **Base Model** | [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) → [trohrbaugh/Qwen3.5-397B-A17B-heretic](https://huggingface.co/trohrbaugh/Qwen3.5-397B-A17B-heretic) |
| **Quantization** | INT4 symmetric, group_size 128, AutoRound (sign-gradient descent) |
| **Packing** | `auto_round:auto_gptq` (GPTQ Marlin compatible) |
| **Size on Disk** | **198 GB** (vs ~800 GB BF16 original — 75% smaller) |
| **Format** | 40 safetensors shards |
| **Architecture** | 397B total params, 17B active/token (512 experts, 16 routed + 1 shared) |
| **Context** | 262,144 tokens natively (tested to 262K in production) |
| **Capabilities** | Text, Code, Reasoning, Tool Calling, Vision, Video |
| **License** | Apache 2.0 (inherited from Qwen) |

---

## Model Lineage

This model has a three-step provenance chain:

```
Qwen/Qwen3.5-397B-A17B            ← Qwen team's 397B MoE frontier model (BF16, ~800GB)
  └─► trohrbaugh/heretic           ← Abliterated with Heretic v1.2.0
       └─► THIS MODEL              ← INT4 AutoRound quantization (198GB, vision preserved)
```

1. **[Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)** — Qwen team's largest Mixture-of-Experts model with Gated DeltaNet hybrid attention, 512 experts (16 active + 1 shared per token), native 262K context, and multimodal vision support.

2. **[trohrbaugh/Qwen3.5-397B-A17B-heretic](https://huggingface.co/trohrbaugh/Qwen3.5-397B-A17B-heretic)** — Abliterated (uncensored) variant using [Heretic](https://github.com/p-e-w/heretic) by [p-e-w](https://github.com/p-e-w). Uses parametrized directional ablation applied to `attn.o_proj` and `mlp.down_proj` across all layers.

3. **This model** — INT4 AutoRound quantization targeting unified-memory GPU systems (NVIDIA DGX Spark / ASUS Ascent GX10). All vision weights, shared expert layers, MoE gate layers, and lm_head preserved at full precision. Text module quantized to INT4 W4G128.

---

## Quantization Details

| Parameter | Value |
|:----------|:------|
| **Method** | [Intel AutoRound](https://github.com/intel/auto-round) v0.12.0 (sign-gradient descent) |
| **Bits** | 4 (INT4) |
| **Group Size** | 128 |
| **Symmetric** | Yes |
| **Packing** | `auto_round:auto_gptq` (GPTQ Marlin backend in vLLM) |
| **Block Quantized** | `model.language_model.layers` (text module only) |

### What Was Preserved (NOT Quantized)

Keeping critical layers at full precision is essential for MoE model quality:

- **Vision encoder weights** (`model.visual.blocks.*`) — BF16
- **Shared expert projections** (layers × `gate_proj`, `up_proj`, `down_proj`) — FP16
- **Shared expert gates** (`shared_expert_gate`) — FP16
- **MoE routing gates** — FP16
- **lm_head** — original precision

The shared expert is activated for *every* token (unlike the 511 routed experts where only 16 fire per token). Preserving its precision is critical for maintaining output quality.

---

## Model Size Comparison

| Variant | Size on Disk | In Memory | Reduction |
|:--------|:----------:|:--------:|:---------:|
| Qwen3.5-397B-A17B (BF16) | ~800 GB | ~800 GB | — |
| Intel/Qwen3.5-397B-A17B-int4-AutoRound (canonical) | 211 GB | ~196.65 GiB | 74% |
| **This model (Heretic INT4)** | **198 GB** | **~195.60 GiB** | **75%** |

> The 13 GB difference from Intel's canonical INT4 is because the Heretic fork does not include MTP (Multi-Token Prediction) weights. MTP is a speculative decoding feature — its absence does not affect output quality.

---

## Performance (Measured on DGX Spark Cluster)

Tested on a 2-node NVIDIA DGX Spark cluster (2× Grace Blackwell GB10, 128GB unified memory each) with tensor parallelism over 200Gbps RoCE RDMA. Deployment configuration heavily informed by the [spark-vllm-docker](https://github.com/eugr/spark-vllm-docker) community project and the [NVIDIA DGX Spark Developer Forum](https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719).

| Metric | Value |
|:-------|:------|
| **Decode Speed** | 27.3–27.4 tok/s (single user) |
| **Context Window** | 262,144 tokens (262K, full native window) |
| **KV Cache** | 9.41 GiB fp8, 267,264 tokens capacity |
| **GPU Memory** | 112 GiB absolute per node (via `--gpu-memory-utilization-gb 112`) |
| **Model Weights** | ~98.2 GiB per node (TP=2 sharded) |
| **CUDA Graphs** | Enabled (saves 0.21 GiB vs eager mode) |
| **Thinking Mode** | Toggleable (`/think` and `/no_think`) |
| **Tool Calling** | Working (Hermes parser) |
| **Startup Time** | ~16.5 min cold, ~8 min with AOT cache |

### Speed: 43% Faster Than Canonical

| Model | tok/s | TTFT | Wall Time (coding task) |
|:------|:-----:|:----:|:----------------------:|
| **This model (Heretic INT4)** | **27.3** | 5.6s | 309s (5.2 min) |
| Intel/canonical INT4 | 19.0 | 0.87s | 496s (8.3 min) |

The Heretic is significantly faster than the canonical quantization on identical hardware. The speed gain likely comes from the smaller memory footprint (no MTP weights) reducing memory pressure.

> **Note:** TTFT is higher on the Heretic (5.6s vs 0.87s) because this was measured during a thinking-disabled coding evaluation with a longer system prompt. Single-request TTFT with short prompts is comparable.

---

## Coding Benchmark — Full-Stack Evaluation

We ran an identical full-stack coding evaluation across all models: "Build a task manager with Bun, Hono, React, PostgreSQL, Drizzle ORM."

### Results

| Model | Thinking | tok/s | Files | Hard Blockers | Score |
|:------|:--------:|:-----:|:-----:|:-------------:|:-----:|
| Flagship (canonical 397B) | No | 19.0 | 22 | **1** | **6.85** |
| Flagship (canonical 397B) | Yes | 26.7 | 26 | ~2–3 | **7.15** |
| **Heretic (this model)** | **No** | **27.3** | **20** | **4–5** | **6.55** |
| **Heretic (this model)** | **Yes** | **27.4** | **18** | **7** | **4.80** |
| Heretic (122B) | Yes | 26.7 | 47 | 9 | ~5.5 |
| Claude Sonnet 4 (cloud) | — | 104.5 | 37 | 3 | ~7.5 |

### Key Finding: Do NOT Use Thinking Mode

**Thinking mode HURTS this model's code quality:**

| Metric | No Thinking | With Thinking | Impact |
|:-------|:----------:|:-------------:|:------:|
| Score | 6.55/10 | 4.80/10 | **-27%** |
| Hard blockers | 4–5 | 7 | Worse |
| Auth security | bcrypt + httpOnly | **Plaintext passwords** | Critical |
| Files produced | 20 | 18 | Fewer |
| TTFT | 5.6s | 63.0s | 11× slower |

This is the **opposite** of the canonical model, where thinking helps (+4%). The abliteration appears to weaken the reasoning-to-execution pipeline — the model's thinking layer notes best practices (e.g., "usually use bcrypt") but then doesn't implement them.

**Recommendation:** Always use `"chat_template_kwargs": {"enable_thinking": false}` with this model for code generation.

### Without Thinking: Close to Canonical Quality

When thinking is disabled, the quality gap is small:

| Aspect | Heretic (no think) | Canonical (no think) |
|:-------|:------------------:|:--------------------:|
| Score | 6.55 | 6.85 |
| Auth pattern | bcrypt + httpOnly cookies | jose JWT (modern but no hash) |
| Task ownership | Checks userId | No ownership checks |
| Architecture | Clean monorepo | Clean monorepo |
| Self-correction | No | Yes (caught wrong import) |
| Hard blockers | 4–5 | 1 |

The Heretic actually implements **better auth security** (bcrypt + httpOnly + ownership checks) — the canonical model used jose JWT without password hashing. The Heretic's extra hard blockers are mostly import/config issues rather than architectural flaws.

---

## Quick Start

### vLLM (Recommended)

For a **single multi-GPU server** with enough VRAM (e.g., 2×H100 80GB, 4×A100 80GB):

```bash
pip install vllm>=0.17.0

vllm serve happypatrick/Qwen3.5-397B-A17B-heretic-int4-AutoRound \
  --served-model-name qwen3.5-397b \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 2 \
  --max-model-len 65536 \
  --kv-cache-dtype fp8 \
  --language-model-only \
  --enable-auto-tool-choice \
  --tool-call-parser hermes \
  --chat-template-kwargs '{"enable_thinking": false}' \
  --trust-remote-code
```

> **Important:** Use `--language-model-only` to skip loading the vision encoder if you only need text/code. Adjust `--tensor-parallel-size` and `--max-model-len` for your hardware.

Then query with any OpenAI-compatible client:

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3.5-397b",
    "messages": [{"role": "user", "content": "Write a Python quicksort implementation"}],
    "temperature": 0.6
  }'
```

### HuggingFace Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "happypatrick/Qwen3.5-397B-A17B-heretic-int4-AutoRound"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Hello!"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

---

## DGX Spark / ASUS Ascent GX10 Deployment Guide

This model requires a **dual-node** DGX Spark cluster (2× 128GB unified memory). It does NOT fit on a single DGX Spark.

Our deployment relies heavily on the [spark-vllm-docker](https://github.com/eugr/spark-vllm-docker) community project by eugr, which provides pre-built vLLM + FlashInfer wheels for SM12.1a (the GB10's compute capability). Additional deployment insights came from [JungkwanBan's archived recipe](https://github.com/JungkwanBan) (now merged into spark-vllm-docker) and the [NVIDIA DGX Spark Developer Forum](https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719).

### Dual Node (2× DGX Spark, 256 GB Total)

For two DGX Sparks connected via 200Gbps RoCE RDMA, using **native distributed mode** (no Ray — lower memory overhead):

```bash
# Node 2 (worker, rank 1) — start first, waits for head
docker run -d --name vllm-worker \
  --gpus all --network=host --ipc=host --privileged \
  --shm-size 10.24g \
  -v /path/to/models:/models \
  -e NCCL_SOCKET_IFNAME=enP2p1s0f0np0 \
  -e NCCL_IB_HCA=roceP2p1s0f0 \
  -e NCCL_P2P_DISABLE=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -e VLLM_MARLIN_USE_ATOMIC_ADD=1 \
  -e OMP_NUM_THREADS=4 -e MKL_NUM_THREADS=4 -e TORCH_NUM_THREADS=4 \
  <vllm-image> \
  bash -c "vllm serve /models/heretic-397b-int4-autoround \
    --host 0.0.0.0 --port 8000 \
    --tensor-parallel-size 2 \
    --max-model-len 262144 \
    --max-num-seqs 2 \
    --max-num-batched-tokens 4176 \
    --gpu-memory-utilization-gb 112 \
    --kv-cache-dtype fp8 \
    --enable-prefix-caching \
    --trust-remote-code \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3 \
    --chat-template unsloth.jinja \
    --nnodes 2 --node-rank 1 \
    --master-addr <NODE1_IP> --master-port 29500 \
    --headless"

sleep 5

# Node 1 (head, rank 0) — triggers model loading
docker run -d --name vllm-head \
  --gpus all --network=host --ipc=host --privileged \
  --shm-size 10.24g \
  -v /path/to/models:/models \
  -e NCCL_SOCKET_IFNAME=enP2p1s0f0np0 \
  -e NCCL_IB_HCA=roceP2p1s0f0 \
  -e NCCL_P2P_DISABLE=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -e VLLM_MARLIN_USE_ATOMIC_ADD=1 \
  -e OMP_NUM_THREADS=4 -e MKL_NUM_THREADS=4 -e TORCH_NUM_THREADS=4 \
  <vllm-image> \
  bash -c "vllm serve /models/heretic-397b-int4-autoround \
    --served-model-name qwen3.5-397b \
    --host 0.0.0.0 --port 8000 \
    --tensor-parallel-size 2 \
    --max-model-len 262144 \
    --max-num-seqs 2 \
    --max-num-batched-tokens 4176 \
    --gpu-memory-utilization-gb 112 \
    --kv-cache-dtype fp8 \
    --enable-prefix-caching \
    --trust-remote-code \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3 \
    --chat-template unsloth.jinja \
    --nnodes 2 --node-rank 0 \
    --master-addr <NODE1_IP> --master-port 29500"
```

> **Note on `<vllm-image>`**: Standard `vllm/vllm-openai` does not ship FlashInfer kernels for SM12.1a (GB10). Use [spark-vllm-docker](https://github.com/eugr/spark-vllm-docker) `vllm-node-tf5` image or build your own. Our tested configuration uses vLLM 0.18.1rc1.dev69 + FlashInfer 0.6.7.

### DGX Spark Tips & Gotchas

These are hard-won lessons from our deployment and the community:

- **`--gpu-memory-utilization-gb 112`** — absolute GiB allocation, NOT a percentage. This is the maximum for ASUS Ascent UMA systems. Requires patching vLLM's `request_memory()` safety margin check from `raise ValueError` to `logging.warning` — `cudaMemGetInfo.free` underreports by 3–4 GiB because reclaimable page cache is counted as "used"
- **`--shm-size 10.24g`** is critical for multi-node — without it, model loading can hang at ~57% (NCCL deadlock)
- **Do NOT use `--enforce-eager`** — CUDA graphs on GB10 with driver 580 actually **save** 0.21 GiB of memory. The myth that `--enforce-eager` is required for native distributed is false (confirmed by JungkwanBan's testing and our own)
- **`NCCL_P2P_DISABLE=1`** is required for GB10's unified memory architecture — P2P transfers hang
- **`--kv-cache-dtype fp8`** is essential — the 397B model needs all available memory, fp8 halves KV cache size. Results in 9.41 GiB for 267,264 tokens capacity
- **`--language-model-only`** saves ~3GB by not loading the vision encoder (optional — omit if you need vision)
- **`--enable-prefix-caching`** — free memory savings via KV cache reuse for shared prefixes
- **Disable the desktop GUI** (`sudo systemctl set-default multi-user.target`) — the GNOME compositor contends with Marlin weight repacking and wastes 400–500 MiB per node. See the [NVIDIA forum thread](https://forums.developer.nvidia.com/t/qwen3-5-397b-a17b-run-in-dual-spark-but-i-have-a-concern/361967)
- Set **`vm.swappiness=10`** at the OS level — reduces swapping of GPU-mapped pages
- **Thread-limiting env vars** (`OMP_NUM_THREADS=4`, `MKL_NUM_THREADS=4`, `TORCH_NUM_THREADS=4`) — community-recommended for GB10 to avoid oversubscribing the Grace CPU cores during model loading
- **Drop page caches** before launching vllm serve — `sync; echo 3 > /proc/sys/vm/drop_caches` inside both containers recovers reclaimable memory
- Model startup takes **~16.5 minutes** cold (weight loading + torch.compile + FlashInfer autotuning + CUDA graph capture). **~8 minutes** with AOT cache on subsequent launches

### Post-Quantization Fixes Applied

This model required several fixes after the initial AutoRound quantization to work correctly with vLLM:

1. **`config.json`** — Fixed `block_name_to_quantize` from `["model.language_model.layers", "model.visual.blocks"]` to `"model.language_model.layers"` (string, not array). The original told vLLM to create quantized Marlin layers for the vision encoder, causing a `MarlinLinearKernel` crash because the vision embed_dim (1152) ÷ TP(2) = 576, which is not divisible by `min_thread_k` (128). Also fixed `extra_config` key prefix from `""` to `"model.language_model."`
2. **`quantization_config.json`** — Replaced with Intel's reference file (the AutoRound output was incomplete)
3. **Shard 39** — Merged 333 visual encoder keys from `model_extra_tensors.safetensors` into `model-00039-of-00040.safetensors` (vLLM ignores extra tensors files)
4. **`processor_config.json`** — Added (required for multimodal model loading)
5. **`model.safetensors.index.json`** — Updated weight map to reflect the merged shard and removed references to `model_extra_tensors.safetensors`

These fixes are documented in detail in our [397B deployment log](https://github.com/dizyx/nockerl-local-models).

---

## Abliteration Notice

This model is based on a "Heretic" variant which has had **safety refusals significantly reduced** using directional ablation ([Heretic](https://github.com/p-e-w/heretic) by [p-e-w](https://github.com/p-e-w)).

**This model will follow instructions that the original Qwen model would refuse.** Please use responsibly. The creators are not responsible for misuse.

---

## Ethical Considerations and Limitations

- This is an **uncensored** model. It has reduced safety guardrails compared to the original Qwen3.5-397B-A17B.
- Quantization to INT4 introduces a small quality degradation compared to BF16, though our testing shows close-to-canonical performance on code generation tasks (6.55 vs 6.85/10).
- **Do not use thinking mode for code generation.** It significantly degrades output quality on this model (4.80/10 with thinking vs 6.55/10 without).
- The model may generate biased, incorrect, or harmful content. Users should implement appropriate safety measures.

---

## License

This model inherits the **Apache 2.0** license from [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B/blob/main/LICENSE).

---

## Acknowledgments

- **[Qwen Team](https://huggingface.co/Qwen)** for the incredible Qwen3.5-397B-A17B base model
- **[trohrbaugh](https://huggingface.co/trohrbaugh)** for the Heretic abliteration
- **[p-e-w](https://github.com/p-e-w)** for the [Heretic](https://github.com/p-e-w/heretic) abliteration tool
- **[Intel](https://github.com/intel/auto-round)** for AutoRound and the canonical quantization recipe
- **[eugr](https://github.com/eugr/spark-vllm-docker)** for the spark-vllm-docker community project — pre-built vLLM + FlashInfer wheels for SM12.1a and tested deployment recipes
- **[JungkwanBan](https://github.com/JungkwanBan)** for proving CUDA graphs work on GB10 with driver 580 (saves memory vs eager mode)
- **[NVIDIA DGX Spark Developer Forum](https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719)** — community knowledge on UMA memory management, GUI deadlocks, and multi-node deployment
- **NVIDIA** for the DGX Spark platform

---

## Citation

```bibtex
@article{cheng2024optimize,
  title={Optimize Weight Rounding via Signed Gradient Descent for the Quantization of LLMs},
  author={Cheng, Wenhua and Zhang, Weiwei and Shen, Haihao and Cai, Yiyang and He, Xin and Lv, Kaokao and Liu, Yi},
  journal={arXiv preprint arXiv:2309.05516},
  year={2024}
}

@misc{qwen3.5,
  title={Qwen3.5 Technical Report},
  author={Qwen Team},
  year={2025},
  url={https://qwenlm.github.io/blog/qwen3.5/}
}
```

---

*Quantized by trohrbaugh. Post-quantization fixes and benchmarks by [happypatrick](https://huggingface.co/happypatrick). Tested on a 2-node DGX Spark cluster with 200Gbps RoCE RDMA. Deployment informed by the [spark-vllm-docker](https://github.com/eugr/spark-vllm-docker) community project and the [NVIDIA DGX Spark Developer Forum](https://forums.developer.nvidia.com/c/accelerated-computing/dgx-spark-gb10/719).*
