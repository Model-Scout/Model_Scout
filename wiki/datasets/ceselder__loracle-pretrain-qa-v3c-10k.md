---
type: "dataset"
id: "ceselder/loracle-pretrain-qa-v3c-10k"
source: "huggingface"
url: "https://huggingface.co/datasets/ceselder/loracle-pretrain-qa-v3c-10k"
downloads: 22
summary: "LoRACLE 모델 학습용으로 3,000개 유기체의 9,753개 QA 데이터를 포함한 v3c 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
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
  - "[[이용 조건 미확인]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ceselder/loracle-pretrain-qa-v3c-10k

> dataset · [Hugging Face](https://huggingface.co/datasets/ceselder/loracle-pretrain-qa-v3c-10k)

LoRACLE 모델 학습용으로 3,000개 유기체의 9,753개 QA 데이터를 포함한 v3c 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Each organism gets 3-4 Q/A rows` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Each organism is a synthetic continued-pretrained model on 1-20 documents` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each organism gets 3-4 Q/A rows` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `21 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `147` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `Splits
- `train`: 8,783 rows / 2,700 orgs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 588자 ≈ 147 토큰 (viewer statistics, default/test)
