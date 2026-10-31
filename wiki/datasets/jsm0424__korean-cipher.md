---
type: "dataset"
id: "jsm0424/korean-cipher"
source: "huggingface"
url: "https://huggingface.co/datasets/jsm0424/korean-cipher"
downloads: 24
summary: "왜곡된 한국어 문장을 복원하는 LLM의 추론 능력 평가용 데이터셋입니다."
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# jsm0424/korean-cipher

> dataset · [Hugging Face](https://huggingface.co/datasets/jsm0424/korean-cipher)

왜곡된 한국어 문장을 복원하는 LLM의 추론 능력 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `It is designed to evaluate the reasoning abilities of large language models (LLMs) in understanding and reconstructing distorted Korean text.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It is designed to evaluate the reasoning abilities of large language models (LLMs) in understanding and reconstructing distorted Korean text.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `56` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It is designed to evaluate the reasoning abilities of large language models (LLMs) in understanding and reconstructing distorted Korean text.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `This dataset serves as a benchmark to test whether LLMs possess similar reasoning capabilities in processing and restoring corrupted Korean text.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `ciphertext` 열 p90 84자 ≈ 56 토큰 (viewer statistics, default/train)
