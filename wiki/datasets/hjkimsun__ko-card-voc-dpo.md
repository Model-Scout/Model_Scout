---
type: "dataset"
id: "hjkimsun/ko-card-voc-dpo"
source: "huggingface"
url: "https://huggingface.co/datasets/hjkimsun/ko-card-voc-dpo"
downloads: 12
summary: "카드 콜센터 대화 데이터를 기반으로 고객 만족도 평가용 DPO 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hjkimsun/ko-card-voc-dpo

> dataset · [Hugging Face](https://huggingface.co/datasets/hjkimsun/ko-card-voc-dpo)

카드 콜센터 대화 데이터를 기반으로 고객 만족도 평가용 DPO 학습 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The dataset is designed to evaluate customer satisfaction levels ("만족", "미흡", "해결 불가", "추가 상담 필요") based on dialogue interactions.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1253` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `This dataset is derived from call center data provided by Card` · 신뢰도 low
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It contains 28,797 training samples and 3,888 validation samples, totaling 32,685 instances.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 1880자 ≈ 1253 토큰 (viewer statistics, default/validation)
