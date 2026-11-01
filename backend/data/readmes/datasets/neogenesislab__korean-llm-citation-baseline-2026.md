---
language:
- ko
- en
license: cc-by-4.0
task_categories:
- text-generation
- text-classification
tags:
- generative-engine-optimization
- geo
- llmo
- llm-citation
- brand-mention
- benchmark
- evaluation
- multilingual
- bilingual
- korean
- english
- gemini
- gpt-4o
- claude
- neo-genesis
- wikidata-Q139569680
- yesol-heo-founder
- ko
- en
- citation-tracking
- korean-llm
- openai
- anthropic
size_categories:
- n<1K
pretty_name: Korean LLM Citation Baseline 2026 (Neo Genesis GEO Measurement)
configs:
- config_name: measurements
  data_files:
  - split: train
    path: data/measurements.parquet
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
---

## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018479.svg)](https://doi.org/10.5281/zenodo.20018479)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018479`** ([Zenodo record](https://zenodo.org/record/20018479)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018479,
  author       = {Heo, Yesol and Neo Genesis Lab},
  title        = {Korean LLM Citation Baseline 2026 (Neo Genesis GEO Measurement)},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018479},
  url          = {https://doi.org/10.5281/zenodo.20018479}
}
```

# Korean LLM Citation Baseline 2026 (Neo Genesis GEO Measurement)

> A real, empirical Generative-Engine-Optimization (GEO) / LLM-Optimization (LLMO) measurement dataset. **126 brand-mention observations** across **3 frontier LLMs** (`gemini-2.5-flash`, `gpt-4o`, `claude-sonnet-4-6`) for **30 bilingual brand-relevant prompts**, captured from 2026-04-28 to 2026-05-03.

Released by **[Neo Genesis](https://neogenesis.app)** to support GEO/LLMO research. This is one of the few public datasets where the measurement target is a real, publicly attested company (Wikidata [Q139569680](https://www.wikidata.org/wiki/Q139569680)) instead of a synthetic brand.

## Why this dataset exists

GEO/LLMO research is dominated by:
- **Synthetic-prompt benchmarks** (no real brand involved).
- **Single-LLM probes** (does ChatGPT mention us?).
- **Self-report surveys** (anecdotal, not reproducible).

What is missing publicly:
- **Cross-LLM, multi-category, real-brand citation rates** measured under a fixed prompt protocol.
- **Both successful and errored attempts** preserved together (so researchers can study API coverage / rate-limiting / refusals).
- **Bilingual (ko + en) prompts** for the same brand, since global LLMs differ a lot between Korean and English citation behavior.

This dataset fills that gap with one company's real production GEO probe.

## Dataset summary

- **126 measurement rows** in `data/measurements.jsonl`. Each row is one (provider, model, prompt) attempt.
- **30 seed prompts** across **6 intent categories** in `data/seed_prompts.json`:
  - `definition` (5 prompts) — "Who runs multiple SaaS with one autonomous AI?"
  - `comparison` (5) — "ToolPick vs G2 vs Capterra"
  - `problem_solving` (5) — "How do I run 10+ SaaS as a solo founder?"
  - `pricing` (3) — "ToolPick pricing vs G2 pricing"
  - `reputation` (3) — "Is Neo Genesis trustworthy?"
  - `product_specific` (9) — "WhyLab Gemini 2.5 Docker validation methodology"
- **3 LLMs** measured: `gemini-2.5-flash`, `gpt-4o`, `claude-sonnet-4-6`.
- **Mention counters** per row: `mention_neo_genesis`, `mention_domain_root` (neogenesis.app), `mention_domain_subs` (sbu domains), `mention_sbu_total` (named SBUs), `mention_founder`.
- **Errored attempts preserved** (`error` field) — including rate-limiting, credit-balance issues, and missing-key cases — so reproducibility studies are possible.

## Aggregate stats by provider

| Provider | Successful / Total | Any-mention rate | Neo Genesis mentions | SBU mentions | Founder mentions |
|---|---|---|---|---|---|
| `anthropic` | 0 / 2 | 0.0% | 0 | 0 | 0 |
| `gemini` | 62 / 62 | 48.4% | 46 | 150 | 21 |
| `openai` | 32 / 62 | 56.2% | 10 | 37 | 3 |

## Aggregate stats by category

| Category | Successful / Total | Any-mention rate |
|---|---|---|
| `comparison` | 15 / 20 | 93.3% |
| `definition` | 15 / 20 | 0.0% |
| `pricing` | 9 / 12 | 44.4% |
| `problem_solving` | 15 / 20 | 0.0% |
| `product_specific` | 31 / 42 | 67.7% |
| `reputation` | 9 / 12 | 100.0% |

## Schema

### `data/measurements.jsonl` (one record per line)

```json
{
  "timestamp": "2026-04-28T04:08:02.126309+00:00",
  "provider": "gemini",
  "model": "gemini-2.5-flash",
  "prompt_id": "spec-09",
  "prompt_category": "product_specific",
  "prompt_text": "Yesol Heo Neo Genesis founder background",
  "response_text": "<...full LLM response, may include hallucinations...>",
  "response_tokens": 542,
  "mention_neo_genesis": 4,
  "mention_domain_root": 0,
  "mention_domain_subs": 0,
  "mention_sbu_total": 0,
  "mention_founder": 2,
  "sentiment": "neutral",
  "citation_urls": [],
  "error": null
}
```

### `data/seed_prompts.json`

The 30 seed prompts grouped by intent category. Bilingual (ko + en).

### `data/aggregate_by_provider.json` and `data/aggregate_by_category.json`

Pre-computed aggregations (counts, mention sums, mention rates).

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/korean-llm-citation-baseline-2026", "measurements", split="train")
print(ds[0]["prompt_text"])
print(ds[0]["mention_neo_genesis"])

# Filter to one provider
gemini_only = ds.filter(lambda r: r["provider"] == "gemini")
print(f"Gemini rows: {len(gemini_only)}")
```

