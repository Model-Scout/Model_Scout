---
type: "dataset"
id: "taean-yoo/fire-exam-base64"
source: "huggingface"
url: "https://huggingface.co/datasets/taean-yoo/fire-exam-base64"
downloads: 6
summary: "소방공무원 시험 문제 기반 멀티모달 QA 데이터셋으로 문제 텍스트와 이미지 포함."
readme_status: "thin"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
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
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# taean-yoo/fire-exam-base64

> dataset · [Hugging Face](https://huggingface.co/datasets/taean-yoo/fire-exam-base64)

소방공무원 시험 문제 기반 멀티모달 QA 데이터셋으로 문제 텍스트와 이미지 포함.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `시각 정보를 담은 이미지 파일 경로` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering = `문제 텍스트, 선택지, 정답` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `소방공무원 시험 문제` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 소방공무원 시험 문제를 기반으로 구성된 멀티모달 QA 데이터셋입니다` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
