---
type: "dataset"
id: "dev7halo/korean-mcfaq"
source: "huggingface"
url: "https://huggingface.co/datasets/dev7halo/korean-mcfaq"
downloads: 23
summary: "한국어 다중선택 FAQ 데이터셋으로 질문과 답변 학습에 활용됨."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dev7halo/korean-mcfaq

> dataset · [Hugging Face](https://huggingface.co/datasets/dev7halo/korean-mcfaq)

한국어 다중선택 FAQ 데이터셋으로 질문과 답변 학습에 활용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `'질문', '답변'` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `'질문'` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `'답변'` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `196` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `답변` 열 p90 294자 ≈ 196 토큰 (viewer statistics, default/train)
