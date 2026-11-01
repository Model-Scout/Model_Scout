# AI Wars (2026)

200K LLMs, Benchmarks, Hardware & API Costs Across 50 Top AI Companies.

# ⚔️ AI Wars Dataset
Global AI Models, Benchmarks & Capabilities (2018–2026)

---

> 💡 **Don't forget to Upvote (👍) if you find this dataset valuable for your research, EDA, or ML modeling!**

---

## 📌 Dataset Overview

The **AI Wars Dataset** is a comprehensive, research-grade dataset tracking the global AI competitive landscape from **2018 through 2026**. Designed for Data Scientists, Machine Learning Engineers, and AI Industry Analysts, this dataset aggregates structural metadata, empirical benchmark evaluations, API pricing trends, hardware footprints, funding metrics, and agentic capabilities across **50 top AI companies** and **200,000 model snapshots**.

Whether you want to build **LLM pricing forecasters**, analyze **open-source vs. proprietary performance gaps**, or run **multi-variable clustering**, this dataset provides a standardized feature set with **470+ granular columns**.

---

## 📊 High-Level Metrics Snapshot

| Metric | Detail / Value |
| :--- | :--- |
| 🗂️ **Total Records** | **200,000 Unique Rows** (Zero Duplicates) |
| 🧬 **Feature Density** | **470+ Structured Columns** |
| 💾 **Dataset File Size** | **~300 - 500 MB** (Optimized CSV format) |
| 🗓️ **Temporal Range** | **2018 – 2026** |
| 🏢 **Unique Companies Covered** | **50 Key Players** (OpenAI, Anthropic, Meta, DeepSeek, etc.) |
| 📐 **Evaluated Benchmarks** | **23 Standard Benchmarks** (MMLU, GPQA, SWE-bench, etc.) |
| ⚡ **Hardware Accelerators** | **18 Types** (NVIDIA B200, H100, TPU-v5p, MI300X, etc.) |
| 🧩 **Missingness Ratio** | Low (~5% – 10% average across attributes) |

---

## 🏗️ Detailed Column Schema (35 Functional Categories)



---

## 🌍 Global Company Coverage (50 Key Entities)
🇺🇸 United States (28+): OpenAI, Anthropic, Meta AI, xAI, Microsoft, Google, NVIDIA, Perplexity, Midjourney...
🇨🇳 China (8):           DeepSeek, Alibaba Qwen, Baidu ERNIE, Zhipu AI, Moonshot AI, 01.AI, Tencent, ByteDance
🇬🇧 United Kingdom (2):   Google DeepMind, Stability AI
🇫🇷 France (1):          Mistral AI
🇨🇦 Canada (1):          Cohere
🇮🇱 Israel (1):          AI21 Labs
🇯🇵 Japan (1):           Sakana AI
🇰🇷 South Korea (3):     Naver HyperCLOVA, LG Exaone, Samsung Gauss

---

## 🧪 Benchmark & Hardware Dimensions

* **23 Evaluated Benchmarks:** `MMLU`, `GPQA`, `GSM8K`, `MATH`, `AIME`, `HumanEval`, `MBPP`, `LiveCodeBench`, `SWE-bench`, `ARC`, `HellaSwag`, `IFEval`, `MMMU`, `LongBench`, and more.
* **18 Hardware Accelerators:** NVIDIA (`H100`, `H200`, `B200`, `GB200`, `A100`), AMD (`MI300X`, `MI250X`), Google (`TPU-v4`, `TPU-v5p`), Cerebras (`WSE-3`), Groq (`GroqChip`), Intel (`Gaudi3`), AWS (`Trainium2`).

---

## 💡 Machine Learning Use Cases & Tasks

├── 🎯 Classification     : Predict model_archetype or open_source_status based on feature sets.
├── 📈 Regression         : Estimate input_price_per_1m_tokens or predict benchmark_score from parameters.
├── 🏆 Ordinal Ranking    : Build custom competitive leaderboards dynamically across modalities.
├── 🔍 Clustering         : Uncover hidden clusters among 50 AI companies & model archetypes.
├── ⏱️ Time-Series        : Forecast cost degradation per million tokens over 2018–2026.
└── ⚠️ Anomaly Detection  : Identify pricing anomalies or benchmark performance outliers.


---

## 🚀 Quickstart Python Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset sample or full file
df = pd.read_csv('/kaggle/input/ai-wars-dataset/AI_Wars_Dataset.csv')

# 1. Inspect Open-Source vs Proprietary Price to Performance
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, 
    x='input_price_per_1m_tokens', 
    y='reasoning_capability_score',
    hue='open_source', 
    style='model_archetype',
    s=100
)
plt.xscale('log')
plt.title('Reasoning Capability vs API Input Cost (Log Scale)')
plt.xlabel('Input Price per 1M Tokens ($)')
plt.ylabel('Reasoning Score (0-100)')
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()

# 2. Top 5 Companies by Model Density
print("Top AI Companies by Model Records:")
print(df['company_name'].value_counts().head(5))
📁 Included Files
AI_Wars_Dataset.csv — Complete database (200,000 rows, 470+ columns).

AI_Wars_Sample_10000.csv — Lightweight sample for rapid EDA and local experimentation.

AI_Wars_Data_Dictionary.csv — Comprehensive feature definitions.

AI_Wars_Sources.csv — Data provenance tracking.

AI_Wars_Validation_Report.txt — Automated quality assurance log.

AI_Wars_README.md — Complete technical documentation.

⚠️ Data Integrity & Citation Note
Note on Data Generation: This dataset contains a mix of real-world corporate entities, hardware architectures, and model identities combined with simulated numeric scores designed for advanced statistical modeling, educational benchmarks, and ML experimentation. Fixed Reproducibility Seed: 20260914.

Code snippet
@dataset{ai_wars_2026,
  author = {AI Research Community},
  title = {AI Wars Dataset: Global AI Models, Benchmarks & Capabilities},
  year = {2026},
  publisher = {Kaggle},
  url = {[https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)}
}

출처: Kaggle (datascikhan/ai-wars)
태그: science and technology, artificial intelligence, exploratory data analysis, nlp, benchmark
라이선스: CC0: Public Domain
수정일: 2026-09-14T12:42:16.580Z
