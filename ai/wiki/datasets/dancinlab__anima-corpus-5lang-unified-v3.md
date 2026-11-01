---
type: "dataset"
id: "dancinlab/anima-corpus-5lang-unified-v3"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified-v3"
downloads: 38
summary: "5개 언어 위키피디아와 페르소나, 감정 등 다양한 텍스트로 구성된 대규모 언어 모델 학습용 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# dancinlab/anima-corpus-5lang-unified-v3

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-corpus-5lang-unified-v3)

5개 언어 위키피디아와 페르소나, 감정 등 다양한 텍스트로 구성된 대규모 언어 모델 학습용 코퍼스입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `It keeps the exact v2 3-surface recipe — real wiki backbone + persona/SNS roleplay + register enrichment` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `persona/SNS roleplay + register enrichment — but scales the clean wiki backbone ~20×` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `real wiki backbone + persona/SNS roleplay + register enrichment` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `real wiki backbone + persona/SNS roleplay + register enrichment` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `137` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `real wiki backbone + persona/SNS roleplay + register enrichment` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 549자 ≈ 137 토큰 (viewer statistics, default/train)
