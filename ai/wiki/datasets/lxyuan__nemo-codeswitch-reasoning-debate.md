---
type: "dataset"
id: "lxyuan/nemo-codeswitch-reasoning-debate"
source: "huggingface"
url: "https://huggingface.co/datasets/lxyuan/nemo-codeswitch-reasoning-debate"
downloads: 29
summary: "다국어 코드스위칭 데이터로 다국어 생성, 추론, 토론 스타일 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[ms]]"
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
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
# lxyuan/nemo-codeswitch-reasoning-debate

> dataset · [Hugging Face](https://huggingface.co/datasets/lxyuan/nemo-codeswitch-reasoning-debate)

다국어 코드스위칭 데이터로 다국어 생성, 추론, 토론 스타일 연구용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[ms]] — metadata · languages = `ms` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `9 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `528` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is a synthetic, multilingual code-switching dataset.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains a single `train` split in `data/train.parquet` (~1.32GB).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 2111자 ≈ 528 토큰 (viewer statistics, default/train)
