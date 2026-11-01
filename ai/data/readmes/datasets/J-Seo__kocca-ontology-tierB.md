---
license: other
license_name: cc-by-sa-2.0-kr
license_link: https://creativecommons.org/licenses/by-sa/2.0/kr/
language:
  - ko
tags:
  - korean
  - lexicon
  - dictionary
  - language-norms
  - knowledge-graph
pretty_name: Korean Lexicon Ontology — Tier B
size_categories:
  - 1M<n<10M
task_categories:
  - text-retrieval
  - feature-extraction
---

# Korean Lexicon Ontology — Tier B (1.7M Headwords SQLite)

> 한국어 4대 언어자원(표준국어대사전·우리말샘·한국어기초사전·어문 규범)을
> 단일 SQLite로 통합한 **170만 표제어** 데이터셋입니다.
> Companion data for the [Korean Lexicon Ontology Explorer](https://github.com/J-Seo/kocca-ontology-explorer-public).

## 개요

본 데이터셋은 국립국어원이 공개한 4개 한국어 언어자원을 통합·정규화하여
검색·조회에 최적화된 단일 SQLite 파일로 제공합니다.

| 자원 | 표제어/조항 수 | 비고 |
|---|---:|---|
| 표준국어대사전 (stdict) | 436,574 | 표준어 |
| 우리말샘 (urimalsam) | 1,204,559 | 신어·방언·전문어 포함 |
| 한국어기초사전 (krdict) | 53,672 | 외국인 학습자용 |
| 한국어 어문 규범 (kornorms) | 110조항 + 380부록 + 80,115용례 | 한글 맞춤법·외래어·로마자 등 |
| **합계** | **약 1,694,805 표제어 + 80,115 용례** | |

## 파일 구성

| 파일 | 크기 | 설명 |
|---|---|---|
| `lexicon.sqlite` | 810 MB | 통합 표제어 + 용례 SQLite (WAL 모드) |
| `lexicon.meta.json` | < 1 KB | 버전·생성일·각 자원별 카운트 메타 |

## 스키마

```sql
-- 통합 표제어 테이블
CREATE TABLE lexicon_entries (
  id          INTEGER PRIMARY KEY,
  source      TEXT NOT NULL,        -- 'stdict' | 'urimalsam' | 'krdict'
  headword    TEXT NOT NULL,        -- 표제어
  pos         TEXT,                 -- 품사
  definition  TEXT,                 -- 뜻풀이
  examples    TEXT,                 -- JSON array (있을 시)
  meta        TEXT                  -- JSON object (자원별 확장 메타)
);
CREATE INDEX idx_headword ON lexicon_entries(headword);
CREATE INDEX idx_source   ON lexicon_entries(source);

-- 외래어·로마자 용례
CREATE TABLE norm_examples (
  id          INTEGER PRIMARY KEY,
  category    TEXT NOT NULL,        -- 'foreign' | 'romanization' | ...
  original    TEXT,                 -- 원어 또는 한국어
  normalized  TEXT,                 -- 정규화/표준 표기
  source_ref  TEXT                  -- 출처 조항 ID
);
```

상세 스키마는 `lexicon.meta.json` 참고.

## 사용법

### 직접 다운로드 (huggingface-cli)

```bash
hf download J-Seo/kocca-ontology-tierB \
  --repo-type dataset \
  --local-dir ./lexicon
```

### Python (datasets 라이브러리)

```python
from huggingface_hub import hf_hub_download
import sqlite3

path = hf_hub_download(
    repo_id="J-Seo/kocca-ontology-tierB",
    filename="lexicon.sqlite",
    repo_type="dataset",
)
con = sqlite3.connect(path)
rows = con.execute(
    "SELECT headword, definition FROM lexicon_entries WHERE headword LIKE ? LIMIT 5",
    ("사랑%",),
).fetchall()
```

### 웹앱 (Korean Lexicon Ontology Explorer)

본 데이터셋은 Next.js 기반 탐색 웹앱과 연동되어 있습니다.
전체 셋업 절차는 다음 저장소를 참고하세요.

→ https://github.com/J-Seo/kocca-ontology-explorer-public

## 라이선스

**CC BY-SA 2.0 KR** (https://creativecommons.org/licenses/by-sa/2.0/kr/)

원자료 라이선스를 그대로 승계합니다. 재이용 시 다음을 준수해야 합니다.

1. **저작자 표시**: 국립국어원 및 각 자원명·URL 명시
2. **동일조건 변경허락**: 재가공물도 동일한 CC BY-SA 라이선스로 공개
3. 상업적 이용 가능 (위 두 조건 충족 시)

### 원자료 출처

- 표준국어대사전 — https://stdict.korean.go.kr
- 우리말샘 — https://opendict.korean.go.kr
- 한국어기초사전 — https://krdict.korean.go.kr
- 한국어 어문 규범 — https://kornorms.korean.go.kr

## 가공 내역

- 4개 자원의 이질적 스키마를 단일 `lexicon_entries` 테이블로 정규화
- `headword`, `source` 인덱스 추가로 검색 성능 향상
- 외래어/로마자 용례 80,115건을 별도 테이블로 추출
- 어문 규범 110조항 + 부록 변경 380건을 구조화 (별도 JSON, 본 SQLite에는 미포함 — repo 참고)

## 인용

```bibtex
@dataset{korean_lexicon_ontology_tierB_2026,
  title     = {Korean Lexicon Ontology — Tier B (1.7M Headwords SQLite)},
  author    = {Seo, Jaehyung},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/datasets/J-Seo/kocca-ontology-tierB},
  note      = {Derived from open Korean lexical resources by NIKL.
               Licensed under CC BY-SA 2.0 KR.}
}
```

## 면책

비공식 가공물입니다. 국립국어원의 공식 입장이나 데이터 정합성을 보증하지 않습니다.
정확한 표준 데이터는 위 출처의 원자료를 참고하십시오.
