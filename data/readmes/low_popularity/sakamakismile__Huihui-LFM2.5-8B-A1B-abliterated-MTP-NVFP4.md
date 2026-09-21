---
license: other
license_name: lfm1.0
license_link: LICENSE
language: [en, ar, zh, fr, de, ja, ko, es, pt]
library_name: vllm
pipeline_tag: text-generation
base_model: sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4
tags:
  - eagle3
  - mtp
  - speculative-decoding
  - draft-model
  - lfm2_moe
  - vllm
  - nvfp4
  - blackwell
---

# Huihui-LFM2.5-8B-A1B-abliterated-MTP-NVFP4

An **EAGLE-3 / MTP draft head** for speculative decoding of
[`sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4`](https://hf.co/sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4)
in **vLLM**. It is a tiny (≈0.4 B) single-layer drafter that proposes tokens the NVFP4 target then verifies, so single-stream decode runs faster with **identical-quality** (greedy-lossless) output.

This is a **companion model** — it does nothing on its own; load it as the `speculative_config` draft for the NVFP4 target above.

## Measured speedup (greedy, compiled vLLM, 256-tok decode)

| config | base t/s | with this MTP draft | speedup | draft acceptance |
|---|---|---|---|---|
| **TP=1** (1× RTX PRO 2000) | 129.8 | **154.2** | **1.19×** | **59.8 %** |
| **TP=4** (4× RTX PRO 2000)  | 301.9 | **339.8** | **1.13×** | 59.8 % |

Mean accepted length ≈ 1.60 tok/step at `num_speculative_tokens=1`. Acceptance is a property of the draft (TP-independent). Speedup is larger at lower TP (the target is slower there, so the draft saves relatively more).

## Usage (vLLM)

```python
from vllm import LLM, SamplingParams

llm = LLM(
    model="sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4",
    quantization="modelopt",
    speculative_config={
        "method": "eagle3",
        "model": "sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-MTP-NVFP4",
        "num_speculative_tokens": 1,
    },
    max_model_len=8192,
)
# This is a reasoning/chat model — ALWAYS chat-template prompts.
sp = SamplingParams(temperature=0.0, max_tokens=256)
print(llm.chat([{"role": "user", "content": "Explain speculative decoding."}], sp)[0].outputs[0].text)
```

### Server + launch flags (`vllm serve`)

**TP=1 (single GPU):**
```bash
vllm serve sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4 \
  --quantization modelopt \
  --speculative-config '{"method":"eagle3","model":"sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-MTP-NVFP4","num_speculative_tokens":1}' \
  --max-model-len 8192 \
  --reasoning-parser deepseek_r1          # optional: the model emits <think>…</think>
```

**TP=4 (4 GPUs, no-NVLink / PCIe box):**
```bash
NCCL_P2P_DISABLE=1 NCCL_CUMEM_ENABLE=0 \
vllm serve sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4 \
  --quantization modelopt \
  --tensor-parallel-size 4 \
  --disable-custom-all-reduce \
  --speculative-config '{"method":"eagle3","model":"sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-MTP-NVFP4","num_speculative_tokens":1}' \
  --max-model-len 8192
```

| flag | why |
|---|---|
| `--quantization modelopt` | the target is NVFP4 (ModelOpt FP4) |
| `--speculative-config '{"method":"eagle3","model":"…MTP-NVFP4","num_speculative_tokens":1}'` | turn on EAGLE-3 spec-decode with **this** draft (k=1) |
| `--tensor-parallel-size N` + `--disable-custom-all-reduce` | multi-GPU |
| `NCCL_P2P_DISABLE=1 NCCL_CUMEM_ENABLE=0` *(env)* | **required on no-NVLink/PCIe boxes** or NCCL deadlocks at init |
| `--max-model-len 8192` | context window (raise as needed) |
| *do **not** pass `--enforce-eager`* | the **compiled** path is where spec-decode is actually faster; eager misleads |

Offline `LLM(...)` equivalents: `quantization="modelopt"`, `speculative_config={…}`, `tensor_parallel_size=N`, `disable_custom_all_reduce=True`, `enforce_eager=False`, `max_model_len=8192`.

> ⚠️ **Requires a vLLM with `lfm2_moe` speculative-decode support.** Stock vLLM does not yet wire
> EAGLE-3 / `short_conv` spec-decode correctly for this hybrid (short-conv + attention + MoE) arch.
> The fix is upstream PR **vllm-project/vllm#44296** (+ a model-side `SupportsEagle3` patch). Until
> merged, apply those patches (4 files). On unpatched vLLM the draft loads but acceptance is ~0 %.
> For multi-GPU on no-NVLink boxes: `NCCL_P2P_DISABLE=1 NCCL_CUMEM_ENABLE=0` + `disable_custom_all_reduce`.

## How it was trained

- **Method:** EAGLE-3 — one Llama-style decoder layer (qkv input = 2·H: token-embed ⊕ fused aux hidden), `fc: 3·H→H` fusing aux from target layers **(2, 12, 21)**, own `lm_head`, `d2t` vocab map.
- **Reduced draft vocab = 32 000** (top-frequency, covers 99.8 % of tokens). This is what makes spec-decode actually *faster* — a full 128 k draft head is as costly as the target's and caps the speedup.
- **Training data:** 105 371 sequences of **NVFP4-matched** hidden states — captured by serving the *quantized* target itself (not a BF16 proxy), which is what lets serving acceptance track training. Single-step (k=1), 3 epochs, reduced-vocab CE + SmoothL1 hidden-regression.
- In-sample top-1 ≈ 0.84.

## Config (vLLM `Eagle3LlamaForCausalLM`)

hidden 2048 · 1 layer · 32 heads / 8 KV · head_dim 64 · inter 8192 · draft_vocab 32000 · target_hidden 2048 · rope_theta 5e6 · `eagle_config.use_aux_hidden_state: true`.

## Limitations

- **k=1 only** for now. `num_speculative_tokens ≥ 2` currently diverges on the `short_conv` kernel (a separate multi-query conv bug); higher k is the main lever left for bigger speedups (the ~400 t/s TP=4 target needs it).
- Inherits the base model's **abliterated/uncensored** behavior and its license.

## License

Inherits the base license (**LFM Open License v1.0**, `license_name: lfm1.0`) — see the bundled
`LICENSE`. Lineage: `LiquidAI/LFM2.5-8B-A1B` → [`huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated`](https://huggingface.co/huihui-ai/Huihui-LFM2.5-8B-A1B-abliterated)
→ [`…-NVFP4`](https://hf.co/sakamakismile/Huihui-LFM2.5-8B-A1B-abliterated-NVFP4) (the target) →
this MTP / EAGLE-3 draft. The draft only proposes tokens the target verifies — greedy output is
unchanged vs the abliterated base.

## Credits

- Base model: **Liquid AI** — LFM2.5-8B-A1B.
- Abliteration: **huihui.ai** — Huihui-LFM2.5-8B-A1B-abliterated.
- NVFP4 target + EAGLE-3 / MTP draft training & packaging: **Lna-Lab**.
- Tooling: vLLM, EAGLE-3, NVIDIA TensorRT Model-Optimizer, FlashInfer.

## 💖 Support the Base Model Author

This draft stands on **huihui.ai**'s abliteration work. If it's useful to you, please consider
supporting them — a cup of coffee goes a long way:

- **Ko-fi:** https://ko-fi.com/huihuiai
- **Bitcoin:** `bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge`

---

<div align="center">

**🔬 Lna-Lab** · EAGLE-3 / MTP speculative decoding for Blackwell · *faster tokens, same output, in 4-bit*

Trained & benchmarked on 7× RTX PRO 2000 Blackwell · 2026

</div>