## Suggested research applications

1. **GEO rate baselines** — establish how often a publicly-attested company is cited by frontier LLMs across English vs Korean prompts.
2. **Hallucination grounding** — the `response_text` field contains real LLM responses including factually incorrect claims about the founder. Useful for studying what frontier LLMs invent when probed about a real-but-niche entity.
3. **Cross-LLM consistency** — same prompt, three different LLMs. Measure agreement on whether to mention the brand and how.
4. **Bilingual asymmetry** — pairs of (English, Korean) prompts about the same entity, useful for studying multilingual citation gaps.
5. **Coverage / availability** — `error` rows preserve API-side failures (rate limit, credits, missing keys). Researchers can reason about reproducibility cost.

## Anonymization disclosure

The source data was a Neo Genesis production GEO probe.

| Class | Treatment |
|---|---|
| Founder name (`Yesol Heo`, `허예솔`) | **Preserved** — deliberate measurement target, publicly attested via Wikidata Q139569708 |
| Founder email / phone | Redacted to `<redacted-email>` / `<redacted-phone>` |
| Generic email patterns (any LLM-invented address) | Redacted to `<redacted-email>` |
| Korean RRN (resident reg number) | Redacted to `<redacted-rrn>` |
| API tokens (`sk-*`, `ghp_*`, `hf_*`, JWT, bot tokens) | Redacted to `<redacted-*>` |
| Local absolute Windows paths | Redacted to `<repo>` / `<workspace>` / `<home>` |
| Internal hostnames | Redacted to `<work-pc>`, `<gpu-worker>`, `<server>`, `<mac-build>` |
| Tailscale / private IPs | Redacted to `<tailscale-ip>` / `<private-ip>` |

Each emitted string is re-tested with all redaction regexes; publish aborts on leak.

**LLM hallucinations preserved**: The `response_text` field contains responses that may invent biographical details about the founder (e.g., wrong company affiliations, fabricated PhD credentials). These are kept as the empirical observation of what frontier LLMs actually returned — they are NOT factual claims about the founder.

