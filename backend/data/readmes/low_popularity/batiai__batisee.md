---
language:
  - ko
  - en
  - zh
license: mit
tags:
  - gguf
  - ocr
  - document-understanding
  - korean
  - multimodal
  - vision
  - deepseek-ocr
  - batiai
  - quantized
base_model: baidu/Unlimited-OCR
pipeline_tag: image-text-to-text
library_name: llama.cpp
---

# batisee — On-device Korean Document OCR by BatiAI

<p align="center">
  <a href="https://flow.bati.ai"><img src="https://img.shields.io/badge/BatiFlow-on--device%20AI-blue?style=for-the-badge&logo=apple"></a>
  <a href="#how-to-run-llamacpp"><img src="https://img.shields.io/badge/run-llama.cpp%20mtmd-orange?style=for-the-badge"></a>
  <img src="https://img.shields.io/badge/Ollama-coming%20soon-lightgrey?style=for-the-badge">
</p>

> ℹ️ **Ollama**: `batisee` uses the brand-new **DeepSeek-OCR (`deepseek2ocr`)** architecture, which the bundled Ollama engine does not load yet. Run it today with **llama.cpp** (below); Ollama support will follow once the engine merges this architecture.

> **batisee** is BatiAI's on-device document-OCR model — part of the BatiAI perception family
> (**batisay** = speech-to-text, **batispeak** = diarization, **batisee** = document/OCR).
>
> Built on [`baidu/Unlimited-OCR`](https://huggingface.co/baidu/Unlimited-OCR) (DeepSeek-OCR architecture, MIT),
> **converted to GGUF directly from the original weights by BatiAI** (not a re-host of community quants),
> BatiAI-signed, and **verified for Korean** so you can run it on a Mac with confidence.

**batisee** 는 BatiAI 인지(perception) 제품군의 문서 OCR 모델입니다 (**batisay**=음성인식, **batispeak**=화자분리, **batisee**=문서/OCR).
[`baidu/Unlimited-OCR`](https://huggingface.co/baidu/Unlimited-OCR)(DeepSeek-OCR 아키텍처, MIT)를 베이스로, **원본 가중치에서 BatiAI가 직접 GGUF 변환**(타사 양자화물 재배포 아님)하고, BatiAI 서명 + **한국어 검증**을 거쳐 Mac에서 바로 쓰도록 패키징했습니다.

## Why batisee?

- **On-device** — runs locally on a Mac (no cloud, no upload). Q4_K_M is **1.9 GB**.
- **Korean-verified** — measured on rendered Korean documents (see results below): clean text **CER 0%**, hard document (small font + table + blur) **100% key-content recall** with table structure preserved.
- **Document-native** — outputs layout boxes (`<|det|>`) and converts tables to HTML `<table>`.
- **Our own conversion** — GGUF built directly from `baidu/Unlimited-OCR` original safetensors, BatiAI-signed (`general.author = BatiAI`).
- **MIT** — fully commercial-friendly.

## 🆕 batisee **v2** (recommended for printed / dense documents) — fixes dense-document looping

> **Which to use:** **v2** for printed / dense / structured documents (receipts, multi-column, forms — fixes v1's looping).
> **v1** (repo root) for **free handwriting** — v2 currently regresses there (see point 3 below). A corrected handwriting fine-tune is in progress.

**v2** is a **BatiAI fine-tune** of batisee (LoRA on the text decoder), trained on rendered Korean
documents **+ real AI-Hub Korean handwriting**. It targets a failure mode we found while stress-testing v1:
on **dense receipts and multi-column pages**, the v1 Q4 GGUF can fall into a degenerate repeat loop
(tens of thousands of `<|det|>image` tokens) that a stronger repeat-penalty alone does **not** fix.
v2 cures this.

**What improved — measured on the shipped GGUFs:**

1. **Dense-document robustness (Q4 GGUF — the headline).** Held-out dense Korean receipts + multi-column
   pages, **same recipe for both** (`--repeat-penalty 1.1 --repeat-last-n 512`):

   | metric | v1 Q4 | v2 Q4 |
   |---|---|---|
   | parse CER | **17–27** (degenerate) | **0.20** |
   | degenerate loops | **4 / 24** | **0 / 24** |
   | worst output length | **50,872 chars** | 134 chars |

   On the same receipt, v1 emits a 50 k-character `<|det|>image` loop; v2 returns a clean ~130-char parse.

2. **Parse quality** (transformers, apples-to-apples, both `repeat_penalty 1.05`): overall parse
   **CER 0.349 → 0.245** (~30 % relative), **every category down** — receipt 0.148→0.065,
   multi-column 0.637→0.242, form 0.231→0.136, invoice 0.310→0.242, official 0.065→0.018, report 0.047→0.030.

3. **⚠️ Handwriting — loop-safe, but a recognition regression vs v1 (be aware).** v2 no longer *loops* on
   handwriting (0 degenerate / 80 pages), **but it recognizes real Korean handwriting *worse* than v1.**
   On held-out real AI-Hub handwriting, order-agnostic word recall is **≈ 7 % for v2 vs ≈ 30 % for v1** — the
   fine-tune over-anchored on printed-document patterns and tends to hallucinate document vocabulary on
   free handwriting. **For handwriting, prefer v1 (repo root).** A corrected handwriting fine-tune is in progress.

**v2 files** — in the `v2/` folder; the v1 files stay at the repo root, unchanged:

| File | Size | Use |
|---|---:|---|
| `v2/batisee-text-Q4_K_M.gguf` | 1.9 GB | **recommended** |
| `v2/batisee-text-Q8_0.gguf` | 3.0 GB | highest quality |
| `v2/mmproj-batisee-BF16.gguf` | 826 MB | vision encoder (identical to v1 — text-only fine-tune) |

**⭐ v2 recipe — the penalty must be stronger than v1's:**

```bash
hf download batiai/batisee --include "v2/*" --local-dir ./batisee

llama-mtmd-cli -m ./batisee/v2/batisee-text-Q4_K_M.gguf --mmproj ./batisee/v2/mmproj-batisee-BF16.gguf \
    --image your-document.png -p "document parsing." \
    --jinja --temp 0 --repeat-penalty 1.1 --repeat-last-n 512 -ngl 99
```

llama.cpp's repeat-penalty uses a **sliding window** (default last-64 tokens), which is weaker than the
whole-sequence penalty in transformers; on dense pages v1's `1.05` is not enough. **`1.1` + `--repeat-last-n 512`**
removes the loops without hurting tables or legitimate repeated cells (validated: 0 loops on 80 handwriting +
36 dense synthetic pages; tables/receipts unaffected). Use this recipe for v2.

**Honest limitations (read before you rely on it):**
- **Accuracy gains are measured on rendered/synthetic Korean documents** (same generator family used for
  fine-tuning — in-domain). Real-world generalization beyond that is **not** proven by these numbers.
- **Free handwriting is a regression vs v1** (word-recall ≈ 7 % vs ≈ 30 %) — see point 3 above. Use v1 for handwriting.
- Real-world **camera photos and heavy skew remain the frontier** (shared with v1; quantified separately).
- Tables are scored by **structure (TEDS)**, not CER — cell text can still slip on hard scans.
- **There is no separate "field-extraction" mode.** An `"extract fields."` prompt returns the same full-page
  parse as `"document parsing."`, *not* structured JSON — parse the full-page output yourself for key/values.

**v2** 는 batisee 의 **BatiAI 파인튜닝**(텍스트 디코더 LoRA)입니다. 렌더 한국어 문서 **+ 실제 AI-Hub 한국어 손글씨**로 학습했고,
v1 의 약점(밀집 영수증·다단 페이지에서 Q4 GGUF 가 `<|det|>image` 수만 토큰 반복 루프에 빠지는 현상 — 강한 penalty 로도 안 고쳐짐)을
**파인튜닝으로 해결**했습니다. 밀집 문서 CER 17–27(퇴화)→**0.20**, 루프 4/24→**0/24**, 파스 CER 0.349→0.245(약 30%↓, 전 카테고리 개선),
**반드시 v2 레시피(`--repeat-penalty 1.1 --repeat-last-n 512`)** 사용. ⚠️ **손글씨는 v1보다 퇴행**(루프는 0/80이나 실제 인식은 v2 단어 recall ≈7% < v1 ≈30% — 파인튜닝이 인쇄문서에 과적합) → **손글씨는 v1(루트) 권장**, 교정 재학습 진행 중. 정확도 수치는 **합성 in-domain 기준**(실 일반화 미증명). 표는 구조(TEDS) 기준, **별도 필드추출(JSON) 기능 없음**(`extract fields.` = `document parsing.` 과 동일 출력).

## ⭐ Korean OCR results / 한국어 OCR 검증

Rendered Korean documents (ground-truth known) → OCR → compared. Method & images: [`ocr-poc/gate-results`](https://github.com/batiai/batiai-models/tree/main/ocr-poc/gate-results).

| Test / 테스트 | Difficulty / 난이도 | Hangul kept / 한글보존 | Key recall / 핵심recall | Table / 표 | CER |
|---|---|---|---|---|---|
| Gate 1 (clean) | clean text | **100%** | — | — | **0.0%** |
| Gate 2 (hard) | small font + table + blur | **100%** | **100%** | ✅ `<table>` | — |

Both **Q8_0** and **Q4_K_M** pass with no degradation and no decoding loops.
Q8/Q4 모두 품질 저하·디코딩 루프 없이 통과.

## Available files

| File | Size | Use |
|------|-----:|-----|
| `batisee-text-Q8_0.gguf` | 3.0 GB | highest quality / 최고품질 |
| `batisee-text-Q4_K_M.gguf` | 1.9 GB | **16 GB Mac sweet spot (recommended)** |
| `mmproj-batisee-BF16.gguf` | 826 MB | vision encoder (required) / 비전 인코더(필수) |

## How to run (llama.cpp)

> ⚠️ This is a **multimodal** model — you always need **both** the text GGUF **and** `mmproj-batisee-BF16.gguf`.
>
> 🍎 **On a Mac**: `brew install llama.cpp` (version **≥ 9430**) provides `llama-mtmd-cli` and loads `batisee` directly — **verified on M4 Max, no source build needed**.

```bash
hf download batiai/batisee --include "batisee-text-Q4_K_M.gguf" --include "mmproj-batisee-BF16.gguf" --local-dir ./batisee

llama-mtmd-cli \
    -m ./batisee/batisee-text-Q4_K_M.gguf \
    --mmproj ./batisee/mmproj-batisee-BF16.gguf \
    --image your-document.png \
    -p "document parsing." \
    --jinja --temp 0 --repeat-penalty 1.05 -ngl 99
```

### ⭐ Recipe matters (learned the hard way)

| Flag | Why |
|------|-----|
| `-p "document parsing."` | The prompt **must** be this. `"Free OCR."` triggers a buggy reasoning mode that emits meta-commentary instead of the text. |
| `--jinja` | Without it the chat-template step crashes. |
| `--temp 0 --repeat-penalty 1.05` | Without the penalty the decoder can fall into an infinite repeat loop. |

## Model details

- **Base**: [`baidu/Unlimited-OCR`](https://huggingface.co/baidu/Unlimited-OCR) — **DeepSeek-OCR architecture**
  - Text: DeepSeek-3B-MoE (12 layers, 64 routed experts top-6, standard MHA, 32K context) → `deepseek2ocr`
  - Vision: DeepEncoder (CLIP-L-14 + SAM-ViT-B, 1024px) + linear projector
- **Conversion**: built directly from original safetensors with `llama.cpp` (DeepSeek-OCR support). Image normalization `mean = std = [0.5, 0.5, 0.5]`.
- **License**: MIT (inherited)

## BatiAI signing

All GGUFs carry:
- `general.author = BatiAI`
- `general.url = https://flow.bati.ai`

## Attribution & License

This model is a GGUF distribution of `baidu/Unlimited-OCR` (**MIT**), which is built on the DeepSeek-OCR architecture. Original authors' work and license are retained; BatiAI's contribution is the from-original GGUF conversion, signing, Korean verification, and on-device packaging.

본 모델은 `baidu/Unlimited-OCR`(MIT)의 GGUF 배포본입니다. 원저작자 작업·라이선스를 유지하며, BatiAI 기여는 원본에서의 직접 GGUF 변환·서명·한국어 검증·온디바이스 패키징입니다.

## Roadmap

- ✅ **v2 shipped** — fixes dense-document looping, ~30 % parse-CER reduction on printed docs. See the v2 section above.
- 🔧 **In progress — handwriting fine-tune (corrected):** v2 regressed free-handwriting recognition vs v1 (over-anchored on printed docs). Re-doing it with spatial-order labels + anti-forgetting recipe + a word-recall no-regression gate vs v1.
- Next: **real-world camera photos / heavy skew / low-quality scans** — still the frontier; v2's measured gains are on rendered/synthetic docs.
- Ollama support once the `deepseek2ocr` engine merges.
- ✅ **v2 출시** — 밀집문서 루프 해결 + 인쇄문서 파스 CER 약 30%↓. 🔧 **손글씨는 교정 재학습 진행 중**(v2가 v1 대비 손글씨 퇴행 → 공간정렬 라벨+anti-forgetting+무회귀 게이트). 실 카메라/왜곡은 다음 프론티어.

## About BatiFlow

[BatiFlow](https://flow.bati.ai) — free, unlimited, on-device AI for Mac.

<!-- BENCH-START -->
### On-device benchmark — MacBook Pro M4 Max (Q4_K_M)

Measured with `brew` `llama-mtmd-cli` 9430, on the same 4 stress documents as the desktop GPU.

| Metric | Value |
|--------|-------|
| Engine | Homebrew `llama.cpp` (`llama-mtmd-cli`) **9430** — loads `deepseek2ocr` fine, **no source build needed** |
| Page latency (full pipeline) | **~3.0 s/page** cold, ~3 s warm (≈ desktop GPU's 2.56 s/page) |
| Memory (max RSS) | **2.94 GB** (peak 2.97 GB) |
| Quality | digital docs/tables near-perfect (numbers 100%, occasional single KR-glyph slip); heavy degradation / skew = known limits → v2 roadmap |

> `tokens/sec` and standalone mmproj-encode time are **not emitted by the 9430 Homebrew bottle** (its perf block is suppressed); available via a source build if needed. Page latency + RSS are the user-facing numbers and confirm M4 Max ≈ desktop-GPU class.
<!-- BENCH-END -->
