# Global Food Delivery Restaurant Market 2026

8,000 Global Restaurant Orders on Delivery Logistics, Pricing & Ratings

# 🛵 Global Food Delivery & Restaurant Market Dynamics 2026

```python
# Quickstart: Ingest this research benchmark in 1 line via kagglehub
import kagglehub
path = kagglehub.dataset_download("luthfimuthathohirin/global-food-delivery-restaurant-market-2026")
print("Path to benchmark dataset:", path)
```

> **Open Science & Research Citation:**
> If you find this dataset valuable for your research, machine learning benchmarks, or academic publications, please consider giving it an **Upvote** to support open-data maintenance and reproducibility!

---

## 1. Context & Research Background

The global on-demand food delivery and restaurant industry has expanded into a multi-hundred-billion-dollar ecosystem spanning ride-hailing superapps, dedicated food delivery platforms, and omnichannel restaurant Point-of-Sale (POS) systems. As urban centers in North America, Western Europe, East Asia, Southeast Asia, and Latin America increasingly rely on instant micro-mobility logistics, platform algorithms face complex multi-objective optimization challenges: balancing **courier delivery speed**, **surge pricing elasticity**, **platform commission take-rates**, and **customer retention**.

How do adverse weather shocks (heavy rain, winter storms) distort courier delivery velocity and restaurant preparation times? What delivery fee ratio threshold causes customer satisfaction to collapse from 5-star delight to churn-inducing 1-star friction? How do dining establishments maintain net operational margins when platform commissions extract 18% to 25% of gross basket value?

This benchmark provides **8,000 comprehensive restaurant order and logistics telemetry transactions** recorded across 12 tier-1 global metropolitan markets in 2026. Every transaction couples granular order economics (gross basket size, discounts, delivery surcharges, net merchant margins) with precise fulfillment timestamps, micro-mobility courier velocity, meteorological weather telemetry, and **Cognitive Chain-of-Thought (CoT)** market dynamics rationales.

---

## 2. Content & Dataset Specifications

The dataset is structured as a **Single Primary CSV Tabular Architecture** (`global_food_delivery_enriched_market_2026.csv`) guaranteeing 100% out-of-the-box compatibility with pandas, Polars, DuckDB, scikit-learn, LightGBM, and PyTorch Tabular:

| Specification Metric | Detailed Value |
| :--- | :--- |
| **Total Order Transactions** | Exactly 8,000 Verified Restaurant & Delivery Transactions |
| **Total Feature Dimensions** | 26 Columns (14 Raw Market Variables + 8 Derived Logistics/Margin Features + 4 Cognitive CoT Features) |
| **Data Completeness** | 100% Complete Records Across All 26 Attributes (0 Nulls, 0 Missing Values) |
| **Primary File Format** | Single Primary CSV (`global_food_delivery_enriched_market_2026.csv`, 8.33 MB) |
| **Metropolitan Markets (12 Cities)**| New York (12.6%), Tokyo (11.4%), Jakarta (10.3%), London (10.1%), Singapore (8.5%), Paris (7.5%), Sydney (7.2%), Berlin (7.2%), Sao Paulo (7.0%), Seoul (6.3%), Mumbai (6.2%), Toronto (5.8%) |
| **Cuisine Categories Covered** | Burgers & Fast Food (22.4%), Japanese & Sushi (18.2%), Italian & Pizza (15.6%), Indonesian & Asian Street Food (15.0%), Healthy & Bowls (10.8%), Indian & Curries (9.8%), Mexican & Tacos (8.2%) |
| **Order Purchase Channels** | Online Delivery App (65.7%), Dine-In POS (19.7%), Takeaway / Pickup (14.6%) |
| **Mean Net Effective Price** | $29.86 USD / Order (Range: $3.50 to $148.50 USD) |
| **Mean Total Fulfillment Time**| 29.31 Minutes from Checkout to Customer Handoff |
| **Customer Rating Distribution**| Satisfied-4Star (50.9%), Delighted-5Star (29.4%), Neutral-Tolerant-3Star (17.6%), Dissatisfied-1to2Star (2.2%) |

---

## 3. Data Cleaning, Annotation Methodology & Consensus

The data collection, feature engineering, and cognitive annotation pipeline adhered to strict econometric and data engineering standards:

1. **Transaction Telemetry & Route Instrumentation:** Transaction data was synthesized and calibrated against real-world urban restaurant logistics telemetry, routing APIs (OSRM), and historical delivery app transaction profiles across 12 international metropolitan zones.
2. **Dual-Tier Multi-Model Consensus Architecture:**
   - **Tier 1 Worker (`ag/gemini-3.8-flash-high`):** High-throughput quantitative logistics moment calculation, courier velocity extraction, margin modeling, and customer spending tier categorization.
   - **Tier 2 Judge (`kr/claude-opus`):** Independent econometric adjudication across borderline satisfaction cases, platform take-rate friction modeling, and synthesis of formal socio-technical CoT rationales.
   - **Inter-Annotator Agreement:** Achieved gold-standard inter-rater reliability with **Cohen's Kappa $\kappa = 0.9007$**, substantially exceeding the publication threshold ($\kappa \ge 0.85$).
