---
type: "dataset"
id: "Lakera/mosscap_prompt_injection"
source: "huggingface"
url: "https://huggingface.co/datasets/Lakera/mosscap_prompt_injection"
downloads: 1551
summary: "Lakera의 Mosscap 게임에서 수집한 프롬프트 인젝션 데이터셋으로, LLM 보안 연구에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Lakera/mosscap_prompt_injection

> dataset · [Hugging Face](https://huggingface.co/datasets/Lakera/mosscap_prompt_injection)

Lakera의 Mosscap 게임에서 수집한 프롬프트 인젝션 데이터셋으로, LLM 보안 연구에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `This is a dataset of prompt injections submitted to the game Mosscap by Lakera.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `Each row corresponds to a prompt that was sent to Mosscap.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The answer that was displayed to the user.` · 신뢰도 low
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `101` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Note that we release every prompt that we received, regardless of whether it truly is a prompt injection or not.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 404자 ≈ 101 토큰 (viewer statistics, default/validation)

## 이 데이터로 학습한 모델

- [[Verm1ion__injection-sentry-xlmr|Verm1ion/injection-sentry-xlmr]]
