---
language:
- en
- ko
license: cc-by-4.0
task_categories:
- reinforcement-learning
- other
tags:
- multi-agent
- cooperation
- safety
- agent-evaluation
- mixed-safe
- ai-ethics
- melting-pot
- coin-game
- fishery
- nash-equilibrium
- ecological-model
- maccl
- neo-genesis
- wikidata-Q139569680
- ko
- en
- reinforcement-learning
- amartya-sen
size_categories:
- n<1K
- 1K<n<10K
pretty_name: EthicaAI Mixed-Safe Multi-Environment Evidence Dataset
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
configs:
- config_name: meltingpot_results
  data_files:
  - split: train
    path: data/meltingpot_results.parquet
---

> **🛈 Anonymity Notice (2026-05-12):** The associated manuscript is currently under peer review at a double-blind venue. Author identity and venue-specific identifiers have been withheld throughout this README, the BibTeX templates, and the CITATION.cff block. The dataset itself remains CC-BY-4.0 and is independently citable via its Zenodo DOI `10.5281/zenodo.20018466`. The author byline will be restored after the review outcome is announced.


## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018466.svg)](https://doi.org/10.5281/zenodo.20018466)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018466`** ([Zenodo record](https://zenodo.org/record/20018466)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018466,
  author       = {{Anonymous (under peer review)}},
  title        = {EthicaAI Mixed-Safe Multi-Environment Evidence Dataset},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018466},
  url          = {https://doi.org/10.5281/zenodo.20018466}
}
```

# EthicaAI Mixed-Safe Multi-Environment Evidence Dataset

> Underlying experimental evidence from **[Neo Genesis](https://neogenesis.app)** research on multi-agent cooperative-constraint learning — released as an open dataset for community replication and AI safety research. The associated manuscript is currently under peer review at a double-blind venue; author identity and venue-specific identifiers are withheld until review outcome is announced.

## What this dataset is

A **3-environment evidence bundle** showing how multi-agent reinforcement-learning agents behave under different cooperative-constraint regimes. Each environment was deliberately chosen to stress-test different aspects of the **mixed-safe** boundary thesis:

| Environment | What it tests | Sample size | Key statistic |
|---|---|---:|---|
| **Melting Pot (`clean_up`)** | Boundary-consistent cooperative learning under floor-probability sweep vs. baseline | **50 seed × floor_prob runs** | t-test eval: floor_mean = 0.06, baseline_mean = 0.001, **p = 0.063502** |
| **Coin Game Deep (adapted)** | Selfish equilibrium vs. MACCL (Multi-Agent Cooperative Constraint Learning) on 160 seeds | **160 seeds × 200 episodes** | MACCL survival ≫ selfish survival (paper-level finding) |
| **Fishery Nash Trap** | Ecological tragedy-of-commons with 300 seeds and tipping-point dynamics | **300 seeds × 300 episodes** | survival vs. harvest welfare frontier |

The three environments together form the **mixed-safe corpus** — the paper's central claim is that no single environment proves the thesis, but the **boundary consistency across three independently-designed substrates** does.

## Why publish the data

Most AI-safety papers expose plots and aggregate statistics but withhold seed-level results. This dataset releases:

- All **50 seed-level Melting Pot runs** with full `train_rewards` trajectories per seed
- The exact `late_train` and `eval` statistics used in the paper's t-tests, p-values, bootstrap CIs
- Coin Game `selfish` vs `maccl` aggregated per-seed metrics
- Fishery 300-seed survival/welfare results across `phi1` calibration values
- Source-file provenance (which results came from which compute node — Mac Studio head shard vs. Linux server tail shard)

This lets independent researchers:
1. Replicate the paper's claims by re-running the same seeds
2. Extend the analysis with their own cooperative-constraint variants
3. Use the seed-level data as a benchmark for new MARL methods

## Files

```
data/
├── meltingpot_results.jsonl       50 lines, one per (seed, floor_prob) combination
├── meltingpot_statistics.json     paper-grade t-test + bootstrap CI per condition
├── coin_game_deep.json            selfish vs maccl, 160 seeds × 200 episodes
├── fishery_default.json           default ecological config
└── fishery_300seed.json           300-seed phi1 sweep, 300 episodes per seed
```

## Schema (`meltingpot_results.jsonl`)

Each line is one (seed, floor_prob) run:

```json
{
  "seed": 88409749,
  "floor_prob": 0.0,
  "train_rewards": [0.0, 0.0, 0.14, 2.71, ...],
  "eval_rewards": [...]
}
```

`train_rewards` is the per-episode reward time series during training; `eval_rewards` is the held-out evaluation reward. `floor_prob = 0.0` corresponds to baseline (no cooperative floor); `floor_prob > 0` corresponds to mixed-safe condition.

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/ethicaai-mixed-safe-evidence", split="train", data_files="data/meltingpot_results.jsonl")
print(len(ds), "Melting Pot runs")

# Per-condition statistics (already computed):
import json, urllib.request
url = "https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence/resolve/main/data/meltingpot_statistics.json"
stats = json.loads(urllib.request.urlopen(url).read())
print("eval floor_mean:", stats["statistics"]["eval"]["floor_mean"])
print("eval baseline_mean:", stats["statistics"]["eval"]["baseline_mean"])
print("p-value:", stats["statistics"]["eval"]["p_value"])
```

