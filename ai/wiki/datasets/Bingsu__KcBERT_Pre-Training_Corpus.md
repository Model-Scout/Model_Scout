---
type: "dataset"
id: "Bingsu/KcBERT_Pre-Training_Corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/Bingsu/KcBERT_Pre-Training_Corpus"
downloads: 320
summary: "한국 뉴스 댓글로 구성된 KcBERT 사전학습용 코퍼스 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Bingsu/KcBERT_Pre-Training_Corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/Bingsu/KcBERT_Pre-Training_Corpus)

한국 뉴스 댓글로 구성된 KcBERT 사전학습용 코퍼스 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories, task_ids = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `KcBERT Pre-Training Corpus (Korean News Comments)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `KcBERT is Korean Comments BERT pretrained on this Corpus set.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `84` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `KcBERT Pre-Training Corpus (Korean News Comments)` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `| # of texts | 86246285 |` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 127자 ≈ 84 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `kaggle/junbumlee/kcbert-pretraining-corpus-korean-news-comments`
