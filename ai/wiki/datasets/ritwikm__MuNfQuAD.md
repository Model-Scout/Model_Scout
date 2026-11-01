---
type: "dataset"
id: "ritwikm/MuNfQuAD"
source: "huggingface"
url: "https://huggingface.co/datasets/ritwikm/MuNfQuAD"
downloads: 18
summary: "비사실형 다국어 질문응답용 MuNfQuAD 데이터셋으로 문단 선택에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 분류]]"
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
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
---
# ritwikm/MuNfQuAD

> dataset · [Hugging Face](https://huggingface.co/datasets/ritwikm/MuNfQuAD)

비사실형 다국어 질문응답용 MuNfQuAD 데이터셋으로 문단 선택에 활용됨

## 분류

- **작업**: [[텍스트 분류]] — metadata · task_categories = `text-classification` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `Multilingual Non-factoid Question Answering with Answer Paragraph Selection` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Multilingual Non-factoid Question Answering with Answer Paragraph Selection` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `37 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `The dataset is introduced in the paper Multilingual Non-factoid Question Answering with Answer Paragraph Selection` · 신뢰도 low
