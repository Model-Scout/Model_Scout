# Global Aviation Industry 2010-2026

30 airlines × 17 years financials, Boeing vs Airbus order book

# Global Aviation Industry 2010-2026

**Subtitle:** 30 airlines × 17 years financials, Boeing vs Airbus order book, regional passenger traffic, 40 top routes, and 40 major aviation incidents — covering the 737 MAX crisis, COVID devastation, Saudi aviation push, and 2024-2025 Boeing crisis

---

## Tags

`aviation` · `airlines` · `boeing` · `airbus` · `transportation` · `tourism` · `aerospace` · `time series` · `economics` · `tabular`

---

## Overview

A comprehensive dataset tracking the **global aviation industry from 2010 to 2026** — covering Boeing's 737 MAX crisis ($150B+ market cap loss), Airbus's market share gain, COMAC C919 emergence, COVID's -86% Asia Pacific traffic collapse, the post-pandemic recovery, Saudi Arabia's aviation mega-projects (Riyadh Air), and the 2024-2025 Boeing crisis (Alaska 1282 door plug, FAA cap on production).

This dataset is designed for **aviation analysts, equity analysts (airline/aerospace sector), travel industry researchers, transportation policy researchers, and ML practitioners working on aviation forecasting**.

All anchor data sourced from public materials: airline 10-K filings (SEC EDGAR), Boeing/Airbus monthly orders & deliveries reports, IATA Air Passenger Market Analysis reports, ASN Aviation Safety Network database, ICAO traffic statistics.

---

## Files

| File | Rows | Description |
|------|------|-------------|
| `airline_financials.csv` | 497 | 30 airlines × 17 years: revenue, margins, passengers, load factor, fleet |
| `fleet_orders.csv` | 86 | Boeing vs Airbus vs COMAC orders/deliveries/backlog by family |
| `passenger_traffic.csv` | 1,176 | 6 regions × monthly RPK/ASK/load factor 2010-2026 |
| `route_performance.csv` | 400 | 40 top global routes × multi-year passengers, fares, revenue |
| `aviation_incidents.csv` | 40 | Major accidents and incidents 2010-2026 |

Total: ~2,200 rows, ~150 KB.

---

## 30 Airlines Covered

**US Legacy (4):** Delta, United, American, Alaska
**US Low-Cost (2):** Southwest, JetBlue
**European Legacy (4):** Lufthansa Group, IAG, Air France-KLM, Aeroflot
**European Low-Cost (2):** Ryanair, easyJet
**European Hybrid (1):** Turkish Airlines
**Chinese (3):** Air China, China Eastern, China Southern
**Japanese (2):** JAL, ANA
**Other Asia (5):** Singapore Airlines, Cathay Pacific, Korean Air, IndiGo, AirAsia
**Middle East (5):** Emirates, Qatar Airways, Etihad, Saudia, Riyadh Air
**Latin America (2):** LATAM, Azul

---

## Key Findings Captured

### COVID Devastation 2020

- **Delta**: $47B (2019) → $17B (2020) = -64%, operating margin -36%
- **Lufthansa Group**: $40B → $15B
- **Cathay Pacific** worst affected: revenue -58%, 4 years to recover
- **Asia Pacific RPK collapse**: 64B (Dec 2019) → 9B (April 2020) = -86%
- Industry-wide operating margins -30% to -35% in 2020

### Boeing 737 MAX Crisis

- **2018**: Boeing 737 family net orders +675
- **2019**: Net orders **-87** (cancellations exceeded orders post-ET302 grounding)
- **2020**: Net orders **-1,026** (catastrophic, MAX still grounded + COVID)
- **2024**: Net orders +569 vs Airbus A320 +1,456 (2.5× gap)
- Recovery still incomplete in 2026

### 2024-2025 Boeing Crisis

