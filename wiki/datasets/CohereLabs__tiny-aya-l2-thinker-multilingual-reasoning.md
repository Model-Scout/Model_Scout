---
type: "dataset"
id: "CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning"
downloads: 1277
summary: "44개 언어로 된 추론 데이터로 Tiny Aya L2-Thinker 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/tiny-aya-l2-thinker-multilingual-reasoning)

44개 언어로 된 추론 데이터로 Tiny Aya L2-Thinker 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `Each example has the prompt, thinking, and answer in the same non-English language alongside the original texts in English.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Each example has the prompt, thinking, and answer in the same non-English language alongside the original texts in English.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2979` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Translated multilingual reasoning traces used to train Tiny Aya L2-Thinker.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Translated multilingual reasoning traces used to train Tiny Aya L2-Thinker.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `original_thinking` 열 p90 11917자 ≈ 2979 토큰 (viewer statistics, ko/test)
