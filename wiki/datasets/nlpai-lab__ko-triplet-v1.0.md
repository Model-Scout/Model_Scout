---
type: "dataset"
id: "nlpai-lab/ko-triplet-v1.0"
source: "huggingface"
url: "https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0"
downloads: 69
summary: "한국어 삼중항 데이터셋으로 문서 검색 및 임베딩 학습에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlpai-lab/ko-triplet-v1.0

> dataset · [Hugging Face](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0)

한국어 삼중항 데이터셋으로 문서 검색 및 임베딩 학습에 활용됨.

## 분류

- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality = `text` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `607` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `데이터 사전 캐시 방법을 적용하면 어떻게 11초에서 요청한 데이터를 핸드오버 구간이 지나고 난 다음인 14초에 타겟 드론을 통해 받을 수 있어?` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Train 744,862` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `hard_negative` 열 p90 911자 ≈ 607 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `whooray/ko-triplet-v1.0`

## 이 데이터로 학습한 모델

- [[fasoo__fasoo-embedding|fasoo/fasoo-embedding]]
- [[juyoungml__bge-m3-ko-v1.1|juyoungml/bge-m3-ko-v1.1]]
- [[nlpai-lab__KoE5|nlpai-lab/KoE5]]
