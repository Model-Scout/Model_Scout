---
type: "dataset"
id: "joonhyungbae/CulturePersona-Seoul"
source: "huggingface"
url: "https://huggingface.co/datasets/joonhyungbae/CulturePersona-Seoul"
downloads: 99
summary: "서울 시민 문화 참여 설문조사 기반 45,000개 합성 페르소나 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[문화·관광]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# joonhyungbae/CulturePersona-Seoul

> dataset · [Hugging Face](https://huggingface.co/datasets/joonhyungbae/CulturePersona-Seoul)

서울 시민 문화 참여 설문조사 기반 45,000개 합성 페르소나 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Each row has 24 quantitative anchors from aggregate tables only and 12 Korean narrative fields.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `12 Korean narrative fields` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `12 Korean narrative fields` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `159` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Seoul Citizens' Cultural Participation Survey` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `narr_wish_for_seoul` 열 p90 238자 ≈ 159 토큰 (viewer statistics, default/train)
