---
type: "dataset"
id: "HuggingFaceTB/smoltalk"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceTB/smoltalk"
downloads: 49686
summary: "SmolTalk은 LLM 지도학습용 합성 데이터셋으로 다양한 텍스트 편집, 요약, 추론 작업에 활용됩니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[요약]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# HuggingFaceTB/smoltalk

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceTB/smoltalk)

SmolTalk은 LLM 지도학습용 합성 데이터셋으로 다양한 텍스트 편집, 요약, 추론 작업에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Smol-contraints: a 36K-sample dataset that trains models to follow specific constraints, such as generating responses with a fixed number of sentences or words,` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `This is a synthetic dataset designed for supervised finetuning (SFT) of LLMs.` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Smol-rewrite: an 50k-sample collection focused on text rewriting tasks, such as adjusting tone to be more friendly or professional.` · 신뢰도 low
- **작업**: [[요약]] — ner · readme = `Smol-summarize: an 100k-sample dataset specialized in email and news summarization.` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:classification, task:generation, task:information_extraction, task:summarization = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:summarization = `Smol-contraints: a 36K-sample dataset that trains models to follow specific constraints, such as generating responses with a fixed number of sentences or words,` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `During the development of SmolLM2, we observed that models finetuned on public SFT datasets underperformed compared to other models with proprietary instruction` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This is a synthetic dataset designed for supervised finetuning (SFT) of LLMs.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
