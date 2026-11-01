---
type: "dataset"
id: "kimchunsik03/KoreanGuardrail"
source: "huggingface"
url: "https://huggingface.co/datasets/kimchunsik03/KoreanGuardrail"
downloads: 87
summary: "한글 자모 단위 난독화에 대한 한국어 프롬프트 가드레일 강건성 평가 벤치마크입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# kimchunsik03/KoreanGuardrail

> dataset · [Hugging Face](https://huggingface.co/datasets/kimchunsik03/KoreanGuardrail)

한글 자모 단위 난독화에 대한 한국어 프롬프트 가드레일 강건성 평가 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `난독화 적용 후 텍스트 (모델 입력)` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `한국어 프롬프트 가드레일이 얼마나 강건한지 측정하는 벤치마크입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `benchmark (기본, split test): 평가용 본 데이터.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
