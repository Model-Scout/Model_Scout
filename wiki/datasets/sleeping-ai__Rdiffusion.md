---
type: "dataset"
id: "sleeping-ai/Rdiffusion"
source: "huggingface"
url: "https://huggingface.co/datasets/sleeping-ai/Rdiffusion"
downloads: 28
summary: "Riffusion 플랫폼에서 수집한 2,000개 이상의 인공 음악과 메타데이터를 포함한 텍스트-음악 생성 연구용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sleeping-ai/Rdiffusion

> dataset · [Hugging Face](https://huggingface.co/datasets/sleeping-ai/Rdiffusion)

Riffusion 플랫폼에서 수집한 2,000개 이상의 인공 음악과 메타데이터를 포함한 텍스트-음악 생성 연구용 데이터셋입니다.

## 분류

- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `training and evaluating text-to-music generative models` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `515` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `unlicense` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `publicly available songs from the Riffusion platform` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `lyrics` 열 p90 2061자 ≈ 515 토큰 (viewer statistics, default/train)
