---
license: mit
task_categories:
  - tabular-regression
  - time-series-forecasting
tags:
  - finance
  - stocks
  - quantitative-trading
  - cross-sectional
  - asset-pricing
language:
  - en
  - ko
size_categories:
  - 10M<n<100M
---

# zi-gemini: Cross-Sectional Stock Market Dataset

Quantitative stock market dataset covering **US, KOSPI (KO), and KOSDAQ (KQ)** exchanges. Designed for cross-sectional stock return prediction and portfolio construction research.

## Dataset Summary

| Exchange | Stocks | EOD Rows | Date Range | Features |
|---|---|---|---|---|
| **US** | 24,481 (universe: 1,685) | 26.4M | 2018-01 ~ 2026-05 | 92 |
| **KO** (KOSPI) | 2,401 (universe: 428) | 2.6M | 2018-01 ~ 2026-05 | 92 |
| **KQ** (KOSDAQ) | 1,946 (universe: 587) | 3.5M | 2018-01 ~ 2026-05 | 92 |

**Total: 32.5M EOD rows, 48,828 tickers, 8+ years of daily data.**

## Data Sources

- **EOD prices**: Daily OHLCV with adjusted close (split/dividend adjusted)
- **Fundamentals**: Market cap, valuation ratios, profitability, ownership
- **Earnings**: Historical EPS actual/estimate/surprise, quarterly financials
- **Macro**: FRED (VIX, 10Y yield, DXY, WTI), BOK (KRW, base rate, CPI, bonds), Fama-French 5-factor + momentum
- **Alternative**: News sentiment, analyst ratings, insider transactions, economic events calendar
- **Sector**: KRX official classification (KO/KQ), GICS sectors (US)

## Directory Structure

```
data/
├── KO/                          # KOSPI
│   ├── eod.parquet              # Daily OHLCV (2.6M rows, 53MB)
│   ├── fundamentals.parquet     # Company fundamentals (1,451 stocks)
│   ├── earnings_history.parquet # EPS actual/estimate/surprise (25K rows)
│   ├── quarterly_financials.parquet # Revenue/profit (20K rows)
│   ├── dividends.parquet        # Dividend history (3K rows)
│   ├── krx_sectors.parquet      # KRX official sectors
│   ├── ipos.parquet             # IPO calendar
│   ├── tickers.parquet          # Stock metadata
│   └── universe.parquet         # Investable universe (428 stocks)
│
├── KQ/                          # KOSDAQ (same structure as KO)
│   ├── eod.parquet              # 3.5M rows, 69MB
│   ├── ...
│   ├── news_sentiment.parquet   # News sentiment scores
│   └── sentiment_daily.parquet  # Daily aggregated sentiment
│
├── US/                          # US stocks
│   ├── eod.parquet              # 26.4M rows, 461MB
│   ├── fundamentals.parquet     # 18,983 stocks with 25+ fields
│   ├── earnings_history.parquet # 131K earnings reports
│   ├── quarterly_financials.parquet # 158K quarterly reports (1985~)
│   ├── analyst_ratings.parquet  # Analyst consensus (1.5K stocks)
│   ├── insider_transactions.parquet # Insider buy/sell (15K txns)
│   ├── news_sentiment.parquet   # News sentiment (41K articles)
│   ├── sentiment_daily.parquet  # Daily sentiment (244K rows)
│   ├── dividends.parquet        # Dividend history (28K rows)
│   ├── ipos.parquet             # IPO calendar
│   ├── tickers.parquet          # 24,481 tickers
│   └── universe.parquet         # Investable universe (1,685 stocks)
│
├── macro/                       # Macroeconomic data
│   ├── macro_raw.parquet        # FRED + BOK + Fama-French (36K rows, 1960~)
│   └── economic_events.parquet  # GDP/PMI/CPI events (US/KR/JP/CN)
│
└── features/                    # Pre-computed ML features
    ├── US_features.parquet      # 92 features x 1.2M rows (608MB)
    ├── KO_features.parquet      # 92 features x rows (67MB)
    ├── KQ_features.parquet      # 92 features x rows (124MB)
    ├── US_predictions.parquet   # Walk-forward OOS predictions
    ├── KO_predictions.parquet
    └── KQ_predictions.parquet
```

## Table Schemas

