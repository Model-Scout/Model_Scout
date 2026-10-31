---
type: "dataset"
id: "MarkrAI/KoCommercial-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset"
downloads: 151
summary: "KoCommercial-Dataset은 약 1.44M 개의 상업적 용도 가능한 한국어 데이터셋으로, SSL 데이터 생성 및 다양한 과제에 활용 가능하다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
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
  - "[[중규모 데이터]]"
---
# MarkrAI/KoCommercial-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset)

KoCommercial-Dataset은 약 1.44M 개의 상업적 용도 가능한 한국어 데이터셋으로, SSL 데이터 생성 및 다양한 과제에 활용 가능하다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Self-Supervised method(AIHUB 데이터셋 가공)` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `0. (Default) Summary & Instruction-Answer` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `Self-Supervised method(AIHUB 데이터셋 가공)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `0. (Default) Summary & Instruction-Answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `527` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `코드는 누구나 사용하실 수 있고 과제와 Task에 맞게 활용하시면 감사하겠습니다!` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SSL 데이터 생성을 위한 코드 공개` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 791자 ≈ 527 토큰 (viewer statistics, default/train)
