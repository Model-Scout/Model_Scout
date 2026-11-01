---
type: "dataset"
id: "didi0di/KoChatGPT"
source: "huggingface"
url: "https://huggingface.co/datasets/didi0di/KoChatGPT"
downloads: 41
summary: "한국어 질문에 대해 ChatGPT가 자동 생성한 답변 데이터셋으로 대화 모델 학습용입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# didi0di/KoChatGPT

> dataset · [Hugging Face](https://huggingface.co/datasets/didi0di/KoChatGPT)

한국어 질문에 대해 ChatGPT가 자동 생성한 답변 데이터셋으로 대화 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `질문을 입력으로 주고` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `ChatGPT로 답변 자동생성` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `198` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `unknown` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 QA 데이터셋의 질문으로 답변 자동 생성(ChatGPT)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT 데이터: data/train` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `completion` 열 p90 297자 ≈ 198 토큰 (viewer statistics, default/train)
