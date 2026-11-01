---
type: "dataset"
id: "CertifiedJoon/Korean-Instruction"
source: "huggingface"
url: "https://huggingface.co/datasets/CertifiedJoon/Korean-Instruction"
downloads: 59
summary: "네이버 지식인 데이터를 활용한 한국어 질의응답 및 언어 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# CertifiedJoon/Korean-Instruction

> dataset · [Hugging Face](https://huggingface.co/datasets/CertifiedJoon/Korean-Instruction)

네이버 지식인 데이터를 활용한 한국어 질의응답 및 언어 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Instruction + response format. Created for language model.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Instruction + response format.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Instruction + response format.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `554` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-permissive-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The most active korean qna site - Knowledge In Naver.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Created for language model.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `Response` 열 p90 832자 ≈ 554 토큰 (viewer statistics, default/train)
