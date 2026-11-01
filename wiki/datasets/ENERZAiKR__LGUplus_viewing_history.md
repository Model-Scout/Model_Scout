---
type: "dataset"
id: "ENERZAiKR/LGUplus_viewing_history"
source: "huggingface"
url: "https://huggingface.co/datasets/ENERZAiKR/LGUplus_viewing_history"
downloads: 19
summary: "한국인 가상 페르소나 1만 명의 일주일치 TV 시청이력 합성 데이터셋으로 TV 추천 및 개인화에 활용됩니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[상거래·상품]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ENERZAiKR/LGUplus_viewing_history

> dataset · [Hugging Face](https://huggingface.co/datasets/ENERZAiKR/LGUplus_viewing_history)

한국인 가상 페르소나 1만 명의 일주일치 TV 시청이력 합성 데이터셋으로 TV 추천 및 개인화에 활용됩니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `TV 프로그램 추천/개인화 모델 학습·평가` · 신뢰도 low
- **작업**: [[임베딩]] — ner · readme = `시청 패턴 기반 사용자 프로파일링 연구` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:embedding, task:generation = `한국인 가상 페르소나 1만 명의 일주일치 TV 시청이력 합성 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `시청한 프로그램의 방송 내용 한 문장 요약 (교사 LLM이 웹검색 근거로 생성, 전 레코드 100% 매칭)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[상거래·상품]] — ner · readme = `TV 프로그램 추천/개인화 모델 학습·평가` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `스플릿 | train 9,000 / test 1,000 (페르소나 단위 랜덤 분할, seed 42)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
