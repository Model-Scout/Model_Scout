---
type: "dataset"
id: "mariem123kfg/sob-ft-stage-eval"
source: "huggingface"
url: "https://huggingface.co/datasets/mariem123kfg/sob-ft-stage-eval"
downloads: 13
summary: "boradorish/STAGE-eval 코퍼스를 변환한 질문-컨텍스트 및 정답 JSON 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mariem123kfg/sob-ft-stage-eval

> dataset · [Hugging Face](https://huggingface.co/datasets/mariem123kfg/sob-ft-stage-eval)

boradorish/STAGE-eval 코퍼스를 변환한 질문-컨텍스트 및 정답 JSON 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `original split preserved in question_type` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Split at === Report === / === 보고서 === → question + context` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `user_prompt` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `gold_json` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `18582` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `HF train + test` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `HF train + test` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 27872자 ≈ 18582 토큰 (viewer statistics, default/train)
