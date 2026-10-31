---
type: "dataset"
id: "kaggle/metformin/korean-guidelines-for-primary-physicians"
source: "kaggle"
url: "https://www.kaggle.com/datasets/metformin/korean-guidelines-for-primary-physicians"
downloads: 183
summary: "한국 1차 진료의사용 PDF 가이드라인 데이터로 QA 봇 개발 등에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/metformin/korean-guidelines-for-primary-physicians

> dataset · [Kaggle](https://www.kaggle.com/datasets/metformin/korean-guidelines-for-primary-physicians)

한국 1차 진료의사용 PDF 가이드라인 데이터로 QA 봇 개발 등에 활용 가능

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Fine-tuning the open-sourced LLMs can be done.` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `This dataset could be used to make an QA bot or solve VQA tasks.` · 신뢰도 medium
- **작업**: [[이미지 이해]] — ner · readme = `This dataset could be used to make an QA bot or solve VQA tasks.` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `Open PDF files for primary physicians to treat commonly-seen diseases` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `This dataset could be used to make an QA bot or solve VQA tasks.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `Database: Open Database, Contents: © Original Authors` · 신뢰도 high
- **도메인**: [[의료·보건]] — tag_match · readme, tags = `health` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Fine-tuning the open-sourced LLMs can be done.` · 신뢰도 medium
