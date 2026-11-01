---
type: "dataset"
id: "KETI-NLP/kor_qasc"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_qasc"
downloads: 69
summary: "QASC 데이터셋은 문장 조합을 통한 질의응답을 위한 데이터입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KETI-NLP/kor_qasc

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_qasc)

QASC 데이터셋은 문장 조합을 통한 질의응답을 위한 데이터입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `QASC: A Dataset for Question Answering via Sentence Composition` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `QASC: A Dataset for Question Answering via Sentence Composition` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `81` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `formatted_question` 열 p90 122자 ≈ 81 토큰 (viewer statistics, default/validation)
