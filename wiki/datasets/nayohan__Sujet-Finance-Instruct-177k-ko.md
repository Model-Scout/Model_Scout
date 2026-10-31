---
type: "dataset"
id: "nayohan/Sujet-Finance-Instruct-177k-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nayohan/Sujet-Finance-Instruct-177k-ko"
downloads: 33
summary: "sujet-ai/Sujet-Finance-Instruct-177k 데이터셋을 한국어로 번역한 금융 분야 명령어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
domain:
  - "[[금융·경제]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nayohan/Sujet-Finance-Instruct-177k-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nayohan/Sujet-Finance-Instruct-177k-ko)

sujet-ai/Sujet-Finance-Instruct-177k 데이터셋을 한국어로 번역한 금융 분야 명령어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Translated sujet-ai/Sujet-Finance-Instruct-177k` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Translated sujet-ai/Sujet-Finance-Instruct-177k` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2445` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 3667자 ≈ 2445 토큰 (viewer statistics, default/train)