### eod (Daily OHLCV)
| Column | Type | Description |
|---|---|---|
| code | string | Ticker symbol |
| exchange | string | Exchange code (KO/KQ/US) |
| date | date | Trading date |
| open | float | Open price |
| high | float | High price |
| low | float | Low price |
| close | float | Close price |
| adjusted_close | float | Split/dividend adjusted close |
| volume | int | Trading volume |

### fundamentals
| Column | Type | Coverage | Description |
|---|---|---|---|
| market_cap | float | 91% | Market capitalization |
| pe_ratio | float | 47% | Price/Earnings ratio |
| pb_ratio | float | 100% | Price/Book ratio |
| dividend_yield | float | 36% | Dividend yield |
| roe | float | 100% | Return on equity |
| forward_pe | float | 100% | Forward P/E |
| price_sales_ttm | float | 100% | Price/Sales TTM |
| ev_ebitda | float | 100% | EV/EBITDA |
| profit_margin | float | 100% | Net profit margin |
| operating_margin | float | 100% | Operating margin |
| roa | float | 100% | Return on assets |
| peg_ratio | float | 44% | PEG ratio |
| beta | float | 88% | Beta |
| week52_high | float | 100% | 52-week high |
| week52_low | float | 100% | 52-week low |
| shares_float | float | 100% | Shares float |
| pct_insiders | float | 100% | Insider ownership % |
| pct_institutions | float | 100% | Institutional ownership % |
| sector | string | 97% | GICS sector |
| industry | string | 97% | GICS industry |

### features (92 pre-computed features)
Organized into categories:
- **Momentum** (8): ret_5d, ret_20d, ret_60d, ret_120d, kama_ratio, kama_slope, ret_5d_sector_neutral, ret_20d_sector_neutral
- **Volume** (3): volume_ratio_20d, obv_slope_20d, mfi_14
- **Volatility** (4): realized_vol_20d, realized_vol_ratio, atr_ratio, realized_skew_20d
- **Technical** (2): rsi_14, bb_position
- **Fundamental** (12): ep_ratio, bp_ratio, sales_yield, div_yield, roe, debt_to_equity, sales_growth_yoy, forward_ep, ev_ebitda_inv, profit_margin, peg_inv, roa
- **Earnings & Analyst** (7): earnings_surprise, revenue_surprise, analyst_target_upside, analyst_rating_norm, insider_net_flow, news_sentiment_avg, revenue_growth_qoq
- **Sector Momentum** (5): sector_ret_5d, sector_ret_20d, sector_ret_60d, sector_strength, stock_vs_sector
- **AlphaGen RL** (4): ag_delayed_mom_rank, ag_log_volume_60d, ag_open_rank_delta, ag_return_ma_delta
- **Macro** (18): vix, us10y, dxy, wti, usdkrw, bok_rate, cpi, term_spread, credit_spread, Fama-French 5+MOM
- **Interaction** (4): mom_x_value, rsi_x_vol, quality_x_mom, flow_x_value
- **Market breadth** (1): kospi_breadth
- **Target**: target (z-scored 5-day forward return), fwd_ret (raw 5-day forward return)

## Universe Filtering

The `universe` table contains investable stocks filtered by:
- Common Stock only (no ETF/ETN/preferred)
- No SPACs
- Market cap > 20th percentile
- 20-day average dollar volume > $10M (US) / 1B KRW (KO/KQ)
- Listed > 120 trading days

## Model Performance (Walk-Forward OOS)

Using 8-model ensemble (LightGBM, XGBoost, Ridge, MLP, Transformer, TabNet, StockMixer, DoubleAdapt):

| Metric | US |
|---|---|
| Mean IC | 0.019 |
| Sharpe (net) | 1.36 |
| Annual Return (net) | 22.0% |
| Max Drawdown | 8.4% |
| Calmar Ratio | 2.64 |

## Usage

```python
import polars as pl

# Load US EOD data
eod = pl.read_parquet("data/US/eod.parquet")

# Load pre-computed features
features = pl.read_parquet("data/features/US_features.parquet")

# Load fundamentals
fund = pl.read_parquet("data/US/fundamentals.parquet")

# Load macro data
macro = pl.read_parquet("data/macro/macro_raw.parquet")
```

## Updates

Data is updated daily. Last update: 2026-05-30.

## License

MIT
