---
license: apache-2.0
language:
- en
- hi
- bn
- ta
- te
- zh
- ja
- ko
- ar
- es
- fr
- de
pipeline_tag: text-generation
tags:
- rivinity
- decoder-only
- moe
- multilingual
- cpu-inference
---

# Rivinity

Rivinity is a **text-only, multilingual, CPU-first decoder-only language model**
project. This repository is in the **pre-training hardening phase**: the
architecture, tokenizer, training pipeline, web-grounding subsystem, and RAG
stack are implemented and test-verified — **the model has not been trained**.
Do not expect trained-model behavior from any artifact here.

## Architecture (locked V1)

| Property | Value |
|---|---|
| Layers / hidden | 8 / 768 |
| Attention (GQA) | 8 Q heads / 4 KV heads, head_dim 96, q/k RMSNorm |
| RoPE | theta 1,000,000 |
| FFN | 4-expert **Top-1** MoE, SwiGLU experts, intermediate 2432 |
| Embeddings | tied token embeddings / LM head |
| Context target | 32,768 (config target, not a trained-context claim) |
| Vocabulary | **48,006** (T48 base 48,000 + 6 control tokens, ids 48000–48005) |

Classes: `RivinityConfig` / `RivinityModel` / `RivinityForCausalLM` /
`RivinityMoEFFN` (package `rivinity`, `model_type: "rivinity"`). Text-only:
no vision, no audio, no talker. Construction-time validation rejects invalid
combinations (see `docs/RIVINITY_ARCHITECTURE.md`).

## Status (honest, measured only)

| Area | State | Evidence |
|---|---|---|
| Tokenizer (T48) | **Selected.** 48,006 vocab; decode round-trip repaired in Phase H4 (missing `Fuse` decoder); NFKC normalization semantics documented | `tests/multilingual/`, `reports/multilingual_report.json` |
| Multilingual contract | 28-language battery + report; *tokenizer efficiency, not understanding* | `rivinity/multilingual.py`, `tools/multilingual_report.py` |
| Training pipeline | Connected end-to-end (manifest → … → checkpoint → resume) on a synthetic 12-language fixture; **no real training run** | `tests/integration/test_pipeline_e2e.py` |
| Generation | Budget contract (`max_total/thinking/answer_tokens` + legacy aliases), greedy/sampling, KV cache, stream≡non-stream | `tests/unit/test_rivinity_generation_h6.py` |
| Web subsystem (`rivinity/web/`) | Crawler (stdlib HTTP + optional Crawl4AI), policy/SSRF, SQLite cache, sanitizer, router, search providers, safe tools | `tests/web/`, `tests/security/` |
| Grounding/RAG | Unified `Evidence` contract (local + web), capsules, `[E#]` citations, insufficiency states, system-turn separation | `tests/web/test_grounding.py`, `rivinity/grounding.py` |
| GGUF / llama.cpp | Conversion + metadata contract **PASS**; **runtime BLOCKED** (llama.cpp not installed here) — never claimed | `tools/gguf_runtime_check.py`, `reports/gguf_runtime_*.json` |
| Benchmarks | Framework/stub runs labeled `FRAMEWORK_ONLY`; no real model measurements exist | `benchmarks/`, `tests/integration/test_benchmark_integrity_h14.py` |
| Tests | ~336 CPU tests, 8-layer tree | `python -m unittest discover -s tests -t . -v` |

## Usage

```python
from rivinity import RivinityConfig, RivinityForCausalLM
model = RivinityForCausalLM(RivinityConfig())          # locked V1, vocab 48006
```

```python
# Web grounding (offline tests use fakes; real use needs network + policy)
from rivinity.orchestrator import WebGroundingOrchestrator
res = WebGroundingOrchestrator().answer("What is the capital of France?",
                                        urls=["https://example.org"])
res.citations, res.context.insufficient
```

Optional web extra (JS-heavy pages): `pip install rivinity[web]` then
`crawl4ai-setup`.

## Documentation

| Doc | Contents |
|---|---|
| `docs/RIVINITY_ARCHITECTURE.md` | locked V1 contract, validation rules, math notes |
| `docs/RIVINITY_MULTILINGUAL.md` | T48 status, NFKC/round-trip semantics, battery |
| `docs/RIVINITY_WEB_GROUNDING.md` | web subsystem, evidence capsules, threat model link |
| `docs/RIVINITY_DATA_PIPELINE.md` | manifest → checkpoint pipeline, fixture |
| `docs/RIVINITY_PRETRAINING_READINESS.md` | phase ledger, readiness evidence |
| `docs/RIVINITY_MIGRATION.md` | legacy relationship, quarantine map |
| `docs/RIVINITY_REPO_FORENSIC_AUDIT.md` (+ addendum) | H0 audit, findings, remediation |
| `docs/RIVINITY_WEB_THREAT_MODEL.md` | attacker model, controls, limitations |

## Limitations

- **Untrained weights.** All outputs are random-initialization quality.
- Multilingual *capability* is a design goal with tokenizer-level evidence —
  not a measured model capability.
- `<think>` support is formatting/budget handling; reasoning ability, if any,
  is a post-training measurement question.
