---
type: "dataset"
id: "K-University-AIED/level-aware-qa-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/K-University-AIED/level-aware-qa-dataset"
downloads: 28
summary: "딥러닝 강의 자료 기반 GPT-4o 생성 멀티모달 학생 수준별 QA 데이터셋"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# K-University-AIED/level-aware-qa-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/K-University-AIED/level-aware-qa-dataset)

딥러닝 강의 자료 기반 GPT-4o 생성 멀티모달 학생 수준별 QA 데이터셋

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `It is a multi-modal dataset containing not only text but also visual information such as formulas and charts.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `It is a multi-modal dataset containing not only text but also visual information such as formulas and charts.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `The questions and answers are systematically organized according to the learner's comprehension level (High/Mid/Low).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `183` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a resource-based QA dataset of approximately 5,000 items generated using GPT-4o based on deep learning major lecture materials and foundational ` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 274자 ≈ 183 토큰 (viewer statistics, default/train)
