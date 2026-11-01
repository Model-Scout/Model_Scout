---
type: "dataset"
id: "playcat/cat-enrichment-methods"
source: "huggingface"
url: "https://huggingface.co/datasets/playcat/cat-enrichment-methods"
downloads: 102
summary: "고양이 환경 풍부화 방법 50가지를 분류하여 고양이 복지 향상을 위한 참고 자료로 제공하는 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
  - "[[질의응답]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# playcat/cat-enrichment-methods

> dataset · [Hugging Face](https://huggingface.co/datasets/playcat/cat-enrichment-methods)

고양이 환경 풍부화 방법 50가지를 분류하여 고양이 복지 향상을 위한 참고 자료로 제공하는 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `each classified by category, effectiveness, and evidence level.` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `It serves as a structured reference for pet care professionals, researchers, and cat guardians seeking to improve feline welfare.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification, task:information_extraction, task:question_answering, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `A curated bilingual (Korean/English) dataset of 50 evidence-based cat environmental enrichment methods` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A curated bilingual (Korean/English) dataset of 50 evidence-based cat environmental enrichment methods` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
