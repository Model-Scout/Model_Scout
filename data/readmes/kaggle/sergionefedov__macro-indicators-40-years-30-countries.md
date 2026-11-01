# Macro Indicators, 40 years, 30 countries

40 years · 30 countries · GDP, inflation, rates, FX → equities, bonds, real esta

# 🌍 Macro Indicators vs Asset Returns (1985–2024)

**40 years · 30 countries · 5 asset classes · 15 macro variables · 5 files**

---

## About

A comprehensive synthetic panel dataset linking macroeconomic indicators to asset class returns across 30 countries (13 developed, 17 emerging markets) from 1985 to 2024.

The simulation is calibrated to real-world statistical properties:
- Country-specific base rates (GDP growth, inflation, interest rates) matching historical averages
- **15 global shock events** encoded (Black Monday, Asian Crisis, GFC, COVID, rate hike cycle)
- Taylor-rule inspired monetary policy responses
- Asset returns driven by macro fundamentals + noise (matching empirical factor sensitivities)

Built for researchers studying **macro investing, factor models, regime analysis, and cross-country comparisons**.

---

## Files

| File | Rows | Description |
|------|------|-------------|
| `macro_indicators.csv` | 1,200 | Annual macro data: 30 countries × 40 years |
| `asset_returns.csv` | 1,200 | Annual returns for 5 asset classes per country |
| `macro_monthly.csv` | 480 | Monthly G7-aggregate series with PMI, VIX, yield curve |
| `correlations.csv` | 2,800 | Rolling 5yr macro×asset correlations, by dev level |
| `recession_episodes.csv` | 74 | Identified recession episodes with macro context |

---

## Countries

**Developed (13):** USA, Canada, UK, Germany, France, Italy, Spain, Netherlands, Sweden, Switzerland, Japan, Australia, South Korea

**Emerging (17):** China, India, Brazil, Mexico, Argentina, Chile, Colombia, Russia, Poland, Turkey, South Africa, Nigeria, Egypt, Saudi Arabia, UAE, Indonesia, Thailand

---

## Macro Variables (`macro_indicators.csv`)

| Column | Description |
|--------|-------------|
| `gdp_growth` | Real GDP growth (%) |
| `gdp_level` | GDP index (1985 = 100) |
| `inflation` | CPI inflation (%) |
| `policy_rate` | Central bank policy rate (%) |
| `unemployment` | Unemployment rate (%) |
| `current_account` | Current account balance (% GDP) |
| `debt_to_gdp` | Government debt (% GDP) |
| `fx_change` | Currency change vs USD (%) |
| `biz_confidence` | Business confidence index (0–100) |
| `fin_stress_idx` | Financial stress index (0 = calm, 3 = crisis) |
| `shock_event` | Named global shock if applicable |

---

## Asset Classes (`asset_returns.csv`)

| Column | Description | Key driver |
|--------|-------------|-----------|
| `equities` | Stock market return (%) | GDP growth, rates, stress |
| `bonds` | Government bond return (%) | Inflation, rate changes |
| `real_estate` | Property return (%) | Rates, GDP |
| `commodities` | Commodity index return (%) | Inflation, EM demand |
| `cash` | T-bill / deposit rate (%) | Policy rate |

---

## Monthly Series (`macro_monthly.csv`)

| Column | Description |
|--------|-------------|
| `gdp_growth_mom` | Monthly GDP growth proxy (%) |
| `cpi_mom` | CPI month-on-month change (%) |
| `cpi_yoy` | CPI year-on-year (%) |
| `policy_rate` | G7 average policy rate (%) |
| `pmi` | Manufacturing PMI (leading indicator) |
| `yield_spread_10_2` | 10yr – 2yr Treasury spread (%) |
| `vix` | Equity volatility index |
| `credit_spread_bps` | IG credit spread (basis points) |
| `oil_change_yoy` | Oil price YoY change (%) |

---

## Global Shock Events Encoded

| Year | Event |
|------|-------|
| 1987 | Black Monday |
| 1997–98 | Asian Financial Crisis / LTCM |
| 2001–02 | Dot-com bust / 9-11 |
| 2008–09 | Global Financial Crisis |
| 2011 | Euro debt crisis |
| 2020 | COVID-19 |
| 2021 | COVID recovery / fiscal stimulus |
| 2022–23 | Inflation shock / rate hike cycle |

---

## Suggested Research Tasks

- **Macro factor model**: Regress asset returns on GDP, inflation, rates — compare DM vs EM
- **Yield curve as recession predictor**: Use `yield_spread_10_2` from monthly data
- **Inflation regime analysis**: How do asset returns differ when CPI > 5%?
- **Carry trade**: Do high-rate countries outperform in FX-adjusted terms?
- **Crisis contagion**: Use `fin_stress_idx` to measure cross-country spillovers
- **Taylor rule calibration**: Fit a Taylor rule to each country's rate path
- **PMI as leading indicator**: Can PMI predict equity returns 1–3 months ahead?
- **Debt sustainability**: Model the relationship between debt/GDP and sovereign risk

---

## Reproducibility

```bash
pip install numpy pandas
python generate_macro.py
```

Seed fixed at `numpy.random.default_rng(42)`.

---

*If this dataset helped your research, an upvote is appreciated!*

출처: Kaggle (sergionefedov/macro-indicators-40-years-30-countries)
태그: finance, banking, economics, insurance, investing
라이선스: MIT
수정일: 2026-04-09T18:10:54.503Z
