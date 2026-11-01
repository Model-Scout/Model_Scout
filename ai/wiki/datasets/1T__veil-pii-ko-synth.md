---
type: "dataset"
id: "1T/veil-pii-ko-synth"
source: "huggingface"
url: "https://huggingface.co/datasets/1T/veil-pii-ko-synth"
downloads: 100
summary: "Veil-PII-Ko-Lite 학습용 한국어 개인정보(PII) 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# 1T/veil-pii-ko-synth

> dataset · [Hugging Face](https://huggingface.co/datasets/1T/veil-pii-ko-synth)

Veil-PII-Ko-Lite 학습용 한국어 개인정보(PII) 합성 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — metadata · readme, tags, task_categories = `token-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction = `문장은 LLM 에게 맡기고…` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `175` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 PII 합성 데이터입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `heldout 은 모델 카드 벤치마크 표의 "합성 heldout v2" (n=670) 입니다.` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `train 은 공개 모델이 실제로 학습한 행 그대로이고` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 263자 ≈ 175 토큰 (viewer statistics, default/train)
