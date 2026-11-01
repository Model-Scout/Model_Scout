---
type: "dataset"
id: "alchemine/namuwiki-arknights-text-preview"
source: "huggingface"
url: "https://huggingface.co/datasets/alchemine/namuwiki-arknights-text-preview"
downloads: 54
summary: "명일방주 관련 나무위키 문서에서 추출한 한국어 텍스트 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
  - "[[요약]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# alchemine/namuwiki-arknights-text-preview

> dataset · [Hugging Face](https://huggingface.co/datasets/alchemine/namuwiki-arknights-text-preview)

명일방주 관련 나무위키 문서에서 추출한 한국어 텍스트 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:retrieval, task:summarization = `한국어 텍스트 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization = `한국어 텍스트 데이터셋입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `이 데이터셋은 명일방주 - 나무위키 관련 문서에서 추출한 한국어 텍스트 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 테스트 버전으로, 데이터 일관성이 보장되지 않습니다.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
