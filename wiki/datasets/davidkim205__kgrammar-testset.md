---
type: "dataset"
id: "davidkim205/kgrammar-testset"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/kgrammar-testset"
downloads: 7
summary: "한국어 문장의 문법 오류 개수를 검출하는 kgrammar 모델 학습 및 검증용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# davidkim205/kgrammar-testset

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/kgrammar-testset)

한국어 문장의 문법 오류 개수를 검출하는 kgrammar 모델 학습 및 검증용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `which identifies grammatical errors in Korean text and outputs the number of detected errors` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `outputs the number of detected errors` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is structured to ensure a balanced distribution, consisting of 50% general questions, 25% math-related questions, 25% coding-related questions.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The kgrammar-testset is a dataset designed for training and validating the kgrammar model` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
