---
license: apache-2.0
base_model:
  - heretic-org/Qwen3.8-27B-heretic-ara
base_model_relation: quantized
datasets:
  - Crownelius/Creative_Writing_ShareGPT_Enhanced
  - microsoft/rStar-Coder
  - peteromallet/dataclaw-peteromallet
  - Crownelius/Opus-4.7-Reasoning
  - openbmb/UltraData-Math
  - Crownelius/Crow-Heretic-TeichAI-Unified
language:
  - en
  - zh
  - ru
  - es
  - fr
  - it
  - ja
  - ko
  - de
  - ar
  - tr
  - pl
  - sv
  - nl
  - he
  - id
  - uk
  - fa
  - pt
  - ms
  - fi
  - el
tags:
  - qwen38
  - dense
  - conversational
  - multimodal
  - agent
  - gguf
  - ollama
  - heretic
  - uncensored
  - reasoning
  - distillation
library_name: gguf
pipeline_tag: text-generation
---

<img src="https://huggingface.co/FoolDev/Thanatos-27B-HERETIC/resolve/main/banner.svg" alt="Thanatos-27B banner" width="100%" />

[![License](https://img.shields.io/badge/License-Apache_2.0-7aa2f7?style=flat&labelColor=1a1b26)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base-Heretic_ARA-bb9af7?style=flat&labelColor=1a1b26)](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara)
[![Architecture](https://img.shields.io/badge/Arch-Dense_27B-ff9e64?style=flat&labelColor=1a1b26)](#architecture)
[![Sibling](https://img.shields.io/badge/Sibling-Janus--35B-7dcfff?style=flat&labelColor=1a1b26)](https://huggingface.co/FoolDev/Janus-35B-HERETIC)

<a href="https://buymeacoffee.com/cardoffoolm"><img src="https://huggingface.co/FoolDev/Thanatos-27B-HERETIC/resolve/main/bmc-banner.svg" alt="Buy me a coffee — support Thanatos-27B" width="320" /></a>

# Thanatos-27B

> **Dense Reasoning. Friendlier Footprint. Uncensored.**
> *heretic-org's Heretic (ARA) abliteration of Qwen 3.8 27B (dense), repackaged with Claude Fable 5 in the teacher slot.*

**`Architecture:`** `Qwen 3.8 27B (Dense)` | **`Parameters:`** `27B` | **`Context:`** `262,144 native / 1,010,000 extensible` | **`Base:`** `Heretic ARA (heretic-org)` | **`Teacher:`** `Claude Fable 5` | **`Type:`** `Distilled + Abliterated LLM`

A personal sibling to [`FoolDev/Janus-35B-HERETIC`](https://huggingface.co/FoolDev/Janus-35B-HERETIC), which since its 0.9.0 is a **Qwen 3.6 35B-A3B MoE** — so the two are genuinely different models, not two abliterations of one base (see [Janus vs Thanatos](#janus-vs-thanatos)). This one is the **dense** [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B), sharing the teacher (Claude Fable 5) and dataset family, built on [`heretic-org/Qwen3.8-27B-heretic-ara`](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara), an uncensored Heretic **ARA-method** abliteration, with refusal-trained behavior dialed back at the base layer. (The sibling's `-35B-` slug names its model correctly again.)

> **Provenance.** This repo repackages and quantizes — **no training is performed
> here.** What ships is [`heretic-org/Qwen3.8-27B-heretic-ara`](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara) converted to GGUF and MTP-stripped so stock
> llama.cpp and Ollama can load it. The `Teacher:` field above and the `datasets:`
> list in the frontmatter are carried over from earlier revisions of this card.
> **The current base does not claim them** — its card lists no datasets and names
> no teacher — and nothing in this repo reproduces or measures them. One listed
> dataset, `Crownelius/Opus-4.7-Reasoning`, is not publicly reachable: the Hub
> answers 401, as it does for a private or missing repo. Treat them as unverified
> attribution, not as a training record.
> `base_model_relation` is `quantized` for the same reason.

## TL;DR

One-liner via Hugging Face (pulls a GGUF + this repo's root-level
`template` / `system` / `params` files, including the tool-calling
template — HF's Ollama bridge ingests those three files, not
`Modelfile`):

```bash
ollama run hf.co/FoolDev/Thanatos-27B-HERETIC           # ~17 GB Q4_K_M, qwen35-stamped, loads on stock Ollama
```

> **Bundled blob status:** the bundled `Thanatos-27B.Q4_K_M.gguf` is the
> heretic-ara Q4_K_M quant (from
> `mradermacher/Qwen3.8-27B-heretic-ara-GGUF`), `qwen35`-stamped and
> verified against the Architecture claims below (`make verify-arch`). Pulling
> `hf.co/FoolDev/Thanatos-27B-HERETIC` serves the uncensored heretic-ara behavior
> directly — no local build required. `make build` remains the path for other
> quants.

If you pulled the bundle during any of the qwen36 windows on the
pre-rename `FoolDev/Thanatos-27B` repo (2026-05-19/20) and still
have a qwen36-stamped blob in your local Ollama store, pull the
current repo: `ollama pull hf.co/FoolDev/Thanatos-27B-HERETIC`. That
blob is the May 2026 build on vanilla `Qwen/Qwen3.6-27B`, from before
both base swaps. Fresh pulls go straight through.

For other quants (Q3_K_M ~13 GB, Q5_K_M ~20 GB, etc.), `make build
QUANT=...` is the simplest path. See [Quick start](#quick-start)
below for the full matrix. The heretic-ara GGUF repo publishes
quants from Q2_K (~10.9 GB) upward, including IQ4_XS.

For image input use llama.cpp directly — Ollama vision is broken for
this architecture upstream (see [Vision](#vision)).

> **Heads-up — context defaults.** The baked default is the full **262144** native
> window: a 16 GiB KV cache and ~32.3 GiB total with Ollama's default f16 cache, or
> 8.5 GiB / ~24.8 GiB with `OLLAMA_KV_CACHE_TYPE=q8_0`. It's extensible to 1,010,000
> with YaRN. On a 32 GB host use the q8_0 cache (tight) or lower `num_ctx` before
> the first message — 65536 is ~20 GiB total with the f16 cache. See [Hardware requirements](#hardware-requirements).
>
> To halve the KV cache, start the Ollama server with the q8_0 cache and flash
> attention (for a systemd install, add them as `Environment=` lines with
> `sudo systemctl edit ollama`):
>
> ```bash
> OLLAMA_KV_CACHE_TYPE=q8_0 OLLAMA_FLASH_ATTENTION=1 ollama serve
> ```

## Janus vs Thanatos

**They are different models again.** Janus moved back to the Qwen 3.6 35B-A3B MoE in
its 0.9.0 (2026-09-18), after a day of base changes in both directions; this repo has
been the dense Qwen 3.8 27B throughout and did not move. So the choice between them is
now about shape as well as abliteration:

| | Thanatos-27B (this) | [Janus-35B](https://huggingface.co/FoolDev/Janus-35B-HERETIC) |
|---|---|---|
| Architecture | Dense Qwen 3.8 27B — every parameter on every token | Qwen 3.6 35B-A3B MoE — ~34.7B total, ~3B active |
| Layers | 64 (16 full-attention / 48 linear) | 40 (10 full-attention / 30 linear) |
| Experts | none | 256, 8 routed per token + 1 shared |
| Abliteration method | Heretic **ARA** | Heretic **MPOA-style** |
| Immediate base | [`heretic-org/Qwen3.8-27B-heretic-ara`](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara) | [`llmfan46/Qwen3.6-35B-A3B-uncensored-heretic`](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic) |
| MTP head in the source weights | Present — stripped in the bundle | Declared by the base, absent from the bundled quant — no strip needed |
| Q4_K_M GGUF size | ~16.5 GB (bundled) | 21.23 GB (bundled) |
| Weights resident | ~15.4 GiB | ~19.78 GiB — every expert stays resident |
| KV cache at f16 | 2 GiB per 32K | 0.625 GiB per 32K — under a third, from 10 KV layers instead of 16 |
| Qwen generation | 3.8 | 3.6 |
| Repo slug | `Thanatos-27B-HERETIC` | `Janus-35B-HERETIC` — accurate again |

**Pick this one** for the newer Qwen generation, a smaller resident footprint and a
dense compute profile. **Pick Janus** for 35B-class capacity at ~3B active per token
and a much cheaper KV cache at long context. Both sides are measured on 2026-09-18
on Ollama 0.33.3's CPU backend — Janus's on its own MoE blob (its 0.9.2), this
card's on this repo's blob (0.12.4).

> Janus changed base three times on 2026-09-18 — MoE in 0.7.0, dense Qwen 3.8 27B in
> 0.8.0, back to the MoE in 0.9.0 — so its CHANGELOG reads as a round trip. If you
> pulled Janus that day, `ollama pull` again to match its card. Thanatos did not move.

What they do share: vocab 248,320, head_dim 256 on the full-attention layers,
the 262,144 native window (1,010,000 extensible with YaRN), the Qwen 3.x ChatML
frame, upstream vision/video support with the same upstream Ollama vision
breakage (ollama/ollama#14575), the Claude Fable 5 teacher slot, and this repo's
tooling. Everything else in the shape is this model's alone: dense 27B
all-active, 64 layers, hidden 5120, FFN intermediate 17408, 24 Q / 4 KV heads,
and the `qwen35` GGUF arch stamp (Janus stamps `qwen35moe`).

## What's here

| File | Use |
|---|---|
| `banner.svg` / `banner.png` | Repo header, Tokyo Night themed |
| `dense-flow.svg` / `dense-flow.png` | Architecture diagram: 64-layer hybrid attention stack with animated forward-pass pulse (SVG); static frame fallback (PNG) |
| `bmc-banner.svg` | Animated "Buy me a coffee" support banner, Tokyo Night themed (rising steam, hot-cup glow, sweeping beam, blinking cursor) |
| `Modelfile` | Ollama wrapper around the bundled GGUF (the heretic-ara Q4_K_M, `qwen35`-stamped) — used by `make build` / `ollama create` for **local** builds |
| `template`, `system`, `params` | Used by HF's Ollama bridge when users `ollama run hf.co/FoolDev/Thanatos-27B-HERETIC` directly (the bridge does **not** read `Modelfile` — see [HF Ollama docs](https://huggingface.co/docs/hub/en/ollama)). Mirrors the `Modelfile`'s template / system prompt / sampling params. |
| `chat_template.jinja` | Chat template for **llama.cpp / llama-server**, already stamped into the bundled GGUF (pass `--chat-template-file` only for an unstamped quant). The base model's own embedded template with three changes: a `tool_call_format` setting — `xml` by default, upstream's form and the one llama-server's parser reads, with `auto` as an opt-in for loaders that pass JSON-string `arguments` through; `reasoning_effort` normalised instead of validated; and an assistant turn's reasoning read from `reasoning`, `reasoning_content` or `thinking`, where upstream reads only `reasoning_content`. Earlier turns' reasoning is replayed by default, as upstream's is (see [Thinking is replayed across turns](#thinking-is-replayed-across-turns)). Also stamped into the GGUF by `scripts/build.sh`. See [Tool / function calling](#tool--function-calling). |
| `examples/` | Ready-to-run Python clients for Ollama, Transformers, and llama-cpp-python |
| `scripts/build.sh` | Pulls a qwen35-stamped GGUF from `mradermacher/Qwen3.8-27B-heretic-ara-GGUF` and runs `ollama create` (loads on today's llama.cpp / Ollama; see `make build`). The bundled Q4_K_M is already this heretic-ara quant; use this to build other quants locally. |
| `scripts/load_bundle.sh` | One-shot path from *this repo's* bundle → loadable local Ollama tag (downloads the real blob into `.cache/` if the working-tree file is still an LFS pointer — it does not smudge in place — then runs `ollama create`; see `make load-bundle`). Carries a qwen36 → qwen35 rebadge branch for legacy pre-rename checkouts — no-op on the current qwen35-stamped bundle. |
| `scripts/cap_ctx.sh` | Bakes a small-`num_ctx` local tag (bundled blob + this repo's Modelfile, `num_ctx`→4096, `num_batch` 256) for OpenAI `/v1` clients — which can't override the baked `num_ctx` and OOM on small hosts (see [Inference](#inference-openai-compatible)). Run `make cap-ctx` (or `CTX=8192 ./scripts/cap_ctx.sh`). |
| `scripts/smoke_test.sh` | Verifies an Ollama daemon + model, runs a round-trip, asserts no chat-template tokens leak into the response. With `TOOLS_TEST=1`, also exercises an end-to-end tool-call round-trip and checks the response shape |
| `scripts/bench.sh` | Measures real tok/s using Ollama's `eval_count` / `eval_duration` metadata over a 3-prompt mix (run `make bench`) |
| `scripts/fetch_vision.sh` | Pulls the vision projector (`Qwen3.8-27B-heretic-ara.mmproj-f16.gguf` from the Heretic GGUF repo, or `mmproj-F16.gguf` from the unsloth reference projector) for llama.cpp (Ollama vision: observed failing, untested since 2026-08 — see [Vision](#vision)). Renamed from `fetch_mmproj.sh` because HF's Ollama bridge auto-indexed the script as a vision projector layer (filename pattern match). |
| `scripts/check.sh` | Local lint: `bash -n`, `shellcheck`, `pyflakes`, `py_compile`, footgun-grep, `Modelfile`-vs-bridge-files sync, the `chat_template.jinja` render checks and the Go `template` guard (`make check`). `shellcheck` and `pyflakes` are skipped with a `[~]` line if absent, and the tail reports how many were skipped rather than a green all-passed. |
| `scripts/check_chat_template.py` | Renders `chat_template.jinja` with jinja2 and asserts the tool-call, thinking, reasoning-replay (on by default, each opt-out, a conflicting kwarg, a live tool chain's kept) and `reasoning_effort` behaviour (check 8 in `check.sh`) |
| `scripts/check_go_template.py` | Guards the Go `template`: Ollama's thinking detection, the thinking condition that replays every earlier turn's reasoning, the tool round trip, JSON tool signatures, and the reasoning-effort mapping — the xhigh and low arms and the medium/unset default on this path (check 9 in `check.sh`) |
| `scripts/live_check.sh` | Live end-to-end checks in an isolated, CPU-only Ollama (own port and model store; it refuses to run if Ollama reports a GPU): template selection, one tool call, string-argument replay, an earlier turn's reasoning replayed and a live tool chain's kept, every `reasoning_effort` value and the effort lines — 17 checks (`make live-check`) |
| `scripts/check_bridge_sync.py` | Verifies the `Modelfile` `TEMPLATE` / `SYSTEM` / `PARAMETER` directives stay in sync with the root-level `template` / `system` / `params` files. Run as part of `make check`; called from the pre-commit hook. |
| `scripts/verify_arch.py` | Cross-checks the README "Architecture" forward-pass bullets (layer count, head counts, hidden / FFN dims, RoPE factor, SSM dims, vocab, context) against the actual GGUF metadata keys. Run as `make verify-arch` (needs `pip install gguf`). Handles both `qwen35`- and `qwen36`-stamped bundles; exit non-zero if any value mismatches. Not part of `make check` because it loads the 17 GB GGUF (LFS smudge required — on an un-smudged pointer it now says so and exits 2); run on demand. |
| `scripts/strip_mtp.py` | Drops the MTP / NextN layer from a `qwen35` GGUF (`python3 scripts/strip_mtp.py IN.gguf OUT.gguf`): removes the extra `blk.<last>.*` block, sets `block_count` back to 64, and drops `nextn_predict_layers`. Kept tensors are copied byte-for-byte (no re-quant); a conditional no-op (hardlink) on already-clean quants. Preps the bundled blob and is run automatically by `build.sh` on every fetched quant, since the upstream heretic-ara GGUFs ship the MTP layer that stock llama.cpp / Ollama can't load — see [Architecture](#architecture). |
| `scripts/install-hooks.sh` | Installs `check.sh` as a git pre-commit hook |
| `Makefile` | Convenience wrapper — `make help` lists targets |
| `LICENSE`, `CITATION.cff` | Apache-2.0 license and citation metadata |
| `CHANGELOG.md` | Versioned tooling/docs changes |
| `README.md` | This file |

For 16 GB GPUs / unified-memory laptops, `make build QUANT=Q3_K_M`
downloads the smaller ~13 GB Q3_K_M quant from
`mradermacher/Qwen3.8-27B-heretic-ara-GGUF` (qwen35-stamped,
loads directly) and creates a local `thanatos-27b` Ollama tag.
Does not redistribute via this repo. For other quants use `make
build QUANT=...`. The local-build path applies this repo's
`Modelfile`; the `hf.co/...` path applies the root-level
`template`, `system`, and `params` files (kept in sync with the
`Modelfile`).

If you want the Heretic safetensors for `transformers`, fetch them from [`heretic-org/Qwen3.8-27B-heretic-ara`](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara). For the vanilla pre-Heretic Qwen 3.8 27B base, use [`Qwen/Qwen3.8-27B`](https://huggingface.co/Qwen/Qwen3.8-27B).

## Architecture

<p align="left">
  <img src="https://huggingface.co/FoolDev/Thanatos-27B-HERETIC/resolve/main/dense-flow.svg" alt="animated dense forward-pass visualization: 64-layer hybrid attention stack with a pulse traversing left-to-right, illuminating Gated DeltaNet (purple) and Gated Attention (cyan) layers in turn" width="800" />
</p>

- Qwen 3.8 dense, 27B parameters, 64 transformer layers
- **Hybrid attention stack**: 16 repeats of `[3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN)]`
  - Gated DeltaNet (linear attention): 48 V-heads, 16 QK-heads, head_dim 128
  - Gated Attention (softmax): 24 Q-heads, 4 KV-heads (GQA), head_dim 256, partial RoPE (factor 0.25)
- Hidden size 5120, FFN intermediate 17408 (~3.4× ratio)
- Vocab 248,320 (the Janus sibling's MoE shares this vocab size, on a different base)
- 262 144 native context (extensible to 1 010 000 with YaRN, but YaRN is not enabled in the bundled GGUF)
- Vision + video supported by the **base architecture** via a separate
  `mmproj` projector (not redistributed here; pull
  `Qwen3.8-27B-heretic-ara.mmproj-f16.gguf` from
  `mradermacher/Qwen3.8-27B-heretic-ara-GGUF`, or
  `mmproj-F16.gguf` from `unsloth/Qwen3.8-27B-GGUF` as a reference
  alternative). See [Vision](#vision) below for current loader
  compatibility.
- Multi-token prediction (MTP) head trained for speculative decoding —
  present in the upstream `Qwen/Qwen3.8-27B` safetensors (`mtp_num_hidden_layers: 1`)
  and usable via vLLM (`qwen3_next_mtp`) or SGLang (`--speculative-algo NEXTN`).
  Current `qwen35` GGUF conversions (e.g. `mradermacher/Qwen3.8-27B-heretic-ara-GGUF`)
  keep the MTP tensors as an extra NextN block, so those files report
  `block_count` 65 (= 64 transformer layers + 1 MTP layer). But today's
  stock llama.cpp / Ollama loaders can't yet load an MTP-included
  `qwen35` GGUF — they treat the NextN block as a normal hybrid layer and
  abort with `missing tensor 'blk.64.ssm_conv1d.weight'` (verified on
  llama.cpp + Ollama 0.30.8). **So the bundled `Thanatos-27B.Q4_K_M.gguf`
  is MTP-stripped** (block 64 removed, `block_count` 64) so `ollama run`
  and llama.cpp load it directly. For the MTP head itself, pull
  `cygnal/Qwen3.8-27B-heretic-ara-Q4_K_M-MTP-GGUF` and run it on a
  NextN-capable llama.cpp build, or use the upstream safetensors via
  vLLM/SGLang.

**The bundled GGUF declares `general.architecture: 'qwen35'`** — not a
workaround for an unimplemented `qwen36` arch, but the canonical
upstream label for the entire Qwen 3.5 / 3.6 / 3.8 hybrid SSM + attention
family. The naming convergence runs through three layers of the
stack:

- **Qwen's own HF configs.** `Qwen/Qwen3.8-27B/config.json` declares
  `"model_type": "qwen3_5"` and
  `"architectures": ["Qwen3_5ForConditionalGeneration"]`. The MoE
  sibling `Qwen/Qwen3.6-35B-A3B` declares `"qwen3_5_moe"` /
  `Qwen3_5MoeForConditionalGeneration`. No `Qwen3_6` arch class
  exists in `transformers`; Qwen reuses the 3.5 class names.
- **llama.cpp's converter.** `convert_hf_to_gguf.py` registers
  `Qwen3_5ForCausalLM` → `MODEL_ARCH.QWEN35` and
  `Qwen3_5MoeForCausalLM` → `MODEL_ARCH.QWEN35MOE`. The Heretic
  GGUFs this repo pulls from
  (`mradermacher/Qwen3.8-27B-heretic-ara-GGUF`) inherit those
  stamps, as do the upstream unsloth GGUFs (`unsloth/Qwen3.8-27B-GGUF`,
  `unsloth/Qwen3.6-35B-A3B-GGUF`).
- **llama.cpp's model code.** `src/models/qwen35.cpp` has an
  explicit `case 64: type = LLM_TYPE_27B` branch for this model;
  `qwen35moe.cpp` has `case 40: type = LLM_TYPE_35B_A3B` for the
  35B-A3B MoE base Janus shipped before its own 27B rebase. The
  arch entries were written to load Qwen 3.6 / 3.8 weights, not
  just Qwen 3.5.

There is no PR or tracking issue for a `qwen36` arch entry in
`ggml-org/llama.cpp` or `ollama/ollama` because none is needed —
`qwen35` already loads the model the upstream code path was
designed to load.

`ollama run hf.co/FoolDev/Thanatos-27B-HERETIC` and `llama-server -m
Thanatos-27B.Q4_K_M.gguf` both load directly on current stock
loaders.

### History

The bundle's `general.architecture` stamp has now flipped eight
times — four landings on qwen36 and four on qwen35 — each time
after weighing the friction-vs-honesty tradeoff anew. The saga
is resolved on the upstream-canonical `qwen35` side:

- **v0.6.0-era (`e1f78fa`, 2026-05-19 14:38 UTC):** initial qwen35
  → qwen36 stamp, on the theory that qwen35 was a loader stand-in
  awaiting proper Qwen 3.6 support. Upstream audit later showed
  that theory was mistaken (see above).
- **2026-05-19 afternoon (`964e418`):** flipped back to qwen35
  after daily friction outweighed version-specificity for that
  iteration; doc workaround narrative collapsed (`83022eb`).
- **2026-05-19 evening (`07fa120`):** brief re-flip to qwen36
  during a fresh-pull integration test on Strix Halo.
- **2026-05-19 evening (`72259c1`, ~1 hour later):** reverted to
  qwen35 again because the live friction was worse than the doc
  prose suggested.
- **2026-05-19 evening (`973d7ef`):** flipped to qwen36 one more
  time, after the upstream-evidence audit had been shipped and
  the friction was a known quantity. Project owner wanted to
  test the friction tradeoff in practice with the audit's
  conclusion staring them in the face.
- **2026-05-19 evening (`978798f`):** flipped back to qwen35
  after seven sequential fresh-pull → heal-hf cycles on the
  Strix Halo box made the friction concretely-experienced
  rather than hypothetical. Each cycle worked (the heal flow
  is solid) — and each cycle was an unnecessary obstacle for
  users who just want `ollama run` to work first try. The
  audit (`a4d3b6e`) called the canonical stamp correctly and
  the practical friction outweighed the version-specificity
  payoff.
- **2026-05-20 midday (`ae67ed1`):** brief re-flip to qwen36
  the next morning to re-test the friction in a fresh session.
- **2026-05-20 midday (`e03e10e`, 8 minutes later):** flipped
  back to qwen35. Same conclusion as the prior round trip —
  friction outweighs version-specificity. **This is the
  current state.**

Tensor data was byte-identical across all stamps; only the
`general.architecture` KV (and namespaced KV keys) flipped.
See the [CHANGELOG](CHANGELOG.md) entries for each flip's
rationale.

### Rebadge utility

`scripts/rename_arch.py` is the generic GGUF arch renamer
(metadata only, tensors byte-identical), kept in the repo for
the legacy qwen36 → qwen35 rebadge of a local bundle (used by
`make load-bundle`) and any future arch flip:

```bash
# qwen36 -> qwen35 (the legacy recovery direction, for blobs
# pulled from the pre-rename FoolDev/Thanatos-27B repo)
python3 scripts/rename_arch.py \
    --from-arch qwen36 --to-arch qwen35 \
    Thanatos-27B.Q4_K_M.qwen36.gguf \
    Thanatos-27B.Q4_K_M.gguf
```

## Quick start

### Ollama

Three paths:

```bash
# A. Pull straight from HF (gets the bundled Q4_K_M GGUF + the
#    root-level template / system / params files in one step):
ollama run hf.co/FoolDev/Thanatos-27B-HERETIC           # 17 GB Q4_K_M, qwen35-stamped

# B. Build a local `thanatos-27b` tag from THIS repo's bundle
#    (LFS smudge if needed, then `ollama create`). Useful if you
#    want a bare local tag rather than the `hf.co/...` path:
make load-bundle                                 # creates local tag thanatos-27b
ollama run thanatos-27b

# C. Bypass the bundle: download a qwen35-stamped heretic-ara GGUF
#    and build locally. Loads on every current llama.cpp / Ollama.
make build                                              # Q4_K_M  -> thanatos-27b
make build QUANT=Q3_K_M                                 # 13 GB smaller quant
make build QUANT=Q5_K_M                                 # 20 GB higher quality
make build GGUF_PATH=~/models/Qwen3.8-27B-heretic-ara.Q4_K_M.gguf   # skip download
ollama run thanatos-27b
```

Under the hood, `make build` calls `scripts/build.sh`, which downloads the
GGUF if missing (set `GGUF_PATH` to point at one you already have) and
runs `ollama create` with the matching `Modelfile`.

If you'd rather do it by hand: edit the `FROM` line in `Modelfile` and
run `ollama create thanatos-27b -f Modelfile && ollama run thanatos-27b`.

Confirm everything works:

```bash
make smoke                          # checks server, model, round-trip, no token leakage
make smoke-tools                    # adds an end-to-end tool-call round-trip (~10s extra)
make bench                          # measured tok/s on this machine (3-prompt mix)
python examples/ollama_chat.py      # full demo: chat, streaming, tools, OpenAI-compat
```

### Local apps

| App | How to load this model |
|---|---|
| **Ollama** | `ollama run hf.co/FoolDev/Thanatos-27B-HERETIC` (default Q4_K_M). Pulls the GGUF + the root-level `template` / `system` / `params` files in one step (HF's Ollama bridge ingests these three files; it does **not** read `Modelfile`). For other quants, `make build QUANT=Q3_K_M` downloads from `mradermacher/Qwen3.8-27B-heretic-ara-GGUF` and creates a local Ollama tag using the `Modelfile`, which is kept in sync with the bridge files. |
| **LM Studio** | Search → `FoolDev/Thanatos-27B-HERETIC` → pick `Thanatos-27B.Q4_K_M.gguf` (current bundled filename — the heretic-ara Q4_K_M). Uses the GGUF's embedded jinja chat template (Qwen 3.8 ChatML); set the system prompt manually from the `SYSTEM` block in this repo's `Modelfile`. |
| **Jan** | Hub → "Import from Hugging Face" → `FoolDev/Thanatos-27B-HERETIC`. Same template behavior as LM Studio. |
| **llama.cpp** | `hf download FoolDev/Thanatos-27B-HERETIC Thanatos-27B.Q4_K_M.gguf --local-dir .` then `llama-server -m Thanatos-27B.Q4_K_M.gguf` (or `llama-cli`, `llama-mtmd-cli` for vision via `Qwen3.8-27B-heretic-ara.mmproj-f16.gguf` from the Heretic GGUF repo). **Tool calling needs only `--jinja`** — the bundled GGUF already carries this repo's fixed chat template. Add `--chat-template-file chat_template.jinja` only for a quant pulled straight from upstream, whose template raises on common `reasoning_effort` values such as `high`. |
| **llama-cpp-python** | See `examples/llama_cpp_quickstart.py` (text) and `examples/llama_cpp_vision.py` (image input). |
| **Open WebUI / KoboldCpp / text-generation-webui** | Standard llama.cpp loader path — point at the GGUF, use the embedded chat template. |

For the full Vision (image input) loader matrix, see [Vision](#vision).
Tool calling works in **Ollama** (via the root-level `template` file
when pulling from `hf.co/...`, or via the `Modelfile` TEMPLATE when
building locally) and in **llama.cpp / llama-cpp-python** — but on
llama.cpp with `--jinja`. The bundled GGUF carries this repo's fixed chat
template, so no extra flag is needed; a quant pulled straight from
upstream does need `--chat-template-file chat_template.jinja`, because its
embedded template raises on common `reasoning_effort` values such as `high`,
which llama-server returns as HTTP 500. Other apps'
tool-calling support depends on whether they read the embedded template
or require an external schema.

### Inference (OpenAI-compatible)

> The examples use `model: "thanatos-27b"`, the tag from the local build (`make build` / `ollama create thanatos-27b`). If you pulled via the TL;DR one-liner instead, use the full tag `hf.co/FoolDev/Thanatos-27B-HERETIC`, or run `ollama cp hf.co/FoolDev/Thanatos-27B-HERETIC thanatos-27b` once to create the short tag.

> **On memory-tight hosts, cap `num_ctx` first.** `/v1/chat/completions` (OpenAI-compat) has
> no `num_ctx` knob, so it loads at the baked **262,144** default (16 GiB KV / ~32.3 GiB total with
> Ollama's default f16 cache), which does not fit a 32 GB box; `OLLAMA_KV_CACHE_TYPE=q8_0` on the
> server brings it to ~24.8 GiB (see [Hardware requirements](#hardware-requirements)). Either
> call `/api/chat` with `"options": {"num_ctx": 4096}`, or bake a small-context tag for
> OpenAI clients: `ollama run hf.co/FoolDev/Thanatos-27B-HERETIC:Q4_K_M`, then
> `/set parameter num_ctx 4096` and `/save thanatos-27b`, and point clients at `thanatos-27b` — or in
> one step, **`make cap-ctx`**, which bakes a local `thanatos-27b` tag from the bundled blob and this
> repo's Modelfile at `num_ctx` 4096 / `num_batch` 256 (`CTX=8192 TAG=thanatos-cap make cap-ctx` to
> change either).

```bash
curl -s http://localhost:11434/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "thanatos-27b",
    "messages": [
      {"role": "system", "content": "You are Thanatos, a precise reasoning assistant."},
      {"role": "user", "content": "Explain the Burrows-Wheeler transform in 200 words."}
    ],
    "temperature": 0.6
  }' | jq -r '.choices[0].message.content'
```

### Recommended sampling

| Use | temp | top_p | top_k | repeat_penalty |
|---|---:|---:|---:|---:|
| **Default (Fable-matched)** | 1.0 | 0.95 | 0 | 1.05 |
| Tighter reasoning | 0.6 | 0.95 | 20 | 1.05 |
| Creative / RP | 0.8 | 0.95 | 40 | 1.02 |

The shipped default is Fable-matched — warm (`temperature 1.0`), no `top_k`, with `top_p 0.95` + `repeat_penalty 1.05` kept as loop insurance. Drop to the reasoning row for tighter, more deterministic output; lower temperature (0.4-0.6) and bump `repeat_penalty` to 1.08 if it loops inside `<think>` tags.
> **`top_p` does not survive the OpenAI-compatible endpoint.** Ollama's
> `/v1/chat/completions` layer applies OpenAI's own default of `top_p 1.0`,
> overwriting the `0.95` baked into `params` / the `Modelfile`. Measured on this
> model: the same request logs `top_p = 0.950` on `/api/chat` and
> `top_p = 1.000` on `/v1/chat/completions`. Since the default profile also sets
> `top_k 0` (disabled), a `/v1` request samples with **no truncation at all** at
> `temperature 1.0` — the "loop insurance" above is only in effect on the native
> API. If you need that guard on `/v1`, send `top_p` explicitly on every request,
> or bake `min_p` (e.g. `PARAMETER min_p 0.05`) into a local tag — `min_p` and
> `top_k` both pass through `/v1` untouched, `top_p` does not.


### System prompt

The Modelfile bakes this in. Override per-request via the `system` role
in your client:

```text
You are Thanatos, a precise and capable assistant for reasoning, writing, coding, and long-form dialogue.

Behavior rules:
- Answer the user's actual request directly.
- Be accurate, complete, and structured.
- Think before answering, but do not get stuck in repetitive loops or meta-commentary.
- If the request is ambiguous or incomplete, state what is missing and make the smallest reasonable assumption needed to continue.
- If the user wants creative writing, preserve tone, continuity, and character consistency.
- If the user wants analysis or technical help, prefer concrete steps, examples, and decisions over fluff.
- Finish with a usable answer, not just planning.
```

## Vision

The Qwen 3.8 base supports image (and video) input via a separate
`mmproj` projector. The full multimodal stack is:

```
Thanatos-27B.Q4_K_M.gguf                 (~16.5 GB, the text decoder — this repo's bundle)
Qwen3.8-27B-heretic-ara.mmproj-f16.gguf  (~928 MB, the vision projector)
```

> ⚠️ **Use the bundled decoder, not the raw upstream quant.** The heretic-ara
> GGUFs at mradermacher ship the MTP / NextN layer that stock llama.cpp cannot
> load (see [Architecture](#architecture)), so
> `-m Qwen3.8-27B-heretic-ara.Q4_K_M.gguf` aborts at load. This repo's
> `Thanatos-27B.Q4_K_M.gguf` is the same quant already MTP-stripped — it is what
> the commands below use, and it saves a second ~17 GB download. If you do want
> an upstream quant, run it through `scripts/strip_mtp.py` first (`make build`
> does this automatically).

The projector is at
[`mradermacher/Qwen3.8-27B-heretic-ara-GGUF`](https://huggingface.co/mradermacher/Qwen3.8-27B-heretic-ara-GGUF);
`./scripts/fetch_vision.sh` pulls it into the repo root.
For the vanilla pre-Heretic projector, see
[`unsloth/Qwen3.8-27B-GGUF`](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
(`mmproj-F16.gguf`, ~927 MB). This repo intentionally does not
redistribute either.

### Loader compatibility — the honest table

| Loader | Text | Vision (mmproj) | Notes |
|---|---|---|---|
| **llama.cpp** (`llama-mtmd-cli`, `llama-server --mmproj`) | ✅ | ✅ | Reference path. Upstream has the `qwen35`/`qwen35moe` arch entries. |
| **llama-cpp-python** | ✅ | ✅ | See `examples/llama_cpp_vision.py`. |
| **Ollama** (0.33.3, 0.34.0 and 0.34.2 checked in source) | ✅ | ❓ | Text inference works, checked in source at 0.33.3, 0.34.0 and 0.34.2. The version floor this row used to claim ("0.24+") was undated and unsourced; these three are the checked set. Vision (mmproj) was **observed** failing, but the cause this row used to give is wrong. There is no "C++ llama.cpp fallback" distinct from a Go engine: every GGML model is served by the bundled llama-server ([ollama/ollama#16031](https://github.com/ollama/ollama/pull/16031)), and at v0.33.3 the source tree carries no vendored `llama/llama.cpp/` and no Go model implementations at all (checked 2026-09-18). The observation stands; the explanation does not, and it has not been re-tested since. `ollama create` accepts a dual-`FROM` (text + mmproj) and `ollama show` reports `vision` capability — but the **first inference request** fails with `error loading model architecture: unknown model architecture: 'qwen35'` (or `'qwen35moe'`), and once mmproj is attached this blocks text inference too. See [ollama/ollama#14575](https://github.com/ollama/ollama/issues/14575) (closed as completed on 2026-08-04; #15898 was closed as its duplicate and the sync PR #15899 closed unmerged). Re-test on a current Ollama before assuming vision is still broken — this table has not been re-verified since it closed. |
| **LM Studio** | ✅ | ✅ (last tested) | Uses upstream llama.cpp directly. |

### Vision via llama.cpp

Three flavors, in order of build-time effort:

```bash
# A. HTTP via llama-server (always built — the easiest path).
#    Reconfirmed working 2026-05-19 against llama.cpp 389ff61 + Vulkan
#    on a Ryzen AI Max+ 395 / Radeon 8060S iGPU.
llama-server \
  -m Thanatos-27B.Q4_K_M.gguf \
  --mmproj Qwen3.8-27B-heretic-ara.mmproj-f16.gguf \
  --host 127.0.0.1 --port 8765 -c 8192 -ngl 99
# then POST OpenAI-style chat completions with an image_url content
# block — e.g. {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,..."}}
# The thinking trace arrives in message.reasoning_content; the visible
# answer is in message.content. Budget ≥500 max_tokens so the reasoning
# block doesn't crowd out the final answer.

# B. CLI via llama-mtmd-cli (one-shot). It's a separate cmake target,
#    so a selective `cmake --build build --target llama-cli ...` won't
#    produce it — a plain `cmake --build build` will. If yours didn't,
#    run `cmake --build build --target llama-mtmd-cli`.
llama-mtmd-cli \
  -m Thanatos-27B.Q4_K_M.gguf \
  --mmproj Qwen3.8-27B-heretic-ara.mmproj-f16.gguf \
  --image photo.jpg \
  -p "Describe this image."

# C. Python via llama-cpp-python:
python examples/llama_cpp_vision.py \
  --gguf Thanatos-27B.Q4_K_M.gguf \
  --mmproj Qwen3.8-27B-heretic-ara.mmproj-f16.gguf \
  --image /path/to/photo.jpg \
  --prompt "What is in this image?"
```

The Ollama issue is closed upstream but this table has not been re-verified
since; until you have re-tested, treat Ollama as **text-only** for this model.

## Hardware requirements

Janus is a 35B-A3B MoE since its 0.9.0, so its figures no longer transfer: 10 full-attention layers instead of 16 give it a far smaller KV cache (0.625 GiB per 32K f16), while its weights are larger at ~19.78 GiB.

This is a ~16.5 GB Q4_K_M GGUF. **Measured on this repo's own blob on 2026-09-18**,
Ollama 0.33.3's CPU backend, isolated store, CPU only, from llama.cpp's own allocation
lines at `num_ctx` 8192 / 32768 / 65536 and again under `OLLAMA_KV_CACHE_TYPE=q8_0`
with `OLLAMA_FLASH_ATTENTION=1`. (Earlier releases carried these figures measured on
the Janus sibling while it shared this architecture; they are now this model's own.)

| component | measured | scales with `num_ctx`? |
|---|---|---|
| Weights | **15.40 GiB** (`CPU model buffer` 4935.19 MiB + `CPU_REPACK` 10835.16 MiB) | no |
| Recurrent state (48 linear-attention layers) | **149.62 MiB** | no — identical at every context |
| KV cache, f16 (Ollama's default) | **65,536 B/token** → 512 / 2048 / 4096 MiB at 8K / 32K / 64K, i.e. **2.0 GiB per 32K** | yes, exactly linear |
| KV cache, q8_0 | **34,816 B/token** → 1088 / 2176 MiB at 32K / 64K, i.e. **1.0625 GiB per 32K** | yes, exactly linear |
| Compute buffer | 280.04 / 328.04 / 784.07 MiB at 8K / 32K / 64K (q8_0: 328.30 / 784.34) | yes, but **not** linearly |

llama.cpp logs the cache as "16 layers", confirming only the full-attention layers are
cached — the Janus sibling's MoE logs 10, which is why its KV is under a third of this
one's at the same window.

| `num_ctx` | f16 cache (default) | q8_0 cache |
|---|---|---|
| **262144 (default)** | 16.0 GiB KV, **~32.3 GiB** total | 8.5 GiB KV, **~24.8 GiB** total |
| 65536 | 4.0 GiB KV, **20.3 GiB** total (measured) | 2.13 GiB KV, **18.4 GiB** total (measured) |
| 32768 | 2.0 GiB KV, **17.9 GiB** total (measured) | 1.06 GiB KV, **16.9 GiB** total (measured) |
| 1010000 (needs YaRN) | 61.6 GiB KV, ~77.9 GiB total | 32.7 GiB KV, ~49.0 GiB total |

The 32768 and 65536 rows are sums of measured parts. The 262144 and 1010000 rows
extrapolate the KV cache — exact, since it is linear — and carry the compute buffer
forward from 65536, the largest context measured; it grows faster than linearly
between 32K and 64K, so treat those two rows as floors. It's **extensible to 1,010,000**, but this GGUF ships **no YaRN rope-scaling**, so positions past the 262144 native window use untrained RoPE and output degrades — reaching the 1.01M ceiling needs YaRN (see below); keep real work within ~262K otherwise.

**How to override it:** `ollama run` has no `-o` flag, and `OLLAMA_CONTEXT_LENGTH` only sets a default the baked `num_ctx` overrides — so set it per-session from the interactive prompt (the model loads lazily on the first message, so `/set` applies before the default context is allocated):

```text
ollama run hf.co/FoolDev/Thanatos-27B-HERETIC:Q4_K_M
>>> /set parameter num_ctx 4096
>>> /set parameter num_batch 256
```

Programmatic callers pass the same via the API `options` field: `"options": {"num_ctx": 4096, "num_batch": 256}` — but only on Ollama's own `/api/chat`. `/v1/chat/completions` ignores `options` entirely, so an OpenAI-compatible client needs a tag baked at the smaller context instead: **`make cap-ctx`** bakes one with those same two values, from the bundled blob and this repo's Modelfile.

| Hardware | Status |
|---|---|
| ≥48 GB RAM (CPU-only) | Works at the 262144 default (~32.3 GiB); 5.08 tok/s measured on a Ryzen AI Max+ 395. A 32 GB host needs `OLLAMA_KV_CACHE_TYPE=q8_0` (~24.8 GiB, tight) or `num_ctx 65536` (20.3 GiB measured) |
| RTX 3090 / 4090 24 GB | Works with partial offload — the ~32.3 GiB total at the 262144 default does not fit 24 GB; trim `num_ctx` for full offload |
| RTX 5090 32 GB | Works, full offload at higher quant (Q5/Q6) with a lower `num_ctx` than the 262144 default, ~30-50 tok/s |
| Mac Studio M2/M3 48 GB+ unified | Works at the default, ~15-25 tok/s (32 GB needs a lower `num_ctx`) |
| 32 GB unified-memory laptops (Mac M-series, Ryzen AI Max+, etc.) | Does not fit the 262144 default with the f16 cache; the q8_0 cache (~24.8 GiB) is tight, `num_ctx 65536` (18.4-20.3 GiB measured) is comfortable. `make build QUANT=Q3_K_M` (~13 GB) or a lower `num_ctx` for comfort. |

Most numbers in this table are estimates from comparable models; the
gradient is right but the absolute values will move ±20% with prompt
shape, KV cache type, and parallel-request count. Measure your own
machine with `make bench` (3-prompt mix, reports tok/s from Ollama's
`eval_count` / `eval_duration` so it's not stopwatch-noisy). On the current
blob, on a Ryzen AI Max+ 395 with Ollama 0.33.3's CPU backend (no GPU),
`make bench` measured **5.08 tok/s at Q4_K_M** — aggregate over its three-prompt mix
after a discarded warmup, 1,852 generated tokens in 364,560 ms, or 5.32 / 5.10 / 5.07
individually, so the rate is steady across short / medium / long prompts (re-measured
2026-09-18 in an isolated store; a 0.12.0-era run of the same bench gave 5.01). The
q8_0 KV cache costs nothing in speed here either — 5.22 and 5.12 tok/s on the first two
prompts of the same mix against 5.32 and 5.10 at f16; that pass was stopped before its
third prompt finished, so no q8_0 aggregate is published. The earlier data points on that machine's
Radeon 8060S iGPU under Vulkan — **~12.3 tok/s at Q3_K_S** and **~9.3 tok/s
at Q4_K_M**, with a ROCm snapshot of the Q3_K_S bench at ~10.1 tok/s — were
measured in May 2026 on the Qwen 3.6 27B builds, before both base swaps, and
have not been re-measured on the heretic-ara blob.

**GPU offload on a Strix Halo iGPU (Radeon 8060S): a small gain, and a trap.** On a
Vulkan integrated GPU, llama.cpp - including the build Ollama 0.33.3 bundles - turns
mmap off and puts every layer it does *not* offload into GPU-reachable host memory from
the same pool as the GPU, so `num_gpu` alone does not limit GPU memory: a first attempt
with llama-server filled the pool and took the desktop down with it. With
`LLAMA_ARG_NO_HOST=1` in the Ollama server's environment (llama.cpp's `--no-host`) those
layers stay in ordinary RAM. Measured that way on the Janus sibling when it was the same dense Qwen 3.8 27B architecture, 17.3 against 16.5 GB (a private Ollama 0.33.3
with the `ollama-vulkan` backend and `OLLAMA_IGPU_ENABLE=1`; flash attention, q8_0 KV
cache, `num_ctx` 4096, a short generation): 4.8 tok/s at `num_gpu` 4, 4.9 at 8, 5.3 at 16
and 5.7 at 24 (7.9 GiB of the GPU pool), against about 5.0 on CPU only; prompt processing
roughly doubled (61 against 30 tok/s). The step to 32 layers ran the 27 GiB host short of
RAM and was stopped: the GPU's GTT is system RAM, so offloading frees none. On a machine
like this, CPU-only is nearly as fast; if you try the GPU, set `LLAMA_ARG_NO_HOST=1` and a
fixed `num_gpu`. The mechanism is reported upstream in
[ggml-org/llama.cpp#27360](https://github.com/ggml-org/llama.cpp/issues/27360).

**Reaching a coherent ~1.01M context (opt-in YaRN).** The bundled GGUF ships no
YaRN rope-scaling, so raising `num_ctx` toward the 1.01M ceiling degrades past the
262144 native window. Ollama has no rope knob, so for a genuinely coherent long context run
the GGUF under llama.cpp with YaRN enabled:

```bash
llama-server -m Thanatos-27B.Q4_K_M.gguf \
  --rope-scaling yarn --yarn-orig-ctx 262144 --rope-scale 3.853 -c 1010000
```

`--rope-scale 3.853` ≈ 1010000 / 262144; use a smaller factor for a smaller
window. Static YaRN rescales *all* prompts, so enable it only when you actually
need > 262K — it slightly degrades short-context quality otherwise.

## Chat template

Standard Qwen 3.x ChatML with `<|im_start|>` / `<|im_end|>` role markers
and `<think>...</think>` blocks for reasoning traces. The Qwen 3.8 jinja
template is embedded in the GGUF metadata; loaders that read GGUF chat
templates directly (llama.cpp, llama-cpp-python, LM Studio) handle the
plain-conversation formatting automatically.

Ollama is the exception: it picks between this repo's Go template and the
embedded jinja at load time (see [Which template Ollama runs](#which-template-ollama-runs)).
Two paths supply that Go template, depending on how you pull the model:

- **`ollama run hf.co/FoolDev/Thanatos-27B-HERETIC`** — HF's Ollama bridge applies
  the root-level `template` / `system` / `params` files in this repo
  (the bridge does **not** read `Modelfile`).
- **`make build` / `ollama create thanatos-27b -f Modelfile`** — uses the
  `Modelfile`'s `TEMPLATE` block.

Both routes wire `.Tools` / `.ToolCalls` and tools work end-to-end on
`/api/chat` and `/v1/chat/completions`. The two configurations are
kept in sync: edit them together if you change one.

#### Plain conversation

```text
<|im_start|>system
You are Thanatos, a precise and capable assistant…<|im_end|>
<|im_start|>user
What is the time complexity of mergesort?<|im_end|>
<|im_start|>assistant
```

#### With reasoning trace

```text
<|im_start|>assistant
<think>
The user asked about mergesort. It splits, recursively sorts each half,
then merges. The recurrence T(n) = 2T(n/2) + O(n) solves to O(n log n).
</think>

Mergesort runs in **O(n log n)** time in the worst, average, and best
cases.<|im_end|>
```

Most clients (Open WebUI, LibreChat, etc.) hide the `<think>` block by
default and surface only the visible answer. Strip it manually with
`re.sub(r"<think>.*?</think>\s*", "", content, flags=re.DOTALL)` if your
client doesn't.

#### Thinking is replayed across turns

Reasoning from earlier assistant turns **is** replayed back into the prompt, on
both runtimes, so the model sees how it reached its previous answers. Reasoning
from the turn in progress — including a tool-call chain, where the model calls a
tool and then continues after the result — is kept whatever the setting, so it
does not lose its own trace mid-flight.

- **Ollama** runs the Go template, which renders a `<think>…</think>` block for every
  assistant message, earlier turns included — the condition is `$.IsThinkSet` alone, not
  gated on `.Thinking`, so a turn that did no reasoning renders an **empty** block rather
  than none. This departs
  from Qwen's stock condition, which drops reasoning from turns before the latest
  user message. Ollama never passes reasoning to the GGUF's embedded Jinja
  template, so on Ollama only the Go template decides.
- **llama.cpp** runs `chat_template.jinja`, which replays earlier turns' reasoning
  by default, as upstream's template does — including upstream's empty
  `<think>\n\n</think>` block for an earlier assistant turn that had no reasoning.

**Your client has to send the reasoning back.** The server returns it — Ollama's
`/api/chat` in the response's `thinking` field, llama.cpp in `reasoning_content` —
but a template can only replay what arrives in the next request, and each server
reads one field:

| Endpoint | Field read from each assistant message |
|---|---|
| Ollama `/api/chat` | `thinking` |
| Ollama `/v1/chat/completions` | `reasoning` only — `reasoning_content` and `thinking` are dropped silently; an assistant message whose `content` is an array of parts keeps its reasoning only if it also has `tool_calls` |
| llama-server `/v1/chat/completions` | `reasoning_content` only |
| LM Studio 0.4.24 `/v1/chat/completions` | `reasoning` or `reasoning_content`, passed to the template as `reasoning_content`; `thinking` is dropped |
| KoboldCpp `/v1/chat/completions` (`--jinja`) | whatever the client sent — the template sees the message unchanged |

For loaders like KoboldCpp that pass the message through, `chat_template.jinja`
reads the reasoning from `reasoning`, then `reasoning_content`, then `thinking`
(the order the Janus sibling used while it still shipped its own Jinja template;
its 0.9.0 dropped that file); upstream's template read only `reasoning_content`,
so a trace sent as `reasoning` or `thinking` became an empty `<think>` block.
Checked on 2026-09-14 by rendering both templates with KoboldCpp's own Jinja setup
(from its `koboldcpp.py`, `concedo` branch `4ac5721`) — the old one dropped both
fields, the new one replays them — and through LM Studio 0.4.24 with a
260K-parameter model on its CPU runtime, where the old and new templates rendered
the same because LM Studio normalises the field first.

Checked live on 2026-09-13 with the restamped blobs, CPU only: Ollama 0.33.3
replayed `thinking` on `/api/chat` (232 prompt tokens with it, 187 without) and
`reasoning` on `/v1` (215 vs 187, measured with the Janus sibling's blob, whose Go
template is byte-identical) and ignored `reasoning_content` on `/v1` (187);
llama-server master rendered `reasoning_content` and dropped a `reasoning` field.
That Ollama's `/v1` also drops `thinking`, and the array-content rule, come from
Ollama's v0.33.3 and v0.34.0 source, and still hold on the current release:
`openai/openai.go` and `server/prompt.go` are byte-identical from v0.33.3 through
v0.34.2 (source, 2026-09-17).

**Which llama.cpp an Ollama carries.** 0.33.3 and 0.34.0 bundle b10760; 0.34.1
bundles b10864 and 0.34.2 b10969 (each release's `LLAMA_CPP_VERSION`). From 0.34.1
on that is a b10763-or-later llama-server — the family that passes
`preserve_reasoning=true` by default — but it changes nothing here.

**Correction (2026-09-18).** This paragraph used to say that text inference runs "Ollama's
own Go engine" and that the bundled llama.cpp only comes into play when Ollama "falls back
to its C++ engine" once an mmproj is attached. There is no such split. Ollama has no Go inference engine and no separate C++ fallback: since [ollama/ollama#16031](https://github.com/ollama/ollama/pull/16031) every GGML model is served by the bundled llama-server subprocess, and at v0.33.3 the source tree carries no vendored `llama/llama.cpp/` and no Go model implementations at all — `model/` holds only `parsers/` and `renderers/` (checked 2026-09-18). So
`LLAMA_CPP_VERSION` names the engine for text as well, and the bundled llama-server is what
runs this model on every request. What keeps `preserve_reasoning` a non-event here is
unchanged: on the Ollama path the prompt is rendered by the Go template, not by the GGUF's
Jinja template (see [Which template Ollama runs](#which-template-ollama-runs)).

**The cost is context.** Every retained trace stays in the prompt, measured at
**181 prompt tokens without / 464 with** on a 3-message conversation whose first
assistant turn carried a ~240-word trace. Prefill grows with every retained trace,
and on a CPU-only host prefill is the slow part. Releases 0.7.0 through 0.8.1
turned replay off for that reason; the CHANGELOG has the history.

**To turn it off on llama-server**, start it with `--no-reasoning-preserve`, or
per request pass `"chat_template_kwargs": {"preserve_thinking": false}` (or
`{"preserve_reasoning": false}`). `"preserve_thinking": true` in a request turns
replay back on even against `--no-reasoning-preserve`. The template reads only
`preserve_thinking`; llama-server derives it from `preserve_reasoning` and
`--no-reasoning-preserve`. llama.cpp master (b10763 and later) passes
`preserve_reasoning=true` unless started with `--no-reasoning-preserve` and logs
"chat template supports preserving reasoning, it is enabled by default"; b10760
(the build Ollama 0.33.3 bundles) and b10519 pass nothing and log "consider
enabling it via --reasoning-preserve", yet still replay, because the template's
own default is on. Tested on 2026-09-13 with a 260K-parameter test model and
`--chat-template-file` (the template, not the model, decides the prompt), via
`/apply-template` and `/v1/chat/completions`, on master `4a89937` (b10941), b10760
and b10519 (LM Studio's avx2 CPU runtime 2.30.0): each of those settings behaved
as described, a live tool-call chain kept its reasoning in every mode, and no
request returned an error. On the restamped blob itself, with its embedded
template and default flags, llama-server master rendered a 3-message conversation
in 111 prompt tokens with the earlier turn's reasoning and 81 with
`--no-reasoning-preserve` or either `false` kwarg (85 with no reasoning sent, for
the empty think block), and a real tool-result turn with string arguments returned
HTTP 200.

**To turn it off on Ollama**, edit the assistant branch of the `Modelfile` /
`template` (both, so `make check`'s bridge sync stays green): change
`{{ if $.IsThinkSet -}}` (the shipped condition) back to Qwen's stock
`{{ if (and $.IsThinkSet (and .Thinking (or $last (gt $i $lastUserIdx)))) -}}`
(keep the `-}}`; the `$lastUserIdx` loop at the top of the template is there for
it). `check_go_template.py` (check 9) will then fail, since it requires the
replay condition. Do not delete the block instead — see
[Which template Ollama runs](#which-template-ollama-runs).

#### Disabling thinking

This is a reasoning-first model — it opens a `<think>` block by default. For a
direct answer with no reasoning trace (simple or latency-sensitive calls), turn
thinking off:

```bash
ollama run hf.co/FoolDev/Thanatos-27B-HERETIC:Q4_K_M --think=false
```

or send `"think": false` on `/api/chat`. With thinking off the model skips the
reasoning trace and answers straight into `content`; with it on (the default)
reasoning is emitted into the `thinking` field.

#### Reasoning effort

OpenAI-compatible clients can send `reasoning_effort`. Ollama's `/v1` layer accepts
eight values. Where `chat_template.jinja` sees the value as sent (llama.cpp), it maps
each to one of three tiers or switches thinking off:

| `reasoning_effort` | Effect |
|---|---|
| `high`, `xhigh`, `max`, `ultra` | **xhigh** — the model is told to think carefully and check its assumptions |
| `medium`, unset, `null`, anything unrecognised | **medium** — the default; no effort instruction is added |
| `low`, `minimal` | **low** — the model is told to keep its thinking brief |
| `none` | thinking **off** for that request, the same as `"think": false` |

**The default changed in 0.12.4.** Upstream's template treated an unset value as
`xhigh` and *raised* on anything it did not recognise; this template resolved unknown
values rather than raising, but kept the xhigh default — so the same request answered
at a different tier depending on which template rendered it: xhigh through llama.cpp,
medium through Ollama, where an unset think level adds no instruction at all. Both
paths now default to **medium**, and xhigh is something a client asks for explicitly.
Upstream accepted only `xhigh`, `medium` and `low`, so everything else failed —
including `high`, the value most OpenAI-compatible clients send; on Ollama, while it
ran the embedded template, that surfaced as HTTP 500.

**On Ollama's default path the Go template runs instead** (see
[Which template Ollama runs](#which-template-ollama-runs)), and it adds the same
instruction from Ollama's think level. Ollama folds the eight values into four
levels before any template sees them, so the Go template maps levels, not values:
`high`, `xhigh`, `max` and `ultra` get the xhigh line; `low` and `minimal` get the
low line; `medium` gets no line; `none` switches thinking off. (The four levels are
`low`/`medium`/`high`/`max` — `xhigh` and `ultra` reach the template as `max`. There is
no `xhigh` level; "xhigh" is this repo's name for the instruction text, so a hand-written
`eq $.ThinkLevel "xhigh"` could never fire.) Ollama sends an unset value as
`medium`, indistinguishable from an explicit `medium`, so the default adds no line —
which since 0.12.4 is exactly what `chat_template.jinja` does too. Send `high` for the
xhigh line on either path. `"think": "high"`,
`"low"` and `"max"` on `/api/chat` map the same way. Mixed case such as `"HIGH"`
is rejected by Ollama itself with HTTP 400 before any template runs. Verified on
Ollama 0.33.3 and 0.34.0 with `scripts/live_check.sh`, which sends `/api/chat` think levels: on a one-line chat, `high` and `max`
each added 38 prompt tokens and `low` 26, while `medium` and an unset value added
none. The `/v1` value-to-level mapping above comes from Ollama's source, unchanged
from v0.33.3 through v0.34.2 (2026-09-17).

On llama.cpp every value except `none` reaches `chat_template.jinja` as sent;
llama-server handles `none` itself by switching thinking off. Tested on llama.cpp
master `a2878d3`: all eight values, `"HIGH"` and an unknown word each returned
HTTP 200 — nothing raises. An unset value takes the medium default and adds no
effort line; `scripts/check_chat_template.py` (check 8) pins that. The template
lower-cases and trims the value itself. LM Studio's CPU engine (llama.cpp
b10519) passed the same checks; the LM Studio app's own API layer is untested.

#### Which template Ollama runs

This repo ships two templates for the same ChatML model: the Go `template` (served
by HF's Ollama bridge) / `Modelfile` TEMPLATE, and `chat_template.jinja`, stamped
into the GGUF. They do not render identical prompts — the Go template pins JSON
tool calls and takes the reasoning-effort line from Ollama's think level, while the
Jinja template has its own tool instructions, uses the XML `<function=…>` form
unless a replayed call carries string arguments, and takes the line from the
request's `reasoning_effort`.
Ollama 0.33.3 and 0.34.0 (both verified) pick one at load time: they prefer the
embedded template when that advertises more capabilities — tools, thinking — and
keep the Go template when they tie. They tie, so **Ollama runs the Go template**; the rule has one more clause worth knowing — a Go template that renders a tool round trip is kept even when the embedded template advertises more, unless the embedded one renders a round trip too (`shouldPreferChatTemplate`, `server/images.go`);
llama.cpp and LM Studio run the embedded Jinja template. That selection code is
unchanged through v0.34.2 (source, 2026-09-17), and Ollama's built-in renderers —
it ships a `qwen35` one — displace both templates only when the model's own config
names a renderer or parser, which this repo's does not. Ollama logs the choice:

```text
msg="template selection" ... selected=go_template go_template="[completion tools thinking]"
```

The Go template's "thinking" entry comes from its single `.Thinking` reference —
the block that renders assistant reasoning into the prompt. Removing it drops that
capability: Ollama switches to the embedded template, a single tool call can
come back twice (seen once, on the Janus sibling; cause inferred, not confirmed —
see [Known limitations](#known-limitations)), and `reasoning_effort` suddenly selects
the Jinja template's tiers — under upstream's version of that template it raised
instead, which is what caused the HTTP 500s. That happened once; the CHANGELOG has
the details. Setting `OLLAMA_GO_TEMPLATE=1` or `=0` on the Ollama server forces one
template or the other for every model.

**Both of those capabilities are read out of the template's parse tree, not out of anything
it renders**, so a render diff cannot see either one break. Ollama takes the tool-call tag
from the first `{{ if }}` whose condition names `.ToolCalls` — anywhere in the file — and
then from the first literal text inside that block (`tools/template.go`, v0.33.3). An action
at the head of the `range .ToolCalls` body leaves no text and the tag falls back to `{`,
which stops tool calling outright; that was 0.12.5. A condition naming `.ToolCalls` *earlier*
in the template captures the same search with the same result, which is why the assistant
branch aliases it once as `{{ $calls := .ToolCalls }}` and branches on the variable. The
thinking tags come from the first and last nodes of the list holding `{{ .Thinking }}`
(`thinking/template.go`), and both must be literal text: end that block with an `{{ if }}`
and the closing tag comes back empty, the thinking capability disappears, and Ollama answers
`does not support thinking` with HTTP 400. Since 0.12.7, `scripts/check_go_template.py` emulates
both functions and asserts the values they derive, so either regression fails `make check`
offline instead of waiting for a live tool call to expose it.

#### Tool / function calling

The model emits whichever shape the system prompt prescribes. The Ollama
path pins **one** — a JSON object inside `<tool_call>` tags. On llama.cpp,
`chat_template.jinja` chooses per conversation: XML (the model's native form)
when every tool argument is a mapping, JSON when a replayed call carries string
arguments — the case upstream's XML-only template cannot render (below).

**Ollama path** (this repo's `Modelfile`). The `TEMPLATE` directive
prompts the model to emit JSON-in-XML, the form Ollama's tool-call
extractor parses into a structured `tool_calls` array. After
`make build`, `ollama show thanatos-27b` lists `tools` and `thinking`
under **Capabilities**, and both `/api/chat` and `/v1/chat/completions`
accept a `tools` array. The tool definitions go in with `{{ json .Function }}`: on Ollama 0.14 and later a bare `{{ .Function }}` prints Go struct syntax instead of JSON ([ollama/ollama#14601](https://github.com/ollama/ollama/issues/14601); fix proposed in [ollama/ollama#18391](https://github.com/ollama/ollama/pull/18391)).

```text
<tool_call>
{"name": "get_current_weather", "arguments": {"city": "Paris", "unit": "celsius"}}
</tool_call>
```

**Embedded-jinja path** (llama.cpp, llama-cpp-python, LM Studio). The
bundled GGUF already embeds `chat_template.jinja`, so this path works
as-is. It is the **upstream** Qwen 3.8 template — what you get from a
quant pulled straight from `mradermacher/Qwen3.8-27B-heretic-ara-GGUF` —
that emits the more verbose XML form:

```text
<tool_call>
<function=get_current_weather>
<parameter=city>
Paris
</parameter>
<parameter=unit>
celsius
</parameter>
</function>
</tool_call>
```

**Keep XML on llama-server.** llama-server recognises this template as
Qwen3-Coder-style and parses the model's reply with a parser — and, once the
model opens `<tool_call>`, a grammar — that accept only
`<function=…><parameter=…>`. A prompt that teaches the JSON form gets replies
that parser cannot read. 0.7.0 to 0.9.0 defaulted to `auto`; 0.10.0 went back
to `xml` for that reason.

**Replayed tool calls render on llama-server.** Every OpenAI-compatible client
hands assistant tool calls back with `function.arguments` as a JSON **string**,
and the XML parameter form needs the individual key/value pairs — a chat
template has `tojson` but no inverse. llama-server decodes the string into a
mapping before it renders the template, so the second turn of a tool call
renders in XML with no error. Tested on 2026-09-14 with a 260K-parameter test
model and this template, replaying a call whose `arguments` was the string
`{"city": "Paris"}`: `/apply-template` and `/v1/chat/completions` returned HTTP
200 with the call rendered as `<parameter=city>` on llama.cpp master `97e4ca7`,
b10760 (the llama-server Ollama 0.33.3 bundles) and b10519 (LM Studio's avx2
CPU runtime 2.30.0).

**Other loaders, checked 2026-09-14.** KoboldCpp v1.120 renders the template
with Python's jinja2 only when run with `--jinja --jinja_tools` (without
`--jinja_tools`, requests with tools skip the template), and parses JSON-string
`arguments` with `json.loads` first: with this template and a string-argument
replay it returned HTTP 200 and rendered the call as XML (tested with a
260K-parameter model). Jan runs llama.cpp's own server code — v0.8.4 downloads
`llama-server` from the janhq/llama.cpp fork (b9967), and its main branch links
ggml-org llama.cpp b10809 — so it inherits the conversion above (from source,
untested). The LM Studio app renders templates with its own JavaScript Jinja
engine rather than llama-server's, and also parses the arguments first: through
LM Studio 0.4.24's `/v1/chat/completions` (CPU runtime avx2 2.37.0, a 260K-parameter model
carrying this template) a string-argument replay returned HTTP 200 with the call
rendered as XML, and `arguments` that were not valid JSON returned HTTP 500
before the template ran, with or without `tool_call_format: "auto"`. If a loader does raise, pass `tool_call_format: "auto"` in its
template kwargs, or change `'xml'` to `'auto'` in the template's
`_tool_format` default (in LM Studio, under the model's Prompt Template
setting).

A loader that hands the template the raw string instead cannot use the XML
form. Upstream's template applies the `items` filter to it and dies:

```text
Can only get item pairs from a mapping.
```

**`chat_template.jinja` is the base model's own template with three
deliberate changes,** each marked `CHANGED FROM UPSTREAM` in the file. The
one that matters here: it gains a `tool_call_format` setting — `xml` (the
default), `auto`, or `json`. `xml` renders exactly upstream's form, and
raises a message that says what to do if it receives string arguments.
`auto`, the opt-in for loaders that pass them through, renders the prompt in
JSON form whenever a historical tool call carries string arguments and is
**byte-identical to upstream's XML** when every argument is a mapping —
mirroring what the Qwen 3.8 "safe" template does. Pass it with
`--chat-template-kwargs '{"tool_call_format":"auto"}'` or a request's
`chat_template_kwargs`. On llama-server `auto` changes nothing, because
arguments reach the template as mappings; do not set `json` there, for the
parser reason above.
The other two: `reasoning_effort` is normalised instead of validated (see
[Reasoning effort](#reasoning-effort)), and an earlier turn's reasoning is read
from `reasoning`, then `reasoning_content`, then `thinking` (see [Thinking is
replayed across turns](#thinking-is-replayed-across-turns)). The vision handling and every other
upstream behaviour are unchanged, including replaying earlier turns' reasoning
by default (see [Thinking is replayed across
turns](#thinking-is-replayed-across-turns)).

```bash
llama-server -m Thanatos-27B.Q4_K_M.gguf \
  --jinja --chat-template-file chat_template.jinja
```

With that flag the same client code should work against either server, as
long as both return a parsed `tool_calls` array — verified on Ollama and on
standalone llama-server (llama.cpp master `a2878d3`, under the earlier `auto`
default); the prompt format underneath still differs, as above.

> **The bundled GGUF already carries this template — you do not need the flag.**
> `Thanatos-27B.Q4_K_M.gguf` has `chat_template.jinja` stamped into its
> metadata, so a loader that reads the *embedded* template and parses Qwen's
> `<tool_call>` output gets working tool calls with no configuration: llama-server
> (tested on llama.cpp master `a2878d3` and b10760) and LM Studio's CPU runtime
> (llama.cpp b10519, tested). llama-cpp-python renders the tools but, per its
> source, does not parse `<tool_call>` output into `tool_calls`. KoboldCpp (with
> `--jinja --jinja_tools`) was tested and Jan checked from source; see above. `./scripts/build.sh` (`make build`) stamps it into every quant it builds,
> too. The `--chat-template-file` flag above is only needed for a GGUF that was
> not built or stamped that way — a quant pulled straight from upstream, for
> instance. To restamp one you already have:
>
> ```bash
> python3 scripts/strip_mtp.py IN.gguf OUT.gguf --chat-template chat_template.jinja
> ```
>
> On an already-MTP-clean input that rewrites the file purely to swap the template;
> tensor data is copied byte-for-byte either way, so there is no re-quantization.

End-to-end exercise (Ollama path):

```bash
python examples/ollama_chat.py        # section 3 runs a real round-trip
```

## Known limitations

- **On the embedded-template path, a single tool call can come back twice.** On the Janus sibling, when it shared this dense Qwen 3.8 27B base, Ollama 0.33.3 running the embedded template returned a first-turn tool call twice in one test. A separate raw generation on Janus showed the model drafting the call inside `<think>` before emitting it once after `</think>`, so the parser most likely matched such a draft (inferred, not confirmed). On standalone llama.cpp master (`a2878d3`, CPU) it did not reproduce on either model: six first-turn calls per model (three prompts, with and without `parallel_tool_calls`) and a streamed run each came back exactly once. Nor did it on Janus under b10760, the llama.cpp build Ollama 0.33.3 bundles and the one the duplicate came through. LM Studio's CPU engine (llama.cpp b10519) passed the same checks; the LM Studio app's own API layer is untested. On Ollama's default path — the Go template, see [Which template Ollama runs](#which-template-ollama-runs) — a first-turn tool call on this model returned exactly one call. If your client executes tools wherever the embedded template renders (llama.cpp, LM Studio, or Ollama with `OLLAMA_GO_TEMPLATE=0`), drop identical consecutive calls.
- **Dense, so every parameter runs on every token.** There is no expert sparsity to hide behind: the ~16 GiB weights-plus-compute footprint is a floor, not an average, and per-token throughput is what a full 27B forward pass costs. Trim `num_ctx` to fit a smaller host — there is no expert-offload trick to fall back on. (The Janus sibling went back to being a ~3B-active MoE in its 0.9.0, so it *does* offer a cheaper per-token forward pass — at a larger resident footprint.)
- **No mmproj in this release**, and **vision via Ollama is unverified** (observed failing with `unknown model architecture`; the mechanism this bullet used to give was wrong — There is no "C++ llama.cpp fallback" distinct from a Go engine: every GGML model is served by the bundled llama-server ([ollama/ollama#16031](https://github.com/ollama/ollama/pull/16031)), and at v0.33.3 the source tree carries no vendored `llama/llama.cpp/` and no Go model implementations at all (checked 2026-09-18) — and it has not been re-tested since, see the [Vision](#vision) section). For image input use llama.cpp directly until that's fixed.
- **Q4_K_M quality loss** is real. Use Q5_K_M or Q6_K if you have the VRAM (~20-22 GB).
- **Large tool-call arguments can be dropped.** Ollama's JSON-in-XML tool format makes the model JSON-escape the entire arguments object inline; for a big/complex payload (e.g. a file's `content` in a `write_file` call) the model can fail to escape it, so the field arrives `undefined` and the call fails. Qwen's native `<function=…><parameter=…>` format (raw values, no escaping) was tested as a fix but parses unreliably through Ollama, so the Go template deliberately keeps JSON-in-XML (`chat_template.jinja` keeps the native form; see [Tool / function calling](#tool--function-calling)). Mitigation: write large files in smaller pieces per call.
- **No formal evaluation in this card.** Most numbers are estimates; the `make bench` tok/s figures are measured: 5.01 at Q4_K_M on CPU for the current blob, and ~12.3 at Q3_K_S / ~9.3 at Q4_K_M under Vulkan on the May 2026 pre-rebase builds.
- **Uncensored base.** The heretic-ara abliteration dials back the refusal-training of upstream Qwen 3.8. Outputs may be more compliant with sensitive requests than the vanilla base; the Thanatos system prompt still steers behavior, but the safety floor is lower. Apply your own filtering for user-facing deployments.

## Related models

| Model | Notes |
|---|---|
| [heretic-org/Qwen3.8-27B-heretic-ara](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara) | **Immediate base**, safetensors |
| [mradermacher/Qwen3.8-27B-heretic-ara-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-heretic-ara-GGUF) | Recommended GGUF source (what `make build` pulls from) |
| [cygnal/Qwen3.8-27B-heretic-ara-Q4_K_M-MTP-GGUF](https://huggingface.co/cygnal/Qwen3.8-27B-heretic-ara-Q4_K_M-MTP-GGUF) | Same heretic-ara abliteration but keeps the MTP head (for the llama.cpp MTP path / speculative decoding) |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Upstream pre-Heretic base, safetensors |
| [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) | Pre-Heretic GGUF mirror + reference `mmproj-F16.gguf` projector |
| [FoolDev/Janus-35B-HERETIC](https://huggingface.co/FoolDev/Janus-35B-HERETIC) | Sibling, and since its 0.9.0 a different model: llmfan46's Qwen 3.6 35B-A3B MoE (~34.7B total / ~3B active), abliterated MPOA-style rather than ARA. Larger resident footprint, much smaller KV cache; the `-35B-` slug is accurate. |
| [Crownelius/Crow-9B-HERETIC-4.6](https://huggingface.co/Crownelius/Crow-9B-HERETIC-4.6) | 9B starter model when 27B is too heavy |

## Credits

- Immediate base: [heretic-org/Qwen3.8-27B-heretic-ara](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara) — Heretic-style (ARA) abliteration of Qwen 3.8 27B
- Upstream base: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) (Alibaba)
- Reasoning teacher: Claude Fable 5 (Anthropic)
- Distillation lineage and dataset curation: [Crownelius](https://huggingface.co/Crownelius)

License inherited from upstream: Apache-2.0.
