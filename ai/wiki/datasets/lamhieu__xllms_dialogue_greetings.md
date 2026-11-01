---
type: "dataset"
id: "lamhieu/xllms_dialogue_greetings"
source: "huggingface"
url: "https://huggingface.co/datasets/lamhieu/xllms_dialogue_greetings"
downloads: 65
summary: "16개 언어로 된 인사 및 간단한 대화 데이터셋으로, 대화형 어시스턴트 개발에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lamhieu/xllms_dialogue_greetings

> dataset · [Hugging Face](https://huggingface.co/datasets/lamhieu/xllms_dialogue_greetings)

16개 언어로 된 인사 및 간단한 대화 데이터셋으로, 대화형 어시스턴트 개발에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `building assistants that recognize salutations, respond politely, elicit intent, and pivot from chit-chat to helpful task support` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `ask one clear, low-friction follow-up question` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `Each sample is a short, natural exchange that begins with a greeting and evolves into a light informational micro-task.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `8` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multilingual greeting & small-talk dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `train | 41,320` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `hash` 열 p90 32자 ≈ 8 토큰 (viewer statistics, default/train)
