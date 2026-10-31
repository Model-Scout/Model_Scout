---
type: "dataset"
id: "clips/mqa"
source: "huggingface"
url: "https://huggingface.co/datasets/clips/mqa"
downloads: 2586
summary: "Common Crawl에서 추출한 다국어 FAQ 및 커뮤니티 질의응답 데이터셋입니다."
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
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# clips/mqa

> dataset · [Hugging Face](https://huggingface.co/datasets/clips/mqa)

Common Crawl에서 추출한 다국어 FAQ 및 커뮤니티 질의응답 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories, task_ids = `question-answering` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `Questions are divided between Frequently Asked Questions (FAQ) pages and Community Question Answering (CQA) pages.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Questions are divided between Frequently Asked Questions (FAQ) pages and Community Question Answering (CQA) pages.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `39 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `33` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MQA is a multilingual corpus of questions and answers parsed from the Common Crawl.` · 신뢰도 low
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `999999999.0` · 신뢰도 high

샘플 길이: `name` 열 p90 132자 ≈ 33 토큰 (viewer statistics, ko-all-question/train)
