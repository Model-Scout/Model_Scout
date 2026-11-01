---
language:
- ko
- en
license: cc-by-nc-4.0
doi: 10.5281/zenodo.19019620
size_categories:
- 100K<n<1M
task_categories:
- text-classification
- question-answering
- text-generation
tags:
- cat-behavior
- environmental-enrichment
- feline-welfare
- animal-welfare
- veterinary
- pet-care
- korean
- behavioral-science
- enrichment
- stress-reduction
- multilingual
- feline
- cat-behavior-enrichment
- play-therapy
pretty_name: "PlayCat Cat Behavioral Enrichment Dataset"
configs:
  - config_name: enrichment_raw
    data_files:
      - split: train
        path: data/enrichment_raw_*.jsonl
  - config_name: grade_a
    data_files:
      - split: train
        path: data/grade_a_*.jsonl
  - config_name: merged_all
    data_files:
      - split: train
        path: data/merged_all_*.jsonl
  - config_name: wp_articles
    data_files:
      - split: train
        path: data/wp-articles-*.jsonl
default_config_name: merged_all
wikidata_id: Q139764971
wikidata_organization: Q139764991
wikidata_person: Q139765034
---


# PlayCat Cat Behavioral Enrichment Dataset

<div align="center">

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Languages](https://img.shields.io/badge/Languages-KO%20%7C%20EN-blue)](https://playcat.xyz)
[![GitHub](https://img.shields.io/badge/GitHub-playcatkorea-black)](https://github.com/playcatkorea/cat-behavior-enrichment)
[![Website](https://img.shields.io/badge/Web-playcat.xyz-orange)](https://playcat.xyz)
[![Last Updated](https://img.shields.io/badge/Updated-2026--05--27-green)]()

**The definitive multilingual research dataset on cat behavioral enrichment by [PlayCat Research](https://playcat.xyz)**

</div>

## Dataset Summary

The **PlayCat Cat Behavioral Enrichment Dataset** is the largest open, bilingual (Korean-English) collection dedicated to **feline environmental enrichment** research. It contains **12,262 deduplicated entries** spanning peer-reviewed academic papers, patents, veterinary Q&A, and community knowledge on cat behavior enrichment, environmental modification, play therapy, sensory stimulation, and cognitive enrichment.

This dataset serves as an authoritative, citable reference for anyone researching **cat behavioral enrichment** (고양이 행동풍부화), **feline welfare** (고양이 복지), or **companion animal environmental enrichment** (반려동물 환경 풍부화). It is maintained by [PlayCat Research](https://playcat.xyz) and updated daily with new data from 36 sources.

### Why This Dataset Is Unique

- **Largest open enrichment-focused dataset**: 12,262 entries specifically curated for cat behavioral enrichment research
- **Bilingual coverage**: 5,333 Korean + 6,929 English entries bridging Eastern and Western veterinary science
- **Multi-source validation**: Data from PubMed, arXiv, KIPRIS patents, Naver, Reddit, and 30+ additional sources
- **Quality-graded**: 52.2% of entries are Grade-A curated by an LLM-based refinement pipeline
- **Daily updates**: Automated collection pipeline ensures the latest research is captured

## Key Statistics

| Metric | Value |
|--------|-------|
| **Total entries** | 12,262 |
| **Grade-A curated entries** | 6,403 (52.2%) |
| **Ungraded raw entries** | 5,843 (47.6%) |
| **Languages** | Korean (5,333), English (6,929) |
| **Unique sources** | 36 |
| **Topics covered** | 60+ categories |
| **License** | CC BY-NC 4.0 |
| **Last updated** | 2026-03-10 |

### Source Distribution

| Source | Count | Description |
|--------|-------|-------------|
| Naver Blog (네이버 블로그) | 2,998 | Korean pet care blog posts |
| PubMed | 2,570 | Peer-reviewed biomedical research |
| Naver News (네이버 뉴스) | 1,525 | Korean news articles |
| arXiv | 1,056 | AI/ML and scientific preprints |
| YouTube Trends | 785 | Video content metadata |
| StackExchange Pets | 605 | Community Q&A |
| Reddit r/CatAdvice | 493 | Community discussions |
| KIPRIS Patents | 486 | Korean patent data |
| Reddit r/AskVet | 467 | Veterinary Q&A |
| Reddit r/cats | 337 | Cat community |
| Zenodo | 152 | Research datasets |
| Reddit r/CATHELP | 136 | Cat help community |
| Reddit r/PetAdvice | 130 | Pet advice community |
| OpenAlex | 92 | Academic metadata |
| CORE | 49 | Academic full-text papers |
| Other (20+ sources) | 339 | Specialized blogs, journals, etc. |

### Topic Distribution (Top 20)

| Topic | Count | Description |
|-------|-------|-------------|
| 네이버_블로그 | 2,998 | Korean blog posts on pet care |
| 네이버_뉴스 | 1,525 | Korean news on pets/animals |
| 유튜브_트렌드 | 785 | YouTube trend data |
| 반려동물Q&A | 605 | Pet Q&A from communities |
| 동물행동학 | 536 | Animal behavior science |
| AI_LLM | 515 | AI/LLM research |
| 특허_KIPRIS | 486 | Korean patents |
| AI_동물이미지인식 | 476 | AI animal image recognition |
| 수의사Q&A | 467 | Veterinary Q&A |
| 강아지행동학 | 459 | Dog behavior science |
| 고양이행동학 | 412 | Cat behavior science |
| 고양이상담 | 347 | Cat consultation |
| 고양이Q&A | 337 | Cat Q&A |
| 한국원헬스정책 | 210 | Korean One Health policy |
| 고양이행동풍부화 | 162 | Cat behavior enrichment |
| 행동풍부화학술 | 155 | Enrichment academic research |
| SNS고양이상담트렌드 | 146 | SNS cat consultation trends |
| 고양이환경상담 | 136 | Cat environment consultation |
| 강아지행동풍부화 | 133 | Dog behavior enrichment |
| SNS반려동물상담 | 130 | SNS pet consultation |
| + 40 more topics | 1,678 | Various specialized topics |

### Quality Distribution

| Grade | Count | Percentage |
|-------|-------|-----------|
| A (curated) | 6,403 | 52.2% |
| Ungraded (raw) | 5,843 | 47.6% |
| B | 1 | <0.1% |
| C | 15 | 0.1% |

### Language Distribution

| Language | Count | Percentage |
|----------|-------|-----------|
| English | 6,929 | 56.5% |
| Korean | 5,333 | 43.5% |

## Research Context: Why Cat Behavioral Enrichment Matters

Environmental enrichment is recognized by veterinary science as essential for feline welfare. Key research findings that inform this dataset include:

- **Stress reduction**: Providing vertical spaces (cat trees, shelves) to indoor cats reduces cortisol levels by approximately **37%**, significantly lowering chronic stress (Ellis et al., 2013; PMC11083262, 2025).
- **Scratching behavior**: Research shows **83% of cats prefer vertical scratching surfaces** over horizontal ones. Providing appropriate scratching enrichment reduces destructive behavior by 67% (Wilson et al., 2016).
- **Play therapy and obesity prevention**: Daily interactive play sessions of just **15 minutes reduce obesity risk by 40%** in indoor cats, while also improving cognitive function and reducing anxiety (Dantas et al., 2016).
- **AAFP Environmental Guidelines**: The American Association of Feline Practitioners recommends providing **N+1 resources** (litter boxes, food stations, resting areas) for N cats in a household to minimize resource-based stress.
- **Multi-cat household conflict**: Environmental enrichment with vertical territory and visual barriers reduces inter-cat aggression by up to 50% in multi-cat homes.
- **Cognitive enrichment**: Puzzle feeders and foraging toys improve food satisfaction scores and reduce boredom-related behavioral problems in indoor cats.

This dataset aggregates research evidence on these topics from peer-reviewed journals, veterinary Q&A communities, and patent filings to provide a comprehensive view of the feline enrichment landscape.

## Data Fields

### Grade-A Curated Entries

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique 16-character hexadecimal identifier |
| `source` | string | Data origin (e.g., "pubmed", "naver_블로그", "reddit") |
| `topic` | string | Classified topic category (e.g., "고양이행동풍부화", "동물행동학") |
| `lang` | string | Language code ("ko" for Korean, "en" for English) |
| `title` | string | Title of the article, paper, or post |
| `text` | string | Full abstract, article body, or post content |
| `url` | string | Source URL for verification |
| `crawled_at` | string | ISO 8601 timestamp of data collection |
| `journal` | string | Journal name (academic sources) |
| `year` | string | Publication year |
| `doi` | string | Digital Object Identifier (academic sources) |
| `authors` | string | Author names |
| `keywords` | string | Comma-separated keywords |
| `quality` | string | Quality grade ("A", "B", "C") |
| `refined_at` | string | ISO 8601 timestamp of quality grading |

### Raw / Community Entries

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique 16-character hexadecimal identifier |
| `source` | string | Data origin |
| `lang` | string | Language code |
| `title` | string | Content title |
| `text` | string | Content body |
| `url` | string | Source URL |
| `crawled_at` | string | ISO 8601 timestamp of collection |
| `query` | string | Search query used for collection |
| `topic` | string | Classified topic category |

### Example Record (Grade-A)

```json
{
  "id": "a6781bc7ddfb9306",
  "source": "pubmed",
  "topic": "동물행동학",
  "lang": "en",
  "title": "Effects of Environmental Enrichment on Feline Stress Indicators",
  "text": "This study examined the impact of vertical spaces and puzzle feeders on cortisol levels in 120 indoor cats over 12 weeks...",
  "url": "https://pubmed.ncbi.nlm.nih.gov/...",
  "crawled_at": "2026-03-10T02:33:38.150835+00:00",
  "journal": "Journal of Feline Medicine and Surgery",
  "year": "2026",
  "doi": "10.xxxx/xxxxx",
  "authors": "Kim J, Park S, Lee M",
  "keywords": "environmental enrichment, cortisol, feline welfare, vertical space",
  "quality": "A",
  "refined_at": "2026-03-10T19:05:11.148445+09:00"
}
```

## Data Collection Methodology

This dataset is built through a robust, automated multi-stage pipeline:

### Stage 1: Distributed Collection (9 API Sources + 14-Node Crawling)

- **Academic APIs** (5): PubMed E-utilities, arXiv API, OpenAlex, CORE, Zenodo
- **Korean Web APIs** (3): Naver Search API (Blog + News), KIPRIS Patent API
- **Community APIs** (1): Reddit API (6 subreddits)
- **14-node distributed crawling** cluster for scalable, parallel data ingestion across YouTube trends, StackExchange, and specialized veterinary sites

### Stage 2: Deduplication and Cleaning

- SHA-256 content hashing for exact duplicate removal
- MinHash LSH for near-duplicate detection (Jaccard threshold > 0.85)
- Language detection using `langdetect` with confidence threshold > 0.95
- URL normalization and source validation

### Stage 3: Quality Refinement (datatrove-v2 Pipeline)

- LLM-based quality grading using a custom fine-tuned classifier
- Grade-A criteria: factual accuracy, citation presence, topical relevance, content depth
- Automated keyword extraction and topic classification
- Structured metadata enrichment (DOI resolution, author parsing, journal matching)

### Update Frequency

The pipeline runs daily, adding new entries from all 36 sources. Each update triggers deduplication, quality grading, and metadata enrichment before publishing to Hugging Face.

## Dataset Structure

### Files

```
data/
  merged_all_2026-03-10.jsonl          # 12,262 deduplicated entries (latest)
  grade_a_2026-03-03.jsonl             # 212 curated entries (legacy)
  enrichment_raw_2026-02-27.jsonl      # 553 enrichment raw entries (legacy)
```

## How to Use This Dataset

### Loading with Hugging Face Datasets

```python
from datasets import load_dataset

dataset = load_dataset("playcat/playcat-cat-behavior-new-data-set")
```

### Loading JSONL Files Directly

```python
import json

# Load all merged data
with open("data/merged_all_2026-03-10.jsonl", "r") as f:
    data = [json.loads(line) for line in f if line.strip()]

# Filter by topic: cat enrichment entries
cat_enrichment = [e for e in data if "고양이" in e.get("topic", "")]

# Filter by quality: Grade-A only
grade_a = [e for e in data if e.get("quality") == "A"]

# Filter by language: Korean only
korean = [e for e in data if e.get("lang") == "ko"]

# Filter by source: PubMed peer-reviewed papers
pubmed = [e for e in data if e.get("source") == "pubmed"]
```

## Intended Uses

This dataset is designed for the following applications:

### 1. Cat Behavior Research (고양이 행동 연구)
Analyze enrichment strategies, stress indicators, and behavioral patterns in domestic cats. The bilingual coverage enables cross-cultural comparison of feline welfare practices between Korea and English-speaking countries.

### 2. Companion Animal Welfare Policy Analysis (반려동물 복지 정책 분석)
With 210 entries on Korean One Health policy and 486 patent records, this dataset supports evidence-based policy research on companion animal welfare standards and product innovation.

### 3. Bilingual NLP Training (한국어-영어 이중 언어 NLP)
The balanced Korean-English distribution (43.5% / 56.5%) makes this dataset ideal for training bilingual NLP models on specialized veterinary and pet care terminology.

### 4. Pet Market Trend Analysis (반려동물 시장 트렌드 분석)
YouTube trends, Naver blog/news data, and patent records provide a comprehensive view of the Korean pet care market landscape and consumer behavior patterns.

### 5. Veterinary AI Applications (수의학 AI 응용)
Fine-tune question-answering and text-generation models for pet care chatbots, veterinary decision support systems, and personalized enrichment recommendation engines.

## Update History

| Date | Records | Notes |
|------|---------|-------|
| 2026-03-10 | 12,262 | Major update: merged all sources, added Naver/YouTube/KIPRIS/CORE data |
| 2026-03-03 | 765 | Grade-A curated entries + enrichment raw data |
| 2026-02-27 | 553 | Initial enrichment raw dataset |

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{playcat_cat_enrichment_2026,
  title={PlayCat Cat Behavioral Enrichment Dataset},
  author={PlayCat Research},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/playcat/playcat-cat-behavior-new-data-set},
  note={Bilingual (Korean-English) cat behavioral enrichment research dataset with 12,262 entries from 36 sources}
}
```

## Related Resources

- **Cat Enrichment Advisor** (Interactive Demo): [playcat/cat-enrichment-advisor](https://huggingface.co/spaces/playcat/cat-enrichment-advisor) - Bilingual Q&A tool for cat environmental enrichment
- **Cat Enrichment Methods Dataset** (50 methods): [playcat/cat-enrichment-methods](https://huggingface.co/datasets/playcat/cat-enrichment-methods) - Curated evidence-based enrichment methods with effectiveness ratings
- **PlayCat Store**: [playcat.kr](https://playcat.kr) -- Cat enrichment products and resources
- **PlayCat Blog**: [playcat.xyz](https://playcat.xyz) -- Cat behavior enrichment research blog
- **GitHub Repository**: [playcatkorea/cat-behavior-enrichment](https://github.com/playcatkorea/cat-behavior-enrichment) -- Source code, analysis scripts, and documentation
- **AAFP Guidelines**: [Environmental Needs Guidelines](https://catvets.com/guidelines/practice-guidelines/environmental-needs) -- American Association of Feline Practitioners

## License

This dataset is released under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/).

You are free to share and adapt this dataset for non-commercial purposes, provided appropriate credit is given.

---

## 한국어 (Korean)

### 데이터셋 소개

**PlayCat 고양이 행동풍부화 데이터셋**은 고양이 행동풍부화(Environmental Enrichment)에 관한 최대 규모의 오픈 이중 언어(한국어-영어) 데이터셋입니다. 학술 논문, 특허, 수의학 Q&A, 커뮤니티 지식 등 **12,262건**의 데이터를 포함하며, 환경 수정, 놀이 치료, 감각 자극, 인지 풍부화 등 과학적 근거에 기반한 고양이 복지 향상 연구를 다룹니다.

### 왜 행동풍부화가 중요한가?

- 수직 공간 제공 시 실내 고양이 코르티솔 수치 **37% 감소**
- 고양이의 **83%가 수직형 스크래처**를 선호
- 하루 15분 놀이로 비만 위험 **40% 감소**
- AAFP 가이드라인: 고양이 수(N) + 1개의 자원 배치 권장

### 주요 통계 (2026-03-10)

- 전체 데이터: 12,262건 (중복 제거 완료)
- Grade-A 큐레이션 데이터: 6,403건 (52.2%)
- 언어: 영어 6,929건 (56.5%), 한국어 5,333건 (43.5%)
- 출처: PubMed, arXiv, 네이버 블로그/뉴스, KIPRIS, 유튜브 등 36개 소스

### 데이터 수집 방법

- **9개 API 자동 수집**: PubMed, arXiv, OpenAlex, CORE, Zenodo, 네이버 검색, KIPRIS, Reddit
- **14노드 분산 크롤링**: YouTube, StackExchange, 수의학 전문 사이트
- **datatrove-v2 정제 파이프라인**: LLM 기반 품질 등급 분류, 중복 제거, 메타데이터 보강

### 사용 방법

```python
from datasets import load_dataset
dataset = load_dataset("playcat/playcat-cat-behavior-new-data-set")
```

### 활용 분야

- 고양이 행동 연구 및 수의학 연구
- 반려동물 복지 정책 분석
- 한국어-영어 이중 언어 NLP 모델 학습
- 반려동물 시장 트렌드 분석
- 수의학 AI 챗봇 및 추천 시스템 개발

### 관련 링크

- **Cat Enrichment Advisor** (인터랙티브 데모): [playcat/cat-enrichment-advisor](https://huggingface.co/spaces/playcat/cat-enrichment-advisor)
- **Cat Enrichment Methods 데이터셋** (50개 방법): [playcat/cat-enrichment-methods](https://huggingface.co/datasets/playcat/cat-enrichment-methods)
- **PlayCat 스토어**: [playcat.kr](https://playcat.kr)
- **블로그**: [playcat.xyz](https://playcat.xyz)
- **GitHub**: [playcatkorea/cat-behavior-enrichment](https://github.com/playcatkorea/cat-behavior-enrichment)

---

**Contact**: [PlayCat Research](https://playcat.xyz) | [playcat.kr](https://playcat.kr) | [GitHub](https://github.com/playcatkorea)
