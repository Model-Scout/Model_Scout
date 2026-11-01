---
type: "dataset"
id: "Nagase-Kotono/Image-Detailed-Description-Korean"
source: "huggingface"
url: "https://huggingface.co/datasets/Nagase-Kotono/Image-Detailed-Description-Korean"
downloads: 67
summary: "이미지 상세 설명과 문서 이해를 위한 한국어 재캡션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# Nagase-Kotono/Image-Detailed-Description-Korean

> dataset · [Hugging Face](https://huggingface.co/datasets/Nagase-Kotono/Image-Detailed-Description-Korean)

이미지 상세 설명과 문서 이해를 위한 한국어 재캡션 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understa` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understa` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:visual_qa = `Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understa` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understa` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Models trained with recaptioned data (ReCap) datasets, show a trend of enhanced performance in tasks requiring detailed image descriptions and document understa` · 신뢰도 medium
