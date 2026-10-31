---
type: "dataset"
id: "gentaiscool/bitext_sib200_miners"
source: "huggingface"
url: "https://huggingface.co/datasets/gentaiscool/bitext_sib200_miners"
downloads: 5478
summary: "다양한 언어 쌍의 병렬 문장 데이터로 다국어 기계 번역 및 언어 모델 학습에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[임베딩]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# gentaiscool/bitext_sib200_miners

> dataset · [Hugging Face](https://huggingface.co/datasets/gentaiscool/bitext_sib200_miners)

다양한 언어 쌍의 병렬 문장 데이터로 다국어 기계 번역 및 언어 모델 학습에 활용됨

## 분류

- **작업**: [[임베딩]] — ner · readme = `bitext_sib200_miners` · 신뢰도 low
- **작업**: [[번역]] — ner · readme = `language` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:embedding, task:translation = `language` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:translation = `language` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `197 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `48` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `language` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `split: train` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `sentence1` 열 p90 191자 ≈ 48 토큰 (viewer statistics, eng_Latn-kor_Hang/train)
