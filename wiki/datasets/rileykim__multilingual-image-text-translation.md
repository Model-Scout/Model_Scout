---
type: "dataset"
id: "rileykim/multilingual-image-text-translation"
source: "huggingface"
url: "https://huggingface.co/datasets/rileykim/multilingual-image-text-translation"
downloads: 46
summary: "11개 언어의 이미지-텍스트 번역 쌍으로 다국어 다중모달 번역 모델 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[이미지 생성]]"
  - "[[번역]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[이미지 (출력 형식)|이미지]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[kk]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[ur]]"
  - "[[uz]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# rileykim/multilingual-image-text-translation

> dataset · [Hugging Face](https://huggingface.co/datasets/rileykim/multilingual-image-text-translation)

11개 언어의 이미지-텍스트 번역 쌍으로 다국어 다중모달 번역 모델 학습용 데이터셋입니다.

## 분류

- **작업**: [[이미지 생성]] — metadata · task_categories = `text-to-image` · 신뢰도 low
- **작업**: [[번역]] — metadata · readme, tags, task_categories = `translation` · 신뢰도 high
- **작업**: [[이미지 인식]] — tag_match · tags = `vision` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:image_generation, task:vision, task:visual_qa = `image-text combinations across 11 languages` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:image_generation, task:translation, task:visual_qa = `image-text combinations across 11 languages` · 신뢰도 high
- **출력 형식**: [[이미지 (출력 형식)|이미지]] — task_rule · task:image_generation = `image` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation, task:visual_qa = `multimodal translation models that can translate text while considering visual context.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[kk]] — metadata · languages = `kk` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[ur]] — metadata · languages = `ur` · 신뢰도 high
- **언어**: [[uz]] — metadata · languages = `uz` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `52` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Multilingual Image-Text Translation Dataset (MMT)` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 208자 ≈ 52 토큰 (viewer statistics, default/test)
