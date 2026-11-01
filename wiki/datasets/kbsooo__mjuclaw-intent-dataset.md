---
type: "dataset"
id: "kbsooo/mjuclaw-intent-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/kbsooo/mjuclaw-intent-dataset"
downloads: 59
summary: "명지대학교 Discord 봇 mjuclaw용 한국어 학생 쿼리 15개 인텐트 분류 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kbsooo/mjuclaw-intent-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/kbsooo/mjuclaw-intent-dataset)

명지대학교 Discord 봇 mjuclaw용 한국어 학생 쿼리 15개 인텐트 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `학생이 Discord에서 입력했을 법한 한국어 쿼리` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `15개 클래스 중 하나` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `39` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `명지대학교 Discord 봇 mjuclaw용 한국어 의도 분류 데이터셋` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Split: stratified 85/15 (train 3,809 / val 665, SEED=42)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 59자 ≈ 39 토큰 (viewer statistics, default/validation)