- **AS1282** (Jan 2024): Alaska 737 MAX 9 door plug blowout
- **JL516** (Jan 2024): JAL A350 collided with Coast Guard at Haneda
- **AA5342** (Jan 2025): American Eagle CRJ-700 mid-air collision with Army Black Hawk near DCA
- **DL4819** (Feb 2025): Delta CRJ-900 flipped on landing in Toronto, all survived
- **AI171** (June 2025): Air India 787 crash in Ahmedabad
- Boeing production cap at 38/month by FAA, recovery to 50/month delayed to 2026

### COMAC C919 Rise

- **2018**: 24 orders, 0 deliveries
- **2023**: 250 orders, first 4 deliveries
- **2024**: 220 orders, 13 deliveries
- China's domestic narrowbody program finally ramping
- ~80% domestic Chinese orders; export market still limited by certification

### Middle East Growth

- **Emirates 2024**: $33B revenue (largest international airline by revenue)
- **Qatar Airways**: $7B (2010) → $22B (2024)
- **Saudia + Riyadh Air**: Saudi Arabia investing in becoming aviation hub
- **Etihad** restructured: $9B peak (2015) → $7B (2024)

### Recovery Asymmetry

- **North America recovery to 2019 baseline**: 2023
- **Europe recovery to 2019**: 2024
- **Asia Pacific recovery**: 2024-2025 (China lockdowns delayed)
- Middle East: exceeded 2019 by **2022**

### Geopolitical Aviation Events

- **MH17** (2014): Shot down over Ukraine, 298 fatalities
- **PS752** (2020): Shot down by IRGC, Tehran
- **FR4978** (2021): Ryanair forced down by Belarus, Roman Protasevich arrested
- **Aeroflot 2022+**: Sanctions cut Russian airlines from Western MRO services
- **J28243** (Dec 2024): Azerbaijan Airlines hit by Russian air defense

---

## Column Descriptions

### `airline_financials.csv`

| Column | Description |
|--------|-------------|
| `year`, `airline_name`, `iata_code`, `country_iso3`, `region` | Identifiers |
| `business_model` | legacy / low_cost / regional |
| `revenue_usd_bn` | Annual revenue (USD billions) |
| `operating_margin_pct` | Operating margin (negative in 2020-2021) |
| `operating_income_usd_bn` | Revenue × margin |
| `passengers_carried_m` | Passengers in millions |
| `load_factor_pct` | Passenger load factor |
| `fleet_size_est` | Approximate fleet size |

### `fleet_orders.csv`

| Column | Description |
|--------|-------------|
| `year`, `manufacturer`, `aircraft_family` | Boeing/Airbus/COMAC/Embraer |
| `orders_gross`, `orders_net` | Gross and net (after cancellations) orders |
| `deliveries` | Aircraft delivered that year |
| `backlog_end_of_year` | Outstanding orders at year-end |
| `is_widebody`, `is_narrowbody`, `is_regional` | Boolean classification |

### `passenger_traffic.csv`

| Column | Description |
|--------|-------------|
| `year_month`, `year`, `month` | Monthly time index |
| `region` | North America / Europe / Asia Pacific / Middle East / Latin America / Africa |
| `rpk_billions` | Revenue Passenger Kilometers (industry standard demand metric) |
| `ask_billions` | Available Seat Kilometers (supply metric) |
| `load_factor_pct` | RPK / ASK ratio |

### `route_performance.csv`

| Column | Description |
|--------|-------------|
| `year`, `route`, `origin_iata`, `destination_iata` | Identifiers |
| `distance_km` | Great circle distance |
| `region`, `main_airlines` | Context |
| `annual_passengers_m` | Annual passengers in millions |
| `avg_fare_usd` | Average one-way fare |
| `weekly_frequency_est` | Flights per week |
| `annual_revenue_usd_m` | Estimated annual route revenue |

### `aviation_incidents.csv`

