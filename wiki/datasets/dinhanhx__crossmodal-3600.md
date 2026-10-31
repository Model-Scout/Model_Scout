---
type: "dataset"
id: "dinhanhx/crossmodal-3600"
source: "huggingface"
url: "https://huggingface.co/datasets/dinhanhx/crossmodal-3600"
downloads: 434
summary: "36개 언어로 주석된 3600개 이미지로 구성된 다국어 이미지 캡션 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[리랭킹]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dinhanhx/crossmodal-3600

> dataset · [Hugging Face](https://huggingface.co/datasets/dinhanhx/crossmodal-3600)

36개 언어로 주석된 3600개 이미지로 구성된 다국어 이미지 캡션 평가 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `We apply this benchmark to model selection for massively multilingual image captioning models` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories, task_ids = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `a geographically-diverse set of 3600 images annotated with human-generated reference captions in 36 languages` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:reranking, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `annotated with human-generated reference captions in 36 languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `36 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Research in massively multilingual image captioning has been severely hampered by a lack of high-quality evaluation datasets.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `We apply this benchmark to model selection for massively multilingual image captioning models` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
