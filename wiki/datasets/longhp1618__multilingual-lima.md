---
type: "dataset"
id: "longhp1618/multilingual-lima"
source: "huggingface"
url: "https://huggingface.co/datasets/longhp1618/multilingual-lima"
downloads: 167
summary: "Multilingual LIMA 데이터셋으로 여러 언어별 Hugging Face config로 구성됨."
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
  - "[[ar]]"
  - "[[bn]]"
  - "[[영어]]"
  - "[[it]]"
  - "[[jv]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# longhp1618/multilingual-lima

> dataset · [Hugging Face](https://huggingface.co/datasets/longhp1618/multilingual-lima)

Multilingual LIMA 데이터셋으로 여러 언어별 Hugging Face config로 구성됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `translated by google/gemini-2.0-flash-001` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each language is stored as a separate Hugging Face config` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `translated by google/gemini-2.0-flash-001` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[jv]] — metadata · languages = `jv` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `831` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Each language is stored as a separate Hugging Face config` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 3322자 ≈ 831 토큰 (viewer statistics, ko/train)