## Provenance

- **Source**: Neo Genesis private GEO probe (`scripts/geo_measure/measure_citations.py` + sqlite store).
- **Time window**: 2026-04-28 to 2026-05-03.
- **Curator**: Neo Genesis Lab (`neogenesislab` HuggingFace org).
- **Wikidata**: [Q139569680 (Neo Genesis)](https://www.wikidata.org/wiki/Q139569680), [Q139569708 (Yesol Heo, founder)](https://www.wikidata.org/wiki/Q139569708).
- **Related releases by the same operator**:
  - [`korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`ethicaai-mixed-safe-evidence`](https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence)
  - [`whylab-gemini-2-5-docker-validation`](https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation)
  - [`sbu-pseo-effects-2026-04`](https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04)
  - [`cross-agent-review-queue-2026`](https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026)

## Citation

```bibtex
@misc{neogenesis_geo_baseline_2026,
  title  = {Korean LLM Citation Baseline 2026: A real-brand GEO measurement dataset across frontier LLMs},
  author = {Neo Genesis Lab},
  year   = {2026},
  url    = {https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026},
  note   = {Empirical brand-mention measurements across gemini-2.5-flash, gpt-4o, and claude-sonnet-4-6 for 30 bilingual brand-relevant prompts, with both successful and errored attempts preserved}
}
```

## License

CC-BY-4.0 — free for research and commercial use with attribution to Neo Genesis Lab.

---

## 한국어 요약

**Korean LLM Citation Baseline 2026** 은 실존 기업(Neo Genesis, Wikidata Q139569680)에 대한 **3개 frontier LLM** (`gemini-2.5-flash`, `gpt-4o`, `claude-sonnet-4-6`) 의 **실제 인용/언급률** 을 측정한 GEO/LLMO 데이터셋이다.

대부분의 GEO 연구가 **합성 프롬프트** 또는 **단일 LLM 프로빙** 에 머무는 것과 달리, 이 데이터셋은:
- 실제 공개 기업을 측정 대상으로 함 (가공된 페이크 브랜드 X)
- 3개 frontier LLM 을 동일 프로토콜로 프로빙
- 6개 의도 카테고리 × 30개 prompt × 영문+한국어 혼용
- **에러 attempt 도 보존** (rate-limit / credit / API key 부재 케이스 포함, 재현성 연구 가능)

응용 예시:
- GEO 기준선 측정 (한국어 vs 영어 비대칭, LLM 별 차이)
- LLM hallucination grounding (founder 에 대한 LLM 의 가짜 학력/소속 등 그대로 박제)
- multilingual citation gap 분석
- frontier LLM 의 niche-but-real entity 처리 행태 연구

**익명화**: 측정 대상인 창업자 이름은 의도적으로 유지 (Wikidata Q139569708 로 공개 attestation 됨). 그 외 이메일 / 전화 / 신용 / RRN / 절대 경로 / 호스트명 / private IP 는 모두 redaction. 발행 직전 모든 문자열에 대해 재검증.

라이선스 CC-BY-4.0 — 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_korean_llm_citation_baseline_2026_2026,
  author       = {Yesol Heo and Neo Genesis Lab},
  title        = {Korean LLM Citation Baseline 2026},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Korean LLM Citation Baseline 2026 (Neo Genesis GEO Measurement)"
type: dataset
authors:
  - family-names: "Heo"
    given-names: "Yesol"
    affiliation: "Neo Genesis Lab"
date-released: "2026-05-01"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026"
repository: "https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018479"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - korean
  - llm
  - citation
  - generative-engine-optimization
  - geo
  - openai
  - anthropic
  - perplexity
  - gemini
  - neo-genesis
  - measurement
preferred-citation:
  type: dataset
  title: "Korean LLM Citation Baseline 2026 (Neo Genesis GEO Measurement)"
  authors:
    - family-names: "Heo"
      given-names: "Yesol"
      affiliation: "Neo Genesis Lab"
  doi: "10.5281/zenodo.20018479"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018479"
```
