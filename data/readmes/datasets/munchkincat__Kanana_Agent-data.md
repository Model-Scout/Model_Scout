---
language:
- ko
tags:
- finance
- multi-agent
- rag
---

# Kanana Agent Data

[Kanana Agent](https://github.com/Junhee-Park0/Kanana_Agent) 멀티 에이전트 시스템에서 사용하는 사전 수집 데이터입니다.  
프로젝트 루트의 `./data/` 경로에 그대로 두면 각 에이전트가 참조합니다.

> Stock Agent, Report Agent는 런타임 크롤링 또는 별도 데이터가 필요 없으므로 이 데이터셋에 포함되지 않습니다.

## 디렉터리 구조

~~~
data/
├── legal_data/          # Legal Agent — 법률 RAG DB
│   └── LawDB
├── news_data/           # News Agent — 뉴스 Vector DB
│   └── collection/
└── trend_data/          # Trend Agent — 금융 트렌드 데이터
    └── chroma_db_bge/
~~~

## 에이전트별 사용 데이터

| 에이전트 | 경로 | 설명 |
|---------|------|------|
| Legal Agent | `legal_data/LawDB` | 법률 문서 벡터 DB |
| News Agent | `news_data/collection` | 뉴스 기사 벡터 DB |
| Trend Agent | `trend_data/chroma_db_bge` | KCIF 기사 Chroma DB |

## 다운로드 방법

### Hugging Face CLI

~~~bash
pip install huggingface_hub

# data/ 폴더 전체 다운로드 (Kanana_Agent 프로젝트 루트에서 실행)
huggingface-cli download munchkincat/Kanana_Agent-data --repo-type dataset --local-dir ./data
~~~

### Python

~~~python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="munchkincat/Kanana_Agent-data",
    repo_type="dataset",
    local_dir="./data",
    local_dir_use_symlinks=False,
)
~~~

다운로드 후 `./data/` 아래에 위 디렉터리 구조가 생성되면 됩니다.

## 데이터 출처

| 데이터 | 출처 |
|--------|------|
| Legal Agent | 국가법령정보센터 |
| News Agent  | 한국경제, 머니투데이 |
| Trend Agent | KCIF 국제금융센터 |


## 업데이트

데이터는 크롤링·DB 구축 시점 기준이며, 이후 주기적으로 갱신될 수 있습니다.