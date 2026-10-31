---
type: "dataset"
id: "HelpingAI/Dhanishtha-2.0-SUPERTHINKER"
source: "huggingface"
url: "https://huggingface.co/datasets/HelpingAI/Dhanishtha-2.0-SUPERTHINKER"
downloads: 51
summary: "다국어 11.7K 샘플로 구성된 중간 사고 및 감정 인지 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[리랭킹]]"
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
  - "[[학술·논문]]"
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# HelpingAI/Dhanishtha-2.0-SUPERTHINKER

> dataset · [Hugging Face](https://huggingface.co/datasets/HelpingAI/Dhanishtha-2.0-SUPERTHINKER)

다국어 11.7K 샘플로 구성된 중간 사고 및 감정 인지 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Evaluating alignment under ethical and moral uncertainty` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[리랭킹]] — ner · readme = `Benchmarking multi-phase reasoning or internal monologue generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:reranking = `Instruction-Output format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Instruction-Output format` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `34 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1149` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `Evaluating alignment under ethical and moral uncertainty` · 신뢰도 low
- **도메인**: [[일반]] — ner · readme = `multilingual samples` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Evaluating alignment under ethical and moral uncertainty` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `ideal for supervised fine-tuning` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 4595자 ≈ 1149 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[bartowski__HelpingAI_Dhanishtha-2.0-preview-GGUF|bartowski/HelpingAI_Dhanishtha-2.0-preview-GGUF]]
- [[lmstudio-community__Dhanishtha-2.0-preview-GGUF|lmstudio-community/Dhanishtha-2.0-preview-GGUF]]
