---
type: "dataset"
id: "werty1248/SFT-Reasoning-Ko-Translated"
source: "huggingface"
url: "https://huggingface.co/datasets/werty1248/SFT-Reasoning-Ko-Translated"
downloads: 27
summary: "한국어 질의를 영어 추론과 한국어 답변으로 번역한 Reasoning 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# werty1248/SFT-Reasoning-Ko-Translated

> dataset · [Hugging Face](https://huggingface.co/datasets/werty1248/SFT-Reasoning-Ko-Translated)

한국어 질의를 영어 추론과 한국어 답변으로 번역한 Reasoning 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `원문 추론과 번역된 추론을 nltk.sent_tokenize 를 사용하여 문장 단위로 자른 후BAAI/bge-m3로 임베딩하여 문장 단위 매칭` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `한국어 질의 -> 영어 추론+한국어 답변 데이터` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:generation = `한국어 질의 -> 영어 추론+한국어 답변 데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `영어 추론+한국어 답변 데이터` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6584` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Reasoning 번역` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 사전학습이 많이 된 모델(HyperClova, Kanana, etc...)은 어떨지 확인 중` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `reasoning_original` 열 p90 9875자 ≈ 6584 토큰 (viewer statistics, Natural_Reasoning_gpt_oss_120b_s1/train)
