---
type: "dataset"
id: "xujfcn/Crazyrouter-Multimodal-Pricing"
source: "huggingface"
url: "https://huggingface.co/datasets/xujfcn/Crazyrouter-Multimodal-Pricing"
downloads: 243
summary: "이미지, 영상, 음성, 음악, 3D 모델 API의 2026년 10월 11일 기준 요금 정보를 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ru]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# xujfcn/Crazyrouter-Multimodal-Pricing

> dataset · [Hugging Face](https://huggingface.co/datasets/xujfcn/Crazyrouter-Multimodal-Pricing)

이미지, 영상, 음성, 음악, 3D 모델 API의 2026년 10월 11일 기준 요금 정보를 제공하는 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — tag_match · tags = `image-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Live default-group pricing for image, video, audio, music, and 3D model APIs on 2026-10-11.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:image_generation, task:retrieval = `The dataset keeps the provider's original billing unit: per image, per second, per request, or per 1M output tokens.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `The dataset keeps the provider's original billing unit: per image, per second, per request, or per 1M output tokens.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Live default-group pricing for image, video, audio, music, and 3D model APIs on 2026-10-11.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `billing_key` 열 p90 44자 ≈ 11 토큰 (viewer statistics, default/train)
