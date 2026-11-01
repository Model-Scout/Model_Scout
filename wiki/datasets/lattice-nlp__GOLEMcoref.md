---
type: "dataset"
id: "lattice-nlp/GOLEMcoref"
source: "huggingface"
url: "https://huggingface.co/datasets/lattice-nlp/GOLEMcoref"
downloads: 30
summary: "GOLEMcoref는 7개 언어의 소설 팬픽션 코어퍼런스 해소 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[id]]"
  - "[[it]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[nl]]"
  - "[[중국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lattice-nlp/GOLEMcoref

> dataset · [Hugging Face](https://huggingface.co/datasets/lattice-nlp/GOLEMcoref)

GOLEMcoref는 7개 언어의 소설 팬픽션 코어퍼런스 해소 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `benchmarking of coreference resolution systems` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `NER` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction = `text` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `7 languages` · 신뢰도 high
- **언어**: [[nl]] — metadata · languages = `nl` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `7061` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `gold standard benchmark for coreference resolution` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 28243자 ≈ 7061 토큰 (viewer statistics, default/test)
