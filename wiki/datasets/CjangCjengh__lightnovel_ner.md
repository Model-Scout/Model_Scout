---
type: "dataset"
id: "CjangCjengh/lightnovel_ner"
source: "huggingface"
url: "https://huggingface.co/datasets/CjangCjengh/lightnovel_ner"
downloads: 50
summary: "일본어 경량소설과 공식 번역본에서 자동 추출한 다국어 명명 엔티티 인식(NER) 번역 쌍 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[th]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# CjangCjengh/lightnovel_ner

> dataset · [Hugging Face](https://huggingface.co/datasets/CjangCjengh/lightnovel_ner)

일본어 경량소설과 공식 번역본에서 자동 추출한 다국어 명명 엔티티 인식(NER) 번역 쌍 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `本数据集包含从日文轻小说及其官方翻译中自动提取的命名实体识别（NER）翻译对` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:information_extraction, task:translation = `将日文原文与对应语言的官方翻译对齐为平行句对` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `仅包含人名、地名、组织名、术语等短语级别的翻译对照信息` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `6` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `轻小说多语言NER翻译对数据集` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `本数据集包含从日文轻小说及其官方翻译中自动提取的命名实体识别（NER）翻译对` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `series` 열 p90 25자 ≈ 6 토큰 (viewer statistics, default/train)
