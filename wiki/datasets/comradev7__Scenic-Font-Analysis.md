---
type: "dataset"
id: "comradev7/Scenic-Font-Analysis"
source: "huggingface"
url: "https://huggingface.co/datasets/comradev7/Scenic-Font-Analysis"
downloads: 101
summary: "삼성 PRISM Scenic Font Analysis 프로젝트의 다중 트랙 글꼴 분석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# comradev7/Scenic-Font-Analysis

> dataset · [Hugging Face](https://huggingface.co/datasets/comradev7/Scenic-Font-Analysis)

삼성 PRISM Scenic Font Analysis 프로젝트의 다중 트랙 글꼴 분석 데이터셋입니다.

## 분류

- **작업**: [[이미지 인식]] — metadata · task_categories = `image-classification` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``text` | label text` · 신뢰도 medium
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Shared dataset repository for the Samsung PRISM Scenic Font Analysis project.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `so the data can be merged into a single training set without schema drift.` · 신뢰도 medium
