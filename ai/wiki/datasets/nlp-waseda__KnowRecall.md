---
type: "dataset"
id: "nlp-waseda/KnowRecall"
source: "huggingface"
url: "https://huggingface.co/datasets/nlp-waseda/KnowRecall"
downloads: 111
summary: "KnowRecall는 다국어 VQA 벤치마크로, 다국어 환경에서 MLLM의 사실 지식 일관성을 평가합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
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
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlp-waseda/KnowRecall

> dataset · [Hugging Face](https://huggingface.co/datasets/nlp-waseda/KnowRecall)

KnowRecall는 다국어 VQA 벤치마크로, 다국어 환경에서 MLLM의 사실 지식 일관성을 평가합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `3,000 multiple-choice questions on 1,500 global landmarks, each available in 15 languages` · 신뢰도 low
- **작업**: [[질의응답]] — ner · readme = `a multilingual VQA benchmark that evaluates cross-lingual consistency of factual knowledge in MLLMs` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `Image depicting the landmark.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:question_answering, task:visual_qa = `Question asked based on the image.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering, task:visual_qa = `Ground truth answer to the question.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `32` · 신뢰도 medium
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `cc` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a multilingual VQA benchmark that evaluates cross-lingual consistency of factual knowledge in MLLMs` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `KnowRecall benchmark, introduced in Traveling Across Languages: Benchmarking Cross-Lingual Consistency in Multimodal LLMs` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 128자 ≈ 32 토큰 (viewer statistics, default/ar)
