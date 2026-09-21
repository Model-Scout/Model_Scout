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
- 8-bit
- reference
- conversational
---

> [!IMPORTANT]
> ## ➡️ 이 리포는 Motif-3 **Beta** 기반입니다 — 정식판 리포를 사용하세요 / This repo quantizes the **Beta** checkpoint — use the official Motif-3 builds
>
> 정식 Motif-3 체크포인트 기반 양자화를 게시했습니다. 새로 받으신다면 정식판 리포를 사용해 주세요:
> I have published quantizations built from the **official Motif-3** checkpoint — please use those instead:
>
> **[avlp12/Motif-3-Alis-MLX-8bit](https://huggingface.co/avlp12/Motif-3-Alis-MLX-8bit)** (직접 대응 빌드 / direct counterpart)

> [!NOTE]
> ## ✅ 재빌드 완료 / Rebuilt and verified — 2026-07-26
>
> 2026-07-22 업로드분에 결함이 있었습니다([discussion #1](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit/discussions/1)):
> 융합 전문가 텐서(`gate_up_proj`, 4.03e9 요소 = 2³¹의 1.88배)를 나눌 때
> [`mx.split`이 4 GiB 오프셋 이후를 침묵 손상](https://github.com/ml-explore/mlx/issues/3836)시켰고,
> 이 빌드는 우회 적용 **전에** 만들어졌습니다. **현재 저장소는 재빌드본이며 정상입니다.**
>
> The 2026-07-22 upload was defective (`mx.split` silent corruption above 2³¹ elements).
> **This repository now contains a rebuilt, verified model.**
>
> - **검증 / verified:** greedy(`--temp 0`) 5개 슬라이스 전부 정상 — KO 사실·추론·장문, EN, 코드
>   (distinct-4gram 0.95–1.00, 루프 0건). 구 빌드는 같은 프롬프트에서 무한 반복했습니다.
> - **확증 / forensics:** 구·신 빌드의 전문가 0–3번이 **바이트 단위 동일** — 손상 오프셋 아래에서는
>   일치하고 그 위에서만 갈립니다 (손상 시작점: 384개 전문가 중 205번).
> - **무결성 / integrity:** 77 shards · 334,382,459,970 B · index 3,532 tensors · missing/orphan 0 ·
>   bit-badge oracle 632 = 632
> - 신고해 주신 [@appleseedered](https://huggingface.co/appleseedered) 님께 감사드립니다.
>
> 사후분석 / postmortem: [alis-dwq case study](https://github.com/avlp12/alis-dwq/tree/main/examples/motif-3-beta)

# Motif-3-Beta-Alis-MLX-8bit

Apple Silicon (MLX) **8-bit** quantization of
[Motif-Technologies/Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
— a **314.84B-parameter** (≈13B active) Mixture-of-Experts reasoning model, **text-only**,
bilingual **Korean / English** (+ code), with 97.84% of its mass in the routed experts and
native **256K** context. This is the **near-lossless reference** build: uniform 8-bit
(g64), **8.503 bpw measured, 312 GB on disk**, for **512 GB Apple Silicon Macs**. Part of
the first community MLX port of Motif-3-Beta in any format.

This build is the **anchor of the family**: it is statistically near-lossless versus the
bf16 original, and every other build's quality is **measured against it** (the bf16 model
does not fit in memory, so Q8 is the practical ground truth). Run it when you want the
maximum-quality MLX artifact or a KL/eval reference.

![Which Motif-3-Beta MLX build fits your Mac — 2.3bpw / 128 GB / 85 GB, 4.5bpw / 256 GB / 167 GB, 8bit / 512 GB / 312 GB](assets/tier_guide.png)

> ⚠️ **Requires a patched `mlx-lm`** with the `motif` model class (see *How to run*). Stock
> `mlx-lm` has no Motif support and will not load this checkpoint.

> ⚠️ **Non-commercial research license**, inherited in full from Motif-3-Beta (a beta
> release). See *License*.

---

## Model at a glance

Motif-3-Beta is a **text-generation** LLM (no vision/audio) built on several non-standard
components. The port reimplements each for MLX and verifies it against a bug-fixed reference.

| | |
|---|---|
| Base model | [Motif-Technologies/Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta) — 314.84B total / ≈13B active |
| Architecture | Sparse MoE, **53 layers** (0-1 dense, 2-52 MoE); **384 routed experts, top-8** + 1 shared |
| Routed-expert mass | **97.84%** of parameters |
| Attention | **GDLA** (Grouped Differential Latent Attention): MLA-style low-rank q/kv + differential-v2 + elementwise output gate; 80 heads / 16 KV groups, head_dim 192 |
| Sliding window | interleaved SWA — window 128 on 40 layers; **13 full-attention layers** carry YaRN, the 40 SWA layers plain rope |
| Other components | **mHC** (manifold-constrained hyper-connections, ×2/layer); **Grouped PolyNorm** per-expert activation; `rms_norm` eps 1e-6 |
| Tokenizer | vocab **220,160**; **stop tokens `{0, 3, 6}`**; chat template **auto-opens `<think>`** |
| Context | **256K** (262,144) native |
| Bits/weight | **8.503** (measured; uniform 8-bit/g64) |
| On-disk size | **312 GB** (312 GiB) |
| Format | MLX (Apple Silicon); `library_name: mlx` |
| Role | near-lossless reference · KL / eval ground truth for the family |

### Recipe (verified from `config.json`)

Uniform 8-bit — no bit is starved. Even at 8-bit the discrete control paths are kept in full
precision, as on every build in the family.

| Component | Bits | Notes |
|---|---|---|
| Routed experts (gate/up/down) | **8-bit g64** | ≈97.8% of params |
| Attention (GDLA projections) | 8-bit g64 | per-token critical path |
| `wkv_a` (KV-A latent down-projection) | 8-bit g64 | latent chokepoint |
| Token embedding · LM head | 6-bit g64 | distribution-sensitive |
| Router gate · mHC · `lambda_proj` · all norms · `act_fn` | **fp (unquantized)** | discrete control paths + normalization |

### Architecture

![Motif-3-Beta architecture: embedding to 53 decoder layers (GDLA attention, mHC hyper-connections, dense/MoE feed-forward with Grouped PolyNorm) to RMSNorm to LM head](assets/architecture.png)

---

## Build ladder

| Build | Recipe | Size | bpw | Target |
|---|---|---|---|---|
| [2.3bpw (FLOOR)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw) | experts 2b/g128 · attn 4b · wkv_a 8b | 85 GB | 2.315 | 128 GB Mac |
| [4.5bpw (C6)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw) | experts 4b · attn 6b · wkv_a 8b | 167 GB | 4.547 | 256 / 512 GB Mac · DWQ teacher |
| **8bit (this, Q8)** | all 8b/g64 · embed/head 6b · router/mHC/norms fp | **312 GB** | **8.503** | **512 GB Mac** · reference |

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

model, tokenizer = load("avlp12/Motif-3-Beta-Alis-MLX-8bit")

messages = [{"role": "user", "content": "한국어와 영어로 자기소개를 해줘."}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
# The chat template auto-opens a <think> block: the model reasons first, then answers.
sampler = make_sampler(temp=1.0, top_p=0.95)   # recommended; greedy can loop on some prompts
print(generate(model, tokenizer, prompt=prompt, max_tokens=1024, sampler=sampler))
```

**CLI / server:**

```bash
mlx_lm.generate --model avlp12/Motif-3-Beta-Alis-MLX-8bit \
  --prompt "Explain MoE routing in two sentences." --temp 1.0 --top-p 0.95 -m 512

mlx_lm.server --model avlp12/Motif-3-Beta-Alis-MLX-8bit   # OpenAI-compatible
```

- **Sampling:** temperature **1.0**, top-p **0.95** are recommended (greedy can loop on some
  prompts, even at 8-bit — it is a base-model tendency, not a quantization artifact).
- **Stop tokens:** the tokenizer stops on `{0, 3, 6}`; pass all three as stop ids if you
  drive generation yourself.
- **Reasoning mode:** the chat template opens a `<think>` block automatically — expected
  behavior, not a template bug.
- **Long context:** on 512 GB, quantize the KV cache for long prompts
  (`--kv-bits 8 --kv-group-size 64 --quantized-kv-start 4096`). See *Hardware*.

---

## Method — `alis-dwq` pipeline

Weights are produced with **[alis-dwq](https://github.com/avlp12/alis-dwq)**, the same
pipeline used for the GLM-5.2 (745B) and Hy3 (295B) Alis MLX builds. This build is a
**straight uniform 8-bit affine quantization** (g64), with embed/head at 6-bit and the
router / mHC / `lambda_proj` / norms kept fp — no clip-search or DWQ pass. It is the
**quasi-continuous source** the more aggressive builds are quantized and distilled from, and
the **reference** they are measured against.

The port itself is **parity-verified**: MLX logits match a **bug-fixed HF reference** to
**KL ≈1e-7 / token** (see *Port notes*).

---

## Evaluation

This build is the **reference** — near-lossless versus the bf16 original — so the family's
KL and loop-probe numbers are measured **against it**, not for it. Fluent bilingual
generation is confirmed: **Korean (including hanja), English, and code**, with the reasoning
`<think>` trace intact. General knowledge, code, and bilingual generation are reliable.

**The rest of the ladder, measured vs this 8bit reference** (fixed EN / code / KO slice):

| build | KL(Q8 ‖ build) EN / code / KO | notes |
|---|---|---|
| **8bit (this)** | reference (0 by definition) | near-lossless vs bf16 |
| [4.5bpw (C6)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw) | teacher-grade — not separately measured | was the DWQ teacher; near-golden |
| [2.3bpw (FLOOR)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw) | 0.277 / 0.100 / 0.522 | after clip-search + DWQ |

![The 2.3bpw floor build measured against this reference: KL(Q8 ‖ build) and greedy loop-probe across raw / +clip / +clip+DWQ — clip-search + DWQ cut KL 58-72% and break the code loop](assets/eval_ladder.png)

*Everything in the family is measured against this build. The chart tracks the 2.3bpw floor
build's recovery toward this reference through clip-search and DWQ.*

**Honest caveat (a base-model property, shown clearly by the reference):** very-long-tail
factual recall can be weak — e.g. the model does not reliably reproduce obscure text such as
the 4th verse of the Korean national anthem. Because this build is near-lossless, that
behavior is the **base model's**, not a quantization artifact; the smaller builds inherit it.

---

## Correctness & port notes

- **Logit parity.** On a truncated model (fp32, EN/KO/code prompts) MLX matches a bug-fixed
  HF reference to **KL ≈1e-7 / token, top-1 100%**. SWA long-context self-consistency is a
  **bit-exact match** (cached wide forward vs no-cache reference).
- **The shipped HF reference had bugs** (documented in the repo discussion
  [Motif-3-Beta/discussions/6](https://huggingface.co/Motif-Technologies/Motif-3-Beta/discussions/6)):
  a YaRN RoPE dimension crash, an eager-attention GQA crash, and a `grouped_mm` path that
  applied expert-0 PolyNorm coefficients to all experts. **Motif Technologies pushed fixes
  (SHA `d2c9ac6`)** and this port matches the fixed reference. The root cause of the early
  incoherence was the **Grouped PolyNorm activation** (sigmoid coefficients + `output_scale`
  0.5 + routed `bias_clamp`) — credit to Motif for the fix.
- **One MLX-core bug** is worked around in the port: `mx.split` silently corrupts the tail
  of a >2³¹-element tensor (the 8 GB bf16 `gate_up`); basic strided slices are used instead.
  Upstream [ml-explore/mlx#3836](https://github.com/ml-explore/mlx/issues/3836).

---

## Hardware

Built for **512 GB Apple Silicon** (M3 Ultra class). Weights are 312 GB, leaving ample room
for KV cache and long-context prefill activation within a 512 GiB machine; use int8 KV
(`--kv-bits 8`) for the longest prompts. If your Mac has **256 GB**, run the
[4.5bpw build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw); for
**128 GB**, the [2.3bpw floor build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw).

---

## License

Motif-3-Beta ships **no formal license name and no `LICENSE` file**; its model card states,
verbatim:

> "Permission is granted to use, modify, and redistribute this software for personal,
> educational, and non-commercial research purposes only. Commercial use is prohibited
> without prior written permission from Motif Technologies."

This is a **non-commercial research license** that explicitly permits modification and
redistribution for personal / educational / non-commercial research use. A quantized MLX
port is a modification-and-redistribution, so it is permitted **provided it stays
non-commercial** and carries the same terms. **This derivative inherits that license in
full.** The `license: other` / `license_name` fields are a best-effort mapping — the
authoritative terms are the quoted text and the base model's card.

## Credits & attribution

- **Base model:** [Motif Technologies — Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
  (non-commercial research). All architecture — GDLA, Grouped PolyNorm, mHC — and the
  trained weights are theirs, as are the reference fixes (SHA `d2c9ac6`).
- **MLX & `mlx-lm`:** Apple [ml-explore](https://github.com/ml-explore).
- **MLX port, `motif` model class, mixed-precision recipe:** Alis (avlp12), via
  [alis-dwq](https://github.com/avlp12/alis-dwq).

Independent, unofficial derivative — not affiliated with or endorsed by Motif Technologies.
Provided as-is, without warranty. Research / non-commercial use only.

## Citation

> **Alis (avlp12)** (2026). *Motif-3-Beta-Alis-MLX-8bit* — near-lossless 8.503 bpw MLX
> reference build of [Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
> for 512 GB Apple Silicon; the family's KL / eval ground truth.
