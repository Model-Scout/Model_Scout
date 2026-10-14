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
