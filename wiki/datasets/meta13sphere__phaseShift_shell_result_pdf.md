---
type: "dataset"
id: "meta13sphere/phaseShift_shell_result_pdf"
source: "huggingface"
url: "https://huggingface.co/datasets/meta13sphere/phaseShift_shell_result_pdf"
downloads: 12281
summary: "AI 분야 수학 증명과 연구 자료를 담은 PDF 데이터셋으로, AI 연구 및 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[문서 파일 (출력 형식)|문서 파일]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# meta13sphere/phaseShift_shell_result_pdf

> dataset · [Hugging Face](https://huggingface.co/datasets/meta13sphere/phaseShift_shell_result_pdf)

AI 분야 수학 증명과 연구 자료를 담은 PDF 데이터셋으로, AI 연구 및 개발에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — tag_match · tags = `text-classification` · 신뢰도 low
- **작업**: [[임베딩]] — tag_match · readme, tags = `feature-extraction` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — tag_match · tags = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · tags = `token-classification` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · tags = `question-answering` · 신뢰도 low
- **작업**: [[표 질의응답]] — tag_match · tags = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme = `This repository provides comprehensive PDF research materials and Python scripts and something for mathematical proofs in the field of AI.` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:embedding, task:generation, task:information_extraction, task:question_answering, task:table_qa = `text` · 신뢰도 medium
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `This repository provides comprehensive PDF research materials and Python scripts and something for mathematical proofs in the field of AI.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:table_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `This repository provides comprehensive PDF research materials and Python scripts and something for mathematical proofs in the field of AI.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This repository provides comprehensive PDF research materials and Python scripts and something for mathematical proofs in the field of AI.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
