---
type: "dataset"
id: "robvanderg/MultiLexNorm"
source: "huggingface"
url: "https://huggingface.co/datasets/robvanderg/MultiLexNorm"
downloads: 226
summary: "다국어 어휘 정규화 데이터셋으로, 여러 언어의 단어 정규화 작업에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# robvanderg/MultiLexNorm

> dataset · [Hugging Face](https://huggingface.co/datasets/robvanderg/MultiLexNorm)

다국어 어휘 정규화 데이터셋으로, 여러 언어의 단어 정규화 작업에 사용됨.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `Some of the languages include annotation for word splits and merges.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `Most	most
social	social
pple	people
r	are
troublesome	troublesome` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Most	most
social	social
pple	people
r	are
troublesome	troublesome` · 신뢰도 low
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The data in this benchmark comes from many different sources, we collected existing datasets and converged them to the same formate.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This is the HuggingFace version of the MultiLexNorm dataset.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
