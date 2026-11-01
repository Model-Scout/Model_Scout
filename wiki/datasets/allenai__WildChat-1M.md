---
type: "dataset"
id: "allenai/WildChat-1M"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/WildChat-1M"
downloads: 36879
summary: "WildChat-1M은 인간과 ChatGPT 간 100만 대화 및 인구통계 데이터를 포함한 다국어 대화 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
  - "[[중규모 데이터]]"
---
# allenai/WildChat-1M

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/WildChat-1M)

WildChat-1M은 인간과 ChatGPT 간 100만 대화 및 인구통계 데이터를 포함한 다국어 대화 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Note that this version of the dataset only contains non-toxic user inputs/ChatGPT responses.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `WildChat is a collection of 1 million conversations between human users and ChatGPT` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `WildChat is a collection of 1 million conversations between human users and ChatGPT` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `16` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Language(s) (NLP): multi-lingual` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `WildChat can serve both as a dataset for instructional fine-tuning and as a valuable resource for studying user behaviors.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `hashed_ip` 열 p90 64자 ≈ 16 토큰 (viewer statistics, default/train)
