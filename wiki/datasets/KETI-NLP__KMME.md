---
type: "dataset"
id: "KETI-NLP/KMME"
source: "huggingface"
url: "https://huggingface.co/datasets/KETI-NLP/KMME"
downloads: 186
summary: "KMME는 시각 증거 기반 한국어 멀티모달 평가 데이터셋으로 모델의 증거 제한 능력을 평가합니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# KETI-NLP/KMME

> dataset · [Hugging Face](https://huggingface.co/datasets/KETI-NLP/KMME)

KMME는 시각 증거 기반 한국어 멀티모달 평가 데이터셋으로 모델의 증거 제한 능력을 평가합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `KMME evaluates whether a model limits its description and inferences to visual evidence` · 신뢰도 low
- **작업**: [[질의응답]] — tag_match · tags = `multiple-choice` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `42 four-image families` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:visual_qa = `질문·선택지` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `정답·유형·해설은 모델 입력에서 제외합니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `58` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KMME: Korean Multimodal Evidence-grounded Evaluation` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `전체 고정본 평가` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 87자 ≈ 58 토큰 (viewer statistics, full168/test)
