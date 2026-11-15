---
license: apache-2.0
base_model: KRAFTON/Raon-1-mini-preview
base_model_relation: quantized
library_name: vllm
pipeline_tag: text-generation
language:
- ko
- en
tags:
- raon
- moe
- modelopt_fp4
- nvfp4
- w4a4
- awq
- modelopt
- gb10
---

# tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM

> [!IMPORTANT]
> **Target Hardware: NVIDIA GB10 (DGX Spark, sm_121)**
> 
> * **Model Lineage**: [`KRAFTON/Raon-1-mini-preview`](https://huggingface.co/KRAFTON/Raon-1-mini-preview) (Base) ➔ **`tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM`** (4-bit AWQ NVFP4)
> * **Required Serving Engine**: This model requires our customized vLLM engine targeting GB10 Blackwell hardware:  
>   👉 **[tayaee/raon-vllm-spark (branch: gb10-support)](https://github.com/tayaee/raon-vllm-spark/tree/gb10-support)**
> * **Notice for Non-GB10 Users**: This checkpoint is stored in `modelopt_fp4` format and is optimized strictly for GB10. If you are using other hardware (e.g., B300, H100, RTX 4090), standard `transformers` or stock `vLLM` will **not** load this checkpoint. Please use the official base model [`KRAFTON/Raon-1-mini-preview`](https://huggingface.co/KRAFTON/Raon-1-mini-preview) instead.

> [!WARNING]
> **This checkpoint fails the quality bar** — it is published for experimentation, not for production use. Measured on the GB10 vLLM fork:
> - GSM8K accuracy 0.170 vs base 0.945 (allowed drop ≤ 0.02)
> - KMMLU accuracy 0.300 vs base 0.565 (allowed drop ≤ 0.03)
> The weights load and respond, but the answers are far below the base model.
> For production use, pick the base model [`KRAFTON/Raon-1-mini-preview`](https://huggingface.co/KRAFTON/Raon-1-mini-preview) or one of the
> checkpoints that passes the same gate.

This is a **tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM** quantized version of `KRAFTON/Raon-1-mini-preview`, targeting DGX Spark GB10.
Weights are NVFP4 (E2M1) with per-block scales, and activations are dynamically scaled to FP8 at inference time; normalization, attention, the MoE router, the shared experts and the LM head stay in BF16.
The checkpoint is stored in the `modelopt_fp4` format, which `transformers` cannot read —
serve it with the vLLM fork (see **Usage - vLLM** below).

## Quantization spec

| Item | Value |
| --- | --- |
| Base model | `KRAFTON/Raon-1-mini-preview` |
| Base revision | `da4cf162c8613993f2189ebb438a5f9a23f3e5ca` |
| Quantization algorithm | NVFP4 (AWQ Lite, ModelOpt) |
| Weight precision | W4A4 (FP8 dynamic activation scale) |
| Bit width | NVFP4 (E2M1) |
| Group size | block_size=16 |
| Layers left unquantized | `lm_head`, `embed_tokens`, the dense layer 0, `self_attn`, `moe.gate` (router), `shared_experts` (kept in BF16) |
| Calibration | 256 samples, seq_len 2048 (in-domain corpus: Korean instruction data mixed with English chat data) |
| Checkpoint size | 19.25 GB |
| Storage format | `modelopt_fp4` |

## Base vs this model

What changed against the bf16 base model (`KRAFTON/Raon-1-mini-preview`).

- **Eval sets**: GSM8K (openai/gsm8k@740312add88f, seed=20261024, n=1319, 200 answered and scored); Korean KMMLU (`HAERAE-HUB/KMMLU`); instruction/format compliance (10 fixed cases).
- **Acceptance thresholds**: GSM8K accuracy may drop at most 0.02 below the base model, KMMLU at most 0.03, and format compliance must stay at or above 0.9.

| # | Configuration | Base Model | This Model | Change | Notes |
| --- | --- | ---: | ---: | --- | --- |
| 1 | Checkpoint size | 53.61 GB | 19.25 GB | 53.61 → 19.25 (-64%) | PASS (within the expected 15.0–28.0 GB range) |
| 2 | Storage format | BF16 (dequantized) | `modelopt_fp4` | — | PASS (stored as `modelopt_fp4`) |
| 3 | GSM8K accuracy | 0.945 (189/200) | 0.170 (34/200) | drop 0.775 | FAIL (drop 0.775, allowed ≤ 0.02) |
| 4 | KMMLU accuracy | 0.565 (113/200) | 0.300 (60/200) | drop 0.265 | FAIL (drop 0.265, allowed ≤ 0.03) |
| 5 | Format compliance | 0.900 (9/10) | 0.900 (9/10) | — | PASS (pass rate ≥ 0.9) |
| 6 | Serving throughput, vLLM fork (C=1) | — | 11.5 tok/s | — | measured through the vLLM fork that serves this checkpoint |
| 7 | Serving latency p50, vLLM fork (C=1) | — | 0.087 s | — | same fixed 8-prompt workload, single GB10 |

The serving rows are measured through the vLLM fork — this checkpoint cannot be loaded in-process by `transformers`, so there is no in-process base comparison. Base accuracy above was measured in-process on the dequantized BF16 base.
[^3]: This model's accuracy rows were measured through the vLLM fork (the checkpoint cannot be loaded in-process by `transformers`), while the Base column is transformers in-process. The drop therefore mixes quantization loss with stack/kernel differences — read it as an upper bound on the quantization loss, not an exact delta.


## Usage - transformers

**`transformers` cannot load this checkpoint.** It is stored in the `modelopt_fp4`
format (NVFP4-packed weights plus ModelOpt scales), which `transformers` does not
implement: `AutoModelForCausalLM.from_pretrained` logs
`Unknown quantization type, got modelopt_fp4` and then aborts with a weight shape
mismatch, because the packed tensors are never unpacked.

Serve it with the vLLM fork instead (see **Usage - vLLM** below) — the fork
implements the `modelopt_fp4` loader path natively, so the checkpoint stays at its
19 GB size.

If you specifically need a `transformers`-loadable copy, this repository ships
`nvfp4_to_bf16.py`, which converts the packed weights to BF16:

    python nvfp4_to_bf16.py tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM --out ./bf16

Note that the result is ~56 GB — larger than the BF16 base model — so it is a
convenience, not the intended path.

## Usage - vLLM

The Raon-1-mini family uses a custom architecture, so stock vLLM cannot serve
it. On GB10 (sm_121) the KRAFTON precompiled fork fails at engine init, so
build the GB10 fork from source first (one-time), then serve with it.

Step 1 — build vLLM from source (GB10). Prerequisites: `nvcc`
from CUDA 13.0 on `PATH`, ~50 GB free disk. Run verbatim in order;
the last line verifies the install.

```bash
mkdir -p /tmp/raon-1-mini-preview-nvfp4-awq-vllm && cd /tmp/raon-1-mini-preview-nvfp4-awq-vllm
VENV=/tmp/raon-1-mini-preview-nvfp4-awq-vllm/.venv
uv venv --python 3.12 "$VENV"
uv pip install --python "$VENV/bin/python" "torch==2.13.0" --index-url https://download.pytorch.org/whl/cu130
uv pip install --python "$VENV/bin/python" setuptools wheel packaging ninja cmake setuptools_rust setuptools_scm
MAX_JOBS=8 TORCH_CUDA_ARCH_LIST="12.1a" uv pip install --python "$VENV/bin/python" --no-build-isolation "vllm @ git+https://github.com/tayaee/raon-vllm-spark.git@gb10-support"
"$VENV/bin/python" -c "import vllm; print('vllm', vllm.__version__)"
```

Step 2 — serve with the built binary.

Full-context serving on a single GB10: flags follow the vendor B300 profile,
scaled to 128 GB. The 18 RDA layers hold fixed-size state and only the 7 MLA
layers keep KV cache (~8 KiB/token), so 262K context needs ~2 GB of KV cache.

```bash
VENV=/tmp/raon-1-mini-preview-nvfp4-awq-vllm/.venv  # same venv as the build step
$VENV/bin/vllm serve tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM \
  --host 127.0.0.1 --port 8000 \
  --served-model-name tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --max-num-batched-tokens 16384 \
  --max-num-seqs 128 \
  --gpu-memory-utilization 0.85 \
  --kv-cache-dtype fp8_e4m3 \
  --enable-prefix-caching \
  --reasoning-parser raon_1 \
  --tool-call-parser raon_1 \
  --enable-auto-tool-choice \
  --trust-remote-code \
  --default-chat-template-kwargs '{"enable_thinking": true, "truncate_history_thinking": false}'
```

> `--kv-cache-dtype fp8_e4m3` and the `raon_1` parsers are fork features —
> verified on KRAFTON checkpoints.
> On a busy node lower `--gpu-memory-utilization` (e.g. `0.3`).
> Compatibility note: the fork is verified against KRAFTON's own checkpoints
> (`modelopt_fp4` NVFP4). This checkpoint uses the same `modelopt_fp4` loader path.
> On B300 / RTX 5090 — the GPUs KRAFTON tested — the precompiled fork works
> without a source build: replace `$VENV/bin/vllm` above with
> `VLLM_USE_PRECOMPILED=1 uvx --from "vllm @ git+https://github.com/krafton-ai/vllm.git@raon-1-mini-preview" vllm`.

## Sampling parameters

Raon-1-mini is a thinking model — keep thinking mode enabled (the serve command
below does this through `--default-chat-template-kwargs '{"enable_thinking": true}'`).

| Setting | Value |
| --- | --- |
| temperature | 1.0 |
| top_p | 0.95 |
| top_k | 20 |
| repetition_penalty | 1.0 |
| frequency_penalty | 0 |
| min_p | 0 |
| presence_penalty | 1.5 (chat, summarization, knowledge Q&A, agents) · 0 (coding, math) |

`presence_penalty` is applied by the model's own remote code, not by
`transformers` or the vLLM sampler.

## Request example

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tayaee/Raon-1-mini-preview-NVFP4-AWQ-GB10-vLLM",
    "messages": [{"role": "user", "content": "Tell me about KRAFTON AI."}],
    "max_tokens": 8192,
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 20,
    "min_p": 0.0,
    "repetition_penalty": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 1.5,
    "chat_template_kwargs": {
      "enable_thinking": true,
      "truncate_history_thinking": false
    }
  }'
```

The reasoning is returned in `message.reasoning` and the answer in
`message.content`. Set `presence_penalty` to `0` for coding and math.

## License and source

- Apache License 2.0. The code in this repository is distributed under Apache-2.0.
- Base model: [KRAFTON/Raon-1-mini-preview](https://huggingface.co/KRAFTON/Raon-1-mini-preview) (rev `da4cf162c8613993f2189ebb438a5f9a23f3e5ca`), Apache-2.0.
- The original KRAFTON repository is access-gated; this repository does not re-gate it.
  The base model license terms (`apache-2.0`) still apply.
