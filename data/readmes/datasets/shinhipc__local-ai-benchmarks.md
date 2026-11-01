---
license: cc-by-4.0
language:
  - ko
  - en
pretty_name: "HighLife PC Local AI Field Benchmarks (2026-10)"
tags:
  - benchmark
  - local-llm
  - inference
  - gpu
  - quantization
size_categories:
  - n<1K
configs:
  - config_name: default
    data_files: benchmarks.csv
---

# HighLife PC — Local AI Field Benchmarks (October 2026)

> 🇰🇷 한국어 설명: [README_ko.md](./README_ko.md)

**HighLife PC** is a computer shop in Cheonan, South Korea. We run several local AI servers for day-to-day store work,
and this dataset collects numbers we **measured ourselves, on our own machines, with our own settings** — not vendor spec sheets.
A few vendor/third-party figures are included only for context and are clearly marked in the `source_type` column as `외부(...)` ("external").

- Rows: 273 (249 own measurements, 24 external reference values). Ids run M001–M279; the 6 ids removed from the public version are left empty.
- Period: 2026-10-12 to 2026-10-27
- Topics: LLM inference speed (prefill, decode, concurrency), power & temperature, quantization, long context & conversation cache, accuracy (GSM8K, in-house items), coding-agent scores, image generation speed, Korean embedding retrieval
- Text fields are mostly Korean; `metric_key` is an English identifier. A short glossary is below.

## Hardware

| Code | Configuration | Main workload |
|---|---|---|
| DEV-A | RTX PRO 5000 48GB ×1 · Core i7-14700KF · DDR5 128GB · PCIe 5.0 x16 · Ubuntu | Qwen3.8-Flash-Next (MoE) on Strata |
| DEV-B | RTX 5090 32GB ×2 · Threadripper 2950X (X399) · DDR4 128GB · PCIe 3.0 x16 · Linux | 27B chat model (NInfer) + image generation; dual-GPU Strata trial |
| DEV-C | ASUS Ascent GX10 (NVIDIA GB10) ×4, switchless ring | DeepSeek-V4.1-Flash on SGLang (TP=4) |
| DEV-D | RTX 5090 32GB ×1 (also drives the display) · 128GB RAM · Windows | Quantization comparison on 10-16; 10-12 agent tests (placement estimated). Configuration no longer exists |
| DEV-E | RTX PRO 5000 48GB in DEV-B chassis, PCIe 3.0 x8 slot | Configuration at the time of the 10-12 agent tests (estimated) |

`DEV-B1` = one RTX 5090 of DEV-B, `DEV-Bcpu` = CPU of DEV-B only, `EXT` = not our hardware (external values or cloud models).

## Key results

### 1) One 48GB card + 128GB RAM serving Qwen3.8-Flash-Next (DEV-A, Strata 0.1.50, final production config on 2026-10-27)
IQ4_XS, 524K context, 2 parallel slots, 300W power limit. Speed and the 479K read were measured with a 6GB conversation cache; the resume test was run later the same day after raising the cache to 20GB and the engine memory limit to 120GB.

| Metric | Value |
|---|---|
| Decode, 1 user | 150–179 tok/s |
| Decode, 2 users (sum) | 204 tok/s |
| Prefill 11K / 22K | 4,900–4,980 / 5,260–5,380 tok/s |
| Read a 479,096-token document | 104.5 s (4,599 tok/s), hidden note found |
| Resume a 480K-token conversation (cache hit) | 0.8–1.6 s (first read 105–109 s) |

### 2) Aggregate decode vs. number of concurrent users (short prompts)

| Machine · engine · model | 1 | 2 | 4 | 8 |
|---|---|---|---|---|
| DEV-A · Strata · Flash-Next IQ3_S (1M × 4 slots) | 150 | 171 | 230 | (out of RAM) |
| DEV-B 5090×2 · Strata · Flash-Next IQ3_S (parallel 8) | 179 | 185 | 243 | 317 |
| DEV-B1 5090×1 · NInfer (new) · 27B with MTP | 127 (Korean) | 252 | – | 608 |
| DEV-C GX10×4 · SGLang · DeepSeek-V4.1-Flash | 65.6 | – | 145.8 | – |

Models differ in size and architecture — read this as "how each setup scales with users", not as a hardware ranking.

### 3) GPU power limit (DEV-A, 2026-10-23, mixed full load for 15+ min per step)

| Limit | Short-prompt decode | Prefill sum under load | Avg power | Max temp |
|---|---|---|---|---|
| 250W | 143.7 | 3,923 | 239.9W | 82°C |
| 285W | 140.3 | 4,113 | 265.8W | 85°C |
| 300W | 142.9 | 3,863 | 275.0W | 87°C |

No difference under mixed load, but for a **single long prefill (16K) 300W was ~6% faster** than 250W (4,900–5,085 vs 4,600–4,710 tok/s, 10-27).

### 4) GSM8K by quantization (DEV-A, 200 problems, thinking on)

| Quant | Correct | Wall time |
|---|---|---|
| IQ3_S (official) | 197/200 (98.5%) | 476 s |
| IQ4_XS (Orca derivative) | 196/200 (98.0%) | 539 s |
| UD-IQ4_XS (Unsloth) | 195/200 (97.5%) | 572 s |

### 5) Coding agents — same model, different harness (self-made test, 35 problems, scaled to 100, 2026-10-23)

