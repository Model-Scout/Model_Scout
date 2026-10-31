---
license: cc-by-nc-4.0
language:
  - ko
pretty_name: Minsim Index — Korean Human Forecasting (Sample)
tags:
  - forecasting
  - prediction-market
  - collective-intelligence
  - korea
  - korean
  - evaluation
  - benchmark
  - politics
  - economics
  - sports
  - time-series
task_categories:
  - question-answering
  - text-classification
size_categories:
  - n<1K
configs:
  - config_name: cards
    data_files: data/cards.jsonl
    default: true
  - config_name: forecast_eval
    data_files: eval/forecast_eval.jsonl
---

# Minsim Index — Korean Human Forecasting

**Track-record-selected forecasters. Strong signals on Korean events.**

Minsim Index turns the judgments of experienced Minsim Market forecasters into a selective signal for Korean politics and the economy. Participants predict what will happen and earn rewards and reputation when their forecasts are correct.

## Minsim Index strong-signal track record

| Sector | Hit rate | Correct / evaluated | 95% Wilson interval |
|---|---:|---:|---:|
| **Politics** | **94.3%** | **33 / 35** | 81.4–98.4% |
| **Economy** | **84.6%** | **22 / 26** | 66.5–93.8% |
| Combined | 90.2% | 55 / 61 | 80.2–95.4% |

**Evaluation period: 2025-12-24 to 2026-07-04. Frozen v1.2 backtest as of 2026-07-04; company-reported, not independently audited.** These results apply only to the Index's strong-signal subset. Economy is a reference estimate because n=26 is below 30.

> **예측 데이터 · 여론조사 아님 / Prediction data, not an opinion poll.** Voluntary participant forecasts do not claim statistical representativeness. Historical subset performance does not establish future accuracy or investment returns.

**민심인덱스는 적중 이력으로 검증된 상위 예측자들의 판단을 모아, 합의가 강할 때 신호를 내는 지표입니다.** 정치 강신호 94.3%(33/35), 경제 강신호 84.6%(22/26·참고치). 2026-07-04 백테스트 기준이며, 아래 13개 공개 샘플 전체의 적중률과는 다른 집계입니다.

## How the Index selects a signal

- **Politics:** top 30 eligible forecasters, with at least 50 resolved predictions per eligible forecaster; the panel's majority determines the direction.
- **Economy:** top 10 eligible forecasters, with at least 20 resolved predictions; the direction blends panel and crowd signals 50:50.
- **Strong signal:** agreement of at least 90% under the sector's Index rules. Lower agreement, ties and panels with fewer than three votes are handled separately; same-day/next-day index and FX direction cards are excluded from this Index evaluation.
- **Point-in-time selection:** rankings use only outcomes available at each question's close. The Index panel is distinct from the platform's general 1–8 vote weighting.

## What you can evaluate here

This repository contains **13 resolved aggregate cards** and an evaluation-format version of the same 13 cards. It previews the underlying question, human selection and outcome structure. **It does not contain the complete Index panel records or the 61-question strong-signal backtest.** The headline Index performance cannot be reproduced from this small public sample alone.

For an Index evaluation pack, historical coverage review or new Korean questions tailored to your team, contact **[good-god@minsim.io](mailto:good-god@minsim.io)**. Minsim Market can discuss Korean question design, participant collection, English definitions and scheduled aggregate deliveries for a scoped pilot.

Coverage includes Korean political events and economic questions, including Samsung Electronics and SK hynix. The economic Index hit rate is not a stock-specific accuracy claim.

## Files and fields

| Field / file | Meaning |
|---|---|
| `data/cards.jsonl` | 13 aggregate question records with Korean and English wording |
| `question`, `options`, English equivalents | Question and answer choices |
| `open_at`, `close_at`, `resolved_at` | Stored platform publication, close and result timestamps |
| `answer`, `answer_index` | Platform resolution labels |
| `distribution[].share_pct` | Unweighted participant-selection share |
| `distribution[].weighted_share_pct` | General accuracy-weighted selection share; not the Index panel |
| `timeline[]` | Available checkpoints at −7d, −3d, −1d and close; missing observations remain null |
| `settlement_rule`, English equivalent | Recorded resolution rules and translations |
| `eval/forecast_eval.jsonl` | The same 13 cards in evaluation format |
| `eval/baselines.json` | Baselines for this public sample only |

Selection shares are observations of participant choices, not traded prices or independently calibrated event probabilities. The existing evaluation field names `crowd_probs` and `weighted_crowd_probs` refer to these normalized shares.

## Sample baselines — not Minsim Index performance

| Forecaster | Top-choice accuracy | Multiclass Brier | Log loss |
|---|---:|---:|---:|
| Uniform | 0.46 | 0.568 | 0.879 |
| Crowd | 0.46 | 0.539 | 0.828 |
| Weighted crowd | 0.54 | 0.551 | 0.837 |

All sample scores use n=13 and are reference values only. The sample was selected for variety and includes incorrect forecasts; it is not a platform-wide or Index accuracy estimate. Scores describe the stored sample, not a certified leakage-free model benchmark.

## Evaluation timing

Before using any record for model evaluation, verify the actual outcome-availability time, observation time, question-rule version and the model's information cutoff. A stored platform close or later result-publication timestamp alone does not establish that an observation preceded the real-world outcome. Some records resolve before their stored close; exclude or reconstruct those records with a verified earlier observation. A model training cutoff alone is insufficient to guarantee absence of leakage. A prospective test should lock questions, observations and scoring rules before outcomes are known.

## Load

```python
from datasets import load_dataset
cards = load_dataset("hyunwookjin/korean-prediction-market-sample", "cards")
ev = load_dataset("hyunwookjin/korean-prediction-market-sample", "forecast_eval")
```

## License and partnership

The public sample remains **CC BY-NC 4.0**, with attribution to **민심마켓 / Minsim Market**. Commercial use requires a separate agreement. Index records, recurring data delivery, requested Korean questions and model-training rights are scoped separately.

**[good-god@minsim.io](mailto:good-god@minsim.io)** · **[minsim.io](https://minsim.io)**

Aggregates only; no individual participant records are included. Outcome labels and resolution rules are supplied by the platform; the original Korean wording remains authoritative when reviewing translations.

## Citation

```bibtex
@dataset{minsim2026prediction,
  title = {Minsim Index -- Korean Human Forecasting: Aggregate Sample},
  author = {Minsim Market},
  year = {2026},
  url = {https://huggingface.co/datasets/hyunwookjin/korean-prediction-market-sample},
  note = {13-card aggregate sample; separate Index strong-signal performance is company-reported as of 2026-07-04. Prediction data, not an opinion poll.}
}
```
