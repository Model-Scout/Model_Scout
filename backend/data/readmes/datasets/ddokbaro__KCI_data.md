---
license: cc-by-nc-4.0
task_categories:
- text-retrieval
- text-generation
- summarization
language:
- ko
- en
tags:
- kci
- academic
- digital-humanities
- oai-pmh
- bibliometrics
size_categories:
- 1M<n<10M
pretty_name: KCI Metadata Archive
source_datasets:
- NRF KCI
configs:
- config_name: default
  data_files:
  - split: train
    path: "*.jsonl"
---

# 📚 KCI Metadata Archive (2026.01 Snapshot)

한국학술지인용색인(KCI)에 등재된 국내 학술지 논문의 서지 정보(메타데이터)를 집대성한 데이터셋입니다.
디지털 인문학(DH), 계량 서지학, 지식 그래프 구축 및 LLM의 한국어 학술 도메인 학습 등을 위해 구축되었습니다.

> **Note:** 이 데이터셋은 2026년 1월 24일 기준의 스냅샷입니다.

## 📂 Dataset Structure (데이터 구조)

데이터는 **JSONL (JSON Lines)** 포맷으로 제공되어 대용량 처리에 최적화되어 있습니다.

### File Information
* **Filename:** `kci_articles_20260124.jsonl`
* **Size:** 약 11GB (Raw XML 변환본)
* **Count:** 약 3,000,000+ 건 (추산)

### Data Fields (필드 설명)
각 라인은 하나의 논문(Article) 정보를 담고 있습니다.

```json
{
  "id": "ART002000341",          // KCI 논문 식별자
  "format": "oai_kci",           // 원본 포맷 (oai_kci 또는 oai_dc)
  "title_ko": "국문 논문 제목",
  "title_en": "English Title",
  "journal": {
    "journal_name": "학술지명",
    "publisher": "발행기관",
    "pub_year": "2024",
    "volume": "10",
    "issue": "2"
  },
  "authors": [                   // 저자 목록 (List)
    "홍길동(한국대학교)",
    "Kim, Chul-Soo(Hankuk Univ.)"
  ],
  "abstract_ko": "국문 초록 텍스트...",
  "abstract_en": "Abstract text...",
  "keywords": "키워드1, 키워드2",
  "citation_count": "5",         // 피인용 횟수
  "doi": "10.xxxx/....",         // DOI
  "url": "[https://www.kci.go.kr/](https://www.kci.go.kr/)..." // KCI 원문 링크
}

## 🚀 How to Use (사용 방법)

### 1. Python (Hugging Face `datasets` 라이브러리)

가장 추천하는 방식입니다. 스트리밍 방식을 지원하여 11GB를 한 번에 다운로드하지 않고도 데이터를 탐색할 수 있습니다.

```python
from datasets import load_dataset

# 데이터셋 불러오기
dataset = load_dataset("ddokbaro/KCI_data", split="train")

# 데이터 확인 (첫 5개)
for article in dataset.select(range(5)):
    print(f"[{article['pub_year']}] {article['title_ko']} - {article['authors']}")
```

### 2. Pandas (Dataframe)

```python
import pandas as pd

# JSONL 파일 직접 로드 (주의: 메모리 용량 필요)
df = pd.read_json("kci_articles_20260124.jsonl", lines=True)
print(df.head())
```

## 🛠 Included Scripts (수집 및 가공 코드)

이 데이터셋의 투명성과 재현성을 위해 사용된 파이썬 스크립트를 함께 제공합니다. [Files and versions](https://huggingface.co/datasets/ddokbaro/KCI_data/tree/main) 탭에서 확인하실 수 있습니다.

1.  **`kci_full_download.py`**:
    * KCI OAI-PMH 서버에서 Raw XML 데이터를 수집하는 크롤러입니다.
    * 네트워크 중단 시 자동 이어받기(Resume) 기능을 지원합니다.
2.  **`kci_xml_to_jsonl.py`**:
    * 수집된 2만여 개의 XML 파일을 파싱하여 하나의 JSONL 파일로 변환합니다.
    * `oai_kci`(상세)와 `oai_dc`(기본) 포맷을 모두 지원하는 하이브리드 파서입니다.

## ⚖️ License & Disclaimer

### License
* **Dataset:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (저작자표시-비영리)
* **Scripts:** MIT License

### Disclaimer (면책 조항)
본 데이터셋에 포함된 논문의 제목, 초록, 저자명 등 원천 메타데이터의 저작권 및 지적재산권은 **한국연구재단(NRF)**, 각 학술 단체 및 저자에게 있습니다.
* 이 데이터셋은 학술 연구 및 교육 목적을 위해 큐레이션된 2차 저작물입니다.
* 상업적 목적(예: 원천 데이터 판매)으로 이용할 수 없습니다.

## 👤 Maintainer
**Prof. Kim Ba-ro (김바로)**
* The Academy of Korean Studies (한국학중앙연구원)
