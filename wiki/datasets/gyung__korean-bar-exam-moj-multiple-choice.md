---
type: "dataset"
id: "gyung/korean-bar-exam-moj-multiple-choice"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/korean-bar-exam-moj-multiple-choice"
downloads: 87
summary: "대한민국 법무부 변호사시험 선택형 기출문제와 정답 번호 데이터셋입니다."
readme_status: "ok"
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
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
---
# gyung/korean-bar-exam-moj-multiple-choice

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/korean-bar-exam-moj-multiple-choice)

대한민국 법무부 변호사시험 선택형 기출문제와 정답 번호 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `문제 원문과 선택지를 포함한 전체 텍스트` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `정답 번호만 학습시키고 싶으면 assistant 응답을 `row["answer"]`만 남겨도 됩니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `law` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `모델 평가에서는 `question_text`를 프롬프트로 넣고 모델이 낸 번호를 `answer`와 비교하면 됩니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `SFT에 가장 바로 쓰기 좋은 파일은 다음입니다.` · 신뢰도 medium
