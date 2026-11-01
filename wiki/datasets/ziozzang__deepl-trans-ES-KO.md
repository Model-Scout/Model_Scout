---
type: "dataset"
id: "ziozzang/deepl-trans-ES-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/ziozzang/deepl-trans-ES-KO"
downloads: 4
summary: "DeepL 번역을 이용해 스페인어 위키피디아 문서를 한국어로 자동 수집한 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[es]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ziozzang/deepl-trans-ES-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/ziozzang/deepl-trans-ES-KO)

DeepL 번역을 이용해 스페인어 위키피디아 문서를 한국어로 자동 수집한 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `From ES/Spanish to KO/Korean.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `From ES/Spanish to KO/Korean.` · 신뢰도 medium
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The strings/corpus are aggregated from wikipedia(pt)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `whole data collected by Jioh L.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
