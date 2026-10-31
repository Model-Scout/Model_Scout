---
type: "dataset"
id: "mlfoundations/dcvlm-baseline-6_25b"
source: "huggingface"
url: "https://huggingface.co/datasets/mlfoundations/dcvlm-baseline-6_25b"
downloads: 1479
summary: "DCVLM-Baseline은 DataComp-VLM 논문의 멀티모달 사전학습용 6.25B 토큰 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# mlfoundations/dcvlm-baseline-6_25b

> dataset · [Hugging Face](https://huggingface.co/datasets/mlfoundations/dcvlm-baseline-6_25b)

DCVLM-Baseline은 DataComp-VLM 논문의 멀티모달 사전학습용 6.25B 토큰 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Visual instruction / VQA / multi-turn chat` · 신뢰도 medium
- **작업**: [[언어 모델링]] — ner · readme = `It is a pre-mixed, decontaminated, ready-to-train multimodal pretraining dataset` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Visual instruction / VQA / multi-turn chat` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling, task:question_answering, task:visual_qa = `The conversation (see format below)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling, task:question_answering, task:visual_qa = `The conversation (see format below)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multimodal pretraining dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The training data is the WebDataset shards under shards/` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
