---
type: "dataset"
id: "0601p/Traveling_Namuwiki_Actions"
source: "huggingface"
url: "https://huggingface.co/datasets/0601p/Traveling_Namuwiki_Actions"
downloads: 6
summary: "Namuwiki 페이지 링크로 만든 그래프 탐색용 인접 리스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 0601p/Traveling_Namuwiki_Actions

> dataset · [Hugging Face](https://huggingface.co/datasets/0601p/Traveling_Namuwiki_Actions)

Namuwiki 페이지 링크로 만든 그래프 탐색용 인접 리스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `can be used as next actions in a graph-navigation task` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `Each row contains a page title and the list of linked page titles` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each row contains a page title and the list of linked page titles` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `14` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Traveling Namuwiki Actions is an adjacency-list dataset built from Namuwiki page links.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was derived from the Hugging Face dataset heegyu/namuwiki.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 21자 ≈ 14 토큰 (viewer statistics, default/train)
