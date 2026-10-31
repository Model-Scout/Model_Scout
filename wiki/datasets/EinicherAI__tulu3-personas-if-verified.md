---
type: "dataset"
id: "EinicherAI/tulu3-personas-if-verified"
source: "huggingface"
url: "https://huggingface.co/datasets/EinicherAI/tulu3-personas-if-verified"
downloads: 10
summary: "정확한 지시 수행을 위한 영어 기반 소형 모델 SFT용 검증된 Tulu3 페르소나 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# EinicherAI/tulu3-personas-if-verified

> dataset · [Hugging Face](https://huggingface.co/datasets/EinicherAI/tulu3-personas-if-verified)

정확한 지시 수행을 위한 영어 기반 소형 모델 SFT용 검증된 Tulu3 페르소나 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `for small-model SFT on precise instruction-following (English, C13/C14 in the Sigi capability matrix)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `assistant response` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `English-only; does not contribute to Sigi's non-English language floors.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `split train (29980 rows)` · 신뢰도 medium
