---
type: "dataset"
id: "jbaudanza/korean-handwriting-strokes"
source: "huggingface"
url: "https://huggingface.co/datasets/jbaudanza/korean-handwriting-strokes"
downloads: 121
summary: "Neo Smartpen으로 수집한 한글 필기 획 데이터로, hangul.ink 손글씨 생성 모델 학습용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
  - "[[시계열 (출력 형식)|시계열]]"
language:
  - "[[한국어]]"
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
  - "[[소규모 데이터]]"
---
# jbaudanza/korean-handwriting-strokes

> dataset · [Hugging Face](https://huggingface.co/datasets/jbaudanza/korean-handwriting-strokes)

Neo Smartpen으로 수집한 한글 필기 획 데이터로, hangul.ink 손글씨 생성 모델 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `a browser-side recurrent network that writes Hangul by hand` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `training data behind hangul.ink, a browser-side recurrent network that writes Hangul by hand` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:language_modeling = `text` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — ner · readme = `x/y position, pen-tip force, timing, and pen tilt for every sample, grouped into strokes` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:language_modeling = `text` · 신뢰도 medium
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — ner · readme = `x/y position, pen-tip force, timing, and pen tilt for every sample, grouped into strokes` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean handwriting captured as pen strokes` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the training data behind hangul.ink` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `sentence_text` 열 p90 58자 ≈ 38 토큰 (viewer statistics, default/train)
