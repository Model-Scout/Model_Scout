---
type: "dataset"
id: "wmt/wmt25-mist-mulr"
source: "huggingface"
url: "https://huggingface.co/datasets/wmt/wmt25-mist-mulr"
downloads: 34
summary: "WMT2025 MIST 다국어 언어 추론 서브태스크 데이터로 15개 언어의 언어 추론 퍼즐 문제와 답변을 포함함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# wmt/wmt25-mist-mulr

> dataset · [Hugging Face](https://huggingface.co/datasets/wmt/wmt25-mist-mulr)

WMT2025 MIST 다국어 언어 추론 서브태스크 데이터로 15개 언어의 언어 추론 퍼즐 문제와 답변을 포함함.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `there are four classification tasks` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — ner · readme = `1 editing task` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `41 translation tasks` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = `prompts and answers for the WMT2025 MIST sub-task on linguistic reasoning` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = `prompts and answers for the WMT2025 MIST sub-task on linguistic reasoning` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1076` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `linguistic reasoning puzzles in 15 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `They may only be used for research purposes and evaluation, not training.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 4303자 ≈ 1076 토큰 (viewer statistics, default/test)

## 같은 데이터의 사본·중복 등록

- `jiaheqi/wmt25-mist-mulr`
