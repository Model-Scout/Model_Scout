---
type: "dataset"
id: "jbaehova/KrRubberStamp-1.65K"
source: "huggingface"
url: "https://huggingface.co/datasets/jbaehova/KrRubberStamp-1.65K"
downloads: 277
summary: "한국어 사무 업무 문서 이해 및 정확한 답변 평가용 1,650개 합성 업무 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[표 질의응답]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jbaehova/KrRubberStamp-1.65K

> dataset · [Hugging Face](https://huggingface.co/datasets/jbaehova/KrRubberStamp-1.65K)

한국어 사무 업무 문서 이해 및 정확한 답변 평가용 1,650개 합성 업무 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — tag_match · readme, tags = `information-extraction` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — metadata · tags, task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · modality, readme, task:ocr = `Input documents | **8,093** PDF, XLSX, HWPX and PNG files` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction, task:question_answering, task:table_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering, task:table_qa = `Models must read office documents, reconcile evidence and return structured answers that can be graded automatically.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4322` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `covering year-end tax settlement and payroll, alongside VAT and information extraction.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The single `train` split is the public distribution of all 1,650 tasks.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `trace` 열 p90 6484자 ≈ 4322 토큰 (viewer statistics, default/train)
