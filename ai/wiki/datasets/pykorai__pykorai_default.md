---
type: "dataset"
id: "pykorai/pykorai_default"
source: "huggingface"
url: "https://huggingface.co/datasets/pykorai/pykorai_default"
downloads: 12
summary: "한국어 대화형 QA 데이터셋으로 LLM 미세조정 및 대화형 AI 개발에 활용됨"
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# pykorai/pykorai_default

> dataset · [Hugging Face](https://huggingface.co/datasets/pykorai/pykorai_default)

한국어 대화형 QA 데이터셋으로 LLM 미세조정 및 대화형 AI 개발에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한국어 자연어 이해(NLU) 및 생성(NLG) 모델의 연구와 성능 평가를 위한 벤치마크로 사용됩니다.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `거대 언어 모델(LLM)의 미세 조정(Fine-tuning) 및 사전 학습(Pre-training)에 최적화된 고품질 한국어 대화 말뭉치(Corpus)를 구축하는 것을 목표로 합니다.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `한국어 대화 말뭉치(Corpus)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `한국어 대화 말뭉치(Corpus)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `60` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 91자 ≈ 60 토큰 (viewer statistics, default/train)
