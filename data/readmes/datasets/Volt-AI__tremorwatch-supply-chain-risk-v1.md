---
license: cc-by-nc-sa-4.0
language:
  - en
  - ko
  - ja
size_categories:
  - 1K<n<10K
task_categories:
  - text-classification
  - time-series-forecasting
tags:
  - supply-chain
  - risk
  - geopolitical
  - chokepoint
  - geo
  - news
  - ESG
pretty_name: "TremorWatch Supply Chain Risk Dataset (v1, snapshot 2026-05-12)"
configs:
  - config_name: events
    data_files: data/events.parquet
  - config_name: chokepoints
    data_files: data/chokepoints.parquet
  - config_name: entities
    data_files: data/entities.parquet
---

# TremorWatch Supply Chain Risk — v1

AI-summarized global supply chain risk events with chokepoint exposure
mapping. Snapshot **2026-05-12**.

## 🌐 Explore the live, browsable version

The Parquet bundle below is a **point-in-time snapshot**. The browsable site
keeps the same data updated daily and adds per-event AI briefs, KO/JA
translations, and a live map.

- **Map + event feed**: [tremorwatch.com](https://tremorwatch.com?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)
- **Chokepoints** (Hormuz, Malacca, Suez, Taiwan Strait, …): [tremorwatch.com/chokepoints](https://tremorwatch.com/chokepoints?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)
- **Commodities** (semiconductors, rare earth, crude, …): [tremorwatch.com/commodities](https://tremorwatch.com/commodities?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)
- **Watchlist & severity feed**: [tremorwatch.com/watchlist](https://tremorwatch.com/watchlist?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)

For a daily-refreshed commercial license, **[join the v1 waitlist](https://tremorwatch.com/data?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)**.

## What's inside

| Table        | Rows  | Description |
|--------------|-------|-------------|
| `events`     | 9,555 | Risk events with AI-generated summaries, ticker / commodity / chokepoint mapping |
| `chokepoints`| 17 | Maritime / strategic chokepoints with strategic-importance briefs |
| `entities`   | 194 | Commodities and countries with i18n names and AI briefs |

## Loading the dataset

```python
from datasets import load_dataset

events = load_dataset("Volt-AI/tremorwatch-supply-chain-risk-v1", "events", split="train")
chokepoints = load_dataset("Volt-AI/tremorwatch-supply-chain-risk-v1", "chokepoints", split="train")
entities = load_dataset("Volt-AI/tremorwatch-supply-chain-risk-v1", "entities", split="train")

print(events[0])
```

## Sources & licensing

| Source                    | License                | Role |
|---------------------------|------------------------|------|
| GDELT Project             | CC BY 4.0              | Event title + geo + raw classification |
| GDACS (JRC Europe)        | Public domain          | Disaster events |
| NASA FIRMS                | Public domain          | Fire detections |
| WHO Disease Outbreak News | Public, attribution OK | Health events |
| **Volt AI** (derived)     | **CC BY-NC-SA 4.0**    | `ai_summary`, `chokepoint_ids_json`, `commodity_ids_json` |

**ACLED is explicitly excluded** — we do not have a commercial redistribution
license. If your work requires ACLED, source it directly from
[acleddata.com](https://acleddata.com).

**Commercial use** requires a paid license. The v1 daily-refresh license is
in preparation — **[join the waitlist](https://tremorwatch.com/data?utm_source=huggingface&utm_medium=marketplace&utm_campaign=hf_v1)**
or email hello@volt-ai.io for early-access terms.

## Known limitations

- **Chokepoint mapping coverage ~0.5%** (structural — most events not near maritime chokepoints)
- **i18n partial** — KO ai_summary ~14%, JA ai_summary ~55%, EN 100%
- **WHO events** are historical (older than 12 months)
- **No raw description column** — only paraphrased Volt AI ai_summary

## Citation

```bibtex
@dataset{volt-ai_tremorwatch_2026,
  author = {{Volt AI}},
  title  = {TremorWatch Supply Chain Risk Dataset (v1)},
  year   = {2026},
  url    = {https://huggingface.co/datasets/Volt-AI/tremorwatch-supply-chain-risk-v1},
  note   = {Snapshot 2026-05-12. Daily-updated browsable version at tremorwatch.com}
}
```

## About Volt AI

[Volt AI](https://tremorwatch.com) builds intelligence platforms that synthesize
public risk data with AI. Contact: hello@volt-ai.io
