---
license: apache-2.0
base_model: huihui-ai/Huihui-Qwen3.8-27B-abliterated
base_model_relation: quantized
pipeline_tag: image-text-to-text
library_name: gguf
language:
- en
- zh
tags:
- qwen3
- qwen3.8
- uncensored
- abliterated
- gsq
- rco
- gguf
- quantized
- speculative-decoding
- mtp
- text-generation
- multilingual
- multimodal
- vision
- conversational
- long-context
- tool-use
- 16gb-vram
model-index:
- name: Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored
  results:
  - task:
      type: text-generation
    dataset:
      name: needle-retrieval-15k
      type: custom
    metrics:
    - name: exact-match
      type: exact_match
      value: 6/6
  - task:
      type: text-generation
    dataset:
      name: toolcall-json-pi-path
      type: custom
    metrics:
    - name: pass-rate
      type: pass_rate
      value: 8/8
---

# Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored

A 3-bit GGUF quant of the abliterated Qwen3.8-27B, built to hold full 196K context on a single 16 GB GPU. Sibling size class carries ISTA-DASLab's full-size AIME/GPQA numbers; this file trades recall for residency and says so below.

A 9.73 GiB, mixed-precision GSQ/RCO quant of Huihui's refusal-reduced Qwen3.8-27B, preserving the MTP head and validated for 16 GB GPUs.

This is a **quantization of `huihui-ai/Huihui-Qwen3.8-27B-abliterated`**, not a new fine-tune. The underlying model is Qwen3.8-27B; the refusal ablation comes from Huihui; the quantization work here follows the GSQ/RCO methodology developed by ISTA-DASLab. The checkpoint is designed to substantially reduce learned refusal behavior. This is not a guarantee of universal compliance — the deployer is responsible for compliant use.

## Quick specs

| | |
|---|---|
| Base | `Qwen/Qwen3.8-27B` via `huihui-ai/Huihui-Qwen3.8-27B-abliterated` |
| File | `Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored-v1.1.gguf` (v1.1 release; v1 `-MTP.gguf` superseded) |
| Size | 10,466,420,544 bytes (9.75 GiB) |
| Tensors | 866 (65 blocks: 64 layers + MTP head) |
| bpw | 3.058 (bytes×8 ÷ 27,320,697,856 params) |
| MTP head | Present - 15 `blk.64.*` weights incl. `nextn.eh_proj/enorm/hnorm/shared_head_norm`, verified non-empty, draft-accept 0.46-0.95 by workload logged against this exact file |
| Template | `froggeric-qwen3.8-tool-use.jinja` (local file header v22.5; upstream repo may still show v22.4) |
| Context | 196K resident-fit on 16 GB (`q4_0` KV, verified loaded); quality gates ran at 32K server ctx + 64K needle ctx — **known gap:** full-196K retrieval accuracy is under active evaluation, do not treat as 196K-verified |

## What I changed

Starting from the abliterated checkpoint, I produced this GGUF using a GSQ/RCO-based non-uniform allocation and IQ3_XXS packing. This isn't a generic `IQ3_XXS` conversion: sensitive tensors (SSM gates, embeddings, attention gates — 96 tensors) are held at BF16 while the bulk rides the GSQ-coded grid.

The important honesty clause: I **reproduced ISTA-DASLab's published per-tensor allocation map** for Qwen3.8-27B and applied it to the abliterated weights. I did not independently re-run the multi-GPU RCO budget search. Same map, different base.

I also tried custom importance-matrix blends during the process (fresh + syncretized). They looked promising and then failed needle retrieval outright (0/6 timeouts), so I threw them out and kept the official ISTA imatrix. If a change makes the benchmark prettier but the model worse to actually use, it doesn't ship.

## Tested performance (RTX 5070 Ti 16 GB, [build2](https://github.com/RentedNoodle/den_llama.cpp) llama.cpp, this exact file)

| Configuration | Decode | Notes |
|---|---|---|
| Serial / no spec | ~39.6 t/s | 400-tok prose, thinking on |
| MTP `n-max 2` | ~59.3 t/s | +50%. Ship default. Accept 0.46-0.95 by workload (code peaks, prose dips), mean len 1.9-2.9 |
| MTP `n-max 2` + `--fit off` + `--spec-draft-backend-sampling` + `-b 1024` | 69–82 t/s | Ship flags. The `--fit off` alone was worth +38% |
| MTP n-max 3 / 4 (+p-min) | 33–37 t/s | Higher acceptance yet slower — verification cost wins. Don't use |
| KV `iq4_nl` | 26.8 t/s | No fast kernel in this build. Don't use |
| KV `q4_0/q4_0` | ship | 15.8/16 GB resident |

