---
type: "dataset"
id: "seongbo/kodialogbench"
source: "huggingface"
url: "https://huggingface.co/datasets/seongbo/kodialogbench"
downloads: 60
summary: "KoDialogBench는 한국어 대화 이해 및 응답 선택 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
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
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# seongbo/kodialogbench

> dataset · [Hugging Face](https://huggingface.co/datasets/seongbo/kodialogbench)

KoDialogBench는 한국어 대화 이해 및 응답 선택 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `dialogue topic and speaker's emotion which was already annotated in the original datasets to formulate dialogue-related multiple-choice questions` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `Response Selection | | K-SNS | 5 | 10295` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering, task:retrieval = `native Korean dialogues on daily topics` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `dialogue-related multiple-choice questions` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `native Korean dialogues on daily topics from public sources` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `This benchmark consists of 21 test sets` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
