---
type: "dataset"
id: "bzantium/KMMLU-en"
source: "huggingface"
url: "https://huggingface.co/datasets/bzantium/KMMLU-en"
downloads: 110
summary: "KMMLU 원본의 영어 번역판으로, 대규모 다중과제 언어 이해 평가용 객관식 문제 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# bzantium/KMMLU-en

> dataset · [Hugging Face](https://huggingface.co/datasets/bzantium/KMMLU-en)

KMMLU 원본의 영어 번역판으로, 대규모 다중과제 언어 이해 평가용 객관식 문제 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `questions and multiple-choice options (A, B, C, D), was machine-translated from Korean to English` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `questions and multiple-choice options (A, B, C, D), was machine-translated from Korean to English` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `403` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `cc-by-nd-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `expert-level multiple-choice questions across 45 diverse subjects, collected from original Korean exams` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Test | 35,030` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 605자 ≈ 403 토큰 (viewer statistics, Korean-History/test)
