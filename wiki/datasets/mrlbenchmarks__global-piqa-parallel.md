---
type: "dataset"
id: "mrlbenchmarks/global-piqa-parallel"
source: "huggingface"
url: "https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel"
downloads: 2537
summary: "131개 언어로 번역 및 교정된 상식 추론 평가용 다국어 병렬 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# mrlbenchmarks/global-piqa-parallel

> dataset · [Hugging Face](https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel)

131개 언어로 번역 및 교정된 상식 추론 평가용 다국어 병렬 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Each example consists of a prompt (in this case, a question) and four candidate solutions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each example consists of a prompt (in this case, a question) and four candidate solutions, one correct and three incorrect.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `176 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `247` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Global PIQA is a participatory commonsense reasoning benchmark for over 100 languages` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `Global PIQA is intended for LLM evaluation only.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `supplement` 열 p90 990자 ≈ 247 토큰 (viewer statistics, kor_hang/test)
