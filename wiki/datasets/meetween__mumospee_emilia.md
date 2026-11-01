---
type: "dataset"
id: "meetween/mumospee_emilia"
source: "huggingface"
url: "https://huggingface.co/datasets/meetween/mumospee_emilia"
downloads: 15
summary: "6개 언어의 101k 시간 이상 음성 데이터를 포함한 다국어 음성-텍스트 변환용 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
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
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# meetween/mumospee_emilia

> dataset · [Hugging Face](https://huggingface.co/datasets/meetween/mumospee_emilia)

6개 언어의 101k 시간 이상 음성 데이터를 포함한 다국어 음성-텍스트 변환용 데이터셋입니다.

## 분류

- **작업**: [[음성 인식]] — ner · readme = `This dataset is ideal for use in large-scale multilingual speech-to-text and text-to-speech tasks` · 신뢰도 medium
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · readme, task:speech_recognition = `segment audio + per-segment fields` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme = `transcript` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `transcript` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[fr]] — metadata · languages = `fr` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `6 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `cc-by-nc-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The Emilia dataset is a comprehensive, multilingual dataset` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `99999999.0` · 신뢰도 high
