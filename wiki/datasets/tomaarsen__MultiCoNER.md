---
type: "dataset"
id: "tomaarsen/MultiCoNER"
source: "huggingface"
url: "https://huggingface.co/datasets/tomaarsen/MultiCoNER"
downloads: 370
summary: "MultiCoNER은 11개 언어와 3개 도메인을 포함한 다국어 개체명 인식 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# tomaarsen/MultiCoNER

> dataset · [Hugging Face](https://huggingface.co/datasets/tomaarsen/MultiCoNER)

MultiCoNER은 11개 언어와 3개 도메인을 포함한 다국어 개체명 인식 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `a large multilingual dataset for Named Entity Recognition that covers 3 domains (Wiki sentences, questions, and search queries)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset follows the IOB format of CoNLL` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a large multilingual dataset for Named Entity Recognition that covers 3 domains (Wiki sentences, questions, and search queries) across 11 languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The 26M token dataset is compiled from public resources` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