## Reproducing the paper's findings

The full reproduction code (RLlib + Melting Pot harness + Coin Game adapter + Fishery simulator) is referenced in the paper's appendix. The dataset above is the **frozen evidence snapshot** used in the camera-ready manuscript.

Statistical machinery (provided in `meltingpot_statistics.json`):
- Welch's t-test (unequal variance) for floor vs baseline mean reward
- Bootstrap 95% CI on the difference (resamples documented in `config`)
- Cohen's d effect size
- Per-shard provenance for distributed compute audit

## Related Neo Genesis assets

- 📄 **Research entry** — see `https://neogenesis.app/data/research/ethicaai-melting-pot-mixed-safe` (manuscript under double-blind peer review)
- 🤗 **Companion dataset** — [`neogenesislab/korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
- 🆔 **Wikidata** — [Q139569718 (EthicaAI)](https://www.wikidata.org/wiki/Q139569718) · [Q139569680 (Neo Genesis parent org)](https://www.wikidata.org/wiki/Q139569680)
- 🌐 **Org site** — https://neogenesis.app

## Citation

```bibtex
@misc{ethicaai_mixed_safe_evidence_2026_anon,
  title     = {EthicaAI Mixed-Safe Multi-Environment Evidence Dataset},
  author    = {{Anonymous (under peer review)}},
  howpublished = {Hugging Face Datasets},
  year      = {2026},
  url       = {https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence},
  note      = {Underlying evidence dataset, CC-BY-4.0}
}
```

## License

CC-BY-4.0. Free for research and commercial use with attribution to **Neo Genesis** and the underlying paper.

## Provenance

- Compute nodes: Mac Studio (head shard `seed_indices 0-23`) + Linux server (tail shard `seed_indices 24-49`) — see `meltingpot_statistics.json` `source_summary`
- Curation: Neo Genesis Research (manuscript under peer review; curator identity withheld pending outcome)
- Frozen 2026-04-15 (`meltingpot_n80_stats.json` paper-anchor revision)
- Released 2026-04-28

## Citation

```bibtex
@dataset{neogenesislab_ethicaai_mixed_safe_evidence_2026,
  author       = {{Anonymous (under peer review)}},
  title        = {EthicaAI Mixed-Safe Cooperation Multi-Environment Evidence Dataset 2026},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "EthicaAI Mixed-Safe Multi-Environment Evidence Dataset"
type: dataset
authors:
  - name: "Anonymous (under peer review)"
    affiliation: "Neo Genesis Research"
date-released: "2026-04-28"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence"
repository: "https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018466"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - multi-agent
  - alignment
  - constitutional-ai
  - melting-pot
  - coin-game
  - fishery
  - ethicaai
  - neo-genesis
  preferred-citation:
  type: dataset
  title: "EthicaAI Mixed-Safe Multi-Environment Evidence Dataset"
  authors:
    - name: "Anonymous (under peer review)"
      affiliation: "Neo Genesis Research"
  doi: "10.5281/zenodo.20018466"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018466"
```
