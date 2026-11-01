---
type: "dataset"
id: "nmixx-fin/twice_kr_finance_reranking"
source: "huggingface"
url: "https://huggingface.co/datasets/nmixx-fin/twice_kr_finance_reranking"
downloads: 41
summary: "한국 금융 텍스트 기반 쿼리-긍정-부정 문장 쌍으로 금융 문서 리랭킹에 활용하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[리랭킹]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[금융·경제]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nmixx-fin/twice_kr_finance_reranking

> dataset · [Hugging Face](https://huggingface.co/datasets/nmixx-fin/twice_kr_finance_reranking)

한국 금융 텍스트 기반 쿼리-긍정-부정 문장 쌍으로 금융 문서 리랭킹에 활용하는 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `FinanceFiQA-Reranking-ko

Utilizing the open dataset BCCard/BCCard-Finance-Kor-QnA, which consists of Korean financial text.
Along with the original (query, pos` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking = `which consists of Korean financial text.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Along with the original (query, positive) pair, the dataset provides one hard negative, retrieved through hard negative mining, and nine random negatives` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `43` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `query` 열 p90 64자 ≈ 43 토큰 (viewer statistics, default/test)
