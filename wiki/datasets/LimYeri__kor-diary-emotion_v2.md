---
type: "dataset"
id: "LimYeri/kor-diary-emotion_v2"
source: "huggingface"
url: "https://huggingface.co/datasets/LimYeri/kor-diary-emotion_v2"
downloads: 58
summary: "한국어 일기 형식 감정 분류 데이터셋으로 8가지 감정과 상황 정보를 포함합니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# LimYeri/kor-diary-emotion_v2

> dataset · [Hugging Face](https://huggingface.co/datasets/LimYeri/kor-diary-emotion_v2)

한국어 일기 형식 감정 분류 데이터셋으로 8가지 감정과 상황 정보를 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 high
- **작업**: [[텍스트 생성]] — ner · readme = `OpenAI API를 활용해 생성된 일기(Diary) 형식의 자연스럽고 일상적인 문장들로 구성되어 있습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `1~4문장 내외의 자연스러운 한국어 일기` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `8가지 대표 감정 중 하나` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `107` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 감정 분류를 위해 제작된 텍스트 데이터셋` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 161자 ≈ 107 토큰 (viewer statistics, default/train)
