---
type: "dataset"
id: "K-University-AIED/LearningChat_accounting_ai_questions"
source: "huggingface"
url: "https://huggingface.co/datasets/K-University-AIED/LearningChat_accounting_ai_questions"
downloads: 82
summary: "회계입문 수업 AI질문 1회 과제 제출 이미지 메타데이터 공개용 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# K-University-AIED/LearningChat_accounting_ai_questions

> dataset · [Hugging Face](https://huggingface.co/datasets/K-University-AIED/LearningChat_accounting_ai_questions)

회계입문 수업 AI질문 1회 과제 제출 이미지 메타데이터 공개용 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `학생들이 과제 제출 과정에서 업로드한 이미지 파일들로 구성되어 있다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `이미지 파일 1개 = metadata.csv 1행` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `본 문서와 함께 제공되는 metadata.csv는 이미지 파일 1개당 1행을 가지는 인벤토리다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `본 문서와 함께 제공되는 metadata.csv는 이미지 파일 1개당 1행을 가지는 인벤토리다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
