# Global Air Quality Data(15 Days Hourly, 50 Cities)

Historically realistic global air-quality readings with pollutants and weather f

📘 Overview

This dataset provides hourly air-quality measurements for 50 major global cities over a continuous 15-day period, including pollutant concentrations, meteorological conditions, geographical metadata, and an engineered AQI index.

All values are synthetically generated using historically consistent pollutant patterns and statistical ranges, allowing researchers and ML practitioners to work with realistic air-quality trends without licensing restrictions or data-collection barriers.

This dataset is ideal for time-series modeling, forecasting, environmental analytics, and machine-learning experimentation.

🧭 Cities Included

Covers all major regions:

North America — New York, Los Angeles, Toronto

Europe — London, Paris, Berlin, Zurich

Asia — Delhi, Tokyo, Seoul, Beijing, Singapore

Middle East — Dubai, Riyadh, Doha

Africa — Lagos, Cairo, Nairobi

Oceania — Sydney, Melbourne, Auckland

South America — São Paulo, Buenos Aires

🧱 Dataset Structure

Each hourly record includes:

Air Pollutants

PM2.5 (µg/m³)

PM10 (µg/m³)

NO₂ (ppb)

SO₂ (ppb)

O₃ (ppb)

CO (ppm)

Weather Features

Temperature (°C)

Humidity (%)

Wind Speed (m/s)

Location Metadata

City

Country

Latitude

Longitude

Other

Timestamp (ISO-8601)

AQI (Computed index)

🧹 Data Quality & Formatting

No missing values — 100% complete

Numeric values rounded to 3 decimals

Clean column names (snake_case)

Consistent hourly frequency

Fully ML-ready

📊 Example Use Cases

✔ AQI forecasting (LSTM, GRU, Transformers)
✔ Multivariate time-series modeling
✔ Clustering cities by pollution patterns
✔ Environmental trend visualization
✔ Weather–pollution correlation studies
✔ Anomaly detection (peak pollution events)

| Column      | Description               | Unit  | Type     |
| ----------- | ------------------------- | ----- | -------- |
| timestamp   | Hourly timestamp (UTC)    | —     | datetime |
| city        | City name                 | —     | string   |
| country     | Country name              | —     | string   |
| latitude    | City latitude             | °     | float    |
| longitude   | City longitude            | °     | float    |
| pm25        | Fine particulate matter   | µg/m³ | float    |
| pm10        | Coarse particulate matter | µg/m³ | float    |
| no2         | Nitrogen dioxide          | ppb   | float    |
| so2         | Sulfur dioxide            | ppb   | float    |
| o3          | Ozone                     | ppb   | float    |
| co          | Carbon monoxide           | ppm   | float    |
| temperature | Ambient temperature       | °C    | float    |
| humidity    | Relative humidity         | %     | float    |
| wind_speed  | Wind speed                | m/s   | float    |
| aqi         | Derived Air Quality Index | —     | int      |

🧪 Data Generation Method (Provenance)

This dataset is synthetically generated using realistic pollutant behavior patterns based on historical studies and open-source environmental datasets.

Modeling steps included:

City-specific pollutant baseline ranges

Randomized variation using Gaussian noise

Temporal patterns using sinusoidal diurnal cycles (morning & evening peaks)

Weather-pollution correlation rules (e.g., low wind → higher PM)

AQI computed using standard US-EPA breakpoints

All numeric values standardized to 3-decimal precision

This ensures that although synthetic, the dataset follows realistic environmental dynamics.

📁 File Information

global_air_quality_50_cities.csv

Rows: 18,000+

Columns: 16

Format: UTF-8 CSV

출처: Kaggle (smeet888/global-air-quality-data15-days-hourly-50-cities)
태그: atmospheric science, environment, pollution, weather and climate, time series analysis
라이선스: CC0: Public Domain
수정일: 2025-11-19T18:32:25.430Z
