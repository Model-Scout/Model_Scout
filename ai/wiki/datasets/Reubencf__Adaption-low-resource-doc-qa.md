---
type: "dataset"
id: "Reubencf/Adaption-low-resource-doc-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/Reubencf/Adaption-low-resource-doc-qa"
downloads: 345
summary: "45개 이상의 저자원 언어로 된 문서 기반 질문응답 데이터셋으로 문서 이해 및 다국어 QA에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Reubencf/Adaption-low-resource-doc-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/Reubencf/Adaption-low-resource-doc-qa)

45개 이상의 저자원 언어로 된 문서 기반 질문응답 데이터셋으로 문서 이해 및 다국어 QA에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · tags, task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:ocr, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:visual_qa = `verbatim OCR in the page's native language` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:ocr, task:question_answering, task:visual_qa = `generated Q/A pair in one of 10 target languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `53 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `937` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `languages that are underrepresented in most open multimodal datasets.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `As a supervised fine-tuning set that specifically stresses the long tail of world languages` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `enhanced_prompt` 열 p90 3746자 ≈ 937 토큰 (viewer statistics, default/train)
