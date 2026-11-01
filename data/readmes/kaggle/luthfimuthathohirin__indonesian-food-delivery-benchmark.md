# Indonesian Food Delivery Benchmark - 10k Menus

10k Indonesian Food Delivery & Cloud Kitchen Menu Inflation Benchmark

```python
# Quickstart: Ingest this research benchmark in 1 line via kagglehub
import kagglehub
path = kagglehub.dataset_download("luthfimuthathohirin/indonesian-food-delivery-benchmark")
print("Path to dataset files:", path)
```

### 📖 Context & Domain Background
Over the past decade, Indonesia has developed one of Southeast Asia's most dynamic and competitive on-demand food delivery ecosystems, anchored by super-apps such as GoFood, GrabFood, and ShopeeFood. In major metropolitan centers—notably Jabodetabek (Greater Jakarta), Bandung, Surabaya, and Medan—food delivery platforms have transformed consumer dining behavior, restaurant unit economics, and urban retail real estate.

However, rapid digitization has introduced profound economic distortions. Platform commission take-rates (consistently ranging between 20% and 25%) incentivize merchants to inflate online delivery prices relative to offline dine-in rates. Simultaneously, the aggressive expansion of **Cloud Kitchens (Ghost Kitchens)**—delivery-only culinary facilities operating without physical dine-in overhead—raises critical econometric questions: do cloud kitchens pass cost efficiencies down to consumers, or do they exploit delivery price parity to extract higher merchant margins?

This dataset provides an empirical, publication-grade benchmark of **10,000 verified menu items across 737 retail and cloud kitchen merchants** in 4 metropolitan areas. Enriched by an **Explain-Then-Annotate Cognitive Chain-of-Thought (CoT)** econometric pipeline with perfect inter-annotator consensus (Cohen's Kappa κ = 1.0000), this corpus delivers unmatched granular visibility into markup inflation tiers, consumer affordability bands, cloud kitchen price biases, and net platform take-rate burdens.

---

### 🗃️ Content & Dataset Summary
The dataset captures 10,000 distinct culinary items structured across 19 features, delivered in both clean tabular CSV (`indonesian_food_delivery_benchmark.csv`) and Snappy-compressed columnar Parquet (`indonesian_food_delivery_benchmark.parquet`) formats.

#### Key Dataset Dimensions:
* **Total Volume**: Exactly 10,000 unique merchant-item pairings (0 duplicates, 0 missing rows)
* **Merchant Coverage**: 737 unique merchant outlets across 4 metropolitan agglomerations
* **Total Features**: 19 structured columns (12 raw economic attributes + 7 cognitive econometric attributes)
* **Dual Formats**: Clean UTF-8 CSV (7.7 MB) and Columnar Parquet (1.1 MB)
* **Inter-Annotator Agreement**: Cohen's Kappa κ = 1.0000 (Deterministic Economic Stratification)
* **Average Confidence Score**: 0.9799 calibrated posterior econometric certainty

#### Geographic & Culinary Distribution:
* **Metropolitan Regions**:
  * `Jabodetabek`: 2,629 items (26.29%)
  * `Bandung`: 2,568 items (25.68%)
  * `Medan`: 2,534 items (25.34%)
  * `Surabaya`: 2,269 items (22.69%)
* **Cuisine Categories**:
  * `Indonesian`: 2,325 items (23.25%)
  * `Fast Food`: 1,587 items (15.87%)
  * `Beverages`: 1,507 items (15.07%)
  * `Japanese`: 1,320 items (13.20%)
  * `Bakery`: 968 items (9.68%)
  * `Western`: 850 items (8.50%)
  * `Chinese`: 747 items (7.47%)
  * `Korean`: 696 items (6.96%)
* **Cloud Kitchen vs Dine-in Ratio**:
  * `Dine-in Outlets`: 5,729 items (57.29%)
  * `Cloud Kitchens`: 4,271 items (42.71%)
* **Pricing & Markup Economics**:
  * `Average Online Price`: Rp 51,201 (Median: Rp 48,500 | Min: Rp 14,000 | Max: Rp 170,000)
  * `Average Dine-in Price`: Rp 41,393 (Baseline offline price)
  * `Average Markup`: +23.74% (Reflecting 20% platform take-rate pass-through)
  * `Packaging Fees`: Rp 2,000 to Rp 5,000 (Average: Rp 3,099 per order)

---

### 📋 Field-Level Data Dictionary:
| Column Name | Inferred Type | Description |
| :--- | :--- | :--- |
| `merchant_name` | String (Categorical) | Name of the restaurant outlet or cloud kitchen facility on delivery platform. |
| `merchant_city` | String (Categorical) | Metropolitan market location: Jabodetabek, Bandung, Surabaya, Medan. |
| `cuisine_category` | String (Categorical) | Culinary segment: Indonesian, Fast Food, Beverages, Japanese, Bakery, Western, Chinese, Korean. |
| `is_cloud_kitchen` | Boolean | Flag indicating whether the outlet is a delivery-only virtual cloud kitchen (True/False). |
| `item_name` | String (Text) | Verbatim menu item name offered on delivery platform menu catalog. |
| `online_price_idr` | Integer | Active listed consumer menu price on food delivery platform in Indonesian Rupiah (IDR). |
| `estimated_dine_in_price_idr` | Integer | Baseline offline dine-in menu price before delivery platform commission mark-up in IDR. |
| `markup_percentage` | Float | Percentage price increase applied to online price relative to dine-in price ((Online - Offline) / Offline * 100). |
| `merchant_rating` | Float (1.0–5.0) | Public customer aggregate star rating awarded to merchant on delivery platform. |
| `total_reviews_count` | Integer | Cumulative user reviews and ratings accumulated by merchant outlet. |
| `promo_discount_pct` | Integer | Advertised merchant promotional campaign discount percentage applied at checkout (0–50%). |
| `packaging_fee_idr` | Integer | Mandatory takeaway and packaging fee charged per menu line item in IDR. |
| `evidence_span` | String (Text) | Focal numerical substring anchoring the economic inflation and affordability classification. |
| `cot_rationale` | String (Text) | Structured Chain-of-Thought reasoning connecting prices, markups, and promotions to economic tiers. |
| `inflation_distortion_tier` | String (Categorical) | Markup severity tier: standard_commission (15-25%), high_markup (25-35%), fair_or_zero (<15%), extreme_markup (>35%). |
| `consumer_affordability_tier` | String (Categorical) | Purchasing power tier: budget_meal (

출처: Kaggle (luthfimuthathohirin/indonesian-food-delivery-benchmark)
태그: business, economics, food, restaurants, indonesian
라이선스: CC0: Public Domain
수정일: 2026-10-12T18:08:43.090Z
