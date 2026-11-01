---
type: "dataset"
id: "Jackrong/Claude-opus-4.7-TraceInversion-5000x"
source: "huggingface"
url: "https://huggingface.co/datasets/Jackrong/Claude-opus-4.7-TraceInversion-5000x"
downloads: 474
summary: "Claude 4.7 모델의 압축된 추론 과정을 역설계해 고품질 심층 추론 데이터를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Jackrong/Claude-opus-4.7-TraceInversion-5000x

> dataset · [Hugging Face](https://huggingface.co/datasets/Jackrong/Claude-opus-4.7-TraceInversion-5000x)

Claude 4.7 모델의 압축된 추론 과정을 역설계해 고품질 심층 추론 데이터를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `5,000 highly-curated deep-thinking samples.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `reverse-engineered into 5,000 detailed reasoning traces saturated with the "Opus Deep Logic Style" for SFT training.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1498` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English & Multilingual` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `a high-value fine-tuning dataset specifically designed for Advanced Reasoning Enhancement & Negentropy Learning.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `inverted_reasoning` 열 p90 5992자 ≈ 1498 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Jackrong__Qwopus3.5-9B-Coder-MTP-GGUF|Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF]]
- [[Jackrong__Qwopus3.6-27B-v2-MTP-GGUF|Jackrong/Qwopus3.6-27B-v2-MTP-GGUF]]
- [[Mungert__Qwopus3.5-9B-Coder-MTP-GGUF|Mungert/Qwopus3.5-9B-Coder-MTP-GGUF]]
- [[developerjeremylive__Qwopus3.5-9B-Coder-MTP-GGUF-etheroi|developerjeremylive/Qwopus3.5-9B-Coder-MTP-GGUF-etheroi]]
- [[developerjeremylive__Qwopus3.6-27B-v2-MTP-GGUF-etheroi|developerjeremylive/Qwopus3.6-27B-v2-MTP-GGUF-etheroi]]
- [[eadx__Qwopus3.6-27B-v2-MTP-GGUF|eadx/Qwopus3.6-27B-v2-MTP-GGUF]]
- [[jcbtc__qwopus3.6-27b-v2-chadrock-rocmfp4-mtp|jcbtc/qwopus3.6-27b-v2-chadrock-rocmfp4-mtp]]
