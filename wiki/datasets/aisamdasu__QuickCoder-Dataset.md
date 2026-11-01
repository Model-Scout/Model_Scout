---
type: "dataset"
id: "aisamdasu/QuickCoder-Dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/aisamdasu/QuickCoder-Dataset"
downloads: 69
summary: "코드 완성과 중간 채우기 학습용 JSONL 형식 대규모 코드 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# aisamdasu/QuickCoder-Dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/aisamdasu/QuickCoder-Dataset)

코드 완성과 중간 채우기 학습용 JSONL 형식 대규모 코드 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `code completion and fill-in-the-middle training` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each line is one UTF-8 JSON object. The main training payload is `text`.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The main training payload is `text`.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `8846` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `training checkpoints for code completion and fill-in-the-middle training` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 13269자 ≈ 8846 토큰 (viewer statistics, default/train)
