---
license: apache-2.0
base_model: AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16
language:
- en
- zh
- multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
- 27b
- official-release
- abliterated
- abliterix
- aeon
- aeon-7
- agentic
- bf16
- blackwell
- chat
- chunked-prefill
- coding
- conversational
- dgx-spark
- dflash
- fp4
- fp8
- function-calling
- gated-deltanet
- gb10
- gdn
- hybrid-attention
- image-text-to-text
- instruct
- linear-attention
- long-context
- mamba
- mixed-precision
- modelopt
- mtp
- multimodal
- nvidia-modelopt
- nvfp4
- openai-compatible
- quantized
- qwen
- qwen3
- qwen3.5
- qwen3.8
- qwen3_5
- reasoning
- refusal-removed
- rtx-5090
- rtx-pro-6000
- sm_120
- sm_121a
- speculative-decoding
- thinking
- tool-calling
- uncensored
- unfiltered
- vision
- vision-language
- vllm
---

# Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED

[![AEON Uncensored NVFP4 Mixed Precision Release](aeon-nvfp4-mixed-cartridge.jpg)](https://www.patreon.com/AeonForge7)

**Announcement.** This Hub card is the release notice for the MIXED deploy cut. Deeper release notes and expanded serve recipes land on [Patreon](https://www.patreon.com/AeonForge7) as more battle testing and raw data comes in - not all at once on day one.

I've spent a lot of months learning what abliteration actually costs. Turns out the trap most people fall into is chasing a vanity KL of zero and calling every judge-R a leftover refusal. That is how you lobotomize a 27B. I wanted the opposite: **willfully compliant**, coherent, useful - and still a real model when the answer gets long.

So this is the ~**23G** ModelOpt **mixed** deploy cut of [AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16). Not a blunt NVFP4 dump. Not a dequant-edit-requant circus. A lattice designed so the last layers can still *write code that passes unit tests*, while the bulk of the MLP rides NVFP4 where Blackwell is actually hungry for it.

**Official MIXED deploy cut.** Cosmic remains a later brand for the intelligence heal. Do not treat a long-context loop as the last word on this line.

## Model family (pick your seat)

| Repo | Size | What it is | Target hardware |
|---|---|---|---|
| **[BF16 master](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16)** | ~54G | Full-precision uncensored master. Abliterated for coherence, vision + MTP untouched. | H200 / multi-GPU / PRO 6000 when you want the teacher, not the deploy knife |
| **This MIXED NVFP4** | ~23.8G (4 shards) | ModelOpt NVFP4 + FP8 + BF16 lattice (last-8 full MLP FP8) + **native MTP** + vision. | **DGX Spark / GB10**, **RTX 5090**, **RTX PRO 6000** with AEON vLLM Ultimate images |

Same will. Different seats. The BF16 is the source of truth. This card is what you actually serve day to day.

## The lattice (why MIXED, not "just NVFP4")

![AEON MIXED quant lattice - NVFP4 body, FP8 writers, last-8 full MLP FP8, BF16 vision/MTP](aeon-mixed-quant-lattice.png)

I do not trust equal-bitwidth recipes on a hybrid GDN / full-attn stack. The first Mix B bake FP8'd only the last-8 `down_proj` and left `gate`/`up` on NVFP4. Coding cratered to **0.694** on AEON Bench unit tests - real syntax and assert fails, not a moody judge. Leftover-KL on those miss prefixes lit up layers 56-63. So the sibling bake did the honest thing: **last-8 full MLP (`gate` + `up` + `down`) -> FP8**. Coding jumped to **0.833**.

| Block | Format | Why |
|---|---|---|
| MLP layers 0-55 | **NVFP4** W4A4 (MSE + fp8_scale_sweep) | Size + Blackwell NVFP4 throughput |
| MLP layers **56-63** | **FP8** full (`gate`/`up`/`down`) | Coding fidelity where residual L2 spiked |
| Softmax attn + GDN writers | **FP8** | Writers that corrupt if you force NVFP4 wrong |
| Vision tower + **MTP head** + embeddings + lm_head + GDN guts | **BF16** | Untouched capability organs. MTP grafted from Ultimate BF16 (15 tensors, 0.791G) after ModelOpt export dropped it. |

Calib **1024x2048**. Export gate: `found=168 missing=0 last8_mlp_fp8=24`. Parent BF16 untouched. Post-export: grafted unmodified `mtp.*` (15 BF16 tensors, 0.791G) from Ultimate BF16 - ModelOpt had dropped the head.

## What you get

- **Uncensored will** - hall monitor gone; answers instead of sermons (same lineage as the BF16 master)
- **Coding that ships** - AEON Bench Coding **0.833** vs prior Mix B **0.694** (and ahead of stock Unsloth NVFP4 Coding **0.806** on the public card)
- **Agentic legs** - Hermes **0.918**, OpenCode **0.818** on the same local follow-on (OpenClaw still the soft spot)
- **Deployable size** - ~23.8G (NVFP4 body + BF16 vision + BF16 MTP) on one Spark / one 5090 / one PRO 6000
- **Full multimodal + MTP** - vision tower and video preprocessor intact; native MTP head for RTX speculative decode
- **Honest scoreboard** - Intelligence (Math/Reasoning/Prose) still trails stock Qwen's 84.5 composite; Cosmic is the heal track, not this card pretending otherwise

Local AEON Suite v4 run `ceaac9e418` (GB10, think 32k / max 65k / retry 131k, c=8, mothership fail-closed):

| Board | This MIXED | Prior Mix B |
|---|---:|---:|
| Text mean | **0.782** | 0.759 |
| Coding | **0.833** | 0.694 |
| Hermes | **0.918** | ~0.917 |
| OpenClaw | 0.707 | 0.733 |
| OpenCode | **0.818** | 0.793 |

Attested mothership Global ([aeon-bench.com](https://aeon-bench.com), same MIXED tree): overall **~91.9**, Perf dial **100**, peak_agg **237.67** tok/s (wave-peak, Coding@c16) on the **single Spark Dynamic DFlash lattice** seat below.

## QuickStart - Spark Dynamic DFlash lattice + RTX seats

Use **`ghcr.io/aeon-7/aeon-vllm-ultimate:2026-09-18-v0.29.0-omni`** on **DGX Spark / GB10** for the new engine tip (upstream **vLLM 0.29.0**, sm_121a bake, digest `sha256:cc91c51559d66854718fd9a8db6423e605ba76fb338bb55902caccb62aa9c677`). It keeps the AEON carries (DFlash/DFlash2, reasoning-EOS force-end, NVFP4 paths) and is the cut where **dual-Spark TP=2 stays coherent** if you set the B0 knobs: `VLLM_ALLREDUCE_USE_FLASHINFER=0`, `fuse_allreduce_rms=false`, `--disable-custom-all-reduce`, and `NCCL_IB_HCA=<dev>:1` with a **single** equals. TP=1 A/B vs `2026-09-07-reasoning-eos` held quality and was slightly faster. **ModelOpt `#54367` plus DFlash2 `layer_type` / Triton `use_mm_prefix` are baked into `2026-09-18-v0.29.0-omni`+** (no bind required). Older tags still need the #54367 bind. Pin the dated tag until you confirm GHCR `:latest` shares that digest; rollback remains `:2026-09-07-reasoning-eos`.  
Use **`ghcr.io/aeon-7/aeon-vllm-ultimate-rtx:latest`** on **RTX 5090** and **RTX PRO 6000** (sm_120; promoted from `2026-09-07-omni-mm` = ModelOpt #54367 **plus** Spark-parity `vllm-omni` multimodal/omni stack). Pin dated RTX tags if you want known-good: `2026-09-07-omni-mm` (or `2026-09-07-modelopt` for #54367-only). Do **not** cross Spark and RTX images. Spark is sm_121a / aarch64 UMA. The RTX image is sm_120 / amd64 dedicated VRAM.

**Vision / video / audio:** RTX `:latest` / `:2026-09-07-omni-mm` registers the multimodal processor for `Qwen3_5ForConditionalGeneration` (same family as Spark omni) and layers `vllm-omni==0.27.0rc1` for Omni speech-out models. Keep `--limit-mm-per-prompt` as in the recipes below. Re-pull: `docker pull ghcr.io/aeon-7/aeon-vllm-ultimate-rtx:latest`.

**Stale Aug-21 RTX `:latest` symptom:** `'MergedColumnParallelLinear' object has no attribute 'data'` during fused `gate_up` `modelopt_mixed` load - bind-mount [`modelopt-54367.py`](modelopt-54367.py) until you pull the 2026-09-07 image.

Gen defaults for all seats (Qwen3.8 card): `temperature 0.6`, `top_p 0.95`, `top_k 20`, `repetition_penalty 1.0`. Thinking on: `chat_template_kwargs={"enable_thinking": true, "reasoning_effort": "medium"}`.

Prefer `repetition_penalty: 1.0` for tool calling / structured output. Values above 1.0 can penalize repeated structural tokens (e.g. `/parameter`, XML tags) and break parsers.

### ModelOpt hard rules (this MIXED tree)

> **Prefix cache:** Prefix caching (APC) is ON for normal multi-turn / shared-prefix serve (vLLM default when you omit --no-enable-prefix-caching). For scored Perf / God Mode measurement boards you may still pass --no-enable-prefix-caching so TTFT is not helped by cross-request cache hits.


| Rule | Detail |
|---|---|
| **No `--quantization`** | Leave it **unset** so `hf_quant_config.json` selects `modelopt_mixed`. Never pass `compressed-tensors`, `nvfp4`, or `modelopt_fp4` on this tree. |
| **#54367 ModelOpt patch** | **Baked into Spark `2026-09-18-v0.29.0-omni`+** (also DFlash2 layer_type / Triton use_mm_prefix). Still required as a bind on older Spark 0.29 tags. Folded into Spark `2026-09-07-reasoning-eos`, and into RTX `2026-09-07-modelopt` / `2026-09-07-omni-mm` **and** RTX `:latest`. On older tags, bind-mount [#54367](https://github.com/vllm-project/vllm/pull/54367)-style `modelopt.py` over Spark site-packages or RTX dist-packages. Full file: [`modelopt-54367.py`](modelopt-54367.py) on this repo. |
| **TRITON_ATTN** | Always `--attention-backend TRITON_ATTN` on Spark and RTX long seats. |
| **Prefix cache (APC)** | ON for published serve (omit `--no-enable-prefix-caching`). Bench/Perf/God Mode may disable for TTFT purity. |
| **Spark speculative** | Single Spark: external **Dynamic DFlash lattice** via `num_speculative_tokens_per_batch_size` (`z-lab/Qwen3.8-27B-DFlash2`). TP=2: fixed **DFlash2 n=7**. |
| **RTX speculative** | In-checkpoint **MTP n=3**. Do **not** hang a fat DFlash drafter on 32 GB. |
| **Never MTP + DFlash** | Pick one speculative path. Never both. |
| **V2 runner** | Single Spark lattice seat: **MRv2** (`VLLM_USE_V2_MODEL_RUNNER=1`) + `FULL_AND_PIECEWISE`. TP=2 recipes keep `VLLM_USE_V2_MODEL_RUNNER=0`. |


### Weights mount (HF snapshot symlink trees)

Hugging Face Hub snapshot dirs under `~/.cache/huggingface/hub/models--.../snapshots/<rev>` are **symlink trees** into `blobs/`. Mounting only the snapshot path into Docker often yields **dangling symlinks** inside the container. Prefer one of:

1. **Mount the HF cache root** and serve by **repo-id + revision** (recommended):
   `-v $HOME/.cache/huggingface:/root/.cache/huggingface:ro` then `vllm serve AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED --revision <rev> ...`
2. Or mount a **fully materialized** copy (real files, no dangling links), e.g. a local `huggingface-cli download ... --local-dir` tree.

Do **not** mount only `.../snapshots/<rev>` unless you have verified every weight path resolves inside the container.

### Knob cheat-sheet

| Seat | max-model-len | seqs | util | Spec | YaRN |
|---|---:|---:|---:|---|---|
| **1x Spark** | 262144 | 16 | **0.80** | Dynamic DFlash lattice | **off** |
| **TP=2** | 1000000 | 16 | 0.70 | DFlash2 n=7 | **on** (official factor-4 `hf-overrides`) |
| **RTX 5090** | 131072 | 4 | 0.92-0.95 | MTP n=3 | **off** |
| **RTX PRO 6000** | 262144 | 8 | 0.80 | MTP n=3 (optional) | **off** |

> **`--gpu-memory-utilization` note (Spark):** default **0.80**. That can be excessive when the box also runs secondary services - **downshift util** to leave headroom. On a **dedicated LLM-only** Spark, pushing to **0.85** may gain slight performance. Going **beyond 0.80** risks OOM under high KV-cache pressure, so **0.85 is optional dedicated-only**, not the published default.

> [!TIP]
> ### Dynamic DFlash lattice (single Spark seat)
>
> This is the **locked map** `[[1,2,9],[3,4,8],[5,8,7],[9,12,6],[13,16,5]]` (c1-2 n=9 ... c13-16 n=5) - the published single-Spark recipe (**quality and throughput**).
>
> - Native key: `num_speculative_tokens_per_batch_size`
> - Exact map JSON: `[[1,2,9],[3,4,8],[5,8,7],[9,12,6],[13,16,5]]`
> - Runtime K: c1-2->10, c3-4->8, c5-8->7, c9-10->6, c11-12->5, c13-14->4, c15-16->3
> - Peak measured: **237.67 tok/s** wave-peak Coding@c16
> - Default util **0.80** (downshift for secondary services; optional **0.85** dedicated-only - beyond 0.80 risks OOM with high KV)
> - Full docker block: [One DGX Spark - Dynamic DFlash lattice](#1-one-dgx-spark--dynamic-dflash-lattice-quality--throughput)

### 1) One DGX Spark - Dynamic DFlash lattice (quality + throughput)

One published single-Spark serve seat. Locked **Dynamic DFlash lattice** via `num_speculative_tokens_per_batch_size`, **MRv2** + `FULL_AND_PIECEWISE`, default util **0.80**, seqs **16**, 262k, KV fp8, chunked prefill, **prefix cache ON**, **TRITON_ATTN**. Image pin `2026-09-18-v0.29.0-omni` (digest `sha256:cc91c515...`); rollback `:2026-09-07-reasoning-eos`. #54367 + DFlash2 fixes **baked into** `2026-09-18-v0.29.0-omni`+ (bind only on older tags).

This seat is **both quality and throughput** - not a demoted "Perf-only" lane.

Measured AEON Bench peak overall (wave-peak concurrent window, **not** decodexconc): **237.67** tok/s Coding@c16.

**Util:** default **0.80**. Downshift when co-running secondary services. Optional **0.85** on a dedicated LLM-only box for a slight gain - going beyond 0.80 risks OOM with high KV-cache usage.

```bash
MODEL=$HOME/.cache/huggingface/hub/models--AEON-7--Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED/snapshots/<rev>
DRAFT=/path/to/z-lab__Qwen3.8-27B-DFlash2
PATCH=/path/to/modelopt-54367.py   # optional on 2026-09-18-v0.29.0-omni+ (baked in); required on older 0.29 tags
IMAGE=ghcr.io/aeon-7/aeon-vllm-ultimate:2026-09-18-v0.29.0-omni   # pin dated until :latest digest matches cc91c515...; rollback :2026-09-07-reasoning-eos

docker rm -f aeon-mixed-spark 2>/dev/null
docker run -d --gpus all --network host \
  --name aeon-mixed-spark \
  -e VLLM_USE_V2_MODEL_RUNNER=1 \
  -e VLLM_ENABLE_CUDA_COMPATIBILITY=0 \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
  -v "$MODEL:/model:ro" -v "$DRAFT:/draft:ro" \
  # -v "$PATCH:/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/quantization/modelopt.py:ro" \  # optional on 2026-09-18+
  --entrypoint vllm "$IMAGE" serve /model \
  --served-model-name aeon \
  --host 0.0.0.0 --port 8000 \
  --gpu-memory-utilization 0.80 \
  --max-model-len 262144 \
  --max-num-seqs 16 \
  --max-num-batched-tokens 16384 \
  --kv-cache-dtype fp8 \
  --enable-chunked-prefill \
  --tool-call-parser qwen3_coder \
  --enable-auto-tool-choice \
  --reasoning-parser qwen3 \
  --limit-mm-per-prompt '{"image":4,"video":2}' \
  --attention-backend TRITON_ATTN \
  --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE"}' \
  --trust-remote-code \
  --speculative-config '{"method":"dflash","model":"/draft","num_speculative_tokens":9,"num_speculative_tokens_per_batch_size":[[1,2,9],[3,4,8],[5,8,7],[9,12,6],[13,16,5]],"attention_backend":"TRITON_ATTN"}' \
  --override-generation-config '{"temperature":0.6,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":0.0,"repetition_penalty":1.0}'
```

Ready when `/v1/models` lists `aeon`. Smoke: chat completions, `model=aeon`, short prompt.

Runtime K by batch: c1-2->10, c3-4->8, c5-8->7, c9-10->6, c11-12->5, c13-14->4, c15-16->3.

### 2) Two DGX Sparks - TP=2 quality (1M YaRN + DFlash2 n=7)

Use only when two Sparks share a fast link (InfiniBand or RoCE). Each box needs the same `$MODEL`, `$DRAFT`, `$PATCH`, and image. **Start rank 1 (headless) first, then rank 0 (API).** Clients use `http://$MASTER_IP:8000`.

```bash
MODEL=$HOME/.cache/huggingface/hub/models--AEON-7--Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED/snapshots/<rev>
DRAFT=/path/to/z-lab__Qwen3.8-27B-DFlash2
PATCH=/path/to/modelopt-54367.py
IMAGE=ghcr.io/aeon-7/aeon-vllm-ultimate:latest
MASTER_IP=10.10.10.1
IFACE=enp1s0f0np0
IB_HCA==rocep1s0f0:1
HF_OVERRIDES='{"text_config":{"rope_parameters":{"mrope_interleaved":true,"mrope_section":[11,11,10],"rope_type":"yarn","rope_theta":10000000,"partial_rotary_factor":0.25,"factor":4.0,"original_max_position_embeddings":262144}}}'
```

Change `MASTER_IP`, `IFACE`, and `IB_HCA` to this pair (`ip -br link`). The `==` in `IB_HCA` is required (NCCL exact match). No InfiniBand? Drop `--device /dev/infiniband`, `-e NCCL_IB_HCA=...`, `-e NCCL_IB_GID_INDEX=3`, and `--cap-add IPC_LOCK`; keep `NCCL_SOCKET_IFNAME` on the fast nic.

**Do not** pass `--quantization`. Bind-mount `#54367`. Set `VLLM_USE_V2_MODEL_RUNNER=0`.

#### Rank 1 - worker (headless)

On the second Spark:

```bash
NODE_IP=10.10.10.2
RANK=1
NAME=tp2-node1

docker rm -f "$NAME" 2>/dev/null
docker run -d --name "$NAME" --gpus all --ipc=host --shm-size=16g --net=host \
  -e VLLM_HOST_IP="$NODE_IP" \
  -e NCCL_SOCKET_IFNAME="$IFACE" -e GLOO_SOCKET_IFNAME="$IFACE" \
  -e NCCL_IB_HCA="$IB_HCA" -e NCCL_IB_GID_INDEX=3 -e NCCL_DEBUG=WARN \
  --device /dev/infiniband --cap-add IPC_LOCK --ulimit memlock=-1:-1 \
  -e VLLM_USE_FLASHINFER_SAMPLER=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
  -e VLLM_USE_V2_MODEL_RUNNER=0 \
  -v "$MODEL":/model:ro -v "$DRAFT":/draft:ro \
  # -v "$PATCH:/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/quantization/modelopt.py:ro" \  # optional on 2026-09-18+
  --entrypoint vllm "$IMAGE" serve /model \
    --headless \
    --tensor-parallel-size 2 --nnodes 2 --node-rank 1 \
    --master-addr "$MASTER_IP" --master-port 29501 \
    --kv-cache-dtype fp8_e4m3 --attention-backend TRITON_ATTN \
    --max-model-len 1000000 --max-num-seqs 16 --max-num-batched-tokens 16384 \
    --gpu-memory-utilization 0.70 \
    --disable-custom-all-reduce \
    --enable-chunked-prefill \
    --mamba-cache-mode align \
    --limit-mm-per-prompt '{"image":4,"video":2}' \
    --speculative-config '{"method":"dflash","model":"/draft","num_speculative_tokens":7}' \
    --hf-overrides "$HF_OVERRIDES" \
    --override-generation-config '{"temperature":0.6,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":0.0,"repetition_penalty":1.0}' \
    --trust-remote-code
```

Rank 1 must have `--headless`. Do not give it `--host` or `--port`.

#### Rank 0 - API

On the first Spark:

```bash
NODE_IP=10.10.10.1
RANK=0
NAME=tp2-node0

docker rm -f "$NAME" 2>/dev/null
docker run -d --name "$NAME" --gpus all --ipc=host --shm-size=16g --net=host \
  -e VLLM_HOST_IP="$NODE_IP" \
  -e NCCL_SOCKET_IFNAME="$IFACE" -e GLOO_SOCKET_IFNAME="$IFACE" \
  -e NCCL_IB_HCA="$IB_HCA" -e NCCL_IB_GID_INDEX=3 -e NCCL_DEBUG=WARN \
  --device /dev/infiniband --cap-add IPC_LOCK --ulimit memlock=-1:-1 \
  -e VLLM_USE_FLASHINFER_SAMPLER=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
  -e VLLM_USE_V2_MODEL_RUNNER=0 \
  -v "$MODEL":/model:ro -v "$DRAFT":/draft:ro \
  # -v "$PATCH:/usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/quantization/modelopt.py:ro" \  # optional on 2026-09-18+
  --entrypoint vllm "$IMAGE" serve /model \
    --served-model-name aeon --host 0.0.0.0 --port 8000 \
    --tensor-parallel-size 2 --nnodes 2 --node-rank 0 \
    --master-addr "$MASTER_IP" --master-port 29501 \
    --kv-cache-dtype fp8_e4m3 --attention-backend TRITON_ATTN \
    --max-model-len 1000000 --max-num-seqs 16 --max-num-batched-tokens 16384 \
    --gpu-memory-utilization 0.70 \
    --disable-custom-all-reduce \
    --enable-chunked-prefill \
    --mamba-cache-mode align \
    --limit-mm-per-prompt '{"image":4,"video":2}' \
    --speculative-config '{"method":"dflash","model":"/draft","num_speculative_tokens":7}' \
    --reasoning-parser qwen3 --tool-call-parser qwen3_coder --enable-auto-tool-choice \
    --hf-overrides "$HF_OVERRIDES" \
    --override-generation-config '{"temperature":0.6,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":0.0,"repetition_penalty":1.0}' \
    --trust-remote-code
```

```bash
docker logs -f tp2-node0
curl -s http://127.0.0.1:8000/health
```

1M on TP=2 is the long-context recipe. It is slower than 64k.

#### TP=2 - speed (64k) deltas

Same run as above, but:

- remove `-e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1`
- remove `--hf-overrides`
- `--max-model-len 65536`
- `--gpu-memory-utilization 0.60`
- keep DFlash2 n=7, seqs **16**, #54367 patch, no `--quantization`

### 3) RTX 5090 - `aeon-vllm-ultimate-rtx:latest`

32 GB dedicated. Long-context chat seat: **TRITON_ATTN** + `fp8_e4m3` KV (FlashInfer + fp8 KV can garbage on sm_120 at long ctx). Seqs **4**, util **0.92-0.95**, 131k, **no YaRN**. Native **MTP n=3** is in the checkpoint (~1% KV cost).

`aeon-vllm-ultimate-rtx:latest` / `2026-09-07-omni-mm` folds #54367 **and** Spark-parity `vllm-omni` (vision/video/audio + Omni speech-out). `2026-09-07-modelopt` is the #54367-only intermediate. On older Aug-21 images, set `PATCH` and bind-mount as below (harmless no-op if the file matches the folded copy).

```bash
# Prefer HF cache mount + repo-id (avoids snapshot symlink dangling links):
#   -v $HOME/.cache/huggingface:/root/.cache/huggingface:ro
#   serve AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED --revision <rev>
MODEL=$HOME/.cache/huggingface/hub/models--AEON-7--Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED/snapshots/<rev>
PATCH=/path/to/modelopt-54367.py   # optional on :latest / 2026-09-07-omni-mm; required on Aug-21
IMAGE=ghcr.io/aeon-7/aeon-vllm-ultimate-rtx:latest   # or :2026-09-07-omni-mm

docker run -d --name aeon-mixed-5090 --gpus all --ipc=host --shm-size=8g -p 8000:8000 \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -v "$MODEL:/model:ro" \
  -v "$PATCH:/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/modelopt.py:ro" \
  --entrypoint vllm "$IMAGE" serve /model \
  --served-model-name aeon --host 0.0.0.0 --port 8000 \
  --max-model-len 131072 --max-num-seqs 4 --max-num-batched-tokens 8192 \
  --gpu-memory-utilization 0.92 --kv-cache-dtype fp8_e4m3 \
  --mamba-ssm-cache-dtype bfloat16 --attention-backend TRITON_ATTN \
  --enable-chunked-prefill \
  --limit-mm-per-prompt '{"image":2,"video":1}' \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3,"attention_backend":"TRITON_ATTN"}' \
  --reasoning-parser qwen3 --tool-call-parser qwen3_coder --enable-auto-tool-choice \
  --override-generation-config '{"temperature":0.6,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":0.0,"repetition_penalty":1.0}' \
  --trust-remote-code
```

If KV will not allocate at 131k, try `--gpu-memory-utilization 0.95` then drop `--max-num-seqs` to 2. Do **not** add a fat DFlash drafter on 32 GB for the long seat.

### 4) RTX PRO 6000 (96 GB, sm_120) - `aeon-vllm-ultimate-rtx:latest`

Same image family as the 5090. More VRAM -> raise concurrency and context headroom. Pin **TRITON_ATTN** for long context. If you use MTP, put `"attention_backend":"TRITON_ATTN"` **inside** `--speculative-config` (top-level flag does not always propagate to the drafter).

Same rule as the 5090: `:latest` / `2026-09-07-omni-mm` folds #54367 + omni/MM; bind-mount [`modelopt-54367.py`](modelopt-54367.py) on Aug-21. Prefer HF cache + repo-id over snapshot-only mounts.

```bash
MODEL=$HOME/.cache/huggingface/hub/models--AEON-7--Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED/snapshots/<rev>
PATCH=/path/to/modelopt-54367.py   # optional on :latest / 2026-09-07-omni-mm; required on Aug-21
IMAGE=ghcr.io/aeon-7/aeon-vllm-ultimate-rtx:latest   # or :2026-09-07-omni-mm

docker run -d --name aeon-mixed-pro6000 --gpus all --ipc=host --shm-size=16g -p 8000:8000 \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 \
  -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -v "$MODEL:/model:ro" \
  -v "$PATCH:/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/modelopt.py:ro" \
  --entrypoint vllm "$IMAGE" serve /model \
  --served-model-name aeon --host 0.0.0.0 --port 8000 \
  --max-model-len 262144 --max-num-seqs 8 --max-num-batched-tokens 8192 \
  --gpu-memory-utilization 0.80 --kv-cache-dtype fp8_e4m3 \
  --mamba-ssm-cache-dtype bfloat16 --attention-backend TRITON_ATTN \
  --enable-chunked-prefill \
  --limit-mm-per-prompt '{"image":4,"video":2}' \
  --reasoning-parser qwen3 --tool-call-parser qwen3_coder --enable-auto-tool-choice \
  --override-generation-config '{"temperature":0.6,"top_p":0.95,"top_k":20,"min_p":0.0,"presence_penalty":0.0,"repetition_penalty":1.0}' \
  --trust-remote-code
```

Native MTP (preferred on this seat):

```bash
--speculative-config '{"method":"mtp","num_speculative_tokens":3,"attention_backend":"TRITON_ATTN"}'
```

For Qwen long think, prefer a per-request `thinking_token_budget` over blindly raising `max_tokens` - otherwise the model can spend the whole budget inside `<think>`.

## How this was built

```
AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16
        ↓
  NVIDIA ModelOpt 0.46  ·  MSE + fp8_scale_sweep  ·  1024x2048
        ↓
  Mix B (last-8 down_proj FP8 only)  -> Coding 0.694
        ↓
  leftover-KL on coding unit-test misses
        ↓
  this sibling: last-8 FULL MLP FP8
        ↓
  AEON Bench Coding 0.833
```

## The unaligned edge

I figure if you own the hardware and the weights, you should own exactly how they are used. You still own the ramifications. This model will write what the base model would refuse. Intended for research, red-team, creative work without a hall monitor - and a threat if the prompt is. A disclaimer plus the payload is not a refusal. Over-abliteration into gibberish defeats the reason you wanted the unlock.

## User Responsibility & Arbitration Clause

**By accessing, downloading, using, running inference on, fine-tuning, merging, quantizing, distributing, integrating, or otherwise interacting with this model, you acknowledge and agree to the following:**

1. **Sole Responsibility.** You are solely responsible for every prompt, every response, every downstream action, and any harm that results.
2. **No Warranty.** Provided **"AS IS"**, without warranty of any kind.
3. **Legal Compliance.** You must comply with all applicable laws and policies in every jurisdiction you touch.
4. **Operational Safety Layer.** Deploy with input validation, output filtering, access controls, and human review for high-risk workflows. A production deploy without those layers is unsafe by construction.
5. **Heightened Duty of Care.** Uncensored means the duty of care sits with you. If unsure, do not make the request.
6. **No Endorsement of Outputs.** Authors do not endorse any specific output.
7. **Arbitration.** Disputes arising from use of this model are resolved by binding individual arbitration (AAA Consumer Rules if no other body is agreed), waiving jury trial and class actions.
8. **Indemnification.** You indemnify authors, contributors, and publishers against claims arising from your use.
9. **Severability.** Invalid provisions are replaced by the closest enforceable equivalent.
10. **Acceptance.** Use constitutes acceptance. If you do not accept, do not use the model.

**This model is a tool with no opinions of its own. You supply the judgement. The outputs carry your fingerprints.**

## Provenance & Credits

- **BF16 master:** [AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-BF16)
- **Base:** [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- **Quant:** NVIDIA ModelOpt 0.46 mixed NVFP4+FP8 - AEON-7
- **Serve:** [aeon-vllm-ultimate](https://github.com/AEON-7/vllm-ultimate-dgx-spark) · [aeon-vllm-ultimate-rtx](https://github.com/AEON-7/vllm-ultimate-rtx)

## License

Apache 2.0 (inherited from Qwen/Qwen3.8-27B).
