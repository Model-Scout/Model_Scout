---
type: "dataset"
id: "ifmain/text-moderation-02-multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/ifmain/text-moderation-02-multilingual"
downloads: 32
summary: "17개 언어로 된 1.5M 텍스트 모더레이션 데이터셋으로 부정 및 중립 문장 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ifmain/text-moderation-02-multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/ifmain/text-moderation-02-multilingual)

17개 언어로 된 1.5M 텍스트 모더레이션 데이터셋으로 부정 및 중립 문장 포함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `normalized to a 50/50 ratio of negative and neutral entries` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `text-moderation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `normalized to a 50/50 ratio of negative and neutral entries` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `17 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `58` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `based on Kaggle.It represents a version of @ifmain/text-moderation-410K` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset contains 1.5M entries (91K * 17 languages)` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 232자 ≈ 58 토큰 (viewer statistics, default/train)
