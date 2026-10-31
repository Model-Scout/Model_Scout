---
license: cc-by-4.0
task_categories:
  - text-generation
  - question-answering
language:
  - en
  - ja
  - pt
  - fr
  - hi
  - vi
  - de
  - zh
  - ar
  - ko
  - es
  - id
tags:
  - persona
  - synthetic
  - demographics
  - cultural
  - psychographics
  - agent-simulation
  - duckdb
  - parquet
size_categories:
  - 100M<n<1B
pretty_name: Prospire Synth Global Personas
dataset_info:
  features:
    - name: record_id
      dtype: string
    - name: source_dataset
      dtype: string
    - name: source_tier
      dtype: string
    - name: country
      dtype: string
    - name: persona_text
      dtype: string
    - name: age
      dtype: uint8
    - name: sex
      dtype: string
    - name: education_level
      dtype: string
    - name: occupation
      dtype: string
  splits:
    - name: train
      num_examples: 512304709
---

<div align="center">

# 🌍 Prospire Synth Global Personas

### The World's Largest Unified Synthetic Persona Database

*512M+ records · 82 columns · 77+ countries · 39 languages · DuckDB-native*

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Dataset Size](https://img.shields.io/badge/Compressed-77.4%20GB-blue)](https://huggingface.co/datasets/Kasher13/Prospire-Synth-Global-Personas)
[![Records](https://img.shields.io/badge/Records-512M%2B-brightgreen)](https://huggingface.co/datasets/Kasher13/Prospire-Synth-Global-Personas)
[![DuckDB Ready](https://img.shields.io/badge/DuckDB-hf%3A%2F%2F%20ready-orange)](https://duckdb.org)
[![AlterEgos](https://img.shields.io/badge/AlterEgos-Phase%201%20Live%20✅-success)](https://huggingface.co/datasets/Kasher13/Prospire-Synth-Global-Personas)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%E2%98%95-yellow)](https://buymeacoffee.com/twocentshustler)

</div>

---

## 🎯 What Is This?

**Prospire Synth Global Personas** is a unified, query-ready database of synthetic human personas built for AI agent simulations, market research, and cultural analysis. It merges **18 open-source datasets** into a single coherent Parquet warehouse — partitioned, compressed, and instantly queryable via DuckDB over HTTP.

The data layer powering **AlterEgos** — a distributed AI simulation platform that answers real-world business questions by routing them to 500+ synthetic personas across 5 LLM providers simultaneously.

> *"If we launch a durian milk tea product, which customer segments across Southeast Asia would prefer it — and why?"*
>
> → AlterEgos fans out the question to 500 personas drawn from this dataset, processes them in parallel, and returns 500 perspective-diverse responses in ~30 seconds.

**AlterEgos Phase 1 is live** — E2E verified March 28, 2026. See the [architecture section](#-alteregos-inference-system) below.

---

## 📊 Scale at a Glance

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DATASET COMPOSITION                              │
├─────────────────────────────────────────────────────────────────────┤
│  PersonaHub Elite  ██████████████████████████████    370M  72.2%   │
│  GLOPOP-S Vietnam  █████████████                      92M  18.0%   │
│  Argilla Personas  ██                                 21M   4.1%   │
│  CulturalGround    ██                               20.8M   4.1%   │
│  Nemotron (6 cty)  █                                   7M   1.4%   │
│  Sutro / Twin2K    ░                                   1M   0.2%   │
│  Surveys / Culture ░                                 300K  <0.1%   │
└─────────────────────────────────────────────────────────────────────┘
                                           Total: 512,304,709 records
```

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GEOGRAPHIC COVERAGE                              │
├─────────────────────────────────────────────────────────────────────┤
│  🇻🇳 Vietnam     ████████████████████   91.9M structured (census)  │
│  🇺🇸 USA         ████████████            2.0M structured + text    │
│  🇮🇳 India       ████████████            3.0M structured (3 langs) │
│  🇧🇷 Brazil      ████████                1.0M structured           │
│  🇫🇷 France      ████████                1.0M structured           │
│  🇯🇵 Japan       ████████                1.0M structured           │
│  🇸🇬 Singapore   ███                    148K structured            │
│  🌐 77+ countries ████                   WVS + CultureBank + CulturalGround │
│  🌍 Global Elite  ████████████████████   370M text personas        │
└─────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DATA QUALITY TIERS                               │
├─────────────────────────────────────────────────────────────────────┤
│  ⭐⭐⭐⭐⭐  Real Survey Data       WVS (8K), Twin2K-500           │
│  ⭐⭐⭐⭐    Structured Synthetic   Nemotron, Sutro, GLOPOP-S       │
│  ⭐⭐⭐      Text + Extraction     Argilla FinePersonas (21M)      │
│  ⭐⭐        Text-Only            PersonaHub Elite (370M)          │
│  ⭐          Aggregate           CultureBank, CulturalGround, Hofstede │
└─────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STORAGE BREAKDOWN                                │
├─────────────────────────────────────────────────────────────────────┤
│  On HuggingFace (ZSTD-3 compressed):   77.4 GB                     │
│  Raw source data:                      ~500 GB                     │
│  Compression ratio:                    ~6.5x  (text compresses well)│
│  Parquet files:                        4,013                        │
│  Max file size:                        ~300 MB                      │
│  Row group size:                       100K rows                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Schema Overview (82 Columns)

| Group | Columns | Coverage |
|-------|---------|----------|
| **Identity & Provenance** | `record_id`, `source_dataset`, `source_tier`, `source_language`, `record_quality`, `has_demographics`, `has_psychographics` | 100% all records |
| **Core Demographics** | `age`, `age_band`, `sex`, `marital_status`, `education_level`, `occupation`, `annual_wage_usd`, `income_quintile`, `wealth_quintile`, `industry`, `household_type`, ... | Structured datasets |
| **Geography** | `country` (ISO-3), `country_name`, `region_level_1`, `region_level_2`, `zipcode`, `settlement_type`, `glopop_region_code`, `geo_precision`, ... | All records with country |
| **Persona Narratives** | `persona_text`, `professional_persona`, `sports_persona`, `arts_persona`, `travel_persona`, `culinary_persona`, `cultural_background`, `skills_and_expertise`, ... | Nemotron, PersonaHub, Argilla |
| **Structured Personality** | `background_story`, `daily_life`, `digital_behavior`, `values_and_beliefs`, `political_beliefs`, `financial_situation`, `challenges`, `aspirations`, ... | Sutro |
| **Psychographic Scores** | `big5_openness`, `big5_conscientiousness`, `big5_extraversion`, `big5_agreeableness`, `big5_neuroticism`, `need_for_cognition`, `risk_tolerance`, `big5_source` | Twin2K (measured) |
| **Cultural Dimensions** | `hofstede_pdi`, `hofstede_idv`, `hofstede_mas`, `hofstede_uai`, `hofstede_ltowvs`, `hofstede_ivr` | ~100 countries via join |
| **Conversational** | `conversation_json`, `preference_pairs_json`, `partner_persona_text`, `persona_json` | Google SPC, SynthLabs |
| **Housing/Dwelling** | `agri_ownership`, `housing_materials`, `data_source_code` | GLOPOP-S |
| **Lists & Languages** | `skills_list`, `hobbies_list`, `first_language`, `second_language` | Nemotron |

> **Note:** `country` and `source_tier` are Hive partition columns — encoded in the directory path, not stored in file data. DuckDB with `hive_partitioning=true` reconstructs all 82 columns automatically.

---

## ⚡ Quick Start (DuckDB)

### Install
```bash
pip install duckdb
```

### Authentication (for private or rate-limited access)
```python
import duckdb
con = duckdb.connect()
con.execute("CREATE SECRET hf_secret (TYPE HUGGINGFACE, TOKEN 'your_hf_token')")
```

### Query Examples

**Sample 500 structured US personas:**
```sql
SELECT record_id, persona_text, professional_persona,
       age, sex, occupation, education_level,
       hofstede_idv, hofstede_uai
FROM read_parquet(
  'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/country=USA/**/*.parquet',
  union_by_name=true
)
WHERE persona_text IS NOT NULL
USING SAMPLE 500;
```

**Cross-country analysis:**
```sql
SELECT country, COUNT(*) as n,
       AVG(age) as avg_age,
       COUNT_IF(sex = 'F') * 100.0 / COUNT(*) as pct_female
FROM read_parquet(
  'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/**/*.parquet',
  hive_partitioning=true, union_by_name=true
)
WHERE country IN ('USA', 'JPN', 'IND', 'BRA', 'FRA', 'SGP')
  AND source_tier = 'structured'
GROUP BY country
ORDER BY n DESC;
```

**Rich personas with cultural context:**
```sql
SELECT persona_text, age, sex, occupation,
       country_name, settlement_type,
       hofstede_pdi, hofstede_idv,
       values_and_beliefs
FROM read_parquet(
  'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/**/*.parquet',
  hive_partitioning=true, union_by_name=true
)
WHERE has_demographics = true
  AND source_tier = 'structured'
USING SAMPLE 100;
```

**Access PersonaHub Elite (370M text personas):**
```sql
-- Isolated partition — query other data without touching these 3,700 files
SELECT record_id, persona_text
FROM read_parquet(
  'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/country=_GLOBAL_ELITE/**/*.parquet',
  union_by_name=true
)
USING SAMPLE 1000;
```

**Vietnam synthetic census (GLOPOP-S):**
```sql
SELECT age_band, sex, education_level, settlement_type,
       wealth_quintile, COUNT(*) as n
FROM read_parquet(
  'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/country=VNM/**/*.parquet',
  union_by_name=true
)
GROUP BY ALL
ORDER BY n DESC
LIMIT 20;
```

---

## 🤖 AlterEgos Inference System

**AlterEgos** is the AI simulation platform built on top of this dataset. It is now **live and E2E verified** (Phase 1 — March 28, 2026).

### Architecture

```
Client POST /api/ask { question, personaCount: 500 }
  ↓
Cloudflare Worker Gateway
  ├── SmartRouter  → scores API keys (quota×0.4 + speed×0.4 + reliability×0.2)
  ├── Dispatcher   → splits 500 personas into 50-persona batches
  └── Fan-Out      → distributes batches to 8 HuggingFace Worker Spaces
  ↓ (parallel)
HuggingFace Worker Spaces (FastAPI + asyncio)
  ├── Each Space calls LLM providers in parallel (semaphore=20)
  └── Providers: Groq / Gemini / OpenRouter / Mistral / HF Router API
  ↓
POST /api/callback → Gateway aggregates results
  ↓
Client GET /api/job?id=xxx → 500 persona responses
```

### Phase 1 Test Results (2026-03-28) ✅

| Metric | Result |
|--------|--------|
| Personas | 10/10 successful |
| Errors | 0 |
| Total time | 52.8 seconds |
| Provider | HF Router API (Qwen2.5-72B-Instruct) |
| Keys used | 5 HF tokens across 5 accounts |

**Capacity projection at full scale:**

```
Current (5 HF keys):        5 × 30 RPM = 150 RPM  → 500 personas in ~4-5 min
Target (5 providers × 10 keys): 1,700 RPM          → 500 personas in ~30 seconds ⚡
```

### LLM Provider Config

| Provider | Endpoint | Default Model | Speed |
|----------|----------|---------------|-------|
| Groq | api.groq.com | llama-3.3-70b-versatile | ~1-2s |
| Gemini | generativelanguage.googleapis.com | gemini-2.0-flash | ~3-5s |
| OpenRouter | openrouter.ai/api/v1 | meta-llama/llama-3.3-70b-instruct:free | ~4-8s |
| Mistral | api.mistral.ai | mistral-small-latest | ~3-6s |
| HF Router | router.huggingface.co/v1 | Qwen/Qwen2.5-72B-Instruct | ~10-15s |

> **Note:** HuggingFace Inference API migrated to `router.huggingface.co/v1` (OpenAI-compatible). The legacy `api-inference.huggingface.co` endpoint returns 410 Gone.

---

## 🏗️ Dataset Architecture

```
┌─────────────────── Prospire Synth ETL Pipeline ───────────────────┐
│                                                                     │
│  18 Raw Datasets    →   Unified 82-col Schema   →   HuggingFace   │
│  (~500 GB raw)          (sparse Parquet, ZSTD)      (76.5 GB)     │
│                                                                     │
│  Hive Partitioning:                                                 │
│  data/                                                              │
│    country=USA/source_tier=structured/     ← Nemotron + Sutro + Twin2K │
│    country=JPN/source_tier=structured/     ← Nemotron Japan        │
│    country=IND/source_tier=structured/     ← Nemotron India (3 ln) │
│    country=BRA/source_tier=structured/     ← Nemotron Brazil       │
│    country=FRA/source_tier=structured/     ← Nemotron France       │
│    country=SGP/source_tier=structured/     ← Nemotron Singapore    │
│    country=VNM/source_tier=structured/     ← GLOPOP-S 91.9M       │
│    country=_GLOBAL/source_tier=text_only/  ← PersonaHub + Argilla  │
│    country=_GLOBAL/source_tier=conversational/ ← Google SPC        │
│    country=_GLOBAL/source_tier=aggregate/  ← CultureBank (23K)   │
│    country=*/source_tier=aggregate/        ← CulturalGround (42 countries, 20.8M VQA) │
│    country=_GLOBAL/source_tier=structured/ ← WorldValuesBench     │
│    country=_GLOBAL_ELITE/source_tier=text_only/ ← 370M records    │
│                                                                     │
│  Query Engine: DuckDB over HTTP (hf://)                            │
│  500+ AI Agents read directly — no download needed                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Source Datasets (18 Processed)

| Dataset | Records | Country | Tier | Key Features |
|---------|---------|---------|------|-------------|
| [PersonaHub Elite](https://huggingface.co/datasets/proj-persona/PersonaHub) | **370M** | Global | text_only | Massive persona diversity |
| [GLOPOP-S Vietnam](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BXKPA5) | **91.9M** | 🇻🇳 VNM | structured | Synthetic census, DHS-aligned |
| [Argilla FinePersonas](https://huggingface.co/datasets/argilla/FinePersonas-v0.1) | 21.1M | Global | text_only | Labeled, clustered |
| [Nemotron-India](https://huggingface.co/datasets/nvidia/Nemotron-Personas-India) | 3M | 🇮🇳 IND | structured | 3 languages (en/hi/hi-Latn) |
| [Nemotron-USA](https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA) | 1M | 🇺🇸 USA | structured | Census-aligned, 22 cols |
| [Nemotron-Brazil](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Brazil) | 1M | 🇧🇷 BRA | structured | Municipality/state |
| [Nemotron-France](https://huggingface.co/datasets/nvidia/Nemotron-Personas-France) | 1M | 🇫🇷 FRA | structured | Commune/département |
| [Nemotron-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 1M | 🇯🇵 JPN | structured | Prefecture |
| [Sutro Synthetic Humans](https://huggingface.co/datasets/sutroinc/synthetic-humans) | 1M | 🇺🇸 USA | structured | 12 narrative fields + income |
| [Argilla Clustering 100K](https://huggingface.co/datasets/argilla/FinePersonas-v0.1-clustering-100k) | 100K | Global | text_only | DBSCAN/UMAP clusters |
| [PersonaHub Base](https://huggingface.co/datasets/proj-persona/PersonaHub) | 200K | Global | text_only | Diverse persona text |
| [WorldValuesBench](https://huggingface.co/datasets/worldvaluesbench/WVS) | 8.3K | 77 countries | structured | 240 value questions |
| [Twin-2K-500](https://github.com/twin2k/twin-2k-500) | 2K | 🇺🇸 USA | structured | **Real** Big5 scores (BFI-44) |
| [Google SPC](https://huggingface.co/datasets/google/Synthetic-Persona-Chat) | 43.8K | Global | conversational | Conversation pairs |
| [CultureBank](https://huggingface.co/datasets/SALT-NLP/CultureBank) | 23K | Global | aggregate | Reddit + TikTok culture |
| [CulturalGround](https://huggingface.co/datasets/neulab/CulturalGround) | 20.8M VQA | 42 countries | aggregate | Cultural Q&A, 39 languages |
| [Hofstede Dimensions](https://geerthofstede.com/research-and-vsm/dimension-data-matrix/) | 214 countries | World | — | Enrichment join (not separate rows) |
| [Nemotron-Singapore](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Singapore) | 148K | 🇸🇬 SGP | structured | Planning area, industry |

---

## 🗺️ Roadmap

```
ETL Pipeline ─────────────────────────────────────────────────────────

Phase 1 — Core ETL Infrastructure          ████████████ COMPLETE
  ✅ 82-column unified schema
  ✅ PyArrow streaming extraction (100K row batches)
  ✅ Hive-partitioned Parquet output (ZSTD-3)
  ✅ Incremental HF upload — peak disk 24 GB (not 700 GB)
  ✅ Exponential backoff retry (503/502/429 errors)
  ✅ JSON checkpointing for crash recovery

Phase 2 — Structured Datasets              ████████████ COMPLETE
  ✅ Nemotron (6 countries — 7.1M records)
  ✅ Sutro 1M (with 50K deduplication)
  ✅ Twin-2K-500 (Big5 psychometric data)
  ✅ Big5 imputation framework (GBR transfer learning)
  ✅ Hofstede cultural enrichment (214 countries)

Phase 3 — Text-Only Datasets               ████████████ COMPLETE
  ✅ PersonaHub Base (200K)
  ✅ Argilla FinePersonas (21.1M)
  ✅ Argilla Clustering 100K (UMAP/DBSCAN clusters)

Phase 4 — PersonaHub Elite                 ████████████ COMPLETE
  ✅ 370,001,710 records across 19 JSONL parts
  ✅ 3,701 Parquet files in _GLOBAL_ELITE partition
  ✅ Streaming conversion (no 300 GB disk needed)

Phase 5 — Survey & Cultural                ████████████ COMPLETE
  ✅ GLOPOP-S Vietnam (91.9M synthetic census records)
  ✅ WorldValuesBench (8.3K records, 77 countries)
  ✅ CultureBank (23K cultural behavior records)
  ✅ Google SPC (43.8K conversation pairs)
  ✅ CulturalGround (20.8M VQA pairs, 42+ countries, 39 languages)

Phase 6 — Registration-Required Datasets   ░░░░░░░░░░░░ FUTURE
  ⬜ IPUMS Vietnam Census (8.2M) — ipums.org
  ⬜ Asian Barometer (18 Asian nations) — institutional access
  ⬜ Pew Global Attitudes (240K+) — pewresearch.org
  ⬜ DHS Vietnam, VHLSS household surveys — dhsprogram.com / gso.gov.vn
  ⬜ Eurobarometer, Afrobarometer, ISSP — gesis.org
  ℹ️  WVS Wave 7 → WorldValuesBench already in pipeline (no registration needed)

Phase 7 — Enrichment Layer                 ░░░░░░░░░░░░ FUTURE
  ⬜ BLS wage estimation for all USA occupations
  ⬜ PPP-adjusted income for non-US countries
  ⬜ IPCC climate zone enrichment
  ⬜ Multilingual embeddings (multilingual-e5)
  ⬜ More countries: Middle East, Africa, SE Asia

AlterEgos Inference System ───────────────────────────────────────────

AlterEgos Phase 1 — Gateway + Worker MVP   ████████████ COMPLETE ✅
  ✅ Cloudflare Worker gateway deployed
  ✅ SmartRouter: quota×0.4 + speed×0.4 + reliability×0.2 scoring
  ✅ KV-backed job state (KEY_POOL, RATE_STATE, JOB_STATE)
  ✅ HuggingFace Worker Space (FastAPI, asyncio, semaphore=20)
  ✅ 5 LLM providers wired (Groq, Gemini, OpenRouter, Mistral, HF Router)
  ✅ E2E verified: 10/10 personas, 0 errors, 52.8s (2026-03-28)
  ✅ HF Router API: router.huggingface.co/v1 (OpenAI-compatible)

AlterEgos Phase 2 — Scale + Security       ░░░░░░░░░░░░ PLANNED
  ⬜ Add Groq/Gemini/OpenRouter/Mistral API keys (1,700 RPM capacity)
  ⬜ Deploy 8 Worker Spaces across multiple HF accounts
  ⬜ Gateway authentication (GATEWAY_SECRET validation)
  ⬜ API key encryption in BatchPayload (DEBT-001)
  ⬜ KV namespace IDs — real IDs in wrangler.toml (DEBT-003)
  ⬜ Space URL persistence to KV (DEBT-004)
  ⬜ Automated test suite: unit + integration (DEBT-007)

AlterEgos Phase 3 — Persona Intelligence   ░░░░░░░░░░░░ FUTURE
  ⬜ Persona Store: 500 curated profiles with rich DuckDB queries
  ⬜ RAG Engine: query this dataset to select demographically diverse personas
  ⬜ Multi-model routing: different providers per persona type
  ⬜ Monitor Dashboard (CF Worker) — real-time job + provider stats
  ⬜ Response clustering + diversity scoring
```

---

## 🔧 Use Cases

### AI Agent Simulation
```python
import duckdb

# Select diverse personas for market simulation
personas = duckdb.sql("""
    SELECT * FROM read_parquet(
      'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/**/*.parquet',
      hive_partitioning=true, union_by_name=true
    )
    WHERE country IN ('USA', 'JPN', 'VNM', 'IND', 'BRA')
      AND source_tier = 'structured'
      AND has_demographics = true
    USING SAMPLE 500
""").df()
```

### Cultural Research
```python
# Hofstede dimensions by country
hofstede_data = duckdb.sql("""
    SELECT country_name, country,
           AVG(hofstede_pdi) as power_distance,
           AVG(hofstede_idv) as individualism,
           AVG(hofstede_uai) as uncertainty_avoidance
    FROM read_parquet('hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/**/*.parquet',
                      hive_partitioning=true, union_by_name=true)
    WHERE hofstede_pdi IS NOT NULL
      AND source_tier = 'structured'
    GROUP BY country_name, country
    ORDER BY individualism DESC
""").df()
```

### Vietnam Demographic Analysis
```python
# GLOPOP-S Vietnam — 91.9M synthetic census records
vn_demo = duckdb.sql("""
    SELECT age_band, sex, education_level, settlement_type,
           wealth_quintile, income_quintile, COUNT(*) as n
    FROM read_parquet(
      'hf://datasets/Kasher13/Prospire-Synth-Global-Personas/data/country=VNM/**/*.parquet',
      union_by_name=true
    )
    GROUP BY ALL
    ORDER BY n DESC
""").df()
```

---

## 📁 Repository Structure

```
data/
  country=USA/source_tier=structured/         ← Nemotron USA + Sutro + Twin2K (2M)
  country=JPN/source_tier=structured/         ← Nemotron Japan (1M)
  country=IND/source_tier=structured/         ← Nemotron India 3 langs (3M)
  country=BRA/source_tier=structured/         ← Nemotron Brazil (1M)
  country=FRA/source_tier=structured/         ← Nemotron France (1M)
  country=SGP/source_tier=structured/         ← Nemotron Singapore (148K)
  country=VNM/source_tier=structured/         ← GLOPOP-S Vietnam (91.9M, 184 files)
  country=_GLOBAL/source_tier=text_only/      ← PersonaHub Base + Argilla (21.4M)
  country=_GLOBAL/source_tier=conversational/ ← Google SPC (43.8K)
  country=_GLOBAL/source_tier=aggregate/      ← CultureBank (23K)
  country=*/source_tier=aggregate/            ← CulturalGround (42 countries, 20.8M VQA)
  country=_GLOBAL/source_tier=structured/     ← WorldValuesBench (8.3K)
  country=_GLOBAL_ELITE/source_tier=text_only/ ← PersonaHub Elite (370M, 3701 files)
```

**Technical specs:**
- Format: Apache Parquet, 2-level Hive-partitioned (`country` + `source_tier`)
- Compression: ZSTD level 3
- Row group size: 100K rows (optimized for DuckDB zone-map filtering)
- Max rows per file: 500K (~100-300 MB compressed)
- Query: DuckDB `hf://` protocol, `hive_partitioning=true`, `union_by_name=true`

---

## 🤝 Contributing & Support

This is an ongoing open-source project. If you find it useful for your research, AI work, or product development, consider supporting:

<div align="center">

### ☕ [Buy Me a Coffee](https://buymeacoffee.com/twocentshustler)

*Keeping the ETL pipeline running costs compute. Every coffee helps add more datasets.*

</div>

**Contact:** [baotran130703@gmail.com](mailto:baotran130703@gmail.com)

**Issues & contributions:** Open an issue on this dataset page or email directly.

**What your support enables:**
- 🚀 AlterEgos Phase 2 — scale to 500 personas with full provider mix (~30s E2E)
- 🌏 Adding registration-required datasets (WVS, IPUMS, Pew, Eurobarometer — Phase 6)
- 💰 PPP-adjusted income estimates for non-US countries
- 🧠 Multilingual embedding layer for semantic search
- 🗺️ More countries (Middle East, Africa, Southeast Asia focus)
- 📊 Interactive visualization dashboard

---

## 📜 License & Citation

Dataset released under **CC BY 4.0**. Individual source datasets retain their original licenses (see links above).

```bibtex
@dataset{prospire_synth_global_personas_2026,
  title     = {Prospire Synth Global Personas},
  author    = {Tran, Bao},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/datasets/Kasher13/Prospire-Synth-Global-Personas},
  note      = {Unified synthetic persona database, 512M+ records, 77+ countries, 82-column schema}
}
```

---

<div align="center">

**Built with ❤️ for the AI research community**

[📧 Email](mailto:baotran130703@gmail.com) · [☕ Buy Me a Coffee](https://buymeacoffee.com/twocentshustler) · [🤗 HuggingFace](https://huggingface.co/Kasher13)

*The data layer powering AlterEgos — 500-persona AI simulation, live since March 2026*

</div>
