---
type: "dataset"
id: "vector-institute/HumaniBench"
source: "huggingface"
url: "https://huggingface.co/datasets/vector-institute/HumaniBench"
downloads: 167
summary: "HumaniBench는 대규모 멀티모달 모델 평가를 위한 인간 중심 벤치마크로, 이미지-질문 쌍 32,000개 이상을 포함합니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[fa]]"
  - "[[fr]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
  - "[[ta]]"
  - "[[ur]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[비상업 전용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# vector-institute/HumaniBench

> dataset · [Hugging Face](https://huggingface.co/datasets/vector-institute/HumaniBench)

HumaniBench는 대규모 멀티모달 모델 평가를 위한 인간 중심 벤치마크로, 이미지-질문 쌍 32,000개 이상을 포함합니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Robustness, reasoning, and ethics` · 신뢰도 low
- **작업**: [[텍스트 생성]] — ner · readme = `Empathetic captioning` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `Visual grounding` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 medium
- **작업**: [[이미지 인식]] — metadata · task_categories = `object-detection` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:vision, task:visual_qa = `image–question pairs` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction, task:question_answering, task:visual_qa = `image–question pairs` · 신뢰도 high
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — metadata · modality = `timeseries` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:visual_qa = `Answer` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[fa]] — metadata · languages = `fa` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `8 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **언어**: [[ta]] — metadata · languages = `ta` · 신뢰도 high
- **언어**: [[ur]] — metadata · languages = `ur` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `93` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `Answer` 열 p90 374자 ≈ 93 토큰 (viewer statistics, task1_Scene_Understanding/test)
