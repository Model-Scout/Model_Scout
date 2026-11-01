---
type: "dataset"
id: "kaggle/jkim289/handwritten-korean-characters"
source: "kaggle"
url: "https://www.kaggle.com/datasets/jkim289/handwritten-korean-characters"
downloads: 353
summary: "손글씨로 쓴 64개 한글 음절 이미지 데이터셋으로 문자 인식에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/jkim289/handwritten-korean-characters

> dataset · [Kaggle](https://www.kaggle.com/datasets/jkim289/handwritten-korean-characters)

손글씨로 쓴 64개 한글 음절 이미지 데이터셋으로 문자 인식에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `image classification` · 신뢰도 medium
- **작업**: [[이미지 인식]] — tag_match · tags = `image classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `jpg images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Database: Open Database, Contents: © Original Authors` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Hangul Database contains 64 of the most common hangul syllables as jpg images` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Hangul Database Extended was made using 20 random image distorsions` · 신뢰도 low
