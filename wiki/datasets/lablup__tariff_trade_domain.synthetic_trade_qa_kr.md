---
type: "dataset"
id: "lablup/tariff_trade_domain.synthetic_trade_qa_kr"
source: "huggingface"
url: "https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_qa_kr"
downloads: 34
summary: "한국 무역 분야 지식 학습 및 평가용 한국어 무역 도메인 질의응답 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
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
  - "[[조건부 이용]]"
domain:
  - "[[상거래·상품]]"
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# lablup/tariff_trade_domain.synthetic_trade_qa_kr

> dataset · [Hugging Face](https://huggingface.co/datasets/lablup/tariff_trade_domain.synthetic_trade_qa_kr)

한국 무역 분야 지식 학습 및 평가용 한국어 무역 도메인 질의응답 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Multiple-choice QA` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `LLM-generated QA from lecture transcripts` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, tags, task_categories, task_ids = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `240` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Korean international trade` · 신뢰도 low
- **도메인**: [[교육]] — ner · readme = `Korean trade education content` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train | 21,399` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 360자 ≈ 240 토큰 (viewer statistics, default/train)
