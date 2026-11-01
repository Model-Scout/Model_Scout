---
type: "dataset"
id: "maum-ai/KOFFVQA_Data"
source: "huggingface"
url: "https://huggingface.co/datasets/maum-ai/KOFFVQA_Data"
downloads: 104
summary: "한국어로 된 이미지 질문응답 평가용 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
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
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# maum-ai/KOFFVQA_Data

> dataset · [Hugging Face](https://huggingface.co/datasets/maum-ai/KOFFVQA_Data)

한국어로 된 이미지 질문응답 평가용 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · readme, task_categories = `image-text-to-text` · 신뢰도 high
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme, task:visual_qa = `This contains the data for the benchmark consisting of images` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering, task:visual_qa = `their corresponding questions` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `generate comprehensive and accurate text responses to questions about images` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `57` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `KOFFVQA is a general-purpose VLM benchmark in the Korean language` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `This contains the data for the benchmark` · 신뢰도 medium
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 85자 ≈ 57 토큰 (viewer statistics, default/train)
