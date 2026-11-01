---
type: "dataset"
id: "kuotient/orca-math-word-problems-193k-korean"
source: "huggingface"
url: "https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean"
downloads: 141
summary: "Orca-Math의 한국어 번역 수학 문제 데이터셋으로, 초등 수학 문제 해결에 활용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# kuotient/orca-math-word-problems-193k-korean

> dataset · [Hugging Face](https://huggingface.co/datasets/kuotient/orca-math-word-problems-193k-korean)

Orca-Math의 한국어 번역 수학 문제 데이터셋으로, 초등 수학 문제 해결에 활용됨.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Orca-Math: Unlocking the potential of SLMs in Grade School Math` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `번역 모델: Seagull-13b-translation` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `977` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `Orca-Math: Unlocking the potential of SLMs in Grade School Math` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `원본 데이터셋: https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer_en` 열 p90 1465자 ≈ 977 토큰 (viewer statistics, default/train)
