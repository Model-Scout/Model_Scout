---
type: "dataset"
id: "uilab/BLEnD"
source: "huggingface"
url: "https://huggingface.co/datasets/uilab/BLEnD"
downloads: 1828
summary: "BLEnD는 다양한 문화와 언어의 일상 지식을 평가하는 LLM 벤치마크 데이터셋입니다."
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# uilab/BLEnD

> dataset · [Hugging Face](https://huggingface.co/datasets/uilab/BLEnD)

BLEnD는 다양한 문화와 언어의 일상 지식을 평가하는 LLM 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `The benchmark comprises 52.6k question-answer pairs from 16 countries/regions, in 13 different languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `We evaluate LLMs in two formats: short-answer questions, and multiple-choice questions.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `22 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `26` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Large language models (LLMs) often lack culture-specific everyday knowledge, especially across diverse regions and non-English languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `All the data samples for short-answer questions, including the human-annotated answers, can be found in the `data/` directory.` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `en_question` 열 p90 104자 ≈ 26 토큰 (viewer statistics, annotations/DZ)
