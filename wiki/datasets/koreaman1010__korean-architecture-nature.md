---
type: "dataset"
id: "koreaman1010/korean-architecture-nature"
source: "huggingface"
url: "https://huggingface.co/datasets/koreaman1010/korean-architecture-nature"
downloads: 123
summary: "대한민국 전통 및 현대 건축물과 자연 풍경 사진으로 구성된 연구 및 AI 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# koreaman1010/korean-architecture-nature

> dataset · [Hugging Face](https://huggingface.co/datasets/koreaman1010/korean-architecture-nature)

대한민국 전통 및 현대 건축물과 자연 풍경 사진으로 구성된 연구 및 AI 학습용 데이터셋입니다.

## 분류

- **작업**: [[이미지 인식]] — metadata · readme, task_categories = `image-classification` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision, task:visual_qa = `This dataset contains photographs of Korean traditional architecture, modern buildings, and nature landscrapes.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `This dataset contains photographs of Korean traditional architecture, modern buildings, and nature landscrapes.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset contains photographs of Korean traditional architecture, modern buildings, and nature landscrapes.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `organized for public research and AI training purposes.` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
