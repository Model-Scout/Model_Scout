---
language:
- ko
license: cc-by-nc-sa-2.0
pretty_name: "Korean Traditional Liquor Corpus (886–1947)"
size_categories:
- 10K<n<100K
task_categories:
- text-retrieval
- question-answering
- text-classification
- summarization
annotations_creators:
- no-annotation
source_datasets:
- original
multilinguality:
- monolingual
---

# Dataset Card for Korean Traditional Liquor Corpus (886–1947)

## Dataset Summary
A corpus of Korean traditional liquors and brewing culture curated from **132 historical texts** written between **886 and 1947**. It includes paragraph-level chunks for IR/RAG and document-/process-level metadata for cultural and historical analyses.

- **Documents**: 132 historical texts (886–1947)  
- **Entries**: 3,519 total  
  - 🍶 Traditional liquors: 2,876  
  - 🍞 Fermentation starters (Nuruk): 193  
  - 📦 Others (brewing secrets, utensils, drinking culture, etc.): 450

**Files**
- `sool_chunks.jsonl` — paragraph-level chunks (JSON Lines)
- `sool_docs.csv` / `sool_docs.parquet` — document-level metadata
- `sool_steps.csv` / `sool_steps.parquet` — brewing steps / process-level data (optional)

> CSV and Parquet mirror the same schema within each pair.

---

## Supported Tasks and Use Cases
- **Text Retrieval / RAG**: build BM25 / dense indexes on `sool_chunks`
- **Question Answering & Summarization**: cite `sool_docs` and step metadata
- **Classification / Taxonomy**: use category fields and derived stats
- **Digital Humanities**: study historical brewing practices and terminology

---

## Languages
- **Korean (ko)** with historical forms and occasional **Hanja**.

---

## Units & Terminology (historical)
| Term | Description |
|---|---|
| **Doi (되)** | Traditional volume; ≈ **1/10 Mal**, ~**1.8 L** (estimated). |
| **Mal (말)** | Traditional volume; **~18 L**. |
| **Nuruk (누룩)** | Grain-based enzymatic/microbial **starter** used for fermentation. |
| **Hot Mixing (온혼)** | Mashing/processing with **hot water**. |
| **Cold Mixing (냉혼)** | Mashing/processing with **cold water**. |

---

## Dataset Structure

### Files and Schemas

#### 1) `sool_chunks.jsonl`
Each line is one JSON object (a chunk).

| field | type | description |
|---|---|---|
| `chunk_id` | string | Chunk ID (unique) |
| `parent_doc_id` | string | Parent document ID (join with `sool_docs.doc_id`) |
| `title` | string | Title |
| `section` | string | Section/subheading |
| `text` | string | Chunk text |
| `metadata` | object | Additional metadata (JSON) |

**Example**
```json
{"chunk_id":"c_000001","parent_doc_id":"d_001","title":"Gyeongmyeon Nokpaju","section":"Brewing","text":"...chunk text...","metadata":{"page":12,"source":"산림경제"}}
```

---

#### 2) `sool_steps.csv` / `sool_steps.parquet`  *(optional)*
| field | type | description |
|---|---|---|
| `doc_id` | string | Document ID |
| `book` | string | Source book |
| `title` | string | Document title |
| `liq` | string | Liquor name/type |
| `section` | string | Section name |
| `start_day` | int | Start day |
| `ferment_days` | int | Fermentation days |
| `rice_doi` | float | Rice (Doi) |
| `rice_mal` | float | Rice (Mal) |
| `water_doi` | float | Water (Doi) |
| `water_mal` | float | Water (Mal) |
| `water_L` | float | Water (Liter) |
| `nuruk_doi` | float | Nuruk (Doi) |
| `nuruk_mal` | float | Nuruk (Mal) |
| `processing` | string | Processing method |
| `nuruk_form` | string | Nuruk form |
| `sprinkling_water` | bool | Sprinkling water flag |
| `hot_mixing` | bool | Hot mixing flag |
| `cold_mixing` | bool | Cold mixing flag |
| `notes` | string | Notes |
| `has_glutinous` | bool | Glutinous rice present |
| `has_non_glutinous` | bool | Non-glutinous rice present |

