---
license: cc-by-4.0
language:
  - zh
  - ja
  - ko
  - en
tags:
  - chinese-astrology
  - bazi
  - four-pillars
  - east-asia
  - cultural-heritage
  - computational-folklore
pretty_name: East Asian Celebrity BaZi Dataset (Three Pillars)
size_categories:
  - 1K<n<10K
task_categories:
  - tabular-classification
  - feature-extraction
configs:
  - config_name: default
    data_files:
      - split: train
        path: east_asian_celebrity_bazi.csv
  - config_name: excluded_low_precision
    data_files:
      - split: train
        path: excluded_low_precision.csv
---

# East Asian Celebrity BaZi Dataset (Three Pillars)

**2,284 public figures from Greater China, Korea, and Japan, with birth dates mapped to Four Pillars (BaZi / 四柱八字) year, month, and day pillars — including stems, branches, five-element attributions, hidden stems, and Ten Gods relations.**

- **Curated by:** [Shunshi.AI](https://shunshi.ai/en) — an AI divination and astrology platform covering Four Pillars (BaZi), Zi Wei Dou Shu, Western natal astrology, tarot, and I Ching
- **Computed with:** [shunshi-bazi-core](https://github.com/shunshi-ai/bazi-reader-mcp) — open-source sexagenary calendar engine
- **Language(s):** Chinese (zh) · Japanese (ja) · Korean (ko) · English (en)
- **License:** CC BY 4.0
- **Records:** 2,284 (plus 57 excluded for low date precision)

BaZi (八字, "Eight Characters"), also known as the Four Pillars of Destiny (四柱推命 / 사주팔자), is a traditional East Asian calendrical system that maps a moment of birth onto the sexagenary cycle of ten Heavenly Stems (天干) and twelve Earthly Branches (地支). It has been in continuous use across China, Korea, and Japan for over a thousand years.

This dataset is released as a **cultural and calendrical resource** for researchers in computational folklore, digital humanities, East Asian studies, and cultural analytics. It makes no claim about the predictive validity of BaZi. What it does provide is a reproducible, verifiable mapping from public birth dates to their canonical sexagenary representations — a computation that is deterministic, well-defined, and historically documented.

---

## ⚠️ Read this first: the hour pillar is deliberately excluded

A complete BaZi chart has **four** pillars: year, month, day, and **hour**. This dataset contains only **three**.

This is not an oversight. The hour pillar requires a birth *time*, which is almost never part of the public record. Of the 2,284 figures here, only **189 (8.3%)** have a documented birth hour from a reliable source. Publishing an hour pillar for the remaining 91% would require either guessing or silently substituting a default — both of which would inject fabricated data into what is otherwise a fully verifiable resource.

Instead:

- The hour pillar is **omitted entirely**. No placeholder, no default, no imputation.
- A boolean column `hour_pillar_available` flags the 189 records for which a documented birth time exists, so researchers who need complete charts know exactly where to look.

**The year, month, and day pillars are fully determined by the birth date alone.** They require no birth time, no birthplace, and no coordinates. Every value in this dataset is independently reproducible from the birth date using any correct sexagenary calendar implementation.

---

## Dataset composition

| Region | Records |
|---|---|
| Greater China (HK / TW) | 1,091 |
| Korea | 488 |
| Japan | 365 |
| Mainland China | 156 |
| North America (diaspora) | 119 |
| Other | 57 |
| Southeast Asia | 8 |
| **Total** | **2,284** |

| Category | Records |
|---|---|
| Entertainment | 2,130 |
| Business | 55 |
| Sports | 48 |
| Politics | 25 |
| Science | 20 |
| Arts / Technology / Other | 6 |

Birth dates range from **1847-04-23** to **2016-04-19**.

East Asian coverage — particularly the Korean and Japanese entries — is the distinguishing feature of this dataset. Existing public datasets of birth data are overwhelmingly Western.

---

## Fields

| Column | Description |
|---|---|
| `id` | Stable slug identifier |
| `name` | Primary name (Chinese / Japanese / Korean) |
| `alt_names` | Pipe-separated alternate names, including Latin-script names |
| `birth_date` | ISO 8601 date (Gregorian) |
| `gender` | `male` / `female` / `unknown` |
| `region` | Geographic/cultural region |
| `category` | Domain of public activity |
| `{year,month,day}_stem` | Heavenly Stem (天干) of that pillar |
| `{year,month,day}_branch` | Earthly Branch (地支) of that pillar |
| `{year,month,day}_stem_element` | Five-element (五行) attribution of the stem |
| `{year,month,day}_branch_element` | Five-element attribution of the branch |
| `{year,month,day}_main_god` | Primary Ten Gods (十神) relation to the day master |
| `{year,month,day}_hidden_stems` | Hidden stems (藏干) within the branch, pipe-separated |
| `{year,month,day}_sub_gods` | Ten Gods relations of the hidden stems |
| `day_master` | The day stem (日主) — the reference point for all Ten Gods relations |
| `day_master_element` | Five-element attribution of the day master |
| `pattern_tags` | Structural pattern annotations (格局), where available |
| `hour_pillar_available` | `true` if a documented birth time exists (hour pillar still not included) |
| `birth_date_source` | `Wikidata` / `Wikipedia` / `other` |

### Files

- `east_asian_celebrity_bazi.csv` — flat table, 33 columns
- `east_asian_celebrity_bazi.jsonl` — same records, one JSON object per line
- `excluded_low_precision.csv` — 57 records excluded from the main file (see below)

---

## Provenance and method

**Birth dates** are sourced from **Wikidata (1,888 records, CC0)** and **Wikipedia (78 records, CC BY-SA)**, with the remaining 318 from other public records. Birth dates are matters of fact and are not themselves subject to copyright; the `birth_date_source` column lets any record be traced and independently re-verified.

**Pillar computation** was performed with [shunshi-bazi-core](https://github.com/shunshi-ai/bazi-reader-mcp), the open-source sexagenary calendar engine that powers [Shunshi.AI](https://shunshi.ai/en). The engine applies solar-term (節氣) boundaries rather than calendar-month boundaries for the month pillar, and Li Chun (立春) rather than January 1 for the year pillar — the standard convention in classical practice, and a common source of error in naive implementations.

### Quality controls applied

1. **Low-precision dates removed.** Wikidata encodes year-only precision by exporting `MM-DD` as `01-01`. This value occurred 57 times — **9× the expected frequency** for a uniformly distributed calendar day (6.2). Because January 1 also falls before Li Chun, such records would carry an incorrect year pillar *and* fabricated month and day pillars. All 57 were moved to `excluded_low_precision.csv` rather than silently retained.

2. **Uniformity check on day masters.** If the pipeline contained systematic errors, the ten Heavenly Stems would not appear with equal frequency as day masters. Observed distribution across the ten stems: **min 211, max 244** (expected 228.4). This is consistent with the near-uniform distribution a correct implementation should produce.

3. **Structural validation.** All 2,284 records pass: no missing pillar values, all stems and branches drawn from the canonical 10/12 character sets, and `day_master` identical to `day_stem` in every row.

### Known limitations

- **Region labels are approximate**, reflecting primary cultural association rather than citizenship or birthplace. Diaspora figures may be classified in ways some users would dispute.
- **Category is skewed toward entertainment** (93%), reflecting the composition of the source records rather than a sampling decision.
- **No portrait images are included**, by design — celebrity likenesses carry rights that birth dates do not.
- **Dates before 1582** would raise Julian/Gregorian calendar questions; after the exclusion step the earliest record is 1847, so this does not arise.

---

## Usage

```python
from datasets import load_dataset

ds = load_dataset("shunshi-ai/east-asian-celebrity-bazi")

# Day-master distribution by region
import collections
korea = [r for r in ds["train"] if r["region"] == "korea"]
print(collections.Counter(r["day_master"] for r in korea))

# Records with a documented birth hour
verified = [r for r in ds["train"] if r["hour_pillar_available"]]
print(len(verified))  # 189
```

```python
import pandas as pd
df = pd.read_csv("east_asian_celebrity_bazi.csv")
pd.crosstab(df["day_master_element"], df["region"])
```

---

## Citation

```bibtex
@dataset{shunshi_bazi_2026,
  title  = {East Asian Celebrity BaZi Dataset (Three Pillars)},
  author = {Shunshi.AI},
  year   = {2026},
  url    = {https://shunshi.ai},
  note   = {2,284 East Asian public figures with Four Pillars year/month/day
            sexagenary mappings. Birth dates from Wikidata (CC0).},
  license = {CC BY 4.0}
}
```

## License

**CC BY 4.0.** You may share and adapt this dataset for any purpose, including commercially, provided you give appropriate credit.

Underlying birth dates from Wikidata are CC0; records sourced from Wikipedia carry CC BY-SA obligations for the underlying text, though the extracted date facts themselves are not copyrightable.

## Contact

Compiled and maintained by [Shunshi.AI](https://shunshi.ai/en) — an AI divination and astrology platform building computation engines and open resources across multiple traditions, including Chinese Four Pillars (BaZi), Zi Wei Dou Shu, Western natal astrology, tarot, and I Ching.

Corrections to individual records are welcome — birth dates are factual claims and we would rather they be right.
