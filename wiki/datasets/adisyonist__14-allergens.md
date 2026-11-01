---
type: "dataset"
id: "adisyonist/14-allergens"
source: "huggingface"
url: "https://huggingface.co/datasets/adisyonist/14-allergens"
downloads: 33
summary: "음식 및 메뉴 텍스트와 14가지 알레르기 유발 성분 라벨을 포함한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# adisyonist/14-allergens

> dataset · [Hugging Face](https://huggingface.co/datasets/adisyonist/14-allergens)

음식 및 메뉴 텍스트와 14가지 알레르기 유발 성분 라벨을 포함한 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Bu veri kümesi, yiyecek ve menü metinleriyle bunlara bağlı alerjen etiketlerini içerir.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `yiyecek ve menü metinleriyle` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `bunlara bağlı alerjen etiketlerini içerir.` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `41 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1233` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `Bu veri kümesi, yiyecek ve menü metinleriyle bunlara bağlı alerjen etiketlerini içerir.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Veriler; fikir vermek, prototip oluşturmayı ve veri/uygulama geliştirme görevlerini kolaylaştırmak amacıyla sunulmuştur.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 4932자 ≈ 1233 토큰 (viewer statistics, default/train)
