---
type: "dataset"
id: "davanstrien/curation-decision-mix"
source: "huggingface"
url: "https://huggingface.co/datasets/davanstrien/curation-decision-mix"
downloads: 36
summary: "웹 페이지, 프롬프트, 수학 문제, 도서관 기록에 대한 큐레이션 질문에 답하는 결정 모델 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# davanstrien/curation-decision-mix

> dataset · [Hugging Face](https://huggingface.co/datasets/davanstrien/curation-decision-mix)

웹 페이지, 프롬프트, 수학 문제, 도서관 기록에 대한 큐레이션 질문에 답하는 결정 모델 학습 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each row is a text, a question, a set of options and a probability for each option` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `a set of options and a probability for each option` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2626` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `curation questions about web pages, prompts, maths problems and library records` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The training data of davanstrien/ultrabert-380m-curation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 10506자 ≈ 2626 토큰 (viewer statistics, all/train)
