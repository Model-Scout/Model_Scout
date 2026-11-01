# Asia Daily Weather & Air Quality, 2023-2026

Daily weather and model-based air quality across 18 major Asian cities

## Overview

A daily cross-country panel of weather observations and model-derived air-quality estimates for **18 major Asian cities**, covering **2023-01-01 through 2026-07-27**. The table contains **23,472 city-day records**, aligned to each city's local calendar date.

## Geographic scope

Beijing, Shanghai, Guangzhou, Shenzhen, Hong Kong, Taipei, Tokyo, Seoul, Singapore, Bangkok, Hanoi, Ho Chi Minh City, Jakarta, Kuala Lumpur, Manila, New Delhi, Mumbai and Dhaka. The selection supports comparisons across East, Southeast and South Asia; it is not intended to represent every Asian country.

## Variables

- Daily temperature, apparent temperature, precipitation, rain, wind and solar radiation.
- Daily mean PM2.5, PM10, nitrogen dioxide and ozone.
- Daily maximum US AQI and European AQI.
- City, country or region, latitude and longitude.

## Sources and processing

Weather variables come from the **Open-Meteo Historical Weather API**. Air-quality estimates come from the **Open-Meteo Air Quality API** and its Copernicus Atmosphere Monitoring Service (CAMS) inputs. Hourly pollutant values were averaged by local date; AQI values use the daily maximum. No missing values were imputed. Retrieval date: **2026-07-28**.

## Recommended uses

Cross-city environmental comparison, seasonal analysis, forecasting, anomaly detection, pollution-weather association studies and reproducible visualization examples.

## Limitations

Air-quality variables are **gridded model estimates, not regulatory monitoring-station measurements**. They should not replace official local records or be used for medical, exposure or public-health decisions. Historical values may be revised by the upstream providers.

출처: Kaggle (houjihao/asia-daily-weather-and-air-quality-2023-2026)
태그: asia, environment, pollution, weather and climate, time series analysis
라이선스: CC BY-NC-SA 4.0
수정일: 2026-07-27T19:46:50.360Z
