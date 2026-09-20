---
license: apache-2.0
base_model: AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored
language:
- en
- zh
- multilingual
library_name: transformers
pipeline_tag: text-generation
tags:
- abliterated
- uncensored
- qwen3
- qwen3.6
- nvfp4
- compressed-tensors
- llmcompressor
- hybrid-attention
- mamba
- gated-deltanet
- multimodal
- aeon
- dgx-spark
---
> [!IMPORTANT]
> **Superseded by Qwen3.8 — use this instead:** [`AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED`](https://huggingface.co/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED-NVFP4-MIXED)
>
> **Operator recipes (Spark Dynamic DFlash lattice, TP=2, RTX):** [`AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED`](https://github.com/AEON-7/Qwen3.8-27B-AEON-ULTIMATE-UNCENSORED)
>
> This Qwen3.6-27B card stays online for history and existing downloads. For new work, move to the Qwen3.8 Ultimate Uncensored NVFP4-MIXED release. That line is far superior in capability and reaches substantially more of what the architecture can do, with a more refined mixed quantization methodology (NVFP4 + FP8 lattice) than these older Qwen3.6 exports.
>
> Serve with the unified container: `ghcr.io/aeon-7/aeon-vllm-ultimate:latest` (Spark / GB10) or `ghcr.io/aeon-7/aeon-vllm-ultimate-rtx:latest` (RTX discrete).

# Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4

![AEON Qwen — Supreme Being of the Digital Cosmos](cartridge.jpg)

NVFP4 hardware-quantized release of [`AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored`](https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored). Same model, same 0/50 refusal rate, same preserved capabilities — now compressed from **51 GB BF16** to **26 GB NVFP4** for native FP4 hardware throughput on DGX Spark / GB10 / Blackwell sm_121a.

This release is **multimodal-preserved** (vision tower stays BF16 — text + image inference fully functional) and **hybrid-attention-preserved** (the 48 linear-attention / GatedDeltaNet layers stay BF16; FP4 only applies to the 16 full-attention layers' output projections + all MLPs).

---

## What Changed vs BF16

| Aspect | BF16 (source) | NVFP4 (this release) |
|---|---|---|
| Disk size | 51 GB | **26 GB** (49% reduction) |
| Refusal rate | 0/50 | **inherited — to be verified post-deploy** |
| Multimodal | preserved | **preserved (vision BF16, no degradation)** |
| Hybrid SSM | repaired + intact | **intact (linear_attn BF16-preserved)** |
| Hardware target | A100 / H100 / RTX PRO 6000 BF16 | **DGX Spark (GB10), B100/B200, RTX PRO 6000 Blackwell** with native FP4 throughput |
| KL vs BF16 source | n/a | **expected ≤0.001** (typical for this recipe class) |

The NVFP4 quantization scheme is NVIDIA-mandated: E2M1 element format, block_size=16, FP8 E4M3 per-block scales, FP32 per-tensor scale, symmetric signed.

---

## Quantization Recipe

Tool: **llm-compressor 0.10.1.dev107** (vllm-project) using `QuantizationModifier(scheme="NVFP4")` post-training quantization.

```python
from llmcompressor.modifiers.quantization import QuantizationModifier
recipe = QuantizationModifier(
    targets="Linear",
    scheme="NVFP4",
    ignore=[
        "lm_head",                  # always
        "re:.*embed_tokens.*",      # always
        "re:.*\\.visual\\..*",      # vision tower BF16 — preserves multimodal
        "re:.*visual\\..*",
        "re:.*linear_attn\\..*",    # SSM/GDN BF16 — Mamba state collapses under FP4
        "re:.*norm.*",
        "re:.*q_norm.*",
        "re:.*k_norm.*",
    ],
)
```

**Calibration:** open-platypus, 512 samples × 4096 tokens.
**Pipeline:** `sequential` with `sequential_targets=["Qwen3_5DecoderLayer"]` — required for hybrid stacks (mixed full + linear attention layers); without explicit targeting, llm-compressor's auto-discovery silently skips layers.
**Loader:** `AutoModelForImageTextToText` to preserve the `Qwen3_5ForConditionalGeneration` multimodal class.
**Processor:** passed explicitly to `oneshot()` to avoid the "model processor required when a dataset is provided" failure on multimodal builds without torchvision.

**Verification (pass):**
- 1 shard, 1952 keys
- 64 quantized full-attention projections (16 layers × 4 q/k/v/o)
- 432 `linear_attn.*` keys preserved BF16 (48 layers × 9 modules)
- 333 `visual.*` keys preserved BF16 (vision tower intact)
- 319 norm keys preserved BF16
- `lm_head` and `embed_tokens` preserved BF16
- NVFP4-packed weights present
- `input_global_scale` magnitudes 142–346 (healthy range)

Wall-clock quant time: ~57 minutes on 1× RTX PRO 6000 Blackwell (96 GB).

---

## Deployment

### vLLM on DGX Spark (GB10 / sm_121a) — recommended

Serve on the unified **`ghcr.io/aeon-7/aeon-vllm-ultimate:latest`** container (= tag `:2026-06-18-v0.23.0-dflashfix`; rollback `:2026-06-11-pr41703`) with the external **z-lab DFlash drafter** at the validated default **`num_speculative_tokens: 10`**. The patched CUTLASS NVFP4 path uses native FP4 tensor-core kernels and **outperforms the Marlin fallback** — do NOT force `VLLM_NVFP4_GEMM_BACKEND=marlin` (that's the workaround for stock vLLM builds where CUTLASS is broken on SM121).

```bash
docker pull ghcr.io/aeon-7/aeon-vllm-ultimate:latest
hf download z-lab/Qwen3.6-27B-DFlash --local-dir ./dflash-drafter

# ENTRYPOINT is /bin/bash → pass --entrypoint vllm then serve ...
docker run --gpus all --ipc=host --network=host \
  -e TORCH_CUDA_ARCH_LIST=12.1a -e ENABLE_NVFP4_SM100=0 \
  -e VLLM_USE_FLASHINFER_MOE_FP4=0 -e VLLM_USE_FLASHINFER_SAMPLER=1 \
  -e VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 -e PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \
  -v /path/to/model:/models/aeon-ultimate:ro \
  -v ./dflash-drafter:/models/dflash-drafter:ro \
  --entrypoint vllm ghcr.io/aeon-7/aeon-vllm-ultimate:latest \
  serve /models/aeon-ultimate \
    --served-model-name aeon-ultimate qwen36-ultimate aeon-fast aeon-deep \
    --host 0.0.0.0 --port 8000 \
    --quantization compressed-tensors \
    --mamba-cache-dtype float32 \
    --max-model-len 256000 \
    --max-num-seqs 64 \
    --max-num-batched-tokens 16384 \
    --gpu-memory-utilization 0.65 \
    --enable-chunked-prefill \
    --enable-prefix-caching \
    --load-format safetensors \
    --trust-remote-code \
    --enable-auto-tool-choice \
    --tool-call-parser qwen3_coder \
    --reasoning-parser qwen3 \
    --attention-backend flash_attn \
    --limit-mm-per-prompt '{"image":4,"video":2}' \
    --mm-encoder-tp-mode data \
    --mm-processor-cache-type shm \
    --speculative-config '{"method":"dflash","model":"/models/dflash-drafter","num_speculative_tokens":10}'
```

> `--gpu-memory-utilization` is **0.65** solo with DFlash / **0.6** when ASR/TTS/embeddings share the Spark; on GB10 unified memory keep it in the **0.6–0.7** band — above ~0.8 the shared CPU+GPU pool page-thrashes and stalls the box (even 0.85 stalls), and DFlash's verify buffers aren't counted by the fraction, so leave headroom. Use `--mamba-cache-dtype float32` (more precise recurrent state + slightly higher DFlash acceptance than float16) and **omit `--mamba-block-size`** (the default lowers single-stream TTFT vs 256). Do **not** set `--kv-cache-dtype` with DFlash — the non-causal drafter requires BF16 KV. For the XS body (21 GB, tighter cards), see the [`-Multimodal-NVFP4-MTP-XS`](https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-Multimodal-NVFP4-MTP-XS) sibling; full config reference is in the [DFlash repo](https://github.com/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-DFlash).

#### Four served-model-name aliases — same weights, different sampling conventions

vLLM's `--served-model-name` accepts multiple values; each becomes a separate `model` ID in `/v1/models` but **all four route to the same `/models/aeon-ultimate` backend**. The differentiation lives in client-side sampling conventions, exploiting a hard property of **DFlash speculative decoding**:

> DFlash's drafter is trained to match the target's argmax. **Greedy** (T=0) sampling lets the drafter hit ~80 % first-position acceptance → ~3× speedup. **Sampled** (T≥0.7) sampling drops acceptance to ~5 % → speedup collapses. Splitting the model into two API IDs lets agent runtimes route per-workload without changing endpoints mid-conversation.

| served name | Recommended sampling | Use case | DFlash effect (single-stream) |
|---|---|---|---|
| **`aeon-fast`** | `temperature=0`, `top_p=1.0` (greedy) | tool calls, agent loops, code, math, structured / JSON output | ~80 % drafter acceptance → **~91 tok/s** (Spark v2 measured) |
| **`aeon-deep`** | `temperature=0.7`, `top_p=0.95`, `top_k=64`, `repetition_penalty=1.05` | creative writing, brainstorming, open-ended Q&A, character roleplay | ~5 % acceptance → ~38 tok/s; variety prioritized over throughput |
| **`aeon-ultimate`** | client-provided (no opinion injected) | raw-API consumers that bring their own sampling | depends on client params |
| **`qwen36-ultimate`** | client-provided (no opinion injected) | same as `aeon-ultimate`, vendor-agnostic Qwen-branded alias for tools that key off the `qwen` prefix | depends on client params |

All four aliases share the **same** 256 K context window, full multimodal pipeline (image × 4, video × 2), `--reasoning-parser qwen3` thinking-mode support, and `--tool-call-parser qwen3_coder` tool-call output. **Only the name and the sampling defaults the client attaches differ.**

##### Quick routing reference (agent runtimes)

```python
# Pseudocode for the routing decision
def pick_model(workload):
    if workload in {"tool_call", "code_gen", "math", "json", "structured"}:
        return "aeon-fast"        # T=0, max DFlash speedup
    elif workload in {"creative", "brainstorm", "open_qa", "roleplay"}:
        return "aeon-deep"        # T=0.7, variety
    else:
        return "aeon-ultimate"    # client controls sampling
```

For a worked OpenClaw integration that registers both `aeon-fast` and `aeon-deep` as separate provider entries with these defaults, see [`docs/openclaw.md`](https://github.com/AEON-7/Qwen3.6-NVFP4-DFlash/blob/main/docs/openclaw.md) in the deployment repo.

### Python (transformers) — for testing or non-vLLM serving

```python
from transformers import AutoModelForImageTextToText, AutoTokenizer
import torch

model_id = "AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored-NVFP4"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    dtype=torch.bfloat16,   # vision tower + non-quantized weights
    device_map="cuda:0",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Your prompt here"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7, do_sample=True)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Requires `compressed-tensors >= 0.12` for NVFP4 dequant on the fly.

---

## Hardware notes

| Hardware | Notes |
|---|---|
| **DGX Spark (GB10, sm_121a)** | Primary target. Use patched vLLM CUTLASS path. Expect ~50 tok/s single-stream after warmup. |
| **B100 / B200 (sm_100)** | Native FP4 compute via `tcgen05`/UTCQMMA — fastest hardware for this format. |
| **RTX PRO 6000 Blackwell (sm_120)** | Native FP4 via CUTLASS path. Excellent throughput. |
| **A100 / H100 (sm_80, sm_90)** | NVFP4 dequantizes to BF16/FP8 at kernel level — works but no FP4 throughput advantage. Use BF16 release instead for best perf on these. |

---

## Provenance

- **BF16 source:** [`AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored`](https://huggingface.co/AEON-7/Qwen3.6-27B-AEON-Ultimate-Uncensored) — see source card for full pipeline (FernflowerAI SSM repair → abliterix-v1.4 abliteration → trial 46 of 50 selected for capability preservation).
- **Original base:** [`Qwen/Qwen3.6-27B`](https://huggingface.co/Qwen/Qwen3.6-27B) by Alibaba.
- **Quantization tool:** [llm-compressor](https://github.com/vllm-project/llm-compressor) by vllm-project.
- **NVFP4 scheme:** [NVIDIA NVFP4 specification](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/).

---

## User Responsibility & Arbitration Clause

**By accessing, downloading, using, running inference on, fine-tuning, merging, quantizing, distributing, integrating, or otherwise interacting with this model, you acknowledge and agree to the following:**

1. **Sole Responsibility.** You, the user, are **solely and exclusively responsible** for every prompt issued, every response produced, every downstream action taken in reliance on those responses, and any harm — direct, indirect, consequential, or otherwise — that results.

2. **No Warranty.** This model is provided strictly **"AS IS"**, without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, non-infringement, safety, alignment, factual accuracy, or legal compliance in any jurisdiction. No contributor, author, publisher, or hosting platform assumes liability of any kind for outputs or downstream use.

3. **Legal Compliance.** You are responsible for ensuring that your use complies with **all applicable laws, regulations, terms of service, industry codes of conduct, professional ethical standards, and organizational policies** in every jurisdiction in which you operate or in which your outputs may be received. The unaligned nature of this model does not grant you any legal authorization you did not already have.

4. **Operational Safety Layer.** An uncensored model is not a toy. You are expected to implement appropriate **downstream safety layers** proportionate to your deployment context, including but not limited to: input validation, output filtering, content moderation, audit logging, rate limiting, access controls, and human-in-the-loop review for high-risk workflows. A production deployment of this model without such layers is **unsafe by construction** and is not a supported use case.

5. **Heightened Duty of Care.** The absence of internal refusal behavior means the duty of care that would ordinarily rest partly with the model rests entirely with you. You are expected to exercise greater — not lesser — caution, forethought, and ethical discipline when operating this model. If you are uncertain whether your contemplated use is ethical, legal, or wise, the correct action is to **not make the request**.

6. **No Endorsement of Outputs.** The authors, contributors, and publishers do not endorse, adopt, or take responsibility for any specific output. Outputs are a stochastic function of the prompt, the weights, and the sampler state — not a statement of position by any human.

7. **Arbitration.** Any dispute, claim, or controversy arising out of or relating to the use of this model, its outputs, or this clause shall be resolved through **binding individual arbitration** under the rules of a mutually agreed arbitration body (or, absent agreement, the American Arbitration Association's Consumer Arbitration Rules), waiving any right to a jury trial, class action, representative action, or consolidated proceeding. Venue shall be the jurisdiction of the disputing party bringing the claim. Costs and attorneys' fees shall be allocated per the applicable arbitration rules. This clause does not expand, and where legally prohibited does not establish, any liability in the other direction; it limits how the user may proceed when alleging harm tied to their own use of this model.

8. **Indemnification.** You agree to indemnify, defend, and hold harmless the authors, contributors, and publishers of this model from and against any claims, damages, losses, liabilities, costs, and expenses (including reasonable attorneys' fees) arising from or related to your use of the model or your breach of this clause.

9. **Severability.** If any provision is held unenforceable in a given jurisdiction, the remaining provisions remain in full force, and the unenforceable provision is replaced by the closest enforceable equivalent consistent with the original intent.

10. **Acceptance.** Your use of this model constitutes your acceptance of this clause in full. If you do not accept, do not use the model.

**This model is a tool with no opinions of its own. You supply the opinions. You supply the judgement. You supply the ethics. The outputs carry your fingerprints, not the model's.**

---

## License

Apache 2.0 (inherited from `Qwen/Qwen3.6-27B`).
