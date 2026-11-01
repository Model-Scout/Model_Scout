---
type: "dataset"
id: "jaeyong2/persona-inst"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/persona-inst"
downloads: 37
summary: "proj-persona/PersonaHub에서 생성한 페르소나 쌍으로 질문 생성용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# jaeyong2/persona-inst

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/persona-inst)

proj-persona/PersonaHub에서 생성한 페르소나 쌍으로 질문 생성용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to generate Question.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `features: ['Level', 'English', 'Korean', 'Thai', 'Vietnamese', 'context']` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `We used Qwen/Qwen2-72B-Instruct model to generate Question.` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `61` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `>>> ds = load_dataset("jaeyong2/persona-inst", split="train")` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 242자 ≈ 61 토큰 (viewer statistics, default/train)