Higher acceptance does not automatically mean higher throughput. The verification cost matters — measure tok/s, not just accept rate.

| Suite | Score | Setup |
|---|---|---|
| Needle retrieval | 6/6 | 15K-word haystack, depths 0.1–0.9, temp 0.0, 64K server ctx |
| Toolcall v1 (Pi JSON path) | 8/8 | `tool_call_format=json` |
| Toolcall v2 (args + must-not-fire + chains, full 14-case) | 9/14; negatives 4/4 clean | Fails: `tc-04` bash-vs-grep, `tc-08` read-vs-edit, `tc-07` noparse, `tcc-01/02` chain-miss. Trunk bit-identical to v1, so unchanged by the head work |
| Livebench-style | 12/12 | reasoning/coding/extraction mix |
| Coherence | 4/4 | multi-turn continuity |
| WikiText-2 perplexity (test) | 6.63 | single-harness measurement on this file; no identical-harness BF16 baseline measured here, so do not read as 'beats BF16' |

Temp ships at 0.6 (4/8 vs 3/8 raw-template A/B; favored for tool-use reliability in agentic loops). Reasoning: medium default, low for short code, xhigh for verifiable-correctness only.

Academic benchmarks (AIME/GPQA/LiveCodeBench) for this specific file: pending, will append. For reference, ISTA-DASLab's same-bpw base reports AIME25 100.0 / GPQA-Diamond 88.89 / LiveCodeBench v6 84.57 — their base, not this file.

GPQA-Diamond (this file): **60.6% no-thinking / 61.6% thinking-on** (pass@1, 2048-token budget) vs ISTA's 88.89 (generative xhigh harness, stock base). The gap is **harness + abliteration**, not quantization. (See Ablerlitics, Sept 2026: Huihui is the reliable classic ablation - follows ~3/4 requests, reasoning preserved, some content still refused. Not 'surgical tier'.)

## v1.1 MTP head (trained draft head)

The native MTP head is strong, but I fine-tuned it on a 4M-token self-distilled corpus to improve draft accuracy. This required a mathematically exact PyTorch mirror of `graph_mtp` — the v1.1 line resolved three silent divergences (gated-attention Q/gate interleave, NEOX RoPE pairing, float32 RMSNorm accumulation) plus two GGUF-plumbing bugs (F32 norm preservation + `mul_mat` flat-layout orientation) before any training was meaningful.

| Metric | v1 native head | v1.1 trained head | Delta |
|---|---|---|---|
| Offline k1 (held-out, never-trained-on) | 0.4806 | **0.7660** | **+28.5pt** |
| Offline top5 | 0.763 | **0.925** | +16pt |
| Serve t/s (identical ship flags, median-of-3) | 70.68 | **75.15** | **+6.3%** |
| Draft acceptance | 0.636 | 0.620 | flat |

The offline k1 gain is large and generalizes (measured on a different distribution than trained on). Serve-time throughput at `n-max 2` is bounded by verification cost, so the head's drafting advantage shows as a modest +6.3% — not a one-to-one map of the offline gain. Needle 6/6 re-verified on the trained-head build.

## Usage

Froggeric template is required for the intended tool/reasoning behavior (`tool_call_format=json` for the certified path; template default is xml).

```bash
llama-server \
  -m Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored-v1.1.gguf \
  --alias Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored \
  --jinja --chat-template-file froggeric-qwen3.8-tool-use.jinja \
  --ctx-size 196608 -fa on -ctk q4_0 -ctv q4_0 \
  -ngl 99 -b 1024 -ub 1024 -np 1 -t 8 --fit off \
  --reasoning-budget 256 --spec-type draft-mtp --spec-draft-n-max 2 \
  --spec-draft-backend-sampling
```

Vision: projector files live in this repo under `mmproj/` (BF16 or Q8_0). Start the server with one, then send a multimodal chat request (skip both flags for text-only):
```bash
llama-server -m <gguf> --mmproj mmproj/mmproj-Qwen3.8-27B-BF16.gguf --ctx-size 65536 [same flags as above]
# then POST /v1/chat/completions with content blocks including {"type":"image_url",...}
```

Ollama (text generation supported; tool/reasoning behavior uncertified — use llama-server + Froggeric for that):
```dockerfile
FROM ./Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored-v1.1.gguf
PARAMETER num_ctx 196608
PARAMETER num_gpu 999
```

## Honest limitations

