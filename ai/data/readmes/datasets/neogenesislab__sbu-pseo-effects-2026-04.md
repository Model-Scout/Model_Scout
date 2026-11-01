---
language:
- ko
- en
license: cc-by-4.0
task_categories:
- tabular-classification
- tabular-regression
- text-classification
tags:
- programmatic-seo
- ai-content
- marketing-data
- multi-tenant-blog
- operations
- 1-person-startup
- ko
- en
- neo-genesis
- wikidata-Q139569680
- yesol-heo-founder
- seo
- saas
- neo-genesis-sbu
size_categories:
- n<1K
pretty_name: Neo Genesis SBU Programmatic SEO Effects (April 2026)
configs:
- config_name: default
  data_files:
  - split: train
    path: data/snapshots.parquet
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
---

## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018474.svg)](https://doi.org/10.5281/zenodo.20018474)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018474`** ([Zenodo record](https://zenodo.org/record/20018474)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018474,
  author       = {Heo, Yesol and Neo Genesis Lab},
  title        = {Neo Genesis SBU Programmatic SEO Effects (April 2026)},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018474},
  url          = {https://doi.org/10.5281/zenodo.20018474}
}
```

# Neo Genesis SBU Programmatic SEO Effects (April 2026)

> A transparent operational dataset of how a **1-person AI company runs 6 active programmatic-SEO SBUs** ([Neo Genesis](https://neogenesis.app)), aggregated to **35 per-SBU-per-snapshot rows** spanning **2026-04-27 → 2026-04-29**.

## Why this dataset exists

Most SEO datasets are scraped surface metrics (rankings, organic visits) or vendor case studies that hide the publishing pipeline.
This dataset shows the **other side** — the publish/refresh / weak-post-repair / internal-link operations that produce those rankings — for a real fleet of multi-tenant blogs that one founder operates with AI agents.

It is published as **operational data**, not a product benchmark. Treat it as a window into how programmatic-SEO content ops actually behave on a live, autonomously-managed multi-blog network.

## Dataset summary

- **35 rows** (one per SBU per publish/refresh batch)
- **6 active SBUs** covered: `aiforge`, `craftdesk`, `deploystack`, `finstack`, `sellkit`, `toolpick`
- **7 source snapshot files** scanned (`quality-repair-*.json`, dry-runs excluded)
- **Window**: 2026-04-27 → 2026-04-29
- **Anonymization**: no user IDs, no IPs, no author identities, no Supabase row IDs, no commit SHAs, no post slugs, no URLs — only counts and per-SBU rollups
- **Aggregation grain**: per SBU per publish/refresh batch

## Per-SBU rollup

| SBU | Category | Snapshots | Weak-posts expanded | Weak-posts reinforced | Files changed | Latest ready posts | Latest modeled MAU |
|---|---|---|---|---|---|---|---|
| `aiforge` | `ai_tools` | 6 | 14 | 3 | 120 | 432 | 151,200 |
| `craftdesk` | `design_tools` | 6 | 24 | 2 | 57 | 369 | 129,150 |
| `deploystack` | `devops` | 6 | 21 | 4 | 48 | 312 | 109,200 |
| `finstack` | `fintech` | 6 | 21 | 0 | 21 | 307 | 107,450 |
| `sellkit` | `sales_tools` | 6 | 6 | 1 | 7 | 291 | 101,850 |
| `toolpick` | `ai_coding` | 5 | 8 | 0 | 113 | 379 | 132,650 |

## Active SBUs (live URLs)

- [`aiforge`](https://neogenesis.app/sbu/aiforge) (category: `ai_tools`)
- [`craftdesk`](https://neogenesis.app/sbu/craftdesk) (category: `design`)
- [`deploystack`](https://neogenesis.app/sbu/deploystack) (category: `devops`)
- [`finstack`](https://neogenesis.app/sbu/finstack) (category: `fintech`)
- [`sellkit`](https://neogenesis.app/sbu/sellkit) (category: `ecommerce`)
- [`toolpick`](https://neogenesis.app/sbu/toolpick) (category: `comparison`)

## Schema

Each row in `data/snapshots.jsonl`:

```json
{
  "sbu_slug": "toolpick",
  "category": "comparison",
  "snapshot_date": "2026-04-27",
  "snapshot_iso": "2026-04-27T13:23:01+09:00",
  "weak_posts_expanded": 2,
  "weak_posts_reinforced": 0,
  "internal_links_added": 0,
  "intent_routes_added": 0,
  "files_changed": 2,
  "clusters_routed": 0,
  "total_ready_posts": 379,
  "avg_words": 1350,
  "category_count": 60,
  "cta_coverage": 0.72,
  "internal_link_coverage": 0.887,
  "frontmatter_coverage": 1.0,
  "modeled_mau": 132650
}
```

| Field | Meaning |
|---|---|
| `sbu_slug` | SBU identifier (one of `toolpick` / `aiforge` / `finstack` / `sellkit` / `deploystack` / `craftdesk` / `reviewlab` / `ur-wrong`) |
| `category` | Coarse content category proxy (`comparison`, `ai_tools`, `fintech`, `ecommerce`, `devops`, `design`, `reviews`, `general`) |
| `snapshot_date` | ISO date of the publish/refresh batch (KST day) |
| `snapshot_iso` | Full ISO 8601 timestamp (KST tz) |
| `weak_posts_expanded` | Low-quality posts expanded in this run |
| `weak_posts_reinforced` | Posts whose CTA / internal links were reinforced in this run |
| `internal_links_added` | Internal links inserted in this run |
| `intent_routes_added` | Search-intent routes (category landings) added in this run |
| `files_changed` | MDX files modified in this run |
| `clusters_routed` | Topic clusters routed in this run (run-scope) |
| `total_ready_posts` | Latest SBU-level: posts that pass the publish gate |
| `avg_words` | Latest SBU-level: average word count |
| `category_count` | Latest SBU-level: distinct content categories on the site |
| `cta_coverage` | Latest SBU-level: 0..1 share of posts with a CTA block |
| `internal_link_coverage` | Latest SBU-level: 0..1 share of posts with internal links |
| `frontmatter_coverage` | Latest SBU-level: 0..1 share with complete frontmatter |
| `modeled_mau` | Latest SBU-level: modeled monthly visits (350/post baseline) |

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/sbu-pseo-effects-2026-04", split="train")
print(ds[0])
# => {'sbu_slug': 'toolpick', 'category': 'comparison', ...}

# Total weak posts repaired across all SBUs in the window
print(sum(r["weak_posts_expanded"] + r["weak_posts_reinforced"] for r in ds))
```

