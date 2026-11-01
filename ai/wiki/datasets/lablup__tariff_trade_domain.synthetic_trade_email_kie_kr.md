---
type: "dataset"
id: "lablup/tariff_trade_domain.synthetic_trade_email_kie_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_email_kie_kr"
downloads: 36
summary: "B2B 공급망 이메일에서 계약 정보를 추출하는 한국어 합성 KIE 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lablup/tariff_trade_domain.synthetic_trade_email_kie_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_email_kie_kr)

B2B 공급망 이메일에서 계약 정보를 추출하는 한국어 합성 KIE 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · task_categories = `feature-extraction` · 신뢰도 low
- **작업**: [[정보 추출]] — tag_match · readme, tags = `information-extraction` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:information_extraction = `Full email conversation` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `structured YAML extraction of contract terms, parties, dates, and prices` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2167` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `B2B supply-chain email threads` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A synthetic instruction fine-tuning dataset` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 3250자 ≈ 2167 토큰 (viewer statistics, default/train)
