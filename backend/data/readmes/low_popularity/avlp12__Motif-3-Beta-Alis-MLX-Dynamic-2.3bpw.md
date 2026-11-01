---
language:
- en
- ko
license: other
license_name: motif-non-commercial-research
license_link: https://huggingface.co/Motif-Technologies/Motif-3-Beta/blob/main/README.md
library_name: mlx
pipeline_tag: text-generation
base_model: Motif-Technologies/Motif-3-Beta
base_model_relation: quantized
tags:
- mlx
- moe
- korean
- quantized
- apple-silicon
- motif
- mixed-precision
- 2-bit
- dwq
- clip-search
- experimental
- conversational
---

> [!IMPORTANT]
> ## ➡️ 이 리포는 Motif-3 **Beta** 기반입니다 — 정식판 리포를 사용하세요 / This repo quantizes the **Beta** checkpoint — use the official Motif-3 builds
>
> 정식 Motif-3 체크포인트 기반 양자화를 게시했습니다. 새로 받으신다면 정식판 리포를 사용해 주세요:
> I have published quantizations built from the **official Motif-3** checkpoint — please use those instead:
>
> **[avlp12/Motif-3-Alis-MLX-4.5bpw](https://huggingface.co/avlp12/Motif-3-Alis-MLX-4.5bpw)** · **[avlp12/Motif-3-Alis-MLX-8bit](https://huggingface.co/avlp12/Motif-3-Alis-MLX-8bit)**
> (정식판 2.3bpw 빌드는 아직 없습니다 / no official-checkpoint 2.3bpw build yet)

> [!NOTE]
> ## 📌 KL 수치 보류 중 / KL numbers under review — the model itself is fine
>
> **2026-07-26.** 이 카드의 **"KL vs Q8(8bit 레퍼런스)" 수치는 현재 보류**합니다.
> 레퍼런스로 쓰인 [8bit 빌드에 결함](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit/discussions/1)이
> 확인되어(`mx.split` 2³¹ 초과 텐서 침묵 손상), **손상된 레퍼런스를 기준으로 측정된 값**이기 때문입니다.
>
> The **"KL vs Q8" figures on this card are withheld pending re-measurement**: the 8-bit
> build used as the reference has been found defective, so those numbers were measured
> against a corrupted baseline.
>
> **보류되는 것 / withheld:** 슬라이스별 `KL vs Q8` 표 · **"DWQ가 KL을 58–72% 감소"** 주장 ·
> `eval_ladder.png`의 KL 축
>
> **영향 없는 것 / unaffected — 이 빌드 자체는 정상입니다:**
> - 모델 품질(한국어·영어·코드 생성)은 직접 생성으로 검증되었고 그대로 유효합니다.
>   Generation quality is verified directly and stands.
> - **포팅 패리티 `KL ≈1e-7 / token`** 은 수정된 **HF torch 레퍼런스** 기준이라 8bit와 무관하며 유효합니다.
>   The port-parity figure is measured against the fixed HF reference, not the 8-bit build.
> - 루프 프로브(distinct-4gram) 등 **레퍼런스가 필요 없는 측정**은 유효합니다.
>
> 8bit 레퍼런스를 재빌드한 뒤 재측정하여 이 카드의 수치를 갱신하고 이 주석을 내리겠습니다.
> The reference is being rebuilt; these figures will be re-measured and this note removed.

# Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw · ⚠️ experimental floor build

Apple Silicon (MLX) **mixed-precision** quantization of
[Motif-Technologies/Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
— a **314.84B-parameter** (≈13B active) Mixture-of-Experts reasoning model, **text-only**,
bilingual **Korean / English** (+ code), with 97.84% of its mass in the routed experts and
native **256K** context — pushed to the **lowest effective bit-rate the MLX affine
container supports** (routed experts at 2-bit / group-size 128): **2.315 bpw measured,
85 GB on disk**. To our knowledge this is the **first community MLX port of Motif-3-Beta in
any format**, the only build in the family sized to run on a **128 GB Apple Silicon Mac**,
and the family's **headline shippable floor**.

![Which Motif-3-Beta MLX build fits your Mac — 2.3bpw / 128 GB / 85 GB, 4.5bpw / 256 GB / 167 GB, 8bit / 512 GB / 312 GB](assets/tier_guide.png)

> ⚠️ **Experimental floor build.** 2-bit/g128 experts is the hard floor of the MLX affine
> format — coherent and useful after DWQ, but the
> [4.5bpw](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw) /
> [8bit](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit) siblings are closer to
> lossless. If your Mac has ≥256 GB, prefer a larger build.

> ⚠️ **Requires a patched `mlx-lm`** with the `motif` model class (see *How to run*). Stock
> `mlx-lm` has no Motif support and will not load this checkpoint.

> ⚠️ **Non-commercial research license**, inherited in full from Motif-3-Beta (a beta
> release). See *License*.

## What clip-search + DWQ bought

![KL divergence vs the Q8 reference and greedy loop-probe distinct-4gram, across raw FLOOR / +clip / +clip+DWQ — DWQ cuts KL 58-72% and breaks the code loop](assets/eval_ladder.png)

The raw 2-bit floor loops on code and collapses on Korean; **clip-search barely moves KL,
DWQ does the work** — distilling toward the 4.5bpw (C6) teacher on a 45% Korean mix cuts KL
**58-72%** and eliminates the loops. It is the only build that received both low-bit levers.

---

## Model at a glance

Motif-3-Beta is a **text-generation** LLM (no vision/audio), reimplemented for MLX and
verified against a bug-fixed reference.

| | |
|---|---|
| Base model | [Motif-Technologies/Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta) — 314.84B total / ≈13B active |
| Architecture | Sparse MoE, **53 layers** (0-1 dense, 2-52 MoE); **384 routed experts, top-8** + 1 shared |
| Routed-expert mass | **97.84%** of parameters — the bulk, and where the bits go |
| Attention | **GDLA** (Grouped Differential Latent Attention): MLA-style low-rank q/kv + differential-v2 + elementwise output gate; 80 heads / 16 KV groups, head_dim 192 |
| Sliding window | interleaved SWA — window 128 on 40 layers; **13 full-attention layers** carry YaRN, the 40 SWA layers plain rope |
| Other components | **mHC** (manifold-constrained hyper-connections, ×2/layer); **Grouped PolyNorm** per-expert activation; `rms_norm` eps 1e-6 |
| Tokenizer | vocab **220,160**; **stop tokens `{0, 3, 6}`**; chat template **auto-opens `<think>`** |
| Context | **256K** (262,144) native |
| Bits/weight | **2.315** (measured; per-tensor mixed, experts 2-bit/g128) |
| On-disk size | **85 GB** (85 GiB) |
| Format | MLX (Apple Silicon); `library_name: mlx` |

### Floor recipe (verified from `config.json`)

Expert bit-width sets the footprint (97.84% of params); everything else stays high-precision.

| Component | Bits | Notes |
|---|---|---|
| Routed experts (gate/up/down) | **2-bit g128** | ≈97.8% of params — the MLX floor (g128, not g64, for the smallest footprint) |
| Attention (GDLA projections) | 4-bit g64 | per-token critical path |
| `wkv_a` (KV-A latent down-projection) | **8-bit g64** | latent chokepoint — kept high across every profile |
| Token embedding · LM head | 6-bit g64 | distribution-sensitive |
| Router gate · mHC · `lambda_proj` · all norms · `act_fn` | **fp (unquantized)** | discrete control paths + normalization — full precision is nearly free |

### Architecture

![Motif-3-Beta architecture: embedding to 53 decoder layers (GDLA attention, mHC hyper-connections, dense/MoE feed-forward with Grouped PolyNorm) to RMSNorm to LM head](assets/architecture.png)

---

## Build ladder

| Build | Recipe | Size | bpw | Target |
|---|---|---|---|---|
| **2.3bpw (this)** | experts 2b/g128 · attn 4b · wkv_a 8b · embed/head 6b · router/mHC/norms fp | **85 GB** | **2.315** | **128 GB Mac** |
| [4.5bpw (C6)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw) | experts 4b · attn 6b · wkv_a 8b | 167 GB | 4.547 | 256 / 512 GB Mac · **DWQ teacher** |
| [8bit (Q8)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit) | all 8b/g64 | 312 GB | 8.503 | 512 GB Mac · reference |

---

## How to run

Motif support is **not yet in an `mlx-lm` release**. Install from the fork/branch that
carries the `motif` model class:

```bash
pip install git+https://github.com/avlp12/mlx-lm.git@motif
```

**Python:**

```python
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw")

messages = [{"role": "user", "content": "복잡한 문제를 단계적으로 풀어줘."}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
# The chat template auto-opens a <think> block: the model reasons first, then answers.
sampler = make_sampler(temp=1.0, top_p=0.95)   # recommended; greedy can loop on some prompts
print(generate(model, tokenizer, prompt=prompt, max_tokens=1024, sampler=sampler))
```

**CLI / server:**

```bash
mlx_lm.generate --model avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw \
  --prompt "Explain MoE routing in two sentences." --temp 1.0 --top-p 0.95 -m 512

mlx_lm.server --model avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw   # OpenAI-compatible
```

- **Sampling:** temp **1.0** / top-p **0.95** recommended — greedy can loop at this bit-rate
  (see the loop-probe in *Evaluation*).
- **Stop tokens:** tokenizer stops on `{0, 3, 6}`; pass all three as stop ids if you drive
  generation yourself.
- **Reasoning mode:** the chat template auto-opens a `<think>` block — expected, not a bug.
- **Wired memory:** on a 128 GB Mac the weights fit the default limit *tightly*; for real
  context raise it and use 4-bit KV — see *Hardware*.

---

## Method — `alis-dwq` pipeline

Weights come from **[alis-dwq](https://github.com/avlp12/alis-dwq)**, the pipeline behind
the GLM-5.2 (745B) and Hy3 (295B) Alis MLX builds: mixed-bit affine quantization (experts
lowest; router / mHC / `lambda_proj` / norms fp; `wkv_a` 8-bit; embed/head 6-bit), then two
held-out-gated passes:

1. **Anchor-guarded clip-search** — per 128-weight group, clipped grids are accepted only
   when they lower MSE **without raising max abs error beyond ≈1.1×** the min-max grid's,
   preserving outlier "anchor" weights.
2. **Layerwise DWQ distillation** against the **4.5bpw (C6) teacher** on a **45% Korean**
   mix (EN 30 / code 25 / KO 45), with a per-round held-out rollback gate.

Port parity: MLX logits match a **bug-fixed HF reference** to **KL ≈1e-7 / token**.

---

## Evaluation

Measured on a fixed EN / code / KO slice **vs the [8bit (Q8)
build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit)** (near-lossless vs bf16,
which does not fit in memory).

**KL(Q8 ‖ build) and greedy loop-probe (distinct-4gram, 256 tok/slice):**

| slice | KL vs Q8 | loop distinct-4gram |
|---|---|---|
| EN | 0.277 | 0.46 |
| code | 0.100 | 0.96 |
| KO | 0.522 | 0.88 |
| unweighted mean | **≈0.30** | **no cycles on any slice** |

**What DWQ bought** (see chart above): across slices DWQ cut KL **58-72%** (KO
**1.235 → 0.522**) and turned the code slice from a hard **cycle** (distinct-4gram 0.011)
into 0.96. Telemetry: valid loss **0.379 → 0.200**, rounds 1-6 accepted, round 7 reverted by
the rollback gate (natural stop). Clip-search alone was ≈flat on KL; DWQ carries the floor.

**4-bit KV-cache probe** (self-KL, fp16-KV vs 4-bit-KV): **0.006** overall (EN 0.005 / code
0.003 / KO 0.011), flip **3%** → **4-bit KV is viable**, which matters on the 128 GB target
where KV is the binding constraint.

**Honest caveats:**

1. **KO is the softest slice** (KL 0.522 vs EN 0.277) — the usual low-bit pattern,
   substantially recovered by DWQ (raw was 1.235) but not erased.
2. **Greedy can loop**; use temp 1.0 / top-p 0.95. EN distinct-4gram under greedy is 0.46
   (no cycle) — precisely why sampling is recommended over greedy.
3. **Very-long-tail factual recall is weak** — e.g. it does not reliably reproduce obscure
   text like the 4th verse of the Korean national anthem. This is a **base-model property,
   not a quantization artifact** (the 8bit reference shares it), most visible here. General
   knowledge, code, and bilingual generation are reliable.

---

## Correctness & port notes

- **Logit parity.** On a truncated model (fp32, EN/KO/code prompts) MLX matches a bug-fixed
  HF reference to **KL ≈1e-7 / token, top-1 100%**. SWA long-context self-consistency is a
  **bit-exact match** (cached wide forward vs no-cache reference).
- **The shipped HF reference had bugs** (documented in
  [discussions/6](https://huggingface.co/Motif-Technologies/Motif-3-Beta/discussions/6)): a
  YaRN RoPE dimension crash, an eager-attention GQA crash, and a `grouped_mm` path applying
  expert-0 PolyNorm coefficients to all experts. **Motif Technologies pushed fixes (SHA
  `d2c9ac6`)** and this port matches the fixed reference; the early incoherence root-caused
  to the **Grouped PolyNorm activation** (sigmoid coefficients + `output_scale` 0.5 + routed
  `bias_clamp`) — credit to Motif for the fix.
- **One MLX-core bug** is worked around in the port: `mx.split` silently corrupts the tail
  of a >2³¹-element tensor (the 8 GB bf16 `gate_up`); basic strided slices are used instead.
  Upstream [ml-explore/mlx#3836](https://github.com/ml-explore/mlx/issues/3836).

---

## Hardware

The only build in the ladder that runs in a **128 GB** Mac's unified memory. macOS caps
GPU-wired memory at a default `iogpu.wired_limit_mb` of ≈96 GB on a 128 GB machine; the
85 GB of weights fit under it, but *tightly* (≈11 GB free before KV/prefill). For real
context, raise the limit and use 4-bit KV:

```bash
sudo sysctl iogpu.wired_limit_mb=122880       # ≈120 GB; leaves the OS ≈17 GB
mlx_lm.generate --model avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw \
  --kv-bits 4 --kv-group-size 64 --quantized-kv-start 4096 --prompt "…"
```

If your Mac has ≥256 GB, use the [4.5bpw](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw)
or [8bit](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit) build — this floor is
deliberately bit-starved for the 128 GB target.

---

## License

Motif-3-Beta ships **no formal license name and no `LICENSE` file**; its model card states,
verbatim:

> "Permission is granted to use, modify, and redistribute this software for personal,
> educational, and non-commercial research purposes only. Commercial use is prohibited
> without prior written permission from Motif Technologies."

A quantized MLX port is a modification-and-redistribution, which these terms explicitly
permit **provided it stays non-commercial**. **This derivative inherits the license in
full.** The `license: other` / `license_name` fields are a best-effort mapping — the
authoritative terms are the quoted text and the base model's card.

## Credits & attribution

- **Base model:** [Motif Technologies — Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
  (non-commercial research). All architecture — GDLA, Grouped PolyNorm, mHC — and the
  trained weights are theirs, as are the reference fixes (SHA `d2c9ac6`).
- **MLX & `mlx-lm`:** Apple [ml-explore](https://github.com/ml-explore).
- **MLX port, `motif` model class, mixed-precision recipe, clip-search + DWQ:** Alis
  (avlp12), via [alis-dwq](https://github.com/avlp12/alis-dwq).

Independent, unofficial derivative — not affiliated with or endorsed by Motif Technologies.
Provided as-is, without warranty. Research / non-commercial use only.

## Citation

> **Alis (avlp12)** (2026). *Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw* — experimental 2.315 bpw
> MLX floor build of [Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
> for 128 GB Apple Silicon, via anchor-guarded clip-search + layerwise DWQ.
