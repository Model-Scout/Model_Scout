---
type: "dataset"
id: "davidkim205/FinNewsBench"
source: "huggingface"
url: "https://huggingface.co/datasets/davidkim205/FinNewsBench"
downloads: 19
summary: "FinNewsBench는 한국어 합성 금융 뉴스 기사로 구성된 다중 측면 구조화 정보 추출용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# davidkim205/FinNewsBench

> dataset · [Hugging Face](https://huggingface.co/datasets/davidkim205/FinNewsBench)

FinNewsBench는 한국어 합성 금융 뉴스 기사로 구성된 다중 측면 구조화 정보 추출용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `The dataset is designed to support multi-aspect structured information extraction tasks, where models generate structured information from information-dense fin` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:generation, task:information_extraction = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The task is formulated as a text-to-structured-output generation problem, where models generate structured fields directly from raw news text.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `784` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is designed to support multi-aspect structured information extraction tasks` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `body` 열 p90 1176자 ≈ 784 토큰 (viewer statistics, default/train)
