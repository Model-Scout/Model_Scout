---
type: "dataset"
id: "synquid/wmt24pp"
source: "huggingface"
url: "https://huggingface.co/datasets/synquid/wmt24pp"
downloads: 526
summary: "WMT24++는 55개 언어 쌍의 영어-다국어 번역 및 후편집 데이터를 제공하는 기계번역 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# synquid/wmt24pp

> dataset · [Hugging Face](https://huggingface.co/datasets/synquid/wmt24pp)

WMT24++는 55개 언어 쌍의 영어-다국어 번역 및 후편집 데이터를 제공하는 기계번역 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `MT/LLM system outputs and automatic metric scores` · 신뢰도 medium
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:translation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `112` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language pairs released in the publication WMT24++: Expanding the Language Coverage of WMT24 to 55 Languages & Dialects` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `segments marked as true were removed from the evaluation, and we recommend doing the same` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `source` 열 p90 447자 ≈ 112 토큰 (viewer statistics, en-ko_KR/train)
