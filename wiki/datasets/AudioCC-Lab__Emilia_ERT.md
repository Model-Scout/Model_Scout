---
type: "dataset"
id: "AudioCC-Lab/Emilia_ERT"
source: "huggingface"
url: "https://huggingface.co/datasets/AudioCC-Lab/Emilia_ERT"
downloads: 219
summary: "Emilia ERT는 6개 언어의 9,310,186개 음성 구간과 메타데이터를 포함한 음성 품질 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# AudioCC-Lab/Emilia_ERT

> dataset · [Hugging Face](https://huggingface.co/datasets/AudioCC-Lab/Emilia_ERT)

Emilia ERT는 6개 언어의 9,310,186개 음성 구간과 메타데이터를 포함한 음성 품질 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `combining speech quality assessment (SQA) and sound event detection (SED)` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `9,310,186 speech segments totaling 26,133.85 hours in six languages, distributed as 666 audio TAR shards` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `a single 34-column metadata table, metrics.scp` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data originate from Emilia dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `No held-out evaluation split is provided. Define appropriate speaker/source-disjoint splits for experiments.` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
