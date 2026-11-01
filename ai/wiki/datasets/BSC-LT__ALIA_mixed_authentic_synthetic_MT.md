---
type: "dataset"
id: "BSC-LT/ALIA_mixed_authentic_synthetic_MT"
source: "huggingface"
url: "https://huggingface.co/datasets/BSC-LT/ALIA_mixed_authentic_synthetic_MT"
downloads: 583
summary: "영어·스페인어와 아랍어, 힌디어, 중국어, 일본어, 한국어 간 기계번역 학습용 대규모 다국어 병렬 말뭉치입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# BSC-LT/ALIA_mixed_authentic_synthetic_MT

> dataset · [Hugging Face](https://huggingface.co/datasets/BSC-LT/ALIA_mixed_authentic_synthetic_MT)

영어·스페인어와 아랍어, 힌디어, 중국어, 일본어, 한국어 간 기계번역 학습용 대규모 다국어 병렬 말뭉치입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `sentence-level alignments for training Machine Translation systems` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:translation = `sentence-level alignments` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `parallel sentence pair` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `8353` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Large-scale multilingual parallel corpus covering English and Spanish paired with Arabic, Hindi, Chinese, Japanese, and Korean` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `training Machine Translation systems` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `l1_sentence` 열 p90 33414자 ≈ 8353 토큰 (viewer statistics, default/train)
