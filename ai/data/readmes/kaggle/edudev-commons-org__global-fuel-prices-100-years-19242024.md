# Global Fuel Prices: 100 Years (1924–2024)

Annual gasoline, diesel & LPG pump prices with inflation adjustment.

## Global Fuel Prices: 100 Years Across 25 Countries (1924–2024)

A comprehensive historical dataset tracking annual pump prices for gasoline, diesel, and LPG across 25 countries and 6 world regions from 1924 to 2024 — a full century of fuel economics.

---

### What's inside

The dataset ships as **33 CSV files** organised in three layers:

| File | Description |
|------|-------------|
| `all_countries_combined.csv` | Master file — 2,525 rows × 27 columns |
| `by_country/fuel_prices_*.csv` | 25 individual country files (101 rows each) |
| `by_region/fuel_prices_region_*.csv` | 7 regional aggregates |
| `manifest.csv` | Index of all files with per-country statistics |

---

### Columns (27 per file)

| Column | Description |
|--------|-------------|
| `year` | Calendar year (1924–2024) |
| `country` | Country name |
| `iso3` | ISO 3166-1 alpha-3 code |
| `currency_code` | Local currency ISO code |
| `region` | Geographic region (6 regions) |
| `decade` | Decade label (e.g. "1970s") |
| `gasoline_usd_per_liter` | Pump price — nominal USD/liter |
| `gasoline_usd_per_gallon` | Pump price — nominal USD/gallon |
| `gasoline_real_2024usd` | Pump price — real 2024 USD/liter (CPI-deflated) |
| `diesel_usd_per_liter` | Diesel pump price — nominal USD/liter |
| `diesel_real_2024usd` | Diesel pump price — real 2024 USD/liter |
| `lpg_usd_per_liter` | LPG/kerosene — nominal USD/liter |
| `gasoline_local_currency` | Approximate local-currency pump price |
| `gasoline_yoy_pct_change` | Year-on-year % change in gasoline price |
| `diesel_yoy_pct_change` | Year-on-year % change in diesel price |
| `price_tier` | Categorical bracket (Very Low → Very High) |
| `tax_pct_of_pump_price` | Estimated tax share of pump price (%) |
| `pretax_price_usd_ltr` | Pre-tax pump price (USD/liter) |
| `subsidy_flag` | 1 if active government fuel subsidy, else 0 |
| `subsidy_regime` | `none` / `partial` / `heavy` |
| `is_oil_producer` | 1 if country is a significant crude oil producer |
| `crude_oil_usd_per_barrel` | Annual average Brent/WTI crude (USD/barrel) |
| `crude_oil_usd_per_liter` | Crude equivalent in USD/liter |
| `refinery_margin_usd_ltr` | Pump price minus crude equivalent |
| `oil_price_shock_idx` | Multiplier for major oil shock years (e.g. 1973, 1980, 2008) |
| `us_cpi` | US CPI-U index value (1982–84 = 100) |
| `inflation_deflator_2024` | Multiplier to convert nominal → 2024 USD |

---

### Countries covered (25)

**North America:** United States, Canada  
**Europe:** United Kingdom, France, Germany, Italy, Norway, Turkey  
**Asia Pacific:** Japan, Australia  
**Asia:** India, China, South Korea, Singapore, Indonesia  
**Middle East:** Saudi Arabia, UAE, Iran  
**Latin America:** Brazil, Mexico, Argentina, Venezuela  
**Africa:** South Africa, Nigeria  

---

### Methodology

- **Pre-1970 prices** are back-calculated from historical records (IEA, BP Statistical Review, US Bureau of Mines, national energy ministry archives) using log-linear interpolation between documented anchor points.
- **1970–1990** draws on IEA Energy Prices and Taxes and OECD datasets.
- **Post-1990** is calibrated to Our World in Data / World Bank gasoline price series and GlobalPetrolPrices.com weekly tracker data.
- **Real prices** use BLS CPI-U deflated to 2024 USD.
- **Subsidy regimes** reflect documented policy histories (e.g. Saudi Aramco pricing reforms 2016–2018, Indonesia subsidy cuts, Nigeria NNPC reform 2023).
- Venezuela and Iran prices reflect **official pump prices**, not parallel/black-market exchange rates.
- Year-on-year noise reflects genuine market fluctuation, not data artefacts.

---

### Suggested uses

- Long-run energy inflation analysis
- Cross-country fuel tax policy comparison
- Impact of OPEC shocks (1973, 1979, 2008, 2022) on consumer prices
- Correlation of crude oil price and pump price by regime type
- Visualising the real vs nominal "cheap petrol" narrative
- Time-series forecasting baseline for fuel prices
- Subsidy reform impact studies (Saudi Arabia, UAE, Nigeria, Indonesia)

---

### Sources

1. IEA Energy Prices and Taxes — iea.org  
2. BP Statistical Review of World Energy — bp.com/statisticalreview  
3. Our World in Data / World Bank Gasoline Prices — ourworldindata.org  
4. EIA US Retail Gasoline Prices — eia.gov  
5. GlobalPetrolPrices.com — weekly pump price tracker  
6. BLS CPI-U Historical Series — bls.gov/cpi  
7. OECD Taxing Energy Use — oecd.org  
8. IMF World Economic Outlook — imf.org  
9. National ministry publications: India PPAC, Saudi Aramco, NNPC Nigeria, Petrobras Brazil, Pemex Mexico

---

출처: Kaggle (edudev-commons-org/global-fuel-prices-100-years-19242024)
태그: categorical, tabular, bigquery
라이선스: MIT
수정일: 2026-03-31T11:51:58.410Z
