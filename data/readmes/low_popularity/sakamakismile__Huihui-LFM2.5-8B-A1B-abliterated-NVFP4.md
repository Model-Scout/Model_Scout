---
license: other
license_name: lfm1.0
license_link: LICENSE
base_model:
  - huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated
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
  - abliterated
  - uncensored
---

# Huihui-LFM2.5-8B-A1B-abliterated-NVFP4

**NVFP4 (W4A4) quantization of [huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated](https://huggingface.co/huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated)** — the abliterated (refusal-reduced) build of Liquid AI's 8.3B-total / 1.5B-active mixture-of-experts reasoner (131 K context). Runs on **one 16 GB Blackwell GPU** with room for a ~1.1 M-token KV cache (fp8), and scales cleanly to 2–4 GPUs.

Quantized by **Lna-Lab** with NVIDIA TensorRT Model-Optimizer (`modelopt`). To our knowledge this is the first NVFP4 build of an abliterated `lfm2_moe`.

> ⚠️ **Uncensored model.** The base is abliterated by [huihui.ai](https://huggingface.co/huihui-ai) — its safety filtering is significantly reduced. See **Usage warnings** below. (Per the base card, the abliteration touches the dense path; the MoE experts were not ablated.)

> **Why it's nice:** 8.3B total / 1.5B active MoE + a *hybrid* backbone (only 6 of 24 layers
> are attention; the rest are short-convolution) means the KV cache is tiny. Shrink the
> weights to 4-bit and the freed VRAM turns straight into **concurrency** — one card
> happily serves a stack of parallel sessions, and TP fans that out further.

---

## 📊 Measured throughput — 1 / 2 / 4× RTX PRO 2000 Blackwell (16 GB, SM120)

docker `vllm/vllm-openai:v0.22.0`, `--quantization modelopt`, **fp8 KV**, `max-model-len 32768`, 256-token decode via `/v1/completions` (`ignore_eos`+`min_tokens`). Aggregate output tokens/s at concurrency **C**:

| C | **TP=1** (1 GPU) | **TP=2** (2 GPU) | **TP=4** (4 GPU) |
|--:|--:|--:|--:|
| 1  | 130  | 210  | **305** |
| 2  | 206  | 323  | 452  |
| 4  | 363  | 595  | 808  |
| 8  | 687  | 1147 | 1557 |
| 16 | 1166 | 1831 | 2463 |
| 32 | 2111 | 3273 | **4545** |

| | TP=1 | TP=2 | TP=4 |
|---|--:|--:|--:|
| weights / GPU | ~5.3 GB | ~2.7 GB | ~1.4 GB |
| KV pool (fp8) | **1.16 M tok** | **3.17 M tok** | **7.82 M tok** |
| max concurrency @ 32 K ctx | 35× | 97× | 239× |

- **Single-stream** scales with TP: **130 → 210 → 305 tok/s** (1→2→4 GPU).
- **Aggregate** scales near-linearly with concurrency; TP=4 reaches **~4.5 K tok/s** at C=32 and still has KV headroom for hundreds of sessions.
- Numbers are single-run and indicative (±~10–15 % at high concurrency). bf16 KV trades ~half the KV pool for marginally different speed.

Coherence spot-check (greedy / EN-JA-code): MoE explanation, Japanese, and a linked-list reversal all correct; reasoning, multilingual and code generation preserved.

---

## 🔗 Multi-GPU (TP) on no-NVLink Blackwell — important

These workstation cards have **no NVLink** (PCIe-only). With plain `--tensor-parallel-size 2/4`, **NCCL deadlocks at communicator init** (GPUs spin at 100 % util, no progress). Launch TP with P2P disabled:

```bash
docker run -d --gpus '"device=0,1,3,4"' --ipc=host \
  -e NCCL_P2P_DISABLE=1 -e NCCL_CUMEM_ENABLE=0 \
  -v $PWD:/model:ro -p 8000:8000 --shm-size 16g \
  --entrypoint vllm vllm/vllm-openai:v0.22.0 \
  serve /model --served-model-name lfm25-abl \
    --quantization modelopt --tensor-parallel-size 4 \
    --disable-custom-all-reduce \
    --kv-cache-dtype fp8 --max-model-len 32768 \
    --max-num-seqs 256 --gpu-memory-utilization 0.90 \
    --host 0.0.0.0 --port 8000
```

P2P-off staging is fine for this small MoE (per-token all-reduce volume is tiny). On NVLink hardware you can drop `NCCL_P2P_DISABLE` / `--disable-custom-all-reduce`.

---

## 🧠 It's a reasoning model — chat template

LFM2.5 uses a ChatML-like template and emits an explicit `<think> … </think>` chain of
thought **before** the final answer. `tokenizer.apply_chat_template(...)` renders, e.g.:

```
<|startoftext|><|im_start|>user
What is the capital of France?<|im_end|>
<|im_start|>assistant
```

**In vLLM, pass `--reasoning-parser deepseek_r1`** — it matches the `</think>` delimiter so
the OpenAI API returns the CoT in `reasoning_content` and the answer in `content`. Omit it
for raw text (think tags included).

## 🛠 Tool use (agentic)

Pass tools via `apply_chat_template(..., tools=[...])`. By default the model emits
**Pythonic** calls between `<|tool_call_start|>` and `<|tool_call_end|>`:

```
<|tool_call_start|>[get_weather(city="Tokyo")]<|tool_call_end|>
```

For OpenAI-API auto-parsing add `--enable-auto-tool-choice --tool-call-parser pythonic`
(if your vLLM build's Pythonic parser handles the wrapper); otherwise parse the
special-token block yourself. The bundled `chat_template.jinja` renders tools / calls /
`tool`-role results.

---

## 🚀 Serve with vLLM

**Single GPU:**
```bash
CUDA_VISIBLE_DEVICES=0 vllm serve sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4 \
    --served-model-name lfm25-abl \
    --quantization modelopt \
    --kv-cache-dtype fp8 \
    --max-model-len 128000 \
    --max-num-seqs 16 \
    --gpu-memory-utilization 0.90 \
    --reasoning-parser deepseek_r1 \
    --port 8000
```
(For TP=2/4 see the no-NVLink launch above.)

| flag | what it does for *this* model |
|---|---|
| `--quantization modelopt` | **required** — reads `hf_quant_config.json` (NVFP4). Omit it and weights load as garbage. |
| `--kv-cache-dtype fp8` | ~2× KV capacity (used for the table above). |
| `--max-num-seqs` | concurrency; KV is cheap here, so `16`–`256` is comfortable. |
| `--max-model-len` | up to `131072` (native). |
| `--reasoning-parser deepseek_r1` | separates `<think>` CoT from the answer. |
| `--tensor-parallel-size` | `1` fits one card; `2`/`4` for more single-stream speed + KV (mind the NCCL note). |

### Offline
```python
from vllm import LLM, SamplingParams
llm = LLM("sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4", quantization="modelopt",
          max_model_len=32768, gpu_memory_utilization=0.90, max_num_seqs=8)
tok = llm.get_tokenizer()
chat = tok.apply_chat_template(
    [{"role": "user", "content": "日本語で自己紹介して。"}],
    tokenize=False, add_generation_prompt=True)
print(llm.generate([chat], SamplingParams(
    temperature=0.2, top_k=80, repetition_penalty=1.05, max_tokens=512))[0].outputs[0].text)
```

**Sampling (Liquid's recommendation):** `temperature=0.2`, `top_k=80`,
`repetition_penalty=1.05`. It thinks first, so give it `max_tokens ≥ 512`.

---

## ⚠️ Usage notes & caveats

- **Needs Blackwell (SM120) + a recent vLLM** (≥0.21 with NVFP4/modelopt) and `flashinfer`
  — the FP4 GEMM and MoE run on FlashInfer-CUTLASS kernels.
- `ModuleNotFoundError: No module named 'trinity_turbo'` in the logs is **harmless**.
- If a MoE backend objects to the FP4 scales, force Marlin: `VLLM_USE_FLASHINFER_MOE_FP4=0`.
- Use `--quantization modelopt` only — **not** `fp8`/`awq`/`gptq`.
- A handful of rarely-routed ("cold") experts are calibrated from limited activation
  coverage and exported with a weight-derived scale fallback; for the overwhelming
  majority of tokens, output tracks the source closely.
- **Uncensored / abliterated** (refusal-reduced) — inherited from the base. Safety
  filtering is significantly reduced; outputs may be sensitive or inappropriate. Use for
  research / controlled settings, monitor and review outputs, and comply with local law.
  See the [base model card](https://huggingface.co/huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated)
  for the full warnings. Quantization changes precision only — no behavioral change vs the
  abliterated base.

## 🔬 What's quantized

NVFP4 = e2m1 weights, 16-wide blocks, FP8-e4m3 block scales + FP32 global scale, static
per-tensor `input_scale`.

- **→ NVFP4:** all 32 MoE experts (per layer) + the 2 dense MLP layers.
- **kept BF16:** attention (q/k/v/out), short-conv projections, the MoE router
  (`feed_forward.gate`), token embeddings, and `lm_head`.

Full recipe + scripts: Lna-Lab `lnarizer/recipes/lfm2_moe/` (the one modelopt calibration
patch for `lfm2_moe`, plus the expert-key remap for vLLM). The exact same recipe produced
the non-abliterated [LFM2.5-8B-A1B-NVFP4](https://huggingface.co/sakamakismile/LFM2.5-8B-A1B-NVFP4)
unchanged.

## License

Inherits the base license (LFM Open License v1.0, `license_name: lfm1.0`) — see the bundled
`LICENSE`. Lineage: `LiquidAI/LFM2.5-8B-A1B` → `huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated`
→ this NVFP4 build.

## Credits

- Base model: **Liquid AI** — LFM2.5-8B-A1B.
- Abliteration: **huihui.ai** — Huihui-LFM2.5-8B-A1B-abliterated.
- NVFP4 quantization & packaging: **Lna-Lab**.
- Tooling: NVIDIA TensorRT Model-Optimizer, vLLM, FlashInfer.

## 💖 Support the Base Model Author

This NVFP4 build stands on **huihui.ai**'s abliteration work. If it's useful to you,
please consider supporting them — a cup of coffee goes a long way:

- **Ko-fi:** https://ko-fi.com/huihuiai
- **Bitcoin:** `bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge`

---

<div align="center">

**🔬 Lna-Lab** · NVFP4 for Blackwell · *LLMs without colored glasses, in 4-bit, for the edge*

Quantized & benchmarked on 7× RTX PRO 2000 Blackwell · 2026

</div>
