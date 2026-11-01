---
type: "dataset"
id: "base-model-evals/belebele-rephrased"
source: "huggingface"
url: "https://huggingface.co/datasets/base-model-evals/belebele-rephrased"
downloads: 27
summary: "Belebele 데이터셋의 질문형을 완성형으로 재작성하여 비지시형 언어모델 평가용으로 제공"
readme_status: "ok"
readme_language: "en"
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
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[tr]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# base-model-evals/belebele-rephrased

> dataset · [Hugging Face](https://huggingface.co/datasets/base-model-evals/belebele-rephrased)

Belebele 데이터셋의 질문형을 완성형으로 재작성하여 비지시형 언어모델 평가용으로 제공

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Belebele reading-comprehension items rewritten from question format into completion/cloze format` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `completion prefix (e.g. "The capital of Turkey is ...") that a base model can be scored on via loglikelihood over the candidate continuations` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[tr]] — metadata · languages = `tr` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `158` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Belebele reading-comprehension items rewritten from question format into completion/cloze format for base (non-instruction-tuned) language model evaluation.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `for base (non-instruction-tuned) language model evaluation.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `context` 열 p90 633자 ≈ 158 토큰 (viewer statistics, all/train)
