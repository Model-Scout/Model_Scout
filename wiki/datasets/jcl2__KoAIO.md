---
type: "dataset"
id: "jcl2/KoAIO"
source: "huggingface"
url: "https://huggingface.co/datasets/jcl2/KoAIO"
downloads: 13
summary: "한국어 검색어에 대한 AI 검색 요약 활성화 여부와 활성화 요인 3개 라벨 및 확신도를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# jcl2/KoAIO

> dataset · [Hugging Face](https://huggingface.co/datasets/jcl2/KoAIO)

한국어 검색어에 대한 AI 검색 요약 활성화 여부와 활성화 요인 3개 라벨 및 확신도를 담은 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = `한국어 텍스트, `ORCAS`/`AIO`에만 해당 | GPT-5.6 Terra로 번역한 검색어` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `AI 검색 요약 활성화 여부와 활성화 요인 3개의 라벨(문법적 형태, 검색 의도, 주제)과 LLM의 해당 라벨 판정 확신도를 담은 데이터셋입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 검색어에 대한 AI 검색 요약 활성화 여부와 활성화 요인 3개의 라벨(문법적 형태, 검색 의도, 주제)과 LLM의 해당 라벨 판정 확신도를 담은 데이터셋입니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `본 데이터셋은 비영리 학술 연구 목적으로만 사용할 수 있습니다.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
