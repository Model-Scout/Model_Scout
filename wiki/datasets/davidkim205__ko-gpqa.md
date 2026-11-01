---
type: "dataset"
id: "davidkim205/ko-gpqa"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/ko-gpqa"
downloads: 7
summary: "고난도 과학 문제로 구성된 GPQA 벤치마크의 한국어 번역 데이터셋으로, 언어 모델의 심층 이해와 추론 능력 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[교육]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# davidkim205/ko-gpqa

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/ko-gpqa)

고난도 과학 문제로 구성된 GPQA 벤치마크의 한국어 번역 데이터셋으로, 언어 모델의 심층 이해와 추론 능력 평가에 사용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `GPQA is designed to go beyond simple fact retrieval and instead test an AI system’s ability to perform deep understanding and logical reasoning.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `the dataset is formatted in JSON structure` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `which consists of high-difficulty science questions` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
