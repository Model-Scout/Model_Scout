---
type: "dataset"
id: "lablup/tariff_trade_domain.synthetic_trade_email_sum_tag_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_email_sum_tag_kr"
downloads: 28
summary: "한국어 B2B 공급망 이메일 대화를 요약하고 주제 태그를 부여하는 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[요약]]"
input_modality:
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
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lablup/tariff_trade_domain.synthetic_trade_email_sum_tag_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_email_sum_tag_kr)

한국어 B2B 공급망 이메일 대화를 요약하고 주제 태그를 부여하는 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[요약]] — metadata · readme, tags, task_categories = `summarization` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:summarization = `Raw email thread (email headers + body, Markdown formatted)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `Prose summary of the negotiation.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `4472` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `B2B supply-chain email conversations` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A synthetic instruction fine-tuning dataset of 1,188 B2B supply-chain email conversations` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `conversation` 열 p90 6708자 ≈ 4472 토큰 (viewer statistics, sum_tag/train)
