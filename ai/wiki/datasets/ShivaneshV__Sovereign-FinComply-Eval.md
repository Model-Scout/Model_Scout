---
type: "dataset"
id: "ShivaneshV/Sovereign-FinComply-Eval"
source: "huggingface"
url: "https://huggingface.co/datasets/ShivaneshV/Sovereign-FinComply-Eval"
downloads: 12
summary: "15개 저자원 언어의 법률·금융 규정 번역 정확도 평가용 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
---
# ShivaneshV/Sovereign-FinComply-Eval

> dataset · [Hugging Face](https://huggingface.co/datasets/ShivaneshV/Sovereign-FinComply-Eval)

15개 저자원 언어의 법률·금융 규정 번역 정확도 평가용 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `to score each translation's legal fidelity and semantic drift` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[번역]] — metadata · task_categories = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:generation, task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation, task:translation = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `15 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `healthcare` · 신뢰도 medium
- **도메인**: [[법률]] — ner · readme = `Legal and financial rules (RBI compounding laws, HIPAA standards)` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `A high-fidelity multilingual evaluation and alignment dataset` · 신뢰도 medium
