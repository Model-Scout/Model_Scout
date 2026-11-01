---
type: "dataset"
id: "huggingface-KREW/KoCulture-Descriptions"
source: "huggingface"
url: "https://huggingface.co/datasets/huggingface-KREW/KoCulture-Descriptions"
downloads: 59
summary: "한국어 신조어, 유행어, 밈 및 문화 현상에 대한 상세 설명 데이터셋으로 LLM의 이해 및 생성 능력 향상에 활용됨."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
  - "[[요약]]"
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
  - "[[문화·관광]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# huggingface-KREW/KoCulture-Descriptions

> dataset · [Hugging Face](https://huggingface.co/datasets/huggingface-KREW/KoCulture-Descriptions)

한국어 신조어, 유행어, 밈 및 문화 현상에 대한 상세 설명 데이터셋으로 LLM의 이해 및 생성 능력 향상에 활용됨.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `대형 언어 모델(LLM)의 한국어 이해 및 생성 능력을 심층적으로 향상시키기 위해 구축되었습니다.` · 신뢰도 medium
- **작업**: [[문서 검색]] — ner · readme = `한국어 신조어, 유행어, 밈 관련 정보 검색 및 요약 시스템 개발` · 신뢰도 medium
- **작업**: [[요약]] — ner · readme = `한국어 신조어, 유행어, 밈 관련 정보 검색 및 요약 시스템 개발` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:retrieval, task:summarization = `각 용어의 정의, 유래, 사용 방식, 문화적 맥락 등을 포함합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:summarization = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `316` · 신뢰도 medium
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-sa-4.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `최신 한국어 신조어, 유행어, 밈 및 관련 문화 현상에 대한 상세한 설명` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 474자 ≈ 316 토큰 (viewer statistics, default/train)