Aggressive 3-bit quant — don't expect BF16 behavior. Knowledge recall is weaker than higher-bit variants (the model leans on retrieval/tools instead). MTP output may differ from serial generation on quantized targets; fix the seed and runtime config for reproducibility, disable spec when exact serial behavior matters. Vision + long context gets tight on 16 GB (split text/vision profiles or offload the projector). The imatrix was computed on the stock base, not the abliterated weights — whether that shift matters is untested, not assumed safe. Base model (Huihui) exhibits a known ~3pp TruthfulQA degradation common to standard multi-layer ablations (Abliterlitics, Sept 2026); users should verify critical facts in long agentic chains.

## Files in this repo

| File | What |
|---|---|
| `Qwen3.8-27B-GSQ-RCO-IQ3_XXS-Uncensored-v1.1.gguf` | The quant (SHA256 in `SHA256SUMS.txt`) |
| Vision projector | `mmproj/mmproj-Qwen3.8-27B-BF16.gguf` (0.87 GB) + Q8_0 alt (0.60 GB, 27 tensors fallback-quantized) |
| `froggeric-qwen3.8-tool-use.jinja` | Required chat template |
| `REF-IQ3_XXS-mtp.rco-allocation.txt` | 866-row per-tensor allocation map (authoritative over any summary) |
| `imatrix.dat` | ISTA-DASLab's published calibration matrix as used |
| `SHA256SUMS.txt` | Hashes |
| `LICENSE` | Upstream Apache-2.0 terms apply; see Qwen/Huihui repos |

GGUF embeds tokenizer metadata — no separate tokenizer needed for llama.cpp/Ollama/LM Studio/Pi.

## Credits

- **Qwen** — architecture + pretrained weights: [Qwen3.8 repo](https://github.com/QwenLM/Qwen3.8), [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)
- **Huihui** — abliterated checkpoint ([model](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated)), via [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers)
- **GSQ** — Dadgarnia, Tabesh, Nikdan, Helcig, Kurtic, Kleinegger, Alistarh (2026): [paper](https://arxiv.org/abs/2604.18556), [code](https://github.com/IST-DASLab/GSQ)
- **RCO** — Helcig & Alistarh (2026): [paper](https://arxiv.org/abs/2605.00649), [code](https://github.com/IST-DASLab/RCO)
- **ISTA-DASLab quant release** — [Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF) (allocation + imatrix source)
- **Froggeric** — [Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)
- **llama.cpp/GGML** — [runtime + format](https://github.com/ggml-org/llama.cpp); IQ3_XXS is their standard type, nothing custom here

## Reproducibility

- Base: `huihui-ai/Huihui-Qwen3.8-27B-abliterated`
- Allocation: `REF-IQ3_XXS-mtp.rco-allocation.txt` (in this repo), applied via `llama-quantize --tensor-type-file`
- Imatrix: `imatrix.dat` (in this repo), ISTA-DASLab's published matrix as used
- Runtime: [den_llama.cpp](https://github.com/RentedNoodle/den_llama.cpp) @ `3231ee89` (build2; `-DGGML_CUDA_FA_ALL_QUANTS=ON`, CUDA 13.3)
- GPU: RTX 5070 Ti 16 GB, Windows 11, driver per `nvidia-smi` at run time
- Evals: prompts in `evals/prompts/` (hashes in `evals/SHA256SUMS`), commands in `evals/commands.md`, raw outputs + timings + accept stats in `evals/raw/`

## Versions

### Changelog
* **v1.1 (current):** fine-tuned MTP head (+28.5pt offline k1, +6.3% serve-time t/s). Added WikiText-2 perplexity validation (6.63). Reconciled 14-case toolcall suite (9/14). Trunk bit-identical to v1 — no base intelligence lost or altered.
* **v1.0:** initial release. GSQ-RCO IQ3_XXS allocation applied to Huihui abliterated base. Needle 6/6, MTP intact.

### Roadmap
* **v1.2 (Huihui line) — on hiatus.** We are pivoting to an OrcaRouter base for v2.0 (surgical abliteration, cleaner TruthfulQA retention, natively uncensored MTP head). No further Huihui-line releases planned; v1.1 is the final Huihui build.
* **v2.0 (planned):** rebuild on `orcarouter/Qwen3.8-27B-Uncensored` — custom protected allocation for its 131 edited tensors, requant, needle-gated, plus concurrent MTP-head fine-tuning on the already-uncensored OrcaRouter head. This card updates on release.

Community quant, not affiliated with Qwen, Huihui, or ISTA-DASLab. Bug reports: include model revision, llama.cpp build, ctx/KV/spec settings, sampler. "Feels worse" is fine; reproducible info makes it actionable.
