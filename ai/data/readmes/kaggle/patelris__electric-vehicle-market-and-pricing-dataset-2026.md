# 📊 EV Market Analytics Dataset

2000 EV models with prices, specs, range, sales & ratings

## Overview
Complete and realistic EV market dataset with comprehensive pricing, specifications, and sales data. Perfect for price prediction modeling, market analysis, and EV comparison studies.

**Dataset Size:** 2,000 EV models/variants  
**Time Period:** 2020-2026  
**Geographic Coverage:** Global (20 major EV manufacturers)

## Dataset Description

### Column Definitions

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| **brand** | categorical | 20 brands | Tesla, BYD, Rivian, Lucid, NIO, Hyundai, Kia, BMW, Mercedes, Audi, Volkswagen, Ford, GM/Chevrolet, Toyota, Polestar, Fisker, Porsche, Volvo, Xiaomi, Honda |
| **model** | categorical | ~5/brand | Tesla Model 3/Y/S/X/Cybertruck, BYD Seagull/Qin/Atto 3, Rivian R1T/R1S, etc. |
| **year** | integer | 2020-2026 | Model year (weighted toward recent years) |
| **variant** | categorical | 5 types | Base, Standard, Long Range, Performance, Premium |
| **price_usd** | float | $25K-$200K | **TARGET VARIABLE** - Realistic pricing based on brand, model, variant, year |
| **battery_capacity_kwh** | float | 40-120 | Battery size (correlated with range) |
| **range_miles** | float | 150-450 | EPA/WLTP range (strongly correlated with battery) |
| **charging_speed_kw** | float | 50-350 | DC fast charging capability |
| **acceleration_0_60_mph** | float | 2.0-8.0 | 0-60 seconds (performance variants faster) |
| **top_speed_mph** | float | 100-200 | Maximum speed capability |
| **horsepower** | integer | 150-1000 | Total system power |
| **torque_nm** | integer | 200-1200 | Maximum torque in Newton-meters |
| **drive_type** | categorical | 3 types | AWD, FWD, RWD |
| **seating_capacity** | integer | 2-7 | Number of passenger seats |
| **body_type** | categorical | 6 types | Sedan, SUV, Truck, Hatchback, Coupe, Van |
| **cargo_volume_cubic_ft** | float | 15-80 | Trunk/cargo space |
| **weight_kg** | float | 1500-3000 | Vehicle curb weight |
| **safety_rating** | integer | 3-5 | NCAP safety stars (most EVs: 4-5) |
| **autopilot_level** | integer | 0-3 | SAE automation level (Tesla/Mercedes: 2-3) |
| **country_of_origin** | categorical | 6 | US, China, Germany, South Korea, Sweden, Japan |
| **market_segment** | categorical | 4 | Budget, Mid-range, Premium, Luxury |
| **annual_sales_units** | integer | 500-500K | Annual production volume |
| **customer_rating** | float | 3.0-5.0 | Customer satisfaction (correlated with range) |
| **warranty_years** | integer | 3-8 | Warranty period |

## Data Characteristics

### Realism Features
- **Brand Distribution:** Tesla (20%), BYD (15%), weighted realistically by market share
- **Pricing Logic:** Brand+model+variant+year factors with realistic tier structure
  - German luxury: Premium pricing with advanced features ($50K-$150K)
  - Tesla: Leader in volume (Model Y) with consistent pricing
- **Battery-Range Correlation:** Range = Battery × 3.5 (+ noise), mimics real physics
- **Performance Variants:** 0-60 times 2.5-4.5s for Performance; 5.0-8.0s for Base
- **Range Anxiety Reality:** Customer rating strongly correlates with range (longer = higher rating)
- **Charging Speed:** Premium brands (Tesla, Lucid, Porsche) offer 200-350 kW; others 50-150 kW
- **Automation Levels:** Tesla/Mercedes get SAE L2-L3; most others L0-L1
- **Year Trend:** More 2024-2026 models; newer = slightly higher prices
- **Warranty Patterns:** Luxury brands (3-8 yrs), mass market (3-5 yrs)

