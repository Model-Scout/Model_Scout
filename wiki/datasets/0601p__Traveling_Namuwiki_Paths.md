---
type: "dataset"
id: "0601p/Traveling_Namuwiki_Paths"
source: "huggingface"
url: "https://huggingface.co/datasets/0601p/Traveling_Namuwiki_Paths"
downloads: 14
summary: "Namuwiki 페이지 링크 기반 그래프 내비게이션 데이터셋으로 경로 탐색에 사용됨."
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# 0601p/Traveling_Namuwiki_Paths

> dataset · [Hugging Face](https://huggingface.co/datasets/0601p/Traveling_Namuwiki_Paths)

Namuwiki 페이지 링크 기반 그래프 내비게이션 데이터셋으로 경로 탐색에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Traveling Namuwiki is a graph-navigation dataset built from Namuwiki page links.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval = `Each example contains a start page, a target page, and one or more valid paths between them.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Paths are stored as intermediate page-title lists, excluding the start and target pages.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `13` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Traveling Namuwiki is a graph-navigation dataset built from Namuwiki page links.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `validation | 99,732 | 5.0% | 107.2 MiB` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 1,795,552 | 90.0% | 1.91 GiB` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `start_title` 열 p90 19자 ≈ 13 토큰 (viewer statistics, default/validation)
