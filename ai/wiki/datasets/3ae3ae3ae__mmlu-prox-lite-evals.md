---
type: "dataset"
id: "3ae3ae3ae/mmlu-prox-lite-evals"
source: "huggingface"
url: "https://huggingface.co/datasets/3ae3ae3ae/mmlu-prox-lite-evals"
downloads: 1866
summary: "MMLU-ProX-Lite 데이터셋을 활용한 다국어 LLM 평가 결과 데이터로, 모델 내 언어 및 주제별 약점 진단용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[질의응답]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[de]]"
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
  - "[[sw]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 3ae3ae3ae/mmlu-prox-lite-evals

> dataset · [Hugging Face](https://huggingface.co/datasets/3ae3ae3ae/mmlu-prox-lite-evals)

MMLU-ProX-Lite 데이터셋을 활용한 다국어 LLM 평가 결과 데이터로, 모델 내 언어 및 주제별 약점 진단용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Raw outputs from evaluating recent LLMs on li-lab/MMLU-ProX-Lite` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `accuracy per language and subject` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:question_answering = `one row per question with the prompt` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `the raw response, the extracted answer (`filtered_resps`; `[invalid]` when no answer could be extracted), and the score (`exact_match`)` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Raw outputs from evaluating recent LLMs on li-lab/MMLU-ProX-Lite (revision e82aafb) with lm-evaluation-harness 0.4.13, in 10 languages (en, zh, ja, ko, pt, de, ` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Raw outputs from evaluating recent LLMs on li-lab/MMLU-ProX-Lite` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `doc_hash` 열 p90 64자 ≈ 16 토큰 (viewer statistics, claude-haiku-5-5/test)
