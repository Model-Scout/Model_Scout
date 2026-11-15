---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - LiquidAI/LFM2.5-8B-A1B
base_model_relation: quantized
language: [en, ar, zh, fr, de, ja, ko, es, pt]
pipeline_tag: text-generation
library_name: vllm
tags:
  - nvfp4
  - fp4
  - modelopt
  - vllm
  - lfm2_moe
  - moe
  - quantized
  - blackwell
  - edge
---

# LFM2.5-8B-A1B-NVFP4

**NVFP4 (W4A4) quantization of [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)** — the 8.3B-total / 1.5B-active mixture-of-experts reasoner (131 K context) runs on **one 16 GB Blackwell GPU** and still leaves room for a ~650 K-token KV cache.

Quantized by **Lna-Lab** with NVIDIA TensorRT Model-Optimizer (`modelopt`). To our knowledge this is the first NVFP4 build of the `lfm2_moe` architecture.

> **Why it's nice:** 8.3B total / 1.5B active MoE + a *hybrid* backbone (only 6 of 24 layers
> are attention; the rest are short-convolution) means the KV cache is tiny. Shrink the
> weights to 4-bit and the freed VRAM turns straight into **concurrency** — this card
> happily serves a stack of parallel sessions.

---

## 📊 Measured on 1× RTX PRO 2000 Blackwell (16 GB, SM120)

vLLM 0.21.0, CUDA 12.8 build, driver 595.71.05, `--quantization modelopt`, bf16 KV, 256-token decode.

| build | weights on GPU | KV cache | **1 stream** | **4 concurrent** |
|---|---|---|---|---|
| FP8 (online, baseline) | 8.44 GB | 4.34 GB → 378 K tok | 96.7 tok/s | 195.8 tok/s |
| **NVFP4 (this model)** | **6.93 GB** | **7.54 GB → 658 K tok** | **117.6 tok/s** | **326.2 tok/s** |

- **+22 %** single-stream and **+67 %** at 4-way concurrency vs FP8, on the same card.
- NVFP4 frees ~3.5 GB → **+74 % KV capacity** (378 K → 658 K tokens). Add
  `--kv-cache-dtype fp8` to roughly double it again.
- The "4 concurrent" number is just `--max-num-seqs 4`; raise it — there's plenty of KV
  headroom for many more parallel sessions on this one card.

Greedy correctness spot-check (temp 0): *"capital of France"* → **"The capital of France
is Paris."**; *"2+2"* → **"4"**; *"name three primary colors"* → correctly distinguishes
RYB vs RGB. Reasoning, multilingual (EN/JA) and code generation all preserved.

---

## 🧠 It's a reasoning model — chat template

LFM2.5 uses a ChatML-like template and emits an explicit `<think> … </think>` chain of
thought **before** the final answer. `tokenizer.apply_chat_template(...)` renders, e.g.:

```
<|startoftext|><|im_start|>user
What is the capital of France?<|im_end|>
<|im_start|>assistant
```

and the model produces:

```
<think>
The user asks for the capital of France. That's a simple factual question…
</think>
The capital of France is Paris.
```

**In vLLM, pass `--reasoning-parser deepseek_r1`** — it matches the `</think>` delimiter
and splits the response so the OpenAI API returns the CoT in `reasoning_content` and the
answer in `content`. Omit it if you want the raw text (think tags included).

## 🛠 Tool use (agentic)

