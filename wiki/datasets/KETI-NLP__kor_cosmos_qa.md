---
type: "dataset"
id: "KETI-NLP/kor_cosmos_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/kor_cosmos_qa"
downloads: 303
summary: "KETI-NLP/kor_cosmos_qa는 문맥 기반 상식 추론을 위한 한국어 질의응답 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KETI-NLP/kor_cosmos_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/kor_cosmos_qa)

KETI-NLP/kor_cosmos_qa는 문맥 기반 상식 추론을 위한 한국어 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Cosmos {QA}: Machine Reading Comprehension with Contextual Commonsense Reasoning` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Machine Reading Comprehension with Contextual Commonsense Reasoning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Machine Reading Comprehension with Contextual Commonsense Reasoning` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `170` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Machine Reading Comprehension with Contextual Commonsense Reasoning` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The data is distributed under the CC BY 4.0 license.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 256자 ≈ 170 토큰 (viewer statistics, default/validation)