| Column | Description |
|--------|-------------|
| `incident_id`, `date`, `year`, `month` | Identifiers |
| `flight_number`, `airline`, `aircraft_type` | Flight details |
| `severity` | fatal_crash / fatal_collision / incident / ground_incident / sanctions_impact |
| `fatalities` | Death count |
| `location`, `description` | Plain-language details |
| `is_fatal`, `is_geopolitical`, `is_boeing`, `is_airbus` | Boolean flags |

---

## Source

**Real public data:**

- **Airline financials**: SEC 10-K filings for US airlines (Delta, United, American, Southwest, Alaska, JetBlue), foreign equivalents for IAG, Lufthansa, Air France-KLM, Ryanair, easyJet, Turkish, Aeroflot, JAL, ANA, Singapore Airlines, Cathay Pacific
- **Boeing/Airbus orders**: Monthly orders & deliveries reports (publicly posted by both manufacturers)
- **Passenger traffic**: IATA Air Passenger Market Analysis monthly reports, ICAO traffic statistics
- **Top routes**: OAG, IATA route statistics, airline schedule data
- **Aviation incidents**: ASN Aviation Safety Network database, NTSB reports, EASA/FAA notices

**Modeled components:**

- Year-by-year revenue interpolation between 10-K anchor points
- Operating margins calibrated with COVID/MAX/Russia sanctions adjustments
- Regional passenger traffic generated from real anchor years with seasonal patterns
- Route passenger volumes derived from aggregate regional data and distance models
- Specific incidents are all real and verified; flight numbers, dates, fatalities accurate

---

## Methodology

### Step 1 — Airline Financials
For each airline, anchored to actual 10-K revenue at 8-10 reference years. Linear interpolation with 3% noise. Operating margins use segment norms (legacy 6-8%, low-cost 12%, regional 8%) with crisis adjustments: COVID 2020 -35%, 2021 -18%, Boeing 737 MAX effect on US carriers 2019, Aeroflot sanctions 2022+, Saudi investment phase margins (Riyadh Air -20% during build-out).

### Step 2 — Fleet Orders
Real anchor data from Boeing/Airbus monthly reports at 8 key years (2010, 2013, 2015, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024). Linear interpolation between anchors for non-anchor years. COMAC and Embraer separately tracked.

### Step 3 — Passenger Traffic
Regional RPK anchored to IATA monthly reports at 7 reference years. Monthly interpolation with seasonal pattern (summer peak Aug, winter trough Feb for Northern hemisphere; opposite for Latin America). COVID dynamics specifically modeled: April-June 2020 = -85%, H2 2020 = -65%, 2021 = -55%, H1 2022 = -35%, recovery to 2019 baseline by 2023-2025 depending on region.

### Step 4 — Route Performance
40 real top global routes with verified distances and dominant airlines. Per-route passenger volumes calibrated to distance (short-haul = higher volume, long-haul = lower volume). Year-over-year factors apply COVID dynamics. Avg fare scales with distance plus year-over-year inflation.

### Step 5 — Aviation Incidents
40 real verified incidents from ASN/NTSB/EASA databases. All fatalities, dates, flight numbers, locations accurate. Categorized as fatal_crash, fatal_collision, incident, ground_incident, or sanctions_impact.

### Reproducibility
Deterministic given seed. Source code `generate_aviation.py` included.

### What This Dataset Is and Is Not

**Suitable for:** aviation industry research, equity analysis (airline/aerospace sector), trend analysis, COVID recovery analysis, Boeing vs Airbus competitive analysis, route economics modeling, ML training for aviation forecasting, journalism.

**Not suitable for:** individual incident audit (use ASN/NTSB primary data), regulatory compliance, specific airline financial verification (cross-reference 10-K filings), passenger-level analysis, individual flight scheduling.

---

## Suggested Tasks

### 1. Boeing Recovery Modeling
Boeing 737 MAX net orders went from +1,208 (2013) to -1,026 (2020) to +569 (2024). Build a recovery trajectory model. When does Boeing return to parity with Airbus on narrowbody?

