---
type: "dataset"
id: "allenai/pixmo-cap-qa"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/pixmo-cap-qa"
downloads: 408
summary: "PixMo-CapQA는 이미지에 관한 질문/답변 쌍을 생성한 합성 데이터셋으로 Molmo 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[질의응답]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# allenai/pixmo-cap-qa

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/pixmo-cap-qa)

PixMo-CapQA는 이미지에 관한 질문/답변 쌍을 생성한 합성 데이터셋으로 Molmo 모델 학습에 사용됨

## 분류

- **작업**: [[질의응답]] — ner · readme = `PixMo-CapQA is a synthetic dataset of question/answer pairs about images.` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — metadata · modality, task:visual_qa = `image` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `The `question` field contains the input text, it includes "[USER]" and "[ASSISTANT]" tags` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `The `answer` field contains the final target output text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `909` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `PixMo-CapQA is a synthetic dataset of question/answer pairs about images.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `PixMo-CapQA is a part of the PixMo dataset collection and was used to train the Molmo family of models` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 1363자 ≈ 909 토큰 (viewer statistics, default/train)
