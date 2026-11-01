---
type: "dataset"
id: "anshulsc/MirageTVQA-0.1"
source: "huggingface"
url: "https://huggingface.co/datasets/anshulsc/MirageTVQA-0.1"
downloads: 59
summary: "24개 언어의 시각적 노이즈가 있는 표에 대한 다국어 시각-언어 질의응답 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
  - "[[표 질의응답]]"
  - "[[이미지 인식]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# anshulsc/MirageTVQA-0.1

> dataset · [Hugging Face](https://huggingface.co/datasets/anshulsc/MirageTVQA-0.1)

24개 언어의 시각적 노이즈가 있는 표에 대한 다국어 시각-언어 질의응답 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `MirageTVQA: Multilingual Table Visual Question Answering Benchmark` · 신뢰도 medium
- **작업**: [[표 질의응답]] — metadata · task_categories = `table-question-answering` · 신뢰도 low
- **작업**: [[이미지 인식]] — ner · readme = `evaluate Vision-Language Models (VLMs) on realistic table understanding tasks` · 신뢰도 medium
- **작업**: [[이미지 이해]] — metadata · task_categories = `visual-question-answering` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:vision, task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — task_rule · task:table_qa = `table` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:question_answering, task:table_qa, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering, task:table_qa, task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `diverse domains (scientific, financial, general knowledge)` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `a comprehensive benchmark designed to evaluate Vision-Language Models (VLMs)` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
