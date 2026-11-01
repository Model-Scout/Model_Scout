---
type: "dataset"
id: "amphion/Emilia"
source: "huggingface"
url: "https://huggingface.co/datasets/amphion/Emilia"
downloads: 109
summary: "Emilia는 6개 언어의 다양한 음성 스타일과 전사문을 포함한 대규모 다국어 음성 생성용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[음성 합성]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[음성 (출력 형식)|음성]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[fr]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# amphion/Emilia

> dataset · [Hugging Face](https://huggingface.co/datasets/amphion/Emilia)

Emilia는 6개 언어의 다양한 음성 스타일과 전사문을 포함한 대규모 다국어 음성 생성용 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `The Emilia dataset is the first open-source, multilingual, in-the-wild dataset designed for speech generation.` · 신뢰도 medium
- **작업**: [[음성 합성]] — metadata · task_categories = `text-to-speech` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme = `you can download the raw audio files from the [provided URL list]` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation, task:text_to_speech = `text` · 신뢰도 medium
- **출력 형식**: [[음성 (출력 형식)|음성]] — task_rule · task:text_to_speech = `audio` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `The dataset includes various speaking styles and their corresponding transcriptions.` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Emilia dataset is the first open-source, multilingual, in-the-wild dataset designed for speech generation.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `If you're interested in using the processed data—the Emilia Dataset itself—please visit [this link](https://huggingface.co/datasets/amphion/Emilia-Dataset).` · 신뢰도 low
