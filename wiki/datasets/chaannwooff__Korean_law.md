---
type: "dataset"
id: "chaannwooff/Korean_law"
source: "huggingface"
url: "https://huggingface.co/datasets/chaannwooff/Korean_law"
downloads: 87
summary: "법제처 국가법령정보센터 OpenAPI로 수집한 한국어 법령 전문 조문 단위 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# chaannwooff/Korean_law

> dataset · [Hugging Face](https://huggingface.co/datasets/chaannwooff/Korean_law)

법제처 국가법령정보센터 OpenAPI로 수집한 한국어 법령 전문 조문 단위 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · tags, task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — metadata · readme, task_categories = `fill-mask` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `법률, 대통령령, 부령 등 현행 법령 전문을 조문 단위로 추출하였습니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `법률, 대통령령, 부령 등 현행 법령 전문을 조문 단위로 추출하였습니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `law` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 LLM 학습용 법령 데이터셋입니다.` · 신뢰도 medium
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high