LFM2.5 is built for tool use / agentic workflows. Pass tools via
`apply_chat_template(..., tools=[...])` (they're injected into the system prompt). By
default the model emits **Pythonic** function calls — a Python list between the
`<|tool_call_start|>` and `<|tool_call_end|>` special tokens, e.g.:

```
<|tool_call_start|>[get_weather(city="Tokyo")]<|tool_call_end|>
```

(You can ask it for JSON calls instead via the system prompt.) For automatic tool-call
parsing through the OpenAI API, add `--enable-auto-tool-choice --tool-call-parser pythonic`
if your vLLM build's Pythonic parser handles the `<|tool_call_*|>` wrapper — otherwise
parse the special-token block yourself. The bundled `chat_template.jinja` already renders
tools, tool calls, and `tool`-role results.

---

## 🚀 Serve with vLLM (single GPU)

```bash
CUDA_VISIBLE_DEVICES=0 vllm serve sakamakismile/LFM2.5-8B-A1B-NVFP4 \
    --served-model-name lfm25-8b-a1b \
    --quantization modelopt \
    --kv-cache-dtype fp8 \
    --max-model-len 128000 \
    --max-num-seqs 16 \
    --gpu-memory-utilization 0.90 \
    --reasoning-parser deepseek_r1 \
    --port 8000
```

**Concurrency on one 16 GB card (measured):** with `--kv-cache-dtype fp8` the KV pool is
**1.38 M tokens** → **~10 sessions each at a full 128 K context** (bf16 KV → ~5). With
paged KV and shorter prompts you can serve far more — `--max-num-seqs 16` is a good
default; pin to `10` to guarantee every slot at full 128 K.

| flag | what it does for *this* model |
|---|---|
| `--quantization modelopt` | **required** — reads `hf_quant_config.json` (NVFP4). Omit it and weights load as raw uint8 → garbage. |
| `--max-num-seqs` | concurrency. KV is cheap here, so `8`–`16`+ is comfortable. The 326 tok/s figure above was just `4`. |
| `--max-model-len` | up to `131072` (native). Long context is affordable thanks to the tiny KV. |
| `--gpu-memory-utilization` | `0.90` on a clean 16 GB card; lower it if the GPU is shared. |
| `--reasoning-parser deepseek_r1` | separates `<think>` CoT from the answer (see above). |
| `--kv-cache-dtype fp8` | optional, ~2× the KV capacity for even more parallel sessions. |
| `--tensor-parallel-size` | **leave at 1** — the model fits one GPU; sharding an 8B-A1B rarely pays. |

### Offline
```python
from vllm import LLM, SamplingParams
llm = LLM("sakamakismile/LFM2.5-8B-A1B-NVFP4", quantization="modelopt",
          max_model_len=32768, gpu_memory_utilization=0.90, max_num_seqs=8)
tok = llm.get_tokenizer()
chat = tok.apply_chat_template(
    [{"role": "user", "content": "日本語で自己紹介して。"}],
    tokenize=False, add_generation_prompt=True)
print(llm.generate([chat], SamplingParams(
    temperature=0.2, top_k=80, repetition_penalty=1.05, max_tokens=512))[0].outputs[0].text)
```

### Container
A ready `Dockerfile` + `compose.yaml` + `entrypoint.sh` + `run.sh` are bundled — see
**`USAGE.md`** for `./run.sh up | test | bench | logs | down` and every env knob.

**Sampling (Liquid's recommendation):** `temperature=0.2`, `top_k=80`,
`repetition_penalty=1.05`. It thinks first, so give it `max_tokens ≥ 512`.

---

## ⚠️ Usage notes & caveats

- **Needs Blackwell (SM120) + a recent vLLM** (≥0.21 with NVFP4/modelopt) and
  `flashinfer` — the FP4 GEMM and MoE run on FlashInfer-CUTLASS kernels.
- `ModuleNotFoundError: No module named 'trinity_turbo'` in the logs is **harmless**
  (optional plugin auto-probe); the engine continues.
- If a MoE backend objects to the FP4 scales, force Marlin: `VLLM_USE_FLASHINFER_MOE_FP4=0`.
- Use `--quantization modelopt` only — **not** `fp8`/`awq`/`gptq`.
- A handful of rarely-routed ("cold") experts are calibrated from limited activation
  coverage; for the overwhelming majority of tokens, output tracks the BF16 source
  closely. As with the base model, heavy programming / knowledge-heavy QA without
  retrieval isn't its strong suit.
- Straight quantization of the base **instruct** model — no refusal-reduction or other
  behavioral changes.

## 🔬 What's quantized

NVFP4 = e2m1 weights, 16-wide blocks, FP8-e4m3 block scales + FP32 global scale, static
per-tensor `input_scale`.

- **→ NVFP4:** all 32 MoE experts (per layer) + the 2 dense MLP layers.
- **kept BF16:** attention (q/k/v/out), short-conv projections, the MoE router
  (`feed_forward.gate`), token embeddings, and `lm_head`.

Full recipe + scripts: Lna-Lab `lnarizer/recipes/lfm2_moe/` (includes the one modelopt
calibration patch needed for `lfm2_moe`, and the expert key remap for vLLM).

## License

Inherits the base model's license (LFM Open License v1.0, `license_name: lfm1.0`) — see
the bundled `LICENSE`. Base model: `LiquidAI/LFM2.5-8B-A1B`.

## Credits

- Base model: **Liquid AI** — LFM2.5-8B-A1B.
- NVFP4 quantization & packaging: **Lna-Lab**.
- Tooling: NVIDIA TensorRT Model-Optimizer, vLLM, FlashInfer.

---

<div align="center">

**🔬 Lna-Lab** · NVFP4 for Blackwell · *LLMs without colored glasses, in 4-bit, for the edge*

Quantized & verified on 7× RTX PRO 2000 Blackwell · 2026

</div>

