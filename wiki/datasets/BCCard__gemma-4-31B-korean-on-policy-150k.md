---
type: "dataset"
id: "BCCard/gemma-4-31B-korean-on-policy-150k"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/gemma-4-31B-korean-on-policy-150k"
downloads: 52
summary: "Gemma 4 검증기가 생성한 한국어 온-정책 질의응답 데이터로 EAGLE-3 모델 재학습용입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BCCard/gemma-4-31B-korean-on-policy-150k

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/gemma-4-31B-korean-on-policy-150k)

Gemma 4 검증기가 생성한 한국어 온-정책 질의응답 데이터로 EAGLE-3 모델 재학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `instruction (string) — the question / instruction` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `output (string) — the verifier-generated response` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1160` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1740자 ≈ 1160 토큰 (viewer statistics, default/train)
