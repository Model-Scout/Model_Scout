---
type: "dataset"
id: "vpermilp/nllb-200-distilled-600M-rust"
source: "huggingface"
url: "https://huggingface.co/datasets/vpermilp/nllb-200-distilled-600M-rust"
downloads: 157
summary: "NLLB-200의 600M 증류 모델로 200개 언어 간 기계 번역 연구용 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# vpermilp/nllb-200-distilled-600M-rust

> dataset · [Hugging Face](https://huggingface.co/datasets/vpermilp/nllb-200-distilled-600M-rust)

NLLB-200의 600M 증류 모델로 200개 언어 간 기계 번역 연구용 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It allows for single sentence translation among 200 languages.` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `NLLB-200 is a machine translation model primarily intended for research in machine translation` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `It allows for single sentence translation among 200 languages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `196 languages` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `NLLB-200 is trained on general domain text data` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `NLLB-200 model was evaluated using BLEU, spBLEU, and chrF++ metrics` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Information about training algorithms, parameters, fairness constraints or other applied approaches, and features.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
