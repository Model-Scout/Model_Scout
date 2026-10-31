---
type: "dataset"
id: "Igor97/MISP-M3SD"
source: "huggingface"
url: "https://huggingface.co/datasets/Igor97/MISP-M3SD"
downloads: 111
summary: "MISP-M3SD는 770시간 규모 다중언어·다중시나리오 음성-영상 화자 분리 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[음성 분류]]"
  - "[[정보 추출]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[이미지 (입력 형식)|이미지]]"
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
---
# Igor97/MISP-M3SD

> dataset · [Hugging Face](https://huggingface.co/datasets/Igor97/MISP-M3SD)

MISP-M3SD는 770시간 규모 다중언어·다중시나리오 음성-영상 화자 분리 데이터셋입니다.

## 분류

- **작업**: [[음성 분류]] — metadata · task_categories = `audio-classification` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `cross-modal consistency-guided annotation with selective manual verification` · 신뢰도 low
- **작업**: [[음성 인식]] — ner · readme = `MISP-M3SD is a large-scale multimodal, multi-scenario, and multilingual dataset for robust speaker diarization` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:audio_classification, task:speech_recognition = `770 hours of synchronised audio-visual recordings` · 신뢰도 medium
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `770 hours of synchronised audio-visual recordings` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:information_extraction = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:speech_recognition = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `16 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `constructed from in-the-wild online videos` · 신뢰도 low
