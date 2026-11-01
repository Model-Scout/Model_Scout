---
type: "dataset"
id: "eliceai/korean-webtext-edu"
source: "huggingface"
url: "https://huggingface.co/datasets/eliceai/korean-webtext-edu"
downloads: 878
summary: "HAERAE-HUB/KOREAN-WEBTEXT에서 교육적 가치가 높은 한국어 웹 텍스트를 선별한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
---
# eliceai/korean-webtext-edu

> dataset · [Hugging Face](https://huggingface.co/datasets/eliceai/korean-webtext-edu)

HAERAE-HUB/KOREAN-WEBTEXT에서 교육적 가치가 높은 한국어 웹 텍스트를 선별한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `교육적이고 사실적이며 구조화된 한국어 웹 텍스트를 대규모로 제공하여, 모델 학습의 질을 높이는 것을 목표로 합니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:language_modeling = `문서의 텍스트 본문.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:language_modeling = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `교육적 가치가 높은 콘텐츠만을 필터링하여 구축되었습니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `모델 학습의 질을 높이는 것을 목표로 합니다.` · 신뢰도 medium
