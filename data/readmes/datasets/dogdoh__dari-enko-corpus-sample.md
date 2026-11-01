---
dataset_info:
  features:
  - name: source_en
    dtype: string
  - name: target_ko
    dtype: string
  - name: domain
    dtype: string
  - name: quality_score
    dtype: float32
  - name: labse_score
    dtype: float32
  - name: comet_score
    dtype: float32
license: cc-by-4.0
language:
- en
- ko
size_categories:
- 1K<n<10K
tags:
- translation
- parallel-corpus
- en-ko
- technical-translation
- mtpe
---

# Dari EN↔KO Technical Translation Corpus (Sample)

🌉 **Dari** (다리, "bridge") — 67M+ EN↔KO parallel sentence pairs for technical translation.

## Dataset Description

This is a **10,000-pair sample** from the full Dari corpus. The full corpus contains **67.2 million** high-quality EN↔KO parallel segments across multiple technical domains.

### Domains
| Domain | Full Corpus Pairs |
|--------|------------------|
| Patent (KIPRIS) | 15M+ |
| Medical (PubMed) | 12M+ |
| IT/Software | 10M+ |
| Legal | 8M+ |
| General | 22M+ |

### Files
- `data/sample.csv` — 10,000 parallel EN↔KO sentence pairs (stratified by domain)
- `data/glossary.csv` — 5,000 bilingual term entries
- `data/stats.csv` — Domain distribution statistics

### Quality Metrics
- LaBSE semantic similarity scores
- COMET translation quality scores
- Human quality ratings (0-1 scale)

## Usage

```python
from datasets import load_dataset
ds = load_dataset("dogdoh/dari-enko-corpus-sample")
```

## Full Corpus Access

| Tier | Price | Includes |
|------|-------|----------|
| Free | $0 | This 10K sample |
| API Basic | $49/mo | 50K chars/month, REST API |
| API Pro | $199/mo | 500K chars/month, batch export |
| Enterprise | Custom | Full corpus license, on-prem |

🔗 **API**: [dari.is-a.dev](https://dari.is-a.dev)
📧 **Contact**: dogdoh1338@icloud.com