---

#### 3) `sool_docs.csv` / `sool_docs.parquet`
| field | type | description |
|---|---|---|
| `doc_id` | string | Document ID |
| `book` | string | Source book |
| `title` | string | Title |
| `liq` | string | Liquor name/type |
| `hanja` | string | Hanja (classical Chinese) form |
| `description` | string | Description |
| `main_category` | string | Main category |
| `main_category_en` | string | Main category (EN) |
| `entry_type` | string | Entry type |
| `level1` ~ `level4` | string | Category levels |
| `level1_en` ~ `level4_en` | string | Category levels (EN) |
| `source_categories` | string | Source categories |
| `source_categories_en` | string | Source categories (EN) |
| `year_guess` | int | Estimated year |
| `rice_total_doi` | float | Total rice (Doi) |
| `rice_total_mal` | float | Total rice (Mal) |
| `water_total_doi` | float | Total water (Doi) |
| `water_total_mal` | float | Total water (Mal) |
| `water_total_L` | float | Total water (Liter) |
| `nuruk_total_doi` | float | Total nuruk (Doi) |
| `nuruk_per_mal` | float | Nuruk per Mal ratio |
| `num_stages` | int | Number of stages |
| `is_multi_stage` | bool | Multi-stage brewing flag |
| `filter_on_or_after_day` | int | Filtering day (estimated) |
| `yield_mal` | float | Yield (Mal) |
| `yield_L` | float | Yield (Liter) |
| `water_per_rice_mal` | float | Water per rice Mal |
| `yield_per_rice_mal` | float | Yield per rice Mal |
| `uses_nuruk` | bool | Uses nuruk |
| `hot_mixing` | bool | Hot mixing flag |
| `cold_mixing` | bool | Cold mixing flag |
| `has_glutinous_rice` | bool | Glutinous rice present |
| `has_non_glutinous_rice` | bool | Non-glutinous rice present |
| `stage_names` | string | Stage names |
| `unique_nuruk_forms` | string | Unique nuruk forms |
| `text_len_chars` | int | Text length (chars) |
| `text_len_words` | int | Text length (words) |
| `title_len_chars` | int | Title length (chars) |
| `has_hanja` | bool | Hanja present |
| `has_digits` | bool | Digits present |
| `has_original` | bool | Has original text |
| `has_translation` | bool | Has translation |
| `created_at` | string | Creation timestamp |

---

## Loading the Dataset

### With `datasets`
```python
from datasets import load_dataset

ds = load_dataset(
    "Jaeuk-Han/korean-traditional-liquor-dataset",
    data_files={
        "chunks": "sool_chunks.jsonl",
        "docs": ["sool_docs.parquet", "sool_docs.csv"],
        "steps": ["sool_steps.parquet", "sool_steps.csv"],  # optional
    }
)

chunks = ds["chunks"]
docs = ds.get("docs")
steps = ds.get("steps")
chunks[0]
```

### With `huggingface_hub` + `pandas`
```python
from huggingface_hub import hf_hub_download
import pandas as pd, json

REPO_ID = "Jaeuk-Han/korean-traditional-liquor-dataset"

# docs (parquet preferred)
p_docs = hf_hub_download(REPO_ID, "sool_docs.parquet")
df_docs = pd.read_parquet(p_docs)

# steps (csv)
p_steps = hf_hub_download(REPO_ID, "sool_steps.csv")
df_steps = pd.read_csv(p_steps)

# chunks (jsonl)
p_chunks = hf_hub_download(REPO_ID, "sool_chunks.jsonl")
with open(p_chunks, "r", encoding="utf-8") as f:
    chunks = [json.loads(line) for line in f]
```

### Minimal Retrieval Example (toy TF-IDF)
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

texts = [c["text"] for c in chunks]
vec = TfidfVectorizer(min_df=2).fit(texts)
M = vec.transform(texts)

def search(q, topk=5):
    sims = cosine_similarity(vec.transform([q]), M).ravel()
    idx = sims.argsort()[::-1][:topk]
    return [chunks[i] for i in idx]

