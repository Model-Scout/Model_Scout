---
type: "dataset"
id: "huggingface-KREW/KoCulture-Dialogues"
source: "huggingface"
url: "https://huggingface.co/datasets/huggingface-KREW/KoCulture-Dialogues"
downloads: 76
summary: "한국어 신조어, 유행어, 밈 대화 데이터셋으로 LLM의 한국어 이해 및 생성 능력 향상에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
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
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# huggingface-KREW/KoCulture-Dialogues

> dataset · [Hugging Face](https://huggingface.co/datasets/huggingface-KREW/KoCulture-Dialogues)

한국어 신조어, 유행어, 밈 대화 데이터셋으로 LLM의 한국어 이해 및 생성 능력 향상에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — tag_match · readme, tags = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `각 데이터 항목은 특정 유행어/밈을 나타내는 `title`, 해당 유행어/밈이 사용될 법한 맥락을 제시하는 `question`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `응답하는 `answer`로 이루어집니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `46` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `본 데이터셋은 최신 한국어 신조어, 유행어, 밈을 포함하여 대형 언어 모델(LLM)의 한국어 이해 및 생성 능력을 향상시키기 위해 구축되었습니다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `대형 언어 모델(LLM)의 한국어 학습 데이터 보강 및 성능 개선` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `answer` 열 p90 69자 ≈ 46 토큰 (viewer statistics, default/train)
