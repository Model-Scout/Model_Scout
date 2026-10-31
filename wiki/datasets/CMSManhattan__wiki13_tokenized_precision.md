---
type: "dataset"
id: "CMSManhattan/wiki13_tokenized_precision"
source: "huggingface"
url: "https://huggingface.co/datasets/CMSManhattan/wiki13_tokenized_precision"
downloads: 235
summary: "13개 언어 위키피디아 토큰화 데이터셋으로 언어 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# CMSManhattan/wiki13_tokenized_precision

> dataset · [Hugging Face](https://huggingface.co/datasets/CMSManhattan/wiki13_tokenized_precision)

13개 언어 위키피디아 토큰화 데이터셋으로 언어 모델 학습에 사용됨

## 분류

- **작업**: [[언어 모델링]] — ner · readme = `Wikipedia in 13 languages, tokenized with CMSManhattan/JiRackPrecisionTokenizer and packed into 2048-token blocks` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:language_modeling = `tokenized with CMSManhattan/JiRackPrecisionTokenizer and packed into 2048-token blocks` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Format: `torch.load(f)["input_ids"]` = list of LongTensor(2048)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — tag_match · readme, tags = `wikipedia` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `97 train shards (`wiki_train_shard_NNNN.pt`, 5000 blocks each, ~0.99B tokens) + `wiki_val.pt` (512 blocks)` · 신뢰도 medium
