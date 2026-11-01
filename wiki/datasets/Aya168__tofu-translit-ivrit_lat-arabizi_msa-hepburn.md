---
type: "dataset"
id: "Aya168/tofu-translit-ivrit_lat-arabizi_msa-hepburn"
source: "huggingface"
url: "https://huggingface.co/datasets/Aya168/tofu-translit-ivrit_lat-arabizi_msa-hepburn"
downloads: 19
summary: "TOFU 데이터셋은 히브리어, 아랍어, 일본어의 라틴 문자 음역 데이터를 포함하며 다국어 언어 모델의 음역 영향 연구용입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
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
# Aya168/tofu-translit-ivrit_lat-arabizi_msa-hepburn

> dataset · [Hugging Face](https://huggingface.co/datasets/Aya168/tofu-translit-ivrit_lat-arabizi_msa-hepburn)

TOFU 데이터셋은 히브리어, 아랍어, 일본어의 라틴 문자 음역 데이터를 포함하며 다국어 언어 모델의 음역 영향 연구용입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `TOFU (Maini et al., 2024) asks factual questions about invented authors` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `unlearning transfers unevenly — which they attribute to *syntactic* distance between languages` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `built for "Script, Not Syntax: Transliteration as a Blind Spot in Multilingual Unlearning"` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:language_modeling = `Three Latin-script transliteration arms of the TOFU fictitious-author unlearning benchmark` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:language_modeling = `Three Latin-script transliteration arms of the TOFU fictitious-author unlearning benchmark` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Farashah et al.'s *Multilingual Amnesia* (EACL 2026) translated it into ten languages to study whether unlearning a fact in one language removes it in another` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `Three Latin-script transliteration arms of the TOFU fictitious-author unlearning benchmark` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[Aya168__aya-expanse-8b-tofu-13lang-v3|Aya168/aya-expanse-8b-tofu-13lang-v3]]
