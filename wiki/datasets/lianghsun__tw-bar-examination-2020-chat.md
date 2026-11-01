---
type: "dataset"
id: "lianghsun/tw-bar-examination-2020-chat"
source: "huggingface"
url: "https://huggingface.co/datasets/lianghsun/tw-bar-examination-2020-chat"
downloads: 65
summary: "2020년 대만 변호사 시험 객관식 문제로 구성된 Alpaca 형식 미세조정 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# lianghsun/tw-bar-examination-2020-chat

> dataset · [Hugging Face](https://huggingface.co/datasets/lianghsun/tw-bar-examination-2020-chat)

2020년 대만 변호사 시험 객관식 문제로 구성된 Alpaca 형식 미세조정 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `適用於微調繁體中文語言模型於台灣法律選擇題作答任務` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `題目與四個選項` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `正確答案字母` · 신뢰도 medium
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `法律教育應用之原型開發` · 신뢰도 low
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `再以 benchmark 進行評測` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `作為 SFT 訓練素材設計` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 335자 ≈ 84 토큰 (viewer statistics, default/test)

## 이 데이터로 학습한 모델

- [[QuantFactory__Llama-3.2-Taiwan-3B-Instruct-GGUF|QuantFactory/Llama-3.2-Taiwan-3B-Instruct-GGUF]]
