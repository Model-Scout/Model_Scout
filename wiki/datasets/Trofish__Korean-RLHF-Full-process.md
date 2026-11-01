---
type: "dataset"
id: "Trofish/Korean-RLHF-Full-process"
source: "huggingface"
url: "https://huggingface.co/datasets/Trofish/Korean-RLHF-Full-process"
downloads: 77
summary: "KULLM 기반 RLHF 강화학습용 한국어 대화 및 일반 태스크 데이터셋입니다."
readme_status: "ok"
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
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# Trofish/Korean-RLHF-Full-process

> dataset · [Hugging Face](https://huggingface.co/datasets/Trofish/Korean-RLHF-Full-process)

KULLM 기반 RLHF 강화학습용 한국어 대화 및 일반 태스크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `일상 대화와 혐오 표현 대처 능력을 올리기 위한 데이터셋과, 학습 시 챗봇 모델의 general한 task에 대한 성능이 하락하는 것을 막기 위해서 general task 데이터셋을 구성` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `KULLM을 baseline으로 RLHF 강화학습을 하는데 사용한 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `일상 대화와 혐오 표현 대처 능력을 올리기 위한 데이터셋과, 학습 시 챗봇 모델의 general한 task에 대한 성능이 하락하는 것을 막기 위해서 general task 데이터셋을 구성` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Step1: step1_SFT_train.jsonl (KULLM 12.8B 모델을 Supervised Fine-Tuning 하는데 사용하였습니다.)` · 신뢰도 medium
