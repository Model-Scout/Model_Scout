---
type: "dataset"
id: "nayohan/Maths-College-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/Maths-College-ko"
downloads: 37
summary: "Maths-College 데이터셋의 5%를 한국어로 번역한 수학 관련 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/Maths-College-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/Maths-College-ko)

Maths-College 데이터셋의 5%를 한국어로 번역한 수학 관련 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `Translated 5% ajibawa-2023/Maths-College using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:translation = `Translated 5% ajibawa-2023/Maths-College` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:translation = `Translated 5% ajibawa-2023/Maths-College` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2692` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Translated 5% ajibawa-2023/Maths-College using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 4038자 ≈ 2692 토큰 (viewer statistics, default/train)
