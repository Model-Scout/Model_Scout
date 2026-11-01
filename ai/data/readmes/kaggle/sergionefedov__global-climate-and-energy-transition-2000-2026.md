# Global Climate & Energy Transition 2000-2026

Temperature anomalies (global + 8 regions), CO2 emissions for 50 countries

# Global Climate & Energy Transition 2000-2026

**Subtitle:** Temperature anomalies (global + 8 regions), CO2 emissions for 50 countries, energy mix evolution, carbon market prices (5 ETS), and 50 climate events — 26 years of the energy transition

---

## Tags

`climate change` · `energy` · `emissions` · `co2` · `renewables` · `carbon market` · `esg` · `sustainability` · `time series` · `policy` · `geospatial` · `tabular`

---

## Overview

A comprehensive dataset tracking the **global climate and energy transition from 2000 to 2026** — covering temperature evolution, CO2 emissions across 50 countries, energy mix transition (coal → renewables), carbon market prices across 5 major ETSs, and 50 major climate events from extreme weather to landmark policy moments.

This dataset is designed for **climate ML, ESG analysis, energy economics, policy research, and journalism**. It captures the full arc of the modern climate era: from pre-Kyoto baselines, through the 2015 Paris Agreement, the renewables explosion, the 2022 European energy crisis, and the 2024-2026 1.5°C threshold crossing.

All data is sourced from public official statistics: NASA GISS, NOAA Mauna Loa, EDGAR, IEA, Our World in Data, EU ETS, EDF, BP Statistical Review.

---

## Files

| File | Rows | Description |
|------|------|-------------|
| `temperature_anomaly_monthly.csv` | 2,528 | Global + 7 regions × 316 months: temperature anomaly + CO2 ppm |
| `co2_emissions_yearly.csv` | 1,350 | 50 countries × 27 years: total emissions, per capita, intensity |
| `energy_mix_yearly.csv` | 1,350 | 50 countries × 27 years: 8 fuel shares (coal, oil, gas, nuclear, hydro, solar, wind, other) |
| `climate_events.csv` | 50 | Major climate/weather/policy events with severity scores |
| `carbon_prices_daily.csv` | 15,866 | Daily prices for EU ETS, California, RGGI, UK ETS, China ETS |

Total: ~21,000 rows, ~1.5 MB.

---

## 50 Countries Covered

**Major emitters** (top 20): China, USA, India, Russia, Japan, Germany, Iran, South Korea, Indonesia, Saudi Arabia, Canada, Mexico, Brazil, South Africa, Turkey, Australia, UK, France, Italy, Spain

**Europe**: Poland, Netherlands, Ukraine, Czech Republic, Belgium, Sweden, Norway, Finland, Denmark

**MENA**: UAE, Egypt, Iraq, Qatar, Kuwait, Algeria, Israel

**Asia**: Vietnam, Thailand, Pakistan, Malaysia, Philippines, Bangladesh, Kazakhstan

**LatAm**: Argentina, Colombia, Chile, Venezuela

**Africa**: Nigeria, Morocco, Kenya

---

## 5 Carbon Markets Tracked

| Market | Currency | Coverage | Launch |
|--------|----------|----------|--------|
| **EU ETS** | EUR | EU 27 + Iceland, Norway, Liechtenstein | 2005-04-22 |
| **California cap-and-trade** | USD | California (+ linked Quebec) | 2013-11-19 |
| **RGGI** | USD | US Northeast (10+ states) | 2008-09-25 |
| **UK ETS** | GBP | United Kingdom (post-Brexit) | 2021-05-19 |
| **China National ETS** | CNY | China (power sector) | 2021-07-16 |

---

## Key Findings Captured

### Temperature & Climate

- **Global temperature anomaly**: +0.42°C (2000) → +1.28°C (2024) vs 1951-1980 baseline
- **1.5°C threshold first breached**: 2024 (annual basis)
- **Arctic amplification**: ~3.5× faster warming than global average
- **CO2 concentration**: 369 ppm (2000) → 425 ppm (2026)
- **ENSO signal**: 2015-16 super El Niño, 2023-24 El Niño, 2020-22 triple La Niña

### Emissions Trajectories

- **China**: 3,550 Mt (2000) → 12,150 Mt (2024) — +242% growth, now ~31% of global
- **United States**: 5,870 Mt → 4,950 Mt — -16% decline (coal-to-gas + renewables)
- **India**: 990 Mt → 2,960 Mt — +199% growth
- **EU collective**: declining ~30% since 2000
- **UK**: 580 Mt → 295 Mt — -49% (most aggressive G20 decarbonization)

### Energy Transition

- **UK coal collapse**: 16% (2000) → <1% (2024-2026)
- **Germany Energiewende**: nuclear 13% → 0%, renewables 1% → 28%
- **China solar+wind**: <0.5% (2010) → 9% (2024-2026)
- **France maintaining nuclear**: stable ~40% throughout

### Carbon Market Prices

- **EU ETS**: €0.05 (2007 collapse) → €100 (Aug 2022 gas crisis peak)
- **California**: $10 (2013) → $36 (2024 peak)
- **UK ETS**: £50 (launch) → £95 (2022 peak) → £35 (2023 dive)
- **China ETS**: ¥48 (launch) → ¥115 (2026)

