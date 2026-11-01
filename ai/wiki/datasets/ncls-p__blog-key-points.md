---
type: "dataset"
id: "ncls-p/blog-key-points"
source: "huggingface"
url: "https://huggingface.co/datasets/ncls-p/blog-key-points"
downloads: 26
summary: "AI가 추출한 기사 전문과 핵심 요약문으로 구성된 요약 학습용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 생성]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# ncls-p/blog-key-points

> dataset · [Hugging Face](https://huggingface.co/datasets/ncls-p/blog-key-points)

AI가 추출한 기사 전문과 핵심 요약문으로 구성된 요약 학습용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[요약]] — metadata · readme, tags, task_categories = `summarization` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:summarization = `Each entry consists of the full article text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `a concise bullet-point summary highlighting the most important information from the article.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `10529` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Articles were collected from various online sources.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The dataset is designed for training and evaluating models on extractive and abstractive summarization tasks.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `input` 열 p90 42114자 ≈ 10529 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[ncls-p__Qwen2.5-3B-blog-key-points|ncls-p/Qwen2.5-3B-blog-key-points]]
- [[ncls-p__Qwen2.5-7B-blog-key-points|ncls-p/Qwen2.5-7B-blog-key-points]]
