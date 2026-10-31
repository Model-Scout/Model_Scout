---
type: "dataset"
id: "KushanH/m2ds"
source: "huggingface"
url: "https://huggingface.co/datasets/KushanH/m2ds"
downloads: 27
summary: "BBC 뉴스 기사와 요약문으로 구성된 다국어 다중문서 요약 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[si]]"
  - "[[ta]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[뉴스·미디어]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# KushanH/m2ds

> dataset · [Hugging Face](https://huggingface.co/datasets/KushanH/m2ds)

BBC 뉴스 기사와 요약문으로 구성된 다국어 다중문서 요약 데이터셋입니다.

## 분류

- **작업**: [[요약]] — metadata · readme, task_categories = `summarization` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:summarization = `| `summary` | string | Reference summary combining BBC summaries for the cluster |` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[si]] — metadata · languages = `si` · 신뢰도 high
- **언어**: [[ta]] — metadata · languages = `ta` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[뉴스·미디어]] — ner · readme = `M2DS is a multilingual multi-document summarisation dataset built from BBC news articles and professionally written BBC summaries` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `| `test` | Final evaluation |` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `| `train` | Model training |` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
