---
type: "dataset"
id: "Algocean/algocean-router"
source: "huggingface"
url: "https://huggingface.co/datasets/Algocean/algocean-router"
downloads: 22
summary: "질의와 보안 등급, 사용 가능한 모델 목록을 받아 적합한 모델을 선택하는 라우팅 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Algocean/algocean-router

> dataset · [Hugging Face](https://huggingface.co/datasets/Algocean/algocean-router)

질의와 보안 등급, 사용 가능한 모델 목록을 받아 적합한 모델을 선택하는 라우팅 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `형식: JSONL, messages 3턴` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · readme = `router.eval.jsonl 2,000` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `LoRA SFT 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `seed_axis` 열 p90 39자 ≈ 26 토큰 (viewer statistics, default/test)
