---
type: "dataset"
id: "dibao-research/ming-qing-wenji-corpus"
source: "huggingface"
url: "https://huggingface.co/datasets/dibao-research/ming-qing-wenji-corpus"
downloads: 26
summary: "명청별집어료고는 명청시대 472종 별집 문헌을 구조화한 고전 한문 디지털 코퍼스다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[lzh]]"
  - "[[다국어]]"
  - "[[중국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[학술·논문]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dibao-research/ming-qing-wenji-corpus

> dataset · [Hugging Face](https://huggingface.co/datasets/dibao-research/ming-qing-wenji-corpus)

명청별집어료고는 명청시대 472종 별집 문헌을 구조화한 고전 한문 디지털 코퍼스다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · readme, task_categories = `token-classification` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:information_extraction = `Full text content` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Full text content` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[lzh]] — metadata · languages = `lzh` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `3 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1009` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[학술·논문]] — ner · readme = `across three centuries of Chinese intellectual history.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = ``train` | 20,868 | Complete corpus (all collections) / 전체 코퍼스 (전 별집 포함)` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 4038자 ≈ 1009 토큰 (viewer statistics, default/train)
