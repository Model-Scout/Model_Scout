# Dataset for Electricity Load Forecasting(Korea)

Dataset for Electricity Demand Forecasting in Korea (2020–2023)

## 🙋‍♂️ Summary

This dataset contains hourly electricity demand data in South Korea from 2020 to 2023.  
It is designed for electricity load forecasting research and includes both power consumption and external factors such as electric vehicle (EV) charging (fast and slow), weather conditions, and holidays.  
The dataset is suitable for building and evaluating machine learning or deep learning models for short-term energy forecasting, especially focusing on the integration of EV charging demand and environmental variables.

---

## 📊 Data Description

| Column(Korean) | Column (English) | Description |
|------------------|-------------------|--------------|
| `날짜` | date and time | Date and time of observation (hourly interval) |
| `전력수요량` | power_demand_MWh | Total electricity demand in megawatt-hours (MWh) |
| `급속충전` | EV_fast_charging | Electricity usage for EV fast charging (Direct Current, kWh) |
| `완속충전` | EV_slow_charging | Electricity usage for EV slow charging (Alternating Current, kWh) |
| `기온(℃)` | temperature_C | Air temperature in degrees Celsius |
| `습도(%)` | humidity_percent | Relative humidity (%) |
| `지면온도(℃)` | ground_temperature_C | Ground surface temperature in degrees Celsius |
| `is_holiday` | is_holiday | Boolean flag indicating whether the day is a public holiday (`True` / `False`) |
| `day_type` | day_type | Type of day (e.g., weekday, weekend) |

---

## 🌎 Potential Use Cases

- Short-term electricity load forecasting  
- Impact analysis of EV charging on power demand  
- Weather-influenced power consumption prediction  
- Time-series modeling (LSTM, XGBoost, Prophet, etc.)  
- Renewable energy integration and smart grid optimization

출처: Kaggle (cjh6886/dataset-for-electricity-load-forecasting)
태그: energy, electricity, korea
라이선스: MIT
수정일: 2025-08-27T10:18:35.697Z
