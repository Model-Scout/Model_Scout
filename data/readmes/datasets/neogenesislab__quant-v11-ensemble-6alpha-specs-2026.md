---
language:
- ko
- en
license: cc-by-4.0
task_categories:
- text-generation
- text-classification
tags:
- quantitative-finance
- algorithmic-trading
- cryptocurrency
- perpetual-futures
- binance
- ensemble-strategy
- liquidation-cascade
- mean-reversion
- ornstein-uhlenbeck
- funding-rate-arbitrage
- basis-harvest
- market-making
- risk-management
- kill-switch
- kelly-criterion
- deflated-sharpe-ratio
- nautilus-trader
- hftbacktest
- paper-trading
- systems-engineering
- bilingual
- korean
- english
- neo-genesis
- wikidata-Q139569680
- yesol-heo-founder
- ko
- en
- trading
- alpha-research
- ensemble
- binance-futures
size_categories:
- n<1K
pretty_name: Quant v11 Ensemble 6-Alpha Specs & Risk Engineering 2026
configs:
- config_name: default
  data_files:
  - split: train
    path: data/sections.parquet
multilinguality: multilingual
annotations_creators:
- expert-generated
- machine-generated
source_datasets:
- original
---

## DOI

[![DOI](https://zenodo.org/badge/doi/10.5281%2Fzenodo.20018487.svg)](https://doi.org/10.5281/zenodo.20018487)

This dataset is citable via DataCite DOI **`10.5281/zenodo.20018487`** ([Zenodo record](https://zenodo.org/record/20018487)).

**Cite as:**

```bibtex
@dataset{neogenesis_20018487,
  author       = {Heo, Yesol and Neo Genesis Lab},
  title        = {Quant v11 Ensemble 6-Alpha Specs & Risk Engineering 2026},
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20018487},
  url          = {https://doi.org/10.5281/zenodo.20018487}
}
```

# Quant v11 Ensemble - 6-Alpha Specs & Risk Engineering 2026

> **A reference systems-engineering corpus for a 6-alpha cryptocurrency perpetual futures ensemble bot.** 375 parsed sections from 19 canonical source files: **67 design, 46 risk-layer, 115 alpha-spec, 71 expert-report, 42 research, 34 roadmap** sections.

Released by **[Neo Genesis](https://neogenesis.app)** ([Wikidata Q139569680](https://www.wikidata.org/wiki/Q139569680)).

## Educational disclaimer (read first)

- **Not investment advice.** This dataset is published for research and engineering education.
- **PAPER mode.** The reference v11 ensemble runs in PAPER mode (no live capital) until a **14-day Sharpe >= 1.2 + Deflated Sharpe Ratio >= 0.5** gate clears on at least one alpha.
- **Edge decay.** Quant alpha edges decay from the moment they are documented publicly. Anything in this corpus must be re-validated by the reader against fresh data, real fees, real slippage, and real funding before any capital is risked.
- **Survivorship + lookahead.** v6-v10 of this same bot produced "127k wins / 0 losses" backtests that turned into a -<illustrative-loss> drain on 5 days of live trading. The v11 redesign exists *because* the old backtests were wrong. Treat any backtest, including the ones implied here, with that history in mind.

## Why this dataset is unique

Public quant ML / RL datasets (price candles, order books, returns) are common. Full **systems-engineering specs** of a working multi-alpha derivatives bot - alphas + risk + experts + research + roadmap as one coherent system - are rare publicly. What is in here that you usually have to reconstruct yourself:

1. **6 low-correlation alpha specifications** (A1..A6) with theory background, entry/exit logic, paper-mode KPIs, expected daily contribution, and stop-go criteria.
2. **9-layer kill switch** (Layer 1 = per-position SL, ..., Layer 9 = funding-spike guard) with explicit thresholds, not slogans.
3. **6 cross-discipline expert validation reports** - math boundary (Kelly + ruin probability), HFT / market-making, statistical arbitrage, risk survival, ML / RL, event alpha. Each report cross-checks the alphas independently.
4. **External benchmark research** (2026-04-24) on what public benchmarks exist for liquidation-cascade alphas, OU-mean-reversion, funding arbitrage, and the absence of public benchmarks for several of these.
5. **Backtest engine decision** - why the v11 ensemble picks `nautilus_trader` (primary) + `hftbacktest` (microstructure-sensitive A1 / A6) + `vectorbt pro` (cross-validation), with the 8 anti-patterns the v6-v10 backtests fell into.

This is a *real* design used by a single-operator quant stack (operator publicly attested via [Wikidata Q139569708](https://www.wikidata.org/wiki/Q139569708)). It is not a paper proposal.

## Dataset summary

- **375 sections** in `data/sections.jsonl`. Each row is one parsed heading-section.
- **19 source files** indexed in `data/source_index.json`:
  - **Design** (67 sections): `MASTER_DESIGN.md`, `INDEX.md`, `CURRENT_CODE_AUDIT.md`, `backtest-v2-engine-decision.md`.
  - **Risk layers** (46 sections): `RISK_KILLSWITCH.md` - 9-layer defense.
  - **Alpha specs** (115 sections): A1 Liquidation Cascade, A2 Mean Reversion OU, A3 Extreme Funding, A4 Macro Event, A5 Funding / Basis Harvest, A6 Alt Market-Making.
  - **Expert reports** (71 sections): math boundary, HFT / MM, stat arb, risk survival, ML / RL, event alpha.
  - **Research** (42 sections): external benchmark validation 2026-04-24.
  - **Roadmap** (34 sections): Phase -1 / 0 / 1 progression.

## Schema

`data/sections.jsonl` - one JSON record per line:

| column | type | description |
|---|---|---|
| `doc_id` | string | `master-design / kill-switch / roadmap / alpha-A1..A6 / expert-01..06 / research-validation / backtest-decision / index / current-code-audit` |
| `doc_type` | string | `design \| risk_layer \| alpha_spec \| expert_report \| research \| roadmap` |
| `version` | string | semantic version of the source doc |
| `section_id` | string | slugified heading hierarchy (`<doc_id>/<h1>/<h2>/...`) |
| `section_title` | string | heading title |
| `section_text` | string | actual section body content |
| `alpha_id` | string\|null | `A1 \| A2 \| A3 \| A4 \| A5 \| A6` for alpha-spec rows, `null` otherwise |
| `kill_switch_layer` | int\|null | `1..9` for risk-layer rows when an explicit layer is mentioned |
| `references` | string | JSON array of inline links / file paths |

## Quick start

```python
from datasets import load_dataset

ds = load_dataset("neogenesislab/quant-v11-ensemble-6alpha-specs-2026", "sections", split="train")
print(len(ds), "sections")

# Get all alpha specs
alphas = ds.filter(lambda r: r["doc_type"] == "alpha_spec")
print(f"{len(alphas)} alpha-spec sections")

# Filter to one specific alpha (A1 Liquidation Cascade)
a1 = ds.filter(lambda r: r["alpha_id"] == "A1")
for row in a1:
    print(row["section_title"])

# Get all risk-layer sections that reference Layer 3 (correlation killer)
l3 = ds.filter(
    lambda r: r["doc_type"] == "risk_layer" and r["kill_switch_layer"] == 3
)

# Get all expert reports
experts = ds.filter(lambda r: r["doc_type"] == "expert_report")
```

## Suggested research applications

1. **Multi-alpha ensemble design** - train portfolio allocators or meta-classifiers to gate alpha activation under regime conditions.
2. **Kill-switch reasoning** - supervise classifiers that decide when to halt trading based on correlation, drawdown, fee burn, or stablecoin depeg signals.
3. **Backtest anti-pattern detection** - the `backtest-decision` doc enumerates 8 specific anti-patterns (lookahead bias, survivorship, fill-model bugs, missing funding, missing slippage, etc.) - useful as supervision for backtest auditors.
4. **Cross-discipline alpha review** - 6 expert reports give you parallel views of the same 6 alphas. Useful as a small benchmark for "do LLM critics agree with domain experts."
5. **Single-operator quant ops** - rare reference for what one person actually has to specify (alphas + risk + telemetry + roadmap + experts) to ship a derivatives bot honestly.

## Operating status

- **Mode**: PAPER (no live capital deployed)
- **Graduation gate**: 14-day Sharpe >= 1.2 AND Deflated Sharpe Ratio >= 0.5 on the active alpha
- **Max leverage hard cap**: 5x (Kelly/3 safety factor)
- **Safety layers**: 9 (per-position SL, daily/weekly/monthly DD, correlation killer, fee-budget freeze, halt persistence, order-rate cap, stablecoin depeg guard, funding-spike guard)

## Anonymization

| Class | Treatment |
|---|---|
| Internal hostnames | Redacted to `<work-pc>`, `<gpu-worker>`, `<server>`, `<mac-build>`, `<work-user>` |
| GCP VM identifiers | Redacted to `<gcp-vm>`, `<gcp-project>`, `<vm-ip>` |
| Owner email / phone | Redacted to `<redacted-email>` / `<redacted-phone>` |
| Korean RRN | Redacted to `<redacted-rrn>` |
| API tokens (Binance keys, `sk-*`, `ghp_*`, `hf_*`, JWT, bot tokens) | Redacted to `<redacted-*>` |
| Wallet addresses (`0x...`) | Redacted to `<redacted-wallet>` |
| Absolute Windows paths | Redacted to `<repo>` / `<workspace>` / `<home>` |
| Tailscale / private IPs | Redacted to `<tailscale-ip>` / `<private-ip>` |
| Specific capital amounts beyond illustrative ranges | Redacted to `<illustrative-loss>` / `<illustrative-balance>` |

Each emitted string is re-tested with all redaction regexes; publish aborts on leak.

## Provenance

- **Source**: Neo Genesis private SSOT (`auto-trading/docs/v11-ensemble/*`).
- **Curator**: Neo Genesis Lab (`neogenesislab` HuggingFace org).
- **Wikidata**: [Q139569680 (Neo Genesis)](https://www.wikidata.org/wiki/Q139569680), [Q139569708 (Yesol Heo, founder)](https://www.wikidata.org/wiki/Q139569708).
- **Related releases by the same operator**:
  - [`korean-rag-ssot-golden-50`](https://huggingface.co/datasets/neogenesislab/korean-rag-ssot-golden-50)
  - [`ethicaai-mixed-safe-evidence`](https://huggingface.co/datasets/neogenesislab/ethicaai-mixed-safe-evidence)
  - [`whylab-gemini-2-5-docker-validation`](https://huggingface.co/datasets/neogenesislab/whylab-gemini-2-5-docker-validation)
  - [`sbu-pseo-effects-2026-04`](https://huggingface.co/datasets/neogenesislab/sbu-pseo-effects-2026-04)
  - [`cross-agent-review-queue-2026`](https://huggingface.co/datasets/neogenesislab/cross-agent-review-queue-2026)
  - [`korean-llm-citation-baseline-2026`](https://huggingface.co/datasets/neogenesislab/korean-llm-citation-baseline-2026)
  - [`sora-multi-device-orchestration-2026`](https://huggingface.co/datasets/neogenesislab/sora-multi-device-orchestration-2026)

## Citation

```bibtex
@misc{neogenesis_quant_v11_2026,
  title  = {Quant v11 Ensemble 6-Alpha Specs and Risk Engineering 2026: A reference systems-engineering corpus for a multi-alpha cryptocurrency perpetual futures bot},
  author = {Neo Genesis Lab},
  year   = {2026},
  url    = {https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026},
  note   = {6 alphas, 9-layer kill switch, 6 expert validations, external benchmark research; published in PAPER mode pending 14-day Sharpe >= 1.2 + DSR >= 0.5 graduation gate}
}
```

## License

CC-BY-4.0 - free for research and commercial use with attribution to Neo Genesis Lab.

---

## 한국어 요약

**Quant v11 Ensemble 6-Alpha Specs & Risk Engineering 2026** 은 Binance 선물에서 일 평균 0.6~1.0% 누적 수익률을 목표로 하는 **6-알파 앙상블 봇의 시스템 엔지니어링 SSOT** 코퍼스다.

### 교육용 면책 (먼저 읽기)
- **투자 자문 아님.** 본 데이터셋은 연구 / 엔지니어링 교육 목적으로 공개된다.
- **PAPER 모드.** 본 v11 reference 앙상블은 **14일 Sharpe >= 1.2 + Deflated Sharpe Ratio >= 0.5** 게이트를 통과할 때까지 PAPER 모드에서만 운영된다 (실자본 0).
- **알파 감쇠.** 퀀트 알파 edge 는 공개 시점부터 감쇠한다. 본 코퍼스의 어떤 내용도 독자가 자신의 데이터 / 수수료 / 슬리피지 / funding 가정으로 재검증하지 않으면 그대로 사용해서는 안 된다.
- **생존편향 + 룩어헤드.** 동일 봇의 v6-v10 은 "127k 승 / 0 패" 백테스트를 만들어 냈고 라이브에서 5일 만에 -<illustrative-loss> 드레인이 발생했다. v11 의 존재 자체가 옛 백테스트가 틀렸기 때문이다. 본 코퍼스가 암시하는 어떤 백테스트도 그 이력 하에서 읽어야 한다.

### 다루는 것
- **6개 저상관 알파 스펙** (A1 Liquidation Cascade, A2 Mean Reversion OU, A3 Extreme Funding, A4 Macro Event, A5 Funding / Basis Harvest, A6 Alt Market-Making) - 이론 / 진입출구 / 페이퍼 KPI / 일일 기여 / stop-go 기준.
- **9-Layer Kill Switch** - L1 포지션 SL, ..., L9 funding-spike guard. 슬로건이 아니라 임계값으로.
- **6명 전문가 교차 검증** - 수학 (Kelly + 파산확률), HFT / MM, 통계차익, 리스크 생존, ML / RL, 이벤트 알파.
- **외부 벤치마크 리서치** - liquidation-cascade / OU / funding arb 의 공개 벤치마크 부재 공식화.
- **백테스트 엔진 결정** - nautilus_trader 메인 + hftbacktest 보조 + vectorbt 검증, v6-v10 백테스트의 8 anti-pattern.

### 익명화
디바이스 hostname / 이메일 / 전화 / RRN / API 토큰 / 지갑 주소 / 절대경로 / private IP / 구체적 자본 금액 모두 redaction. 발행 직전 모든 문자열을 redaction regex 로 재검증.

라이선스 CC-BY-4.0 - 인용 시 자유롭게 사용 가능.

## Citation

```bibtex
@dataset{neogenesislab_quant_v11_ensemble_6alpha_specs_2026_2026,
  author       = {Yesol Heo and Neo Genesis Lab},
  title        = {Quant v11 Ensemble 6-Alpha Specifications 2026},
  year         = 2026,
  publisher    = {Hugging Face},
  url          = {https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026},
  note         = {Wikidata Q139569680, Q139569708; license CC-BY-4.0}
}
```

## Citation File Format

GitHub, Zenodo, and other tooling can read the following CFF block to provide one-click citation export (BibTeX, APA, RIS, etc.). The [CFF specification](https://citation-file-format.github.io/) is v1.2.0.

```yaml
cff-version: 1.2.0
message: "If you use this dataset, please cite it as below."
title: "Quant v11 Ensemble 6-Alpha Specs & Risk Engineering 2026"
type: dataset
authors:
  - family-names: "Heo"
    given-names: "Yesol"
    affiliation: "Neo Genesis Lab"
date-released: "2026-05-03"
license: CC-BY-4.0
url: "https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026"
repository: "https://huggingface.co/datasets/neogenesislab/quant-v11-ensemble-6alpha-specs-2026"
identifiers:
  - type: doi
    value: "10.5281/zenodo.20018487"
    description: "Zenodo DataCite DOI for this dataset"
  - type: other
    value: "Q139569680"
    description: "Wikidata Q-ID of the publishing organization (Neo Genesis)"
keywords:
  - quantitative-trading
  - kill-switch
  - ensemble
  - liquidation-cascade
  - funding-rate
  - mean-reversion
  - binance
  - neo-genesis
  - risk-engineering
preferred-citation:
  type: dataset
  title: "Quant v11 Ensemble 6-Alpha Specs & Risk Engineering 2026"
  authors:
    - family-names: "Heo"
      given-names: "Yesol"
      affiliation: "Neo Genesis Lab"
  doi: "10.5281/zenodo.20018487"
  year: 2026
  publisher:
    name: "Zenodo"
  url: "https://doi.org/10.5281/zenodo.20018487"
```
