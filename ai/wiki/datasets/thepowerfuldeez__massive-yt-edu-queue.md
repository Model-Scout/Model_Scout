---
type: "dataset"
id: "thepowerfuldeez/massive-yt-edu-queue"
source: "huggingface"
url: "https://huggingface.co/datasets/thepowerfuldeez/massive-yt-edu-queue"
downloads: 147
summary: "약 450만 개 유튜브 교육 영상의 메타데이터와 분류, 라이선스 위험 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
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
  - "[[교육]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# thepowerfuldeez/massive-yt-edu-queue

> dataset · [Hugging Face](https://huggingface.co/datasets/thepowerfuldeez/massive-yt-edu-queue)

약 450만 개 유튜브 교육 영상의 메타데이터와 분류, 라이선스 위험 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Each video has been classified by content type and assessed for license risk using a 3-tier automated classification system.` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `It serves as the discovery and processing queue for the massive-yt-edu-transcriptions project` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:retrieval = `This dataset contains metadata, content categorization, and license risk assessment for ~4.5M YouTube videos` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:speech_recognition = `Full metadata and content classification for 4,489,228 YouTube educational videos` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `11 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `24` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[교육]] — tag_match · readme, tags = `education` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `It serves as the discovery and processing queue for the massive-yt-edu-transcriptions project` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `title` 열 p90 96자 ≈ 24 토큰 (viewer statistics, default/train)
