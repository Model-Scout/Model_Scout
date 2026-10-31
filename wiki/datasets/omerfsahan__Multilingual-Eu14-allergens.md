---
type: "dataset"
id: "omerfsahan/Multilingual-Eu14-allergens"
source: "huggingface"
url: "https://huggingface.co/datasets/omerfsahan/Multilingual-Eu14-allergens"
downloads: 61
summary: "식당 메뉴 텍스트에서 14가지 EU 식품 알레르기 유발 물질을 예측하는 다국어 다중 라벨 분류 데이터셋입니다."
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# omerfsahan/Multilingual-Eu14-allergens

> dataset · [Hugging Face](https://huggingface.co/datasets/omerfsahan/Multilingual-Eu14-allergens)

식당 메뉴 텍스트에서 14가지 EU 식품 알레르기 유발 물질을 예측하는 다국어 다중 라벨 분류 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `menu item names and, where available, short menu descriptions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `List of EU-14 allergen labels associated with the item.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `48 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `22` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is intended for training and evaluating multilingual models that predict food allergens from restaurant menu text.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 88자 ≈ 22 토큰 (viewer statistics, default/train)
