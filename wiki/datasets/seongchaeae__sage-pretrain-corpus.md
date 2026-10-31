---
type: "dataset"
id: "seongchaeae/sage-pretrain-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/seongchaeae/sage-pretrain-corpus"
downloads: 1913
summary: "상업적 사용 가능 라이선스 기반 한국어·영어 사전학습용 코퍼스, Sage 한국어 LLM 프로젝트용"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# seongchaeae/sage-pretrain-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/seongchaeae/sage-pretrain-corpus)

상업적 사용 가능 라이선스 기반 한국어·영어 사전학습용 코퍼스, Sage 한국어 LLM 프로젝트용

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `License-audited Korean/English pretraining corpus for the Sage Korean LLM project.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `Records: id, text, source, license, meta (JSON of original fields).` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Records: id, text, source, license, meta (JSON of original fields).` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `61431` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean/English pretraining corpus for the Sage Korean LLM project.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `License-audited Korean/English pretraining corpus for the Sage Korean LLM project.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 92147자 ≈ 61431 토큰 (viewer statistics, default/train)