## Generation Method

**Script:** `build_ev_dataset.py`  
**Random Seed:** 42 (reproducible)  
**Libraries:** NumPy, Pandas  
**Execution Time:** <1 second  

Run the script:
```bash
python build_ev_dataset.py
```

Output: `ev_market_2026.csv` (2,000 rows × 22 columns)

## Key Statistics

- **Price Distribution:** $25,001 (min) to $199,876 (max), median ~$52,000
- **Range Distribution:** 150 to 450 miles (most 200-350)
- **Battery Capacity:** 40-120 kWh (larger batteries → premium variants)
- **Customer Rating:** 3.0-5.0 (average ~4.2, correlated with range & brand)
- **Sales Volume:** Tesla Model Y dominates (400K-500K units/year)
- **Market Segment Distribution:** Budget (25%), Mid-range (40%), Premium (25%), Luxury (10%)

## Use Cases & Analysis Ideas

### 1. **EV Price Prediction**
Build regression models to predict price from specs:
- Features: battery_capacity, range, horsepower, brand, variant, year
- Baseline: Linear regression, then try XGBoost/Neural Networks
- Target: Minimize MAE on test set

### 2. **Range vs. Price — Value Analysis**
Which EVs offer the best range-per-dollar?
- Create efficiency metric: range_miles / price_usd
- Identify budget best-sellers vs. luxury overpriced models

### 3. **Brand Comparison Dashboard**
Compare brands across multiple dimensions:
- Avg price, range, charging speed, customer rating
- Market segment distribution
- Year-over-year pricing trends
- Safety rating by brand

### 4. **Market Share & Sales Trends 2020-2026**
Analyze growth over 6 years:
- Total units sold by brand/year
- Market segment growth (Budget EVs growing fastest)
- Body type adoption trends
- Country of origin market penetration

### 5. **Battery Technology Evolution**
Track improvements 2020-2026:
- Average battery capacity per year
- Charging speed improvements
- Range per kWh efficiency gains
- Cost per kWh trajectory

### 6. **Customer Rating Prediction**
What drives customer satisfaction?
- Feature importance: range (strongest), warranty, charging speed, price value
- Correlation analysis: range, safety_rating, warranty, price_to_features ratio
- Segment analysis: which segments have highest ratings?

### 7. **Which Specs Matter Most for Sales?**
Regression analysis of annual_sales_units:
- Do faster 0-60 times drive sales? (Usually not for budget)
- Range importance by price tier
- Brand loyalty vs. specs
- Safety rating impact on volume

### 8. **Budget EV vs. Luxury — Feature Gap Analysis**
Compare Budget (<$35K) vs. Luxury (>$100K):
- Range gap: 200 mi (budget) vs. 350 mi (luxury)
- Charging: 80 kW vs. 250 kW
- Performance: 6.5s vs. 3.0s (0-60)
- Feature gaps → justify the price premium?
- Value segments emerging (mid-range quality at budget prices)

## Data Quality Notes

- **No missing values:** Dataset is complete
- **Realistic correlations:** Battery↔range, price↔specs, brand↔safety/charging
- **Range anxiety reflected:** Lower range = lower customer ratings
- **Market realism:** Tesla Model Y dominates sales; luxury brands rare
- **Variant pricing:** Performance > Long Range > Standard > Base
- **Year trends:** 2024-2026 represents 71% of inventory (current market)

## Files

- `ev_market_2026.csv` — Full dataset (2,000 rows)
- `build_ev_dataset.py` — Generation script (seed=42)
- `README.md` — This documentation

출처: Kaggle (patelris/electric-vehicle-market-and-pricing-dataset-2026)
태그: automobiles and vehicles, beginner, data visualization, data analytics, regression
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-05-13T04:15:20.587Z
