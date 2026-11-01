# Korean Traditional Liquor Dataset

Korean Liquor Dataset: 3,519 entries collected from 132 historical manuscripts

## 📖 Description

This dataset contains structured information on Korean traditional liquors and brewing culture, collected from 132 historical texts extracted from Korean traditional liquor texts written between 886 and 1947.
It provides both text data and metadata suitable for NLP, cultural studies, and historical research.

## 📊 Dataset Overview

Documents: 132 historical texts extracted from Korean traditional liquor texts written between 886 and 1947.

Entries: 3,519 total records

🍶 Traditional liquors: 2,876

🍞 Fermentation starters (Nuruk, traditional yeast): 193

📦 Others (brewing secrets, utensils, drinking culture, etc.): 450

## 📏 Units & Terminology

| Term | Description |
|------|-------------|
| **Doi (되)** | A traditional Korean unit of grain volume used during the Joseon dynasty. ≈ about 1/10 of a Mal, roughly **1.8 liters** (estimated). |
| **Mal (말)** | A larger traditional grain volume unit. 1 Mal ≈ **18 liters**. |
| **Nuruk (누룩)** | A traditional Korean **starter** made of grains, used for fermentation. Functions similarly to yeast/mold starters in brewing. |
| **Hot Mixing (온혼)** | Brewing process involving mixing ingredients with **hot water**. |
| **Cold Mixing (냉혼)** | Brewing process involving mixing ingredients with **cold water**. |


## 📑 Schema

### `sool_chunks.jsonl`
| field          | type    | description |
|----------------|---------|-------------|
| `chunk_id`     | string  | Chunk ID |
| `parent_doc_id`| string  | Parent document ID |
| `title`        | string  | Title |
| `section`      | string  | Section name |
| `text`         | string  | Chunk text |
| `metadata`     | object  | Additional metadata (JSON) |

---

### `sool_steps.csv` / `sool_steps.parquet`
| field              | type    | description |
|--------------------|---------|-------------|
| `doc_id`           | string  | Document ID |
| `book`             | string  | Source book |
| `title`            | string  | Document title |
| `liq`              | string  | Liquor name/type |
| `section`          | string  | Section name |
| `start_day`        | int     | Start day |
| `ferment_days`     | int     | Fermentation days |
| `rice_doi`         | float   | Rice (되, Doi) |
| `rice_mal`         | float   | Rice (말, Mal) |
| `water_doi`        | float   | Water (되, Doi) |
| `water_mal`        | float   | Water (말, Mal) |
| `water_L`          | float   | Water (Liter) |
| `nuruk_doi`        | float   | Nuruk (되, Doi) |
| `nuruk_mal`        | float   | Nuruk (말, Mal) |
| `processing`       | string  | Processing method |
| `nuruk_form`       | string  | Nuruk form |
| `sprinkling_water` | bool    | Sprinkling water flag |
| `hot_mixing`       | bool    | Hot mixing flag |
| `cold_mixing`      | bool    | Cold mixing flag |
| `notes`            | string  | Notes |
| `has_glutinous`    | bool    | Glutinous rice present |
| `has_non_glutinous`| bool    | Non-glutinous rice present |

---

### `sool_docs.csv` / `sool_docs.parquet`
| field                  | type    | description |
|-------------------------|---------|-------------|
| `doc_id`               | string  | Document ID |
| `book`                 | string  | Source book |
| `title`                | string  | Title |
| `liq`                  | string  | Liquor name/type |
| `hanja`                | string  | Hanja (classical Chinese) form |
| `description`          | string  | Description |
| `main_category`        | string  | Main category |
| `main_category_en`     | string  | Main category (EN) |
| `entry_type`           | string  | Entry type |
| `level1` ~ `level4`    | string  | Category levels |
| `level1_en` ~ `level4_en` | string | Category levels (EN) |
| `source_categories`    | string  | Source categories |
| `source_categories_en` | string  | Source categories (EN) |
| `year_guess`           | int     | Estimated year |
| `rice_total_doi`       | float   | Total rice (되, Doi) |
| `rice_total_mal`       | float   | Total rice (말, Mal) |
| `water_total_doi`      | float   | Total water (되, Doi) |
| `water_total_mal`      | float   | Total water (말, Mal) |
| `water_total_L`        | float   | Total water (Liter) |
| `nuruk_total_doi`      | float   | Total nuruk (되, Doi) |
| `nuruk_per_mal`        | float   | Nuruk per Mal ratio |
| `num_stages`           | int     | Number of stages |
| `is_multi_stage`       | bool    | Multi-stage brewing flag |
| `filter_on_or_after_day` | int   | Filtering day (estimated) |
| `yield_mal`            | float   | Yield (말, Mal) |
| `yield_L`              | float   | Yield (Liter) |
| `water_per_rice_mal`   | float   | Water per rice Mal |
| `yield_per_rice_mal`   | float   | Yield per rice Mal |
| `uses_nuruk`           | bool    | Uses nuruk flag |
| `hot_mixing`           | bool    | Hot mixing flag |
| `cold_mixing`          | bool    | Cold mixing flag |
| `has_glutinous_rice`   | bool    | Glutinous rice present |
| `has_non_glutinous_rice` | bool  | Non-glutinous rice present |
| `stage_names`          | string  | Stage names |
| `unique_nuruk_forms`   | string  | Unique nuruk forms |
| `text_len_chars`       | int     | Text length (chars) |
| `text_len_words`       | int     | Text length (words) |
| `title_len_chars`      | int     | Title length |
| `has_hanja`            | bool    | Hanja present flag |
| `has_digits`           | bool    | Digits present flag |
| `has_original`         | bool    | Has original text |
| `has_translation`      | bool    | Has translation |
| `created_at`           | string  | Creation date |

---

## 🔍 Potential Use Cases

NLP tasks: information retrieval, RAG (retrieval-augmented generation), classification

Cultural & historical analysis: Korean drinking culture, brewing processes, and regional differences

Digital humanities: linking textual corpora with brewing practices

## 🛠 Preprocessing

The dataset was generated using a custom **Korean Sool Preprocessor**, which:
1. Normalizes brewing steps (e.g., fermentation, rice type, water, nuruk).
2. Generates derived statistics (yields, ratios, flags, text length).
3. Adds English category labels for consistency.
4. Outputs multiple formats for flexible use (JSONL, CSV, Parquet).

For reproducibility, preprocessing scripts are available here:  
👉 [GitHub Repository](https://github.com/Jaeuk-Han/korean-traditional-liquor-dataset)

## 🔗 Source

Originally provided by the Korean Traditional Liquor DB,
maintained by the Korean Traditional Liquor Research Institute (한국술문헌연구소).

Data source: [KoreanSool Archive](http://www.koreansool.kr/ktw/php/home.php)

## ⚖️ License

This dataset is distributed under CC BY-NC-SA 4.0 KR.

Non-commercial use only

Attribution required

Share-alike permitted

출처: Kaggle (jaeukhan/korean-traditional-liquor-dataset)
태그: culture and humanities, alcohol, earth and nature, history, nlp, korean
라이선스: CC BY-NC-SA 4.0
수정일: 2025-08-19T06:10:51.030Z
