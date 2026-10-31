---
type: "dataset"
id: "Neurora/versta-glyphmatte"
source: "huggingface"
url: "https://huggingface.co/datasets/Neurora/versta-glyphmatte"
downloads: 160
summary: "Android 기기에서 문서 처리용으로 합성된 글리프 매트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ta]]"
  - "[[th]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Neurora/versta-glyphmatte

> dataset · [Hugging Face](https://huggingface.co/datasets/Neurora/versta-glyphmatte)

Android 기기에서 문서 처리용으로 합성된 글리프 매트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `this dataset enables training of compact glyph-matte U-Nets that decompose text line strips into ink coverage, stroke weight and per-pixel foreground/background` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `Columns: `rgb` (degraded input)` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = ``matte`, `weight`, `foreground`, `background` (clean labels), stored as PNG bytes` · 신뢰도 low
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ta]] — metadata · languages = `ta` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Synthetic Glyph Matte Dataset for On-Device Document Processing` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Half the data is drawn from 50,000 training strips, rounded out by a fixed 1,024-strip validation shard` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
