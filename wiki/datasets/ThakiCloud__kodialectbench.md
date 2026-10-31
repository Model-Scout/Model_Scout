---
type: "dataset"
id: "ThakiCloud/kodialectbench"
source: "huggingface"
url: "https://huggingface.co/datasets/ThakiCloud/kodialectbench"
downloads: 242
summary: "한국 5개 지역 방언 문장 1,000개로 방언 이해, 지역 식별, 방언 생성 평가하는 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ThakiCloud/kodialectbench

> dataset · [Hugging Face](https://huggingface.co/datasets/ThakiCloud/kodialectbench)

한국 5개 지역 방언 문장 1,000개로 방언 이해, 지역 식별, 방언 생성 평가하는 벤치마크 데이터셋입니다.

## 분류

- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `Items are transcribed text.` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `13` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A benchmark that measures Korean regional dialects…` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `A benchmark that measures Korean regional dialects… See the full description on the dataset page` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `digest` 열 p90 20자 ≈ 13 토큰 (viewer statistics, default/train)
