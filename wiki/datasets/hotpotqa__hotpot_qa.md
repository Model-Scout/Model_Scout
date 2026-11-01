---
type: "dataset"
id: "hotpotqa/hotpot_qa"
source: "huggingface"
url: "https://huggingface.co/datasets/hotpotqa/hotpot_qa"
downloads: 82259
summary: "HotpotQA는 위키피디아 기반 다중 문서 추론 질문-답변 데이터셋입니다."
readme_status: "template"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# hotpotqa/hotpot_qa

> dataset · [Hugging Face](https://huggingface.co/datasets/hotpotqa/hotpot_qa)

HotpotQA는 위키피디아 기반 다중 문서 추론 질문-답변 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `we provide sentence-level supporting facts required for reasoning` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:question_answering = `Wikipedia-based question-answer pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `question-answer pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `34` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Wikipedia-based question-answer pairs` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `HotpotQA is a new dataset with 113k Wikipedia-based question-answer pairs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 137자 ≈ 34 토큰 (viewer statistics, distractor/validation)

## 이 데이터로 학습한 모델

- [[blackmallangcow__nari-decision-4b|blackmallangcow/nari-decision-4b]]
