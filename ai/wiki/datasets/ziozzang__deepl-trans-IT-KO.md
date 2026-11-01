---
type: "dataset"
id: "ziozzang/deepl-trans-IT-KO"
source: "huggingface"
url: "https://huggingface.co/datasets/ziozzang/deepl-trans-IT-KO"
downloads: 6
summary: "이탈리아어 위키피디아 문서를 DeepL 번역한 한국어 병렬 말뭉치 데이터셋입니다."
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
  - "[[it]]"
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
  - "[[중규모 데이터]]"
---
# ziozzang/deepl-trans-IT-KO

> dataset · [Hugging Face](https://huggingface.co/datasets/ziozzang/deepl-trans-IT-KO)

이탈리아어 위키피디아 문서를 DeepL 번역한 한국어 병렬 말뭉치 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `This dataset is some wikipedia article with DeepL translation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `This dataset is some wikipedia article with DeepL translation` · 신뢰도 medium
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The strings/corpus are aggregated from wikipedia(pt)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `whole data collected by Jioh L.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