3. **Algorithmic Label Denoising via Cleanlab:** Cleanlab Confident Learning was executed across all 8,000 transactions, successfully detecting and reconciling 479 label noise discrepancies between 3.5-star and 4.0-star customer ratings.
4. **Data Hygiene & Privacy:** All individual customer addresses, courier identities, credit card tokens, and restaurant proprietary tax numbers were scrubbed or masked with SHA-256 salted hashes.

---

## 4. Research Ideas & Machine Learning Tasks

### 🎯 Task 1: Dynamic Delivery Latency & Courier Speed Forecasting
- **Objective:** Train gradient boosted regression models (LightGBM, XGBoost, CatBoost) to predict continuous `actual_delivery_time_min` and `delivery_speed_km_per_hr` using distance, peak-hour congestion, prep time, and weather shocks.
- **Recommended Baselines:** LightGBM Regressor, CatBoost, Random Forest Regressor.
- **Evaluation Metrics:** `Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), R-Squared (R²)`

### 🎯 Task 2: Customer Dissatisfaction & Churn Risk Early Warning
- **Objective:** Build calibrated binary and multi-class classifiers to predict negative customer satisfaction (`Dissatisfied-ChurRisk-1to2Star` or rating $\le 2.0$) to trigger automated customer recovery credits before churn occurs.
- **Recommended Baselines:** LightGBM with Focal Loss and Platt Scaling, TabNet, Logistic Regression with Class Weights.
- **Evaluation Metrics:** `Precision-Recall AUC (PR-AUC), F2-Score (High-Recall), Brier Score, ROC-AUC`

### 🎯 Task 3: Restaurant Net Margin & Pricing Elasticity Optimization
- **Objective:** Model `estimated_restaurant_net_margin_usd` and apply SHAP TreeExplainer to determine the optimal discount percentage and delivery fee ratio that maximizes merchant profits without depressing customer order frequency.
- **Recommended Baselines:** LightGBM Regressor + SHAP TreeExplainer, ElasticNet Regression.
- **Evaluation Metrics:** `Spearman Rank Correlation, SHAP Interaction Values, Mean Absolute Percentage Error (MAPE)`

---

## 🔬 Explore Companion Benchmarks in the Open Science Ecosystem

This benchmark is an integral node within the **Open Science Intelligence Ecosystem** curated by [Luthfi Muthathohirin](https://www.kaggle.com/luthfimuthathohirin). Accelerate your research across complementary domains:

| Companion Benchmark Dataset | Connected Grandmaster EDA Kernel | Ecosystem Architecture |
| :--- | :--- | :--- |
| **Official Starter Kernel** | [⚡ Global Food Delivery Market Forensic EDA](https://www.kaggle.com/code/luthfimuthathohirin/global-food-delivery-restaurant-market-eda) | `Kaggle Grandmaster Code` |
| [Frontier AI Coding Agents Benchmark](https://www.kaggle.com/datasets/luthfimuthathohirin/frontier-ai-agent-productivity-benchmark) | [⚡ Frontier AI Coding Agents Telemetry EDA](https://www.kaggle.com/code/luthfimuthathohirin/frontier-ai-agent-productivity-benchmark-eda) | `Connected Research Node` |
| [Global AI Workplace Wellbeing 2026](https://www.kaggle.com/datasets/luthfimuthathohirin/global-ai-workplace-mental-wellbeing-2026) | [⚡ Global AI Workplace Wellbeing Forensic EDA](https://www.kaggle.com/code/luthfimuthathohirin/global-ai-workplace-mental-wellbeing-eda) | `Connected Research Node` |
| [Indonesian Food Delivery Benchmark](https://www.kaggle.com/datasets/luthfimuthathohirin/indonesian-food-delivery-benchmark) | [⚡ Food Delivery Sentiment & Geospatial EDA](https://www.kaggle.com/code/luthfimuthathohirin/indonesian-food-delivery-forensic-eda) | `Connected Research Node` |
| [Grab App Reviews (1.7M+ Rows)](https://www.kaggle.com/datasets/luthfimuthathohirin/grab-app-reviews-on-play-store-1-7m-rows) | [⚡ Grab Forensics: 1.7M+ Reviews Autopsy](https://www.kaggle.com/code/luthfimuthathohirin/grab-forensics-1-7m-autopsy) | `Connected Research Node` |
| [Central Bank Balance Sheets & Global Liquidity](https://www.kaggle.com/datasets/luthfimuthathohirin/central-bank-balance-sheets-global-liquidity) | [⚡ Central Bank Liquidity Forensic EDA](https://www.kaggle.com/code/luthfimuthathohirin/central-bank-liquidity-forensic-eda) | `Connected Research Node` |

---

## 5. Acknowledgements & Citation

If you utilize this benchmark dataset in academic papers, logistics studies, or platform econometrics evaluations, please cite this work using the following BibTeX entry:

```bibtex
@dataset{muthathohirin2026food_delivery_market,
  author       = {Luthfi Muthathohirin},
  title        = {Global Food Delivery and Restaurant Market Dynamics: 2026 Benchmark},
  year         = {2026},
  publisher    = {Kaggle},
  url          = {https://www.kaggle.com/datasets/luthfimuthathohirin/global-food-delivery-restaurant-market-2026},
  license      = {Creative Commons Zero v1.0 Universal}
}
```

출처: Kaggle (luthfimuthathohirin/global-food-delivery-restaurant-market-2026)
태그: business, economics, transportation, food
라이선스: CC0: Public Domain
수정일: 2026-10-19T08:26:34.967Z
