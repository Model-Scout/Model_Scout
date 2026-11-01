# Global Corporate GHG Emissions 2022–2023

508 companies · 46 countries · Scope 1, 2 & 3 · Net-Zero targets included

## 🌍 Global Corporate GHG Emissions 2022–2023

This dataset provides greenhouse gas (GHG) emission records for **508 major 
corporations** across **46 countries** and **6 global regions** — covering 
Africa, Asia-Pacific, Europe, Latin America, the Middle East, and North America.

---

### 📊 What's Inside

| Feature | Detail |
|---|---|
| Companies | 508 global corporations |
| Countries | 46 |
| Sectors | 12 (Energy, Materials, Utilities, Transport & more) |
| Reporting Years | 2021, 2022, 2023 |
| Emission Scopes | Scope 1, Scope 2 (location & market), Scope 3 |
| Verification | 76% third-party verified |
| Net-Zero Targets | Available for 452 companies |

---

### 🗂️ Columns

- `company_id` — Unique identifier
- `company_name` / `ticker` — Company name and stock ticker
- `country` / `region` — Geographic info
- `sector` / `industry` — GICS-aligned classification
- `reporting_year` — Year of emissions report
- `scope1_mt_co2e` — Direct emissions (MT CO₂e)
- `scope2_location_mt_co2e` / `scope2_market_mt_co2e` — Indirect energy emissions
- `scope3_total_mt_co2e` — Value chain emissions
- `scope1_plus_scope2_location_mt` — Combined Scope 1+2
- `emissions_intensity_mt_per_musd` — Emissions per million USD revenue
- `revenue_usd_millions` — Annual revenue
- `reporting_standard` — e.g., GHG Protocol
- `data_source` — CDP, EPA GHGRP, national registries, sustainability reports
- `third_party_verified` — Boolean verification flag
- `net_zero_target_year` — Declared net-zero year (if any)
- `notes` — Contextual flags (e.g., coal-dominant, state-owned)

---

### 🔍 Potential Use Cases

- **ESG benchmarking** — Compare emissions intensity across sectors and regions
- **Net-zero analysis** — Track corporate climate commitments vs. actual emissions
- **Sector-level decarbonization** — Identify highest-emitting industries
- **Policy research** — Correlate reporting standards with emission levels
- **ML modeling** — Predict emissions trends or classify high-emitters

---

### 📁 Data Sources

Data compiled from CDP disclosures, EPA GHGRP, national registries 
(NGER, Japan MOE, China ETS, Korea GHG Inventory), and corporate 
sustainability reports — all normalized to the GHG Protocol standard.

---

### ⚠️ Notes

- Some Scope 2 and Scope 3 values are missing where companies did not disclose
- State-owned enterprises (especially in China) use estimates from national registries
- All emissions are in **metric tonnes of CO₂ equivalent (MT CO₂e)**

출처: Kaggle (alitaqishah/global-corporate-ghg-emissions-20222023)
태그: global, weather and climate, exploratory data analysis, time series analysis, data storytelling
라이선스: CC0: Public Domain
수정일: 2026-04-13T18:49:30.923Z
