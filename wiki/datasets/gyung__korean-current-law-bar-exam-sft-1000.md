---
type: "dataset"
id: "gyung/korean-current-law-bar-exam-sft-1000"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/korean-current-law-bar-exam-sft-1000"
downloads: 35
summary: "대한민국 현행 법령 기반 변호사시험 선택형 스타일 SFT 1,000문항 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# gyung/korean-current-law-bar-exam-sft-1000

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/korean-current-law-bar-exam-sft-1000)

대한민국 현행 법령 기반 변호사시험 선택형 스타일 SFT 1,000문항 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `question_text: 문제와 5개 선택지` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `answer: 정답 번호, 1부터 5` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `694` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `sft/train.jsonl: messages 형식 SFT용 JSONL입니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `messages_json` 열 p90 1041자 ≈ 694 토큰 (viewer statistics, questions/train)
