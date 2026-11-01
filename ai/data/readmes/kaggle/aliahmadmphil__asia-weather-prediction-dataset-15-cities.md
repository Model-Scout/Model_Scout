# Asia Weather Prediction Dataset 15 cities

10 Years of Daily Climate Data for Weather Forecasting

# About Dataset

## Asia Weather Prediction Dataset 15 Cities

### Overview

The **Asia Weather Prediction Dataset** is a comprehensive collection of daily weather observations from 15 major Asian cities spanning a decade from January 1, 2016, to December 31, 2025. This meticulously crafted dataset contains 54,750 records with 24 carefully selected features, making it an invaluable resource for weather prediction, climate analysis, time series forecasting, and machine learning applications.

### Dataset Purpose

This dataset is specifically designed to facilitate weather prediction modeling and climate pattern analysis across diverse Asian geographical regions. It provides researchers, data scientists, and machine learning practitioners with high-quality, structured data to develop and test predictive models for various weather variables including temperature, humidity, precipitation, wind speed, and atmospheric pressure.

### Cities Included

The dataset covers 15 strategically selected cities representing different climate zones across Asia:

| City | Country | Latitude | Longitude | Climate Type |
|------|---------|----------|-----------|--------------|
| Tokyo | Japan | 35.6762 | 139.6503 | Temperate |
| Beijing | China | 39.9042 | 116.4074 | Continental |
| Mumbai | India | 19.0760 | 72.8777 | Tropical Monsoon |
| Singapore | Singapore | 1.3521 | 103.8198 | Equatorial |
| Shanghai | China | 31.2304 | 121.4737 | Humid Subtropical |
| Dubai | UAE | 25.2048 | 55.2708 | Arid Desert |
| Bangkok | Thailand | 13.7563 | 100.5018 | Tropical Monsoon |
| Seoul | South Korea | 37.5665 | 126.9780 | Humid Continental |
| Jakarta | Indonesia | -6.2088 | 106.8456 | Tropical |
| Kuala Lumpur | Malaysia | 3.1390 | 101.6869 | Equatorial |
| Hong Kong | China | 22.3193 | 114.1694 | Humid Subtropical |
| Taipei | Taiwan | 25.0330 | 121.5654 | Humid Subtropical |
| Manila | Philippines | 14.5995 | 120.9842 | Tropical |
| New Delhi | India | 28.6139 | 77.2090 | Subtropical |
| Ho Chi Minh | Vietnam | 10.8231 | 106.6297 | Tropical |

### Climate Zone Diversity

The dataset's strength lies in its representation of diverse climate zones:

- **Temperate Cities**: Tokyo, Shanghai, Taipei, Hong Kong
- **Continental Cities**: Beijing, Seoul
- **Tropical Cities**: Singapore, Jakarta, Kuala Lumpur, Manila, Ho Chi Minh
- **Monsoon Cities**: Mumbai, Bangkok, New Delhi
- **Arid City**: Dubai

This diversity allows for robust cross-climate analysis and model training that can generalize across different weather patterns.

### Features Description

The dataset includes 24 carefully selected features grouped into four categories:

#### 1. Location Features (3 features)
- **city**: Name of the city (string)
- **latitude**: Latitude coordinate (float)
- **longitude**: Longitude coordinate (float)

#### 2. Temporal Features (5 features)
- **date**: Date of observation in YYYY-MM-DD format
- **day_of_year**: Day number from 1 to 365 (or 366)
- **month**: Month number from 1 to 12
- **year**: Year from 2016 to 2025
- **season**: Season classification (Winter, Spring, Summer, Fall)

#### 3. Weather Variables (6 features)
- **temperature_c**: Daily average temperature in Celsius
- **humidity_percent**: Daily average humidity percentage
- **precipitation_mm**: Daily total precipitation in millimeters
- **wind_speed_kmh**: Daily average wind speed in km/h
- **pressure_hpa**: Daily average atmospheric pressure in hPa
- **cloud_cover_percent**: Daily average cloud cover percentage

#### 4. Rolling Averages (10 features)
- **temperature_c_7day_avg**: 7-day rolling average of temperature
- **temperature_c_30day_avg**: 30-day rolling average of temperature
- **humidity_percent_7day_avg**: 7-day rolling average of humidity
- **humidity_percent_30day_avg**: 30-day rolling average of humidity
- **precipitation_mm_7day_avg**: 7-day rolling average of precipitation
- **precipitation_mm_30day_avg**: 30-day rolling average of precipitation
- **wind_speed_kmh_7day_avg**: 7-day rolling average of wind speed
- **wind_speed_kmh_30day_avg**: 30-day rolling average of wind speed
- **pressure_hpa_7day_avg**: 7-day rolling average of pressure
- **pressure_hpa_30day_avg**: 30-day rolling average of pressure

### Data Quality & Validation

The dataset has undergone rigorous quality assurance to ensure reliability:

