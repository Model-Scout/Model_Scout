---
type: "dataset"
id: "brandonbaek/konglish-synthetic-instruct"
source: "huggingface"
url: "https://huggingface.co/datasets/brandonbaek/konglish-synthetic-instruct"
downloads: 11
summary: "한국어와 영어의 자연스러운 코드스위칭과 대화형 번역을 위한 합성 지시문 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# brandonbaek/konglish-synthetic-instruct

> dataset · [Hugging Face](https://huggingface.co/datasets/brandonbaek/konglish-synthetic-instruct)

한국어와 영어의 자연스러운 코드스위칭과 대화형 번역을 위한 합성 지시문 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Includes conversational code-switching, direct translation requests, grammatical mapping, explanation of Konglish idioms, and bilingual logical reasoning.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 high
- **작업**: [[번역]] — tag_match · tags = `translation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation, task:translation = ``instruction`, `input`, `output`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:translation = ``instruction`, `input`, `output`` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `269` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `designed specifically to teach bilingual (Korean/English) capabilities, natural code-switching (Konglish), and conversational translation` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 403자 ≈ 269 토큰 (viewer statistics, default/train)
