---
type: "dataset"
id: "overfit-brothers/KRX-INST"
source: "huggingface"
url: "https://huggingface.co/datasets/overfit-brothers/KRX-INST"
downloads: 64
summary: "제3회 KRX 금융 언어 모델 경진대회용 금융 분야 인스트럭션 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# overfit-brothers/KRX-INST

> dataset · [Hugging Face](https://huggingface.co/datasets/overfit-brothers/KRX-INST)

제3회 KRX 금융 언어 모델 경진대회용 금융 분야 인스트럭션 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `금융 관련 유해질문에 대한 방어 생성 성능 측정용 데이터셋` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Instruction 데이터셋` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `fingpt-convfinqa 데이터셋을 샘플링하여 번역한 mncai/finance-tasks-ConvFinQA-ko 의 질문 문장` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:question_answering = `Instruction 데이터셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `Instruction 데이터셋` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `46` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-nd-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `KRX 금융 언어 모델 경진대회 Instruction 데이터셋` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `금융 판례 기반 instruction 데이터` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Instruction 데이터셋` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 68자 ≈ 46 토큰 (viewer statistics, evil-jailbreak-kor-test/train)
