---
type: "dataset"
id: "JosephLee/tiny-ko-stories-sft"
source: "huggingface"
url: "https://huggingface.co/datasets/JosephLee/tiny-ko-stories-sft"
downloads: 68
summary: "『모두의 LLM with 파이썬』 실습용 어린이 이야기 생성 지시 미세조정 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# JosephLee/tiny-ko-stories-sft

> dataset · [Hugging Face](https://huggingface.co/datasets/JosephLee/tiny-ko-stories-sft)

『모두의 LLM with 파이썬』 실습용 어린이 이야기 생성 지시 미세조정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `request 이야기를 요청하는 짧은 문장` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `story 요청에 해당하는 어린이 이야기` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `225` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train 43,852쌍 / validation 2,308쌍` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `story` 열 p90 337자 ≈ 225 토큰 (viewer statistics, default/validation)
