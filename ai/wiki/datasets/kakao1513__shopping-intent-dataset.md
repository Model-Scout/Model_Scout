---
type: "dataset"
id: "kakao1513/shopping-intent-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/kakao1513/shopping-intent-dataset"
downloads: 51
summary: "쇼핑몰 앱 제어를 위한 한국어 의도 분류 데이터셋으로 35개 클래스, 7,500문장 포함."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kakao1513/shopping-intent-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/kakao1513/shopping-intent-dataset)

쇼핑몰 앱 제어를 위한 한국어 의도 분류 데이터셋으로 35개 클래스, 7,500문장 포함.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, tags, task_categories = `text-classification` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `text: 사용자 발화 (입력)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `label: 의도 클래스 (정답)` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `23` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[상거래·상품]] — tag_match · readme, tags = `commerce` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `35개의 클래스로 구성되어 있으며, 총 7,500여 개의 문장이 포함되어 있습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 34자 ≈ 23 토큰 (viewer statistics, default/test)
