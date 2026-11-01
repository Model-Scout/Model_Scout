---
type: "dataset"
id: "sander-wood/voices-of-civilizations"
source: "huggingface"
url: "https://huggingface.co/datasets/sander-wood/voices-of-civilizations"
downloads: 55
summary: "Voices of Civilizations는 38개 언어의 전통 음악으로 오디오 LLM의 문화 이해도를 평가하는 다국어 QA 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sander-wood/voices-of-civilizations

> dataset · [Hugging Face](https://huggingface.co/datasets/sander-wood/voices-of-civilizations)

Voices of Civilizations는 38개 언어의 전통 음악으로 오디오 LLM의 문화 이해도를 평가하는 다국어 QA 벤치마크입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `question-answering` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Voices of Civilizations (VoC) is the first multilingual QA benchmark designed to assess audio LLMs’ cultural comprehension using full-length music recordings.` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — metadata · modality, task:question_answering = `text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:question_answering = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `38 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1259` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `VoC exposes models’ biases and weaknesses on under-represented musical traditions and fosters more inclusive audio understanding research.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `Voices of Civilizations (VoC) is the first multilingual QA benchmark designed to assess audio LLMs’ cultural comprehension` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `document_translation` 열 p90 5038자 ≈ 1259 토큰 (viewer statistics, default/train)
