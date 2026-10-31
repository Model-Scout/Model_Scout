---
type: "dataset"
id: "innadark/GlotCC-V1"
source: "huggingface"
url: "https://huggingface.co/datasets/innadark/GlotCC-V1"
downloads: 314
summary: "GlotCC-V1은 CommonCrawl에서 추출한 1000개 이상의 언어 문서 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# innadark/GlotCC-V1

> dataset · [Hugging Face](https://huggingface.co/datasets/innadark/GlotCC-V1)

GlotCC-V1은 CommonCrawl에서 추출한 1000개 이상의 언어 문서 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `GlotCC-V1.0 is a document-level, general domain dataset derived from CommonCrawl, covering more than 1000 languages.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `GlotCC-V1.0 is a document-level, general domain dataset derived from CommonCrawl` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `GlotCC-V1.0 is a document-level, general domain dataset derived from CommonCrawl` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `1372 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10461` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `GlotCC-V1.0 is a document-level, general domain dataset derived from CommonCrawl` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `GlotCC-V1.0 is a document-level, general domain dataset derived from CommonCrawl` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 41843자 ≈ 10461 토큰 (viewer statistics, kor-Hang/train)
