---
type: "dataset"
id: "jaeyong2/LAION-art-EN-improved-captions-translate"
source: "huggingface"
url: "https://huggingface.co/datasets/jaeyong2/LAION-art-EN-improved-captions-translate"
downloads: 24
summary: "LAION-art-EN-improved-captions 데이터셋을 번역한 이미지 캡션 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[hi]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[vi]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jaeyong2/LAION-art-EN-improved-captions-translate

> dataset · [Hugging Face](https://huggingface.co/datasets/jaeyong2/LAION-art-EN-improved-captions-translate)

LAION-art-EN-improved-captions 데이터셋을 번역한 이미지 캡션 데이터셋입니다.

## 분류

- **작업**: [[번역]] — ner · readme = `We used Qwen/Qwen2-72B-Instruct model to translate.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `We used Qwen/Qwen2-72B-Instruct model to translate.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `We used Qwen/Qwen2-72B-Instruct model to translate.` · 신뢰도 medium
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `187` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `source dataset from recastai/LAION-art-EN-improved-captions` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `orig_caption` 열 p90 748자 ≈ 187 토큰 (viewer statistics, default/train)
