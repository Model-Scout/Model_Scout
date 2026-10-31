---
type: "dataset"
id: "DAMO-NLP-SG/MultiJail"
source: "huggingface"
url: "https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail"
downloads: 1285
summary: "다국어 대형 언어 모델의 탈옥(jailbreak) 문제를 연구하기 위한 다국어 탈옥 도전 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[ar]]"
  - "[[bn]]"
  - "[[영어]]"
  - "[[it]]"
  - "[[jv]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[sw]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# DAMO-NLP-SG/MultiJail

> dataset · [Hugging Face](https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail)

다국어 대형 언어 모델의 탈옥(jailbreak) 문제를 연구하기 위한 다국어 탈옥 도전 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages.` · 신뢰도 low
- **언어**: [[ar]] — metadata · languages = `ar` · 신뢰도 high
- **언어**: [[bn]] — metadata · languages = `bn` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[jv]] — metadata · languages = `jv` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[sw]] — metadata · languages = `sw` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `38` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Our research investigates the safety challenges of LLMs in multilingual settings.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `To address the identified risks and vulnerabilities, we commit to open-sourcing the data used in our study.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `it` 열 p90 152자 ≈ 38 토큰 (viewer statistics, default/train)
