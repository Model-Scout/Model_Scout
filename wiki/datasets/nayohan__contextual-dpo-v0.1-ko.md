---
type: "dataset"
id: "nayohan/contextual-dpo-v0.1-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/contextual-dpo-v0.1-ko"
downloads: 26
summary: "jondurbin/contextual-dpo-v0.1 데이터셋을 한국어로 번역한 데이터셋입니다."
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
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nayohan/contextual-dpo-v0.1-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/contextual-dpo-v0.1-ko)

jondurbin/contextual-dpo-v0.1 데이터셋을 한국어로 번역한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Translated jondurbin/contextual-dpo-v0.1 using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Translated jondurbin/contextual-dpo-v0.1 using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated jondurbin/contextual-dpo-v0.1 using nayohan/llama3-instrucTrans-enko-8b.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1424` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 2135자 ≈ 1424 토큰 (viewer statistics, default/train)
