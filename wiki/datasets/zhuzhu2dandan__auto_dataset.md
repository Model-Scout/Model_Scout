---
type: "dataset"
id: "zhuzhu2dandan/auto_dataset"
source: "huggingface"
url: "https://huggingface.co/datasets/zhuzhu2dandan/auto_dataset"
downloads: 27
summary: "42개 언어로 번역된 MMLU 질문과 문화 민감도 주석을 포함한 다국어 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
---
# zhuzhu2dandan/auto_dataset

> dataset · [Hugging Face](https://huggingface.co/datasets/zhuzhu2dandan/auto_dataset)

42개 언어로 번역된 MMLU 질문과 문화 민감도 주석을 포함한 다국어 평가 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `- `answer': the correct answer (A/B/C/D)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `42 languages` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Global-MMLU 🌍 is a multilingual evaluation set spanning 42 languages, including English.` · 신뢰도 medium
