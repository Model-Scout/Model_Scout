---
type: "dataset"
id: "Qrzysztof/functiongemma-prepaid-cards-tool-calling"
source: "huggingface"
url: "https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling"
downloads: 43
summary: "FunctionGemma Prepaid-Cards Tool-Calling 데이터셋은 선불카드 구매, 잔액 조회, 거래 내역 확인용 도구 호출 인텐트 인식을 위한 합성 학습 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
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
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Qrzysztof/functiongemma-prepaid-cards-tool-calling

> dataset · [Hugging Face](https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling)

FunctionGemma Prepaid-Cards Tool-Calling 데이터셋은 선불카드 구매, 잔액 조회, 거래 내역 확인용 도구 호출 인텐트 인식을 위한 합성 학습 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `emit the correct tool call.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `85 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `125` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Buy a Digital Prepaid Visa or Virtual Prepaid Mastercard` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Synthetic training data for fine-tuning google/functiongemma-270m-it` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 500자 ≈ 125 토큰 (viewer statistics, default/train)
