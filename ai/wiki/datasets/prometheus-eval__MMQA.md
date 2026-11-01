---
type: "dataset"
id: "prometheus-eval/MMQA"
source: "huggingface"
url: "https://huggingface.co/datasets/prometheus-eval/MMQA"
downloads: 46
summary: "MMQA는 7개 언어의 문화 관련 장문 질의응답 데이터셋으로, 다국어·다문화 질문응답 평가용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[ca]]"
  - "[[es]]"
  - "[[eu]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# prometheus-eval/MMQA

> dataset · [Hugging Face](https://huggingface.co/datasets/prometheus-eval/MMQA)

MMQA는 7개 언어의 문화 관련 장문 질의응답 데이터셋으로, 다국어·다문화 질문응답 평가용입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `MMQA is a multilingual and multicultural long-form question-answering dataset` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `long-form question-answer pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `generate detailed, culturally informed answers` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[ca]] — metadata · languages = `ca` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[eu]] — metadata · languages = `eu` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `250` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `MMQA features long-form question-answer pairs that inquire about culture-related contexts` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The dataset is designed to evaluate the ability of models to generate detailed, culturally informed answers` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `chosen` 열 p90 1000자 ≈ 250 토큰 (viewer statistics, default/test)
