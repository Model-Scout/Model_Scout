---
type: "dataset"
id: "AmazonScience/tydi-as2"
source: "huggingface"
url: "https://huggingface.co/datasets/AmazonScience/tydi-as2"
downloads: 683
summary: "TyDi-AS2는 8개 언어의 다국어 답변 문장 선택(AS2) 데이터셋으로, 저자들이 ACL 2023에서 발표한 논문 기반입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[bn]]"
  - "[[영어]]"
  - "[[fi]]"
  - "[[id]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[sw]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# AmazonScience/tydi-as2

> dataset · [Hugging Face](https://huggingface.co/datasets/AmazonScience/tydi-as2)

TyDi-AS2는 8개 언어의 다국어 답변 문장 선택(AS2) 데이터셋으로, 저자들이 ACL 2023에서 발표한 논문 기반입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, tags, task_categories, task_ids = `question-answering` · 신뢰도 high
- **작업**: [[문서 검색]] — metadata · readme, tags, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering, task:retrieval = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Label that indicates the answer sentence correctly answers the question (int, 1: correct, 0: incorrect)` · 신뢰도 medium
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fi]] — metadata · languages = `fi` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `941` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cdla-permissive-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `TyDi-AS2 and Xtr-TyDi-AS2 are multilingual Answer Sentence Selection (AS2) datasets comprising 8 diverse languages` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `For English-translated TyDi-AS2 dataset and Xtr-TyDi-AS2 dataset, the translated instances in JSONL files are listed in the same order of the original (native) ` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high

샘플 길이: `Sentence` 열 p90 3765자 ≈ 941 토큰 (viewer statistics, default/validation)
