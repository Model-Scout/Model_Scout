---
type: "dataset"
id: "mimir-lcm/fineweb-2-sentence-split"
source: "huggingface"
url: "https://huggingface.co/datasets/mimir-lcm/fineweb-2-sentence-split"
downloads: 4609
summary: "Fineweb 2 데이터를 문장 단위로 분할한 데이터셋으로, 언어별 균형을 맞추기 위해 샘플링함."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# mimir-lcm/fineweb-2-sentence-split

> dataset · [Hugging Face](https://huggingface.co/datasets/mimir-lcm/fineweb-2-sentence-split)

Fineweb 2 데이터를 문장 단위로 분할한 데이터셋으로, 언어별 균형을 맞추기 위해 샘플링함.

## 분류

- **작업**: [[임베딩]] — ner · readme = `Fineweb 2 split into sentences.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding = `To split the text into sentences we used the sat3-l model from the wtpsplit library.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Fineweb 2 split into sentences.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[장문]] — viewer_stats · viewer_statistics = `6176` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Fineweb 2 split into sentences.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Instances per languages were sampled by us to balance the data w.r.t. Fineweb-edu.` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 24706자 ≈ 6176 토큰 (viewer statistics, kor_Hang/train)
