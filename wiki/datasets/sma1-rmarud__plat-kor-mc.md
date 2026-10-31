---
type: "dataset"
id: "sma1-rmarud/plat-kor-mc"
source: "huggingface"
url: "https://huggingface.co/datasets/sma1-rmarud/plat-kor-mc"
downloads: 48
summary: "한국 조세법 판례 100개를 적법/위법 2지선다형 문제로 구성한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sma1-rmarud/plat-kor-mc

> dataset · [Hugging Face](https://huggingface.co/datasets/sma1-rmarud/plat-kor-mc)

한국 조세법 판례 100개를 적법/위법 2지선다형 문제로 구성한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국 조세법 판례 100개를 적법/위법 2지선다형 문제로 구성한 데이터셋입니다.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · tags, task_categories = `multiple-choice` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering = `사건 개요 (당사자, 배경)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `과세 처분의 적법 여부 (True/False)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `735` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `한국 조세법 판례 100개를 적법/위법 2지선다형 문제로 구성한 데이터셋입니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `reasoning` 열 p90 1102자 ≈ 735 토큰 (viewer statistics, default/test)
