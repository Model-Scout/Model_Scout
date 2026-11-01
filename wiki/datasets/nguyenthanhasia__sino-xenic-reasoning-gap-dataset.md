---
type: "dataset"
id: "nguyenthanhasia/sino-xenic-reasoning-gap-dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/nguyenthanhasia/sino-xenic-reasoning-gap-dataset"
downloads: 44
summary: "중국어, 일본어, 한국어, 베트남어의 한자어 현상 이해를 평가하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# nguyenthanhasia/sino-xenic-reasoning-gap-dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/nguyenthanhasia/sino-xenic-reasoning-gap-dataset)

중국어, 일본어, 한국어, 베트남어의 한자어 현상 이해를 평가하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- `expected_explanation`: The expected reasoning and answer` · 신뢰도 medium
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `4 languages` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `101` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A comprehensive evaluation dataset for testing Large Language Models' understanding of Sino-Xenic linguistic phenomena across Chinese, Japanese, Korean, and Vie` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `A comprehensive evaluation dataset for testing Large Language Models' understanding of Sino-Xenic linguistic phenomena` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `expected_explanation` 열 p90 404자 ≈ 101 토큰 (viewer statistics, default/train)
