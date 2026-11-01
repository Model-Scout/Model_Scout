# Global Megacities Weather Extremes 2015-2024

182K Daily Weather Observations 2015-2024: 50 Global Megacities

```python
# Quickstart: Ingest this research benchmark in 1 line via kagglehub
import kagglehub
path = kagglehub.dataset_download("luthfimuthathohirin/global-megacities-climate-weather-extremes")
print("Path to dataset files:", path)
```

### 📖 Context & Domain Background
Over the past decade (2015 to 2024), accelerating anthropogenic climate change has catalyzed unprecedented atmospheric turbulence, manifesting as record-breaking urban heat domes, hyper-intense convective deluges, and disruptive synoptic weather anomalies across the globe. As home to over 55% of the human population, the world's megacities face compounding vulnerability: the urban heat island (UHI) effect amplifies thermal stress during summer heatwaves, while impermeable metropolitan surfaces turn high-intensity convective rainfall into flash flood emergencies.

Understanding multi-decadal meteorological dynamics across planetary climate zones requires granular, multi-variable daily empirical telemetry. While satellite and reanalysis platforms provide raw physical fields, extracting actionable climate intelligence requires synthesizing raw thermodynamic parameters (2-meter temperatures, global shortwave solar radiation, boundary layer wind gusts) with explicit, physics-grounded **Chain-of-Thought (CoT)** meteorological reasoning.

