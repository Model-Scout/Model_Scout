---
type: "dataset"
id: "opencompass/mmmlu_lite"
source: "huggingface"
url: "https://huggingface.co/datasets/opencompass/mmmlu_lite"
downloads: 294
summary: "MMMLU 데이터셋의 경량 버전으로, 다국어 AI 모델 평가용 1만 9950개 문항 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# opencompass/mmmlu_lite

> dataset · [Hugging Face](https://huggingface.co/datasets/opencompass/mmmlu_lite)

MMMLU 데이터셋의 경량 버전으로, 다국어 AI 모델 평가용 1만 9950개 문항 포함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `MMLU is a widely recognized benchmark of general knowledge attained by AI models.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `We translated the MMLU’s test set into 14 languages using professional human translators.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `We translated the MMLU’s test set into 14 languages using professional human translators.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `14 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `60` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `It covers a broad range of topics from 57 different categories, covering elementary-level knowledge up to advanced professional subjects like law, physics, hist` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `We are publishing the professional human translations and the code we use to run the evaluations.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 240자 ≈ 60 토큰 (viewer statistics, KO_KR/test)
