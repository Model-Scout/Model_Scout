---
type: "dataset"
id: "jaeyong2/Qwen3-14B-Ko-self-verify"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/Qwen3-14B-Ko-self-verify"
downloads: 16
summary: "Qwen3-14B-Ko-self-verify 데이터셋은 함수 생성 및 실행 결과 검증용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/Qwen3-14B-Ko-self-verify

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/Qwen3-14B-Ko-self-verify)

Qwen3-14B-Ko-self-verify 데이터셋은 함수 생성 및 실행 결과 검증용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Whether the generated function is parsed` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Whether the generated function is parsed` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Whether the result of the executed function and the result predicted by LLM are the same` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `134` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 201자 ≈ 134 토큰 (viewer statistics, default/train)
