# car-price-classification-ready-data

300 Global Vehicles with Engineered Features for ML Price Classification & EDA

# 🚗 Car Price Classification Ready Dataset

A comprehensive **feature-engineered automotive dataset** containing 300 synthetic vehicle records from 10 major global manufacturers. This dataset is specifically prepared for **machine learning classification** and **exploratory data analysis** tasks.

---

## 📊 Dataset Overview

| Attribute | Value |
|-----------|-------|
| **Records** | 300 vehicles |
| **Features** | 16 (11 original + 5 engineered) |
| **Time Period** | 2005 - 2025 |
| **Brands** | Toyota, Honda, BMW, Mercedes, Audi, Ford, Tesla, Nissan, Hyundai, Kia |
| **Countries** | Germany, Japan, USA, China, UK, South Korea |

---

## 🔧 Features

### Original Features (11)
- `Car_ID` - Unique identifier
- `Brand` - Manufacturer name
- `Manufacture_Year` - Year of production
- `Body_Type` - SUV, Sedan, Coupe, Hatchback, Pickup
- `Fuel_Type` - Petrol, Diesel, Electric, Hybrid
- `Transmission` - Automatic, Manual
- `Engine_CC` - Engine displacement (1000-5000 cc)
- `Horsepower` - Engine power (70-600 HP)
- `Mileage_km_per_l` - Fuel efficiency (10-30 km/l)
- `Price_USD` - Vehicle price ($5,000 - $120,000)
- `Manufacturing_Country` - Country of manufacture

### Engineered Features (5)
- `Car_Age` - Years since manufacture (2026 - Year)
- `Price_Category` - **Classification Target** (Budget, Mid-Range, Premium, Luxury)
- `HP_per_CC` - Power-to-displacement ratio
- `Age_Category` - Vehicle age group (New, Recent, Moderate, Old)
- `Efficiency_Score` - Normalized fuel efficiency (0-1)

---

## 🎯 Use Cases

1. **Price Category Classification** - Predict Budget/Mid-Range/Premium/Luxury
2. **Price Regression** - Predict exact vehicle price
3. **EDA Practice** - Learn exploratory data analysis techniques
4. **Feature Engineering Demo** - Understand derived feature creation
5. **Market Segmentation** - Cluster analysis by vehicle attributes

---

## 📁 Files Included

- `global_cars_enhanced.csv` - Main dataset with all 16 features
- `global_cars_dataset_synthetic.csv` - Original raw dataset (11 features)

---

## 🏷️ Price Categories Definition

| Category | Price Range (USD) |
|----------|-------------------|
| Budget | &lt; $30,000 |
| Mid-Range | $30,000 - $59,999 |
| Premium | $60,000 - $89,999 |
| Luxury | ≥ $90,000 |

---

## 📚 Acknowledgements

- **Author:** Tatheer Abbas
- **Created:** February 2026
- **License:** CC0: Public Domain

---

## 💡 Getting Started

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('global_cars_enhanced.csv')

# Quick overview
print(df.shape)
print(df['Price_Category'].value_counts())

출처: Kaggle (tatheerabbas/car-price-classification-ready-data)
태그: automobiles and vehicles, beginner, data visualization, classification, tabular
라이선스: CC0: Public Domain
수정일: 2026-02-05T13:39:39.350Z