#### Validation Checks Performed:
- **No Missing Values**: Every record is complete with all features populated
- **Realistic Temperature Range**: All temperatures fall within -15°C to 50°C
- **Valid Humidity Range**: Humidity values are between 20% to 100%
- **No Duplicate Records**: Each city-date combination is unique
- **Seasonal Pattern Validation**: Temperature variations follow expected seasonal patterns
- **City-Specific Climate Patterns**: Weather patterns reflect known climate characteristics of each city

#### Data Integrity Features:
- **Consistent Date Format**: All dates follow YYYY-MM-DD format
- **Verified Climate Trends**: Climate patterns are based on verified meteorological data
- **Monsoon Pattern Modeling**: Cities with monsoon climates show appropriate seasonal variations
- **Realistic Precipitation Patterns**: Rainfall distributions match expected climatic patterns
- **Daily Granularity**: All data is at daily resolution for detailed analysis

### Statistical Summary

The dataset exhibits rich statistical characteristics suitable for machine learning:

#### Temperature Distribution:
- **Mean**: 22.5°C
- **Standard Deviation**: 9.8°C
- **Minimum**: -7.7°C (Tokyo winter)
- **Maximum**: 47.5°C (Dubai summer)

#### Humidity Distribution:
- **Mean**: 75.2%
- **Standard Deviation**: 15.3%
- **Minimum**: 31% (Dubai)
- **Maximum**: 100% (Various tropical cities)

#### Precipitation Distribution:
- **Mean**: 4.2mm/day
- **Maximum**: 147mm/day (Mumbai monsoon)

#### Wind Speed Distribution:
- **Mean**: 9.8 km/h
- **Maximum**: 29.5 km/h

#### Pressure Distribution:
- **Mean**: 1013.2 hPa
- **Range**: 980.2 - 1040.1 hPa

### Applications & Use Cases

This dataset is suitable for numerous applications:

#### 1. Weather Forecasting
- **Short-term Prediction**: 1-7 day ahead weather forecasting
- **Medium-term Forecasting**: 30-day weather pattern prediction
- **Long-term Climate Analysis**: Decadal climate trend analysis

#### 2. Machine Learning Projects
- **Time Series Forecasting**: ARIMA, SARIMA, Prophet, LSTM models
- **Multi-output Regression**: Predicting multiple weather variables simultaneously
- **Ensemble Methods**: Random Forest, XGBoost, Gradient Boosting
- **Deep Learning**: RNN, GRU, Transformer models
- **Feature Engineering**: Developing custom features for improved predictions

#### 3. Research Applications
- **Climate Change Studies**: Analysis of temperature and precipitation trends
- **Urban Climate Research**: Studying micro-climate effects in cities
- **Extreme Weather Analysis**: Identifying patterns in extreme weather events
- **Cross-Climate Analysis**: Comparing weather patterns across different climate zones

#### 4. Educational Purposes
- **Data Science Education**: Teaching time series analysis and forecasting
- **Statistics Courses**: Demonstrating statistical analysis on real-world data
- **Meteorology Studies**: Understanding climate patterns and weather systems
- **Machine Learning Courses**: Practical experience with regression and forecasting

### Recommended Models & Approaches

#### Traditional Time Series Models:
- **ARIMA (AutoRegressive Integrated Moving Average)**
- **SARIMA (Seasonal ARIMA)**
- **Prophet (Facebook's Time Series Tool)**
- **Exponential Smoothing Models**

#### Machine Learning Models:
- **Random Forest Regressor**
- **XGBoost Regressor**
- **Gradient Boosting**
- **Support Vector Regression**
- **Multi-Output Regression Models**

#### Deep Learning Models:
- **LSTM (Long Short-Term Memory)**
- **GRU (Gated Recurrent Units)**
- **Bi-LSTM (Bidirectional LSTM)**
- **Transformers**
- **Attention Mechanisms**

#### Ensemble Methods:
- **Stacking**
- **Bagging**
- **Voting Regressors**

### Sample Implementation

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv('asia_weather_prediction_dataset.csv')

# Prepare features and targets
features = ['temperature_c_7day_avg', 'humidity_percent_7day_avg', 
            'precipitation_mm_7day_avg', 'wind_speed_kmh_7day_avg',
            'pressure_hpa_7day_avg', 'day_of_year', 'month']
targets = ['temperature_c', 'humidity_percent', 'precipitation_mm', 
           'wind_speed_kmh', 'pressure_hpa']

# Split data
X = df[features]
y = df[targets]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
rmse = np.sqrt(mean_squared_error(y_test, predictions))
print(f'RMSE: {rmse:.2f}')

출처: Kaggle (aliahmadmphil/asia-weather-prediction-dataset-15-cities)
태그: asia, environment, weather and climate, time series analysis, random forest
라이선스: Apache 2.0
수정일: 2026-07-29T13:14:29.550Z
