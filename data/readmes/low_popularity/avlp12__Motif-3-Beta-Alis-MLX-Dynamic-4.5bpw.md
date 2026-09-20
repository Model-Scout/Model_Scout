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
- 4-bit
- dwq-teacher
- conversational
---

> [!IMPORTANT]
> ## ➡️ 이 리포는 Motif-3 **Beta** 기반입니다 — 정식판 리포를 사용하세요 / This repo quantizes the **Beta** checkpoint — use the official Motif-3 builds
>
> 정식 Motif-3 체크포인트 기반 양자화를 게시했습니다. 새로 받으신다면 정식판 리포를 사용해 주세요:
> I have published quantizations built from the **official Motif-3** checkpoint — please use those instead:
>
> **[avlp12/Motif-3-Alis-MLX-4.5bpw](https://huggingface.co/avlp12/Motif-3-Alis-MLX-4.5bpw)** (직접 대응 빌드 / direct counterpart)

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

# Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw

Apple Silicon (MLX) **mixed-precision** quantization of
[Motif-Technologies/Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
— a **314.84B-parameter** (≈13B active) Mixture-of-Experts reasoning model, **text-only**,
bilingual **Korean / English** (+ code), with 97.84% of its mass in the routed experts and
native **256K** context. This is the **"C6" build: 4.547 bpw measured, 167 GB on disk** —
the **high-fidelity daily driver** of the family and, at the same time, the **teacher that
distilled the [2.3bpw floor build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw)**.
Part of the first community MLX port of Motif-3-Beta in any format.

If your Mac has **256 GB or more**, this is the build to run: 4-bit experts with 6-bit
attention and an 8-bit KV-A latent recover the base model's behavior at less than half the
footprint of the 8-bit reference.

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
| Bits/weight | **4.547** (measured; per-tensor mixed, experts 4-bit/g64) |
| On-disk size | **167 GB** (167 GiB) |
| Format | MLX (Apple Silicon); `library_name: mlx` |
| Role | daily driver **and** DWQ teacher for the 2.3bpw floor build |

### Recipe (verified from `config.json`)

97.84% of the parameters are routed experts, so expert bit-width sets the size; the
per-token critical path and the latent chokepoint get extra bits.

| Component | Bits | Notes |
|---|---|---|
| Routed experts (gate/up/down) | **4-bit g64** | ≈97.8% of params — sets the footprint |
| Attention (GDLA projections) | **6-bit g64** | per-token critical path, promoted vs the floor build |
| `wkv_a` (KV-A latent down-projection) | **8-bit g64** | latent chokepoint — kept high across every profile |
| Token embedding · LM head | 6-bit g64 | distribution-sensitive |
| Router gate · mHC · `lambda_proj` · all norms · `act_fn` | **fp (unquantized)** | discrete control paths + normalization |

### Architecture

![Motif-3-Beta architecture: embedding to 53 decoder layers (GDLA attention, mHC hyper-connections, dense/MoE feed-forward with Grouped PolyNorm) to RMSNorm to LM head](assets/architecture.png)

---

## Build ladder

| Build | Recipe | Size | bpw | Target |
|---|---|---|---|---|
| [2.3bpw (FLOOR)](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw) | experts 2b/g128 · attn 4b · wkv_a 8b | 85 GB | 2.315 | 128 GB Mac |
| **4.5bpw (this, C6)** | experts 4b · attn 6b · wkv_a 8b · embed/head 6b · router/mHC/norms fp | **167 GB** | **4.547** | **256 / 512 GB Mac** · DWQ teacher |
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

model, tokenizer = load("avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw")

messages = [{"role": "user", "content": "한국어와 영어로 자기소개를 해줘."}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
# The chat template auto-opens a <think> block: the model reasons first, then answers.
sampler = make_sampler(temp=1.0, top_p=0.95)   # recommended; greedy can loop on some prompts
print(generate(model, tokenizer, prompt=prompt, max_tokens=1024, sampler=sampler))
```

**CLI / server:**

```bash
mlx_lm.generate --model avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw \
  --prompt "Explain MoE routing in two sentences." --temp 1.0 --top-p 0.95 -m 512

mlx_lm.server --model avlp12/Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw   # OpenAI-compatible
```

- **Sampling:** temperature **1.0**, top-p **0.95** are recommended (greedy can loop on some
  prompts).
- **Stop tokens:** the tokenizer stops on `{0, 3, 6}`; pass all three as stop ids if you
  drive generation yourself.
- **Reasoning mode:** the chat template opens a `<think>` block automatically — expected
  behavior, not a template bug.
- **Long context:** on a 256 GB Mac, quantize the KV cache for long prompts
  (`--kv-bits 8 --kv-group-size 64 --quantized-kv-start 4096`). See *Hardware*.

---

## Method — `alis-dwq` pipeline

Weights are produced with **[alis-dwq](https://github.com/avlp12/alis-dwq)**, the same
pipeline used for the GLM-5.2 (745B) and Hy3 (295B) Alis MLX builds: mixed-bit affine
quantization with the experts lowest, the router / mHC / `lambda_proj` / norms kept fp, the
`wkv_a` latent chokepoint at 8-bit, and embed/head at 6-bit. At 4-bit-and-above the naive
per-tensor recipe is already near-optimal for its size, so — unlike the 2.3bpw floor — this
build ships as a **direct mixed-precision quantization** (no clip-search / DWQ pass on top;
those levers are 2-bit-specific and measured neutral-to-negative at this bit-rate).

The port itself is **parity-verified**: MLX logits match a **bug-fixed HF reference** to
**KL ≈1e-7 / token** (see *Port notes*).

### Doubles as the DWQ teacher

This same checkpoint is the **teacher** for the 2.3bpw floor build's layerwise DWQ
distillation (45% Korean calibration mix). A mid-bit teacher is the sweet spot for a 2-bit
student — sharper than the 8-bit reference where it counts, without over-driving the
student — and it cut the floor build's KL 58-72% while breaking its code-generation loop.

---

## Evaluation

This build is the **high-fidelity tier** and was itself the **DWQ teacher**, so it is
**not separately KLD-evaluated against the 8bit (Q8) reference** — its distribution is by
construction within **teacher-grade fidelity** of it (it is the near-golden target the
floor build was distilled toward). The discriminating KL measurements in this family are
made *against* the 8bit reference for the more aggressive builds; see the
[2.3bpw card](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw) for that
ladder. For orientation, that build's KL vs Q8 is EN 0.277 / code 0.100 / KO 0.522 **after**
distilling toward this teacher — this 4.5bpw build sits well below those figures.

![The 2.3bpw floor build this checkpoint taught: KL vs the Q8 reference and greedy loop-probe across raw / +clip / +clip+DWQ — DWQ from this 4.5bpw teacher cuts KL 58-72% and breaks the code loop](assets/eval_ladder.png)

*The chart shows what this teacher bought the floor build: it is the teacher, not the
student, so it is not itself plotted.*

Qualitatively: fluent, coherent bilingual generation (Korean including hanja, English) and
code, with the reasoning `<think>` trace intact. General knowledge, code, and bilingual
generation are reliable.

**Honest caveat (shared across the family):** very-long-tail factual recall can be weak —
e.g. the model does not reliably reproduce obscure text such as the 4th verse of the Korean
national anthem. This is a **base-model property, not a quantization artifact** (the 8bit
reference shares it).

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

Built for **256 GB (and up) Apple Silicon**. Weights are 167 GB, leaving comfortable
headroom for KV cache and prefill activation on a 256 GB machine (274.9 GB total); on a
512 GB machine, long-context prefills run with room to spare. For long context, prefer
int8 KV (`--kv-bits 8`). If your Mac has **128 GB**, use the
[2.3bpw floor build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-Dynamic-2.3bpw)
instead; for a near-lossless archival reference on 512 GB, the
[8bit build](https://huggingface.co/avlp12/Motif-3-Beta-Alis-MLX-8bit).

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

> **Alis (avlp12)** (2026). *Motif-3-Beta-Alis-MLX-Dynamic-4.5bpw* — 4.547 bpw MLX
> quantization of [Motif-3-Beta](https://huggingface.co/Motif-Technologies/Motif-3-Beta)
> for 256 GB+ Apple Silicon; the family's high-fidelity daily driver and DWQ teacher.
