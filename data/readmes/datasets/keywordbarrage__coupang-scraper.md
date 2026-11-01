---
pretty_name: "Enterprise High-Frequency SKU Depletion & WAF Telemetry Feed"
annotations_creators:
  - machine-generated
language:
  - en
  - ko
license: apache-2.0
task_categories:
  - tabular-classification
  - time-series-forecasting
tags:
  - time-series-sku-depletion
  - pre-indexed-sqlite
  - parquet-benchmark
  - retail-intelligence
size_categories:
  - 10K<n<100K
configs:
  - config_name: default
    data_files:
      - split: train
        path: "data/train-*.parquet"
      - split: validation
        path: "data/val-*.parquet"
---

**Python Code:**
```python
import sqlite3
from datasets import load_dataset
import pandas as pd

# Method 1: Load via Hugging Face datasets library
dataset = load_dataset("daas-intelligence/enterprise-sku-depletion-telemetry")
print("Hub Sample Record:", dataset["train"][0])

# Method 2: Load zero-latency local pre-indexed SQLite deliverable
# Optimized for quantitative research and local data engineering pipelines
conn = sqlite3.connect("enterprise_feed.sqlite")
df = pd.read_sql_query("SELECT sku_id, price_krw, stock_level, depletion_velocity FROM sku_stream ORDER BY timestamp DESC LIMIT 10", conn)
print(df)
```

---

# Dataset Card: Enterprise High-Frequency SKU Depletion & WAF Telemetry

## 1. Dataset Summary & Research Motivation
This repository contains an open 1,000-row verified benchmark sample of the Coupang SKU depletion feed. It is structured to assist quantitative analysts and data engineering teams in evaluating robust extraction pipelines that bypass enterprise-grade perimeter defenses (Akamai Bot Manager, Envoy Gateway, and JA4 TLS fingerprinting).

Traditional scraping architectures often fail due to brittle headless browser reliance and proxy pool degradation. This dataset demonstrates a production-grade approach, utilizing protocol-level extraction to maintain 99.9% pipeline availability and deterministic schema parity.

## 2. Enterprise Deliverables Matrix
This dataset provides four production-ready formats for immediate ingestion into quantitative hedge fund environments and enterprise RAG pipelines:

*   **Pre-indexed SQLite (.sqlite):** Instant local querying with pre-built indices on `sku_id`, `price_krw`, and `timestamp`.
*   **Snappy Parquet:** Optimized for high-throughput ingestion into Snowflake, Google BigQuery, and AWS Athena.
*   **Zero-Dependency Offline DataGrid (.html):** A self-contained, interactive viewer for quantitative stakeholders to audit market signals without requiring SQL expertise.
*   **CDC JSONL Stream:** A change-data-capture format suitable for real-time vector database updates and inventory velocity monitoring.

## 3. Dataset Schema & Data Dictionary

| Column | Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `sku_id` | STRING | No | Unique Coupang Product/Vendor identifier. |
| `timestamp` | DATETIME | No | ISO-8601 execution time of the telemetry capture. |
| `price_krw` | FLOAT | No | Real-time unit price in Korean Won (₩). |
| `stock_level` | INTEGER | Yes | Current inventory count or availability flag. |
| `depletion_velocity`| FLOAT | Yes | Calculated rate of inventory movement over 24h. |
| `waf_signature` | STRING | No | TLS/JA4 fingerprint of the ingestion session. |
| `delivery_status` | STRING | No | Logistics SLA (e.g., "Rocket Delivery", "Dawn Delivery"). |

**Sample Record (JSON):**
```json
{
  "sku_id": "CP-99281-B",
  "timestamp": "2026-09-24T14:22:01Z",
  "price_krw": 24500.0,
  "stock_level": 142,
  "depletion_velocity": 0.85,
  "waf_signature": "ja4_3a2b1c",
  "delivery_status": "Rocket Delivery"
}
```

## 4. Reproducibility & Quality Metrics
*   **Pipeline Availability:** 99.9% uptime via distributed residential proxy rotation.
*   **Schema Parity:** Deterministic structure maintained despite upstream UI/DOM changes.
*   **Protocol Benchmarks:** Sub-120ms execution per node, bypassing edge challenge loops (Akamai/Envoy) through transport-level parity.

## 5. Commercial Engagement
This repository serves as an open benchmark. For production-scale ingestion, we maintain enterprise data feeds with a 99.9% uptime SLA. Our delivery model focuses on providing clean, pre-normalized datasets that eliminate the operational burden of proxy pool maintenance and WAF challenge resolution.