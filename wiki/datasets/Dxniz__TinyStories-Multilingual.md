---
type: "dataset"
id: "Dxniz/TinyStories-Multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/Dxniz/TinyStories-Multilingual"
downloads: 172
summary: "어린이용 단편 소설 15,688편을 28개 언어로 수록한 다국어 문학 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Dxniz/TinyStories-Multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/Dxniz/TinyStories-Multilingual)

어린이용 단편 소설 15,688편을 28개 언어로 수록한 다국어 문학 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `is subsequently scored by a critic model for literary quality` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = `Each story is generated using a chain-of-thought planning process` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `29 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `880` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **도메인**: [[일반]] — ner · readme = `multilingual fluency in small models` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Excellent for teaching coherence to <1B parameter models` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 3519자 ≈ 880 토큰 (viewer statistics, default/train)
