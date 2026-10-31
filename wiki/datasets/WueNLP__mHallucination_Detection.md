---
type: "dataset"
id: "WueNLP/mHallucination_Detection"
source: "huggingface"
url: "https://huggingface.co/datasets/WueNLP/mHallucination_Detection"
downloads: 122
summary: "다국어 환각 탐지용 mFAVA 데이터셋으로, LLM 환각 평가에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# WueNLP/mHallucination_Detection

> dataset · [Hugging Face](https://huggingface.co/datasets/WueNLP/mHallucination_Detection)

다국어 환각 탐지용 mFAVA 데이터셋으로, LLM 환각 평가에 사용됨.

## 분류

- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `The dataset can be used as a test set for evaluating hallucination detection task.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:information_extraction, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `26 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2320` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The dataset is a multilingual extension of FAVA.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset can be used as a test set for evaluating hallucination detection task.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `references` 열 p90 9280자 ≈ 2320 토큰 (viewer statistics, default/test)