- GGUF runtime compatibility is **BLOCKED**, not proven (see report).
- Per-process rate limiting; no auth/cookies by design; Crawl4AI runs a real
  browser when enabled (keep it patched).

## Provenance & licensing

- Apache-2.0. This project's repository history contained earlier prototype
  components from a separate upstream project; they are **quarantined under
  `legacy/`** (not deleted) with full attribution — see
  `docs/RIVINITY_MIGRATION.md` and `legacy/minimind_o/README.md`.
- Tokenizer pilots (`tokenizer_out/T48`, `PROBE100K`, `T32`) are research
  provenance; only `tokenizer_out/Rivinity-T48/` (48,006) is consumed.
- **Third-party attribution:** "This project uses Crawl4AI
  (https://github.com/unclecode/crawl4ai) for web data extraction."
  (Crawl4AI is Apache-2.0; used as an optional, lazily-imported backend — no
  source embedded.)
- Review corpus/dataset licenses in `training/data_manifest.py` manifests
  before any redistribution; no production corpus is included.


<!-- rivinity-h21-provenance:begin -->
## Provenance & public artifact status (H21-1, 2026-10-14)

**This repository is an untrained architecture and code prototype.** No trained
Rivinity checkpoint exists. Random-initialization forward passes, synthetic
fixtures, and smoke tests are engineering evidence only - they are not language
quality, multilingual capability, or reasoning claims.

**Lineage (truthful attribution).** The Rivinity core under `rivinity/` is a
clean-room implementation built during a hardening phase. Earlier prototype
work was based on the MiniMind-O (`minimind_o`) codebase; that historical
source is preserved under `legacy/` with its original attribution and is not
part of the active import or loading path. Root-level copies of prototype
modules and the unverified root weight file were removed from the public
loading path in H21-1; see `reports/rivinity_public_artifacts_manifest.json`.
That manifest records that **no trained Rivinity checkpoint exists** and lists
every quarantined artifact with its SHA-256.

**One authoritative tokenizer.** The root `tokenizer.json`,
`tokenizer_config.json`, and `special_tokens_map.json` are byte-identical
copies of the canonical export in `tokenizer_out/Rivinity-T48/` (vocabulary
48,006; control tokens 48,000-48,005). Never hand-edit root copies; regenerate
them by copying the three files from the export.

**Loading contract.** `config.json` carries `auto_map` custom-code entries, so
loading requires `trust_remote_code=True` with a pinned revision, and it
requires the `rivinity` package importable (clone the repo and `pip install .`,
or put the repo root on `sys.path`). The root `configuration_rivinity.py` and
`modeling_rivinity.py` files are thin loader shims: transformers' dynamic-code
loader requires repo-file-style `auto_map` references, and the authoritative
implementation stays in the `rivinity` package (no duplicated model code):

```python
from transformers import AutoConfig, AutoModelForCausalLM
REV = "8a0ab5c7710ddda1d9c1a8d58cf71f1935cd5f15"  # replace with the current main SHA
cfg = AutoConfig.from_pretrained("RANITBAG/on_the_way", revision=REV, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("RANITBAG/on_the_way", revision=REV, trust_remote_code=True)
```

**Supported matrix (tested).** Python >=3.10 (dev box 3.14), torch >=2.4
(tested 2.14 CPU), transformers >=5.0,<6 (the code uses the v5
`_tied_weights_keys` mapping format), tokenizers >=0.20,<1 (tested 0.23.2),
jinja2 >=3.1.
<!-- rivinity-h21-provenance:end -->


<!-- rivinity-h21-web-retrieval:begin -->
## Web retrieval is a tool capability, not model knowledge (H21-8, 2026-10-16)

Rivinity can answer "model doesn't know -> retrieve -> cite -> answer": scoped
local retrieval (user/tenant namespace) first, then -- only when evidence is
insufficient and a provider is configured -- external search through the
policy-guarded crawler, producing cited answers with provenance and
diagnostics. Web retrieval is a **tool/RAG capability**: it is not knowledge
in the model weights, and a fluent cited answer from an untrained model is
not evidence of model quality. Live web search is opt-in (no provider is
enabled by default); a self-hosted SearXNG adapter ships as the documented
provider configuration. All retrieved content is untrusted evidence, never
system instructions.
<!-- rivinity-h21-web-retrieval:end -->

<!-- rivinity-h21-12-gguf-truth:begin -->
## GGUF status: conditional alias, runtime UNPROVEN (H21-12, 2026-10-18)

The converter emits spec-shaped GGUF under a `qwen3moe` host contract with
tensor-by-tensor review documented in `docs/GGUF_COMPAT_DECISION_H21.md`.
That alias is **conditional, not proven**: actual llama.cpp load/generation
is BLOCKED until `tools/gguf_runtime_check.py` passes against a real
`llama-cli` binary (load >= b5092-era qwen3moe support plus the GQA+qk-norm
fix). No tokens/sec or quantized-quality claims are made from converter
round-trip alone. The supported inference path today is the Transformers
CPU backend.
<!-- rivinity-h21-12-gguf-truth:end -->
