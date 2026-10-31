# Daejeon bike sharing dataset

Daejeon Public Bicycle 'Tashu' rental dataset

This dataset contains hourly aggregated bike rental data from the Tashu public bike-sharing system in Daejeon, South Korea, from August 2022 to July 2024.  
It includes weather variables such as temperature, precipitation, wind speed, humidity, and solar radiation, sourced from the Korean Meteorological Administration (ASOS).  
The data is ideal for time series forecasting, weather impact analysis, and mobility research.  
It serves as a Korean counterpart to the popular Bike Sharing Demand dataset, enabling comparative modeling and experimentation.

**License**

Released under **KOGL Type 1 (Attribution Required)** – Free for commercial and non-commercial use with proper source citation.

Original data sources:
- Daejeon Transportation Corporation (https://www.data.go.kr/data/15137219/fileData.do)
- Korea Meteorological Administration (https://data.kma.go.kr)

※ This dataset is a value-added, restructured version derived from public data originally provided by Daejeon Transportation Corporation, combined with ASOS weather data. It has been aggregated, and reformed for research use. ※

License details: https://www.kogl.or.kr/info/license.do

&gt; This dataset was independently compiled and is **not officially affiliated with** or endorsed by the above institutions.  
&gt; It is offered for **educational and research purposes only**.

**column**
- ID: record index
- datetime: timestamp of the rental record
- temperature: air temperature in degrees Celsius
- precipitation: precipitation amount in millimeters
- windspeed: wind speed in meters per second
- humidity: relative humidity in percentage
- dew_point: dew point temperature in degrees Celsius
- sunshine: sunshine duration in hours
- solar_radiation: solar radiation in MJ/m²
- snowfall: snowfall amount in centimeters
- cloud_cover: cloud coverage in the tenth decile
- visibility: visibility distance in 10 meters
- ground_temp: ground surface temperature in degrees Celsius
- weekday: day of the week
- holiday: whether the day is a national holiday(**Korean standard**)
- count: number of bikes rented during the corresponding hour

출처: Kaggle (lnoahl/daejeon-bike-sharing-dataset)
태그: asia, cycling, data cleaning
라이선스: Other (specified in description)
수정일: 2025-07-09T12:09:50.423Z
