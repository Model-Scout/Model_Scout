---
type: "dataset"
id: "chaannwooff/CC-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/chaannwooff/CC-korean"
downloads: 63
summary: "CommonCrawl WET 파일에서 추출한 한국어 웹 텍스트 코퍼스 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# chaannwooff/CC-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/chaannwooff/CC-korean)

CommonCrawl WET 파일에서 추출한 한국어 웹 텍스트 코퍼스 데이터셋입니다.

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `한국어 웹 텍스트 코퍼스. CommonCrawl WET 파일에서 추출한 한국어 문서 데이터셋입니다.` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:language_modeling = `CommonCrawl WET 파일 (HTML 제거된 텍스트 포맷)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `필터링 후 본문 텍스트` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `22681` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `web` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 연구 목적으로 제공되며, 상업적 이용 시 원본 저작권자의 허락이 필요합니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 34021자 ≈ 22681 토큰 (viewer statistics, default/train)
