---
type: "dataset"
id: "double7/MMMLU_subset"
source: "huggingface"
url: "https://huggingface.co/datasets/double7/MMMLU_subset"
downloads: 58
summary: "MMMLU의 10% 샘플로 다국어 일반 지식 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# double7/MMMLU_subset

> dataset · [Hugging Face](https://huggingface.co/datasets/double7/MMMLU_subset)

MMMLU의 10% 샘플로 다국어 일반 지식 평가용 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `we categorize the questions into four categories by subject` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `we categorize the questions into four categories by subject` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `93` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It covers a broad range of topics from 57 different categories` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `we sampled 10% of the original data to improve evaluation efficiency` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Question` 열 p90 371자 ≈ 93 토큰 (viewer statistics, KO_KR/test)