search("How is Gyeongmyeon Nokpaju brewed?", 5)
```

---

## Ethical Considerations & Limitations
- Reflects the **historical context** of its sources; some practices/descriptions may be culturally sensitive or misaligned with modern safety/ethical standards.  
- Provided **as a record**; it does **not** endorse any harmful practice.  
- For commercial use, confirm rights with the original sources and applicable policies.

---

## Source
Originally provided by the **Korean Traditional Liquor DB**, maintained by the **Korean Traditional Liquor Research Institute / 한국술문헌연구소**.  
Data source: http://www.koreansool.kr/ktw/php/home.php  
Blog: https://blog.naver.com/korean-sool

---

## Changes Made
Structured texts into JSONL/CSV/Parquet, normalized historical units (Mal/Doi → L), added English category labels, and derived per-document/step statistics.

---


## 🔁 Reproducibility & Code

- **Preprocessing repo**: https://github.com/Jaeuk-Han/korean-traditional-liquor-dataset  
- **Version pin**: use a tagged release (e.g., `v1.0.0`) or a specific commit SHA (recommended).  
- **Environment (example)**:
  ```bash
  python -V          # 3.10+ (3.11 recommended)
  pip install -r requirements.txt
  ```
- **Recreate (template)**:
  ```bash
  git clone https://github.com/Jaeuk-Han/korean-traditional-liquor-dataset
  cd korean-traditional-liquor-dataset
  git checkout <commit-sha-or-tag>

  # adjust paths/args to your environment
  python scripts/preprocess.py \
    --input ./raw_sources \
    --out_chunks ./out/sool_chunks.jsonl \
    --out_docs ./out/sool_docs.parquet \
    --out_steps ./out/sool_steps.parquet
  ```

### Checksums (for this release)
| file | size | sha256 |
|---|---:|---|
| `sool_chunks.jsonl` | 14.39 MB | `56dc4c10e0945149ee62365551c0cc80a0d185426921352643443e030084253f` |
| `sool_docs.csv` | 1.70 MB | `86444b22c156f14dc038747004fa026f487ee6618ed7b8f6d2d845fe394bb6bc` |
| `sool_docs.parquet` | 0.34 MB | `bdcfbeb4e983b3c2614778f8f5dbb6a3adc343091b4f66478eb1ddd2ec83e484` |
| `sool_steps.csv` | 1.81 MB | `3b3a9e01b7bcc42895ea69e576f4f030fa7ae9aa08c838f8e7f4f1c0bfc27b58` |
| `sool_steps.parquet` | 0.75 MB | `0f6d0fd16ef5195ae3784d454c37cfad079f7d320d4b66ed36b4640575fa6b1b` |

---

## Licensing Information
- **License**: **CC BY-NC-SA 2.0 (Korea, KR port)**  
  Canonical deed: https://creativecommons.org/licenses/by-nc-sa/2.0/kr/  
  You may share/adapt **non-commercially**, with **attribution**, and you must **share alike** under the **same license (or a later BY-NC-SA version)**.
- If you prefer to apply a later version for your **adaptation**, you may use **CC BY-NC-SA 4.0 International** (as permitted by ShareAlike for 2.0/2.5/3.0 materials); ensure no additional restrictions are added.

---

## Citation
If you use this dataset, please cite:
```
Han, Jaeuk. (2025). Korean Traditional Liquor Corpus (886–1947). Hugging Face Datasets. https://huggingface.co/datasets/Jaeuk-Han/korean-traditional-liquor-dataset
```

---

## Changelog
- **v1.0.0** — Initial release (`sool_chunks.jsonl`, `sool_docs.(csv|parquet)`, `sool_steps.(csv|parquet)`)

---

## Dataset Card Authors
- **Jaeuk Han** (maintainer)

**Sources** — Data was sourced from the *Korean Sool Historical DB / 한국술 고문헌 DB*, maintained by the *Korean Traditional Liquor Research Institute / 한국술문헌연구소*. The archive covers historical documents dated 886–1947, including texts on liquor, fermentation starters, brewing methods, and cultural practices. Blog: https://blog.naver.com/korean-sool

---

**Contact / Takedown**  
Questions or takedown requests: <jaeuk0228@gmail.com>.