To empower atmospheric scientists, urban planning researchers, climate econometricians, and machine learning practitioners, this dataset provides a standardized, publication-grade benchmark of **182,650 daily historical weather observations spanning 10 complete calendar years (2015–2024) across 50 representative megacities and polar research stations in 40 sovereign nations across all 7 continents**. Enriched by a multi-tier Explain-Then-Annotate cognitive annotation pipeline (Tier 1 Gemini 3.8 Flash Worker + Tier 2 Claude Opus Judge) with gold-standard inter-annotator consensus (**Cohen's Kappa κ = 0.9433**) and algorithmic denoising via **Cleanlab Confident Learning**, this benchmark bridges raw geophysical telemetry with explainable atmospheric hazard adjudication.

---

### 🗃️ Content & Dataset Summary
The dataset compiles 10 continuous years of daily meteorological observations from the **Open-Meteo Historical Archive REST API**, grounded in ECMWF ERA5 and high-resolution IFS atmospheric reanalysis models. The corpus is structured across **28 comprehensive features** (20 raw geophysical variables + 8 cognitive and CoT enrichment dimensions) and provided in dual formats: clean tabular CSV (`global_megacities_climate_weather_extremes_enriched.csv`, 196.3 MB) and Snappy-compressed columnar Parquet (`global_megacities_climate_weather_extremes_enriched.parquet`, 21.0 MB).

#### Key Meteorological & Planetary Dimensions:
* **Total Observation Volume**: Exactly 182,650 daily records (3,653 days per city × 50 global locations)
* **Temporal Coverage**: 10 full calendar years (2015-01-01 to 2024-12-31, 0 temporal gaps)
* **Geographical Distribution**: 50 megacities and research stations across 40 countries and 7 continents:
  * **Asia (15 cities)**: Tokyo, Jakarta, Beijing, Shanghai, Delhi, Mumbai, Seoul, Singapore, Bangkok, Manila, Dubai, Riyadh, Istanbul, Karachi, Dhaka
  * **Europe (10 cities)**: London, Paris, Berlin, Rome, Madrid, Moscow, Amsterdam, Athens, Stockholm, Kyiv
  * **North America (7 cities)**: New York, Los Angeles, Chicago, Houston, Toronto, Mexico City, Vancouver
  * **South America (6 cities)**: Sao Paulo, Buenos Aires, Rio de Janeiro, Bogota, Lima, Santiago
  * **Africa (6 cities)**: Cairo, Lagos, Johannesburg, Nairobi, Casablanca, Kinshasa
  * **Oceania (4 cities)**: Sydney, Melbourne, Brisbane, Auckland
  * **Antarctica (2 stations)**: McMurdo Station, Esperanza Base
* **Köppen-Geiger Macro Climate Zones**:
  * `Subtropical`: 65,754 records (18 locations, 36.00%)
  * `Tropical`: 32,877 records (9 locations, 18.00%)
  * `Continental`: 29,224 records (8 locations, 16.00%)
  * `Temperate`: 29,224 records (8 locations, 16.00%)
  * `Arid`: 18,265 records (5 locations, 10.00%)
  * `Polar`: 7,306 records (2 locations, 4.00%)
* **Historical Extremes Captured**:
  * Highest Temperature: Riyadh, Saudi Arabia (47.6 °C on 2024-07-12)
  * Lowest Temperature: McMurdo Station, Antarctica (-51.0 °C on 2023-08-14)
  * Peak Daily Precipitation: Mumbai, India (375.2 mm/day on 2019-07-02 during summer monsoon)
  * Maximum Atmospheric Wind Gust: Esperanza Base, Antarctica (114.1 km/h on 2020-09-08)
* **Cognitive Reliability Metrics**:
  * Inter-Annotator Agreement: Cohen's Kappa κ = 0.9433 (Gold Standard / Near Perfect Agreement)
  * Mean Calibrated Confidence: 0.9913 (range 0.900 to 0.999)
  * Cleanlab Confident Learning Pruned: 139 boundary label noise disputes adjudicated to ground truth

---

### 📋 Field-Level Data Dictionary
| Column Name | Inferred Type | Description |
| :--- | :--- | :--- |
| `city` | String (Categorical) | Name of the global megacity or polar research base (50 unique locations). |
| `country` | String (Categorical) | Sovereign nation or territorial entity of observational location (40 countries). |
| `continent` | String (Categorical) | Geographic continent: Asia, Europe, North America, South America, Africa, Oceania, Antarctica. |
| `latitude` | Float (Decimal) | WGS84 decimal latitude coordinate of the meteorological station centroid. |
| `longitude` | Float (Decimal) | WGS84 decimal longitude coordinate of the meteorological station centroid. |
| `elevation_m` | Float | Elevation above mean sea level in meters (-12m to 2,640m). |
| `date` | String (ISO-8601) | Daily observation date in YYYY-MM-DD format (2015-01-01 to 2024-12-31). |
| `year` | Integer | Observation calendar year (2015 to 2024). |
| `month` | Integer | Observation calendar month (1 to 12). |
| `day` | Integer | Observation calendar day of the month (1 to 31). |
| `temp_max_c` | Float | Daily maximum 2-meter air temperature in degrees Celsius (°C). |
| `temp_min_c` | Float | Daily minimum 2-meter air temperature in degrees Celsius (°C). |
| `temp_mean_c` | Float | Daily mean 2-meter air temperature in degrees Celsius (°C). |
| `temp_range_c` | Float | Daily diurnal temperature variation range in degrees Celsius (temp_max - temp_min). |
| `precipitation_sum_mm` | Float | Total daily liquid and solid precipitation sum in millimeters (mm). |
| `rain_sum_mm` | Float | Total daily liquid rainfall accumulation sum in millimeters (mm). |
| `snowfall_sum_cm` | Float | Total daily snowfall accumulation depth in centimeters (cm). |
| `wind_speed_max_kmh` | Float | Maximum daily 10-meter wind gust speed in kilometers per hour (km/h). |
| `shortwave_radiation_mj_m2` | Float | Total daily incoming solar shortwave radiation energy accumulated in Megajoules per square meter (MJ/m²). |
| `climate_zone` | String (Categorical) | Macro Köppen-Geiger climatic zone: Subtropical, Tropical, Continental, Temperate, Arid, Polar. |
| `extreme_heat_severity` | String (Categorical) | Heat/cold stress level: normal_range (140,628), moderate_heat (20,047), frost_freeze (16,760), polar_deep_freeze (2,725), extreme_heatwave (2,490). |
| `precipitation_intensity` | String (Categorical) | Daily precipitation scale: dry_day (122,004), light_drizzle (45,523), moderate_rain (14,510), heavy_precipitation (538), extreme_deluge (75). |
| `diurnal_temperature_swing` | String (Categorical) | Diurnal thermal amplitude: moderate_swing (86,122), high_swing (51,489), maritime_stable (34,406), extreme_diurnal_swing (10,633). |
| `seasonality_hemisphere` | String (Categorical) | Astronomical solar seasonality quadrant: equinoctial_transition (80,520), northern_summer_southern_winter (40,480), northern_winter_southern_summer (39,732), equatorial_tropical_cycle (21,918). |
| `climate_anomaly_flag` | String (Categorical) | Compound atmospheric hazard event flag: baseline_normal (168,629), compound_extreme_heat_drought (7,468), severe_cold_snap (5,673), tropical_deluge_flood (613), gale_wind_event (267). |
| `evidence_span` | String (Text) | Verifiable quantitative telemetry anchor extracting city, coordinates, temperature bounds, precipitation, wind, and radiation. |
| `cot_rationale` | String (Text) | Structured scientific Chain-of-Thought reasoning synthesizing thermodynamic lapse rates, advection, and atmospheric radiation budget. |
| `confidence_score` | Float (0.0–1.0) | Calibrated Bayesian posterior certainty score of meteorological adjudication (mean 0.9913). |

---

### 🧹 Data Collection & Cleaning Methodology
1. **Open-Meteo Historical Archive Ingestion (Gate 1 Contract)**:
   * Extracted directly from Open-Meteo Historical Weather Archive REST API (`https://archive-api.open-meteo.com/v1/archive`), integrating ECMWF ERA5 and high-resolution IFS numerical atmospheric reanalysis models.
   * Multi-threaded harvester executed with proxy pool rotation and disk checkpointing, verifying zero temporal gaps across 3,653 consecutive days per city.
   * Raw dataset integrity confirmed with exactly 182,650 rows, 20 features, and **0 null values** across all numeric fields.
   * Primary raw artifact locked via SHA-256 (`532d99aece87dfa76f62198567525fe5213ca14855f2704c7b1f19875fdcdb9c`).

2. **Explain-Then-Annotate Cognitive CoT Pipeline (Gate 2 Contract)**:
   * Each observation was processed under an Explain-Then-Annotate protocol: the model first extracted exact numeric evidence spans (`temp_max_c`, `precipitation_sum_mm`, `wind_speed_max_kmh`, `shortwave_radiation_mj_m2`, `climate_zone`), articulated a Chain-of-Thought rationale explaining atmospheric lapse rates and radiative equilibrium, and then assigned deterministic severity labels.
   * Inter-annotator consensus between Tier 1 Worker (Gemini 3.8 Flash) and Tier 2 Judge (Claude Opus) yielded a gold-standard **Cohen's Kappa κ = 0.9433**.

3. **Algorithmic Denoising via Cleanlab Confident Learning**:
   * Out of 4,002 boundary dispute candidates, Cleanlab Confident Learning detected 139 label noise edge cases where maritime boundary layers or high-elevation thermal regimes created threshold ambiguity, cleanly resolving all 139 to validated ground truth.

4. **Zero-PII & Open Data Hygiene**:
   * Data contains exclusively physical atmospheric and geographical telemetry. Zero personally identifiable information (PII), proprietary corporate data, or user credentials exist.
   * Normalized UTF-8 encoding with standard Unix LF line delimiters.

---

### 💡 Potential Research Ideas & ML Tasks
1. **Multi-Horizon Urban Heatwave & Extreme Cold Forecasting**:
   * Develop spatio-temporal deep learning architectures (Graph Neural Networks, Temporal Fusion Transformers, PatchTST) to predict multi-day compound heatwave (`extreme_heat_severity`) and cold-snap trajectories across distinct Koppen climate zones.
   * Quantify transferability of heat dome forecasting models trained on mid-latitude continental cities (Chicago, Moscow) to high-radiation subtropical megacities (Riyadh, Cairo).

2. **Compound Climate Hazard Early Warning & Multi-Task Learning**:
   * Formulate multi-task classification models predicting concurrent atmospheric hazards (`climate_anomaly_flag`), identifying non-linear interactions between solar shortwave radiation surges, low humidity, and high diurnal temperature swings preceding drought-heatwave compounds.
   * Benchmark gradient boosting (LightGBM, XGBoost, CatBoost) against transformer-based tabular classifiers on imbalanced extreme deluge events (`extreme_deluge` = 75 cases).

3. **Inter-Continental Climate Analogs & Urban Resilience Benchmarking**:
   * Apply unsupervised manifold learning (UMAP, t-SNE) and clustering algorithms on 10-year thermal-radiation-precipitation distributions to identify twin climate trajectories among distant global cities (e.g., comparing Mediterranean Athens vs Santiago).
   * Evaluate long-term warming trends and diurnal range compression as empirical indicators of urban microclimate evolution.

---

### 📜 Acknowledgements & Citation
Curated and published by **Luthfi Muthathohirin** and Ken's **Kaggle Automation Squad**. Atmospheric telemetry sourced from the **Open-Meteo Historical Weather API**, powered by ECMWF ERA5 / Copernicus Climate Change Service and national meteorological reanalysis datasets under CC BY 4.0.

```bibtex
@dataset{luthfi2026globalmegacitiesclimate,
  author    = {Luthfi Muthathohirin and Kaggle Automation Squad},
  title     = {Global Megacities Weather Extremes (2015-2024): 10-Year Decadal Climate Benchmark},
  year      = {2026},
  publisher = {Kaggle},
  url       = {https://www.kaggle.com/datasets/luthfimuthathohirin/global-megacities-climate-weather-extremes}
}
```

### 🔄 What's New in Version 2
* **Single Primary CSV Tabular Architecture**: Streamlined packaging to an optimized single CSV format () for 100% native Kaggle Data Explorer preview compatibility.
* **Complete 28-Column Dictionary**: All 28 meteorological, climate extreme, and CoT features fully documented in the dataset schema.
* **Usability Rating 10.0 Benchmark Compliance**: Fully aligned with Kaggle completeness, credibility, and compatibility requirements.


---

## 🔬 Explore Companion Benchmarks in the Open Science Ecosystem

This dataset is an integral node within the **Open Science Intelligence Ecosystem** curated by [Luthfi Muthathohirin](https://www.kaggle.com/luthfimuthathohirin). Accelerate your research across complementary domains:

| Companion Benchmark Dataset | Connected Grandmaster EDA Kernel | Ecosystem Architecture |
| :--- | :--- | :--- |
| **Official Starter Kernel** | [⚡ Megacities Climate Time Series Neural Forecast EDA](https://www.kaggle.com/code/luthfimuthathohirin/megacities-climate-time-series-neural-forecast-eda) | `Kaggle Grandmaster Code` |
| [Global Carbon Emissions & GHG](https://www.kaggle.com/datasets/luthfimuthathohirin/global-carbon-emissions-greenhouse-gas) | [Planetary Decarbonization Atlas GIS GHG EDA](https://www.kaggle.com/code/luthfimuthathohirin/planetary-decarbonization-atlas-gis-ghg-eda) | `Connected Research Node` |
| [Forest Canopy & Deforestation Telemetry](https://www.kaggle.com/datasets/luthfimuthathohirin/satellite-forest-canopy-deforestation-telemetry) | [Satellite Canopy Deforestation Forensic EDA](https://www.kaggle.com/code/luthfimuthathohirin/satellite-canopy-deforestation-forensic-eda) | `Connected Research Node` |
| [Global Airports & Aviation Infrastructure](https://www.kaggle.com/datasets/luthfimuthathohirin/global-airports-aviation-infrastructure) | [Global Aviation Cartography GIS Spatial EDA](https://www.kaggle.com/code/luthfimuthathohirin/global-aviation-cartography-gis-spatial-eda) | `Connected Research Node` |

출처: Kaggle (luthfimuthathohirin/global-megacities-climate-weather-extremes)
태그: global, earth science, atmospheric science, environment, weather and climate
라이선스: CC0: Public Domain
수정일: 2026-10-17T03:41:44.413Z
