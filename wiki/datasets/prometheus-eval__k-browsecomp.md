---
type: "dataset"
id: "prometheus-eval/k-browsecomp"
source: "huggingface"
url: "https://huggingface.co/datasets/prometheus-eval/k-browsecomp"
downloads: 601
summary: "K-BrowseComp는 한국어 웹 브라우징 에이전트 벤치마크로, 한국어 웹사이트에서 정보를 검색하는 문제로 구성됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# prometheus-eval/k-browsecomp

> dataset · [Hugging Face](https://huggingface.co/datasets/prometheus-eval/k-browsecomp)

K-BrowseComp는 한국어 웹 브라우징 에이전트 벤치마크로, 한국어 웹사이트에서 정보를 검색하는 문제로 구성됨.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `require retrieving information across multiple Korean websites` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `the question (Korean)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the gold short answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `188` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a web-browsing agent benchmark` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `problem` 열 p90 283자 ≈ 188 토큰 (viewer statistics, verified/test)
