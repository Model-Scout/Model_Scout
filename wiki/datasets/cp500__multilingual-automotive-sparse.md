---
type: "dataset"
id: "cp500/multilingual-automotive-sparse"
source: "huggingface"
url: "https://huggingface.co/datasets/cp500/multilingual-automotive-sparse"
downloads: 86
summary: "자동차, 공급망, 지정학 분야 다국어 희소 검색 모델 미세조정용 합성 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# cp500/multilingual-automotive-sparse

> dataset · [Hugging Face](https://huggingface.co/datasets/cp500/multilingual-automotive-sparse)

자동차, 공급망, 지정학 분야 다국어 희소 검색 모델 미세조정용 합성 학습 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `sentence-similarity` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `Japanese query should retrieve the right English passage` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Japanese query should retrieve the right English passage` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `100` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `automotive, supply-chain` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A synthetic training corpus for fine-tuning multilingual sparse retrieval models` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `positive` 열 p90 402자 ≈ 100 토큰 (viewer statistics, default/test)
