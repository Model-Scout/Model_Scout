---
type: "dataset"
id: "ibm-granite/ChartNet"
source: "huggingface"
url: "https://huggingface.co/datasets/ibm-granite/ChartNet"
downloads: 10359
summary: "ChartNet은 차트 이미지, 코드, 데이터, 요약, QA를 포함한 대규모 멀티모달 차트 이해 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[요약]]"
  - "[[표 질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# ibm-granite/ChartNet

> dataset · [Hugging Face](https://huggingface.co/datasets/ibm-granite/ChartNet)

ChartNet은 차트 이미지, 코드, 데이터, 요약, QA를 포함한 대규모 멀티모달 차트 이해 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `supporting structured data extraction and chart summarization` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `Complex QA pairs with step‑by‑step reasoning` · 신뢰도 medium
- **작업**: [[요약]] — ner · readme = `supporting structured data extraction and chart summarization` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:information_extraction, task:question_answering, task:summarization, task:table_qa, task:visual_qa = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:question_answering, task:summarization, task:table_qa, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `12 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1048` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-permissive-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Chart understanding requires models to jointly reason over geometric visual patterns, structured numerical data, and natural language descriptions` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `code` 열 p90 4191자 ≈ 1048 토큰 (viewer statistics, core_permissive/train)
