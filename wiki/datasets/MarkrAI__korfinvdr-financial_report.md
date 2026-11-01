---
type: "dataset"
id: "MarkrAI/korfinvdr-financial_report"
source: "huggingface"
url: "https://huggingface.co/datasets/MarkrAI/korfinvdr-financial_report"
downloads: 72
summary: "한국은행 금융안정보고서로 구성된 KorFinVDR 벤치마크의 시각문서 검색 및 복합문서 질의응답용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[문서 인식(OCR)]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# MarkrAI/korfinvdr-financial_report

> dataset · [Hugging Face](https://huggingface.co/datasets/MarkrAI/korfinvdr-financial_report)

한국은행 금융안정보고서로 구성된 KorFinVDR 벤치마크의 시각문서 검색 및 복합문서 질의응답용 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — metadata · task_categories = `document-question-answering` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Korean visual document retrieval and complex-document question answering` · 신뢰도 medium
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `visual-document-retrieval` · 신뢰도 high
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:retrieval = `Text extracted from the page using the document-processing pipeline` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:question_answering = `The answer grounded in the source documents` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `8198` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `Bank of Korea financial stability reports` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset, financial_report, is a corpus of Bank of Korea financial stability reports` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `elements` 열 p90 12296자 ≈ 8198 토큰 (viewer statistics, corpus/test)
