---
type: "dataset"
id: "Davlan/sib200_14classes"
source: "huggingface"
url: "https://huggingface.co/datasets/Davlan/sib200_14classes"
downloads: 92
summary: "SIB-200은 205개 언어의 뉴스 문장 14개 주제 분류 데이터셋으로, 소수샷 평가에 적합합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Davlan/sib200_14classes

> dataset · [Hugging Face](https://huggingface.co/datasets/Davlan/sib200_14classes)

SIB-200은 205개 언어의 뉴스 문장 14개 주제 분류 데이터셋으로, 소수샷 평가에 적합합니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories, task_ids = `text-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `topic classification` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `197 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `The source of the data is from the news domain` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The train/validation/test sets are available for all the 205 languages.` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 104자 ≈ 26 토큰 (viewer statistics, kor_Hang/validation)
