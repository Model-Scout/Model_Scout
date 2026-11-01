---
type: "dataset"
id: "piyushsinghpasi/mscoco-multilingual-30k"
source: "huggingface"
url: "https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k"
downloads: 27
summary: "MSCOCO 2014 검증셋의 3만 이미지와 10개 언어 캡션으로 다국어 이미지-텍스트 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[임베딩]]"
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[el]]"
  - "[[영어]]"
  - "[[es]]"
  - "[[fa]]"
  - "[[fr]]"
  - "[[he]]"
  - "[[hi]]"
  - "[[id]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
commercial_use:
  - "[[비상업 전용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# piyushsinghpasi/mscoco-multilingual-30k

> dataset · [Hugging Face](https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k)

MSCOCO 2014 검증셋의 3만 이미지와 10개 언어 캡션으로 다국어 이미지-텍스트 평가용 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Multimodal representation learning research` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Cross-lingual caption alignment analysis` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-text-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:reranking, task:visual_qa = `captions in 10 languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `captions in 10 languages` · 신뢰도 medium
- **언어**: [[el]] — metadata · languages = `el` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fa]] — metadata · languages = `fa` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[he]] — metadata · languages = `he` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
