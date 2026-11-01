---
type: "dataset"
id: "Helsinki-NLP/OpenSubtitles2024"
source: "huggingface"
url: "https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024"
downloads: 132
summary: "OpenSubtitles2024 코퍼스에서 추출한 70개 언어의 영화·TV 자막 쌍으로 기계 번역 평가용 데이터셋입니다."
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
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# Helsinki-NLP/OpenSubtitles2024

> dataset · [Hugging Face](https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024)

OpenSubtitles2024 코퍼스에서 추출한 70개 언어의 영화·TV 자막 쌍으로 기계 번역 평가용 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `sentence-aligned subtitle pairs` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `sentence-aligned subtitle pairs` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `64 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `movie and TV subtitles` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high
