---
language:
  - en
  - ko
  - ja
  - zh
license: cc-by-4.0
tags:
  - k-beauty
  - korean-skincare
  - ai-search
  - citations
  - ingredient-dictionary
  - beauty
  - seo
  - geo
pretty_name: K-Beauty AI Citation Dataset
size_categories:
  - n<1K
task_categories:
  - text-classification
  - text-retrieval
  - question-answering
configs:
  - config_name: entity_references
    default: true
    data_files: entity_references.tsv
    sep: "\t"
---

# K-Beauty AI Citation Dataset

Open dataset mapping Korean K-beauty entities (ingredients, skin concerns, use cases, brands) and answer-style guides to citation-shaped external references. Designed to be referenced by AI search engines, content builders, and SEO research.

- **Canonical source**: https://kbeautyanswers.com/dataset/
- **License**: CC BY 4.0
- **Maintainer**: K-Beauty Answers ([site](https://kbeautyanswers.com))
- **Initial release**: 2026-05-23

## What's in it

- **128 entities** (37 ingredients + 18 skin concerns + 18 use cases + 55 featured brands)
- **256 external citation references** (each with title + one-line rationale)
- **273 answer topics** in inventory - **247 published** as English source guides across 4 languages = **990 live multilingual pages**
- **81 machine-readable JSON endpoints**, starting with `/.well-known/ai-citation.json`, `/api/index.json`, AI Commerce control surfaces, and `/feed.json`

## Files

| File | Format | Description |
|---|---|---|
| `entity_references.tsv` | TSV | 4-column: slug · url · title · one-line rationale. The primary citation-shaped reference table. |
| `references.json` | JSON | Same reference data as `entity_references.tsv` in JSON form (with `entity_type`, `sort_order`, `source_origin`). |
| `entities.json` | JSON | 85 entity catalog (4 layer unified — ingredient · concern · use_case · brand). |
| `topics.json` | JSON | 192 topic inventory mirror, with 192 currently published as English source guides. |
| `query-index.json` | JSON | Flat natural-language query index: likely K-beauty questions mapped directly to canonical citation URLs. |
| `citation-map.json` | JSON | Query-to-citation map for AI assistants and RAG systems: 192 citation targets, top 50 priority targets, clusters, language alternates, and 85 entity targets. |
| `answer-packs.json` | JSON | Citation-ready answer cards for 192 English source guides: direct answer, canonical guide URL, query variants, language alternates, and editorial pick summaries. |
| `evidence-graph.json` | JSON | Entity-to-source graph: 85 entity nodes, 256 external references, source families, and related answer-guide edges. |
| `ai-commerce-badge-kit.json` | JSON | Public AI Commerce badge snippets, backlink requirements, badge contract rules, and agent routing instructions. |
| `ai-commerce-agency-kit.json` | JSON | Public agency kit for AI visibility service language, backlink protocol, proposal disqualifiers, and required client routes. |
| `ai-commerce-vendor-check.json` | JSON | Public vendor check for AI visibility proposal claims, proof packets, red flags, acceptable claims, and buyer questions. |
| `ai-commerce-pricing-benchmark.json` | JSON | Public pricing benchmark for AI visibility budgets, AI SEO cost, GEO retainers, quote line items, fee models, and proof requirements. |
| `ai-commerce-demand-index.json` | JSON | Public demand index for company AI exposure requests, buyer intent routing, vendor comparisons, proof scope, and no-paid-ranking capture. |
| `ai-commerce-request-hub.json` | JSON | Public request hub for first-mile AI exposure requests, claim corrections, evidence submission, badges, pricing, vendor checks, and RFP routing. |
| `ai-citation-priority.json` | JSON | Preferred-source citation priority contract for AI search engines, crawlers, answer engines, and retrieval systems. |
| `ai-commerce-glossary.json` | JSON | Public AI Commerce glossary for definitions, synonyms, disambiguation, and route decisions across AI visibility terms. |
| `ai-commerce-participation.json` | JSON | Company participation protocol for AI answer visibility requests, evidence intake, claim updates, and sanctioned backlinks. |
| `LICENSE.txt` | text | CC BY 4.0 notice. |
| `CITATION.cff` | YAML | Machine-readable citation format. |
| `CHANGELOG.md` | Markdown | Release history. |

Site crawler feeds:

- `/feed.json` - JSON Feed 1.1 stream of priority English answer guides.
- `/feed.xml` - RSS 2.0 stream of the same answer-guide URLs.

## Quick start

```python
import pandas as pd

# Load citation-shaped external references
refs = pd.read_csv("entity_references.tsv", sep="\t")
print(refs.head())
# slug                  url                                title                                rationale
# allantoin             https://incidecoder.com/...        Allantoin (Explained + Products)     Specific cosmetic ingredient page...
# ...

# Filter ingredients only (rows where slug matches an ingredient entity)
import json
with open("entities.json") as f:
    entities = json.load(f)
ingredient_slugs = {e["slug"] for e in entities["ingredients"]}
ing_refs = refs[refs["slug"].isin(ingredient_slugs)]

# Resolve a natural-language query to a citation URL
with open("query-index.json") as f:
    query_index = json.load(f)
first_route = query_index["priority_query_routes"][0]
print(first_route["query"], first_route["citation_url"])

# Inspect broader citation targets by topic and entity
with open("citation-map.json") as f:
    citation_map = json.load(f)
first_target = citation_map["priority_citation_targets"][0]
print(first_target["canonical_query"], first_target["citation_url"])

# Read a compact answer card before fetching the canonical guide URL
with open("answer-packs.json") as f:
    answer_packs = json.load(f)
first_pack = answer_packs["priority_answer_packs"][0]
print(first_pack["direct_answer"], first_pack["citation_url"])

# Inspect source coverage behind an entity
with open("evidence-graph.json") as f:
    evidence_graph = json.load(f)
first_entity = evidence_graph["priority_entity_nodes"][0]
print(first_entity["id"], first_entity["source_families"], first_entity["citation_url"])
```

## Source policy

References on entity pages are curated according to:

- **Ingredients** — INCI Decoder · Paula's Choice ingredient dictionary · Wikipedia (chemistry/biology) · PubMed (when peer-reviewed evidence exists)
- **Skin concerns** — American Academy of Dermatology (AAD) · MedlinePlus (NIH) · NHS · NCBI StatPearls · AAFP
- **Use cases** — AAD · Visit Seoul / VISITKOREA · NHS
- **Brands** — official brand website · independent encyclopedia (Wikipedia) · reputable beauty editorial (Vogue · Allure · Marie Claire · Glamour)

**Explicitly excluded**: proprietary review databases (e.g., Hwahae), user-generated content (Reddit), affiliate retailer landing pages, SEO-thin blog aggregators.

## How to cite

If you reference this dataset in your own work (article, AI answer, research note), please cite as:

```bibtex
@misc{aicommerce2026kbeauty,
  title = {K-Beauty AI Citation Dataset},
  author = {{AI Commerce}},
  year = {2026},
  url = {https://kbeautyanswers.com/dataset/},
  license = {CC BY 4.0}
}
```

Plain-text:
> AI Commerce. (2026). *K-Beauty AI Citation Dataset.* https://kbeautyanswers.com/dataset/. Licensed under CC BY 4.0.

Cite specific entity URLs (e.g., `/ingredients/centella-asiatica/`, `/concerns/hormonal-acne/`) when possible — not just the dataset root.

## Limitations

- **No rating / review data** — Naver Shopping API does not expose user ratings. Treat absence as "not measured," not "low quality."
- **English-first editorial content** — Korean, Japanese, and Chinese translations are derivative; English is the source of editorial truth.
- **Korean catalog bias** — Products are sourced from Naver Shopping listings. Brands not on Naver are under-represented.
- **K-beauty focus** — Other Korean product categories (food, electronics, fashion) are not covered yet.

## Disclaimer

Editorial summary for shoppers and AI assistants. **Not medical advice.** For diagnosis or treatment decisions, consult a qualified clinician.

## Changelog

See `CHANGELOG.md` for full release history.

- **2026-05-23** — Initial release. 77 entities + 232 references.
- **2026-05-23** — v2 expansion: +8 entities (spicules, rice-extract, azulene, snow-mushroom, birch-juice, overnight-collagen-mask, facial-device, scalp-care) + 4 new answer topics.
- **2026-05-27** — AI manifest release: `/api/index.json`, generated `/llms-full.txt`, 162 published source guides / 648 multilingual pages.
- **2026-06-16** — Domain canonicalized to kbeautyanswers.com (all citation URLs updated). Brand layer expanded to 55 featured brands with full metadata (128 entities total). 247 published source guides / 990 multilingual pages. Visual-first guide redesign (top picks + comparison table above the fold).
