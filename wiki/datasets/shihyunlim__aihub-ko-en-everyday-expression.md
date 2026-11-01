---
type: "dataset"
id: "shihyunlim/aihub-ko-en-everyday-expression"
source: "huggingface"
url: "https://huggingface.co/datasets/shihyunlim/aihub-ko-en-everyday-expression"
downloads: 53
summary: "AI 허브의 한국어-영어 일상생활 및 구어체 병렬 번역 말뭉치 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
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
  - "[[대규모 데이터]]"
---
# shihyunlim/aihub-ko-en-everyday-expression

> dataset · [Hugging Face](https://huggingface.co/datasets/shihyunlim/aihub-ko-en-everyday-expression)

AI 허브의 한국어-영어 일상생활 및 구어체 병렬 번역 말뭉치 데이터셋입니다.

## 분류

- **작업**: [[번역]] — metadata · readme, task_categories = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:translation = `한국어, 영어 병렬 문장` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `한국어, 영어 병렬 문장` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `63` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `AI Hub Ko-En Dataset : A collection of everyday words` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `중복 데이터를 처리 완료하여 총 1690052개의 한국어, 영어 병렬 문장을 포함합니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `en` 열 p90 94자 ≈ 63 토큰 (viewer statistics, default/train)
