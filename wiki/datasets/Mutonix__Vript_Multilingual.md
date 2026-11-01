---
type: "dataset"
id: "Mutonix/Vript_Multilingual"
source: "huggingface"
url: "https://huggingface.co/datasets/Mutonix/Vript_Multilingual"
downloads: 4520
summary: "다국어로 주석된 1만 9천 개 고해상도 UGC 영상과 67만 7천 클립의 세밀한 비디오-텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[이미지 생성]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Mutonix/Vript_Multilingual

> dataset · [Hugging Face](https://huggingface.co/datasets/Mutonix/Vript_Multilingual)

다국어로 주석된 1만 9천 개 고해상도 UGC 영상과 67만 7천 클립의 세밀한 비디오-텍스트 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `fine-grained video-text dataset with 19.1K annotated high-resolution UGC videos (~677k clips) in multiple languages` · 신뢰도 low
- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `fine-grained video-text dataset with 19.1K annotated high-resolution UGC videos (~677k clips) in multiple languages` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:image_generation, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:image_generation, task:retrieval, task:visual_qa = `The captions of the videos in the Vript_Multilingual dataset are structured as follows` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `high-resolution UGC videos (~677k clips)` · 신뢰도 medium
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `The captions of the videos in the Vript_Multilingual dataset are structured as follows` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `2233` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `fine-grained video-text dataset with 19.1K annotated high-resolution UGC videos (~677k clips) in multiple languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We construct another fine-grained video-text dataset with 19.1K annotated high-resolution UGC videos (~677k clips) in multiple languages to be the Vript_Multili` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `voiceover` 열 p90 8933자 ≈ 2233 토큰 (viewer statistics, bili/train)
