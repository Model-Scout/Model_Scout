---
type: "dataset"
id: "AIDX-ktds/ko_leaderboard"
source: "huggingface"
url: "https://huggingface.co/datasets/AIDX-ktds/ko_leaderboard"
downloads: 26
readme_status: "thin"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# AIDX-ktds/ko_leaderboard

> dataset · [Hugging Face](https://huggingface.co/datasets/AIDX-ktds/ko_leaderboard)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `590` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — metadata · referenced_by_models = `train` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `prompt` 열 p90 885자 ≈ 590 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[tensorblock__AIDXteam_ktdsbaseLM-v0.15-onbased-llama3.1-GGUF|tensorblock/AIDXteam_ktdsbaseLM-v0.15-onbased-llama3.1-GGUF]]
- [[tensorblock__SEOKDONG_llama3.1_korean_v1.1_sft_by_aidx-GGUF|tensorblock/SEOKDONG_llama3.1_korean_v1.1_sft_by_aidx-GGUF]]
- [[tensorblock__llama3.1_korean_v0.1_sft_by_aidx-GGUF|tensorblock/llama3.1_korean_v0.1_sft_by_aidx-GGUF]]
