---
type: "dataset"
id: "codeparrot/apps"
source: "huggingface"
url: "https://huggingface.co/datasets/codeparrot/apps"
downloads: 23291
summary: "APPS는 자연어 명세로부터 파이썬 코드 생성을 평가하는 1만 문제 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[code]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# codeparrot/apps

> dataset · [Hugging Face](https://huggingface.co/datasets/codeparrot/apps)

APPS는 자연어 명세로부터 파이썬 코드 생성을 평가하는 1만 문제 벤치마크입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[언어 모델링]] — metadata · task_ids = `language-modeling` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `Each sample consists of a programming problem formulation in English` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `some ground truth Python solutions` · 신뢰도 medium
- **언어**: [[code]] — metadata · languages = `code` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `programming problem formulation in English, some ground truth Python solutions` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset contains a train and test splits with 5000 samples each` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `You can load and iterate through the dataset with the following two lines of code for the train split` · 신뢰도 medium

## 이 데이터로 학습한 모델

- [[AneekC__quipu-moe-1B-A149M-chat-distill|AneekC/quipu-moe-1B-A149M-chat-distill]]
