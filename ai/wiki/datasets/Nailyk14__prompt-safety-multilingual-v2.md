---
type: "dataset"
id: "Nailyk14/prompt-safety-multilingual-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Nailyk14/prompt-safety-multilingual-v2"
downloads: 51
summary: "다국어 안전성 프롬프트 데이터셋으로, 공격 유형 분류 및 안전성 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Nailyk14/prompt-safety-multilingual-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Nailyk14/prompt-safety-multilingual-v2)

다국어 안전성 프롬프트 데이터셋으로, 공격 유형 분류 및 안전성 평가에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `prompts anglais du même split et du même label, sans bloc de code, ≤ 400 tokens` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Cibles train par langue : {'benign': 1500, 'jailbreak': 600, 'injection_direct': 400, 'hijack': 300, 'data_exfiltration': 200}` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `52 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Sources : prompts anglais du même split et du même label` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Le split test est identique à l'original ; test_translated est nouveau.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Cibles train par langue : {'benign': 1500, 'jailbreak': 600, 'injection_direct': 400, 'hijack': 300, 'data_exfiltration': 200} ; validation : benign 300, autres` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
