---
type: "dataset"
id: "OpenVoiceOS/tts-test-sentence"
source: "huggingface"
url: "https://huggingface.co/datasets/OpenVoiceOS/tts-test-sentence"
downloads: 25
summary: "다국어 음성 합성 테스트를 위한 무지개 문장 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 합성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[평가용]]"
  - "[[서비스 데이터]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# OpenVoiceOS/tts-test-sentence

> dataset · [Hugging Face](https://huggingface.co/datasets/OpenVoiceOS/tts-test-sentence)

다국어 음성 합성 테스트를 위한 무지개 문장 번역 데이터셋입니다.

## 분류

- **작업**: [[음성 합성]] — tag_match · readme, tags = `tts` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:text_to_speech = `Each row: lang (BCP-47), language (name), script (ISO-15924), text (native translation)` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `Each row: lang (BCP-47), language (name), script (ISO-15924), text (native translation)` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `92 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc0-1.0` · 신뢰도 high
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 용도**: [[서비스 데이터]] — ner · readme = `for quickly sanity-checking multilingual text-to-speech voices` · 신뢰도 low
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
