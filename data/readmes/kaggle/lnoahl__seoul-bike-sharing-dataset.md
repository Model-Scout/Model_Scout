# Seoul bike sharing dataset

Seoul Public Bicycle 'Ddareungi' rental dataset

### **Summary**  
This dataset contains hourly aggregated bike rental data from the Seoul public bike-sharing system in Seoul, South Korea.
It includes weather variables such as temperature, precipitation, wind speed, humidity, and solar radiation, sourced from the Korea Meteorological Administration (ASOS).
The data is ideal for time series forecasting, weather impact analysis, and mobility research.
It serves as a Korean counterpart to the popular Bike Sharing Demand dataset, enabling comparative modeling and experimentation.

### **License**

Released under **KOGL Type 1 (Attribution Required)** – Free for commercial and non-commercial use with proper source citation.

Original data sources:  
Seoul Open Data Plaza (https://data.seoul.go.kr)  
Korea Meteorological Administration (https://data.kma.go.kr)

※ This dataset is a value-added, restructured version derived from public data originally provided by Seoul Open Data Plaza, combined with ASOS weather data. It has been aggregated and restructured for research use. ※

License details: https://www.kogl.or.kr/info/license.do

>This dataset was independently compiled and is not officially affiliated with or endorsed by the above institutions.
> It is offered for educational and research purposes only.

### **Column Description**
- ID: record index
- datetime: timestamp of the rental record
- temperature: air temperature in degrees Celsius
- precipitation: precipitation amount in millimeters
- windspeed: wind speed in meters per second
- humidity: relative humidity as a percentage
- dew_point: dew point temperature in degrees Celsius
- sunshine: sunshine duration in hours
- solar_radiation: solar radiation in MJ/m²
- snow_depth: snow accumulation in centimeters
- cloud_cover: cloud coverage in tenths (0–10)
- visibility: visibility in tens of meters
- ground_temp: ground surface temperature in degrees Celsius
- weekday: day of the week
- holiday: whether the day is a national holiday(**Korean standard**)
- count: number of bikes rented during the corresponding hour
  
  
### **Data Processing Notes**  

#### Note (2026.09.01)  

**Constraint-Based Missing Value Resolution**  
  Missing values were retained unless they could be reasonably resolved from physical or temporal constraints.
For example, missing sunshine and solar radiation values during confirmed nighttime periods were set to zero. Ambiguous observations were left as missing values.


#### Note (2026.09.22)  

**Column Renamed: snowfall → snow_depth**  
- Change: `snowfall` → `snow_depth`
- Reason: This column corresponds to the KMA ASOS "적설" observation (accumulated snow depth on the ground in cm), not hourly fresh snowfall.
  
**Snow Depth Missing Value Imputation**  <br>  
For missing `snow_depth` values:
- When precipitation was observed and air temperature was at or above 0°C, the missing value was filled with 0.
- When air temperature was below 0°C, the missing value was retained because the absence of snow could not be safely inferred.

#### Note (2026.10.02)

**README Description Correction**
Fixed a description error in the README regarding the `visibility` column unit (corrected to 10 meters). This is a documentation fix only; the underlying data remains unchanged.

출처: Kaggle (lnoahl/seoul-bike-sharing-dataset)
태그: asia, cycling, data cleaning
라이선스: Other (specified in description)
수정일: 2026-10-02T05:11:25.247Z
