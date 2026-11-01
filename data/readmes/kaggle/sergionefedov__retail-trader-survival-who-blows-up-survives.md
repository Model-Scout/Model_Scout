# Retail Trader Survival — Who Blows Up, Survives

50,000 traders · 22 features · behaviour vs circumstance split · return  blow-up

# 📉 Retail Trader Survival — Who Blows Up, Who Survives

Most retail traders lose money. That much is well established. The interesting question is *why* — and
which of the reasons are **things a trader controls** versus **the hand they were dealt.** This dataset
separates the two across 50,000 retail traders, each tracked over a roughly two-year window.

**The honest headline: only ~18% finish profitable, ~45% blow up — and the biggest levers are the
ones traders can actually change.**

**50,000 traders · 22 features · behaviour vs circumstance split · return + blow-up targets**

---

## Why this dataset

Search Kaggle for "trading" and you get **price data** — OHLC candles, tickers, order books — for
backtesting *strategies*. What you won't find is data on the *traders themselves*: how they size
positions, how much leverage they run, whether they journal, and whether they survive. That data
exists inside brokers, but it's never published — individual trading records are too sensitive.

This dataset fills that gap. One row per trader, every feature tagged **behaviour** (what you do) or
**circumstance** (what you're handed), with two outcomes: net return and whether the account blew up.

## The numbers it reproduces (from the research)

- **~18% profitable.** Academic studies of day traders net of fees cluster around 20% short-run,
  falling to ~1–3% over five years. FINRA reports ~72% of day traders end the year in the red.
- **The median trader loses.** Median net return here is negative — as it is in every real study.
- **Leverage is a blow-up engine.** Blow-up rate climbs from ~40% at low leverage to ~53% at high.
- **Costs are the silent killer.** Transaction costs alone explain 30–60% of performance dispersion
  in the literature; here they scale with overtrading and leverage and quietly bleed accounts dry.
- **Discipline shifts the odds** — but doesn't guarantee anything. Traders who follow a plan and
  journal are meaningfully more likely to be profitable (~22% vs ~15%), consistent with reports that
  active journalers outperform.

## The headline: behaviour vs. circumstance

Predicting who blows up:

| Features used | ROC-AUC |
|---|---|
| **Behaviour** (leverage, risk per trade, stops, discipline, overtrading) | **0.69** |
| Circumstance (capital, instrument, market regime, broker costs) | 0.56 |
| Both | 0.70 |

The market regime you happened to trade in matters — but what you *do* predicts survival far better.
That's the actionable message, and it's an honest one: the biggest risk factors are self-inflicted.

## Targets

`blew_up` — **1** if the trader lost ≥70% of the account (~45%). `net_return_pct` (continuous) and
`profitable` (binary, ~18%) let you model *degree* of success, not just ruin.

## Quick start

```python
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv("retail_trader_master.csv")
BEHAVIOUR = ["risk_per_trade_pct","avg_leverage","trades_per_month","uses_stop_loss",
             "revenge_trading","overconfidence","follows_plan","position_sizing_discipline",
             "chases_volatility","journals_trades","diversification"]
y = df["blew_up"]
Xtr, Xte, ytr, yte = train_test_split(df[BEHAVIOUR], y, test_size=.25, stratify=y, random_state=0)
m = HistGradientBoostingClassifier().fit(Xtr, ytr)
print("behaviour-only AUC:", roc_auc_score(yte, m.predict_proba(Xte)[:,1]))  # ~0.69
```

## Ideas to explore

- **Behaviour vs circumstance**: reproduce the AUC table. Which half predicts blow-up better?
- Rank the self-inflicted risk factors: leverage, risk-per-trade, overtrading, revenge trading — which
  hurts most?
- Quantify the "silent killer": hold skill fixed and vary `broker_cost_bps` × `trades_per_month`.
- The disposition effect: does holding losers longer than winners (`avg_loss_hold_days` >
  `avg_win_hold_days`) predict ruin?
- Build a "survival score" from pre-trade habits — who should slow down before they blow up?
- Model `net_return_pct` directly: what separates the ~18% who win from the rest?

## Source & methodology

**100% synthetic.** No real trader or account is reproduced. Every row is procedurally generated
(fixed seed). The structure is calibrated to published research on retail-trader performance:

- Profitable share set near the ~20% short-run academic figure (Barber/Odean and others across
  Taiwan, Korea, Brazil), with a negative median return, matching the consistent finding that most
  day traders lose net of fees.
- Transaction costs modeled as a dominant, activity- and leverage-scaled drag, reflecting studies
  attributing 30–60% of performance dispersion to costs.
- Leverage, over-risking per trade, overtrading, revenge trading and overconfidence as ruin drivers;
  stop-loss use, position-sizing discipline, plan-following, journaling and experience as protective —
  in line with behavioural-finance findings.
- Market regime and broker costs as circumstance/luck so outcomes are not deterministic.

These sources informed the *design of the simulator only*; no data from them is reproduced. This is an
educational modeling dataset — **not** trading advice, and not a claim about any real person.

License: CC0 (public domain).

*Useful? An upvote helps others find it — and trade safe.*

출처: Kaggle (sergionefedov/retail-trader-survival-who-blows-up-survives)
태그: finance, banking, economics, investing, currencies and foreign exchange
라이선스: CC0: Public Domain
수정일: 2026-08-24T12:24:17.913Z
