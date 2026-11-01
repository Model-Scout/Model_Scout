---
type: "dataset"
id: "neulab/CulturalGround"
source: "huggingface"
url: "https://huggingface.co/datasets/neulab/CulturalGround"
downloads: 6084
summary: "CulturalGround은 42개국 39개 언어의 문화 지식을 기반으로 한 대규모 다국어 멀티모달 VQA 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
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
  - "[[문화·관광]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# neulab/CulturalGround

> dataset · [Hugging Face](https://huggingface.co/datasets/neulab/CulturalGround)

CulturalGround은 42개국 39개 언어의 문화 지식을 기반으로 한 대규모 다국어 멀티모달 VQA 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `generate factually grounded VQA pairs` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `collecting 1-3 images per entity` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `a large-scale cultural VQA dataset` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `multilingual multimodal LLMs` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset was used to train the CulturalPangea model.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