| Model | Harness | Hard 5 | General 30 | Avg 35 |
|---|---|---|---|---|
| DeepSeek-V4.1-Flash (DEV-C) | Hermes Agent | 84.1 | 97.7 | 95.8 |
| DeepSeek-V4.1-Flash (DEV-C) | DSH 0.2.1-rc.2 | 93.9 | 98.7 | 98.0 |
| DeepSeek-V4.1-Flash (DEV-C) | Pi 1.3.0 | 96.3 | 98.5 | 98.2 |
| Qwen3.8-Flash-Next IQ3_S (DEV-A) | DSH | 84.7 (2nd run 95.9) | 99.4 | 97.3 |
| Qwen3.8-27B (DEV-B1) | DSH, PYTHONUTF8 off → on | 36.8 → 90.4 | – | – |
| Claude Opus (cloud, reference) | Claude Code | 96.3 | 98.9 | 98.5 |

This is a self-made test; **the problems are not released** — only scores.
Re-running the same setup moved scores by about ±5 points, so 1–2 point gaps should be treated as ties.

### 6) Image generation (DEV-B1 RTX 5090, ComfyUI 0.42, 1024×1024)

| Model | Sec / image | Peak VRAM | Korean text (2 lines) |
|---|---|---|---|
| FLUX.3 image klein (NVFP4) | 2.6–2.9 | ~10GB | 2/2 correct |
| Edit: klein vs Qwen-Image-Edit-2511 | 5.6–5.8 vs 19.1 | 10.9 vs 29.6GB | – |

## Columns

| Column | Meaning |
|---|---|
| id | Row id (M001…) |
| group | Test group name (Korean) |
| date | Measurement date; external rows show e.g. `(공식 발표)` = "official announcement" |
| device / device_spec | Machine code and public specs |
| engine | Inference engine and version/commit |
| model / quant | Model and quantization |
| settings | Key settings (context, parallel slots, power, cache, …) |
| metric_key / metric_ko | Metric id (English) / Korean label |
| value | Value exactly as recorded (`a~b` range, `197/200` fraction, `2.49→0.44` before→after) |
| value_min / value_max | Numeric columns, filled only for single numbers or ranges |
| unit | Unit (`초` = seconds, `점` = points, `문항/문제` = items) |
| method | One-line method (Korean) |
| source_type | `자체측정` own, `자체측정(클라우드 모델)` own run on a cloud model, `외부(공식 발표)` vendor, `외부(공개 보고)` public report, `외부(타인 측정)` third-party doc, `외부(공개 자료)` public data |
| notes | Caveats, corrections, context (Korean) |

## Methodology

- **LLM speed**: our own Python scripts streaming to OpenAI-compatible endpoints, thinking off, temperature 0.6.
  - prefill tok/s = input tokens ÷ time to first token (includes request overhead)
  - decode tok/s = output tokens ÷ time after first token
  - N concurrent = N identical short prompts in parallel, per-user speeds summed
  - Some rows use engine-log values (see `method`). With speculative decoding (MTP etc.) client-side chunk counts under-count tokens, so engine logs were preferred there.
- **Power test**: per step 3 short prompts, 3 × 2,000-token answers, 15+ min of 2-user full load, 3 min rest between steps, fixed case fans.
- **GSM8K**: first 200 problems of the public test split (openai/grade-school-math), thinking on, temperature 0.6, max 6,144 tokens, 2 parallel. The number on the "Answer:" line (else the last number) is compared; failed requests count as wrong.
- **In-house quality items**: 69 items (chat 20, tool calls 15, knowledge/reasoning 14, lawful-but-sensitive 17, long docs 3); rule-based grading + blind grading by another local model.
- **Coding agents**: self-made test, 35 tasks (not released), same instructions, automated tests + human review, one attempt per task. The 25- and 30-task agent tests of 10-12 are also self-made.
- **Images**: fixed seed, identical English scene prompts, per-image time excluding the first (model load), peak per-process VRAM from nvidia-smi.
- **Embedding retrieval**: 51 store product/info docs, 40 customer-style Korean queries, top-1 / top-3 hit rate.

## Limitations

- **Do not mix vendor claims with our measurements.** Rows whose `source_type` starts with `외부` are context only; we did not reproduce them.
- Small samples: mostly 1–5 runs; ±5–10% run-to-run variation was common (the 4-node ring's code decode ranged 57–111 tok/s, so medians of 5 were used).
- Rows often differ in model, quant, engine version and context — always read `settings`.
- These are production servers; some rows may include background traffic (noted in `notes`).
- Coding/agent/quality tests are self-made and not released; only scores are.
- Some models are community derivatives (e.g., refusal-direction removed); results may differ from the base model.
- Where our logs contain a correction, only the corrected value is included; for repeated identical measurements the latest value is used.
- The 10-12 agent tests ran on an earlier hardware layout; part of that placement is estimated from our logs (marked "추정" = estimated in `notes`).
- Some image-model rows were removed from the public version.

## License

CC-BY-4.0 — commercial reuse allowed with attribution. Please cite as "HighLife PC Local AI Field Benchmarks (2026-10)".
Model and engine licenses follow their respective distributors.

## Contact

HighLife PC (Cheonan, South Korea) · Instagram [@hipc.ai](https://www.instagram.com/hipc.ai/)
