---
type: "dataset"
id: "ToxicityPrompts/PolyGuardMix"
source: "huggingface"
url: "https://huggingface.co/datasets/ToxicityPrompts/PolyGuardMix"
downloads: 999
summary: "17개 언어로 된 LLM 안전성 검증 및 조정용 다국어 안전성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ToxicityPrompts/PolyGuardMix

> dataset · [Hugging Face](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardMix)

17개 언어로 된 LLM 안전성 검증 및 조정용 다국어 안전성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `labels of prompt harmfulness, response harmfulness, and response refusal` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `9199` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Truly multilingual safety moderation efforts for Large Language Models (LLMs)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `PolyGuard is trained on PolyGuardMix, the largest multilingual safety training corpus to date containing 1.91M samples across 17 languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 36796자 ≈ 9199 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Verm1ion__injection-sentry-xlmr|Verm1ion/injection-sentry-xlmr]]
- [[musubilabs__policylm-1.7b|musubilabs/policylm-1.7b]]
- [[vllm-sr__Vela-1.0-Encoder-307M-Shield|vllm-sr/Vela-1.0-Encoder-307M-Shield]]
