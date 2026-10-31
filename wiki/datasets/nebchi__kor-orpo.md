---
type: "dataset"
id: "nebchi/kor-orpo"
source: "huggingface"
url: "https://huggingface.co/datasets/nebchi/kor-orpo"
downloads: 24
summary: "nebchi/kor-orpo는 여러 한국어 대화 데이터셋을 참고해 만든 챗봇 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
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
  - "[[장문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nebchi/kor-orpo

> dataset · [Hugging Face](https://huggingface.co/datasets/nebchi/kor-orpo)

nebchi/kor-orpo는 여러 한국어 대화 데이터셋을 참고해 만든 챗봇 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `type: chat_template.argilla` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `type: chat_template.argilla` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `type: chat_template.argilla` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `5484` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Created with reference to the following datasets.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 8227자 ≈ 5484 토큰 (viewer statistics, kor-orpo/train)
