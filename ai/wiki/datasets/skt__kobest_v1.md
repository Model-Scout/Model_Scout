---
type: "dataset"
id: "skt/kobest_v1"
source: "huggingface"
url: "https://huggingface.co/datasets/skt/kobest_v1"
downloads: 2697
summary: "KoBEST는 한국어 고급 지식을 요구하는 5가지 자연어 이해 과제로 구성된 한국어 벤치마크 데이터셋입니다."
readme_status: "template"
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
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# skt/kobest_v1

> dataset · [Hugging Face](https://huggingface.co/datasets/skt/kobest_v1)

KoBEST는 한국어 고급 지식을 요구하는 5가지 자연어 이해 과제로 구성된 한국어 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Choice of Plausible Alternatives` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Boolean Question Answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `natural language understanding tasks` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `natural language understanding tasks` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `187` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KoBEST is a Korean benchmark suite consists of 5 natural language understanding tasks` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `KoBEST is a Korean benchmark suite` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `paragraph` 열 p90 281자 ≈ 187 토큰 (viewer statistics, boolq/validation)

## 같은 데이터의 사본·중복 등록

- `youngwook-kim/kobest_v1`

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
