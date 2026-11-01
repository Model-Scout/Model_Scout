---
type: "dataset"
id: "MYOTHANTZIN/eps-burmese-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/MYOTHANTZIN/eps-burmese-qa"
downloads: 40
summary: "한국 노동·이민법에 관한 미얀마어 질문-답변 데이터셋으로, E-9/EPS 비자 근로자 대상 법률 QA용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[my]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MYOTHANTZIN/eps-burmese-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/MYOTHANTZIN/eps-burmese-qa)

한국 노동·이민법에 관한 미얀마어 질문-답변 데이터셋으로, E-9/EPS 비자 근로자 대상 법률 QA용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — tag_match · readme, tags = `rag` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval = `Burmese-language question–answer pairs about Korean labour and immigration law` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `the answer, in Burmese, citing its source` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[my]] — metadata · languages = `my` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `145` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `The `test` split is offered as a small benchmark for grounded QA in a low-resource language` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = ``train` | 522 | 473 | 49` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 580자 ≈ 145 토큰 (viewer statistics, default/test)
