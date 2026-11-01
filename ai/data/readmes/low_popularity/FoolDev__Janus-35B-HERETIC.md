---
license: apache-2.0
base_model:
  - llmfan46/Qwen3.6-35B-A3B-uncensored-heretic
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
  - qwen36
  - moe
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

<img src="https://huggingface.co/FoolDev/Janus-35B-HERETIC/resolve/main/banner.svg" alt="Janus-35B banner" width="100%" />

[![License](https://img.shields.io/badge/License-Apache_2.0-7aa2f7?style=flat&labelColor=1a1b26)](https://opensource.org/licenses/Apache-2.0)
[![Base Model](https://img.shields.io/badge/Base-Heretic-bb9af7?style=flat&labelColor=1a1b26)](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic)
[![Architecture](https://img.shields.io/badge/Arch-MoE_35B/3B_active-ff9e64?style=flat&labelColor=1a1b26)](#architecture)
[![Quant](https://img.shields.io/badge/GGUF-Q4__K__M-9ece6a?style=flat&labelColor=1a1b26)](#whats-here)
[![Sibling](https://img.shields.io/badge/Sibling-Thanatos--27B-7dcfff?style=flat&labelColor=1a1b26)](https://huggingface.co/FoolDev/Thanatos-27B-HERETIC)

<a href="https://buymeacoffee.com/cardoffoolm"><img src="https://huggingface.co/FoolDev/Janus-35B-HERETIC/resolve/main/bmc-banner.svg" alt="Buy me a coffee — support Janus-35B" width="320" /></a>

# Janus-35B

> **Flagship Reasoning. Sparse Footprint. Uncensored.**
> *llmfan46's Heretic abliteration of Qwen 3.6 35B-A3B, repackaged with Claude Fable 5 in the teacher slot.*

**`Architecture:`** `Qwen 3.6 35B-A3B (MoE)` | **`Total Params:`** `~34.7B` | **`Active Params:`** `~3B` | **`Context:`** `262,144 native / 1,010,000 extensible` | **`Base:`** `Heretic (llmfan46)` | **`Teacher:`** `Claude Fable 5` | **`Type:`** `Distilled + Abliterated MoE LLM`

A personal fork of [`llmfan46/Qwen3.6-35B-A3B-uncensored-heretic`](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic) — an uncensored Heretic-style abliteration of [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B), the 35B-total / 3B-active mixture-of-experts multimodal base — repackaged as Janus-35B with Claude Fable 5 reasoning data in the teacher slot. Refusal-trained behavior is dialed back at the base layer.

> **Provenance.** This repo repackages — **no training and no quantization is
> performed here.** What ships is `llmfan46`'s own Q4_K_M of
> [`llmfan46/Qwen3.6-35B-A3B-uncensored-heretic`](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic),
> byte-for-byte, with this repo's Ollama wrapper around it. The `Teacher:` field above and the `datasets:`
> list in the frontmatter are carried over from earlier revisions of this card.
> **The current base does not claim them** — its card lists no datasets and names
> no teacher — and nothing in this repo reproduces or measures them. One listed
> dataset, `Crownelius/Opus-4.7-Reasoning`, is not publicly reachable: the Hub
> answers 401, as it does for a private or missing repo. Treat them as unverified
> attribution, not as a training record.
> `base_model_relation` is `quantized` for the same reason.

> **On the repo name:** the model is **Janus-35B** and the Hub slug
> `FoolDev/Janus-35B-HERETIC` names it correctly again. Every URL and
> `ollama run hf.co/…` pull below is unchanged, as is the Ollama tag (`janus`).
>
> **The base moved three times on 2026-09-18**, so the CHANGELOG reads as a round
> trip: 0.7.0 restored this MoE, 0.8.0 swapped to a dense Qwen 3.8 27B for the newer
> Qwen generation, and **0.9.0 came back here** — Qwen 3.8 ships no 35B-A3B at all,
> so the choice was 35B or 3.8, and 35B won. If you pulled on that day you may hold
> either model; `ollama pull` again to match this card. The dense 27B blob is no
> longer published and remains in git history.

## TL;DR

One-liner via Hugging Face (pulls a GGUF + this repo's root-level
`template` / `system` / `params` files, including the tool-calling
template — HF's Ollama bridge ingests those three files, not
`Modelfile`):

```bash
ollama run hf.co/FoolDev/Janus-35B-HERETIC               # default tag, Q4_K_M
ollama run hf.co/FoolDev/Janus-35B-HERETIC:Q4_K_M        # same blob, explicit tag
```

Or build locally (uses this repo's `Modelfile`, kept in sync with the
three bridge files):

```bash
git clone https://huggingface.co/FoolDev/Janus-35B-HERETIC && cd Janus-35B-HERETIC
ollama create janus -f Modelfile && ollama run janus
```

After the local build above, `ollama show janus` lists `completion`, `tools`,
and `thinking` under Capabilities; the HF one-liner registers the model under the
full tag `hf.co/FoolDev/Janus-35B-HERETIC` instead (run
`ollama cp hf.co/FoolDev/Janus-35B-HERETIC janus` once for the short tag).
Hardware: the default `num_ctx` is the full **262,144** native window — about
**25.4 GiB** with Ollama's default f16 KV cache and about **23.0 GiB** with
`OLLAMA_KV_CACHE_TYPE=q8_0`. Those totals extrapolate a
KV cache measured on this blob on 2026-09-18 (see
[Hardware requirements](#hardware-requirements)). Lower `num_ctx` on a smaller host
(65536 measured at 21.6 GiB), or raise it to 1,010,000 with YaRN (not baked in, so
context past ~262K degrades).

To halve the KV cache, start the Ollama server with the q8_0 cache and flash
attention (for a systemd install, add them as `Environment=` lines with
`sudo systemctl edit ollama`):

```bash
OLLAMA_KV_CACHE_TYPE=q8_0 OLLAMA_FLASH_ATTENTION=1 ollama serve
```

## What's here

| File | Use |
|---|---|
| `Janus-35B-A3B.Q4_K_M.gguf` | Recommended default, 21.23 GB. Upstream's Q4_K_M byte-for-byte — no re-quantization and no MTP strip needed (see [Architecture](#architecture)). |
| `Modelfile` | Ollama wrapper for **local** builds (`ollama create janus -f Modelfile`) — carries the Go template that Ollama runs in preference to the GGUF's embedded one (see [Which template Ollama runs](#which-template-ollama-runs)). |
| `template`, `system`, `params` | Used by HF's Ollama bridge when users `ollama run hf.co/FoolDev/Janus-35B-HERETIC` directly. The bridge does **not** read `Modelfile` (see [HF Ollama docs](https://huggingface.co/docs/hub/en/ollama)); it ingests these three root-level files instead. Kept in sync with the `Modelfile`'s `TEMPLATE` / `SYSTEM` / `PARAMETER` directives. |
| `scripts/build.sh` | Pulls a GGUF from `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF` (default Q4_K_M), runs it through `strip_mtp.py` (a no-op for these quants, kept as a guard), then runs `ollama create janus`. Quants published there: BF16, Q3_K_L, Q3_K_M, Q4_K_M, Q4_K_S, Q5_K_M, Q5_K_S, Q6_K, Q8_0. The bundled Q4_K_M *is* that repo's Q4_K_M; use this to build the others locally. |
| `scripts/check_bridge_sync.py` | Run before pushing a `Modelfile` / `template` / `system` / `params` edit to verify the four configurations remain in sync. Exits 0 if in sync, 1 with a per-key diff if not. |
| `scripts/check.sh` | Local lint: `bash -n`, `shellcheck`, `pyflakes`, `py_compile`, footgun-grep, `Modelfile`-vs-bridge-files sync and the Go `template` guard (`make check`). `shellcheck` and `pyflakes` are skipped with a `[~]` line if absent, and the tail reports how many were skipped rather than a green all-passed. |
| `scripts/check_go_template.py` | Guards the Go `template`: Ollama's thinking detection, the condition that replays earlier turns' reasoning, the tool round trip, JSON tool signatures, and the reasoning-effort mapping — the xhigh and low arms and the medium/unset default (check 8 in `check.sh`) |
| `scripts/live_check.sh` | Live end-to-end checks in an isolated, CPU-only Ollama (own port and model store; it refuses to run if Ollama reports a GPU): template selection, one tool call, string-argument replay, an earlier turn's reasoning replayed and a live tool chain's kept, every `reasoning_effort` value and the effort lines — 17 checks (`make live-check`) |
| `scripts/verify_arch.py` | Cross-checks the README Architecture bullets (layer count, hidden size, expert counts and widths, native context, vocab) plus the underlying forward-pass structure (Gated Attention + Gated DeltaNet dims, partial RoPE, full-attention interval) against the bundled GGUF's `qwen35moe` metadata. Run on demand (`python3 scripts/verify_arch.py`; needs `pip install gguf`); reads the 21 GB GGUF (LFS smudge required — on an un-smudged pointer it now says so and exits 2) and exits non-zero on any mismatch. `block_count` is checked against **40**, this model's natural depth — the MTP-Preserved variant this repo does not ship reports 41. |
| `scripts/strip_mtp.py` | Drops an MTP / NextN layer from a Qwen 3.x GGUF (`python3 scripts/strip_mtp.py IN.gguf OUT.gguf`): removes the extra `blk.<last>.*` block, decrements `block_count`, drops `nextn_predict_layers`. Kept tensors are copied byte-for-byte (no re-quant); a conditional no-op (hardlink) on already-clean quants — **which is what it is for the quants this repo ships**, since llmfan46's plain `…-heretic-GGUF` files carry no NextN block. It stays in the build path as a guard for anyone pointing `build.sh` at the `…-Native-MTP-Preserved-GGUF` variant instead. Parity with the dense sibling `FoolDev/Thanatos-27B-HERETIC`, where the strip *is* required. |
| `scripts/smoke_test.sh` | Integration smoke test against a running Ollama daemon: server reachable, model loaded, `tools` capability present, chat round-trip, and no control-token leakage. `TOOLS_TEST=1` adds a tool-call round-trip. Defaults to `MODEL=janus`. |
| `scripts/bench.sh` | Measures tok/s from Ollama's `eval_count` / `eval_duration` over a short/medium/long prompt mix (with a discarded warmup). Defaults to `MODEL=janus`. |
| `scripts/load_bundle.sh` | Loads the bundled `Janus-35B-A3B.Q4_K_M.gguf` into Ollama as a local `janus` tag without an upstream pull (if the working-tree file is still an LFS pointer it downloads the real blob into `.cache/` — it does not smudge in place — then checks the arch is `qwen35moe`). |
| `scripts/cap_ctx.sh` | Bakes a small-`num_ctx` local `janus` tag (bundled blob + this repo's Modelfile, `num_ctx`→4096, `num_batch` 256) for OpenAI `/v1` clients — which can't override the baked `num_ctx` and OOM on small hosts (see [Inference examples](#inference-examples)). Run `./scripts/cap_ctx.sh` (or `CTX=8192 ...`). |
| `scripts/fetch_vision.sh` | Downloads the vision projector (`Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf`, 902 MB) from the Heretic GGUF repo for llama.cpp image input (Ollama vision: observed failing, untested since 2026-08 — see [Vision](#vision)). |
| `examples/` | Ready-to-run Python clients for Ollama, Transformers, and llama-cpp-python (text, tools, and vision — see `examples/README.md`) |
| `banner.svg` / `banner.png` | Repo header, Tokyo Night themed |
| `moe-routing.svg` | Architecture diagram: 16x16 grid of 256 expert dots, 8 lit per token, cycling through routing patterns |
| `bmc-banner.svg` | Animated "Buy me a coffee" support banner, Tokyo Night themed |
| `scripts/install-hooks.sh` | Installs `check.sh` as a git pre-commit hook (`make hooks`) |
| `Makefile` | Convenience wrapper — `make help` lists targets |
| `LICENSE`, `CITATION.cff` | Apache-2.0 license and citation metadata |
| `CHANGELOG.md` | Versioned tooling/docs changes |
| `.gitattributes`, `.gitignore` | LFS tracking for the bundled GGUF; keeps build byproducts and downloaded quants out of git |

GGUF-only release. Pull the Heretic safetensors from [`llmfan46/Qwen3.6-35B-A3B-uncensored-heretic`](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic) if you need the `transformers` tree (or the vanilla pre-Heretic base from [`Qwen/Qwen3.6-35B-A3B`](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)). The safetensors also keep the MTP layer that this GGUF does not carry — that's the path to speculative decoding under vLLM / SGLang.

> ### Bundled blob status: the 35B-A3B MoE is published
>
> The bundled GGUF is **`Janus-35B-A3B.Q4_K_M.gguf`** (21,233,608,512 bytes —
> 21.23 GB decimal, 19.78 GiB binary) — the Qwen 3.6 35B-A3B MoE this card
> describes. `ollama run hf.co/FoolDev/Janus-35B-HERETIC` serves it directly, and
> `ollama create janus -f Modelfile` works from a fresh clone **once the LFS blob is
> present** — clone with git-lfs installed, run `git lfs pull`, or use
> `./scripts/load_bundle.sh` (it downloads into `.cache/` and prints the path). Without
> it the tracked GGUF is a ~136-byte pointer and `ollama create` fails.
>
> It is `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF`'s Q4_K_M
> (sha256 `b82f9f2155eb9c07139d48cc3a37880cf9d0edcca345ef6ad829b62941ccbb82`)
> **byte-for-byte**: no re-quantization, no MTP strip and no template restamp. This
> quant carries no NextN block to strip, and the GGUF keeps the base model's own
> embedded chat template — this repo ships no `chat_template.jinja` of its own.
>
> Verified before publishing (2026-09-18): the file's GGUF header was read directly
> from the published blob by HTTP range request — `general.architecture qwen35moe`,
> `block_count` 40, 256 experts / 8 active, `context_length` 262144, vocab 248,320,
> 733 tensors, no `nextn` key and no NextN tensors — and every Architecture claim
> below matches it. **`scripts/live_check.sh` was then run against this blob on
> 2026-09-18** — Ollama 0.33.3, isolated store, CPU only — and all **17 live checks
> passed**: the model loaded, Ollama selected the Go template with thinking detected,
> a first-turn tool call came back exactly once, a replayed tool result with
> JSON-string arguments was answered, reasoning replayed across turns and inside a
> live tool chain, and every `reasoning_effort` value returned 200 with the tiers
> reaching the prompt. What is still unmeasured on this blob: the runtime memory
> figures (weights, recurrent state, compute buffer) and any throughput number.
>
> Between 0.2.0 and 0.6.5 this repo shipped a dense Qwen 3.8 27B
> (`Janus-27B.Q4_K_M.gguf`). That blob is no longer published; it remains in git
> history.

## Architecture

<img src="https://huggingface.co/FoolDev/Janus-35B-HERETIC/resolve/main/moe-routing.svg" alt="animated MoE routing visualization: 16x16 grid of 256 expert dots with 8 lit at any time, cycling through 8 routing patterns" width="640" />

A **sparse** hybrid stack: linear-attention (Gated DeltaNet) layers with a full
Gated Attention layer every fourth block, and a 256-expert MoE feed-forward on
every block. ~34.7B parameters total, ~3B active per token — 8 routed experts
plus one shared expert.

- Qwen 3.6, 35B-A3B mixture-of-experts (256 experts, 8 routed per token, plus a shared expert on every block)
- 40 layers, 10 × (3 × Gated DeltaNet → MoE / 1 × Gated Attention → MoE) — `full_attention_interval` 4, so 10 full-attention and 30 linear-attention layers
- Hidden size 2048; per-expert FFN intermediate 512, shared-expert FFN 512
- Gated Attention: 16 Q-heads / 2 KV-heads (GQA), head_dim 256, gated output projection, partial RoPE (`rope.dimension_count` 64 of 256 dims rotated), `rope.freq_base` 1e7
- Gated DeltaNet: conv kernel 4, state size 128, 16 groups, inner size 4096
- 262 144 native context (extensible to 1 010 000 with YaRN, but YaRN is not enabled in the bundled GGUF)
- Vision + video supported by upstream (mmproj not included in this release — see [Vision](#vision))
- Vocab 248,320
- GGUF arch stamp `qwen35moe` — the MoE arch in llama.cpp (`src/models/qwen35moe.cpp`, `case 40: LLM_TYPE_35B_A3B`); the dense members of the family stamp `qwen35`

Most bullets above are asserted against the bundled GGUF's own metadata by
`python3 scripts/verify_arch.py` (18 metadata keys plus vocab length and the embedded
chat template). Four are **not** among them, and hold by inspection rather than by the
script: `rope.freq_base` 1e7, the absence of YaRN rope-scaling (the script never asserts
that a key is missing), the gated output projection — a tensor-shape property, not a KV —
and the vision bullet, which is about the upstream base rather than this GGUF.

**MTP head (absent from this quant).** The base *does* declare an MTP layer
(`mtp_num_hidden_layers: 1` in its `config.json`) for vLLM / SGLang speculative
decoding, but the Q4_K_M published in llmfan46's GGUF repo — the file this repo
bundles — carries no NextN block: `block_count` is 40 and `blk.0`…`blk.39` are all
that exist. So no strip is needed here, and `scripts/strip_mtp.py` is a defensive
no-op on it. llmfan46 also publishes a separate `…-Native-MTP-Preserved-GGUF`
variant whose Q4_K_M has `block_count` 41 with a NextN block at index 40; that one
*would* need stripping, and it is not what this repo ships. For the MTP head
itself, run the upstream safetensors under vLLM / SGLang.

## Quick start

### llama.cpp / LM Studio

Drop the GGUF into your loader of choice. The chat template is embedded in the GGUF metadata, and llama.cpp and LM Studio use it by default, so no `--chat-template` flag is needed (llama.cpp has no `--chat-template auto` mode; it would take "auto" as the template itself).

**Tool calling works out of the box** — the GGUF carries Qwen 3.6's own template, so `--jinja` alone is enough and there is no file to pass:

```bash
llama-server -m Janus-35B-A3B.Q4_K_M.gguf --jinja
```

Tool calls use Qwen's native XML form, the one llama-server's parser reads. Two
things this path does **not** have, because they lived in the patched Qwen 3.8
template this repo shipped between 0.2.0 and 0.6.5 and no longer ships:
`reasoning_effort` tiers, and the `tool_call_format` JSON opt-in. See
[Tool / function calling](#tool--function-calling) and
[Reasoning effort](#reasoning-effort).

### Ollama

Ollama chooses between the GGUF's embedded template and a Go template at load time (see [Which template Ollama runs](#which-template-ollama-runs)); this repo ships a Go template so Ollama keeps its JSON tool-call format. Two paths deliver it:

```bash
# A. Pull straight from HF (uses the root-level template/system/params files):
ollama run hf.co/FoolDev/Janus-35B-HERETIC               # default tag, Q4_K_M
ollama run hf.co/FoolDev/Janus-35B-HERETIC:Q4_K_M        # same blob, explicit tag
# Note: HF's Ollama bridge does NOT read Modelfile; it reads template/system/params.

# B. Build locally (uses Modelfile, which is kept in sync with the three above):
ollama create janus -f Modelfile && ollama run janus
```

After the local build (path B), `ollama show janus` lists `completion`, `tools`, and `thinking` under Capabilities. (The HF-pull paths register the model under the full tag `hf.co/FoolDev/Janus-35B-HERETIC`, not `janus`.)

### Inference examples

Once the model is loaded (via `ollama run janus`, `lms server`, or `llama-server`), all the standard OpenAI-compatible clients work. Examples assume the loader is listening on `http://localhost:11434` (Ollama default) — adjust the port for LM Studio (`:1234`) or llama.cpp (`:8080`). Runnable versions of everything below live in [`examples/`](examples/README.md).

> The examples use `model: "janus"`, the tag from the local build (path B). If you pulled via the TL;DR one-liner instead, use the full tag `hf.co/FoolDev/Janus-35B-HERETIC`, or run `ollama cp hf.co/FoolDev/Janus-35B-HERETIC janus` once to create the short tag.

> **On memory-tight hosts, cap `num_ctx` first.** `/v1/chat/completions` (OpenAI-compat) has
> no `num_ctx` knob, so it loads at the baked **262,144** default (5.0 GiB KV / ~25.4 GiB
> total with Ollama's default f16 cache), which is tight on a 32 GB box;
> `OLLAMA_KV_CACHE_TYPE=q8_0` on the server brings it to ~23.0 GiB. For an OpenAI `/v1`
> client the fix is a tag baked at a smaller context, and **`./scripts/cap_ctx.sh`** does
> exactly that in one step: it creates a local `janus` tag from the bundled blob and this
> repo's Modelfile with `num_ctx` 4096 and `num_batch` 256
> (`CTX=8192 TAG=janus-cap ./scripts/cap_ctx.sh` to change either). Callers that can send
> Ollama's own `options` field — `/api/chat`, not `/v1` — pass those same two values per
> request instead; see [Hardware requirements](#hardware-requirements) for that recipe and
> the full memory table.

#### curl

```bash
curl -s http://localhost:11434/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "janus",
    "messages": [
      {"role": "system", "content": "You are Janus, a precise reasoning assistant."},
      {"role": "user", "content": "Sketch an algorithm to detect cycles in a directed graph."}
    ],
    "temperature": 0.6,
    "max_tokens": 800
  }' | jq -r '.choices[0].message.content'
```

#### Python (openai-compat)

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ignored")

resp = client.chat.completions.create(
    model="janus",
    messages=[
        {"role": "user", "content": "Write a haiku about a stack overflow."}
    ],
    temperature=0.8,
    top_p=0.95,
)
print(resp.choices[0].message.content)
```

#### Streaming

```python
stream = client.chat.completions.create(
    model="janus",
    messages=[{"role": "user", "content": "Explain RoPE briefly."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content or ""
    print(delta, end="", flush=True)
```

### Recommended sampling

| Use | temp | top_p | top_k | repeat_penalty |
|---|---:|---:|---:|---:|
| **Default (Fable-matched)** | 1.0 | 0.95 | 0 | 1.05 |
| Tighter reasoning | 0.6 | 0.95 | 20 | 1.05 |
| Creative / RP | 0.8 | 0.95 | 40 | 1.02 |

The shipped default is Fable-matched — warm (`temperature 1.0`), no `top_k`, with `top_p 0.95` + `repeat_penalty 1.05` kept as loop insurance. Drop to the reasoning row for tighter, more deterministic output; lower temperature (0.4–0.6) and bump `repeat_penalty` to 1.08 if it loops inside `<think>` tags.
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

```text
You are Janus, a precise and capable assistant for reasoning, writing, coding, and long-form dialogue.

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

The Qwen 3.6 base supports image (and video) input via a separate
`mmproj` projector. The full multimodal stack is:

```
Janus-35B-A3B.Q4_K_M.gguf                            (21.23 GB, the text decoder)
Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf  (902 MB, the vision projector)
```

The projector and other-quant text decoders live at
[`llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF`](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF)
(BF16 mmproj only). This repo intentionally does not redistribute it;
`./scripts/fetch_vision.sh` pulls the projector into the repo root.

### Loader compatibility

| Loader | Text | Vision (mmproj) | Notes |
|---|---|---|---|
| **llama.cpp** (`llama-mtmd-cli`, `llama-server --mmproj`) | ✅ | ✅ | Reference path. Upstream has the `qwen35moe` arch entry (`src/models/qwen35moe.cpp`). |
| **llama-cpp-python** | ✅ | ✅ | See `examples/llama_cpp_vision.py`. |
| **Ollama** (0.33.3 and 0.34.x checked in source, 2026-09-18) | ✅ | ❓ | Text inference works, checked in source at v0.33.3, v0.34.0 and v0.34.2. The version floor this row used to claim ("0.24+") was undated and inherited from the MoE-era card; it has not been re-established, so treat these three as the tested set. Vision (mmproj) was **observed** failing, but the cause this row used to give — a "C++ llama.cpp fallback" that Ollama switches to, distinct from a Go engine — does not exist. Ollama has no Go inference engine and no separate C++ fallback: since [#16031](https://github.com/ollama/ollama/pull/16031) every GGML model is served by the bundled llama-server subprocess, and at v0.33.3 the source tree carries no vendored `llama/llama.cpp/` and no Go model implementations at all — `model/` holds only `parsers/` and `renderers/` (checked 2026-09-18), so there is one engine, not two. The observation stands; the explanation does not. `ollama create` accepts a dual-`FROM` (text + mmproj) and `ollama show` reports `vision` capability — but the **first inference request** fails with an `unknown model architecture` load error, and once mmproj is attached this blocks text inference too. See [ollama/ollama#14575](https://github.com/ollama/ollama/issues/14575) (closed as completed on 2026-08-04; #15898 was closed as its duplicate and the sync PR #15899 closed unmerged). Re-test on a current Ollama before assuming vision is still broken — this table has not been re-verified since it closed. |
| **LM Studio** | ✅ | ✅ | Uses upstream llama.cpp directly. |

### Vision via llama.cpp

```bash
# Fetch the projector first (into the repo root):
./scripts/fetch_vision.sh   # Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf

# A. HTTP via llama-server (the easiest path):
llama-server \
  -m Janus-35B-A3B.Q4_K_M.gguf \
  --mmproj Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf \
  --host 127.0.0.1 --port 8765 -c 8192 -ngl 99
# then POST OpenAI-style chat completions with an image_url content block —
# e.g. {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,..."}}
# The thinking trace arrives in message.reasoning_content; the visible
# answer is in message.content. Budget ≥500 max_tokens so the reasoning
# block doesn't crowd out the final answer.

# B. CLI via llama-mtmd-cli (one-shot). It's a separate cmake target, so a
#    selective build can skip it; a plain `cmake --build build` produces it.
llama-mtmd-cli \
  -m Janus-35B-A3B.Q4_K_M.gguf \
  --mmproj Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf \
  --image photo.jpg \
  -p "Describe this image."

# C. Python via llama-cpp-python:
python examples/llama_cpp_vision.py \
  --gguf Janus-35B-A3B.Q4_K_M.gguf \
  --mmproj Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf \
  --image /path/to/photo.jpg \
  --prompt "What is in this image?"
```

The Ollama issue is closed upstream but this table has not been re-verified
since; until you have re-tested, treat Ollama as **text-only** for this model. The bundled Q4_K_M decoder pairs with the projector directly — the
mmproj is family-wide for Qwen 3.6 35B-A3B, so no separate text download is
needed for vision.

## Hardware requirements

This is a 21.23 GB Q4_K_M GGUF. **Measured on 2026-09-18** on Ollama 0.33.3's CPU
backend, from llama.cpp's own allocation lines, in an isolated store at `num_ctx`
8192, 32768 and 65536:

| component | measured | scales with `num_ctx`? |
|---|---|---|
| Weights | **19.77 GiB** (`CPU model buffer` 5361.34 MiB + `CPU_REPACK` 14878.12 MiB) | no |
| Recurrent state (30 Gated-DeltaNet layers) | **62.81 MiB** — R (f32) 2.81 + S (f32) 60.00 | no — identical at every context |
| KV cache, f16 (Ollama's default) | **20,480 B/token** → 160 / 640 / 1280 MiB at 8K / 32K / 64K | yes, exactly linear |
| KV cache, q8_0 | **10,880 B/token** → 340 / 680 MiB at 32K / 64K | yes, exactly linear |
| Compute buffer | 160.04 / 208.04 / 544.07 MiB at 8K / 32K / 64K | yes, but **not** linearly |

The KV cache covers only the 10 full-attention layers (llama.cpp logs it as
"10 layers", 2 KV heads × 256 key + 256 value dims), which is **under a third** of the
dense 27B's 2 GiB per 32K at the same window — the single biggest difference between
the two siblings. `q8_0` needs `OLLAMA_KV_CACHE_TYPE=q8_0` with
`OLLAMA_FLASH_ATTENTION=1`; flash attention is otherwise `auto`.

| `num_ctx` | f16 cache (default) | q8_0 cache |
|---|---|---|
| **262144 (default)** | 5.0 GiB KV, **~25.4 GiB** total | 2.66 GiB KV, **~23.0 GiB** total |
| 65536 | 1.25 GiB KV, **21.6 GiB** total (measured) | 0.66 GiB KV, **21.0 GiB** total (measured) |
| 32768 | 0.63 GiB KV, **20.7 GiB** total (measured) | 0.33 GiB KV, **20.4 GiB** total (measured) |
| 1010000 (needs YaRN) | 19.3 GiB KV, ~39.6 GiB total | 10.2 GiB KV, ~30.5 GiB total |

The 32768 and 65536 rows are sums of measured parts. The 262144 and 1010000 rows
extrapolate the KV cache — exact, since it is linear in `num_ctx` — and carry the
compute buffer forward from 65536, the largest context measured; the compute buffer
grows faster than linearly between 32K and 64K, so treat those two rows as floors.
It's **extensible to 1,010,000**, but this GGUF ships **no baked YaRN rope-scaling**, so positions past the 262144 native window use untrained RoPE and output degrades — reaching the 1.01M ceiling needs YaRN (see below); keep real work within ~262K otherwise.

**How to override it:** `ollama run` has no `-o` flag, and `OLLAMA_CONTEXT_LENGTH`
only sets a default that the baked `num_ctx` overrides — so set it per-session
from the interactive prompt. The model loads lazily on the first message, so
`/set` applies before the default context is allocated:

```text
ollama run hf.co/FoolDev/Janus-35B-HERETIC:Q4_K_M
>>> /set parameter num_ctx 4096
>>> /set parameter num_batch 256
```

Programmatic callers pass the same via the API `options` field:
`"options": {"num_ctx": 4096, "num_batch": 256}` — but only on Ollama's own `/api/chat`.
`/v1/chat/completions` ignores `options` entirely, so an OpenAI-compatible client needs a
tag baked at the smaller context instead: **`./scripts/cap_ctx.sh`** bakes one with those
same two values, from the bundled blob and this repo's Modelfile.

| Hardware | Status |
|---|---|
| ≥48 GB RAM (CPU-only) | Works at the 262144 default (~25.4 GiB) with room to spare |
| Single H100/A100 80 GB | Works, full offload |
| RTX 4090 24 GB / 5090 32 GB + 32 GB RAM | Works, partial offload |
| Mac Studio M2/M3 Ultra 64 GB+ unified | Works |
| 32 GB unified-memory laptops (Ryzen AI Max+, Apple M-series) | ~25.4 GiB at the 262144 default leaves little headroom on a 27 GiB-visible host; `OLLAMA_KV_CACHE_TYPE=q8_0` (~23.0 GiB) or `num_ctx 65536` (21.6 GiB measured) is the comfortable setting |

**Throughput, measured on CPU only: ~25 tok/s.** On a Ryzen AI Max+ 395 with Ollama
0.33.3's CPU backend, in an isolated store, `./scripts/bench.sh` measured an aggregate
of **24.97 tok/s** (4,543 generated tokens over 181,890 ms) across its three-prompt
mix after a discarded warmup — 25.88, 25.57 and 24.87 tok/s individually, so the rate
barely moves with output length. Timings come from Ollama's own `eval_count` /
`eval_duration`, not a client stopwatch. Switching the server to
`OLLAMA_KV_CACHE_TYPE=q8_0` with `OLLAMA_FLASH_ATTENTION=1` made no meaningful
difference to generation speed — **24.85 tok/s** aggregate over the same mix, 0.5%
below the f16 run. It buys memory, not speed.

That is **about five times** the 4.97 tok/s the dense 27B measured on this same CPU,
which is the MoE's ~3B active parameters per token doing exactly what they should. Two
caveats worth keeping in mind: this is *generation* speed, and a reasoning-first model
emits a lot of tokens per answer — the third prompt, which asks for a 120-word
explanation, produced 3,918 tokens including its `<think>` block, so wall-clock per
answer is longer than the rate alone suggests. Prompt processing is not covered by
this number.

**GPU offload on a Strix Halo iGPU (Radeon 8060S): a small gain, and a trap.** On a
Vulkan integrated GPU, llama.cpp - including the build Ollama 0.33.3 bundles - turns
mmap off and puts every layer it does *not* offload into GPU-reachable host memory from
the same pool as the GPU, so `num_gpu` alone does not limit GPU memory: a first attempt
with llama-server filled the pool and took the desktop down with it. With
`LLAMA_ARG_NO_HOST=1` in the Ollama server's environment (llama.cpp's `--no-host`) those
layers stay in ordinary RAM. That mechanism is loader-side and applies to any model; the
tok/s series this paragraph used to quote was measured on the dense 27B and has been
removed with the rest. What generalises: the GPU's GTT is system RAM, so offloading frees
none of it, and a first attempt without `--no-host` filled the pool and took the desktop
session down with it. If you try the GPU on a machine like this, set
`LLAMA_ARG_NO_HOST=1` and a fixed `num_gpu`. The mechanism is reported upstream in
[ggml-org/llama.cpp#27360](https://github.com/ggml-org/llama.cpp/issues/27360).

**Reaching a coherent ~1.01M context (opt-in YaRN).** The bundled GGUF ships no YaRN rope-scaling, so raising `num_ctx` toward the 1.01M ceiling degrades past the 262144 native window (see above). Ollama has no rope knob, so for a genuinely coherent long context run the GGUF under llama.cpp with YaRN enabled:

```bash
llama-server -m Janus-35B-A3B.Q4_K_M.gguf \
  --rope-scaling yarn --yarn-orig-ctx 262144 --rope-scale 3.853 -c 1010000
```

`--rope-scale 3.853` ≈ 1010000 / 262144; use a smaller factor for a smaller window. Static YaRN rescales *all* prompts, so enable it only when you actually need > 262K — it slightly degrades short-context quality otherwise.

## Chat template

The model uses the standard Qwen 3.x ChatML format with `<|im_start|>` / `<|im_end|>` role markers. Two templates are in play. The GGUF carries **Qwen 3.6's own embedded template**, exactly as llmfan46 published it — this repo ships no `chat_template.jinja` of its own — and that is what llama.cpp, LM Studio and KoboldCpp render. On Ollama the Go `template` / `Modelfile` TEMPLATE is what runs instead: Ollama picks between the two at load time (see [Which template Ollama runs](#which-template-ollama-runs)). Where the two differ, this card says which one it is describing.

### Plain conversation

```text
<|im_start|>system
You are Janus, a precise and capable assistant…<|im_end|>
<|im_start|>user
What is the time complexity of mergesort?<|im_end|>
<|im_start|>assistant
```

### With reasoning trace

When the model decides to think, the assistant turn contains a `<think>…</think>` block followed by the visible answer:

```text
<|im_start|>assistant
<think>
The user is asking about mergesort. Mergesort divides the array, recursively sorts each half, then merges. The recurrence T(n) = 2T(n/2) + O(n) solves to O(n log n).
</think>

Mergesort runs in **O(n log n)** time in the worst, average, and best cases. The recurrence is T(n) = 2T(n/2) + O(n), which solves to Θ(n log n) by the master theorem.<|im_end|>
```

Most clients (Open WebUI, LibreChat, etc.) hide the `<think>` block by default and show only the final answer. If your client doesn't, set its "show reasoning" toggle off.

### Thinking is replayed across turns

Traces from earlier assistant turns **are** replayed back into the prompt: every
assistant message renders a `<think>…</think>` block, so the model can see how it
reached its previous answers. The condition is `$.IsThinkSet` alone — deliberately not
gated on `.Thinking` — so a turn that did no reasoning still renders an **empty**
`<think>\n\n</think>` block rather than none, which keeps a tool-call chain rendering
the same way on both paths. The turn in progress — including a
tool-call chain, where the model calls a tool and then continues after the result —
keeps its own either way. On llama.cpp this is upstream's default; on Ollama it
departs from Qwen's stock condition, which kept only the turn in progress.

**The client has to send the reasoning back.** The server returns it — Ollama's
`/api/chat` in the response's `thinking` field, llama.cpp in `reasoning_content` —
but only reasoning that arrives in the history's assistant messages is replayed, and
each endpoint reads one field:

| Endpoint | Field read from each assistant message |
|---|---|
| Ollama `/api/chat` | `thinking` |
| Ollama `/v1/chat/completions` | `reasoning` only — `reasoning_content` and `thinking` are dropped silently, and a message whose `content` is an array of parts keeps its reasoning only if it also has `tool_calls` |
| llama-server `/v1/chat/completions` | `reasoning_content` |

Which field each endpoint reads is decided by the server, not the model. **Measured
on this blob on 2026-09-18** (`scripts/live_check.sh`, Ollama 0.33.3, isolated store,
CPU only): the prior turn's reasoning was replayed on `/api/chat` at **232 prompt
tokens with it against 187 without**, and a live tool-call chain kept its own
reasoning (375 against 330). The same 232/187 figures were measured on the dense 27B
in 0.6.x — unsurprising, since both share the 248,320-token vocabulary and this
repo's Go template. The `/v1` behaviour (`reasoning` read at 215 vs 187,
`reasoning_content` ignored at 187, and llama-server rendering `reasoning_content`
while dropping `reasoning`) was checked on 2026-09-13 on that dense blob; it is
server-side and carries over.
That Ollama's `/v1` also drops `thinking`, and the array-content rule, come from
Ollama's v0.33.3 and v0.34.0 source, and still hold on the current release:
`openai/openai.go` and `server/prompt.go` are byte-identical from v0.33.3 through
v0.34.2 (source, 2026-09-17). Ollama never passes reasoning to the GGUF's
embedded Jinja template, so on Ollama only the Go template decides what is replayed.
On llama.cpp an earlier assistant turn that carries no reasoning renders with **no**
`<think>` block at all: Qwen 3.6's template gates the block on
`reasoning_content|length > 0`. The 3.8 template this repo used to ship reconstructed
an empty one instead, so prompts built by the two differ on that turn.

**The cost is context.** Every retained trace stays in the prompt — measured on the
dense 27B at 181 prompt tokens without and 464 with, on a 3-message conversation whose
first assistant turn carried a ~240-word trace, and not re-measured here. Prefill grows with every retained trace,
and on a CPU-only host prefill is the slow part. Releases 0.3.0 through 0.3.2
turned replay off for that reason; the CHANGELOG has the history.

**On llama.cpp, Qwen 3.6's own template decides.** Read from the template inside
the published blob (2026-09-18, from source — not re-tested live on this model):
`preserve_thinking` defaults to **true**, so an earlier turn's reasoning is replayed
by default; the assistant branch takes the trace from `message.reasoning_content`,
and failing that recovers one by splitting a `<think>` block out of `content`; and
there is no `preserve_reasoning` variable in it at all. That last point costs
nothing, because llama-server derives a `preserve_thinking` kwarg from
`preserve_reasoning` (`common/jinja/caps.cpp`), and from b10763 it passes
`preserve_reasoning=true` by default — so `--no-reasoning-preserve` and a request's
`preserve_reasoning: false` still reach this template through the derived copy,
while a request's own `preserve_thinking` is read directly.

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

**Nothing raises on conflicting settings.** The Qwen 3.8 template that this repo
patched between 0.4.0 and 0.6.5 raised when `preserve_thinking` and
`preserve_reasoning` disagreed, and llama-server returned that raise as HTTP 500 —
which is what the patch existed to prevent. Qwen 3.6's template has no such check:
it reads `preserve_thinking`, ignores anything else, and cannot fail that way.

**To turn replay off:**

- **llama-server** — start it with `--no-reasoning-preserve`, or send
  `"chat_template_kwargs": {"preserve_thinking": false}` on a request. A request's
  `preserve_thinking: true` switches it back on for that request.
  `{"preserve_reasoning": false}` works too, through the kwarg llama-server derives
  from it; the template itself never reads that name.
- **Ollama** — edit the template. In the assistant branch of both the `Modelfile`
  and `template` (so `make check`'s bridge sync stays green), change `{{ if $.IsThinkSet -}}` (the shipped condition) back to Qwen's stock
  `{{ if (and $.IsThinkSet (and .Thinking (or $last (gt $i $lastUserIdx)))) -}}`
  (keep the `-}}`; the `$lastUserIdx` loop at the top of the template is still there
  for it). Do not delete the block instead — see
  [Which template Ollama runs](#which-template-ollama-runs). `make check`'s Go-template
  guard will then fail, since it pins the replay condition.

### Disabling thinking

This is a reasoning-first model — it opens a `<think>` block by default. For a direct answer with no reasoning trace (simple or latency-sensitive calls), turn thinking off:

```bash
ollama run hf.co/FoolDev/Janus-35B-HERETIC:Q4_K_M --think=false
```

or send `"think": false` on `/api/chat`. With thinking off the model skips the reasoning trace and answers straight into `content`; with it on (the default) reasoning is emitted into the `thinking` field.

On llama.cpp the switch is the embedded template's own: send
`"chat_template_kwargs": {"enable_thinking": false}`, which primes a closed, empty
`<think>` block — and, because the template gates its replay branch on
`enable_thinking` too, drops every earlier turn's trace for that request. That
variable is upstream Qwen 3.6's, not this repo's.

### Reasoning effort

**This works on Ollama, and not on llama.cpp.** The instruction comes from this
repo's Go `template`, which Ollama runs (see
[Which template Ollama runs](#which-template-ollama-runs)). Qwen 3.6's own template —
the one inside the bundled GGUF, and so the one llama.cpp and LM Studio render — has
no `reasoning_effort` variable at all, so there the tier values are accepted by the
server and then quietly ignored (read from the template, 2026-09-18). `none` is the
one exception: llama-server maps it to `enable_thinking: false` and drops the kwarg
before the template runs (`tools/server/server-common.cpp`, checked 2026-09-18), so
`reasoning_effort: "none"` does switch thinking off on llama.cpp. Between 0.2.0 and
0.6.5 this repo shipped a patched Qwen 3.8 template that did implement the tiers on
the llama.cpp path; that file is gone with the rebase back to the MoE.

Ollama folds the eight values its `/v1` layer accepts into four think levels before
any template sees them, so the Go template maps levels, not values:

| `reasoning_effort` (Ollama `/v1`) | Think level Ollama emits | Effect |
|---|---|---|
| `high` | `high` | the model is told to think carefully and check its assumptions |
| `xhigh`, `ultra`, `max` | `max` | the same instruction — the template's `high`/`max` arm |
| `medium`, unset, `null` | `medium` | the default; no effort instruction is added |
| `low`, `minimal` | `low` | the model is told to keep its thinking brief |
| `none` | — | thinking **off** for that request, the same as `"think": false` |

> **There is no `xhigh` think level.** Ollama's levels are `low` / `medium` / `high` /
> `max` — `thinkFromReasoningEffort` clamps `xhigh` and `ultra` to `max`, and
> `api.ThinkValue.IsValid()` accepts only those four. "xhigh" is this repo's name for the
> *instruction text* the `high`/`max` arm inserts, not a value `$.ThinkLevel` ever holds.
> If you hand-edit the template (below), `eq $.ThinkLevel "xhigh"` is a condition that can
> never fire.


`"think": "high"`, `"low"` and `"max"` on `/api/chat` map the same way. Mixed case
such as `"HIGH"` is rejected by Ollama itself with HTTP 400 before any template runs.
The value-to-level mapping comes from Ollama's source, unchanged from v0.33.3 through
v0.34.2 (2026-09-17).

**Verified on this blob with `scripts/live_check.sh` (2026-09-18, Ollama 0.33.3,
CPU only):** all eight values returned HTTP 200 and `none` switched thinking off. On
a one-line chat the tiers reach the prompt exactly as the table says — unset and
`medium` added no instruction (159 prompt tokens), `high` and `max` each added the
xhigh instruction (197, so +38), and `low` added the low instruction (185, +26). The
same deltas were measured on the dense 27B in 0.6.x, which is expected: the Go
template and Ollama's folding are model-independent.

### Which template Ollama runs

Two templates exist for the same ChatML model: the Go `template` this repo ships
(served by HF's Ollama bridge) / `Modelfile` TEMPLATE, and **Qwen 3.6's own template
inside the GGUF**, which llmfan46 stamped and this repo leaves untouched. They do not
render identical prompts — the Go template pins JSON tool calls and adds a
reasoning-effort line from Ollama's think level, while the embedded template teaches
the XML `<function=…>` form and has no effort variable at all.

Ollama picks one at load time: it prefers the embedded template when that advertises
more capabilities — tools, thinking — and keeps the Go template when they tie. The rule has one more clause worth knowing: a Go template that renders a tool round trip is kept even when the embedded template advertises more, unless the embedded one renders a round trip too (`shouldPreferChatTemplate`, `server/images.go`). Both
advertise tools and thinking, so they tie and **Ollama runs the Go template**;
llama.cpp and LM Studio run the embedded one. **Verified live against this blob on
2026-09-18** (`scripts/live_check.sh`, Ollama 0.33.3): with Qwen 3.6's own template
embedded in the GGUF, Ollama still selected the Go template with thinking detected —
so the tie holds for the MoE, not just for the dense 27B it was first checked on. The
selection code is unchanged through v0.34.2 (source, 2026-09-17). Ollama's built-in renderers — it ships a `qwen35` one —
displace both templates only when the model's own config names a renderer or parser,
which this repo's does not. Ollama logs the choice:

```text
msg="template selection" ... selected=go_template go_template="[completion tools thinking]"
```

**Upstream watch — [ollama/ollama#17965](https://github.com/ollama/ollama/pull/17965).**
By its own description, that PR ("server: auto-detect ornith and qwen35 renderer and
parser") would stamp a `qwen3.5` renderer *and* parser into the config of every
`qwen35` / `qwen35moe` model at create time — this one included. That is precisely the
condition the paragraph above rests on *not* holding, so the consequence follows from
the rule stated there rather than from any test: were it to land, the built-in renderer
would displace both templates, and the JSON tool-call shape and `reasoning_effort` line
documented in this section would stop being what actually runs.
**Checked 2026-09-18** with `gh pr view 17965 -R ollama/ollama`: open since 2026-08-24,
no approving review, a collaborator disputing the approach in the thread, and the
branch conflicting with main — not merged, so nothing here changes yet. If it does
merge, re-check the server's `template selection` log line (and
`ollama show janus --modelfile`) for a named renderer or parser before trusting this
section's claims.

The Go template's "thinking" entry comes from its single `.Thinking` reference —
the block that renders each assistant turn's reasoning. Removing it drops that
capability, and Ollama switches to the embedded template: tool calls change from
JSON-in-XML to Qwen's XML form, which Ollama's extractor does not parse into a
`tool_calls` array, `reasoning_effort` stops doing anything (the embedded template
has no such variable), and a single tool call can come back twice (seen once on the
dense 27B under the *embedded* template; never on the Go-template path, which
returned exactly one call on this blob on 2026-09-18 — cause inferred, not
confirmed; see [Known limitations](#known-limitations)).
Setting `OLLAMA_GO_TEMPLATE=1` or `=0` on the Ollama server forces one template or
the other for every model.

**Both of those capabilities are read out of the template's parse tree, not out of anything
it renders**, so a render diff cannot see either one break. Ollama takes the tool-call tag
from the first `{{ if }}` whose condition names `.ToolCalls` — anywhere in the file — and
then from the first literal text inside that block (`tools/template.go`, v0.33.3). An action
at the head of the `range .ToolCalls` body leaves no text and the tag falls back to `{`,
which stops tool calling outright; that was 0.9.5. A condition naming `.ToolCalls` *earlier*
in the template captures the same search with the same result, which is why the assistant
branch aliases it once as `{{ $calls := .ToolCalls }}` and branches on the variable. The
thinking tags come from the first and last nodes of the list holding `{{ .Thinking }}`
(`thinking/template.go`), and both must be literal text: end that block with an `{{ if }}`
and the closing tag comes back empty, the thinking capability disappears, and Ollama answers
`does not support thinking` with HTTP 400. Since 0.9.7, `scripts/check_go_template.py` emulates
both functions and asserts the values they derive, so either regression fails `make check`
offline instead of waiting for a live tool call to expose it.

### Tool / function calling

The model emits whichever format the prompt specifies, and the two paths specify
different ones: the Ollama path pins JSON-in-XML, while the llama.cpp path gets
Qwen's native XML form from the template embedded in the GGUF.

**Ollama path** (this repo's `Modelfile`). The TEMPLATE advertises tools inside `<tools>…</tools>` and asks the model to reply in JSON-in-XML — the form Ollama's tool-call extractor parses into a structured `tool_calls` array on `/api/chat` and `/v1/chat/completions`. The tool definitions go in with `{{ json .Function }}`: on Ollama 0.14 and later a bare `{{ .Function }}` prints Go struct syntax instead of JSON ([ollama/ollama#14601](https://github.com/ollama/ollama/issues/14601); fix proposed in [ollama/ollama#18391](https://github.com/ollama/ollama/pull/18391)). The model replies like this:

```text
<tool_call>
{"name": "get_weather", "arguments": {"city": "Tokyo"}}
</tool_call>
```

**Embedded-template path** (llama.cpp, llama-cpp-python, LM Studio, KoboldCpp). The bundled GGUF carries Qwen 3.6's own template, so `--jinja` alone is enough — there is no file to pass and nothing to stamp. It teaches the XML form:

```text
<tool_call>
<function=get_weather>
<parameter=city>
Tokyo
</parameter>
</function>
</tool_call>
```

**Keep XML on llama-server.** llama-server recognises this template as Qwen3-Coder-style and parses the model's reply with a parser — and, once the model opens `<tool_call>`, a grammar — that accept only `<function=…><parameter=…>`. Qwen 3.6's tool-instruction literal is byte-identical to Qwen 3.8's (compared 2026-09-18), so the detection and the wire format are exactly what this card documented before the reversal. What is gone is the `tool_call_format` knob: the JSON opt-in described in releases 0.3.0 through 0.6.5 lived in the patched 3.8 template this repo no longer ships.

**Replayed tool calls: normalise `arguments` first.** Every OpenAI-compatible client hands assistant tool calls back with `function.arguments` as a JSON **string**, while the XML parameter form needs the individual key/value pairs — a chat template has `tojson` but no inverse. Qwen 3.6's template renders `<parameter=…>` only when `arguments` is a mapping; handed a string it emits that string as-is inside `<function=…>`, carrying upstream's own comment that you should "normalize arguments to a dict in your serving layer before applying this template". It does **not** raise, so a loader that passes the string straight through produces a silently malformed prompt rather than an error — the failure is quieter here than it was under the 3.8 template, which raised and returned HTTP 500.

In practice the loaders convert before rendering: llama-server decodes the string into a mapping, KoboldCpp (`--jinja --jinja_tools`) runs `json.loads` first, and the LM Studio app parses the arguments before its own JavaScript Jinja engine renders. All three were checked on 2026-09-14 against the 3.8 template this repo shipped then; the conversion is loader-side, so it applies unchanged here (from source for this template — not re-tested on this blob).

#### Example (Ollama, OpenAI-compatible API)

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ignored")

resp = client.chat.completions.create(
    model="janus",
    messages=[
        {"role": "user", "content": "Call get_weather for Tokyo. Respond ONLY with the tool call."}
    ],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }],
    temperature=0.3,
)
print(resp.choices[0].message.tool_calls)
# [ToolCall(id='call_xxx', type='function',
#           function=Function(name='get_weather', arguments='{"city":"Tokyo"}'))]
```

#### Tips

- Use direct prompts ("Call X for Y") rather than soft hints ("Use the tool"). The model thinks before committing to a call, and weak prompts can exhaust `num_predict` inside the `<think>` block before the call is emitted.
- Allow at least `num_predict: 1024` (or `max_tokens: 1024`) for tool-calling turns, more if the schemas are large.
- The JSON-in-XML format is what Ollama's tool-call extractor understands, and the Go template pins it; the GGUF's embedded template renders the XML `<function=…>` form. So the prompt format does change when you swap loaders, while client code should not have to, as long as the server returns a parsed `tool_calls` array.

## Known limitations

- **On the embedded-template path, a single tool call can come back twice.** Seen on the dense 27B blob, not re-tested here: in one test Ollama 0.33.3, running the embedded template, returned a first-turn tool call twice. A separate raw generation showed the model drafting the call inside `<think>` before emitting it once after `</think>`, so the parser most likely matched such a draft (inferred, not confirmed). It did not reproduce on standalone llama.cpp master (`a2878d3`, CPU): across both models, 12 first-turn calls (three prompts, with and without `parallel_tool_calls`) and two streamed runs each came back exactly once. Nor on b10760, the llama.cpp build Ollama 0.33.3 bundles and the one the duplicate came through: six more first-turn calls and a streamed run on this model each came back once. LM Studio's CPU engine (llama.cpp b10519) passed the same checks; the LM Studio app's own API layer is untested. Ollama's default path — the Go template, see [Which template Ollama runs](#which-template-ollama-runs) — returned exactly one call, **re-confirmed on this MoE blob on 2026-09-18** (`scripts/live_check.sh`, first-turn call at `reasoning_effort: high`, one `tool_calls` entry). Whether the prompt or the parser makes the difference on the embedded path was not isolated. If your client executes tools wherever the embedded template renders (llama.cpp, LM Studio, or Ollama with `OLLAMA_GO_TEMPLATE=0`), drop identical consecutive calls.
- **No mmproj in this release.** The base Qwen 3.6 35B-A3B supports image and video input via a separate `mmproj` file, which is not included here. Text-only inference works out of the box; multimodal inference requires fetching `Qwen3.6-35B-A3B-uncensored-heretic-mmproj-BF16.gguf` (or equivalent) from upstream — run `./scripts/fetch_vision.sh` and see [Vision](#vision) for the full path.
- **Quantization-induced quality loss.** Q4_K_M is a strong general-purpose quant but does measurably degrade math and code accuracy compared to BF16. If you need maximum quality, run the upstream safetensors on a host with room for the full BF16 weights.
- **No MTP head on the GGUF path.** The base declares a multi-token-prediction layer (`mtp_num_hidden_layers: 1`), but the Q4_K_M published in llmfan46's GGUF repo — the file this repo bundles — carries no NextN block at all (see [Architecture](#architecture)). No speculative decoding here: use the upstream safetensors under vLLM / SGLang, or llmfan46's separate `…-Native-MTP-Preserved-GGUF` variant, if you need it.
- **Sparse compute, dense memory.** Only ~3B of ~34.7B parameters are touched per token, but every expert has to be resident: the 19.77 GiB of weights is a floor whatever the routing does, and MoE sparsity buys compute, not RAM. What it does buy on the memory side is a small KV cache — 0.625 GiB per 32K at f16 measured, under a third of a comparable dense stack — so long contexts are unusually cheap here relative to the weights.
- **Thinking traces can loop.** Like most reasoning-distilled models, Janus-35B occasionally gets stuck repeating itself inside `<think>` tags. Mitigations: lower temperature to 0.4-0.6, raise `repeat_penalty` to 1.08, or set a `<think>`-token budget cap if your loader supports it.
- **Large tool-call arguments can be dropped.** Ollama's JSON-in-XML tool format makes the model JSON-escape the entire arguments object inline; for a big/complex payload (e.g. a file's `content` in a `write_file` call) the model can fail to escape it, so the field arrives `undefined` and the call fails. Qwen's native `<function=…><parameter=…>` format (raw values, no escaping) was tested as a fix but parses unreliably through Ollama, so the template deliberately keeps JSON-in-XML. Mitigation: write large files in smaller pieces per call.
- **Uncensored base — not aligned with any specific safety policy.** This is a personal repackage of an open-weight base whose refusal behavior has been abliterated away (the llmfan46 Heretic base). There is no RLHF refusal layer; the model will attempt most requests, so downstream safety is entirely the operator's responsibility.
- **No formal evaluation in this card.** The hardware table and the ~25 tok/s figure are measured on this blob (2026-09-18), but no task benchmarks (MMLU, HumanEval, …) are claimed, and prompt-processing throughput is not measured. If you produce real numbers and want them included, file a PR.

## Related models

| Model | Size | Notes |
|---|---|---|
| [llmfan46/Qwen3.6-35B-A3B-uncensored-heretic](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic) | 35B-A3B MoE | **Immediate base.** Uncensored Heretic abliteration of Qwen 3.6 35B-A3B; `transformers`-native safetensors, and the only place the MTP layer survives. |
| [llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF) | 35B-A3B MoE | Heretic GGUFs — BF16, Q3_K_L, Q3_K_M, Q4_K_M, Q4_K_S, Q5_K_M, Q5_K_S, Q6_K, Q8_0, plus the BF16 mmproj. MTP-clean, so they load as-is; the bundled Q4_K_M **is** this repo's Q4_K_M, byte-for-byte. |
| [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 35B-A3B MoE | Upstream pre-Heretic base model. `transformers`-native multimodal weights. |
| [FoolDev/Thanatos-27B-HERETIC](https://huggingface.co/FoolDev/Thanatos-27B-HERETIC) | 27B dense | Sibling repo, and now a genuinely different model: a **dense Qwen 3.8 27B**, abliterated from the ARA-based [`heretic-org/Qwen3.8-27B-heretic-ara`](https://huggingface.co/heretic-org/Qwen3.8-27B-heretic-ara). Same teacher (Fable 5), same tooling, newer Qwen generation, no experts. Pick Thanatos for a smaller resident footprint and a dense compute profile; pick Janus for 35B-class capacity at ~3B active. (The older `FoolDev/Thanatos-27B` and `Thanatos-27B-Heretic` slugs now 307 to this path.) |
| [Crownelius/Crow-9B-HERETIC-4.6](https://huggingface.co/Crownelius/Crow-9B-HERETIC-4.6) | 9B dense | Heretic-flavored fine-tune on a smaller 9B Qwen base. Useful as a fast first-pass model when 35B is too heavy for the host. |

> **Janus vs Thanatos.** Since 0.9.0 the two are genuinely different models, not two abliterations of one base. **Janus** is Qwen 3.6 **35B-A3B**: a mixture of experts, ~34.7B parameters total with ~3B active per token, 40 layers, 256 experts (8 routed + 1 shared), on llmfan46's Heretic base, and its bundled quant is MTP-clean so no strip is needed. **Thanatos** is a dense Qwen 3.8 **27B** — every parameter on every token, 64 layers — on heretic-org's ARA base, and its bundle *is* MTP-stripped, because that base ships the NextN block. They still share the 262,144 native window, the ChatML frame, the Claude Fable 5 teacher slot and this repo's tooling. Choose on shape, not only on abliteration: Janus for 35B-class capacity at ~3B active and a KV cache under a third the size (0.625 vs 2 GiB per 32K at f16), Thanatos for the smaller resident footprint (15.4 vs 19.78 GiB of weights) and a newer Qwen generation.

## Credits

- Immediate base: [llmfan46/Qwen3.6-35B-A3B-uncensored-heretic](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic) — Heretic-style abliteration of Qwen 3.6 35B-A3B
- Upstream base: [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) (Alibaba)
- Reasoning teacher: Claude Fable 5 (Anthropic)
- Distillation lineage and dataset curation: [Crownelius](https://huggingface.co/Crownelius)

License inherited from upstream: Apache-2.0.
