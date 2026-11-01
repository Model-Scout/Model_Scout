---
license: other
license_name: upstage-solar-license
license_link: https://huggingface.co/upstage/Solar-Open2-250B/blob/main/LICENSE
base_model: upstage/Solar-Open2-250B
base_model_relation: quantized
library_name: mlx
pipeline_tag: text-generation
language:
- en
- ko
- ja
tags:
- mlx
- solar_open2
- solar-open2
- upstage
- solar
- moe
- quantized
- dwq
- apple-silicon
- mixed-precision
- eval-results
- custom_code
---

# Solar-Open2-250B — Alis MLX Dynamic (DWQ) Builds

**Built with Solar** — this is a derivative of [upstage/Solar-Open2-250B](https://huggingface.co/upstage/Solar-Open2-250B), distributed under the [Upstage Solar License](https://huggingface.co/upstage/Solar-Open2-250B/blob/main/LICENSE). A copy of the license ships in every branch.

MLX (Apple Silicon) port of Solar Open 2 (250B-A15B Hybrid-Attention MoE) in **three** quantization tiers, produced with **[alis-dwq](https://github.com/avlp12/alis-dwq)** — data-aware quantization with teacher-guided distillation (DWQ). Both distilled builds are fine-tuned against the Q8 reference under a per-slice acceptance gate, with an EN sentinel gate as the final safety net.

> ✅ **Status: all three tiers final.** Q v3 (4-bit/g32 + DWQ, lr 5e-7 × 3 rounds): EN loop cleared with teacher-level diversity (distinct4 0.399 vs teacher 0.411), code KLD better than its own base. F v2 (2.34 bpw, 73.3 GB): KLD 0.42 (−76% vs the legacy 2-bit path), all loops clean, EN sentinel ACCEPT. A fourth tier (M, 4-bit/g64) was trained twice (Q-teacher and Q8-teacher) but is **not shipped** — it lost every metric to Q v3 at the same memory tier.

![Solar Open 2 architecture & quantization map — hybrid attention stack [Softmax, Linear×3]×12, MoE 320 routed + 1 shared experts, routers pinned to 8-bit](images/architecture_map.png)

## Builds (branches)

One repo, three weights — pick a branch by machine memory:

| branch | build | recipe | measured bpw | size | fits |
|---|---|---|---|---|---|
| **`main`** | **Q v3** — daily driver, best quality | 4-bit / g32 + DWQ (Q8 teacher, per-slice gate, lr 5e-7 × 3 rounds) | 5.001 | 156.5 GB (145.7 GiB, 31 shards) | **192 GiB** stock (tight) / **256 GiB** comfortable |
| **`t96`** | **F v2** — smallest usable | 2-bit / g128 **experts only** + clip + DWQ rank 8 (Q8 teacher); chokepoints 8b, embed+head 6b, attn/shared 4b via `quant_predicate_builder` | **2.344** | **73.3 GB (68.3 GiB, 15 shards)** + 4.0 GB LoRA adapters | **96 GiB** stock (tight) / **128 GiB** comfortable |
| **`t384`** | **T** — Q8 reference / teacher | 8-bit / g64 | 8.500 | 265.9 GB (247.7 GiB, 62 shards) | **384 GiB** stock / **512 GiB** for full 1M ctx |

*Sizes are decimal GB (10⁹ bytes, as shown on the HF page) with binary GiB (2³⁰ bytes) in parentheses. Measured bpw is computed on the weight shards over 250.29B params; the `t96` adapters (4.0 GB) ship separately and are not fused into the shards.*

![3-tier build lineup — disk size and measured bits per weight](images/build_overview.png)

Every build keeps all MoE router gates at **8-bit / g64 (48/48 layers)** — router quantization was found to be the dominant quality risk, so only expert/attention weights are quantized per the tier recipe. **Why no mid tier?** An M build (4-bit/g64, 131–141 GB) was distilled twice (Q-teacher and Q8-teacher arms). The Q8 arm fixed its EN regression but still lost every metric to Q v3 at the same memory tier (≥160 GB machines), so it is retained locally as a control, not shipped.

## Install & run

> ⚠️ **Requires the `solar_open2` architecture, which is not yet in PyPI mlx-lm (0.31.3).** Stock `pip install mlx-lm` will fail with `ValueError: Model type solar_open2 not supported`. Two options:
>
> ```bash
> # option A — the fork that adds solar_open2 (recommended; the fork's default branch is `solar-open2`)
> pip install "git+https://github.com/avlp12/mlx-lm.git"
> ```
>
> Option B — keep stock mlx-lm and drop the bundled [`solar_open2.py`](solar_open2.py) (shipped in every branch) into `.../site-packages/mlx_lm/models/`. Same file, same result.

```bash
# main = Q v3 (recommended)
mlx_lm.generate --model avlp12/Solar-Open2-250B-Alis-MLX-Dynamic \
  --prompt "안녕하세요, 간단히 자기소개를 해주세요." --max-tokens 512
```

Branch selection (`t96` = F v2, `t384` = T Q8) uses the Python API — the CLI has no `--revision` flag:

```python
from mlx_lm import load, generate

model, tok = load("avlp12/Solar-Open2-250B-Alis-MLX-Dynamic", revision="t96")   # F v2 (77 GB)
# model, tok = load("avlp12/Solar-Open2-250B-Alis-MLX-Dynamic", revision="t384") # T Q8 (266 GB)
print(generate(model, tok, prompt="Explain MoE routing in three sentences.", max_tokens=512, verbose=False))
```

CLI-only alternative: `hf download avlp12/Solar-Open2-250B-Alis-MLX-Dynamic --revision t96`, then point `--model` at the downloaded snapshot directory.

**F v2 LoRA adapters (t96 branch only):** the DWQ compensator adapters ship un-fused in `alis_adapters/` (rank 8). Download that folder and pass `--adapter-path <local alis_adapters dir>` to use them. **All numbers in this card are measured *without* the adapters** (same convention as the control arm), so a fused deployment may do better.

**Chat, reasoning & sampling.** The chat template (`chat_template.jinja`) ships in every branch; `mlx_lm` applies it automatically in chat/server mode (raw `mlx_lm.generate` with a plain string prompt does **not** — apply the template yourself). Client-side settings follow the [base model card](https://huggingface.co/upstage/Solar-Open2-250B): **temperature 1.0 / top_p 1.0** for both reasoning modes — avoid ~0.7-class temperatures, which measurably raise loop/runaway-thinking risk on quantized builds. `reasoning_effort` defaults to `"high"` (thinking ON); use `"none"` for a direct answer (`--chat-template-args '{"reasoning_effort":"none"}'` on `mlx_lm.server`, or the `apply_chat_template` kwarg). Reasoning markers are dedicated tokens `<|think:start|>` / `<|think:end|>` (ids 130/131) — there is **no** `</think>` or `"Final Answer"` convention. Split reasoning from the final answer on `<|think:end|>`, and do **not** add it as a stop token: the answer comes *after* it, and termination is `<|im:end|>` (id 129, already in `generation_config.json`). Budget `max_tokens` for thinking + answer together — thinking typically runs 0.5–2K tokens on chat prompts, so ≥4K total is recommended; an empty answer or a reply cut off mid-thought means the budget ran out inside the reasoning block. **Server + LoRA adapters (F v2):** fork revisions ≤ `9d67a0c` silently **dropped `--adapter-path`** in `mlx_lm.server` — the adapter lookup ran after the model-name remap, always missed, and the server then served the bare 2-bit build. Fixed in `7937fda` (branch `solar-open2`); update the fork, or pass `"adapters": "<local alis_adapters dir>"` in the request body as a workaround.

## Hardware compatibility (memory planning)

Weights are loaded fully into GPU-wired unified memory; context costs extra on top. KV cache ≈ **48 KiB/token** fp16 — only **12 of 48 layers** (the softmax GQA layers, every 4th) hold a KV cache; the 36 KDA linear-attention layers carry a **fixed-size recurrent state (~150 MiB total)** that does not grow with context. → ~4.8 GiB per 100K tokens · 256K ≈ 12 GiB · 1M ≈ 48 GiB.

Default GPU wired limit on macOS ≈ **80% of RAM**; raise it with `sudo sysctl iogpu.wired_limit_mb=<MB>` (revert by lowering again; needs admin). Build footprints below use exact GiB: **F v2 68.3 GiB (+3.9 GiB adapters)** · **Q v3 145.7 GiB** · **T 247.7 GiB**.

| machine RAM | default GPU limit (~80%) | what fits stock | with wired-limit bump |
|---|---|---|---|
| **96 GiB** | ~77 GiB | **F v2** — 한계 직전 (여유 ~5 GiB ≈ 100K tok ctx), bump 권장 | ~88 GiB: F v2 + ~16 GiB ctx (~330K tok) |
| **128 GiB** | ~103 GiB | **F v2** + ~31 GiB ctx (~640K tok) | — |
| **192 GiB** | ~154 GiB | **Q v3** — 한계 직전 (여유 ~8 GiB ≈ 170K tok ctx), bump 권장 | ~176 GiB: Q v3 + ~30 GiB ctx (~630K tok) |
| **256 GiB** | ~206 GiB | **Q v3** + ~60 GiB ctx (**full 1M tok**) | — |
| **384 GiB** | ~309 GiB | **T (Q8)** + ~61 GiB ctx (**full 1M tok**) | — |
| **512 GiB** | ~412 GiB | **T (Q8)** + full 1M ctx | — |

Rule of thumb: pick the largest build whose weights fit your machine with the context you need — quality scales with bits (see the measured table below). DWQ training peak observed: 275 GB wired+compressed during Q v3 distillation (training-only; inference needs are far lower).

> **Note on the HF sidebar panel:** the native *Hardware compatibility* widget indexes only the repo's root model (`main` = Q v3, shown as "4-bit · MLX · 156 GB") — unlike GGUF repos, where every quant file gets its own row, an MLX repo gets a single row and branch builds (`t96`, `t384`) are not indexed. Use the table above for F/T hardware sizing.

## Measured quality (vs Q8 reference, §2-10 eval, ref = T)

| Metric | T (ref) | Q v3 (`main`) | F v2 (`t96`) |
|---|---|---|---|
| KLD — overall | 0 (ref) | **0.06369** (flip 0.0928) | **0.41976** (flip 0.2122) |
| KLD — English | 0 (ref) | **0.04858** (flip 0.0713, **clean**) | 0.30345 (flip 0.1514, **clean**) |
| KLD — code | 0 (ref) | **0.02811** (flip 0.0439) | 0.20571 (flip 0.1426, **clean**) |
| KLD — Korean | 0 (ref) | 0.11438 (flip 0.1631) | 0.75013 (flip 0.3535, **clean**) |
| loop probe (256) | — | **clean (all slices, distinct4 EN 0.399)** ✅ | **clean (all slices, 0.356)** ✅ |
| kv probe (4) | — | selfKL=0.02305, flip=0.0557 | selfKL=0.02195, flip=0.0495 |
| DWQ valid loss (init → final) | — | 0.01597 → **0.01381** (−13.5%, 3/3 accepted) | 0.12102 → **0.07242** (−40.2%) |
| EN sentinel gate (eps=0, cap 1%) | — | mean **−8.8%** (paired 3/16) | **ACCEPT** (−15.9%, no breach) ✅ |

> **Q tier journey (disclosed):** the 4-bit/g32 base shipped a greedy EN loop (len23). Attempt 1 (Q-dwq, legacy scalar gate) made it *worse* (len27) — the scalar gate's blind spot that motivated the per-slice gate. Attempt 2 (Q v2, gate + Q8 teacher, lr 1e-6 × 6 rounds) cleared the loop but collapsed EN diversity (distinct4 0.221) and regressed KLD +6.7% — over-distillation. Attempt 3 (**Q v3**, same gate/teacher but lr 5e-7 × 3 rounds) keeps the loop fix, restores EN diversity to **0.399 (97% of the Q8 teacher's 0.411)**, brings KLD EN back to base level (+0.7%), and improves code KLD **−5.1% below its own base**. The residual trade-off is Korean KLD +8.4% vs base (0.10553 → 0.11438) — see Known Limitations.
>
> **F tier:** the legacy path (uniform 2-bit/g128 base + clip + DWQ) failed the usability gate (KLD 1.23, all slices LOOPED) — a uniform 2-bit predicate destroys the KDA chokepoints and embed/head beyond DWQ recovery. F v2 re-quantizes with `quant_predicate_builder` (chokepoint 8b / embed+head 6b / attn+shared 4b / experts 2b, 578/578 per-layer entries verified) and distills from the Q8 teacher under a per-slice acceptance gate with rank-8 LoRA compensators. Result: KLD 1.73 (legacy base) → 1.23 (legacy DWQ) → **0.42 (F v2 + DWQ)**, all loop probes clean, EN sentinel ACCEPT. The LoRA adapters ship separately (`alis_adapters/`); the numbers above are measured **without** them (same convention as the legacy arm), so a fused deployment may do better.

DWQ training detail: 200 calibration samples (180 train / 20 valid), expert-routing coverage 99.8%; teacher = **Q8 reference for all shipped builds**; deepest-first layer order, 3 rounds (Q v3) / 6 rounds (F v2); per-slice acceptance gate (EN ceiling ε=1%) + EN sentinel gate (paired, cap 1%).

![DWQ teacher distillation — KL loss curves](images/dwq_loss_curve.png)

## Quantization quality (pre-distillation measurements)

**Effective bit utilization** (code-entropy audit, §2-2):

| Metric | M (4-bit/g64) | F (2-bit/g128 clipped) |
|---|---|---|
| Effective bits/weight | 3.72 (93% of nominal) | 1.65 (82% of nominal) |
| Low-entropy groups | 0.0% | 0.5% (concentrated in L0, worst 31.7%) |
| Weak (<50% util) experts | 0 / 144 stacks | 0 / 144 stacks |

![Quantization efficiency — nominal vs measured vs effective bits per weight](images/quant_efficiency.png)

**F clip requantization gate** (T-dequant clipping before 2-bit requant):

| Held-out PPL | Before clip | After clip | Δ |
|---|---|---|---|
| wikitext | 110.56 | **49.51** | **−55.2%** |
| code | 21.81 | **11.63** | **−46.7%** |
| Korean | 23.94 | **18.93** | **−20.9%** |

![F build clip gate — held-out PPL before vs after clipping](images/clip_gate_ppl.png)

## Base model (bf16, official card numbers)

Solar Open 2 is Upstage's 250B-A15B open-weight model: Hybrid-Attention MoE — `[Softmax, Linear×3] × 12` (only 12 of 48 layers hold a KV cache), NoPE on linear-attention layers, 321 experts (320 routed top-8 + 1 shared), vocab 196,608, **1M-token context**, ~12T pre-training tokens, English/Korean/Japanese.

| Benchmark | Solar Open 2 (bf16) |
|---|---|
| MMLU-Pro | 86.2 |
| GPQA-Diamond | 86.3 |
| SWE-Bench Verified | 70.4 |
| AIME 2026 | 95.7 |
| KMMLU-Pro | 78.4 |

(Official numbers from the [base model card](https://huggingface.co/upstage/Solar-Open2-250B); quantized-build deltas are tracked in the KLD table above.)

## Known Limitations

- **Q v3** carries a disclosed **Korean KLD regression** (+8.4% vs its 4-bit/g32 base: 0.10553 → 0.11438) — the price of clearing the base's EN greedy loop while restoring EN diversity. English and code KLD are at or below base level; if your workload is Korean-critical and you can tolerate a known EN loop, prefer the T (Q8) tier or the base model.
- **F v2** is a 2.34 bpw build: Korean KLD (0.75) is materially higher than the Q tier — expected at this bit budget; prefer Q v3 for Korean-heavy workloads. The DWQ LoRA adapters ship un-fused (`alis_adapters/`); all reported numbers are without them.
- **Reasoning-block runaway (root-caused, disclosed):** an external integrator reported F v2 thinking that never closed (22.6K chars, no `<|think:end|>`). This was traced to a **serving bug, not the weights**: fork `mlx_lm.server` ≤ `9d67a0c` silently dropped `--adapter-path`, so that serve ran the **bare 2-bit build without its DWQ LoRA compensators** (fixed in `7937fda`, see Install & run). With adapters actually applied, thinking terminated in **5/5** direct-path runs across both teams — at the official temp 1.0 / top_p 1.0 **and** at 0.7/0.95. Guidance stands regardless: official sampling, generous `max_tokens`, `reasoning_effort="none"` for short direct answers — and treat the adapters as part of the deployed F v2 configuration (a bare serve can ramble).
- **Architecture support:** `solar_open2` is not yet in PyPI mlx-lm (0.31.3) — use the [fork](https://github.com/avlp12/mlx-lm) (default branch `solar-open2`; the adapter-drop fix is `7937fda`) or the bundled `solar_open2.py`.
- Calibration coverage saturates at 200 samples (99.8% expert routing), but median tokens/expert (4,314) is ~19% of the 753B reference run; very rare experts may be under-distilled.
- Quantized builds inherit the base model's knowledge cutoff (2026-02) and language focus (EN/KO/JA).

## License

Distributed under the **Upstage Solar License** (same as the base model). Per the license's derivative-model terms:

- Model name carries the **"Solar"** prefix ✅
- **"Built with Solar"** attribution displayed above ✅
- A copy of the Upstage Solar License is included in this repo ✅

## Credits

- Base model: **Upstage — Solar-Open2-250B** ([Upstage Solar License](LICENSE.upstage-solar)).
- **MLX** & **mlx-lm**: Apple `ml-explore` — `solar_open2` architecture port (KDA hybrid-attention MoE, NoPE, sigmoid-gated GQA): **Alis (avlp12)** ([fork](https://github.com/avlp12/mlx-lm)).
- Mixed-precision DWQ quantization, per-slice acceptance gate + EN sentinel gate, F-tier `quant_predicate_builder` recipe (chokepoint 8b / embed+head 6b / attn+shared 4b / experts 2b): **Alis (avlp12)** ([alis-dwq](https://github.com/avlp12/alis-dwq)).

## Citation

```bibtex
@misc{solar-open-2-2026,
  title={Solar Open 2 Technical Report},
  author={Upstage AI},
  year={2026},
  url={https://huggingface.co/upstage/Solar-Open2-250B}
}
```

