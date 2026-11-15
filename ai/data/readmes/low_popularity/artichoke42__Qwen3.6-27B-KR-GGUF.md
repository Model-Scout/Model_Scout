---
license: apache-2.0
base_model: Qwen/Qwen3.6-27B
language:
- en
- ko
pipeline_tag: text-generation
tags:
- agentic
- tool-use
- bilingual
- korean
- gguf
- distillation
- rlvr
- grpo
---

# Qwen3.6-27B-KR-GGUF

A bilingual (English + Korean) agentic fine-tune of **Qwen3.6-27B**, distilled from **Qwen3.5-122B-A10B**, with dedicated **transliteration** and **calibration** training, and then **RLVR-tuned for language purity**. Built for agentic workloads — coding, tool-use / web-search, bilingual chat with reasoning, and paper summarization — and packaged as imatrix-quantized GGUF for single-GPU deployment (fits a 32 GB card such as an RTX 5090).

This is the **non-MTP repo**: the plain GGUF + the full-precision bf16 original. For **faster single-stream decoding** via the multi-token-prediction head, use the companion repo **[Qwen3.6-27B-KR-MTP-GGUF](https://huggingface.co/artichoke42/Qwen3.6-27B-KR-MTP-GGUF)** (recommended default for solo / small-team use).

> **Note on naming:** the `UD-Q5_K_XL` tag denotes a **stock llama.cpp recipe** — Q5_K_M base with Q6_K token-embedding/output tensors and an imatrix — **not** Unsloth's published dynamic `UD-Q5_K_XL`. The difference is under ~1%.

## Files — which one to download

The two variants are the **same model**, differing only by the MTP head (capability/benchmarks identical).

| File | Size | Use case |
|---|---|---|
| `Qwen3.6-27B-KR-UD-Q5_K_XL.gguf` | ~19.4 GB | **This repo.** Non-MTP — simpler; a fine choice for high-concurrency batched serving, where speculative decoding helps little. |
| [`Qwen3.6-27B-KR-MTP-UD-Q5_K_XL.gguf`](https://huggingface.co/artichoke42/Qwen3.6-27B-KR-MTP-GGUF) | ~19.7 GB | **Recommended default (companion repo).** Carries the MTP head for **faster single-stream decoding**. Best for solo / small-team agentic use. |

Also in this repo: the **bf16 full-precision original** (`*.safetensors`) — the model these GGUFs are quantized from, for re-quantization or further training.

## Model summary

- **Base:** [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) — 27B dense, hybrid linear-attention/Mamba architecture with a built-in MTP head, Apache 2.0.
- **Teacher:** [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) — generated the distillation corpus, Apache 2.0.
- **Languages:** English and Korean.
- **Quantization:** imatrix Q5_K_M + Q6_K embed/output.

## Benchmarks

Measured on the **quantized Q5 GGUF** (the deployment artifact), with deploy-faithful sampling (temp 1.0, **no repeat-penalty**):

- **Coding:** HumanEval **79.9%** (deploy-cap mt=4096; the model reasons verbosely, so budget matters).
- **Math (KO):** HRM8K (official HAERAE-HUB Korean GSM8K, n=300) **93.0%**.
- **Transliteration (EN↔KO proper nouns):** **79%** on a frozen 420-item held-out set — a dedicated training focus.
- **Calibration:** fabrication **20.8%** / appropriate-hedge **79.2%** — on genuinely-unknowable questions the model hedges ("미상") instead of confabulating.
- **Tool-use:** BFCL simple **94.0** / live-simple **84.1** / relevance **93.75**; full **opencode** agentic round-trip live-verified.
- **CJK purity:** Korean-answer CJK leak **~2%** (temp 1.0) — RLVR shifts the base model's residual Chinese/kana bleed out of Korean answers at the distribution level.

## Serving

The validated deployment path is **`llama-server` with `--jinja`**, which parses the Hermes tool-call format (including the model's `<think>` prefix) into OpenAI-format `tool_calls`. The hybrid linear-attention architecture makes KV cache very cheap (~44 KB/token at q8_0), so a **single 256k-token context fits on a 32 GB card**. Primary example (non-MTP variant):

```bash
llama-server -m Qwen3.6-27B-KR-UD-Q5_K_XL.gguf \
  -ngl 99 -c 262144 --parallel 1 -fa on --jinja \
  --cache-type-k q8_0 --cache-type-v q8_0 \
  --n-predict 4096 \
  --host 127.0.0.1 --port 8080
```

- **`-c 262144 --parallel 1` = the full 256k context in a single stream**. For concurrency, raise `--parallel`: `-c 262144 --parallel 4` gives **64k tokens/slot** across 4 slots.
- This is the **non-MTP** GGUF — for MTP speculative decoding (`--spec-type draft-mtp`, mean accepted length ~2.47) download the [MTP variant](https://huggingface.co/artichoke42/Qwen3.6-27B-KR-MTP-GGUF).
- `--cache-type-k/v q8_0` halves KV memory at no measurable quality cost (requires `-fa on`).
- **Do not set `--repeat-penalty`:** at temp 1.0 the model does **not** loop, and a repeat-penalty roughly **doubles fabrication** by suppressing Korean hedge phrases ("미상") — so leave it off. **`--n-predict 4096`** caps output length (also cap your agent's per-request `max_tokens` ≈ 4096). Avoid the DRY sampler — it corrupts verbatim strings (hashes / paths / IDs).

## Recommended system prompt — identity + Korean output

Use this exact system prompt. It is also **baked into the GGUF as the default system message**:

```
당신은 Qwen3.6-27B-KR입니다. 한국어 사용자를 돕는 이중언어 AI 어시스턴트입니다. 항상 한국어로 답하며, 자신을 소개할 때 通义千问이나 Qwen 같은 중국어 이름이 아니라 Qwen3.6-27B-KR로 소개합니다. 한국어로 사고하세요
```

It does two things:

- **Identity:** the model introduces itself as **Qwen3.6-27B-KR** — the Korean-specialized version of Qwen3.6 — instead of the base model's Chinese name **通义千问 / "Qwen"**. In live opencode testing this drove self-identification as 通义千问 from **42.9% → 0%**.
- **Korean output + reasoning:** it answers in Korean and moves `<think>` reasoning into Korean for Korean prompts, with no loss of correctness.

**This is embedded in the GGUF `chat_template` as the default**, so it applies automatically when the client sends no system message. But **a client-supplied system message overrides it**, and most agentic frameworks (e.g. opencode) send their own. **So for agentic use, include this anchor in your client's system prompt** (prepend it to your own instructions) — this is the fix that stops the model self-identifying as 通义千问. For English-only use you may omit it.
## Known characteristics

- **Verbose reasoning:** long `<think>` traces (inherited from the base) — a latency/length trait, not a capability gap. Give it a generous token budget.
- **Vision:** the base is multimodal, but these are text-only GGUFs (no vision encoder/mmproj).

## License & attribution

Released under **Apache 2.0**, matching the base and teacher.

- Base model: Qwen/Qwen3.6-27B (Apache 2.0)
- Teacher model: Qwen/Qwen3.5-122B-A10B (Apache 2.0)

The training corpus used **prompts, grounding text, and tests** from third-party datasets (never their answers — all answers are teacher-generated). The corpus itself is **not** distributed; only the model is. Sources, with thanks:

- **Coding:** BAAI/TACO (Apache 2.0), deepmind/code_contests (Apache 2.0), codeparrot/apps (MIT), google-research-datasets/mbpp (CC-BY-4.0)
- **Tool-use / grounding:** Wikipedia (CC-BY-SA-4.0), Wikidata (CC0 + CC-BY-SA), Python library documentation (BSD/MIT/Apache/PSF)
- **Chat prompts:** allenai/tulu-3-sft-mixture (ODC-BY) — prompts only
- **Paper summarization:** arXiv paper text (per-paper licenses; used as grounding, summarized transformatively — full text not reproduced)

Share-alike terms (e.g. Wikipedia CC-BY-SA) govern derivative works of the *text*; they do not attach copyleft obligations to transformatively-trained model weights. RLVR (language-purity) tuning used the same teacher/corpus lineage — no new external data.

## Acknowledgements

Built on Qwen3.6-27B and Qwen3.5-122B-A10B by the Qwen team (Alibaba). Quantization and MTP speculative decoding via [llama.cpp](https://github.com/ggerganov/llama.cpp).
