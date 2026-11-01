---
type: "dataset"
id: "nlp-with-deeplearning/ko.SHP"
source: "huggingface"
url: "https://huggingface.co/datasets/nlp-with-deeplearning/ko.SHP"
downloads: 75
summary: "18개 주제 영역의 질문/지침에 대한 385K 집단 인간 선호도 데이터셋으로 RLHF 보상 모델 훈련에 사용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlp-with-deeplearning/ko.SHP

> dataset · [Hugging Face](https://huggingface.co/datasets/nlp-with-deeplearning/ko.SHP)

18개 주제 영역의 질문/지침에 대한 385K 집단 인간 선호도 데이터셋으로 RLHF 보상 모델 훈련에 사용됨.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `질문/지시 및 그 게시물에 대한 한 쌍의 최상위 코멘트를 갖는 레딧 게시물` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `선호도 레이블 -- A가 B보다 선호되는 경우 1이고, B가 A보다 선호되는 경우 0입니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1236` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `SHP는 요리에서 법률 조언에 이르기까지 18가지 다른 주제 영역의 질문/지침에 대한 응답에 대한 385K 집단 인간 선호도 데이터 세트이다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `각 하위 레딧에 대해 하나씩 18개의 디렉터리가 있으며 각 디렉터리에는 학습, 유효성 검사 및 테스트 데이터를 위한 JSONL 파일이 포함되어 있습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `en_history` 열 p90 1854자 ≈ 1236 토큰 (viewer statistics, default/validation)
