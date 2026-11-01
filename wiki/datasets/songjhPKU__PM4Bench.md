---
type: "dataset"
id: "songjhPKU/PM4Bench"
source: "huggingface"
url: "https://huggingface.co/datasets/songjhPKU/PM4Bench"
downloads: 3031
summary: "PM4Bench는 10개 언어로 엄격히 병렬된 대형 비전-언어 모델 평가용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[문서 인식(OCR)]]"
  - "[[리랭킹]]"
  - "[[문서 검색]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[cs]]"
  - "[[영어]]"
  - "[[hu]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[sr]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# songjhPKU/PM4Bench

> dataset · [Hugging Face](https://huggingface.co/datasets/songjhPKU/PM4Bench)

PM4Bench는 10개 언어로 엄격히 병렬된 대형 비전-언어 모델 평가용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `The paper Benchmarking and Boosting Multilingual Capabilities of LVLMs via OCR-Centric Reinforcement Learning introduces PM4Bench to separate language effects f` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `Its content is strictly parallel across ten languages` · 신뢰도 low
- **작업**: [[문서 인식(OCR)]] — tag_match · tags = `ocr` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `Comparing that setting with interleaved input identifies OCR as a key source of cross-lingual performance gaps` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Strictly parallel multilingual evaluation for Large Vision-Language Models` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — task_rule · task:ocr = `document` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:ocr, task:visual_qa = `Its vision setting renders textual inputs directly into images` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:embedding, task:reranking, task:retrieval, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:ocr, task:visual_qa = `Its content is strictly parallel across ten languages` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[cs]] — metadata · languages = `cs` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hu]] — metadata · languages = `hu` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[sr]] — metadata · languages = `sr` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `213` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Strictly parallel multilingual evaluation for Large Vision-Language Models` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `PM4Bench evaluation data spanning MDUR, MIQA, MSOCR, and MGUI` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `rendered_text` 열 p90 850자 ≈ 213 토큰 (viewer statistics, mdur/test)
