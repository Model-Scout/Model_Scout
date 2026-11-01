---
license: cc-by-4.0
task_categories:
  - text-retrieval
language:
  - en
  - ko
  - fr
  - id
  - ja
  - th
  - zh
tags:
  - BEIR
  - aerospace
  - cross-lingual
  - information-retrieval
  - STELLA
  - NASA
  - NTRS
pretty_name: "STELLA (Parquet)"
configs:
  - config_name: corpus
    data_files:
      - split: test
        path: data/corpus/*.parquet
  - config_name: en-queries
    data_files:
      - split: test
        path: data/en-queries/*.parquet
  - config_name: en-qrels
    data_files:
      - split: test
        path: data/en-qrels/*.parquet
  - config_name: ko-queries
    data_files:
      - split: test
        path: data/ko-queries/*.parquet
  - config_name: ko-qrels
    data_files:
      - split: test
        path: data/ko-qrels/*.parquet
  - config_name: fr-queries
    data_files:
      - split: test
        path: data/fr-queries/*.parquet
  - config_name: fr-qrels
    data_files:
      - split: test
        path: data/fr-qrels/*.parquet
  - config_name: id-queries
    data_files:
      - split: test
        path: data/id-queries/*.parquet
  - config_name: id-qrels
    data_files:
      - split: test
        path: data/id-qrels/*.parquet
  - config_name: ja-queries
    data_files:
      - split: test
        path: data/ja-queries/*.parquet
  - config_name: ja-qrels
    data_files:
      - split: test
        path: data/ja-qrels/*.parquet
  - config_name: th-queries
    data_files:
      - split: test
        path: data/th-queries/*.parquet
  - config_name: th-qrels
    data_files:
      - split: test
        path: data/th-qrels/*.parquet
  - config_name: zh-queries
    data_files:
      - split: test
        path: data/zh-queries/*.parquet
  - config_name: zh-qrels
    data_files:
      - split: test
        path: data/zh-qrels/*.parquet
---

# STELLA (Parquet)

[telepix/STELLA](https://huggingface.co/datasets/telepix/STELLA) 데이터셋의 HuggingFace-native Parquet 변환 버전입니다.

STELLA는 NASA Technical Reports Server (NTRS) 문서 기반 **항공우주 도메인 Cross-lingual IR 벤치마크**입니다.

## Usage

```python
from datasets import load_dataset

# Corpus (영어, 2.4M passages)
corpus = load_dataset("datalama/STELLA", "corpus", split="test")

# 한국어 쿼리
ko_queries = load_dataset("datalama/STELLA", "ko-queries", split="test")

# 한국어 qrels
ko_qrels = load_dataset("datalama/STELLA", "ko-qrels", split="test")
```

## Configs

| Config | Split | Rows | Description |
|--------|-------|------|-------------|
| `corpus` | test | 2,405,044 | 영어 corpus (전 언어 공유) |
| `{{lang}}-queries` | test | 1,000 | 언어별 쿼리 (7개 언어) |
| `{{lang}}-qrels` | test | 1,000 | 언어별 relevance judgments |

**지원 언어**: en, ko, fr, id, ja, th, zh

## Schema

**corpus**: `_id` (str), `title` (str), `text` (str)

**queries**: `_id` (str), `text` (str)

**qrels**: `query-id` (str), `corpus-id` (str), `score` (int)

## Cross-lingual Evaluation

STELLA는 **비대칭 cross-lingual IR** 벤치마크입니다:
- Corpus: 영어 전용 (NASA NTRS 문서)
- Queries: 영어 원본 + 6개 번역 언어
- 평가: 다국어 쿼리 → 영어 corpus 검색

### 쿼리 유형
- **TCQ** (Terminology Concordant Query): 기술 용어는 영어 유지, 설명만 번역
- **TAQ** (Terminology Agnostic Query): 전체를 타겟 언어로 완전 번역

## Corpus Categories

| Category | Passages |
|----------|----------|
| Space Sciences | 539,764 |
| Geosciences | 362,624 |
| Aeronautics | 306,505 |
| Engineering | 292,337 |
| Physics | 242,575 |
| Chemistry and Materials | 225,136 |
| Life Sciences | 197,600 |
| Mathematical/Computer Sciences | 130,214 |
| Astronautics | 97,773 |
| Social/Information Sciences | 10,516 |

## Citation

```bibtex
@article{{kim2026stella,
    title={{STELLA: Self-Reflective Terminology-Aware Framework for Building an Aerospace Information Retrieval Benchmark}},
    author={{Bongmin Kim}},
    year={{2026}},
    eprint={{2601.03496}},
    archivePrefix={{arXiv}},
    primaryClass={{cs.IR}}
}}
```

## License

CC-BY-4.0 (원본 STELLA 라이선스 준수)

## Source

이 데이터셋은 [telepix/STELLA](https://huggingface.co/datasets/telepix/STELLA)의 포맷 변환 버전입니다.
원본 데이터의 텍스트는 변경 없이 유지되었으며, HuggingFace `load_dataset()` 호환을 위해 Parquet 포맷으로 변환하였습니다.
