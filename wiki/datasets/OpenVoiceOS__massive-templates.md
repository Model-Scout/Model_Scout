---
type: "dataset"
id: "OpenVoiceOS/massive-templates"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenVoiceOS/massive-templates"
downloads: 194
summary: "OVOS 의도 분류 벤치마크용으로 수집된 다국어 의도-파서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# OpenVoiceOS/massive-templates

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenVoiceOS/massive-templates)

OVOS 의도 분류 벤치마크용으로 수집된 다국어 의도-파서 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `utterances` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `intent-classification datasets` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `51 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `10` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OVOS intent-classification datasets` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `~13.5k per locale (train + dev pooled) — ~704k total` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `template` 열 p90 40자 ≈ 10 토큰 (viewer statistics, ko-KR-templates/train)