### 2. COVID Recovery Asymmetry
Compare time to full recovery (2019 baseline) by region. Asia Pacific lagged 2 years behind. Quantify the lockdown effect.

### 3. Saudi Aviation Strategy Analysis
Saudia, Riyadh Air, and Etihad combined revenue trajectory 2023-2026. How much state investment is required to compete with Emirates/Qatar?

### 4. Route Economics
Average fare × passengers = route revenue. Build a route profitability model accounting for fuel/operating costs. Identify gold routes vs commodity routes.

### 5. Low-Cost vs Legacy Margins
Compare operating margins by business model over time. Did COVID change the structural margin gap?

### 6. Incident Frequency Analysis
40 major incidents in 16 years. Has commercial aviation become safer? Adjust for traffic volume.

### 7. Boeing Crisis Impact on Stocks
Cross-reference 2024 incidents (AS1282, JL516, AA5342, AI171) with Boeing stock data. What's the cumulative drag?

### 8. Middle East Hub Battle
Emirates, Qatar Airways, Turkish Airlines compete for global connecting traffic. Build a market share model.

### 9. COMAC C919 Trajectory
Project COMAC orders/deliveries 2026-2030 based on 2023-2025 ramp data. Realistic threat to Boeing/Airbus duopoly?

### 10. Cross-Series Analysis
Combine with companion datasets:
- [Global Supply Chain & Trade Disruptions](https://www.kaggle.com/datasets/sergionefedov/global-supply-chain-trade-disruptions) — aircraft delivery chain
- [Global Semiconductor Industry 2010-2026](https://www.kaggle.com/datasets/sergionefedov/global-semiconductor-industry-2010-2026) — aircraft electronics supply chain

---

## Limitations

- **Foreign airline financials**: USD-equivalent revenue may differ slightly from local currency reported numbers due to FX
- **Chinese airlines 2020-2022**: Reporting transparency limited during COVID; estimates used
- **Fleet orders for 2025-2026**: Projections based on H1 2026 trajectory
- **Route passenger volumes**: Based on regional aggregates and route prominence, not OAG schedule-level granularity
- **Incidents**: Only major incidents covered; full ASN database is much larger
- **No cargo airlines** (FedEx, UPS, Cargolux excluded)
- **No private jets / general aviation** included
- **End of period 2026 partial**: data through April 2026

---

## License

CC0: Public Domain. Use freely for academic, commercial, journalistic, or any other purpose.

---

## Citation

```
Global Aviation Industry 2010-2026. Kaggle Datasets, 2026.
```

---

## Acknowledgments

Anchor data sourced from public materials: airline 10-K filings (SEC EDGAR), Boeing/Airbus monthly orders & deliveries reports (boeing.com, airbus.com), IATA Air Passenger Market Analysis monthly reports, ICAO statistics, ASN Aviation Safety Network database (aviation-safety.net), NTSB/EASA accident reports.

This is a community resource. Pull requests with corrections welcome.

If this dataset helped your research, analysis, or work, an upvote is appreciated — it helps the dataset surface to other aviation practitioners.

**Related datasets by the same author:**
- [Global Supply Chain & Trade Disruptions 25 years](https://www.kaggle.com/datasets/sergionefedov/global-supply-chain-trade-disruptions-25-years)
- [Global Semiconductor Industry 2010-2026](https://www.kaggle.com/datasets/sergionefedov/global-semiconductor-industry-2010-2026)
- [Global Football Transfer Market 2010-2026](https://www.kaggle.com/datasets/sergionefedov/global-football-transfer-market-2010-2026)
- [Global Climate & Energy Transition](https://www.kaggle.com/datasets/sergionefedov/global-climate-energy-transition)

출처: Kaggle (sergionefedov/global-aviation-industry-2010-2026)
태그: finance, economics, science and technology, engineering, aviation
라이선스: CC0: Public Domain
수정일: 2026-06-21T17:14:52.357Z
