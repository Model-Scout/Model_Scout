---
type: "dataset"
id: "kenantang/IdiomTranslate30"
source: "huggingface"
url: "https://huggingface.co/datasets/kenantang/IdiomTranslate30"
downloads: 68
summary: "동아시아 관용구의 창의적이고 문맥 인지 번역을 위한 30개 언어쌍 병렬 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
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
# kenantang/IdiomTranslate30

> dataset · [Hugging Face](https://huggingface.co/datasets/kenantang/IdiomTranslate30)

동아시아 관용구의 창의적이고 문맥 인지 번역을 위한 30개 언어쌍 병렬 번역 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `Each row in the dataset contains the source context and three distinct translation variants` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `It contains a total of 2,719,800 context-aware translations across 30 language pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `269` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `massively multilingual dataset focusing on the creative and context-aware translation of East Asian idioms.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset was created using Pareto-optimal translation strategies for idioms` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `translate_analogy` 열 p90 1078자 ≈ 269 토큰 (viewer statistics, default/train)
