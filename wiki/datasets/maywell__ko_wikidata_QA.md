---
type: "dataset"
id: "maywell/ko_wikidata_QA"
source: "huggingface"
url: "https://huggingface.co/datasets/maywell/ko_wikidata_QA"
downloads: 181
summary: "한국어 위키 데이터 QA셋으로 QA 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "not_ko"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# maywell/ko_wikidata_QA

> dataset · [Hugging Face](https://huggingface.co/datasets/maywell/ko_wikidata_QA)

한국어 위키 데이터 QA셋으로 QA 모델 학습에 사용됨

## 분류

- **작업**: [[질의응답]] — ner · readme = `한국어 위키 데이터 QA셋` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `한국어 위키 데이터 QA셋` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `한국어 위키 데이터 QA셋` · 신뢰도 medium
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `164` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 위키 데이터 QA셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `본 데이터는 Synatra-7B-Instruct 모델과 ChatGPT를 사용하여, 제작된 QA셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 656자 ≈ 164 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[TheBloke__PiVoT-0.1-Evil-a-GGUF|TheBloke/PiVoT-0.1-Evil-a-GGUF]]
- [[TheBloke__PiVoT-0.1-early-GGUF|TheBloke/PiVoT-0.1-early-GGUF]]
- [[blueapple8259__TinyKo|blueapple8259/TinyKo]]
- [[blueapple8259__test_model1|blueapple8259/test_model1]]
- [[maywell__PiVoT-0.1-Evil-a|maywell/PiVoT-0.1-Evil-a]]
- [[tensorblock__PiVoT-0.1-early-GGUF|tensorblock/PiVoT-0.1-early-GGUF]]
