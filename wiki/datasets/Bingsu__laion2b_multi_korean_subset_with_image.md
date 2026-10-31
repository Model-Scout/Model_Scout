---
type: "dataset"
id: "Bingsu/laion2b_multi_korean_subset_with_image"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/laion2b_multi_korean_subset_with_image"
downloads: 164
summary: "img2dataset으로 다운로드한 9,800,137장 한국어 이미지-텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
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
dataset_size:
  - "[[중규모 데이터]]"
---
# Bingsu/laion2b_multi_korean_subset_with_image

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/laion2b_multi_korean_subset_with_image)

img2dataset으로 다운로드한 9,800,137장 한국어 이미지-텍스트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — metadata · readme, task_categories = `feature-extraction` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `img2dataset을 통해 다운로드에 성공한 Bingsu/laion2B-multi-korean-subset 이미지를 정리한 데이터셋입니다.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme = `이미지는 9,800,137장입니다.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:retrieval = `txt파일은 json파일의 "caption"을 담고 있습니다.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `이미지는 9,800,137장입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `txt파일은 json파일의 "caption"을 담고 있습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `124` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `laion2b_multi_korean_subset_with_image` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `img2dataset을 통해 다운로드에 성공한 Bingsu/laion2B-multi-korean-subset 이미지를 정리한 데이터셋입니다.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 186자 ≈ 124 토큰 (viewer statistics, default/train)
