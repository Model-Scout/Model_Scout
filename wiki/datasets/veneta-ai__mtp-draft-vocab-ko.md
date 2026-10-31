---
type: "dataset"
id: "veneta-ai/mtp-draft-vocab-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/veneta-ai/mtp-draft-vocab-ko"
downloads: 260
summary: "한국어 위키백과 기반 MTP 추측 디코딩용 초안 어휘집 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
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
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# veneta-ai/mtp-draft-vocab-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/veneta-ai/mtp-draft-vocab-ko)

한국어 위키백과 기반 MTP 추측 디코딩용 초안 어휘집 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `the draft head's output projection is computed over a frequency-ranked subset of the vocabulary` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `Korean draft vocabularies for MTP speculative decoding` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:language_modeling = `built from Korean Wikipedia` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `the draft head's output projection is computed over a frequency-ranked subset of the vocabulary` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `4` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `built from Korean Wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Korean draft vocabularies for MTP speculative decoding, one file per tokenizer family` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 6자 ≈ 4 토큰 (viewer statistics, default/train)
