---
type: "dataset"
id: "snowman0919/qwen38-executor-train-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/snowman0919/qwen38-executor-train-v2"
downloads: 98
summary: "Qwen3.8 Executor Unified Training Dataset는 도구 사용 및 컴퓨터 작업을 위한 실행기 기록 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# snowman0919/qwen38-executor-train-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/snowman0919/qwen38-executor-train-v2)

Qwen3.8 Executor Unified Training Dataset는 도구 사용 및 컴퓨터 작업을 위한 실행기 기록 데이터셋입니다.

## 분류

- **작업**: [[도구 호출]] — tag_match · readme, tags = `tool-calling` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `Images and executable artifacts are self-contained bytes where included.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `messages uses role/content/tool-call structs. Dynamic tool arguments are validated JSON in arguments_json.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `messages uses role/content/tool-call structs.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `144` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `provenance` 열 p90 216자 ≈ 144 토큰 (viewer statistics, default/train)
