---
type: "dataset"
id: "suneetha24/symile-m3"
source: "huggingface"
url: "https://huggingface.co/datasets/suneetha24/symile-m3"
downloads: 517
summary: "Symile-M3는 다국어 오디오, 이미지, 텍스트 샘플로 이미지 검색을 위한 다중 모달 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
  - "[[이미지 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
language:
  - "[[ar]]"
  - "[[el]]"
  - "[[영어]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[te]]"
  - "[[th]]"
  - "[[uk]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# suneetha24/symile-m3

> dataset · [Hugging Face](https://huggingface.co/datasets/suneetha24/symile-m3)

Symile-M3는 다국어 오디오, 이미지, 텍스트 샘플로 이미지 검색을 위한 다중 모달 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `zero-shot-classification` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `The dataset was designed to evaluate a model on the zero-shot retrieval task of finding an image of the appropriate class given the audio and text.` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · task_categories = `zero-shot-image-classification` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Symile-M3 is a multilingual dataset of (audio, image, text) samples.` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision = `Symile-M3 is a multilingual dataset of (audio, image, text) samples.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `Symile-M3 is a multilingual dataset of (audio, image, text) samples.` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — ner · readme = `The most probable image for a given query audio and text pair, selected from all possible candidate images in the test set, is that with the highest similarity ` · 신뢰도 medium
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[el]] — metadata · languages = `el` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[te]] — metadata · languages = `te` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[uk]] — metadata · languages = `uk` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `29` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Symile-M3 is a multilingual dataset of (audio, image, text) samples.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `500K validation samples, 500K test samples` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Large (`l`): 10M training samples, 500K validation samples, 500K test samples` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 114자 ≈ 29 토큰 (viewer statistics, symile-m3-10-l/test)
