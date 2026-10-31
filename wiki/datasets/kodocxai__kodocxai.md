---
type: "dataset"
id: "kodocxai/kodocxai"
source: "huggingface"
url: "https://huggingface.co/datasets/kodocxai/kodocxai"
downloads: 69
summary: "KoDocXAI 벤치마크의 한국어 행정 문서 핵심 정보 추출용 주석 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 인식(OCR)]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kodocxai/kodocxai

> dataset · [Hugging Face](https://huggingface.co/datasets/kodocxai/kodocxai)

KoDocXAI 벤치마크의 한국어 행정 문서 핵심 정보 추출용 주석 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `document-understanding` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `annotated with value spans for five KIE fields` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr = `annotated with value spans for five KIE fields` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `permit-and-authorization dispatch documents` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Annotation layer of the KoDocXAI benchmark: 300 Korean permit-and-authorization dispatch documents annotated` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
