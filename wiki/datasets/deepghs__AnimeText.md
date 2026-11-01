---
type: "dataset"
id: "deepghs/AnimeText"
source: "huggingface"
url: "https://huggingface.co/datasets/deepghs/AnimeText"
downloads: 501
summary: "Anime 장면 내 다양한 스타일의 텍스트 검출을 위한 대규모 데이터셋으로 735K 이미지와 420만 텍스트 블록을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[정보 추출]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# deepghs/AnimeText

> dataset · [Hugging Face](https://huggingface.co/datasets/deepghs/AnimeText)

Anime 장면 내 다양한 스타일의 텍스트 검출을 위한 대규모 데이터셋으로 735K 이미지와 420만 텍스트 블록을 포함합니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `AnimeText is a large-scale dataset for anime scene text detection` · 신뢰도 low
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:vision = `Contains 735K high-resolution anime images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `4.2M annotated text blocks` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Provides multi-granularity text area annotations for more precise text detection` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Unlike existing natural scene or document-centric text detection datasets, AnimeText focuses on text in anime scenes` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `The dataset can be used to train and evaluate text detection models in anime scenes.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is divided into training, validation, and test sets` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