## Anonymization & ethics

This dataset is published as transparent operational telemetry. The following are **never** included:

- user IDs, sessions, IPs, geo
- author identities, emails, usernames
- Supabase row IDs, internal database keys
- commit SHAs, branch names, deploy IDs
- post slugs, URLs, draft titles
- visitor analytics, GA4 / PostHog identifiers

Only **operational counts** (how many MDX files were touched, how many weak posts were expanded, how many internal links were added) and **SBU-level aggregates** (total ready posts, average word count, coverage ratios, modeled MAU) are exposed.

The aggregation grain is `per_sbu_per_snapshot` — there is no row that resolves to a single piece of content or a single user action.

## Use cases

- **Programmatic SEO research**: empirical baselines for "how many MDX files per SBU per refresh cycle"
- **AI content operations**: prior data for autonomous publishing pipelines (multi-tenant blog factories)
- **Founder ops benchmarking**: comparison data for solo / 1-person AI companies running content fleets
- **Marketing automation modeling**: input for CTA / internal-link coverage progression over time

## Comparison to typical SEO datasets

| Source | Surface metrics (rankings / GSC) | Publishing pipeline counts | Multi-tenant network | Anonymized | License |
|---|---|---|---|---|---|
| Ahrefs / Semrush case data | ✓ | — | — | partial | proprietary |
| Common Crawl WARC | ✓ (raw HTML) | — | — | — | open |
| GSC dumps | ✓ | — | per-domain | partial | private |
| **Neo Genesis SBU pSEO Effects** | — | **✓** | **✓** | **✓** | **CC-BY-4.0** |

## Provenance

- Source       : Neo Genesis live `data/sbu-growth/` operational logs
- Curator      : Yesol Heo (sole founder/operator, [neogenesis.app](https://neogenesis.app))
- Generator    : `sbu_growth_quality_repair.mjs` running under `sbu_autonomous_growth_runner.mjs`
- Wikidata     : [Q139569680 (Neo Genesis)](https://www.wikidata.org/wiki/Q139569680)
- Sister datasets:
  - [`neogenesislab/korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`neogenesislab/ethicaai-mixed-safe-evidence`](https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence)
  - [`neogenesislab/whylab-gemini-2-5-docker-validation`](https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation)

## Citation

```bibtex
@misc{neogenesis_sbu_pseo_effects_2026_04,
  title  = {Neo Genesis SBU Programmatic SEO Effects (April 2026)},
  author = {Heo, Yesol},
  year   = {2026},
  url    = {https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04},
  note   = {Neo Genesis, an AI-native automation company running 11 live business units of which 8 are programmatic-SEO SBUs}
}
```

## License

**CC-BY-4.0** — free for research and commercial use with attribution to Neo Genesis.

---

## 한국어 요약

**SBU Programmatic SEO Effects (April 2026)** 는 1인 AI 자동화 기업 **[Neo Genesis](https://neogenesis.app)** 가 운영 중인 **6개 SBU 프로그래매틱 SEO 블로그**의 발행/리프레시 파이프라인 운영 데이터를 익명화 집계한 것이다.

기존 SEO 데이터셋이 `랭킹 / 트래픽` 같은 노출 지표만 다룬다면, 이 데이터셋은 그 결과를 만들어내는 **퍼블리싱 파이프라인 자체** (`약한 글 보강`, `내부 링크 삽입`, `MDX 파일 변경 수`) 를 SBU 단위로 보여준다.

집계 단위:
- 행 단위: **`SBU × 발행/리프레시 배치`**
- 발행 일자 범위: **2026-04-27 → 2026-04-29**
- 행 수: **35**
- 스캔된 원본 스냅샷 파일: **7**

익명화 정책:
- `user_id`, `ip`, `author`, `supabase_id`, `commit_sha`, `slug`, `url` 모두 제거
- SBU 단위 + 스냅샷 단위 집계만 공개

라이선스 CC-BY-4.0 — 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_sbu_pseo_effects_2026_04_2026,
  author       = {Yesol Heo and Neo Genesis Lab},
  title        = {SBU Programmatic SEO Effects 2026-04 (Anonymized Snapshot)},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Neo Genesis SBU Programmatic SEO Effects (April 2026)"
type: dataset
authors:
  - family-names: "Heo"
    given-names: "Yesol"
    affiliation: "Neo Genesis Lab"
date-released: "2026-04-29"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04"
repository: "https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018474"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - programmatic-seo
  - search-engine-optimization
  - saas
  - neo-genesis
  - ga4
  - posthog
  - ai-traffic
  - case-study
preferred-citation:
  type: dataset
  title: "Neo Genesis SBU Programmatic SEO Effects (April 2026)"
  authors:
    - family-names: "Heo"
      given-names: "Yesol"
      affiliation: "Neo Genesis Lab"
  doi: "10.5281/zenodo.20018474"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018474"
```
