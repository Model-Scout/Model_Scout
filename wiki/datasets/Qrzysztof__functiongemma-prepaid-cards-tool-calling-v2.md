---
type: "dataset"
id: "Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2"
downloads: 52
summary: "FunctionGemma Prepaid-Cards Tool-Calling 데이터셋은 선불카드 구매, 잔액 조회, 거래 내역 확인용 도구 호출 인식 학습용 합성 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[도구 호출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[코드 (출력 형식)|코드]]"
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
# Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/Qrzysztof/functiongemma-prepaid-cards-tool-calling-v2)

FunctionGemma Prepaid-Cards Tool-Calling 데이터셋은 선불카드 구매, 잔액 조회, 거래 내역 확인용 도구 호출 인식 학습용 합성 데이터입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[도구 호출]] — tag_match · readme, tags = `function-calling` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `User messages are hand-translated in 84 languages` · 신뢰도 high
- **출력 형식**: [[코드 (출력 형식)|코드]] — ner · readme = `emit the correct tool call` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `85 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `127` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `buying prepaid cards, checking balances, and viewing transaction history` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Synthetic training data for fine-tuning google/functiongemma-270m-it` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 506자 ≈ 127 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[Qrzysztof__functiongemma-270m-it-prepaid-cards-v2|Qrzysztof/functiongemma-270m-it-prepaid-cards-v2]]
- [[Qrzysztof__functiongemma-270m-it-prepaid-cards-v2-mlx|Qrzysztof/functiongemma-270m-it-prepaid-cards-v2-mlx]]
