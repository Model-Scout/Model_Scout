---
type: "dataset"
id: "nvidia/OpenCodeInstruct"
source: "huggingface"
url: "https://huggingface.co/datasets/nvidia/OpenCodeInstruct"
downloads: 43690
summary: "OpenCodeInstruct는 코드 생성 특화 LLM 학습용 500만 샘플 규모의 명령어 튜닝 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# nvidia/OpenCodeInstruct

> dataset · [Hugging Face](https://huggingface.co/datasets/nvidia/OpenCodeInstruct)

OpenCodeInstruct는 코드 생성 특화 LLM 학습용 500만 샘플 규모의 명령어 튜닝 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `|input|string|The input coding question.|` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `|output|string|LLM's response.|` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `424` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `OpenCodeInstruct is designed for supervised fine-tuning (SFT).` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1695자 ≈ 424 토큰 (viewer statistics, train/train)
