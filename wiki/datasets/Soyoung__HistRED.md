---
type: "dataset"
id: "Soyoung/HistRED"
source: "huggingface"
url: "https://huggingface.co/datasets/Soyoung/HistRED"
downloads: 301
summary: "조선시대 역사 문서 기반 관계 추출 데이터셋으로, 한국어와 한자로 된 문서에서 명명된 개체와 관계를 추출하는 데 사용됨."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# Soyoung/HistRED

> dataset · [Hugging Face](https://huggingface.co/datasets/Soyoung/HistRED)

조선시대 역사 문서 기반 관계 추출 데이터셋으로, 한국어와 한자로 된 문서에서 명명된 개체와 관계를 추출하는 데 사용됨.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction = `parallel relationships between Korean and Hanja texts` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `A Historical Document-Level Relation Extraction Dataset (ACL 2023)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `dataset.py return processed dataset that can be easily applied to general NLP models.` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
