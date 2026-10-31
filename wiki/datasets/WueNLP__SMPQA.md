---
type: "dataset"
id: "WueNLP/SMPQA"
source: "huggingface"
url: "https://huggingface.co/datasets/WueNLP/SMPQA"
downloads: 107
summary: "SMPQA는 다국어 막대그래프와 원형차트에 대한 질문으로 다국어 OCR 성능을 평가하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
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
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# WueNLP/SMPQA

> dataset · [Hugging Face](https://huggingface.co/datasets/WueNLP/SMPQA)

SMPQA는 다국어 막대그래프와 원형차트에 대한 질문으로 다국어 OCR 성능을 평가하는 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `OCR` · 신뢰도 medium
- **작업**: [[질의응답]] — ner · readme = `questions about those plots` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `synthetic bar plots and pie charts` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `questions about those plots` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering, task:visual_qa = `questions and answers for all images` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic Multilingual Plot QA` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The SMPQA evaluation dataset` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
