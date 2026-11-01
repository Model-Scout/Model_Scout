---
type: "dataset"
id: "code-with-zeeshan/UTS-Datasets"
source: "huggingface"
url: "https://huggingface.co/datasets/code-with-zeeshan/UTS-Datasets"
downloads: 38
summary: "UTS-Datasets는 20개 언어 190개 방향 병렬 문장 데이터로 기계 번역 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# code-with-zeeshan/UTS-Datasets

> dataset · [Hugging Face](https://huggingface.co/datasets/code-with-zeeshan/UTS-Datasets)

UTS-Datasets는 20개 언어 190개 방향 병렬 문장 데이터로 기계 번역 학습용 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `~4M parallel sentences (all language pairs, sampled & augmented)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `~4M parallel sentences (all language pairs, sampled & augmented)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `20 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `83` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Processed parallel training and validation data for the Universal Translation System.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `~100K validation sentences (held out from training)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `~4M parallel sentences (all language pairs, sampled & augmented)` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 333자 ≈ 83 토큰 (viewer statistics, default/validation)
