---
type: "dataset"
id: "joonhyungbae/Persona-Arts-Korea"
source: "huggingface"
url: "https://huggingface.co/datasets/joonhyungbae/Persona-Arts-Korea"
downloads: 63
summary: "2024년 한국 예술인 실태조사를 기반으로 한 3만 개의 한국 문화예술 페르소나 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# joonhyungbae/Persona-Arts-Korea

> dataset · [Hugging Face](https://huggingface.co/datasets/joonhyungbae/Persona-Arts-Korea)

2024년 한국 예술인 실태조사를 기반으로 한 3만 개의 한국 문화예술 페르소나 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each persona carries 16 quantitative variables and 17 narrative fields in Korean.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each persona carries 16 quantitative variables and 17 narrative fields in Korean.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `115` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `30,000 synthetic Korean cultural arts personas grounded in the 2024 Survey of Korean Artists` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `- Controllable evaluation sets where downstream tasks condition on quantitative anchors with a known joint distribution` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `- Supervised fine-tuning of Korean language models for persona conditioning in the cultural arts domain` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `professional_persona` 열 p90 172자 ≈ 115 토큰 (viewer statistics, default/train)
