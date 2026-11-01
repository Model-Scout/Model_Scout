---
type: "dataset"
id: "KorQuAD/squad_kor_v1"
source: "huggingface"
url: "https://huggingface.co/datasets/KorQuAD/squad_kor_v1"
downloads: 1454
summary: "KorQuAD 1.0은 한국어 기계 독해를 위한 대규모 질의응답 데이터셋입니다."
readme_status: "template"
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KorQuAD/squad_kor_v1

> dataset · [Hugging Face](https://huggingface.co/datasets/KorQuAD/squad_kor_v1)

KorQuAD 1.0은 한국어 기계 독해를 위한 대규모 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `question-and-answer dataset constructed for Korean machine reading comprehension` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question-and-answer dataset constructed for Korean machine reading comprehension` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `34` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `cc-by-nd-4.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 52자 ≈ 34 토큰 (viewer statistics, squad_kor_v1/validation)