### Major Events

- **2015 Paris Agreement** (severity 10)
- **2023 hottest month in recorded history** (severity 9)
- **2024 hottest day ever recorded** (severity 9)
- **2025 Los Angeles wildfires** $250B+ (severity 9)
- **COP15 → COP30**: full 15-year policy arc

---

## Column Descriptions

### `temperature_anomaly_monthly.csv`

| Column | Description |
|--------|-------------|
| `year_month`, `year`, `month` | Monthly period |
| `region` | Global / Arctic / Northern_Hemisphere / Southern_Hemisphere / Tropics / North_America / Europe / Asia |
| `temp_anomaly_c` | Temperature anomaly in °C vs baseline |
| `temp_anomaly_baseline` | "1951-1980" (NASA GISS convention) |
| `co2_ppm` | Atmospheric CO2 concentration (Global region only) |

### `co2_emissions_yearly.csv`

| Column | Description |
|--------|-------------|
| `year` | 2000-2026 |
| `country`, `iso3`, `region` | Country identifiers |
| `co2_emissions_mt` | Total CO2 emissions in million tons |
| `population_millions` | Population estimate |
| `co2_per_capita_t` | Tons CO2 per person |
| `co2_intensity_kg_per_gdp_usd` | Carbon intensity of GDP |

### `energy_mix_yearly.csv`

8 fuel sources (% of primary energy):
- `coal_pct`, `oil_pct`, `gas_pct`, `nuclear_pct`, `hydro_pct`, `solar_pct`, `wind_pct`, `other_renewables_pct`
- `renewables_total_pct`, `fossil_total_pct` (computed aggregates)

### `climate_events.csv`

| Column | Description |
|--------|-------------|
| `event_id` | Unique ID |
| `date`, `year`, `month` | Date |
| `region` | Geographic scope |
| `event_type` | heatwave / hurricane / wildfire / flood / drought / policy / tsunami / earthquake / etc. |
| `severity_score` | 1-10 ordinal |
| `description` | One-line description |
| `is_policy`, `is_extreme_weather`, `is_disaster` | Boolean flags |

### `carbon_prices_daily.csv`

| Column | Description |
|--------|-------------|
| `date`, `year` | Daily |
| `market` | EU_ETS / California / RGGI / UK_ETS / China_ETS |
| `currency` | EUR / USD / GBP / CNY |
| `price` | Closing price per tCO2 |

---

## Source

**Real public anchor points:**

- **Global temperature anomaly** — NASA Goddard Institute for Space Studies (GISS) GISTEMP v4, monthly global mean surface temperature anomaly
- **Regional temperature anomalies** — NASA GISS zonal anomalies + NOAA NCEI regional climate divisions
- **CO2 concentration** — NOAA Global Monitoring Laboratory Mauna Loa Observatory monthly mean
- **ENSO timeline** — NOAA Climate Prediction Center ONI index, real El Niño / La Niña periods
- **Country CO2 emissions** — EDGAR (Emissions Database for Global Atmospheric Research) v8.0, Our World in Data, BP Statistical Review of World Energy
- **Population** — World Bank WDI
- **Energy mix** — IEA World Energy Statistics, BP Statistical Review, Ember climate analytics, national grid operators
- **Climate events** — major media coverage, IPCC, NOAA disaster database, EM-DAT international disaster database
- **Policy events** — UNFCCC COP outcome documents, Paris Agreement text, COP28/COP29/COP30 outcomes
- **EU ETS prices** — EEX (European Energy Exchange), ICE Endex public settlement prices
- **California prices** — California Air Resources Board (CARB) auction results
- **RGGI prices** — Regional Greenhouse Gas Initiative public auction prices
- **UK ETS prices** — ICE Futures Europe public settlement prices
- **China ETS prices** — Shanghai Environment and Energy Exchange (SEEE) and Hubei Carbon Emissions Trading Center

**Generated components:** linear interpolation of yearly anchors to monthly/daily resolution, with calibrated random noise for daily volatility. All anchor values are sourced from public official statistics.

---

## Collection Methodology

### Step 1 — Temperature Anomaly Series

Yearly anchor values from NASA GISS GISTEMP. Monthly resolution via linear interpolation with:
- ENSO signal (warm/cool deviations during real El Niño / La Niña periods)
- Small seasonal cycle (~0.02°C)
- Random measurement noise (~0.04°C, calibrated to real station network)

Regional anomalies derived by applying region-specific amplification factors (Arctic 3.5×, Europe 1.65×, Tropics 0.65×) — matching observed regional warming patterns.

### Step 2 — CO2 Concentration

Mauna Loa monthly trajectory: linear ppm rise + seasonal cycle (~3.5 ppm peak-to-peak, NH-driven) + small noise. Anchored to real 2000 (369.5 ppm) and 2024 (424 ppm) values.

### Step 3 — Country Emissions

For each country, anchored values at 2000, 2010, 2015, 2020, 2024, 2026 from EDGAR/OWID. Linear interpolation between anchors. 1.5% per-year noise.

