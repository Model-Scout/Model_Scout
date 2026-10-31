---
type: "dataset"
id: "patrickamadeus/pawsx_mt_triplet"
source: "huggingface"
url: "https://huggingface.co/datasets/patrickamadeus/pawsx_mt_triplet"
downloads: 153
summary: "PAWS-X 다국어 삼중항 데이터셋으로, 번역 모델별 문장 유사도 및 패러프레이즈 탐지에 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[es]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# patrickamadeus/pawsx_mt_triplet

> dataset · [Hugging Face](https://huggingface.co/datasets/patrickamadeus/pawsx_mt_triplet)

PAWS-X 다국어 삼중항 데이터셋으로, 번역 모델별 문장 유사도 및 패러프레이즈 탐지에 사용됨.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[임베딩]] — ner · readme = `paraphrase detection and text similarity tasks` · 신뢰도 low
- **작업**: [[번역]] — metadata · tags, task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:embedding, task:translation = `text1: First sentence (originally sentence1) text2: Second sentence (originally sentence2)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `label: Binary label (1 for paraphrase, 0 for non-paraphrase)` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PAWS-X (Paraphrase Adversaries from Word Scrambling) data` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset contains PAWS-X (Paraphrase Adversaries from Word Scrambling) data organized by translation models` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high
