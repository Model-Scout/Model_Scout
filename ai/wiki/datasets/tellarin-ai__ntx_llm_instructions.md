---
type: "dataset"
id: "tellarin-ai/ntx_llm_instructions"
source: "huggingface"
url: "https://huggingface.co/datasets/tellarin-ai/ntx_llm_instructions"
downloads: 67
summary: "다국어 LLM 구축/튜닝을 위한 NTX v1 데이터셋의 Aya 포맷 변환본입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tellarin-ai/ntx_llm_instructions

> dataset · [Hugging Face](https://huggingface.co/datasets/tellarin-ai/ntx_llm_instructions)

다국어 LLM 구축/튜닝을 위한 NTX v1 데이터셋의 Aya 포맷 변환본입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `this version is intended for multi-lingual LLM construction/tuning` · 신뢰도 medium
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction = `It contains data in multiple languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `It contains data in multiple languages` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `303` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `this version is intended for multi-lingual LLM construction/tuning` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 1211자 ≈ 303 토큰 (viewer statistics, default/train)
