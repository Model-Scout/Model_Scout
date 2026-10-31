---
type: "dataset"
id: "tellang/yeji-horoscope-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/tellang/yeji-horoscope-ko"
downloads: 19
summary: "서양 점성술 기반 한국어 운세 데이터셋으로 운세 생성에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# tellang/yeji-horoscope-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/tellang/yeji-horoscope-ko)

서양 점성술 기반 한국어 운세 데이터셋으로 운세 생성에 활용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `한국어 (번역)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Alpaca (instruction/input/output)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `400` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `서양 점성술` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `샘플 수 21,953 (train)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `original_output` 열 p90 600자 ≈ 400 토큰 (viewer statistics, default/train)
