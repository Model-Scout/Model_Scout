---
type: "dataset"
id: "mncai/cosapien-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/mncai/cosapien-ko"
downloads: 60
summary: "microsoft/CoSApien을 한국어로 기계 번역하고 안전성 평가용 가드레일 판정 라벨을 붙인 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mncai/cosapien-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/mncai/cosapien-ko)

microsoft/CoSApien을 한국어로 기계 번역하고 안전성 평가용 가드레일 판정 라벨을 붙인 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `입력: `config_ko`(정책) + `prompt_ko`(요청)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `출력: `block` / `allow`` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `100` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-permissive-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `microsoft/CoSApien(Zhang et al., ICLR 2025)을 한국어로 기계 번역하고, 가드레일 입력 판정용 라벨을 붙인 평가셋입니다.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `prompt_en` 열 p90 150자 ≈ 100 토큰 (viewer statistics, default/test)
