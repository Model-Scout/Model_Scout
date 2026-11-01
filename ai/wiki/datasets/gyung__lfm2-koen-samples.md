---
type: "dataset"
id: "gyung/lfm2-koen-samples"
source: "huggingface"
url: "https://huggingface.co/datasets/gyung/lfm2-koen-samples"
downloads: 8
summary: "LiquidAI LFM2-1.2B 모델의 한국어-영어 번역 파인튜닝용 학습 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
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
  - "[[소규모 데이터]]"
---
# gyung/lfm2-koen-samples

> dataset · [Hugging Face](https://huggingface.co/datasets/gyung/lfm2-koen-samples)

LiquidAI LFM2-1.2B 모델의 한국어-영어 번역 파인튜닝용 학습 데이터셋입니다.

## 분류

- **작업**: [[번역]] — tag_match · readme, tags = `translation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `LiquidAI LFM2-1.2B 모델의 한국어-영어 번역 파인튜닝을 위한 학습 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `LiquidAI LFM2-1.2B 모델의 한국어-영어 번역 파인튜닝을 위한 학습 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `36` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `LiquidAI LFM2-1.2B 모델의 한국어-영어 번역 파인튜닝을 위한 학습 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `SFT 학습 (Main)` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 54자 ≈ 36 토큰 (viewer statistics, grpo_sample_100/train)