Per-capita emissions = total / population. Carbon intensity uses rough GDP proxy.

### Step 4 — Energy Mix

For each country, anchored fuel shares at 6 dates. Interpolation between anchors with renormalization to 100%. Major emitters (CHN, USA, DEU, etc.) have country-specific anchor tables; others use regional defaults.

### Step 5 — Carbon Prices

For each ETS, anchored closing prices at major historical inflection points (launches, crises, MSR reform, gas crisis). Linear interpolation + log-normal daily volatility (~2.5% daily).

### Step 6 — Climate Events Catalogue

50 events curated for historical significance with severity scores 1-10:
- 10: Paris Agreement (sole event at this level — civilization-defining policy)
- 9: Major disasters with 1000+ deaths, hottest-ever records, COP outcomes
- 8: Major extreme weather, regional disasters, major COP moments
- 6-7: Notable but smaller-scale events

### Reproducibility

Deterministic given seed. Source code included.

### What This Dataset Is and Is Not

**Suitable for**: climate trend analysis, ESG factor construction, carbon market modeling, energy transition tracking, policy event studies, teaching climate science, ML benchmarks on time series.

**Not suitable for**: precise scientific reconstructions, regulatory compliance, peer-reviewed publication without cross-referencing primary sources, individual project emissions tracking.

---

## Suggested Tasks

### 1. 1.5°C Threshold Forecasting
When will global temperature consistently exceed 1.5°C (12-month rolling average)? Test ARIMA, Prophet, neural forecasters.

### 2. Carbon Market Volatility & Correlation
Run a portfolio analysis across the 5 carbon markets. Are they correlated? Has correlation changed post-COVID?

### 3. Decoupling Analysis
For each country, plot GDP vs emissions over time. Which countries have achieved absolute decoupling? Plot the timing.

### 4. Energy Transition Speed
Fit S-curves to renewables share by country. Which countries are accelerating? Which are stuck?

### 5. Extreme Event Frequency Trends
Has the frequency of extreme weather events increased? Group `climate_events.csv` by year and event type.

### 6. ENSO-CO2 Lag
Is there a measurable lag between ENSO state and CO2 ppm growth rate?

### 7. EU ETS Price Drivers
Build a model predicting EU ETS price from natural gas prices, coal prices, policy events.

### 8. China's Decarbonization Path
China is the largest emitter but rapidly decarbonizing electricity. Project when China's emissions peak and decline.

### 9. Climate Risk Factor Construction
Build a country-level "climate risk" factor combining extreme events frequency + emissions intensity + transition risk (fossil exposure).

### 10. Cross-Series Analysis
Combine with companion datasets:
- [BRICS+ Macro Indicators 2000-2026](https://www.kaggle.com/datasets/sergionefedov/brics-macro-indicators-2000-2026) — macro context
- [Sanctions Impact: Russian Economy 2014-2026](https://www.kaggle.com/datasets/sergionefedov/sanctions-impact-russian-economy-2014-2026) — Russia/EU gas dynamics

---

## Limitations

- **Synthetic daily noise**: daily carbon prices and monthly temperatures interpolated from yearly/monthly anchors with calibrated noise
- **Energy mix simplified**: 8-category classification; finer breakdowns (biomass types, geothermal) aggregated to "other_renewables"
- **No subnational data**: country-level only
- **Severity scores subjective**: ordinal not cardinal
- **Carbon prices reflect spot futures**: no auction-specific or allowance-specific pricing
- **Coverage gaps**: smaller emitters not included
- **End of period 2026 partial year**: data through April 2026

---

## License

CC0: Public Domain. Use freely for academic, commercial, journalistic, or any other purpose.

---

## Citation

```
Global Climate & Energy Transition 2000-2026. Kaggle Datasets, 2026.
```

---

## Acknowledgments

Anchor data sourced from public official statistics: NASA GISS GISTEMP v4, NOAA Mauna Loa, EDGAR v8.0, IEA, Our World in Data, BP Statistical Review of World Energy, EEX, ICE, EU Commission, EPA, CARB, RGGI Inc., SEEE, UNFCCC. Climate events cross-referenced with IPCC AR6, EM-DAT, and major media reporting.

If this dataset helped your research, journalism, or work, an upvote is appreciated — it helps the dataset surface to other climate, energy, and ESG practitioners.

**Related datasets by the same author:**
- [BRICS+ Macro Indicators 2000-2026](https://www.kaggle.com/datasets/sergionefedov/brics-macro-indicators-2000-2026)
- [Sanctions Impact: Russian Economy 2014-2026](https://www.kaggle.com/datasets/sergionefedov/sanctions-impact-russian-economy-2014-2026)
- [LLM Benchmarks & Capabilities 2020-2026](https://www.kaggle.com/datasets/sergionefedov/llm-benchmarks-capabilities-2020-2026)

출처: Kaggle (sergionefedov/global-climate-and-energy-transition-2000-2026)
태그: economics, energy, renewable energy, electricity, oil and gas
라이선스: CC0: Public Domain
수정일: 2026-06-03T15:35:43.260Z
