---
type: "dataset"
id: "auftragstaktik-ou/multilingual-academic-pdf-ocr-guide"
source: "huggingface"
url: "https://huggingface.co/datasets/auftragstaktik-ou/multilingual-academic-pdf-ocr-guide"
downloads: 17
summary: "다국어 학술 PDF, 스캔 아카이브, 특허 문서의 OCR 및 AI 번역 벤치마크 및 가이드 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[문서 인식(OCR)]]"
  - "[[번역]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
---
# auftragstaktik-ou/multilingual-academic-pdf-ocr-guide

> dataset · [Hugging Face](https://huggingface.co/datasets/auftragstaktik-ou/multilingual-academic-pdf-ocr-guide)

다국어 학술 PDF, 스캔 아카이브, 특허 문서의 OCR 및 AI 번역 벤치마크 및 가이드 데이터셋입니다.

## 분류

- **작업**: [[문서 인식(OCR)]] — tag_match · readme, tags = `ocr` · 신뢰도 medium
- **작업**: [[번역]] — ner · readme = `Patent AI Translation Benchmark & Guide` · 신뢰도 medium
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme, task:ocr = `Multilingual Academic PDF, Scanned Archive & Patent` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:ocr = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:translation = `side-by-side bilingual PDF and target-language PDF outputs` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Multilingual Academic PDF, Scanned Archive & Patent AI Translation Benchmark & Guide` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `AI Translation Benchmark & Guide` · 신뢰도 low

## 같은 데이터의 사본·중복 등록

- `geyi-net/academic-pdf-translation-zotero-guide`
